# Pilot report: the readability edit on three chapters and the front of the book

Director's report to Jon, 2026-10-26, 10:50 PM. Everything below is committed on
`feature/local-cloud-code-homebrew` and pushed. The book to read is `book/history-book.pdf`
(1,990 pages) or `book/history-book.md`.

## What to read, and how long it takes

| Piece | Where in the PDF | Time |
|---|---|---|
| How This Book Works (the new introduction) | first page after the contents | 2 minutes |
| Before You Start, Four Ways to Read, A Ten-Minute History | the next three sections | 10 minutes |
| Chapter 1, Exploration and Discovery | the first chapter | about 110 minutes, or the opening card and the closing in 5 |
| Chapter 20, Government, Law, and Politics | the middle of Part 5 | about 140 minutes, or the card and closing in 5 |
| Chapter 37, Holidays | the last chapter | about 95 minutes, or the card and closing in 5 |

The fastest useful read is the four front pieces, then each pilot chapter's opening card, one era
of your choice, and the closing. That is about 30 minutes and shows every device.

## What the pilot did

Four writers on Fable and one tools agent on Opus ran at once, each on its own files, and each
kept a checkpoint for resume. None needed resuming; the wave fit inside one 5-hour window.

**The introduction.** The 3,834-word method essay is gone from the front. In its place:

- *How This Book Works*: 290 words, three paragraphs. The grid, how to read it either way, what the
  furniture is for, and one sentence on where the facts come from.
- *Before You Start*: 179 words. The size, that order does not matter, that skipping is normal,
  what the bold lines and the boxes are, what to do when a page feels heavy.
- *Four Ways to Read This Book*: 363 words. Honest reading times from the real word counts:
  straight through about 68 hours; one chapter one to two hours; one era across all 37 chapters
  from about 2 hours (before 1500) to 11.5 hours (1900 to 1950); the short road (the ten-minute
  history, the 37 cards, the 37 closings and the 37 "five minutes" sections) about 4.5 hours.
- *A Ten-Minute History*: 1,256 words, ten beats, one per era, each led by its through-line, every
  fact checked against a chapter's bank.
- The method essay, *How We Know What Happened*, is now the first piece of back matter, cut from
  3,834 to 1,392 words, keeping the three kinds of uncertainty and four examples (John Punch,
  Amelia Stewart Knight, Jane at Jamestown, the Hoover Dam count).

**The three chapters.** Each got the full architecture from `control/ARCHITECTURE-GUIDE.md`:

- An opening card as the first thing under the chapter heading: the chapter number and reading
  time, the spine sentence, an anchor (a real object or record), the narrator's "watch for",
  three questions, a "five minutes?" pointer and a "can skip" list.
- An era strip at the top of every era ("Era 6 of 10 · 1800 to 1850 · about 9 minutes").
- "By [year]" lines inside the long eras, stating where things stand.
- An era closer at the end of eras over 2,500 words ("If you remember one thing", three dated
  facts, a bridge to the next era), in four rotating shapes.
- A closing that answers the three questions word for word, states what changed, lists five
  dates, states one thing not known, names one place to go, and points to the next chapter.
- Every story box opens with a one-line hook; résumé lines were cut; the scene stayed.
- Inside the body: long paragraphs split, date-first paragraphs re-led, definitions folded into
  the sentence, hedges turned into Known / Not known pairs, disputes adjudicated.

## The numbers, before and after

| Chapter | Words | Paragraphs over 90 words | Paragraphs opening with a date | Story boxes over 400 words |
|---|---|---|---|---|
| Exploration | 20,056 to 21,715 | 84 to 6 | 28.9% to 0.7% | 14 to 14 |
| Government, Law, and Politics | 25,809 to 27,595 | 120 to 31 | 29.0% to 12.7% | 10 to 10 |
| Holidays | 18,088 to 19,284 | 55 to 28 | 19.8% to 3.0% | 4 to 3 |

The book grew from 832,669 to 837,003 words with three chapters done. Nothing in the grid moved.
Every cut (résumé lines in story boxes, repeated definitions, two minor names demoted to roles) is
listed in the checkpoints with its reason. All three chapters pass the prose gate.

## What I read, and what I think

I read the opening, one full era, one story box and the closing of each pilot chapter, and all
four front pieces.

**The shape works.** The openings are the best new writing in the book. Exploration opens on a
six-by-eight-inch lead plate buried beside the Missouri in 1743 and dug up in 1913; Government
opens on the one surviving copy of John Pory's 1619 record; Holidays opens on Sarah Josepha Hale,
88 and nearly blind, still writing to Congress. Each states its point in the first bold sentence,
tells you what to watch for, and asks three questions the closing answers word for word. The
closed loop is there. The "By [year]" lines and era closers give a reader a place to stop every
few minutes without the book talking about itself.

**The hard subjects came through intact.** The Oñate passage in Government is now five short
paragraphs with bold lead-ins and a Known / Disputed pair on the count of the dead, and it is
plainer and harder to look away from than the 330-word block it replaced. Sacagawea's death in
Exploration now puts the 1812 fur-post record and Clark's 1813 guardianship first, then credits the
Shoshone and Hidatsa accounts as disputed, which is the adjudication DeepSeek asked for.

**Where the writers used judgment against my targets, I agree with them.** Government kept
10 of 14 story boxes over 400 words and 12.7 percent of paragraphs date-first: its stories are
scene chains about killings and trials that cannot be compressed under the hard-subjects policy,
and in a chapter of laws and rulings the date is often the point. Exploration kept 14 long boxes
for the same reason. Attribution stayed near 8.5 per thousand words in Government and Holidays
because what remains is contested counts and witnesses, which DECISIONS #37 and #45 require.

**Two small things to carry into the next wave's brief.**

1. Some story boxes still explain a word in a sentence of its own ("Claptrap means silly talk
   meant to win cheers"). Guideline 7 as reworded wants the gloss inside the sentence. The writers
   did this in the body and missed it in a few boxes.
2. The ten-minute history's first draft read as a list of dated facts; one revision pass fixed it.
   The same risk applies to era summary paragraphs, which still open on several dated facts in a
   row. The next brief will say: the era's first paragraph leads with the era's through-line.

## Decisions I made on your behalf today

- DECISIONS #50 to #53 are recorded: the fourth-wall rule withdrawn; guideline 7 reworded as you
  approved; #20 amended so shrinking is allowed only to improve; the parallel-and-resume rule.
- The introduction comes before the front-matter pages (how it works, then the contract, the menu,
  the map). One setting in the build flips it if you prefer the contract first.
- Writers run on Fable; the tools agent ran on Opus.

## Usage, and the plan for the other 34 chapters

| Window | Before the pilot | After | Resets |
|---|---|---|---|
| 5-hour | 6% | 29% | 3:10 AM |
| Weekly, all models | 29% | 35% | 12:00 PM Oct 27 |
| Weekly, Fable | 50% | 62% | 12:00 PM Oct 27 |

Each chapter on Fable cost about 4 percent of the weekly Fable allowance and 300,000 to 380,000
tokens. The remaining 34 chapters on Fable would need about 135 percent of a weekly Fable
allowance, so this week they cannot all run on Fable. The choices:

1. **Wait for the weekly reset at noon tomorrow**, then run the 34 on Fable in waves of about eight
   per 5-hour window (each window takes about 8 chapters at 4 percent of the weekly Fable each,
   which spends the week's Fable allowance on this one job).
2. **Run the long and hard chapters on Fable now** (about nine: rights-movements, education,
   religion, art, crime-justice, music, slavery-freedom, native-nations, war) and the rest on
   Opus, which draws on the all-models allowance at 35 percent.
3. **Run everything on Opus** starting now, and keep Fable for the second read and the back matter.

My recommendation is 2: the chapters where judgment matters most get the best model while the
Fable allowance lasts, and the 5-hour window is otherwise idle until 3:10 AM.

## What is not done

- The other 34 chapters.
- The back matter beyond the method essay: glossary, timeline, people index, places, the movie
  list with accuracy notes, and the answers to all 111 questions. These are built after the
  chapters, because they depend on them.
- A second read of each chapter by a different agent, which I would do after the wave.
- The four story headings with nicknames still warn in the HTML build (the heading carries the
  nickname in quotes, the name attribute does not). Cosmetic; the viewer fix from T-658 handles it
  in the viewer, and the build uses the heading.
