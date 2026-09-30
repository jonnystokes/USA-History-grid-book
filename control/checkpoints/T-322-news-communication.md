# CHECKPOINT T-322 | news-communication | prose | ONE writer, all 10 eras (part1, part2, part3)

STATUS: T-322 landed (director verified: PASS  news-communication / prose)
VERIFY: python tools/project_state.py --check news-communication --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/news-communication/part1-before-1800.md (eras 1-5) · manuscript/news-communication/part2-1800s.md (eras 6-7)
        · manuscript/news-communication/part3-1900s-and-today.md (eras 8-10) · research/research-news-communication.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-322 finished all 11 units 2026-09-30.
NEXT:   director: close IN-FLIGHT entry and commit.

## Research state before writing (2026-09-29)

PASS  news-communication / research
measured: stage=RESEARCHED eras=10/10 stories=23 (v23 c0 t0) verify_tags=0 bank=36416w outline=18134w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-322 | done | file 476w, 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-322 | done | file 1250w, 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-322 | done | file 2649w, 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-322 | done | file 4440w, 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-322 | done | file 7152w, 0 errors, emdash=0 semicolon=0; part1 self-review run |
| 6 | era 06 1800-1850 -> part2 | T-322 | done | file 2820w, 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-322 | done | file 5973w, 0 errors, emdash=0 semicolon=0; part2 self-review run |
| 8 | era 08 1900-1950 -> part3 | T-322 | done | file 2703w, 0 errors, emdash=0 semicolon=0 |
| 9 | era 09 1950-2000 -> part3 | T-322 | done | file 5668w, 0 errors, emdash=0 semicolon=0 |
| 10 | era 10 2000-today -> part3 | T-322 | done | file 7952w, 0 errors, emdash=0 semicolon=0 |
| 11 | final: self-review, --punct, validator, prose check | T-322 | done | PASS prose, 20945w, 23 stories verified |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- era 4 | Gazette as only paper, Morris removal, seditious libel definition (outline claims absent from this bank) | PATCH | "PATCH 2026-09-30 (T-322): the Gazette, Morris's removal and the meaning of seditious libel"
- era 4 | did the Mather bomb explode | PATCH | "PATCH 2026-09-30 (T-322): the bomb at Cotton Mather's house did not explode"
- era 4 | who threw the bomb | SEARCHED, NOT FOUND | "SEARCHED, NOT FOUND 2026-09-30 (T-322): who threw the bomb..."
- era 5 | Samuel Adams and the Boston committee | PATCH | "PATCH 2026-09-30 (T-322): Samuel Adams and the Boston committee, 1772"
- era 5 | Congress in Baltimore, Jan 1777 | PATCH | "PATCH 2026-09-30 (T-322): Congress in Baltimore, January 1777"
- era 8 | who ordered the removal of Japanese Americans (outline: "an order Roosevelt signed"; not in this bank) | PATCH | "PATCH 2026-09-30 (T-322): who ordered the removal of Japanese Americans, 1942"
- era 8 | Defender printed job listings and train schedules (outline claim not in bank) | PATCH | "PATCH 2026-09-30 (T-322): what the Defender printed to urge migration north"
- era 9 | Till killing facts for the Jet span (bank pointed to crime-justice only) | PATCH | "PATCH 2026-09-30 (T-322): the Till killing, for the Jet span"
- era 7 | Wells: birth, how the three Memphis men were killed, no charges, exodus and boycott (bank pointed to rights-movements only) | PATCH | "PATCH 2026-09-30 (T-322): Ida B. Wells, the Memphis killings..."

## OPEN (should be rare)

## Outline claims left out
- era 5: Fenno's paper "from 1789" (bank: search summary only).
- era 5: Banneker clause (told in science and city-building; not needed).
- era 6: David Walker's 1829 pamphlet; "85 or 86" syllabary count (86 unsourced).
- era 7: Van Lew as a Union spy; Palfrey's antislavery and newspaper work.
- era 7 defect fixed: outline said the three Memphis men were "killed"; bank (via rights-movements) gives the method, shot to death after being taken from their cells. Prose states it.
- era 7 defect fixed: outline "Thousands did" (left Memphis) now quoted from Wells with attribution.

## Decisions and defects fixed (part1)
- era 4: outline says "Published by Authority" told readers Campbell printed with government approval; bank confirms only the words. Prose states the words and glosses Authority, no approval claim.
- era 4: outline "the thrower was never identified" was search-summary only; PATCH/SNF, prose "No record names the person who threw it", and adds the sourced fact that the bomb did not explode.
- era 4: outline Zenger facts (Gazette only paper, Morris removal, seditious libel meaning) were not in this bank; PATCHed from nycourts before writing.
- era 5: "armed" Sons of Liberty at Rivington's (not in bank) dropped.

## Decisions and defects fixed

## TO PARK (for the director, burst runs only)

## Log
- 2026-09-30 Unit 1 era 01: part1 file 476 words, validator 0 errors, --punct emdash=0 semicolon=0. No PATCH this era.
- 2026-09-30 Unit 2 era 02: part1 file 1250 words, validator 0 errors (1 story), --punct emdash=0 semicolon=0. No PATCH this era. Story manteo-news-communication.
- 2026-09-30 Unit 3 era 03: part1 file 2649 words, validator 0 errors (3 stories), --punct emdash=0 semicolon=0. No PATCH this era. Stories benjamin-harris-news-communication, catua-and-omtua.
- 2026-09-30 Unit 4 era 04: part1 file 4440 words, validator 0 errors (6 stories), --punct emdash=0 semicolon=0. PATCHes: Zenger/Gazette/seditious libel (nycourts); Mather bomb fuse. SNF: bomb thrower. Stories anna-zenger-news-communication, elizabeth-timothy, benjamin-franklin-news-communication.
- 2026-09-30 Unit 5 era 05: part1 file 7152 words, validator 0 errors (10 stories), --punct emdash=0 semicolon=0. PATCHes: Samuel Adams (MHS); Congress in Baltimore 1777 (NCHE). Stories isaac-bissell, thomas-paine, mary-katharine-goddard, matthew-lyon. Self-review of part1 done (story openings varied, Manteo introduced at first mention).
- 2026-09-30 Unit 6 era 06: part2 file ~2820 words, validator 0 errors (3 stories), --punct emdash=0 semicolon=0. No new PATCH. Stories elias-boudinot, elijah-lovejoy, frederick-douglass-publisher. Left out: David Walker's 1829 pamphlet (outline only, not in bank); "85 or 86" symbols (bank has 85 only).
- 2026-09-30 Unit 7 era 07: part2 file 5973 words, validator 0 errors (6 stories), --punct emdash=0 semicolon=0. PATCH: Wells/Memphis (copied with sources from rights-movements bank). Stories william-cooper-nell, nellie-bly, ida-b-wells-news-communication. Left out: Van Lew "spied for the Union" (not in this bank); Nell story "Palfrey worked against slavery and for newspapers" (not in bank).
- 2026-09-30 Unit 8 era 08: part3 file 2703 words, validator 0 errors (3 stories), --punct emdash=0 semicolon=0. PATCHes: Defender printed jobs/train schedules (Washington Informer); EO 9066 and DeWitt (copied from rights-movements bank). Stories robert-s-abbott, victor-berger, edward-r-murrow. Used parked Hooper survey (storytelling-evolution parked line). Left out: 1930 radio census share (search summary only); "protected the papers" (bank says only "compromise").
- 2026-09-30 Unit 9 era 09: part3 file 5668 words, validator 0 errors (5 stories), --punct emdash=0 semicolon=0. PATCH: Till facts (copied from crime-justice bank, DOJ). Stories walter-cronkite, woodward-and-bernstein. Defects fixed: outline "crowd of segregationists attacked" at Ole Miss rewritten to the DOJ memo's facts; outline Pentagon Papers "the Post fought the order too" not in bank, dropped; talk-radio cause stated as a dispute.
- 2026-09-30 Unit 10 era 10: part3 file 7952 words, validator 0 errors (7 stories), --punct emdash=0 semicolon=0. PATCH: perishables re-checked (Paramount-WBD not closed 30 Sep 2026; no Medill 2026 report). Stories jeff-german, darnella-frazier. Defects fixed: outline 'at least 28 years' for Telles (sources disagree: CPJ 28 to life, ABC parole in 26) written as the CPJ sentence; outline 'Floyd died' kept with the murder verdict stated.
- 2026-09-30 Unit 11: all three files validator 0 errors, --punct 0/0 each; prose check PASS (20945 words, 10/10 eras, 23 stories verified).
