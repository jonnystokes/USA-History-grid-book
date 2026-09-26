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

NOW:    T-237a writing part1 era 1600s.
NEXT:   write part1 era 1600s (append to manuscript/immigration/part1-before-1800.md).

## Units

| # | unit | state | landed (commit / note) |
|---|------|-------|------------------------|
| 1 | part1 era before-1500 (thin) | landed | file created, era written |
| 2 | part1 era 1500s (thin) | landed | era written |
| 3 | part1 era 1600s | working | |
| 4 | part1 era 1700-1750 | todo | |
| 5 | part1 era 1750-1800 | todo | |
| 6 | part2 era 1800-1850 | todo | |
| 7 | part2 era 1850-1900 | todo | |
| 8 | part3 era 1900-1950 | todo | |
| 9 | part3 era 1950-2000 | todo | |
| 10 | part3 era 2000-today | todo | |

## Outline claims NOT in the bank (left out, per DECISIONS #13)

<!-- The claim, the outline line, and where it would have gone. -->

- "small and often in danger" (St. Augustine, outline 1500s span, line 30). Bank does not say it. Left out of 1500s span.

## Defects in the outline or bank, fixed in the prose (go to AUDIT-QUEUE)

- Glosses from general knowledge, not in the bank (word definitions only, no historical claim): "Norse" = sailors from northern Europe; Newfoundland "in what is now Canada"; land bridge = dry ground joining Asia to North America.
- LAND ERASURE GAP (bank): bank section 2 does not name the Native nation on whose land Menendez built St. Augustine, and section 3 names only the Powhatan for the 1600s colonies (no Wampanoag for Plymouth, no nation for Massachusetts Bay, New Amsterdam, Maryland or Pennsylvania). Prose states "on Native land" from the bank's general lines. Audit should add the nations to the bank.
- Glosses (1500s): continental US = states other than Alaska and Hawaii; feast day; missionary.

## Log

<!-- date-time | unit | words | validator | --punct -->
- 2026-09-26 | 1 before-1500 | ~230 prose | 0 errors (--part) | emdash=0 semicolon=0
- 2026-09-26 | 2 1500s | ~380 prose | 0 errors (--part) | emdash=0 semicolon=0
