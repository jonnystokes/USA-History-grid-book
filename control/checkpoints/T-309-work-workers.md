# CHECKPOINT T-309 | work-workers | prose | ONE writer, all 10 eras (part1, part2, part3)

STATUS: T-309 landed (director verified: PASS  work-workers / prose)
VERIFY: python tools/project_state.py --check work-workers --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/work-workers/part1-before-1800.md (eras 1-5) · manuscript/work-workers/part2-1800s.md (eras 6-7)
        · manuscript/work-workers/part3-1900s-and-today.md (eras 8-10) · research/research-work-workers.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    DONE. All 11 units complete, all three files self-reviewed. Prose check PASS.
NEXT:   Director: commit.

## Research state before writing (2026-09-29)

PASS  work-workers / research
measured: stage=RESEARCHED eras=10/10 stories=17 (v17 c0 t0) verify_tags=0 bank=18263w outline=6280w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-309 | done | file 307w, validator 0 errors, punct 0/0 |
| 2 | era 02 1500s -> part1 | T-309 | done | file 623w, validator 0 errors, punct 0/0 |
| 3 | era 03 1600s -> part1 | T-309 | done | file 1628w, validator 0 errors, punct 0/0 |
| 4 | era 04 1700-1750 -> part1 | T-309 | done | file 2147w, validator 0 errors, punct 0/0 |
| 5 | era 05 1750-1800 -> part1 | T-309 | done | file 2450w (wc incl. markers), validator 0 errors, punct 0/0; part1 self-review run |
| 6 | era 06 1800-1850 -> part2 | T-309 | done | file 1654w, validator 0 errors, punct 0/0 |
| 7 | era 07 1850-1900 -> part2 | T-309 | done | file 4190w, validator 0 errors, punct 0/0; part2 self-review run |
| 8 | era 08 1900-1950 -> part3 | T-309 | done | file 4465w, validator 0 errors, punct 0/0 |
| 9 | era 09 1950-2000 -> part3 | T-309 | done | file 6996w, validator 0 errors, punct 0/0 |
| 10 | era 10 2000-today -> part3 | T-309 | done | file 9238w (wc incl. markers), validator 0 errors, punct 0/0 |
| 11 | final: self-review, --punct, validator, prose check | T-309 | done | 3 files 0 errors, punct 0/0 each, prose check PASS (14452w, 17 stories verified) |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 03 | Tsenacomoco extent and 1622 counts (were search-summary only) | PATCH: confirmed; Martin's Hundred "at least 58" replaces 73 | "Tsenacomoco and the 1622 death counts"
- 03 | how branding was done (clinical word) | PATCH: red-hot iron, general method (Encyclopedia.com); Virginia record gives letter and place only | "what branding was"
- 06 | Lowell hours (were search-summary only) and the 1845 hearing | PATCH: 1845 House report hours, Schouler committee | "the Lowell working day"
- 06 | Lowell weekly pay | left out (unconfirmed), noted in same PATCH
- 07 | Haymarket names (search summary only) | PATCH: confirmed (CHM, PBS) | "Haymarket names confirmed"
- 07 | 1877 national death toll | SEARCHED, NOT FOUND; 10% cut confirmed | "a national death toll for the 1877 railroad strike"
- 08 | silicosis (clinical word; bank wording unconfirmed) | PATCH: OSHA, NIOSH | "what silicosis does"
- 08 | Keating-Owen provisions and vote (unconfirmed) | PATCH: Encyclopedia.com, Capitol Visitor Center | same heading
- 09 | name of the 16-year-old killed March 28, 1968 | PATCH: Larry Payne, DOJ file | "Larry Payne"
- 09 | El Monte 1995 (parked from styles) | PATCH: copied with sources | "El Monte, 1995"
- 10 | federal minimum wage (no DOL page opened) | PATCH: DOL chart | "the federal minimum wage confirmed"
- 10 | Impact Plastics 2024 (parked from disasters) | PATCH: copied with sources | same heading

## OPEN (should be rare)

## Outline claims left out
- 01: children learned by working beside adults (not in bank).
- 03: Martin's Hundred 20,000 acres, 1617 founding, "73 killed" (unconfirmed; replaced by "at least 58").
- 04: Franklin worked as a journeyman before owning a shop (not in bank story line).
- 06: Lowell weekly pay $2.40-$3.20 (unconfirmed); LFLRA "first legislative investigation" (the "first" is outline-only).
- 07: 1877 national toll "about 100" (SEARCHED, NOT FOUND); Captain Ward's order; Homestead governor's name; Avondale owner (all unconfirmed).
- 08: Addie Card "barefoot"; Grace Fryer's death; Keating-Owen sons' names; Lawrence (LoPizzo) death; Hawks Nest company count 109; Memorial Day union SWOC (all unconfirmed or not in bank).
- 09: Youngstown "5,000 jobs" (outline-only).
- 10: "most Americans work in services" (not in bank); Amazon's dispute of the Senate report; ALU-Teamsters affiliation date; Starbucks 131-day length (all unconfirmed).
- Parked items not used: whaling (Haley), Persis Albee, Lucy Larcom, NM encomienda tribute, Patapsco, company scrip, Maggie Walker, AFM recording ban, Ardathy Spikes, MIRA survey, WGA/SAG-AFTRA 2023 (told in storytelling-evolution), LA garment piece rates, Rana Plaza, Esteban Chavez Jr., Renica Turner.

## Decisions and defects fixed
- Bank defect: Martin's Hundred "73 killed" (search summary) replaced by the confirmed "at least 58" (HistoryNet, official report overcounted).
- Bank defect: branding method was unstated; defined from Encyclopedia.com (red-hot iron), prose says the Virginia records name only the letter and place.
- Outline softening/agent gaps repaired in prose: 1877 Pittsburgh shooting now names the Philadelphia militia and the woman and three children killed; Memphis 16-year-old now named (Larry Payne) with DOJ findings; King's killer named (James Earl Ray, HSCA); bracero 10 percent now names US employers as the ones who withheld it.
- Outline personification ("the city granted", "Congress banned", "GM recognized", "company cut off food") rewritten with people as actors.
- Parked items added: El Monte 1995 (era 09) and Impact Plastics 2024 (era 10), copied into the bank with sources.

## TO PARK (for the director, burst runs only)

## Log
- 2026-09-29 T-309: eras 01-10 written one at a time, each logged in the Units table (validator 0 errors, punct 0/0 after every era). Final: prose check PASS, manuscript 14452w, 17 stories verified.
