# CHECKPOINT T-248 | transportation | patch + bank check | eras 1-10

STATUS: DONE (director verified: patch PASS, research PASS)
VERIFY: python tools/project_state.py --check transportation --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/transportation.md · research/research-transportation.md · workspace/transportation.md

NOW:    finished
NEXT:   director: commit; note pypdf was pip-installed by the agent.

## Measured before dispatch (2026-09-27)

FAIL patch: stories=17 (16 verified, 0 candidate, 1 target), 0 [VERIFY], bank 4,764w against
outline 4,511w (barely above the size bar, and thin for 17 stories), validator 0 errors.
Before 1500 and the 1500s have no story (allowed). Gate blocker:

- line 275 `ride-hail-driver` (target, 2000-today): a real, named, documented ride-hail driver
  whose story the bank sources, or handle it honestly (never invent a name; an unnamed documented
  account becomes hb-zoom prose, and the hb-story block is removed). Keep slugs unique across the
  book (ignore `outlines/BOOK-OUTLINE.md`, a compiled copy).

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | the target story | done | ride-hail-driver target replaced by verified `barbara-berwick` (primary source: Labor Commissioner decision 11-46739 EK); Prop 22 + Mass. settlement bullet added to era-10 span; bank PATCH + SEARCHED NOT FOUND (appeal outcome); parked to work-workers |
| 2 | check that each of the 16 verified stories' key facts are in the bank; source any that are not | done | 12 stories fully in bank. Patched: Fulton (New Orleans 1811, 69 boats by 1820; "every major river" flagged too broad), Vanderbilt (1810 periauger, disputed money), Sprague (75%->1% animal power 1890-1902; earlier electric lines, "first" check), Wright (cross-sourced from technology bank), Dusty Roads (Ideastream interview in her words) |
| 3 | bank check, eras 1-5 | done | era1 no harms (trails already name nations). era2 Seloy/Timucua land + 800 vs 1,500 count. era3 Pequot/Narragansett/Nipmuc paths under the Post Road. era4 Great Warriors Path + 1744 Lancaster treaty; Virginia road duty (tithables) + SNF on enslaved road-crew counts; Conestoga people + Paxton killings 1763 (native-nations lead). era5 turnpike investors/Bingham/12,000 mi by 1830s + SNF on the workers. Scratch texts in scratchpad e2-e5.md |
| 4 | bank check, eras 6-10 | done | era6 DONE: Erie labor/pay/1819 malaria (1,000 SICK per Commissioners, not 1,000 dead) from NPS Svejda 1969; Haudenosaunee land + Clinton 1811 quote; Dismal Swamp enslaved diggers; Southern railroads 85/113, ~15,000 in 1860; NEW verified story `moses-grandy` (1843 narrative, overseer Wiley M'Pherson); outline span + railroad bullet added. era7 DONE: CP deaths "50 to 1,200, no count" (outline line rewritten), pay $35 vs $42+housing, 1862 act 6,400 acres + $48k/mi + extinguish-title clause, ~130M acres, nations (Utah Spike 150 page), Sand Creek/Julesburg/Plum Creek, Aldrich trainmen death rates, Wells 1884 + Plessy 1892/1896 (cross-sourced from rights-movements). era8 DONE: NEW verified story `irene-morgan` (Encyclopedia Virginia), car deaths 1913/1937 two series. era9 DONE: DOT 475k households/1M people, Engelhardt I-85 Montgomery 356 homes, Freedom Rides (Encyc. Alabama: Connor 15 min, Bergman, Seigenthaler, ICC 9/22-11/1/1961), 1972 peak 54,589, 1956 Grand Canyon 128 dead (FAA). era10 DONE: NHTSA 2025 est 36,640 (DOT HS 813 800), EV 7.8% 2025 + Q4 -46%, APTA 8.1B trips (summary only), CAHSR $4B cut Jul 2025 / suit dropped Dec 2025 / $1B/yr cap-and-trade, ARTBA/NBI 41,677 poor of 624,167, Key Bridge 6 named dead + NTSB + May 2026 indictment, Potomac 67 dead + NTSB Jan 2026. Outline era-10 bullets updated. |
| 5 | final: flags, validator, both checks | done | all 10 eras progress=researched; validator 0 errors; PASS patch and PASS research (19 stories v19, bank 13,064w vs outline 6,684w) |

## SUBJECT NOTES (from the director)

Registry angle: how people and goods move: trails, roads, canals, rail, cars, planes, the
vehicles and systems. Not: the people migrating (`migration`), engine science (`science`),
fuels (`energy`).

The bank is thin for 17 verified stories. A story marked verified whose facts are not in the bank
is a defect the gate does not catch. Source it or report it.

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the bank): who
built the roads, canals and railroads (enslaved labor on Southern canals and railroads, Irish and
Chinese workers, deaths on the Erie Canal and the transcontinental line with sourced ranges) ·
whose land the railroads crossed and the land grants (who granted them, how many acres) · the
Chinese workers' pay and the 1867 strike · segregated travel (Plessy, the Freedom Riders and who
attacked them, as this chapter's angle allows; `rights-movements` leads the movement) · highways
built through Black neighborhoods (who chose the routes, how many people displaced) · crashes
and deaths (railroad, car, air) with dated official figures · 2000-today: gig-work driver pay and
the lawsuits, with dated figures.

Perishable: every 2000-today figure (traffic deaths, EV sales, transit ridership, ride-hail
numbers, CAHSR and FHWA figures). Date each figure and refresh to 2026 where a newer official
figure exists.

## Sources in hand
- Berwick decision PDF: http://cdn.arstechnica.net/wp-content/uploads/2015/06/04954780-Page0-20.pdf (read in full; settles all Berwick facts)
- Ballotpedia Prop 22 page (results, finance, Castellanos case); WBUR 2024-06-27 (Mass. settlement); TIME + TechCrunch 2015-06-17

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

## Log
- 2026-09-27 Unit 5 done. Both checks PASS.
- 2026-09-27 Unit 4 era 6 landed (bank + outline). Note: agent pip-installed pypdf (user Python) to read NPS PDF.
- 2026-09-27 Unit 3 done (bank only, outline untouched for eras 1-5).
- 2026-09-27 Unit 2 done.
- 2026-09-27 Unit 1 done. Validator 0 errors, 17 stories.
