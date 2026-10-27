# CHECKPOINT T-653 | food-farming, government-politics, health, holidays, home-family | gaps | GAPS-FINAL items 1-8

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check <slug> --stage prose (each of the five slugs)
BRIEF:  control/briefs/GAPS.md (dispatch: control/briefs/GAPS-FINAL-DISPATCH.md, section T-653)
MODEL:  opus
FILES:  research/research-<slug>.md · manuscript/<slug>/... for the five slugs

NOW:    all 8 items done; checks run 2026-10-26, all PASS. Waiting for the director.
NEXT:   nothing; director reviews and commits

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | food-farming: Kansas 1885-86 quarantine law purpose (Texas fever), primary/scholarly source | CLOSED (T-653) | bank PATCH era 07 from MKT Ry v. Haber, 169 U.S. 613 (1898); prose states no purpose, unchanged |
| 2 | food-farming: who arrested Ward Rodgers, Jan 1935, Marked Tree | CLOSED (T-653) | CALS EoA 'State v. Rodgers (1935)': Sheriff J. D. Dubard; bank PATCH era 09 area; part3 era 08 span names him; 'same account' antecedent fixed |
| 3 | food-farming: Chavez March 2026 accounts in part 3 (#46), verify or copy T-601 PATCH | CLOSED (T-653) | verified present: part3 line ~206, credited to NYT, matches work-workers; bank T-609 PATCH present; no change |
| 4 | government-politics: part3 row 22 era 9, who kept 1 million disabled children out of school before 1975 | CLOSED (T-653) | ed.gov IDEA history opened (curl 200): state laws excluded deaf, blind, emotionally disturbed, intellectually disabled children; prose names the state laws, bank PATCH era 9 |
| 5 | health: Puerto Rico sterilisation, factories/hospitals (Briggs 2002, Lopez 2008) | SEARCHED, NOT FOUND | Briggs TOC only (Google Books quota 429), Lopez book pages + Lopez SFOnline article p1-5 opened: no named factory/hospital; bank SNF added; prose unchanged |
| 6 | holidays: part1 era 5, Fithian's Nelson enslaved at Nomini Hall? | SEARCHED, NOT FOUND | journal (PG #40044) all Nelson lines, 1900 index (servant vs slave), Nomini Hall Slave Legacy (Nelson Gumby b.1766, not tied to Fithian); Farish 1943 not reachable; prose unchanged |
| 7 | home-family: earth lodge "up to 30 people" source (low priority) | CLOSED (T-653) | no source for 30 (NPS 10-20; SHSND markers 8-18, 8-20); prose '30' sentence replaced by SHSND size 35-45 ft and 150 trees; bank PATCH era 01 |
| 8 | home-family: who coined "cult of domesticity" (low priority) | CLOSED (T-653) | bank PATCH era 06: Winter, SAGE American Masculinities (2004): Kraditor coined it 1968, Welter 1966 'cult of true womanhood'; prose does not attribute the term, unchanged |

## Sources in hand

## Gaps researched

## Decisions and defects fixed

## Log

- 2026-10-26 | items 1-8 | prose changed: food-farming part3 (Rodgers arrest), government-politics part3 (IDEA state laws), home-family part1 (earth lodge size); banks patched in all five | validator 0 errors each | --punct 0/0 each | --check prose + research PASS for all five slugs
