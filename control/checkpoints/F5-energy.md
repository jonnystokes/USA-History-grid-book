# CHECKPOINT F5 | energy | step 5 fixer, whole chapter

STATUS: T-451 landed (director verified: PASS  energy / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/energy/part1|part2|part3 + control/audit/energy/part1|2|3-findings-sonnet.md
        + research/research-energy.md (PATCH entries only)

NOW:    finished
NEXT:   none (director: commit). Formerly (verdict files kept in scratchpad T-451/v1.tsv, v2.tsv, v3.tsv; the findings table fixer column is applied with T-451/apply_verdicts.py <findings> <tsv>. Word counts are `wc -w` of the part file)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 86 / 4 / 0, plus 2 found by fixer (both FIXED) | 3769 -> 4213 |
| part2 | 6-7 | done | 47 / 5 / 0, plus 3 found by fixer (all FIXED) | 3621 -> 3928 |
| part3 | 8-10 | done | 82 / 5 / 0, plus 4 found by fixer (all FIXED). One cut detail parked below | 6725 -> 7299 |

## NEEDS-RESEARCH
- energy era 8 (Monongah 1907): whether boys and helpers not on the company list went underground and account for the 500+ estimate. Only search summaries say so; prose now gives the e-WV / Mine Wars Museum reason (identification system destroyed, poor records). Find a reliable page (e.g. McAteer, *Monongah*, 2007).

## Log
- part1 era 1 done: findings 1-12 judged (11 FIXED, 1 REJECTED). PATCH 2026-10-01 (T-451) era 1: travois load, burning cut back and revived (NPS Travois Road; TNC 2020). validate 0 errors, punct 0/0.
- part1 era 2 done: findings 13-26 (13 FIXED, 1 REJECTED). PATCH 2026-10-01 (T-451) era 2: Hymahi, Camino Real, the word pueblo. validate 0, punct 0/0.
- part1 era 3 done: findings 27-54 (28 FIXED). No PATCH. validate 0, punct 0/0.
- part1 era 4 done: findings 55-67 (13 FIXED), F1 found by fixer. PATCH 2026-10-01 (T-451) era 4: transported convicts (Encyclopedia Virginia). validate 0, punct 0/0.
- part1 era 5 done: findings 68-90 (21 FIXED, 2 REJECTED), F2 found by fixer. PATCH 2026-10-01 (T-451) era 5: Schuyler engine from McCormick's full text with Hornblower's 1768 letter; Hopewell on French Creek. validate 0, punct 0/0. PART1 DONE.
- part2 era 6 done: findings 1-17 (16 FIXED, 1 REJECTED), F1-F2 found by fixer. No PATCH. validate 0, punct 0/0. NEXT part2 era 7.
- part2 era 7 done: findings 18-52 (31 FIXED, 4 REJECTED). PATCH 2026-10-01 (T-451) era 7: Drake and Pearl Street firsts, Kemmler (Buffalo, Auburn, Cockran), Westinghouse Niagara generators. validate 0, punct 0/0. PART2 DONE.
- part3 era 8 done: findings 1-38 + 29b (35 FIXED, 3 REJECTED, 1 to NEEDS-RESEARCH as a cut detail), F1 found by fixer. PATCH 2026-10-01 (T-451) era 8: Monongah count, Insull flight, TVA/REA signers, Norris first, Kettle Falls, Osage killers. validate 0, punct 0/0.
- part3 era 9 done: findings 39-65 (26 FIXED, 1 REJECTED), F2-F3 found by fixer. PATCH 2026-10-01 (T-451) era 9: Shippingport and TMI in Pennsylvania, the 1973 war. validate 0, punct 0/0.
- part3 era 10 done: findings 66-86 (20 FIXED, 1 REJECTED), F4 found by fixer. PATCH 2026-10-01 (T-451) era 10: Vogtle in Georgia, Palisades rechecked to September 2026. validate 0, punct 0/0. PART3 DONE.
- cross-part: era 7 opening reworded so eras 6 and 7 no longer open the same way (part2 F3).
- FINAL: python tools/project_state.py --check energy --stage prose -> PASS (manuscript=14450w, 11 stories verified, 0 em dashes, 0 semicolons, validator 0 errors).
