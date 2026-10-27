# CHECKPOINT T-661 | exploration | readability | the whole chapter (opening, eras 1 to 10, closing)

STATUS: IN-FLIGHT (agent finished; the director sets DONE after reading the report)
VERIFY: python tools/project_state.py --check exploration --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-DISPATCH.md, T-661)
MODEL:  fable
FILES:  manuscript/exploration/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md (bank research/research-exploration.md only for a PATCH)

NOW:    nothing. All 13 units landed, 2026-10-26 evening.
NOTE (director, mid-task): the build checks the card's "about N minutes" against measure_readability's words / 200 rounded to 5, and each strip against the era's words / 200. Done: card 110, strips from the tool's era_sizes (script: scratchpad T-661/era_minutes.py).
NEXT:   the director reads the report and Jon reads the chapter. If anything is reopened, start from the Units table: every unit is landed.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | chapter opening (part1) | landed | opening block written as first block of era 1 (spine, lead-plate anchor, turn, 3 questions, five minutes, can skip); reading time set at 115, confirm at the end |
| 2 | era 01 before-1500 (part1) | landed | strip; era summary "By 1500" para re-led; footprints label is a question, 169-word para split with a lead-in; the three definitions in a row folded into their sentences; Leif: hook, two lead-ins, "In 1960"/"In 2021" re-led, closing hedges turned into Known / Not known. No cuts. No closer (907 words) |
| 3 | era 02 1500s (part1) | landed | strip; era summary re-led; Columbus: hook, "born in Genoa in 1451" cut (the Who line has Genoa), three lead-ins, dates moved off the front; coasts span relabeled "Four captains along the coast", one lead-in per captain, three long paras split, the 44-word Verrazzano quote split into two pieces under 25 words each (same words); Cabeza/Estevanico: hook, two paras split, "there" (Hawikuh) made clear; Armies: six lead-ins, four paras split; St. Augustine re-led; closer "By 1600" with three bullets. Cut: Columbus's birth year and place (résumé; Genoa stays in the Who line) |
| 4 | era 03 1600s (part1) | landed | strip; Champlain para re-led; Hudson: hook, "mate" gloss folded, two lead-ins, three paras split, "September 9"/"October 2" turned into "Three days later"/"The next day"; Marquette: hook, two dates moved off the front; La Salle: hook, two lead-ins, long para split, ambush para re-led. No cuts, no closer (1,444 words) |
| 5 | era 04 1700-1750 (part1) | landed | strip; Bering: hook, three lead-ins, two paras split, the three hedges about the 15 lost men turned into one Not known line; cut "born in Horsens, Denmark, 1681, officer in the Russian navy" (the Who line carries it); La Verendrye span relabeled "The lead plate: ...", two dates moved off the front. No closer (872 words) |
| 6 | era 05 1750-1800 (part1) | landed | strip; Boone: hook, four lead-ins, two paras split, three dates moved off the front (stays at about 690 words: eight sourced events, none a résumé); Pacific span relabeled as a question answered in its first sentence (Ortega's scouts), five lead-ins, four paras split, three dates moved off the front. No cuts, no closer (1,523 words). Part 1 validator 0 errors, punct 0/0 |
| 7 | era 06 1800-1850 (part2) | landed | strip; era summary: "The deal." lead-in with the date second, diplomat/treaty glosses folded (re-gloss, new file), split; Lewis and Clark: hook, Movie line now says the film invents the romance and the rivalry (bank PATCH), three lead-ins, three paras split, two dates off the front (stays at about 790 words: the orders, the doctrine, the Lakota, the Blackfeet killings, the pay, all sourced); Sacagawea: hook, interpreter gloss folded, death rewritten per §5.7 (Luttig 1812 + Clark 1813 first as the strongest record, then Known / Disputed with the Shoshone 1884 tradition and the Hidatsa account credited); York: hook, one split; Pike: hook; Colter: hook, one lead-in, split; Pikes Peak: "By 1810" line, date off the front; Trappers: three lead-ins, split; Glass: hook; Smith: hook, three lead-ins; Bridger: hook, "By 1840" line as its last paragraph (the only seam before Wilkes); Wilkes: hook, three lead-ins, three splits; Frémont: hook, three lead-ins, two splits, "May 12" turned into "Three days later"; closer "By 1850" as a before/after pair. Cuts: Glass "born about 1783", Smith "born in New York in 1799", Frémont "He was born in 1813" (résumé lines; nothing else in the boxes depends on them) |
| 8 | era 07 1850-1900 (part2) | landed | strip; summary's two date-led paras re-led; Beckwourth: hook, "Sand Creek." lead-in, split, two dates off the front; Surveys: three lead-ins, two dates off the front; Alaska: two lead-ins, split; Powell: hook, "The three who left." lead-in, the closing hedge turned into a Not known line, cut "He was born in 1834" (résumé); North Pole span: five lead-ins, four splits, "In 1897"/"By November 1" re-led; 1898 span re-led; closer "By 1900" with one number and a comparison. Part 2 validator 0 errors, punct 0/0 |
| 9 | era 08 1900-1950 (part3) | landed | strip; summary split; Henson: hook, two lead-ins, two splits, birth date cut to the year (Who line carries Maryland); Bingham: hook, cut "born in Honolulu in 1875" and the one-day-governor / senator sentence (résumé, nothing in the box depends on it); Andrews: hook, cut "born in Beloit, Wisconsin, in 1884" (Who line has Wisconsin); Byrd: hook, three lead-ins, one split, cut "born in Virginia in 1888"; Lindbergh: hook, two dates off the front; Earhart: hook, one lead-in, one split, cut "She was born on July 24, 1897". No closer (2,143 words) |
| 10 | era 09 1950-2000 (part3) | landed | strip; Walsh: hook, date off the front; Into space: four lead-ins, three splits, four dates off the front; Johnson: hook, lead-in, two splits, birth date cut to the year; Apollo 11: hook; Apollo 13: hook, split; Earle: hook, split, cut "born in New Jersey in 1935" (Who line has New Jersey); Ballard: hook, lead-in, split, cut "born in Wichita, Kansas, in 1942" (Who line has Kansas); Ride/Jemison: hook, "Jemison." lead-in; Challenger: date off the front, split; closer "By 2000" = one open question (the Moon) answered in era 10 |
| 11 | era 10 2000-today (part3) | landed | strip; summary split; Columbia: date off the front, split; Voyager para split; Cameron: hook, date off the front; Artemis: hook, split. No cuts |
| 12 | chapter closing (part3, last block of era 10) | landed | the three questions answered word for word, What changed, five dates (1021, 1540, 1806, 1909, 1969, all in the chapter), Not known (the 1500 population estimate), Where to go (the lead plate), Next: Chapter 2, Native Nations |
| 13 | self-review (§8), checks, measure, report | landed | a second pass split every paragraph over 90 words that had a seam (my count: 84 before, 2 after, both in the opening block); the ten era first sentences re-read together and three reshaped (eras 3, 4, 7) so no two share a shape; card and strips set from measure_readability's counts (card 110; strips 6, 15, 8, 4, 8, 29, 14, 11, 14, 8); validator 0 errors on all three parts, --punct 0/0, --check prose PASS |

<!-- state: todo | working | landed | skipped (say why) -->

## SUBJECT NOTES (the plan, written before any edit)

**Before (measure_readability, 2026-10-26):** words 20056, paras 253, avg_para 79.3, over90 84, date_first 28.9% (my own count: 101 of 253), def/1k 0.6, attr/1k 3.7, also/1k 1.1, you 0, longest era 5383, eras>4000 1, stories 35, story median 355, stories>400 14.
Per-era words (my count, markers excluded): 1: 907 · 2: 2791 · 3: 1444 · 4: 872 · 5: 1523 · 6: 5347 · 7: 2544 · 8: 2143 · 9: 2602 · 10: 1246. Total 21419 (about 105 minutes).

**Spine:** Almost every place in this chapter was already somebody's home when the explorers arrived, and the people who lived there often showed them the way.

**Three questions:**
1. How do we know people were living here at least 21,000 years ago?
2. What did the explorers do to the people whose land they crossed?
3. Which famous "firsts" are still in doubt?

**Anchor:** the La Verendrye lead plate (era 4): six by eight inches, Latin stamped on one side naming Louis XV, the date and names scratched on the other, buried March 30, 1743 beside the Missouri, found at Pierre, South Dakota in 1913, kept in the South Dakota Cultural Heritage Center. All already in the chapter.

**Five minutes?** "Toward the North Pole, 1879 to 1898" in 1850 to 1900 (about 820 words; the Jeannette, Greely, Minik).

**Can skip:** "The first recorded climb of Pikes Peak, 1820", "Alaska, 1867 to 1885", "1898: islands in two oceans", "Mapping the sea floor".

**Reading time:** words / 200 rounded to 5. Set the opening's figure after the closing is written (expect about 115 minutes).

**"By" lines:** era 6 only (5,347 words): about every 2,000 words, at span seams (after the Lewis and Clark group, after the trappers/Glass/Smith group). None elsewhere.

**Era closers (eras over 2,500 words):** eras 2, 6, 7, 9. Rotate the middle: era 2 three bullets, era 6 before/after pair, era 7 one number with a comparison, era 9 one question left open and answered in era 10. Eras 1, 3, 4, 5, 8, 10 get the strip only (era 8 is 2,143 words, under the line).

**Story boxes:** every box gets the bold hook after the record lines. The 14 over 400 words (Leif 408, Columbus 506, Cabeza/Estevanico 539, Hudson 559, Bering 490, Boone 685, Lewis and Clark 784, Sacagawea 472, Glass 424, Smith 466, Wilkes 660, Frémont 677, Beckwourth 499, Henson 650): cut the résumé lines (birth place and year where the record lines carry them, the honors list), keep every scene and every hard fact. Lewis and Clark, Frémont and Wilkes may stay long: each is a worked account of killings the hard-subjects policy will not let me compress.

**Known trouble spots from the dispatch:** era 1 definitions in a row (obsidian, archaeologists, chert); "Sailing the coasts" is four biographies in a row (bold lead-ins, one explorer per paragraph group, demote minor names); one paragraph in 3.5 opens with a date; The Far Horizons needs the romance warning (fact not in the bank: look it up, PATCH the bank, then write it); Sacagawea's death: the 1812 Luttig record stated first as the stronger record, then the Shoshone tradition with why it matters (§5.7).

**Cuts (every one listed here with its reason):** all are résumé lines in story boxes (birth year or place already in the Who line, or an honors line with nothing to do with the story). No scene, number, name of a victim or sourced act was cut anywhere.
- Columbus: "Columbus was born in Genoa in 1451" (Who line has Genoa).
- Bering: "He was born in Horsens, in Denmark, in 1681, and he served as an officer in the navy of Russia" (Who line has both).
- Glass: "He was born about 1783."
- Smith: "He was born in New York in 1799" (Who line has New York).
- Frémont: "He was born in 1813."
- Powell: "He was born in 1834."
- Henson: birth date "August 8, 1866" cut to the year.
- Bingham: "He was born in Honolulu in 1875" and "He later served one day as governor of Connecticut, in 1925, and then as a US senator until 1933" (not part of the Machu Picchu story).
- Andrews: "Andrews was born in Beloit, Wisconsin, in 1884" (Who line has Wisconsin).
- Byrd: "Byrd was born in Virginia in 1888" (kept "became a Navy pilot in 1918").
- Earhart: "She was born on July 24, 1897."
- Johnson: birth date "August 26" cut to the year.
- Earle: "She was born in New Jersey in 1935" (Who line has New Jersey).
- Ballard: "He was born in Wichita, Kansas, in 1942" (Who line has Kansas).

**Boxes left over 400 words on purpose (14):** Leif 404, Columbus 513, Cabeza/Estevanico 559, Hudson 572, Bering 485, Boone 710, Lewis and Clark 817, Sacagawea 508, Glass 429, Smith 472, Wilkes 674, Frémont 694, Beckwourth 510, Henson 664. Each is a worked account of sourced events (most of them killings, captives or a disputed claim) that the hard-subjects policy and DECISIONS #52 do not let me compress. Every one now opens with a hook and has lead-ins and paragraphs under 90 words, so the length reads as scenes, not a résumé.

**Rules broken on purpose:** none. Two choices to flag: (1) the "By 1840" line sits as the last paragraph of the Bridger story box, because the era has no zoom block between Bridger and Wilkes and a By line cannot sit between blocks; (2) the three era closers and the chapter closing use a question once ("Would anyone go back?", era 9), the form §4.5 allows, answered by era 10.

## Sources in hand

- research/research-exploration.md line 335: The Far Horizons is "a 1955 film about the expedition" (Wikipedia page of the expedition). The romance claim needs its own source: see Gaps.
- research/research-exploration.md line 347: Luttig's 1812 entry, Clark's 1813 guardianship, Shoshone 1884 tradition, Hidatsa account.

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- era 06 | what *The Far Horizons* (1955) invents | PATCH (Wikipedia, "The Far Horizons": "many details are fictional and historically inaccurate", the Lewis-Clark rivalry is fictional, Time review cites the Sacagawea-Clark romantic subplot as misleading) | research-exploration.md, Lewis and Clark entry, "PATCH 2026-10-26 (T-661): what the film invents"

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

## Log

<!-- One line per save: date-time | unit | what landed | validator | --punct -->
- 2026-10-26 (evening) | plan | read the five binding files, DECISIONS #28-#53, the whole chapter; ran measure_readability (before line above); checkpoint created | baseline: validator 0 errors all three parts, --punct 0/0, --check prose PASS |
- 2026-10-26 (evening) | opening, eras 1-5 | part1 saved after each era | validator 0 errors | punct 0/0
- 2026-10-26 (evening) | eras 6-7 | part2 saved after each era | validator 0 errors | punct 0/0
- 2026-10-26 (evening) | eras 8-10, closing | part3 saved after each era | validator 0 errors | punct 0/0
- 2026-10-26 (evening) | self-review pass | 40 more paragraph splits across all three parts, three era first sentences reshaped, card and strips set from the tool | validator 0 errors x3 | punct 0/0 x3 | --check prose PASS
- **After (measure_readability):** words 21715, paras 408, avg_para 53.2, over90 6, date_first 0.7%, def/1k 0.6, attr/1k 3.7, also/1k 1.1, you 4, longest era 5737, eras>4000 1, stories 35, story median 364, stories>400 14.
