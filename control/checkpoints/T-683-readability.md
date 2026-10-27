# CHECKPOINT T-683 | drugs-alcohol | readability | the whole chapter (opening, eras 1 to 10, closing)

STATUS: IN-FLIGHT (agent finished; the director sets DONE after reading the report)
VERIFY: python tools/project_state.py --check drugs-alcohol --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md, T-683)
MODEL:  opus
FILES:  manuscript/drugs-alcohol/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md (bank research/research-drugs-alcohol.md only for a PATCH) · hand-off control/backmatter/drugs-alcohol.md

NOW:    nothing. All 13 units landed, 2026-10-27.
NEXT:   the director reads the report. If anything is reopened, every unit below is landed. Method: each era is rewritten into a scratch file and spliced between its hb-time markers by scratchpad T-683/splice.py (markers and the ## heading are never touched).

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | chapter opening (part1, first block of era 1) | landed | card (minutes to reset at the end), spine, anchor (Coles's red D), turn, three questions, Five minutes, Can skip |
| 2 | era 01 before-1500 (part1) | landed | strip; summary re-led on the through-line; 2 labels turned into questions (each answered in its first sentence); hearth, nicotine and addiction glosses folded; Keep It Sacred para split under a lead-in; 3 lead-ins in the plants span; Abbott para re-led (fact first, 1996 second). No cuts. No closer |
| 3 | era 02 1500s (part1) | landed | strip; summary re-led; Nicot label a promise; Hariot: hook, birth year cut, put in date order (Wingina's killing 1586 before the 1588 book), 4 lead-ins; St. Augustine re-led, one of two museum attributions dropped; Mancall's gift line said once (was in summary and span). No closer |
| 4 | era 03 1600s (part1) | landed | strip; summary leads with the through-line; laws label a promise; 1619 para split; pounds/shillings/pence explanation cut to "half a pound" in the sentence; stocks gloss folded; Cole hook; Coles hook (a different detail from the anchor), birth line cut, 4 lead-ins, "oft (often)"; Hudson para split, Kieft para split, 6 lead-ins; King James glosses in parentheses; Massachusetts smoking para split. No closer |
| 5 | era 04 1700-1750 (part1) | landed | strip; summary leads with rum as the through-line, Georgia ban as a lead-in; Molasses Act "It put a tax" made "Under it, importers owed"; indentured gloss folded; 1705 law, 1733 lodge, 1728 duel, 1745 privateer, 1733 Georgia paras re-led off their dates; tavern span given 4 lead-ins; Georgia span 2 lead-ins, pernicious in parentheses; Hamilton: hook, birth line cut, bumper para split, flushed and sundry glosses folded. No cuts beyond the birth line. No closer |
| 6 | era 05 1750-1800 (part1) | landed | strip; summary leads with rum giving way to whiskey; drinking label a question; Sally cut to a Chapter 16 callback plus the rum's part and the harms (see Cuts); Native leaders span split, 2 lead-ins; Rush: hook, ardent spirits gloss folded, 2 lead-ins; Whiskey Rebellion label a promise, 7 lead-ins, every date moved off the front, Bower Hill hedges turned into Known / Not known; Vigol: hook, 4 lead-ins; Washington span re-led, 3 lead-ins. No closer: the era is 2,472 words by the tool, under 2,500 |
| 7 | era 06 1800-1850 (part2) | landed | strip; summary leads with a comparison (almost three times today's drinking); laudanum gloss shortened in the summary; first span relabeled "A dram with breakfast" (was a repeat of era 5's label) and put breakfast first, Bustard dropped as a second attribution (Rorabaugh's count kept); temperance gloss folded, 5 lead-ins, every date moved off the front; Washingtonians: three lead-ins, gall gloss folded (six founders kept by name on purpose: they are the subject); Gough: hook, birth date cut to the year, bookbinding gloss once, 5 lead-ins; Douglass "deemed" in parentheses; Native nations span 3 lead-ins; Sertürner made "a German druggist". No closer (1,761 words) |
| 8 | era 07 1850-1900 (part2) | landed | strip; summary leads with bans versus open sale of drugs, split under 2 lead-ins, "addicted, which means" gloss dropped (a word a child knows); constitution gloss kept once (summary), cut in the Kansas span; 3 labels reworded (2 promises, 1 question); Maine span: riot para split, 4 lead-ins; Civil War: dates off the front, 400,000 claim and the uncounted total as Not known / Disputed; Goolrick: hook, siege gloss folded, 4 lead-ins; medicine span: Courtwright para split, cocaine definition sentence cut (glossed in summary); Pemberton: hook, birth year cut; opium span put in date order (1875, 1883 hoax, 1887, 1896); WCTU: Willard para split, grog shop in parentheses, 5 lead-ins; Native nations para split in three; closer "By 1900" with three bullets |
| 9 | era 08 1900-1950 (part3) | landed | strip; summary leads with "labeling, then banning", split under 2 lead-ins, opium/cocaine/addict glosses dropped (given earlier or known); Carry Nation: hook, birth date cut to the year, constitution gloss dropped, alcoholism gloss folded, 5 lead-ins; 2 labels reworded (promise, question); Harrison span: racist-claims para split, Wright's rape quote explained inside the sentence, the dispute under a lead-in, 7 lead-ins, every date off the front; Prohibition span split, 4 lead-ins; Izzy: hook, 4 lead-ins; agents span: Hamm's article detail cut, 4 lead-ins; poison span: split in 8 paragraphs, death counts as Known / Disputed, jake leg count as Not known; AA anonymous gloss folded; repeal span label a question, Known / Not known; Marijuana span 4 lead-ins; peyote gloss dropped (era 7 re-glossed it). Closer "By 1950": one number with a comparison (cigarettes 54 to 4,345). No By line: the era stays under 4,000 words |
| 10 | era 09 1950-2000 (part3) | landed | strip; summary leads with smoking and the drug budget ($81 million to $18.4 billion), split under a lead-in; drinking-age label a promise; Wynder repeat cut to a callback to era 8; Holiday: 2 lead-ins, Hari/Porter as Disputed, lynching re-glossed once; 1953 span split, discriminatory gloss folded; Nixon span: every date off the front, Ehrlichman quote split under 25 words with criminalizing glossed inside; Ford: hook, intervention and arthritis glosses folded; Busch/Lightner re-led, Disputed pair on lives saved; crack span 4 lead-ins, Hinton's second criminalizing gloss dropped; Wigand: hook, birth date cut, nicotine gloss folded, 3 lead-ins; Oxy span split, "Purdue trained" made "Purdue's managers trained". Closer "By 2000": a question left open, answered in era 10 |
| 11 | era 10 2000-today (part3) | landed | strip; summary leads with the three waves of opioid deaths (answers era 9's question), the provisional peak moved into the span, split under a lead-in; overdose counts split into a rising and a falling paragraph, "about 300 deaths a day" added as the comparison (arithmetic on 107,941); Purdue label now the promise "Why no Sackler went to prison", answered in its first two sentences from Arleo's own words, 10 lead-ins, attorney general and settlement glosses folded; Goldin: hook, birth line cut, 4 lead-ins; marijuana and vaping spans re-led, Schedule III gloss folded. No separate era closer: the chapter closing is era 10's last block (the era is 2,890 words with it, about 2,560 without) |
| 12 | chapter closing (part3, last block of era 10) | landed | the three questions word for word with answers; What changed; five dates (1634, February 13, 1826, January 17, 1920, June 17, 1971, 1996, all in the chapter); Not known (Prohibition poison deaths); Where to go (Temple of Dendur, Metropolitan Museum); Next: Chapter 29, Religion |
| 13 | self-review (§8), checks, measure, back-matter hand-off, report | landed | 24 more paragraphs split at seams (over 90: 26 to 2, both the closer and closing blocks, which the tool counts as one paragraph); 13 more paragraphs re-led off their dates; era first sentences re-read together and 4 reshaped (eras 3, 4, 7, 8: two began with "Rum", two with "between X and Y"); era 5 no longer ends on a death line like era 4; Goolrick Who line trimmed of a repeat (413 to 397 words); card 110, strips 6, 4, 9, 7, 12, 9, 16, 19, 15, 14 from the tool's era_sizes; every "you" is inside a quotation; validator 0 errors x3, punct 0/0 x3, --check prose PASS; hand-off control/backmatter/drugs-alcohol.md written |

<!-- state: todo | working | landed | skipped (say why) -->

## SUBJECT NOTES (the plan, written before any edit)

**Before (measure_readability, 2026-10-27):** words 20402, paras 309, avg_para 66.0, over90 53, date_first 33.3%, def/1k 1.5, attr/1k 7.2, also/1k 1.2, you 13 (all inside quotations), longest era 3709, eras>4000 0, stories 14, story median 365, stories>400 0.
Per-era words (my count, markers excluded): 1: 922 · 2: 772 · 3: 1867 · 4: 1352 · 5: 2441 · 6: 1753 · 7: 2949 · 8: 3699 · 9: 2877 · 10: 2415. About 105 minutes.

**Spine:** People in this land have used drugs and alcohol for at least 12,000 years, and when Americans turned against a drug, the punishment fell hardest on the people who had the least power.

**Three questions:**
1. How long have people here used tobacco, and what did they use it for?
2. What happened when the whole country banned alcohol from 1920 to 1933?
3. Who has been punished for drugs, and who has not?

**Anchor:** Robert Coles's red letter D (era 3 story): in 1634 Massachusetts judges ordered him to wear a D of red cloth on white, hanging from his neck, for a year, after his fourth drunkenness case; Winthrop's journal line. All already in the chapter.

**Five minutes?** "Poisoned alcohol and jake leg" in 1900 to 1950 (about 650 words; the Treasury poison order, the Bellevue deaths, Norris and Lowman, Harry Gross's Jamaica ginger). Label to be rechecked after the era 8 edit.

**Can skip:** "Chewing tobacco" (era 6), "Drinks for voters" (era 4), "The tavern as the town's meeting place" (era 4). Labels to be rechecked after their eras are edited.

**Reading time:** words / 200 rounded to 5, from measure_readability once the closing is written (expect about 105 to 110). Strips from the tool's era_sizes.

**"By" lines:** no era is over 4,000 words. Era 8 (3,699) gets one only if the edit takes it past 4,000.

**Era closers (eras over 2,500 words after the edit):** era 5 (1750-1800, 2,441 now, will pass 2,500 with furniture: three bullets), era 7 (before/after pair, 1850 vs 1900), era 8 (one number with a comparison), era 9 (one question left open, answered in era 10). Eras 1, 2, 3, 4, 6 get the strip only; era 10 ends on the chapter closing.

**Date style:** the draft uses day-month-year ("8 September 1565") throughout. §5.13: month-day-year everywhere. Convert every one.

**Story boxes (14, none over 400):** each gets a bold hook after the record lines; résumé lines (birth dates the story does not use) cut; glosses folded into their sentences.

**Repetition across chapters (§5.12):** Chapter 16, Economy, already tells the *Sally* voyage in full, stage by stage. Here: a callback to Chapter 16 plus the rum angle and the harms in plain words (DECISIONS #36), the stage arithmetic left to Economy. The Whiskey Rebellion is also in Economy, but in about 250 words; this chapter's telling is the only full one in the book (John Connor, Oliver Miller, the enslaved defenders, the barefoot prisoners, the Christmas parade, Vigol), so it stays in full. Billie Holiday's drug arrests: Music (Chapter 33) comes later, so this chapter keeps the full telling. Purdue/Sacklers: Health (Chapter 26) has one paragraph; this chapter keeps the full telling.

**Known trouble spot from the dispatch:** a third of the paragraphs open with a date. Target under 1 in 20.

**Next chapter:** Chapter 29, Religion.

**Where to go (planned):** the Temple of Dendur in the Metropolitan Museum of Art, New York, in the wing where Nan Goldin's group protested in 2018 and that dropped the Sackler name in 2021 (in the chapter; bank line 823 for "on display").

## Cuts (every one, with its reason)

- Era 2, Spanish wine span and summary: Mancall's "some Europeans surely offered it as a gift" stood in both the summary and the span; kept once, in the span.
- Era 2, Hariot: "Hariot was born in about 1560" (résumé).
- Era 3, laws span: "English money was counted in pounds, shillings and pence. Twelve pence made a shilling, and 20 shillings made a pound." Replaced by "half a pound in English money" in the fine sentence (the Coles box still gives five marks as pounds, shillings and pence).
- Era 3, Cole: the bibliographic detail of Drake's book (first printed 1886, enlarged 1917). Drake stays named as the source of the date.
- Era 3, Coles: "Coles was born in England in about 1600" (résumé).
- Era 5, *Sally*: Chapter 16 (Economy) tells the voyage stage by stage. Cut here: the stage counts (19 before leaving Africa, four in the first week, 68 on the crossing, 20 after landing, one on the way to Providence) and the note on the report's 107/108 arithmetic. Kept: 17,274 gallons of rum, chains, shackles and guns; 196 people bought; at least 109 dead by Brown University's count; several children; the woman who hanged herself; "Destroyed 8"; "Some Drowned themselves Some Starved...". So no harm is softer here than in Chapter 16 (DECISIONS #36).
- Era 6, first span: Bruce Bustard named as the writer who gives Rorabaugh's figures (a second attribution for one uncontested count; Rorabaugh stays named).
- Era 7, Pemberton: "Pemberton was born in 1831" (résumé); "earned a medical degree in 1850" kept as "had a medical degree".
- Era 7, medicine span: "Cocaine is a drug made from the leaves of the coca plant" (the era summary glosses cocaine).
- Era 7, Kansas span: the constitution gloss (given in the era summary).
- Era 8, Carry Nation: birth day and month (kept the year and place).
- Era 8, agents span: "Richard F. Hamm, a professor at the University at Albany, gives these figures in a 2026 article in The Conversation" made "by the count of the historian Richard F. Hamm" (attribution kept, bibliography cut).
- Era 9, smoking span: "In the 1940s and 1950s, Ernst Wynder and other scientists linked cigarettes to lung cancer" was a repeat of era 8's sentence; now a one-line link ("The studies that Ernst Wynder and others began in the 1940s went on into the 1950s").
- Era 9, Wigand: "Wigand was born in New York City on 17 December 1942" (résumé).
- Era 3, tobacco span: "Those words show the king's scorn for Native people" (the narrator telling the reader what to think). The quote now sits under "he insulted Native people", which states the same fact.

## Decisions and defects fixed

- Dates: every day-month-year date in the draft converted to month-day-year (§5.13).
- Whiskey Rebellion kept in full although Chapter 16 also tells it: Economy's telling is about 250 words, and this chapter's is the only full one in the book (see SUBJECT NOTES).
- Washingtonian founders: all six names kept in one sentence, against §5.4's three-names guide, because the six are the subject of the span and appear nowhere else.
- Era 5 has no closer: 2,472 words by the tool, under the 2,500 line. Closers: era 7 (three bullets), era 8 (one number with a comparison), era 9 (a question answered in era 10).
- Glosses repeated across eras trimmed to one first use plus at most one later re-gloss (constitution, cocaine, peyote, opium, addiction, criminalizing, patent medicines, withdrawal, overdose, lynching).
- Wright's 1910 testimony: "rape" and "Negro" are now explained inside the sentence (DECISIONS #31, #40, #51).
- Personification repairs made while re-leading: "It put a tax" (Molasses Act) to "Under it, importers owed"; "Purdue trained" to "Purdue's managers trained"; "a 1986 law set" avoided ("Under a 1986 law passed by ... 5 grams of crack carried").
- Defect parked for the audit (source left alone): none found in the bank; the draft's 1933 Kansas sentence and the era 8 Carry Nation box both say the ban ran 1881 to 1948, consistent.

## Log

<!-- One line per save: date-time | unit | what landed | validator | --punct -->
2026-10-27 | part1 eras 1-5 + opening | spliced era by era | validate --part 0 errors after each | punct 0/0 after each
2026-10-27 | part2 eras 6-7 | spliced | validate --part 0 errors | punct 0/0
2026-10-27 | part3 eras 8-9 | spliced | validate --part 0 errors | punct 0/0
