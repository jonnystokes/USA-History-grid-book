# CHECKPOINT F7 | war | step 7 fixer on the second-audit findings (T-625)

STATUS: DONE (T-625, PASS  war / prose)
BRIEF:  control/briefs/FIX7-DISPATCH.md + FIXER.md (whole-chapter mode)

NOW:    done
NEXT:   director: commit

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 41 FIXED / 0 REJECTED / 0 NR, +7 found by fixer (all FIXED) | 9606 -> 9877 |
| part2 | 6-7 | done | 38 FIXED / 0 REJECTED / 0 NR, +6 found by fixer (all FIXED) | 6914 -> 7093 |
| part3 | 8-10 | done | 54 FIXED / 0 REJECTED / 0 NR, +3 found by fixer (all FIXED) | 9464 -> 9786 |

## NEEDS-RESEARCH (round 2; prose already true without them)
- war part1 era 2 (EXTRA): was the Tiguex rape at Arenal? Only Wikipedia / Legends of America summaries say so (and name Juan de Villegas). Prose no longer ties the rape to Arenal. Round 2: Flint and Flint, trial testimony. Bank: SEARCHED, NOT FOUND 2026-10-03 (T-625).
- war part1 era 3: Mashantucket 1666 rests on Wikipedia ("created by the Connecticut Colony"); the tribe's history page returned 403. Confirm in round 2.
- war part1 era 5 / part3 era 9: Gnadenhutten 'no charges' and the Calley sentence cuts rest on Wikipedia (+ EBSCO for Calley). Stronger sources welcome.

## Log
- 2026-10-03 part1 era 1: findings 1-6 FIXED. validate 0 errors, punct 0/0.
- 2026-10-03 part1 era 2: findings 7-15 FIXED, 2 found by fixer (#42 'died', #43 prosecutor/upheld). Arenal EXTRA done. validate 0, punct 0/0.
- 2026-10-03 part1 era 3: 16-22 FIXED, found #44 (#45 record-silence x5), #45 'put to death'. PATCHes: Providence (NPS, Narragansett), Mashantucket 1666 (Wikipedia, thin).
- 2026-10-03 part1 era 4: 23-29 FIXED, found #46 (unnamed NCpedia historians). PATCH: Louisbourg 1748 copied from america-world bank.
- 2026-10-03 part1 era 5: 30-41 FIXED, found #47 (Gnadenhutten no charges, Wikipedia PATCH), #48 (prison ships 'died', actor named). PATCH: NEHS on Mann's book. PART 1 DONE.
- 2026-10-03 part2 era 6: 1-13 FIXED, found #39 (#45 x2).
- 2026-10-03 part2 era 7: 14-38 FIXED, found #40-44. PART 2 DONE.
- 2026-10-03 part3 era 8: 1-27 FIXED, found #55, #56. PATCH: Smith/Waller (HistoryNet).
- 2026-10-03 part3 era 9: 28-38 FIXED. PATCHes: Saigon (HISTORY), Calley sentence cuts (Wikipedia, EBSCO).
- 2026-10-03 part3 era 10: 39-54 FIXED, found #57. PATCHes: Costs of War indirect causes, Tillman testimony, Duckworth crew roles. PART 3 DONE.
- Sweeps: no 'In plain words', no slur, 'Colored' explained once (part2), record-silence lines name the silent source (#45), unnamed sources named (#32/#37), 'died' replaced where people were killed (#44).
- Final: python tools/project_state.py --check war --stage prose -> PASS (25329 w, 0 errors, 0/0 punct).
- Harness note: python open(...,'w') gave OSError Errno 22 twice (checkpoint, part3); a retry seconds later or the Write tool worked.
