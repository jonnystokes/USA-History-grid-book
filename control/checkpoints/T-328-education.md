# CHECKPOINT T-328 | education | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-9 (part3), writer C: era 10 (part3) + final

STATUS: T-328b landed (director verified: FAIL  education / prose)
VERIFY: python tools/project_state.py --check education --stage prose   (passes only after writer C)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/education/part1-before-1800.md (eras 1-5) · manuscript/education/part2-1800s.md (eras 6-7)
        · manuscript/education/part3-1900s-and-today.md (eras 8-10) · research/research-education.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-328b finished units 8-9 (2026-09-30). part3 16896w (era 08 7410w, era 09 9495w), 0 validator errors, 0 em dashes, 0 semicolons. Self-review run.
NEXT:   T-328c: unit 10

## Research state before writing (2026-09-29)

PASS  education / research
measured: stage=RESEARCHED eras=10/10 stories=21 (v21 c0 t0) verify_tags=0 bank=81878w outline=32417w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-328a | done | 671w file total, 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-328a | done | 1469w file total, 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-328a | done | 3867w file total, 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-328a | done | 6152w file total, 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-328a | done | 8531w file total, 0 errors, emdash=0 semicolon=0 (after part1 self-review) |
| 6 | era 06 1800-1850 -> part2 | T-328a | done | 4510w file total, 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-328a | done | 10206w file total, 0 errors, emdash=0 semicolon=0 (after part2 self-review) |
| 8 | era 08 1900-1950 -> part3 | T-328b | done | 7430w file total, 0 errors, emdash=0 semicolon=0 (7410w after self-review) |
| 9 | era 09 1950-2000 -> part3 | T-328b | done | 16896w file total (era 09 9495w), 0 errors, emdash=0 semicolon=0 (after part3 self-review) |
| 10 | era 10 2000-today -> part3 | T-328c | todo | |
| 11 | final: self-review, --punct, validator, prose check | T-328c | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 01 | how Native children were taught, a sourced account; wampum material and the five nations | PATCH | PATCH 2026-09-30 (T-328a): how children learned
- 03 | Shawmut peninsula land (bank note was unconfirmed search summary) | PATCH | PATCH 2026-09-30 (T-328a): Shawmut land, now read directly
- 04 | Lenape homeland and Penn's purchases (unconfirmed in bank) | PATCH | PATCH 2026-09-30 (T-328a): Lenape homeland, read directly
- 04 | who enacted the 1740 act, its stated reason, how the fine was enforced | PATCH | PATCH 2026-09-30 (T-328a): who enacted the 1740 act
- 04 | names of the drafters; any prosecution under section 45 | SEARCHED, NOT FOUND | SEARCHED, NOT FOUND 2026-09-30 (T-328a): which individual members drafted the 1740 act
- 05 | Fort McIntosh treaty date and signers (unconfirmed in bank) | PATCH | PATCH 2026-09-30 (T-328a): Fort McIntosh treaty date and signers
- 07 | officials who set up Carlisle (Schurz, Hayt, McCrary); military discipline and the fence | PATCH | PATCH 2026-09-30 (T-328a): the officials who set up Carlisle, and the fence
- 07 | names of Carlisle staff who cut hair and punished children, 1879-1900 | SEARCHED, NOT FOUND | SEARCHED, NOT FOUND 2026-09-30 (T-328a): the names of the Carlisle staff

- 08 | a named child beaten at a federal boarding school (T-261c SEARCHED, NOT FOUND) | PATCH (found) | PATCH 2026-09-30 (T-328b): Julia Hardin at Carlisle
- 08 | Carlisle's 1914 petition and hearings, Pop Warner | PATCH | PATCH 2026-09-30 (T-328b): the student petition and the 1914 hearings
- 08 | Poston land: which nation, tribal council objection | PATCH | PATCH 2026-09-30 (T-328b): Poston's land
- 08 | EO 9066 gloss and DeWitt, Depression gloss | PATCH (copied from war, rights-movements, economy banks) | PATCH 2026-09-30 (T-328b): two short glosses
- 09 | Boston 1974 ruling (Garrity), East LA walkouts, Tinker, New Rider (parked pointers only in this bank) | PATCH (copied from rights-movements, styles banks) | PATCH 2026-09-30 (T-328b): three school items copied from other chapters' banks

## OPEN (should be rare)

## Outline claims left out
- 04: "an indenture often required the master to teach the child to read" (no bank source for indentures in 1700-1750). The 1642 law's duty on masters is told in 03 instead.
- (restored) Webster's 60 million: the era-6 bank PATCH (T-261b) sources it, so the era-05 story now gives 15 million by 1837, about 60 million by 1890, up to 100 million.
- 03: Wycliffe (1382) and Skelton (1529) versions of "spare the rod" left out for length and reading level. Ælfric, Proverbs and Butler kept.
- 03/04: Deer Island midnight boat trip and Daniel Henchman's ban on fires (bank: unconfirmed search summary only).
- Parked art item (Loara Standish sampler, era 03) not written: its text is in research-art.md, not this bank.
- 06: Prudence Crandall (outline pointer only, no bank text; rights-movements tells it). Mann's Fourth Report used; Pennsylvania and Ashtabula wage figures left out for length.
- 06: the outline's rattan, ferule and switch-from-a-tree line moved to 07 (the bank sources rattan and ferule to the 1866 pamphlet and Boston rules). The switch is defined in the anti-literacy span.
- 07: Pop Warner and the 1914 football-money hearing, and the 279 children transferred in 1918 (belong to era 08). Ward v. Flood (1874) and Edmonia Lewis (parked notes too thin to write). The Morrill 73 million acres by 1920 (Knepper, parked for eras 6-8) not used. The Fort Marion "Six Unknown Indians" graves and 2023 naming (only a pointer to research-art.md).
- 07: Arozina Perkins (bank 7o: not confirmed she boarded round).
- 08 (T-328b): Terman's first paragraph not reprinted (slur), per bank ruling; its claim stated in full. Watson v. Cambridge (1893) not used (full text never fetched). Cuyahoga parents 1933 not used (no founders named). The 1.75 million child-labor alternative not used (bank rule). Rosenwald funding split not printed (bank). Delgado census figure (3.5 years) left out (scope unconfirmed). Manzanar opening-day counts and the pupil's floor quote left out (unconfirmed: search summary only). Poston 71,000 acres left out (unconfirmed).
- 09 (T-328b): Little Rock Lost Year count (3,665) and the four school names (unconfirmed: search summary only). Leander Perez quote (partly garbled source). Ole Miss: Barnett's personal blocking of Meredith (unconfirmed). Boston: Garrity receivership 1975 (unconfirmed). Bilingual Education Act four-years figure (bank rule). Blackwell 'burial of Mr. Spanish' (bank rule). Homeschool alliance split and HSLDA 1983 left out for length. In re Gault (crime-justice tells it). Dollywood and Imagination Library (music, not schooling). Riddle quote cut before its em dash. Norman New Rider's name (search summary only).

## Decisions and defects fixed
- Outline defect: "Reading and conversion were the same lesson here" (copular slogan) rewritten as a statement about Eliot's books.
- Outline defect: "it is worth being plain about what the land was" (metadiscourse) and "The treaty ... pushed" (personification): prose names the US commissioners and states the land's people first.
- Outline defect: "The college itself bought" / "the Society bought" style institution-actors: prose names leaders or members.
- Outline defect: Ann Wager story ended on her death, the Bray span ended on a closing antithesis ("Both things happened in the same room"): prose ends the story on Isaac Bee's escape and states the two facts plainly.
- Outline defect: Christopher Dock "He was gentler than most schoolmasters" without a unit: kept as the bank's "milder than the schoolmasters around him", with whipping defined.
- Placement: dame school and hornbook moved from 03 (outline) to 04 (where the bank sources them). Pareja's printed books moved from 02 to 03 (bank boundary rule).
- Stono Rebellion given a one-clause gloss ("an uprising by enslaved people") from general knowledge. Flag for audit if the bank must hold it. Same for Nat Turner ("a rebellion of enslaved people in Virginia") and the Ku Klux Klan gloss in 07.
- Outline/official-source defect: the 2024 proclamation places Zitkala-Ša's haircut at Carlisle. Prose states it happened at White's Institute and names the error.
- Outline defect: era-7 summary "Four enormous things happen at once" (promotional, count abstraction) rewritten as plain facts. "Everyone says" (summer break) rewritten as "Many people say".
- Outline defect: Josephine Foster story opened with "We know her name" (breaks the fourth wall toward the reader) rewritten.
- Outline defect: "the Choctaw Nation paid for it", "Congress hands states", "the Army did it" and similar institution-actors rewritten with officials or lawmakers as subjects.
- Outline defect: Horace Mann span "See Sarah Roberts, below" (metadiscourse) removed.

- 08 (T-328b): Outline defect: "The federal Indian boarding schools were at their largest in this era" contradicts the bank (enrollment peaked about 60,000 in 1973). Prose says "held tens of thousands".
- 08 (T-328b): Outline defect: "Very few American classrooms were rebuilt on his plan" and "The school was small and it was well known" have no bank source. Cut. Outline "Army officers"/"the federal government held" (institution actor) rewritten naming Roosevelt and DeWitt.
- 08 (T-328b): Outline defects: "The one-room school did not fade away" (contrastive negation), "What went with it was the school inside walking distance" (no bank source), "the plainest description of them is the government's own" (evaluative), "The whole case was about which language" (closing line): all cut or rewritten.
- 08 (T-328b): Outline gave Justice Butler and Sutherland no first names, prose kept surnames only (bank has no first names).

- 09 (T-328b): Outline defect: "Almost nothing changed in the classrooms for another ten years" and "the argument it started is still the main argument about American schools" (unanchored, era-10 claim): rewritten as the sourced figures. "Nobody ended it after four years" rewritten from the FSA handbook patch. "Ten years of work made no difference to what the job paid" (quotable closer) cut. "The Act did not start the change. It made it a right." (antithesis) rewritten. "Children were being sorted into different groups, as well as counted in greater numbers" (closing line) cut. "The school year inside was the part nobody photographed" (decoration) cut. "Buses were not new ... it is what the argument was about" cut (no bank line for 'forty years' in this span).
- 09 (T-328b): Outline 'Michigan certified-teacher rule, the strictest rule left anywhere' (bank forbids the superlative): not printed. Outline Hawaiian 'first indigenous-language immersion classes in the United States' attributed to the group's own history. Outline 'Navajo Community College ... first community college run by a tribe' attributed to the college.
- 09 (T-328b): Outline 'The Indian boarding schools were largest in 1973' stated as the museum's count, with the lower federal counts beside it (bank handling note).
- 08 (T-328b): Era-7 gloss carried: part2's 'Carlisle closed 1918' now given its cause (War Department, Army hospital).

## TO PARK (for the director, burst runs only)

## HANDOFF for writers B and C (from T-328a, 2026-09-30)

Voice: plain present-day, US dates ("May 10, 1740"), numbers as numerals, "lawmakers"/"officials" as actors, never an institution. Stories open on their teaching point and close on what the person did.

Terms already defined in part1/part2 (use freely, do not re-define): apprentice, elders, oral tradition, syllabary, wampum, mission, conversion, friar, doctrine, baptism, Jesuits, interpreter, public school ("one that a town or a state runs"), sachem, epidemic, General Court, selectmen, grammar school, primer, woodcut, catechism, birch rod, "correct" (= beat), internment, charter, scribe, forfeit, pass, dame school, hornbook, charity school, boarding school, academy, whipping ("hitting a person again and again with a whip, a rod or a strap"), yoke, ordinance, reserve, duress, natural philosophy, journeyman, shilling, slave code, manual labor, corporal punishment ("hitting a child as a punishment"), pagan, common school, normal school, slate, recitation bench, boarding round, nonsectarian, nativist, seminary, militia, eclectic, sign language, lash, switch, grand jury, insurrection, mulatto, damages, compulsory attendance law, land-grant college, land cession, mechanic arts, Freedmen's Bureau, Ku Klux Klan, lynch, misanthrope, rattan, ferule, Taps, guardhouse, outing system, solitary confinement, flogging, cuffing, shingled.

Threads started that continue after 1900:
- Boarding schools: Carlisle told in full in 07 (Pratt, Schurz/Hayt/McCrary, day, labor, outing system, 180+ deaths, the nine Rosebud children returned 2021, the 1893 rations law, the 2022/2024 Interior counts of 417 schools and at least 973 deaths, the 2022 punishment list and the proclamation's sexual-abuse line). Do NOT repeat those system totals. Carlisle closes 1918 (7,800 children stated in 07); 279 children transferred in 1918 and the 1914 hearing (Pop Warner, Gus Welch) are yours. Meriam 1928, Kennedy 1969, Native control 1968-75 are yours.
- Zitkala-Ša's story already covers her adult work to 1938 (Society of American Indians, National Council of American Indians). Mention her in era 08 only by pointing back, not retelling.
- Corporal punishment: 07 states New Jersey 1867 and "no other state followed for 104 years, until Massachusetts in 1971." Eras 09-10 carry Ingraham v. Wright and the state sequence. Do not restate 1867 as new.
- Compulsory attendance: 07 already states Massachusetts 1852, 32 states by 1900, all by 1918 (Mississippi last). Era 08 should not re-announce it.
- Teaching as women's work: 07 gives 1869-70 and 1899-1900 federal counts (70 percent women). The 86 percent of 1919-20 and the marriage bar (bank 7l) are era 08.
- Catholic system: 1884 Baltimore council told in 07. Pierce v. Society of Sisters is era 08.
- Separate schools: 07 tells Tennessee's 1873 law, San Francisco 1854/1859/1870, Plessy (1896, citing Sarah Roberts) and Cumming (1899, Ware High School). Brown is era 09.
- Booker T. Washington's story ends with his death in 1915 and names Du Bois's "Atlanta Compromise" attack.
- Summer calendar: 07 gives Kenneth Gold's account and 1869-70/1899-1900 term lengths. Current day counts are era 10.
- Normal schools: 180 by 1900 stated. Their becoming teachers colleges is yours.
- Land: Land Ordinance 1785 (05) and Morrill 1862 (07, Lee and Ahtone's 10.7 million acres) both told as land taken from Native nations.

## HANDOFF for writer C (from T-328b, 2026-09-30)

Part3 exists with eras 08 and 09. Append era 10 after the line `<!-- hb-time:end id="1950-2000" -->`. The hb-note at the top already names eras 08-10.

Terms defined in part3 (use freely): intelligence test, eugenics, cerebral palsy, parochial school, evolution, asylum, sterilize, committed, salpingectomy / Fallopian tubes, tuberculosis, trachoma, migrant worker, strap, manual training, marriage bar, teachers college, adobe, tuition, veteran, desegregate, integration, segregationist, federal marshal, NAACP, sharecropper, coercive assimilation, frostbite, barrio, immersion class, magnet school, segregation academy, charter school, epilepsy, hematoma, Eighth Amendment, paddle (wooden board swung against the buttocks), truant, probation, union, mediocrity, psychiatrist, anthropologist, felony conspiracy.

Threads that continue into era 10:
- Corporal punishment: era 09 ends with 27 states + DC banned by 1994, none again until Delaware 2003, 23 states still allowing it in 2000, and OCR counts 1976/1990/2000. Era 10 starts from Delaware 2003 (named only as the year the pause ended) and needs a current, dated state count.
- Boarding schools: era 09 gives the 1973 peak (museum), 1969/1971 federal counts, the Yazzie brothers (1968), Kennedy Report 1969, Navajo Community College 1968, 1975 Act, ICWA 1978. Era 08 already gives 417 schools system total only by reference; part2 has the 2022/2024 Interior counts. Era 10 owns the 2021-2024 investigation, the 2024 apology and the Carlisle monument (Dec. 9, 2024).
- Special education: era 09 stops at 4,641,000 / 11.4 percent in 1989-90 and the 1975 Act. The 1990 IDEA renaming is era 10's.
- Charter schools: Minnesota 1991, City Academy 1992, cap raised to 20 in 1993. Magnet: about 2,400 by 1991. Catholic: 2,475,439 in 1990-91. Homeschool: most states settled by 1989, DeJonge 1993. Era 10 has current shares.
- Teacher pay: flat in real terms 1989-90 to 1999-2000 (about $63,500); Allegretto's gap 6 percent in 1996, widening after. Era 10 has the record 2024 gap.
- College: 15,312,289 enrolled in 2000; borrowing 65 percent of 1999-2000 graduates, average $19,300.
- Segregation: Coleman 1965-66 figures in era 09. The UCLA 2014 resegregation figure (35.8 percent) is era 10's.
- Nation at Risk (1983) is where era 09 leaves testing and standards. No Child Left Behind is era 10's.
- Hawaiian immersion 1987 in era 09. Wôpanâak (1993) not used; era 10 may.
- Ruby Bridges: McDonogh No. 19 reopened May 4, 2022, as the Tate, Etienne and Prevost Center (bank §9b), not used; era 10 may.
- Blackwell School: national historic site October 2022 is in era 09 already (as the end of its span). Do not repeat.

## Log
- 2026-09-30 unit 1 era 01: part1 created, 671 words, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 unit 2 era 02: 1469 words (file), validator 0 errors, --punct emdash=0 semicolon=0. Story paquiquineo-don-luis with the 1572 hangings. Pareja's printed books moved to era 03 (bank boundary rule).
- 2026-09-30 unit 3 era 03: 3867 words (file), validator 0 errors, --punct emdash=0 semicolon=0. Stories ezekiel-cheever, caleb-cheeshahteaumuck. Barnard told in a zoom (no new story block). Deer Island, Harvard's at least 79 enslaved, Timucua in print added from bank patches. Dame school and hornbook placed in era 04, where the bank sources them (§4a).
- 2026-09-30 unit 4 era 04: 6152 words (file), validator 0 errors, --punct emdash=0 semicolon=0. Story christopher-dock. 1740 act now names Lt. Gov. William Bull, Council, Commons House, the act's own reason, and the informer's half of the fine.
- 2026-09-30 unit 5 era 05: 8531 words (file), validator 0 errors, --punct emdash=0 semicolon=0. Stories ann-wager (closes on Isaac Bee), noah-webster (60 million dropped, unsourced). Fort McIntosh date and signers confirmed. Part1 self-review run: document-verb, institution-as-actor and anaphora repairs applied.
- 2026-09-30 unit 6 era 06: part2 created, 4510 words, validator 0 errors, --punct emdash=0 semicolon=0. Stories horace-mann, mary-swift-education, catharine-beecher-education, sarah-roberts-education. No new research needed (bank complete for era 6). Rattan and ferule held for era 07 (the bank sources them to the 1866 pamphlet and Boston rules). Prudence Crandall left to rights-movements (no bank text here).
- 2026-09-30 unit 8 era 08 (T-328b): part3 created, 7430 words, validator 0 errors, --punct emdash=0 semicolon=0. Stories mamie-garvin-fields, john-dewey, sylvia-mendez. New span on Julia Hardin, beaten at Carlisle (Joint Commission testimony, Feb. 7, 1914), plus the Gus Welch petition. Freeman 1902 prayer case and New London 1937 added from bank pointers. Four semicolons inside Uintah quotations split at the semicolon, no word changed.
- 2026-09-30 unit 9 era 09 (T-328b): 16896 words (file; era 09 9495w), validator 0 errors, --punct emdash=0 semicolon=0. Stories ruby-bridges, peter-mills-education, dejonge-family-homeschool. New spans: Tinker and New Rider, Boston 1974 with Garrity's ruling, East LA walkouts. Part3 self-review run: institution-as-actor (schools, boards, report verbs), repeated era openings ('In these years', 'In 19xx the justices'), hard-word glosses added (integration, marshals, NAACP, sharecropper, probation, psychiatrist, anthropologist, felony conspiracy, veteran).
- 2026-09-30 unit 7 era 07: 10206 words (file), validator 0 errors, --punct emdash=0 semicolon=0. Stories charlotte-forten-education, josephine-foster-education, zitkala-sa-education, booker-t-washington. Carlisle span names Schurz, Hayt, McCrary. Women's colleges span added from parked rights-movements notes in the bank. Part2 self-review run: institution-as-actor (Congress, the Army, the Department, the district), document verbs, duplicated Mann material removed from his story.
