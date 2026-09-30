# CHECKPOINT T-302 | energy | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-302b landed (director verified: PASS  energy / prose)
VERIFY: python tools/project_state.py --check energy --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/energy/part1-before-1800.md (eras 1-5) · manuscript/energy/part2-1800s.md (eras 6-7)
        · manuscript/energy/part3-1900s-and-today.md (eras 8-10) · research/research-energy.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-302b done 2026-09-29. part3 (eras 08-10, 6724w) written, self-review run, validator 0 errors, --punct 0/0, prose check PASS. (Prev: T-302a done 2026-09-29. part1 (eras 01-05, 3768w) and part2 (eras 06-07, 3620w) written, self-review run, validator 0 errors, --punct 0/0 both.
NEXT:   T-302b: Unit 8, era 08 1900-1950 -> create manuscript/energy/part3-1900s-and-today.md (eras 08-10). Copy part2's hb-chapter line with file="part3" and a matching hb-note. Voice and layout: part1/part2. Do not re-explain: coal gas, anthracite, AC/DC, transformer, dynamo, central power station, charcoal, collier, cord, kerosene, distillation, horsepower (all defined in parts 1-2). Samuel Insull already named in the Current War movie line (era 07).

## Research state before writing (2026-09-29)

PASS  energy / research
measured: stage=RESEARCHED eras=10/10 stories=11 (v11 c0 t0) verify_tags=0 bank=11300w outline=6615w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-302a | done | ~330w, 0 err, 0/0 |
| 2 | era 02 1500s -> part1 | T-302a | done | ~400w, 0 err, 0/0 |
| 3 | era 03 1600s -> part1 | T-302a | done | ~1010w, 0 err, 0/0 |
| 4 | era 04 1700-1750 -> part1 | T-302a | done | ~580w, 0 err, 0/0 |
| 5 | era 05 1750-1800 -> part1 | T-302a | done | ~1345w, 0 err, 0/0 |
| 6 | era 06 1800-1850 -> part2 | T-302a | done | ~1100w, 0 err, 0/0 |
| 7 | era 07 1850-1900 -> part2 | T-302a | done | ~2450w, 0 err, 0/0 |
| 8 | era 08 1900-1950 -> part3 | T-302b | done | ~2350w, 0 err, 0/0 |
| 9 | era 09 1950-2000 -> part3 | T-302b | done | ~2030w, 0 err, 0/0 |
| 10 | era 10 2000-today -> part3 | T-302b | done | ~2170w, 0 err, 0/0 |
| 11 | final: self-review, --punct, validator, prose check | T-302b | done | part3 6724w, 0 err, 0/0, PASS energy / prose |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 01 | what a travois is; what cultural burning was for; Karuk/Yurok burn cycle | PATCH | era 01 PATCH 2026-09-29 (T-302a)
- 02 | which expeditions brought horses, how many | PATCH | era 02 PATCH 2026-09-29 (T-302a)
- 03 | whose land Flowerdew was; who worked it; a cord; fate of Mason's mills | PATCH | era 03 PATCH 2026-09-29 (T-302a)
- 03 | what the 1621 windmill ground | SEARCHED, NOT FOUND | same era 03 PATCH
- 04 | whose land the Baltimore Iron Works stood on | PATCH | era 04 PATCH 2026-09-29 (T-302a)
- 05 | how the Newcomen engine worked; Schuyler engine fires and fate; whose land Hopewell stood on | PATCH | era 05 PATCH 2026-09-29 (T-302a)
- 05 | who did the labor at the Schuyler mine (enslaved?) | SEARCHED, NOT FOUND | era 05 SNF 2026-09-29 (T-302a)
- 06 | Fell's grate; how coal gas was made and who could afford it; how whale oil was made; Haley's life | PATCH | era 06 PATCH 2026-09-29 (T-302a)
- 06/07 | what camphene was; lamp-fuel prices | PATCH | era 07 PATCH 2026-09-29 (T-302a)
- 07 | Drake's drive pipe; Pearl Street's coal boilers; AC, DC and the transformer; Kemmler's crime and execution; the 1888 NY law; Avondale's ventilating furnace and owner | PATCH | era 07 PATCH 2026-09-29 (T-302a)

- 08 | Spindletop driller and land; Insull's fall and the 1935 act; what was done to the Osage (FBI/OHS via crime-justice bank) | PATCH | era 08 PATCH 2026-09-29 (T-302b)
- 09 | how a nuclear plant makes power; was Vogtle 3 really the first reactor since TMI (no: Watts Bar 2, 2016) | PATCH | era 09 PATCH 2026-09-29 (T-302b)
- 10 | what fracking is; Oklahoma earthquakes; Dakota Access dates and actors; TMI-1 restart status | PATCH | era 10 PATCH 2026-09-29 (T-302b)

## OPEN (should be rare)

## Outline claims left out
- eras 08-10 (T-302b), 10 claims: Spindletop oil "just as the automobile arrived to drink it" (TSHA does not name cars). REA co-ops strung "the wires the companies would not" as a general claim (kept only Pearl Yates's case). "Most city homes were wired" in 1935. Insull "wiping out small investors" and the "Ishmael or Insull" wording (prose: Roosevelt named him). Ickes's "most potent weapons" quote (no first name or title in bank). Grand Coulee 1994 settlement (unconfirmed). Garrison "80 percent" count and 152,360 acres (search summary of Wikipedia). Oregon and New Jersey gas flags (unconfirmed). Data centers and AI pushing demand (no figure in bank). ERCOT collapse "could have taken weeks to fix" (not in bank).
- era 07: Drake "ex-railroad conductor" (not in bank). "AC could be stepped up, sent miles" (bank has only: AC voltage easily converted by transformer, DC line losses limit distance). Niagara-Buffalo distance. "Alternating current ... still is" closing line. Westinghouse "absorbed the smear campaign without answering in kind" (not in bank). Tesla "immigrant" (not in bank). Movie cast first names (bank has surnames only, prose uses surnames). Avondale owner's railroad link (search summary only).
- Total outline claims left out, eras 01-07: 14.
- era 06: "steam engines spread through boats and mills" (not in bank for this era). "nearly smokeless" anthracite (not in bank). "Pacific whaling grounds" for Haley (search summary only).
- era 05: span "Whale oil toward its peak" (bank has only "fleet growth"; "one of the young country's biggest businesses" not in bank). One line kept in the era zoom. Unconfirmed: Bird's enslaved workers built the headrace; Collier Sam in Baker Johnson's 1809 will (search summary only).
- era 04: "Water wheels powered colonial industry" and "far more of them" (no bank figure). Outline's "Feeding one furnace took forestland by the hundreds of acres" kept for era 05 where Hopewell documents it.
- era 03: "Oxen and horses did the plowing and hauling in the colonies" (not in bank). "Forests near towns went first" (not in bank). Wall's deposition detail "three or four years" and the two houses (genealogy pages only, unconfirmed).

## Decisions and defects fixed
- eras 08-10 (T-302b): outline and bank say no newly built US reactor came online for four decades after TMI. EIA: Watts Bar 2 started in 2016 (begun 1973). Prose states both. Outline "passed Saudi Arabia" 2018: prose says Russia (bank correction note). Bank's "A 1921 law put Osage money under guardians" and outline "TVA gained", "Norris Dam moved families": personification, prose names judges and TVA officials. Outline Monongah "Many of the dead were immigrants": source gives no share, prose says "the dead included". Garrison: Cultural Survival's 300 of 356 families does not equal its "more than 90 percent", so prose gives only the source's own percentage "by one count". Osage: outline gives only "more than 60", prose gives all three counts and what was done (shooting, poison, bombing) with Hale named. TMI: outline's "the fear was real and it mattered" dropped as evaluative. Uranium: added ACHRE 1995 finding (federal officials did not require ventilation or warn miners).
- era 07: outline "Kerosene did not so much kill whaling" and "handed the market to petroleum" personify; prose names members of Congress and the tax. DOE credits Edison himself with electrocuting animals, Smithsonian says Brown ran the tests with Edison paying: prose follows Smithsonian and bank. Outline says Kemmler's execution was "botched and gruesome": prose states what was done (17 s, revived, 1 to 4 more minutes, coat on fire, smell of burning flesh) with no adjective. Kemmler's crime and victim added (hard subject, actor named). Avondale: outline passive; prose names the Steuben Coal Company as owner and says the owners built the breaker over the only shaft. Houck birth year: both NPS figures stated.
- era 07: bank says Pennsylvania granted Drake's pension, AOGHS says Titusville residents secured it: prose says the state granted it after residents pushed for it.
- era 05: outline says Schuyler ordered the engine "from England in 1748". Lienhard: the mine flooded in 1748 and Schuyler then paid Jonathan Hornblower. Prose follows the sources. Lienhard and McCormick disagree on the engine's end (repaired 1793 vs broken up about 1800): prose uses McCormick, who cites contemporary newspapers.
- era 01: bank/outline say "no draft animals north of Mexico" yet dogs dragged the travois. Prose says no horses, oxen or mules, and dogs were the only hauling animals.
- era 01: bank credits NPS with naming Karuk, Yurok and Hupa. The NPS page names none of them. Prose uses the Forest Service study (Karuk, Yurok) and leaves Hupa out.
- era 02: outline calls the horse "the first new power source"; the 1598 mill is the first water power. Oñate colony size left out (two counts, 400 men vs 600).

## PARKED EARLIER (FILED by the director)
- native-nations / exploration, era 1500s: NPS says de Soto's men took all the food at Hymahi and de Soto burned at least one inhabitant to death while questioning them about Cofitachequi (energy bank era 02 PATCH 2026-09-29, NPS Congaree page). Energy tells it in one sentence.
- crime-justice, era 1850-1900: Kemmler v. Durston, full sourced account (crime, 1888 law, appeals, execution) in energy bank era 07 PATCH 2026-09-29 (NY Courts Historical Society, Smithsonian).
- slavery-freedom / elements, era 1700-1750: search summary says the Schuyler family relied on enslaved laborers in the Schuyler copper mine (Montclair State University "Slavery in Mid-18th-Century New Jersey" part 3, page now 404). Unconfirmed. Energy bank era 05 SNF 2026-09-29.

## Log
- 2026-09-29 T-302b: self-review run on part3 (Version 2 Self-Review, amendment 5, hard-subjects 7): fixed dam-as-actor, anaphora (Guardsmen x2, "point to" x4), unsupported "most/much/last", derived 90-percent math, split 5 sentences over 30 words (avg 14 words), defined shares, fraud, truce flag, bottomlands, phlegm, conspiring, supervised release, autopsy, civilian, Allies. Final: part3 6724w, validator 0 errors, --punct 0/0, PASS energy / prose.
- 2026-09-29 T-302b: era 10 written. part3 has 6630 words. validator 0 errors. --punct emdash=0 semicolon=0. PATCH: era 10 (fracking defined, EPA; Oklahoma quakes, USGS 2017; Dakota Access dates, Harvard EELP; TMI-1 restart, WITF 2026).
- 2026-09-29 T-302b: era 09 written. 4458 words in file. validator 0 errors. --punct emdash=0 semicolon=0. PATCH: era 09 (how a nuclear plant works, EIA; Watts Bar 2 correction).
- 2026-09-29 T-302b: era 08 written, part3 created. 2425 words in file. validator 0 errors. --punct emdash=0 semicolon=0. PATCHes: era 08 (Spindletop driller/land, Insull and the 1935 act, what was done to the Osage from FBI/OHS pages recorded in the crime-justice bank).
- 2026-09-29 T-302a: era 07 written. part2 complete. Self-review (Version 2 Self-Review, amendment 5, hard-subjects 7) run on both files: fixed personification (coal, drill, station, story, law), metadiscourse in Edison story, unsourced glosses (conductor, iron pipe, Constitution, 20 miles, GE origin, shiny, hills), duplicate claims, era-opening shapes (eras 02/03). Final: part1 3768w, part2 3620w, validator 0 errors both, --punct emdash=0 semicolon=0 both.
- 2026-09-29 T-302a: era 06 written to part2. 1173 words in file. validator 0 errors. --punct emdash=0 semicolon=0.
- 2026-09-29 T-302a: era 05 written. part1 complete, 3795 words. validator 0 errors. --punct emdash=0 semicolon=0.
- 2026-09-29 T-302a: era 04 written. 2450 words in file. validator 0 errors. --punct emdash=0 semicolon=0.
- 2026-09-29 T-302a: era 03 written. 1868 words in file. validator 0 errors. --punct emdash=0 semicolon=0.
- 2026-09-29 T-302a: eras 01-02 written to part1. 854 words in file. validator 0 errors. --punct emdash=0 semicolon=0.
