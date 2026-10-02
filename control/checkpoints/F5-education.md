# CHECKPOINT F5 | education | step 5 fixer, split by part (giant chapter)

STATUS: T-479 landed (director verified: PASS  education / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode, applied to the parts assigned)
FILES:  manuscript/education/part1|part2|part3 + control/audit/education/part1|2|3-findings-sonnet.md
        + research/research-education.md (PATCH entries only)

NOW:    T-479 finished part3 (eras 8, 9, 10). Prose check PASS.
NEXT:   part1 (eras 1-5) and part2 (eras 6-7), by a later fixer

## Units
| part | eras | fixer | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|---|
| part1 | 1-5 | later | todo | | 8548 -> |
| part2 | 6-7 | later | todo | | 10207 -> |
| part3 | 8-10 | T-479 | DONE | 113 / 6 / 0 of 119, +25 found by fixer (era 8: 54/4/0 +12; era 9: 33/1/0 +10; era 10: 26/1/0 +3) | 24243 -> 25721 |

T-479 scratch: scratchpad/T-479 (verdicts.py + apply.py rebuild the findings table's fixer column from findings-orig.md).

## NEEDS-RESEARCH (round 2, from T-479)
- education era 10, Colin Gray: the exact meaning of second-degree murder under Georgia law (O.C.G.A. 16-5-1(d), believed to be causing a death while committing second-degree cruelty to children). Prose now says only "a murder charge one level below the most serious". Confirm from the statute and gloss it exactly.
- education era 10, vouchers and ESAs: how many children using them were already in private school. Clause cut as unsourced.
- education era 9, Sal Castro: arrest among the thirteen rests on Wikipedia citing the LA Times; confirm in the LA Times obituary or the LOC guide.
- education era 8, the matron and rattan glosses are word meanings, not bank facts; a round-2 check may want a dictionary line in the bank.

## Log
- 2026-10-02 T-479 era 8: 58 findings judged. Hardin testimony re-read in the scanned PDF: "Shall I whip her some more?", the oath and the family's "we will have to go rather hard on you" are all in it (checker and dispatch were wrong); PATCH added with her exact words. Rutherford date, three-city overstatement, Priddy test case, Gong Lum actor, UDC membership, Dewey school activities fixed or sourced. PATCHes (T-479): Hardin re-read; Dewey school (Mayhew and Edwards); Priddy test case; Gong Lum; UDC membership. validate 0 errors, punct 0/0.
- 2026-10-02 T-479 era 9: 34 findings judged (33 FIXED, 1 REJECTED in part: Sal Castro was among the thirteen arrested). PATCHes (T-479): Sputnik date (State Dept historian); Sal Castro (Wikipedia citing LA Times); Sandia report disputing A Nation at Risk (ERIC). Unnamed "some researchers" on paddling counts now attributed to Deana Pollard Sacks. validate 0 errors, punct 0/0.
- 2026-10-02 T-479 era 10: 27 findings judged (26 FIXED, 1 REJECTED: Uvalde's two staff were teachers). PATCHes (T-479): NCLB reporting groups (statute); ESSA kept and changed (statute); Uvalde teachers (Wikipedia with news cites); Florida SB 296 signed 21 May 2025 (Florida Senate); named studies on NCLB (Dee and Jacob) and Louisiana vouchers (Mills and Wolf; Egalite). Two unnamed "researchers/studies disagree" sentences replaced with named studies. validate 0 errors, punct 0/0.
- Final: `python tools/project_state.py --check education --stage prose` -> PASS (manuscript 42392w, validator 0 errors, emdash 0, semicolon 0). Part3 words 24243 -> 25721.
