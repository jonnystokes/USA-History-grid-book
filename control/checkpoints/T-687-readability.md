# CHECKPOINT T-687 | immigration | readability | the whole chapter (opening, eras 1 to 10, closing)

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check immigration --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md, T-687)
MODEL:  opus
FILES:  manuscript/immigration/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md (bank research/research-immigration.md only for a PATCH)

NOW:    nothing. All 13 units landed, 2026-10-27. --check immigration --stage prose PASS.
NEXT:   the director reads the report. If anything is reopened, every unit is landed (part3 is LF; parts 1 and 2 are CRLF: run unix2dos -q after any Write to them).

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | chapter opening (part1) | landed | spine, Lazarus-plaque anchor (with the 1882 law a year earlier), turn (118 words), 3 questions, five minutes, can skip; reading time 95 placeholder, confirm at the end |
| 2 | era 01 before-1500 (part1) | landed | strip; era summary leads with "No one from across the ocean came to settle"; Chapter 2 population paragraph cut to one range sentence + callback; Leif retelling cut to a Chapter 1 callback, kept the immigration angle (only camp before Columbus, 1021 wood, 6,000-year Native site, stay of a few years to twenty). No closer |
| 3 | era 02 1500s (part1) | landed | strip; summary leads with the through-line (came to conquer, almost none stayed; only St. Augustine lasted); span relabeled "Which settlement lasted?" answered in sentence 1; 4 lead-ins (Seloy, Fort Caroline, Roanoke, What White found); 3 long paras split; "continental" dropped for "US mainland"; feast-day and council-house glosses folded. No cuts, no closer |
| 4 | era 03 1600s (part1) | landed | strip; summary re-led on indentured servants (the era's through-line); Jamestown: 2 lead-ins, 1 split, "joint-stock company" spelled out, Chesapeake gloss folded, date-first "In the Chesapeake" re-led, 80-90% given as eight or nine of ten; 1619: date moved off the front, privateer gloss folded, long para split, lead-in; Frethorne: hook (his own words), loblollie glossed in parentheses, date-first last para re-led; Plymouth: Laud para split with lead-in, ears/branding sentence re-led on the three writers; Hutchinson: hook, banished gloss folded, Cotton named in sentence 1, archaic words glossed in parentheses inside the quote, 2 lead-ins, death para split off; Dutch: 1664 re-led; Jewish refugees: refugee gloss folded; Huguenots: lead-in, date off the front. Cut: Hutchinson "born in 1591 in Alford" (résumé). No closer (1,769) |
| 5 | era 04 1700-1750 (part1) | landed | strip; summary re-led on the through-line (not English, many bound), its repeat of the span numbers (200,000 / 2,100 / 12,000) dropped since the spans give them; Germans span relabeled as a promise "Why Germans and Scots-Irish left home", answered in sentence 1; Test Act lead-in, communion gloss folded, split; Zenger: Who line now says why he matters, hook (one issue missed), apprentice and bail glosses folded, 2 lead-ins, split; convicts: lead-in, date off the front, emigrate gloss folded; Charleston: Sullivan's Island lead-in, quarantine gloss folded, Wood para re-led (and a broken clause fixed: "and say that"). Cuts: Zenger "born in 1697", "sailed for New York in April 1710", "He died on July 28, 1746" (the When line keeps the death date). No closer |
| 6 | era 05 1750-1800 (part1) | landed | strip; summary leads with the citizenship rule; Hamilton: Who line one clause, hook (the hurricane letter), orphan/clerk glosses folded; Loyalists: date-led para merged and re-led, gloss folded; Naturalization span relabeled "Who could become a citizen in 1790?", answered in sentence 1 with the law's words; Toussaint: hook, 2 lead-ins, yellow fever gloss folded, 1990/1996 date-first sentences re-led; Saint-Domingue: date off the front, split. Cut: Toussaint "He died on June 30, 1853" from the body (When line keeps it). No closer. Part 1: validator 0 errors, punct 0/0 |
| 7 | era 06 1800-1850 (part2) | landed | strip; summary re-led on the through-line (first big wave, Germans and Irish, mobs against Irish Catholics), split, the 1808 sentence re-led; 1807 law re-led, importation gloss folded, "After 1808" re-led; Forty-Eighters: date-first para re-led with a lead-in, split; Bruns: hook, glosses folded; mobs span: 5 lead-ins (Charlestown, Philadelphia, St. Philip de Neri, Who was blamed), six long paras split, "convicted" glossed in parentheses in the quote, pardon and militia glosses folded, $10,000 vs $100,000 given as ten times; famine: date-first opening re-led, "about 1 million died" made "at least 1 million" to match the 1 to 1.5 million range later in the span, 4 lead-ins, 3 long paras split, perverse/turbulent glossed in parentheses inside the quote; Kennedy: hook, date-first para re-led. Cut: Bruns "She died in 1899" from the body (the When line keeps it). No closer (2,161 words) |
| 8 | era 07 1850-1900 (part2) | landed | strip; summary re-led on the through-line (the first group shut out by law); Know-Nothings: date-first para re-led, Bloody Monday lead-in, long para split; Schurz: hook; Clotilda: date off the front, Foster's burning moved up beside the landing (it happened then), 2 lead-ins, split; Chinese West: 3 lead-ins (railroad, strike, count of the dead), causes of death put before the count, the hedging run turned into a Known / Not known pair; Page/Exclusion: date-first paras re-led, exclusion and ethnicity glosses folded; "By 1882" line at the seam (about word 2,000); attacks span: the "In the cases below" line cut to a plain statement, 6 place lead-ins, LA para (190 words) split in three, Rock Springs, Eureka, Tacoma/Seattle, Hells Canyon split; pogrom span: lead-in, split, May Laws split; Castle Garden date-first re-led; Annie Moore, Berlin, Wong: hooks, lead-ins, splits. Cut: Schurz birth line and "he died in 1906" (the When line keeps both). Closer "By 1900" (one number: 61 years). Era is 4,101 words, so one "By" line. Part 2: validator 0 errors, punct 0/0 |
| 9 | era 08 1900-1950 (part3) | landed | strip; summary re-led on the through-line (peak, then quotas), quota gloss folded, date-first para re-led; melting pot lead-in, gloss folded; Capra: hook, birth date cut, 1946 sentence re-led; Bacos: hook, birth date cut, long para split with lead-in; Angel Island (the "five minutes" span): refusal rate given its own short para, dormitory gloss folded, 3 lead-ins (doctors, paper sons, poems), board para split, the two short closing paras merged; Lee Puey You: hook, date-first para re-led; quota span relabeled "How the quota laws of 1921 and 1924 worked", 2 date-first paras re-led, lead-ins, long para split, homogeneity glossed in parentheses inside the quote; eugenics: Laughlin para split (his "expert" title moved up beside the hearings), model-law gloss folded, sterilization kept at full clinical explanation, Buck and Germany split off with lead-ins, "Virginia could sterilize" made "Virginia officials"; Repatriation: date-first para re-led, repatriation and relief glosses folded, raids para split, La Placita re-led, braceros re-led; St. Louis: date-first re-led, Kristallnacht para split, the Holocaust sentence made active (Nazis killed 254), DP Act re-led. Closer "By 1950" (before/after pair). No cuts beyond the two birth dates |
| 10 | era 09 1950-2000 (part3) | landed | strip; summary re-led on 1965 (the era's through-line); 1954: date off the front, 3 lead-ins (who ran it, roundups, heat), long paras split, sunstroke gloss folded, the run of "no record" sentences turned into one Not known line, the count para (165 words) split in three with a lead-in; García: hook, birth date cut; 1965 span relabeled "What the 1965 law changed", answered in sentence 1, act made the instrument not the actor; Cubans: 2 date-first paras re-led; Arenas: Who line simplified, hook, birth date cut, 2 lead-ins, splits (box about 400 words, kept: a chain of charges, prison and a forced confession, all sourced, and the hard-subjects policy forbids compressing it); boat people: date-first paras re-led, pirates lead-in; Tung Trinh: hook, captain lead-in, cannibalism gloss folded; Brin: hook, communist-country gloss folded; IRCA: date off the front, "the law let the government" made "officials could". Closer "By 2000" (the open question, answered by the 2023 count in era 10) |
| 11 | era 10 2000-today (part3) | landed | strip; summary re-led ("share ... rose almost to its highest ever ... detention than ever before"), its facts put in date order; Who comes now: date-first re-led, Pew list split; DHS: 9/11 sentence re-led, 2 lead-ins, DACA para split, "DACA has faced challenges" made "Lawyers and judges have fought over DACA"; border deaths: 895 given as more than three times 2018, GAO sentence re-led, auditors re-led, IOM lead-in; children taken: 5 lead-ins, Horowitz split, apprehended/minors glossed in parentheses inside the quote, counts split, settlement re-led; 2025-2026: detention gloss folded, 4 lead-ins, Lunas Campos split ("The report" made "The human rights groups' report" so it is clear which report), removals split, shootings split, state-police sentence re-led; Giannis: hook, birth date cut, one restated sentence added linking to Wong Kim Ark (the 1898 ruling); Lost Boys: hook, long para split with lead-in. No separate closer: the chapter closing is the era's last block, as in the pilot |
| 12 | chapter closing (part3) | landed | three questions answered word for word, what changed, five dates (1565, 1790, 1882, 1924, 1965), Not known (railroad dead), Where to go (Ellis Island), Next (Chapter 5, Migration Across America). Card time 95 confirmed with build_full_book.load_chapter (19,412 words) |
| 13 | back-matter hand-off control/backmatter/immigration.md | landed | six sections: glossary (about 200 terms), 20 people, 15 dates, 13 places, 6 movies, 3 questions; no semicolons or em dashes |

## SUBJECT NOTES

Measured before (measure_readability.py): 18,326 words, 259 paras, avg 70.8, 65 over 90 words,
21.2% date-first, def 2.4/1k, attr 5.1/1k, also 1.7/1k, 13 "you", longest era 3,897, 0 eras over
4,000, 20 stories, median 249, 1 over 400.

Era sizes (era_sizes, words): 1: 353 · 2: 622 · 3: 1,751 · 4: 1,200 · 5: 1,083 · 6: 2,137 ·
7: 3,891 · 8: 3,068 · 9: 2,602 · 10: 2,903.

Dispatch trouble spot (applies): era 1 repeats Chapter 2's opening (how many people lived here,
the population estimates) and retells Leif Erikson, which Chapter 1 owns. Cut both to callbacks
(ARCHITECTURE-GUIDE 5.12), keep the immigration angle (the Norse camp did not last; people had
lived at the spot for 6,000 years).

**Spine:** People came here to stay from almost every country on earth, and in every era the
Americans already here argued, voted and sometimes fought over who could join them.

**Anchor:** Emma Lazarus's poem "The New Colossus" (1883), written to raise money for the
statue's pedestal; nobody read it at the 1886 opening; Georgina Schuyler had it cast on a bronze
plaque mounted inside the pedestal in 1903. One year before the poem, Arthur signed the Chinese
Exclusion Act (1882). All in era 7.

**Three questions:**
1. Why did people leave home to come here?
2. Who did Americans try to keep out, and how?
3. Who could become a citizen, and how did that change?

**Five minutes:** "Angel Island" in 1900 to 1950.
**Can skip:** "The Dutch and the Swedes" (1600s), "Jewish communities" (1700 to 1750), "The
Revolution and the Loyalists" (1750 to 1800).

**Furniture plan:** strips in every era. No era is over 4,000 words, so "By" lines only where an
era grows past 4,000 or a long era needs a stop (era 7, about 3,900: one "By 1882" line at the
seam before the Chinese laws if it crosses 4,000, or as a stopping place). Closers for eras over
2,500 words: 7, 8, 9 (and 6 if it grows past 2,500), rotated shapes: 6 three bullets, 7 one
number, 8 before/after, 9 question answered in era 10. Era 10 ends on the chapter closing (as the
pilot did), no separate closer. Next chapter: Chapter 5, Migration Across America. Forced arrival
from Africa belongs to Chapter 24, Slavery and Freedom.

## Sources in hand

(none needed beyond the chapter and bank so far)

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

- Era 4 summary had claimed in a draft line that most newcomers were not English. The chapter says only "large numbers"; the summary now names the Scots-Irish and Germans instead (no overclaim).
- Era 6 famine: "about 1 million died" sat beside "1 million to 1.5 million" later in the same span. Now "at least 1 million" (consistent with the range).
- Era 4 Wood paragraph: the original had a broken clause ("put at least 200,000 ... and that about 40 percent"); fixed to "and say that".
- Span labels changed: "Which settlement lasted?" (1500s), "Why Germans and Scots-Irish left home" (1700-1750), "Who could become a citizen in 1790?" (1750-1800), "How the quota laws of 1921 and 1924 worked" (1900-1950), "What the 1965 law changed" (1950-2000). Labels named in the opening's "five minutes" and "can skip" lines are unchanged.
- No bank PATCH needed: every furniture sentence restates the chapter.

## Cuts (each with its reason)

- Era 1: the four-source population paragraph (Denevan 3.8 million, the 1978 atlas, 18 to 20 million, Fixico) cut to one range sentence and a callback to Chapter 2, which owns the count (dispatch, ARCHITECTURE-GUIDE 5.12).
- Era 1: the Leif Erikson retelling (sagas, Vinland, Erik the Red, the tree-ring method, "only exact date") cut to a callback to Chapter 1, which owns it. Kept: the camp, 1021, only known camp before Columbus, Native people there 6,000 years, a short stay.
- Era 4: the era summary's repeat of the span numbers (200,000 Scots-Irish, 2,100 and 12,000 Germans) dropped; each number stays in its span.
- Story résumé lines: Hutchinson born 1591 in Alford; Zenger born 1697, sailed April 1710, died 1746 (When line keeps it); Toussaint died 1853 (When line keeps it).
- More résumé lines, each kept in its When line: Bruns died 1899; Schurz born March 2, 1829, died 1906; Capra born May 18, 1897; Bacos born December 18, 1904; García born June 13, 1937; Arenas born July 16, 1943; Giannis born December 6, 1994.
- Era 7: "In the cases below" (a line about the text itself) became a plain statement.
- Era 9: three "no record" sentences in a row merged into one Not known line (no fact lost).

## Measurements after (measure_readability.py)

19,412 words, 368 paras, avg 52.8, 3 over 90 words (all three furniture: the opening's turn at 118, the era 8 closer and the closing list as the tool joins their lines), 0.0% date-first, def 1.3/1k, attr 5.1/1k, also 1.5/1k, 19 "you" (all in quotes, Lee Puey You's name and "If you remember" lines), longest era 4,096 (era 7, one "By 1882" line), 20 stories, median 251, 1 over 400 (Arenas, kept on purpose).

## Log

- 2026-10-27 | opening + eras 1-5 | part1 rewritten | validator 0 errors | punct 0/0
- 2026-10-27 | eras 6-7 | part2 rewritten | validator 0 errors | punct 0/0
- 2026-10-27 | eras 8-10 + closing | part3 rewritten | validator 0 errors | punct 0/0
- 2026-10-27 | self-review pass (era first sentences varied, box glosses folded, hooks checked at 12 words or fewer) | all three parts | validator 0 errors | punct 0/0 | --check prose PASS
- 2026-10-27 | back-matter hand-off written | control/backmatter/immigration.md
