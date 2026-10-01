# CHECKPOINT F5 | money | step 5 fixer, whole chapter

STATUS: T-450 landed (director verified: PASS  money / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/money/part1|part2|part3 + control/audit/money/part1|2|3-findings-sonnet.md
        + research/research-money.md (PATCH entries only)

NOW:    done
NEXT:   none (director: commit)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 62 / 0 / 0, plus 3 found by fixer (FIXED) | 3688 (wc 3687) -> 4153 (wc) |
| part2 | 6-7 | DONE | 61 / 4 / 0, plus 2 found by fixer (FIXED) | 4259 (wc 4258) -> 4630 (wc) |
| part3 | 8-10 | DONE | 74 / 1 / 0, plus 5 found by fixer (FIXED) | 6199 (wc 6198) -> 6562 (wc) |

Chapter total (project_state prose count): 14,372 words after (before: 3688 + 4259 + 6199 = 14,146).

## NEEDS-RESEARCH
None. Every "not in bank" item was either banked by a PATCH or rewritten to the bank's own words.

## PATCHes added to research/research-money.md (all "PATCH 2026-10-01 (T-450)")
- era 1: Haudenosaunee gloss (copied from native-nations bank), whelk and quahog.
- era 2: the mita drafted Native men 18 to 50, about one in seven (Dell 2010).
- era 3: 12 pence a shilling, 20 shillings a pound; Charles I tried by Parliament's court and beheaded January 30, 1649; John Hull born December 18, 1624 (so 27, not 28, in May 1652).
- era 5: British counterfeiting of Continentals in New York (Hatfield, Journal of the American Revolution 2015; Clinton to Germain 1780; New York Gazette ad 1777); eagle = $10.
- era 7: Bryan's Bible imagery (Britannica; date note July 8 vs bank July 9, July 9 kept); electoral votes.
- era 10: Hanyecz's Mac client and GPU mining (CoinDesk 2025); FTX payouts above 100 percent were interest (Entrepreneur 2024, John Ray).

## Log
- part1 era 1: findings 1-3 FIXED. validate 0, punct 0/0.
- part1 era 2: findings 4-12 FIXED. validate 0, punct 0/0.
- part1 era 3: findings 13-31 FIXED (#28 age was false: 28 -> 27). validate 0, punct 0/0.
- part1 era 4: findings 32-46 FIXED. validate 0, punct 0/0.
- part1 era 5: findings 47-62 FIXED, F1-F3 found by fixer FIXED. Re-read eras 2-5 after repair. PART 1 DONE.
- part2 era 6: findings 1-32: 28 FIXED, 4 REJECTED (#22, #24, #31, #32); F1-F2 FIXED. BLOCKING #1 fixed (1836-1862). validate 0, punct 0/0.
- part2 era 7: findings 33-65 all FIXED. validate 0, punct 0/0. PART 2 DONE.
- part3 era 8: findings 1-31: 30 FIXED, 1 REJECTED (#29); F1-F2 FIXED. validate 0, punct 0/0.
- part3 era 9: findings 32-49 all FIXED (#44 put a 1980 rate on 1979); F3-F4 FIXED. validate 0, punct 0/0.
- part3 era 10: findings 50-75 all FIXED; F5 FIXED. validate 0, punct 0/0. PART 3 DONE.
- Final: python tools/project_state.py --check money --stage prose -> PASS (10/10 eras written, 12 stories verified, 0 VERIFY, 0/0 punctuation, 14372 w, validator 0 errors).
