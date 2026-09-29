# CHECKPOINT T-305 | transportation | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-305a landed (director verified: FAIL  transportation / prose)
VERIFY: python tools/project_state.py --check transportation --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/transportation/part1-before-1800.md (eras 1-5) · manuscript/transportation/part2-1800s.md (eras 6-7)
        · manuscript/transportation/part3-1900s-and-today.md (eras 8-10) · research/research-transportation.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-305a finished units 1-7 (part1 and part2 written, self-review run, both files validator-clean and punct-clean).
NEXT:   T-305b: Unit 8. Create manuscript/transportation/part3-1900s-and-today.md (eras 8-10) with the same header
        layout as part2 (hb-chapter line with file="part3", hb-note naming eras 08-10). Voice notes from writer A:
        era zooms open on different shapes (avoid "Between X and Y, ..."), define every hard word in the next sentence,
        people as actors ("members of Congress passed", "Central Pacific managers hired"). Porters were deferred to
        era 8 by the outline ("The porters' story is told next era"): part2 mentions Pullman's Pioneer (1865) and the
        Pullman Palace Car Company (1867) only, so era 8 can introduce the porters without repeating the car.
        Part2 already tells Ida B. Wells (1884) and Plessy (1892/1896) on the railroads.

## Research state before writing (2026-09-29)

PASS  transportation / research
measured: stage=RESEARCHED eras=10/10 stories=19 (v19 c0 t0) verify_tags=0 bank=13064w outline=6684w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-305a | done | 493w, validator 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-305a | done | 417w, validator 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-305a | done | 566w, validator 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-305a | done | 828w, validator 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-305a | done | 494w, validator 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-305a | done | 2422w, validator 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-305a | done | 2241w, validator 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-305b | todo | |
| 9 | era 09 1950-2000 -> part3 | T-305b | todo | |
| 10 | era 10 2000-today -> part3 | T-305b | todo | |
| 11 | final: self-review, --punct, validator, prose check | T-305b | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- era 2 | whose land Oñate's wagons entered, and is "first wheels" true | PATCH (cross-sourced from migration bank; "first" dropped) | PATCH 2026-09-29 (T-305a): Oñate's wagons...
- era 4 | did Virginia "tithables" include enslaved men | PATCH (Virginia Places, opened) | PATCH 2026-09-29 (T-305a): who counted as a "tithable"...
- era 6 | whose path the National Road followed | PATCH (Columbia Encyclopedia via encyclopedia.com, opened) | PATCH 2026-09-29 (T-305a): the National Road ran on a Native path
- era 6 | Moses Grandy after freedom (outline close contradicted the sold wife) | PATCH (Narrative full text, DocSouth) | PATCH 2026-09-29 (T-305a): Moses Grandy after freedom
- era 7 | 1867 strike demands and how it ended | PATCH (PBS, opened) | PATCH 2026-09-29 (T-305a): the 1867 strike...
- era 7 | which "last rails" Ging Cui, Wong Fook, Lee Shao carried | PATCH (SFSU APIA Biography Project, opened) | PATCH 2026-09-29 (T-305a): which "last rails"...
Totals: 6 found, 0 SEARCHED, NOT FOUND (existing T-248 records used for road-crew counts and turnpike workers).

## OPEN (should be rare)
None.

## Outline claims left out
1. Era 6: covered wagons and ox teams as machines (no facts in this bank, only a pointer to migration's).
2. Era 7: "about 9 in 10" of Central Pacific workers were Chinese (not in the bank).
3. Era 7: Ten-Mile Day "still the record for hand-laid track" (not in the bank).
4. Era 7: Sprague "horsecars began disappearing within a decade" replaced by the dated street-railway figures from the bank.
5. Era 2: Oñate's wagons as "the first documented wheeled vehicles" (false-first risk).
6. Era 3: John Winthrop the Younger on the Old Connecticut Path, 1645 (unconfirmed).
7. Era 5: Lancaster Turnpike cost $465,000 and 2-inch stone ring (unconfirmed).
8. Era 7: Hung Wah's PBS "topic documentary" note (not about him).
9. Era 7: Julesburg retaliation's Turkey Leg as Plum Creek leader (unconfirmed).

## Decisions and defects fixed
- Outline defect, era 6 Grandy: "saved enough to buy his wife and children" read as if the sold first wife was bought back. Prose states he married again and bought his second wife, his son ($450), and his daughters paid $1,200 each.
- Bank/outline defect, era 7: Ging Cui, Wong Fook, Lee Shao were placed on Ten-Mile Day; they laid the last track at Promontory, May 10, 1869.
- Outline defect, era 7: Ida B. Wells "dragged" (not in bank). Prose: the crew forced her off the train.
- Outline defect, era 7: 1867 strike "ended without formal concessions" kept, and the bank's LOC note that experienced men's pay later rose a little is stated; PBS ending (fines, lost June pay, armed posse) added.
- Outline defect, era 2: false "first wheeled vehicles" claim dropped.
- Outline defect, era 6: "Clinton's numbers answered the mockery" closing reversal removed; Clinton story ends on the Six Nations population fact.
- Personification repaired throughout: "the railroads split the continent into time zones" became railroad managers; Safety Appliance Act "forced" became members of Congress passed; companies hiring/buying became managers.
- Era 4 Paxton killings (1763) told in the 1700-1750 Conestoga span, signaled with its date, because the wagon's name is there.

## TO PARK (FILED by the director, 2026-09-27)
- `migration` / `native-nations`: none new.
- Bank hygiene for the audit: research-transportation.md line under "## 7" Ten-Mile Day still says the three men carried "the last rails" that day; the T-305a PATCH corrects it.

## Log
- 2026-09-29 T-305a: before writing, added bank PATCHes: era 2 Oñate wagons/Pueblo land/"first wheels" check; era 4 Virginia tithables (confirms free and enslaved); era 6 Nemacolin's Path under the National Road, Moses Grandy after freedom; era 7 1867 strike demands and ending (PBS), Ging Cui/Wong Fook/Lee Shao at Promontory (not Ten-Mile Day).
- 2026-09-29 T-305a unit 1 era 01: 493 words, avg sentence 13.2, validator 0 errors, emdash=0 semicolon=0. No gaps.
- 2026-09-29 T-305a unit 2 era 02: 413 words, validator 0 errors, emdash=0 semicolon=0. PATCH: Oñate wagons, La Toma, Pueblo land (cross-sourced from migration bank). "First wheels" dropped.
- 2026-09-29 T-305a unit 3 era 03: 566 words, 1 story (edward-converse), validator 0 errors, emdash=0 semicolon=0. No new gaps. Old Connecticut Path/Winthrop 1645 line left out (unconfirmed in bank).
- 2026-09-29 T-305a unit 4 era 04: ~820 words, 1 story (sarah-kemble-knight-transportation), validator 0 errors, emdash=0 semicolon=0. PATCH: Virginia tithables (free and enslaved men). Paxton killings told in the Conestoga span (dated 1763, one paragraph pair). Susquehannock descent and treaty signers left out (unconfirmed).
- 2026-09-29 T-305a unit 5 era 05: ~505 words, 1 story (john-fitch), validator 0 errors, emdash=0 semicolon=0. Turnpike workforce written from the T-248 SEARCHED, NOT FOUND line. $465,000 cost and 2-inch stone ring left out (unconfirmed). Part 1 complete.
- 2026-09-29 T-305a unit 6 era 06: ~2410 words, 4 stories (robert-fulton, dewitt-clinton-transportation, james-garfield-transportation, moses-grandy), validator 0 errors, emdash=0 semicolon=0. PATCHes: Nemacolin's Path under the National Road; Grandy after freedom (second wife). Covered wagons/ox teams line left out (no facts in this bank).
- 2026-09-29 T-305a unit 7 era 07: 2241 words, 4 stories (hung-wah, cornelius-vanderbilt-transportation, mark-twain-transportation, frank-sprague), validator 0 errors, emdash=0 semicolon=0. PATCHes: 1867 strike (PBS); Promontory last-track names.
- 2026-09-29 T-305a self-review (Version 2 + amendment §5) run on both files: fixed institutions-as-actors, added-fact glosses not in bank (Roger Williams "minister", Sand Creek "Colorado Territory", clock-by-sun line, flatboat description, "record" claim), split long sentences and paragraphs, varied era openings. Final: part1 2798w, part2 4663w, both validator 0 errors, emdash=0 semicolon=0.
