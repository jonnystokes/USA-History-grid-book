# CHECKPOINT F5 | art | step 5 fixer, whole chapter (test 2 of 3: largest one-agent chapter)

STATUS: T-443 landed (director verified: PASS  art / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/art/part1|part2|part3 + control/audit/art/part1|2|3-findings-sonnet.md
        + research/research-art.md (PATCH entries only)

NOW:    T-443 fixer started 2026-10-01: style files, brief, DECISIONS #28-38, AUDIT-QUEUE read. Working part1 era 1.
NEXT:   none. All three parts done; prose check PASS.
SCRATCH: scratchpad/T-443/ (bank slices bank-eN.md)
WORDS:  counted with `wc -w` on the part file

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 102 / 5 / 0, plus 5 found by fixer (all FIXED) | 6915 -> 7799 |
| part2 | 6-7 | DONE | 73 / 1 / 0, plus 4 found by fixer (all FIXED) | 7990 -> 8864 |
| part3 | 8-10 | DONE | 141 / 12 / 0, plus 7 found by fixer (all FIXED) | 13166 -> 13922 |

## NEEDS-RESEARCH
- None open. Every gap was searched and PATCHed (T-443, eras 01-10) or the unsourced words were cut.

## Log
- part1 era 1 (before-1500) DONE: rows 1-28 judged (26 FIXED, 2 REJECTED), 2 found by fixer (108-109). PATCH T-443 era 01 (Craig = Great Temple Mound, Birdman/falcon dancer, Cahokia in Illinois, brands). validator 0 errors, punct 0/0.
- part1 era 2 (1500s) DONE: rows 29-39 (10 FIXED, 1 REJECTED). PATCH T-443 era 02 (White leaves for supplies, Dasamonquepeuc attack). Checks clean.
- part1 era 3 (1600s) DONE: rows 40-62 (22 FIXED, 1 REJECTED), 2 found by fixer. PATCH T-443 era 03 (Acoma copied from native-nations bank per #36; two book titles). Checks clean.
- part1 era 4 (1700-1750) DONE: rows 63-81 (19 FIXED), 1 found by fixer. Span label "Portraits paid for with money from slavery" -> "Two portraits that show slavery" (label made an unsourced claim). PATCH T-443 era 04 (Walking Purchase walk, Huguenots, Royall page). Checks clean.
- part1 era 5 (1750-1800) DONE: rows 82-107 (25 FIXED, 1 REJECTED). PATCH T-443 era 05 (Athenaeum portrait unfinished, Warren plays). Checks clean. PART 1 DONE.
- part2 era 6 (1800-1850) DONE: rows 1-42 (42 FIXED, row 32 and 33 partly), 1 found by fixer (row 75). PATCH T-443 era 06 (Dave/Miles, Douglass homes, Daguerre, Cherokee soldiers). Checks clean.
- part2 era 7 (1850-1900) DONE: rows 43-74 (31 FIXED, 1 REJECTED), 3 found by fixer (76-78, incl. Pratt's Fort Marion acts added per #36). PATCH T-443 era 07. Checks clean. PART 2 DONE.
- part3 era 8 (1900-1950) DONE: rows 1-62 (60 FIXED, 2 REJECTED), 4 found by fixer (154-157; Truman's slur removed per #35). PATCH T-443 era 08. Checks clean.
- part3 era 9 (1950-2000) DONE: rows 63-112 (46 FIXED, 4 REJECTED), 1 found by fixer (158). PATCH T-443 era 09. Checks clean.
- part3 era 10 (2000-today) DONE: rows 113-153 (35 FIXED, 6 REJECTED), row 59 changed to REJECTED (Wilder renaming told once, in era 10), 2 found by fixer (incl. 'Confederate' glossed in part2). #30 applied: kehinde-wiley block and its marker lines removed; Rumors of War and Freedom Monument Sculpture Park moved to "Answering the Confederate statues"; no accusation mentioned. PATCH T-443 era 10. PART 3 DONE.
- Final: `python tools/project_state.py --check art --stage prose` PASS (33 stories, 28958 prose words, 0/0 punct, 0 validator errors).
- For the director: outlines/art.md and outlines/BOOK-OUTLINE.md still carry the kehinde-wiley story (not this fixer's files).
