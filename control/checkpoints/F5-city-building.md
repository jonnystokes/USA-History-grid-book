# CHECKPOINT F5 | city-building | step 5 fixer, whole chapter

STATUS: T-454 landed (director verified: PASS  city-building / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/city-building/part1|part2|part3 + control/audit/city-building/part1|2|3-findings-sonnet.md
        + research/research-city-building.md (PATCH entries only)

NOW:    all three parts done; prose check PASS
NEXT:   (none) director commits
SCRATCH: scratchpad/T-454 (apply_verdicts.py rebuilds the fixer column from v<part>.txt; wc = whole-file words, as the baseline)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 84 / 6 / 0 of 90, plus 2 found by fixer (FIXED) | 4685 -> 5561 |
| part2 | 6-7 | DONE | 111 / 2 / 0 of 113, plus 2 found by fixer (FIXED) | 5109 -> 5583 |
| part3 | 8-10 | DONE | 90 / 1 / 0 of 91, plus 2 found by fixer (FIXED) | 7246 -> 7916 |

## NEEDS-RESEARCH
- None open. SEARCHED, NOT FOUND items, each logged in its bank PATCH and stated record-side or cut in the prose:
  - Half-freedom and the right to go to court: SEARCHED, NOT FOUND (logged in bank era 03 PATCH); the claim was cut.

## Log
- part1 era 1 DONE: rows 1-15 FIXED 15. PATCH era 01 (Cahokia location/rank, Mesa Verde setting, "pueblo"). validate 0 errors, punct 0/0.
- part1 era 2 DONE: rows 16-23 FIXED 6, REJECTED 2. PATCH era 02 (Seloy 1565-66, "the Indies"). checks clean.
- part1 era 3 DONE: rows 24-51 FIXED 26, REJECTED 2. PATCH era 03 (Jamestown/Paspahegh, Santa Fe/Ogha Po'oge, Boston/Shawmut + Dudley 1631 + watch, Lenape Manhattan, half-freedom petition + dues + Kieft, Philadelphia Lenape + Penn purchases, Quakers, TCLF precedent). checks clean.
- part1 era 4 DONE: rows 52-64 FIXED 12, REJECTED 1. PATCH era 04 (London 700,000; Franklin 1735 letter; bags; other Philadelphia companies; BPL 1711 fire; Cincinnati 1853). Label changed to "Fire in wooden towns". checks clean.
- part1 era 5 DONE: rows 65-90 FIXED 25, REJECTED 1. PATCH era 05 (1791 landowners' deal; L'Enfant's reburial; Centre Square details and Watering Committee; CDC recovery). checks clean.
- part1 reread: F1, F2 found by fixer and FIXED. validate 0 errors, punct 0/0. Words 4685 -> 5561.
- part2 era 6 DONE: rows 1-42 FIXED 42. PATCH era 06 (Rochester/Seneca + Phelps-Gorham + mills; Chicago/Potawatomi + mud; San Francisco/Yelamu + six fires; grid on the ground, 721 buildings moved; water before Croton; cholera speed; 1835 fire origin; Croton dam and brick tunnel). checks clean.
- part2 era 7 DONE: rows 43-113 FIXED 69, REJECTED 2. PATCH era 07 (Otis, rents by floor, Monadnock, Post, White City + City Beautiful, 1867 tenement law, Riis, swill milk, Seneca Village taking and voters, Olmsted, horsecars, Mayor William L. Strong, 1889 land run copied from migration bank). Label changed to 'Out: streetcar lines and streetcar suburbs'. F1 (Strong name collision), F2 (own marker slip) FIXED. validate 0 errors, punct 0/0. Words 5109 -> 5583.
- part3 era 8 DONE: rows 1-43 FIXED 42, REJECTED 1. PATCH era 08 (Ellis Island 1907; Chicago intakes + Missouri suit; SF 1906 water + Wilson + PG&E; Equitable shadow; Buchanan + Euclid; Plan of Chicago money; HOLC terms + the map dispute; Groves + cemesto + secrecy; Colleen Black's words; Hiroshima deaths from war bank). checks clean.
- part3 era 9 DONE: rows 44-72 FIXED 29. PATCH era 09 (urban renewal mechanics + Berman; Eisenhower + route choices; Anderson born 1940, the false age-8 line dropped, Rangh Court, Rondo Days purpose; Levittown 27 steps + whites-only lease; blockbusting + North Lawndale; Jacobs eyes on the street + Lindsay 1969; Cuyahoga details + Clean Water Act 1972; Black mayors by name). checks clean.
  - The individual officials who carried out the Seneca Village taking (era 07 PATCH); prose names the city officials as a group and says published histories do not name them.
  - Which 1866 cession the 1889 Unassigned Lands came from (copied from the migration bank).
- Resolved disputes: Marvin Anderson born 1940 (AARP 2023, his own words); Sahan's 'eight in 1958' dropped as false. Mayor Strong given his first name (William L.) to end the AUDIT-QUEUE name collision. HOLC maps: the scholars' dispute is now stated, with the agreed FHA fact.

- part3 era 10 DONE: rows 73-91 FIXED 19. PATCH era 10 (Brookings downtowns; remote work; U Street history, 1968 riots, condos; EPA heat mechanism; Miami Beach drains; 1WTC height). F1, F2 FIXED. Words 7246 -> 7916.
- FINAL: prose check PASS (manuscript 18101 words, 0 em dashes, 0 semicolons, validator 0 errors). Totals: FIXED 285, REJECTED 9, NEEDS-RESEARCH 0, found by fixer 6.
