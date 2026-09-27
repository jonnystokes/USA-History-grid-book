# CHECKPOINT T-256 | big-business | patch (bank write-up) + bank check | T-256a eras 1-7, T-256b eras 8-10

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check big-business --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/big-business.md · research/research-big-business.md · workspace/big-business.md

NOW:    T-256a finished units 1-3 (2026-09-27). Idle until T-256b.
NEXT:   T-256b: Unit 4 (bank write-up + verify stories, eras 8-10). Read eras with `python tools/slice_bank.py big-business --eras 8-10`. The bank's parked economy/marketplace sections (U.S. Steel $480M, A&P, Woolworth, TARP, Lehman) are yours. Patch check already PASSES; keep it passing. Unit 6 must still check every era's progress= flag.

## Measured before dispatch (2026-09-27)

FAIL patch: stories=14 (13 verified, 1 candidate, 0 target), 1 [VERIFY] tag, **bank 409w against
outline 6,759w**, validator 0 errors. DECISIONS #11: the outline's `hb-note` claims a full bank
exists, but it was never written. **The sources are inline in the outline, so the main job is a
write-up: every fact the outline states goes into the bank under its era, with its source, checked
against that source.** A fact whose source does not support it is corrected in the bank (with a
note) and in the outline.

Gate items:
- 13 stories marked `verified` with no bank behind them. Each needs its key facts in the bank.
- line 146 `franklin-tarbell` (candidate, era 7): Ida Tarbell's father, an independent oil
  producer ruined in the South Improvement fight.
- line 149: one `[VERIFY]` tag (in the Tarbell story).
- the bank must end larger than the outline.

Outline size by era: 1-5 about 2,060w, 6 about 630w, 7 about 1,510w, 8 about 1,220w,
9 about 1,150w, 10 about 1,070w. Hence the split.

## Units

| # | unit | agent | state | landed (note) |
|---|------|-------|-------|---------------|
| 1 | bank write-up + verify stories, eras 1-5 | T-256a | done | bank eras 01-05 written (about 5,800w). 3 stories backed (Sandys, Hancock, Morris). Corrections noted in bank: lottery ban was the king's not Parliament's; the '16 charters' limited-liability count is the Handlins' (via Wright), not Wright's; BNA plan 26 May 1781 vs charter 31 Dec 1781; Morris $2.95M is the 1801 finding. PATCHes: Royal African Company (era 03), Hancock-Apthorp ships in the 1755 Acadian expulsion (era 04). Land: Tsenacomoco, Lenape Manhattan, Chinookan Fort Vancouver site, Seneca land at Big Tree 1797 (Morris). |
| 2 | bank write-up + verify stories, eras 6-7, including Franklin Tarbell and the [VERIFY] | T-256a | done | bank eras 06-07 written; bank now 12,895w vs outline 7,228w; --stage patch PASSES. Franklin Tarbell verified from primary sources (Ida Tarbell, All in the Day's Work, 1939, Gutenberg 63754; his 1905 obituary on Find a Grave). CORRECTED in outline: partner's suicide was about 1892 (not after 1872), home mortgaged in the 1893 panic, 'most of five years' not four, 'refused to join' dropped. [VERIFY] cleared; partner's name is a SEARCHED, NOT FOUND. Other outline corrections: lottery ban by King James I; Wrote's count; Wright $25B -> Sylla-Wright 22,419 corps / $4.5B; Lowell 2,500 in 1826; Biddle comparisons ($25M/$75M) removed (SEARCHED, NOT FOUND), 1822/1823 and 29/25 branches; PRR 'assets double' dropped; Cleveland buyout six weeks to three months; Carnegie 'three-quarters of Mesabi' dropped; Holway beating added and closing triad replaced; ICC 'model for every' -> 'first'. Added to outline: Royal African Company bullet (era 03, branding defined), Hancock-Apthorp Acadian transports (era 04), Big Tree/Seneca (Morris), Lenape/Mohican/Pennacook/Ojibwe land lines, Southern exclusion of non-white incorporators (Hilt). |
| 3 | bank check, eras 1-7 (hard subjects, actors, land) | T-256a | done | 'BANK CHECK, eras 01 to 07' section at end of bank. PATCH: American Tobacco 1890 (era 07). Era-zoom claims flagged for writers: 'railroads larger than the governments that chartered them' (only PRR capital vs federal receipts supported), 'mostly in the companies' favour' (interpretation, name the cases). Homestead named dead (Klein, Joseph Sotak, Streigle) added. 3 SEARCHED, NOT FOUND (Biddle-era comparisons, Tarbell partner's name, plus 'no record names the men who fired' at Homestead as a how-to-say line). Nothing parked elsewhere. Workspace lists Debs as a story here but the outline has none (director's call). |
| 4 | bank write-up + verify stories, eras 8-10 | T-256b | todo | |
| 5 | bank check, eras 8-10, perishables | T-256b | todo | |
| 6 | final: flags, bank >= outline, validator, both checks | T-256b | todo | |

## SUBJECT NOTES (from the director)

Registry angle: the scale of business and its clashes with government and the public: trusts,
regulation, lobbying, corporate power. Not: the daily job (`work-workers`), the whole economy
(`economy`). DECISIONS #12: film does not live here.

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the outline
and the neighbouring banks, especially `economy`, `work-workers`, `money`, `energy`,
`transportation`): chartered companies and enslaved labor (the Royal African Company, the Virginia
Company) · railroad land grants and whose land · Standard Oil's methods (rebates, the South
Improvement Company) · private armies against strikers (the Pinkertons at Homestead, company
guards at Ludlow) with the dead · companies that knew their product harmed people (asbestos,
leaded gasoline, tobacco) and who knew, when · the 2008 crisis and who ran the firms · 2000-today:
antitrust cases against the largest tech firms, dated.

Perishable: every 2000-today figure. Date each and refresh to 2026.

## Sources in hand
- Encyclopedia Virginia, Virginia Company of London (charters, shares, lotteries, Wrote's 4,270/1,240/347/2,683, Sandys, headright, revocation 1624).
- Britannica Muscovy Company (via curl) · Wikipedia Levant Co., EIC (31 Dec 1600) · Avalon Project WIC charter 3 June 1621 · NYS Museum Fort Orange 1624 · HistoryLink 5251 Fort Vancouver 19 Mar 1825 · Canadian Encyclopedia HBC 2 May 1670 · Teaching American History, Cambridge Agreement (26/29 Aug 1629) · History of Massachusetts Blog (charter revoked 23 Oct 1684).
- History.com + Wikipedia Royal African Company (186,748 people, 16,077 deaths, branding, 1698 Act).
- Wright, NBER c11744 PDF (319 corporations, 8 colonial, 'few, small, and largely inconsequential', Handlins' 16, 20,000 corporations with $6-7 billion by 1860).
- EH.Net Klein & Majewski (59 toll bridges 1786-98) · Encyclopedia of Greater Philadelphia + Richmond Fed 2026 (Bank of North America) · Boston Tea Party Ships & Museum + UK National Archives (Tea Act, 340 chests, £9,659) · Wikipedia Robert Morris ($2,948,711.11, Prune Street) · Encyclopedia.com/Baxter + Wikipedia (Thomas Hancock) · acadian.org (Apthorp & Hancock transports 1755).

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed
- T-256a corrected the outline where sources disagreed with it (list in unit 2 row). Bank text written this session carries CORRECTION notes beside each.

## Log
- 2026-09-27 T-256a: Unit 1 done, eras 01-05 appended to the bank. Next: Unit 2 (eras 06-07).
- 2026-09-27 T-256a: Unit 2 done. patch check PASS (bank 12,895w, outline 7,228w, 0 candidate, 0 VERIFY). Next: Unit 3 bank check eras 1-7.
- 2026-09-27 T-256a: Unit 3 done. Bank check eras 01-07 appended. NEXT set for T-256b.
