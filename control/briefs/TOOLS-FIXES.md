# TOOLS-FIXES brief: the prose gate and the back-matter assembler (model: opus)

Two tools have bugs that let errors reach the printed book. They are described, with evidence, in
`external-input-bug-find.md` (project root): items 1, 2, 7, 9 and 10. Read those five items, then
the two tools. Verify each bug yourself before you fix it (the file is a review, not a spec).

## Your files

`tools/project_state.py` and `tools/build_backmatter.py`. Nothing else. Chapter writers are running
`project_state.py --check` while you work, so save each change in one write and test it at once.
No git, no installs, no sub-agents. Scratch: your own scratchpad subfolder.

## What to fix

1. **Gate, item 1:** the punctuation count (and the `--punct` listing) must also count em dashes and
   semicolons inside the `label="..."` and `name="..."` values of `hb-zoom`, `hb-story` and `hb-time`
   marker lines, because the build prints those values as headings.
2. **Gate, item 9:** a note closed with `<!-- hb-note:end -->` must not switch the check off for the
   rest of the file.
3. **Back matter, item 2:** a title or place with a colon of its own must not be cut there. Movies:
   split after the `(year)` group. Places and the rest: split at the first `": "` whose left side
   has balanced quotes and brackets.
4. **Back matter, item 7:** a bullet that is only "None", "None." or the like is not an entry.
5. **Back matter, item 10:** group places by a real US state or territory (accept "D.C.", "DC" and
   "Washington, D.C." as one; full names and the usual abbreviations); anything else goes under
   "Other places", never a fake state.

## Proof

- Run `python tools/project_state.py --check <slug> --stage prose` for all 37 chapters (slugs from
  `control/chapter-registry.md`). Chapters still being edited may fail for their own reasons: list
  every FAIL with its reason. Do not edit any manuscript file.
- Run `python tools/build_backmatter.py --draft-dir <your scratch>` on the hand-offs present and
  show that the five cut titles from item 2 now come out whole.

## Report (under 200 words)

What each fix changed, the gate results for all 37 chapters, the back-matter trial result.
