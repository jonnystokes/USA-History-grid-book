# CHECKPOINT T-304 | home-family | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-304a landed (director verified: FAIL  home-family / prose)
VERIFY: python tools/project_state.py --check home-family --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/home-family/part1-before-1800.md (eras 1-5) · manuscript/home-family/part2-1800s.md (eras 6-7)
        · manuscript/home-family/part3-1900s-and-today.md (eras 8-10) · research/research-home-family.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-304a: DONE 2026-09-29. part1 (eras 1-5) and part2 (eras 6-7) written, self-reviewed, validator 0 errors each, --punct 0/0 each.
NEXT:   T-304b: Unit 8 (era 08 1900-1950) -> create manuscript/home-family/part3-1900s-and-today.md. Copy part2's hb-chapter line with file="part3". Voice notes from writer A: the discipline shift of the 1920s-30s was left for era 08 (part2 stops at 1800s advice manuals). Rogarshevsky (97 Orchard, TB 1918) and the 1935 closing belong to era 08. part2 already told 97 Orchard's build date, the 1879 and 1901 laws, the 1870 servant count and the 1890 running-water figure (24%): do not repeat them. Buffalo Bird Woman's story already runs to 1921 and her death in 1932.

## Research state before writing (2026-09-29)

PASS  home-family / research
measured: stage=RESEARCHED eras=10/10 stories=16 (v16 c0 t0) verify_tags=0 bank=12701w outline=5460w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-304a | done | 470w, validator 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-304a | done | 363w, validator 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-304a | done | 803w, validator 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-304a | done | 346w, validator 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-304a | done | 651w, validator 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-304a | done | 1503w, validator 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-304a | done | 1371w, validator 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-304b | todo | |
| 9 | era 09 1950-2000 -> part3 | T-304b | todo | |
| 10 | era 10 2000-today -> part3 | T-304b | todo | |
| 11 | final: self-review, --punct, validator, prose check | T-304b | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 01 | Taos Pueblo location and adobe; longhouse family rules | PATCH | "PATCH 2026-09-29 (T-304a): Taos Pueblo place and adobe, and the longhouse family"
- 02 | Seloy landing (whose land), Camacho household details | PATCH (26 women, not 24) | "PATCH 2026-09-29 (T-304a): Seloy's town and the Camacho household"
- 03 | Patuxet, the 1616-1619 epidemic, Hunt's 1614 kidnapping | PATCH | "PATCH 2026-09-29 (T-304a): Patuxet, the epidemic and the kidnapping"
- 05 | what the 1776 smallpox inoculation was and did | PATCH | "PATCH 2026-09-29 (T-304a): Abigail Adams and the 1776 inoculation"
- 05 | which nation lived at Hallowell, Maine | SEARCHED, NOT FOUND | "SEARCHED, NOT FOUND 2026-09-29 (T-304a): which Native nation lived at Hallowell"
- 06 | the exact "spare the rod" verse | PATCH | "PATCH 2026-09-29 (T-304a): the spare the rod verse"
- 07 | how a sod house was built; Spirit Lake bands | PATCH | "PATCH 2026-09-29 (T-304a): how a sod house was built, and the Spirit Lake bands"

## OPEN (should be rare)

## Outline claims left out
- 02: "many married Timucua" women (NPS names no nation for the wives; wrote "Native women").
- 03: "birth and death all happened in the same space"; "schooling at a kitchen table" (neither in bank).
- 04: Knight rode "alone" (not in bank; she is known to have hired guides). "Privacy invented here" kept only as privacy for the wealthy.
- 05: contents of the Adams letters (crops, tenants, shortages: outline only, not bank). "Store-bought would start replacing homemade" (next century, not in bank). Household-production span folded into the era text (would have repeated era 04's span).
- 06: "childhood as a time to protect"; "most farm and working households could not live this way" (not in bank). Stove saved fuel / wood shortage (search summary only). The 1920s-30s discipline shift left to era 08.
- 07: Ingalls "family of five"; the $413 buy-and-resell of 1876 (confusing, not needed); tuberculosis as the 1900 commission's concern (search summary only); Massachusetts law as "first" (not in bank).
Count: 12.

## Decisions and defects fixed
- Bank 1565 party "24 women": opened Florida Museum page says 26. Wrote 26, PATCH records the correction.
- Bank "epidemic about 1614-1620" and Tisquantum "the only Patuxet still alive": CDC EID gives 1616-1619 and "one of the last of the Patuxets". Wrote those.
- Outline/bank "Proverbs' spare the rod": the phrase is not in Proverbs. Quoted Proverbs 13:24 (KJV) exactly and explained it.
- Buffalo Bird Woman lodge quote: bank replaced the original dash with parentheses. Paraphrased instead of printing altered punctuation inside quote marks.
- Buffalo Bird Woman 1921 quote contains a semicolon: split at it, words unchanged.
- Personification in outline ("Massachusetts passed", "Congress authorized", "the law required a toilet", "war took men away") repaired with named people (legislators, members of Congress, owners, men who left).
- Bank correction honored: "open hearth largely gone by the Civil War" not written. Petticoat-fire myth not written.
- Mary Ring story enriched from the styles bank's opened inventory (PATCHed into our bank first, with source).
- Land named for every newcomer settlement: Seloy (Timucua), Patuxet (Wampanoag), New Sweden (Lenape), Walnut Grove (Dakota, 1851), Devils Lake (Spirit Lake Dakota). Hallowell left unnamed (SEARCHED, NOT FOUND).

## TO PARK (for the director, burst runs only)
- native-nations / slavery-freedom: Florida Museum "First Contacts" page (opened 2026-09-29) confirms Menendez's ~800 colonists included 26 women and an unknown number of enslaved Africans, and that Seloy's council house was the first Spanish fort. Plymouth 400, Inc. (opened) gives Hunt's 1614 capture as 20 from Patuxet and 7 from Nauset. Full text: research-home-family.md, eras 02 and 03 T-304a PATCHes.
- health: 1776 inoculation method (lancet, pus-soaked thread) and death rates (about 30% natural smallpox, 2-3% inoculation), Journal of the American Revolution, April 2026. research-home-family.md era 05 T-304a PATCH.

## Log
- 2026-09-29 T-304a unit 1: era 01 written (3 spans: longhouse, earth lodge, pueblos/wigwams/tipis; no story, as outlined). 470w. validate_grid --part: 0 errors. --punct: emdash=0 semicolon=0.
- 2026-09-29 T-304a unit 2: era 02 written (span St. Augustine in Seloy's town, story Camacho). 363w. validator 0 errors. --punct emdash=0 semicolon=0.
- 2026-09-29 T-304a unit 3: era 03 written (spans Patuxet, one room then two, big families; story Mary Ring, with inventory lines from the styles bank PATCHed in). 803w. validator 0 errors. --punct emdash=0 semicolon=0.
- 2026-09-29 T-304a unit 4: era 04 written (spans Georgian house, hearth as workplace; story Sarah Kemble Knight). 346w. validator 0 errors. --punct emdash=0 semicolon=0.
- 2026-09-29 T-304a unit 5: era 05 written (span log cabin with Lenape land; household production folded into the era text; stories Abigail Adams with the 1776 inoculation defined, Martha Ballard). 651w. validator 0 errors. --punct emdash=0 semicolon=0. part1 complete.
- 2026-09-29 T-304a unit 6: era 06 written (spans parlor/domesticity, stove, child's day with Proverbs 13:24 quoted, home under slavery; stories Catharine Beecher, Buffalo Bird Woman). 1503w. validator 0 errors. --punct emdash=0 semicolon=0.
- 2026-09-29 T-304a unit 7: era 07 written (spans tenement flat, Victorian house and help, sod houses and dugouts with Dakota 1851 treaty land, the law reaches for the children; stories Gumpertz, Calof with Spirit Lake land). 1371w. validator 0 errors. --punct emdash=0 semicolon=0.
- 2026-09-29 T-304a: self-review run on both files (read-aloud, shapes, document-element verbs, institutions as subjects, passives, hard words, softening, repeated era openings). Repairs applied. Final: part1 validator 0 errors, emdash=0 semicolon=0. part2 validator 0 errors, emdash=0 semicolon=0. Words: part1 2632, part2 2879.
