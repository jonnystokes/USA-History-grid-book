# CHECKPOINT F5 | landmarks | step 5 fixer, whole chapter

STATUS: T-447 landed (director verified: PASS  landmarks / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/landmarks/part1|part2|part3 + control/audit/landmarks/part1|2|3-findings-sonnet.md
        + research/research-landmarks.md (PATCH entries only)

NOW:    T-447 fixer (opus) finished all three parts
NEXT:   none (director: commit)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 63 / 8 / 1, plus 8 found by fixer (F1-F8) | 5316 -> 5732 (wc -w) |
| part2 | 6-7 | DONE | 36 / 5 / 1, plus 1 found by fixer (F1) | 2664 -> 2935 (wc -w) |
| part3 | 8-10 | DONE | 75 / 4 / 0, plus 5 found by fixer (F1-F5) | 5680 -> 6299 (wc -w) |

## NEEDS-RESEARCH
- part1 era 4 (row 57): how Native people came to live at Mission San Antonio de Valero (the Alamo), and whether they could leave. TSHA Handbook does not say. Prose definition "where Native people lived and were taught the Catholic religion" may be soft.
- part2 era 7 (row 40): what became of the 32 burials found inside Big Mound, St. Louis, when it was dug away in 1868-69, and whether any archaeologist recorded the removal.

## Log
- 2026-10-01 part1 era 1 done. PATCH 2026-10-01 (T-447): Chaco descendants, Poverty Point listing body, WVXU. Validator 0 errors, punct 0/0. Findings table has a `fixer` column; found-by-fixer rows are numbered F1, F2...
- part1 era 2 done (validator 0, punct 0/0).
- part1 era 3 done (validator 0, punct 0/0). PATCH 2026-10-01 (T-447): Governor Diego de Quiroga y Losada.
- part1 era 4 done (validator 0, punct 0/0). PATCHes 2026-10-01 (T-447): Worthylake household and pay, Franklin's ballad, Old North steeple; Alamo founder (TSHA).
- part1 era 5 done (validator 0, punct 0/0). PART1 DONE.
- part2 era 6 done: 15 / 4 / 0 (validator 0, punct 0/0). PATCH 2026-10-01 (T-447) at end of era 7 bank: Jefferson's count, DC emancipation act, Roebling's treatment, caisson cases.
- part2 era 7 done: 21 / 1 / 1 (+1 fbf) (validator 0, punct 0/0). PART2 DONE.
- part3 era 8 done: 33 / 0 / 0 (+2 fbf) (validator 0, punct 0/0). PATCHes 2026-10-01 (T-447): first Klan's acts (from slavery-freedom bank), Empire State record lost in 1970, Hoover agency; and in era 10: mammy, Derek Chauvin.
- part3 era 9 done: 15 / 2 / 0 (+2 fbf) (validator 0, punct 0/0). PATCH 2026-10-01 (T-447): 1966 walkout and suit, Title VII, WTC record.
- part3 era 10 done: 27 / 2 / 0 (+1 fbf) (validator 0, punct 0/0). PATCH 2026-10-01 (T-447): National Monument to Freedom size (43 x 155 ft, settles the 50-ft line). PART3 DONE.
- Final: project_state --check landmarks --stage prose PASS (manuscript 13934 prose words; wc -w 14966 against 13660 before).
