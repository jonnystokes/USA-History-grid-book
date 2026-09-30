# ROADMAP: from here to a finished book

**Restructured 2026-09-26 on Jon's instruction** (DECISIONS #17) into eight steps:

1. Research. 2. Write. 3. Audit the whole thing. 4. More research. 5. More writing.
6. Audit. 7. Polish. 8. Done.

**Steps 1 and 2 aim at feature complete.** Research and write each chapter once, fully.
Steps 4 and 5 exist only for the gaps that writing and auditing turn up, and the writers now
research their own small gaps as they go (DECISIONS #21), so steps 4 and 5 should be small.
**No step starts until the one before it is finished for the whole book.**

**The book's size is intended** (DECISIONS #20). History is huge, and this book tells all of
American history from every perspective. Finished chapters run 13,000 to 17,000 words, and
that is right. Efficiency comes from overhead (reading, duplicate passes, agent count, the
model used for checking), never from length or coverage.

Numbers here are measured by `python tools/project_state.py`. Re-measure before trusting them.
The previous roadmap (three phases, 2026-09-07) is in git history. Its reasoning about reading
instead of pattern-matching is kept in step 3 below.

---

## Where the book is (measured 2026-09-26)

| Measure | Value |
|---|---|
| Chapters | 37, all with valid ten-era grid outlines |
| Stories | 620 (430 verified, 87 candidate, 103 target) |
| Outlines | 237,936 words |
| Research banks | 410,120 words |
| Written and passing `--stage prose` | **7**: native-nations, city-building, immigration, science, elements, land-environment, economy (about 110,000 words) |
| Pass `--stage research`, not written | **5**: government-politics, war, religion, education, rights-movements |
| `RESEARCHED*` (need a patch) | **13** |
| `SEED` | **11**, and `exploration` is `PARTIAL` |

**What a chapter has cost (cloud, 2026-09-26):** a bank check about 200k tokens, three writers
about 160k to 250k each, a gap agent about 265k to 385k. That is 1.0M to 1.2M tokens a chapter.
The 2026-09-26 changes remove the separate bank-check agent (folded into research), the third
writer (two writers per chapter) and the per-chapter gap agent (writers research their own
gaps), and they cut each agent's reading with `tools/slice_bank.py`. Measure the new cost in
`control/usage-log.tsv` before sizing anything off it.

---

## STEP 1: Research everything (COMPLETE 2026-09-29: all 37 chapters pass)

Brief: `control/briefs/RESEARCH.md` (model opus). **Every research task ends with the bank
check,** so the writers find the bank complete. Gates: `--stage research`, or `--stage patch`
for a patched chapter.

**Sizing:** use `python tools/slice_bank.py <slug> --eras <a-b> --summary`. Past full-research
agents used 300k to 400k tokens for half a chapter, and single agents asked to research a whole
chapter died having written nothing (`america-world`, twice). Split full research into eras 1-5
and 6-10. Split further when a slice passes about 25,000 words.

**1a. Patch the 13 `RESEARCHED*` chapters** (mode `patch`, usually one agent each):
`migration` · `home-family` · `technology` · `energy` · `transportation` · `landmarks` ·
`work-workers` · `food-farming` · `money` · `marketplace` · `america-world` ·
`slavery-freedom` · `big-business` (its bank is 409 words against a 6,759-word outline. The
sources are inline in the outline, so this is mostly a write-up).
Known debt: `energy` (5 of 11 stories unverified) · `home-family` (6 unfilled of 16, both
2000-today stories placeholders) · `technology` · **the kitchen thread** (spans home-family,
technology and energy, entirely unsourced, so fix it once across all three) · `marketplace`
(largest outline, thinnest backing).

**1b. `exploration`** (mode `full` on a `PARTIAL` chapter): reformat the seven-section bank to
ten eras, add per-fact citations, clear 9 candidates.

**1c. Bank check the 5 chapters that pass research** (mode `bankcheck`): `government-politics`
· `war` · `religion` · `education` · `rights-movements`. The last three have banks of 40,000 to
56,000 words, so split their checks by eras.

**1d. Research the seeds that have parked material** (mode `full`, about two agents each):
`health` · `disasters` · `crime-justice` · `drugs-alcohol`. `hard-subjects-policy.md` matters
most here.

**1e. Research from scratch** (mode `full`): `art` (115 `[VERIFY]`, empty bank) · `music` (128
`[VERIFY]`, empty bank, Dolly Parton is its flagship modern story) · `storytelling-evolution`
(65 `[VERIFY]`, 22 targets, empty bank) · `news-communication` · `sports-play` · `styles` ·
`holidays`. The first three may need three agents each.

**Step 1 ends when all 37 chapters pass `--stage research` or `--stage patch`.**

---

## STEP 2: Write everything

Brief: `control/briefs/WRITER.md` (model opus). **Single-writer mode where the chapter fits**
(DECISIONS #26, 2026-09-29): one writer does all ten eras and all three files (`part1-before-1800.md`,
`part2-1800s.md`, `part3-1900s-and-today.md`), about 8% of a 5-hour window per chapter. Larger
chapters get two writers (eras 1-7, then 8-10). The giants (`education`, `rights-movements`,
`religion`) are split further along era lines, still into the same three files. One writer per
chapter at a time, in order; parallelism is across chapters, longest chains first; Jon sets how many
run at once (#27). Status on 2026-09-29: 23 written, 14 to go (see `control/TODO.md`).

**The writer researches its own gaps** (DECISIONS #21): a few searches per question. What it
finds goes into the bank as a PATCH, then into the prose. What it cannot find goes into the bank
as SEARCHED, NOT FOUND and is written honestly as unrecorded. The aim is no open questions
left behind.

Order: the chapters that passed research first, then the patched ones, then the newly
researched. `native-nations` and `city-building` set the house voice, and
`manuscript/science/part1-before-1800.md` is the layout model.

**Standing obligations:** override a bad source in the prose and name it in the report (the
director parks it in `control/AUDIT-QUEUE.md`). Refresh perishable facts in the chapter being
written: Bears Ears (July 2026 reduction to about 121,100 acres, litigation promised) ·
corporal-punishment counts · CAHSR and FHWA figures · H-2A farm-labor figures (FY2024) ·
element 120 · nuclear restarts and SMRs · gig-work litigation (Pew data is Aug 2021) · federal
privacy law · Confederate monument removals · wolf delisting.

Gate: `--stage prose`. **Step 2 ends when all 37 chapters pass it.**

---

## STEP 3: Audit the whole book (read, report, edit nothing)

Brief: `control/briefs/CHECKER.md` (model sonnet), one checker per part file, writing findings
with suggested repairs to `control/audit/<slug>/`. **Calibration first:** the first three part
files are also checked by opus with the same brief, and the fixer's verdicts show what sonnet
misses. The brief is improved until sonnet matches opus (`control/audit/CHECKER-CALIBRATION.md`).

**Language cannot be audited by pattern matching.** A search finds "empty prairie" and walks
past "the land was open for the taking", which is the same erasure. Every defect this project
has caught was caught by an AI reading a sentence and understanding what it was doing. The
scripts still run (`validate_grid.js`, `project_state.py --check`, `--punct`) because they are
authoritative on file syntax, and the checker runs them too. They say nothing about whether the
book is good.

The checker's six passes cover the three old audits: **structure** (the 25 silent failures in
`VIEWER-CONTRACT.md` §3), **language** (every Version 2 rule, the amendment, and one voice
across 37 chapters) and **fact and source** (every fact against the bank: who was already there,
what the number actually says, whether two dates can both be true).

`control/AUDIT-QUEUE.md` holds the defects already known. They join the findings.

**Every finding is also evidence about the writing instructions.** A defect that appears in
several chapters means the writer brief let it through. Fix the brief as well as the sentence.

---

## STEP 4: Research round 2

Brief: `control/briefs/GAPS.md` (model opus). Only what is left: items writers marked OPEN,
and audit findings the fixer marks NEEDS-RESEARCH. A `SEARCHED, NOT FOUND` entry in the bank
is settled unless a new lead appears.

## STEP 5: Writing round 2

Brief: `control/briefs/FIXER.md` (model opus) for the audit findings, and `GAPS.md` for the
passages the new research changes. The fixer judges every finding. It does not apply them
blindly.

## STEP 6: Audit again

`CHECKER.md` (sonnet) on every part file changed in step 5, and a lighter read of the rest.
The expected result is a clean report. If it is not clean, fix the instructions that let the
defects through before repairing chapters.

## STEP 7: Polish

Fix what step 6 found (`FIXER.md`, opus). Write the afterword `how-we-know` (not a grid chapter,
no eras). Rebuild `outlines/BOOK-OUTLINE.md` and the full book. Open it in `viewer/viewer.html`
(v2) and look at it. Jon's own audit pass. Final render.

## STEP 8: Done.
