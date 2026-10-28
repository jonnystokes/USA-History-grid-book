# CHECKPOINT T-713 | education (Chapter 30) | review fix pass for R19

STATUS: DONE (all 25 findings handled; --check education --stage prose PASS)
BRIEF:  control/briefs/REVIEW-FIX.md
REVIEW: control/review/R19.md (25 findings for education, plus a Flow note)
FILES:  manuscript/education/part1-before-1800.md, part2-1800s.md, part3-1900s-and-today.md,
        control/backmatter/education.md
VERIFY: python tools/project_state.py --check education --stage prose
BASELINE (before any edit): PASS, validator 0 errors on all three parts, --punct 0/0 on all three.

## Findings (numbered in the order of R19.md)

| # | era | finding (first words) | state | note |
|---|-----|-----------------------|-------|------|
| 1 | closing | "Horace Mann argued for free schools" | fixed | Q1 "came in steps, not on one date" (no date for general free schooling in the bank); Q2 adds Native children, courts both ways (Roberts, Plessy, Lum / Mendez, Brown, Mills), the two 1975 laws; back matter in step |
| 2 | 1850 to 1900 | "The mayor read out the Virginia" | fixed | mayor's figures credited to Douglass's account and set against the 1831 law; opener no longer calls it the 1831 law (bank does not say which law he read) |
| 3 | 1850 to 1900 | "Alvord's count for the half year" | fixed | kept 1,094, 210,018, one million; cut schools, teachers, buildings, month and subject counts |
| 4 | 1950 to 2000 | "In much of the Southwest, school" | fixed | opens with the hearing and the slip, then the children's words; survey cut to two sentences after them; enforcement percentages cut |
| 5 | 1750 to 1800 | "Ann Wager taught every class the" | fixed | God's-will point once in the section (with the W&M quote), cut from era intro and box; box keeps widowhood, pay, rent, death date, Isaac Bee; irony line cut. The chapter-opening anchor keeps it (furniture) |
| 6 | 1700 to 1750 | "In 1774 Lewis Burwell advertised for" | fixed | 1740 section: enslavers feared forged passes, one unnamed 1774 ad as evidence; Isaac Bee and the quote only in the Wager box, which points back to the opening |
| 7 | 1850 to 1900 | "Officials of the US Department of" | fixed | full count once (2000 to Today, with 74 sites and both "too low" statements); 1850-1900 pointer (417, at least 973); 1900-1950 pointer without numbers; monument told once in 2000 to Today; closer bullet and closing Not known kept (furniture) |
| 8 | 1850 to 1900, 2000 to Today | "By 1899: Southern lawmakers had written" | fixed | era 7: 1870, 1899, 1900; era 8: "By 1948" moved to the end of the camps span as "By 1945" (spans cannot move, so the line moved); era 10: 2023, 2024, 2025 |
| 9 | 1950 to 2000 | "One question left open: Would the" | fixed | 43 percent now in the era-9 Brown span; era-10 separation span opens with the plain answer (43 to 16); kept one national measure beside it and the enrolment change, cut the GAO and 2017 series; era-10 one-thing rewritten; era-6 bullets now include the 1837 Mann line |
| 10 | 1900 to 1950 | "The federal government's own figures show" | fixed | high-school span cut to 6/half, 29 to 51, the Depression reason, days 178/158/99; one-room counts rounded, buses in one sentence; literacy counts and 1838 wages trimmed |
| 11 | 2000 to Today | "The same survey shows which children" | fixed | finding stated in words, five pairs in a short list, cut in-school, expulsion, Black girls, police-referral figures; college, disabled-child, homeschool and separation walls trimmed |
| 12 | The 1600s | "When one classmate did not know" | fixed | warning restated plainly, then the events in order; "the other boy" now "the classmate" throughout |
| 13 | 1850 to 1900 | "They flogged children, beating them with" | fixed | flogging defined without tools, report's silence on difference and tools stated; list kept in 1850-1900 only, pointer from 2000 to Today; Collier gloss and glossary made the same |
| 14 | 1950 to 2000 | "Of the Southern cities counted, the" | fixed | two cities (Mobile, Charlotte), Kansas City dropped; second Catholic figure dropped; By-line now "By 1991" with 2,400 magnet schools |
| 15 | The 1600s and later | "Caleb Cheeshahteaumuck was the first Native" | fixed | Caleb box starts at his letter; Mann box at his boyhood; Dewey box drops the retold date; seven Mills names trimmed to three, box drops the retold filing |
| 16 | 1900 to 1950 | "Justice Oliver Wendell Holmes Jr. wrote" | fixed (part) | plain restatement added; Carrie (second) and Vivian (third) named; the first generation is not in the bank, so not named |
| 17 | 1800 to 1850 | "Georgia's lawmakers passed their law in" | fixed | Virginia in one place; other four states one line each; South Carolina's widening stated; Walker/Turner reduced to one accurate sentence ("most followed Turner" is false per the bank's T-485 note) |
| 18 | several | "Her book about Bridgman, built mostly" | fixed (part) | Swift book, missions order, Hartford sources, blind school 1829/1832 with Howe's father, Cumming request, Mendez hook; Webster sentence clarified but no spelling example: none in the bank |
| 19 | 1900 to 1950 | "A court fight over religious teaching" | fixed (part) | timing sentence replaced by the 1962 link; what was taught is not in the bank; heading is a marker line and stays |
| 20 | 1900 to 1950 and later | "Members of a joint committee of" | fixed (part) | hearing money cut to one clause with the Warner testimony (gives his leaving a context); New London led by the board's choice, count made plain, pointer to Chapter 27; Evers linked to Meredith; tablets paragraph moved to the 2020 span; Sputnik span not moved (ARCHITECTURE-GUIDE §2: no span moves), Virginia span now links back to Faubus instead |
| 21 | The 1600s, 1800 to 1850 | "The word dunce comes from the" | fixed | spare-the-rod cut to two sentences, Duns Scotus paragraph cut |
| 22 | The 1500s | "Pedro Menéndez de Avilés and about" | fixed | Florida span opens with Pareja; founding one sentence (kept Seloy's town and enslaved Africans); why-line under the hook; travel stops and the three family names trimmed |
| 23 | several | "College leaders began to admit women" | fixed | women's colleges, Boston land, Primer, Carlisle approval, normal schools, Prince Edward, Minnesota charter, Mamie Garvin Fields school names all trimmed (bank forbids a Fields scene, so the box stays biographical) |
| 24 | Before 1500 | "No writing system was in use" | fixed | syllabary "invented", Sequoyah named, priests' and ministers' alphabet sentence; Great Law overlap explained but not merged into one range (bank: oral tradition starts about 1000, "do not pick one") |
| 25 | card and later | "School in America grew from a" | fixed | spine split; Scopes fact moved to the front; stones attached; Bray irony cut; Nation at Risk aside now history; three-part line kept only in the era-10 intro |

## Cuts (DECISIONS #52), each because it was a repeat, a tangent or a number wall
Chickataubut and the 75,000/100,000 figures; Primer advertisement history; Ælfric and the Hudibras dates; Seloy's council-house fort and the 26 women; Paquiquineo's travel dates and three family names; Lockridge middle data points; Bray curriculum paragraph and Wager-box retelling; 1838 Connecticut and Pennsylvania wage figures; Duns Scotus; Alvord's school, teacher, building, month and subject counts; Wilkinson, Stockwell, Cornell 1872, opening dates and class sizes of three women's colleges; Baird, Schurz, McCrary; normal schools state by state; high-school graduate and enrolment counts, war and girls figures; one-room and bus seven-digit counts; Carlisle football fund figures, buildings, Friedman's train tickets; Kansas City and four other city figures; 13,292; Bruce, Fitzpatrick, Longwood, the 25 against; 1960 college enrolment; Minnesota bill history, Carlson, Bluffview, 1993 limit; four of the seven Mills children by name, two Mills counts; special-education raw counts; homeschool 2012 and online figures, fourth reason, private/public shares; GAO and 2017 separation series, Black and Latino 1968 shares; discipline pairs beyond five; 2000-to-Today repeat of the punishment list.

## Log

<!-- file | what landed | validator | --punct -->
- part1 | F5, F6, F10 (literacy), F12, F15 (Caleb), F18 (missions, Webster), F21 (rod), F22, F23 (Boston, Primer), F24, F25 (spine, Bray irony); era-3 strip 12 to 11 | 0 errors | 0/0
- part2 | F2, F3, F7, F8 (era 7), F9 (era-6 closer), F10 (wages), F13, F15 (Mann), F17, F18 (Swift, Hartford, blind school, Cumming), F21 (dunce), F23 (colleges, Carlisle approval, normal schools), F25 (stones) | 0 errors | 0/0
- part3 | F1, F4, F7 (pointers, full count, monument), F8 (eras 8 and 10), F9, F10 (high school, one-room), F11, F13 (Collier gloss, pointer), F14, F15 (Dewey, Mills), F16, F18 (Mendez hook), F19, F20, F23 (Fields, Prince Edward, charter), F25 (Scopes, Nation at Risk, three-part line); strips era 9 52 to 51, era 10 38 to 37 | 0 errors | 0/0
- backmatter | Q1 and Q2 answers match the closing word for word; glossary: spareth/hateth removed, flogging re-defined, national monument moved to 2000 to Today | n/a | 0/0
- final | python tools/project_state.py --check education --stage prose: PASS (46139w, validator 0 errors, 0 em dashes, 0 semicolons)
