# CHECKPOINT T-674 | education | readability | whole chapter (opening, 10 eras, closing)

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check education --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md, T-674)
MODEL:  opus
FILES:  manuscript/education/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md

NOW:    done; report sent to the director
NEXT:   nothing for a successor; the director reads the result

Method: each era is rewritten whole in the scratch folder
(`...\scratchpad\T-674\eraNN.md`) and spliced between its hb-time markers by `splice.py`, which
refuses the splice if any hb-time or hb-story marker line changes, the span count changes, the
zooms do not balance, or an em dash or semicolon is present. Files are CRLF and stay CRLF.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | chapter opening (part 1, era 1 first block) | landed | card (time to be reset at the end), spine, anchor (Bray School building and Isaac Bee), turn, 3 questions, five minutes, can skip |
| 2 | era 01 before-1500 | landed | strip; summary no longer date-led; apprentice/integral/Indigenous glosses folded into their sentences; wampum para split under two lead-ins; the founding-date hedge made a Disputed line; "No names survive" made a Not known line. No cuts, no closer |
| 3 | era 02 1500s | landed | strip; summary leads with the through-line (priests taught to convert), split; mission/conversion/friar/doctrine glosses folded; St. Augustine para re-led off its date; Paquiquineo: hook, the opening explanation moved to a closing "Why this story is here" line, 5 lead-ins, the hanging para split, Menendez tied back to St. Augustine. No cuts, no closer |
| 4 | era 03 1600s | landed | strip; summary re-led and split; Boston Latin para split (Whose land, The first schoolmaster), archaic words glossed in parentheses, Collegiate made a Disputed line; 1642 law split, master gloss folded; Old Deluder lead-in; Cheever: hook, classroom lead-in, birch-rod gloss; Barnard: date moved off the front, correct-gloss folded, The other boy lead-in, Not known line, Spare the rod lead-in, monk gloss cut (a child knows it); Deer Island split into four paras, two "No record" sentences merged; charter defined here once; Harvard enslavers lead-in; Caleb: hook, benefactor gloss folded; Timucua: 200,000 to 2,000 given as one in a hundred, Raids lead-in. Cuts below. No closer (2,319 words) |
| 5 | era 04 1700-1750 | landed | strip; summary split, through-line first (most children learned at home), 1740 moved to the second paragraph; 1740 law span split into six paras under lead-ins (The law, The uprising before it, Why writing), scribe/forfeit/forge glosses folded; Protestant defined once here, in the Harry and Andrew span; dame school/hornbook split; literacy span split under Men, Women, Enslaved people; Ursuline and Moravian paras re-led off their dates; school-day span made a Known / Not known pair; William & Mary split (Four captive boys); Dock: hook, Brumbaugh introduced at first mention, whipping gloss folded into the quote's sentence, the 170-word para split in three. No cuts, no closer (2,387 words) |
| 6 | era 05 1750-1800 | landed | strip; summary split (Williamsburg school its own paragraph); Jefferson span split under The plan / Who was left out, archaic words glossed in parentheses; Land Ordinance re-led off its date, ordinance gloss folded, Knepper's duress gloss folded, Whose land lead-in; girls' academies split (Litchfield), natural philosophy gloss folded; Bray School re-led off its date, Psalms/Prayer Book/Creed/curriculum glosses folded, How many pupils and The schoolhouse lead-ins; Ann Wager: hook, journeyman gloss folded, Isaac Bee lead-in, the AP hedge made a Not known line; Georgia and Wheelock paras re-led off dates, The money Occom raised lead-in; Webster: hook, birth date cut, Blue-Backed Speller lead-in; Teaching as a job ends on a Not known line. No closer (2,347 words). Part 1 done: validator 0 errors, punct 0/0 |
| 7 | era 06 1800-1850 | landed | strip; summary leads with "The free public school began as an argument in Massachusetts", split (the South its own paragraph); Mann span re-led off 1837, common-school gloss folded, Free for whom lead-in; Mann story: hook, birth line cut, The secretary lead-in, passive election made active; one-room span split, Two terms lead-in; normal school and Miles re-led; Swift: hook, Laura Bridgman lead-in, dumb gloss folded; pay span split under The pay in 1838 (Massachusetts women's pay given as less than a third of men's); Beecher: hook, Hartford and The salt lead-ins, pious glossed in parentheses, dates put in order (1847, 1852, 1857); hitting span split, schoolmasters lead-in; one By line (By 1845) after the dunce passage; McGuffey eclectic gloss folded; deaf/blind span split under two lead-ins and re-led off dates; Catholic span split into New York, Philadelphia, Southwark, nativist/seminary/bishop glosses folded, "The Catholic Church used" made "Catholics used"; enslaved-reading span split under Virginia, North Carolina, The other states, Walker and Turner, lash/grand jury glosses folded, "His Appeal urged" made "In it he urged"; Civilization Fund extinction and inadequate glossed in parentheses, Choctaw Academy split; Canaan split, The oxen lead-in, yoke gloss folded; Sarah Roberts: hook, The lawsuit lead-in, colored gloss folded. Closer By 1850 (three bullets). No cuts except the Mann birth line (see Cuts). 4,800 words |
| 8 | era 07 1850-1900 | landed | strip; summary in three paragraphs, through-line first ("School became a legal duty"); compulsory label made a promise ("When school became the law"), its gloss folded; Morrill span re-led off dates, cession gloss folded, $400,000 against $17.7 million given as "more than forty times"; Freedmen's Bureau span re-led and split (count, months, subjects); attacks span split under Georgia 1869, Tennessee and Delaware, Memphis and Cross Plains, proscribed glossed in parentheses, Confederacy/lynch glosses folded; By 1870 line; Forten: hook, birth line cut, Salem and St. Helena Island lead-ins, misanthrope glossed in parentheses; Norfolk split under The arrest / The sentence, constable gloss folded; separate-schools span split under North and West, Plessy 1896, Augusta 1899 ("the constitution forbade" made "the men who wrote the constitution forbade"); women's colleges split under three lead-ins; Boston rules split, corporal punishment re-glossed once (first use in part 2); By 1899 line; Foster: hook, scene split into six paras, age made a Disputed line, The hearing lead-in; summer span The middle ground lead-in; Catholic 1884 re-led, archbishop/pastor glosses folded; Carlisle span split under Fort Marion, Setting up the school, Arrival, An Army post, Work without pay, The dead, Rations, The count, The punishments, disease/flogging/cuffing/sexual abuse glosses folded; Zitkala-Sa: hook, shingled glossed in parentheses, Where it happened lead-in; Washington: hook, birth line cut, Tuskegee lead-in. Closer By 1900 (before/after pair, 1850 / 1900). 6,205 words |
| 9 | era 08 1900-1950 | landed | strip; summary in three paragraphs, through-line first (high school went from rare to ordinary); HS span re-led, Depression lead-in; one-room span tightened; Fields: hook, birth line cut, Grown-ups too lead-in, migrant/colored glosses folded; child labor split, The courts lead-in; hitting-rules label made a promise ("Who could hit a child, city by city"), split under San Francisco / New Haven and Omaha, corporal punishment and rattan re-glossed once (first use in part 3); By 1920 line; Carlisle hearing re-led on Julia Hardin, split into twelve paras under The hearings, Julia Hardin, The beating, Afterward, The end of Carlisle; Dewey span split; Dewey: hook, The school lead-in; tests span: the second gloss of intelligence test cut (summary has it), Terman's 60-word quote given in four pieces under 25 words each with every word kept, abstractions glossed, eugenics gloss folded, Army tests and SAT lead-ins; By 1926 line; disabled span re-led ("No law before 1950"), special education gloss folded; German and Oregon spans split, Klan re-glossed once (first in part 3) as a sentence of history; textbooks split, Scopes lead-in, "the book said" made "states"; Buck: rape glossed in plain words (DECISIONS #31), committed/epileptic folded, Holmes's 50-word quote given in four pieces under 25 words (every word kept), vaccination gloss folded, The test case and The operation lead-ins, the clinical salpingectomy passage kept whole; By 1927 line; separate-schools span split under The 1917 survey, Rosenwald schools, Martha Lum, Lemon Grove and Bastrop, "Mississippi's constitution kept" made "Under Mississippi's constitution", 22.22 against 1.78 given as more than twelve times; boarding-schools span split under The numbers, The Meriam Report, Food and sickness, The children's work, Uintah, The whippings, the Meriam quote split in two with glosses in parentheses, tuberculosis/trachoma glosses folded; marriage bar lead-in; New London re-led off its date; camps span split, Poston lead-in; Mendez: hook, The lawsuit lead-in; G.I. Bill split, Black veterans lead-in. Closer By 1950 (one number with a comparison). 8,380 words |
| 10 | era 09 1950-2000 | landed | strip; summary leads with the through-line (judges and lawmakers opened the schools, officials fought them), split; Brown re-led off its date, desegregate gloss folded, With all deliberate speed lead-in; Little Rock split into fourteen paras under The Guard, The mob, Inside, The Lost Year, integration/segregationist glosses folded; Sputnik re-led; Virginia span split under Prince Edward County, Five years without school, supervisors gloss folded; By 1964 line; Ruby Bridges: hook, marshal/sharecrop/psychiatrist glosses folded, The test and What it cost her family lead-ins; Meredith split, The riot lead-in; prayer span split under Engel, Schempp, Yoder, Black's 31-word quote given in two pieces under 25 (every word kept); ESEA re-led, Johnson's 26-word line given in two pieces, Head Start and Title IX lead-ins, the 36-word Title IX text given in two pieces; By 1972 line; college span split, The 1965 law and The cost lead-ins, Johnson's Cotulla line given in pieces under 25; speech span split under The armbands / The braids, deportment glossed in parentheses; Black teachers/bus span: "Then came the buses" cut for a lead-in, Boston lead-in; boarding 1970s: "the Bureau ran" made "officials of the Bureau ran", Crownpoint 1968, A National Tragedy, Taken from their families lead-ins, frostbite/anthropologist glosses folded, "Its purpose was" made "Lawmakers wrote it to"; By 1978 line; Spanish span split under Hit for speaking Spanish, The children's own words (two long essay lines given in pieces under 25, every word kept), The law in Texas, The walkouts, Lau 1974, "the Blackwell School taught" made "teachers at the Blackwell School taught"; Hawaiian span re-led and split; new-kinds span split under Magnet schools, Segregation academies, Catholic schools, Charter schools, charter gloss folded, Negro gloss folded; disabled span split under Seven children and The 1975 law, epilepsy re-gloss folded into the seizure explanation; By 1990 line; Mills: hook, The case / The ruling lead-ins; paddle span split under James Ingraham, Ingraham v. Wright, The states, the 30-word opinion line in two pieces, Eighth Amendment gloss folded into Powell's sentence, Andrews passive given its actor (staff); home span split under Holt and the Moores / The courts, dubious glossed in parentheses, courts as actors made "the justices of"; DeJonge: hook, the second certificate gloss cut, The trial and Nine times in court lead-ins; Nation at Risk: the 30-word quote in two pieces, "it began the argument" made "the argument ... began with this report"; strike span split under New York 1960, Florida 1968, The pay, union gloss folded; last one-room schools given a comparison (617 against 59,652, about one in a hundred). Closer By 2000 (one question, answered in era 10). 10,394 words |
| 11 | era 10 2000-today | landed | strip; summary split, through-line first (which school, what was taught, how learning was measured); NCLB span: achievement-gap and proficient glosses folded, Bush's 28-word line in two pieces, What the tests covered / The 2015 law / How many tests lead-ins, prescriptive glossed in parentheses, standardized-test gloss folded; choice span split under Private schools, Public money for private school (the three standalone definitions rebuilt as one / another / the third), The argument over the money, "Studies of one program found" made "Researchers who studied"; homeschool span split, 2020 and The rules lead-ins, agency actions given their staff, "Texas requires" made "Texas law requires"; By 2023 line; special education re-led off "By the 2020s"; separate-schools span The South lead-in (answers era 9's closing question); school-year span split under The four-day week and Start times, devices para re-led; paddle span re-led, The 2026 count and Suspensions lead-ins, "students were hit" given its actor (school staff), suspension gloss folded; By 2022 line; shootings span split under A narrower count, Sandy Hook 2012, Parkland 2018, Uvalde 2022, Apalachee 2024, the four "He ..." sentences in a row merged, 327 against 30 given as more than ten times, prosecutor and grand jury glossed (first use in part 3); closures re-led, the second pandemic gloss cut; Rosproy: hook, Teaching from home lead-in; test scores split, Twelfth grade lead-in; By 2025 line; teachers span split, The pay lead-in; college span Canceling loans lead-in, principal gloss folded, default para re-led; boarding-investigation span: The reports / The apology lead-ins, the 2022 punishment list (told in full in era 7) cut to one sentence that still names every punishment, "First Nation had reported" given its leaders; book-bans span split under Counting bans, Limits on teaching, Mahmoud v. Taylor, orientation/identity/guise/LGBTQ glosses folded; Department span The court fight lead-in, unilateral gloss folded. Closer By today (three bullets). 7,628 words with the closing |
| 12 | chapter closing (part 3, era 10 last block) | landed | three questions answered word for word; What changed; five dates (all in the chapter); Not known (the boarding-school death count); Where to go (Bray School building, the anchor); Next: Chapter 31, News and Communication |
| 13 | self-review, checks, back-matter hand-off, report | landed | read the opening, closing and era 4 aloud; fixed "the charity wanted" (now the men who ran it), tense in the turn, "long before" (an added intensifier), three standalone glosses missed in the first pass, 23 institution-as-actor sentences (courts, a union, a church, "each state set", reports that "found" or "said"), five By lines and one closer bullet that stretched a fact ("about 1,000 magnet schools" by 1990 made "more than 1,000"; "Members of Congress were paying for Head Start" made "Federal money paid for"); added By 1884 (era 7) and By 1948 (era 8) where 3,000 words ran without a stop; split the last body quotation over 25 words; checked every Can skip / Five minutes label exists, the five closing dates appear in the chapter, the card time matches build_full_book.py's rule (230); wrote control/backmatter/education.md. Validator 0/0/0, punct 0/0 x3, --check prose PASS |

## SUBJECT NOTES (the plan, written before any edit)

**Chapter card:** Chapter 30 of 37 · School and Education · 10 eras · reading time set at the end
from measure_readability (words / 200, rounded to 5). Before the edit: 44,320 words = about 220.

**Spine:** School in America grew from a reading lesson for a few children into a right for every
child, and at every step the adults in charge decided which children could come in and what could
be done to them there.

**Three questions** (word for word in the closing):
1. When did school become free, and required, for every child?
2. Which children were kept out of school, and how did they get in?
3. Is it still lawful for a teacher to hit a child?

**Anchor:** the Williamsburg Bray School building (era 5): enslaved and free Black children aged
three to ten learned to read there from 1760, taught by Ann Wager, while the London charity that
paid wanted them taught that slavery was God's will; one pupil on the 1765 list, Isaac Bee, ran
away in 1774 and his enslaver warned that he could read; the building was moved to Colonial
Williamsburg on February 10, 2023 (all in era 5).

**Five minutes?** "Punished for speaking Spanish" in 1950 to 2000.
**Can skip:** "The academies", "Catholic schools become a system", "The school year and the school
day", "The last one-room schools".

**Era words before the edit (words / 200):** 1: 549 (3) · 2: 862 (4) · 3: 2,433 (12) · 4: 2,439 (12)
· 5: 2,308 (12) · 6: 4,599 (23) · 7: 6,033 (30) · 8: 8,129 (41) · 9: 9,941 (50) · 10: 7,027 (35).
Paragraphs over 90 words: 205 of 510. Date-first: 18.4 percent. Stories over 400: 6 of 21.

**Closers (eras over 2,500 after the edit):** 6, 7, 8, 9, 10, and any of 3 to 5 that end up over
2,500. Rotate the middle: 6 = three bullets; 7 = before/after pair (1850 / 1900); 8 = one number with
a comparison (high school graduates, 6 in 100 to 51 in 100); 9 = one question answered in era 10
(did the schools stay desegregated?); 10 "By today" = three bullets, then the chapter closing.
**"By" lines (eras over 4,000):** era 6 one; era 7 two; era 8 three; era 9 four; era 10 three.

**Five dates to keep (closing):** April 23, 1635 Boston Latin School opens · May 10, 1740 South
Carolina's law against teaching enslaved people to write · 1852 the first law that made children
attend school (Massachusetts) · October 6, 1879 the first children reach Carlisle · May 17, 1954
*Brown v. Board of Education*.
**Not known:** how many children died at the federal Indian boarding schools (at least 973; the
investigators' own report says the real number is higher).
**Where to go:** the Williamsburg Bray School building at Colonial Williamsburg, Virginia.
**Next:** Chapter 31, News and Communication (control/chapter-registry.md: how Americans learned
what was happening).

**Trouble spots (dispatch and measurement):** longest era 10,062 words by the tool (1950-2000); average
paragraph 87 words; 205 paragraphs over 90; 18 percent date-first; attribution 7.6 per 1,000 (keep the
counts and witnesses, drop the uncontested "X states"); era summaries open on several dated facts in
a row (lead with the through-line); glosses as sentences of their own throughout (fold them in);
re-glosses of words already explained earlier in the chapter (corporal punishment, flogging,
tuberculosis, grand jury, reservation, segregated, charter, colored) cut to one gloss per chapter,
with one re-gloss allowed in a later part file where a reader opening there would be lost.

**Cross-chapter overlap (§5.12):** government-politics (Ch 20) also tells Buck v. Bell, Engel,
Yoder, Ingraham, Brown. This chapter's tellings are the school angle and are left whole: cutting
them would collapse worked passages (DECISIONS #52), and the dispatch names no repeat here.

## Cuts (every one, with the reason)

<!-- era | what was cut | why -->
- era 3 | Cheever story: "He was born in London on January 25, 1615. Some sources give 1614, because the English calendar then began the year on March 25" | birth-date résumé (§4.8); the When line keeps "Born in London in 1615", and the calendar fact is told in the Boston Latin span
- era 3 | Barnard span: the gloss of "monk" | a word an 11-year-old knows (guideline 7)
- era 6 | Mann story: "He was born on May 4, 1796, into" (now "He grew up in") | résumé; the When line keeps the birth date
- era 7 | Forten story: "She was born in Philadelphia in 1837, into" (now "She grew up in Philadelphia in") | résumé; the When line keeps the year and place
- era 7 | Washington story: "He was born in 1856 on" (now "He grew up on") | résumé; the When line keeps it
- era 8 | Fields story: "She was born in Charleston in 1888." | résumé; the When line keeps it
- era 8 | tests span: "An intelligence test is a set of questions meant to measure how quickly and how well a person can think." | the era summary three paragraphs earlier glosses the same word
- era 9 | DeJonge story: "A certified teacher is one who holds that license." | the sentence before it already explains the certificate
- era 9 | bus span: "Then came the buses." | a fragment for emphasis, replaced by the lead-in "The buses."
- era 10 | boarding-investigation span: the full second telling of the 2022 punishment list with its glosses (solitary confinement, flogging, cuffing) | era 7 tells the same list in full; the era 10 sentence still names every punishment plainly (DECISIONS #52, a repeat cut to a short restatement)
- era 10 | closures span: the second gloss of "pandemic" | the era summary glosses it
- era 5 | Webster story: "He was born on October 16, 1758" | résumé; the When line keeps the full birth date and place

## Rules broken on purpose

- Six story boxes over 400 words, the same six as before: Paquiquineo 477 (a chain of sourced events, voyage, mission, killings, hangings, with no résumé left), Dock 422 (his rewards and punishments are the point of the box), Josephine Foster 536 (the committee's own blow-by-blow report and the hearing, which the hard-subjects policy keeps whole), Zitkala-Ša 432 (her own words of the haircut), Ruby Bridges 607 (the year inside Frantz and what it cost her family), DeJonge 417 (nine court rounds over ten years). Every box now opens with a hook of 12 words or fewer and has no paragraph over 90 words.
- Quotations over 25 words stay only inside story boxes (Shaw in Sarah Roberts, Zitkala-Ša's account, Rosproy), as §5.10 allows. In the body every long quotation was split into pieces under 25 words with every word kept (Terman, Holmes, Hugo Black, Johnson twice, Title IX, Bush, A Nation at Risk, the Meriam Report, the Ingraham opinion, the Spanish essays).
- Five eras still run over 4,000 words (6: 4,803 · 7: 6,230 · 8: 8,425 · 9: 10,408 · 10: 7,640). The grid fixes the content. They carry 1, 3, 4, 4 and 3 By lines and a closer each, so the longest run without a stop is about 2,700 words (era 6, By 1845 to its closer).
- Glosses in some later part files repeat a word glossed in an earlier part (corporal punishment, rattan, grand jury, Klan, reservation, flogging, tuberculosis), once per part file at most, because a reader opening part 2 or part 3 would be lost without them (guideline 7's one re-gloss).
- The measure's 6 paragraphs over 90 are the furniture blocks (the opening turn, five closers and the closing, whose lines it reads as one paragraph).
- Cross-chapter overlap with government-politics (Buck v. Bell, Engel, Schempp, Yoder, Ingraham, Brown) left whole: these are the school angle, and the dispatch names no repeat for this chapter.

## Could not improve

- Attribution stays at 7.4 per thousand (was 7.6). What remains is counts that depend on who counted (Alvord, the Meriam team, the federal surveys, PEN America, EdChoice, NPR, the Civil Rights Project), witnesses and court records (Barnard, Julia Hardin, the Uintah testimony, Ellison), and disputes (Collegiate against Boston Latin, the Bray School count, Carlisle's numbers). DECISIONS #37 and #45 keep those.
- Span labels: only two changed ("When school became the law", "Who could hit a child, city by city"). Most labels were already promises or plain and clear ("Why school boards hired women", "Where the summer break came from", "How separate the schools are now"), and the opening's Can skip and Five minutes lines name labels that stay fixed.
- Era 9 is still the longest era in the chapter at 10,408 words.
- The chapter grew from 44,320 to 46,249 words (measure's count); the furniture is the increase, minus the cuts listed above.

## Decisions and defects fixed

- Defects found and fixed in the prose (none in the bank or outline): the anchor's "the London charity wanted" and the era 10 "the federal government kept" (institutions acting) now name the men and officials; the Mills Who line no longer says a case "gave" a right; courts as actors made judges or justices throughout; "Studies found", "the report found", "the union said" given their people.
- No PATCH to the bank: every furniture sentence restates a fact already in the chapter. The comparisons added (three in four, one in a hundred, one in twenty, less than a third, more than forty times, more than twelve times, about two in five, nearly eight times, more than ten times, about one in a hundred) are arithmetic on figures already in the chapter.
- Carrie Buck: "rape" glossed as "sex forced on her" (DECISIONS #31, the word explained in plain words at first use); the clinical salpingectomy passage kept whole.

## Log

<!-- date-time | unit | what landed | validator | --punct -->
- 2026-10-27 | units 1-5 | opening, eras 1-4 spliced into part 1 | 0 errors | 0/0
- 2026-10-27 | unit 6 | era 5 spliced; part 1 complete | 0 errors | 0/0
- 2026-10-27 | unit 7 | era 6 spliced into part 2 | 0 errors | 0/0
- 2026-10-27 | unit 8 | era 7 spliced; part 2 complete | 0 errors | 0/0
- 2026-10-27 | unit 9 | era 8 spliced into part 3 | 0 errors | 0/0
- 2026-10-27 | unit 10 | era 9 spliced | 0 errors | 0/0
- 2026-10-27 | unit 13 | self-review fixes, By 1884 and By 1948 added, back-matter hand-off written | 0 errors x3 | 0/0 x3 | --check prose PASS
- 2026-10-27 | units 11-12 | era 10 and the closing spliced; card set to 230 minutes (46,155 words / 200 = 230.8, rounded to 5); era first sentences varied (three "in these fifty years" removed) | 0 errors x3 | 0/0 x3 | --check prose PASS
