# CHECKPOINT T-237 | immigration | prose (Phase 2, first new chapter) | 10 eras, 3 part files

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check immigration --stage prose
        (per part: node tools/validate_grid.js <file> --part · python tools/project_state.py --punct <file>)
BRIEF:  standard WRITING brief (control/RESUME.md) + cloud lines (control/CLOUD-WORKFLOW.md §5)
SOURCES (read-only): outlines/immigration.md (the plan) · research/research-immigration.md (THE ONLY
        source of facts, DECISIONS #13) · workspace/immigration.md
MODEL:  manuscript/native-nations/ and manuscript/city-building/ are finished v2 chapters.
        Copy their file layout: an hb-chapter line with mode="prose" part="2" file="partN", an
        hb-note naming the file's eras, then the hb-time sections.
PLAN:   T-237a = part1-before-1800.md (eras 1-5), T-237b = part2-1800s.md (eras 6-7),
        T-237c = part3-1900s-and-today.md (eras 8-10).

NOW:    T-237c: part 3 era 1900-1950 landed (unit 8). Next era 1950-2000.
NEXT:   part 3, era 1950-2000 (unit 9), then 2000-today (unit 10).

## Units

| # | unit | state | landed (commit / note) |
|---|------|-------|------------------------|
| 1 | part1 era before-1500 (thin) | landed | file created, era written |
| 2 | part1 era 1500s (thin) | landed | era written |
| 3 | part1 era 1600s | landed | 6 spans + stories frethorne, hutchinson, jewish-refugees-1654 |
| 4 | part1 era 1700-1750 | landed | 4 spans + story zenger |
| 5 | part1 era 1750-1800 | landed | 3 spans + stories hamilton, toussaint |
| 6 | part2 era 1800-1850 | landed (revised T-237b2) | file created. 3 spans + stories jette-bruns, patrick-kennedy-bridget-murphy |
| 7 | part2 era 1850-1900 | landed (revised T-237b2) | 7 spans + stories carl-schurz, annie-moore, irving-berlin, wong-kim-ark |
| 8 | part3 era 1900-1950 | landed | file created. 6 spans (Ellis/melting pot, Angel Island, quotas, eugenics, Mexican Repatriation + braceros, St. Louis + DP Act) + stories frank-capra, doukenie-bacos, lee-puey-you |
| 9 | part3 era 1950-2000 | todo | |
| 10 | part3 era 2000-today | todo | |

## Outline claims NOT in the bank (left out, per DECISIONS #13)

<!-- The claim, the outline line, and where it would have gone. -->

- "small and often in danger" (St. Augustine, outline 1500s span, line 30). Bank does not say it. Left out of 1500s span.
- Hutchinson "to worship as they believed" and "on trial ... for her religious meetings" (outline line 44). Bank gives only "following minister John Cotton to Boston" and "tried November 1637 and banished". Left out.
- Frethorne "bound to Martin's Hundred plantation" (outline line 48): bank says only "at Martin's Hundred". Written as "worked at a place called Martin's Hundred".
- Hamilton "the first Secretary of the Treasury" (outline line 82). Bank says only "his Treasury work". Prose: "worked for the new national government at the Treasury".
- Toussaint "quietly", "for years", "the city's first Catholic charities" (outline line 86). Bank: "early Catholic charities". Left out / written as bank.
- Zenger "the poor refugee boy" and "1735 acquittal began press freedom in America" (outline line 66). Bank gives only the 1735 seditious-libel acquittal. Left out.

- [T-237b, 1800-1850] Irish "grew through the 1840s" (outline line 96): bank gives no decade for anti-Irish feeling. Left out.
- [T-237b] Kennedy "on a farm" (outline line 100), Bridget "made the same crossing", "leaving Bridget a widow with four young children", "youngest son's grandson", JFK "president in 1961": bank has none of these (bank: five children, line Patrick > P.J. > Joseph P. > JFK). Left out.
- [T-237b] Jette Bruns "a doctor sold on the promise of cheap land", letters "recording frontier sickness, grief, work, and the long strangeness of a new country" (outline line 104). Not in bank. Left out.
- [T-237b, 1850-1900] Schurz "near Cologne" kept (bank Key line has it). Wong Kim Ark "the exclusion laws applied to him, said the government, because his parents were Chinese" and "Held aboard ship while his lawyers filed suit, he took the fight to the Supreme Court" (outline line 126): bank has neither the government's reason nor the detention nor who appealed. Prose: officials refused him landing, a court issued habeas corpus Oct 2 1895, the case reached the Supreme Court. "He took the fight" dropped (the case was US v. Wong, the government appealed per its name).
- [T-237b] Berlin "only memory", "family of a poor cantor", "singing for pennies on the Lower East Side", "the country's most successful songwriter", "the unofficial anthem written by an immigrant" (outline line 130). Not in bank. Left out. Bank: "remembered image", songs list, 1918 draft, Kate Smith 1938.
- [T-237b] Annie Moore "For a century" kept as bank's "century-long mix-up". Outline's Emma Lazarus and Statue lines all in bank.
- [T-237b] Castle Garden "the federal station" / Ellis "replacing Castle Garden" in bank. Outline's "German arrivals peaked" (bank: "1854 was an early peak") written as numbers only.

- [T-237c, 1900-1950] Capra "when he was six", "cheapest steerage berths" kept only as steerage, "one of Hollywood's most honored directors" (outline line 140). Bank gives birth May 18, 1897 and 1903 crossing, no age, no ranking. Left out ("as a young boy").
- [T-237c] Bacos "a teenager determined to leave", "heard older girls whisper she might be sent back", "She was admitted", "one of nearly 2,000 recorded immigrant voices" (outline line 144). Not in bank. Left out. Prose does not state her admission (bank implies it only through the 1991 Ellis Island interview).
- [T-237c] Lee Puey You "settled in San Francisco" kept (bank). Outline "after the exclusion law's repeal" kept via bank line 171 (repealed 1943). Outline "interrogation ... 200 to 1,000 questions" style range (bank patch: "exact source not confirmed") left out.
- [T-237c] Outline era line "stay shut through the years people most needed to get out" is interpretation, not bank fact. Left out.

## Defects in the outline or bank, fixed in the prose (go to AUDIT-QUEUE)

- [T-237b, 1800-1850] SOFTENING / GIST GAP (bank s6): the Irish famine is given only as "a potato blight caused mass starvation". The bank has no human actors (landlords, evictions, British government food policy). Prose states the bank's facts only. Audit should add the documented human causes to the bank.
- [T-237b, 1800-1850] REIFICATION (bank s6 and outline): "Anti-Irish and anti-Catholic feeling grew". Prose: "Some Americans turned against the Irish newcomers and against Catholics". Bank gives no acts, places, numbers or dates (no Philadelphia 1844 riots, no Ursuline convent burning). Audit gap: nativist riots are absent from the bank, so the prose cannot state them.
- [T-237b, 1800-1850] PERSONIFICATION (outline line 96): "the Act signed March 2, 1807" as actor ("Legal arrival ... ended under the Act"). Prose: "President Thomas Jefferson signed a law that banned ...". Smuggling agentless in bank ("smuggling continued"): prose "Smugglers kept bringing in captives".
- [T-237b, 1850-1900] SELF-CONTRADICTION (bank s7 Castle Garden): "New York took over from the federal side amid corruption complaints; the federal government then took charge". The first clause contradicts the rest. Prose: state and city officials ran Castle Garden 1855-1890, there were complaints of corruption, federal officials then took charge and opened Ellis Island. Audit should fix the bank sentence.
- [T-237b, 1850-1900] PERSONIFICATION (bank s7 Schurz): "when Prussia crushed them". Prose: "When Prussian forces crushed them".
- [T-237b, 1850-1900] PERSONIFICATION (bank s7 Page Act): "It barred ... most Chinese women". Prose: "Under it, ... could not come in" and "In practice, most Chinese women could not get in under the Page Act". Also "Central Pacific Railroad hired" -> "managers of the Central Pacific Railroad hired". "The Know-Nothing party swept Massachusetts" -> "Know-Nothing candidates won almost every race". "Split over slavery" -> "the party's members split".
- [T-237b, 1850-1900] AUDIT GAPS (hard subjects, bank has nothing): no anti-Chinese violence at all (no Los Angeles 1871, no Rock Springs 1885, no expulsions), no nativist riots, no causes for the ~1,200 Chinese railroad deaths, no attackers or casualty numbers for the 1881 pogroms, no killers named for Alexander II, no actor for the fire Berlin remembered, no names of the officials who refused Wong Kim Ark. Prose states each absence plainly ("The sources for this chapter do not record ..."). Brief asked for anti-Chinese violence and nativist riots under the hard-subjects policy. They cannot be written until the bank holds them.
- [T-237b, 1850-1900] ACTOR INFERRED: bank "May Laws of 1882 that restricted" has no issuer. Prose "Russian officials issued rules called the May Laws". Audit should confirm the issuer in the bank.
- [T-237b, 1850-1900] Clotilda kept to one short span per the Scope ruling (slavery-freedom leads). Kossola not told.
- [T-237b] Glosses (1850-1900, general knowledge, definitions only): nationality, ethnicity, Prussia = a kingdom in what is now Germany, Secretary of the Interior = a department head who advises the president, Gold Rush, contract laborer, "coolie" = insulting word, prostitution, pretext, exclusion, repeal, assassinated, pogrom (bank's own gloss), Pale of Settlement, dedicated, pedestal, refuge, depot, corruption, genealogist, tenement, writ of habeas corpus, Fourteenth Amendment = an addition to the Constitution.
- [T-237b] Glosses (1800-1850, general knowledge, definitions only): importation, democratic government, professionals, Westphalia = a region of Germany, Jefferson City = capital of Missouri, boardinghouse, capitol, potato blight = plant disease, famine, Catholics = church led by the pope in Rome, cooper = barrel maker, cholera (disease from dirty water or food, heavy diarrhea, death within days).

- Glosses from general knowledge, not in the bank (word definitions only, no historical claim): "Norse" = sailors from northern Europe; Newfoundland "in what is now Canada"; land bridge = dry ground joining Asia to North America.
- LAND ERASURE GAP (bank): bank section 2 does not name the Native nation on whose land Menendez built St. Augustine, and section 3 names only the Powhatan for the 1600s colonies (no Wampanoag for Plymouth, no nation for Massachusetts Bay, New Amsterdam, Maryland or Pennsylvania). Prose states "on Native land" from the bank's general lines. Audit should add the nations to the bank.
- PERSONIFICATION (outline 1600s, line 44): "The colony she joined ... put her on trial". Prose: "she was tried in Massachusetts and banished. The sources used here do not name her judges." Bank should name the court (General Court, Winthrop presiding) in audit.
- PERSONIFICATION (bank s3/s4 and outline line 52): "Portugal retook Dutch Brazil", "the Dutch West India Company overruled him". Prose: "Portuguese forces took it back", "Officials of the Dutch West India Company ... overruled him".
- CHRONOLOGY (outline 1700-1750 span, line 62): Huguenots "after 1685" sit in 1700-1750, but the bank says the 1,500 to 2,000 arrived by 1700. Moved to the 1600s era.
- POLICY QUESTION: jewish-refugees-1654 is a group story; only Jacob Barsimson is named. Kept as hb-story per brief (same slug/name). Director may want it as hb-zoom (policy s4: hb-story is named people only).
- Siwanoy attack on Hutchinson: bank gives no reason or land context. Prose says the sources used here give no reason. Audit gap.
- 1619 captors unnamed in bank: prose says "Captors whom the sources do not name".
- Glosses (1600s, general knowledge, not bank): loblollie = thin porridge; privateer; Puritans = English Protestants who disagreed with how the Church of England was run; Archbishop of Canterbury = head of the Church of England; Quakers = Society of Friends; Edict of Nantes = law that had let French Protestants worship in France; West Indies.
- Jamestown: bank says only "conflict with the Powhatan". Prose says the Powhatan people already lived on the land around Jamestown (land-erasure rule).
- PERSONIFICATION (bank s4): "South Carolina Lowcountry rice economy ... imported" Africans. Prose names rice planters as buyers. Sullivan's Island: bank uses agentless "were held"; prose says the sources used here do not name who held them.
- Convict transport: "Britain shipped" (outline line 62) is personification. Prose: "Under a British law of 1718 ... convicts were shipped" plus "The sources do not say who shipped and sold them."
- ADDED from bank (not in outline): 1700-1750 forced-arrival span (Charleston, Sullivan's Island, SlaveVoyages scale figures). Kept short per slavery-freedom lead.
- Glosses (1700-1750): Palatinate = region along the Rhine; Presbyterians; backcountry; apprentice; seditious libel; emigrate; quarantine; Lowcountry.
- CHRONOLOGY (outline line 86): Toussaint's 1787 arrival called "part of the refugee stream from Saint-Domingue". The revolution began 1791 (bank). Prose says the Berards fled unrest four years before the revolution began.
- SOFTENING GAP (bank s5): bank never says who fought the Haitian Revolution (enslaved people rising against enslavers). Prose says only "a revolution began". Audit should add it to the bank.
- Personification repaired from bank s5: "War slowed immigration" and the 1808 clause "a twenty-year protection for the trade". Prose: "Fewer people crossed ..." and "slave traders could legally bring captives ... for twenty more years".
- ADDED from bank (not in outline): 1787 Constitution 1808 clause, 1783 border and Native land line, Charming Sally 1791.
- Glosses (1750-1800): naturalization, Loyalists, orphan, unrest, free people of color, crypt, Venerable ("a title the Catholic Church gives to a person it is studying as a possible saint").
- Glosses (1500s): continental US = states other than Alaska and Hawaii; feast day; missionary.

- [T-237c, 1900-1950] OUTLINE SOFTENING/MINIMIZATION: outline gives Mexican Repatriation as "roughly 500,000 pressured or forced out, many U.S. citizens". Bank patch: range 500,000 to 2 million, about 60 percent US-born citizens. Prose gives the range and "most were US citizens", names Doak, Hoover, Visel, the county welfare officers, the stretcher removals, property sold, La Placita.
- [T-237c, 1900-1950] OUTLINE AGENTLESS: "the great wave ended", "gates shut", St. Louis "refused by Cuba, the United States, and Canada" (nations as actors). Prose names Johnson, Reed, Coolidge, Laredo Bru, Roosevelt, the State Department reply, Canadian officials. Passenger destinations written with passengers as subject, not "Britain took".
- [T-237c, 1900-1950] OUTLINE HELD BACK THE EUGENICS ARGUMENT: outline has no Laughlin, Grant or Coolidge "America must be kept American". Written from the patch. Sterilization kept to one sentence with its definition (health / rights-movements lead). Bank gives no surgical method beyond "surgery"; prose says surgery only.
- [T-237c, 1900-1950] Bank self-inconsistency (Angel Island Board of Special Inquiry): listed as "two inspectors, a stenographer and a translator" then "two of the three board members had to agree". Prose names the four roles and leaves out the voting rule.
- [T-237c] Glosses (1900-1950, general knowledge, definitions only): quota, melting pot, steerage, Sicily belongs to Italy, Thrace = region divided among Greece, Turkey, Bulgaria, Piraeus = port city of Athens, underage, detainee, dormitory, trachoma (bank), genitals, stenographer, deport, war bride, census, homogeneity (bank), feeblemindedness etc. = old words, sterilization (bank), Hitler "later ruled Germany", Mexican Revolution = a war in Mexico, repatriation, Great Depression, relief, bracero = Spanish for a man who works with his arms, refugee, Holocaust = murder of Jews and others by the Nazis, displaced persons.

## Log

<!-- date-time | unit | words | validator | --punct -->
- 2026-09-26 | 8 1900-1950 (T-237c) | ~2,300 prose, 6 spans, 3 stories | 0 errors (--part), 3 stories | emdash=0 semicolon=0
- 2026-09-26 | 7 1850-1900 revised from patched bank (T-237b2) | Bloody Monday in Know-Nothing span, railroad pay/strike/deaths (50 to 1,200, no record), new span Attacks on Chinese immigrants 1871-1887, pogroms/May Laws (Ignatiev, Alexander III). Part now 5,300 words (was 2,808) | 0 errors (--part) | emdash=0 semicolon=0
- 2026-09-26 | 6 1800-1850 revised from patched bank (T-237b2) | new span Mobs against Catholics 1834/1844, famine span rebuilt (exports, Russell, Trevelyan, quarter-acre, evictions, 1-1.5M range, coffin ships) | 0 errors (--part) | emdash=0 semicolon=0
- 2026-09-26 | part2 self-review done (T-237b) | 2,470 prose words, avg sentence 13.2 | 0 errors (--part), 6 stories | emdash=0 semicolon=0
- 2026-09-26 | 7 1850-1900 (T-237b) | ~1,670 prose | 0 errors (--part), 6 stories total | emdash=0 semicolon=0
- 2026-09-26 | 6 1800-1850 (T-237b) | ~800 prose | 0 errors (--part), 2 stories | emdash=0 semicolon=0
- 2026-09-26 | 1 before-1500 | ~230 prose | 0 errors (--part) | emdash=0 semicolon=0
- 2026-09-26 | 2 1500s | ~380 prose | 0 errors (--part) | emdash=0 semicolon=0
- 2026-09-26 | part1 self-review done | 3,180 prose words, avg sentence 13.1 | 0 errors (--part), 6 stories | emdash=0 semicolon=0
- 2026-09-26 | 5 1750-1800 | ~900 prose | 0 errors (--part), 6 stories total | emdash=0 semicolon=0
- 2026-09-26 | 4 1700-1750 | ~800 prose | 0 errors (--part), 4 stories total | emdash=0 semicolon=0
- 2026-09-26 | 3 1600s | ~1,450 prose | 0 errors (--part), 3 stories | emdash=0 semicolon=0
