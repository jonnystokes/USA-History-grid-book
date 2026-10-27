# CHECKPOINT T-684 | slavery-freedom | readability | the whole chapter (opening, 10 eras, closing)

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check slavery-freedom --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md)
MODEL:  opus
FILES:  manuscript/slavery-freedom/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md · research/research-slavery-freedom.md (PATCH only) · control/backmatter/slavery-freedom.md

NOW:    all units landed; prose gate PASS (2026-10-27)
NEXT:   nothing; the director reviews and commits

Method: each era is rewritten whole in the scratch folder, then spliced in with a script that
refuses to run unless every hb-time and hb-story marker line is byte-identical. Files keep CRLF.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | chapter opening | landed | spine, Copeland anchor, turn, 3 questions, five minutes, can skip; reading time to confirm at the end |
| 2 | era 01 before-1500 | landed | strip; era paragraph led by through-line; span relabelled "Captives who could become family"; mourning-war gloss folded in |
| 3 | era 02 1500s | landed | strip; through-line first; span split into 5 with bold lead-ins (3 paras over 90 gone); Estevanico: hook, résumé birth line kept short, Known / Not known on his death |
| 4 | era 03 1600s | landed | strip; 6 paras over 90 split; Point Comfort relabelled as a question, servant-or-slave hedge now Known / Not known; Equiano birthplace Known / Not known; Punch hook, glosses folded in; "From servant to slave for life" relabelled "How did a servant become a slave for life?", Massachusetts 1641 moved ahead of Casor 1654 for date order; Negro, rape glossed inside the sentence |
| 5 | era 04 1700-1750 | landed | strip; through-line first; 5 paras over 90 split; 7 date-first re-led; Carolina span relabelled as a question, Fort Mose relabelled "A free town to run to", Negro Act "What the Negro Act took away"; Menéndez hook; lash and justice of the peace glossed inside the sentence |
| 6 | era 05 1750-1800 | landed | strip; through-line first (13 date-first paras before, 0 now); 5 paras over 90 split; "Which states ended slavery first?" label; hooks on Wheatley, Freeman, Judge; Hemings span split with bold lead-ins, DECISIONS #32/#49 wording kept exactly; Wheatley: "the Wheatleys named her" avoided (bank says no source names who chose the name) |
| 7 | era 06 1800-1850 | landed | strip (24 min); through-line first; 13 paras over 90 split to 0 in the body; date-first 10 to 0; By 1830 (top of "Reading made a crime") and By 1840 (top of "The Underground Railroad and the abolitionists"); closer (before/after shape, Mississippi 1830 and 1840); "The slave trade inside the country" relabelled "Sold south"; 7 story boxes given hooks; Douglass birthday moved to the end; Northup kept at about 470 words on purpose (names the kidnappers, the trader, the rescuers and the courts that let them go); Tubman's 19-trips legend kept with the NPS credit; rape, negro, flogging re-glossed once for this part file, lash and Lowcountry not |
| 8 | era 07 1850-1900 | landed | strip (31 min); through-line first; 21 paras over 90 split to 0 in the body; date-first 12 to 0; By 1861 (top of "Freedom taken during the war"), By 1866 (top of "Freedom, day to day"), By 1868 (top of "Black political power"); closer (three dated bullets); Emancipation span relabelled "Who did the Emancipation Proclamation free?"; 7 story boxes given hooks; Revels and Bruce: exact birth dates cut (résumé), birthplaces kept; Celia's pardon cut to one sentence (era 10 owns it); second glosses of Freedmen's Bureau, massacre and Negroes cut; segregation glossed inside the Plessy sentence |
| 9 | era 08 1900-1950 | landed | strip (7 min); 6 paras over 90 split to 0; date-first 6 to 0; Plessy cut to a callback (era 7 tells it), Jim Crow kept here; Alabama convict leasing 1875-1928 numbers cut to a callback (era 7 owns them), Banner Mine, James Knox and the 1928 end kept; Bailey case told in order (story first, ruling second); lynching, poll tax, literacy test, autopsy, advance glossed inside the sentence; 13th Amendment and segregation re-glossed once for part 3; rape not re-glossed; Hughes: hook from his own words, birth year a Not known line |
| 10 | era 09 1950-2000 | landed | strip (4 min); through-line first; 2 paras over 90 split; 4 date-first re-led; amendment glossed inside the sentence; the Courlander settlement told once (in the Haley box), the span keeps one sentence; Haley hook from the family story, Not known line on Kunta Kinte |
| 11 | era 10 2000-today | landed | strip (10 min, closing not counted); through-line first; 9 paras over 90 split; 5 date-first re-led; Celia's pardon owned here, with a one-sentence recap of her story; Cherokee Freedmen and Sherman's forty acres cut to callbacks (era 7 owns them); hooks on Short-Colomb and Davis (Davis's own words) |
| 12 | chapter closing | landed | three questions word for word, What changed, five dates (1640, 1662, 1808, 1865, 1964, chosen not to repeat the era 7 closer), Not known (1619 servants or slaves), Where to go (NMAAHC), Next (Chapter 25); about 300 words, a little over the 280 target |
| 13 | back-matter hand-off | landed | control/backmatter/slavery-freedom.md: 150 glossary lines, 24 people, 15 dates, 11 places, 7 movies, 3 questions |

## SUBJECT NOTES

**Before (measure_readability.py):** 20,268 words, 281 paragraphs, avg 72.1, 70 over 90 words,
23.5% date-first, def/1k 1.6, attr/1k 5.8, also/1k 1.4, you 5, longest era 6,106 (1850-1900),
2 eras over 4,000, 24 stories, median 259, 1 over 400 (Northup 474).

Era sizes before: before-1500 241 · 1500s 681 · 1600s 1,839 · 1700-1750 1,895 · 1750-1800 1,883 ·
1800-1850 4,729 · 1850-1900 6,106 · 1900-1950 1,565 · 1950-2000 746 · 2000-today 2,041.

**Spine:** Slavery here was built on purpose, one law and one sale at a time, and enslaved people
fought it until it ended in 1865, then had to fight again when white lawmakers and mobs took much
of their new freedom away.

**Anchor:** Thornton Copeland's "Information wanted" advertisement, *Colored Tennessean*, Nashville,
October 1865: sold away from his mother Betty in Richmond in 1844; item 918 of more than 5,000 in
"Last Seen"; no record shows whether he found her. (All in era 7.)

**Three questions (repeat word for word in the closing):**
1. How did a servant in Virginia become a slave for life, and a child a slave from birth?
2. How did enslaved people fight back?
3. What happened to the freedom people won in 1865?

**Five minutes?** the span "How did a servant become a slave for life?" (relabelled from "From
servant to slave for life, 1640 to 1705") in The 1600s.

**Can skip:** "Enslaved builders of the capital" (1750-1800), "Churches and hush harbors"
(1800-1850), "Roots and the search for family" (1950-2000). Nothing later depends on them.

**"By" lines:** 1800-1850 (two), 1850-1900 (three). **Era closers:** 1800-1850 and 1850-1900 only
(the other eras stay under 2,500 words; era 10 carries the chapter closing).

**Next chapter:** Chapter 25, Rights and Movements (it takes the campaigns from 1877 on).

**Repetitions inside the chapter to cut to callbacks:** Alabama convict leasing told in full in
era 7 and again in era 8 (era 7 owns it); Plessy told in era 7 and era 8 (era 8 owns the Jim Crow
laws, era 7 keeps one sentence); Celia's 2024 pardon told in era 7 and era 10 (era 10 owns the
pardon, era 7 keeps a line); Cherokee Freedmen treaty in era 7 and era 10; Sherman's forty acres in
era 7 and era 10. Words glossed again and again (rape, Negro, flogging, lash, clause, census,
segregation, Freedmen's Bureau, militia, appeal, pardon, massacre, Lowcountry, 13th Amendment):
glossed once, re-glossed at most once in a later part file where a reader opening there would be
lost (flogging, a clinical word, keeps its full explanation at first use).

## Decisions and defects fixed

- Reading time on the card: 21,110 words, so about 105 minutes (the build's rounding). Era strips use each era's own words; era 1 and era 10 do not count the opening and closing.
- Era closers only in eras 6 and 7: every other era is under 2,500 words of body.
- Phillis Wheatley: the draft's "her first name came from the ship" kept, but no sentence says who chose it (the bank says no source names who did).
- William Harvey Carney's Who line keeps the NPS wording ("the earliest act of ... bravery to be recognized"), not "the first Black recipient", which would be wrong.
- Jefferson and Hemings: the DECISIONS #32 / #49 wording kept exactly; only split into shorter paragraphs with lead-ins.
- Nothing was added that is not already in the chapter or the bank. One restated comparison per big number, computed from the chapter's own figures (one in seven died on the crossing, more than 400 times the 1790 cotton crop, more than a hundred times the 1700 rice, almost six times the 1790 enslaved count, about one in four county prisoners died, three times as many enslaved people in Mississippi).
- The 1808 actor: "a federal law ... took effect on January 1, 1808" (bank: Act Prohibiting Importation of Slaves, signed March 2, 1807).

## Cuts (each with its reason)

- Era 8, "Forced labor after slavery": the Alabama convict-leasing paragraph's repeat of era 7 (1875 to 1928, Tennessee Coal, 95 percent Black, 181 of 745 died) cut to a one-line callback. Era 7 tells it in full; telling it twice in one chapter is repetition.
- Era 8, "Segregation and the stolen vote": the full retelling of Plessy cut to a callback; era 7 tells the ruling.
- Era 7, "Celia, 1855": the pardon's details and the definition of a pardon moved out; era 10 tells the 2024 pardon. One sentence stays.
- Era 9, "Roots and the search for family": the Courlander settlement and genealogists paragraph cut to one sentence, because the Haley story box tells it in the same words.
- Era 10: Celia's recap trimmed to her story in one sentence (no new loss: era 7 has it all); the Cherokee 2,500 figure and the treaty's background cut to a callback (era 7 has it); Sherman's land cut to one clause.
- Revels and Bruce box: exact birth dates (September 27, 1827, March 1, 1841) cut as résumé; birthplaces kept.
- Repeated glosses cut: rape (third gloss), Negro (third and fourth), clause (second), census (second), segregation (third), Freedmen's Bureau (second and third), militia, appeal, pardon, massacre, lash and Lowcountry (second each).
- Story boxes: opening sentences that only restated the Who line were cut where the hook now does the work (Estevanico, Punch, Menéndez, Freeman, Judge, Douglass, Pieh, Northup, Truth, Tubman, Scott, Kossola, Smalls, Taylor, Revels and Bruce, Hughes, Haley, Short-Colomb).

## What I chose not to do

- Northup's box stays at about 470 words: it names the kidnappers, the trader, the rescuers and the courts that let them all go, and cutting any of it would hide who did what.
- The 1850 to 1900 era stays name-heavy. The names are the people who killed, freed, judged and testified, and the hard-subjects policy wants actors named.
- Three paragraphs still open with a date ("In 1534", "In the 1840s", "In 2017"), under 1 percent; in each the date is the point of the sentence.
- Attribution stays at 5.7 per thousand words: what is left is contested counts, witness accounts and named historians' judgments.

## Log

- 2026-10-27 | opening, eras 1-5 | spliced into part1 | validator 0 errors | punct 0/0. Note: a `sed -i` touch-up stripped the file's CRLF (Git Bash sed does that); restored with unix2dos and checked (405 CR for 405 lines). All later edits went through a CRLF-keeping script.
- 2026-10-27 | eras 6-7 | spliced into part2 | validator 0 errors | punct 0/0
- 2026-10-27 | eras 8-10, closing | spliced into part3 | validator 0 errors | punct 0/0
- 2026-10-27 | --check slavery-freedom --stage prose | PASS
- After: 21,110 words, 431 paragraphs, avg 49.0, 6 over 90 (the opening turn, two closers, the closing card, the era 7 lead paragraph at 92, the *Wanderer* paragraph at 91), 0.7% date-first, attr/1k 5.7, you 8 (all in furniture or quotes), longest era 6,229, stories median 265, 1 over 400 (Northup, on purpose).

## Cuts (each with its reason)

## Log
