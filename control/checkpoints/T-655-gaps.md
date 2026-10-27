# CHECKPOINT T-655 | music, native-nations, news-communication, rights-movements | gaps | GAPS-FINAL items 1-7

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check <slug> --stage prose (each of the four slugs)
BRIEF:  control/briefs/GAPS.md + control/briefs/GAPS-FINAL-DISPATCH.md (section T-655)
MODEL:  opus
FILES:  research/research-{music,native-nations,news-communication,rights-movements}.md · manuscript/<slug>/...
SCRATCH: C:\Users\jon\AppData\Local\Temp\claude\C--Users-jon-Projects\60b4fd0b-3ca5-4e19-ac34-4e7802a1ccd8\scratchpad\T-655\

NOW:    done; all 7 items closed or banked; --check prose and research PASS for all four slugs
NEXT:   director reviews and commits

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | music p2 era 6: Foster Jan 1864 fall, suicide claim (Emerson / O'Connell) | CLOSED (T-655) | bank PATCH era 06; prose: accounts differ, Emerson 1997 fall vs O'Connell 2016 suicide |
| 2 | music p3 era 8: Hay 1945 DeFord Bailey race remark, exact quote | CLOSED (T-655) | Wolfe 1999 quotes Hay in full; prose quotes exactly; corrected 'refused to learn new tunes' to 'refused to learn more'; added Bailey's own account via Wolfe |
| 3 | music p3 era 10: PERISHABLE Kennedy Center closure + Suno/Udio, refresh to 2026-10-26 | CLOSED (T-655) | Kennedy: still closed as of Oct 26 (AP Oct 25, Daily Beast Oct 26), Beatty's Oct 25 motion added; Suno: Sept 18 second UMG/Sony suit (DMN), Oct 21 Reservoir suit (MBW); paragraph reordered by date; 'late September' line refreshed |
| 4 | native-nations p1 era 3: Beaver Wars nations pushed out | CLOSED (T-655) | Canadian Encyclopedia 'Iroquois Wars' (opened in browser pane): Wendat 1649, Neutral 1651, Erie absorbed 1657, Susquehannock by 1675, Ohio Valley; Shawnee Wikipedia-only, not used |
| 5 | native-nations p1 era 1: count of nations / languages before 1500 (Goddard) | CLOSED (T-655) for languages; nations SEARCHED, NOT FOUND | Lyle Campbell, Britannica (opened in browser): >300 languages in US+Canada at contact, 57 families, 20 only in California; prose credits Campbell; Goddard vol 17 not reachable |
| 6 | news-communication p3 era 9: Ole Miss 1962 crowd = white segregationists | CLOSED (T-655) | JFK Library 'rioting erupted by white protesters'; DOJ 2011 closing memo: >2,000 protesters, segregationist supporters, 212 detained, 24 Ole Miss students |
| 7 | rights-movements p3 era 9: Chicano Moratorium other three dead, how, who | CLOSED (T-655); killers' names SEARCHED, NOT FOUND | Cordova (Glasstire 2020, citing Ruiz 2012 and E. Chavez 2002) + LA Conservancy: Diaz (police say shot running a barricade; Ruiz: shot in back of head as passenger), Ward (witnesses: tear gas canister exploded; police: protesters' bomb); Montag killed Jan 31 1971, not Aug 29; prose 'Four died' -> 'At least three were killed' + count dispute stated |

## Sources in hand

- archive.org search-inside works ONLY from the browser pane: navigate to archive.org/details/<item>, then javascript fetch https://<server>/fulltext/inside.php?item_id=<id>&doc=<id>&path=<dir>&q=<q> with credentials:'include' (server/dir from archive.org/metadata/<id>). curl gets 'Item not available'. Google Books API: quota 0 (429).
- Wolfe, A Good-Natured Riot (1999) = goodnaturedriotb0000wolf (Hay 1945 quote at scan p.161)
- Emerson Doo-Dah! = doodahstephenfos00unse; O'Connell 2016 = lifesongsofsteph0000ocon

## Gaps researched

## Decisions and defects fixed

## Log

- 2026-10-26 | item 1 | music part2 Foster passage + bank PATCH | validator 0 errors | punct 0/0
- 2026-10-26 | item 2 | music part3 Bailey story + bank PATCH (correction) | validator 0 errors | punct 0/0
- 2026-10-26 | item 3 | music part3 Suno + Kennedy refresh + bank PATCH | validator 0 errors | punct 0/0
- 2026-10-26 | item 4 | native-nations part1 era 3 Beaver Wars sentences + bank PATCH | validator 0 errors | punct 0/0
- 2026-10-26 | item 5 | native-nations part1 era 1 languages sentence + bank PATCH | validator 0 errors | punct 0/0
- 2026-10-26 | item 6 | news-communication part3 Ole Miss crowd + bank PATCH | validator 0 errors | punct 0/0
- 2026-10-26 | item 7 | rights-movements part3 Moratorium paragraph + bank PATCH | validator 0 errors | punct 0/0
- 2026-10-26 | final | self-review pass (Foster sentence reworded); --check prose + research PASS x4 | validator 0 errors | punct 0/0
