# REVIEW-FIX brief: the one improvement pass after the reader review (model: fable)

The dispatch gives you a TASK id, a CHAPTER slug and the review file that covers it
(`control/review/<GROUP>.md`, your chapter's section only). Sonnet readers read the finished book as
a 12-year-old with ADHD would and listed what made them stop, get lost or get bored. You make ONE
pass over those findings. There is no second review: what you leave is what the book prints.

## Read first

1. `control/writing-style-guide.md`, `control/ARCHITECTURE-GUIDE.md`,
   `control/general-writing-style-guide.md`, `control/hard-subjects-policy.md` (all BINDING).
2. Your chapter's section of the review file.
3. For each finding, the passage in `manuscript/<slug>/part*.md` and enough around it to judge.

## How to judge a finding

A finding is a reader's report, not an order. Fix it when the reader is right and the fix makes
the chapter better under the guides. Skip it when it asks for softening, contradicts the guides,
asks for a fact that is not in the chapter or the bank, or is a matter of taste. Never shrink a
worked passage into a summary (DECISIONS #52). Never change a marker line, era id, story slug or
record key. Add no fact that is not already in the chapter or `research/research-<slug>.md`.

## Rules

- Edit only your chapter's part files and `control/backmatter/<slug>.md` (keep the hand-off in
  step if you change a glossary explanation, a date, a question or an answer). No git, no
  installs, no sub-agents.
- After each part file you save: `node tools/validate_grid.js <file> --part` (0 errors) and
  `python tools/project_state.py --punct <file>` (0/0). Before you report:
  `python tools/project_state.py --check <slug> --stage prose` must PASS.
- Keep a short list in `control/checkpoints/<TASK>-reviewfix.md`: each finding, fixed or skipped,
  and a reason of a few words for each skip.

## Report (under 150 words)

Findings fixed, findings skipped (with the reasons in a word or two each), and the `--check` line.
