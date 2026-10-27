# CHECKPOINT T-673 | rights-movements | readability (second edition) | all ten eras

STATUS: IN-FLIGHT            (agent finished; director sets DONE)
VERIFY: python tools/project_state.py --check rights-movements --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md)
MODEL:  opus
FILES:  manuscript/rights-movements/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md · research/research-rights-movements.md (PATCH only if needed)

NOW:    done; reported
NEXT:   carry on with the first unit whose state is not "landed". Each era is rewritten whole in
        scratch and applied with the scratch script apply_era.py (it checks that every hb-time and
        hb-story marker line is unchanged and the span count is unchanged, and fills {MIN} in the strip).

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 0 | chapter opening | landed | spine, Germantown anchor, turn, 3 questions, five minutes, can skip; reading time 275 minutes (55,480 / 200, rounded to 5) |
| 1 | era 01 before-1500 | landed | strip; summary leads with through-line; clan-mother span split in 6 paras with 2 lead-ins; Not known line |
| 2 | era 02 1500s | landed | strip; label "What was the encomienda?"; glosses folded into sentences; Las Casas span split into 10 paras, 3 lead-ins |
| 3 | era 03 1600s | landed | strip; Hutchinson box reshaped (hook, 4 lead-ins, ~620 w: trial scene plus Kieft massacre context kept); Quaker span split 4 -> 12 paras |
| 4 | era 04 1700-1750 | landed | strip; Lay paras split, lead-ins; no date-first paras |
| 5 | era 05 1750-1800 | landed | strip; Adams box reshaped (hook from both letters; long quote split; ~720 w, the three letters are the story); NJ span split 4 -> 8. Era under 2,500 so no closer (one was drafted and removed) |
| 6 | era 06 1800-1850 | landed | strip; summary leads with through-line; 2 "By" lines (1834, 1843); closer "By 1850" (bullets); Crandall, Grimké, Dix, Stanton-Mott boxes reshaped with hooks and lead-ins (Crandall ~760 w and Stanton-Mott ~700 w: scene chains, long for that reason); mobs span split 6 -> 13 paras |
| 7 | era 07 1850-1900 | landed | strip; 4 "By" lines (1870, 1875, 1879, 1887); closer "By 1900" (one number: 728); label "Why the women's movement split in 1869"; all 5 boxes hooked (Anthony ~1,000 w, Wells ~1,000 w, Winnemucca ~900 w, Tape ~780 w: courtroom and lynching scenes and Mary Tape's letter kept whole, hard-subjects policy); Wilmington count as Known / Disputed |
| 8 | era 08 1900-1950 | landed | strip; summary split in 3 paras, leads with the methods; 6 "By" lines (1918, 1920, 1925, 1929, 1935, 1941); closer "By 1950" (before/after pair); labels "Tulsa, June 1, 1921: ...", "Could a school turn a disabled child away?"; Elaine and Tulsa death counts as Disputed lines; Gaines box ends Known / Not known; 7 boxes hooked (Carrie Buck ~800 w: the rigged case and the operation stated in full, hard-subjects policy) |
| 9 | era 09 1950-2000 | landed | strip; summary split in 3 paras; 4 "By" lines (1956, 1962, 1964, 1974); closer "By 2000" (one open question, answered in era 10: the Voting Rights Act); labels "Brown v. Board of Education, May 17, 1954", "The March on Washington, August 28, 1963", "What did Title IX change?"; King killing as a Disputed line; 5 boxes hooked (Parks-King ~880 w and Hamer ~900 w: two lives and a beating told from her testimony, long for that reason) |
| 10 | era 10 2000-today | landed | strip; summary split in 4 paras with lead-ins; 4 "By" lines (2015, 2021, 2022, September 2026); no era closer (the chapter closing is the last block, as in the pilot); label "Minneapolis, May 25, 2020"; Burke dates as a Disputed line; "Today." line with the 45.8 million count; 3 boxes hooked |
| 11 | chapter closing | landed | 3 questions answered word for word; what changed; five dates; Not known (Tulsa dead); Where to go (Haverford College); Next: Chapter 26 |
| 12 | back-matter hand-off control/backmatter/rights-movements.md | landed | 6 sections, 373 bullets |

## SUBJECT NOTES

**Measured before (measure_readability.py):** 54,849 words, 628 paragraphs, average 87.3 words,
262 over 90, 25.0% date-first, def/1k 2.4, attr/1k 6.9, also/1k 0.9, "you" 49 (all in quotes),
longest era 12,863 (1900-1950), 5 eras over 4,000, 26 stories, median 683, 21 over 400.
Era words: 677 / 975 / 2,229 / 954 / 2,366 / 4,954 / 10,319 / 12,863 / 10,990 / 9,818.

**Spine:** Most of the rights Americans have today were won by people who were first refused them,
organized, and kept asking for years, often at the cost of their jobs, their freedom or their
lives, and some of those rights were later narrowed or taken back.

**Three questions (word for word in opening and closing):**
1. How did people without power get the people in power to listen?
2. What did organizing cost the people who did it?
3. Can a right that has been won be taken away again?

**Anchor:** the Germantown protest of April 18, 1688: four men sign it, four Quaker meetings pass
it on without acting, it is forgotten, found in 1844, lost again, found in a vault at the Arch
Street Meetinghouse in March 2005, now kept at Haverford College. (Era 3.)

**Five minutes?** "Sit-ins and Freedom Rides, 1960 and 1961" in 1950 to 2000.
**Can skip:** "Two men climb the Gateway Arch, 1964", "Suffragists remember the clan mothers,
1891 and 1893", "Equal pay for the women's soccer team, 2016 to 2022". (Labels kept as is.)

**Furniture plan:** strips in all ten eras. "By" lines: era 6 (2), era 7 (4), era 8 (5 to 6),
era 9 (5), era 10 (4). Closers: eras 6 to 10 (over 2,500 words); eras 1 to 5 get the strip only
unless an era passes 2,500 words. Closer middles rotate: bullets / before-after / one number /
one open question answered in the next era.

**Where to go:** Haverford College, Pennsylvania, which keeps the 1688 Germantown protest.
**Next:** Chapter 26, Health, Disease, and Medicine.

**Glosses (once per chapter, inside the sentence):** petition, coverture, Quaker, abolitionist,
convention, suffrage, lynching, segregation, amendment / ratify, union, habeas corpus, NAACP
"colored", "Negro" (period word, re-glossed once later at most), sterilization (full clinical
explanation at Carrie Buck / eugenics span; hysterectomy and tubal ligation keep theirs).

## Cuts (every one, with the reason)

<!-- era | what | why -->
- era 1 | the era summary's second retelling of the clan mother's powers | the span tells it in full; summary now names it in one clause
- era 1 | repeated definitions of clan and wampum | kept once each
- era 2 | standalone gloss sentences (exploitive, feudal, Indigenous, dehumanizing) | folded into the sentence (guideline 7)
- era 3 | Hutchinson box: born about 1591 at Alford; the ship *Griffin*; following John Cotton | résumé, not scene (ARCHITECTURE-GUIDE §4.8)
- era 3 | Hutchinson box: opening summary paragraph that repeated the trial | replaced by the hook; the trial is told once
- era 5 | Adams box: the opening summary paragraph | replaced by the hook built from her letter and his answer
- era 6 | Stanton-Mott box: Mott's birth on Nantucket, 1793, Nine Partners school; Stanton's birth date | résumé
- era 6 | Grimké box: the sisters' birth dates | résumé
- era 6 | Crandall box: opening summary paragraph | replaced by the hook (Harris's own words)
- era 7 | Winnemucca box: born 1844 in what became Nevada (kept in When and where) and the opening summary paragraph | résumé, hook
- era 7 | Wells box: parents' names James and Lizzie Wells | résumé
- era 7 | Sojourner Truth box: opening summary paragraph | replaced by the hook
- era 7 | Tape box: "the judges held that separate schools were lawful" folded into the next sentence | same fact, one sentence
- era 8 | Alice Paul box: Swarthmore 1905, master's 1907 (doctorate kept); opening summary paragraph | résumé, hook
- era 8 | Gaines box: born 1911 at Water Valley, mother Callie, Vashon High School, Stowe Teachers College | résumé (father kept; "one of eleven children" restates "ten brothers and sisters")
- era 8 | Korematsu box: father's arrival 1905, mother through Angel Island 1914, three brothers | résumé
- era 8 | Randolph box: born April 15, 1889, Crescent City; opening summary paragraph | résumé, hook
- era 8 | sit-in 1935 span: the member's quote trimmed from about 50 words to two pieces under 25 ("What started it was finding out that jobs were available, that the government was handing out jobs" dropped) | body quotation limit, §5.10; the point of the quote is kept
- era 9 | Barbara Johns box: born in New York City, March 6, 1935; the standalone definition of strike | résumé; "stayed out of class" carries the meaning
- era 9 | Parks-King box: Parks born Tuskegee February 4, 1913, married 1932, "secretary from 1943 to 1956" (kept as "twelve years") | résumé
- era 9 | Hamer box: born Montgomery County, Mississippi, October 6, 1917 | résumé
- era 9 | Heumann box: born Philadelphia, December 18, 1947 | résumé
- era 9 | Rustin box: opening summary paragraph | replaced by the hook (the pardon)
- era 10 | Darnella Frazier citation: "highlighting the crucial role of citizens in journalists' quest for truth and justice" | body quotation limit, §5.10
- era 10 | Burke box: born September 12, 1973 | résumé (the Bronx kept)
- all eras | standalone gloss sentences ("X means Y.") after quotes | folded into the sentence, about 30 (guideline 7); "rape" keeps its own sentence (DECISIONS #31)
- all eras | 73 paragraphs over 90 words split at the sentence nearest the middle (scratch split.py, reviewed); two that came out date-first reworded
- era 5 | Adams box: Blackstone's "or at least is incorporated and consolidated into that of the husband" | the plain sentence after the quote states it

## Decisions and defects fixed

- Date style changed to month-day-year throughout (ARCHITECTURE-GUIDE §5.13). No date changed.
- Rule broken on purpose: Lucy Burns's forced-feeding log (about 80 words) and her Night of Terror entry stay whole in the Silent Sentinels span, over the 25-word body limit (§5.10). It is the victim's own account of what was done to her body (hard-subjects policy §3, floor), and the span cannot move into a story box. Legal texts quoted in spans (amendments, Title IX, Section 504) also keep their full sentence.
- Cross-chapter repetition (§5.12): not cut. Checking 24 earlier chapters for full tellings of
  Brown, Plessy, the Dawes Act and the camps was outside this task's reading; noted for the director.

## Log

<!-- date-time | unit | what landed | validator | --punct -->
- 2026-10-27 | opening + eras 1-5 (part1) | landed | 0 errors | 0/0
- 2026-10-27 | eras 6-7 (part2) | landed | 0 errors | 0/0
- 2026-10-27 | era 8 (part3) | landed | 0 errors | 0/0
- 2026-10-27 | era 9 (part3) | landed | 0 errors | 0/0
- 2026-10-27 | era 10 + closing (part3), paragraph splits, gloss folds, era first sentences varied | landed | 0 errors x3 | 0/0 x3
- 2026-10-27 | --check rights-movements --stage prose | PASS
- After: 55,480 words, 962 paras, avg 57.7, 8 over 90, 0.6% date-first, def/1k 0.6, attr/1k 6.9, 26 stories, median 624, 19 over 400
