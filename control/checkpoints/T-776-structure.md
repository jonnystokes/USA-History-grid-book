# CHECKPOINT T-776 | art (Chapter 32) | structure pass (DECISIONS #54)

STATUS: IN-FLIGHT            (agent finished; director sets DONE)
BRIEF:  control/briefs/STRUCTURE-PASS.md
FIX CHECKPOINT: control/checkpoints/T-721-reviewfix.md
REVIEW: control/review/R21.md
FILES:  manuscript/art/part1-before-1800.md, part2-1800s.md, research/research-art.md (PATCH only)
DIRECTOR FACT ITEM: smallpox vaccination in the 1800s was scratched into the skin (Chapter 26), not "a shot"

## Findings the old grid rule blocked (from T-721)

T-721 marks no finding "skipped because a span or story could not move, split or be relabeled". Its one
"in part" (#7, the Acoma retelling) rests on DECISIONS #36, not on section 2, so it stays. Three fixes were
workarounds the old rule forced (a bridge, or a span left where it no longer fits):

| # | era | finding (first words) | T-721 workaround | what T-776 did | state |
|---|-----|-----------------------|------------------|----------------|-------|
| 21 | 1, Before 1500 | "At 86, he carved an eight-foot" | bridge sentence opening the Nathan Jackson box ("Carving on the Northwest Coast did not stop in 1500, and Nathan Jackson carves in that tradition today.") | span "Carving on the Northwest Coast" moved to just before the box, after "Who dug the objects up, and where did they go?"; the dig span now follows the pipes, plates and Craig Mound it is about, and the era ends on a living carver. Bridge cut (the span's last line and the Who line now say it); the box opens "Nathan Jackson is Chilkoot Tlingit." | DONE (moved) |
| 3 | 6, 1800 to 1850 | "The Hudson River School's painters worked" | duplicate cut, but span "Writers" stayed before the Hudson span although its new point ("as the painters did", "the same mountains the Hudson River School painted", the Mohican "in New York and Wisconsin that year") leans on it | span "Writers" moved, text unchanged, from before the Hudson span to after the Thomas Cole box (before the Catlin span and its By 1840 line); its three forward references are now callbacks | DONE (moved) |
| 25 | 9, 1950 to 2000 | "Maya Lin, a student of 21," | Maya Lin kept under "Native artists and Native objects" with a bridge from Cannon | left: the only other place for her is the AIDS quilt span, and joining two memorials there would need a relabel and a link the bank does not give; the Cannon bridge (he served in that war) ties her to the span | LEFT |
| 7 | 3, The 1600s | "Oñate sentenced the Acoma men over" | retelling kept (DECISIONS #36) | not a grid-rule block | LEFT |

Card lines: no label changed, so "Five minutes?" and "Can skip:" stand ("Writers" keeps its label and its era).
No cuts beyond the one bridge sentence (#21, 17 words, now said twice just above it).

## Director fact item

| item | state | note |
|------|-------|------|
| vaccination "shots" (part 2, span "George Catlin and the people he painted", the Indian Vaccination Act paragraph) | DONE | "vaccinations, shots that protect a person from smallpox" now reads "vaccinations. To vaccinate a person, a doctor scratched fluid from a sore of cowpox, a mild disease of cows, into the skin, and it protected the person against smallpox." (Chapter 26's sentence, cowpox glossed). PATCH 2026-10-28 (T-776) copies research-health.md line 336 with its source (Countway Library of Medicine, Waterhouse exhibit) and lines 337 and 339 (doctors did it) |

## For the director (outside this task's files)

- control/backmatter/art.md line 76, "vaccination: a shot that protects a person from smallpox (1800 to 1850)", is now wrong; the prose says scratched into the skin. The joined glossary (manuscript/_backmatter/02-glossary.md line 4034, Chapter 26) is already right. Not edited (brief: no back matter).
- Same paragraph, a cross-chapter difference not dispatched: Chapter 26 says "Cass left the Mandan, Hidatsa and Arikara nations ... out of the program" (research-health.md line 343, Wikipedia after Pearson 2003); Chapter 32 says "The records do not name the officials who left them out" (its bank has only ND Studies' "had been denied access"). Left as is.

## Log

<!-- file | what landed | validator | --punct -->
- baseline 2026-10-28: validator 0 errors x3, --punct 0/0 x3, --check art --stage prose PASS (33,104 words); build load_chapter: 30,929 words, 155 minutes = card, no warning; era words 1,850 / 782 / 1,444 / 1,362 / 1,937 / 4,336 / 4,536 / 4,906 / 4,267 / 4,767 (strips 9/4/7/7/10/22/23/25/21/24)
- part1-before-1800.md | #21 (NW Coast span moved, bridge cut) | 0 errors | 0/0 | CRLF kept
- part2-1800s.md | #3 (Writers moved) and the vaccination sentence | 0 errors | 0/0 | CRLF kept
- research-art.md | PATCH 2026-10-28 (T-776) at the end | CRLF kept
- after: build load_chapter 30,933 words, 155 minutes = card, no warning; era words 1,833 / ... / 4,357 (era 6) / ..., strips unchanged 9/4/7/7/10/22/23/25/21/24; "Writers" still resolves to the era 6 span
