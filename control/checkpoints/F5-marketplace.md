# CHECKPOINT F5 | marketplace | step 5 fixer, whole chapter

STATUS: T-452 landed (director verified: PASS  marketplace / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/marketplace/part1|part2|part3 + control/audit/marketplace/part1|2|3-findings-sonnet.md
        + research/research-marketplace.md (PATCH entries only)

NOW:    T-452 fixer, all three parts done
NEXT:   none (director: commit, close the IN-FLIGHT entry)

Fixer scratch: scratchpad T-452/ (apply_verdicts.py adds the fixer column from v<part>.txt; the
untouched findings table sits beside the findings file as *.orig while a part is open, then moves
to scratch). Word counts are `wc -w` of the whole part file.

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH (+ found by fixer) | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 85 / 3 / 0 (+5) | 4428 -> 4741 |
| part2 | 6-7 | done | 39 / 8 / 0 (+1) | 3736 -> 3967 |
| part3 | 8-10 | done | 52 / 2 / 0 (+10) | 6514 -> 7110 |

## NEEDS-RESEARCH
- part1 era 5, country store: what a 1700s country store sold, from a named account book (e.g. the Robert Townsend books, East Hampton Library). The unsourced list "salt, iron, cloth, sugar, tea, tools and rum" was cut.

## Log
- part3 era 10: rows 37-54 judged (16 FIXED, 2 REJECTED incl. row 39 under DECISIONS #33), 4 found by fixer (Bezos profile given its labor record per #33). PATCH 2026-10-01 (T-452) CFPB 14-day term. Checks clean. Part3 done.
- Final: `python tools/project_state.py --check marketplace --stage prose` = PASS (10/10 eras written, 17 stories verified, 0 em dashes, 0 semicolons, validator 0 errors, 14692 prose words).
- Note for the director: the AUDIT-QUEUE housekeeping item from T-310 (Coresight "(unconfirmed)" tag) is answered by the T-310 PATCH already in the bank; the prose uses the confirmed figures.
- part3 era 9: rows 21-36 judged (16 FIXED), 2 found by fixer. PATCH 2026-10-01 (T-452) Anschluss violence against Vienna's Jews (USHMM). Checks clean.
- part3 era 8: rows 1-20 judged (19 FIXED, 1 REJECTED), 4 found by fixer. PATCH 2026-10-01 (T-452) Greensboro (A&T, Geneva Tisdale), 1941 FCC licenses, Jim Crow copied from slavery-freedom and crime-justice. Checks clean.
- part2 era 7: rows 20-47 judged (23 FIXED, 5 REJECTED). PATCHes 2026-10-01 (T-452) Macy/A&P/Woolworth (A&P founding disputed, stated), USPS rural mail, Thomson's Tribune title. Checks clean. Part2 done.
- part2 era 6: rows 1-19 judged (16 FIXED, 3 REJECTED: Barnum facts now banked), 1 found by fixer. PATCH 2026-10-01 (T-452) Barnum name, first show, Boston newspaper letter. Checks clean.
- part1 era 5: rows 70-88 judged (19 FIXED), 2 found by fixer. PATCH 2026-10-01 (T-452) Seider funeral correction (editors: largest in Boston, not America). Checks clean. Part1 done.
- part1 era 4: rows 49-69 judged (20 FIXED, 1 REJECTED), 2 found by fixer. PATCH 2026-10-01 (T-452) shop credit and debt (American Yawp). Checks clean.
- part1 era 3: rows 24-48 judged (24 FIXED, 1 REJECTED). PATCH 2026-10-01 (T-452) Dunbar prisoners handed to Becx and Foote (SPOWS). Checks clean.
- part1 era 2: rows 14-23 judged (10 FIXED). Checks clean.
- part1 era 1: rows 1-13 judged (12 FIXED, 1 REJECTED), 1 found by fixer. PATCH 2026-10-01 (T-452) Cahokia place and population, horses early 1700s. validate 0 errors, punct 0/0.
