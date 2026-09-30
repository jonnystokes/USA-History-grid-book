# CHECKPOINT T-320 | disasters | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-320a landed (director verified: FAIL  disasters / prose)
VERIFY: python tools/project_state.py --check disasters --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/disasters/part1-before-1800.md (eras 1-5) · manuscript/disasters/part2-1800s.md (eras 6-7)
        · manuscript/disasters/part3-1900s-and-today.md (eras 8-10) · research/research-disasters.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-320a finished units 1-7 (part1 and part2 written, self-reviewed, validator 0 errors, --punct zero). Writer B takes over.
NEXT:   T-320b: unit 8

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
| 8 | era 08 1900-1950 -> part3 | T-320b | todo | |
| 9 | era 09 1950-2000 -> part3 | T-320b | todo | |
| 10 | era 10 2000-today -> part3 | T-320b | todo | |
| 11 | final: self-review, --punct, validator, prose check | T-320b | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 03 | Why did Powhatan besiege Jamestown, and how many were alive? | PATCH | "PATCH 2026-09-30 (T-320a): why Powhatan besieged Jamestown, and the Starving Time counts"
- 06 | Where was the Pulaski bound? | PATCH | "PATCH 2026-09-30 (T-320a): the Pulaski's route"
- 06 | Did Captain Perin die in the Moselle blast? | PATCH (Lloyd 1856) | "PATCH 2026-09-30 (T-320a): Captain Perin's death, and the month of the New Madrid relief law"
- 06 | Date of the New Madrid relief law | PATCH for the month (February 1815). The day (Feb 17) stays unconfirmed, so the prose gives the month only. | same heading

## OPEN (should be rare)

## Outline claims left out
- 01: none of substance. Chaco and Cahokia towns left to native-nations as the outline says.
- 02: the "Shared with other chapters" pointer bullets (Ribault's 1565 wreck, Narvaez 1528). Pointers to other chapters would break the fourth wall and this bank does not source the events.
- 02: "The viceroy of New Spain gave him command" (Luna story). The bank does not say who appointed Luna.
- 03: the colonists ate "horses, dogs, rats and leather" (only in the food-farming bank, not this one).
- 05: "It is the deadliest Atlantic hurricane on record" (Great Hurricane of 1780). Not sourced. Replaced with NOAA's sourced claim about the 1780 season.
- 07: Avondale mine fire pointer (sourced only in research-energy.md, and energy / work-workers tell it).
- 07: the exact hour the Johnstown dam broke (3:10 p.m. is search summary only).

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
