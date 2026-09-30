# CHECKPOINT T-319 | crime-justice | prose | ONE writer, all 10 eras (part1, part2, part3)

STATUS: T-319 landed (director verified: PASS  crime-justice / prose)
VERIFY: python tools/project_state.py --check crime-justice --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/crime-justice/part1-before-1800.md (eras 1-5) · manuscript/crime-justice/part2-1800s.md (eras 6-7)
        · manuscript/crime-justice/part3-1900s-and-today.md (eras 8-10) · research/research-crime-justice.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-319 complete.
NEXT:   director: commit; audit step.

## Research state before writing (2026-09-29)

PASS  crime-justice / research
measured: stage=RESEARCHED eras=10/10 stories=13 (v13 c0 t0) verify_tags=0 bank=31451w outline=15260w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-319 | done | 605w, validator 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-319 | done | 689w, validator 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-319 | done | 2662w, validator 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-319 | done | 1456w, validator 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-319 | done | 1898w, validator 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-319 | done | 1712w, validator 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-319 | done | 3369w, validator 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-319 | done | 3192w, validator 0 errors, emdash=0 semicolon=0 |
| 9 | era 09 1950-2000 -> part3 | T-319 | done | 4160w, validator 0 errors, emdash=0 semicolon=0 |
| 10 | era 10 2000-today -> part3 | T-319 | done | 3137w, validator 0 errors, emdash=0 semicolon=0 |
| 11 | final: self-review, --punct, validator, prose check | T-319 | done | 23057w total, 3 files 0 errors, emdash=0 semicolon=0, PASS |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 05 | Owen Sullivan's Rhode Island ears and branding | PATCH (copied from money bank T-308a) | "PATCH 2026-09-30 (T-319): Owen Sullivan's ears and cheeks, confirmed"
- 07 | New Orleans 1891 lynching, justice side | PATCH (copied from holidays bank T-273b) | "PATCH 2026-09-30 (T-319): New Orleans, 14 March 1891"

## OPEN (should be rare)
- none

## Outline claims left out
- 03: Jamestown death for sodomy (not needed); trials declared unlawful 1702 (no actor in bank); Percy's account 'the only one' (not in bank).
- 04: Virginia 1692 no-jury courts (search summary only); county courts 'tried local crimes' (not supported by Encyclopedia Virginia).
- 06: Nat Turner 53/18/12/21 counts (search summary only; Breen's counts used); Lighthorse name; NY 800-man force.
- 07: draft-riot trials (SNF); LA 1871 'California Supreme Court' overturned (not in bank).
- 08: Tulsa 'when a shot was fired'; Fall 'bribery' charge; Capone 'paid police'; FBI name date 1935 (summary only).
- 09: Kemba Smith 'finished college / voting work'; Wounded Knee 'Oglala Lakota people held the village'; Nixon quote (unconfirmed).
- 10: Florida 19 of 47 executions (summary only); Fletcher's 2021 quote (not in this bank); Arredondo trial date (summary only).

## Decisions and defects fixed
- Quaker ears 1658: this bank says 'hangman's deputy', religion bank says Marshal's deputy; prose says 'a court officer'.
- Outline 'No one was punished for Tulsa' vs Gustafson's conviction: prose says no white person was sent to prison.
- Outline Nat Turner counts were search-summary only: replaced with Encyclopedia Virginia (Breen) counts, and the three-dozen vs hundreds dispute stated.
- Personified institutions throughout the outline (courts, the Nation, laws, the Bureau) rewritten with people as actors.
- Parked material told in full: Michael Eugene Thomas (1989), New Orleans 1891, Owen Sullivan's punishment, Springfield 1908, Marion 1930, Teapot Dome, civil-rights killers' trials, Michael Stewart 1983, Danziger Bridge 2005, Ferguson DOJ report, school-shooting prosecutions.

## TO PARK (for the director, burst runs only)

## Log
- 2026-09-30 era 01: 605w, validator 0 errors, --punct emdash=0 semicolon=0. Bank PATCHes added before writing: era 5 "Owen Sullivan's ears and cheeks, confirmed" (from money bank), era 7 "New Orleans, 14 March 1891" (from holidays bank).
- 2026-09-30 era 02: 689w, validator 0 errors, --punct emdash=0 semicolon=0. Matanzas 1565 told in one short span (bank allows one line, Shared with war/america-world).
- 2026-09-30 unit 3: 2662w, validator 0 errors, emdash=0 semicolon=0. Stories philip-ratcliffe, rebecca-nurse. Quaker ears: bank says hangman's deputy, religion bank says Marshal's deputy; prose says a court officer. Jamestown sodomy item and 1702 unlawful declaration (no actor) left out.
- 2026-09-30 unit 4: 1456w, validator 0 errors, emdash=0 semicolon=0. Story quack-and-cuffee. PATCH: what the Virginia county courts did (Encyclopedia Virginia, WebFetch): outline's county court 'tried local crimes' not supported, prose says licenses, deeds, wills, land and debt quarrels. Virginia 1692 no-jury courts left out (search summary only in bank).
- 2026-09-30 unit 5: 1898w, validator 0 errors, emdash=0 semicolon=0. Story patrick-lyon. Sullivan's ears and C brands written from the new PATCH.
- 2026-09-30 unit 5r: 0w, validator 0 errors, emdash=0 semicolon=0. Part1 self-review run: fixed personified courts/records/laws (courts -> judges, record 'says/gives/settles' -> states/records), 'European law reached', county courts sentence, 'the point was', grand jury definition moved to first use (1741), Bill of Rights verbs. Part1 totals: 7292w, validator 0 errors, emdash=0 semicolon=0.
- 2026-09-30 unit 6: 1712w, validator 0 errors, emdash=0 semicolon=0. Story charles-williams. PATCH: Southampton trial counts from Encyclopedia Virginia (Breen): 30 enslaved + 1 free condemned, 19 executed, 12 commuted; about three dozen killed without trial (vs Library of Virginia 'hundreds'); 55 vs 57 whites. Outline's 53/18/12/21 counts were search-summary only and are not used. Lighthorse name (search summary only) and NY 800-man figure left out.
- 2026-09-30 unit 7: 3369w, validator 0 errors, emdash=0 semicolon=0. Stories allan-pinkerton, henry-smith. New span: New Orleans 1891 (from the PATCH). Outline defects fixed: LA 1871 verdicts 'thrown out by the California Supreme Court' not in bank (prose: overturned on a technicality); draft riots 'police held back the mob so the children got out' not in bank (prose: children all got out). Draft-riot trials SNF honored (left out). Wilmington 1898, Portland Rum Riot, Carthage 1844 parked items not told (other chapters lead, bank has pointer only).
- 2026-09-30 unit 7r: 0w, validator 0 errors, emdash=0 semicolon=0. Part2 self-review run: states/cities/courts as actors named as officials/judges, 'law set' -> 'law specified', tribunal defined. Part2 validator 0 errors, emdash=0 semicolon=0.
- 2026-09-30 unit 7s: 0w, validator 0 errors, emdash=0 semicolon=0. Slice 8-10 read. PATCH era 9: Michael Eugene Thomas killing (styles bank + Wikipedia 'James David Martin' WebFetch).
- 2026-09-30 unit 8: 3192w, validator 0 errors, emdash=0 semicolon=0. Stories ed-johnson, eliot-ness-al-capone. Added spans from parked bank material: Springfield 1908 and Marion 1930 (mobs and the courts), Teapot Dome 1929 (cabinet member convicted). Deputy Dial quote split at its semicolon, no word changed. Outline defects fixed: Tulsa 'when a shot was fired' not in bank (dropped); Fall 'convicted of bribery' not in bank (prose: convicted). Outline said Capone 'paid police and officials' (not in bank, left out).
- 2026-09-30 unit 9: 4160w, validator 0 errors, emdash=0 semicolon=0. Stories emmett-till, clarence-earl-gideon, kemba-smith. New spans from parked material: civil-rights killers in court (PATCH copied from rights-movements bank), Michael Eugene Thomas 1989 (PATCH), Michael Stewart 1983 (art park). Outline defects fixed: 'Mississippi kept women off' (actor unknown, passive kept); Kemba Smith 'while pregnant turned herself in' and 'finished college/worked to restore the vote' not in bank (dropped, pregnancy-timing dispute stated); Wounded Knee 'Oglala Lakota people held the village' not in bank.
- 2026-09-30 unit 9s: 0w, validator 0 errors, emdash=0 semicolon=0. PATCH era 10: prosecutions after three school shootings (copied from education bank T-261e).
- 2026-09-30 unit 10: 3137w, validator 0 errors, emdash=0 semicolon=0. Story exonerated-five. New spans from parked material: Danziger Bridge 2005, Ferguson DOJ report 2015, prosecutions after school shootings (PATCH). Outline defects fixed: Florida '19 of 47' executions (search summary only, dropped); Fletcher's quote not in crime bank (dropped); 'No one was punished for Tulsa' contradicted Gustafson's conviction (prose: no white person sent to prison).
