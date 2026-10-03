"""Close a step 7 fixer: python tools/close7.py <tid> <slug> <tokens> <tools> <ms> ["note"]
Runs the prose check, closes the WORKLOG entry, marks the F7 checkpoint, logs usage, commits that chapter's files."""
import os, re, subprocess, sys
os.chdir(r"C:\Users\jon\Projects\History-Book-Project-claude")
tid, slug, tok, tools, ms = sys.argv[1:6]
note = sys.argv[6] if len(sys.argv) > 6 else ""
chk = subprocess.run(["python", "tools/project_state.py", "--check", slug, "--stage", "prose"], capture_output=True, text=True).stdout.splitlines()
verdict = chk[0].strip() if chk else "?"
mins = round(int(ms) / 60000, 1)
p = "control/WORKLOG.md"; s = open(p, encoding="utf-8").read()
s = re.sub(rf"(\[LOCAL\] {re.escape(tid)} [^\n]*\n)STATUS: IN-FLIGHT",
           lambda m: m.group(1) + f"STATUS: DONE\nRESULT: {verdict}. {tok} tokens, {tools} tools, {mins} min (opus). {note}", s, count=1)
open(p, "w", encoding="utf-8").write(s)
cp = f"control/checkpoints/F7-{slug}.md"
c = open(cp, encoding="utf-8").read()
c = re.sub(r"^STATUS: .*$", f"STATUS: DONE ({tid}, {verdict})", c, count=1, flags=re.M)
open(cp, "w", encoding="utf-8").write(c)
with open("control/usage-log.tsv", "a", encoding="utf-8") as f:
    f.write(f"2026-10-03\t{tid}\tprose\tgeneral-purpose/opus\t[LOCAL] {slug} step 7 fixer\t?\t?\t?\t{tok}\t{tools}\t{ms}\t?\tcompleted\t{verdict}\n")
files = [f"manuscript/{slug}", f"research/research-{slug}.md", f"control/audit/{slug}", cp, p, "control/usage-log.tsv"]
subprocess.run(["git", "add"] + files, capture_output=True)
subprocess.run(["git", "commit", "-qm", f"{tid} step 7 fixer {slug}: {verdict} [opus, {tok} tokens]\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"], capture_output=True)
print(verdict)
