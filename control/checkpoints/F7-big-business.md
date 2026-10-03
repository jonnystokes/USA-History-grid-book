# CHECKPOINT F7 | big-business | step 7 fixer on the second-audit findings (T-616)

STATUS: DONE (T-616, PASS  big-business / prose)
BRIEF:  control/briefs/FIX7-DISPATCH.md + FIXER.md (whole-chapter mode)

NOW:    T-616 fixer (opus) 2026-10-03: all three parts DONE. Scratch: scratchpad/T-616 (originals copied, apply_verdicts.py, v1.json)
NEXT:   none (director)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 35 / 4 / 0, plus 3 found by fixer | 5095 -> 5221 (wc -w) |
| part2 | 6-7 | done | 29 / 4 / 0, plus 5 found by fixer | 5509 -> 5619 (wc -w) |
| part3 | 8-10 | done | 40 / 2 / 0, plus 4 found by fixer | 8300 -> 8541 (wc -w) |

## NEEDS-RESEARCH
- none new. Still open from earlier tasks: who sued Biddle for nearly $25 million; who at UCIL turned off the Bhopal scrubber (both SEARCHED, NOT FOUND in the bank).

## Log
- part1 eras 1-5: rows 1-39 judged (35 FIXED, 4 REJECTED), F1-F3 found by fixer. EXTRA: shilling/penny, Puritan, Quaker, PA charter 1782 confirmed on opened pages; 1619 Campeche/Rolfe/White Lion purchase confirmed (Encyclopedia Virginia). PATCH 2026-10-03 (T-616) in era 03. No other unconfirmed line is stated in part1 prose. validate 0 errors, punct 0/0.
- part2 eras 6-7: rows 1-33 judged (29 FIXED, 4 REJECTED), F1-F3 found by fixer. EXTRA: 1880 receipts (Treasury report), 51M state acres (49M dropped), Rockefeller's 900 of 2,000 SIC shares, mid-Feb to mid-Mar 1872 (six weeks dropped), tugboats, Frick testimony, Dartmouth 1816 changes all on opened pages. PATCHes T-616 in eras 06 and 07 (incl. Pullman dead copied from work-workers). validate 0 errors, punct 0/0.
- part2 later: F4 label 'Homestead, 1892' (fourth wall), F5 'Neither Wolff nor Britannica names the men who fired' (#45).
- part3 eras 8-10: rows 1-42 judged (40 FIXED, 2 REJECTED), F1-F4 found by fixer. EXTRA: Wilson/Eisenhower, tobacco 'each executive', Powell memo content, Morgan, Berle-Means, FTC s.5 (quote trimmed), TR film, ITT 350, Microsoft 7 judges, Enron, Khan at Yale, Meta ruling, Apple no trial date, Citizens United and unions confirmed on opened pages (PATCH T-616 in era 10 section); Kennedy 'different forms' cut. Ludlow and Bhopal 'died' -> 'killed' (#44). validate 0 errors, punct 0/0.
- final: python tools/project_state.py --check big-business --stage prose -> PASS (18320w by project_state, 10/10 eras, 14 stories verified, 0/0 punct, validator 0 errors).
