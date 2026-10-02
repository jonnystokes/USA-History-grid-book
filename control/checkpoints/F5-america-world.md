# CHECKPOINT F5 | america-world | step 5 fixer, whole chapter

STATUS: T-459 landed (director verified: PASS  america-world / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/america-world/part1|part2|part3 + control/audit/america-world/part1|2|3-findings-sonnet.md
        + research/research-america-world.md (PATCH entries only)

NOW:    finished
NEXT:   none (director: commit, then step 6 read)
VERDICTS: fixer column in each findings table; found-by-fixer rows are F1, F2... at the table end.
WORDS:  "before" in the Units table is the dispatch figure; the "tool" figures are
        tools/project_state.py prose_words() on the HEAD file and on the fixed file.

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH (+ found by fixer) | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 92 / 3 / 1 (+9) | 5553 -> (tool: 5136 -> 5387) |
| part2 | 6-7 | done | 74 / 7 / 0 (+5); #37 partly NR | 4173 -> (tool: 3851 -> 4442) |
| part3 | 8-10 | done | 78 / 7 / 0 (+13) | 7087 -> (tool: 6590 -> 7093) |

## NEEDS-RESEARCH
- part1 #53 (1700-1750, Louisbourg): what Pepperrell's "about 1,200 men lost" counts (dead only, or dead plus sick/sent home/deserted). Prose keeps the bank's wording.
- part2 #37 (1800-1850): the specific acts behind Britannica's "violence and discrimination" against Mexican Americans after 1848, beyond the squatter lynchings now in the prose.

## PATCHes added to research/research-america-world.md
- 2026-10-01 (T-459): the date of the first Matanzas killing (era 2)
- 2026-10-01 (T-459): the Dutch retaking of 1673 (era 3)
- 2026-10-01 (T-459): Florida 1818, the Monroe Doctrine's British side, who broke up the New Mexico land grants (+ California squatters, SJSU) (era 6)
- 2026-10-01 (T-459): Kake 1869, who ordered it and what it cost (era 7)
- 2026-10-01 (T-459): Smith's punishment, the Haitian legislature, Les Cayes (era 8)
- 2026-10-01 (T-459): Castle Bravo's people (copied from war and health banks), Blair House checked (era 9)
- 2026-10-01 (T-459): the Iraq counts and the Iranian dead (era 10)
- 2026-10-01 (T-459): four small era-5 facts checked (XYZ papers published by Adams; Britain-France war 1793; Barbary tribute; Tuscarora joined about 1722)

## Log
- part1 era 1 (before-1500): done. 11 FIXED, 0 REJ, 0 NR, 2 found by fixer. validate 0 errors, punct 0/0.
- part1 era 2 (1500s): done. 11 FIXED (21 partly rejected), 0 NR. PATCH Matanzas date. validate 0, punct 0/0.
- part1 era 3 (1600s): done. 13 FIXED, 1 REJ, 0 NR, 1 found by fixer. PATCH Dutch retaking 1673. validate 0, punct 0/0.
- part1 era 4 (1700-1750): done. 18 FIXED, 0 REJ, 1 NR (#53), 1 found by fixer. validate 0, punct 0/0.
- part1 era 5 (1750-1800): done. 39 FIXED, 2 REJ (+2 partial), 0 NR, 5 found by fixer. PATCH era-5 facts. validate 0, punct 0/0.
- PART 1 DONE.
- part2 era 6 (1800-1850): done. 37 FIXED, 7 REJ (3 of them because a PATCH sourced the fact), 0 NR left open (#37 partly: wider acts), 1 found by fixer. PATCH era-6 (Florida/Monroe/land grants/California squatters). validate 0, punct 0/0.
- part2 era 7 (1850-1900): done. 37 FIXED, 1 REJ, 0 NR, 4 found by fixer. PATCH Kake 1869 (KTOO). validate 0, punct 0/0.
- PART 2 DONE.
- part3 era 8 (1900-1950): done. 34 FIXED, 1 REJ, 0 NR, 5 found by fixer. PATCH Smith/Haiti legislature/Les Cayes. validate 0, punct 0/0.
- part3 era 9 (1950-2000): done. 25 FIXED, 4 REJ, 0 NR, 4 found by fixer. PATCH Castle Bravo (copied from war + health banks) and Blair House. validate 0, punct 0/0.
- part3 era 10 (2000-today): done. 18 FIXED, 3 REJ, 0 NR, 4 found by fixer. PATCH Iraq/Iran counts. validate 0, punct 0/0.
- PART 3 DONE.
- FINAL: python tools/project_state.py --check america-world --stage prose -> PASS (manuscript 16922w, validator 0 errors, emdash 0, semicolon 0).
