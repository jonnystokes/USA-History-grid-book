# CHECKPOINT T-233 | native-nations | prose (v2 revision) | all 10 eras, 3 part files

<!-- The director fills the header and the unit list before dispatch. The agent keeps
     everything else current, and commits and pushes after every unit. Write it for a
     stranger who has only this file and the repo. -->

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check native-nations --stage prose
        (per part: python tools/project_state.py --punct manuscript/native-nations/<part>.md)
BRIEF:  standard REVISION brief (control/RESUME.md) + cloud lines (control/CLOUD-WORKFLOW.md §5)
FILES:  manuscript/native-nations/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md
        (read-only sources: outlines/native-nations.md · research/research-native-nations.md)
PLAN:   one agent per part file. T-233a = part 1, T-233b = part 2, T-233c = part 3.

NOW:    T-233a working on part 1. Units 1-3 landed. Unit 4 (era 1700-1750) next.
NEXT:   part 1, era 1700-1750.

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
| 4 | part1 era 1700-1750 | todo | |
| 5 | part1 era 1750-1800 | todo | |
| 6 | part2 era 1800-1850 | todo | |
| 7 | part2 era 1850-1900 | todo | |
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
- Canasatego named as the 1744 speaker (already in the file's 1700-1750 era; bank §4) -> Great Law span.

## Decisions and known gaps

<!-- Rule conflicts settled, and how. Defects beyond style found and fixed (these go to
     AUDIT-QUEUE). Anything a successor must not undo. -->
- Agent rule used throughout: the name of a people (the Comanche, the Oneida, the Acoma, the Haudenosaunee) names a group of persons and may act. The name of a state or institution (Spain, Britain, the United States, the colonies, Congress, a treaty, the Confederacy as a body) may not; the people who acted are named, or the text says the record does not name them.
- DEFECT FIXED (self-contradiction): the Paquiquineo record lines said "carried off" and "Taken in 1561" while the story says the records do not settle whether he went willingly. Record lines now say he left, and that the records do not say whether willingly.
- DEFECT FIXED (one-sided dispute): the Acoma paragraph gave only the historians who doubt the feet were cut off. Added Acoma's own account (right feet of 24 men, reported by the NYT 1998) from the bank. Also added the trial-location dispute and the APCG count of sixty children, which the prose had resolved silently.
- DEFECT FIXED (suspense): the 1500s horse paragraph withheld the word "horse" for a sentence. Now named first.
- NOT FIXED, for the director: bank Acoma §1 records the Pueblos' account that Zaldivar's soldiers assaulted (per the Rio Grande Sun, raped) an Acoma woman. The bank says the director decides how the book states it. The prose still gives only the demand for food. Park in AUDIT-QUEUE.
- DEFECT FIXED (self-contradiction): Cahokia was said to be lived in "to about 1400" and its people "gone by about 1350". Bank §1 gives both (occupied ~700-1400, dispersed by ~1350). Prose now says the people had scattered by about 1350 and nobody lived there by about 1400.

## Log

<!-- One line per save: date-time | unit | what landed | validator result | --punct result -->
- 2026-09-26 | unit 1 before-1500 | full v2 revision of era zoom + 2 spans | 0 errors | file emdash=22 semicolon=8 (era before-1500 has 0)
- 2026-09-26 | unit 2 1500s | full v2 revision of era zoom, entradas, Paquiquineo story, Acoma span | 0 errors | file emdash=18 semicolon=6 (era 1500s has 0)
- 2026-09-26 | unit 3 1600s | full v2 revision of both era zooms, 4 spans, Metacom and Po'pay stories | 0 errors | file emdash=10 semicolon=3 (era 1600s has 0)
