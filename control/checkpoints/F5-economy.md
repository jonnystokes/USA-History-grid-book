# CHECKPOINT F5 | economy | step 5 fixer, whole chapter (test 1 of 3: smallest chapter)

STATUS: T-442 landed (director verified: PASS  economy / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/economy/part1|part2|part3 + control/audit/economy/part1|2|3-findings-sonnet.md
        + research/research-economy.md (PATCH entries only)

NOW:    finished
NEXT:   none. Director: commit; park the two NEEDS-RESEARCH items for step 4.

## Units
Word counts: first figure is `wc -w` of the whole file (the basis of the original table, which read one higher); prose_words is tools/project_state.py's reader-facing count.
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 39 / 4 / 2 of 45 checker rows, plus 5 found by fixer (F1-F5), all FIXED | 4019 -> 4548 (prose_words 3628 -> 4153) |
| part2 | 6-7 | DONE | 53 / 9 / 0 of 62 checker rows, plus 5 found by fixer (F6-F9, F11), all FIXED | 4720 -> 5284 (prose_words 4413 -> 4977) |
| part3 | 8-10 | DONE | 58 / 6 / 0 of 64 checker rows, plus 1 found by fixer (F10), FIXED | 5647 -> 6230 (prose_words 5252 -> 5835) |
| total | | | 150 / 19 / 2 of 171, plus 11 found by fixer | 14386 -> 16062 (prose_words 13293 -> 14965) |

## NEEDS-RESEARCH
- economy part1 era 3 (row 16): servant women's pregnancies. Who fathered the children (masters?) and how Virginia courts punished the women (extra years; 1662 law on masters as fathers). Bank is silent.
- economy part1 era 4 (row 24): a death rate for enslaved children in the Lowcountry ("especially high rates" has no number).
- (recorded in the bank as SEARCHED, NOT FOUND, prose already says so) the names of the men who tortured James Knox at Flat Top, 1924.

## PATCHes added to research/research-economy.md (all "2026-10-01 (T-442)")
- era 1: how the hoe blades were made, and obsidian distances
- era 3: Jamestown's gold hunt, and the 1705 slave code (copied from slavery-freedom)
- era 5: the Sally's deaths, John Brown's 1797 trial, the Whiskey Rebellion arrests
- era 7: debtors' prison, Tompkins Square, Coxey's arrest, James Knox, Homestead 1892, Hall, Homestead Act land
- era 10 block: names, actors and dates for eras 8 to 10 (Bonus Army shooters, STFU violence, CCC/AAA/CES, CPI fall, Ida May Fuller, Volcker, grain and oil embargoes, Farm Aid, TARP)

## Log
- part1 era 1 (before-1500): rows 1-6 + F1 judged (FIXED 3+F1, REJECTED 3). PATCH era 1 (chipping, quarry pits, obsidian). validate 0 errors, punct 0/0.
- part1 era 2 (1500s): rows 7-10 FIXED 4. validate 0, punct 0/0.
- part1 era 3 (1600s): rows 11-22 + F2: FIXED 11+F2, NEEDS-RESEARCH 1 (row 16). PATCH era 3 (gold hunt, 1705 code). validate 0, punct 0/0.
- part1 era 4 (1700-1750): rows 23-31 + F3, F4: FIXED 8+F3+F4, REJECTED 1 (31), NEEDS-RESEARCH 1 (24). validate 0, punct 0/0.
- part1 era 5 (1750-1800): rows 32-44 + F5: FIXED 13+F5. PATCH era 5. validate 0, punct 0/0. PART1 DONE.
- part2: PATCH for eras 6-7 written.
- part2 era 6 (1800-1850): rows 1-24 + F6: FIXED 20+F6, REJECTED 4 (10, 12, 21, 24). validate 0, punct 0/0.
- part2 era 7 (1850-1900): rows 25-62 + F7-F9: FIXED 33+3, REJECTED 5 (27, 34, 52, 59, 62). validate 0, punct 0/0. PART2 DONE.
- part3: PATCH for eras 8-10 written.
- part3 era 8 (1900-1950): rows 1-32: FIXED 30, REJECTED 2 (4, 11). validate 0, punct 0/0.
- part3 era 9 (1950-2000): rows 33-51: FIXED 15, REJECTED 4 (34, 42, 43, 49). validate 0, punct 0/0.
- part3 era 10 (2000-today): rows 52-64 + F10: FIXED 13+F10. validate 0, punct 0/0. PART3 DONE.
- final scan: part2 line 69 "The sources disagree" (fourth wall) fixed as F11. Prose check: PASS economy / prose, 10/10 eras, 11 stories verified, 0 em dashes, 0 semicolons, 14965w, validator 0 errors.
