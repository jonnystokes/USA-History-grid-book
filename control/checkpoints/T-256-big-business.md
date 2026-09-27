# CHECKPOINT T-256 | big-business | patch (bank write-up) + bank check | T-256a eras 1-7, T-256b eras 8-10

STATUS: DONE (director verified: patch PASS, research PASS)
VERIFY: python tools/project_state.py --check big-business --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/big-business.md · research/research-big-business.md · workspace/big-business.md

NOW:    T-256b finished units 4-6 (2026-09-27). Idle.
NEXT:   Director: commit. Both gates PASS (patch, research). Writers: read the bank's CORRECTION and 'unconfirmed' tags; outline eras 8-10 were rewritten to match the bank.

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
| 4 | bank write-up + verify stories, eras 8-10 | T-256b | done | eras 08, 09, 10 written to the bank with CORRECTION notes, outline corrected (see log) |
| 5 | bank check, eras 8-10, perishables | T-256b | done | 'BANK CHECK, eras 08 to 10' at end of bank. PATCHes: La Follette committee (era 08), tobacco/asbestos/Nader/Bhopal (era 09), Enron/Kessler/Purdue (era 10), Apple suit, suit filing dates, Amazon Prime. 1 SEARCHED, NOT FOUND (Johns-Manville 1930s knowledge). Perishables refreshed to Sept 2026. Parked: drugs-alcohol (Purdue), health (tobacco etc.). |
| 6 | final: flags, bank >= outline, validator, both checks | T-256b | done | all 10 eras progress=researched (true: bank written for all). Bank 25,538w vs outline 8,653w. Validator 0 errors. Eras 8-10 zero em dashes/semicolons. hb-note status line corrected. patch PASS, research PASS. |

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
- 2026-09-27 T-256b: Era 08 written to bank ('## 08 · 1900 to 1950 (T-256b...)', inserted before the eras 01-07 bank check). Outline era 08 corrected: era zoom rewritten (no personification), US Steel date/capital/share ranges + watered stock ($682M, Bureau of Corporations via EBSCO), Morgan story (Harriman dropped, unconfirmed), Tarbell (19 installments Nov 1902-Oct 1904 per Allegheny/Britannica, 'this book' meta sentence removed), TR (Taft 75-99 not 90), Standard Oil 34 pieces, $900M by end-1913, gasoline line removed, American Tobacco 1911 added, 1914 laws dated, Kennedy date range, war contracts (Higgs top 10 30%, GM 8%). Sources: Cambridge UP Lamoreaux page; HBS Baker exhibit; EBSCO Morgan; EH.Net Warren review; Wikipedia US Steel/NSC/SO case/Clayton; Smithsonian + Plain Dealer (Tarbell/Backus); Allegheny; Milken Review, Miller Center (suit counts); LOC SO + SEA 1934; Independent Institute (Rockefeller $); NCpedia (tobacco); FTC history; Davis 2011 PDF (Berle-Means); Pittsburgh Quarterly + GWU ER papers (Kennedy); Hawaii Business Mag (Big Five); Higgs 1995.
- 2026-09-27 T-256b: Era 09 written to bank. Outline era 09 rewritten whole: era zoom (no personification, figures), GM share 51-54% range, 1-in-200 marked unconfirmed (NOT in Britannica, attribution dropped), Wilson exact quote (American Heritage 1995), 'gave up' line removed, NEW spans: Eisenhower 1961 (NARA), 'Products that hurt people' (Frank Statement 1954, Yeaman 1963 via FRONTLINE, 1994 CEOs transcript UCSF, MSA 1998, Johns-Manville 1982 Manville Trust, Bhopal 1984 PMC review); Nader/GM 1966 added; ITT 250-350, ABC 1966, Chile $350,000; Powell memo 23 Aug 1971 (W&L), '34-page' dropped; BRT 13 Oct 1972; FEC PAC table replaces 'mid-1980' figures; Carter Library dates; Bell: AT&T kept $34B (RCR Wireless), IBM comparison dropped; Microsoft story repaired (upheld monopoly finding; settlement 1 Nov 2001); Vlasic confirmed from Fast Company via Internet Archive, threat added.
- 2026-09-27 T-256b: Era 10 written to bank (perishables refreshed to Sept 2026). Outline era 10 rewritten: caps as of 7 Sept 2026 (Motley Fool: Nvidia 5.6T, Apple 4.7T, Alphabet 4.1T), Walmart FY2026 $713.2B / 2.1M / 1.6M US (SEC), Amazon 1,576,000 (10-K), GM comparison corrected to ~2.5x (not 3x), TARP GAO $443.5B / $31.1B with program split, Lehman Fuld + Repo 105, Google search remedies (Dec 2025, appeal 2026, Courthouse News), Google ad tech remedies Sept 2026 (no AdX sale, NLR), Meta appeal 20 Jan 2026 (CNBC) pending (MediaPost Aug 2026), Amazon trial moved to 29 March 2027 (MLex), Prime $2.5B, Apple suit added, Khan (CNBC: Senate 69-28, sworn chair 15 June 2021), Citizens United figures replaced with Brennan Center ($6.4B 2010-22, $2.7B 2024, dark >$1B), lobbying $5.08B 2025 / 15,768 orgs (OpenSecrets), gig: BLS 1.6M 1.0% May 2017 + Pew, '42M/70M' removed. NEW span 'Fraud at the top': Enron convictions (DOJ 2006), Kessler 2006 tobacco RICO, Purdue 2007/2020/2025 $7.4B. 'this book went to press' meta removed.
- 2026-09-27 T-256b: Units 5 and 6 done. Both checks PASS. Open for later rounds: Boeing 737 MAX company side; Angelo Mozilo (Countrywide) not named anywhere; 1-in-200 GM figure and Bell 'bigger than GM+GE+...' need an opened source; Harriman in Northern Securities unconfirmed; Johns-Manville 1930s knowledge (SEARCHED, NOT FOUND).
