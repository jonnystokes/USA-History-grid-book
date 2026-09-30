# CHECKPOINT T-305 | transportation | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-305b landed (director verified: PASS  transportation / prose)
VERIFY: python tools/project_state.py --check transportation --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/transportation/part1-before-1800.md (eras 1-5) · manuscript/transportation/part2-1800s.md (eras 6-7)
        · manuscript/transportation/part3-1900s-and-today.md (eras 8-10) · research/research-transportation.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-305b finished units 8-11. part3 written (eras 08-10), self-review run, validator 0 errors, punct clean, prose check PASS.
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
| 8 | era 08 1900-1950 -> part3 | T-305b | done | ~1850w, validator 0 errors, emdash=0 semicolon=0 |
| 9 | era 09 1950-2000 -> part3 | T-305b | done | ~1950w, validator 0 errors, emdash=0 semicolon=0 |
| 10 | era 10 2000-today -> part3 | T-305b | done | ~1670w, validator 0 errors, emdash=0 semicolon=0 |
| 11 | final: self-review, --punct, validator, prose check | T-305b | done | part3 ~5060w, avg sentence 14.2, validator 0 errors, emdash=0 semicolon=0, PASS transportation / prose |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- era 2 | whose land Oñate's wagons entered, and is "first wheels" true | PATCH (cross-sourced from migration bank; "first" dropped) | PATCH 2026-09-29 (T-305a): Oñate's wagons...
- era 4 | did Virginia "tithables" include enslaved men | PATCH (Virginia Places, opened) | PATCH 2026-09-29 (T-305a): who counted as a "tithable"...
- era 6 | whose path the National Road followed | PATCH (Columbia Encyclopedia via encyclopedia.com, opened) | PATCH 2026-09-29 (T-305a): the National Road ran on a Native path
- era 6 | Moses Grandy after freedom (outline close contradicted the sold wife) | PATCH (Narrative full text, DocSouth) | PATCH 2026-09-29 (T-305a): Moses Grandy after freedom
- era 7 | 1867 strike demands and how it ended | PATCH (PBS, opened) | PATCH 2026-09-29 (T-305a): the 1867 strike...
- era 7 | which "last rails" Ging Cui, Wong Fook, Lee Shao carried | PATCH (SFSU APIA Biography Project, opened) | PATCH 2026-09-29 (T-305a): which "last rails"...
Totals: 6 found, 0 SEARCHED, NOT FOUND (existing T-248 records used for road-crew counts and turnpike workers).
- era 8 | porters' hours, pay, tips, "George", largest employer | PATCH (Chicago History Museum, History.com, opened) | PATCH 2026-09-29 (T-305b): the porters' hours...
- era 8 | what Lindbergh's flight was | PATCH (cross-sourced from exploration bank) | PATCH 2026-09-29 (T-305b): what Lindbergh's 1927 flight was
- era 9 | what the 1978 deregulation act changed | PATCH (Econlib, opened) | PATCH 2026-09-29 (T-305b): what the Airline Deregulation Act changed
- era 9 | Dusty Roads dates, lobbying, APFA | PATCH (CET public media, opened; EEOC 1965 still unconfirmed) | PATCH 2026-09-29 (T-305b): Dusty Roads, dates...
- era 10 | Key Bridge case status at writing time | PATCH (DOJ release, opened; no verdict found) | PATCH 2026-09-29 (T-305b): the Key Bridge charges...
T-305b totals: 5 found, 0 SEARCHED, NOT FOUND (existing T-248 record used for the Berwick appeal).

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
10. Era 8: trucks, buses, diesel locomotives and paved-road mileage (not in bank).
11. Era 8: 1937 as "the highest rate on record" (NSC figure unconfirmed).
12. Era 9: interstate design line (limited access, no stoplights, engineered grades) and the Divided Highways documentary.
13. Era 9: Ideal X "the first container ship" and McLean "invented container shipping" by "asking why cargo was loaded twice" (false-first risk, not in bank).
14. Era 9: SUV growth in the 1990s and two-car households (not in bank).
15. Era 9: Amtrak's losses caused by "jets and interstates" (cause not in bank).
16. Era 9: Dusty Roads's 1965 EEOC complaint with Jean Montague (unconfirmed).
17. Era 10: turn-by-turn phone navigation, "paper maps become souvenirs" (not in bank).
18. Era 10: "the country that built the transcontinental in six years has not yet built one true high-speed line" (closing reversal, not in bank).
19. Era 10: CAHSR official $89-128B range, 2033 service date; APTA transit ridership (all unconfirmed).

## Decisions and defects fixed
- Outline defect, era 6 Grandy: "saved enough to buy his wife and children" read as if the sold first wife was bought back. Prose states he married again and bought his second wife, his son ($450), and his daughters paid $1,200 each.
- Bank/outline defect, era 7: Ging Cui, Wong Fook, Lee Shao were placed on Ten-Mile Day; they laid the last track at Promontory, May 10, 1869.
- Outline defect, era 7: Ida B. Wells "dragged" (not in bank). Prose: the crew forced her off the train.
- Outline defect, era 7: 1867 strike "ended without formal concessions" kept, and the bank's LOC note that experienced men's pay later rose a little is stated; PBS ending (fines, lost June pay, armed posse) added.
- Outline defect, era 2: false "first wheeled vehicles" claim dropped.
- Outline defect, era 6: "Clinton's numbers answered the mockery" closing reversal removed; Clinton story ends on the Six Nations population fact.
- Personification repaired throughout: "the railroads split the continent into time zones" became railroad managers; Safety Appliance Act "forced" became members of Congress passed; companies hiring/buying became managers.
- Era 4 Paxton killings (1763) told in the 1700-1750 Conestoga span, signaled with its date, because the wagon's name is there.
- T-305b, outline defect era 8: "Congress ... staged" / "The Post Office staged" and "Congress funded" repaired to Post Office officials and members of Congress. "the Pullman Company was ... largest employer" kept as sourced; porters' conditions added from PATCH (400-hour month, lowest pay, tips, "George" as a slavery practice).
- T-305b, bank/outline defect era 8: DC-3 curator's first name not in bank, left out. Lindbergh flight facts cross-sourced rather than assumed.
- T-305b, outline defect era 9: Ideal X "first container ship" and McLean "invented" (false firsts) dropped. "Congress created the FAA" became "the crash led members of Congress to create". Deregulation "ends government control of routes and fares" restated from Econlib (the CAB's control phased out, board closed 1984). "flying became a bus, not a luxury" dropped.
- T-305b, outline defect era 9: highway displacement written with actors (highway officials, and Engelhardt's department choosing the Montgomery route); "Most of the neighborhoods chosen" attributed to Deborah Archer's quote.
- T-305b, outline defect era 10: "the government switches off" became US officials; Key Bridge charges written as an accusation with presumption of innocence (DOJ wording); Potomac "flew into" became "collided with" (bank wording).
- T-305b, era 8 buses: the bank names the 1932, 1943 and 1945 riders but not who threw them off, jailed or beat them. Prose says the records do not name them.

## PARKED EARLIER (FILED by the director)
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
- 2026-09-29 T-305b: before writing, bank PATCHes: era 8 porters' hours/pay/tips/"George" (Chicago History Museum, History.com, opened); era 8 Lindbergh flight facts (cross-sourced from exploration bank); era 9 Dusty Roads 1928-2023, lobbying, lineup, APFA 1977 (CET public media, opened; EEOC 1965 still unconfirmed, not written); era 10 Key Bridge charges (DOJ release May 12, 2026, opened; no verdict found).
- 2026-09-29 T-305b unit 8 era 08: ~1850 words, 4 stories (wright-brothers-transportation, jack-knight, miles-of-smiles-porters, irene-morgan), validator 0 errors, emdash=0 semicolon=0. Left out: trucks/buses/diesel and paved-mileage line (not in bank); "highest rate on record" for 1937 (NSC figure unconfirmed); DC-3 unnamed curator first name.
- 2026-09-29 T-305b unit 9 era 09: ~1950 words, 3 stories (dwight-eisenhower-transportation, barbara-dusty-roads, malcom-mclean), validator 0 errors, emdash=0 semicolon=0. PATCH: what the Airline Deregulation Act changed (Econlib, opened). Left out: Divided Highways documentary line; interstate "limited access, no stoplights" (not in bank); SUV growth and two-car households (not in bank); Ideal X as "first container ship" and McLean "invented" (false-first risk); Amtrak losses "to jets and interstates" as cause (not in bank); Roads's 1965 EEOC complaint (unconfirmed).
- 2026-09-29 T-305b unit 10 era 10: ~1670 words, 1 story (barbara-berwick), validator 0 errors, emdash=0 semicolon=0. Every figure dated and sourced in plain words. Key Bridge: DOJ indictment written as an accusation (no verdict as of 2026-09-29). Left out: "paper maps become souvenirs", "turn-by-turn in every phone" (not in bank); transcontinental-vs-high-speed comparison (closing reversal, not in bank); APTA transit ridership (unconfirmed); CAHSR $89-128B official range and 2033 service date (unconfirmed).
- 2026-09-29 T-305b unit 11: self-review (Version 2 + amendment §5 + policy §7) run on part3. Fixed: facts not in bank (early-car roads, porter duties, "four-wheel-drive", Uber "cab" order detail, "turn-by-turn", Amtrak cause, Ideal X "converted tanker", Retzlaff title, Morrison/Winston first names), anaphora in era 9 zoom, abstraction-as-actor ("federal road building forced", "phones changed"), unlike subjects merged (1972 deaths and minivan split into two spans), long sentences split, unsourced 2000-today figures given year and source. Final: part3 ~5060 words, avg sentence 14.2, validator 0 errors, emdash=0 semicolon=0, PASS transportation / prose.
