# BUILD-POLISH brief: make the printed book look as good as it reads (model: opus)

Jon asked for a PDF that is "feature complete and very nice". The text is being finished by other
agents right now; your job is the build. A design review written this morning,
`EXTERNAL-INPUT-DESIGN-IMPROVEMENTS.md` (project root), proposes build-only changes. The director
has chosen which to take. Read the review's sections named below, `BUGS.md` (first entry),
`external-input-bug-find.md` item 8, `control/ARCHITECTURE-GUIDE.md` section 4 (the furniture
formats), then the three tools. Verify every problem yourself before fixing it.

## Your files

`tools/build_full_book.py`, `tools/build_full_book_md.py`, `tools/make_pdf.py`. Nothing else: no
manuscript file, no front-matter file, no other tool. No git, no installs, no downloads, no
sub-agents. Scratch: your own scratchpad subfolder.

Other agents call `python tools/build_full_book_md.py` while you work (the reader-review extracts in
`tools/review_extract.py` cut its output at `# Part N:` and `## Chapter N:` lines). Keep that build
working after every save and keep those two heading forms exactly as they are.

## What to build

1. **Furniture, review section 1, all three parts.** Consecutive lines in the furniture (opening and
   closing cards, era closers, Known / Not known / Disputed, "Five minutes?", "Can skip:", "Next:")
   print as separate lines, in the HTML, the PDF and the Markdown book (BUGS.md entry 1, bug-find
   item 8). First measure whether any body prose is hard-wrapped across lines, and choose the rule
   that cannot join or split real prose. Give each furniture kind its own class and look as the
   review describes (era strip, "By" lines, era closer panel, Known/Not known panel, card, closing,
   the story box "Who:" line at body size and ink). Link "Five minutes?" and "Can skip:" names to
   their spans and "Chapter N" mentions to their chapters; print a warning for every name that
   matches no span. Print per-chapter counts of each furniture kind, so a miss shows as a number.
2. **Era look, review section 4, without the era footer.** Ten era colours from one warm family
   (contrast-checked against text, still distinct in grey), used on the era heading rule, the era
   strip and the story-box bar of that era; a ten-square ribbon in each era strip. No era footers
   and no named pages per era (they would force a page break at every era).
3. **The grid page, review section 3.** One page (two at most) after the contents: 37 chapters by
   10 eras, each cell the page where that chapter's era starts, linked, filled from the PDF
   bookmarks the way the contents page numbers are.
4. **Back-matter links and page numbers, review section 8.** Every line of the six back-matter
   files (`manuscript/_backmatter/02-` to `07-`, written by `tools/build_backmatter.py` in the form
   "(Chapter N, era label)") links to its target and shows a page number in the PDF: people to their
   story box (match the story's `name`), glossary, timeline and places to the era, answers to the
   chapter closing. Warn on every miss. The files may not exist yet: build and test with
   `python tools/build_backmatter.py --draft-dir <scratch>` output copied into a scratch copy of the
   project, never into `manuscript/`.
5. **Type, review section 7, in part.** 12 pt body, a measure of about 72 characters, line height
   1.6, left aligned, no hyphenation, `text-wrap: pretty`. Keep the system fonts (no font files, no
   downloads, white page). After every PDF build run `pdffonts` and stop with a plain message if any
   font family other than the expected ones was embedded: a substituted font must fail, never slip
   through.
6. **Front-matter numbers.** The front matter types counts by hand ("about 820,000 words", hours,
   shortest and longest chapter), and they are already stale. Add tokens such as `{{book_words}}`
   that the build replaces with its own counts in every format, and list the tokens in the
   docstring. Do not edit the front-matter files: the director places the tokens later.

Keep everything that works: the page-break rule (no heading may start in the bottom half of a page;
`make_pdf.py`'s front-to-back loop), the contents page numbers, chapter footers, bookmarks and the
segment-parallel settling. Any new heading element must stay in step with `tag_headings` and the
bookmark check in `make_pdf.py`, or the build stops with a bookmark-count error. Furniture labels
that are not headings should not be heading tags.

## Proof

A full `python tools/build_full_book.py --pdf` on the current manuscript, clean: no errors, the
furniture counts, the warning list, pages before and after, build time, and `pdffonts` passing.
Then look at the PDF yourself: render a few pages to PNG with `pdftoppm` (the opening card, an era
strip with its ribbon, a closer, a Known/Not known pair, a story box, the grid page, a contents
page) and check each one.

## Report (under 300 words)

What you built, what you left out and why, the numbers above, and the PNG paths.
