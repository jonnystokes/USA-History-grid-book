# CHECKPOINT F5 | transportation | step 5 fixer, whole chapter

STATUS: T-445 landed (director verified: PASS  transportation / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/transportation/part1|part2|part3 + control/audit/transportation/part1|2|3-findings-sonnet.md
        + research/research-transportation.md (PATCH entries only)

NOW:    nothing
NEXT:   nothing (director: commit)

Word counts: "wc" = `wc -w` of the whole file (the method behind the starting numbers below);
"prose" = tools/project_state.py prose_words().

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH (+ found by fixer) | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 43 / 8 / 0 (+5 found by fixer, all FIXED) | wc 3166 -> 3408 · prose 2881 -> 3124 |
| part2 | 6-7 | done | 55 / 6 / 0 (+6 found by fixer, all FIXED) | wc 5072 -> 5345 · prose 4735 -> 5009 |
| part3 | 8-10 | done | 75 / 6 / 0 (+4 found by fixer, all FIXED) | wc 5968 -> 6075 · prose 5508 -> 5616 |

## PATCHes added (research/research-transportation.md)
- era 4: PATCH 2026-10-01 (T-445): Treaty of Lancaster signers (the printed treaty's title) and the dispute over what it covered (Virginia Places).
- era 6: PATCH 2026-10-01 (T-445): Congress approved the National Road in 1806 (NPS).
- era 7: PATCH 2026-10-01 (T-445): why "the day of two noons", Allen as editor of the railway guide (LOC); Plessy test case and ruling copied from the rights-movements bank.

## NEEDS-RESEARCH
- none from the findings.

## For the director (AUDIT-QUEUE candidates)
- Bank hygiene: era 10 GPS line says Selective Availability's end improved accuracy "~tenfold, ~100 m -> ~20 m"; 100 to 20 is five times. Prose now gives only the meters. Check gps.gov wording.
- Bank hygiene: era 7 untagged rows still carry "roughly 1,200 died" and the Ten-Mile Day "last rails" line; the T-248 and T-305a PATCHes correct them (already parked for Ten-Mile Day).
- Rule question: part3 used "X is told in the Y chapter" ten times; all cut as fourth-wall breaks (writing-style-guide §0 forbids mentioning the book or a chapter). Other chapters may carry the same habit.
- The FAA's creation in 1958: prose follows the bank ("a major reason the Federal Aviation Agency was set up"); faa.gov history pages returned 403, so Congress/Eisenhower as actors were not added.

## Log
- part1 era 1: 9 findings (8 FIXED, 1 REJECTED). Validator 0 errors, punct 0/0.
- part1 era 2: 11 findings (10 FIXED, 1 REJECTED).
- part1 era 3: 6 findings (4 FIXED, 2 REJECTED).
- part1 era 4: 15 findings (13 FIXED, 2 REJECTED) + 3 found by fixer. Treaty of Lancaster PATCH.
- part1 era 5: 10 findings (8 FIXED, 2 REJECTED) + 1 found by fixer. Era 1 fixer row (nations as actors).
- part1 done: validator 0 errors, punct 0/0.
- part2 era 6: 29 findings (28 FIXED, 1 REJECTED) + 3 found by fixer. National Road PATCH (NPS). Validator 0, punct 0/0.
- part2 era 7: 32 findings (27 FIXED, 5 REJECTED) + 3 found by fixer. Two noons + Plessy PATCH. Validator 0, punct 0/0.
- part3 era 8: 24 findings (21 FIXED, 3 REJECTED) + 2 found by fixer. Cross-chapter "is told in" lines cut. Validator 0, punct 0/0.
- part3 era 9: 27 findings (25 FIXED, 2 REJECTED). Validator 0, punct 0/0.
- part3 era 10: 30 findings (29 FIXED, 1 REJECTED) + 2 found by fixer. Source lines folded into their sentences (DECISIONS #37). Validator 0, punct 0/0.
- Final: `python tools/project_state.py --check transportation --stage prose` PASS (manuscript 13749 prose words, 19 stories verified, validator 0 errors, emdash 0, semicolon 0).
