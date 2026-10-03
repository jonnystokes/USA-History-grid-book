# CHECKPOINT F7 | science | step 7 fixer on the second-audit findings (T-604)

STATUS: DONE (T-604, PASS  science / prose)
BRIEF:  control/briefs/FIX7-DISPATCH.md + FIXER.md (whole-chapter mode)

NOW:    done
NEXT:   director: commit
HELPER: scratchpad T-604/verdict.py adds the fixer column to a findings file from a JSON of verdicts.

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 21 FIXED (incl. 3 found by fixer) / 2 REJECTED / 0 | 4189 -> 4187 |
| part2 | 6-7 | done | 21 FIXED (incl. 3 found by fixer) / 0 REJECTED / 0 | 4769 -> 4941 |
| part3 | 8-10 | done | 36 FIXED (incl. 6 found by fixer) / 0 REJECTED / 0 | 11228 -> 11306 |

## NEEDS-RESEARCH
- science era 10: a named source for the spread of AI tools in labs in the 2020s (sentence cut, it rested on unnamed "news reports"; a Nature 2023 survey of researchers is a lead, page needs login).

## Log
- 2026-10-03 part1 era 1: rows 1-3 judged (1 FIXED, 2 REJECTED). PATCH T-604 (SUNY rank) added to bank era 1. Also PATCHes for Roanoke Island (era 2) and Tom Tucker's kite doubt (era 5). validate 0 errors, punct 0/0.
- 2026-10-03 part1 eras 2-5: rows 4-20 judged, all FIXED; 3 found-by-fixer rows (era openings, "inferior", "companion"). validate 0 errors, punct 0/0.
- 2026-10-03 part2 era 6: rows 1-5 FIXED, F4 found by fixer. Real error found: the 2022 Morton reburial was January 2024 (PATCH T-604 under era 10; part3 line ~460 repeats the 2022 claim, fix there). PATCH T-604 Morrill land copied from the education bank (era 7). validate 0, punct 0/0.
- 2026-10-03 part2 era 7: rows 6-18 FIXED; F5 (#44 Pawnee 'died') and F6 (#45 record-silent x3) found by fixer. Morrill land and the HCN count of land taken from Native nations added from PATCH. validate 0, punct 0/0. Part2 words 4769 -> 4941.
- 2026-10-03 part3 era 8: rows 1-13 FIXED; F7-F9 found by fixer. PATCH T-604 (Oppenheimer's job; ACHRE consent-form wording) before era 9 heading. validate 0, punct 0/0.
- 2026-10-03 part3 era 9: rows 14-22 FIXED; F10 found by fixer (Cosmos 'press reports'; PATCH T-604 Spokesman-Review). validate 0, punct 0/0.
- 2026-10-03 part3 era 10: rows 23-30 FIXED; F11 (false 2022 reburial date, corrected to January 2024, matches part2) and F12 (unnamed news reports, cut) found by fixer. Feynman record line "in plain words" changed to "simply" (sweep). validate 0, punct 0/0. prose check PASS (19114 w).
