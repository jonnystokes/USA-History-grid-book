# CHECKPOINT T-234 | city-building | prose (v2 revision) | all 10 eras, 3 part files

<!-- The director fills the header and the unit list before dispatch. The agent keeps
     everything else current, and commits and pushes after every unit. Write it for a
     stranger who has only this file and the repo. -->

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check city-building --stage prose
        (per part: python tools/project_state.py --punct manuscript/city-building/<part>.md)
BRIEF:  standard REVISION brief (control/RESUME.md) + cloud lines (control/CLOUD-WORKFLOW.md §5)
FILES:  manuscript/city-building/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md
        (read-only sources: outlines/city-building.md · research/research-city-building.md)
PLAN:   one agent per part file. T-234a = part 1, T-234b = part 2, T-234c = part 3.
MODEL:  native-nations (T-233) is the finished v2 example. Its three parts show the voice.

NOW:    T-234b landed unit 6 (part 2 era 1800-1850). Working on unit 7 (era 1850-1900).
NEXT:   part 2, era 1850-1900.

## Baseline before revision (measured 2026-09-26)

| part | prose words | em dashes | semicolons |
|---|---|---|---|
| part1-before-1800.md | 3,810 | 12 | 5 |
| part2-1800s.md | 4,238 | 23 | 6 |
| part3-1900s-and-today.md | 5,720 | 48 | 12 |

A large drop in words after revision is a warning sign of lost facts. The director compares.

## Units

| # | unit | state | landed (commit / note) |
|---|------|-------|------------------------|
| 1 | part1 era before-1500 | landed | v2 revision, T-234a |
| 2 | part1 era 1500s | landed | v2 revision, T-234a |
| 3 | part1 era 1600s | landed | v2 revision, T-234a |
| 4 | part1 era 1700-1750 | landed | v2 revision, T-234a |
| 5 | part1 era 1750-1800 | landed | v2 revision, T-234a, plus whole-file self-review |
| 6 | part2 era 1800-1850 | landed | v2 revision, T-234b |
| 7 | part2 era 1850-1900 | working | T-234b |
| 8 | part3 era 1900-1950 | todo | |
| 9 | part3 era 1950-2000 | todo | |
| 10 | part3 era 2000-today | todo | |

<!-- state: todo | working | landed | skipped (say why) -->

## Facts taken from the research bank

<!-- Fact, bank section, and the sentence it went into. -->

- (none taken for eras before-1500, 1500s)
- 1600s, bank "Fort towns" (MAAP/Columbia): Paulo d'Angola, Simon Congo and Anthony Portuguese are named as men who DUG the 1653 trench. The prose had named them only as 1644 half-freedom grantees and implied the link. Now stated.
- 1600s, bank "Fort towns": the 1644 grant's words "at present born or yet to be born", now quoted for the children. "North River" glossed as the Hudson (MAAP: "to the Hudson River"). Wall "reported complete" (bank) replaces "reported standing".
- 1600s, bank "Fort towns": Boston cow-path legend source named as Boston Magazine, 2018. Boston PD history pages as source for the watch as the start of the police.
- 1750-1800, bank "The land the capital was built on": Residence Act SIGNED July 16, 1790 (prose had "Congress passed" on that date, an institution-as-actor and a date error). Washington "rode" the country. Nameroughquena (west bank of the Potomac, opposite Theodore Roosevelt Island) and a third unnamed town on a northwest bluff, added to the three Native towns. The 245 figure attributed to the Smithsonian NMAAHC (whose site was part of Young's plantation), 260 to Histories of the National Mall (George Mason Univ.).
- 1750-1800, bank "L'Enfant": the Residence Act let the President appoint three commissioners (used to define "commissioners").
- 1750-1800, bank "Banneker": Silvio Bedini, the NPS and the Library of Congress named as the historians crediting Banneker with the boundary astronomy.
- 1750-1800, bank "Philadelphia's waterworks": 20,000 "fled" (prose had "left").
- 1800-1850, bank "Rochester": 1830 census figure 9,269 (prose had "about 9,200"). 12,630 dated to 1834, "the charter year" (prose had "mid-1830s"), now "By 1834, the year Rochester became a city". The prose's "fifteen years" became "more than eight times as many as in 1820" (1820 to 1834 is fourteen years, so "fifteen" was wrong).
- 1800-1850, bank "San Francisco": growth placed "during the California Gold Rush" (bank: Gold Rush references, "migration leads the rush").

## Decisions and known gaps

<!-- Rule conflicts settled, and how. Defects beyond style found and fixed (these go to
     AUDIT-QUEUE). Anything a successor must not undo. -->

- before-1500: the Chaco paragraph said "Those two dates measure different things" before the 1140s date had appeared (information-order defect, reads as a contradiction). Fixed: each date now says what it measures. Keep "prehistoric" on Monks Mound (bank flag 14).
- before-1500: "Four Corners country" defined as where Colorado, Utah, Arizona and New Mexico meet. This is a plain-geography definition, not from the bank.
- 1500s: era summary was metadiscourse plus a fragment triad. Rewritten as facts. Laws of the Indies imperatives recast as "had to" statements (no quotation, so no wording to keep). "Among the first" claim attributed to writers on town-planning history (bank: ArchDaily, scholarly literature).
- 1600s: "American town-builders copied it for the next two hundred years" is in the outline but NOT in the bank. Kept (no fact may leave), flagged for AUDIT-QUEUE.
- 1600s: the bank has nothing on which Native nations lived on the sites of Jamestown, Boston, New Amsterdam or Philadelphia, so the prose cannot name them. "Before the settlers arrived" now reads "before the English settlers arrived" so it does not imply empty land. Gap for AUDIT-QUEUE (land-erasure watch).
- 1600s: Wall paragraphs reordered so the workers stay the subject and the name of Wall Street comes first. Closing lines "The wall is long gone..." and "Nobody decided Boston's streets. Somebody decided Philadelphia's..." (antithesis, closing reversal) removed, their facts moved into earlier sentences.
- 1700-1750: span label "Fire, the city killer" personifies fire, but marker lines are frozen by the brief. Left as is, flagged for AUDIT-QUEUE.
- 1750-1800: era summary and span no longer withhold names ("a French-born engineer ... a free Black farmer" now L'Enfant, Ellicott, Banneker). "Washington looks like no other American city" cut as an unsourced superlative; the two-street-system fact kept. "workmen moved his body" became a passive: the bank says only "reinterred", with no actor. Closing moral "The idea lasted..." cut, and its fact kept as a plain sentence. Native deaths "in wars": the NPS page does not say who fought, and the prose says so. Tobacco "inspection house" glossed from the term itself, not from the bank.
- 1800-1850: LAND ERASURE fixed. Era summary said San Francisco had been "a stretch of empty coast"; the bank has about 200 people there in 1846. Now "a small coastal settlement". The bank names no Native nation at Rochester, Chicago, San Francisco or Manhattan, so the prose cannot name them. Gap for AUDIT-QUEUE.
- 1800-1850: claims in the prose NOT in the bank, kept and flagged for AUDIT-QUEUE: Chicago settled where "a short river met Lake Michigan"; cholera's bodily course (definition); "no piped water", wells beside privies; Randel's marker "at every corner of every future crossing"; Strong could "turn a tap" and "almost nobody in an American city" could bathe at home before; wheat in / flour out by canal.
- 1800-1850: "The men governing New York" decided on the Croton water: the bank names no official, so the prose says "New York's leaders" and names Jervis as the only person the records give. Strong's quotation split at its em dash with no word changed. Strong's closing lines ("That is the whole change in one household...") cut as a closing reversal; their facts (41 miles, parade) stand in the span. "While the water came nearer his part of town" became "while the water was still on its way" (the quotation itself says it was flowing towards the city).
- 1700-1750: "London ... hundreds of thousands" and "volunteer fire companies ... for the next hundred years" are in the outline/prose, not in the bank. Kept, flagged for AUDIT-QUEUE.

## Log

<!-- One line per save: date-time | unit | what landed | validator result | --punct result -->

- 2026-09-26 | 1 before-1500 | era revised to v2 | 0 errors | era clean (file still has later-era marks)
- 2026-09-26 | 2 1500s | era revised to v2 | 0 errors | era clean
- 2026-09-26 | 3 1600s | era revised to v2 | 0 errors | era clean
- 2026-09-26 | 4 1700-1750 | era revised to v2 | 0 errors | era clean
- 2026-09-26 | 5 1750-1800 + whole-file self-review | revised to v2 | 0 errors | emdash=0 semicolon=0
- 2026-09-26 | 6 1800-1850 | era revised to v2 (T-234b) | 0 errors | era clean (file still has era-07 marks: emdash=16 semicolon=6)
