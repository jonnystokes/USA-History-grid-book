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
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

### Sonnet misses by rule (real defects opus found and sonnet did not)

| Rule | Run 1 | Run 2 | Run 3 |
|---|---|---|---|

### Cost

| Run | Sonnet tokens | Opus tokens |
|---|---|---|

## Brief changes

<!-- date | change to CHECKER.md | the misses it answers -->

## Verdict

<!-- After run 3: is sonnet close enough to opus to check the rest of the book alone? If not,
     what next: more calibration runs, or opus for some passes (for example Pass 2, hard
     subjects)? This is Jon's call; record the recommendation and his ruling. -->
