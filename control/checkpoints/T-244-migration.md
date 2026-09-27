# CHECKPOINT T-244 | migration | patch + bank check | eras 1-10

STATUS: DONE (director verified: patch PASS, research PASS)
VERIFY: python tools/project_state.py --check migration --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/migration.md · research/research-migration.md · workspace/migration.md

NOW:    finished.
NEXT:   director: verify with both checks and commit.

## Measured before dispatch (2026-09-26)

FAIL patch and research: stories=15 (14 verified, 0 candidate, 1 target), 0 [VERIFY], bank 9,871w
against outline 3,298w, validator 0 errors. The ONLY gate blocker is the target story
`recent-mover` (outline line 207, era 10). Eras 1700-1750 and before-1500 have no story (that is
allowed, not a gate item). Every era is already `progress="researched"`.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | era 10: fill `recent-mover` with a documented, named recent mover (or convert it honestly, see the brief) | done | target replaced by `kimberly-rivers-roberts` (verified, movie Trouble the Water 2008). Bank PATCH in section 10. Patch check PASSES. |
| 2 | bank check, eras 1-5 | done | PATCH: Oñate "first" corrected (Luna 1559, St. Augustine 1565); Hartford land (Sequassen, Suckiaug deed); Tuscarora War actors and counts (Moore, Neoheroka 950); Shenandoah land (Shawnee, Lancaster 1744); Acadian order (Lawrence, Winslow, Monckton); Kentucky land (Sycamore Shoals, Henderson, Dragging Canoe). 1 SEARCHED NOT FOUND (enslaved people in Oñate column). Era 1: no gaps (no harms with actors in the bank). |
| 3 | bank check, eras 6-10 | done | PATCH: Cherokee removal actors (Scott, 7,000 troops, Ross detachments) and death range 1,000 to 8,000+; Choctaw/Creek/Chickasaw counts; Franklin & Armfield; trade-vs-owner share 16-70%; Long Walk (Carleton, Carson, Ute scouts); California Native loss (Madley); Great Migration push, obstruction (Macon $25,000), Defender, Chicago 1919; bum blockade (Chief Davis); EO 9066 movement facts; Gretna bridge; Houston evacuees; Vintage 2025 figures. 1 SEARCHED NOT FOUND (Gretna count). |
| 4 | final: flags, validator, both checks | done | validator 0 errors; patch PASS; research PASS; all eras progress=researched. |

## SUBJECT NOTES (from the director)

Registry angle: people moving and being moved across the land once here: Native movements, the
trails, forced removals, the Great Migration, the Sun Belt. Not: who found the routes
(`exploration`), arrival from abroad (`immigration`), city growth (`city-building`). Workspace
ruling: the domestic slave trade is told here as a forced journey (routes, coffles, ships,
numbers, conditions), with `slavery-freedom` leading on the system.

Hard subjects the bank check should test for actor, act, count and cause (check the bank first,
these are prompts, not claims): forced removals of Native nations and who carried them out
(officers, troops, contractors) with death counts and their ranges · the domestic slave trade as
a journey (traders by name where recorded, routes, numbers) · the violence and laws that drove
the Great Migration, and how migrants were met in Northern cities · Dust Bowl migrants turned back
at the California line in 1936 (who ordered the "bum blockade") · the forced removal of Japanese
Americans in 1942 as a movement (check which chapter owns it in the registry and park if not
this one) · displacement after Hurricane Katrina, 2005 · land: whose land each trail and
settlement crossed.

Perishable: anything in era 10 with a figure (Sun Belt moves, census numbers). Date every figure
and refresh to 2026 where a newer official figure exists.

## Sources in hand
- tcm.com/articles/383009 (Roberts: Lower Ninth Ward, $20 camcorder, attic, Red Cross shelter, uncle's trailer, Memphis, return, film awards)
- americamagazine.org 2025-08-22 (attic, 911, punching bag, Navy base at gunpoint + Navy denial, grandmother died)
- popmatters.com/73507 (car stolen, Alexandria shelter, Memphis cousin, FEMA check, Uncle Ned)
- democracynow.org 2008-08-22 (quotes, ~500 empty rooms at naval facility)
- independent.com 2008-11-20 (Memphis "briefly", returned). Bay State Banner 2008-09-10 (six months, no diplomas) seen only via search summary (403).

## Gaps researched

## OPEN (should be rare)

## Outline claims left out
- None removed. Oñate "first" narrowed to "first overland" (bank correction). Era 10 Texas/Florida "each up about 500,000 from other states in 2023-24" replaced with Census Vintage 2025 figures (bank correction note: the old figure looks like total growth).

## Decisions and defects fixed
- Target story replaced by a verified named mover. Outline era-10 and era-8 spans updated (Gretna bridge, Houston, bum blockade actor).
- Japanese American removal: rights-movements leads (its workspace); movement facts recorded in this bank only, not added to the outline.
- Weak points flagged in bank: Bay State Banner six-months claim seen only via search summary; New Orleans 2025 city figure via third-party site; Tadman 60-70% via search summary; Treaty of Lancaster payment unconfirmed.

## Log
- 2026-09-26 T-244: units 1-4 done.
