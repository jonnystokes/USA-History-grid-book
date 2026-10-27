# CHECKPOINT T-675 | religion | prose (readability edit, second edition) | all 10 eras

STATUS: IN-FLIGHT            (agent finished all 13 units; the director sets DONE)
VERIFY: python tools/project_state.py --check religion --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md)
MODEL:  opus
FILES:  manuscript/religion/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md · research/research-religion.md (PATCH only if needed)

NOW:    finished. All units landed, --check religion --stage prose PASS.
NEXT:   nothing for this task. The director reviews and commits.

Method: each era is rewritten whole in the scratchpad (T-675\era-<id>.md) and spliced in by
T-675\splice.py, which refuses the splice unless every original marker line survives in order.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 0 | chapter opening (era 01 first block) | landed | card (reading time 200 is a placeholder until the end), spine, Po'pay anchor, turn, 3 questions, five minutes, can skip |
| 1 | era 01 before-1500 | landed | strip; summary re-led on the through-line (hundreds of nations, hundreds of religions), date moved off the front; first span relabeled "What the ground can show, and what it cannot"; archaeologist, missionary, clan, migration path, equinox glosses folded into their sentences; lead-ins "Woodhenge", "Whose name?"; Cahokia's closing hedge made a Not known line; earthworks para re-led. No cuts, no closer (under 2,500) |
| 2 | era 02 1500s | landed | strip; summary leads with what the friars came to do; Catholic, order, friar, mission, baptism glosses folded; lead-ins (Missions and government, Workers for St. Augustine, The first group, The second group, The governor's revenge, Lucas, Acoma, What the friars said, The killing, The sentences, The children); 1565, Guale, Lucas and Acoma paragraphs split (6 over 90 to 0); Guale hedge made a Not known line; 5 date-first openings moved. Doña María: hook (her own quoted credit), Not known line. No cuts |
| 3 | era 03 1600s | landed | strip; summary split in three, through-line first, Puritan/Quaker/Trinity glossed once there (span re-glosses cut: Quakers, Trinity, Puritans); 2 labels ("Why the Puritans left England", "Maryland, 1649: freedom for Christians, death for others"); By 1650 (end of Reading for God) and By 1677 (end of Quakers); closer By 1700 (three bullets); about 20 lead-ins; 19 paras over 90 to 0; date-first 17 to 0 (the two By lines aside); Leighton hedge made a Not known line; apprentice, prejudice, charter, epidemic, ploughman (now "farm worker"), moderation glosses folded or replaced; one comparison added (three in four died, arithmetic on the chapter's own figures); "you" in the Toleration gloss removed. Stories: Mary Dyer hook (ladder and rope) and lead-in; Williams hook ("forced worship stinks"), "born in London, son of a merchant" cut (Who/When lines carry London 1603), lead-ins; Hutchinson hook ("rather been a Husband"), birth line cut (When line carries it), magistrate gloss folded |
| 4 | era 04 1700-1750 | landed | strip; summary leads with the revivals (revival gloss folded), 1704/1741 moved to a third paragraph; lead-ins (Ayubale, Patale, How many were taken, Princeton, The fires of 1741, The hunt for priests, The trial); 11 paras over 90 to 0; 10 date-first to 0; label "Should enslaved people be taught Christianity?" (answered in its first sentence); closer By 1750 as a before/after pair (the 1690 and 1771 New York drawings). Whitefield: hook (eggs and dead cat), birth line cut (When line), lead-ins, the "is estimated" passive made "by one estimate"; stays about 530 words (preaching plus his push for slavery in Georgia, all sourced events). Edwards: hook (spider over the fire), birth date and "went to Yale in 1716" cut, inoculation gloss folded, lead-ins; stays about 670 words because it carries the sermon, the people he enslaved by name, and the Mohican land loss, none of which is résumé |
| 5 | era 05 1750-1800 | landed | strip; summary leads with the church-tax argument, split in three with a "New churches and new missions" lead-in; stocks gloss moved up to first use; Virginia span relabeled "How Virginia ended its church tax"; the Gentile/Mahometan/Hindoo/Infidel glosses put in parentheses inside the quoted sentence; religious-test gloss turned into a plain restatement; Payson's 29-word quote cut to its key phrases (under 25 words); By 1791 line at the end of "The last church tax"; Gnadenhutten given a callback to Chapter 22, War, with the full harms kept (DECISIONS #36); mission counts get one comparison (about seven deaths for every ten baptisms, arithmetic); closer By 1800 in the "one number" shape; 16 paras over 90 to 0; date-first 9 to 1 (By line aside). Allen: hook (pulled off his knees), birth date cut (When line), lead-ins, two paras split; stays about 620 words for the walkout scene in Allen's own words. Jones: hook (family sold), birth date cut (When line), diocese gloss folded. Toypurina: hook (21 arrested), closing hedge made a Not known line |
| 6 | era 06 1800-1850 | landed | strip; summary keeps the revival through-line first, the six societies made one list sentence, "Mobs and splits" lead-in, one sentence added on California (restates the span); Protestant and revival re-glosses dropped (eras 2 and 4 own them), communion, militia, shackles and flogging re-glossed once each for part 2; By 1844 (end of "Whose Bible?") and By 1845 (end of "The churches split over slavery"); closer By 1850 as an open question answered in era 7 (parish schools); about 30 lead-ins; 31 paras over 90 to 0; date-first 14 to 0 (By lines aside); Danites/vigilante, exterminate, nativist, nun, retainer glosses folded. Haun's Mill kept in full (Chapter 5 has a shorter telling; this chapter's is the religious one). Joseph Smith: hook (100 men at the jail), lead-ins, three paras split; about 670 words, kept for the Nauvoo land dispute and the trial. Finney: hook (the retainer), the long birth-and-wilderness quote cut to its last phrase (see Cuts), lead-ins |
| 7 | era 07 1850-1900 | landed | strip; summary leads with the growth of Catholics and Jews and the Protestant fight against it; "The end of slavery" and "On the reservations" lead-ins; the Jewish population figures left to the span (they were stated twice); census personification fixed ("Census takers counted"); Grant's 32-word order quoted in pieces under 25 words; Mountain Meadows: lead-ins, the Young question made a Disputed line; about 20 lead-ins; 16 paras over 90 to 0; date-first 8 to 0; deacon and class-leader re-glosses cut (era 6 explains both, same part file); bigamy, Taoism, Romanism, steward, boarding-school, unprecedented, annihilated, sect, open-secret glosses folded; comparisons added (about half of 417 schools; Jews about a hundred times as many in 1880 as 1800, arithmetic). Wounded Knee kept as one plain sentence with a callback to Chapter 2. Closer By 1900 as a before/after pair (one in twenty Catholic, one in six). Frazier: hook ("land, and turn it and till it"), lead-ins |
| 8 | era 08 1900-1950 | landed | strip; summary keeps its through-line first, the revival re-gloss dropped, "Attacks" and "On the reservations" lead-ins; the opening restatement of the 1883 rules cut to a one-sentence callback to era 7 (see Cuts); By 1915 (end of the Leo Frank span) and By 1929 (end of the evolution-laws span); closer By 1950 with three bullets; about 20 lead-ins; 15 paras over 90 to 0; date-first 14 to 0 (By lines aside); Butler Act, Darrow and Jackson quotes cut under 25 words with nothing lost (Jackson's "fixed star" kept as its own short quote); catechist, circular, pardon, bigot/ignoramus, speaking-in-tongues glosses folded; castration and castor oil keep their full clinical explanations. Black Elk: hook ("the pipe religion"), birth line folded into the vision paragraph, lead-ins. Seymour: hook (the hallway), birth date cut (When line), lead-ins. McPherson: hook (motorcycle), "born in 1890" cut (When line), lead-ins, disappearance split; about 570 words, kept for the radio temple, the Depression meals and the five missing weeks |
| 9 | era 09 1950-2000 | landed | strip; summary first sentence now states the era's through-line (settling religion in public schools and public life, mostly in court), then four short paragraphs with lead-ins; synagogue/mosque, deacon, atheism, Trinity, Communist glosses folded or given once for part 3; By 1958 (end of the Atlanta synagogue span) and By 1987 (end of "Evolution in court again"); closer By 2000 in the "one number" shape (about 145 attacks on Black churches); Waco "who fired first" made a Disputed line with the House report's better-supported finding first; O'Connor quote cut under 25 words; about 30 lead-ins; 29 paras over 90 to 0; date-first 22 to 0 (By lines aside). Revis: hook (Laverne saw the bomb), deacon gloss moved to the span, lead-ins. Graham: hook (King's prayer), degrees trimmed (see Cuts), lead-ins. Yoder: hook (the only child who testified), lead-ins |
| 10 | era 10 2000-today | landed | strip; summary first sentence shortened to the through-line ("Fewer Americans have belonged to a congregation since 2000"), with the 2007 figure added from the span for comparison; "Abuse and courts" lead-in; By 2018 (end of the Charleston/Sutherland Springs/Pittsburgh span) and By 2024 (end of the United Methodist span); no era closer (the chapter closing ends the era); about 35 lead-ins; 33 paras over 90 to 0; the Charleston court quote (40 words) given in pieces under 25 words; Pope Francis quote cut under 25 words; white supremacist, gay, LGBTQ+, petitioner, stonewalling, misappropriate glosses folded; grand-jury and nun/order re-glosses cut (see Cuts); sexual abuse and rape keep their plain explanations; comparisons added (one priest in twenty-five, about seventeen times as many incidents, more than one adult in four, all arithmetic on the chapter's figures); one "today" only, in the era label. Saini: hook ("the dignity of being a statistic"), lead-ins. Kennedy: hook (the 50-yard line), first sentence split, lead-ins |
| 11 | chapter closing (era 10 last block) | landed | three questions word for word (checked by script against the opening and the hand-off), What changed, five dates, Not known (Cahokia's Woodhenge), Where to go (the Po'pay statue, closing the loop on the anchor), Next: Chapter 30, School and Education. 272 words |
| 12 | back-matter hand-off control/backmatter/religion.md | landed | six sections only: Glossary (about 300 terms with era labels), People (20 story subjects), Dates (closing five plus ten), Places (10), Movies (none: no Movie lines), Questions (3, matching the closing). 0 em dashes, 0 semicolons |

## SUBJECT NOTES (decided before writing)

**Before (measure_readability.py):** words 39,038 · paras 472 · avg_para 82.7 · over90 176 ·
date_first 21.8% · def/1k 1.9 · attr/1k 7.6 · also/1k 1.9 · you 24 · longest_era 5,919 ·
eras>4000 6 · stories 20 · story_med 455 · stories>400 11.

Per era (words): 01 895 · 02 1,622 · 03 4,924 · 04 2,727 · 05 4,023 · 06 5,425 · 07 3,771 ·
08 4,392 · 09 5,783 · 10 5,476.

**Spine:** Freedom of worship in the United States grew one fight at a time, and most of those
fights were started by people who were being punished for their faith.

**Anchor:** the statue of Po'pay in the US Capitol (National Statuary Hall Collection, 2005).
Cliff Fragua of Jemez Pueblo carved the whipping scars on its back. Spanish officials had Po'pay
flogged in public in 1675 for Pueblo ceremonies; in 1680 he led the rising that kept the Spanish
out of New Mexico for twelve years. (All in era 03.)

**Three questions:**
1. Why did colonists who crossed the ocean to worship freely punish other people for their faith?
2. How did Americans stop paying taxes to support churches?
3. How long did US officials treat Native ceremonies as crimes?

**Five minutes?** "Quakers punished in Massachusetts" in The 1600s.
**Can skip:** "Three more colleges with church backing", "Laws against teaching evolution, 1921 to
1929", "Worship on a screen", "Teaching religion at home".

**Next chapter:** Chapter 30, School and Education.

**Furniture plan:** strips on all ten eras. "By" lines: era 03 two, era 05 one, era 06 two, era 08
one or two, era 09 two, era 10 two. Era closers on eras 03 to 09 (era 10 ends on the chapter
closing; eras 01 and 02 are under 2,500 words). Closer middles rotate: bullets, before/after,
one number, an open question.

**Dispatch trouble spot:** 24 "you" in the prose. Check each: quotations stay; narrator "you" only
in furniture.

**Reading time:** words / 200 rounded to 5: 40,690 words, about 205 minutes (the build's own count agrees: 205, card set to 205).

**After (measure_readability.py, final):** words 40,690 · paras 730 · avg_para 55.7 · over90 3 (the opening's turn at 118 words, inside the guide's 80 to 120, and two furniture blocks counted as one paragraph each) · date_first 0.0% · def/1k 1.2 · attr/1k 7.2 · also/1k 1.6 · you 29 (every one inside a quotation or in furniture) · longest_era 6,115 · eras>4000 6 · stories 20 · story_med 458 · stories>400 14.

## Sources in hand

None needed so far; every furniture fact restates the chapter.

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

- "you" (dispatch trouble spot): the original 24 were all inside quotations (Endecott, Edwards's sermon, the St. George's trustee, Wovoka, Higbee, McPherson's sermon title, King's letter, Saini, Kennedy, the Revis sisters) except one narrator "you" in the Toleration Act gloss, now removed. The body has no narrator "you". Darrow's "and you know it" went when his quote was cut under 25 words.
- Story boxes kept over 400 words on purpose: Williams 463, Hutchinson 438 (two trials and her death are the story), Whitefield about 510 (preaching plus his push for slavery in Georgia), Edwards 675 (the sermon, the named people he enslaved, the Mohican land), Allen 624 (the walkout in his own words), Smith 668 (the Nauvoo land dispute and the trial), Finney 505, Black Elk 420, McPherson 573 (the radio temple, the Depression meals, the five missing weeks), Graham about 415, Kennedy 428 (two readings of one record). Each lost its résumé lines (see Cuts). What is left is sourced events, not birth-to-death lists.
- Repetition across chapters (5.12): Gnadenhutten gets a callback to Chapter 22, War, and Wounded Knee a callback to Chapter 2, Native Nations, with the harms still named in plain words (DECISIONS #36). Haun's Mill, Deer Island, Po'pay and Mother Emanuel are told here for their religious side and kept. The earlier chapters' tellings were checked by grep, not read in full.
- Inside the chapter, era 8 now calls back to era 7 for the 1883 penalties instead of restating them.
- Furniture facts: every By line, closer and the closing restate the chapter. Added comparisons are arithmetic on the chapter's own figures. No bank PATCH was needed.
- Corrections made while checking furniture against the body: the era 6 summary first said the mission whippings stopped when Mexican officials took over (the span says those officials whipped people too); the By 1929 line first said Klan members "pushed through" the Oregon law (they put it on the ballot and voters passed it); the By 2024 line first credited "the bishops" with the count (John Jay researchers working for them made it). All three fixed.
- Date-first openings: 0 by the measure. About twenty paragraphs open with a bold lead-in followed by a date, the form 4.7 allows. Seven plain date-first paragraphs created by splits were reordered.
- Era first sentences read together and varied: two "Americans spent these years" and two "preachers held revivals" openings rewritten.

## Cuts (each with its reason)

- era 03 Roger Williams: "He was born in London about 1603, the son of a merchant." Résumé line; the When line keeps London and 1603. "son of a merchant" is the only fact lost.
- era 03 Anne Hutchinson: "She was born about 1591 in Alford, England." The When line carries it.
- era 04 Whitefield (second trim): "He first reached Georgia in May 1738. He came back in November 1739, landing at Philadelphia, and reached Savannah in January 1740." Résumé. The When line keeps "Seven visits to America from 1738".
- era 09 Graham (second trim): the 1939 ordination, the Florida Bible Institute and Wheaton College, the film company and the newspaper column. Résumé. The crusades, King's prayer and letters, and the honors stay.
- era 10 football span: "The chaplain was the student who said the prayers." (repeated the sentence before it) and the second "On June 19, 2000" (the span's first sentence gives the date).
- era 10 re-glosses already given earlier: grand jury in the priests span (the era summary carries it), and "Sisters, also called nuns, are women who belong to Catholic religious orders, groups whose members make religious promises and live and work together" (now "sister, or nun"; eras 2 and 6 explain orders and nuns).
- era 07 summary: the Jewish population figures were stated in the summary and again in the span. Kept in the span only.
- eras 06 and 08: re-glosses of Protestant and revival (eras 2 and 4 explain them).
- era 09 Graham: "He earned a degree in theology, the study of religious belief, at the Florida Bible Institute in 1940 and a degree from Wheaton College in Illinois in 1943. That August he married Ruth Bell." became "He studied at the Florida Bible Institute and at Wheaton College in Illinois, and in 1943 he married Ruth Bell." Résumé trim; the degree years are lost.
- era 08 first span: the repeat of the 1883 penalties ("For a first dance the punishment was losing food rations for up to ten days. After that it was fifteen to thirty days without rations, or up to thirty days in the agency jail. A medicine man could be jailed for at least ten days.") cut to a one-sentence callback; era 7 states them in full.
- era 08 McPherson: "She was born in 1890" (When line). Seymour: "He was born on May 2, 1870, at Centerville, Louisiana" (When line). Black Elk: "in December 1863" (When line).
- era 07 ministers span: "A deacon is an officer who helps run a church, and a class leader led a small group of members." Era 6 explains both in the same part file.
- era 06 Finney: his opening quote "I was born in Warren, Litchfield county, Connecticut, August 29, 1792. When I was about two years old, my father removed to Oneida county" cut to "to a great extent, a wilderness" with Oneida County kept. The When line carries Warren and the date. Lost: the move at age two.
- era 06 California span: "Franciscans are members of a Catholic religious order, and their priests and brothers are called friars." Era 2 explains it.
- era 05 Virginia span: "Virginia's established church was the Church of England. Colonists had to attend its services and pay taxes for its ministers." The era summary says the same thing three paragraphs earlier.
- era 05 Allen: "He was born into slavery on February 14, 1760." Jones: "on November 6, 1746." Both When lines carry the dates.
- era 04 deists: "Deists were always a small group." It repeated "A small number of colonists" one sentence earlier.
- era 04 Whitefield: "He was born in Gloucester, England, on December 16, 1714." The When line carries it. Edwards: "He was born on October 5, 1703, in East Windsor, Connecticut" (When line) and "He went to Yale in 1716" (résumé; "first in the class of 1720" stays).
- era 03 span re-definitions of Puritans, Quakers and the Trinity, now glossed once in the era summary (guideline 7).

## Log

2026-10-27 | opening, era 01, era 02 | landed in part1 | validator 0 errors | punct 0/0
2026-10-27 | era 03 | landed in part1 | validator 0 errors | punct 0/0
2026-10-27 | era 04 | landed in part1 | validator 0 errors | punct 0/0
2026-10-27 | era 05 | landed in part1 (part 1 complete) | validator 0 errors | punct 0/0
2026-10-27 | era 06 | landed in part2 | validator 0 errors | punct 0/0
2026-10-27 | era 07 | landed in part2 (part 2 complete) | validator 0 errors | punct 0/0
2026-10-27 | era 08 | landed in part3 | validator 0 errors | punct 0/0
2026-10-27 | era 09 | landed in part3 | validator 0 errors | punct 0/0
2026-10-27 | era 10 + chapter closing | landed in part3 (part 3 complete) | validator 0 errors | punct 0/0
2026-10-27 | self-review pass (first sentences, By lines, hooks, date-first, reading times) | all parts | validator 0 errors x3 | punct 0/0 x3
2026-10-27 | back-matter hand-off | control/backmatter/religion.md | 0 em dashes, 0 semicolons
2026-10-27 | FINAL | python tools/project_state.py --check religion --stage prose | PASS
