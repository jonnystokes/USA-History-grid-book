# Architecture Guide: how a chapter is built so a reader can get through it

Written 2026-10-26 by the director after Jon's read of the finished first draft and a DeepSeek
critique. Binding for the readability edit (DECISIONS #50 to #53). It sits above the two style
guides on questions of structure and below them on questions of sentences.

**Precedence.** `hard-subjects-policy.md` governs content. `writing-style-guide.md` (the
amendment) governs the reader, the subject and Jon's seven guidelines. This guide governs
architecture: where units begin and end, how long they run, what furniture they carry, and the
narrator's voice. `general-writing-style-guide.md` governs sentence mechanics. Where this guide and
the general guide disagree about a sentence, the general guide wins. Where they disagree about
where a chapter starts, ends or pauses, this guide wins. The general guide's sections
"Metadiscourse", "Staged Scenes" and "End When the Information Ends" now carry a furniture
exception that points here.

**How to use it.** Read it once in full. Then read the whole chapter you are editing, start to
finish, before you change a word. The measurements (`python tools/measure_readability.py <slug>`)
tell you where to look. Your reading tells you what is wrong. Jon's instruction: do not rely on
lint; rely on reading, and on your own judgment of what makes the book better.

---

## 1. The diagnosis

The first draft is accurate, plain and sourced, and it is not a book anyone reads through. Its
sentences pass every rule. Its chapters have no beginning, no end, no progress signal and no
spine. A reader meets fifty dates and thirty names in twenty pages with no one to follow. One
paragraph in four opens with a date. Forty-four eras run past 4,000 words, the longest to 12,863,
with no place to stop. Every paragraph has the same shape: a claim, a dated example, a source, a
definition. The best passages (York asking Clark for his freedom, Frethorne's "peas and loblollie",
Fountain Hughes on tape, the Verrazzano boy) prove the book can be alive. They are exceptions.

A reader with ADHD does not bounce off hard sentences. They bounce because nothing tells them
why to start, how long it will take, how much is left, where they may stop, or what the point
was. Every device below answers one of those.

## 2. What never changes

The grid stays exactly as it is: 37 chapters in their order, 10 eras in their order, every span
and story in its era. No chapter, era, span or story moves, merges, splits or is removed. Every
marker line, era id, story slug, `status=`, `progress=` and record key stays as it is. Each
chapter still covers only its own subject.

Shrinking is allowed only when it makes the book better (DECISIONS #52): a repeated explanation
cut to a one-line callback, a story box trimmed of its birth-to-death résumé, three hedging
sentences replaced by a Known / Not known pair. Note every cut in your checkpoint. What is
forbidden is collapsing a worked passage into a summary. The book grows: good, informative
material in, fluff out.

No new facts in furniture. Every sentence you add is one of three things: a restatement of a fact
already in the chapter, a navigation sentence with no factual content, or a fact from the
research bank with its source. Openings and closings are where writers invent. Do not.

## 3. The narrator

The fourth-wall rule is withdrawn. The book now has a narrator: a calm adult who knows this
history, is on the reader's side, and says so plainly when it matters. The narrator may address the
reader as "you", name the chapter and the book, point to another chapter, say how long something
takes, say "look at this" before a fact worth looking at, and say "you can stop here" after a hard
section.

The narrator is not a TV host. No jokes forced into history that is not funny. No "imagine you
are..." and never "imagine being" a victim (hard-subjects policy). No "kids" or "young readers".
No praise of the book or its method ("this honest account"). No "in this chapter we will explore".
The narrator talks like a good teacher at a table, not like a brochure.

Where the narrator speaks: chapter openings and closings, era strips, "By [year]" lines, era
closers, chapter cards, front and back matter, and at most one "look at this" line per 600 words
of body. Inside the body, the history still tells the history.

## 4. The furniture, unit by unit

The ten canonical eras and the three part files are the container. The furniture sits inside
them, in the same place in every chapter, so a reader never spends attention on "where am I".

### 4.1 The chapter opening (every chapter, 200 to 320 words)

Placed as the **first block of era 1**, before any other zoom or story:

```
<!-- hb-zoom level="era" label="Chapter opening" -->
**Chapter 1 of 37 · Exploration and Discovery · 10 eras · about 50 minutes**

**[The spine, one bold sentence: the claim the whole chapter supports.]**

[The anchor, 60 to 90 words: one real object, place or person, dated, already in the chapter.]

[The turn, 80 to 120 words, in the narrator's voice: what the chapter follows, era by era, and
what to watch for. May say "you".]

**Three questions this chapter answers**
- [question]
- [question]
- [question]

**Five minutes?** Read "[span label]" in [era label].
**Can skip:** [two to four span labels]. The chapter still makes sense without them.
<!-- /hb-zoom -->
```

Rules. The spine states the point first (the Teaching Point rule): no suspense. The three
questions are real questions the chapter answers, repeated word for word in the closing. The
anchor uses a fact already in the chapter. "Five minutes?" names a real span. "Can skip" must be
true. The reading time is the chapter's words divided by 200, rounded to five minutes. The label
`Chapter opening` is fixed: the build script moves this block above the era heading.

### 4.2 The chapter closing (every chapter, 180 to 280 words)

Placed as the **last block of era 10**:

```
<!-- hb-zoom level="era" label="Chapter closing" -->
**The three questions, answered**
- [Question 1, word for word.] [Answer, one or two sentences.]
- [Question 2.] [Answer.]
- [Question 3.] [Answer.]

**What changed:** [one sentence, the arc of the ten eras.]

**Five dates to keep**
- [date]: [event, a few words]
- (five lines)

**Not known:** [one sentence, a statement, never a question.]

**Where to go:** [one real place, museum, site or archive, one sentence.]

**Next:** Chapter 2, Native Nations. [One sentence on what it asks.]
<!-- /hb-zoom -->
```

The closed loop (asked in the opening, answered here) is the single most satisfying thing you
can give a reader who has held on for 20,000 words. The five dates must all appear in the chapter.

### 4.3 The era strip (every era, one line)

The first paragraph inside the era's first zoom (after the chapter opening block in era 1):

```
**Era 6 of 10 · 1800 to 1850 · about 9 minutes**
```

Words divided by 200, rounded. If the strip says "about 66 minutes", the era needs "By" lines.

### 4.4 "By [year]" lines (eras over 4,000 words)

One bold line about every 2,000 words, at a natural seam between spans, as its own paragraph
inside the current block:

```
**By 1830:** The fur trade had moved past the Rockies, and the first wagons were on the Santa Fe Trail.
```

It states where things stand. It is not "halfway" and not a restatement of the last two thousand
words. It is history, so it carries no "you". A 12,000-word era gets five or six.

### 4.5 The era closer (eras over 2,500 words)

The last block of the era:

```
<!-- hb-zoom level="era" label="By 1850" -->
**If you remember one thing:** [one sentence: what changed in this era.]
- [date]: [fact]
- [date]: [fact]
- [date]: [fact]
**Next:** [one line bridging to the next era.]
<!-- /hb-zoom -->
```

Rotate the middle so 370 closers do not share a shape: three bullets; a before/after pair ("In
1800: ... In 1850: ..."); one number that matters, with a comparison; or one question the era
leaves open, answered in the next era. The label and position stay fixed. Short eras (under
2,500 words) get no closer; the strip is enough.

### 4.6 Span labels

Keep a plain label where it is clear. Turn about half into a question or a promise ("How old are
the footprints?", "Why Columbia broke apart"). Never two questions in a row. A question label is
answered in the first two sentences under it.

### 4.7 Bold lead-ins

Where the eye needs a handle, start a paragraph with two to four bold words and a period:
`**The deal.**`, `**The cost.**`, `**What the judges did.**` Not every paragraph, and not
mechanically one in three. Use them where a reader skimming would otherwise lose the thread,
and where a paragraph would otherwise open with a date.

### 4.8 Story boxes

684 stories, median 317 words, 146 over 400, many shaped like résumés (born, did, died). New
shape, inside the existing `hb-story` block, keeping the `###` heading and the record lines:

```
### [Name]

> **Who:** [the role and the reason the reader should care, in one clause; not the birth date.]
> **When and where:** ...
> **Movie:** [title (year). If the film invents a romance or an event, say so in five words.]

**[The hook, 12 words or fewer, with a concrete detail: a number, an object, a line of speech.]**

[The scene or the problem, 120 to 260 words, two to four paragraphs, none over 80 words. Built
only from sourced detail. The person's own words where the bank has them.]

[Optional, where the story needs it: **Why this story is here:** one sentence. **Known:** one
sentence. **Not known:** one sentence.]
```

The hook is mandatory. The trailer lines are optional: use them when the story's point or its
uncertainty is not obvious from the scene, and leave them out otherwise. Six hundred identical
trailers would be the next tic. Cut the résumé, keep the scene. Most boxes land between 200 and
400 words. A box may run longer when the story earns it (York, Celia, Fountain Hughes); say so in
the checkpoint. The Movie line keeps the viewer's record format exactly.

## 5. The body: changes inside paragraphs

### 5.1 Paragraph size

Target 40 to 75 words. Split anything over 90 at its seam, in the same order. The Oñate paragraph
in government-politics (about 330 words, six ideas) becomes four paragraphs: the attack and the
numbers, the sentences, the dispute over the feet, the trial. No fact moves.

### 5.2 No date-first paragraphs

The first sentence of a paragraph names a person, a place, an object or an action. The date goes
in the second clause or the second sentence. "On April 30, 1803, American diplomats in Paris agreed
to pay France $15 million" becomes "**The deal.** American diplomats in Paris agreed to pay France
$15 million for Louisiana. The date was April 30, 1803." Under one paragraph in twenty may still
open with a date, where the date is the point.

### 5.3 Era first sentences

Read the ten first sentences of a chapter together. They must differ in shape and must not all be
broad and date-led. After the strip, the first sentence names something specific.

### 5.4 Names

No more than three new proper nouns in 400 words. Where a passage introduces eight people, split
at the subject change or demote the minor ones to roles ("a Portuguese governor", "the ship's
captain"). The full chain can live in a story box or the back matter.

### 5.5 Definitions

Guideline 7 as reworded (DECISIONS #51): explain a hard word once per chapter, inside the
sentence, in a few words; clinical words get the hard-subjects policy's full explanation; never
explain a word an 11-year-old knows; the glossary carries every term; a later era may re-gloss
once if a reader opening there would be lost.

### 5.6 Attribution

Keep "the National Park Service says" when the claim is contested, the source is a witness, or
the number depends on who counted (DECISIONS #37 and #45 still apply). Otherwise state the fact.
The bank still holds the source. A chapter at nine attributions per thousand words reads like a
report.

### 5.7 Known, Not known, Disputed

Three different things the draft runs together. Known: the record shows it; state it. Not known:
no record survives; say so once, in a labeled line. Disputed: the evidence conflicts; state the
better-supported version first, say why in a clause, then give the other, credited. Where a span
ends in two or three hedging sentences, replace them with:

```
**Known:** [one sentence.]
**Not known:** [one sentence.]
```

Do not give a documented record and a later tradition equal weight. Sacagawea's death is the
test: the 1812 fur-post record is stronger than the 1884 tradition, and the book says so while
saying why the tradition matters to the Shoshone.

### 5.8 Numbers

Every large number gets one familiar comparison. Never seven numbers in one paragraph: state the
range once, name the best-supported figure, and put the rest in the Known / Disputed pair.

### 5.9 Connectives and rhythm

"Also" adds a fact without saying how it connects; most of them become "because", "but", "so",
"after", or a full stop. One sentence of eight words or fewer somewhere in every hundred words.
Never four sentences in a row of nearly the same length. Never four sentences in a row with the
same subject ("He ... He ... He ... He ...").

### 5.10 Quotations

No quotation over 25 words in the body. Introduce the speaker by role. Gloss an archaic word in
parentheses. A long quotation that matters goes in a story box.

### 5.11 "Today"

One "today" per era, and it carries a number: "In 1900 the census counted about 250,000 Native
people. In 2020, 9.7 million people identified as American Indian or Alaska Native."

### 5.12 Repetition across chapters

The first chapter that tells an event owns the full telling. A later chapter gets one callback
sentence and the new angle, and may name the owner: "Chapter 2 tells the Beaver Wars in full; here
is what they did to the fur trade." Chapter 4 currently repeats Chapter 2's opening paragraph and
retells Leif Erikson. Cut to the callback.

### 5.13 Dates and abbreviations

Month-day-year everywhere ("March 31, 1776"). "US" in prose, "U.S." only inside a quoted name.
One percent style ("percent" in prose).

## 6. The front and back of the book

**Introduction.** One or two paragraphs: what the book is, how the grid works (37 subjects, the same
ten eras, read one subject through or one era across), how to use it (the cards, the strips, the
"can skip" lists, the glossary), and one sentence on where the facts come from. Under 300 words.

**Before you start** (about 150 words) and **Four ways to read this book** (a short list with
honest reading times) follow it. The ten-minute history (ten beats, one per era, about 90 words
each) comes next. These are furniture and may say "you".

**How We Know What Happened** moves to the back, cut to about a third of its length, keeping its
best three or four examples (John Punch, Amelia Stewart Knight, Jane at Jamestown, the Hoover Dam
count) and the three kinds of uncertainty. The rest of its examples are already in their chapters.

**Back matter**, built after the chapters are done: the glossary (every defined term, one line,
chapter of first use), a timeline of about 150 dates, the people index (every story subject, with
chapter and era), places to see, the movie list with accuracy notes, and the answers to all 111
questions.

## 7. Process for one chapter

1. Read the two style guides and this guide. Read the whole chapter. Run the measurement for it.
2. Decide the spine sentence, the three questions, the anchor, the "five minutes" span, the "can
   skip" list, and which eras need "By" lines and closers. Write them in the checkpoint first.
3. Write the chapter opening. Add the era strips.
4. Era by era, in order: the "By" lines, the body passes (5.1 to 5.13), the story boxes, the
   closer. Save and check after every era. Update the checkpoint after every era.
5. Write the chapter closing.
6. Read the opening and closing aloud in your head. Then read one whole era aloud the same way. If
   it sounds like a list, fix the list. If it sounds performed, fix the performance.
7. Checks: `node tools/validate_grid.js <file> --part` (0 errors), `python tools/project_state.py
   --punct <file>` (0/0), `python tools/project_state.py --check <slug> --stage prose` (PASS),
   `python tools/measure_readability.py <slug>` (for your report, not as a gate).
8. Report what you changed, what you cut and why, what you could not improve, and where you broke a
   rule on purpose because the chapter needed it.

Architecture first, then scenes and stories, then voice, then sentence mechanics, then
consistency, then a fact check against the bank. Do not polish sentences before the chapter has a
spine and an ending.

## 8. Self-review before reporting

- Does the first sentence of the chapter state the point? Could a reader stop after the opening
  and know what the chapter says?
- Are the three questions answered, word for word, in the closing?
- Is there a place to stop every 2,000 words in the long eras?
- Open three paragraphs at random. Does any start with a date? Is any over 90 words? Does any
  define a word a child knows?
- Open three story boxes at random. Does each open with a hook? Does each have a scene, not a
  résumé? Is each under 400 words, or longer for a reason you wrote down?
- Count the hedges in one era. Are they Known / Not known pairs, or fog?
- Read the ten era first sentences in a row. Do they differ?
- Is every added sentence a restatement, a navigation line, or a banked fact?
- Is the narrator a calm adult, and does the narrator stay out of the body?
- Did anything shrink? Is each cut listed, with the reason, in the checkpoint?
- Are there zero em dashes and zero semicolons, and does the chapter pass `--stage prose`?
