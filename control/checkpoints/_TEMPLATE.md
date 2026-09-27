# CHECKPOINT T-<nnn> | <slug> | <research | patch | bankcheck | prose | check | fix | gaps> | <scope, e.g. eras 1-7>

<!-- Copy to control/checkpoints/T-<nnn>-<slug>.md. The director fills the header and the unit
     list before dispatch. The agent keeps everything else current and updates it after every
     unit. No git: the director commits once the agent finishes. Write it for a stranger who
     has only this file and the repo. (Cloud version: control/archive/cloud/checkpoints/.) -->

STATUS: IN-FLIGHT            <!-- IN-FLIGHT | PARTIAL | DONE (the director sets the last two) -->
VERIFY: python tools/project_state.py --check <slug> --stage <stage>
BRIEF:  control/briefs/<RESEARCH|WRITER|CHECKER|FIXER|GAPS|SALVAGE>.md
MODEL:  <opus | sonnet>
FILES:  outlines/<slug>.md · research/research-<slug>.md · manuscript/<slug>/...

NOW:    <the unit being worked on right now. Set this BEFORE starting it.>
NEXT:   <exactly what the next agent should do first>

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | era 01 before-1500 | todo | |
| 2 | era 02 1500s | todo | |

<!-- state: todo | working | landed | skipped (say why) -->

## SUBJECT NOTES (from the director)

<!-- Hard subjects to look for, perishable facts to refresh, neighbours' angles. -->

## Sources in hand

<!-- URL: what it settled. A successor re-reads these instead of re-searching. -->

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->

## OPEN (should be rare)

<!-- era | passage | what is missing | why it cannot be written honestly without it -->

## Outline claims left out

<!-- era | claim | why (not in bank, not quickly found, low value) -->

## Decisions and defects fixed

<!-- Defects found in the outline or bank and fixed in the prose (these go to AUDIT-QUEUE).
     Disputes recorded. Anything a successor must not undo. -->

## Log

<!-- One line per save: date-time | unit | what landed | validator | --punct -->
