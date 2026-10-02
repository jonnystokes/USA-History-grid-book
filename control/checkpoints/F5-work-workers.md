# CHECKPOINT F5 | work-workers | step 5 fixer, whole chapter

STATUS: T-457 landed (director verified: PASS  work-workers / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/work-workers/part1|part2|part3 + control/audit/work-workers/part1|2|3-findings-sonnet.md
        + research/research-work-workers.md (PATCH entries only)

NOW:    done
NEXT:   none. Every finding in the three files carries a verdict in its `fixer` column; found-by-fixer rows are F1... at the end of each table.

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 52 / 6 / 0, found by fixer 6 (F1-F6) | 2451 -> 2805 |
| part2 | 6-7 | done | 52 / 4 / 0, found by fixer 1 (F1) | 4191 -> 4784 |
| part3 | 8-10 | done | 83 / 2 / 0, found by fixer 8 (F1-F8) | 9240 -> 9896 |

Word counts are whole-file whitespace splits, the same method as the baseline. Prose words (project_state): 16055.

## NEEDS-RESEARCH
None. Gaps were filled with PATCHes or the unsourced fact was cut. Facts cut as unsourced: "Owners closed steel mills and factories across the Midwest" (part3 era 9); "without pay" for convict leasing (Curtin shows overtime cash; replaced by sourced whipping and death rates); "so he could come home" (Frethorne); "in San Francisco from 2015" (Lawson record line).

For the audit (not this fixer's files): the PBS quote "the trial and the conduct of the judge had been shamefully unjust" is quoted in the bank as Altgeld's reason; it may be PBS's own wording. Prose no longer quotes it as his.

## PATCHes added to research/research-work-workers.md (all dated 2026-10-01, T-457)
- era 02: Acoma 1598-1599, the harms (copied from the native-nations bank: the Acoma account of the rape, the January 1599 killings, 300 to 1,500 dead, the disputed foot-cutting)
- era 03: wages, the pregnancy penalty, and who sat on the General Court (Encyclopedia Virginia)
- era 04: how fast the enslaved workforce grew in Virginia (Encyclopedia Virginia)
- era 06: 1806 trial actors (Encyclopedia of Greater Philadelphia), Hopewell second payroll count (from energy bank), cholera (CDC), Waldron 1676 and the Pennacook (Wikipedia, Handbook text unconfirmed), King Philip's War gloss (native-nations bank)
- era 07: Reading 1877 shooters (Wikipedia, unconfirmed), Haymarket order, shooting and Judge Gary (Chicago History Museum), Knights demands and the 1890 fall (Encyclopedia.com), Jennie Curtis testimony, convict leasing actors, whipping and death rate (slavery-freedom bank; Curtin)
- era 08: Addie Card's later life (VTDigger 2024), Executive Order 8802 text (National Archives)

## Log
- part1 era 1 (before-1500): rows 1-7 judged (5 FIXED, 2 REJECTED), F1 found by fixer. validate 0 errors, punct 0/0.
- part1 era 2 (1500s): rows 8-15 all FIXED; F2-F4 found by fixer (F2: Acoma harms added under #36/#31). PATCH added: "Acoma 1598-1599, the harms". validate 0, punct 0/0.
- part1 era 3 (1600s): rows 16-42: 23 FIXED, 4 REJECTED (19, 25, 32, 38); F5 found by fixer. PATCH added: "wages, the pregnancy penalty, and who sat on the General Court" (Encyclopedia Virginia). validate 0, punct 0/0.
- part1 era 4 (1700-1750): rows 43-53 all FIXED. PATCH added: "how fast the enslaved workforce grew in Virginia" (Encyclopedia Virginia). validate 0, punct 0/0.
- part1 era 5 (1750-1800): rows 54-58 all FIXED; F6 found by fixer. validate 0, punct 0/0. PART 1 DONE.
- part2 era 6 (1800-1850): rows 1-22: 20 FIXED, 2 REJECTED (10, 15); row 13 fixed in part ("sachem" kept as a word of the time). PATCH added: "era 06 gaps filled". validate 0, punct 0/0.
- part2 era 7 (1850-1900): rows 23-56: 32 FIXED, 2 REJECTED (25, 31); F1 found by fixer (Altgeld quote). PATCH added: "era 07 gaps filled". validate 0, punct 0/0. PART 2 DONE.
- part3 era 8 (1900-1950): rows 1-40: 38 FIXED, 2 REJECTED (12, 32); F1-F5 found by fixer (incl. one span label that personified the Court). PATCH added: "Addie Card's later life, and the words of Executive Order 8802". validate 0, punct 0/0.
- part3 era 9 (1950-2000): rows 41-62 + 59a (23 rows): all FIXED; F6-F7 found by fixer. validate 0, punct 0/0.
- part3 era 10 (2000-today): rows 63-84: all FIXED; F8 found by fixer. validate 0, punct 0/0. PART 3 DONE.
- Final: `python tools/project_state.py --check work-workers --stage prose` PASS (10/10 eras written, 17 stories verified, 0 em dashes, 0 semicolons, 16055 words, validator 0 errors).
