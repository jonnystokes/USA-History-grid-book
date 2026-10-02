# CHECKPOINT F5 | news-communication | step 5 fixer, whole chapter

STATUS: T-471 landed (director verified: PASS  news-communication / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/news-communication/part1|part2|part3 + control/audit/news-communication/part1|2|3-findings-sonnet.md
        + research/research-news-communication.md (PATCH entries only)

NOW:    done (T-471 fixer started 2026-10-02; style files, brief, DECISIONS #28-38, AUDIT-QUEUE read)
NEXT:   none (director: commit; NEEDS-RESEARCH items to round 2)
SCRATCH: scratchpad/T-471 (bank slices bank-eN.md, verdicts.py, p1.json / p2.json / p3.json = fixer column per part)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 92 findings: 83 FIXED / 9 REJECTED / 2 NEEDS-RESEARCH (34, 89, both also fixed); 6 found by fixer (F1-F6) | 7753 -> 8487 (wc -w +1, same method as before) |
| part2 | 6-7 | DONE | 98 findings: 84 FIXED / 14 REJECTED / 1 NEEDS-RESEARCH (25, also partly fixed); 2 found by fixer (F1-F2) | 6370 -> 7066 |
| part3 | 8-10 | DONE | 147 findings: 136 FIXED / 11 REJECTED / 1 NEEDS-RESEARCH (128, also partly fixed); 0 found by fixer | 8550 -> 9423 |

## NEEDS-RESEARCH
- part1 era 5 (finding 89): who barred Benjamin Franklin Bache from the House floor, 1797-98. Search summary names Speaker Jonathan Dayton (Founders Online editorial note); confirm on a real page.
- part1 era 3 (finding 34): how the Spanish tortured Catua and Omtua, 1680 (method). Prose says the accounts do not say.
- part2 era 6 (finding 25): a page stating the Treaty of New Echota ceded the land to the United States (prose says what the Cherokee gave up and where they were bound to move).
- part3 era 10 (finding 128): what the Clark County Public Administrator does (prose says only 'a county official').

## Log
- 2026-10-02 part1 era 1 done: findings 1-6 FIXED (6/0/0). PATCH era 1: Haudenosaunee home and names. validate 0 errors, punct 0/0.
- 2026-10-02 part1 era 2 done: findings 7-18 (16 FIXED, 17 REJECTED by PATCH; 16 fixed via PATCH). PATCHes era 2: Harriot at Roanoke (from health bank), Amadas and Barlowe first names. validate 0, punct 0/0.
- 2026-10-02 part1 era 3 done: findings 19-34 (15 FIXED, 1 REJECTED, 1 NEEDS-RESEARCH (34, also fixed), F1 found by fixer). PATCHes era 3: Virginia first allowed press 1730; Po'pay Tewa; SEARCHED NOT FOUND torture method. validate 0, punct 0/0.
- 2026-10-02 part1 era 4 done: findings 35-58 (22 FIXED incl. 45 part, 2 REJECTED (38; 56 by PATCH), 0 NR; F2 found by fixer). PATCHes era 4: inoculation/Onesimus/Courant dates; Franklin to Philadelphia, Poor Richard, Sauer in Germantown. validate 0, punct 0/0.
- 2026-10-02 part1 era 5 done: findings 59-92 (27 FIXED, 5 REJECTED (64, 78, 90, 91 + partial), 1 NR (89); F3-F5 found by fixer). PATCHes era 5: Lexington letter detail (Bell), Boston Pamphlet content, July 4 and Dunlap distribution, 'African Slavery in America' authorship dispute, Quasi-War (america-world), Hamilton Treasury (money), Bache barred SEARCHED, Lyon plea + grand jury + poet Barlow (FJC). validate 0, punct 0/0. PART1 DONE.
- 2026-10-02 part2 era 6 done: findings 1-45 (39 FIXED, 5 REJECTED/partly (6, 9, 34, 45), 1 NR (25, partly fixed); F1 found by fixer). PATCHes era 6: Chase/Cooper fine dispute (FJC), Boudinot resignation and treaty terms (OHS, NGE, native-nations), Garrison immediate end (NPS), Douglass 1841 (FD Papers), Missouri slavery (slavery-freedom). validate 0, punct 0/0.
- 2026-10-02 part2 era 7 done: findings 46-98 (40 FIXED, 13 REJECTED; F2 found by fixer: cause of the 1802 mail rule). Wilmington rewritten per director note: white mob shot and killed Black men, all reported dead Black, 'murdered', 'each side' kept only at the argument. PATCHes era 7: 1802 rule and 1865 repeal (USPS Historian), Antietam (war), Bly scenes (her book), Bly trip (Heinz), Wells editorial and lynching (Southern Horrors), Wilmington killers (PBS, DNCR, NCpedia). validate 0, punct 0/0. PART2 DONE.
- 2026-10-02 part3 era 8 done: findings 1-58 (56 FIXED, 2 REJECTED (15, 55)). PATCHes era 8: Jungle/1906 laws/Adams/Standard Oil/Hampton (other banks), Leader permit actor (MTSU), Sengstacke-Biddle terms and Double V (PBS), Manzanar/Heart Mountain (NPS), first fireside chat (money bank). validate 0, punct 0/0.
- 2026-10-02 part3 era 9 done: findings 59-106 (39 FIXED, 9 REJECTED). My Lai rapes named per DECISIONS #36 (PATCH from war bank). PATCHes era 9: My Lai; Evers, Pettus, Butterfield, Berners-Lee (other banks); Tet (State Dept), Jet (Henry Ford), McCarthy Wisconsin (Senate), Telecom Act signing (MTSU). validate 0, punct 0/0.
- 2026-10-02 part3 era 10 done: findings 107-147 (39 FIXED, 2 REJECTED (143 by PATCH; 128 partly NR)). PATCHes era 10: AP barred by Leavitt + McFadden ruling (CBS), Rescissions Act signing (CBS). F6 added to part1 (Sources differ -> The accounts differ). All three parts: validate 0 errors, punct 0/0.
- 2026-10-02 FINAL: python tools/project_state.py --check news-communication --stage prose -> PASS (10/10 eras written, 23 stories verified, 0 VERIFY, 0 em dashes, 0 semicolons, 23248 w, validator 0 errors). Word counts by wc -w +1: part1 7753 -> 8487, part2 6370 -> 7066, part3 8550 -> 9423.
- Note: two early bank PATCH headers (era 1 and era 2) were appended with a short Bash heredoc before the rule was noticed; all later bank writes used Edit. Content is unaffected.
