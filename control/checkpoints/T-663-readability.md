# CHECKPOINT T-663 | holidays | readability | chapter 37, all ten eras

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check holidays --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-DISPATCH.md, section T-663)
MODEL:  fable
FILES:  manuscript/holidays/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md

NOW:    done; reported to the director (all eleven units landed, checks PASS)
NEXT:   nothing for the agent. Director: read the report, commit. If the build warns about the card's minutes, the card says "about 95 minutes" from measure_readability's 19,2xx words (words/200 = 96, rounded to 5); strips are era words/200 rounded (era 1's strip excludes the opening block's ~310 words)

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | chapter opening + era strips 1 to 5 | landed | opening block in era 1; strips on eras 1-5 (eras 6-10 get theirs with their era). Minutes are provisional: set from measure_readability at the end (coordinator's note) |
| 2 | era 01 before-1500 | landed | summary names the five regions; five spans each open on a different thing (Faith Keepers, the fires going out, the Sun-priest, Salmon's offer, the Pleiades); 3 labels turned into promises; 1898 annexation moved to a parenthesis at the end of its paragraph; "fasted" inline; fast-length dispute into one "Accounts differ" paragraph |
| 3 | era 02 1500s | landed | feast-day gloss folded, repeat cut; Protestants/Mass/friar glosses folded; 2 date-first paragraphs reordered; "What the Spanish did next" lead-in; 2 NPS attributions replaced by Gannon named once; labels: "Two services of thanks...", "The thanksgiving Texans claim, 1598", "What John White painted at Secotan, 1585" |
| 4 | era 03 1600s | landed | first sentence now Smith's Christmas vs the 1659 law; epidemic/perpetually/shilling/profane glosses folded; Bradford hook, résumé paragraph cut (repeat of the span); Pequot span: lead sentence states the massacre, passive "were killed" made active, order paragraph split, Newell claim under a lead-in, Known / Not known pair; 3 date-first paragraphs fixed |
| 5 | era 04 1700-1750 | landed | summary opens on Boston boys and Pinkster, not the date range; Saltonstall order reordered; Hercules paragraph: evidence first, hedge last; 2 labels |
| 6 | era 05 1750-1800 | landed | Wight hook, birth line cut, land passage kept under a lead-in, cannon paragraph trimmed of a repeat (414 to about 380 words); Anderson hook; Pope's Night 1764 and Stamp Act paragraphs reordered; Washington's order lead-in, "soliciting" glossed in parentheses; Adams's three glosses into one sentence; Whiskey Rebellion split out under "A second day, 1795"; Christmas label now "Four days off at Christmas, and who got none" |
| 7 | era 06 1800-1850 | landed | strip; summary first sentence no longer date-led; lead-ins "The poem", "Who wrote it", "Hiring day", "The sale days", "July 5, not July 4", "August 1"; the 140-word July 1827 paragraph split; bayou/brethren/deliverance/deprive glosses folded or in parentheses; Hale hook, birth line cut, two long paragraphs split ("The magazine", "Still asking"), "a federal law gave" made "under a federal law ... had"; 2 labels |
| 8 | era 07 1850-1900 | landed | strip and closer ("By 1900", three bullets); "federal workers" gloss folded; "A proclamation is..." cut (glossed in era 6, same file); lead-ins on the 1870/1879/1888 laws, Nast, Hale's letter, the first Juneteenth, the police chief, the mob, no one charged, the proclamation; Norfolk span split into three with lead-ins, veto gloss folded; Yates hook, segregation gloss folded, birth line shortened; Decoration Day rebuilt (see Decisions); Columbus lynching/verdict/grand jury glosses folded; boarding-school span reordered into date order (1883 rules first, then 1879 schools, then 1890 holiday) and its 150-word paragraph split; 4 labels |
| 9 | era 08 1900-1950 | landed | strip; summary no longer date-led, "proclaim" gloss folded (first use in part 3); Mother's Day label is a question answered at once; Jarvis hook, birth date shortened, lead-ins "The fight", "Arrested"; Armistice "The 1938 law"; Thanksgiving label now the promise "Why Thanksgiving is the fourth Thursday, not the last", Macy's paragraph reordered, "The date fight" lead-in; grab-bag span given five lead-ins and the 1883 Price rules cut to a one-line callback (era 7 owns them) |
| 10 | era 09 1950-2000 | landed | strip and closer ("By 2000", a 1950/2000 before-and-after pair); Monday-holiday paragraph split, "a bill proposed" reworded; Karenga crimes paragraph split in two under "The crimes" (nothing cut); Day of Mourning paragraphs reordered and given lead-ins; James hook, "He lived from 1923 to 2001" cut; King Day span split into five under lead-ins, label "Fifteen years to get King's day"; second "federal holiday" gloss cut (summary keeps one); "The Super Bowl" lead-in; Byrd hook, birth date cut; Pride/Columbus span put in date order (1970, 1977, 1992, 1999) |
| 11 | era 10 2000-today + chapter closing | landed | strip; Hodges/Virginia/Hochul/Newsom/Biden date-first sentences reordered; "The vote", "Juneteenth 2025", "Park fees" (130-word paragraph split), "October 2025" lead-ins; the three assimilate/displace/eradicate glosses made one sentence; Lee hook, birth line shortened, civilian gloss folded; Lee box stays about 420 words on purpose (the 1939 mob scene and the walk both earn it); chapter closing block written: three questions answered word for word, What changed, five dates, Not known, Where to go, Next |

<!-- state: todo | working | landed | skipped (say why) -->

## SUBJECT NOTES (the architecture, decided before any edit)

**Measurement before (measure_readability.py, 2026-10-26):**
holidays 18088 words, 263 paras, avg 68.8, over90 55, date_first 19.8%, def/1k 1.7, attr/1k 9.1, also/1k 1.1, you 5, longest era 3401, eras>4000 0, stories 9, story median 350, stories>400 4.

**Era words (own count):** 1: 1170 · 2: 1015 · 3: 1869 · 4: 842 · 5: 2116 · 6: 1940 · 7: 3397 · 8: 1614 · 9: 2960 · 10: 1495. No era over 4,000, so no "By [year]" lines. Closers for eras 7 and 9 only (over 2,500). Reading time about 90 minutes (recompute at the end).

**Spine:** Every holiday on the American calendar got there because people asked for it, argued over it or fought for it, and the arguing is not over.

**Anchor:** Sarah Josepha Hale's May 1877 letter (she was 88, her eyes too weak, a helper wrote it), still asking Congress for a law making the last Thursday in November a legal holiday. Lincoln had proclaimed the day in 1863. The law came in 1941. All in the chapter (era 6 story, era 7, era 8).

**Three questions:**
1. Who decided when Americans would give thanks, and why did it take until 1941 to fix the date?
2. Which days did Black Americans make their own, from election days to Juneteenth?
3. Why did President Harrison proclaim the first Columbus Day in 1892, and why do some states no longer keep it?

**Five minutes?** "Juneteenth, 1865" in 1850 to 1900 (the Jack Yates story follows it).

**Can skip:** "Places named for holy days" (1500s), "Washington's birthday" (1750 to 1800), "Pinkster banned in Albany, 1811" (1800 to 1850), "Columbus Day, 1905 to 1937" (1900 to 1950).

**Closing, five dates:** fall 1621 Plymouth harvest meal · October 3, 1863 Lincoln proclaims Thanksgiving · June 19, 1865 Granger at Galveston · October 21, 1892 first national Columbus Day · June 17, 2021 Juneteenth becomes federal. (King Day 1983 goes in "What changed".)
**Not known:** the first name of the boy Brown killed by the Pope wagon in 1764, and who drove it (bank: SEARCHED, NOT FOUND).
**Where to go:** Cole's Hill, Plymouth (Massasoit statue, the Day of Mourning plaque, the Metacom plaque in Post Office Square).
**Next:** last chapter; point back to chapter 1.

**Decoration Day (§5.7, dispatch trouble spot):** lead with the documented start of the national day (Logan's order, May 5, 1868, and the GAR's own credit to a comrade's letter about a German custom, Mary Logan's Virginia claim, both in the bank at research line 437). Then the earlier local days in date order (Boalsburg 1864, Charleston 1865, Columbus 1866), Charleston carrying the most detail because it is the best documented (Blight). Known / Disputed pair: what is documented, and whether Logan copied any of them (College of Charleston: debated; NCA: recent scholarship points to Columbus, GA). Waterloo 1966 stays in era 9 as what Congress did, not as a finding.

**Definitions to fold or cut (guideline 7):** "time immemorial" (keep, it is in Eldredge's quote, gloss stays inside the sentence), "fasted" (inline), "saint's feast day" (fold into the church-year sentence, cut the repeat under St. Augustine), "Mass" (inline), "friar" (inline), "perpetually" (inside the quote sentence), "epidemic" (inline). Across the chapter: fold own-sentence glosses into the sentence or cut the ones an 11-year-old knows. "Proclaim" glossed three times (eras 6, 7, 8): keep era 6 and a short one in era 8 (new part file), cut era 7. "Federal workers" glossed four times: once per part file.

**Attribution (9.1/1k):** drop "a National Park Service page states" and "a Plimoth Patuxet Museums page states" where the fact is not contested. Keep where sources differ (Matanzas counts, the fast length, the first-Thanksgiving claims, the 1939 state counts, the King vote margin, Granger's troop count).

**Story hooks (all nine, mandatory):** Bradford, Wight, Anderson, Hale, Yates, Jarvis, James, Byrd, Lee. Boxes over 400 (Wight 414, Hale 435, Jarvis 457, Lee 434): trim résumé lines, keep scenes.

## Cuts (every one, with the reason)

<!-- era | what was cut | why -->
- era 2 | "A saint's feast day is a day kept each year to honor a holy person." and the repeat under St. Augustine ("the day Catholics kept each year to honor him") | folded into the church-year sentence once (guideline 7)
- era 2 | "A National Park Service page describes this Mass and meal as..." | the phrase is Gannon's; he is named once and the NPS once, two attributions become one
- era 3 | Bradford story, first paragraph (governor, sent four men to hunt, the five deer) | word-for-word repeat of the Plymouth span above it; the box now opens on the Christmas scene
- era 3 | "A Plimoth Patuxet Museums page states that" (summary, 1841) | the fact is stated plainly in the summary and sourced in the span below it
- era 3 | "Commemorated means marked or celebrated the memory of." | gloss moved inside the quotation in parentheses (§5.10)
- era 5 | Wight: "Wight was born in Medfield, Massachusetts, on May 26, 1752." and "In 1785, his first year in Bristol, Wight led the town's first Patriotic Exercises on the Fourth of July." | birth line is résumé; the second was a repeat of the box's first sentence
- era 5 | "Solemnized meant marked with ceremony. Shews meant shows. Illuminations were candles lit in the windows." | three gloss sentences made one (guideline 7); no fact lost
- era 5 | "Soliciting meant asking for." | moved inside the quotation in parentheses
- era 6 | Hale: "She was born in Newport, New Hampshire, on October 24, 1788." | résumé line; the box opens on what she did
- era 6 | "A bayou is a slow, swampy stream." / "To deprive someone of a thing is to take it away." / "Brethren means brothers and sisters, and deliverance means being set free." | folded into the sentence or into parentheses inside the quotation (guideline 7); no fact lost
- era 7 | "A proclamation is a public order or announcement by a president or governor." | "proclaim" is glossed in the Hale story in the same part file
- era 7 | "Federal workers are people who work for the national government." / "A lynching is a killing by a mob, without a trial." / "A verdict is a jury's decision." / "A grand jury is a group of citizens..." / "A veto is a president's refusal to sign a law." / "Emancipation means being freed from slavery." / "Segregation was the system of laws..." / "A martyr is a person who dies for a cause." / "Exposure means being left outside..." / "Fasting means going without food, here as a way to pray." | each folded into its sentence or into parentheses (guideline 7); every definition survives
- era 7 | Decoration Day: "Accounts still differ about which came first, and about whether the later ceremonies copied the one in Charleston." | replaced by the Known / Disputed pair, which says the same more exactly and credits each side
- era 8 | Jarvis: "on May 1, 1864" (the day and month of her birth) | résumé detail; the year and the Civil War stay
- era 8 | the 1883 Price rules repeat: the ration penalties (ten days, 15 to 30 days, jail up to thirty days) and the treaty-rations sentence | era 7 now tells the rules in full in date order; era 8 keeps a one-line callback (§5.12, DECISIONS #52)
- era 8 | "A proclamation is..." style gloss on "proclaimed" | folded into the summary sentence ("proclaimed, that is, named in a public order")
- era 9 | James: "He lived from 1923 to 2001." · Byrd: "and she was born on April 20, 1926" | résumé lines
- era 9 | "a federal holiday, a day off for the national government's workers" (the states span) | the era summary glosses "federal holiday" four paragraphs earlier
- era 10 | Lee: "on October 7, 1926" (day and month) · "A civilian is a person who is not in the military." (folded) | résumé detail; gloss folded
- era 10 | "To assimilate... To displace... To eradicate..." three sentences | made one sentence; all three meanings kept

## Decisions and defects fixed

<!-- Anything a successor must not undo. -->
- **Decoration Day (era 7, §5.7).** The span now opens on the documented start of the national day (Logan's order, May 5, 1868) and adds two banked facts with their sources (research line 437): the Grand Army of the Republic's own credit to a member's letter about a German custom, and Mary Logan's claim of a Virginia Confederate cemetery. The three earlier local days follow in date order under bold place-and-year lead-ins, Charleston with the most detail because Blight's newspaper find documents it best. A Known / Disputed pair replaces "Accounts still differ about which came first": Known = Logan's order and the three documented days; Disputed = whether Logan copied any of them (College of Charleston: debated; NCA: recent scholarship points to Columbus, Georgia). No claim was dropped. The 1966 Waterloo resolution stays in era 9 as an act of Congress, not a finding.
- **Era 7 boarding-school span reordered** into date order (1883 Price rules, 1879 schools and the 1891/1893 laws, 1890 Morgan's holiday). The 1883 rules had come last, after 1890. No fact changed.
- **Pequot span (era 3):** the passive "Between 400 and 700 Pequot were killed" now names Mason's men as the killers (hard-subjects policy: the actor always matters). Newell's claim and Bangs's answer stay in full, followed by a Known / Not known pair.
- **Era 6 Hale story:** "a federal law gave ... the day off" (a law acting) is now "under a federal law ... had the day off".

## Log

<!-- One line per save: date-time | unit | what landed | validator | --punct -->
- 2026-10-26 (start) | read the brief, the four guides, DECISIONS #28-53, the whole chapter, the bank's era 1, Decoration Day and Waterloo sections; measurement run; usage 9% of the 5-hour window
- 2026-10-26 (late) | units 1-6, part1-before-1800.md | opening block, strips 1-5, eras 1-5 body passes, 3 story hooks | validator 0 errors | punct 0/0
- 2026-10-26 (late) | units 7-8, part2-1800s.md | strips 6-7, eras 6-7 body passes, Decoration Day rebuilt, closer "By 1900", 2 story hooks | validator 0 errors | punct 0/0 | usage 19%
- 2026-10-27 (12:00 AM) | units 9-11, part3-1900s-and-today.md | strips 8-10, eras 8-10 body passes, closer "By 2000", chapter closing, 4 story hooks | validator 0 errors | punct 0/0 | --check PASS
- 2026-10-27 (12:15 AM) | final pass | strips 7, 9, 10 set from era counts (18, 16, 10); era 7 first sentence varied from era 5's; era 7 closer's "nearly every one" corrected to "three of them"; §8 read of the opening, the closing and era 7 whole | validator 0 errors x3 | punct 0/0 x3 | --check PASS
- 2026-10-27 (12:35 AM) | paragraph pass | 24 paragraphs of 105 words or more split at their seam, same order, nothing moved or cut (the remaining ones over 90 run 91 to 104 words and are one scene each) | validator 0 errors x3 | punct 0/0 x3 | --check PASS
- Self-review (§8): opening states the point in its first bold line; the three questions are answered word for word in the closing; no era over 4,000 words, so no "By" lines needed, closers on eras 7 and 9; ten era first sentences differ in shape; every added sentence is a restatement, a navigation line or a banked fact (the two Decoration Day additions cite research line 437); narrator stays in the opening, strips, closers and closing; every cut is listed above; 0 em dashes, 0 semicolons
