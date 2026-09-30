# Checker calibration: sonnet against opus (Jon, 2026-09-26)

**Why:** reading and checking runs on sonnet to save money. Sonnet is less capable, so it needs
sharper instructions. For the first three checker runs, the same part file is checked twice with
the same brief (`control/briefs/CHECKER.md`), once by sonnet and once by opus. The results show
what sonnet misses, and the brief is improved until sonnet matches opus.

## How a calibration run works

1. Dispatch the sonnet checker. Its findings go to `control/audit/<slug>/<part>-findings-sonnet.md`.
2. Dispatch the opus checker on the same file with the same brief. Its findings go to
   `...-findings-opus.md`. Record the usage-log row for each.
3. Dispatch the opus FIXER with BOTH findings files. It judges every finding (FIXED, REJECTED,
   NEEDS-RESEARCH), notes which checker found each one, and adds rows for defects both missed.
   The fixer's verdicts are the ground truth.
4. The director fills in the table below from the verdict columns, then edits `CHECKER.md`
   to target each pattern of misses. Every edit is recorded under "Brief changes".

## Results

| Run | Part file | Real defects (fixer) | Found by sonnet | Found by opus | Found by both | Sonnet false findings | Opus false findings | Found only by fixer |
|---|---|---|---|---|---|---|---|---|
| 1 | native-nations part1 (5,813w, cloud era) | 99 | 78 (79%) | 77 (78%) | 59 | 18 of 101 (18%) | 5 of 85 (6%) | 3 |
| 2 | crime-justice part2 (5,488w, hard subjects) | 110 | 76 (69%) | 74 (67%) | 46 | 11 of 89 (12%) | 1 of 79 (1%) | 6 |
| 3 | government-politics part3 (10,507w, 1900-today) | 192 | 134 (70%) | 127 (66%) | 77 | 10 of 160 (6%) | 1 of 143 (1%) | 8 |

### Sonnet misses by rule (real defects opus found and sonnet did not)

| Rule | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| The Reader (hard word undefined, long sentence) | 6 | 8 | 13 |
| Personification | 3 | 6 (incl. Root Metaphors) | 20 |
| Hard subjects §2 | 2 | 3 | |
| AI Cadence, Passives, Precise Words, Root Metaphors, Unanchored Comparatives | 1 each | | |
| Not in bank | 2 | 4 | |
| Information Order | | 3 | 3 |
| Precise Words, Teaching Point | | | 3 each |
| Claims, Semantic Bleaching, Reification, Repeated units | | 1 each | |

### Cost

| Run | Sonnet tokens | Opus tokens |
|---|---|---|
| 1 | 248k (10.2 min) | 211k (8.2 min); fixer 364k (16.4 min) |
| 2 | 222k (8.4 min) | 195k (7.4 min); fixer 306k (14.0 min) |
| 3 | 266k (9.4 min) | 274k (12.4 min); fixer 395k (19.9 min) |

## Brief changes

<!-- date | change to CHECKER.md | the misses it answers -->
- 2026-09-30, after run 1: (a) Pass 1: before reporting "Not in bank", grep the WHOLE chapter bank and its PATCH
  sections, not only the era slice (sonnet's most common false finding). (b) Pass 5: "No surviving record
  names..." / "the records do not say" is the prescribed sentence, not a defect, and needs no SEARCHED, NOT FOUND
  line (sonnet's other false finding). (c) Pass 5: list every word a sixth-grader might not know (proclamation,
  inquiry, treaty...) and check each is defined at first use in this file (sonnet's largest miss). (d) Pass 3:
  a nation named as a people may act; a state, colony or crown may not (director ruling, run 1). (e) Leave
  hb-note editor notes alone.
- 2026-09-30, after run 2 (sonnet's false findings were mostly Structure; its misses were The Reader and false
  actors again): (f) "What not to do": the `### Name` heading inside an hb-story is the template (grid-markers
  §8), not a defect; never propose moving text between eras or cells; a date outside the era's range is not a
  defect. (g) Pass 3: news outlets, newspapers, committees, boards, juries-as-institutions acting are false
  actors too; list every sentence subject in the era and test each one. (h) Pass 5: the hard-word list comes
  before the other Pass 5 checks, and law and court words (grand jury, penitentiary, reprieve, posse, pardon)
  are always on it.

## Verdict (director's recommendation, 2026-09-30; Jon's ruling pending)

**The numbers across three runs:** sonnet found 79%, 69%, 70% of the real defects; opus 78%, 67%, 66%. Sonnet's
false findings fell with each brief change: 18%, 12%, 6% (opus 6%, 1%, 1%). **Sonnet now finds as many real defects
as opus.** The two models overlap on only 40-60%: each alone misses about 30%, and the fixer adds only 3-8 per file.

**What this means:** the checker model is not the limit. A single read of any model misses about a third. The
number of independent reads is what matters (two reads catch roughly 90%).

**Recommendation:** check the remaining 108 part files with **sonnet alone** now (the cheapest, and as good as
opus), and count on the plan's **second audit (step 6)** as the second independent read of every file. If Jon wants
more before step 5, the next-cheapest option is a second sonnet read per file with the six passes split between two
checkers (facts and hard subjects; language and reader), which would need its own small calibration first.

**Cost of the remaining audit, sonnet alone:** about 245k tokens and 9 minutes per part file, ~108 files.

**Jon's ruling:** (pending). Until he rules, the director proceeds with sonnet alone, one at a time, which changes
no chapter (checkers only read) and so costs nothing to extend later.
