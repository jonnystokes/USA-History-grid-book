# CHECKPOINT T-328 | education | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-9 (part3), writer C: era 10 (part3) + final

STATUS: T-328a landed (director verified: FAIL  education / prose)
VERIFY: python tools/project_state.py --check education --stage prose   (passes only after writer C)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/education/part1-before-1800.md (eras 1-5) · manuscript/education/part2-1800s.md (eras 6-7)
        · manuscript/education/part3-1900s-and-today.md (eras 8-10) · research/research-education.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-328a finished units 1-7 (2026-09-30). part1 8547w, part2 10206w, both 0 validator errors, 0 em dashes, 0 semicolons.
NEXT:   T-328b: unit 8

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
| 8 | era 08 1900-1950 -> part3 | T-328b | todo | |
| 9 | era 09 1950-2000 -> part3 | T-328b | todo | |
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

## Log
- 2026-09-30 unit 1 era 01: part1 created, 671 words, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 unit 2 era 02: 1469 words (file), validator 0 errors, --punct emdash=0 semicolon=0. Story paquiquineo-don-luis with the 1572 hangings. Pareja's printed books moved to era 03 (bank boundary rule).
- 2026-09-30 unit 3 era 03: 3867 words (file), validator 0 errors, --punct emdash=0 semicolon=0. Stories ezekiel-cheever, caleb-cheeshahteaumuck. Barnard told in a zoom (no new story block). Deer Island, Harvard's at least 79 enslaved, Timucua in print added from bank patches. Dame school and hornbook placed in era 04, where the bank sources them (§4a).
- 2026-09-30 unit 4 era 04: 6152 words (file), validator 0 errors, --punct emdash=0 semicolon=0. Story christopher-dock. 1740 act now names Lt. Gov. William Bull, Council, Commons House, the act's own reason, and the informer's half of the fine.
- 2026-09-30 unit 5 era 05: 8531 words (file), validator 0 errors, --punct emdash=0 semicolon=0. Stories ann-wager (closes on Isaac Bee), noah-webster (60 million dropped, unsourced). Fort McIntosh date and signers confirmed. Part1 self-review run: document-verb, institution-as-actor and anaphora repairs applied.
- 2026-09-30 unit 6 era 06: part2 created, 4510 words, validator 0 errors, --punct emdash=0 semicolon=0. Stories horace-mann, mary-swift-education, catharine-beecher-education, sarah-roberts-education. No new research needed (bank complete for era 6). Rattan and ferule held for era 07 (the bank sources them to the 1866 pamphlet and Boston rules). Prudence Crandall left to rights-movements (no bank text here).
- 2026-09-30 unit 7 era 07: 10206 words (file), validator 0 errors, --punct emdash=0 semicolon=0. Stories charlotte-forten-education, josephine-foster-education, zitkala-sa-education, booker-t-washington. Carlisle span names Schurz, Hayt, McCrary. Women's colleges span added from parked rights-movements notes in the bank. Part2 self-review run: institution-as-actor (Congress, the Army, the Department, the district), document verbs, duplicated Mann material removed from his story.
