# CHECKPOINT T-251 | food-farming | patch + bank check | eras 1-10

STATUS: DONE (director verified: patch PASS, research PASS). TO PARK pending.
VERIFY: python tools/project_state.py --check food-farming --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/food-farming.md · research/research-food-farming.md · workspace/food-farming.md

NOW:    done.
NEXT:   director: commit; file TO PARK items.

## PARALLEL RUN (Jon, 2026-09-27): five agents at once

This agent runs at the same time as four others (T-251 to T-255, one chapter each). **Write only
your own chapter's three files and this checkpoint.** Do NOT edit any other chapter's outline,
research bank or workspace, even to park material there: another agent may be writing to it at
the same moment. Instead, list anything that belongs to another chapter under "TO PARK" below
(target chapter, era, the sourced text to add). The director files it after all five finish.
Reading other chapters' banks is fine.

## Measured before dispatch (2026-09-27)

FAIL patch: stories=18 (15 verified, 0 candidate, 3 target), bank 6,845w vs outline 4,895w, 0 [VERIFY], validator 0 errors. Gate blockers:

- line 80 `lowcountry-rice-grower` (target): a Lowcountry rice grower. Rice was grown by enslaved Africans whose knowledge built it: a named, documented enslaved person is the strongest fit if the record has one.
- line 99 `farm-household-daybook` (target): a documented farm household (a diary or daybook).
- line 184 `ration-book-household` (target, 1900-1950): a ration-book or victory-garden household. `marketplace` also has a rationing target (`ration-book-shopper`): pick a different person from whoever T-253 uses, and tell it from the food and garden angle.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | the open story slots | done | patten (1750-1800), adelaide-wisdom-benjamin (1900-1950) verified; lowcountry-rice-grower removed -> span zoom + SEARCHED, NOT FOUND. Patch gate PASS. |
| 2 | check that each verified story's key facts are in the bank; source any that are not | done | Tudor corrected (180 tons shipped, ~100 arrived; 1806 loss); Steele 'cheapest meat' replaced with NCC per-capita figures. Other stories' facts already in bank. |
| 3 | bank check, eras 1-5 | done | PATCHes: De Soto/Anhaica corn (era 2 end); Percy 1610 Paspahegh + 1622-32 corn destruction; Cornhill corn taken Nov 1620 + repaid 1621; Winslow fish-manure quote; Jefferson 620+ enslaved + Monticello rations; Pinckney 20 enslaved; rice exports/task/land (Kiawah, Etiwan, Stono). |
| 4 | bank check, eras 6-10 | done | PATCHes eras 06-10 (see workspace list); SEARCHED, NOT FOUND for Fillmore County nation; outline got short hard-subject bullets in 1600s, 1750-1800, 1900-1950, 1950-2000, 2000-today. |
| 5 | final: flags, validator, both checks | done | all 10 eras progress=researched; validator 0 errors; patch PASS; research PASS. |

## SUBJECT NOTES (from the director)

Registry angle: what Americans ate and how they grew it. Not: farm machinery as invention (`technology`), farm economics (`economy`). Hard subjects (prompts; check the bank): who did the farm work (enslaved people, sharecroppers, braceros, migrant workers, children), with actors, pay and deaths · land taken for farms and whose it was · famine and hunger (the Dust Bowl, hunger counts today) · pesticides and the people poisoned · Black farmers' land loss and the USDA discrimination cases (Pigford) with dated figures.

Each open slot must become a real, named, documented person whose story the bank sources, or be
handled honestly (never invent a name; an unnamed documented account becomes hb-zoom prose, and
the hb-story block is removed). Before choosing a person, search `outlines/` and `manuscript/`
so no other chapter already tells them (ignore `outlines/BOOK-OUTLINE.md`, a compiled copy).
Keep slugs unique across the book.

Perishable: every 2000-today figure. Date each and refresh to 2026 where a newer official figure
exists.

## PARKED EARLIER (FILED by the director)
- `health`, era 1900-1950: pellagra. Science History Institute, "Joseph Goldberger's Filth Parties" (opened): 1900 to 1940, about 3 million US cases and 100,000 deaths; diet of cornmeal, molasses, dried pork; niacin identified 1937; WWII laws required niacin in bread. Rankin State Prison Farm, Mississippi, 1915: 11 prisoner volunteers fed a corn-based diet for pardons from Gov. Earl L. Brewer; 5 (Wikipedia) or 6 (Mississippi Encyclopedia, search summary) developed pellagra. Full text in research/research-food-farming.md era 08 PATCH.
- `work-workers`, era 2000-today: CDC MMWR 57(24), June 20, 2008: 68 crop workers died of heat 1992-2006; rate 0.39 per 100,000 vs 0.02 for all civilian workers; unnamed 56-year-old H-2A tobacco worker, North Carolina, July 2005, body temperature 108 F. And 29 U.S.C. 213(c)(1) (Cornell LII): farm child-labor exemptions (under 12 on parent's farm; 12-13 with parental consent; 14+ outside school hours).
- `rights-movements`, era 1900-1950: Japanese American farms. San Francisco News, March 4 and 9, 1942 (sfmuseum.org/hist9/harvest.html): FSA's Lawrence Hewes said 6,000 farms, about 200,000 acres registered; more than 1,000 farms (50,000 acres) transferred in March 1942; California Farm Bureau: 40 percent of state vegetables.
- `slavery-freedom`, eras 1700-1750 and 1750-1800: the Monticello weekly ration (Sawyer and Bowen, DAACS 2012, citing Stanton 2000: peck of cornmeal, half-pound pork or pickled beef, four salted fish); rice exports 268,602 lb/yr (1698-1702) to 30 million+ (1738-42) (SC Encyclopedia "Rice"); task normally a quarter acre (SC Encyclopedia "Slave Labor"); Africans landed at Charles Town 300/yr (1710), 1,000+/yr (1720), 3,000+/yr (1770) (LDHI "Africans in Carolina"). Also the SEARCHED, NOT FOUND on a named 1700-1750 rice grower, so they do not repeat the search.
- `native-nations`, eras 1500s and 1600s: Anhaica occupation Oct 1539 to Mar 1540 (Florida Division of Historical Resources); Cornhill seed corn and grave-opening, Nov 1620, and the Nauset repayment (Mourt's Relation, Gutenberg #66359, with line quotes in our bank); Kiawah/Etiwan/Stono and the 1684 cession (CCPL "First People of the South Carolina Lowcountry").
- `marketplace` (T-253): this chapter now tells Adelaide Wisdom Benjamin (slug adelaide-wisdom-benjamin) for its WWII garden/ration slot. If T-253 chose her too, one of the two must change.

## Sources in hand
- https://archive.org/details/diaryofmatthewpa00patt (Patten diary 1903 full text; 1767 food year)
- https://www.ww2online.org/view/adelaide-benjamin and nationalww2museum.org article (Benjamin oral history)
- NPS food rationing article (sugar 26 lb/yr, 64 red/48 blue points)
- CCPL Ten Things Lowcountry Rice; CCPL First People of the SC Lowcountry; SC Encyclopedia Rice and Slave Labor; LDHI Rice in the Lowcountry, Africans in Carolina, Jericho Plantation

## Gaps researched
- See workspace/food-farming.md 'Bank check 2026-09-27' list (every era).

## OPEN (should be rare)

## Outline claims left out
- 'Chicken ... the cheapest meat' (Steele) removed: unsourced. Replaced with NCC per-capita pounds.
- Tudor 'landed 180 tons ... still frozen' corrected: 180 tons shipped, about 100 arrived.

## Decisions and defects fixed
- Removed hb-story `lowcountry-rice-grower` (no named 1700-1750 rice grower in the record); collective telling now in span 'The rice workers, unnamed in the records'.
- DIRECTOR NOTE: T-253 (marketplace, ration-book-shopper) may also reach for National WWII Museum oral histories. This chapter now uses Adelaide Wisdom Benjamin (slug adelaide-wisdom-benjamin). Tell T-253's result to pick someone else, or check for a clash.

## Log
- Unit 1 done. Patch gate PASS (bank 9109w vs outline 5426w).
- Unit 1 part: farm-household slot -> Matthew Patten (Bedford NH day book, year 1767). Bank PATCH written under Era 05. Outline not yet edited. Source: https://archive.org/details/diaryofmatthewpa00patt (full text saved in scratchpad as patten.txt). Martha Ballard ruled out (home-family uses her).
