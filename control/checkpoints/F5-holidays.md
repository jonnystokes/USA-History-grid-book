# CHECKPOINT F5 | holidays | step 5 fixer, whole chapter

STATUS: T-464 landed (director verified: PASS  holidays / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/holidays/part1|part2|part3 + control/audit/holidays/part1|2|3-findings-sonnet.md
        + research/research-holidays.md (PATCH entries only)

NOW:    done
NEXT:   none (all three parts DONE; prose check PASS)
WORDS:  wc -w on the part file
TOOLS:  scratch T-464/verdicts.py adds the fixer column from a json (see p1e1.json)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 124 / 1 / 0 (+7 found by fixer) | 6118 -> 7311 |
| part2 | 6-7 | DONE | 92 / 4 / 0 (+4 found by fixer) | 4565 -> 5513 |
| part3 | 8-10 | DONE | 96 / 5 / 0 (+2 found by fixer) | 5363 -> 6155 |

## NEEDS-RESEARCH
- None open. Unsourced items were searched and PATCHed or cut: "many families keep both" Kwanzaa and Christmas (cut), Italian American heritage sentence for Columbus Day (cut), Jarvis wanting visits (cut), "on Sundays" preaching (cut).

## Log
- part1 era 1: 25 FIXED, 0 REJECTED, 0 NR, 2 found by fixer (F1 taro/kapa, F2 salmon-feast order). PATCH 2026-10-01 era 1 (Akwesasne, Onondaga, Aquinnah, Bartram, Hawkins, Hopi, CRITFC, Celilo, Hawaii 1898, kapa/taro). validate 0 errors, punct 0/0.
- part1 era 2: 19 FIXED, 0 REJECTED, 0 NR, 1 found by fixer (F3 Oñate detail). Matanzas: Menéndez's own counts restored from his letter (PATCH era 2). validate 0, punct 0/0.
- part1 era 3: 35 FIXED, 1 REJECTED (47), 0 NR, 1 found by fixer (F4 Newell quote marks). PATCH era 3 (Berkeley Co., Plimoth renewal, Young, 1623 drought, pitching the bar, synod, kiva, Po'pay copied from religion, money). validate 0, punct 0/0.
- part1 era 4: 17 FIXED, 0 REJECTED, 0 NR, 1 found by fixer (F5 dropped vivid detail). PATCH era 4 (RMG, Knox, sassafras). validate 0, punct 0/0.
- part1 era 5: 28 FIXED, 0 REJECTED, 0 NR, 2 found by fixer (F6 Pope's Night end, F7 Metacom per #36). Fithian entry read in full (Gutenberg). PATCH era 5. validate 0, punct 0/0. PART1 DONE.
- part2 era 6: 40 FIXED, 4 REJECTED (9, 32, 34, 36), 0 NR, 3 found by fixer (F8 Johnkannaus detail, F9 Fanny escaped, F10 reindeer). PATCH era 6. validate 0, punct 0/0.
- part2 era 7: 52 FIXED, 0 REJECTED, 0 NR, 1 found by fixer (F11 Yates pastorate date). Boarding schools and Dawes brought up to the native-nations bank (#36), Code of Indian Offenses penalty from religion bank, all PATCHed. validate 0, punct 0/0. PART2 DONE.
- part3 era 8: 30 FIXED, 0 REJECTED, 0 NR, 1 found by fixer (F12 dropped bank detail). PATCH era 8 (Howe, Jarvis lawsuits and arrest, Jarvis quotes). validate 0, punct 0/0.
- part3 era 9: 46 FIXED, 1 REJECTED (72), 0 NR, 1 found by fixer (F13 settlement money). PATCH era 9 (Kwanzaa principles, King shot copied from work-workers, Wamsutta, Bridger, Pride annual). validate 0, punct 0/0.
- part3 era 10: 21 FIXED, 3 REJECTED (82, 91, 101), 0 NR, 0 found by fixer. validate 0, punct 0/0. PART3 DONE.
- Final: `python tools/project_state.py --check holidays --stage prose` PASS (9 stories verified, manuscript=17807w, 0/0 punct, 0 validator errors).
