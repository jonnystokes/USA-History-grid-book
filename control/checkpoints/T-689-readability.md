# CHECKPOINT T-689 | science | readability (second edition) | all 10 eras

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check science --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md)
MODEL:  opus
FILES:  manuscript/science/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md · research/research-science.md (PATCH only) · control/backmatter/science.md

NOW:    done; reported
NEXT:   director: second read

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 0 | chapter opening | landed | landed: spine, moose anchor, turn, 3 questions, five minutes, can skip; reading time to be reset at the end |
| 1 | era 01 before-1500 | landed | landed: strip; Sun Dagger label made a question; petroglyph word dropped; definitions folded; Kimmerer box hook + split |
| 2 | era 02 1500s | landed | landed: strip; Hariot paragraphs split, date-first removed |
| 3 | era 03 1600s | landed | landed: strip; through-line first; bold lead-ins; definitions folded; Holm hook |
| 4 | era 04 1700-1750 | landed | landed: strip; through-line first; Franklin + Bartram hooks; date-first runs broken |
| 5 | era 05 1750-1800 | landed | landed: strip; lightning label made a question; Query XIV long quote cut to two quotes under 25 words; Rittenhouse, Banneker hooks; Banneker box split into lead-in paragraphs |
| 6 | era 06 1800-1850 | landed | landed: strip; through-line first; Henry span relabeled as a question (credit thread); Morton span split into lead-in paragraphs with Disputed / Known lines; Smithson Not known line; hooks on Smithson, Henry, Mitchell; Henry box reordered to open on the weather maps. No closer (about 2,000 words) |
| 7 | era 07 1850-1900 | landed | landed: strip; Agassiz through-line first; Darwin span split; Army museum span relabeled as a question and split (Dakota man, orders, Mulberry Creek); Morrill span split, 'the United States paid' made 'US officials paid'; hooks on Gibbs, Michelson, Fleming; closer (three bullets) |
| 8 | era 08 1900-1950 | landed | strip; through-line first; two By lines (By 1930 before Hrdlicka, By 1939 before fission); Leavitt label made a question (question 1); every span split under 90 words with bold lead-ins; plutonium patients each under a name lead-in, no fact dropped; Trinity Not known line; hooks on all six boxes; closer (before/after pair). Era now 5,012 words |
| 9 | era 09 1950-2000 | landed | strip; Lacks through-line first; one By line (By 1970, before the Moon span; era is 3,700 words, so a stopping place at the seam); plates and Bell Labs spans relabeled as questions (not adjacent); Viking Disputed line; Clinton quote cut under 25 words; Watson quote glosses in parentheses; hooks on Tharp, Hoffman, Morabito, Feynman; closer (one number with a comparison) |
| 10 | era 10 2000-today | landed | strip; through-line first (team size); spans split; Morton apology and Eden Cemetery repeat cut to one callback sentence (told in era 6); Watson death trimmed to the new fact plus one line; hooks on Dunford, Doudna, Weiss. No closer (the chapter closing ends the era) |
| 11 | chapter closing | landed | three questions word for word; five dates all in the chapter; Not known = Trinity fallout count; Where to go = International African American Museum, Charleston; Next = Chapter 10, Energy. About 300 words: over the 280 target because the questions repeat word for word |
| 12 | back-matter hand-off | landed | control/backmatter/science.md |

## SUBJECT NOTES (decided before writing)

**Measurements before:** 17,866 words, 278 paragraphs, avg 64.3, 44 over 90 words, 24.5% date-first,
def 2.7/1k, attr 4.6/1k, also 2.2/1k, 4 "you" (all inside quotations), longest era 4,861 (1900-1950),
1 era over 4,000, 25 stories, median 226, 1 over 400 (Banneker).

Era words (my count): 1 = 809, 2 = 167, 3 = 662, 4 = 600, 5 = 1,493, 6 = 2,019, 7 = 2,557,
8 = 4,833, 9 = 3,526, 10 = 2,241.

**Spine:** Science in America grew from a few people watching the sky into labs with thousands of
workers, and along the way many scientists used people who never agreed to be studied.

**Anchor:** Jefferson's moose, 1786-1787 (rotted body, another animal's antlers "may be fixed on at
pleasure"); the same book called Black people inferior as "a suspicion only". Already in era 5.

**Three questions:**
1. How did American scientists learn how far away the stars are?
2. Why did scientists collect human skulls and brains, and where are those remains now?
3. Who did the work but was left out of the credit?

**Five minutes?** "The shape of DNA, and who got the credit" in 1950 to 2000.

**Can skip:** "Charting the winds at sea", "The physics inside the transistor, 1947", "Heavy
elements, made by many countries", "Computers that predict the shapes of proteins".

**Furniture plan:** era strips on all ten. "By" lines in era 8 (two: before the Hrdlicka span and
before the fission span). Era closers on eras 7, 8, 9 (over 2,500 words), and on 6 if it grows past
2,500. Era 10 ends with the chapter closing. Closers rotate shape: era 7 three bullets, era 8
before/after pair, era 9 one number with comparison.

**Next chapter:** Chapter 10, Energy (what powered American life).

## Sources in hand

Bank: research/research-science.md. No new facts planned.

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

- Reading times: chapter 95 minutes (build's reading_minutes, 18,895 words). Era strips use body words only (opening and closing excluded): 4, 1, 3, 3, 7, 10, 14, 25, 19, 11.
- Era 9 is 3,700 words (under the 4,000 line) but got one By line (By 1970) so there is a stopping place near the 2,000-word mark.
- Banneker box is 461 words, over 400 on purpose: the story is the exchange of letters (his letter, Jefferson's reply, the 1809 letter calling his work a "suspicion") and each step needs its quotation.
- Derived comparisons added (arithmetic on facts already in the chapter, no new facts): Woodhenge circle "longer than a football field" (475 ft), Ratliff dose "more than 30 times the limit" (47 vs 1.4), genome cost "more than 9,000 times less" ($14 million vs under $1,500), Hrdlicka-era share "three of every five" (62 percent), remains not yet returnable "more than two of every five" (42 percent), Keeling Curve "more than a third above" the first reading (430 vs 313), closer "about one new experiment every three days for thirty years" (4,000 over 1944-1974).
- Question labels (7, never adjacent): Sun Dagger, lightning test, induction, Army skulls, Leavitt, continents, Bell Labs hiss.
- Over-90 paragraphs left: 5, all furniture (the opening's turn, three era closers, the chapter closing), which the measurement tool counts as single paragraphs.
- No research PATCH needed.

## Cuts (every shortening, with the reason)

- era 1 Chaco: dropped the word "petroglyph" and its definition sentence (a hard word the passage does not need; the carved spirals stay).
- era 5 Banneker: dropped "Tables like these are called ephemerides" (hard word not needed; the plain description of the tables stays).
- era 5 Megalonyx: dropped the definition of "fossil" (a word an 11-year-old knows).
- era 5 Query XIV: the 40-word quotation became two quotations under 25 words ("are inferior to the whites in the endowments both of body and mind" plus "a suspicion only"); nothing of the claim is lost.
- era 6/7: no facts cut. Agassiz zoologist definition replaced by "who studied animals".
- era 8: dropped the gloss of "inject" (children know a shot) and of "physiology" (it is part of the prize's name). Manhattan Project re-definition in the Einstein box cut (defined in the era summary).
- era 9: McClintock span cut the repeated "first woman to win that prize without sharing it" (told in her era 8 box); the 39-years fact stays. Two-laws span: the recap of the Army museum and Hrdlicka cut to one callback sentence (both told in full in eras 7 and 8).
- era 3: "A mariner is a sailor" replaced by "a sailor named William Pierce".

## Log

- 2026-10-27 | opening + eras 1-5 | part1 rewritten | validator 0 errors | punct 0/0
- 2026-10-27 | era 10 + closing + hand-off | spliced; --check science --stage prose PASS | validator 0 errors | punct 0/0
- 2026-10-27 | era 9 | spliced into part3 | validator 0 errors | punct 0/0
- 2026-10-27 | era 8 | spliced into part3 | validator 0 errors | punct 0/0
- 2026-10-27 | eras 6-7 | part2 rewritten | validator 0 errors | punct 0/0
