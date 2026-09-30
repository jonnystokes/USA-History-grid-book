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
