# CHECKPOINT T-306 | food-farming | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-306a landed (director verified: FAIL  food-farming / prose)
VERIFY: python tools/project_state.py --check food-farming --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/food-farming/part1-before-1800.md (eras 1-5) · manuscript/food-farming/part2-1800s.md (eras 6-7)
        · manuscript/food-farming/part3-1900s-and-today.md (eras 8-10) · research/research-food-farming.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-306a done (units 1-7). part1 4680w, part2 2638w. Self-review run on both files, repairs applied.
NEXT:   T-306b: Unit 8. Create manuscript/food-farming/part3-1900s-and-today.md (file="part3", eras 08-10), copying the hb-chapter/hb-note layout of part2. Already told in part2, do not repeat: Homestead figures and Dawes acreage, bison collapse, Swift cars, the Grange, the Hatch Act stations (1887), sharecropping terms. Carver origin (born enslaved c. 1864) goes inside his 1900-1950 story. Last writer runs --check food-farming --stage prose.

## Research state before writing (2026-09-29)

PASS  food-farming / research
measured: stage=RESEARCHED eras=10/10 stories=17 (v17 c0 t0) verify_tags=0 bank=13721w outline=6104w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-306a | done | ~640w, validator 0 errors, punct 0/0 |
| 2 | era 02 1500s -> part1 | T-306a | done | ~560w, validator 0 errors, punct 0/0 |
| 3 | era 03 1600s -> part1 | T-306a | done | ~1250w, validator 0 errors, punct 0/0 |
| 4 | era 04 1700-1750 -> part1 | T-306a | done | ~1240w, validator 0 errors, punct 0/0 |
| 5 | era 05 1750-1800 -> part1 | T-306a | done | ~1000w, validator 0 errors, punct 0/0 |
| 6 | era 06 1800-1850 -> part2 | T-306a | done | ~1000w, validator 0 errors, punct 0/0 |
| 7 | era 07 1850-1900 -> part2 | T-306a | done | ~1640w, validator 0 errors, punct 0/0 |
| 8 | era 08 1900-1950 -> part3 | T-306b | todo | |
| 9 | era 09 1950-2000 -> part3 | T-306b | todo | |
| 10 | era 10 2000-today -> part3 | T-306b | todo | |
| 11 | final: self-review, --punct, validator, prose check | T-306b | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 02 | did de Soto's army take villagers' corn and seize people as carriers? | PATCH (found, WHE + Wikipedia Apalachee) | PATCH 2026-09-29 (T-306a): de Soto's seizures confirmed
- 03 | Percy's 1610 raid and the killing of the Paspahegh children (was search-summary only) | PATCH (found, Encyclopedia Virginia) | PATCH 2026-09-29 (T-306a): Percy's 1610 raid
- 04 | Eliza Lucas's enslaved workers, indigo makers (was search-summary only) | PATCH (found, Wikipedia; names Quash/Togo/Sawney still unconfirmed, not written) | PATCH 2026-09-29 (T-306a): Eliza Lucas's plantations
- 05 | Monticello enslaved families' gardens and sales (was search-summary only) | PATCH (found in part, LOC exhibit; Grangers/Sundays not confirmed, not written) | PATCH 2026-09-29 (T-306a): enslaved families' gardens
- 06 | Potawatomi sale of northern Illinois before Deere's plow (was search-summary only) | PATCH (found, Milwaukee Public Museum) | PATCH 2026-09-29 (T-306a): the 1833 Potawatomi sale
- 07 | Oblinger letters: food details, who wrote "poor here together" | PATCH (found, LOC + Hanover College; correction: Uriah wrote it) | PATCH 2026-09-29 (T-306a): the Oblinger letters

## OPEN (should be rare)
- none

## Outline claims left out
- 04: New England mixed farms and Chesapeake tobacco as regions (era line), not in the bank.
- 04: names Quash, Togo, Sawney in Pinckney's indigo work (search summary only).
- 05: Grangers selling on Sundays, "evenings and Sundays" (search summary only); Jefferson's nailery boys (not food).
- 06: Tudor's sawdust packing and ice houses, and "refrigerated cars are Tudor's idea on wheels" (not in bank / interpretive).
- 06: Ho-Chunk village at Grand Detour and the 1800 Rock River nations list (search summary only). Wrote the confirmed 1832 war and 1833 Potawatomi sale instead.
- 07: causes of homestead failure ("drought, grasshoppers, loneliness, debt"), not in bank.
- 07: "about 3,000 pages" of Oblinger letters, not on the LOC page; wrote "318 letters".
- 07: "one of the best-documented ordinary farm lives" (evaluative, unsourced).

## Decisions and defects fixed
- Outline 07 gives "we will all be poor here together" to Mattie Oblinger. LOC: Uriah wrote it, Dec 1, 1872. Prose gives it to Uriah (PATCH in bank).
- Outline 04 has one Caribbean indigo maker. Bank/Wikipedia: first a Montserrat maker, then a maker of African descent from the French West Indies. Prose states both.
- Personification in outline repaired in prose: "Virginia planted a crop", "the government gave farms away", "Chicago turned animals into boxed meat", "the colony's own assembly had to force", "rice made planters rich", "Allotment cut".
- Outline 02 cadence ("not just cargo") and 03 era line reversal not copied.
- Outline 01 "cannot reseed itself" kept, without an invented mechanism.
- Percy raid death count stated as a range (more than a dozen per Percy, up to 75 in other accounts), no silent resolution.

## TO PARK (for the director, burst runs only)
- migration / home-family: if either chapter quotes "we will all be poor here together" as Mattie Oblinger's, LOC gives it to Uriah (letter of Dec 1, 1872). Collection is 318 letters, 1862-1911. See research-food-farming.md PATCH 2026-09-29 (T-306a): the Oblinger letters.

## Log
- 2026-09-29 T-306a: research pass before writing. PATCHes added to bank (eras 02, 03, 04, 05, 06, 07), see Gaps researched.
- 2026-09-29 T-306a unit 1: era 01 written (5 blocks, no story, as outline). validator 0 errors, punct emdash=0 semicolon=0.
- 2026-09-29 T-306a unit 2: era 02 written (era + 2 spans). validator 0 errors, punct 0/0.
- 2026-09-29 T-306a unit 3: era 03 written (era + 4 spans + story squanto-food-farming). part1 total 2450w. validator 0 errors, punct 0/0.
- 2026-09-29 T-306a unit 4: era 04 written (era + 4 spans + story eliza-lucas-pinckney). validator 0 errors, punct 0/0.
- 2026-09-29 T-306a unit 5: era 05 written (era + 2 spans + stories matthew-patten, amelia-simmons). part1 total 4690w. validator 0 errors (4 stories), punct 0/0.
- 2026-09-29 T-306a unit 6: part2 created; era 06 written (era + 4 spans + story frederic-tudor). validator 0 errors, punct 0/0.
- 2026-09-29 T-306a unit 7: era 07 written (era + 5 spans + stories oblinger-family, charles-goodnight). part2 total 2638w. validator 0 errors (3 stories), punct 0/0.
- 2026-09-29 T-306a: self-review (Version 2 + amendment 5 + hard-subjects 7) run on part1 and part2; repairs applied (personified colonies/laws, passives, anaphora, era-opening shapes, one run-on). Final: both files validator 0 errors, punct 0/0.
