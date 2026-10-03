# CHECKPOINT F7 | city-building | step 7 fixer on the second-audit findings

STATUS: DONE (T-632, PASS  city-building / prose)
BRIEF:  control/briefs/FIX7-DISPATCH.md + FIXER.md (whole-chapter mode)
TASK:   T-632 (fixer: opus)

NOW:    done
NEXT:   director: commit; see NEEDS-RESEARCH

## Units
| part | eras | fixer | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|---|
| part1 | 1-5 | T-632 | done | 43 / 2 / 0, +5 found by fixer (F1-F5) | 5560 -> 5755 |
| part2 | 6-7 | T-632 | done | 66 / 4 / 0, +3 found by fixer (2 FIXED, F4 NEEDS-RESEARCH) | 5653 -> 5906 |
| part3 | 8-10 | T-632 | done | 51 / 3 / 0, +1 found by fixer | 7937 -> 8081 |

## NEEDS-RESEARCH
- part2 era 7 (F4): the 1889 Creek and Seminole payment amounts ($2.28 million, $1.91 million) rest on BatesLine's statute citations and Wikipedia; Edmond History Museum confirms a payment, no amounts. Round 2: read 25 Stat. ch. 317 and ch. 412 (1889) directly.
- part2 era 7 (director note): Seneca Village accounts differ. Prose now gives both, credited (Conservancy + Rosenzweig & Blackmar: no violence; NYPL guide: forced and violent, Aug 1857). No other manuscript file mentions Seneca Village (grep 2026-10-03), so no #36 conflict.

## Log
- 2026-10-03 T-632: read briefs, style files, DECISIONS #28-46, AUDIT-QUEUE. Bank PATCHes 2026-10-03 (T-632) added: chunkey (era 01), St. Augustine fire + continuous occupation (era 02), Powhatan + 1607 arrival (era 03), Banneker's home (era 05).
- part1 era 1: rows 1-7 FIXED, F1 found by fixer. validate 0 errors, punct 0/0.
- part1 eras 2-5 done, each era validated 0 errors, punct 0/0. EXTRA St. Augustine: prose now says the town moved twice and people lived in it through both moves (City of St. Augustine + Florida Museum). Florida Museum names the Timucua's flaming-arrow attack of 1566.
- part2 era 6: rows 1-27 done (26 FIXED, 1 REJECTED). validate 0 errors, punct 0/0. Seneca Village research: Central Park Conservancy Q&A + Rosenzweig & Blackmar say residents left without violence, last evicted by Oct 1857; NYPL guide + Mental Floss say police drove them out by force Aug 1857. Bank PATCH era 07 records both.
- part2 era 7 done: 43 rows (40 FIXED, 3 REJECTED), +3 found by fixer. validate 0 errors, punct 0/0.
- part3 era 8 done: rows 1-25 (22 FIXED, 3 REJECTED), +1 found by fixer (Chicago estimate now credited to Strobel 2025). PATCH era 08 (Strobel, RERF). validate 0 errors, punct 0/0.
- part3 eras 9-10 done: era 9 rows 26-45 all FIXED, era 10 rows 46-54 all FIXED. validate 0 errors, punct 0/0. Sweeps: no 'In plain words', no unnamed 'sources say', 'Negro' only inside the Baldwin quote, explained.
- prose check: PASS city-building / prose (18,795 words).
