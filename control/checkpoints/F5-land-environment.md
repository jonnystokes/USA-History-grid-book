# CHECKPOINT F5 | land-environment | step 5 fixer, whole chapter

STATUS: T-453 landed (director verified: PASS  land-environment / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/land-environment/part1|part2|part3 + control/audit/land-environment/part1|2|3-findings-sonnet.md
        + research/research-land-environment.md (PATCH entries only)

NOW:    done
NEXT:   none (director: commit)
SCRATCH: scratchpad/T-453 (merge.py adds the fixer column from v<era>.txt verdict files)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 41 / 1 / 0, plus 4 found by fixer | 3858 -> 4161 (wc) |
| part2 | 6-7 | DONE | 48 / 5 / 0, plus 6 found by fixer (1 added during part3) | 5084 -> 5516 (wc) |
| part3 | 8-10 | DONE | 57 / 5 / 0, plus 8 found by fixer | 9078 -> 9763 (wc) |

## NEEDS-RESEARCH

## Log
- part1 era 1: findings 1-6 FIXED, 1 found by fixer (F101). validate 0 errors, punct 0/0.
- part1 era 2: findings 7-13 FIXED, 1 found by fixer (F102). validate 0 errors, punct 0/0.
- part1 era 3: findings 15-20 FIXED. validate 0 errors, punct 0/0.
- part1 era 4: findings 22-31 FIXED. validate 0 errors, punct 0/0.
- part1 era 5: findings 32-44: 12 FIXED, 1 REJECTED (#37), 2 found by fixer. PATCH 2026-10-01 (T-453) first survey 1785-86 added. validate 0 errors, punct 0/0. PART1 DONE.
- part2 era 6: findings 1-13: 11 FIXED, 2 REJECTED (#3, #6). PATCH 2026-10-01 (T-453) Thoreau/Savage post/Sierra Club added. validate 0 errors, punct 0/0.
- part2 era 7: findings 14-53: 37 FIXED, 3 REJECTED (#25, #34, #38), 5 found by fixer. validate 0 errors, punct 0/0. PART2 DONE.
- part3 era 8: findings 1-32: 29 FIXED, 3 REJECTED (#16, #18, #22), 2 found by fixer. PATCH 2026-10-01 (T-453) May 1903 trip + Ballinger dispute. validate 0 errors, punct 0/0.
- part3 era 9: findings 33-51: 18 FIXED, 1 REJECTED (#49), 3 found by fixer. PATCH 2026-10-01 (T-453) NEPA. validate 0 errors, punct 0/0.
- part3 era 10: findings 52-62: 10 FIXED, 1 REJECTED (#62), 2 found by fixer (+1 era-9 row, +1 part2 row found while fixing). validate 0 errors, punct 0/0. PART3 DONE.
- Word counts are wc -w (the before figures match wc). project_state prose_words after: 3819 / 5225 / 9242 = 18286.
- PATCHes added (all "PATCH 2026-10-01 (T-453)"): first survey 1785-86 (era 5); Thoreau "Walking", the Dec 1850 raid on Savage's post, Sierra Club aims (era 7); May 1903 trip and Ballinger dispute (era 8); NEPA (era 9).
- NEEDS-RESEARCH: none.
- prose check: PASS land-environment / prose (validator 0 errors, emdash 0, semicolon 0, 15/15 stories verified).
