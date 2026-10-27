# BACKMATTER-EDIT brief: turn the assembled back matter into finished pages (model: fable)

`python tools/build_backmatter.py` has assembled six files in `manuscript/_backmatter/` from the
writers' hand-offs in `control/backmatter/<slug>.md`: 02-glossary, 03-timeline, 04-people,
05-places, 06-movies, 07-answers. They are a mechanical first draft. The dispatch names which of
the six files are yours. Make them finished pages a reader aged 8 to 15, often with ADHD, can use
to look something up in seconds.

## Read first

`control/writing-style-guide.md` (§0 and guideline 7), `control/ARCHITECTURE-GUIDE.md` §6,
`control/general-writing-style-guide.md`, `control/hard-subjects-policy.md`. Then your files.

## What to do

- **Glossary:** one entry per word. Where two chapters explain the same word, keep the clearest
  explanation and list every chapter. Explanations stay as plain as the chapters give them, one
  line, no new facts. Alphabetical, letter headings kept. Clinical words keep their full
  explanation (policy §3b).
- **Timeline:** about 150 dates, oldest first, under the ten era headings. Keep every chapter's
  five closing dates (they come first in each hand-off), then the dates that make the story of the
  country readable in order. Merge lines that name the same event. One short line each.
- **People:** one line per person, by last name, role in one clause, chapter and era. Fix the
  sort where the script's last-name guess is wrong (single names, Spanish and Native names,
  "de", "van", titles). A person in two chapters gets one line listing both.
- **Places:** group by state, alphabetical. Fix a place the script filed under "Other places" when
  its state is plain from the line. Drop exact duplicates.
- **Movies:** one line per movie; where two chapters mention one movie, merge the notes.
- **Answers:** check each question and answer reads as a pair; light edits for flow only.

Every line must already be in a chapter: when in doubt, check the chapter
(`manuscript/<slug>/part*.md`) and leave the line as the chapter gives it. No em dashes, no
semicolons (`python tools/project_state.py --punct <file>` must show 0/0). The one-sentence
introduction under each title may speak to the reader. Edit only your files. No git.

## Report (under 150 words)

Entries per file before and after, what you merged, anything you could not settle.
