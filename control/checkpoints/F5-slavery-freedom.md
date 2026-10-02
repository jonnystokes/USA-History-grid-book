# CHECKPOINT F5 | slavery-freedom | step 5 fixer, whole chapter

STATUS: T-466 landed (director verified: PASS  slavery-freedom / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/slavery-freedom/part1|part2|part3 + control/audit/slavery-freedom/part1|2|3-findings-sonnet.md
        + research/research-slavery-freedom.md (PATCH entries only)

NOW:    all three parts done; prose check PASS.
NEXT:   none (director: commit; see NEEDS-RESEARCH)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 87 / 10 / 0 (95 rows + 2 found by fixer, both FIXED) | 6238 -> 6825 (wc -w; 6237 before by wc) |
| part2 | 6-7 | DONE | 105 / 6 / 1 (106 rows + 6 found by fixer, all FIXED) | 10227 -> 11077 (wc -w; 10226 before by wc) |
| part3 | 8-10 | DONE | 68 / 0 / 2 (69 rows + 1 found by fixer, FIXED) | 3572 -> 4214 (wc -w; 3571 before by wc) |

## NEEDS-RESEARCH
- part3 row 55: who in Evanston's government carried out the 1919-1969 housing discrimination.
- part3 row 62: confirm on a page that Interior officials told The Hill they had not directed the Fort Pulaski removal; then state that accounts differ.
- part2 row 19: a sourced runaway-ad quote describing whip scars ("much marked by the whip" not confirmed; sentence cut).
- part2 row 31: who passed Charleston's ban on Black churches after 1822 (EJI gives only the passive).
- part3 row 9: how Mississippi's 1890 understanding clause worked (SEARCHED, NOT FOUND).
- part2 row 54: who hanged Celia (no actor in the bank).
- part1 row 84 / DECISIONS #32: a historian's published statement calling Jefferson's conduct rape (sources opened give 'sexual exploitation', 'forced embrace'); prose follows the ruling.

## Log
- part1 era 1 DONE: rows 1-5 judged (4 FIXED, 1 REJECTED). validate 0 errors, punct 0/0. Scratch: scratchpad/T-466 (v1.json = verdicts, apply_verdicts.py regenerates findings from base-part1.md).
- part1 era 2 DONE: rows 6-16 (9 FIXED, 2 REJECTED... see table). PATCHes: Estevanico captivity/killers (from exploration), New Laws + Spanish rights (NPS), Seloy (Florida Museum). Checks clean.
- part1 era 3 DONE: rows 17-44 + F1. PATCH: nose-slitting (Barbados code). Middle Passage now says "raped" (#31). Checks clean.
- part1 era 4 DONE: rows 45-67 + F2. PATCH: rice exports (from food-farming). Checks clean.
- part1 era 5 DONE: rows 68-95. 1790 census SETTLED = 697,681 (Census Bureau WP 56, Table 1). Hemings per #32 (note for director: sources show 'sexual exploitation'/'forced embrace', no historians' consensus on the word rape found; prose follows the ruling). PATCHes: census, three-fifths seats, Hemings sources + Sept 2026 Smithsonian DNA study, Boston Massacre. PART1 DONE.
- part2 era 6 DONE: rows 1-48 + F1-F3 (48 FIXED, 2 REJECTED, 1 NR incl. extras). 1811 count SETTLED (40-45 battle + 44 after tribunals + killings without trial = about 95). PATCHes: 1811, Gabriel actors, Northup family (Mintus enslaved by the Northups), Peter's sellers, Tubman Philadelphia, Choctaw removal. Checks clean.
- part2 era 7 DONE: rows 49-106 + F4-F6. PATCH 2026-10-02 era 7 (Burns's arrest, CDC smallpox, DC act, Freedman's bank charter, Hayes and the 1877 commission, Weeping Time) all copied from sibling banks or opened. 13th/Juneteenth reordered by date. PART2 DONE.
- part3 era 8 DONE: rows 1-27 + F1 (Louisiana voter counts corrected from pages). PATCHes: Taylor/Pollock, Ed Johnson (from crime-justice), Louisiana counts and grandfather clause. Checks clean.
- part3 era 9 DONE: rows 28-39 all FIXED. Checks clean.
- part3 era 10 DONE: rows 40-69 (68 FIXED, 2 NR). Label of the parks span changed (it personified the parks). PART3 DONE.
- FINAL: validate 0 errors and punct 0/0 on all three parts. prose check: PASS slavery-freedom / prose (ms_eras 10/10, 24 stories verified, 0 em dashes, 0 semicolons, manuscript=20755w, validator 0 errors).
