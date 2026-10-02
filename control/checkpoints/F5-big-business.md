# CHECKPOINT F5 | big-business | step 5 fixer, whole chapter

STATUS: T-460 landed (director verified: PASS  big-business / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/big-business/part1|part2|part3 + control/audit/big-business/part1|2|3-findings-sonnet.md
        + research/research-big-business.md (PATCH entries only)

NOW:    T-460 fixer (opus) 2026-10-01: all three parts DONE
NEXT:   none (director: commit, then route NEEDS-RESEARCH to round 2)
SCRATCH: scratchpad/T-460 (orig findings copies, v1/v2/v3.txt cumulative verdicts, apply_verdicts.py)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 79 / 7 / 0, plus 9 found by fixer | 4386 -> 5088 (wc -w: 4385 -> 5088) |
| part2 | 6-7 | done | 51 / 7 / 1, plus 7 found by fixer | 5099 -> 5398 (wc -w: 5098 -> 5398) |
| part3 | 8-10 | done | 86 / 13 / 0, plus 7 found by fixer | 7535 -> 8262 (wc -w: 7534 -> 8262) |

## NEEDS-RESEARCH
- part2 era 6, rows 22-23 (Biddle story): who sued Nicholas Biddle for nearly $25 million, who brought the criminal conspiracy charge (and when), and who ran the investigation that found "massive fraud" at the bank (1841). Passives left in place. SEARCHED, NOT FOUND entry in the bank (T-460).
- part3 era 9, row 64 (Bhopal): who at Union Carbide India Limited turned off the vent-gas scrubber and drained the refrigeration unit. Prose now says Broughton's review does not name them. Fixed in place, listed for round 2.
- part3 era 9: AT&T's 1984 holdings, Johns-Manville's size, Gates's CEO dates and Redmond are banked from search summaries only (unconfirmed). Round 2 should open a page for each.

## Log
- part1 era 1: rows 1-4 judged (3 FIXED, 1 REJECTED). validate 0 errors, punct 0/0.
- part1 era 2: rows 5-9 FIXED, F1 found by fixer (named Osborne, Elizabeth I). validate 0, punct 0/0.
- part1 era 3: rows 10-42 judged (31 FIXED, 2 REJECTED), F2-F4 found by fixer. 1619 arrival retold from Encyclopedia Virginia (buyers Yeardley and Peirsey). validate 0, punct 0/0.
- part1 era 4: rows 43-61 judged (17 FIXED, 2 REJECTED). validate 0, punct 0/0.
- part1 era 5: rows 62-86 judged (22 FIXED, 3 REJECTED), F5-F9 found by fixer. Part 1 re-read whole after repairs. validate 0, punct 0/0.
- part2 era 6: rows 1-23 judged (19 FIXED incl. 1 partial, 2 REJECTED, 1 NEEDS-RESEARCH + row 23 partly), F1-F3 found by fixer. PATCH: 1832 recharter votes and Clay/Webster pressure. validate 0, punct 0/0.
- part2 era 7: rows 24-60 judged (32 FIXED, 5 REJECTED), F4-F7 found by fixer. PATCH: Frick 11% and chairman 1892, Carnegie 73.5% of Frick Coke by 1888, Monongahela/tugboats, South Improvement secrecy (Tarbell). validate 0, punct 0/0.
- part3 era 8: rows 1-44 judged (41 FIXED, 3 REJECTED), F1-F2 found by fixer (incl. Tarbell 4 vs 5 years contradiction with part2). PATCH: Berle-Means title, Morgan/Wall Street, Backus name, FTC Act section 5, Memorial Day marchers (copied from work-workers). validate 0, punct 0/0.
- part3 era 9: rows 45-78 judged (28 FIXED, 6 REJECTED), F3-F5 found by fixer. PATCH: Microsoft case subject, Gates CEO/deposition, en banc affirmance, AT&T kept long-distance/Bell Labs/Western Electric, Johns-Manville size. validate 0, punct 0/0.
- part3 era 10: rows 79-99 judged (17 FIXED, 4 REJECTED), F6-F7 found by fixer. PATCH: Citizens United holding (copied from government-politics), CDC opioid deaths (copied from drugs-alcohol), Enron, Khan at Yale. validate 0, punct 0/0.
- final: python tools/project_state.py --check big-business --stage prose -> PASS (manuscript 17680w by project_state, 10/10 eras, 14 stories verified, 0/0 punct, validator 0 errors).
- bank PATCHes added (T-460): 1619 arrival buyers/sellers (era 3), half-freedom 1644 (era 3), definitions shilling/penny/Puritan/Quaker (era 3), "likely" in sale ads (era 4), Haudenosaunee and clan mothers (era 5). Later: 1832 recharter votes (era 6), Frick share/river/SIC secrecy (era 7), Berle-Means/Morgan/Backus/FTC s.5/Memorial Day (era 8), Microsoft/AT&T/Johns-Manville (era 9), Citizens United/opioid deaths/Enron/Khan (era 10). Two SEARCHED, NOT FOUND notes (Biddle suits).
