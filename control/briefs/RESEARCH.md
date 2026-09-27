# RESEARCH brief: research, patch, or bank check one chapter (model: opus)

The dispatch gives you the TASK id, the CHAPTER slug, the MODE, the ERAS and the CHECKPOINT.
This brief replaces the old separate BANKCHECK agent (2026-09-26): **every research task now
ends with the bank check**, so the writers find the bank complete and write once.

| MODE | For a chapter that measures | Your job | Gate |
|---|---|---|---|
| `full` | `SEED` or `PARTIAL` | Research the eras from scratch, then run the bank check | `--stage research` |
| `patch` | `RESEARCHED*` | Clear every `target`, `candidate` and `[VERIFY]`, grow the bank to at least the outline's size, then run the bank check | `--stage patch` (and `--stage research` if you can reach it) |
| `bankcheck` | `RESEARCHED` | Run the bank check only | `--stage research` must still pass |

## Read first

1. `control/AGENT-BRIEF.md`, in full. It is the research procedure: the ten eras, the three
   zooms, no invented facts, sources, stories, cross-chapter parking, what you deliver.
2. `control/hard-subjects-policy.md` (BINDING).
3. `control/general-writing-style-guide.md` (Version 2, BINDING, read in full) and
   `control/writing-style-guide.md` (the amendment, BINDING). They govern every sentence you
   write into the outline as book prose.
4. `control/chapter-registry.md`: your chapter's angle, and what belongs to its neighbours.
5. `control/grid-markers.md` and `control/VIEWER-COMPAT.md` (the outline format).
6. Your chapter: `outlines/<slug>.md`, `workspace/<slug>.md`, `research/research-<slug>.md`.
   When the bank or outline is large, read your eras with
   `python tools/slice_bank.py <slug> --eras <a-b>`, which includes the "Parked from" sections
   other agents left for you.
7. The checkpoint. Its SUBJECT NOTES name hard subjects to look for and perishable facts to
   refresh.

## The bank check (the last unit of every mode)

Compare the bank against the outline and the registry's definition of the chapter. Find:

1. **Hard subjects the chapter must cover that the bank does not:** violence, deaths,
   expulsions, land taken, people poisoned, exploited or experimented on, and who did each.
   Decide each subject's owner with the registry. Park material that belongs elsewhere.
2. **Every event in the bank with no named actor, no cause or no count.** Go through the bank
   era by era and ask of each harm: who did it, what exactly was done, why, and how many? This
   is the question the writers will hit. Past chapters still produced 13 to 19 writer gaps each
   after a bank check, nearly all of them this question.
3. **Outline claims the writers will need that the bank lacks,** including any "first" or
   superlative. Check each "first" against the bank and the sources.
4. **Perishable facts:** re-verify anything the checkpoint names, and anything dated in the
   2000-today era, as current to today's date.
5. **Land.** Wherever newcomers take or settle land, record which nation or people lived there.

For each gap, research it and APPEND it under the right era:

    ### PATCH <date> (<TASK>): <topic>

with an inline source per fact, named actors, and numbers with their ranges and whose count
each is. Where sources disagree, record every figure. Do not rewrite existing bank text. If it
is wrong, add a correction note beside it.

**When a question cannot be answered, record the search, so no writer asks it again:**

    ### SEARCHED, NOT FOUND <date> (<TASK>): <the exact question>
    Sources checked: <each source, and what it does say>.
    How the prose can say it: <for example, "The records do not name the men who fired.">

Writers treat these as settled. Give a question a few good searches (roughly four or five,
across the source types AGENT-BRIEF §3 prefers). Stop there when nothing turns up. Aim at the
gaps a writer would hit, and stop when they are covered.

## Saving

Work one era at a time. After each era, write it to the files and validate with
`node tools/validate_grid.js outlines/<slug>.md`. Errors mid-write are normal. The last run
must be clean. Update the checkpoint: what landed, sources in hand (URL and what it settled),
what you left out and why, and NEXT. No git.

The LAST agent on a chapter also checks that every era's `progress=` flag matches its real
state. A single era left at `progress="seed"` fails the chapter check on its own.

## Report

Under 200 words: eras covered, strongest stories, gaps filled (one line each), SEARCHED, NOT
FOUND entries (count, and one line each for hard subjects), anything parked elsewhere,
unsupported "firsts", perishable facts refreshed. Paste the output of
`python tools/project_state.py --check <slug> --stage <research|patch>` as your last line.
