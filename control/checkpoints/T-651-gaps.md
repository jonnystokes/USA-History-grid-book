# CHECKPOINT T-651 | city-building, crime-justice, disasters, drugs-alcohol | gaps | GAPS-FINAL items 1-7

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check <slug> --stage prose (and --stage research) for city-building, crime-justice, disasters, drugs-alcohol
BRIEF:  control/briefs/GAPS.md + control/briefs/GAPS-FINAL-DISPATCH.md (section T-651)
MODEL:  opus
FILES:  research/research-<slug>.md · manuscript/<slug>/... for the four chapters only

NOW:    all 7 items done; reported to the director
NEXT:   nothing; director to review and commit

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | city-building part2 era 7: 1889 Creek ($2.28M) and Seminole ($1.91M) payments, 25 Stat. ch. 317 and ch. 412 | CLOSED (T-651) | amounts confirmed in the govinfo Statutes at Large scans (Creek $2,280,857.10, Seminole $1,912,942.02/.20); bank PATCH 2026-10-26 in era 7; prose already correct, unchanged |
| 2 | crime-justice part2: Myrtle Vance (Paris, Texas, 1893), period sources' word; "rape" if supported (#31) | LEFT AS IS (already done by T-485) | bank PATCH T-485 has the NY Sun 2 Feb 1893 "ravisher" (via Wells, Red Record, Gutenberg); prose already says "Newspaper reports said that she had also been raped" with Wells's witnesses who saw no sign; no 'sexually attacked' left in the chapter |
| 3 | crime-justice: gloss "Lower Agency" (Lower Sioux Agency) from MNHS or NPS | CLOSED (T-651) | MNHS Lower Sioux Agency history page; bank PATCH era 7; part2 Dakota trials sentence glossed |
| 4 | crime-justice: Eastern State / other polish notes under NEEDS-RESEARCH in control/checkpoints/F7-crime-justice.md | CLOSED (T-651) | Eastern State: warden named Samuel Wood (Janofsky, Encyc. Greater Philadelphia full page) and the 1834-35 legislative committee named as investigator (Hayden, Vanderbilt repository abstract); bank PATCH era 6. Attica and Wounded Knee notes already settled in prose and bank by T-626-era patches (jury verdict, AP 2000, FBI 2000): no change |
| 5 | disasters part2 era 7: Sea Islands 1893, Caroline Grego on the politicians and newspaper writers | CLOSED (T-651) | Grego's LDHI exhibit (College of Charleston) names Eugene Gregorie, William Elliott, the Columbia Daily Register (May 25, 1894), Gov. Tillman backing a Bluffton collection for white farmers, and the seven Black petitions; prose updated, silent-record sentence removed; bank PATCH era 7 |
| 6 | disasters: Palisades Fire case status refreshed to 2026-10-26 | CLOSED (T-651) | DOJ CDCA case page updated Oct 22, 2026 (pretrial conference Oct 29, jury selection Nov 2, Judge Anne Hwang) + NBC4 Oct 22 report; prose now 'As of October 26, 2026 ... not convicted'; bank PATCH era 10 |
| 7 | drugs-alcohol (low priority): 1791 whipped messenger = John Connor? Founders Online | CLOSED (T-651) | director opened Founders Online Hamilton to Washington [5 Aug] 1794 in a browser: Hamilton's text + editors' note 20 'John Connor'; bank PATCH era 05 (supersedes the earlier SEARCHED, NOT FOUND); part1 prose names Connor and adds money, horse, blindfold, five hours |

## Sources in hand

- https://ldhi.library.cofc.edu/exhibits/show/mapping-recovery-hurricane (Grego exhibit; sub-pages racial-tensions-rise, petitions-acts-of-resistance, conclusion)
- https://www.mnhs.org/lowersioux/learn/history: what the Lower Sioux Agency was
- https://www.govinfo.gov/content/pkg/STATUTE-25/pdf/STATUTE-25-Pg757.pdf and ...Pg980.pdf: 25 Stat. ch. 317 and ch. 412 (LOC statute PDFs are behind Cloudflare; govinfo works)

## Gaps researched

## Decisions and defects fixed

## Log

- 2026-10-26 | item 1 | bank PATCH only, no prose change
- 2026-10-26 | item 2 | no change, already done
- 2026-10-26 | item 3 | crime-justice part2 + bank | validator 0 errors | punct 0/0
- 2026-10-26 | item 4 | crime-justice part2 Eastern State + bank | validator 0 errors | punct 0/0
- 2026-10-26 | item 5 | disasters part2 Sea Islands + bank | validator 0 errors | punct 0/0
- 2026-10-26 | item 6 | disasters part3 Palisades + bank | validator 0 errors | punct 0/0
- 2026-10-26 | item 7 | bank only
- 2026-10-26 | item 7 reopened on coordinator message | drugs-alcohol part1 + bank | validator 0 errors | punct 0/0 | --check prose PASS
- 2026-10-26 | final | --check prose and research PASS for city-building, crime-justice, disasters, drugs-alcohol
