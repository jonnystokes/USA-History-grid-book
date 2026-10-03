"""Step 6 (second audit) bookkeeping.

Usage: python tools/audit2.py                  # progress
       python tools/audit2.py --list           # every part file and its state
       python tools/audit2.py --prompt <tid> <slug> <part>   # print the checker prompt

Findings go to control/audit/<slug>/<partN>-findings-r2.md (the round-1 files stay as they are).
A file counts as FINISHED when the validator output ("0 errors") is pasted at its end.
"""
import os, re, sys
ROOT = r"C:\Users\jon\Projects\History-Book-Project-claude"
os.chdir(ROOT)
PARTS = [("part1-before-1800", "1-5", "part1"), ("part2-1800s", "6-7", "part2"),
         ("part3-1900s-and-today", "8-10", "part3")]
reg = open("control/chapter-registry.md", encoding="utf-8").read()
SLUGS = [s for s in re.findall(r"^\| \d+ \| `([a-z-]+)` \|", reg, flags=re.M) if os.path.isdir(f"manuscript/{s}")]

def state(slug, short):
    f = f"control/audit/{slug}/{short}-findings-r2.md"
    if not os.path.exists(f):
        return "TODO"
    return "FINISHED" if "0 errors" in open(f, encoding="utf-8").read()[-4000:] else "PARTIAL"

PROMPT = """You are a CHECKER (step 6, the second audit) on the History Book Project at C:\\Users\\jon\\Projects\\History-Book-Project-claude (Windows; use forward-slash paths in the Bash tool, or PowerShell).

TASK: {tid} | CHAPTER: {slug} | PART FILE: manuscript/{slug}/{part}.md | ERAS: {eras}
FINDINGS FILE: control/audit/{slug}/{short}-findings-r2.md
MODEL: sonnet.

This is the second, independent read. The part file was checked once, every finding was judged and fixed, and round-2 research has filled gaps since. Report only defects present in the text as it is now. Do not open the round-1 findings file ({short}-findings-sonnet.md): your read must be independent.

Read your brief, control/briefs/CHECKER.md, in full and follow it exactly: the files to read first, in order and in full (including control/writing-style-guide.md section 0, Jon's seven guidelines, and control/DECISIONS.md #28-38); starting the findings file before your first pass; the six passes over each era, every sentence in every pass; writing each era's findings as you finish it; and the finish and report. Get your bank slice with `python tools/slice_bank.py {slug} --eras {eras} --bank-only -o <scratch file>` (keep scratch files in your own subfolder of the scratchpad, named {tid}). Search the whole bank file before you report "Not in bank".

If the findings file already exists (an earlier checker was interrupted), do not start over: read it, keep every row, and continue from the first era that has no findings written.

You are a reader, not an editor. Change no file except your findings file. No git. Install nothing. Save downloads only in your own scratch subfolder, and never open a PDF link in the browser pane. Write the findings file with the Write or Edit tool, never a Bash heredoc. Check file sizes before reading; never read viewer/*.html whole.

Report in under 120 words: total findings by severity, the three rules broken most often, and anything you were unsure how to judge."""

if "--prompt" in sys.argv:
    i = sys.argv.index("--prompt")
    tid, slug, part = sys.argv[i + 1:i + 4]
    p = next(x for x in PARTS if x[0] == part or x[2] == part)
    os.makedirs(f"control/audit/{slug}", exist_ok=True)
    print(PROMPT.format(tid=tid, slug=slug, part=p[0], eras=p[1], short=p[2]))
    sys.exit(0)
rows = [(s, p, e, sh, state(s, sh)) for s in SLUGS for p, e, sh in PARTS]
if "--list" in sys.argv:
    for r in rows:
        print(f"{r[4]:9} {r[0]:24} {r[1]}")
    sys.exit(0)
n = sum(1 for r in rows if r[4] == "FINISHED")
print(f"step 6 audit: {n}/{len(rows)} FINISHED, {sum(1 for r in rows if r[4]=='PARTIAL')} PARTIAL")
