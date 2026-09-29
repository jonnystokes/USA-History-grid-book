# CHECKPOINT T-301 | landmarks | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-301a landed (director verified: FAIL  landmarks / prose)
VERIFY: python tools/project_state.py --check landmarks --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/landmarks/part1-before-1800.md (eras 1-5) · manuscript/landmarks/part2-1800s.md (eras 6-7)
        · manuscript/landmarks/part3-1900s-and-today.md (eras 8-10) · research/research-landmarks.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-301a finished units 1-7 (part1 + part2 written, self-review run, both files validator 0 errors, --punct 0/0).
NEXT:   T-301b: Unit 8 (era 08 1900-1950 -> create manuscript/landmarks/part3-1900s-and-today.md). Copy part2's hb-chapter line with file="part3". Already told in part2 era 07, do not repeat: Sugarloaf Mound (1928 house, Osage purchase 2009, house razed 2017, rest returned 2025) and the 1904 World's Fair mound destruction. Era 10 may carry Andrea Hunter's 2025 quote and the Osage plans only. The Capitol slave-labor marker (2012, Emancipation Hall) is era 10's: part1 era 05 tells the Capitol payrolls, owners and Allen's 2005 report, so era 10 need not re-explain them.

## Research state before writing (2026-09-29)

PASS  landmarks / research
measured: stage=RESEARCHED eras=10/10 stories=17 (v17 c0 t0) verify_tags=0 bank=12406w outline=5726w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-301a | done | file 1379w, 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-301a | done | file 1554w, 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-301a | done | file 3108w, 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-301a | done | file 3782w, 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-301a | done | file 4922w, 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-301a | done | file 637w, 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-301a | done | file 2459w, 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-301b | todo | |
| 9 | era 09 1950-2000 -> part3 | T-301b | todo | |
| 10 | era 10 2000-today -> part3 | T-301b | todo | |
| 11 | final: self-review, --punct, validator, prose check | T-301b | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
| 1 | who made the 1831 Lewistown treaty; 800-mile walk | PATCH (Gardiner, OSU treaty text; OHC) | 01, PATCH 2026-09-29 (T-301a): who made the 1831 treaty |
| 1 | who led the 1832 march west; count of dead | SEARCHED, NOT FOUND | 01, SEARCHED, NOT FOUND 2026-09-29 (T-301a) |
| 3 | who burned St. Augustine in 1702; how many sheltered | PATCH (NPS Siege of 1702) | 03, PATCH 2026-09-29 (T-301a): who burned St. Augustine |
| 3 | Pueblo Revolt definition; what happened to San Miguel | PATCH (NPS San Geronimo de Taos, NPS and HSFF San Miguel) | 03, PATCH 2026-09-29 (T-301a): the Pueblo Revolt |
| 5 | whose land the federal city was built on | PATCH (NPS The Indigenous Capital) | filed under 03, PATCH 2026-09-29 (T-301a): whose land the federal city |
| 6 | what Bunker Hill Monument marks; quarry, stops, cost | PATCH (NPS Building the Bunker Hill Monument) | 06, PATCH 2026-09-29 (T-301a): Bunker Hill |
| 7 | who owned Philip Reid and took his pay | PATCH (Architect of the Capitol) | 07, PATCH 2026-09-29 (T-301a): who owned Philip Reid |

## OPEN (should be rare)

## Outline claims left out

- 01: Monks Mound "shared with" pointers and the Cahokia nation (other chapters); Mesa Verde "consulted on research" (search summary only).
- 03: "Tlaxcalan workers from Mexico" built San Miguel (bank cites NPS and HSFF, neither page says it: left out, see defects). Palace of the Governors (city-building). Parked art item San Esteban at Acoma (disputed, Wikipedia-only).
- 04: George Worthylake "returning from a sermon", "within sight of the lighthouse", "the light stayed lit anyway" (not in bank).
- 05: Monticello "half-built for most of his life" (bank says drop). "Most visited houses" (unsourced). L'Enfant plan (city-building).
- 06: Hemmings "the house tourists admire is his craftsmanship" (evaluative, unsourced). Lafayette and Webster at the Bunker Hill cornerstone (sourced but left out to avoid undefined names for the reader).
- 07: Brooklyn Bridge "longest suspension bridge in the world then" (not in bank). Capitol dome "iron" and "rose through the Civil War" (not in bank). Reid "stayed in Washington as a plasterer" (not in bank). Bartholdi "lived to see the statue lit" (bank says drop). Emma Lazarus plaque 1903 (immigration, and outside era). Chicago steel-frame buildings and Yellowstone pointers (other chapters' subjects, and a pointer would name another chapter). Caisson disease "more than 100 sickened" and "severe joint pain" (search summary only).

## Decisions and defects fixed

- Outline/bank defect: bank era-03 line cites NPS and Historic Santa Fe Foundation for "built c. 1610-1626 by Tlaxcalan workers" and "burned in the 1680 Pueblo Revolt". Both pages, fetched 2026-09-29, say "partly destroyed" and neither names the Tlaxcalans. Prose says "built around 1620 ... in use before 1626", "partly destroyed", and leaves the Tlaxcalans out. Correction note added in the bank PATCH.
- Outline personification in span labels fixed: "The fort that swallowed cannonballs" became "A fort built of shell stone"; "Mounds leveled for fill" kept as "Mounds dug away for fill".
- Outline "Congress took the stub over", "France gave the statue; America had to build the pedestal", "Jefferson's will freed him", "the revolt drove the Spanish out", "the Crown recognized" (institutions acting): rewritten with people as actors.
- Outline Wallace story tied removal to the Indian Removal Act and named no US actor: prose names treaty commissioner James B. Gardiner (PATCH) and states the march leaders are not named.
- Outline "Philip Reid's owner took the other six days" left the owner unnamed: prose names Clark Mills (PATCH).
- Outline "the town burned" (1702) had no actor: prose names Daniel's troops and Native allies (PATCH).
- Outline "at least 20" Brooklyn Bridge deaths replaced by the bank's 21 / 27 / up to 40 with whose count each is, and the named dead.
- Outline "a cycle of 18.6 years" kept; outline "circles, squares and octagons" reduced to what the bank supports (circle and eight-sided figures).
- Fourth wall: outline "this chapter says it plainly" and "(that night's events belong to war)" style pointers removed from prose.

## TO PARK (for the director, burst runs only)

- native-nations / migration: the 1831 Treaty of Lewistown was made by US commissioner James B. Gardiner (OSU Tribal Treaties Database); the 1832 march leaders were not found (research-landmarks.md, era 01 T-301a PATCH and SEARCHED, NOT FOUND).
- religion / native-nations: NPS San Geronimo de Taos page confirms Popé planned the 1680 Pueblo Revolt from Taos and the Spanish were out until 1692 (research-landmarks.md, era 03 T-301a PATCH).
- slavery-freedom: Architect of the Capitol page names Clark Mills as Philip Reid's owner, bought in Charleston for $1,200 (research-landmarks.md, era 07 T-301a PATCH).

## Log
- 2026-09-29 T-301a unit 1 era 01: part1 created, 1379 words in file, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-29 T-301a unit 2 era 02 1500s: manuscript/landmarks/part1-before-1800.md now 1554 words, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-29 T-301a unit 3 era 03 1600s: manuscript/landmarks/part1-before-1800.md now 3108 words, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-29 T-301a unit 4 era 04 1700-1750: manuscript/landmarks/part1-before-1800.md now 3782 words, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-29 T-301a unit 5 era 05 1750-1800: manuscript/landmarks/part1-before-1800.md now 4922 words, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-29 T-301a unit 6 era 06 1800-1850: manuscript/landmarks/part2-1800s.md now 637 words, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-29 T-301a unit 7 era 07 1850-1900: manuscript/landmarks/part2-1800s.md now 2459 words, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-29 T-301a: self-review (Version 2 "Self-Review Before Reporting" plus amendment §5) run on part1 and part2. Repairs: pronoun ambiguity (Reid), institution-as-actor (fair raised, society spent, uprising drove), unsourced glosses removed, era openings varied, over-long sentences split. Final: part1 0 errors, emdash=0 semicolon=0. part2 0 errors, emdash=0 semicolon=0.
