# CHECKPOINT T-<nnn> | <slug> | <research | patch | prose> | <scope, e.g. eras 5-10>

<!-- Copy to control/checkpoints/T-<nnn>-<slug>.md. The director fills the header and the unit
     list before dispatch; the agent keeps everything else current, and commits and pushes after
     every unit. Write it for a stranger who has only this file and the repo. -->

STATUS: IN-FLIGHT            <!-- IN-FLIGHT | PARTIAL | DONE (the director sets the last two) -->
VERIFY: python tools/project_state.py --check <slug> --stage <stage>
BRIEF:  standard <research|writing> brief (control/RESUME.md) + cloud lines (control/CLOUD-WORKFLOW.md §5)
FILES:  outlines/<slug>.md · research/research-<slug>.md · manuscript/<slug>/...

NOW:    <the unit being worked on right now. Set this BEFORE starting it, and push.>
NEXT:   <exactly what the next agent should do first>

## Units

| # | unit | state | landed (commit / note) |
|---|------|-------|------------------------|
| 1 | era 05 1750-1800 | todo | |
| 2 | era 06 1800-1850 | todo | |

<!-- state: todo | working | landed | skipped (say why) -->

## Sources in hand (research/patch only)

<!-- URL: what it settled. A successor re-reads these instead of re-searching. -->

## Decisions and known gaps

<!-- Facts left out rather than hedged. Disputes recorded. Defects found in the outline or
     bank and fixed in the prose (these go to AUDIT-QUEUE). Anything a successor must not undo. -->

## Log

<!-- One line per save: date-time | unit | what landed | validator result -->
