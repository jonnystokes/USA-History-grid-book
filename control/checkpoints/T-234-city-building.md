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

NOW:    T-234a working on part 1, unit 4 (era 1700-1750).
NEXT:   part 1, era 1700-1750.

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
| 4 | part1 era 1700-1750 | working | |
| 5 | part1 era 1750-1800 | todo | |
| 6 | part2 era 1800-1850 | todo | |
| 7 | part2 era 1850-1900 | todo | |
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

## Decisions and known gaps

<!-- Rule conflicts settled, and how. Defects beyond style found and fixed (these go to
     AUDIT-QUEUE). Anything a successor must not undo. -->

- before-1500: the Chaco paragraph said "Those two dates measure different things" before the 1140s date had appeared (information-order defect, reads as a contradiction). Fixed: each date now says what it measures. Keep "prehistoric" on Monks Mound (bank flag 14).
- before-1500: "Four Corners country" defined as where Colorado, Utah, Arizona and New Mexico meet. This is a plain-geography definition, not from the bank.
- 1500s: era summary was metadiscourse plus a fragment triad. Rewritten as facts. Laws of the Indies imperatives recast as "had to" statements (no quotation, so no wording to keep). "Among the first" claim attributed to writers on town-planning history (bank: ArchDaily, scholarly literature).
- 1600s: "American town-builders copied it for the next two hundred years" is in the outline but NOT in the bank. Kept (no fact may leave), flagged for AUDIT-QUEUE.
- 1600s: the bank has nothing on which Native nations lived on the sites of Jamestown, Boston, New Amsterdam or Philadelphia, so the prose cannot name them. "Before the settlers arrived" now reads "before the English settlers arrived" so it does not imply empty land. Gap for AUDIT-QUEUE (land-erasure watch).
- 1600s: Wall paragraphs reordered so the workers stay the subject and the name of Wall Street comes first. Closing lines "The wall is long gone..." and "Nobody decided Boston's streets. Somebody decided Philadelphia's..." (antithesis, closing reversal) removed, their facts moved into earlier sentences.

## Log

<!-- One line per save: date-time | unit | what landed | validator result | --punct result -->

- 2026-09-26 | 1 before-1500 | era revised to v2 | 0 errors | era clean (file still has later-era marks)
- 2026-09-26 | 2 1500s | era revised to v2 | 0 errors | era clean
- 2026-09-26 | 3 1600s | era revised to v2 | 0 errors | era clean
