# CHECKPOINT F5 | technology | step 5 fixer, whole chapter

STATUS: T-455 landed (director verified: PASS  technology / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/technology/part1|part2|part3 + control/audit/technology/part1|2|3-findings-sonnet.md
        + research/research-technology.md (PATCH entries only)

NOW:    done
NEXT:   none (director: commit, park the NEEDS-RESEARCH item)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 93 / 2 / 0, plus 14 found by fixer (F1-F14, all FIXED) | 5507 raw (prose_words 5138) -> prose_words 5828 |
| part2 | 6-7 | done | 53 / 8 / 1, plus 3 found by fixer (F1-F3, all FIXED) | 4056 raw (prose_words 3778) -> prose_words 4177 |
| part3 | 8-10 | done | 66 / 3 / 0, plus 6 found by fixer (F1-F6, all FIXED) | 6114 raw (prose_words 5700) -> prose_words 6128 |

Word counts: "raw" is the figure the checkpoint was opened with. prose_words is tools/project_state.py's own count, before (git HEAD) and after.

## NEEDS-RESEARCH
- part2 era 7, row 30 (Ned, 1857): what Oscar Stuart's threat to "correct" Ned "according to our Southern usage" meant in practice. One search found no source that glosses it (try Swanson 2020's notes, Yancy 1984, Boyle 1960). Prose keeps "To correct meant to punish. Stuart did not write what the punishment would be."

## Log
- 2026-10-01 part1 era 1 done: rows 1-20 (18 FIXED, 2 REJECTED), F1 found by fixer. PATCH 2026-10-01 (T-455) weir mechanism + National Heritage Fellowship. validate 0 errors, punct 0/0.
- part1 era 2 done: rows 21-29 all FIXED. validate 0, punct 0/0.
- part1 era 3 done: rows 30-57 all FIXED, F2-F6 found by fixer (Undertakers gloss the main one). validate 0, punct 0/0.
- part1 era 4 done: rows 58-71 all FIXED, F7-F10 found by fixer. PATCH 2026-10-01 (T-455) inverted siphon + convict transportation (Encyclopedia Virginia). validate 0, punct 0/0.
- part1 era 5 done: rows 72-95 all FIXED, F11-F14 found by fixer. PATCH 2026-10-01 (T-455) Schuyler owner + Newcomen mechanism + Mulberry Grove enslaved + Northup on Patsey's whipping. validate 0, punct 0/0. PART 1 DONE.
- part2 era 6 done: rows 1-23 (20 FIXED, 3 REJECTED), F1 found by fixer. PATCH 2026-10-01 (T-455) Daguerre + Anderson's own words. validate 0, punct 0/0.
- part2 era 7 done: rows 24-62 (33 FIXED, 5 REJECTED, 1 NEEDS-RESEARCH), F2-F3 found by fixer. PATCH 2026-10-01 (T-455) Watson/Boston + Edison Pioneers + National Archives barbed-wire exact words (corrects the bank's "already displaced"). validate 0, punct 0/0. PART 2 DONE.
- part3 era 8 done: rows 1-27 (25 FIXED, 2 REJECTED), F1 found by fixer. PATCH 2026-10-01 (T-455) Dayton/Daniels + Model T line (History.com) + 1908 injuries + ENIAC programmers' method. validate 0, punct 0/0.
- part3 era 9 done: rows 28-46 all FIXED, F2-F4 found by fixer. validate 0, punct 0/0.
- part3 era 10 done: rows 47-69 (22 FIXED, 1 REJECTED), F5-F6 found by fixer. Span label "The camera that picks a face" changed to "A wrongful arrest and face recognition" (the label broke the personification rule). PATCH 2026-10-01 (T-455) Williams charges dropped + Worthy's apology + CRISPR (copied from science bank). validate 0, punct 0/0. PART 3 DONE.
- Final: python tools/project_state.py --check technology --stage prose -> PASS (10/10 written, 23 stories verified, 0 em dash, 0 semicolon, 16133 words, validator 0 errors).
