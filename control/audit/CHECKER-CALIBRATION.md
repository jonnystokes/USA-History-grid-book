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
| 3 | | | | | | | | |

### Sonnet misses by rule (real defects opus found and sonnet did not)

| Rule | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| The Reader (hard word undefined, long sentence) | 6 | 8 | |
| Personification | 3 | 6 (incl. Root Metaphors) | |
| Hard subjects §2 | 2 | 3 | |
| AI Cadence, Passives, Precise Words, Root Metaphors, Unanchored Comparatives | 1 each | | |
| Not in bank | 2 | 4 | |
| Information Order | | 3 | |
| Claims, Semantic Bleaching, Reification, Repeated units | | 1 each | |

### Cost

| Run | Sonnet tokens | Opus tokens |
|---|---|---|
| 1 | 248k (10.2 min) | 211k (8.2 min); fixer 364k (16.4 min) |
| 2 | 222k (8.4 min) | 195k (7.4 min); fixer 306k (14.0 min) |

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

## Verdict

<!-- After run 3: is sonnet close enough to opus to check the rest of the book alone? If not,
     what next: more calibration runs, or opus for some passes (for example Pass 2, hard
     subjects)? This is Jon's call; record the recommendation and his ruling. -->
