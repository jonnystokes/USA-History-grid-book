# CHECKPOINT T-765 | landmarks (Chapter 12) and elements (Chapter 13) | structure pass after R07

STATUS: DONE (landmarks: 1 split, 2 left with reasons; elements: the Flint fact item settled)
BRIEF:  control/briefs/STRUCTURE-PASS.md
FIX CHECKPOINT: control/checkpoints/T-722-reviewfix.md
REVIEW: control/review/R07.md
FILES:  manuscript/landmarks/part2-1800s.md, manuscript/elements/part3-1900s-and-today.md,
        research/research-elements.md (PATCH only)
VERIFY: python tools/project_state.py --check landmarks --stage prose
        python tools/project_state.py --check elements --stage prose

## Blocked findings in T-722 (the old grid rule) and other skips

| T-722 # | chapter | finding (first words) | state | why |
|---------|---------|-----------------------|-------|-----|
| 15 | landmarks | "The Castle. Workers in Washington put" | DONE: SPLIT | 1800 to 1850: the Castle now has its own span, label "The Smithsonian Castle", after "Two obelisks that ran out of money". CUT as redundant once split: the workaround bridge "One building in the capital in these years was paid for out of one man's gift" and the "The Castle." lead-in (the label and the Smithson sentence do both jobs). The two Castle paragraphs are one paragraph of 4 sentences. The John Hemmings box stays last in the era: moved to the front it would sit right under the opener's Hemmings line (a repeat) and cut the opener's "two tall stone monuments" off from "Both monuments are obelisks". No card line names either span |
| 13 | landmarks | "McComber's work on Manhattan skyscrapers became" | LEFT | the review's second option (fold the box into the Kahnawake passage in 1900 to 1950) moves a story out of its era and merges it, both still forbidden. Within 1950 to 2000 its place, between the Gateway Arch (1963 to 1969) and the World Trade Center (1973), is already the chronological one and beside the Manhattan skyscraper span. T-722 already gave the hook a real detail |
| 24 | landmarks | "Workers died building three of the" | LEFT | skipped under ARCHITECTURE 4.4 (By lines only in eras over 4,000 words; this era is about 2,800), not under the grid rule, so outside this pass |
| none | elements | (no T-722 finding was blocked by the grid rule) | - | - |

## Director fact item (elements, 2000 to Today, "Lead in the water of Flint")

| item | state | note |
|------|-------|------|
| What became of the 2016 and 2017 Flint charges; living officials unnamed unless a court convicted them | DONE | PATCH 2026-10-28 (T-765) in research-elements.md from the Attorney General's report of August 25, 2026 (and its release), AP 2016 to 2019, ABC12 2019 and 2020, Michigan Public 2017, the *People v Peeler* opinion (2022) and WDIV 2026. Prose: outcome first (no one tried, no judge sent anyone to jail or prison); 15 charged in 2016 and 2017; the seven deals (each had a felony charge, accepted one lesser charge without admitting guilt; judges later dismissed all seven, no criminal record); the other eight dropped in June 2019; nine charged in 2021, six of the eight and the former governor; the 2022 ruling; all nine dismissed; closed October 31, 2023, with the time limit for most charges run out |
| names | DONE | the charges passage now names no living person (Busch, Prysby, Earley and Snyder taken out of it; roles kept: "the former governor", "the state's health director and its chief medical executive"). The earlier paragraphs still name Earley, Busch and Prysby for what the 2016 task force report found, which is a record, not a charge |
| correction | DONE | "ruled in 2022 that this broke the state constitution" was wrong: the Peeler opinion rests on the statutes. Now "ruled that, under Michigan's laws, such a judge had no power to start a criminal case". Correction note in the PATCH beside the T-241a line |

No new glossary term: the no-contest plea is spelled out in plain words; felony, misdemeanor, willful
neglect of duty, involuntary manslaughter and one-judge grand jury keep their glosses and back-matter lines.
"Lawyers" replaces "prosecutors" in the passage (plain word, no gloss needed).

## Log

<!-- file | what landed | validator | --punct -->
- landmarks part2 | #15 Castle split into its own span; bridge and lead-in cut | 0 errors | 0/0
- research-elements.md | PATCH 2026-10-28 (T-765) appended: the 15, the seven deals and their dismissals, the eight dropped, the 2021 nine, Peeler, the time limits, no trial or jail, correction note | - | -
- elements part3 | Flint charges rewritten (4 paragraphs plus "How the cases ended") | 0 errors | 0/0
- elements part3 | self-review: "Lower-court judges" -> "Judges in Genesee County"; the last paragraph split at its seam (was 92 words); "team" -> "lawyers" throughout the passage (one term) | 0 errors | 0/0
- strips | elements era 10: 2,277 words = 11.4, strip "about 11 minutes" still right; landmarks era 6: 729 words = 3.6, strip "about 4 minutes" still right; elements card 16,892 words = 84.5, stays 85. No strip, card or closing answer changed
- back matter | no line made wrong. Noticed, not caused here: control/backmatter/landmarks.md line 81 dates "interest" to 1900 to 1950, but the word now first appears, unglossed, in the Castle sentence of 1800 to 1850 (T-722 text)
- bank defect named (left alone, PATCH note only): research-elements.md line 315 (T-241a) says the 2022 ruling found the one-judge grand jury "unconstitutional"; the opinion rests on the statutes
- measure_readability after: landmarks 14,912 words, 298 paras, over 90: 2; elements 16,892 words, 315 paras, over 90: 4 (all furniture, as before); date-first 0.0% in both
--check: PASS landmarks / prose (validator 0 errors on all three parts, emdash 0, semicolon 0, manuscript 15,867 w)
--check: PASS elements / prose (validator 0 errors on all three parts, emdash 0, semicolon 0, manuscript 17,636 w)
