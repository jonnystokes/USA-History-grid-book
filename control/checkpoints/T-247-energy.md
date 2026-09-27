# CHECKPOINT T-247 | energy | patch + bank check | eras 1-10

STATUS: DONE (director verified: patch PASS, research PASS, after T-247b)
VERIFY: python tools/project_state.py --check energy --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/energy.md · research/research-energy.md · workspace/energy.md

NOW:    done
NEXT:   T-247b: Unit 1 continues. Chadbourne is DONE in the bank (PATCH era 03) but the outline story
        is still status="candidate": flip it after checking the PATCH. Then the collier/furnace target,
        using the pages below, then the other three slots.

## Measured before dispatch (2026-09-27)

FAIL patch: stories=11 (6 verified, 2 candidate, 3 target), 0 [VERIFY], bank 4,646w against
outline 4,187w (barely above the size bar, and thin for the chapter), validator 0 errors.
Before 1500 and the 1500s have no story (allowed). Gate blockers:

- line 54  `william-chadbourne` (candidate)
- line 74  `target-collier-or-furnace-worker` (target)
- line 190 `pearl-yates` (candidate)
- line 216 `target-1973-gas-line-account` (target, a documented 1973-74 gas-line voice)
- line 251 `target-lineworker-or-solar-installer` (target, a lineworker, solar installer, or a
  household through Winter Storm Uri, Texas, February 2021)

Each target must become a real, named, documented person whose story the bank sources, or be
handled honestly (never invent a name; an unnamed documented account becomes hb-zoom prose, and
the hb-story block is removed). Replace a `target-...` slug with the person's own slug. Keep
slugs unique across the book.

The bank already has three parked sections (from home-family twice, and from technology). Use
what serves this chapter. Two of them are marked "kept verbatim": leave their text alone.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | the two candidates and the three targets | done | chadbourne, pearl-yates verified; collier -> era04 SNF + lafayette-houck (era07); david-falconer (era09); cristian-pavon-pineda (era10) |
| 2 | bank check, eras 1-5 | done | Onate land (era02), Baltimore/Hopewell/Catoctin labor (04-05) |
| 3 | bank check, eras 6-10 | done | Avondale, Monongah, Ludlow, coal totals, TVA/Grand Coulee, Osage ptr, TMI cause, Farmington+black lung, Garrison, uranium/Church Rock ptr, UBB, Dakota Access ptr, 2025 EIA refresh |
| 4 | final: flags, validator, both checks | done | 10/10 researched, validator 0 errors |

## SUBJECT NOTES (from the director)

Registry angle: energy, the fuels and power themselves: wood, charcoal, water, coal, oil, gas,
electricity, nuclear, renewables. Check the registry for the exact line and the neighbours
(`technology` for machines, `land-environment` for damage to the land, `work-workers` for
working conditions, `disasters` for disasters as events).

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the bank):
who cut the wood and made the charcoal (enslaved and bound labor) · coal mining deaths and the
companies and officials responsible (Monongah 1907, the Ludlow killings 1914 as far as this
chapter's angle reaches, black lung) · whose land coal, oil and uranium came from (Osage oil
and the murders, Navajo uranium: check `elements` and `native-nations` banks before re-researching)
· dams that flooded Native land (who decided, how many people moved) · Three Mile Island and
the 2021 Texas freeze (who ran the grid, deaths with sources, ranges) · pipelines and
protests (Dakota Access) with dated facts.

Perishable: every 2000-today figure (energy mix, renewables share, prices, nuclear restarts and
small modular reactors, EV numbers). Date each figure and refresh to 2026 where a newer official
figure exists (EIA is the default source).

## SALVAGE 2026-09-27 (first agent killed when Jon's app restarted)

Landed (measured with git diff): one bank PATCH under era 03, "William Chadbourne confirmed, and
whose land the mills stood on" (Old Berwick Historical Society, James Wall's 1652 deposition,
Abenaki land). The outline was NOT changed: `william-chadbourne` is still `candidate`.
Stopped at: researching the collier or furnace worker (Hopewell Furnace, Catoctin Furnace).
Nothing from those pages was written. Do not redo the Chadbourne research.

Pages the killed agent fetched (re-read the useful ones rather than searching again):
- https://catoctinfurnace.org/history/
- https://www.sciencehistory.org/stories/magazine/o
- https://bioethicsarchive.georgetown.edu/achre/final/chap12_2.html
- https://semspub.epa.gov/work/06/1000720.pdf
- https://www.wikitree.com/wiki/Chadbourne-4
- https://freepages.rootsweb.com/~dearle/genealogy/CHADBOURNE.html
- https://en.wikipedia.org/wiki/Great_Works_River
- https://www.findagrave.com/memorial/46651181/william-chadbourne
- http://freepages.rootsweb.com/~mainegenie/genealogy/SPENCER.htm
- https://www.oldberwick.org/history-articles/trades-occupations/timeline-of-the-great-works-mills.html
- https://www.oldberwick.org/history-articles/trades-occupations/great-works.html
- http://www.brazoriaroots.com/p8422.htm
- http://chadbourne.org/Genealogy.html
- http://freepages.rootsweb.com/~mainegenie/genealogy/CDBRN.htm
- https://en.wikipedia.org/wiki/South_Berwick,_Maine
- https://accessgenealogy.com/new-hampshire/new-hampshire-indian-tribes.htm
- https://www.oldberwick.org/history-articles/people/17th-century/south-berwicks-first-people.html
- https://micummcintireclanassociation.org/native-americans-in-maine-mcintire-settlement/
- https://en.wikipedia.org/wiki/Berwick,_Maine
- https://www.berwickmaine.gov/community/berwick_historical_society/native_americans.php
- http://mynewenglandancestors.blogspot.com/2016/08/they-came-to-stay.html
- https://www.trashpaddler.com/2015/05/to-newichawannock-and-falls.html
- https://www.nps.gov/sair/learn/news/landscapes-of-indenture.htm
- https://www.nps.gov/articles/000/scottish-prisoners-at-the-iron-works.htm
- https://www.virtualjamestown.org/phatmass.html
- https://www.dhr.virginia.gov/historic-registers/020-0063/
- https://www.nps.gov/articles/settlejames.htm
- https://www.durham.ac.uk/departments/academic/archaeology/research/archaeology-research-projects/scottish-soldiers/
- https://spows.org/battle-of-dunbar/battle-of-dunbar-prisoners-of-war/
- https://www.mountclare.org/historic-site/industry/baltimore-iron-works
- http://www.heritage.umd.edu/chrsweb/associatedprojects/chidesterreport/chapter%20v.htm
- https://news.maryland.gov/dnr/2026/02/28/historic-african-american-cemetery-of-enslaved-catoctin-furnace-workers-becomes-part-of-cunningham-falls-state-park/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10958645/
- https://npgallery.nps.gov/Areas/HOFU/Content/data/HOFU_books_BrianSchmult.pdf
- http://home.nps.gov/articles/hopewell-furnace-a-pennsylvania-iron-making-plantation-teaching-with-historic-places.htm
- https://www.nps.gov/articles/hopewell-furnace-a-pennsylvania-iron-making-plantation-teaching-with-historic-places.htm
- https://www.nps.gov/parkhistory/online_books/hofu/adhi.pdf
- https://www.nationalparkstraveler.org/2015/06/art-making-charcoal-hopewell-furnace-national-historic-site26699
- https://www.bctv.org/2017/04/03/friends-of-hopewell-furnace-to-demonstrate-access-to-hopewell-furnace-account-books-ccc-records/
- https://www.nps.gov/hofu/learn/historyculture/charcoal-making.htm
- https://www.nps.gov/hofu/learn/historyculture/collections.htm
- https://npgallery.nps.gov/HOFU/About
- https://dnr.maryland.gov/publiclands/pages/western/cunninghamfalls/catoctin-furnace.aspx
- https://www.hmdb.org/m.asp?m=104641
- https://decorativeartstrust.org/rock-ford-article/
- http://www.heritage.umd.edu/chrsweb/associatedprojects/chidesterreport/Chapter%20VII.htm
- https://en.wikipedia.org/wiki/History_of_the_iron_and_steel_industry_in_the_United_States
- https://en.wikipedia.org/wiki/Richard_Snowden_(ironmaster
- https://encyclopediavirginia.org/entries/runaway-slaves-and-servants-in-colonial-virginia/
- https://paparksandforests.org/black-history-charcoal-and-state-lands/

## Sources in hand
- OBHS Great Works + timeline (Chadbourne) · NPS Hopewell: charcoal-making, charcoal, prominent-families, African Americans at Hopewell, TwHP lesson, Cuff Dix · CFHS Catoctin history · PMC10958645 (Catoctin Science paper) · Mount Clare (Baltimore Iron Works)
- UNC SOHP catalog D-0044 (Pearl Yates) · HISTORY.com Blakemore 2018
- Yale Energy History Falconer gallery · NARA Flickr 412-DA-5686 · NBC26 2022
- Texas Tribune, CBS, Al Dia, Patch (Pineda)
- MSHA coal fatalities table + disasters fact sheet + 1969 Act page + UBB page · Clio + WV Mine Wars Museum (Monongah) · EARTH Magazine (Avondale) · Colorado Encyclopedia (Ludlow) · Smithsonian Mag 2017 (black lung) · NPR 2016 (Blankenship)
- Facing South 1995 (TVA removals) · HistoryLink 7577 (Kettle Falls) · Cultural Survival 2010 + ND Studies (Garrison) · Allegheny Front (Kinzua) · NPS San Gabriel del Yunque · WNA (TMI)
- EIA electricity-in-the-US, TIE 67144, 67844, 67724 · Canary Media July 2026 (Palisades)

## Gaps researched

## OPEN (should be rare)

## Outline claims left out
- Outline's older em dashes (73) and semicolons (95) untouched: audit/polish work, not patch.
- "Oregon first with odd-even" kept only as Falconer's caption claim.

## Decisions and defects fixed
- Collier story moved from era 04 to era 07 (Lafayette Houck); era 04 has no named collier (SNF).
- Pearl Yates occupation corrected to teacher (UNC catalog).
- Pineda cause of death: carbon monoxide (autopsy), not hypothermia.
- 2018 crude: US overtook Russia (EIA), outline had "passed Saudi Arabia": fixed.
- Hopewell cords: two NPS figures (5,000-6,000 and 6,000-7,000): outline now 5,000-7,000.

## Log
- T-247b 2026-09-27: william-chadbourne -> verified (outline rewritten from the T-247 PATCH, whose land added). Collier target: no named collier 1700-1750 exists in the sources -> era 04 story block REMOVED, SEARCHED NOT FOUND in bank era 04, Baltimore Iron Works enslaved charcoal hauling added (era 04 PATCH + span). Era 05 PATCH: charcoal method, Hopewell cords correction (5,000-7,000), Mark Bird enslaved 18 (1780), Collier Sam at Catoctin, Cuff Dix (parked note). Era 07 PATCH + new span + new story `lafayette-houck` (verified, NPS; birth-year dispute recorded). Validator 0 errors.
- T-247b: pearl-yates -> verified from UNC catalog D-0044 (May 29, 1984, Bonnie Bishop; Haywood County; she was a TEACHER, HISTORY.com said farmer's wife: correction in bank). Gas-line target -> `david-falconer` (EPA DOCUMERICA photographer, NARA captions via Yale Energy History) + SEARCHED NOT FOUND for a contemporaneously quoted named driver. 2021 target -> `cristian-pavon-pineda` (Conroe, died Feb 16 2021; autopsy = carbon monoxide, not hypothermia; $100M suit vs ERCOT/Entergy; outcome not found).
