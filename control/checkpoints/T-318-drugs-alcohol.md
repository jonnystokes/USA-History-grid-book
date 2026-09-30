# CHECKPOINT T-318 | drugs-alcohol | prose | ONE writer, all 10 eras (part1, part2, part3)

STATUS: T-318 landed (director verified: PASS  drugs-alcohol / prose)
VERIFY: python tools/project_state.py --check drugs-alcohol --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/drugs-alcohol/part1-before-1800.md (eras 1-5) · manuscript/drugs-alcohol/part2-1800s.md (eras 6-7)
        · manuscript/drugs-alcohol/part3-1900s-and-today.md (eras 8-10) · research/research-drugs-alcohol.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-318 finished all 11 units.
NEXT:   none (director: commit).

## Research state before writing (2026-09-29)

PASS  drugs-alcohol / research
measured: stage=RESEARCHED eras=10/10 stories=14 (v14 c0 t0) verify_tags=0 bank=30093w outline=14971w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-318 | done | 860w, 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-318 | done | 644w, 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-318 | done | 1640w, 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-318 | done | 1272w, 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-318 | done | 2087w, 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-318 | done | 1582w, 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-318 | done | 2545w, 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-318 | done | 3318w, 0 errors, emdash=0 semicolon=0 |
| 9 | era 09 1950-2000 -> part3 | T-318 | done | 2640w, 0 errors, emdash=0 semicolon=0 |
| 10 | era 10 2000-today -> part3 | T-318 | done | 2277w, 0 errors, emdash=0 semicolon=0 |
| 11 | final: self-review, --punct, validator, prose check | T-318 | done | PASS drugs-alcohol / prose, 18970w, 0 errors x3, emdash=0 semicolon=0 x3 |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 07 | what opiate withdrawal does to the body | PATCH | "PATCH 2026-09-30 (T-318): what opiate withdrawal does to the body"
- 08 | when and by whom heroin was banned | PATCH (Anti-Heroin Act, 7 June 1924) | "PATCH 2026-09-30 (T-318): the 1924 law against heroin"
- 09 | Billie Holiday arrests (parked from music) | PATCH (copied from research-music.md) | "PATCH 2026-09-30 (T-318): Billie Holiday and the federal narcotics agents"
- 10 | distributor company names (search summary only before) | PATCH (confirmed) | "PATCH 2026-09-30 (T-318): the distributors' names, confirmed"

## OPEN (should be rare)
- none

## Outline claims left out
- 02: none. 06: Gough "shaking hand" and "Newburyport" (not in bank). 08: Carry Nation "after that she used a hatchet" (bank has only the joke and hatchet pins); "five justices" in Webb (bank gives no count). 01: datura painting "read as its flower" (not in bank). 10: Mehmet Oz quote (kept out, off-angle).

## Decisions and defects fixed
- Outline era 03 boundary slip (29 million lb in 1709) written in era 04 only, as the bank directs.
- Outline era 08 "Economists who measured deaths and arrests" not in bank: written as "a 1991 study by the economists Miron and Zwiebel".
- Outline era 08 WW1 "anti-German" line: breweries gloss not in bank, not written.
- Pure-alcohol comparison to 2023 moved from era 05 to era 06 so units match (bank warns against comparing 1790 drink gallons with 2023 pure alcohol).
- Self-review: institution subjects repaired (court, law, ban, navy, campaign, government); one altered quotation restored (Goolrick's brother); unsupported "first" claims removed from my own drafts.

## TO PARK (for the director, burst runs only)

## Log
- era 01: 860 words, validator 0 errors, emdash=0 semicolon=0. No new research.
- era 02: 644 words, validator 0 errors, emdash=0 semicolon=0. No new research. Dropped an unsupported 'first description in English' from my own draft.
- era 03: 1640 words, validator 0 errors, emdash=0 semicolon=0. No new research. Outline boundary slip (29 million pounds in 1709 in era 03) left to era 04 as the bank directs.
- era 04: 1272 words, validator 0 errors, emdash=0 semicolon=0. No new research. Georgia 'first prohibition' marker claim not used.
- era 05: 2087 words, validator 0 errors, emdash=0 semicolon=0. No new research. Kept both Bower Hill crowd figures (400, 600) and both pardon dates. Part 1 self-review run: fixed repeated Hariot line, a closing turn on clean water, two institution subjects (the ban, the navy). Avg sentence 13.9 words.
- era 06: 1582 words, validator 0 errors, emdash=0 semicolon=0. No new research. Outline's 'shaking hand' and 'Newburyport' for Gough not in bank: left out.
- era 07: 2545 words, validator 0 errors, emdash=0 semicolon=0. PATCH 2026-09-30 (T-318): opiate withdrawal symptoms (MedlinePlus), used to define withdrawal. Part 2 self-review run: fixed document-verb subjects, Lee's 'army surrendered', a changed quotation (Goolrick's brother), 'first laws' claim in era summary.
- era 08 prep: slice eras 8-10 read. PATCH 2026-09-30 (T-318): Anti-Heroin Act of 1924 (Wikipedia, opened), answers part of T-266b's heroin SEARCHED, NOT FOUND.
- era 08: 3318 words, validator 0 errors, emdash=0 semicolon=0. Used PATCH (T-318) on the 1924 heroin law. Signer of the 1926 poison order and agents killed: existing SEARCHED, NOT FOUND, written as 'the records do not name'. Outline's 'after that she used a hatchet' (Carry Nation) and 'five justices' (Webb) not in bank: left out. Billie Holiday parked item placed in era 09.
- era 09: about 2640 words, validator 0 errors, emdash=0 semicolon=0. PATCH 2026-09-30 (T-318): Billie Holiday arrests 1947 to 1959, copied into this bank from research-music.md (already opened there). No new searches.
- era 10: 2277 words, validator 0 errors, emdash=0 semicolon=0. PATCH 2026-09-30 (T-318): distributor names confirmed (National Opioid Settlement). Every figure carries year and source.
