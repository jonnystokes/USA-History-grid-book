# WRITER brief (Phase 2, cloud and local)

The director's dispatch message gives you: the TASK id, the CHAPTER slug, the PART file, the
ERAS, the CHECKPOINT file and your UNIT number. Everything else is here. This file holds the
standard writing brief from `control/RESUME.md`, with the rules added on 2026-09-26.

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
5. Your chapter's `outlines/<slug>.md`, `research/research-<slug>.md` (grep it for your eras
   when it is large) and `workspace/<slug>.md`.
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
shows only this chapter's files.

## Facts come from the research bank only (Jon, DECISIONS #13)

Every fact in your prose must be in `research/research-<slug>.md`. The outline is a plan of what
to cover. When it states something the bank does not contain, do not write it. List it in the
checkpoint's "Outline claims NOT in the bank". Thin eras are correct. Never pad. Do not add
identity glosses from general knowledge (a first name, "Swedish botanist") unless the bank has
them. The bank may carry "PATCH" sections added by a pre-write check. Use them, and follow any
correction note beside older text.

**A gap on a hard subject or a central cause is BLOCKING.** If the bank names harm but not who
did it, what was done or why, do not write "the sources do not record" in its place. Write the
rest, list the gap under "BLOCKING GAPS" in the checkpoint (era, passage, what is missing), and
report it. The director closes collected gaps after the last part.

**If your outline or bank contains a defect** (softening, a false comparison, a manufactured
dispute, personification, a false "first", a fact that contradicts itself), **fix it in your
prose and NAME IT in your report.** Do not repair the source file. Watch for land erasure:
when newcomers take land, name who lived there if the bank does. For 2000-today, give the year of
every figure and name its source in plain words. Name people, not institutions, as actors. The
outline may mention `_reference/`. That folder is not in the repository. Do not look for it.

## Checks

Write incrementally: create the file early and append one era at a time.
`node tools/validate_grid.js <file> --part`: **errors mid-write are normal. The run that
counts is your last one, and it must be clean.** `python tools/project_state.py --punct <file>`
must print zero for both. A quotation keeps its words exactly. If one contains a semicolon or an
em dash, split it at that point with no word changed. On the LAST part, also run
`python tools/project_state.py --check <slug> --stage prose`. Check file sizes before reading.
Never read `viewer/*.html` whole (line 89 is a 373 KB base64 image).

## Cloud: commit after every era

Only what you commit and push survives. Keep the checkpoint current: set NOW before each era.
After each era, add a Log line (words, validator, --punct), then run:

    git add manuscript/<slug>/<part>.md control/checkpoints/<checkpoint>.md
    git commit -m "<TASK> <slug> <part>: <era> written"
    git push -u origin claude/gifted-volta-lfl54k

Retry the push after 2, 4, 8 and 16 seconds on a network failure. Use `git add` with named paths
only. Never push to main. Touch no other file. When done, mark your unit `landed` and set NEXT
as the dispatch message says.

## Report

Under 200 words: what each era holds, the stories written, how many outline claims you left out,
the blocking gaps, and the defects you fixed. Paste the `--punct` output and the validator's last
line (or, on the last part, the prose check) as your last lines.
