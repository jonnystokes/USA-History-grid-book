# CHECKPOINT F5 | disasters | step 5 fixer, whole chapter

STATUS: T-469 landed (director verified: PASS  disasters / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/disasters/part1|part2|part3 + control/audit/disasters/part1|2|3-findings-sonnet.md
        + research/research-disasters.md (PATCH entries only)
SCRATCH: scratchpad/T-469 (bank slices bank-e<n>.md, verdict.py, p1/p2/p3.json verdict lists)

NOW:    done
NEXT:   none (director: commit)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after (wc -w) |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 85 / 1 / 0, found by fixer 2 | 7415 -> 7667 |
| part2 | 6-7 | DONE | 55 / 0 / 0, found by fixer 2 | 5027 -> 5345 |
| part3 | 8-10 | DONE | 124 / 4 / 0, found by fixer 0 | 11516 -> 11932 |

## NEEDS-RESEARCH
- None open. Facts the fixer could not confirm were cut or stated as unknown:
  - 1779 Galvez hurricane: day and where the ships lay (SEARCHED, NOT FOUND, PATCH era 05). Prose gives neither.
  - Pulaski: the counts disagree (168 aboard vs 128 dead + 59 saved). Prose says the records disagree. Round 2 could settle it.
  - Palisades Fire: retrial set for November 2, 2026 (LAist, August 19, 2026). Step 6/7 must refresh the case status.

## Log
- part1 era 1: 9 findings, 9 FIXED. PATCH era 01 (Crater Lake filling, Crow Canyon location, Chaco in NM). validate 0 errors, punct 0/0.
- part1 era 2: 18 findings, 18 FIXED, 1 found by fixer (F1). PATCH era 02 (St. Augustine founding 1565, Timucua reason). Checks clean.
- part1 era 3: 18 findings, 18 FIXED. PATCH era 03 (Bradford governor, Thacher Island + Elizabeth, swab pole, USGS magnitude). Checks clean.
- part1 era 4: 23 findings, 22 FIXED, 1 REJECTED (#63 Mather quote), 1 found by fixer (F2). PATCH era 04 (1715 departure dispute, fire wards, Union bags). Checks clean.
- part1 era 5: 18 findings, 18 FIXED. PATCH era 05 (1776 weather; SEARCHED NOT FOUND for the 1779 hurricane date). Checks clean. PART 1 DONE.
- part2 era 6: 25 findings, 25 FIXED. PATCH era 06 (Erie route, painters' first stop). Checks clean.
- part2 era 7: 30 findings, 30 FIXED, 2 found by fixer (F3, F4). PATCH era 07 (Chicago wood/wind/drought, Red Cross in DC, Signal Service, 1888 Census details, Johnstown rain). Checks clean. PART 2 DONE.
- part3 era 8: 46 findings, 46 FIXED. PATCH era 08 (Eastland, Caernarvon purpose, New London crawlspace, Hindenburg newsreels, Cocoanut Grove doors, Texas City fires, St. Francis location, Sullivan). Checks clean.
- part3 era 9: 40 findings, 37 FIXED, 3 REJECTED (#56, #67, #74: true facts, now banked). PATCH era 09 (Air Florida, Loma Prieta, Chenega Island, ANCSA, Johnston, TMI location). Checks clean.
- part3 era 10: 42 findings, 41 FIXED, 1 REJECTED (#105, true, now banked). PATCH era 10 (Palisades retrial status, Surfside 2018 report, Maria/Irma, PR citizenship). Checks clean. PART 3 DONE.
- Final: `python tools/project_state.py --check disasters --stage prose` PASS (manuscript=23558w by the tool's count, 0 errors, 0/0).
