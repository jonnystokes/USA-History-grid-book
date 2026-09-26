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

NOW:    T-233a dispatched on part 1. Unit 1 (era before-1500) not started.
NEXT:   part 1, era before-1500.

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
| 1 | part1 era before-1500 | todo | |
| 2 | part1 era 1500s | todo | |
| 3 | part1 era 1600s | todo | |
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

## Decisions and known gaps

<!-- Rule conflicts settled, and how. Defects beyond style found and fixed (these go to
     AUDIT-QUEUE). Anything a successor must not undo. -->

## Log

<!-- One line per save: date-time | unit | what landed | validator result | --punct result -->
