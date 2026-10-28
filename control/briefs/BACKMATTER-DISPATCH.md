# BACKMATTER dispatch: assemble, edit in parallel, read once, fix once (2026-10-28)

Runs after every chapter's fix pass, because fixers update the hand-offs in `control/backmatter/`.

1. `python tools/build_backmatter.py` writes `manuscript/_backmatter/02-` to `07-` from the 37 hand-offs.
2. `python tools/backmatter_chunks.py split 8` cuts the glossary into `control/backmatter-work/glossary-1.md`
   to `-8.md` at letter boundaries (balanced, every spelling of a word in one part).
3. Ten editors at once, model opus, brief `control/briefs/BACKMATTER-EDIT.md`, one file each:

| Task | File |
|---|---|
| T-740 .. T-747 | `control/backmatter-work/glossary-1.md` .. `glossary-8.md` |
| T-748 | `manuscript/_backmatter/03-timeline.md` |
| T-749 | `manuscript/_backmatter/04-people.md` |
| T-750 | `manuscript/_backmatter/05-places.md` |
| T-751 | `manuscript/_backmatter/06-movies.md` and `07-answers.md` |

4. `python tools/backmatter_chunks.py join` puts the glossary back together (numbered entries first).
5. Reader R25 (sonnet, brief READER-REVIEW.md) reads the back matter: every title and introduction,
   the timeline, people, places, movies and answers in full, the glossary for format and plainness.
6. One fixer (opus, brief REVIEW-FIX.md adapted to the back matter) makes one pass over R25's findings.
7. The final build: `python tools/build_full_book_md.py`, `python tools/build_full_book.py --pdf`.
