# CHECKPOINT T-303 | technology | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-303a landed (director verified: FAIL  technology / prose)
VERIFY: python tools/project_state.py --check technology --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/technology/part1-before-1800.md (eras 1-5) · manuscript/technology/part2-1800s.md (eras 6-7)
        · manuscript/technology/part3-1900s-and-today.md (eras 8-10) · research/research-technology.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-303a done (units 1-7 written, self-review run). Waiting for writer B.
NEXT:   T-303b: Unit 8 (era 08 1900-1950), creating manuscript/technology/part3-1900s-and-today.md. Copy the
        hb-chapter line from part2 with file="part3" (id="08" slug="technology" title="Technology" part="3"
        mode="prose"). Already told in part1/part2, do not repeat: Edison's life and death (1931), Latimer's
        life (died 1928), Tesla's 1888 motor and the Westinghouse license, Emma Nutt, Bell/Gray, the 1858
        "Invention of a Slave" ruling and its end. Write "Jeremiah Black" in full if he is mentioned (bare
        "Black" reads as a race word). Writer B runs the final prose check (unit 11).

## Research state before writing (2026-09-29)

PASS  technology / research
measured: stage=RESEARCHED eras=10/10 stories=23 (v23 c0 t0) verify_tags=0 bank=12851w outline=5360w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-303a | done | 717w, validator 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-303a | done | 188w, validator 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-303a | done | 1602w, validator 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-303a | done | 804w, validator 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-303a | done | 1545w, validator 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-303a | done | ~1250w, validator 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-303a | done | 2179w, validator 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-303b | todo | |
| 9 | era 09 1950-2000 -> part3 | T-303b | todo | |
| 10 | era 10 2000-today -> part3 | T-303b | todo | |
| 11 | final: self-review, --punct, validator, prose check | T-303b | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 04 | Franklin's own reason for no patent; how the stove worked | PATCH | "PATCH 2026-09-29 (T-303a): Franklin's own reason..."
- 04 | whose land was the Baltimore Iron Works (Patapsco) on | PATCH (Susquehannock and Piscataway, 1652 treaty; journalism + Contingent) | "PATCH 2026-09-29 (T-303a): whose land the Baltimore Iron Works stood on"
- 05 | how the lightning rod works | PATCH (Franklin's 1753 almanac text) | "PATCH 2026-09-29 (T-303a): how the lightning rod works"
- 05 | who Arkwright was | PATCH | "PATCH 2026-09-29 (T-303a): Richard Arkwright..."
- 05 | what "faced violence" meant for cotton pickers | PATCH (Northup 1853) | "PATCH 2026-09-29 (T-303a): what 'violence' meant..."
- 05 | who carried out the removals | PATCH (LOC: Jackson signed May 28, 1830; Cherokee 1838-39, ~4,000 dead; NPS Scott) | "PATCH 2026-09-29 (T-303a): who carried out the removals..."
- 06 | how the telegraph worked; who paid for the line | PATCH (LOC Morse Papers: $30,000, 1843, Tyler) | "PATCH 2026-09-29 (T-303a): how Morse's telegraph worked..."
- 06 | how a daguerreotype was made | PATCH, search summary only (not written as chemistry) | "PATCH 2026-09-29 (T-303a): how a daguerreotype was made"
- 06 | whose land at Grand Detour | PATCH (Ho-Chunk village, Jipson; 1832 Fort Armstrong treaty) | "PATCH 2026-09-29 (T-303a): whose land Deere's plow broke at Grand Detour"
- 06 | Morse as painter, life dates | PATCH, painter career and dates search-summary only (not written); 1832 ship idea confirmed (LOC) | "PATCH 2026-09-29 (T-303a): Morse's idea of 1832..."
- 07 | how the telephone and lamp work | PATCH (Bell 1876; DOE) | "PATCH 2026-09-29 (T-303a): how the telephone and the electric lamp work"

## OPEN (should be rare)
None for eras 1-7.

## Outline claims left out
1. Morse as "painter turned inventor" (era 6): bank had no source; Britannica/LOC pages returned 403, search summary only. Recorded as unconfirmed PATCH.
2. Jenks grant date "March 6, 1646" (era 3): search summary only; wrote the archive date May 10, 1646.
3. Three Sisters mechanics (corn as bean pole, squash as ground cover): not in bank; wrote only the interplanting.
4. Daguerreotype chemistry (era 6): search summary only; wrote the process name only.
5. Whitney losing gin profits in lawsuits; Principio's labor force; John Stewart becoming Springfield's blacksmith; Valliere starting at 14; Falling Creek's two women and three children dead: all tagged unconfirmed in the bank; left out.
6. Parked items not in the outline and not used: Kinetoscope/Black Maria (era 7), Swift/Chase refrigerator car (era 7).
7. Used one parked item not in the outline: the 1755 Schuyler mine steam engine (era 5, parked from energy).

## Decisions and defects fixed
- Land erasure (outline/bank silent): named the Susquehannock and Piscataway and the 1652 treaty for the Baltimore Iron Works (bank had "not supplied"); named the Ho-Chunk village at Grand Detour and the 1832 Fort Armstrong treaty for Deere's plow; named Native displacement by barbed wire (NARA) where the outline said only "fenced the open range".
- Hidden actors: outline/bank "Demand for cotton land drove the 1830s removal" and the museum's "the American government" replaced with President Andrew Jackson (signed May 28, 1830) and General Winfield Scott (1838), plus the 4,000 Cherokee dead (LOC).
- Semantic abstraction: the museum's "faced violence if they did not meet quotas" replaced with Solomon Northup's 1853 account (200-pound task, nightly weighing, 25/50/100 lashes, Epps himself whipping).
- Closing reversal in the bank ("the machine that was supposed to save labor instead multiplied the demand"): stated as plain fact.
- False "first": outline's "first PRACTICAL" electric light (era 7) and "first successful" mill are not in the sources; wrote "long-lasting lamp" (DOE hours) and "the start of the factory textile industry".
- Falling Creek: bank's original "destroyed before it shipped" contradicted by DHR; told as a disagreement between DHR and the county.
- Quotations with a semicolon or dashes split with no word changed: Jenks petition, Franklin autobiography, Northup, Bell's "Mr. Watson" sentence.
- Ambiguity: "Jeremiah Black" written in full each time.

## TO PARK (for the director, burst runs only)
- `food-farming` (era 6, Deere's plow): Ho-Chunk village at Grand Detour (Jipson) and the September 15, 1832 Treaty with the Winnebago at Fort Armstrong (Scott, Reynolds; $10,000 a year for 27 years). Full text: research-technology.md, "PATCH 2026-09-29 (T-303a): whose land Deere's plow broke at Grand Detour".
- `slavery-freedom` (eras 5-6): Solomon Northup's cotton-picking passages with exact quotes and lash counts. research-technology.md, "PATCH 2026-09-29 (T-303a): what 'violence' meant...".
- `land-environment` / `native-nations` (era 7): NARA barbed-wire lesson quotes ("the Devil's rope", range wars). research-technology.md, "PATCH 2026-09-29 (T-303a): Joseph Glidden and what barbed wire did".
- `news-communication` (era 6): LOC Morse Papers telegraph mechanism, $30,000 appropriation, Cornell's poles, Gale's relay. research-technology.md, "PATCH 2026-09-29 (T-303a): how Morse's telegraph worked...".
- `slavery-freedom` / `work-workers` (era 4): Patapsco land (Susquehannock, Piscataway, 1652 treaty) under the Baltimore Iron Works.

## Log
- 2026-09-29 T-303a unit 1 era 01: 717 words, avg 13.8 words/sentence; validator 0 errors; --punct emdash=0 semicolon=0. Story: wayne-valliere.
- 2026-09-29 T-303a unit 2 era 02 (thin): 188 words; validator 0 errors; --punct emdash=0 semicolon=0. No story (outline has none).
- 2026-09-29 T-303a unit 3 era 03: 1602 words, avg 13.3; validator 0 errors; --punct emdash=0 semicolon=0 (Jenks quote split at its semicolon, no word changed). Story: joseph-jenks.
- 2026-09-29 T-303a unit 4 era 04: 804 words, avg 14.4; validator 0 errors; --punct emdash=0 semicolon=0 (Franklin quote split at its semicolon). Story: benjamin-franklin-technology.
- 2026-09-29 T-303a unit 5 era 05: 1545 words, avg 13.2; validator 0 errors; --punct emdash=0 semicolon=0 (Northup quote split at its semicolon). Stories: eli-whitney, samuel-slater. Added a short span on the 1755 Schuyler mine steam engine from the parked energy note. part1 complete (5 eras, 5 stories).
- 2026-09-29 T-303a unit 6 era 06: part2 created. ~1250 words, avg 13.4; validator 0 errors; --punct emdash=0 semicolon=0. Stories: samuel-morse, mccormick-deere.
- 2026-09-29 T-303a unit 7 era 07: 2179 words, avg 13.8; validator 0 errors; --punct emdash=0 semicolon=0 (Bell's "Mr. Watson" sentence split at its dashes). Stories: alexander-graham-bell, emma-nutt, thomas-edison-technology, lewis-latimer, granville-t-woods, nikola-tesla-technology.
- 2026-09-29 T-303a self-review (Version 2 "Self-Review Before Reporting" + amendment §5) run on part1 and part2: fixed institution-as-actor (courts, Patent Office, museum/LOC "names"), story openings that all began "Name + verb" (varied Franklin, Whitney, Slater, Bell, Nutt, Latimer, Tesla), era openings that all began with a date, a dangling "his" (Goodyear), an inverted-order sentence, unsourced glosses removed. Both files: validator 0 errors, emdash=0 semicolon=0.
