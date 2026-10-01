# CHECKPOINT F5 | food-farming | step 5 fixer, whole chapter

STATUS: T-448 landed (director verified: PASS  food-farming / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/food-farming/part1|part2|part3 + control/audit/food-farming/part1|2|3-findings-sonnet.md
        + research/research-food-farming.md (PATCH entries only)

NOW:    all three parts done; prose check PASS (14376 w).
NEXT:   none (director: commit; NEEDS-RESEARCH items go to step 4)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 75 FIXED / 7 REJECTED / 0 NR, +4 found by fixer | 4679 -> 5122 (raw split; prose_words 4270 -> 4711) |
| part2 | 6-7 | done | 40 FIXED / 11 REJECTED / 0 NR (1 row withdrawn by checker), +2 found by fixer | 2637 -> 3061 (raw split; prose_words 2399 -> 2823) |
| part3 | 8-10 | done | 92 FIXED / 8 REJECTED / 2 NR, +4 found by fixer | 6843 -> 7417 (raw split; prose_words 6270 -> 6842) |

## NEEDS-RESEARCH
- part3 era 8, school lunch (finding 53): a figure for WWII draft rejections from poor nutrition (Gen. Lewis Hershey's testimony; blog summaries only: about 40 percent found unfit, "perhaps one-third" of rejections from nutrition). Prose keeps "many".
- part3 era 9, Black land loss 1910 to 1997 (finding 72): the bank counts the loss but names no cause before 1983. Find what sources name (violence, credit denial, heirs' property, forced sales) so the passage can say who took the land. SEARCHED, NOT FOUND entry in the bank.
- part3 era 8, Japanese American farms (enrichment, finding 47): confirm Densho's Yoshimi Matsuura sale ($23 an acre against about $200 netted from a harvest) on an opened page (densho.org refuses automated fetch). Not written.
- part3 era 10, Benitez: the "more than 700 farmworkers freed in one case" figure (search summaries only). Not written.

## Log
- part1 era 1 done: 9 FIXED, 1 REJECTED, 0 NR, 1 found by fixer. PATCH 2026-10-01 (T-448) goosefoot seeds + manoomin shallow water (bank era 01). Verdict scratch: scratchpad/T-448/v-part1.tsv, script apply_verdicts.py. validate 0 errors, punct 0/0.
- part1 era 2 done: 12 FIXED, 0 REJ, 0 NR. PATCH 2026-10-01 (T-448) Ranjel's account (slaves; women raped) in bank era 02. Checks clean.
- part1 era 3 done: 15 FIXED, 4 REJ, 0 NR, 1 found by fixer. PATCHes 2026-10-01 (T-448): Percy on the queen's killing (Capt. Davis) + Percy's 15-16 count; hominy/samp/johnnycake definitions. Checks clean.
- part1 era 4 done: 26 FIXED, 1 REJ, 0 NR, 1 found by fixer. No PATCH. Checks clean.
- part1 era 5 done: 13 FIXED, 1 REJ, 0 NR. PATCH 2026-10-01 (T-448) 'Indian corn/meal' + Amoskeag nets confirmed (bank era 05). Whole part re-read for flow; checks clean. PART1 DONE.
- part2 era 6 done: 14 FIXED, 4 REJ (1 row withdrawn by checker), 0 NR, 2 found by fixer. PATCHes 2026-10-01 (T-448) in bank era 06: Ho-Chunk at Grand Detour (copied from technology bank), Bad Axe (copied from war bank), Trail of Tears causes, Tudor 'Ice King' + loss scope. Checks clean. Verdict scratch v-part2.tsv.
- part2 era 7 done: 26 FIXED, 7 REJ, 0 NR. PATCH 2026-10-01 (T-448) Dawes Act + Morrill land-grant (copied from native-nations and education banks). Whole part re-read; checks clean. PART2 DONE.
- part3 era 8 done: 50 FIXED, 5 REJ, 1 NR, 2 found by fixer. PATCH 2026-10-01 (T-448) FDA/Bureau of Chemistry + Carver's enslavers (SHSMO) in bank era 08. Checks clean. Verdict scratch v-part3.tsv.
- part3 era 9 done: 26 FIXED, 1 REJ, 1 NR, 1 found by fixer. No PATCH. Checks clean.
- part3 era 10 done: 16 FIXED, 2 REJ, 0 NR, 1 found by fixer. PATCH 2026-10-01 (T-448) Nephi Craig's café and memoir (KJZZ, Civil Eats), Fair Food code zero-tolerance rules, Benitez medal date. SEARCHED, NOT FOUND entry added for Black land-loss causes (era 09). Part re-read; checks clean. PART3 DONE.
- FINAL: python tools/project_state.py --check food-farming --stage prose -> PASS (manuscript=14376w, 17 stories verified, 0 em dashes, 0 semicolons, validator 0 errors).
