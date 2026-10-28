# Bugs

Bugs noticed in the book as readers get it. Each entry: date, where, evidence, likely cause.
Logged only, not fixed.

## 2026-10-27 · Furniture lines run together into one paragraph in every built format

- **Where:** `tools/build_full_book.py` (`md_blocks`), so `build/history-book.html`, `build/history-book.pdf`, `build/history-book.md` and `book/history-book.md`.
- **Evidence:** `manuscript/exploration/part2-1800s.md` lines 288 to 291 hold the 1800 to 1850 era closer as four lines ("If you remember one thing:", "In 1803:", "In 1850:", "Next:"). Page 51 of `build/history-book.pdf` (the 4:41 AM build) prints them as one paragraph. The same happens to the Leif Erikson box's "Known:" and "Not known:" lines (`part1-before-1800.md` lines 78 and 79) and to the opening card's "Five minutes?" and "Can skip:" lines (lines 30 and 31, PDF page 14).
- **Likely cause:** `md_blocks` joins consecutive non-blank lines into one `<p>`, as Markdown does, while ARCHITECTURE-GUIDE 4.1, 4.5 and 5.7 write these items one per line with no blank line between. Markdown viewers do the same to the `.md` build.

## 2026-10-27 · The shelf edition reads the chapters in alphabetical order

- **Where:** `Projects\cool-tools\books\american-history\book.zip` (made by `cool-tools\books\make_books.py`), as the Book reader opens it (`Projects\Walker of Worlds\src\book.js` and `chapter.js`).
- **Evidence:** the zip's folders run `_introduction`, `america-world`, `art`, `big-business` and so on, with `exploration` (Chapter 1) thirteenth. The reader makes one section per folder and sorts the sections by folder name (`chapter.js`, `group()`), never by the `hb-chapter` id, so the nine parts are lost too. The reader's own collator puts `_backmatter` before `_frontmatter` and `_introduction` (checked with Node), so the next rebuild of the zip, with the new front and back matter folders, would open the book on the back matter.
- **Likely cause:** `make_books.py` zips the manuscript folders under their slugs, and nothing carries the registry order into the zip.

## 2026-10-27 · The shelf edition shows none of the span headings

- **Where:** the same zip and reader.
- **Evidence:** span labels exist only inside `<!-- hb-zoom level="span" label="..." -->` comments (1,968 of them in the manuscript today). The reader deletes HTML comments before it shows or reads text (`chapter.js`, `softenMd`) and builds its contents list from `#` headings only. So "How old are the footprints at White Sands?" never appears, and the opening card's "Five minutes? Read 'Toward the North Pole, 1879 to 1898'" and "Can skip:" lists name headings the shelf reader never shows. Story names do appear, because they are `###` headings.
- **Likely cause:** `make_books.py` copies the raw manuscript files. The book's own build scripts turn span labels into headings; the shelf copy does not.

## 2026-10-27 · "Four Ways to Read" calls 200 words a minute "about the pace of reading aloud"

- **Where:** `manuscript/_frontmatter/02-four-ways-to-read.md` line 3 (reader-facing front matter).
- **Evidence:** Hasbrouck and Tindal, *An Update to Compiled ORF Norms* (Technical Report 1702, University of Oregon, 2017; ERIC ED594994, https://files.eric.ed.gov/fulltext/ED594994.pdf), Table 4: the median (50th percentile) spring oral reading rate is 112 words correct per minute in grade 3, 133 in grade 4, 146 in grade 5 and 146 in grade 6. For this book's readers, 200 words a minute is well above the pace of reading aloud.
- **Likely cause:** the rate comes from the reading-time rule (ARCHITECTURE-GUIDE 4.1), and the comparison was added to the front matter without a source.

## 2026-10-27, 5:45 PM · Update: the first entry is fixed in the build

- The 5:41 PM build (`build/history-book.pdf`, 3,113 pages, after T-706 changed `tools/build_full_book.py` at 5:27 PM) prints each furniture line as its own paragraph: the chapter 1 card's "Five minutes?" and "Can skip:" on page 16, the Leif Erikson Known / Not known pair on page 20 and the 1800 to 1850 closer on page 62. `book/` still holds the 10:42 PM copies until the next rebuild. The other three entries are still open: the shelf zip and `make_books.py` are unchanged since October 22, and `02-four-ways-to-read.md` still has the reading-aloud sentence.

## 2026-10-27 · The validator does not catch a dropped closing span marker (fixed 2026-10-28)

- **Where:** `tools/validate_grid.js`.
- **Evidence:** the landmarks writer (T-701) dropped a span's closing marker by mistake during the readability edit; `node tools/validate_grid.js <file> --part` still reported 0 errors. The writer found it on reread and fixed it.
- **Likely cause:** span blocks are not checked for a matching close (unverified; logged from the writer's report).
- **Fixed 2026-10-28 (T-779):** the cause was right. An `hb-zoom` never went on the parser's block stack, so the next marker closed it without a word (and `tools/build_full_book.py` drops such a block's text with only a build warning). The validator now reports, with its line number, an `hb-zoom` that reaches the next `hb-chapter`, `hb-time`, `hb-zoom` or `hb-story` marker, or the end of the file, without its `<!-- /hb-zoom -->`, and a `<!-- /hb-zoom -->` that closes nothing or closes a story. Tested on a scratch copy of `manuscript/landmarks/part1-before-1800.md` with one closing line removed (`L42: hb-zoom span "Monks Mound and the mound builders" has no closing <!-- /hb-zoom -->: the next marker is hb-zoom at L55`) and six other breaks; the old validator passed six of the seven with 0 errors. All 111 part files, the outlines, the templates and the demo files still give 0 errors.

The six entries below came out of the accessibility pass (design file, "Second pass: accessibility", 9:20 PM). All were measured on a copy of the 5:41 PM build or with test prints in a scratch folder; nothing in the project was run or changed.

## 2026-10-27 · Every PDF page carries the contents page's dotted leaders, drawn off the page

- **Where:** the CSS in `tools/build_full_book.py` (`nav.toc li .lead { ... transform: translateY(-.25em); }`), so `build/history-book.pdf`.
- **Evidence:** pages 2, 3, 20, 500, 1,500, 3,000 and 3,113 of the 5:41 PM build all hold the same 43 runs of 1-by-1 squares in the rule grey (#d6d6d6), 5,772 squares a page, placed far outside the page and clipped. They are the 43 leaders of the contents list. They take about 3.5 KB of each page's compressed content, roughly 11 MB of the 29.8 MB file (estimated from those seven pages), and none of it is tagged or marked as an artifact. A 9-page test page printed by the same Chrome 156 shows it: with the transform, all 10 of its leaders (2,085 squares) are drawn on all 9 pages; with `position: relative; top: -.25em` instead, only on page 1.
- **Likely cause:** Chrome paints an element that has a CSS transform into every page of the print. Confirmed in the small test, not yet in the book's build.

## 2026-10-27 · PDF bookmarks: 382 titles are wrong, and the back matter is filed under Part 9

- **Where:** `tools/make_pdf.py` (Chrome's `--generate-pdf-document-outline`, checked by `Layout.check()`), so `build/history-book.pdf`.
- **Evidence:** of the 3,098 bookmarks, 368 repeat their heading's text ("The GridThe Grid", "The 1600sThe 1600s", "The Challenger explosion, 1986The Challenger explosion, 1986") and 14 lose the space where the heading wraps ("A History of the UnitedStates", "Jews from the Russian Empire, and others from southern and easternEurope"). The 368 are exactly the headings whose tagged content reaches onto a second page (1 H2, 76 H3, 291 H4). `check()` compares only the first 24 non-space characters of a title, so every one passes. "How We Know What Happened" sits inside "Culture and Play" (Part 9) in the bookmarks, and the other back-matter files will land there too.
- **Likely cause:** Chrome builds a title from all the text tagged in a heading, including a piece left on the page before. The back matter's headings are h2, one level below the last part's h1.

## 2026-10-27 · The grid page tells a screen reader that every cell belongs to all nine parts

- **Where:** `grid_page()` in `tools/build_full_book.py`; PDF page 4.
- **Evidence:** the part rows are `<th colspan="11">`. Chrome tags them as column headers (/Scope /Column, /ColSpan 11), so each of the 370 cells lists eleven headers: its era, all nine part rows and its chapter. In a test print by the same Chrome, `scope="row"` on the part rows (or one `<tbody>` per part with `scope="rowgroup"`) leaves each cell with its era and its chapter only.
- **Likely cause:** a header cell in a row with no data cells defaults to column scope.

## 2026-10-27 · In the PDF's tagged text, words run together at every line end

- **Where:** `build/history-book.pdf` (Chrome's output); the fix would go in the CSS in `tools/build_full_book.py`.
- **Evidence:** each printed line is its own text string, with nothing for the space where the line wraps (page 20: "...the oldest about 6,000 years ago. A", then "Native people that archaeologists call the Dorset..."). poppler's reading of the tags gives "Readacross", "onesubject", "A History of the UnitedStates"; chapter 1 alone has about 1,213 such joins. ISO 32000-1, section 14.8.2.5, requires the spaces. A test print of chapter 1 with `white-space: pre-wrap` on the text blocks gives the same 82 pages, the same layout text byte for byte, and 2 joins.
- **Likely cause:** Chrome writes no character for the space a line wraps at.

## 2026-10-27 · Story hooks, bold lead-ins and italic titles are invisible to PDF 1.7 tag readers

- **Where:** `build/history-book.pdf`.
- **Evidence:** Chrome tags `<strong>` and `<em>` as Strong and Em (4,909 and 1,973 elements), PDF 2.0 names, in a file marked PDF 1.4 with no role map. poppler rejects every one ("StructElem object is wrong type (Strong)") and drops its text: all 684 story hook paragraphs come out empty, and the "Five minutes?" and "Can skip:" labels, every bold lead-in and every italic title are missing from its reading of the tags. PDF/UA-1 requires non-standard types to be role-mapped (veraPDF rule 7.1-5).
- **Likely cause:** Chromium's tag mapping (`printing/common/metafile_utils.cc`) uses PDF 2.0 names and writes no role map.

## 2026-10-27 · The shelf edition read aloud: the reader's text rules change this book's words

- **Where:** `Projects\Walker of Worlds\src\text.js` and `numbers.js`, applied to `Projects\cool-tools\books\american-history\book.zip`. Logged here, not in the reader's own BUGS.md, because this job could write only in this folder.
- **Evidence:** the reader's own code (`chapter.js` softenMd, then `text.js` clean with the default settings), run in Node over all 116 manuscript files: 1,896 capital-letter words are lowercased, among them "US" 390 times, so "US troops fought in Afghanistan" reaches the voice as "Us troops fought..." (also FBI 67, NAACP 49, CDC 40, PBS 70). 33 real words are deleted as website watermarks: History.com 8 times, JFK8 4, the Lakota word Wicaŋȟpi 2, GU272, CRISPR-Cas9, AlphaFold2, MLK50, 9to5 and others. With "Read numbers as words" on, a bare year becomes a count ("In 1987" goes to the voice as "In one thousand nine hundred and eighty-seven"), while "August 1908" is read as a year.
- **Likely cause:** rules written for scraped web novels (shouted capitals, site watermarks, numbers as counts) apply to every book.
