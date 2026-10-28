# The book is finished: report, October 28, 2026

## In short

- **All 37 chapters** were rewritten for readers who lose the thread easily. Fable wrote three of them
  (Exploration, Government, Holidays) and the front matter in the pilot. Opus wrote the other 34 after Fable ran
  out for the week. The full list is in `control/WHO-WROTE-WHAT.md`.
- **Every part was read once and fixed once.** 25 Sonnet readers read the book as a 12-year-old with ADHD would
  and made 1,036 findings. One Opus fixer per group made one pass over them. There was no second review.
- **The back matter** is built and linked: a glossary of 4,132 words, a timeline of 192 dates, 734 people,
  342 places to see, 157 movies and 111 answers, plus "How We Know What Happened". It was read once and fixed once.
- **The PDF** is `book/history-book.pdf` (3,548 pages, 47 MB). Every heading starts in the top half of a page, placed by
  the script from front to back. It has a contents page with page numbers, a grid page with the page of every
  chapter's every era, era colours with a 1-of-10 ribbon, chapter footers, bookmarks and 12 pt type, and every
  back-matter line has a page number. The build has 0 warnings and its font check passes.
- **The Markdown edition** is `book/history-book.md`.

## What changed in the chapters

| Measure (37 chapters) | Before | After the rewrite |
|---|---|---|
| Words | 777,949 | 818,501 (about 830,000 after the fix pass) |
| Paragraphs over 90 words | 2,867 | 218, most of them the lists in cards and closings, which the tool counts as one paragraph |
| Paragraphs opening with a date | about 23 percent | about 0.1 percent |

What a reader now meets in each chapter:

- a **card** at the start: the chapter's one-line spine, three questions, a "Five minutes?" section and the
  sections that can be skipped;
- a **strip** at each era ("Era 6 of 10 · 1800 to 1850 · about 29 minutes");
- **"By [year]" lines** and **era closers** in the long eras, as places to stop;
- story boxes that open with a **hook**, and glosses folded into the sentence;
- a **closing** that answers the three questions.

The front matter's counts (words, hours, era times) are now filled in by the build, so they can never go stale.
The false claim that 200 words a minute is the pace of reading aloud is gone: the page now says it is a quick
reader's pace and many readers take longer.

## Facts corrected along the way (a sample)

The fixers checked the findings against the research banks and fixed errors they found, each with a source in the bank:

- Scott Joplin's first year of sales earned him about $4, not $1 (400 copies at a cent each).
- The bracero pay holdback ran from 1942 to 1946. The two chapters disagreed, and the 1946 Mexican report settles it.
- The Levittown lease barred anyone not white except domestic servants of another race. The research note had it backwards.
- The 1989 rape of Michael Eugene Thomas is now credited to the newspapers that reported it, because the man pleaded
  guilty only to manslaughter and is likely living. The killing stays in the book's voice.
- The 1909 arsenic ruling came from one federal trial judge, not appeals judges.
- A Frederick Douglass quote comes from his 1855 book, not the 1845 *Narrative*.
- The Hindenburg dead were missing from the elements chapter and are now in it.
- Chapter pairs that told the same story twice now tell it once and point back (the Black Hills, the Philippine war,
  Cahokia, the bracero program and others), with their numbers made to agree.
- Seven chapter closings that hid who acted, or made a law the actor, now name the people.
- Rights and Movements now tells the Civil Rights Act of 1964, the March on Washington and the farmworkers' contracts.

## Choices I made that you may want to revisit

1. **Opus for 34 chapters.** This was your call when Fable ran out. If you want Fable's voice everywhere, the 34
   chapters could be redone after Fable resets on November 3. That is a big job.
2. **The half-page rule** stays as you set it. It costs pages: about 25 percent more than without it.
3. **Type at 12 pt with lines of about 71 characters**, as dyslexia guidance suggests. That added about 17 percent
   more pages. The setting is one number in `tools/build_full_book.py`.
4. **Reading times stay at 200 words a minute.** An outside review suggested 150. I kept 200 and changed the
   front matter's wording. Changing the rate would mean re-timing every card and strip, which a script can do.
5. **No era footers.** They would force a page break at every era.
6. **The grid rule.** About 50 findings asked to move a section, split one or reword a section heading. The rule
   says the grid never changes, so the fixers worked around them with bridges, opening lines and lead-ins. If you
   want, the rule could be relaxed for moves within one era and for splits, and those findings done properly.
7. **A full glossary** (4,132 words), since you welcomed a full one. Each word is explained once and points to
   the chapter where it first appears.

## Still open (none of it is needed for the book to be finished)

- **Ten fact questions** in `control/AUDIT-QUEUE.md` under "Open from phase 2":
  - a research-note line about To Tu Ya;
  - the outcome of the 2016 Flint charges;
  - General Motors against the Bell System as 1979's largest employer;
  - two wrong lines in the government research notes;
  - migration's growth figures and the reason officials gave for the Japanese American removal;
  - the backwards Levittown wording in the rights research notes;
  - the Jamestown Starving Time count;
  - loblollie thick or thin;
  - smallpox vaccination as "a shot";
  - Cahokia's dates.
- **From the outside reviews of October 27** (`EXTERNAL-INPUT-DESIGN-IMPROVEMENTS.md`, `external-input-bug-find.md`,
  `BUGS.md`):
  - fixed: the build and gate bugs (the gate's blind spot for punctuation in headings, the back-matter assembler's
    colon and state bugs, run-together furniture lines);
  - not done: the shelf edition in Projects\cool-tools (it opens in alphabetical order and hides the section
    headings), the old viewer's bugs, the README's reading instructions, three old helper scripts, pictures,
    a phone edition, maps and small editions;
  - the grid validator still misses a dropped closing marker (BUGS.md).

## Where things are

- The book: `book/history-book.pdf`, `book/history-book.md` (built copies are also in `build/`).
- Who wrote what: `control/WHO-WROTE-WHAT.md` (made by `tools/who_wrote_what.py`).
- The reviews: `control/review/R01.md` to `R25.md`. What each fixer did, finding by finding:
  `control/checkpoints/T-710` to `T-733` and `T-753` to `T-757-reviewfix.md`.
- The run, step by step: `control/WORKLOG.md`.
- To rebuild after any change: `python tools/build_full_book_md.py`, then `python tools/build_full_book.py --pdf`
  (about 10 minutes, no AI involved).
