# TODO: the live plan and the current step

**Keep this file current.** Update it whenever a task starts or closes, whenever Jon makes a
decision, and before any window closes. The measured truth is `python tools/project_state.py`.
The record of what happened is `control/WORKLOG.md` (read the tail). The cloud-era TODO is archived
at `control/archive/cloud/TODO-at-cloud-stop-2026-09-26.md`.

Last updated: 2026-09-29 (LOCAL, Jon's PC, branch `feature/local-cloud-code-homebrew`)

---

## NOW

NOW-RUNNING: T-324 storytelling-evolution (ONE writer, all 10 eras)

**STEP 1 (RESEARCH): COMPLETE 2026-09-29.** All 37 chapters pass `--stage research`. 684 stories, all verified.
**STEP 2 (WRITING): IN PROGRESS.** 30 chapters written and passing `--stage prose`, 7 to go. Nothing in flight. T-324 storytelling-evolution running (single writer). Art goes last in the Large group, after Jon answers the Wiley question.

Written (30): native-nations, city-building, immigration, science, elements, land-environment, economy (cloud era) ·
landmarks, energy, technology, home-family, transportation, food-farming, migration, money, work-workers,
marketplace, big-business, america-world, slavery-freedom, styles, government-politics, exploration, holidays, drugs-alcohol, crime-justice, disasters, war, news-communication, music (this run).

**Open for Jon:** art era 10 tells Kehinde Wiley. Four men have accused him of sexual assault since May 2024; he
denies it; no court outcome found. The research agent kept it out of the outline and flagged it in the bank. Tell it
or leave it out? (Blocks nothing until art is written.)

## How writing runs now (Jon, 2026-09-29)

- **Jon sets how many agents run at once** (DECISIONS #25, #27): more when the 5-hour window is fresh, one or two
  near the limit, and ONE for any new kind of task until he has measured its size.
- **One agent per chapter at a time, in order** (each writer adds to the chapter's research bank). Parallelism is
  across chapters. Start the longest chains first so they do not finish last.
- **Single-writer mode** (DECISIONS #26): one writer does all ten eras and all three part files where the chapter
  fits. Measured: 360k-495k tokens, 18-28 min (about 22k-28k tokens per 1,000 words written), about 8% of a 5-hour window per chapter (T-313: 72% -> 80%).
- Brief: `control/briefs/WRITER.md`. Model: opus. The director's prompt, cycle and sizing: `control/briefs/WRITER-DISPATCH.md`. Checkpoint per chapter from `tools/mk_writer_checkpoint.py`.

## STEP 2 queue: what is left

| Group | Chapters | Agents | Total |
|---|---|---|---|
| Large (single writer, reading in three slices; T-321 war proved ~54k fits) | storytelling-evolution, sports-play, health, art (last) | 1 | **4** |
| Giant (split by eras, in order) | rights-movements (~4), education (~4), religion (~3) | 3-4 | **~11** |

Sizes (outline + bank words) are measured with `python tools/slice_bank.py <slug> --eras <a-b> --summary`.
Giant slices: religion 1-7 ~50k / 8-10 ~37k · education ~52k / ~69k · rights-movements ~56k / ~80k.
Split any writer whose slice passes ~40,000 words.

## After step 2

- **STEP 3 audit:** ~111 sonnet checkers (one per part file) + 3 opus calibration twins (`control/briefs/CHECKER.md`,
  `control/audit/CHECKER-CALIBRATION.md`). Read-only, so many can run at once.
- **STEP 4 research round 2** (`GAPS.md`): writers' OPEN items (so far none) + audit NEEDS-RESEARCH items + T-243e
  (economy's 19 old blocking gaps, collected in the cloud era, in `control/checkpoints/T-243-economy.md`).
- **STEP 5 fixes** (`FIXER.md`, opus), **STEP 6** audit again, **STEP 7** polish (afterword `how-we-know`, notes for
  it are in `control/AUDIT-QUEUE.md`; full-book build; viewer check), **STEP 8** done.

## Director tools (permanent copies in tools/, 2026-09-29)

- `tools/director_task.py open <tid> <slug> <cpbase> "<title>"` writes the IN-FLIGHT ledger entry and commits;
  `close <tid> <slug> <cpbase> <tokens> <tools> <ms> "<result>" [extra paths]` runs the check, closes the entry,
  marks the checkpoint, adds a usage row and commits named paths. Set `STAGE=prose` for writers.
- `tools/file_parks.py <checkpoint files>` files each checkpoint's TO PARK items into the target banks and marks the
  section FILED. Rename old FILED headers first (see WORKLOG 2026-09-29). `tools/dedupe_parks.py` removes exact
  duplicate parked sections.
- `tools/mk_writer_checkpoint.py T-3nn:<slug>[:single]` and `tools/mk_research_checkpoint.py` make checkpoints.
- `tools/slice_bank.py` gives an agent only its eras.

## Standing rules (details in control/DECISIONS.md)

Eight steps in order (#17) · opus writes, researches, fixes; sonnet checks (#18) · no GitHub; one local commit per
sub-agent (#19) · never shrink the book (#20) · writers research their own small gaps, never break the fourth wall
(#21) · first three sonnet checks calibrated against opus (#22) · Tulsa: rights-movements leads (#23) · burst mode on
Jon's word only (#25) · single-writer mode (#26) · Jon sets the agent count (#27).
