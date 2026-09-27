# CHECKPOINT T-253 | marketplace | patch + bank check | eras 1-10

STATUS: DONE (director verified: patch PASS, research PASS). TO PARK pending.
VERIFY: python tools/project_state.py --check marketplace --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/marketplace.md · research/research-marketplace.md · workspace/marketplace.md

NOW:    all units done.
NEXT:   director: run both checks, file TO PARK items, commit.

## PARALLEL RUN (Jon, 2026-09-27): five agents at once

This agent runs at the same time as four others (T-251 to T-255, one chapter each). **Write only
your own chapter's three files and this checkpoint.** Do NOT edit any other chapter's outline,
research bank or workspace, even to park material there: another agent may be writing to it at
the same moment. Instead, list anything that belongs to another chapter under "TO PARK" below
(target chapter, era, the sourced text to add). The director files it after all five finish.
Reading other chapters' banks is fine.

## Measured before dispatch (2026-09-27)

FAIL patch: stories=17 (14 verified, 0 candidate, 3 target), bank 7,596w vs outline 8,373w (the bank is SMALLER than the outline, so the gate fails on size too: grow the bank past the outline), 0 [VERIFY], validator 0 errors. Gate blockers:

- line 65 `documented-1600s-store-customer` (target): a customer named in a 1600s account book.
- line 253 `ration-book-shopper` (target, 1900-1950): a documented shopper under rationing. `food-farming` (T-251) has a ration-book household target at the same time: pick a different person, and tell it from the shopping angle.
- line 350 `delivery-worker-marketplace` (target, 2000-today): a documented last-mile delivery driver. Avoid Raef Lawson (`work-workers`) and Barbara Ann Berwick (`transportation`).

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | the open story slots | done | |
| 2 | check that each verified story's key facts are in the bank; source any that are not | done | |
| 3 | bank check, eras 1-5 | done | |
| 4 | bank check, eras 6-10 | done | |
| 5 | final: flags, validator, both checks | done | |

## SUBJECT NOTES (from the director)

Registry angle: buying and selling in daily life: stores, mail-order, malls, online shopping, advertising, credit, consumer culture. Not: money as a system (`money`), the macro economy (`economy`). This chapter has the largest outline of the patch group and a bank smaller than it: check that every verified story and every outline claim is in the bank. Hard subjects (prompts; check the bank): the slave trade as a market (auctions, advertisements for people, who sold) · stores that refused Black customers and the sit-ins (`rights-movements` leads the movement) · company stores and scrip · false advertising and patent medicines that harmed people · predatory credit · 2000-today: warehouse and delivery injuries, dated.

Each open slot must become a real, named, documented person whose story the bank sources, or be
handled honestly (never invent a name; an unnamed documented account becomes hb-zoom prose, and
the hb-story block is removed). Before choosing a person, search `outlines/` and `manuscript/`
so no other chapter already tells them (ignore `outlines/BOOK-OUTLINE.md`, a compiled copy).
Keep slugs unique across the book.

Perishable: every 2000-today figure. Date each and refresh to 2026 where a newer official figure
exists.

## TO PARK (for the director to file after the parallel run)
Each item's full sourced text is in `research/research-marketplace.md` under the PATCH named; copy it across.
- `slavery-freedom`, 1700-1750: Wall Street slave market, New York Common Council law of Nov 30, 1711, used to 1762; ~750 of ~5,000 New Yorkers enslaved in 1700 (WNYC, Apr 14, 2015). Bank PATCH "the market where people were sold".
- `slavery-freedom`, 1700-1750: Franklin's *Pennsylvania Gazette* printed at least 277 ads offering at least 308 enslaved people; the printer was middleman (Adam Smyth, *Smithsonian Magazine*, June 2024).
- `slavery-freedom` and `migration`, 1850-1900: the Weeping Time, Mar 2-3, 1859, Ten Broeck Race Course, Savannah; seller Pierce Mease Butler (gambling debts); broker Joseph Bryan; 429-436 people; $303,850; reporter Mortimer Thomson (NPS guge-weeping-time-2020; Southern Spaces, Feb 18, 2010).
- `health` and `drugs-alcohol`, 1850-1900: Mrs. Winslow's Soothing Syrup, from 1849 (Jeremiah Curtis, Benjamin A. Perkins), ~65 mg morphine per fl oz, AMA 1911 "baby killer," morphine removed after 1906 law, sold to 1930s (Canadian Museum of Health Care, July 28, 2017). SEARCHED NOT FOUND: death count.
- `government-politics` and `crime-justice`, 1750-1800: Christopher Seider shot Feb 22, 1770 by customs informer Ebenezer Richardson at Theophilus Lillie's shop; Richardson convicted of murder Apr 21, 1770, judges delayed sentence (Colonial Society of Mass., Hutchinson correspondence vol. 3; "Trial of Ebenezer Richardson").
- `work-workers`, 1900-1950: company stores and scrip (e-WV "Scrip" by Lou Athey: 1891 and 1925 WV laws, 10-30% discounts; EH.net "The Company Town": Coal Commission 1922, 4.2% / 7% markups, Fishback).
- `work-workers`, 2000-today: Renica Turner / Battle Tested Strategies union (Apr 2023, 84 drivers, Teamsters Local 396), Amazon ended contract Jun 2023, NLRB settlement (two weeks' pay, ~$250,000) approved by ALJ G. Rebekah Ramirez late May 2026 (NPR Jul 20, 2023; FreightWaves Apr 22 and Jun 3, 2026). Heat: Esteban Chavez Jr. (Jun 25, 2022, medical examiner: sudden cardiac dysfunction), José Cruz Rodriguez (Waco, Aug 2021, OSHA: heat illness), 40+ UPS drivers hospitalized since 2015, UPS-Teamsters AC deal for vans bought after Jan 1, 2024 (NPR). Senate HELP majority report Dec 16, 2024 (Amazon 30%+ more injuries than industry in 2023).
- `rights-movements` and `money`, 1950-2000: Equal Credit Opportunity Act Oct 1974 (sex, marital status), amended Mar 1976 (race, color, religion, national origin, age, public assistance) (CFPB blog).
- `native-nations`, before-1500 / 1950-2000: Celilo flooded Mar 10, 1957, 10 a.m. order, 4.5 hours, Wyam and S'kin villages, $26.8M settlement for Warm Springs, Yakama, Umatilla, Nez Perce, ~$3,700 per member (HistoryLink 10010).
- `money`, 2000-today: CFPB Apr 24, 2013 payday study (391% APR on $15 per $100, 199 days in debt median).

## Sources in hand
- colonialsociety.org/node/840 (Pynchon Papers II, sec. VIII): John Stewart's accounts. node/805: intro. spows.org John Stewart profile.
- oralhistory.rutgers.edu ... 423-lundberg-donald-e: Lundberg family rationing.
- npr.org 2023/07/20/1188282961: Renica Turner, Chavez, Rodriguez, UPS AC. freightwaves.com (Apr 22 and Jun 3, 2026): BTS settlement.
- vermonthistory.org/journal/misc/GuildJournalPt1.pdf (OCR layer usable): Guild pp. 249-253.
- smithsonianmag.com Franklin newsman (Smyth 2024); visualizingnyc.org Barnum; gutenberg 26640; chicagology rebuilding185; encyclopedia.com Ward and Sears; Duke Hartman guide; tennesseeencyclopedia Saunders; archive.austria.org Gruen; mnhs.org/mnopedia Southdale; repec Neumark 2008; iastate news 2012; nber w11809; historylink 23230 (Amazon), 10010 (Celilo).
- massmoments.org Pynchon deed; wnyc.org slave market 2015; colonialsociety Seider + Richardson trial; nps.gov guge-weeping-time-2020; southernspaces.org 2010 Weeping Time; museumofhealthcare.ca Winslow; wvencyclopedia.org/entries/190 scrip; eh.net company town; consumerfinance.gov ECOA blog + 2013 payday release; help.senate.gov Dec 16 2024; census.gov/retail/ecommerce.html (Q2 2026); bytebacklaw.com Jun 29 2026; newsroom.thredup.com 14th report; dealnews Prime.

## Gaps researched
See Log units 1-4 and the bank's addendum table at its end.

## OPEN (should be rare)
- Guild journal part 2 (account pages, later earnings) unread. Native commerce after 1900 (bank open item 7) not reached. Coresight 2025 count only from a search summary (report paywalled).

## Outline claims left out
- Removed as unsourced: Ward storekeepers-junk line, Wanamaker 'few lines', Sears 'not the goods but the writing', Gruen 'library/post office', Saunders 'none lasted', Bezos 'waiting a week felt broken', Guild door-knocking line. All replaced by sourced text (listed in workspace update).

## Decisions and defects fixed
- Mechanical punctuation pass: 0 em dashes, 0 semicolons in outline outside hb-note.
- 'more than five dollars in six' -> 'more than four in five' (17.1% online Q2 2026).
- Coresight 2025 forecast (15,000) superseded by actual count (8,270, search summary only).
- Old target slugs removed: documented-1600s-store-customer, ration-book-shopper, delivery-worker-marketplace.

## Log
- 2026-09-27 Unit 1a: 1600s slot filled: John Stewart, Springfield blacksmith, Dunbar POW, from Pynchon account books (Colonial Society of Mass. vol 61, node/840) + SPOWS profile. Bank PATCH under era 3; outline story `john-stewart-marketplace` verified (old slug documented-1600s-store-customer removed).
- 2026-09-27 Unit 1b: rationing slot filled: Emilia Ruth Palmquist Lundberg (Jersey City), from Rutgers Oral History Archives, Donald E. Lundberg interview 2008 (paraphrase only; Rutgers requires permission to quote). Slug `emilia-lundberg` (old `ration-book-shopper` removed). Bank PATCH under era 8 also records failed routes (Detroit Free Press list, LOC OWI photos, Texas City, Pacific War Museum, Berkeley 403, Since You Went Away restricted) + NPS point figures + Mrs. Walter J. Edmondson photo (UTA).
- 2026-09-27 Unit 1c: delivery slot filled: Renica Turner (Amazon DSP Battle Tested Strategies, Palmdale/Victorville) from NPR July 20, 2023; NLRB settlement status to June 2026 (FreightWaves). Slug `renica-turner` (old `delivery-worker-marketplace` removed). Added span "The last step: heat in the delivery truck" (Chavez, Rodriguez, UPS AC deal). SEARCHED NOT FOUND: citation over Chavez death. UNIT 1 DONE.
- 2026-09-27 Unit 2: sourced & rewrote stories. Guild: journal PDF pt1 has OCR text (vermonthistory.org/journal/misc/GuildJournalPt1.pdf), pp. 249-253 read, 30 cents in 3 days, goods list. Franklin: Smyth, Smithsonian 2024 (90 -> 1,500 subscribers; >=277 ads offering >=308 enslaved people; David Hall 1748). Barnum: Scudder museum 1841 (visualizingnyc), Humbugs of the World 1865/66 (Gutenberg 26640). Ward: Encyclopedia.com + Chicagology (Tribune "Grangers Beware" Nov 8 1873, $20k libel suit, retraction Dec 24 1873); REMOVED unsourced storekeepers-junk line; guarantee 1874 vs 1875. Wanamaker: 1879 first full-page dept-store newspaper ad (Duke timeline); removed unsourced "few lines" claim. Sears: Encyclopedia.com (b. Dec 7 1863, $14 watches, 1908/1909, d. 1914); removed "not the goods but the writing" cadence. Saunders: Tennessee Encyclopedia (Sole Owner stores, Keedoozle, d. 1953). Gruen: Austria press ($8, no English), MNopedia (500 acres; apartments, schools, medical center 1965, park, lake; $20M) - replaced unsourced "library, post office". Walton: Neumark et al 2008, Artz & Stone 2012, Hausman & Leibtag 2007. Bezos: HistoryLink 2025; removed unsourced "waiting a week felt broken". UNIT 2 DONE.
- 2026-09-27 Unit 3 (bank check eras 1-5): PATCHes: Celilo flooding actor/date/settlement (HistoryLink 10010); Springfield land = Agawam deed July 15 1636 (Mass Moments); NYC Wall Street slave market 1711-1762 (WNYC 2015) + outline span; Franklin Gazette slave ads count (Smyth); Christopher Seider killed at Theophilus Lillie's shop Feb 22 1770 by Ebenezer Richardson (Colonial Society, Hutchinson correspondence + trial) + outline span. SEARCHED-NOT-FOUND style note: buyers/sellers at Wall St market unnamed. UNIT 3 DONE.
- 2026-09-27 Unit 4 (bank check eras 6-10): PATCHes + outline: Weeping Time 1859 (NPS; Southern Spaces) new span era 7; Mrs. Winslow's Soothing Syrup (Canadian Museum of Health Care) + SEARCHED NOT FOUND death count; company store & scrip (e-WV; EH.net, Fishback, Coal Commission 1922) new span era 8; ECOA 1974/1976 (CFPB) era 9; payday loans CFPB 2013 (bank only); Senate HELP Amazon warehouse injuries Dec 2024 (bank + 1 bullet). Perishables refreshed: Census Q2 2026 17.1% (released Aug 18 2026); Coresight 2025 = 8,270 closures (search summary only; 2024 revised 8,825); ThredUp 14th report Apr 2 2026; 24 state privacy laws June 2026, no federal law; Prime $139 unchanged (May 2026); BTS/NLRB settlement approved May 2026. Both checks PASS (bank 15359w vs outline 10352w). UNIT 4 DONE.
