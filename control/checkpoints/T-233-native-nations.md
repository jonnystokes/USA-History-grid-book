# CHECKPOINT T-233 | native-nations | prose (v2 revision) | all 10 eras, 3 part files

<!-- The director fills the header and the unit list before dispatch. The agent keeps
     everything else current, and commits and pushes after every unit. Write it for a
     stranger who has only this file and the repo. -->

STATUS: DONE (2026-09-26. The director ran the prose check: PASS.)
VERIFY: python tools/project_state.py --check native-nations --stage prose
        (per part: python tools/project_state.py --punct manuscript/native-nations/<part>.md)
BRIEF:  standard REVISION brief (control/RESUME.md) + cloud lines (control/CLOUD-WORKFLOW.md §5)
FILES:  manuscript/native-nations/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md
        (read-only sources: outlines/native-nations.md · research/research-native-nations.md)
PLAN:   one agent per part file. T-233a = part 1, T-233b = part 2, T-233c = part 3.

NOW:    T-233c done. Part 3 (units 8-10) landed and self-reviewed. Chapter prose check PASS.
NEXT:   chapter complete. Director runs the prose check.

## Baseline before revision (measured 2026-09-26)

| part | prose words | em dashes | semicolons |
|---|---|---|---|
| part1-before-1800.md | 4,592 | 28 | 9 |
| part2-1800s.md | 3,697 | 27 | 18 |
| part3-1900s-and-today.md | 4,537 | 19 | 13 |

A large drop in words after revision is a warning sign of lost facts. The director compares.

## Units

| # | unit | state | landed (commit / note) |
|---|------|-------|------------------------|
| 1 | part1 era before-1500 | landed | commit T-233a before-1500 |
| 2 | part1 era 1500s | landed | commit T-233a 1500s |
| 3 | part1 era 1600s | landed | commit T-233a 1600s |
| 4 | part1 era 1700-1750 | landed | commit T-233a 1700-1750 |
| 5 | part1 era 1750-1800 | landed | commit T-233a 1750-1800 |
| 6 | part2 era 1800-1850 | landed | commit T-233b 1800-1850 |
| 7 | part2 era 1850-1900 | landed | commit T-233b 1850-1900 |
| 8 | part3 era 1900-1950 | landed | commit T-233c 1900-1950 |
| 9 | part3 era 1950-2000 | landed | commit T-233c 1950-2000 |
| 10 | part3 era 2000-today | landed | commit T-233c 2000-today |

<!-- state: todo | working | landed | skipped (say why) -->

## Facts taken from the research bank

<!-- Fact, bank section, and the sentence it went into. -->
- Ubelaker's estimate dated 1976, Dobyns's 1983 (bank §1 Population) -> era before-1500 zoom, population paragraph.
- Dobyns's area given as "north of Mexico" instead of the undefined "north of Mesoamerica" (bank §1 Population frames the whole 1-18 million range as north of Mexico).
- "Often called one of the oldest continuing governments" attributed to its sources, Library of Congress law blog and PBS Native America (bank §1 Haudenosaunee, third bullet) -> Great Law span.
- 1500s (bank §2 and Acoma section): Paquiquineo "appeared before" Philip II and spent nine years "trying to get home" (bank §2 featured person); Onate's colonists brought horses to New Mexico in 1598 (bank §2 horse). Acoma: Juan de Zaldivar was Onate's nephew and Vicente his brother (Acoma §1); Onate gathered the Acoma elders for the ceremony of submission (Acoma §1); the friars' answer quoted, "possessed both the authority and sufficient cause" (Acoma §1, Carlson citing Simmons); the town burned "much of it" (Acoma §1, NPS); trial location disputed, Santo Domingo vs San Juan Pueblo (Acoma §3); children under 12 handed to the friars (Acoma §3, Carlson); APCG count of sixty children, none returned (Acoma §3); Acoma oral account of the right feet of 24 men, NYT 1998 (Acoma §0/§3); Mexico City exile four years, one source five (Acoma §5); Onate's sentence on the two Hopi men stated as a sentence (Acoma §3 table).
- 1600s: each TRIBE (not town) under its own weroance (bank §3 Tsenacommacah; the prose said "town", corrected to the bank). Covenant Chain made official by Haudenosaunee leaders and Governor Andros (bank §3). "Victors" as the parties of the Treaty of Hartford (bank §3, "handed survivors to the victors"). Metacom's captives sold "to pay the war's costs" -> named as colonial officials, an inference from that purpose (bank §3). Pueblo Revolt "most successful" label attributed to historians (bank §3 sources). Beaver Wars fought "west and north" (bank §3).
- 1700-1750: Haudenosaunee neutrality "used for half a century to bargain with both sides" (bank §4 Play-off). "Slave raids" as a cause of the Tuscarora War, raiders unnamed (bank §4).
- 1750-1800: Washington's Haudenosaunee name Conotocaurius (bank §5 Revolution); the Seneca address dated 1790 (bank §5); "ratified" defined as formally approved.
- Canasatego named as the 1744 speaker (already in the file's 1700-1750 era; bank §4) -> Great Law span.
- 1800-1850 (T-233b): Tenskwatawa was known as "the Prophet", hence Prophetstown (bank §6 Tecumseh); the 1811 fight named as the Battle of Tippecanoe and the burning dated November 8 (bank §6); Library of Congress lists Sequoyah's birth as 1770 with a question mark (bank §6 Cherokee renaissance); the Seminole war named as the Second Seminole War (bank §6 Seminole).
- 1850-1900 (T-233b): the Long Walk named (bank §7 wars); Sand Creek Massacre National Historic Site (bank §7, NPS source); Britannica entry titled "Wounded Knee Massacre" (bank §7); soldier crossfire attributed to Britannica and History.com (bank §7); Nez Perce distance "up to about 1,700 miles" in some accounts (bank §7 After and Disputes 5); Pratt's line misquoted as "kill the Indian, save the man", recorded words printed in the conference's official report (bank §7 schools); punishments tied to speaking one's language, and survivor accounts as a second source (bank §7 On arrival); outing system in summers and school terms (bank §7); burial sites "marked and unmarked" (bank §7 Scale); Meriam Report dated 1928 (bank §7 Half-day labor); Zitkala-Sa named as a student who turned the schooling against the policy (bank §7 other half); Wovoka from the Walker Lake country of Nevada (bank §7 Wounded Knee).
- 1900-1950 (T-233c): Osage Allotment Act named for "a law of 1906" (bank §8 Osage); Collier's term 1933-1945 (bank §8 Citizenship); Meriam Report full title *The Problem of Indian Administration* (bank §8); *High Steel* directed by Don Owen, used to repair "the Film Board made" (bank Parked, Kahnawake line); half-day labor tied to school staff, and Nez's punishment tied to Fort Defiance staff (bank §7 On arrival / §8, policy §6b usage).
- 1950-2000 (T-233c): Custer's 1874 expedition announced gold, and officials ignored the 1868 treaty (bank §7 wars, line "1874") -> Black Hills span; Lakota "refused" the money (bank Parked, Mount Rushmore line); Wounded Knee 1890 toll, between 250 and 300 Lakota killed by the 7th Cavalry (bank §7, already in part 2) -> 1973 occupation now says why the village was chosen; AIM patrols were "against police abuse" (bank §9); ICWA standards meant to keep Native children with Native families, and "a large share" of children removed (bank §9); Kennedy Report named, begun under Robert F. Kennedy and finished under Edward Kennedy (bank §9).
- 2000-today (T-233c): Carlisle cemetery returns attributed to Army officials digging up and returning children (bank §10, "the Army has been disinterring"); burial sites at 53 schools "marked and unmarked" (bank §10 Vol. 1); Pūnana Leo dates attributed to ʻAha Pūnana Leo's official history (bank §10, "attribute the arc"). All source years in the era kept (2004, 2016, 2017, 2018, 2020, 2021, 2022, 2023, 2024, 2025, 1984, 1986, 1987, 1993, 1663, 2010, 1908).

## Decisions and known gaps

<!-- Rule conflicts settled, and how. Defects beyond style found and fixed (these go to
     AUDIT-QUEUE). Anything a successor must not undo. -->
- Agent rule used throughout: the name of a people (the Comanche, the Oneida, the Acoma, the Haudenosaunee) names a group of persons and may act. The name of a state or institution (Spain, Britain, the United States, the colonies, Congress, a treaty, the Confederacy as a body) may not; the people who acted are named, or the text says the record does not name them.
- DEFECT FIXED (self-contradiction): the Paquiquineo record lines said "carried off" and "Taken in 1561" while the story says the records do not settle whether he went willingly. Record lines now say he left, and that the records do not say whether willingly.
- DEFECT FIXED (one-sided dispute): the Acoma paragraph gave only the historians who doubt the feet were cut off. Added Acoma's own account (right feet of 24 men, reported by the NYT 1998) from the bank. Also added the trial-location dispute and the APCG count of sixty children, which the prose had resolved silently.
- DEFECT FIXED (suspense): the 1500s horse paragraph withheld the word "horse" for a sentence. Now named first.
- DEFECT FIXED (false statement): the 1700-1750 era zoom called the Comanche a "confederacy" ("Confederacies grew... Another built the strongest power on the southern Plains"). The bank never calls the Comanche a confederacy. Prose now names the Haudenosaunee and the Comanche separately.
- DEFECT FIXED (self-contradiction): the 1750-1800 era zoom said "When the fighting ended, the United States began making treaties", but the span dates the first treaty to September 1778, during the war. Zoom now says "During the war, in 1778".
- RULE CONFLICT SETTLED: the 1790 Seneca quotation contains a semicolon ("Town-destroyer; and to this day"). Zero semicolons (V2) vs quoting exactly. Settled by quoting the words unchanged in two parts with "they said" between them, so no word changes and no semicolon remains.
- Whole-file self-review (V2 Self-Review + amendment §5) done on part 1: hard words defined at first use (friar, convent, treaty, coalition, delegates, diplomats, refugees, minutes, legion, banished); era openings varied so the five eras no longer all open on a date phrase; marker lines, record keys and hb-note verified byte-identical to the pre-revision file. File words 4,962 -> 5,750 (whole file incl. markers).
- NOT FIXED, for the director: bank Acoma §1 records the Pueblos' account that Zaldivar's soldiers assaulted (per the Rio Grande Sun, raped) an Acoma woman. The bank says the director decides how the book states it. The prose still gives only the demand for food. Park in AUDIT-QUEUE.
- DEFECT FIXED (self-contradiction): Cahokia was said to be lived in "to about 1400" and its people "gone by about 1350". Bank §1 gives both (occupied ~700-1400, dispersed by ~1350). Prose now says the people had scattered by about 1350 and nobody lived there by about 1400.
- T-233b DEFECT FIXED (suspense + false framing): the 1800-1850 era zoom withheld the law's name until its last paragraph ("the United States answered both of them with the same law") and framed the Removal Act as the answer to Tecumseh's confederacy, though the file's own span shows that confederacy ended in war in 1811-1813. Zoom now states up front that both ways failed and gives each outcome.
- T-233b NOTE (not changed): the Removal span says Cherokee leaders took their fight with Georgia to the courts, then cites Worcester v. Georgia. The bank does not name the parties to Worcester. The prose no longer implies the Cherokee Nation was the party in that case, but a successor must not add the party from memory.
- T-233b DEFECT FIXED (self-contradiction): the 1850-1900 era zoom said "beginning in 1879 the government built a system of boarding schools", while the schools span dates the federal schools 1819-1969. Zoom now says Pratt opened the first federal boarding school built far from the reservations in 1879 and officials used it as the model.
- T-233b DEFECT FIXED (minimization): Chief Joseph story said only "some accounts give a longer distance". Now gives the bank's upper figure, about 1,700 miles.
- T-233b DEFECT FIXED (imprecise word / softening): Sand Creek and Wounded Knee were told without the word massacre. Added the NPS site name and the Britannica entry title, with "massacre" defined.
- T-233b DEFECT FIXED (evaluative/meta): era zoom opened "These fifty years are the hardest in this chapter" and closed on "how to keep a people alive" (banned phrase). Replaced with the facts and three dated examples of leaders' choices.
- T-233b RULE DECISION: where the bank names no actor for a harm (the Mankato hanging, Crazy Horse's killing, who took Zitkala-Sa, who promised and who overruled Joseph's return), the prose states that the sources do not identify them, following T-233a. The group-name rule from T-233a (a people may act, an institution may not) is kept. Sources and reports take only approved verbs (states, lists, records, identifies).
- T-233b NOTE: the final era zoom's closing clause "the number the next century starts from" was cut as a closing line. Part 3 era 1900-1950 must open from the 1900 low point itself if it wants that link.
- Part 2 self-review done (V2 Self-Review + amendment §5): marker lines and record keys verified identical to pre-revision; prose words 3,670 -> about 4,500; average sentence about 14 words; hard words defined at first use (confederacy, void, syllabary, constitution, abolished, sovereignty, flag of truce, condemned, federal, recognized, reservation, military commission, interpreter, reprieved, mass execution, massacre, cavalry, bayonet, agency, allotment, surplus, rider, rations, annuities, Commissioner, Indian agent, solitary confinement, autobiography, copyright, uprising, disarming, band, carbine).
- T-233c DEFECT FIXED (false statement): era 1900-1950 zoom said "in both [wars] the United States sent orders in Native languages". Per the file's own span, Choctaw soldiers began it in 1918 and Marine officers recruited Navajo in 1942. Zoom now names both.
- T-233c DEFECT FIXED (agentless harm): Osage killers now stated as unnamed by the sources (bank names none). The 1930s taking of children now states the sources do not say who took them. Chester Nez punished by Fort Defiance staff (policy §6b wording).
- T-233c DEFECT FIXED (suspense): Chester Nez span ended on "the Marine Corps came looking for him", a line built to land. Now states that recruiters signed him up to build a code out of Navajo.
- T-233c DEFECT FIXED (unsupported claim): era 1950-2000 zoom called the Alcatraz occupiers "students". The bank names only Indians of All Tribes. Now says so.
- T-233c DEFECT FIXED (minimization): ICWA span dropped the bank's "a large share" of Native children removed, and the standards' purpose. Both restored. AIM patrols now say "against police abuse" (bank) instead of "watching the police".
- T-233c DEFECT FIXED (overstated win): era zoom said nations "carried treaties into federal court and won" without saying what the Lakota won. Now says the justices ruled the taking broke the treaty (compensation, not land, in the span).
- T-233c NOTE: Wounded Knee 1973: bank says two occupiers "died"; the file said "were killed". Kept "killed" (no fact removed) and added that the sources used do not say who killed them. Director may check.
- T-233c RULE CONFLICT SETTLED: the Kennedy Report title contains an em dash (*Indian Education: A National Tragedy [dash] A National Challenge*). Zero em dashes vs exact title. Settled by keeping every word and replacing the dash with a comma, as T-233a did for the Seneca semicolon.
- T-233c DEFECT FIXED (false statement): Standing Rock span said the pipeline ran "above [the reservation's] water supply". Bank: Lake Oahe IS the water supply. Now says the route ran under the lake, which is the water supply.
- T-233c DEFECT FIXED (gnomic line + closing reversal): "Languages come home" opened on "The direct answer to a school that punished a language is a school that teaches in it" and closed on the war-and-classroom callback. The code-talker fact moved to the front as a plain statement; the span ends on the immersion schools.
- T-233c NOTE: Haaland's grandparents "taken to boarding school": bank gives no actor, so the prose says the sources do not say who took them.
- Part 3 self-review done (T-233c, V2 Self-Review + amendment §5): marker lines and record keys verified identical to pre-revision; prose about 5,400 words (baseline 4,537), average sentence 14.1 words; "members of Congress passed" openings varied; stock phrase "the sources used for this chapter" varied; document subjects checked for approved verbs (report states/records/lists/identifies, treaty states, opinion's first sentence is); hard words defined (headright, guardian, suspicious death, structural iron, rivet, civil rights, delegates, trust land, constitution, day school, code talker, runner, secure, classified, pentathlon, decathlon, professional, paratrooper, exposure, memoir, resolution, termination, proceedings, occupy, proclamation, settle, corporation, marshals, fish-in, harvestable, co-managers, upheld, compensation, interest, self-determination, gaming, compact, repatriation, subcommittee, coercive assimilation, principal chief, federally recognized, enrolled, sovereignty, disestablish, federal criminal law, pipeline, easement, wildlife refuge, solitary confinement, immersion, Indigenous, graduate school, reclamation, linguistics).

## Log

<!-- One line per save: date-time | unit | what landed | validator result | --punct result -->
- 2026-09-26 | unit 1 before-1500 | full v2 revision of era zoom + 2 spans | 0 errors | file emdash=22 semicolon=8 (era before-1500 has 0)
- 2026-09-26 | unit 2 1500s | full v2 revision of era zoom, entradas, Paquiquineo story, Acoma span | 0 errors | file emdash=18 semicolon=6 (era 1500s has 0)
- 2026-09-26 | unit 3 1600s | full v2 revision of both era zooms, 4 spans, Metacom and Po'pay stories | 0 errors | file emdash=10 semicolon=3 (era 1600s has 0)
- 2026-09-26 | unit 4 1700-1750 | full v2 revision of era zoom, 4 spans, Canasatego story | 0 errors | file emdash=6 semicolon=1 (era 1700-1750 has 0)
- 2026-09-26 | unit 5 1750-1800 | full v2 revision of era zoom, 4 spans, Little Turtle story | 0 errors | file emdash=0 semicolon=0
- 2026-09-26 | part 1 self-review | definitions, era-opening variety, institution-subject pass | 0 errors | file emdash=0 semicolon=0
- 2026-09-26 | unit 6 1800-1850 (T-233b) | full v2 revision of era zoom, 4 spans, Tecumseh, Sequoyah, Neugin, Osceola stories | 0 errors | file emdash=21 semicolon=11 (era 1800-1850 has 0)
- 2026-09-26 | unit 7 1850-1900 (T-233b) | full v2 revision of both era zooms, 5 spans, Sitting Bull, Chief Joseph, Winnemucca, Zitkala-Sa stories | 0 errors | file emdash=0 semicolon=0
- 2026-09-26 | part 2 self-review (T-233b) | agent verbs, source verbs, definitions, sentence length, story first/last lines | 0 errors | file emdash=0 semicolon=0
- 2026-09-26 | unit 8 1900-1950 (T-233c) | full v2 revision of era zoom, 6 spans, Thorpe, Hayes, Nez stories | 0 errors | file emdash=16 semicolon=7 (era 1900-1950 has 0)
- 2026-09-26 | unit 9 1950-2000 (T-233c) | full v2 revision of era zoom, 6 spans, Mankiller, Frank, Fortunate Eagle stories | 0 errors | file emdash=10 semicolon=2 (era 1950-2000 has 0)
- 2026-09-26 | unit 10 2000-today (T-233c) | full v2 revision of era zoom, 4 spans, Haaland, Baird stories | 0 errors | file emdash=0 semicolon=0
- 2026-09-26 | part 3 self-review (T-233c) | opening variety, stock phrases, document verbs, definitions | 0 errors | file emdash=0 semicolon=0 | chapter --check prose: PASS
