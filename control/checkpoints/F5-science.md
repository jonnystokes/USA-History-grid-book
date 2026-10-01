# CHECKPOINT F5 | science | step 5 fixer, whole chapter

STATUS: T-449 landed (director verified: PASS  science / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/science/part1|part2|part3 + control/audit/science/part1|2|3-findings-sonnet.md
        + research/research-science.md (PATCH entries only)

NOW:    done
NEXT:   (none) director: commit

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 36 FIXED / 2 REJECTED / 0 NR, +1 found by fixer (fixed) | 3948 -> 4190 (wc -w 3947 -> 4189. prose_words 3578 -> 3820) |
| part2 | 6-7 | DONE | 62 FIXED / 5 REJECTED / 0 NR, +1 found by fixer (fixed) | 4367 -> 4770 (wc -w 4366 -> 4769. prose_words 4086 -> 4489) |
| part3 | 8-10 | DONE | 67 FIXED / 3 REJECTED / 1 NR, +5 found by fixer (fixed) | 10343 -> 11021 (wc -w 10342 -> 11020. prose_words 9676 -> 10351) |

## NEEDS-RESEARCH
- science part3 era 9 (findings row 59): were the Vanderbilt pregnant women (1946-49, about 819, radioactive iron) told of the radiation? Only advocacy/student pages say no; fetch ACHRE ch. 7 Vanderbilt section or the Washington Post, Dec 21, 1993. Prose makes no consent claim.

## PATCHes added (research-science.md)
- 2026-10-01 (T-449) era 2: Roanoke / Carolina Algonquian
- 2026-10-01 (T-449) era 3: Harvard naming 1639, New Sweden, Newton's Principia, "natural philosophy"
- 2026-10-01 (T-449) era 4: Franklin positive/negative, the Junto, Linnaeus
- 2026-10-01 (T-449) era 5: Transactions date settled as 1771, Norriton location, Notes "Queries"
- 2026-10-01 (T-449) era 6: who elected Joseph Henry (Board of Regents, 7 of 12)
- 2026-10-01 (T-449) era 7: Maxwell model 1874, Morley, Michelson birth, Prussia, relativity 1905
- 2026-10-01 (T-449) era 8: Nobel Prizes, Millikan field, Leavitt at HCO, transistor press conference, Hiroshima/Nagasaki deaths (from war bank), sterilization method (from rights-movements bank), Hearst, committee founding
- 2026-10-01 (T-449) era 9: Darleane Hoffman places and the old plutonium belief; Vanderbilt consent SEARCHED, NOT FOUND
- 2026-10-01 (T-449) era 10: the 2015 element recognitions (copied from research-elements.md)

## Log
- part1 era 1: 9 findings judged (8 FIXED, 1 REJECTED), 1 found by fixer. validate 0 errors, punct 0/0.
- part1 era 2: 4 findings, 4 FIXED. validate 0 errors, punct 0/0.
- part1 era 3: 6 findings, 6 FIXED (actors and glosses banked as PATCHes). validate 0, punct 0/0.
- part1 era 4: 8 findings, 7 FIXED, 1 REJECTED. validate 0, punct 0/0.
- part1 era 5: 11 findings, 11 FIXED (Transactions date settled as 1771 by PATCH). validate 0, punct 0/0. PART 1 DONE.
- part2 era 6: 32 findings, 28 FIXED, 4 REJECTED. PATCH (Henry election). validate 0, punct 0/0.
- part2 era 7: 35 findings, 34 FIXED, 1 REJECTED, 1 found by fixer (Maxwell model date). PATCH era 7. validate 0, punct 0/0. PART 2 DONE.
- part3 era 8: 42 findings, 40 FIXED, 2 REJECTED, 4 found by fixer. PATCH era 8. validate 0, punct 0/0.
- part3 era 9: 18 findings, 16 FIXED, 1 REJECTED, 1 NEEDS-RESEARCH (Vanderbilt consent). PATCH era 9. validate 0, punct 0/0.
- part3 era 10: 11 findings, 11 FIXED, 1 found by fixer. PATCH era 10 (2015 elements). validate 0, punct 0/0. PART 3 DONE.

## Final check
```
PASS  science / prose
  measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=25 (verified 25) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=18660w files=3 validator_errors=0
```
