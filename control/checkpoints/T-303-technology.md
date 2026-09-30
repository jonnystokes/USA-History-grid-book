# CHECKPOINT T-303 | technology | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-303b landed (director verified: PASS  technology / prose)
VERIFY: python tools/project_state.py --check technology --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/technology/part1-before-1800.md (eras 1-5) · manuscript/technology/part2-1800s.md (eras 6-7)
        · manuscript/technology/part3-1900s-and-today.md (eras 8-10) · research/research-technology.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-303b done (units 8-11: part3 written, self-review run, final checks below).
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
| 8 | era 08 1900-1950 -> part3 | T-303b | done | 1842w, validator 0 errors, emdash=0 semicolon=0 |
| 9 | era 09 1950-2000 -> part3 | T-303b | done | 1648w, validator 0 errors, emdash=0 semicolon=0 |
| 10 | era 10 2000-today -> part3 | T-303b | done | 1851w, validator 0 errors, emdash=0 semicolon=0 |
| 11 | final: self-review, --punct, validator, prose check | T-303b | done | see Log |

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

- 08 | Wright three-axis control; Audion and transistor mechanism; ENIAC purpose/size/programming; 1908 crash cause | PATCH (NASA Glenn, MagLab, CHM, Army museum, Penn Today, NASM) | "PATCH 2026-09-29 (T-303b): how the Wright control, the Audion and the transistor worked..."
- 09 | who designed the Apple I and II, Jobs's role, first order; what GPS is and Selective Availability | PATCH (NIHF, LOC, CHM, EBSCO, GPS.gov) | "PATCH 2026-09-29 (T-303b): who designed the Apple I and II..."
- 10 | Williams in the ACLU's words (race, lineup, cell); how chatbots make errors (NIST AI 600-1, 2024); a documented chatbot error (Mata v. Avianca, June 22, 2023 opinion); Adafruit dated facts | PATCH | "PATCH 2026-09-29 (T-303b): the Williams arrest in the ACLU's words..."

## OPEN (should be rare)
None for eras 1-7.
None for eras 8-10.

## Outline claims left out
1. Morse as "painter turned inventor" (era 6): bank had no source; Britannica/LOC pages returned 403, search summary only. Recorded as unconfirmed PATCH.
2. Jenks grant date "March 6, 1646" (era 3): search summary only; wrote the archive date May 10, 1646.
3. Three Sisters mechanics (corn as bean pole, squash as ground cover): not in bank; wrote only the interplanting.
4. Daguerreotype chemistry (era 6): search summary only; wrote the process name only.
5. Whitney losing gin profits in lawsuits; Principio's labor force; John Stewart becoming Springfield's blacksmith; Valliere starting at 14; Falling Creek's two women and three children dead: all tagged unconfirmed in the bank; left out.
6. Parked items not in the outline and not used: Kinetoscope/Black Maria (era 7), Swift/Chase refrigerator car (era 7).
7. Used one parked item not in the outline: the 1755 Schuyler mine steam engine (era 5, parked from energy).

8. (T-303b) Selfridge crash details (propeller striking the rudder wire, 150 feet, fractured skull, 2,500 watching, Arlington burial): search summary only. Wrote "one of the propellers failed" (NASM caption).
9. (T-303b) Outline's "Ford's managers set chassis moving": the bank names no managers. Wrote the line without naming who ran it.
10. (T-303b) Community Memory's 25-cent posts and Teletype in a cardboard box; Felsenstein as moderator 1975-1986; other chatbot shares (Gemini, Copilot etc.); Challenger 2025 full-year figure: all unconfirmed, left out.
11. (T-303b) Outline's "No one asked the artists, credited them or paid them" (Ortiz): the testimony supports only "none had been asked" (for the April 2022 style-copy site). Wrote that.
12. (T-303b) Apple I $666 price (EBSCO) not used. CHM's dealer order (50 at $500) used. The two sources give different figures.
13. (T-303b) Parked items not used: iPod/iTunes/Spotify/Auto-Tune (music), Tennis for Two/Pong, Ardathy Spikes, ELVIS Act, Pew teen phone use and school phone bans, Birdseye flash freezing, kitchen inventions ([VERIFY]), copper wire. Used: refrigerator census shares, nylon dates, Fordson/Farmall and census tractor counts, americium smoke detector, Silicon Valley name.
14. (T-303b) ChatGPT launch-week figures kept, labeled "according to news reports".

## Decisions and defects fixed
- Land erasure (outline/bank silent): named the Susquehannock and Piscataway and the 1652 treaty for the Baltimore Iron Works (bank had "not supplied"); named the Ho-Chunk village at Grand Detour and the 1832 Fort Armstrong treaty for Deere's plow; named Native displacement by barbed wire (NARA) where the outline said only "fenced the open range".
- Hidden actors: outline/bank "Demand for cotton land drove the 1830s removal" and the museum's "the American government" replaced with President Andrew Jackson (signed May 28, 1830) and General Winfield Scott (1838), plus the 4,000 Cherokee dead (LOC).
- Semantic abstraction: the museum's "faced violence if they did not meet quotas" replaced with Solomon Northup's 1853 account (200-pound task, nightly weighing, 25/50/100 lashes, Epps himself whipping).
- Closing reversal in the bank ("the machine that was supposed to save labor instead multiplied the demand"): stated as plain fact.
- False "first": outline's "first PRACTICAL" electric light (era 7) and "first successful" mill are not in the sources; wrote "long-lasting lamp" (DOE hours) and "the start of the factory textile industry".
- Falling Creek: bank's original "destroyed before it shipped" contradicted by DHR; told as a disagreement between DHR and the county.
- Quotations with a semicolon or dashes split with no word changed: Jenks petition, Franklin autobiography, Northup, Bell's "Mr. Watson" sentence.
- Ambiguity: "Jeremiah Black" written in full each time.

- (T-303b) Outline "These systems ... make documented errors, state both": the bank named no chatbot error. Added NIST AI 600-1 (July 2024) on how language models produce confident false answers, and the Mata v. Avianca sanctions opinion (June 22, 2023, Judge Castel, $5,000).
- (T-303b) Face-recognition span: added from the ACLU that Williams is Black, that police built a photo lineup from the match and showed it to a contractor who had not seen the theft, and the settlement's lineup rule. The outline had only "Detroit police officials agreed".
- (T-303b) Personification in the outline ("Grace Hopper taught computers", "Ford made the line the way things get built", "the plant started"): rewritten with people or mechanisms. Company verbs kept only where a company literally sells or releases a product.
- (T-303b) Contrastive framing "The web is NOT an American invention": stated plainly who invented it and where, then what Americans built (Mosaic).
- (T-303b) Bank's unconfirmed Selfridge details not written. Bank's "Bell Labs in New Jersey" gloss removed from the prose (not sourced).
- (T-303b) The Steve Jobs (2015) film is labeled a drama in its Movie line, with the documentary named beside it.

## PARKED EARLIER (FILED by the director)
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
- 2026-09-29 T-303b unit 8 era 08: part3 created. 1842 words, avg 13.5; validator 0 errors; --punct emdash=0 semicolon=0. Stories: wright-brothers-technology, henry-ford-technology, eniac-programmers, ernest-lawrence-technology. Used parked items: refrigerator census shares (home-family), nylon dates (styles), Fordson/Farmall and 1920/1954 census (food-farming).
- 2026-09-29 T-303b unit 9 era 09: 1648 words, avg 14.2; validator 0 errors; --punct emdash=0 semicolon=0. Stories: grace-hopper, marty-cooper, lee-felsenstein, jobs-wozniak. Used parked item: americium smoke detector (elements); Silicon Valley name (elements).
- 2026-09-29 T-303b unit 10 era 10: 1851 words, avg 15.8; validator 0 errors; --punct emdash=0 semicolon=0. Stories: limor-fried, karla-ortiz. Every 2000-today figure carries its year and source (Pew 2025/2026, Challenger Aug 2026, NIST 2024, court 2023, ACLU/Michigan Public 2024, news reports labeled).
- 2026-09-29 T-303b unit 11: self-review (Version 2 Self-Review + amendment section 5) run on part3. Fixed: unsourced glosses (Bell Labs location, 'oil company', 'first method', 'free' lessons, Fried's sole ownership), a hedge ('Many AI programs'), institution-as-actor repairs, story openings that began Name + verb (Cooper, Fried), era-09 opening that matched part2's era shape, long sentences split. Final: 1597 / 1659 / 1842 words (eras 8/9/10).
