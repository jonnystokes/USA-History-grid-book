# CHECKPOINT T-766 | work-workers (Chapter 14), food-farming (Chapter 15) | structure pass (DECISIONS #54)

STATUS: DONE (2026-10-28): 3 blocked findings done (3 splits), 1 left on purpose; both director fact items settled
BRIEF:  control/briefs/STRUCTURE-PASS.md
FIX CHECKPOINT: control/checkpoints/T-719-reviewfix.md
REVIEW: control/review/R08.md
FILES:  manuscript/work-workers/part1-before-1800.md, part3-1900s-and-today.md, research/research-work-workers.md (PATCH);
        manuscript/food-farming/part1-before-1800.md, part3-1900s-and-today.md, research/research-food-farming.md (PATCH)
DIRECTOR FACT ITEMS: 1 loblollie (Ch 14 thick, as Ch 4); 2 Starving Time count (Ch 15: 500 in the colony, 240 in the fort, 60 alive in the fort)

## Findings the old grid rule blocked (from T-719)

T-719 marks all 50 findings FIXED, none skipped. Four were done by a workaround for section 2 as it then read
(or in part because of it). The rest were done in place as the review asked and need nothing.

| ch | # | era | finding (first words) | T-719 workaround | what this pass did | state |
|----|---|-----|-----------------------|------------------|--------------------|-------|
| 14 | 12 | 8, 1900 to 1950 | "Naomi Parker was a war worker" | "The box cannot move": span paragraphs reordered (braceros first, "Women in the war plants." last, above the box). Side effect: the bracero paragraph's "during the war" came before World War II is named | SPLIT "War work and the braceros": new span "Women in the war plants" (the women paragraph) now sits right above the box; the two bracero paragraphs follow the box as span "The bracero program, 1942" (label reworded), so the original order is back and "during the war" follows "World War II". CUT the bold lead "Women in the war plants." (the heading says it). KEPT "The missing pay." (handle for the second paragraph; Chapter 15 points to "the story of the missing pay") | DONE |
| 14 | 24 | 9, 1950 to 2000 | "The checkout job changed too." | own bold lead "At the checkout." under "Office workers organize" (the review offered "its own heading") | SPLIT: new span "Cashiers and the barcode, 1974" right after "Office workers organize" (order 1973, 1974, then the mills in 1977); opens on what the scanners did to cashiers' work. CUT the bold lead "At the checkout." | DONE |
| 15 | 15 | 10, 2000 to Today | "Farmers' markets, where farmers sell their" | bridge "**The meat plants.** Other food reaches shoppers from people they never see, such as the workers in ..." (the review offered "Split the heading") | SPLIT "Farmers' markets and the 2020 pandemic" into "Farmers' markets" and "COVID-19 in the meat plants, 2020". CUT the bridge and its bold lead: they only tied two topics under one heading. The new span opens on its point: "The disease COVID-19 spread through the plants that process meat and poultry, birds such as chickens and turkeys." (gloss reworded from "meaning chickens and turkeys": poultry also takes in other birds), then the CDC count as before | DONE |
| 15 | 16 | 8, 1900 to 1950 | "By 1930: Federal inspectors were working" | By line moved to the end of "Tractors, hybrid corn and chickens"; chickens clause dropped, "a story box cannot hold it" | nothing. The By line already ends the span it sums up. The chickens are told only in the Cecile Steele box right after it; a By line cannot sit inside a box or go back under the Dust Bowl heading, and moving the box above the span would put the chickens ahead of the tractors with no lead-in. Label kept: the box right after it brings the chickens | LEFT (no better place) |

Not blocked, so left as T-719 did them: Ch 14 #3 (Lowell, done inside the span), #14 (Knights moved after the pardon, one of the review's two options), #20 and #21 (bridges the review itself asked for); Ch 15 #3 and #6 (the content the headings promise was added), #7, #8, #17, #22 (done inside their spans).

Card lines: no "Five minutes?" or "Can skip:" line names a span this pass split or relabeled. Checked by script after the edits: all 4 names in Chapter 14's card and all 5 in Chapter 15's match span labels; no duplicate labels in either chapter.

## Director fact items

| # | item | state | note |
|---|------|-------|------|
| 1 | loblollie | DONE | Ch 14 Frethorne box: "loblollie, a thin porridge boiled in water" became "a thick porridge boiled in water" (Ch 4: "a thick porridge"). "Boiled in water" stays: Frethorne's own gloss in the letter is "loblollie (that is, water gruel)" (History Matters, from Kingsbury's *Records of the Virginia Company*, opened). PATCH in research-work-workers.md (era 03): the immigration bank's line and source copied, plus Dictionary.com "a thick gruel" (opened with curl) and the letter's gloss |
| 2 | Starving Time | DONE | Ch 15 Jamestown span: "When it began, the colony had about 500 people, and about 240 of them were inside the fort. By spring, about 60 of the people in the fort were still alive." (was: about 500 alive when it began, about 61 by spring). PATCH in research-food-farming.md (era 03): the health bank's Encyclopedia Virginia line copied with its source, re-opened today ("By spring, when the Indians lifted their siege, only 60 of about 240 colonists in the fort had survived."), and the director's reading of how the counts fit |

## Back-matter lines now wrong (not edited: the brief)

- `control/backmatter/work-workers.md` line 22: "- loblollie: a thin porridge boiled in water (The 1600s)". Chapter 14 now says "a thick porridge boiled in water". (The built glossary, `manuscript/_backmatter/02-glossary.md` line 2215, already gives Chapter 4's "a thick porridge".)
- `control/backmatter/food-farming.md` line 18: "- Starving Time: the winter of 1609 to 1610 at Jamestown, when about 500 colonists fell to about 61 (The 1600s)". Chapter 15 now has about 500 in the colony, about 240 in the fort and about 60 of those alive by spring. The same line is built into `manuscript/_backmatter/02-glossary.md` line 3621.

## Era sizes (tools/measure_readability.era_sizes; the strips follow this count, words / 200 rounded half up)

| chapter | era | before | after | minutes | strip |
|---------|-----|--------|-------|---------|-------|
| work-workers | 3 | 1,047 | 1,047 | 5.2 | 5 |
| work-workers | 8 | 5,025 | 5,020 | 25.1 | 25 |
| work-workers | 9 | 3,045 | 3,042 | 15.2 | 15 |
| food-farming | 3 | 1,176 | 1,192 | 6.0 | 6 |
| food-farming | 10 | 2,101 | 2,083 | 10.4 | 11 (not changed: the brief) |

Food-farming era 10 stood one word above the 10.5-minute line, so any cut there crosses it (dropping only the 3-word bold lead would have). Words were not added to hold it. The strip "about 11 minutes" is left for the director, who may make it 10. Seen in passing, not from this pass: work-workers era 4 is 502 words (2.5) under a strip of 2 since T-719's Chapter 24 pointer. Cards unchanged and still right: Chapter 14 17,420 words (85 minutes), Chapter 15 14,981 words (75), by tools/measure_readability.py.

## Log

<!-- file | what landed | validator | --punct -->
- baseline: validate_grid --part 0 errors and --punct 0/0 on all four files to be edited
- work-workers/part3-1900s-and-today.md | #12 split and reorder (Women in the war plants, box, The bracero program, 1942); #24 split (Cashiers and the barcode, 1974) | 0 errors | 0/0
- work-workers/part1-before-1800.md | fact item 1 (thick porridge) | 0 errors | 0/0
- research-work-workers.md | PATCH 2026-10-28 (T-766): what loblollie was (era 03)
- food-farming/part1-before-1800.md | fact item 2 (500 in the colony, 240 in the fort, 60 alive) | 0 errors | 0/0
- research-food-farming.md | PATCH 2026-10-28 (T-766): the Starving Time count (era 03)
- food-farming/part3-1900s-and-today.md | #15 split (Farmers' markets; COVID-19 in the meat plants, 2020), bridge cut | 0 errors | 0/0
- line endings checked with Python after the edits: work-workers parts LF (as before: part 2, untouched, is LF too), food-farming parts and both banks CRLF
- CHECK: python tools/project_state.py --check work-workers --stage prose -> PASS (manuscript=18548w, validator 0 errors, emdash 0, semicolon 0)
- CHECK: python tools/project_state.py --check food-farming --stage prose -> PASS (manuscript=16157w, validator 0 errors, emdash 0, semicolon 0)
