# CHECKPOINT T-310 | marketplace | prose | ONE writer, all 10 eras (part1, part2, part3)

STATUS: T-310 landed (director verified: PASS  marketplace / prose)
VERIFY: python tools/project_state.py --check marketplace --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/marketplace/part1-before-1800.md (eras 1-5) · manuscript/marketplace/part2-1800s.md (eras 6-7)
        · manuscript/marketplace/part3-1900s-and-today.md (eras 8-10) · research/research-marketplace.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    done. Director: commit.
NEXT:   director commit; audit step later

## Research state before writing (2026-09-29)

PASS  marketplace / research
measured: stage=RESEARCHED eras=10/10 stories=17 (v17 c0 t0) verify_tags=0 bank=16320w outline=10386w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-310 | done | 560w, 0 errors, 0/0 |
| 2 | era 02 1500s -> part1 | T-310 | done | 360w, 0 errors, 0/0 |
| 3 | era 03 1600s -> part1 | T-310 | done | 1023w, 0 errors, 0/0 |
| 4 | era 04 1700-1750 -> part1 | T-310 | done | 877w, 0 errors, 0/0 |
| 5 | era 05 1750-1800 -> part1 | T-310 | done | 1164w, 0 errors, 0/0 |
| 6 | era 06 1800-1850 -> part2 | T-310 | done | 1196w, 0 errors, 0/0 |
| 7 | era 07 1850-1900 -> part2 | T-310 | done | 2228w, 0 errors, 0/0 |
| 8 | era 08 1900-1950 -> part3 | T-310 | done | 2230w, 0 errors, 0/0 |
| 9 | era 09 1950-2000 -> part3 | T-310 | done | 1834w, 0 errors, 0/0 |
| 10 | era 10 2000-today -> part3 | T-310 | done | 1963w, 0 errors, 0/0 |
| 11 | final: self-review, --punct, validator, prose check | T-310 | done | 13548w total, 0 errors x3, 0/0 x3, prose PASS |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 02 | who the Basques were, and which nations traded with them | PATCH | "PATCH 2026-09-29 (T-310): who the Basques were..."
- 03 | whose land Aptucxet stood on | PATCH | "PATCH 2026-09-29 (T-310): whose land Aptucxet stood on"
- 05 | spinning-meeting details, Harvard seniors (parked from styles) | PATCH | "PATCH 2026-09-29 (T-310): spinning-meeting details..."
- 06 | who sold Joice Heth to Barnum, who cut open her body, how many watched | PATCH | "PATCH 2026-09-29 (T-310): who sold Joice Heth..."
- 07 | what morphine does to a child's body (clinical-word rule) | PATCH | "PATCH 2026-09-29 (T-310): what morphine does..."
- 07 | Singer installment buying 1856 (parked from styles) | PATCH | "PATCH 2026-09-29 (T-310): buying on installments..."
- 08 | the miners' side of the company store | PATCH | "PATCH 2026-09-29 (T-310): the miners' side..."
- 10 | FTC v. Epic Games (parked from sports-play) | PATCH | "PATCH 2026-09-29 (T-310): selling to children inside a game..."
- 10 | Coresight 2025 closures, confirming an unconfirmed line | PATCH | "PATCH 2026-09-29 (T-310): Coresight's 2025 store count..."
Totals: 9 PATCH, 0 new SEARCHED, NOT FOUND (the two T-253 SEARCHED, NOT FOUND entries were used as written: Wall Street market buyers, Mrs. Winslow deaths).

## OPEN (should be rare)
None.

## Outline claims left out
Each is absent from the bank, or is analysis the bank does not support. 20 in all.
- 04: Samuel Keimer as Franklin's "former employer". The Gazette ad categories ships, land, books, cloth.
- 05: the storekeeper's "considerable power over the neighborhood".
- 06: "roads, canals, and factories" as the cause of peddling. The peddler "carried news" and was "welcomed and distrusted". Barnum "proved the advertisement was what people paid for".
- 07: brand names and printed packages. "City prices" by mail. The guarantee "made mail order possible". Woolworth's "goods out where customers could handle them".
- 08: self-service "cut clerks and let prices fall". Saunders's short sellers "could not buy shares". "An extra charge for the privilege" of installments. Coffee and tires on the ration list, "from 1942".
- 09: Southdale enclosed because of Minnesota weather. Malls drew customers from downtown. Discount stores' "plain buildings with wide aisles". Franchising spread to motels, gas stations and haircuts. The barcode as the start of online tracking.
- 10: the phone as "catalog, store and wallet". Green Street's 1,000 malls (no year).
Also not used: parked Betamax/VHS (era 09) and box-office/Netflix (era 10) items, which are about media rather than the store. Frozen-food retailing 1930.

## Decisions and defects fixed
- era 01: outline drops "captives" from the bank's list of goods traded at The Dalles (softening by omission). Prose states captives were traded. Outline says "nothing carried a price", which contradicts the bank's dentalium-as-measure-of-value line. Prose drops the claim.
- era 06: outline and bank say only that a 'public autopsy' found Heth was about 80, which hides who cut open her body and that Barnum sold tickets to it. Researched and named: Dr. David L. Rogers, 1,500 paying spectators at 50 cents.
- era 07: outline says mail order, brand names and installment buying 'all started' 1850-1900, but Lyon (1958) says furniture and clock makers sold on installments before Singer in 1856. Prose says Singer's company was the first selling nationally that way.
- era 08: outline states 'Miners remembered store debt they could not escape' but the bank says no account was sourced. Prose attributes the debt-bondage view to the West Virginia Mine Wars Museum (PATCH) and sets it against Fishback's measurements. Outline's ration list (coffee, tires, 'from 1942') is not in the bank. Prose uses only the banked goods.
- era 09: outline claims not in the bank were dropped: Southdale's enclosure as a response to Minnesota weather, malls draining downtown shops, the discount stores' 'plain buildings with wide aisles', franchising spreading to motels and haircuts, and the barcode as 'the beginning of the tracking'. Gruen's 1978 quote paraphrased without the rude word, as the bank directs.
- era 10: the bank's Green Street count of about 1,000 malls has no year. Dropped under the rule that every 2000-today figure carries its year. Coresight's 15,000 forecast for 2025 is reported with the actual 2025 count (8,270 closings), so the forecast is not left standing as if it came true.

## TO PARK (FILED by the director, 2026-09-27)
- `slavery-freedom` and `health`: Joice Heth's public dissection, February 25, 1836, City Saloon, New York, by Dr. David L. Rogers, 1,500 people at 50 cents each; R. W. Lindsay of Kentucky sold Barnum possession of her (CUNY Lost Museum Archive, New York Sun 1836). Full text in research-marketplace.md, era 06 PATCH (T-310).
- `economy` and `native-nations`: Basque crews traded with the Beothuk, Innu and Mi'kmaq, and Basque kettles and axes reached Huron and other Iroquoian lands in Ontario (Canadian Museum of History). Full text in research-marketplace.md, era 02 PATCH (T-310).
- `work-workers` and `money`: West Virginia Mine Wars Museum's "debt bondage" description of scrip. research-marketplace.md, era 08 PATCH (T-310).
- `research-marketplace.md` housekeeping for the audit: the T-253 Coresight line (era 10) still carries "(unconfirmed: search summary only)"; the T-310 PATCH below it confirms it on a readable page.

## Log
- 2026-09-29 era 01 before-1500: 560 words, validator 0 errors, --punct emdash=0 semicolon=0. No research needed.
- 2026-09-29 era 02 1500s: 360 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH: Basques and the nations they traded with (Canadian Museum of History).
- 2026-09-29 era 03 1600s: 1023 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH: Aptucxet on Wampanoag land (Bourne Historical Society). Agawam deed from existing T-253 PATCH used for the land.
- 2026-09-29 era 04 1700-1750: 877 words, validator 0 errors, --punct emdash=0 semicolon=0. No research needed. Order made chronological: consumer revolution, Wall Street market 1711, advertising 1729 + Franklin, Murray 1749.
- 2026-09-29 era 05 1750-1800: 1164 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH: spinning details and Harvard seniors filed from the parked styles item. Part 1 self-review run: fixed a copular slogan (ledger), a metaphor (shopping as a weapon), newspapers as actors, repeated era-opening shapes.
- 2026-09-29 era 06 1800-1850: 1196 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH: Joice Heth sold by R. W. Lindsay; dissection by Dr. David L. Rogers, City Saloon, Feb 25 1836, 1,500 at 50 cents (CUNY Lost Museum, New York Sun 1836). Order made chronological: peddlers/Guild 1818, Barnum 1835, museum 1841-42, Stewart 1846.
- 2026-09-29 era 07 1850-1900: 2228 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH: morphine's effect on breathing (MedlinePlus); Singer installment buying 1856 (Lyon, American Heritage 1958, filed from the parked styles item). Part 2 self-review run: removed unsourced 'city prices', 'brand names', the risk analysis of the guarantee, institutional subjects.
- 2026-09-29 era 08 1900-1950: about 2230 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH: miners' side of the company store (West Virginia Mine Wars Museum). Gerety slogan used from the era 07 bank line. Woolworth story told the 1911 merger and building only, since era 07 already tells Utica and Lancaster.
- 2026-09-29 era 09 1950-2000: 1834 words, validator 0 errors, --punct emdash=0 semicolon=0. No new research. Parked Betamax/VHS item not used (a storytelling-evolution subject, not the store counter).
- 2026-09-29 era 10 2000-today: 1963 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH: FTC v. Epic Games 2022 (filed from the parked sports-play item); Coresight 2025 closures confirmed on a readable page (MMCG Invest, April 2026). Every figure carries its year and a named source. Part 3 self-review run: companies as speakers and actors replaced by representatives and managers.
- 2026-09-29 final: validator 0 errors on all three files, --punct 0/0 on all three, --check marketplace --stage prose PASS (13,548 words, 17 stories verified).
