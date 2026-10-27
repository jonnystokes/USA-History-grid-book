# CHECKPOINT T-652 | economy, education, energy, exploration | gaps | GAPS-FINAL items 1-7

STATUS: IN-FLIGHT (all 7 items landed; awaiting director)
VERIFY: python tools/project_state.py --check <slug> --stage prose (economy, education, energy, exploration)
BRIEF:  control/briefs/GAPS.md (dispatch: control/briefs/GAPS-FINAL-DISPATCH.md, section T-652)
MODEL:  opus
FILES:  research/research-{economy,education,energy,exploration}.md · manuscript/{economy,education,energy,exploration}/...

NOW:    done; all checks PASS (prose + research, 4 chapters)
NEXT:   report

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | economy part2 era 6 row 41: name sources of 1837 estimates (a third jobless, 30-50% wage cuts, 343 of 850 banks, NY 25-30%) | landed | CLOSED (T-652) for 343/850: Bancroft ed., The Great Republic by the Master Historians III (1902), opened via Wayback; bank corrected (not Hammond); prose credits Bancroft. SEARCHED, NOT FOUND for the worker figures; prose now says the teaching guides give no source |
| 2 | education part1 era 5: who granted the Young Ladies' Academy of Philadelphia its charter 7 Jan 1792 | landed | SEARCHED, NOT FOUND for a named official (Mifflin = Wikipedia only; Evans-TCP 1794 book and HathiTrust behind Cloudflare; Savin & Abrahams 1957 and Moore et al. 2011 not openable). PATCH: historian Tanya Roth (Sat. Eve. Post 2024) 'the state of Pennsylvania granted'; prose now 'officials of the state of Pennsylvania granted the school a charter' |
| 3 | education bank correction (AUDIT-QUEUE T-482): Black teachers "in every state ... faced the whip" | landed | CLOSED (T-652): bank line rewritten to NC/GA/VA only (T-485 correction note kept below it); part2 span already matched; part2 era summary sentence 'In the South, lawmakers ... wrote whipping into the punishment' narrowed to NC, GA and VA |
| 4 | energy (optional): Garrison Dam 152,360 acres; 300+ families, 1,700 people, 80 percent | landed | CLOSED (T-652), bank only: 152,360 acres on ND Studies (archived) and UMD Recovering Democracy Archives (citing Lawson 2009 p.59); families = 325, about 80 percent (ND Studies); 1,700 not on the cited page, left unconfirmed. No prose change |
| 5 | energy (optional): date of Kemmler's killing of Tillie Ziegler (March 29, 1889) | landed | CLOSED (T-652), bank only: buffaloah.com grave page gives death 3/29/1889; attack hour (night of Mar 28 or Mar 29) unsettled. Prose reads fine without it (next sentence dates May 1889 trial); no change |
| 6 | exploration: Wilkes expedition as "the first" large US-government exploring voyage | landed | CLOSED (T-652): Smithsonian Libraries Ex.Ex. essays (sil.si.edu): W. John Kress 'the first US international exploring expedition'; Walsh 2004 'first government-sponsored scientific expedition' (not used: Lewis and Clark). One credited sentence restored in the charles-wilkes story |
| 7 | exploration (AUDIT-QUEUE T-462): Boone torture detail, confirm scholarly/primary or cut | landed | LEFT AS IS (already closed): bank PATCHes T-484 (2026-10-02) and T-623 (2026-10-03) rest the detail on Lofaro, Daniel Boone: An American Life (UP Kentucky 2010) and O'Malley, Kentucky Frontier to Commonwealth (UP Kentucky 2025); prose already credits both by name and no longer uses the blog or Substack. No change |

## Sources in hand

- http://web.archive.org/web/20221206104017/https://www.publicbookshelf.com/public_html/The_Great_Republic_By_the_Master_Historians_Vol_III/thepanic_ce.html : Bancroft 1902 chapter, 343 of 850 banks (verbatim)

## Gaps researched

## Decisions and defects fixed

## Log

2026-10-26 | item 7 | verified, no change | n/a | n/a
2026-10-26 | item 6 | exploration bank PATCH; part2 story one sentence | validator 0 errors | punct 0/0
2026-10-26 | item 5 | energy bank PATCH only | n/a | n/a
2026-10-26 | item 4 | energy bank PATCH only | n/a | n/a
2026-10-26 | item 3 | education bank line rewritten; part2 era summary narrowed | validator 0 errors | punct 0/0
2026-10-26 | item 2 | education bank PATCH + SEARCHED, NOT FOUND; part1 one sentence | validator 0 errors | punct 0/0
2026-10-26 | item 1 | economy bank PATCH + SEARCHED, NOT FOUND; part2 two sentences | validator 0 errors | punct 0/0
