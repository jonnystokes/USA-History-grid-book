# CHECKPOINT T-261 | education | bankcheck | T-261a: eras 1-5

STATUS: T-261c landed (director verified: PASS  education / research)
VERIFY: python tools/project_state.py --check education --stage research
BRIEF:  control/briefs/RESEARCH.md, MODE bankcheck
MODEL:  opus
FILES:  outlines/education.md · research/research-education.md · workspace/education.md

NOW:    T-261c done (units 8-10). Validator 0 errors. Research check PASS, bank 70,528w, outline 30,013w.
NEXT:   T-261d (era 9, 1950-2000): run the brief's five Find items on era 9 only (`python tools/slice_bank.py education --eras 9-9`). Eras 1-8 are finished; do not change them. Carry-forwards: the era-9 outline still holds em dashes and semicolons (`python tools/project_state.py --punct outlines/education.md` lists them, lines ~831-1000 are era 9); boarding-school enrolment peak ~60,000 in 1973 and the Kennedy Report 1969 are in PART B; Daniel Freeman's 1902 Nebraska school-prayer case is in PART C-FWD (era 9 decides whether to use it); Buck v. Bell law on the books to April 1974 (PART D-FWD); Delgado's language-test loophole ran to Hernandez v. Driscoll 1957 (era 8 T-261c Delgado patch); Rhoads's 1930 punishment circular is unsettled (era 8 T-261c boarding patch, item 4).

## PARALLEL RUN (Jon, 2026-09-27): ten agents at once

Ten agents run at the same time, one chapter each (T-257 to T-266). **Write only your own
chapter's outline, research bank, workspace file and this checkpoint.** Do NOT edit any other
chapter's files, even to park material: list it under "TO PARK" below (target chapter, era, the
sourced text). The director files it after the batch. Reading other chapters' banks is fine.

## Measured before dispatch (2026-09-27)

PASS  education / research
  stage=RESEARCHED eras=10/10 stories=21 (v21 c0 t0) verify_tags=0 bank=56118w outline=26723w manuscript=0w validator_errors=0

**T-261a's job:** Bank check, eras 1-5 only. Later agents do eras 6-10 (a 68,000-word slice).

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | bank check, eras 1-5 (the brief's five Find items, era by era) | done | patches in all five eras, see Log |
| 2 | check each verified story in eras 1-5 has its key facts in the bank | done | bank era 5 'Unit 2 check' patch. Webster 60 million unsourced |
| 3 | final for your eras: validator, research check | done | validator 0 errors, research PASS, bank 61,765w |


## Units, T-261b (eras 6-7)

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 4 | bank check, era 6 (1800-1850): five Find items | done | bank era 6: anti-literacy penalties (Woodson 1915), Noyes Academy 1835, Civilization Fund 1819 and Choctaw Academy, firsts checked, Webster 60 million SOURCED |
| 5 | bank check, era 7 (1850-1900): five Find items | done | bank era 7: Margaret Douglass 1853-54; attacks on freedpeople's schools (Alvord 5th and 9th reports, Encyclopedia of Alabama, William Luke); segregation statutes, Cumming 1899, Plessy on schools; 2022/2024 federal report figures, 1893 rations act, nine named Carlisle children; Morrill land count (HCN) |
| 6 | each verified story in eras 6-7 has its key facts in the bank | done | all 8 blocks match their bank sections; see era-7 'stories and firsts' patch |
| 7 | final for eras 6-7: outline punctuation, validator, research check, NEXT for era 8 | done | outline eras 6-7: new spans (Federal money to school Native children 1819; Northern schools wrecked, Noyes 1835; teacher jailed in Norfolk 1854; Separate schools by law and courts), attacks on freedpeople's schools, Morrill land count, Carlisle named dead and 2024 figures, anti-literacy penalties; 'first time in print' claim removed; CT 1819 'first' attributed; zero em dashes and semicolons in eras 6-7; validator 0 errors; research PASS |

## Units, T-261c (era 8)

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 8 | bank check, era 8 (1900-1950): five Find items | done | bank era 8, 9 T-261c patches: Jones 1917 federal survey ($10.32 vs $2.89; county officers divide the money; $22.22 vs $1.78); Delgado 1948 (TSHA); camp schools 1942-45 (NPS Manzanar, Poston; Munemitsu children; Poston on Colorado River Indian Reservation); attendance laws 1891 VERIFIED (Cohen 1942) and 1920 (41 Stat. 410); Carlisle to War Department 1918; Uintah 1928 Senate hearing (Tilford Denver, Swanson Mowachean named dead; Principal Shafer and whipping); Collier 1930; 2 SEARCHED NOT FOUND; Scopes textbook (Hunter's Civic Biology, eugenics passage, Gutenberg); New London pointer; firsts checked |
| 9 | each verified story in era 8 has its key facts in the bank | done | john-dewey (§8a-8c), mamie-garvin-fields (§8p), sylvia-mendez (§8o): every fact in the blocks matches the bank |
| 10 | final for era 8: outline punctuation, validator, research check, NEXT for era 9 | done | outline era 8: separate-schools span gains the 1917 federal survey figures and the county officers, Lemon Grove 1931 and Delgado 1948; boarding span gains the 1920 attendance law, Carlisle to the War Department, the 1928 Uintah hearing (Tilford Denver, Swanson Mowachean, Principal Shafer and whipping); testing span gains Hunter's Civic Biology and Scopes pointer; new span 'School inside the camps'; 9 semicolons cleared, 0 em dashes and 0 semicolons in era 8; validator 0 errors; research PASS |

## TO PARK (T-261c)

- **native-nations, era 1900-1950: Uintah Boarding School, Whiterocks, Utah, Senate hearing November 1928.** Tilford Denver, 11, killed by an unsecured swing late October 1927; Swanson Mowachean, orphan, died 6 March 1928 after Superintendent H. M. Tidwell delayed hospital care; Principal George N. Shafer told disciplinarian Fred Bruce to whip boys. Source: Salt Lake Tribune, Sheila R. McCann, 9 July 2023, quoting the Senate *Survey of Conditions of the Indians* hearings. Sourced text: `research/research-education.md` era 8, "PATCH 2026-09-27 (T-261c): the boarding schools in this era...", item 3.
- **native-nations, era 1900-1950: Poston camp on the Colorado River Indian Reservation, run by the Office of Indian Affairs for its first year and a half** (Poston Preservation). The tribal council's objection and the 71,000 acres are search-summary only. Education bank era 8, camp-schools patch.
- **native-nations, era 1850-1900 (note for the director): the 1891 compulsory-attendance act is real** (Act of 3 March 1891, 26 Stat. 1014; Cohen, *Handbook of Federal Indian Law*, 1942, ch. 12 §2C), plus the 1892, 1893 and 1894 acts. PART B's line can stand. Education bank era 8, boarding patch item 1.
- **war or rights-movements, era 1900-1950: schools in the incarceration camps** (Manzanar and Poston figures, NPS; more than 30,000 pupils system-wide). Education tells it as a span; nothing to file unless those chapters want a pointer.
- **religion / government-politics / science, era 1900-1950: Hunter's *A Civic Biology* (1914), the Scopes textbook, printed a racial ranking and a eugenics passage** ("If such people were lower animals, we would probably kill them off..."), Gutenberg #39969. Education carries it in its testing span.

## TO PARK (FILED by the director, 2026-09-27)

- **native-nations, era 1800-1850: the Civilization Fund Act (3 March 1819, $10,000 a year, repealed 1873) and the Choctaw Academy, Kentucky, 1825-1848** (Richard M. Johnson's farm, Choctaw treaty money $6,000 a year, 600+ students from 17 nations, 1840 inspection, Pitchlynn withdrew Choctaw students 1842). Sourced text: `research/research-education.md` era 6, "PATCH 2026-09-27 (T-261b): federal schooling of Native children begins in this era" (DOI report Vol I 2022 pp. 27-28; ExploreKYHistory; Penn State on Christina Snyder).
- **native-nations, era 1850-1900: the nine Rosebud Sioux children who died at Carlisle, returned 14 July 2021, and Spotted Tail's request of 23 May 1881** (Proclamation 10870, 2024; DOI report Vol II 2024). Also the 2024 report's figures (417 schools, at least 973 deaths, 18,624 named children, 74 burial sites at 65 schools) and the Act of 3 March 1893 (rations withheld). Sourced text: education bank era 7, "PATCH 2026-09-27 (T-261b): the boarding schools, the two federal reports' figures".
- **slavery-freedom, era 1850-1900: attacks on freedpeople's schools and teachers from Alvord's Fifth (1868) and Ninth (1870) reports** (Gladding and Abram Colby at Greensboro, Georgia; Fisk students whipped at Dresden, Tennessee, 2 Sept 1869; Slaughter Neck, Delaware, school burned; Newberry, SC) and **William Luke, lynched at Cross Plains, Alabama, 11 July 1870** (Encyclopedia of Alabama; Owen Sound Hub; six or eight dead). Education bank era 7, "PATCH ... attacks on the freedpeople's schools".
- **crime-justice, era 1850-1900 (its planned lynching-victim story):** William Luke, as above. Education tells him in two sentences as a teacher.
- **slavery-freedom or rights-movements, era 1850-1900: Margaret Douglass, Norfolk, jailed one month from 10 January 1854** for teaching free Black children (her own 1854 narrative, Gutenberg 70331). Education tells it as a span. Education bank era 7.
- **rights-movements, era 1800-1850: Noyes Academy, Canaan, New Hampshire, dragged off its foundation 10 August 1835** (Colored Conventions Project; Town of Canaan). Education tells it as a span beside a pointer to `prudence-crandall`. Education bank era 6.
- **Director, era 5 of this chapter:** Webster's "about 60 million by 1890" is now sourced (HistoryofInformation; CT Academy of Arts and Sciences) in the education bank era 6 Webster patch. The era-5 block's range can stand. Eras 1-5 were not edited.

## SUBJECT NOTES (from the director)

Registry: School and Education: How people learned — schools, literacy, public education, colleges, reforms. Not: school desegregation as a campaign (`rights-movements`)

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the bank and
the neighbouring chapters' banks first): DECISIONS #4: a named beaten child only if a source supports one. DECISIONS #9: Ruby Bridges is this chapter's. Laws that made teaching enslaved people a crime · boarding schools (who ran them, deaths with the 2022 and 2024 federal report figures) · segregated schools and who enforced them · corporal punishment counts today, dated.

Stories: every target or candidate in your eras must become a real, named, documented person the
bank sources, or be handled honestly (never invent a name; an unnamed documented account becomes
hb-zoom prose, and the hb-story block is removed). Search `outlines/` and `manuscript/` so no
other chapter already tells the person (ignore `outlines/BOOK-OUTLINE.md`). Keep slugs unique.

Perishable: every 2000-today figure is dated and refreshed to 2026.

## PARKED EARLIER (FILED by the director, 2026-09-27)

- **native-nations, era 1600s: Deer Island, 1675-76.** No outline in the book tells it. Sourced text is in `research/research-education.md` era 3, "PATCH 2026-09-27 (T-261a): what happened to the people of the praying towns in 1675 (Deer Island)": order 13 Oct 1675 by Massachusetts authorities, Natick people ferried 30 Oct 1675, about 500 to 1,100 interned, mostly women and children (NPS, https://www.nps.gov/places/deer-island.htm), more than half died over the winter (historicbostons.org), survivors released May 1676, an unknown number sold into slavery in the West Indies or Tangier (NPS).
- **native-nations, eras 1500s-1700-1750: the Timucua.** 200,000 in the 1500s to about 2,000 by the 1650s, epidemics, Carolina slave raids, all survivors taken to Cuba after 1763, last died 1767 (Matthew Holt Jennings, Dictionary of American History, https://www.encyclopedia.com/history/dictionaries-thesauruses-pictures-and-press-releases/timucua). Also the 1572 Spanish hanging of Paquiquineo's people (Encyclopedia Virginia). Copy from the education bank era 2 patch.

## Sources in hand

- Bartleby, Trent and Wells, *Colonial Prose and Poetry*, John Barnard extract (curl works, WebFetch 403). NPS Deer Island page. Encyclopedia Virginia (Paquiquineo, W&M slavery, 1774 Gazette ad). W&M Historic Campus Brafferton page; W&M Bray School scholar names. Woodson 1915 at Gutenberg. Ohio Lands Book PDF (Knepper). Dartmouth Occom Circle and slavery-project pages. Georgia Archives slave-laws PDF. Harvard Magazine April 2022. Florida Museum St Augustine timeline. DAH Timucua entry at Encyclopedia.com.

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

## Log

- 2026-09-27 T-261c units 8-10: era 8 bank patches (9) and outline edits (see units table). Sources: Jones, *Negro Education* vol. I, 1917 (archive.org djvu text); TSHA Handbook, Delgado v. Bastrop ISD (Allsup); NPS Manzanar Block 16, Poston lesson and "Education Behind Barbed Wire"; jrank Encyclopedia of Japanese American History (30,000 pupils); National WWII Museum (120,000 held); Cohen 1942 ch. 12 (thorpe.law.ou.edu); 25 U.S.C. 282 at govinfo; Dickinson Carlisle closure page; Salt Lake Tribune 2023 on the 1928 Uintah hearing; Trennert 1989 abstract; Gutenberg #39969 Civic Biology; Linder Famous Trials. Blocked: Densho encyclopedia and catalyst (403), tennesseeencyclopedia (404 at the guessed URL). Validator 0 errors, research PASS (bank 70,528w, outline 30,013w).

- 2026-09-27 T-261b unit 7: outline eras 6-7 edited (see units table), validator 0 errors, research PASS (bank 66,943w, outline 30,782w; eras 6-7 outline 6,759w to 8,372w).

- 2026-09-27 T-261b units 5-6: era 7 bank patches. Sources: Douglass narrative 1854 (Gutenberg 70331); Alvord 5th and 9th reports (archive.org djvu text); Encyclopedia of Alabama (Hebert); Owen Sound Hub; USCCR 2008 Tennessee report; LII texts of Cumming and Plessy; DOI reports Vol I 2022 and Vol II 2024 (bia.gov PDFs); Proclamation 10870 full text; High Country News 2020.

- 2026-09-27 T-261b unit 4: era 6 bank patches. Sources: Woodson 1915 (Gutenberg 11089) statute footnotes; Colored Conventions Project and Town of Canaan (Noyes); DOI boarding school report Vol I 2022 (bia.gov PDF, pypdf); ExploreKYHistory and Penn State (Choctaw Academy); HistoryofInformation and CT Academy of Arts and Sciences (Webster ~60 million by 1890). Unsourced 'first time in print' claim flagged.

- 2026-09-27 T-261a: era 4 patches: Brafferton Indian school (4 captive boys bought c.1702 by traders Hicks and Evans, 125+ students from 26 nations 1723-76; W&M pages); SEARCHED NOT FOUND on Brafferton deaths and boys' names; Harry and Andrew bought (Woodson 1915, Gutenberg text); Ursulines 1727 (uanola.org); Lenape land (search summary). Era 5: Isaac Bee, named Bray pupil (W&M roster 1765; Burwell ad 3 Sept 1774, Encyclopedia Virginia; AP/NBC link); Georgia 1755/1770 bans (Georgia Archives, disagreement on reading); Fort McIntosh 1785 and Shawnee rejection (Knepper, Ohio Lands Book); Moor's school, Oneida withdrawal 1769, Occom £12,026, Dartmouth charter, Wheelock enslaved 17 (Dartmouth pages). Outline eras 1-5 edited: new spans and story lines from these patches; em dashes, semicolons and self-references cleared from eras 1-5.

- 2026-09-27 T-261a: era 1 patch (Mi'kmaq writing challenge to "no writing north of Mexico", tertiary source, wording advice). Era 2 patch (Seloy's town at St Augustine, Florida Museum; Ajacán people; 1572 Spanish hangings, Encyclopedia Virginia; Timucua fate, DAH). Era 3 patches: John Barnard, a NAMED child beaten by Cheever c.1690-96 in his own words (Bartleby/Trent & Wells, MHS Coll. 3rd ser. v.5); Collegiate School 1628 dispute on "oldest school" (Harvard Crimson 1984); Boston land (West End Museum, search summary); Deer Island 1675-76 (NPS); SEARCHED NOT FOUND on Deer Island order signers and Monequassun's fate; Harvard at least 79 enslaved (Harvard Magazine 2022); W&M 1693 charter, Nottoway 1718 (17 enslaved, £476, Encyclopedia Virginia).
