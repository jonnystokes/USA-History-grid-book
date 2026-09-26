# CHECKPOINT T-233 | native-nations | prose (v2 revision) | all 10 eras, 3 part files

<!-- The director fills the header and the unit list before dispatch. The agent keeps
     everything else current, and commits and pushes after every unit. Write it for a
     stranger who has only this file and the repo. -->

STATUS: IN-FLIGHT (part 1 DONE and verified by the director 2026-09-26. T-233b working on part 2. Part 3 to go)
VERIFY: python tools/project_state.py --check native-nations --stage prose
        (per part: python tools/project_state.py --punct manuscript/native-nations/<part>.md)
BRIEF:  standard REVISION brief (control/RESUME.md) + cloud lines (control/CLOUD-WORKFLOW.md §5)
FILES:  manuscript/native-nations/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md
        (read-only sources: outlines/native-nations.md · research/research-native-nations.md)
PLAN:   one agent per part file. T-233a = part 1, T-233b = part 2, T-233c = part 3.

NOW:    T-233b: unit 6 landed. Working on unit 7 (part 2, era 1850-1900).
NEXT:   part 2, era 1850-1900.

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
| 7 | part2 era 1850-1900 | working | T-233b |
| 8 | part3 era 1900-1950 | todo | |
| 9 | part3 era 1950-2000 | todo | |
| 10 | part3 era 2000-today | todo | |

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

## Log

<!-- One line per save: date-time | unit | what landed | validator result | --punct result -->
- 2026-09-26 | unit 1 before-1500 | full v2 revision of era zoom + 2 spans | 0 errors | file emdash=22 semicolon=8 (era before-1500 has 0)
- 2026-09-26 | unit 2 1500s | full v2 revision of era zoom, entradas, Paquiquineo story, Acoma span | 0 errors | file emdash=18 semicolon=6 (era 1500s has 0)
- 2026-09-26 | unit 3 1600s | full v2 revision of both era zooms, 4 spans, Metacom and Po'pay stories | 0 errors | file emdash=10 semicolon=3 (era 1600s has 0)
- 2026-09-26 | unit 4 1700-1750 | full v2 revision of era zoom, 4 spans, Canasatego story | 0 errors | file emdash=6 semicolon=1 (era 1700-1750 has 0)
- 2026-09-26 | unit 5 1750-1800 | full v2 revision of era zoom, 4 spans, Little Turtle story | 0 errors | file emdash=0 semicolon=0
- 2026-09-26 | part 1 self-review | definitions, era-opening variety, institution-subject pass | 0 errors | file emdash=0 semicolon=0
- 2026-09-26 | unit 6 1800-1850 (T-233b) | full v2 revision of era zoom, 4 spans, Tecumseh, Sequoyah, Neugin, Osceola stories | 0 errors | file emdash=21 semicolon=11 (era 1800-1850 has 0)
