"""Director helper. Usage:
  python tools/director_task.py open  <tid> <slug> <checkpoint> "<title>"
  python tools/director_task.py close <tid> <slug> <checkpoint> <tokens> <tools> <ms> "<one-line result>" [extra files...]
<checkpoint> is the checkpoint's path (control/checkpoints/T-750-readability.md), or a base
name as before: T-315 means control/checkpoints/T-315-<slug>.md.
open: appends the IN-FLIGHT entry, adds NOW-RUNNING under TODO.md's "## NOW" heading, commits.
close: verifies, closes the IN-FLIGHT entry, marks the checkpoint, adds a usage row, commits named paths.
Both read and check every file before writing any, so a close that cannot find its WORKLOG
entry or its checkpoint stops with a message and changes nothing (2026-10-28).
Set STAGE (default research) and MODEL (default opus)."""
import os, re, sys, subprocess, datetime
TODAY = datetime.date.today().isoformat()
STAGE = os.environ.get("STAGE", "research")
MODEL = os.environ.get("MODEL", "opus")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
def run(*a): return subprocess.run(list(a), capture_output=True, text=True).stdout
def read(p):
    with open(p, encoding="utf-8") as f: return f.read()
def write(p, s):
    with open(p, "w", encoding="utf-8") as f: f.write(s)
def stop(msg):
    print(f"director_task {sys.argv[1]}: {msg}\nNothing was written.", file=sys.stderr); sys.exit(2)
def checkpoint_path(arg, slug):
    if arg.endswith(".md") or "/" in arg or "\\" in arg:
        return arg.replace("\\", "/")
    return f"control/checkpoints/{arg}-{slug}.md"
# "## NOW" or "## NOW (2026-10-26, evening): PHASE 2, ...", and the blank line after it.
NOW_HEAD = re.compile(r"^## NOW\b[^\n]*\n\n?", re.M)
if len(sys.argv) < 2 or sys.argv[1] not in ("open", "close"):
    print(__doc__); sys.exit(1)
cmd = sys.argv[1]
for f in ("control/WORKLOG.md", "control/TODO.md", "control/usage-log.tsv"):
    if not os.path.exists(f):
        stop(f"{f} not found under {ROOT}")
if cmd == "open":
    if len(sys.argv) < 6:
        print(__doc__); sys.exit(1)
    tid, slug, base, title = sys.argv[2:6]
    cp = checkpoint_path(base, slug)
    s = read("control/TODO.md")
    s = re.sub(r"^NOW-RUNNING:.*$\n?", "", s, flags=re.M)
    m = NOW_HEAD.search(s)
    if m:
        s = s[:m.end()] + f"NOW-RUNNING: {tid} {slug} ({title})\n" + s[m.end():]
    else:
        print("note: control/TODO.md has no '## NOW' heading, so no NOW-RUNNING line was added")
    if not os.path.exists(cp):
        print(f"note: the checkpoint {cp} does not exist yet; close needs it")
    with open("control/WORKLOG.md", "a", encoding="utf-8") as f:
        f.write(f"\n### {TODAY} | [LOCAL] {tid} | {slug}: {title} | model {MODEL}\nSTATUS: IN-FLIGHT\n"
                f"CHECKPOINT: {cp}\n"
                f"VERIFY: python tools/project_state.py --check {slug} --stage {STAGE}\n")
    write("control/TODO.md", s)
    subprocess.run(["git", "add", "control/WORKLOG.md", "control/TODO.md"])
    subprocess.run(["git", "commit", "-q", "-m", f"{tid} {slug} IN-FLIGHT\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"])
    print("opened", tid)
elif cmd == "close":
    if len(sys.argv) < 9:
        print(__doc__); sys.exit(1)
    tid, slug, base, tok, tools, ms, result = sys.argv[2:9]
    extra = sys.argv[9:]
    # Read and check everything before writing anything.
    wl = read("control/WORKLOG.md")
    pat = re.compile(rf"(### \d{{4}}-\d{{2}}-\d{{2}} \| \[LOCAL\] {re.escape(tid)} \|[^\n]*\n)STATUS: IN-FLIGHT\n((?:CHECKPOINT|VERIFY)[^\n]*\n(?:(?:CHECKPOINT|VERIFY)[^\n]*\n)?)")
    m = pat.search(wl)
    if not m:
        stop(f"control/WORKLOG.md has no open entry for {tid} (a heading '### <date> | [LOCAL] {tid} | ...'"
             " followed by 'STATUS: IN-FLIGHT'). A wave entry, or one already closed, is closed by hand.")
    cp = checkpoint_path(base, slug)
    if not os.path.exists(cp):
        named = re.search(r"^CHECKPOINT: *(\S+)", m.group(2), re.M)
        hint = f" The WORKLOG entry names {named.group(1)}." if named and named.group(1) != cp else ""
        stop(f"checkpoint {cp} not found.{hint} Give the checkpoint's path as the third argument.")
    cps = read(cp)
    todo = read("control/TODO.md")
    chk = run("python", "tools/project_state.py", "--check", slug, "--stage", STAGE).splitlines()
    verdict = chk[0] if chk else "?"
    meas = next((l.strip() for l in chk if l.strip().startswith("measured:")), "")
    mins = round(int(ms) / 60000, 1) if ms.isdigit() else "?"
    body = (f"RESULT: {'DONE' if 'PASS' in verdict else 'LANDED'}. {verdict}. {meas}\n"
            f"        {tok} tokens, {tools} tool uses, {mins} min ({MODEL}). {result}\n")
    wl = wl.replace(m.group(0), m.group(1) + f"STATUS: {'DONE' if 'PASS' in verdict else 'LANDED'}\n" + m.group(2) + body, 1)
    cps, n = re.subn(r"^STATUS: .*$", f"STATUS: {tid} landed (director verified: {verdict})", cps, count=1, flags=re.M)
    if not n:
        print(f"note: {cp} has no 'STATUS:' line to mark")
    todo = re.sub(r"^NOW-RUNNING:.*$\n?", "", todo, flags=re.M)
    # Now write.
    write("control/WORKLOG.md", wl)
    write(cp, cps)
    with open("control/usage-log.tsv", "a", encoding="utf-8") as f:
        f.write(f"{TODAY}\t{tid}\t{STAGE}\tgeneral-purpose/{MODEL}\t[LOCAL] {slug}: {result[:80]}\t?\t?\t?\t{tok}\t{tools}\t{ms}\t?\tcompleted\t{verdict}\n")
    write("control/TODO.md", todo)
    files = [f"outlines/{slug}.md", f"research/research-{slug}.md", f"workspace/{slug}.md", cp,
             "control/WORKLOG.md", "control/usage-log.tsv", "control/TODO.md"] + extra
    subprocess.run(["git", "add"] + [f for f in files if os.path.exists(f)])
    subprocess.run(["git", "commit", "-q", "-m", f"{tid} {slug}: {verdict} [{MODEL}, {tok} tokens, {tools} tools, {mins} min]\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"])
    print(verdict); print(run("git", "status", "--short"))
