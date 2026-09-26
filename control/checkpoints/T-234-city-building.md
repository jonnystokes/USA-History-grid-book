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

NOW:    T-234a working on part 1, unit 3 (era 1600s).
NEXT:   part 1, era 1600s.

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
| 3 | part1 era 1600s | working | |
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

- (none taken for eras before-1500, 1500s)

## Decisions and known gaps

<!-- Rule conflicts settled, and how. Defects beyond style found and fixed (these go to
     AUDIT-QUEUE). Anything a successor must not undo. -->

- before-1500: the Chaco paragraph said "Those two dates measure different things" before the 1140s date had appeared (information-order defect, reads as a contradiction). Fixed: each date now says what it measures. Keep "prehistoric" on Monks Mound (bank flag 14).
- before-1500: "Four Corners country" defined as where Colorado, Utah, Arizona and New Mexico meet. This is a plain-geography definition, not from the bank.
- 1500s: era summary was metadiscourse plus a fragment triad. Rewritten as facts. Laws of the Indies imperatives recast as "had to" statements (no quotation, so no wording to keep). "Among the first" claim attributed to writers on town-planning history (bank: ArchDaily, scholarly literature).

## Log

<!-- One line per save: date-time | unit | what landed | validator result | --punct result -->

- 2026-09-26 | 1 before-1500 | era revised to v2 | 0 errors | era clean (file still has later-era marks)
- 2026-09-26 | 2 1500s | era revised to v2 | 0 errors | era clean
