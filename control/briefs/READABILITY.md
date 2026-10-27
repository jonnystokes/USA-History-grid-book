# READABILITY brief: the second edition of one chapter (model: fable, or the best available)

The dispatch gives you the TASK id, the CHAPTER slug and the CHECKPOINT. You are rewriting one
finished chapter so a reader who cannot hold attention long can get through it and want to. You
are not re-researching it and not restructuring the grid. Everything you need to know about the
shape is in `control/ARCHITECTURE-GUIDE.md`. Everything about the sentences is in the two style
guides. Jon's instruction to you, in his words: do not rely on lint; rely on your intelligence and
your ability to read the text and judge how well it follows the guides, and rewrite it to follow
them. Make up your own mind about what makes this chapter the best it can be.

## Read first, in full, in this order

1. `control/writing-style-guide.md` (the amendment, BINDING; §0 has Jon's seven guidelines and the
   reworded guideline 7, DECISIONS #51).
2. `control/ARCHITECTURE-GUIDE.md` (BINDING for structure and the narrator).
3. `control/general-writing-style-guide.md` (Version 2, BINDING for sentences; note the three
   furniture exceptions added 2026-10-26).
4. `control/hard-subjects-policy.md` (BINDING).
5. `control/DECISIONS.md` rows #28 to #53.
6. The whole chapter: all three part files, start to finish, before you change a word.
7. `python tools/measure_readability.py <slug>`: a first indicator of where to look.

## What you may touch

Your chapter's three part files, `manuscript/<slug>/part*.md`, and your checkpoint. The bank
`research/research-<slug>.md` only to add a PATCH when a furniture sentence needs a fact not yet
banked (rare: openings restate). Nothing else. No git. No installs. No sub-agents. No other chapter.

## What you must not do

Move, merge, split or remove any chapter, era, span or story. Change any marker line, era id,
story slug, `status=`, `progress=`, `movie=` or record key. Add a fact that is not already in the
chapter or the bank. Collapse a worked passage into a summary (DECISIONS #52; a cut is allowed only
when it makes the chapter better, and every cut is listed in the checkpoint with its reason).
Change the facts. Soften anything (the hard-subjects policy stands in full). Mention the research,
agents, drafts or AI in the prose.

## Process

Follow `ARCHITECTURE-GUIDE.md` §7 exactly: read, measure, decide the spine and the three questions
and write them in the checkpoint first, then the opening, strips, and era by era the "By" lines,
body passes, story boxes and closers, then the closing, then the self-review in §8.

**Checkpoint first.** Create `control/checkpoints/<TASK>-readability.md` from
`control/checkpoints/_TEMPLATE.md` before any edit: units = the opening, each of the ten eras, the
closing. Put the spine sentence, the three questions, the anchor, the "five minutes" span and the
"can skip" list in the SUBJECT NOTES section before you write them into the chapter. Update the
checkpoint after every era with what changed, what was cut and why, and what you chose not to do.
**If the checkpoint already exists when you start, you were interrupted: read it and carry on from
NOW. Do not redo finished eras.**

**Checks after every part file you save:** `node tools/validate_grid.js <file> --part` (0 errors)
and `python tools/project_state.py --punct <file>` (0/0). Before you report:
`python tools/project_state.py --check <slug> --stage prose` must PASS, and run
`python tools/measure_readability.py <slug>` for the report.

## Pacing (Jon's standing rules)

Update the checkpoint after each era before anything else. Check the 5-hour window about a quarter,
half and three-quarters of the way through, by feel: ToolSearch
`select:mcp__ccd_session_mgmt__get_usage`, read only its `plan` part. Above 95%: finish the era in
hand, update the checkpoint, report that you are not done, and stop. The director resumes you after
the reset. At the weekly limit: report and halt. No routine context checks.

## Report (under 300 words, no prose pasted)

The spine sentence and the three questions. Per era: what furniture was added, how many paragraphs
split, how many story boxes reshaped, what was cut and why. Any rule you broke on purpose and why.
What you could not improve. The before and after lines from `measure_readability.py`. The `--check`
output last.
