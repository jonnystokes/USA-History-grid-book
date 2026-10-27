# BACKMATTER-HANDOFF brief: back-matter notes for the three pilot chapters (model: opus)

The three pilot chapters (exploration, government-politics, holidays) finished their readability
edit before the back-matter hand-off was added to the brief, so they have no
`control/backmatter/<slug>.md` yet. Write the three files.

## Read first

`control/briefs/READABILITY.md`, section "Hand-off for the back matter": it gives the six `##`
sections and the exact line format. Then each chapter's `manuscript/<slug>/part*.md` in full.

## Rules

- One file per chapter: `control/backmatter/exploration.md`, `control/backmatter/government-politics.md`,
  `control/backmatter/holidays.md`. Edit nothing else. No git, no installs, no sub-agents.
- Everything in a hand-off must already be in the chapter, worded as the chapter gives it. Era
  labels as the chapter prints them. The five closing dates come first under `## Dates`.
- `python tools/project_state.py --punct <file>` must show 0/0 for each file.
- Check your format against any other hand-off already in `control/backmatter/` if one exists.

## Report (under 150 words)

Items per section per chapter, and anything you could not settle.
