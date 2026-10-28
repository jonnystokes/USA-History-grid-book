# CHECKPOINT T-761 | native-nations (Chapter 2) + land-environment (Chapter 3) | structure pass

STATUS: DONE (both --check PASS; see the end of the log)
BRIEF:  control/briefs/STRUCTURE-PASS.md (DECISIONS #54: within one era a span or story may move, a long span may split into two, a label may be reworded)
FIX CHECKPOINT: control/checkpoints/T-726-reviewfix.md
REVIEW: control/review/R02.md
FILES:  manuscript/native-nations/part1-before-1800.md, part2-1800s.md, part3-1900s-and-today.md
        manuscript/land-environment/part3-1900s-and-today.md
        research/research-land-environment.md (PATCH only)
VERIFY: python tools/project_state.py --check native-nations --stage prose
        python tools/project_state.py --check land-environment --stage prose
Baseline (before any edit): both PASS (native-nations 21,448 w, 21 stories; land-environment 19,721 w, 15 stories)

No card line ("Five minutes?", "Can skip:") in either chapter names a span this pass changes, and no back-matter
or manuscript line quotes those labels (only the outlines do, and they are not reader-facing).

## Plan (blocked findings found in T-726, numbered as there)

| ch | # | era | blocked part | plan |
|----|---|-----|--------------|------|
| 2 | 1 | 1850 to 1900 | 1,429-word span could not split | split after Sand Creek: "The wars, from the nations' side" (1862 to 1864) + "From Red Cloud to Geronimo" (1866 to 1886) |
| 2 | 2 | 1950 to 2000 | children/sterilization subhead skipped | order the span's paragraphs harms first, then split: "Children taken and women sterilized" + "Self-rule, casinos and remains sent home" |
| 2 | 9 | The 1600s | horse text had no subhead; cross-era gathering skipped | horse block (era-level, no heading) becomes its own span after Po'pay's box; cross-era part stays undone |
| 2 | 11 | 1750 to 1800 | blankets and Paxton subheads not given | split Paxton off as "The Conestoga killings"; relabel the rest "Pontiac, smallpox and the Line" |
| 2 | 17 | 1950 to 2000 | label unchanged, Alaska under the Alcatraz/Wounded Knee heading | split at Wounded Knee: "Alcatraz, Blue Lake and Alaska" + "Wounded Knee, 1973" |
| 3 | 9 | 1950 to 2000 | label unchanged, Santa Barbara not in the heading | relabel "The river that burned and the Santa Barbara oil spill" (360 words, not long enough to split) |
| 3 | 11 | 1900 to 1950 | span could not fold into the box | still forbidden (merge); leave |
| fact | | 1850 to 1900 | bank line 163 infers her uncles were Tenaya's sons | PATCH narrowing it to NPS, PBS, Taylor 1932, Bunnell |

## Log

<!-- file | what landed | validator | --punct -->
- NN part1 | era 3: horse block now span "Where the Plains horses came from", moved after Po'pay's box, lead-in "The horses left behind." cut; era 5: "Pontiac and the Line" split, relabeled "Pontiac, smallpox and the Line" + "The Conestoga killings" (lead-in "Paxton." cut, bridge kept as "While Pontiac's war went on") | 0 errors | 0/0
- NN part2 | era 7: wars span split after Sand Creek (790 + 639 words), new span "From Red Cloud to Geronimo"; all bridges and lead-ins kept | 0 errors | 0/0
- NN part3 | era 9: "Alcatraz, Blue Lake and Alaska" + "Wounded Knee, 1973" (lead-in "Wounded Knee, 1973." cut); "Children taken and women sterilized" + "Self-rule, casinos and remains sent home" (Ford's act moved after the harms; lead-in "Children taken." and bridges "While nations were taking over their own programs" and "Ten years after the child welfare law" cut) | 0 errors | 0/0
- LE part3 | era 9: "The river that burned" relabeled "The river that burned and the Santa Barbara oil spill" | 0 errors | 0/0
- research-land-environment.md | PATCH 2026-10-28 (T-761) appended: CORRECTION to "To Tu Ya's uncle." (NPS page quoted, PBS, Taylor 1932 read via the Wayback copy, Bunnell) | n/a | n/a
- strips and card | Chapter 2 lost 30 words (lead-ins and bridges); every strip still rounds to its stated minutes (era 3 11.9 -> 12, era 5 7.6 -> 8, era 7 21.7 -> 22, era 9 14.6 -> 15); card 20,381 / 200 -> about 100 minutes, unchanged. Chapter 3: label only, no word change
- CHECK native-nations: PASS (validator 0 errors x3, emdash 0, semicolon 0, manuscript 21,418 w, 21 stories verified)
- CHECK land-environment: PASS (validator 0 errors x3, emdash 0, semicolon 0, manuscript 19,721 w, 15 stories verified)

## Result, finding by finding

| ch | # | state | why, in a few words |
|----|---|-------|---------------------|
| 2 | 1 | DONE | split at the 1864/1866 seam, so the Lakota thread (Red Cloud's War, Fort Laramie, Black Hills, Little Bighorn, Crazy Horse) sits in one span. Split into two only (DECISIONS #54), not the three or four the reviewer named; the 13 bold handles stay. Bridges kept: each still links two events inside its span |
| 2 | 2 | DONE | harms first, then the laws: chronological by start (children taken for decades before 1978 and sterilizations from 1973, then the acts of 1975, 1988, 1990), and "Self-rule" now leads into "Nations take the schools back", which cites the 1975 law. The two T-726 bridges only patched the old order: one rewritten as a plain opening, one cut |
| 2 | 9 | DONE (within the era) | the horse text was an era-level block with no heading, read as the tail of "The Pueblo Revolt"; it is now its own span, after Po'pay's box, so the box follows the revolt it belongs to and the box still ends on the statue. LEFT: gathering it with the 1500s horse paragraph and "Comanche power" (other eras, still forbidden) |
| 2 | 11 | DONE | Paxton has its own span; the smallpox blankets stay in Pontiac's span (one split per span, and Fort Pitt was part of Pontiac's war), so its label now names smallpox. Bridge kept, now says "Pontiac's war" so it stands under its own heading |
| 2 | 17 | DONE | 670 words, two episodes: Alaska and Blue Lake now in a heading. Lead-ins and the "A year after Blue Lake" bridge kept |
| 2 | 6 | NOT A GRID BLOCK | T-726 kept the worked court case by judgment (DECISIONS #52), not because of the grid rule; no change |
| 3 | 9 | DONE (relabel) | 360 words is not a long span, so no split; the heading now names Santa Barbara. Bridge "Earlier the same year" kept (the span still turns from June in Cleveland back to January in California) |
| 3 | 11 | LEFT | folding the pigeon span into the Southworth box would merge a span into a story, still forbidden; T-726 already took the deaths out of the span |
| fact | | DONE | bank line 163 narrowed by PATCH (NPS, PBS, Taylor 1932, Bunnell): no source names her parents or the uncle, says he was Tenaya's son, or links him to the son the guard shot. Prose unchanged, as the dispatch says: it never says the murdered uncle was Tenaya's son. Its "Tenaya's sons were her uncles" is kinship, true unless one son was her own father (no source names him); the PATCH records that |

Back matter: no line names a span this pass changed, and nothing moved between eras, so no glossary, date or
place line changed era. Outlines still carry the old labels (not reader-facing, not touched).
