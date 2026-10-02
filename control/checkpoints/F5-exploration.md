# CHECKPOINT F5 | exploration | step 5 fixer, whole chapter

STATUS: T-462 landed (director verified: PASS  exploration / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/exploration/part1|part2|part3 + control/audit/exploration/part1|2|3-findings-sonnet.md
        + research/research-exploration.md (PATCH entries only)

NOW:    T-462 complete: all three parts judged and fixed
NEXT:   none (director: commit, then step 6 second read)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 82 / 6 / 0, found by fixer 5 (F1-F5) | 6654 -> 7759 (wc -w; 6653 at HEAD) |
| part2 | 6-7 | done | 87 / 3 / 0, found by fixer 3 (F1-F3) | 7352 -> 8147 (wc -w; 7351 at HEAD) |
| part3 | 8-10 | done | 72 / 11 / 0, found by fixer 1 (F1) | 6174 -> 6372 (wc -w; 6173 at HEAD) |

## NEEDS-RESEARCH

No finding left as NEEDS-RESEARCH. Items for round 2 to confirm (the prose already states them as below):
- part1 era 5, James Boone torture method (shot in the hips, knives, fingernails and toenails): sources are a blog (Frontier Partisans) and a Substack citing Glenn F. Williams. Confirm in Faragher, *Daniel Boone* (1992), or Williams, *Dunmore's War*.
- part2 era 7, Minik: the individuals who staged Qisuk's fake burial are named only as "the curatorial staff" (Boas was curator). SEARCHED, NOT FOUND for names (T-316 open question 2, partly answered).
- part1 era 2, Tiguex: Wikipedia names the soldier Juan de Villegas (from Flint); not used. Confirm in Flint's *No Settlement, No Conquest* if wanted.
- part1 era 5, Henderson: Attakullakulla and Oconostota were present; who signed the deeds is not in the page opened.

T-316's six open questions: Q1 Henry's execution ANSWERED; Q2 Minik staff names PARTLY (curatorial staff, Wallace); Q3 2023 White Sands study ANSWERED; Q4 Chirikov's lost crews ANSWERED (about 15); Q5 Norse-era nation SEARCHED, NOT FOUND (no record names it); Q6 Henderson's price ANSWERED (goods worth about 10,000 pounds).

## Log

Scratch: scratchpad/T-462 (orig-p1..3.md pristine findings copies; v1..v3.tsv cumulative verdicts; verdicts.py rebuilds the findings tables).

- part1 era 1 done: 14 rows (FIXED 13, REJECTED 1). PATCHes: 2023 White Sands study (opened), LOC "hundreds of groups", Cahokia location (copied), SEARCHED NOT FOUND Norse-era nation (T-316 Q5, Q3 answered). validator 0, punct 0/0.
- part1 era 2 done: rows 15-48 (FIXED 32, REJECTED 2), found by fixer F1-F3. PATCHes: hawk's bell rule, Narvaez attackers (Apalachee), Esteban sender and killers, Ranjel on Mabila arm, Castaneda on the Tiguex rape and Arenal burnings. validator 0, punct 0/0.
- part1 era 3 done: rows 49-63 (FIXED 13, REJECTED 2). PATCHes: New Amsterdam (copied), Hudson's purpose and the two captives' escape (Juet, Sep 15: prose had wrongly said the journal is silent), Marquette/Jolliet/La Salle occupations and dates, La Salle's four ships. validator 0, punct 0/0.
- part1 era 4 done: rows 64-70 (FIXED 6, REJECTED 1), found by fixer F4. PATCHes: Koryak detachment reason, Chirikov's lost crews (T-316 Q4 answered: about 15 men, Encyclopedia Arctica), Pierre La Verendrye fur trader. validator 0, punct 0/0.
- part1 era 5 done: rows 71-88 (FIXED 18), found by fixer F5. PATCHes: Sycamore Shoals price and Dragging Canoe (T-316 Q6 answered), James Boone torture method, Gray (Boit on Opitsaht, Clayoquot 25, Lopez), Jemima Boone captors. validator 0, punct 0/0. part1 complete.
- part2 era 6 done: rows 1-64 (FIXED 62, REJECTED 2: rows 29, 36). PATCHes: Louisiana location, discovery doctrine, Battle of York, Schoolcraft, Fremont nickname and 4th expedition, Vendovi's skull and 2025 return, flogging. Slur removed from Sacagawea quote (#35). validator 0, punct 0/0.
- part2 era 7 done: rows 65-90 (FIXED 25, REJECTED 1), found by fixer F1-F3 (Sand Creek #36, Beckwourth death, Minik). PATCHes: Tukudika removal (copied), Sand Creek (copied), Henry's execution (T-316 Q1 answered: shot by Brainard, Long, Fredericks on Greely's written order), Minik and the museum (T-316 Q2: only 'curatorial staff', Wallace named). Peary 'persuaded' -> 'deceived'. validator 0, punct 0/0. part2 complete.
- part3 era 8 done: rows 1-32 (FIXED 27, REJECTED 5), found by fixer F1 (Earhart DFC). No PATCH needed. validator 0, punct 0/0.
- part3 era 9 done: rows 33-68 (FIXED 28, REJECTED 5). PATCHes: Tereshkova, Bluford date, Bismarck. validator 0, punct 0/0.
- part3 era 10 done: rows 69-86 (FIXED 17, REJECTED 1). validator 0, punct 0/0.
- final: python tools/project_state.py --check exploration --stage prose -> PASS (manuscript=21091w, validator 0, em0 semi0). Totals: FIXED 241, REJECTED 20, NEEDS-RESEARCH 0, found by fixer 9.
