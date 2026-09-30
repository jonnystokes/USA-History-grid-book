"""Make writer checkpoints for step 2. Usage: python mk_writers.py T-301:landmarks T-302:energy ..."""
import os, sys, subprocess, re
ROOT = r"C:\Users\jon\Projects\History-Book-Project-claude"
os.chdir(ROOT)
for arg in sys.argv[1:]:
    tid, slug = arg.split(":")[:2]
    single = arg.endswith(":single")
    path = f"control/checkpoints/{tid}-{slug}.md"
    if os.path.exists(path):
        print("exists, skipped:", path); continue
    chk = subprocess.run(["python", "tools/project_state.py", "--check", slug, "--stage", "research"],
                         capture_output=True, text=True, encoding="utf-8").stdout.splitlines()
    text = f"""# CHECKPOINT {tid} | {slug} | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check {slug} --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/{slug}/part1-before-1800.md (eras 1-5) · manuscript/{slug}/part2-1800s.md (eras 6-7)
        · manuscript/{slug}/part3-1900s-and-today.md (eras 8-10) · research/research-{slug}.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    (writer sets this)
NEXT:   {tid}a: Unit 1.

## Research state before writing (2026-09-29)

{chk[0] if chk else '?'}
{chk[2].strip() if len(chk) > 2 else ''}

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | {tid}a | todo | |
| 2 | era 02 1500s -> part1 | {tid}a | todo | |
| 3 | era 03 1600s -> part1 | {tid}a | todo | |
| 4 | era 04 1700-1750 -> part1 | {tid}a | todo | |
| 5 | era 05 1750-1800 -> part1 | {tid}a | todo | |
| 6 | era 06 1800-1850 -> part2 | {tid}a | todo | |
| 7 | era 07 1850-1900 -> part2 | {tid}a | todo | |
| 8 | era 08 1900-1950 -> part3 | {tid}b | todo | |
| 9 | era 09 1950-2000 -> part3 | {tid}b | todo | |
| 10 | era 10 2000-today -> part3 | {tid}b | todo | |
| 11 | final: self-review, --punct, validator, prose check | {tid}b | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

## TO PARK (for the director, burst runs only)

## Log
"""
    if single:
        text = text.replace("writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)", "ONE writer, all 10 eras (part1, part2, part3)")
        text = text.replace(f"| {tid}a |", f"| {tid} |").replace(f"| {tid}b |", f"| {tid} |").replace(f"NEXT:   {tid}a: Unit 1.", f"NEXT:   {tid}: Unit 1.")
    open(path, "w", encoding="utf-8").write(text)
    print(tid, path)
