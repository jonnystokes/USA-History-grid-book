# CHECKPOINT T-662 | government-politics | readability | whole chapter (opening, 10 eras, closing)

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check government-politics --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-DISPATCH.md, T-662)
MODEL:  fable
FILES:  manuscript/government-politics/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md

NOW:    done; final report written to the director. (The Minnesota detail landed in era 9.)
NEXT:   nothing for a successor; the director reads the result and Jon reads the chapter.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | chapter opening (part 1, era 1 first block) | landed | card, spine, anchor (Pory), turn, 3 questions, five minutes, can skip |
| 2 | era 01 before-1500 | landed | strip; intro now follows the Haudenosaunee and tells the reader the other two are short; 2 labels reworded (promise, question); council para split; 1988 para: 3 definitions folded; Known/Disputed on the founding date; archaeologists definition folded |
| 3 | era 02 1500s | landed | strip; viceroy re-definition cut (defined in the intro); missionary folded; 2 date-first paras turned; one pointer to era 3 |
| 4 | era 03 1600s | landed | strip; intro split; Oñate label a promise; killings: Known/Disputed; the 218-word sentence paragraph is now five with lead-ins (sentences, children, Hopi men, feet, ruling); tribute folded; 1624 para split with lead-ins; Pory story: hook, résumé cut (see Cuts); Mayflower label a promise; Massachusetts vote split; 1642 school para split, two definitions folded |
| 5 | era 04 1700-1750 | landed | strip; intro rewritten so its first sentence differs from span 1 (jury first); span 1 label a promise, para split; 1723 para split; Zenger span: 2 paras split, lead-in "What the verdict did not change", defense folded, one uncontested attribution dropped (Historical Society); Zenger story hook, 2 small cuts (see Cuts); Hamilton story hook, para split |
| 6 | era 05 1750-1800 | landed | strip; intro split, first sentence now "Fifty-six men signed..."; Declaration and Convention date-firsts turned; NJ vote para split with pointer to era 6; three-fifths lead-in and split; Washington story hook, Farewell para split, 22nd Amendment detail moved to era 9 (pending, see Decisions), enslaver para lead-in and split; Madison hook; 1790 citizen para rewritten (two "also"s gone); Lyon trial para split; closer "By 1800" (three bullets) |
| 7 | era 06 1800-1850 (part 2) | landed | strip; intro split, first sentence no longer date-led; Marshall hook, para split; Louisiana "The deal." / "The question it raised." and split; vote span: three state lead-ins, date-firsts turned; Anti-Masonic split, electoral-vote re-definition cut; Jackson hook, 188-word removal para now two with lead-ins (law, Trail of Tears), Worcester split with lead-in, veto lead-in, House-vote dispute in one sentence; Stevens para split |
| 8 | era 07 1850-1900 (part 2) | landed | strip; intro opens on the Louisiana numbers (130,344 to 5,320) then split; Dred Scott split; secession date-first turned; Lincoln hook, two paras split, "The arrest." lead-in; Morrill date-first turned and split; Tweed two lead-ins, four paras; 1876 split; Rainey hook, birth date and end-of-life résumé cut (see Cuts), Klan para split with lead-in; Mississippi/Louisiana span: five lead-ins, eight paras; Plessy and Cumming split; closer "By 1900" (before/after pair) |
| 9 | era 08 1900-1950 (part 3) | landed | strip; intro rewritten (no longer opens on a definition; "justices" re-definition cut; sterilize folded; pointer to Plunkitt); Plunkitt hook and split; food law date-first turned; 1913 span: two lead-ins, tariff folded, split; Guinn split; Nineteenth split; **By 1920**; Native citizenship lead-in and three paras; Teapot Dome: two lead-ins, four paras, two minor names demoted to roles (see Cuts); school-law span: three question lead-ins, nine paras; Buck v. Bell: three lead-ins, 207-word para now three; **By 1927**; FDR hook, three splits, "Did the plan change the justices' minds?" lead-in, "The camps." lead-in; camps split; poll tax / white primary lead-ins and splits; 1948 three paras, electoral-vote re-definition cut; closer "By 1950" (one number with a comparison) |
| 10 | era 09 1950-2000 (part 3) | landed | strip; intro now opens on Clair Engle's vote, split; 22nd Amendment gets the 1947 proposal and the Minnesota ratification (moved from era 5); 24th date-first turned, Harper split; Brown II split; Marshall story: hook (the law school), opens on the Maryland rejection, four-jobs para second, cases split, last para trimmed (see Cuts); Engel split; Reynolds split; LBJ hook, "Precinct 13." and "The vote counter." lead-ins, 180-word para now three; civil-rights span: four lead-ins, seven paras; **By 1965**; immigration split; school-law span (824 words): five lead-ins, eleven paras; **By 1977**; Watergate span: four lead-ins, nine paras; homeschooling split; Clinton split; closer "By 2000" (an open question, answered in era 10's first span) |
| 11 | era 10 2000-today (part 3) | landed | strip; Bush v. Gore split; "Money." / "Maps." / "Maps drawn by race." lead-ins and splits; schools span: four lead-ins, 205-word para now three; January 6 span: four lead-ins, ten paras; impeachments split; Moss story: hook (the ginger mint), "The count." / "What followed." / "The lawsuit." lead-ins, 220-word para now three, contempt-of-court definition folded; felony lead-in and split; Menendez and DHS splits; closer "By today" (three bullets) |
| 12 | chapter closing (part 3, era 10 last block) | landed | the three questions word for word with answers; What changed; five dates (1619, 1803, 1870, 1920, 1974); Not known (the Acoma feet); Where to go (Independence Hall, from the Hamilton story and the bank line 443); Next: Chapter 21 |
| 13 | self-review (ARCHITECTURE-GUIDE §8), checks, report | landed | card set to 140 minutes from measure's 27,595 words (build's rule: /200, rounded to 5); strips from each era's words /200; validator 0/0/0, punct 0/0 on all three files, --check prose PASS, build_full_book.py gives no warning for this chapter |

## SUBJECT NOTES (the plan, written before any edit)

**Spine:** The rules of American government were written by people, and in every era people with
power rewrote them, most often to decide who could vote and who could not.

**Three questions** (word for word in the closing):
1. Who decided who could vote, and how did the answer change?
2. When did judges first cancel a law, and what have they done with that power since?
3. What happens when a president, a senator or a governor breaks the law?

**Anchor:** John Pory's report of the first General Assembly, July 30 to August 4, 1619: twenty-two
elected men in the church at Jamestown, one surviving copy in the National Archives of the United
Kingdom (all facts already in era 3).

**Five minutes?** "The Zenger trial, 1735" in 1700 to 1750.
**Can skip:** "Land for colleges, 1862", "The food laws of 1906", "New kinds of schools, 1991 to
1996", "Immigration law after 2001".

**Reading time:** 25,809 words before the edit = about 130 minutes. Recompute at the end.

**Era words before the edit (words / 200):** 1: 880 (4 min) · 2: 478 (2) · 3: 2,048 (10) · 4: 1,416 (7)
· 5: 2,820 (14) · 6: 2,162 (11) · 7: 3,945 (20) · 8: 4,391 (22) · 9: 4,597 (23) · 10: 3,697 (18).

**Closers (eras over 2,500):** 5, 7, 8, 9, 10. Rotate the middle: 5 = three bullets; 7 = before/after
pair (1865 / 1900); 8 = one number with a comparison; 9 = one open question answered in era 10;
10 = three bullets (then the chapter closing follows).
**"By" lines (eras over 4,000):** era 8 two (By 1920, By 1937); era 9 two (By 1965, By 1974).

**Five dates to keep (closing):** 1619 first elected assembly · 1803 Marbury · 1870 Fifteenth
Amendment · 1920 Nineteenth Amendment · 1974 Nixon resigns.
**Where to go:** Independence Hall, Philadelphia (named in era 4, Andrew Hamilton story).
**Next chapter:** read from control/chapter-registry.md before writing the closing.

**Trouble spots from the dispatch:** era 1 three governments in a row (fix: the era intro follows
one of them, the Haudenosaunee, and tells the reader the other two are short); the Oñate sentence
paragraph (218 words, split into four: the sentences, the children, the hands, the dispute over the
feet); part 3 is 13,389 words with a 4,608-word era (By lines and closers); attribution 8.7/1000
(drop the uncontested "X reports" where the fact is settled); 10 of 14 story boxes over 400 (hooks,
résumé cut, scene kept); 120 paragraphs over 90 (split at the seam).

## Cuts (every one, with the reason)

<!-- era | what was cut | why -->
- era 3 | Pory story: birth (about 1572, Thompson, Norfolk), Cambridge degrees (1592, 1595), the ship *Discovery*, burial at Sutton Saint Edmunds, the two death years (1636 / 1633) | birth-to-death résumé (ARCHITECTURE-GUIDE §4.8); the scene is the record and the appointment. Facts stay in the bank.
- era 3 | "Accounts differ on how long: four years or five" folded into one clause | same fact, fewer words

- era 4 | Zenger story: the case name *Cosby v. Van Dam*, the *Gazette*'s start year 1725, "more than eight months" (now in the hook) | names and a date that add nothing to the scene; the bank keeps them
- era 5 | Washington story: the 1947 proposal and the February 27, 1951 Minnesota ratification of the 22nd Amendment | told once, in era 9's "Five amendments" span, where the Minnesota detail is added (DECISIONS #52: a repeat cut to a callback)

- era 6 | Anti-Masonic span: the re-definition of electoral votes | defined in era 5 (Washington story) and again in era 5's convention span
- era 7 | Rainey story: "born on June 21, 1832" (the record line has it), the Treasury Department job, the banking business, "died in Georgetown on August 2, 1887" (record line has it) | résumé; the scene is the war, the election, the Klan law and the chair
- era 7 | EBSCO attribution kept but moved to the end of its sentence | it is a count

- era 8 | Teapot Dome: Secretary of the Navy Edwin Denby and Senator John B. Kendrick demoted to "the Secretary of the Navy" and (Kendrick) cut: the sentence now says Walsh led the investigation | §5.4, seven proper nouns in 300 words; both names stay in the bank
- era 8 | "the Court's written explanation of its ruling" (opinion) in the Guinn span | defined in era 6 (Marshall story)
- era 8 | 1948 span: the re-definition of electoral votes | defined in era 5

- era 9 | Marshall story: "for the seat Tom C. Clark had left", the definition of senior status (the fact "stopped full-time work on October 1, 1991" stays), "He was born in Baltimore, Maryland, on July 2, 1908" (record line has Born 1908) | résumé
- era 9 | Senate historians' second "The Senate's historians" replaced by "They" | same source, one sentence earlier
- era 10 | Moss story: nothing cut; only paragraphs split and one definition folded | the story earns its length (see Rules broken)

## Rules broken on purpose

<!-- where | rule | why the chapter needed it -->
- Story boxes over 400 words (ten of fourteen; median 562): Washington 561, Madison 458, Zenger 473, Jackson 771, Lincoln 714, Rainey 558, FDR 645, Marshall 547, Johnson 573, Moss 1,047. Each is a scene or a chain of sourced events, not a résumé (the résumés were cut where they existed: Pory, Rainey, Marshall). Cutting further would drop facts (the camps, the Trail of Tears, Box 13, the threats to Moss and Freeman), which DECISIONS #52 forbids. Every box now opens with a hook and has paragraphs under 90 words except where a quotation runs long.
- Four eras over 4,000 words (7, 8, 9, 10: 4,102 / 4,632 / 4,920 / 4,289). The grid fixes the content; furniture added about 1,800 words in all. Eras 8 and 9 carry two "By" lines each and a closer; eras 7 and 10 a closer; so a reader has a stop at least every 2,000 words in each.
- Era 5 (2,938 words) has no "By" line, only the closer: under 4,000.
- "Today" rule (§5.11): era 10 is labeled "2000 to Today", and the body uses "today" only in the era label and strip.
- Narrator pointers inside the body ("The next era tells...", "Era 9 tells how.", "this era opens with him"): one per era at most, within §3's one-per-600-words allowance.
- The "By 2000" closer carries a question. §4.5 lists "one question the era leaves open, answered in the next era" as one of the four closer shapes; the sentence after it gives the 1948 answer and the next era's first span gives 2000's.

## Could not improve

- Attribution stays at 8.5 per thousand (was 8.7). Nearly every attribution left is a count whose figure depends on who counted (the Acoma dead, the Cherokee dead, the Tweed thefts, the two counts of Marshall's cases, the television audience, the Sentencing Project estimate), a disputed vote (the House on removal), a dated modern figure (DECISIONS #37 requires the source), or a witness ("the Senate's historians describe", "the Court's opinion does not say"). §5.6 and #37/#45 keep those. Dropped only the uncontested ones found (the Historical Society on Zenger).
- 31 paragraphs are still over 90 words (was 120), most between 91 and 106: a quotation plus its gloss, or a list of facts with no seam (the Teapot Dome ruling, the 1964 titles). Splitting them would leave two-sentence fragments.
- Era 1 still tells three governments in a row because the three spans are the era's content and cannot move. The intro now tells the reader which one to follow and that the other two are short.
- The chapter grew from 25,809 to 27,595 words (measure's count); the furniture is the whole increase.

## Decisions and defects fixed

## Log

<!-- date-time | unit | what landed | validator | --punct -->
- 2026-10-26 ~11:20 PM | start | checkpoint created; whole chapter read; measure before: words 25809 paras 300 avg 86.0 over90 120 date_first 29.0% def/1k 2.6 attr/1k 8.7 also/1k 2.6 you 6 longest_era 4608 eras>4000 2 stories 14 story_med 568 stories>400 10 | part1 validator 0 errors | punct 0/0
- 2026-10-27 ~12:05 AM | opening, eras 1-5 | part 1 saved after eras 3 and 5 | validator 0 | punct 0/0
- 2026-10-27 ~12:25 AM | eras 6-7 | part 2 saved | validator 0 | punct 0/0
- 2026-10-27 ~12:45 AM | era 8 | part 3 saved | validator 0 | punct 0/0
- 2026-10-27 ~1:05 AM | eras 9-10, closing, card and strips | part 3 saved; all three files validator 0, punct 0/0; --check prose PASS; measure after: words 27595 paras 464 avg 59.5 over90 31 date_first 12.7% def/1k 2.4 attr/1k 8.5 also/1k 2.2 you 12 longest_era 4931 eras>4000 4 stories 14 story_med 562 stories>400 10; build_full_book.py: no warning for this chapter
