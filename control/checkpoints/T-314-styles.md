# CHECKPOINT T-314 | styles | prose | ONE writer, all 10 eras (part1, part2, part3)

STATUS: T-314 landed (director verified: PASS  styles / prose)
VERIFY: python tools/project_state.py --check styles --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/styles/part1-before-1800.md (eras 1-5) · manuscript/styles/part2-1800s.md (eras 6-7)
        · manuscript/styles/part3-1900s-and-today.md (eras 8-10) · research/research-styles.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    finished. All 11 units done.
NEXT:   director: commit.

## Research state before writing (2026-09-29)

PASS  styles / research
measured: stage=RESEARCHED eras=10/10 stories=16 (v16 c0 t0) verify_tags=0 bank=24824w outline=16797w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-314 | done | 957w, 0 errors, punct 0/0 |
| 2 | era 02 1500s -> part1 | T-314 | done | 911w, 0 errors, punct 0/0 |
| 3 | era 03 1600s -> part1 | T-314 | done | 1627w, 0 errors, punct 0/0 |
| 4 | era 04 1700-1750 -> part1 | T-314 | done | 1033w, 0 errors, punct 0/0 |
| 5 | era 05 1750-1800 -> part1 | T-314 | done | 1289w, 0 errors, punct 0/0 |
| 6 | era 06 1800-1850 -> part2 | T-314 | done | 1709w, 0 errors, punct 0/0 |
| 7 | era 07 1850-1900 -> part2 | T-314 | done | 1949w, 0 errors, punct 0/0 |
| 8 | era 08 1900-1950 -> part3 | T-314 | done | 2057w, 0 errors, punct 0/0 |
| 9 | era 09 1950-2000 -> part3 | T-314 | done | 2679w, 0 errors, punct 0/0 |
| 10 | era 10 2000-today -> part3 | T-314 | done | 2179w, 0 errors, punct 0/0 |
| 11 | final: self-review, --punct, validator, prose check | T-314 | done | 16665w total, 0/0/0 errors, PASS styles / prose |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 01 | was quillwork done before contact (outline cited a search summary) | PATCH | "PATCH 2026-09-29 (T-314): quillwork before contact, confirmed"
- 03 | Herrera Horta's 1601 testimony on blankets taken off women (unconfirmed) | PATCH (paraphrase only, TWU page citing Hammond and Rey) | "PATCH 2026-09-29 (T-314): Herrera Horta's 1601 testimony"
- 10 | Rana Plaza Delaware suit dismissal (search summary only) | PATCH (Business and Human Rights Resource Centre case page) | "PATCH 2026-09-29 (T-314): the Delaware Rana Plaza suit"
- 10 | 97 percent of clothes and shoes imported (search summary only) | PATCH (AP via Yahoo Finance, April 2025) | "PATCH 2026-09-29 (T-314): share of clothes and shoes imported"
- 09 | who moved the Pawnee to Indian Territory (bank said only 'forced') | PATCH (Parks, Oklahoma Historical Society) | "PATCH 2026-09-29 (T-314): who moved the Pawnee"
- 02 | Secotan weroance "painted, not tattooed", copper beads or pearls | not confirmed after 2 tries, left out (minor) | none

## OPEN (should be rare)

## Outline claims left out
- 02: Secotan leader's body paint and copper beads or pearls (search summary only, 2 tries). Onate's flock of about 5,000 (search summary only).
- 03: none beyond wording.
- 05: Great Seal eagle on Federal furniture, Hepplewhite 1788 and Sheraton 1793 dates (search summary only). Tignon as 'the kind of head covering enslaved women wore' (not in bank).
- 06: Northern demand spurring slavery's growth (NPS search summary). Anna Murray sewing the outfit (search summary only).
- 07: Davis's 1872 letter and patent fee, Ho Ah Kow's $10,000, Carlisle 'after' hairstyles, Singer $5 down/$3 terms and $500 family income (all search summary only).
- 08: Jones's 'guardhouse at hard labor', Josephine Lee, zoot suit ban with a 30-day term (search summary only).
- 10: the $800 de minimis rule (its link to clothes is search-summary framing only). 'Facts current to September 2026' sentence (self-reference). Count: 15.

## Decisions and defects fixed
- Chapter heading: outline says 'Chapter 33' but id is 35 (and Music is 33). Prose uses 'Chapter 35', matching the id as the other manuscripts do.
- Outline personified institutions (General Court, county court, school, Library of Congress, War Production Board, DuPont, NWHM): prose names members, judges, officials, or attributes the statement.
- Outline: quillwork regions and pre-contact date were search summary only: confirmed pre-contact (PATCH), used the nations Penn Museum names instead of regions.
- Outline: red ochre 'mixed with fat' not in bank: dropped. Cochineal 'prickly-pear, crushed' not in bank: dropped.
- Outline: Douglass 'Lloyd enslaved him' implied: prose says Lloyd's home plantation only.
- Outline: Pawnee 'forced onto' land (Wikipedia only): prose gives the Parks account (Sioux attacks, agent chose the site). Evidence mixed, 'forced' not used.
- Keckley: outline 'forced himself on her' made plain as 'forced her to have sex with him', her refusal to name him quoted.
- Michael Eugene Thomas: Wikipedia's sexual-assault detail left out, per the bank's note assigning it to crime-justice. Director may review.

## TO PARK (for the director, burst runs only)

## Log
- 2026-09-29 era 01: 957 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH quillwork pre-contact.
- 2026-09-29 era 02: 911 words, validator 0 errors, --punct emdash=0 semicolon=0. No new PATCH. Left out Secotan body-paint and pearls line and Oñate flock size (search summary only).
- 2026-09-29 era 03: 1627 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH Herrera Horta (paraphrased). Stories mary-ring-styles, hannah-lyman-1676.
- 2026-09-29 era 04: 1033 words, validator 0 errors, --punct emdash=0 semicolon=0. No new PATCH. Story jack-gambia-1745.
- 2026-09-29 era 05: 1289 words, validator 0 errors, --punct emdash=0 semicolon=0. No new PATCH. Stories charity-clarke, george-washington-styles. Left out Great Seal eagle line and Hepplewhite/Sheraton dates (search summary only). Part1 self-review run: era openings varied, institutions checked (General Court, county courts rewritten with members, judges).
- 2026-09-29 era 06: 1709 words, validator 0 errors, --punct emdash=0 semicolon=0. No new PATCH. Story frederick-douglass-styles. Anna Murray told from the fetched Encyclopedia citation only (sewing version is search summary only). Northern demand spurring slavery (NPS search summary) left out, Sumner quote kept.
- 2026-09-29 era 07: 1949 words, validator 0 errors, --punct emdash=0 semicolon=0. No new PATCH. Stories elizabeth-keckley, levi-strauss-jacob-davis. Left out (search summary only): Davis's 1872 letter and the patent fee, Ho Ah Kow's $10,000 award, Carlisle 'after' hairstyles, $500 family income and $5 down/$3 terms. Part2 self-review run.
- 2026-09-29 era 08: 2057 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCHes for era 10 made now (Delaware suit, 97 percent). Stories madam-cj-walker, wallace-carothers, ann-lowe. Left out (search summary only): Jones's 'guardhouse at hard labor', Josephine Lee, the zoot suit ban with a 30-day term.
- 2026-09-29 era 09: 2679 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH Pawnee move. Stories charles-ray-eames, mary-beth-tinker, rotchana-cheunchujit-sussman. Ann Lowe 1953 told as a span.
- 2026-09-29 era 10: 2179 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCHes Delaware suit and 97 percent. Stories francisco-tzul, andrew-johnson-wrestler. Every figure carries a year and a named source.
- 2026-09-29 final: self-review run on all three files (era openings varied, institution subjects rewritten, document-element verbs fixed, hard words defined). PASS styles / prose, 16,665 words.
