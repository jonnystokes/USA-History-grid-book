# CHECKPOINT F5 | drugs-alcohol | step 5 fixer, whole chapter

STATUS: T-465 landed (director verified: PASS  drugs-alcohol / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/drugs-alcohol/part1|part2|part3 + control/audit/drugs-alcohol/part1|2|3-findings-sonnet.md
        + research/research-drugs-alcohol.md (PATCH entries only)

NOW:    T-465 fixer (opus), all three parts DONE. Prose check PASS.
NEXT:   none (director: commit; NEEDS-RESEARCH items go to round 2)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 100 / 4 / 1, +3 found by fixer | 6991 -> 7571 |
| part2 | 6-7 | done | 61 / 4 / 0, +2 found by fixer (1 NR item listed from a FIXED row) | 4471 -> 4862 |
| part3 | 8-10 | done | 97 / 9 / 0, +4 found by fixer (1 NR item listed from a FIXED row) | 8764 -> 9274 |

## NEEDS-RESEARCH
- part1 era 3 (#58): why Massachusetts (1638, 1647) banned smoking within twenty poles of houses, barns, corn and haystacks. Fire reason cut from the prose; open the Massachusetts Records.
- part1 era 5 (#105): how the 109 captives on the Sally (1764-65) died; prose gives the count only.
- part2 era 7 (#35): what the WCTU's southern branches did on race under "states rights" (separate branches? Black women kept out?). Prose now quotes and explains the phrase only.
- part3 era 9 (#62): which Native nations kept their liquor bans after 1953 (only a search summary names the Oglala Sioux). Prose now says the law let each nation decide.

## Log
- part1 era 1: 15 FIXED, 0 REJECTED, 0 NR, 1 found by fixer (F1). validate 0 errors, punct 0/0.
- part1 era 2: 13 FIXED, 1 REJECTED, 0 NR, 1 found by fixer (F2). PATCH (era 02): Hariot mathematician, Linnaeus Swedish. Checks clean.
- part1 era 3: 28 FIXED, 1 REJECTED (milder, PATCHed), 0 NR. PATCH (era 03): Rolfe milder; SEARCHED NOT FOUND fire reason. Checks clean.
- part1 era 4: 14 FIXED, 1 REJECTED (George II, PATCHed), 0 NR. Georgia rum-trade direction corrected. Checks clean.
- part1 era 5: 30 FIXED, 1 REJECTED (Fort Stanwix 1768, PATCHed), 1 NR (#105), 1 found by fixer (F3). PATCH (era 05): Fort Stanwix 1784 (copied from america-world bank), 1768 cession confirmed. Checks clean.
- part2 era 6: 26 FIXED, 1 REJECTED (#25), 0 NR, 1 found by fixer (F1). PATCH (era 06): Lincoln address text. Checks clean.
- part2 era 7: 35 FIXED, 3 REJECTED (#43, #56 PATCHed, #64), 0 NR, 1 found by fixer (F2). PATCH (era 07): Harper, Wells. Checks clean.
- part3 era 8: 49 FIXED, 4 REJECTED (#15, #41, #42, #43, all PATCHed), 0 NR, 2 found by fixer. PATCH (era 08): Wheeler drafting, AA founders and meetings, jake leg, Pershing. Checks clean.
- part3 era 9: 23 FIXED, 4 REJECTED (#66, #75, #78, #79; #66 and #78 PATCHed), 0 NR, 1 found by fixer. PATCH (era 09): 1970 ad-ban law, Ford term, OxyContin 12 hours. Checks clean.
- part3 era 10: 25 FIXED, 1 REJECTED (#106), 0 NR, 1 found by fixer. PATCH (era 10): Temple of Dendur. Checks clean.
- Final: validate 0 errors x3, punct 0/0 x3. Word counts (wc -w) part1 6991->7571, part2 4471->4862, part3 8764->9274. python tools/project_state.py --check drugs-alcohol --stage prose: PASS (manuscript=20454w, 14 stories verified, 0 VERIFY, 0 em dash, 0 semicolon, validator 0 errors).
