# CHECKPOINT T-682 | health | readability (second edition) | eras 1-10, opening and closing

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check health --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md)
MODEL:  opus
FILES:  manuscript/health/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md · research/research-health.md (PATCH only)

NOW:    done; report sent
NEXT:   nothing; the director checks and commits

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 0 | chapter opening | landed | card 110 min (recheck at end), spine, Onesimus anchor, turn, 3 questions, five minutes, can skip |
| 1 | era 01 before-1500 | landed | strip; through-line first para; label 'What do the bones show?'; 3 paras split; 6 scholar names demoted to roles; Not known line for the 1492 population |
| 2 | era 02 1500s | landed | strip; first para leads with the three witnesses; 1 bold lead-in; Harriot box hook, split, resume cut |
| 3 | era 03 1600s | landed | strip; through-line; 4 paras split; date-first openings moved; Fuller and Jonas boxes hooked |
| 4 | era 04 1700-1750 | landed | strip; inoculation defined in the first para; Onesimus, Boylston, Phillips boxes hooked; Phillips reshaped round the gravestone |
| 5 | era 05 1750-1800 | landed | strip; Caesar, Rush, Jones and Allen hooked; Fort Pitt split with The blankets / The letters lead-ins and a Known / Not known pair; Doctors' Riot label turned into a question, split |
| 6 | era 06 1800-1850 | landed | strip; through-line 'neither one reached everybody'; summary split in 3; 9 paras split; lead-ins The test / The steamboat / The cleanup / No drug for the pain / The babies; Anarcha and Blackwell hooked; 2,382 words so no closer |
| 7 | era 07 1850-1900 | landed | strip; through-line on dirty water, streets and hands; Barton, Ropes, Picotte hooked; glosses folded (contraband, pestilence); Mahoney span reordered to lead with her |
| 8 | era 08 1900-1950 | landed | strip 20 min; through-line on penicillin and the withheld cure; summary in 3 paras; By 1920 line at the radium span; closer By 1950 (three bullets); Tuskegee span split into 13 paras with lead-ins; Maass, Brown, Pollard hooked; radium lawsuit cut to a callback; Hawks Nest callback |
| 9 | era 09 1950-2000 | landed | strip 24 min; By 1955 and By 1965 lines; closer By 2000 (before/after pair); 14 paras split; lead-ins; Lacks, Salk, Alexander, Relf, White hooked; glosses folded (patent, cripple) |
| 10 | era 10 2000-today | landed | strip 9 min; through-line; 5 paras split; Lindsay hooked; glosses folded (defrauded, rubber stamp) |
| 11 | chapter closing | landed | three answers, what changed, five dates, Not known, Where to go (Phipps Street), Next: Chapter 27 |
| 12 | self-review, back-matter hand-off | landed | control/backmatter/health.md written; --check PASS |

## SUBJECT NOTES (decided before writing)

**Spine:** For most of American history nobody knew what caused disease, and after doctors learned
how to stop it, people with the least power were often the last to be protected and the first to be
tested on.

**Three questions:**
1. Why did new diseases kill so many Native people after 1492?
2. How did Americans learn to stop smallpox, yellow fever and polio?
3. Who was used in medical experiments without agreeing, and what changed because of it?

**Anchor:** Onesimus's scar (1716 letter from Cotton Mather to the Royal Society): the African man
Mather enslaved showed the scar of the "Operation" that would "forever preserve him" from smallpox.
All in era 04's Onesimus box.

**Five minutes?** "The Tuskegee study, 1932 to 1972" in 1900 to 1950.

**Can skip:** "Midwives and surgeons in New Amsterdam", "Medical care for sailors, 1798", "New
operations and new pictures of the body, 1954 to 1963".

**Where to go:** Elizabeth Phillips's gravestone, Phipps Street Burying Ground, Charlestown, MA.

**Next:** Chapter 27, Disasters and Rescue.

**Measured before (measure_readability.py):** 20,820 words, 315 paras, avg 66.1, 54 over 90 words,
28.3% date-first, def 1.3/1k, attr 5.8/1k, also 1.4/1k, "you" 3, longest era 4,682, 1 era over
4,000, 23 stories, median 221, 0 over 400.

**Era sizes before:** 860 / 1183 / 2050 / 1310 / 2000 / 2428 / 1709 / 3963 / 4682 / 1698.

**Furniture plan:** strips in all ten eras. "By" lines: era 08 (one, maybe two, as it passes 4,000)
and era 09 (two). Closers: eras 08 and 09; era 06 only if it ends over 2,500 words; any other era
that ends over 2,500. Opening in era 01, closing at the end of era 10.

**Cross-chapter repeats (ARCHITECTURE §5.12):** the Radium dial painters and Eben Byers are told in
full in Chapter 13 (Elements) and Chapter 14 (Work and Workers); Hawks Nest in full in Chapter 14.
Plan: keep health's body angle, cut the radium lawsuit paragraph to a callback with its outcome, add
a callback to Hawks Nest. Fort Pitt (Chapter 22) and Henrietta Lacks (Chapter 9) stay: disease as a
weapon and consent are this chapter's subject. Tuskegee: this chapter owns it.

**Repeated definitions to cut to once per chapter:** smallpox (1600s, 1800-1850), yellow fever
(1600s, 1850-1900, 1900-1950), bacteria and germ (several), bloodletting (Fuller box, 1849 cholera),
shock (1793, 1846), tuberculosis (before-1500, 1928), scurvy (1620, Civil War), vaccine (1918),
syphilis family, sterilization (1937 full; 1970s may re-gloss once, it names the two operations).

## Sources in hand

None needed so far: furniture restates the chapter.

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

## Cuts (each with its reason)

- era 01: dropped the names of six scholars behind numbers (Bartlett, Black, Lallo, Barquera, Steward/Dobyns/Ubelaker/Denevan kept as dated estimates without names). Reason: ARCHITECTURE 5.4, thirteen proper nouns in 860 words; the facts and dates stay, the bank holds the names.
- era 01: dropped "a team of scientists reported in 2022" on the tuberculosis skeletons. Reason: attribution of an uncontested finding (5.6).
- era 02 Harriot box: cut "born in about 1560", "finished his studies at Oxford University in 1580" and "He died in 1621". Reason: resume lines (4.8); the scene stays.
- era 03 Fuller box: cut "He was baptized in 1580 in Norfolk, England." Reason: resume line.
- era 03 yellow fever: dropped "led by Juliet Bryant" (kept "a team of scientists reported in 2007").
- era 06: cut the second definitions of smallpox (virus, rash, 3 in 10 died), cowpox (kept in the era's first paragraph), germ, bloodletting (how a vein was cut) and shock. Reason: guideline 7 as reworded, explained once in era 03 to 05.
- era 07: cut the second definitions of scurvy, germs and yellow fever. Reason: same.
- era 08 radium: cut "Judge William Clark worked out an agreement" and the names of four of the five women (Schaub, Hussman, Larice, McDonald) to a callback to Chapter 13, which tells the lawsuit in full. Kept: Grace Fryer, the date, the money, the pension, medical costs, no admission of blame, and all the harm to the body (ARCHITECTURE 5.12).
- era 08 1918 flu: cut the span's "A navy nurse in Illinois later described patients with nosebleeds..." because the Josie Mabel Brown box tells the same thing in her own words.
- era 08 Brown box: cut "Brown was born on a farm in southwestern Missouri in 1886" (resume line, still in the When and where line).
- eras 08 to 10: cut second definitions (yellow fever kept once inline, pneumonia, tuberculosis kept as one clause, typhoid kept as one clause).

## Decisions (what I chose not to do)

- Story boxes: all 23 got a hook; none was over 400 words, so none was trimmed for length. Record lines left as they were.
- Fort Pitt (Chapter 22 tells it) and Henrietta Lacks (Chapter 9 tells it) kept in full: disease as a weapon and consent are this chapter's subject.
- Attribution stays at 5.6 per 1,000: what remains are contested counts (Carey, Downs, Caulfield), witnesses (Percy, Bradford, Chardon) and findings people dispute (JSTOR Daily on Flexner, NCpedia on the Cherokee route, DIG on Puerto Rico).
- Eras 01 to 07 got no closer and no By lines (all under 2,500 words). Era 06 ended at 2,382.

## Log

- 2026-10-27 | opening + eras 01-05 (part1) | landed | validator 0 errors | --punct 0/0
- 2026-10-27 | eras 06-07 (part2) | landed | validator 0 errors | --punct 0/0
- 2026-10-27 | eras 08-10 + closing (part3) | landed | validator 0 errors | --punct 0/0
- 2026-10-27 | back-matter hand-off | control/backmatter/health.md | --check health --stage prose PASS
- measured after: 22,050 words, 427 paras, avg 51.6, 9 over 90 (all are furniture lists or the summary/opening blocks), date-first 0.2%, def 0.5/1k, attr 5.6/1k, also 1.3/1k, you 5, longest era 4,962, 2 eras over 4,000 (both carry By lines), 23 stories, median 228, 0 over 400
