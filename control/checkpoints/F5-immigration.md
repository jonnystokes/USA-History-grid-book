# CHECKPOINT F5 | immigration | step 5 fixer, whole chapter

STATUS: T-461 landed (director verified: PASS  immigration / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/immigration/part1|part2|part3 + control/audit/immigration/part1|2|3-findings-sonnet.md
        + research/research-immigration.md (PATCH entries only)

NOW:    all three parts done; prose check PASS
NEXT:   none (director: commit)
SCRATCH: scratchpad/T-461 (verdict.py appends the fixer column from a JSON of verdicts)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 67 / 5 / 0, plus 8 found by fixer | 3941 (wc 3940) -> 5260 (wc) |
| part2 | 6-7 | DONE | 56 / 1 / 1 (row 26 fixed by attribution, also listed NR), plus 1 found by fixer | 5658 (wc 5657) -> 6240 (wc) |
| part3 | 8-10 | DONE | 76 / 1 / 1, plus 1 found by fixer | 7787 (wc 7786) -> 8472 (wc) |

## NEEDS-RESEARCH
- part3 era 8, Doukenie Bacos: whether officials let her in (bank silent). Check her Ellis Island Oral History, series EI no. 049.
- part2 era 7, Louisville Bloody Monday: read "The Myths of Bloody Monday" (Register of the Kentucky Historical Society, Project MUSE 887641; blocked by a verification page) and settle the Quinn's Row shootings and the "well over 100" count. Prose now attributes Quinn's Row to later accounts.

## Log
- part1 era 1 DONE: 5 FIXED, 2 found by fixer (Norse "ten years" false per exploration bank; whose land). PATCH T-461 era 1 (Norse, copied from exploration bank). validate 0 errors, punct 0/0.
- part1 era 2 DONE: 6 FIXED, 3 REJECTED, 1 found by fixer (Roanoke). PATCH T-461 era 2 (Seloy, Fort Caroline, Roanoke signal; copied from city-building, art, drugs-alcohol, news-communication banks). validate 0, punct 0/0.
- part1 era 3 DONE: 27 FIXED, 0 REJECTED, 3 found by fixer (loblollie thick not thin; fourth-wall captors line; Hutchinson record). PATCH T-461 era 3 (whose land, 1609/1622, Laud, Hutchinson trial/death, Edict of Nantes, Duke of York, loblolly). validate 0, punct 0/0.
- part1 era 4 DONE: 12 FIXED, 1 REJECTED, 1 found by fixer (Sullivan's Island fourth-wall line). PATCH T-461 era 4 (Test Act, convict merchants, Sullivan's Island, Zenger arrest/jury). validate 0, punct 0/0.
- part1 era 5 DONE: 17 FIXED, 1 REJECTED, 1 found by fixer. PATCH T-461 era 5 (Haitian Revolution, Toussaint freedom). validate 0, punct 0/0. PART1 COMPLETE.
- part2 era 6 DONE: 21 FIXED. PATCH T-461 era 6 (Acts of Union line inside the famine PATCH). validate 0, punct 0/0.
- part2 era 7 DONE: 35 FIXED, 1 REJECTED, 1 NEEDS-RESEARCH (also fixed by attribution), 1 found by fixer (slur printed, DECISIONS #35). PATCHes T-461 era 7 (Know-Nothing 1854 seats, Wong Kim Ark Wise/Morrow, Page Act practice). validate 0, punct 0/0. PART2 COMPLETE.
- part3 era 8 DONE: 28 FIXED, 1 REJECTED, 1 NEEDS-RESEARCH. Sterilization now meets policy 3b (method, actor, scale). PATCH T-461 era 8. validate 0, punct 0/0.
- part3 era 9 DONE: 24 FIXED, 1 found by fixer (USS Dubuque did stop and give food; captain court-martialed). PATCH T-461 era 9. validate 0, punct 0/0.
- part3 era 10 DONE: 24 FIXED. PATCH T-461 era 10 (DACA pointer copied from rights-movements; glosses). validate 0, punct 0/0. PART3 COMPLETE.
- Word counts by wc -w: 17383 -> 19972. project_state measured manuscript=18764w.
- FINAL: python tools/project_state.py --check immigration --stage prose -> PASS (10/10 eras written, 20/20 stories verified, 0 VERIFY, 0 em dashes, 0 semicolons, validator 0 errors).
