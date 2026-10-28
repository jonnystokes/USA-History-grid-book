# The book is finished: report, October 28, 2026

## In short

- **All 37 chapters** were rewritten for readers who lose the thread easily. Fable wrote three of them
  (Exploration, Government, Holidays) and the front matter in the pilot. Opus wrote the other 34 after Fable ran
  out for the week. The full list is in `control/WHO-WROTE-WHAT.md`.
- **Every part was read once and fixed once.** 25 Sonnet readers read the book as a 12-year-old with ADHD would
  and made 1,036 findings. One Opus fixer per group made one pass over them. There was no second review.
- **The findings the old grid rule blocked are done.** About 50 findings asked to move a section, split one or
  reword a heading, which the architecture guide then forbade. You told me to do what is best. I relaxed the rule
  within one era (DECISIONS #54) and 19 agents made about 45 moves, splits and new headings. Nothing left its era.
  The original example, news-communication's "The penny press, 1833", now sits after the Lovejoy story, so the
  antislavery-press and mob sections run together.
- **Every open fact question is settled**, each with a source in the research notes (list below).
- **The back matter** is built and linked: a glossary of 4,132 words, a timeline of 192 dates, 734 people,
  342 places to see, 157 movies and 111 answers, plus "How We Know What Happened". It was read once and fixed once.
- **The PDF** is `book/history-book.pdf` (3,555 pages, 47 MB). Every heading starts in the top half of a page,
  placed by the script from front to back (1,402 breaks). It has:
  - a contents page with page numbers;
  - a grid page with the page of every chapter's every era;
  - era colours with a 1-of-10 ribbon;
  - chapter footers and bookmarks;
  - 12 pt type;
  - a page number on every back-matter line (6,088 in all).

  The build has 0 warnings and its font check passes.
- **The Markdown edition** is `book/history-book.md`. **The shelf edition** on your Book reader
  (Cool-tools) is rebuilt from the finished book, in book order with its headings showing, and pushed.

## What changed in the chapters

| Measure (37 chapters) | Before | After the rewrite |
|---|---|---|
| Words | 777,949 | 818,501 (about 830,000 now) |
| Paragraphs over 90 words | 2,867 | 218, most of them the lists in cards and closings, which the tool counts as one paragraph |
| Paragraphs opening with a date | about 23 percent | about 0.1 percent |

What a reader now meets in each chapter:

- a **card** at the start: the chapter's one-line spine, three questions, a "Five minutes?" section and the
  sections that can be skipped;
- a **strip** at each era ("Era 6 of 10 · 1800 to 1850 · about 29 minutes");
- **"By [year]" lines** and **era closers** in the long eras, as places to stop;
- story boxes that open with a **hook**, and glosses folded into the sentence;
- a **closing** that answers the three questions.

All 370 era strips and 37 card times now come from one count, the build's, so they agree with each other and
with the front matter. The front matter's counts (words, hours, era times) are filled in by the build, so they
can never go stale. The false claim that 200 words a minute is the pace of reading aloud is gone: the page now
says it is a quick reader's pace and many readers take longer.

## Facts settled and corrected (each with a source in the research notes)

The ten questions that were still open:

- **Flint:** none of the officials charged went on trial or to jail. Seven took misdemeanor deals that judges later
  dismissed, and the rest were dropped or dismissed by 2023 (Michigan attorney general's 2026 report, court records).
  The book names no living official.
- **1979's largest employer:** the Bell System employed 1,029,905 people, against General Motors' 618,365 in the
  US (AT&T's 1979 annual report).
- **The Jamestown Starving Time:** about 500 people in the colony and about 240 in the fort when the winter began,
  and about 60 of those 240 alive by spring (Encyclopedia Virginia and the food-farming notes). Health,
  food-farming, disasters and the glossary now say the same thing.
- **The Japanese American removal:** the reason officials gave is now quoted from the order itself, beside the 1983
  commission's finding that it "was not justified by military necessity".
- **City growth in the Great Migration:** Philadelphia grew about 59 percent from 1910 to 1920, not 500
  (Census). Migration and city-building agree.
- **Cahokia:** most people had left by about 1350, and the city was empty by about 1400 (National Park Service).
  City-building, sports-play and the places page agree.
- **Smallpox vaccination in the 1800s** is described everywhere as a cowpox sore's fluid scratched into the skin,
  not "a shot".
- **Loblollie** was a thick porridge. **The Levittown lease** and **To Tu Ya's family** now say only what the
  sources say. **Two wrong lines** in the government notes are corrected.

Found and fixed along the way, a sample:

- Lewis Cass left the Mandan, Hidatsa and Arikara out of the 1832 vaccination program, and the health chapter now
  gives his reasons (State Historical Society of North Dakota).
- Scott Joplin's first year of sales earned him about $4, not $1.
- The bracero pay holdback ran from 1942 to 1946.
- The 1989 rape of Michael Eugene Thomas is credited to the newspapers that reported it, because the man pleaded
  only to manslaughter and is likely living.
- The Civil Rights Act of 1964, the March on Washington and the farmworkers' contracts are now told in Rights and
  Movements.
- Seven chapter closings that hid who acted, or made a law the actor, now name the people.
- Chapter pairs that told the same story twice now tell it once and point back, with their numbers made to agree.

## Tools and other loose ends

- **The validator** now catches a section whose closing marker is missing, a gap the landmarks writer found.
  Every part file passes it.
- **The resume drill and `control/RESUME.md`** follow your resume rule: a stopped agent is resumed, never
  replaced. The project's CLAUDE.md now says the same and allows parallel agents.
- **Fixed:** the prose gate now checks headings for em dashes and semicolons, the back-matter assembler bugs are
  gone, and three helper-script bugs are fixed. The README now points to `book/`.
- **The shelf edition** (`Projects\cool-tools\books\american-history\`) is rebuilt from the book's own Markdown
  build. It now opens in book order with section headings visible. Your place in it may land on a different chapter
  the first time you open the update, because the chapters were reordered.

## Choices I made that you may want to revisit

1. **Opus for 34 chapters.** This was your call when Fable ran out. If you want Fable's voice everywhere, those
   chapters could be redone after Fable resets on November 3. That is a big job.
2. **The half-page rule** stays as you set it. It costs about 25 percent more pages than without it.
3. **Type at 12 pt with lines of about 71 characters**, as dyslexia guidance suggests, added about 17 percent
   more pages. It is one number in `tools/build_full_book.py`.
4. **Reading times stay at 200 words a minute.** The front matter now calls it a quick reader's pace.
5. **No era footers.** They would force a page break at every era.
6. **The grid rule is relaxed within one era** (moves, splits, headings). It still forbids moving anything between
   eras or chapters, which keeps the grid page, the one-era reading path and the back-matter links true.
7. **A full glossary** (4,132 words), since you welcomed a full one. Each word is explained once and points to
   the chapter where it first appears.

## Not done, on purpose

- The old grid viewer's bugs. It was retired as a reading format (DECISIONS #48), and the PDF, the Markdown book
  and the shelf edition replace it.
- New features from the outside design review: pictures, a phone (EPUB) edition, maps and small editions. Each
  is a project of its own, and the book is complete without them.
- A few old process documents still describe the earlier rules (`control/AGENT-MECHANICS.md`, `WRITER-DISPATCH.md`,
  `SALVAGE.md`). `RESUME.md` and `CLAUDE.md` now govern.

## Where things are

- The book: `book/history-book.pdf`, `book/history-book.md` (built copies are also in `build/`).
- Who wrote what: `control/WHO-WROTE-WHAT.md` (made by `tools/who_wrote_what.py`).
- The reviews: `control/review/R01.md` to `R25.md`. What each fixer did, finding by finding:
  `control/checkpoints/T-710` to `T-757-reviewfix.md`, and the final pass in `T-760` to `T-781`.
- The run, step by step: `control/WORKLOG.md`.
- To rebuild after any change: `python tools/build_full_book_md.py`, then `python tools/build_full_book.py --pdf`
  (about 9 minutes, no AI involved). The shelf edition: `python make_books.py american-history` in
  `Projects\cool-tools\books`.
