# BACKMATTER-EDIT brief: turn the assembled back matter into finished pages (model: opus)

`python tools/build_backmatter.py` has assembled the back matter from the writers' hand-offs in
`control/backmatter/<slug>.md`: a glossary, a timeline, a people list, places, movies and answers. It
is a mechanical first draft. The dispatch names ONE file that is yours: either one of
`manuscript/_backmatter/03-timeline.md` to `07-answers.md`, or one part of the glossary,
`control/backmatter-work/glossary-K.md` (the glossary is cut into letter ranges so several editors can
work at once; every spelling of one word is in one part). Make it a finished page a reader aged 8 to
15, often with ADHD, can use to look something up in seconds.

## Read first

`control/writing-style-guide.md` (section 0 and guideline 7), `control/ARCHITECTURE-GUIDE.md`
section 6, `control/general-writing-style-guide.md`, `control/hard-subjects-policy.md`. Then your file.

## The one format rule the build depends on

Every entry is one bullet that ends with exactly ONE reference in brackets, as the draft has it:
`- **name**: text (Chapter N)` or `- **name**: text (Chapter N, era label)`. The build turns that
reference into a link and a page number, so never write two chapters in one bracket, never drop the
bracket, and never add text after it. Keep the `##` headings. Answers keep their form
(`- **question?** answer`, under their chapter heading).

## What to do

- **Glossary part:** one entry per word. Where several chapters explain the same word, keep the
  clearest explanation (the plainest, the one a child understands first) and the reference of the
  chapter where the word FIRST appears in book order (the lowest chapter number), as the glossary's
  introduction promises. Explanations stay as plain as the chapters give them, one line, no new
  facts. Alphabetical within each letter. Clinical words keep their full explanation (policy
  section 3b). Drop an entry only if it explains a word an 11-year-old already knows. Leave entries
  that start with a numeral where they are (the director moves them).
- **Timeline:** about 150 dates, oldest first, under the ten era headings. Keep every chapter's five
  closing dates, then the dates that make the story of the country readable in order. Merge lines
  that name the same event (keep the reference of the chapter that tells it most fully). One short
  line each.
- **People:** one line per person per chapter: a person who appears in two chapters keeps two lines,
  each with its own role and reference, because each line gets its own page number. Merge only true
  duplicates within one chapter. Sort by last name and fix the sort where the draft's guess is wrong
  (single names, Spanish and Native names, "de", "van", titles).
- **Places:** group by state, alphabetical. Move a place the draft filed under "Other places" when its
  state is plain from the line. Drop exact duplicates.
- **Movies and answers:** one line per movie; where two chapters name one movie, keep one line with the
  fuller note and the first chapter's reference. Answers: check each question and answer reads as a
  pair; light edits for flow only.

Every line must already be in a chapter: when in doubt, check the chapter
(`manuscript/<slug>/part*.md`) and leave the line as the chapter gives it. No em dashes, no
semicolons: `python tools/project_state.py --punct <your file>` must show 0/0. The one-sentence
introduction under a title may speak to the reader. Edit only your file. No git, no installs, no
sub-agents.

## Report (under 150 words)

Entries before and after, what you merged or dropped and why in a few words, anything you could not
settle, and the `--punct` line.
