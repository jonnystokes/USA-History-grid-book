# CHECKPOINT T-320 | disasters | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-320b landed (director verified: PASS  disasters / prose)
VERIFY: python tools/project_state.py --check disasters --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/disasters/part1-before-1800.md (eras 1-5) · manuscript/disasters/part2-1800s.md (eras 6-7)
        · manuscript/disasters/part3-1900s-and-today.md (eras 8-10) · research/research-disasters.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-320b finished units 8-11. PASS  disasters / prose.
NEXT:   director: commit; audit step

## Research state before writing (2026-09-29)

PASS  disasters / research
measured: stage=RESEARCHED eras=10/10 stories=12 (v12 c0 t0) verify_tags=0 bank=36035w outline=16266w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-320a | done | ~950w, validator 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-320a | done | file now 2230w; === part1-before-1800.md : 1 chapters, 1 stories, 0 errors; emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-320a | done | file now 3819w; === part1-before-1800.md : 1 chapters, 2 stories, 0 errors; emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-320a | done | file now 5469w; === part1-before-1800.md : 1 chapters, 2 stories, 0 errors; emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-320a | done | file now 6915w; === part1-before-1800.md : 1 chapters, 3 stories, 0 errors; emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-320a | done | file now 2060w; === part2-1800s.md : 1 chapters, 1 stories, 0 errors; emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-320a | done | file now 4752w; === part2-1800s.md : 1 chapters, 3 stories, 0 errors; emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-320b | done | file now 4661w; === part3-1900s-and-today.md : 1 chapters, 3 stories, 0 errors; emdash=0 semicolon=0 |
| 9 | era 09 1950-2000 -> part3 | T-320b | done | file now 7964w; === part3-1900s-and-today.md : 1 chapters, 4 stories, 0 errors; emdash=0 semicolon=0 |
| 10 | era 10 2000-today -> part3 | T-320b | done | file now 11458w; === part3-1900s-and-today.md : 1 chapters, 6 stories, 0 errors; emdash=0 semicolon=0 |
| 11 | final: self-review, --punct, validator, prose check | T-320b | done | part3 11516w; all three files 0 errors, emdash=0 semicolon=0; PASS disasters / prose (22570w, 12 stories verified) |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 03 | Why did Powhatan besiege Jamestown, and how many were alive? | PATCH | "PATCH 2026-09-30 (T-320a): why Powhatan besieged Jamestown, and the Starving Time counts"
- 06 | Where was the Pulaski bound? | PATCH | "PATCH 2026-09-30 (T-320a): the Pulaski's route"
- 06 | Did Captain Perin die in the Moselle blast? | PATCH (Lloyd 1856) | "PATCH 2026-09-30 (T-320a): Captain Perin's death, and the month of the New Madrid relief law"
- 06 | Date of the New Madrid relief law | PATCH for the month (February 1815). The day (Feb 17) stays unconfirmed, so the prose gives the month only. | same heading
- 08 | How did Triangle workers die at the windows, and what laws followed? | PATCH | "PATCH 2026-09-30 (T-320b): how the Triangle workers died at the windows, and the laws after"
- 09 | USGS count for the 1964 Alaska quake (131 was search summary only) | PATCH (131: 122 tsunami, 9 quake; the 115/16 state split stays unconfirmed, not written) | "PATCH 2026-09-30 (T-320b): the USGS death count for the 1964 Alaska earthquake"
- 09 | What failed at Three Mile Island? | PATCH (copied from research-energy.md, WNA) | "PATCH 2026-09-30 (T-320b): what failed at Three Mile Island"
- 10 | Where the 9/11 planes crashed, rescuers killed | PATCH | "PATCH 2026-09-30 (T-320b): where the September 11 planes crashed, and the rescuers killed"
- 10 | What Pou and the nurses were accused of doing (drugs, patients) | PATCH | "PATCH 2026-09-30 (T-320b): what Anna Pou and two nurses were accused of at Memorial Medical Center"
- 10 | Harvey deaths and rain from a primary source | PATCH (NHC report) | "PATCH 2026-09-30 (T-320b): Hurricane Harvey's deaths and rain, from the National Hurricane Center"

## OPEN (should be rare)

## Outline claims left out
- 01: none of substance. Chaco and Cahokia towns left to native-nations as the outline says.
- 02: the "Shared with other chapters" pointer bullets (Ribault's 1565 wreck, Narvaez 1528). Pointers to other chapters would break the fourth wall and this bank does not source the events.
- 02: "The viceroy of New Spain gave him command" (Luna story). The bank does not say who appointed Luna.
- 03: the colonists ate "horses, dogs, rats and leather" (only in the food-farming bank, not this one).
- 05: "It is the deadliest Atlantic hurricane on record" (Great Hurricane of 1780). Not sourced. Replaced with NOAA's sourced claim about the 1780 season.
- 07: Avondale mine fire pointer (sourced only in research-energy.md, and energy / work-workers tell it).
- 07: the exact hour the Johnstown dam broke (3:10 p.m. is search summary only).
- 08: the "Shared with other chapters" pointer span (Monongah, Hawks Nest, Quebec Bridge, Big Burn): pointers would break the fourth wall.
- 08: Galveston "pumped sand under the city" (bank says only that the grade was raised).
- 08: 1927 "Other levees upstream broke on their own" and "Army engineers built the world's longest system of levees" (not in bank). Prose says the Caernarvon blast was unnecessary and names the Flood Control Act of 1928 only.
- 08: Eastland "long known to be top-heavy" (bank: earlier listing incidents incl. 1906; prose uses that).
- 08: Okeechobee "forced Black survivors to work" in the outline era summary (bank says only that Black workers did most of the cleanup). Dropped.
- 08: San Francisco "Firefighters and soldiers used dynamite" (bank names firefighters only).
- 09: Air Florida "Less than a minute after takeoff" and Williams "twice" caught the line (not in the opened text).
- 09: Mayor Daley "publicly criticized Donoghue's count" (bank has only Donoghue's "when Mayor Daley was being critical"). Prose gives Donoghue's words about no press conferences and Daley told late.
- 09 and 10: pointer spans (Challenger, oil spills, COVID-19, Key Bridge, Potomac collision, Upper Big Branch).
- 10: Katrina "many of them without cars or money" and the Gretna bridge date of September 1 (not in bank).
- 10: Maria "Most people lost clean water"; Harvey "Floods covered much of Houston" (not in bank).
- 10: what the Heaven's 27 Camp Safety Act requires (search summary only). Prose names the law only.
- 10: who reported the Surfside damage in 2018 and who delayed the repair (bank: not named).

## Decisions and defects fixed
- 05 outline: "the deadliest Atlantic hurricane on record" for the Great Hurricane of 1780 is not in the bank. NOAA's line is about the 1780 SEASON. Prose uses the season claim, attributed.
- 06 outline: New Madrid law date "February 17, 1815" is tagged unconfirmed in the bank. Prose gives "February 1815" (PATCH confirms the month).
- 06 outline: "The captain and owner, Isaac Perin" and "The explosion killed Perin" rested on search summaries. Death confirmed by PATCH (Lloyd 1856). Ownership not in bank, dropped.
- 02 outline: the 1587 attack sentence did not name the backstory. Prose names Wingina's killing by Ralph Lane's men (June 1586) and George Howe's killing in revenge, from the bank's PATCH.
- 01 outline: attackers' treatment of bodies at Castle Rock added from the bank (Kuckelman 2002) so the harm is stated, attackers stated as unknown.
- 03 outline: Starving Time cause stated only as "Powhatan's people had stopped trading food and surrounded the fort." Prose now gives the colonists' taking of food by force, Francis West's beheading of two Patawomeck warriors, Ratcliffe's death, and both starting counts (240 vs about 500), from a new PATCH.
- 07 outline: "rich Pittsburgh men" kept as "wealthy" with the bank's specifics (more than fifty steel, coal and railroad owners). Pulaski "Several people died of thirst, heat and exhaustion" replaced with the named deaths the bank records.
- 07 outline: Clara Barton resigned "after growing criticism of how she ran it". Bank says only "mounting criticism". Prose says "after growing criticism".
- Throughout: institutions as subjects repaired (Virginia Company leaders, club members, Signal Service forecasters, Red Cross workers/leaders). Document elements take approved verbs (records, lists, states, describes, identifies).
- 08-10 (T-320b): outline "At least 2,500 ... 131 (USGS)" and others were search-summary figures; replaced with PATCHed or bank-sourced figures. Hugh Kwong Liang story no longer implies the bank shows him in the segregated camp (it shows the Chinese survivors there). Kate Alterman: outline implied she saw Margaret die; prose says she saw Margaret catch fire and that Margaret died in the fire. 1927 camps: outline "Local white leaders" (bank: "rural leaders"), prose says local leaders; the unnamed police killing and the lynching of Owen Flemming added from the bank (camp forced labor, hard-subjects policy). Buffalo Creek plans never sent to the state, Hyatt first design at 60% of code, St. Francis coroner's second finding (public policy blame) added from the bank. Freeman timeline fixed (died the day after the rescue). Institutions as actors repaired (NHC, USGS, NTSB, TSHA, FEMA, Carnegie Fund, newspapers, reports).

## HANDOFF for writer B (T-320b)
- Voice: plain present-day, sentences ~13 words average, each span opens on its point. No pointers to other chapters, no fourth-wall lines.
- Terms ALREADY DEFINED in part1/part2 (do not define again): volcano ash as mulch, archaeologist, radiocarbon dating, drought, tree rings, plates, fault, subduction, hurricane, chiefdom and paramount chiefdom, malnutrition, magnitude (part1 era 03), aftershocks, tsunami, salvage, oakum, militia, vestry, fire insurance, lightning rod, arsonist, manumission, legislature, speculator, seismologist, boiler, starboard, schooner, delirious, tornado, flatboat, safety valve, kickback, quartermaster, coroner, martial law, blizzard, spillway, morgue, "act of God".
- Threads that continue after 1900: (1) Galveston 1900 is in era 08, and Clara Barton's last relief work there is already mentioned in her story (part2), so do not retell her life. (2) The Red Cross (founded 1881) and the civilian Weather Bureau (1890 law, Department of Agriculture) both exist now. (3) Steamboat inspection: 1838 law, 1852 Steamboat Act (Treasury supervising inspectors), 1871 law. The Titanic/Seamen's Act and Eastland continue the ship-safety thread. (4) "Help went mostly to the rich" (Charleston 1740) and relief steered away from Black islanders (Sea Islands 1893) set up the 1927 flood camps and Katrina. (5) Owners and officials blamed, no one punished (Sultana, Johnstown) sets up Triangle and later. (6) Cascadia fault: 19 great quakes, last in 1700 (era 04), for any modern warning mention. (7) Mount St. Helens 1980 is named once in era 01 as a size comparison only.
- Story slugs used in part1/part2: tristan-de-luna-disasters, anthony-thacher, will-st-philips-church, rebecca-lamar, victor-heiser, clara-barton-disasters.

## TO PARK (for the director, burst runs only)

## Log
- 2026-09-30 T-320a unit 1 (before-1500) landed: ~950 words, validator 0 errors, --punct emdash=0 semicolon=0. No new PATCH for this era.
- 2026-09-30 T-320a unit 2 landed. File manuscript/disasters/part1-before-1800.md now 2230 words. === part1-before-1800.md : 1 chapters, 1 stories, 0 errors. manuscript/disasters/part1-before-1800.md: emdash=0 semicolon=0. Story tristan-de-luna-disasters. No new PATCH.
- 2026-09-30 T-320a unit 3 landed. File manuscript/disasters/part1-before-1800.md now 3819 words. === part1-before-1800.md : 1 chapters, 2 stories, 0 errors. manuscript/disasters/part1-before-1800.md: emdash=0 semicolon=0. Story anthony-thacher. PATCH used: Powhatan siege and Starving Time counts (era 03).
- 2026-09-30 T-320a unit 4 landed. File manuscript/disasters/part1-before-1800.md now 5469 words. === part1-before-1800.md : 1 chapters, 2 stories, 0 errors. manuscript/disasters/part1-before-1800.md: emdash=0 semicolon=0. No story (none in outline). No new PATCH.
- 2026-09-30 T-320a unit 5 landed. File manuscript/disasters/part1-before-1800.md now 6915 words. === part1-before-1800.md : 1 chapters, 3 stories, 0 errors. manuscript/disasters/part1-before-1800.md: emdash=0 semicolon=0. Story will-st-philips-church. No new PATCH.
- 2026-09-30 T-320a unit 6 landed. File manuscript/disasters/part2-1800s.md now 2060 words. === part2-1800s.md : 1 chapters, 1 stories, 0 errors. manuscript/disasters/part2-1800s.md: emdash=0 semicolon=0. Story rebecca-lamar. PATCHes: Pulaski route; Perin's death (Lloyd 1856) and relief law month (February 1815).
- 2026-09-30 T-320a unit 7 landed. File manuscript/disasters/part2-1800s.md now 4752 words. === part2-1800s.md : 1 chapters, 3 stories, 0 errors. manuscript/disasters/part2-1800s.md: emdash=0 semicolon=0. Stories victor-heiser, clara-barton-disasters. No new PATCH for this era.
- 2026-09-30 T-320b unit 8 landed. File manuscript/disasters/part3-1900s-and-today.md now 4661 words. === part3-1900s-and-today.md : 1 chapters, 3 stories, 0 errors. emdash=0 semicolon=0. Stories isaac-cline, hugh-kwong-liang, kate-alterman. PATCH: Triangle window deaths and laws after (era 08).
- 2026-09-30 T-320b unit 9 landed. File now 7964 words. === part3-1900s-and-today.md : 1 chapters, 4 stories, 0 errors. emdash=0 semicolon=0. Story melvin-windsor. PATCHes: USGS 1964 count 131 (era 09); Three Mile Island mechanism copied from research-energy.md (era 09).
- 2026-09-30 T-320b unit 10 landed. File now 11458 words. === part3-1900s-and-today.md : 1 chapters, 6 stories, 0 errors. emdash=0 semicolon=0. Stories herbert-freeman-jr, jesse-vazquez. PATCHes: Harvey (NHC report), September 11 crash sites and rescuers killed, Memorial Medical Center accusations (era 10).
- 2026-09-30 T-320b unit 11: self-review run on part3 (cadence, openers, institutions, passives, hard words, facts re-checked against bank). Validator 0 errors on all three files. --punct emdash=0 semicolon=0 on all three. PASS  disasters / prose (22570w, 12 stories verified).
