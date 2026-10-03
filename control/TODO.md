# TODO: the live plan and the current step

**Keep this file current.** Update it whenever a task starts or closes, whenever Jon makes a
decision, and before any window closes. The measured truth is `python tools/project_state.py`.
The record of what happened is `control/WORKLOG.md` (read the tail). The cloud-era TODO is archived
at `control/archive/cloud/TODO-at-cloud-stop-2026-09-26.md`.

Last updated: 2026-09-29 (LOCAL, Jon's PC, branch `feature/local-cloud-code-homebrew`)

---

## NOW (2026-10-03)

**STEPS 1-6 COMPLETE. STEP 7 nearly done.** All 37 chapters fixed on the second-audit findings (T-600..T-639,
plan in control/STEP7-PLAN.md) and passing; POLISH-1 (T-640) cleared the book-wide items; outlines rebuilt to match
(T-641); afterword written at manuscript/_afterword/how-we-know.md (T-642); full-book build running (T-643).
Manuscript ~817,000 words, 684 stories verified. Next: Jon's read of build/, then the final render (step 8).
Open small items: the NEEDS-RESEARCH lines in control/checkpoints/F7-*.md and the unclosed AUDIT-QUEUE items.



NOW-RUNNING: T-486 news-communication (RESEARCH round 2 R4-culture: news-communication music storytelling-evolution sports-play styles art holidays)

**STEP 1 (RESEARCH): COMPLETE 2026-09-29.** All 37 chapters pass `--stage research`. 684 stories, all verified.
**STEP 2 (WRITING): COMPLETE 2026-09-30.** All 37 chapters pass `--stage prose` (111 part files, 0 validator
errors, 0 em dashes, 0 semicolons). Manuscript ~711,000 words, 684 stories, all verified. This run: T-315 to T-330
(16 chapters, 22 writer agents, 2026-09-29/30).

**STEP 4 (RESEARCH ROUND 2): COMPLETE 2026-10-02** (R-1, T-484..T-488).
**STEP 6 (SECOND AUDIT): COMPLETE 2026-10-02.** 111/111 files re-read by sonnet (findings in control/audit/<slug>/<part>-findings-r2.md); about 38 findings and 3 blocking per file, half of round 1. NEXT: step 7, opus fixers per chapter on the r2 findings, then polish (afterword, outline rebuild, full-book build, Jon's read).

**STEP 5 (FIXES, done before the round-2 research leftovers): COMPLETE 2026-10-02.** All 37 chapters fixed by opus whole-chapter fixers (T-442..T-482, waves of 6-8; giants split by part), each fixer researching its own gaps (DECISIONS #21). All 37 PASS prose, 111 part files validate. Manuscript ~785,000 words. Open items for round 2: the NEEDS-RESEARCH lists in control/checkpoints/F5-*.md and control/AUDIT-QUEUE.md (priority: DECISIONS #32 Hemings/Wayles wording).

**STEP 3 (AUDIT): COMPLETE 2026-10-01.** All 111 part files checked by sonnet (T-331..T-441): about 9,700 findings, about 1,000 BLOCKING, in `control/audit/<slug>/<part>-findings-sonnet.md`. The 3 calibration files were also fixed already. Calibration COMPLETE (3 runs, T-331..T-333). Now the sonnet checker on the other 108
part files, one at a time: `python tools/audit_status.py` shows progress and the next file; the prompt and cycle are in
`control/briefs/CHECKER-DISPATCH.md`.

**For Jon: the calibration verdict** (`control/audit/CHECKER-CALIBRATION.md`, "Verdict"). Sonnet now finds as many real
defects as opus (70% vs 66% in run 3) with 6% false findings. But any single read misses about a third, and the two
models overlap on only 40-60%. Recommendation: sonnet alone now, step 6 as the second read. Proceeding that way until
Jon rules (checkers change no chapter, so a second read can be added later at no loss).

**Open for Jon:** art era 10, Kehinde Wiley. Four men have accused him of sexual assault since May 2024; he denies
it; no court outcome found. The story block is written from his life and work only, accusations left out
(T-330). Jon's answer changes that one block in step 5: tell the accusations, keep as is, or swap in another artist.

**For Jon to review (director ruling, T-331f):** native-nations part 1, Acoma 1598. The prose said the soldiers
"assaulted" an Acoma woman. Following the hard-subjects policy (no softening), it now states the Acoma people's own
account plainly: the soldiers raped her, with the word defined in plain words. Keep, or rule otherwise.

**Calibration run 1 (native-nations part1):** 99 real defects; sonnet found 78, opus 77, both 59; sonnet false
findings 18%, opus 6%. CHECKER.md sharpened (see CHECKER-CALIBRATION.md, "Brief changes").
**Run 2 (crime-justice part2):** 110 real; sonnet 76, opus 74, both 46; false findings sonnet 12%, opus 1%.
**Run 3 (government-politics part3):** 192 real; sonnet 134, opus 127, both 77; false sonnet 6%, opus 1%. The three
calibration files were also fixed by the opus fixers (step-5 work done early; each file grew, 5.5-10.5k to 6.1-12.6k).

## How step 2 ran (for the record; the director's prompt and sizing are in control/briefs/WRITER-DISPATCH.md)

- One writer per chapter up to ~60k words of outline+bank (war 54k, music 60k landed cleanly, 20-22k tokens per
  1,000 words written). Two writers cost ~25% more per word (disasters). The giants split by era: religion 2
  writers (1-7, 8-10), education and rights-movements 3 writers (1-7, 8-9, 10).
- Writers researched their own gaps (about 140 PATCHes this run), left ~320 unsourced outline claims out, and
  logged every era in their checkpoint. Items for the audit are in `control/AUDIT-QUEUE.md`.
- exploration (T-316) was written with web research blocked by the usage limit: 6 questions for step 4.

## STEP 3 plan: audit the whole book (read, report, edit nothing)

1. **Calibration (3 runs).** For each of 3 part files: a sonnet checker, an opus checker (same brief,
   `control/briefs/CHECKER.md`), then an opus fixer judging both findings files (`FIXER.md`). Fill in
   `control/audit/CHECKER-CALIBRATION.md` and sharpen CHECKER.md after each run.
   Files: native-nations part1 (house voice, cloud era, 5.8k words) · crime-justice part2 (hard subjects,
   5.5k) · government-politics part3 (2000-today, 10.5k).
2. **Jon's call** on the verdict (sonnet alone, or opus for some passes).
3. **The rest:** one checker per part file, 108 more, findings to `control/audit/<slug>/<part>-findings-<model>.md`.
   Read-only, so several can run at once when Jon says.

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
