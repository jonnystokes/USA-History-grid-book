# REVIEW-FIX brief: the one improvement pass after the reader review (model: opus)

The dispatch gives you a TASK id, a review GROUP, its chapters (one or two; R01 also has the
front matter) and the group's review file `control/review/<GROUP>.md`. Sonnet readers read the finished book as
a 12-year-old with ADHD would and listed what made them stop, get lost or get bored. You make ONE
pass over those findings. There is no second review: what you leave is what the book prints.

## Read first

1. `control/writing-style-guide.md`, `control/ARCHITECTURE-GUIDE.md`,
   `control/general-writing-style-guide.md`, `control/hard-subjects-policy.md` (all BINDING).
2. The review file, one chapter section at a time. Finish one chapter before you start the next.
3. For each finding, the passage in `manuscript/<slug>/part*.md` and enough around it to judge.
   Read only what a finding needs: there is no need to reread the whole chapter.

## How to judge a finding

A finding is a reader's report, not an order. Fix it when the reader is right and the fix makes
the chapter better under the guides. Skip it when it asks for softening, contradicts the guides,
asks for a fact that is not in the chapter or the bank, or is a matter of taste. Never shrink a
worked passage into a summary (DECISIONS #52). Never change a marker line, era id, story slug or
record key. Add no fact that is not already in the chapter or `research/research-<slug>.md`. When a finding
needs a fact your bank lacks, copy it into your bank as a PATCH from another chapter's bank (with
its source line), or after a few searches with a source, as CLAUDE.md allows writers; then write it.

## Rules

- Edit only your chapters' part files, their banks (PATCH only) and their `control/backmatter/<slug>.md` (keep the hand-off
  in step if you change a glossary explanation, a date, a question or an answer). R01 may also
  edit `manuscript/_frontmatter/*.md` and `manuscript/_introduction/*.md`. No git, no installs,
  no sub-agents.
- After each part file you save: `node tools/validate_grid.js <file> --part` (0 errors) and
  `python tools/project_state.py --punct <file>` (0/0). Before you report:
  `python tools/project_state.py --check <slug> --stage prose` must PASS for each chapter.
- Keep a short list in `control/checkpoints/<TASK>-reviewfix.md`: each finding, fixed or skipped,
  and a reason of a few words for each skip.

## Report (under 150 words)

Findings fixed, findings skipped (with the reasons in a word or two each), and the `--check` line.
