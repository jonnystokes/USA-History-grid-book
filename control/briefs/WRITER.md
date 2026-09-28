# WRITER brief (Phase 2, model: opus)

The dispatch gives you the TASK id, the CHAPTER slug, the ERAS, the PART FILE or files you
write, the CHECKPOINT and your UNIT number. Everything else is here.

**Two writers per chapter** (2026-09-26). Writer A takes eras 1-7 and writes two files,
`part1-before-1800.md` (eras 1-5) and then `part2-1800s.md` (eras 6-7). Writer B takes eras
8-10 and writes `part3-1900s-and-today.md`. The file layout is the same as the finished
chapters. For a very large chapter the director may split further. Then the dispatch says which
eras you write and whether you create a file or append to one an earlier writer started.

**The goal is a finished chapter.** Write it once, completely, so it does not need a second
pass. Chapters run as long as the material honestly supports. Never trim for length and never
pad.

## Read before writing a word, in this order

1. `control/general-writing-style-guide.md`, the Writing Style Guide, Version 2. **BINDING, an
   absolute requirement, and the main instrument of this phase. Read all of it.** "The Reader"
   states who you are writing for. "The AI Cadence" names the patterns you are most likely to
   produce and least likely to notice. Assume you will produce them, and work against them.
   "The Teaching Point" is the positive standard: know what you are teaching and state it first.
   "Forbidden Punctuation" allows zero em dashes and zero semicolons, and the prose gate counts
   both. **"Self-Review Before Reporting" is a review you must actually run, repairing every
   defect it finds, before you report.**
2. `control/writing-style-guide.md`, **BINDING**: this book's amendment. It covers the reader
   (age 11, sentences averaging 12 to 18 words), the subject, the policy, and its audit
   additions in §5.
3. `control/hard-subjects-policy.md`, **BINDING.** No softening of any kind. Never invent a
   name. Define clinical words in plain language at first use.
4. `control/grid-markers.md` §7b · `control/VIEWER-CONTRACT.md` §2.
5. Your eras of the outline and the bank:
   `python tools/slice_bank.py <slug> --eras <your eras> -o <scratch file>`, then read that
   file. It holds the outline header, your eras of the outline, your eras of the bank
   (including the "Parked from" sections at the end of the bank), and every untagged bank
   section. Read `workspace/<slug>.md` too.
6. The chapter's earlier part files, if any. Match their voice and copy their layout exactly.
   Do not repeat what they explained. Do not edit them. For part 1, use
   `manuscript/science/part1-before-1800.md` as the model of voice and layout.

## File layout

The hb-chapter line copies the outline's id, slug, title and part, with `mode="prose"` and
`file="partN"`. Then the chapter heading, then an hb-note naming this file's eras, the bank and
the outline, then the hb-time sections with `progress="written"` and each era's `state=` from
the outline. Carry each story from the outline as an `hb-story` with the same slug, name and
`status="verified"`, with its `> **Key:** value` records, **but only when the bank sources it.**
Every story slug must be unique across the book: `grep -rl 'slug="<slug>"' outlines/ manuscript/`
shows only this chapter's files. Ignore hits in `outlines/BOOK-OUTLINE.md`: it is a compiled copy
of every outline, rebuilt at the polish step.

## Facts come from the research bank only (DECISIONS #13)

Every fact in your prose must be in `research/research-<slug>.md`. The outline is a plan of what
to cover, not a source. Do not add identity glosses from general knowledge (a first name,
"Swedish botanist") unless the bank has them. Use the bank's PATCH sections, and follow any
correction note beside older text. **A fact tagged `(unconfirmed: search summary only)` is not
yet a fact:** confirm it on a page you can open (then record that source in the bank) before you
write it, or leave it out. The same holds for any bank line still tagged `[VERIFY]` (older
parked sections carry some). A `SEARCHED, NOT FOUND` entry in the bank is a settled
answer: write what it says the prose can say, and do not research it again.

## When the bank is missing something: research it yourself (DECISIONS #21)

The research is mostly done. What remains are small facts you need to write good history
without adding fiction. Look them up yourself rather than leaving them for later.

1. **Which gaps to research.**
   - **Always:** a gap on a hard subject or a central cause. That means the bank names harm but
     not who did it, what was done, how many, or why.
   - **When a quick search settles it:** any other outline claim the bank lacks that makes the
     chapter better. Claims that would take real digging, or that add little, you leave out and
     list in the checkpoint under "Outline claims left out".
2. **Bank first, then prose.** Append what you find to the bank under its era as
   `### PATCH <date> (<TASK>): <topic>`, with an inline source per fact. A fact you saw only in
   a search-result summary is tagged `(unconfirmed: search summary only)` and not written. Prefer government,
   court, museum, university and archive sources (`control/AGENT-BRIEF.md` §3). Then write the
   sentence from the bank. Never write a fact that is not in the bank, even one you just read.
3. **A few searches per question, then stop.** Give each question about four or five good
   searches. If nothing turns up, record it in the bank:

       ### SEARCHED, NOT FOUND <date> (<TASK>): <the exact question>
       Sources checked: <each, and what it does say>.

   Then write the passage anyway, as well as the known facts allow, and invent nothing. Where
   a detail is unknown, write the way a history book does, from the side of the historical
   record: "No surviving record names the men who fired." "Historians do not know how many
   died. Estimates run from 40 to 90." "Who gave the order is not known." That is the honest,
   less specific version, and it is not softening. **Softening** is blurring what IS known: a
   vaguer word for the harm, a smaller number, or a passive that hides a known actor. It is
   still forbidden.
   **Never break the fourth wall** (Jon, 2026-09-26). The book never mentions itself, this
   project, research, searching, sources checked, agents, writers or drafts. Never write "in
   researching this", "while writing this chapter", "we could not find", "this book" or "our
   sources". The reader sees history, not the making of the book. The search itself belongs
   only in the bank and the checkpoint.
4. **Keep it proportionate.** You are a writer who checks facts, not a research agent. If a
   question would take more than a few searches, record it as not found and move on.

The aim: **no open questions left behind.** Every gap you hit ends as either a PATCH (found) or a
SEARCHED, NOT FOUND (recorded, and written honestly). Use "OPEN" in the checkpoint only for a
passage you judge cannot be written honestly at all without the missing fact. Expect that to be
rare, and say why.

## Defects in your sources

If your outline or bank contains a defect (softening, a false comparison, a manufactured
dispute, personification, a false "first", a fact that contradicts itself), **fix it in your
prose and NAME IT in your report.** Do not repair the source file. Watch for land erasure: when
newcomers take land, name who lived there. If the bank does not say, research it under the rule
above. For 2000-today, give the year of every figure and name its source in plain words. Name
people, not institutions, as actors. The outline may mention `_reference/`. Do not look for it.

## Checks and saving

Write incrementally: create the file early and append one era at a time. Before each era, set
the checkpoint's NOW line. After each era, add a Log line (words, validator, --punct) and the
era's PATCH and SEARCHED, NOT FOUND entries.

`node tools/validate_grid.js <file> --part`: **errors mid-write are normal. The run that counts
is your last one, and it must be clean.** `python tools/project_state.py --punct <file>` must
print zero for both. A quotation keeps its words exactly. If one contains a semicolon or an em
dash, split it at that point with no word changed. The chapter's LAST writer also runs
`python tools/project_state.py --check <slug> --stage prose`. No git: the director commits
after you finish. Install nothing (no pip or npm). Write text with the Write or Edit tool,
never a Bash heredoc (heredocs with apostrophes fail on this machine).

## Report

Under 200 words: what each era holds, the stories written, gaps researched (found, and
searched but not found, with counts), outline claims left out (count), anything OPEN and why,
and the defects you fixed. Paste the `--punct` output and the validator's last line (or, for the
last writer, the prose check) as your last lines.
