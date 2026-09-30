# CHECKPOINT T-317 | holidays | prose | ONE writer, all 10 eras (part1, part2, part3)

STATUS: T-317 landed (director verified: PASS  holidays / prose)
VERIFY: python tools/project_state.py --check holidays --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/holidays/part1-before-1800.md (eras 1-5) · manuscript/holidays/part2-1800s.md (eras 6-7)
        · manuscript/holidays/part3-1900s-and-today.md (eras 8-10) · research/research-holidays.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-317 finished. All 11 units done.
NEXT:   none (director: commit).

## Research state before writing (2026-09-29)

PASS  holidays / research
measured: stage=RESEARCHED eras=10/10 stories=9 (v9 c0 t0) verify_tags=0 bank=26062w outline=14586w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-317 | done | ~1000w, 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-317 | done | ~560w, 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-317 | done | ~1450w, 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-317 | done | ~800w, 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-317 | done | ~1800w, 0 errors, emdash=0 semicolon=0. part1 self-review run: 5632w, avg sentence 14.8 |
| 6 | era 06 1800-1850 -> part2 | T-317 | done | ~1650w, 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-317 | done | ~2650w, 0 errors, emdash=0 semicolon=0. part2 self-review run: 4317w, avg sentence 14.0 |
| 8 | era 08 1900-1950 -> part3 | T-317 | done | ~1650w, 0 errors, emdash=0 semicolon=0 |
| 9 | era 09 1950-2000 -> part3 | T-317 | done | ~2900w, 0 errors, emdash=0 semicolon=0 |
| 10 | era 10 2000-today -> part3 | T-317 | done | ~1500w, 0 errors, emdash=0 semicolon=0 |
| 11 | final: self-review, --punct, validator, prose check | T-317 | done | PASS holidays / prose, 14872w, 9 stories verified, 0/0 punct, 0 validator errors |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 2 | Ponce de León, Pascua Florida | PATCH | "PATCH 2026-09-30 (T-317): Ponce de León and the name Florida"
- 3 | who lived on the Berkeley Hundred land | PATCH (county page names three nations) | "PATCH 2026-09-30 (T-317): the people of the Berkeley Hundred land"
- 3 | Newell's claim, confirmed via Bangs | PATCH | "PATCH 2026-09-30 (T-317): Newell's claim as reported by Bangs"
- 10 | officer who killed George Floyd | PATCH (from crime-justice and rights-movements banks: Chauvin plea) | "PATCH 2026-09-30 (T-317): the officer who killed George Floyd"
- 7 | how the Charleston race course prisoners died | PATCH (NEH: at least 257, exposure and disease, open-air prison) | "PATCH 2026-09-30 (T-317): how the Charleston race course prisoners died"
- 5 | Washington's birth date, calendar change | PATCH | "PATCH 2026-09-30 (T-317): Washington's birth date"

## OPEN (should be rare)

## Outline claims left out
- era 8: none beyond the bank's own left-outs
- era 9: Al Edwards described as 'Black' (bank has only Democrat from Houston)
- era 10: Pride Month 2025 'no plans' (search summary only); Opal Lee's granddaughter and great-granddaughter by relation (bank: 'her family'); Pew's 33-state Juneteenth count (search summary only); Cabrini gloss
- era 6: Pinkster ordinance wording (search summary only); Hale's letters to four presidents who said no
- era 7: Nast's later Santa drawings; Morgan quotation and 'Franchise Day' name
- era 1: busk from Creek puskita (search summary only)
- era 3: Winthrop journal line on the 1637 thanksgiving; Kecoughtan = Hampton; Weyanock as sole owners of Berkeley (county page names three nations instead); Opechancanough as leader of 1622 attack
- era 4: Pope's Night gang fights from the 1740s; Massachusetts Black elections from 1741
- era 5: Wight's 43 years and ~40 speeches; Proctor's band at Valley Forge; drafters of the 1777 proclamation

## Decisions and defects fixed
- era 9: Day of Mourning span and Frank James story overlapped in the outline; speech detail kept in the story only.
- era 10: George Floyd's killer named (Chauvin) instead of an unnamed officer.
- era 10: Senate 15 June unanimous-consent date is search summary only; prose says 'In June 2021'.
- Era opening sentences checked across all ten eras for shared shape; era 6 and era 7 openings rewritten.
- era 7: Morgan's Franchise Day written from the SEARCHED, NOT FOUND fallback, without the quotation or the name 'Franchise Day'.
- era 7: Charleston prisoners: bank said only 'mistreatment' (vague); researched and stated exposure and disease in an open-air prison.
- era 6: Adams and Jefferson as 'signers' left out (not in bank).
- era 3: Newell's claim quoted as reported by Bangs (HNN), attributed; outline's 'former head of anthropology' dropped because Bangs disputes it.
- era 2: Matanzas counts attributed to the NPS, with Menendez's own different count noted.
- era 5: Hartford accounts disagree (Menapace vs Piascik): both stated.
- Institutions as actors (General Court, Congress) recast as 'the members of'.

## TO PARK (for the director, burst runs only)

## Log
- 2026-09-30 units 1-5 landed in part1; validator 0 errors, punct 0/0.
- 2026-09-30 units 6-7 landed in part2; validator 0 errors, punct 0/0.
- 2026-09-30 units 8-10 landed in part3; self-review run on all three files; prose check PASS (14872w).
