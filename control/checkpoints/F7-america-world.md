# CHECKPOINT F7 | america-world | step 7 fixer on the second-audit findings (T-621)

STATUS: DONE (T-621, PASS  america-world / prose)
BRIEF:  control/briefs/FIX7-DISPATCH.md + FIXER.md (whole-chapter mode)

NOW:    done
NEXT:   director: commit

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 29 / 1 / 0 (+4 found by fixer, all FIXED) | 5,821 -> 5,880 |
| part2 | 6-7 | done | 61 / 3 / 0 (0 found by fixer) | 4,830 -> 5,116 |
| part3 | 8-10 | done | 39 / 1 / 1 (+3 found by fixer, all FIXED) | 7,593 -> 8,038 |

## NEEDS-RESEARCH
- part1 era 4 (Nanfan deed, 1701): the bank says "other writers dispute" the Haudenosaunee reading but names none. Prose now says "Others read it differently." Round 2: name who disputes it (a court ruling or a named historian).
- part3 era 9 (Jayuya and Utuado, October 1950): no count of people killed when the National Guard attacked the towns. Round 2: find a sourced count, or name the silent document (#45).
- part3 era 8 (Haiti cacos): the US military count of 3,250 is search-summary only. Round 2: confirm on a real page or drop it from the bank. Same for the Dominican "1,137 killed or wounded".
- part2 era 7 (Samoa 1899): who renounced which claims in the Tripartite Convention is search-summary only (Wikipedia); prose names only the three signers.

## Log
- 2026-10-03 part1 eras 1-5: 30 findings judged (29 FIXED, 1 REJECTED: row 16 "small fleet" is the plain gloss of "squadron"). 4 found by fixer. PATCHes added: Menéndez's 1565 contract with Philip II (era 2); George III's proclamation of rebellion, Aug 23 1775, and Adams as a signer (era 5). validate_grid 0 errors; punct 0/0.
- 2026-10-03 part2 eras 6-7: 64 findings judged (61 FIXED, 3 REJECTED: Polk's name, diplomats as treaty writers, Ealdama already named in part 3). PATCHes: Texas joint resolution and Oregon country (era 6); Guam surrender by Gov. Juan Marina, Samoa's three signers, the Queen's charge/fine/forced abdication, the two-thirds rule (era 7). AUDIT-QUEUE T-484 Kake item: Poulson is named. validate_grid 0 errors; punct 0/0.
- 2026-10-03 part3 eras 8-10: 41 findings judged (39 FIXED, 1 REJECTED: "hospital staff" is in the bank's consent note, 1 NEEDS-RESEARCH: Jayuya toll). 3 found by fixer (Sam's killer unnamed, Les Cayes "died", boat-strike passive). EXTRA done: the Apology Resolution passage now says a group of mostly American businessmen overthrew Queen Liliʻuokalani with 162 American sailors and Marines landed by John L. Stevens, and quotes Public Law 103-150 (PATCH T-621, law text read from GovInfo). PATCHes also: Blair House (Torresola shot Coffelt), Brookings "capture". validate_grid 0 errors; punct 0/0.
- Prose check: PASS america-world / prose (17,798 words measured, 13 stories verified).
