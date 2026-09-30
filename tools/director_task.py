"""Director helper. Usage:
  python task.py close <tid> <slug> <cpbase> <tokens> <tools> <ms> "<one-line result>" [extra files...]
  python task.py open  <tid> <slug> <cpbase> "<title>"
close: verifies, closes the IN-FLIGHT entry, marks the checkpoint, adds a usage row, commits named paths.
open: appends the IN-FLIGHT entry and commits it."""
import os, re, sys, subprocess, datetime
TODAY = datetime.date.today().isoformat()
STAGE = os.environ.get("STAGE", "research")
MODEL = os.environ.get("MODEL", "opus")
ROOT = r"C:\Users\jon\Projects\History-Book-Project-claude"
os.chdir(ROOT)
def run(*a): return subprocess.run(list(a), capture_output=True, text=True).stdout
if len(sys.argv) < 2 or sys.argv[1] not in ("open", "close"):
    print(__doc__); sys.exit(1)
cmd = sys.argv[1]
if cmd == "open":
    tid, slug, base, title = sys.argv[2:6]
    with open("control/WORKLOG.md", "a", encoding="utf-8") as f:
        f.write(f"\n### {TODAY} | [LOCAL] {tid} | {slug}: {title} | model {MODEL}\nSTATUS: IN-FLIGHT\n"
                f"CHECKPOINT: control/checkpoints/{base}-{slug}.md\n"
                f"VERIFY: python tools/project_state.py --check {slug} --stage {os.environ.get('STAGE', 'research')}\n")
    s = open("control/TODO.md", encoding="utf-8").read()
    s = re.sub(r"^NOW-RUNNING:.*$\n?", "", s, flags=re.M)
    s = s.replace("## NOW\n\n", f"## NOW\n\nNOW-RUNNING: {tid} {slug} ({title})\n", 1)
    open("control/TODO.md", "w", encoding="utf-8").write(s)
    subprocess.run(["git", "add", "control/WORKLOG.md", "control/TODO.md"])
    subprocess.run(["git", "commit", "-q", "-m", f"{tid} {slug} IN-FLIGHT\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"])
    print("opened", tid)
elif cmd == "close":
    tid, slug, base, tok, tools, ms, result = sys.argv[2:9]
    extra = sys.argv[9:]
    chk = run("python", "tools/project_state.py", "--check", slug, "--stage", os.environ.get("STAGE", "research")).splitlines()
    verdict = chk[0] if chk else "?"
    meas = next((l.strip() for l in chk if l.strip().startswith("measured:")), "")
    wl = open("control/WORKLOG.md", encoding="utf-8").read()
    pat = re.compile(rf"(### \d{{4}}-\d{{2}}-\d{{2}} \| \[LOCAL\] {re.escape(tid)} \|[^\n]*\n)STATUS: IN-FLIGHT\n((?:CHECKPOINT|VERIFY)[^\n]*\n(?:(?:CHECKPOINT|VERIFY)[^\n]*\n)?)")
    m = pat.search(wl)
    mins = round(int(ms) / 60000, 1) if ms.isdigit() else "?"
    body = (f"RESULT: {'DONE' if 'PASS' in verdict else 'LANDED'}. {verdict}. {meas}\n"
            f"        {tok} tokens, {tools} tool uses, {mins} min ({MODEL}). {result}\n")
    wl = wl.replace(m.group(0), m.group(1) + f"STATUS: {'DONE' if 'PASS' in verdict else 'LANDED'}\n" + m.group(2) + body, 1)
    open("control/WORKLOG.md", "w", encoding="utf-8").write(wl)
    cp = f"control/checkpoints/{base}-{slug}.md"
    s = open(cp, encoding="utf-8").read()
    s = re.sub(r"^STATUS: .*$", f"STATUS: {tid} landed (director verified: {verdict})", s, count=1, flags=re.M)
    open(cp, "w", encoding="utf-8").write(s)
    with open("control/usage-log.tsv", "a", encoding="utf-8") as f:
        f.write(f"{TODAY}\t{tid}\t{STAGE}\tgeneral-purpose/{MODEL}\t[LOCAL] {slug}: {result[:80]}\t?\t?\t?\t{tok}\t{tools}\t{ms}\t?\tcompleted\t{verdict}\n")
    s = open("control/TODO.md", encoding="utf-8").read()
    s = re.sub(r"^NOW-RUNNING:.*$\n?", "", s, flags=re.M)
    open("control/TODO.md", "w", encoding="utf-8").write(s)
    files = [f"outlines/{slug}.md", f"research/research-{slug}.md", f"workspace/{slug}.md", cp,
             "control/WORKLOG.md", "control/usage-log.tsv", "control/TODO.md"] + extra
    subprocess.run(["git", "add"] + [f for f in files if os.path.exists(f)])
    subprocess.run(["git", "commit", "-q", "-m", f"{tid} {slug}: {verdict} [{MODEL}, {tok} tokens, {tools} tools, {mins} min]\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"])
    print(verdict); print(run("git", "status", "--short"))
