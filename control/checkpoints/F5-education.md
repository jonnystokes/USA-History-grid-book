# CHECKPOINT F5 | education | step 5 fixer, split by part (giant chapter)

STATUS: DONE: part1 T-481, part2 T-482, part3 T-479
BRIEF:  control/briefs/FIXER.md (whole-chapter mode, applied to the parts assigned)
FILES:  manuscript/education/part1|part2|part3 + control/audit/education/part1|2|3-findings-sonnet.md
        + research/research-education.md (PATCH entries only)

NOW:    T-479 finished part3 (eras 8, 9, 10). Prose check PASS.
NEXT:   T-481 part1 and T-482 part2 in parallel

## Units
| part | eras | fixer | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|---|
| part1 | 1-5 | T-481 | DONE | 96 / 1 / 0 of 97, +12 found by fixer (era 1: 9/0/0; era 2: 12/0/0 +2; era 3: 26/1/0 +4; era 4: 25/0/0 +4; era 5: 24/0/0 +2) | 8548 -> 9259 |
| part2 | 6-7 | T-482 | DONE | 95 / 2 / 0 of 97, +25 found by fixer (era 6: 48/2/0 +10; era 7: 47/0/0 +15) | 10207 -> 11253 |
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
- 2026-10-02 T-481 era 1: 9 findings judged, 9 FIXED (wampum records "agreements and history", not "law"; Onondaga Keeper attributed; Indigenous glossed; row 9 institution-as-speaker handled file-wide, era by era). Scratch: scratchpad/T-481 (verdicts.py + apply.py). validate 0 errors, punct 0/0.
- 2026-10-02 T-481 era 2: 12 findings judged, 12 FIXED. Encyclopedia Virginia re-read: Paquiquineo was never called guide or interpreter (cut); the three killed were Father Quiros and two Brothers, not three priests (corrected). PATCH (T-481): Paquiquineo and the 1570 mission. validate 0 errors, punct 0/0.
- 2026-10-02 T-482 era 6: 50 findings judged, 48 FIXED, 2 REJECTED (Prussia gloss is a definition; Beecher 452 is dated, the 600 has no named source). Line 144 "were whipped" rewritten state by state; Civilization Fund extinction wording restored; Nat Turner sourced (Walker kept as title and date only, no gloss); Philadelphia riots and Gallaudet sourced. The bank PATCH line "in every state ... faced the whip" (T-261b, Who was punished) is wrong in the same way; left for the audit. PATCHes (T-482): Philadelphia 1844; Gallaudet 1815; Nat Turner copied from slavery-freedom. Scratch: scratchpad/T-482 (verdicts.py + apply.py). validate 0 errors, punct 0/0.
- 2026-10-02 T-481 era 3: 27 findings judged (26 FIXED, 1 REJECTED: Caleb Cheeshahteaumuck was the first Native American Harvard graduate, Harvard Gazette). Deer Island now 'taken ... and held there as prisoners', 'starved and froze'; Wadsworth House four 'were enslaved'; Capital Lawes glossed as the colony's list of crimes punished by death. PATCHes (T-481): Capital Laws; Cheeshahteaumuck first graduate; King Philip's War and NPS Deer Island re-read (SEARCHED, NOT FOUND for the sellers). +4 found by fixer. validate 0 errors, punct 0/0.
- 2026-10-02 T-481 era 4: 25 findings judged, 25 FIXED. Dock 'how he punished children and how he rewarded them'; Harry and Andrew 'the Society owned Harry and Andrew as slaves' (Woodson 1915); Brafferton boys' fate as forced laborers restored. AUDIT-QUEUE Stono gloss (T-328a) now sourced from slavery-freedom bank and told with the same harms (#36). 'Historians explain' (forged pass) had no named historian: replaced by the act's own reason and Burwell's 1774 ad. PATCH (T-481): Stono and the forged-pass reason. +4 found by fixer. validate 0 errors, punct 0/0.
- 2026-10-02 T-482 era 7: 47 findings judged, 47 FIXED (row 97 kept the Zitkala-Sa correction, fact first). Plessy described (train cars); Cumming no longer said to uphold separate schools; Klan gloss sourced; Carlisle labor named forced work, remains restored, 1893 ages restored; boarding-school span now closes on languages kept in secret and friendships across nations, as native-nations does (#36). PATCH (T-482): four era-7 facts copied from slavery-freedom, rights-movements and native-nations. Round 2 (light): a dictionary or period source for 'grammar school, the school that came after primary school'. validate 0 errors, punct 0/0.
- Final T-482: `python tools/project_state.py --check education --stage prose` -> PASS (manuscript 44146w, validator 0 errors, emdash 0, semicolon 0). Part2 words 10207 -> 11253 (raw word count, markers included).
- 2026-10-02 T-481 era 5: 24 findings judged, 24 FIXED. 'First public money for American schools' was false (the 1647 law came first): now 'In 1785 the members of Congress set aside land to pay for public schools, and that land had been taken from Native nations.' Era summary's unsourced 'several plans ... almost all turned down' replaced by the bank's claim and Jefferson's plan; zoom label 'The first schools for girls with charters' changed to "Girls' academies, and the first with a charter" (plural unsupported); unsourced 'teaching was not yet a career' cut. Unnamed 'Historians still argue' (era 2) reworded to the record. PATCH (T-481): Occom was Wheelock's pupil (Dartmouth & Slavery Project). validate 0 errors, punct 0/0.
- Final T-481: `python tools/project_state.py --check education --stage prose` -> PASS (manuscript 44148w, validator 0 errors, emdash 0, semicolon 0). Part1 words 8548 -> 9259 (raw word count, markers included). NEEDS-RESEARCH from part1: none.
