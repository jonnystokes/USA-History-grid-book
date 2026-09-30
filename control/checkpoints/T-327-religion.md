# CHECKPOINT T-327 | religion | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-327a landed (director verified: FAIL  religion / prose)
VERIFY: python tools/project_state.py --check religion --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/religion/part1-before-1800.md (eras 1-5) · manuscript/religion/part2-1800s.md (eras 6-7)
        · manuscript/religion/part3-1900s-and-today.md (eras 8-10) · research/research-religion.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-327a done (units 1-7 landed, both files self-reviewed).
NEXT:   T-327b: unit 8

## Research state before writing (2026-09-29)

PASS  religion / research
measured: stage=RESEARCHED eras=10/10 stories=18 (v18 c0 t0) verify_tags=0 bank=61630w outline=22218w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-327a | done | 872w, validator 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-327a | done | 1157w, validator 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-327a | done | 4420w, validator 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-327a | done | 2517w, validator 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-327a | done | 3880w, validator 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-327a | done | 4627w, validator 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-327a | done | 3146w, validator 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-327b | todo | |
| 9 | era 09 1950-2000 -> part3 | T-327b | todo | |
| 10 | era 10 2000-today -> part3 | T-327b | todo | |
| 11 | final: self-review, --punct, validator, prose check | T-327b | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- era 6 | Charlestown 1834 and Philadelphia 1844 mob facts, counts by source, trials | PATCH (copied from immigration bank T-238 with sources) | ERA 6 end, "PATCH 2026-09-30 (T-327a): the 1834 and 1844 anti-Catholic attacks"
- era 6 | whose land was Nauvoo | PATCH (Wikipedia, opened; two searches for an institutional source found none) | ERA 7 end, "PATCH 2026-09-30 (T-327a): Nauvoo's land"
- era 7 | Louisville 1855 | PATCH (KHS marker, copied from immigration bank) | ERA 7 end

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

## TO PARK (for the director, burst runs only)

## Log

- 2026-09-30 T-327a unit 1 before-1500: 872 words, validator 0 errors, --punct emdash=0 semicolon=0. No research needed. Outline lines "circles, squares, and octagons" and "large enough to hold a crowd" (Hopewell) not in bank: left out.
- 2026-09-30 T-327a unit 2 1500s: 1157 words, validator 0 errors, --punct emdash=0 semicolon=0. Used bank PATCHes (Mendez de Canzo 1597 response, Lucas hanged 1598, Matanzas pointer). No new research. Nombre de Dios friar's first name (bank conflict) not printed. Juanillo not named (bank ruling).
- 2026-09-30 T-327a unit 3 1600s: 4420 words, validator 0 errors, --punct emdash=0 semicolon=0 (one semicolon inside the Hutchinson charge quote split at the mark; IPCC quote split the same way). Used PATCHes: Quakers (Linder/Bishop), Leighton, Posada/Trevino, Virginia 1667, Deer Island, whose land. No new research.
- 2026-09-30 T-327a unit 4 1700-1750: 2517 words, validator 0 errors, --punct emdash=0 semicolon=0. Used PATCHes: Apalachee 1704 (every count with its owner; perpetrators SEARCHED, NOT FOUND already in bank), John Ury 1741, Stockbridge Mohican land. Missions-destroyed count conflict (DAH all but one vs Wikipedia two left) written as 'nearly all'. Edwards Center 'agent in depriving Native Americans' line (search indexing only) not used. Faithful Narrative year not printed (bank conflict).
- 2026-09-30 T-327a unit 5 1750-1800: 3880 words, validator 0 errors, --punct emdash=0 semicolon=0. Used PATCHes: California missions (MPDF), Kumeyaay 1775, Toypurina, Gnadenhutten, Clarke 1790 letter (about fifty whipped; 575 followers explained), first-claims check. Silver Bluff (search summary only) not used. Serra 1780 letter (unconfirmed) not used. No new research.
- 2026-09-30 T-327a part1 self-review (Version 2 checklist + amendment 5): fixed institution-as-actor lines (court, General Court, IPCC, New Mexico statue, missions), 'many' hedges, repeated doctrina definition, era-opening shapes; moved Apalachee 1704 span to the front of era 4 and Gnadenhutten 1782 before the California missions for chronology. Final part1: 12,877 words, validator 0 errors, emdash=0 semicolon=0.
- 2026-09-30 T-327a unit 6 1800-1850: 4627 words, validator 0 errors, --punct emdash=0 semicolon=0. Research: 2 web searches + 1 fetch (Nauvoo land). Olbes and Zalvidea first names not printed (bank). Crooked River date 25 Oct is search-summary only in bank: not printed; prose says 'shortly before the end of October'.
- 2026-09-30 T-327a unit 7 1850-1900: 3146 words, validator 0 errors, --punct emdash=0 semicolon=0. Part 2 self-review done (LOC Latrobe quote re-attributed to LOC, Shakers origin fixed, institution-as-actor lines fixed, 'many' hedges cut, Reynolds span moved for chronology). Final part2: 7,764 words.

## HANDOFF to T-327b (eras 8-10, part3)

- Voice: plain present-day, one idea per sentence, averages 12-16 words; spans labeled with a plain noun phrase; stories open with the one-line teaching point, then dates.
- Terms ALREADY DEFINED in parts 1-2 (do not redefine): missionary, archaeologist, mission, baptism/baptized, friar, catechism, doctrina, flogging (era 3, with method), branding, pillory, established church, revival, Great Awakening, new birth, deist, ordained, heresy, banished, excommunicated, Trinity, toleration, charter, communion, inoculation, remonstrance, religious test, First Amendment religion clauses (meaning given), evangelicalism, camp meeting, tract, nativist, Know-Nothings, tarring and feathering, exterminate, secularization, bigamy, rabbi, synagogue, yeshiva, Talmud, kosher, Orthodox, pogrom, anti-Semitism, parish school, sect/sectarian, rations, assimilate, boarding school, Ghost Dance, Taoism, stocks, hobbling, shackles, militia.
- Threads that continue after 1900: (1) Native ceremonies banned by the 1883 Rules, enforceable until the 1978 American Indian Religious Freedom Act (part2 says so; era 9 should tell the Act). (2) Church-run Indian boarding schools: DOI 2024 counts (417 / 210 / 59 bodies / 132 Protestant, 77 Catholic) and the .3 billion already given in era 7; era 10 has the 2022-2024 apologies (bank §7e). Do not repeat the counts. (3) Catholic parish schools (1884 council, Blaine amendments in 37 states) -> Oregon 1922 / Pierce 1925 and later aid cases. (4) Bible reading in public schools (Philadelphia 1844) -> Engel 1962 / Schempp 1963. (5) Latter-day Saints: Reynolds (belief vs practice) told; Edmunds-Tucker left to rights-movements. (6) Jewish institutions and anti-Semitism (Grant 1862, Seligman 1877) -> Leo Frank era 8. (7) AME and Black congregations (Allen, Jones, Savannah 1865) -> Azusa Street / civil-rights congregations. (8) California missions: counts 1769-1834 (85,840 baptisms, 59,538 deaths) are in era 5; Cook's 310,000 -> 150,000 by 1845 in era 6.
- Stories written: dona-maria-melendez, mary-dyer (new), roger-williams, anne-hutchinson-religion, george-whitefield, jonathan-edwards, richard-allen, absalom-jones, toypurina (new), joseph-smith, charles-grandison-finney, garrison-frazier.
