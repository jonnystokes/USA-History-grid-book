# STRUCTURE-PASS brief: finish what the old grid rule blocked, and settle the director's fact items (model: opus)

The one fix pass after the reader review left some findings undone or done only in part, because
`control/ARCHITECTURE-GUIDE.md` section 2 then said no span or story may move, split or change its
label. Jon has relaxed it (DECISIONS #54): **within one era**, a span or story may move to a better
place in that era, a long span may be split into two spans, and a span's label may be reworded.
Nothing may leave its era, merge or be removed, and era ids, story slugs and record keys stay.

The dispatch gives you a TASK id, your chapters, the fix checkpoint(s) of your group
(`control/checkpoints/T-7xx-reviewfix.md`), the review file (`control/review/<GROUP>.md`) and,
sometimes, director fact items.

## Read first

`control/ARCHITECTURE-GUIDE.md` (section 2 as it now reads, and section 4), `control/writing-style-guide.md`,
`control/general-writing-style-guide.md`, `control/hard-subjects-policy.md`. Then your checkpoint(s): find
every finding marked skipped or done in part because a span or story could not move, a span could not be
split, or a heading on a marker line could not change. Read each one's finding in the review file and the
passage in `manuscript/<slug>/part*.md`.

## What to do

1. **Each blocked finding:** do it now if it makes the chapter better for its reader (8 to 15, often with
   ADHD): move the span or story within its era, split the long span (new
   `<!-- hb-zoom level="span" label="..." -->` and `<!-- /hb-zoom -->` lines, the new label plain and
   short), or reword the label. Where the earlier fixer added a bridge or a lead-in only to work around the
   old rule, keep it if it still helps and cut it if the move makes it redundant. If a finding still should
   not be done (it would move something between eras, or it no longer helps), leave it and say why.
2. **Card pointers:** when you reword or split a span that a card line names ("Five minutes?",
   "Can skip:"), update that card line so the quoted name matches the label exactly.
3. **Director fact items** (if the dispatch gives any): settle each from sources. Copy a fact from another
   chapter's research bank, or find it with a few searches, add it to your chapter's bank as a PATCH with
   its source line, then write it. Add no fact that is not in a bank.
4. **Do not change** any chapter closing's three answers (they must match the back matter word for word),
   any era strip's minutes, or anything outside your chapters' part files and their banks. Do not edit the
   back matter unless the dispatch says so; if one of your changes makes a back-matter line wrong, name the
   file and the line in your checkpoint and report.

## Checks

After each part file you save: `node tools/validate_grid.js <file> --part` (0 errors) and
`python tools/project_state.py --punct <file>` (0/0; it now counts labels too). Before you report:
`python tools/project_state.py --check <slug> --stage prose` must PASS for each chapter. Keep a short list
in `control/checkpoints/<TASK>-structure.md`: each finding and fact item, done or not, and why in a few
words. No git, no installs, no sub-agents. Do not run tools/build_full_book.py (other agents are working
on other chapters; the director runs the build).

## Report (under 150 words)

What you moved, split or relabeled; the fact items settled (with the source in a word); anything left and
why; back-matter lines that now need changing; the `--check` lines.
