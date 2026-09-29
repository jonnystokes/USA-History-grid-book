# CHECKPOINT T-308 | money | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-308a landed (director verified: FAIL  money / prose)
VERIFY: python tools/project_state.py --check money --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/money/part1-before-1800.md (eras 1-5) · manuscript/money/part2-1800s.md (eras 6-7)
        · manuscript/money/part3-1900s-and-today.md (eras 8-10) · research/research-money.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-308a done 2026-09-29 (units 1-7, self-review run). Waiting for T-308b.
NEXT:   T-308b: Unit 8 (era 08 1900-1950 -> create manuscript/money/part3-1900s-and-today.md, file="part3"). Copy the hb-chapter/heading/hb-note layout of part2-1800s.md. Open era 08 with the Gold Standard Act of March 14, 1900 (left out of era 07 by the boundary rule). Voice notes: actors are always named people ("members of Congress", "officers of the bank"), no institution as subject of a human verb. Legal tender, national bank, charter, bank run, suspension, deposit insurance, gold standard, veto, bond, mortgage, collateral are already defined in parts 1-2: do not define again at length. Unit 11 (self-review, prose check) is B's.

## Research state before writing (2026-09-29)

PASS  money / research
measured: stage=RESEARCHED eras=10/10 stories=12 (v12 c0 t0) verify_tags=0 bank=14662w outline=7377w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-308a | done | 300w (file), 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-308a | done | file 746w, 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-308a | done | file 1574w, 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-308a | done | part1-before-1800.md 2300w, 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-308a | done | part1-before-1800.md 3414w, 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-308a | done | part2-1800s.md 2280w, 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-308a | done | part2-1800s.md 4027w, 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-308b | todo | |
| 9 | era 09 1950-2000 -> part3 | T-308b | todo | |
| 10 | era 10 2000-today -> part3 | T-308b | todo | |
| 11 | final: self-review, --punct, validator, prose check | T-308b | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 02 | who dug the Potosí silver (outline said only "Spain found silver") | PATCH | who dug the silver at Potosí
- 02 | how many mita workers died | SEARCHED, NOT FOUND | how many forced workers died in the Potosí mines
- 05 | Sullivan's ear-cropping and branding (was unconfirmed) | PATCH | Owen Sullivan's ears and cheeks, confirmed
- 05 | Hamilton as first Treasury Secretary; full names Madison, Washington | PATCH | Hamilton's office
- 06 | Allison's end (debtors' prison, was unconfirmed) | PATCH | David Allison's end
- 06 | where Jackson's 68,000 acres lay, whose land | SEARCHED, NOT FOUND | where the 68,000 acres ... lay
- 06 | who sold mortgaged enslaved people after 1837 | PATCH (Baptist wording) + SEARCHED, NOT FOUND (seller) | forced sales after 1837 / who ran the sales
- 06 | 1807 cession includes Ann Arbor (was unconfirmed) | PATCH | the 1807 cession included Ann Arbor
- 07 | Bryan's status in 1896 | PATCH (correction: former congressman) | Bryan was a former congressman
- 07 | Secret Service first chief; who shot McKinley | PATCH | the Secret Service's first chief, and who shot McKinley

## OPEN (should be rare)

## Outline claims left out
- 04: "London merchants who were paid in this shrinking paper complained to Parliament" and "paper money became one of the running arguments": not in the bank. Left out.
- 07: Gold Standard Act of 1900 (Bryan story last line): era 08 by the boundary rule, per the bank. Left for T-308b.

## Decisions and defects fixed
- 02: outline/bank "Spain found silver at Potosí" left out that Indigenous men were forced to dig it (mita). Researched and written with Toledo named.
- 07: bank called Bryan "the Nebraska congressman" in 1896. He was a former congressman (Miller Center). Prose says former. Outline's "the next day" for the nomination is not in the bank: dropped.
- 07: Bryan's quote contains a semicolon. Split into two quotations at that point, no word changed.
- 06: two sources give the 1807 cession size (about 8 million acres, NHBP. 5,611,532 acres, AADL). Both stated.
- 06: forced sales of mortgaged people after 1837: the seller is not named in the usable sources. Prose says the accounts do not name who ran each sale. A Yale workshop draft (Murphy 2017) describes sheriff's sales but carries a do-not-cite notice, so it was not used.
- 06: Jackson's 68,000 acres: nation not identified. Prose says so.
- Outline personification throughout ("Massachusetts printed", "Congress created", "Parliament banned", "the crown revoked") rewritten with named people or members of the body.
- Outline Franklin "Philadelphia" not in the money bank: prose says Pennsylvania.
- Rockoff's conditional $1 million Michigan estimate left out as too tangled for the reader. The AADL 60 percent and Dove et al. $350,000 are given.

## TO PARK (FILED by the director, 2026-09-27)
- crime-justice: Owen Sullivan's Rhode Island ear-cropping and branding now confirmed (Boston Evening Post, Oct 9, 1752), see research-money.md era 5 PATCH 2026-09-29.
- crime-justice / government-politics: Czolgosz shot McKinley Sept 6, 1901 (Miller Center), research-money.md era 7 PATCH.
- economy / slavery-freedom: Baptist's "bankruptcy-driven sales" wording and the do-not-cite status of Murphy's 2017 Yale draft, research-money.md era 6.
- native-nations / land-environment: AADL 1807 Treaty of Detroit figures (5,611,532 acres, $57,717.32, Ann Arbor included), research-money.md era 6.

## Log
- 2026-09-29 T-308a: bank PATCHes written before prose: Potosí mita (era 2), Sullivan ears and branding confirmed (era 5), Hamilton's office and Madison/Washington names (era 5), Baptist forced-sales wording (era 6), 1807 cession includes Ann Arbor (era 6). SEARCHED, NOT FOUND: Potosí death count (era 2), who ran the Louisiana forced sales (era 6).
- 2026-09-29 T-308a: era 01 written. part1 300 words, validator 0 errors, emdash=0 semicolon=0.
- 2026-09-29 T-308a: era 02 written (Potosí mita added from PATCH). part1 746 words, validator 0 errors, emdash=0 semicolon=0.
- 2026-09-29 T-308a: era 03 written, story john-hull. part1 1574 words, validator 0 errors, emdash=0 semicolon=0.
- 2026-09-29 T-308a: era 04 written. story benjamin-franklin-money. part1-before-1800.md 2300 words, validator 0 errors, emdash=0 semicolon=0.
- 2026-09-29 T-308a: era 05 written. stories alexander-hamilton-money; Owen Sullivan in hb-zoom (no story block in outline). part1-before-1800.md 3414 words, validator 0 errors, emdash=0 semicolon=0.
- 2026-09-29 T-308a: era 06 written. stories andrew-jackson-money, alpheus-felch-money; new span on the 1807 Treaty of Detroit land. part2-1800s.md 2280 words, validator 0 errors, emdash=0 semicolon=0.
- 2026-09-29 T-308a: era 07 written. stories emanuel-ninger, william-jennings-bryan. part2-1800s.md 4027 words, validator 0 errors, emdash=0 semicolon=0.
- 2026-09-29 T-308a: self-review run on part1 and part2 (cadence, institutions as subjects, repeated era openings, passives on harm, hard words, tells). Fixes applied. Final: part1 0 errors, part2 0 errors, both emdash=0 semicolon=0.
