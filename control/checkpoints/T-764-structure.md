# CHECKPOINT T-764 | energy (Chapter 10), transportation (Chapter 11) | structure pass (DECISIONS #54)

STATUS: DONE (3 done: energy 5 moved, energy 7 split and relabeled, transportation 8 moved; 1 left: energy 23); both chapters PASS --stage prose
BRIEF:  control/briefs/STRUCTURE-PASS.md
FIX CHECKPOINT: control/checkpoints/T-725-reviewfix.md
REVIEW: control/review/R06.md
FILES:  manuscript/energy/part*.md, manuscript/transportation/part*.md (and their banks, PATCH only)
DIRECTOR FACT ITEMS: none

## Findings the old grid rule blocked (from T-725)

| chapter | T-725 # | era | finding (first words) | T-725 workaround | state | note |
|---|---|---|---|---|---|---|
| energy | 5 | 7, 1850 to 1900 | "A fire at the Avondale mine," | bridge line, "spans cannot move" | DONE (moved) | the coal run (span "Avondale, 1869: one way out", span "From charcoal to coal", Lafayette Houck box) moved as one unit from after the Westinghouse and Tesla box to after "Did kerosene save the whales?", before "Pearl Street, 1882". Years now run 1859, 1860s, 1869, Hopewell to 1883, 1882, current war to 1896; the era ends on the current war, the closer's subject; Pearl Street's "Coal into current." follows the coal spans. CUT the T-725 bridge ("Power stations such as Pearl Street burned coal, and miners died digging it. Thirteen years before Pearl Street opened,"): it pointed forward to a span now after it. Avondale opens "A fire at the Avondale coal mine, ..." ("coal" restates the era intro) |
| energy | 7 | 10, 2000 to Today | "Members of the Standing Rock Sioux" | bridge on the "Standing Rock." lead, "no splits" | DONE (split, relabeled) | span "Mine deaths, black lung and a pipeline" split: first part relabeled "Mine deaths and black lung" (Upper Big Branch, the trial, black lung); new span "Standing Rock and the pipeline" (the two pipeline paragraphs). CUT the bold lead "Standing Rock." (the heading now says it). KEPT the T-725 bridge "Pumping more oil also meant moving it." (it ties the pipeline to the era's oil boom, as the review asked). No card line names either label |
| energy | 23 | 1, Before 1500 | "Federal officials in charge of forests" | "After 1500." lead and bridge, "spans cannot move" | LEFT AS IS | the review's move ("move the modern facts to the era that matches") would take paragraphs from era 1 to era 10: still forbidden. A split is not for this span: 291 words in five paragraphs, not long (DECISIONS #54: "a long span may be split"). T-725's "After 1500." lead, its bridge sentence and the date-ordered modern paragraphs already answer the review's first option |
| transportation | 8 | 7, 1850 to 1900 | "Cornelius Vanderbilt left the largest American" | connecting first lines, "boxes cannot move" | DONE (moved) | the review's "move Twain to the steamboat era" would cross eras (era 6), and his years (1859 to 1861) belong to era 7, so within era 7: Twain and Vanderbilt boxes moved from after Hung Wah to the start of the era, right after the era intro, in date order (Twain 1859 to 1861, then Vanderbilt, steamboats to railroads from the early 1860s). The railroad spans now run unbroken, with Hung Wah alone beside "The Chinese workers" (24 eras in the book already open with a story box). KEPT Twain's T-725 line "Steamboats still ran on the Mississippi River while the railroads spread." (it says why a steamboat box sits in a railroad era). CUT Vanderbilt's T-725 clause "the same year Chinese crews were building the Central Pacific through the Sierra Nevada" (it tied him to the Hung Wah box and now pointed ahead); his first paragraph now opens on the steamboats-to-railroads move, which follows Twain's box. Facts unchanged (bank line 189) |

## Log

<!-- file | what landed | validator | --punct -->
- era words before (tools/measure_readability.era_sizes): energy era 7 2,536 (strip 13), era 10 2,556 (13), era 1 719 (4); transportation era 7 2,847 (14)
- energy/part2-1800s.md | finding 5 (coal run moved) | 0 errors | 0/0
- energy/part3-1900s-and-today.md | finding 7 (split, relabel) | 0 errors | 0/0
- transportation/part2-1800s.md | finding 8 (Twain and Vanderbilt boxes moved) | 0 errors | 0/0
- era words after: energy era 7 2,518 (12.59, strip 13 still right), era 10 2,554 (12.77, 13); transportation era 7 2,833 (14.16, 14). No strip or card minutes change. Closing answers untouched
- card check (read-only mirror of the build's warning, scratch script): every "Five minutes?" and "Can skip:" name matches a span label in its era; no duplicate labels; 0 problems in either chapter
- back matter: no line needs changing (people index, timeline and places give the era only, and nothing left its era)
- line ends: the 3 edited part files are CRLF on every line (220/220, 395/395, 329/329)
- `--check energy --stage prose`: PASS (15,928w, validator 0 errors, 0 em dashes, 0 semicolons)
- `--check transportation --stage prose`: PASS (15,959w, validator 0 errors, 0 em dashes, 0 semicolons)
