"""Step 3 audit status: which part files have a finished checker findings file.

Usage: python tools/audit_status.py            # summary + the next file to check
       python tools/audit_status.py --list     # every part file and its state
       python tools/audit_status.py --mk <slug> # make the chapter's audit checkpoint A3-<slug>.md

A findings file counts as FINISHED when it has the validator output pasted at the bottom
(the checker's last step, "0 errors"). Anything else that exists is PARTIAL (an interrupted checker:
re-dispatch with the same prompt, it continues from the last era written).
Order: chapters in chapter-registry order, part1, part2, part3.
"""
import os, re, sys
ROOT = r"C:\Users\jon\Projects\History-Book-Project-claude"
os.chdir(ROOT)
PARTS = [("part1-before-1800", "1-5"), ("part2-1800s", "6-7"), ("part3-1900s-and-today", "8-10")]

def order():
    reg = open("control/chapter-registry.md", encoding="utf-8").read()
    slugs = re.findall(r"^\| \d+ \| `([a-z-]+)` \|", reg, flags=re.M)
    return [s for s in slugs if os.path.isdir(f"manuscript/{s}")]

def state(slug, part):
    short = part.split("-")[0]
    f = f"control/audit/{slug}/{short}-findings-sonnet.md"
    if not os.path.exists(f):
        return "TODO", f
    t = open(f, encoding="utf-8").read()
    return ("FINISHED" if re.search(r"\b0 errors\b", t) else "PARTIAL"), f

rows = [(s, p, e, *state(s, p)) for s in order() for p, e in PARTS]
PROMPT = """You are a CHECKER on the History Book Project at C:\\Users\\jon\\Projects\\History-Book-Project-claude (Windows; use forward-slash paths in the Bash tool, or PowerShell).

TASK: {tid} | CHAPTER: {slug} | PART FILE: manuscript/{slug}/{part}.md | ERAS: {eras}
FINDINGS FILE: control/audit/{slug}/{short}-findings-sonnet.md
MODEL: sonnet.

Read your brief, control/briefs/CHECKER.md, in full and follow it exactly: the files to read first, in order and in full; starting the findings file before your first pass; the six passes over each era, every sentence in every pass; writing each era's findings as you finish it; and the finish and report. Get your bank slice with `python tools/slice_bank.py {slug} --eras {eras} --bank-only -o <scratch file>` (keep scratch files in your own subfolder of the scratchpad, named {tid}).

If the findings file already exists (an earlier checker was interrupted), do not start over: read it, keep every row, and continue from the first era that has no findings written.

You are a reader, not an editor. Change no file except your findings file. No git. Install nothing. Write the findings file with the Write or Edit tool, never a Bash heredoc. Check file sizes before reading; never read viewer/*.html whole (use the VIEWER-CONTRACT.md sections the brief names instead).

Report in under 150 words as the brief says."""
if "--next" in sys.argv:
    # --next T-3nn : make the chapter checkpoint, open the ledger entry, print the prompt
    import subprocess
    tid = sys.argv[sys.argv.index("--next") + 1]
    nxt = next((r for r in rows if r[3] != "FINISHED"), None)
    if not nxt:
        print("ALL FINISHED"); sys.exit()
    slug, part, eras = nxt[0], nxt[1], nxt[2]
    cp = f"control/checkpoints/A3-{slug}.md"
    if not os.path.exists(cp):
        os.makedirs(f"control/audit/{slug}", exist_ok=True)
        open(cp, "w", encoding="utf-8").write(
            f"# CHECKPOINT A3 | {slug} | step 3 audit (sonnet checker, read-only)\n\nSTATUS: IN-FLIGHT\n"
            f"BRIEF:  control/briefs/CHECKER.md\nFILES:  control/audit/{slug}/part1|part2|part3-findings-sonnet.md\n\n## Log\n")
        subprocess.run(["git", "add", cp]); subprocess.run(["git", "commit", "-q", "-m", f"A3 {slug} checkpoint\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"])
    env = dict(os.environ, STAGE="prose", MODEL="sonnet")
    subprocess.run(["python", "tools/director_task.py", "open", tid, slug, "A3", f"CHECKER sonnet, {part.split('-')[0]}"], env=env)
    print(f"SLUG={slug}\n---PROMPT---")
    print(PROMPT.format(tid=tid, slug=slug, part=part, eras=eras, short=part.split("-")[0]))
    sys.exit()
if "--mk" in sys.argv:
    slug = sys.argv[sys.argv.index("--mk") + 1]
    cp = f"control/checkpoints/A3-{slug}.md"
    if not os.path.exists(cp):
        os.makedirs(f"control/audit/{slug}", exist_ok=True)
        open(cp, "w", encoding="utf-8").write(
            f"# CHECKPOINT A3 | {slug} | step 3 audit (sonnet checker, read-only)\n\nSTATUS: IN-FLIGHT\n"
            f"BRIEF:  control/briefs/CHECKER.md\nFILES:  control/audit/{slug}/part1|part2|part3-findings-sonnet.md\n\n## Log\n")
    print(cp); sys.exit()
if "--list" in sys.argv:
    for s, p, e, st, f in rows:
        print(f"{st:9} {s:24} {p:24} eras {e}")
done = sum(1 for r in rows if r[3] == "FINISHED")
print(f"step 3 audit: {done}/{len(rows)} part files FINISHED, "
      f"{sum(1 for r in rows if r[3]=='PARTIAL')} PARTIAL, {sum(1 for r in rows if r[3]=='TODO')} TODO")
nxt = next((r for r in rows if r[3] != "FINISHED"), None)
if nxt:
    print(f"next: {nxt[0]} {nxt[1]} (eras {nxt[2]}) [{nxt[3]}]")
