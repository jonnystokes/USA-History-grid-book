# CHECKPOINT F5 | native-nations | step 5 fixer, whole chapter

STATUS: T-474 landed (director verified: PASS  native-nations / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/native-nations/part1|part2|part3 + control/audit/native-nations/part1|2|3-findings-sonnet.md
        + research/research-native-nations.md (PATCH entries only)

NOW:    T-474 fixer started 2026-10-02; part1 light pass (word counts by `wc -w`: 6836 / 4820 / 6163)
NEXT:   none (director: commit; NEEDS-RESEARCH items to GAPS)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE light pass (14 edits, see Log) | n/a (light pass) | 6836 -> 6874 |
| part2 | 6-7 | DONE | 58 FIXED / 6 REJECTED / 1 NR + 13 found by fixer (era 6: 23/3/0 +6, era 7: 35/3/1 +7) | 4820 -> 5951 |
| part3 | 8-10 | DONE | 76 FIXED / 2 REJECTED / 0 NR + 8 found by fixer (era 8: 26/0/0 +3, era 9: 33/0/0 +3, era 10: 17/2/0 +2) | 6163 -> 6873 |

## NEEDS-RESEARCH
- part3 era 9 (row 57): what Adam Fortunate Eagle's *Pipestone* (2010) says about the system's harm, in his words; the prose says only that he writes about it.
- part3 era 9: who fired the shot that hit Frank Clearwater at Wounded Knee, 1973 (prose: 'No record names who fired that shot').
- part2 era 7 (row 35): who told Black Kettle's Sand Creek camp it was under army protection (Wynkoop? Anthony at Fort Lyon?). Prose keeps the bank's 'had been told'.
- part2 era 7: Wounded Knee share of women and children differs (Britannica 'most', Smithsonian 'almost half'); prose states both. Settle from a primary count if one exists.
- part2 era 7: Sherman's overruling of Miles rests on Wikipedia + NPS (Greene) search summary; confirm on the NPS Greene ch. 14 page (fetch returned the index page).

## Log
- part1 light pass DONE: big words out (continental, in all probability, verdict, victors, solemn, pledged, judged unwinnable, economy, best-documented); 'forced removals' made plain; 'diplomacy' and 'pardon' defined; 'Pueblo nations rose' -> people rose; 'Historians commonly call' Pueblo Revolt -> named source (EBSCO Research Starters, confirmed on search). Validator 0 errors, punct 0/0.
- part2 era 6 DONE: 26 findings judged (22 FIXED, 4 REJECTED: rows 8, 12 (#37), 13; 12 partly), 6 found-by-fixer rows. PATCH 2026-10-02 (T-474) era 6: Tecumseh Vincennes 1810 quotes, Tuckabatchee 1811, Procter, Worcester (AUDIT-QUEUE item closed in prose), Osceola birth/head, Neugin detail, Thornton 1984. Validator 0, punct 0/0.
- part2 era 7 DONE: 39 findings judged (35 FIXED, 3 REJECTED: 33, 62 (#37), 63; 1 NR: 35) + 7 found-by-fixer (Sand Creek per #36, Bear River and Marias added, Mankato details, Wounded Knee dispute, personification, fourth wall, big words). PATCH 2026-10-02 (T-474) era 7 added. Three 'sources do not identify' sentences were false: Duley, Gentles (disputed), Miles/Sherman now named. Validator 0, punct 0/0. Part 2 words 4820 -> 5951.
- part3 era 8 DONE: 26 findings, all FIXED (Osage killers named: Hale, Burkhart; three counts; Osage allotment 657 acres; Thorpe rule; Hayes bond tour and death; fourth-wall lines cut) + 3 found by fixer. PATCHes for eras 8, 9, 10 written to the bank. Validator 0, punct 0/0.
- part3 era 9 DONE: 33 findings, all FIXED (Wounded Knee 1973 dead named, Grimm and Nichol added per #36; ICWA numbers from NICWA; Alcatraz prison; fourth-wall line cut) + 3 found by fixer. Validator 0, punct 0/0.
- part3 era 10 DONE: 19 findings (17 FIXED, 2 REJECTED: 61, 75 (movie= must not change)) + 2 found by fixer (Standing Rock police per #36; big words). Validator 0, punct 0/0. Part 3 words 6163 -> 6873.
- FINAL: python tools/project_state.py --check native-nations --stage prose -> PASS (manuscript=18589w, 10/10 eras, 21 stories verified, 0/0 punct, validator 0). wc -w: 6836->6874, 4820->5951, 6163->6873.
