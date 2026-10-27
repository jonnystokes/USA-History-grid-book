# CHECKPOINT T-672 | sports-play | prose (readability edit, second edition) | all 10 eras + opening + closing

STATUS: IN-FLIGHT (agent finished; director sets DONE)
VERIFY: python tools/project_state.py --check sports-play --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md)
MODEL:  opus
FILES:  manuscript/sports-play/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md · research/research-sports-play.md (PATCH only) · control/backmatter/sports-play.md

NOW:    done; waiting for the director
NEXT:   director: commit; second read by another agent

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 0 | dates to month-day-year, all files (script) | landed | 127 dates with year, 5 without; two ranges by hand |
| 1 | chapter opening + era strips | landed | opening in era 01; strips added era by era; minutes re-checked at the end |
| 2 | era 01 before-1500 | landed | strip, through-line first para, 2 bold lead-ins, Pauketat para split, 1 label to a question; missionary/Jesuit/wampum glossed here once |
| 3 | era 02 1500s | landed | strip; missionary gloss removed (era 01 owns it); engraver gloss folded; de Bry para split with a lead-in |
| 4 | era 03 1600s | landed | 6 paras split, 5 date-first re-led, Bullocke box reshaped (hook, Not known line), shilling/ninepins glosses folded; no closer (under 2,500) |
| 5 | era 04 1700-1750 | landed | strip, through-line first para, 4 date-first re-led, quarter-race and Pinkerton paras split, Thoroughbred and indentured glosses folded; no closer |
| 6 | era 05 1750-1800 | landed | strip, intro split, 8 date-first re-led, Stonie Hadjo para split, Curtis box hook + fidelity gloss folded, hierarchy/diversions/wicket glosses folded; no closer (1,982) |
| 7 | era 06 1800-1850 | landed | strip, 12 date-first re-led, Doubleday and McCoy paras split, Molineaux box reordered to open on the Cribb fights (hook), Larcom box hook + résumé trimmed, rules span relabeled "Who wrote the rules of baseball?" (the card's five-minute pick), closer "By 1850" (three bullets) |
| 8 | era 07 1850-1900 | landed | strip, through-line first para, 16 date-first re-led, 6 paras split, Walker box hook (threat letter) + birth day trimmed, Murphy box hook (628 of 1,412), emancipate gloss folded, closer "By 1900" (before/after pair) |
| 9 | era 08 1900-1950 | landed | strip, through-line first para, "By 1920" and "By 1940" lines (era 4,570 words), ~25 date-first re-led, 10 paras split, 7 story boxes given hooks (Johnson, Ruth, Didrikson, Owens, Stotz, Gibson, Robinson), birth days trimmed to years in Johnson/Ruth/Didrikson/Owens/Gibson/Robinson, Gibson box reordered to open on the 1930 call from the stands, football-deaths label to a question, closer "By 1950" (one number). Robinson box stays over 400 words: the abuse and threats of 1947 are the scene and cannot be cut without softening |
| 10 | era 09 1950-2000 | landed | strip, through-line first para (school-travel numbers left to the span), ~20 date-first re-led, 9 paras split, 5 boxes given hooks (Johnston, Ali, Ernst, King; Pressler quote cut to two short quotes under 25 words), Title IX count given one comparison (about nine times as many girls), afternoon span relabeled as a question, closer "By 2000" (one open question answered in era 10) |
| 11 | era 10 2000-today | landed | strip, through-line first para, "By 2022" and "By 2018" lines, ~20 date-first re-led, 14 paras split, Giersdorf and Denhollander boxes given hooks, Nassar span split into 9 short paragraphs with bold lead-ins (nothing softened, rape and the legal terms still explained), obesity rise given one comparison; no era closer (the chapter closing is the last block, pilot precedent) |
| 12 | chapter closing | landed | three questions answered word for word, what changed, five dates, Not known, Where to go (Hall of Fame, bank line 983), Next: Chapter 37 Holidays; 325 words with markup, a little over the 280 target |
| 13 | self-review, checks, back-matter hand-off | landed | second and third passes split the last long paragraphs, varied era first sentences and closer first lines, fixed strips; card set to 125 minutes (build loader: 24,881 words); control/backmatter/sports-play.md written |

## SUBJECT NOTES

**Before (measure_readability.py):** 23,535 words, 348 paragraphs, avg 67.6, 66 over 90 words,
24.1% date-first, def 1.0/1k, attr 7.9/1k, also 1.7/1k, 6 "you", longest era 4,385, 2 eras over
4,000, 19 stories, median 271, 3 over 400. Era sizes (era_sizes): before-1500 1,116; 1500s 459;
1600s 2,209; 1700-1750 1,082; 1750-1800 1,976; 1800-1850 2,910; 1850-1900 2,590; 1900-1950 4,385;
1950-2000 3,262; 2000-today 4,309. Chapter 36 of 37; next is Chapter 37, Holidays.

**Spine (bold, first sentence of the card):** From chunkey at Cahokia to Fortnite, American games
moved out of open fields and into leagues, arenas and screens run by adults and companies, and at
almost every step someone in charge decided who was allowed to play.

**Three questions (word for word in the closing):**
1. Who invented baseball?
2. Who was kept out of American games, and how did they get in?
3. How has children's free time changed?

**Anchor:** the York County court order of September 10, 1674: James Bullocke, a tailor, fined for
racing because racing was "a sport only for Gentlemen", and the gentleman who fixed the race put in
the stocks (already in the chapter, era 03 story box).

**Five minutes?** "Written rules for ball games" in 1800 to 1850 (answers question 1; label may be
reworded during the era pass; the card must match the final label).

**Can skip:** "Spanish games on horseback, 1598", "Cricket", "The Miracle on Ice", "Television and
the Super Bowl" (final labels to be confirmed against the edited file).

**Where to go:** the National Baseball Hall of Fame in Cooperstown, New York (bank line 983: opened at
Cooperstown in 1939; Gibson's plaque, "almost 800" home runs, is in the chapter).

**Furniture plan:** era strips on all ten. "By" lines in 1900-1950 and 2000-today (both just over
4,000; one each, at the seam nearest 2,000 words). Era closers in 1800-1850, 1850-1900, 1900-1950,
1950-2000 (over 2,500), and 1600s or 1750-1800 if they pass 2,500 after the edit. Era 10 gets no
closer: the chapter closing is its last block (pilot precedent, exploration). Rotate closer shapes.

**Known trouble spots (dispatch):** attribution 7.9 per 1,000 words: cut attributions that are not
contested, witness, or who-counted (#37, #45 stay). Dates were day-month-year throughout: §5.13
wants month-day-year.

**Hard subjects to keep intact:** Dale's punishment at Jamestown (needle through tongue, starved),
the 1680 Virginia law (lashes, killing), Choctaw removal deaths and Dobbs's grave robbing, gouging,
the 1910 Johnson riots, McCoy's death, Von Gammon, the Fairground Park attack, the Monson acid, the
Nassar span (rape word, explained; clinical/legal terms explained), Geddert's suicide, CTE.

## Decisions and defects fixed

- Rules broken on purpose: the anchor opens with its date (September 10, 1674) because the date is
  the point; three story boxes stay over 400 words (Moses Fleetwood Walker 408: the threat letter, the
  Syracuse attack and trial; Jack Johnson 484: the 1910 attacks and the Mann Act prosecution; Jackie
  Robinson 469: the abuse and threats of 1947). None can be cut without softening.
- Attribution stays near 8 per 1,000 words. What remains is witnesses (Wood, Fithian, Douglass,
  Stonie Hadjo, Bingham), disputed counts (football deaths 1905, Choctaw removal deaths, Cato's
  freedom), and who counted a modern figure (#37). The measure also counts "states" as in US states.
- Era 10 claim checks: era 09's closer first said children spent more time "on screens"; the 1981-1997
  diaries show less television, so the closer now asks the screens question from the 1982 count of
  game machines instead. Era 09 intro no longer says afternoons moved "indoors" (not in the record).
- Span labels changed (text only, no marker attributes): "What did children play with?" (era 01),
  "Who wrote the rules of baseball?" (era 06), "How many died playing football in 1905?" (era 08),
  "How did a child's afternoon change?" (era 09). Story slugs, era ids, status, movie and record
  keys untouched.

## Cuts (every cut, with its reason)

- Era 03, Plymouth fines: the names Richard Berry, William Griffin, Richard Michell (and wives), and
  Joseph Thorne, Joseph Peirse, James Benitt, Isacke Woodworth demoted to counts ("five more card
  players, two of them married couples"; "six men and one servant"), and the Woodworth no-fine
  sentence cut. Reason: §5.4, eleven new names in 150 words; the kept names (Shilley, Holbrooke,
  Patricke, Gannet) carry the point that the judges fined people by name.
- Era 01: Jefferson Patterson attribution on the year-600 date dropped (stated as fact; the museum
  is still credited for the contested decline date). Era 02: second gloss of "missionary" (era 01
  owns it). Era 03: second gloss of wampum (era 01 owns it).
- Era 05: repeated "according to Choctaw tradition, towns sometimes settled an argument" (era 01 says it);
  second gloss of base (the era summary glosses it); the sentence restating that the 1787 rhyme was
  first printed in England (era 04 says it) folded into "with the English rhyme".

- Era 06: the 1790 beaver-pond game retold in full a second time (era 05 owns it) cut to a
  one-clause callback before the Dobbs grave robbing. Trotting and jockey re-glosses cut (era summary
  and era 05 own them). Larcom box: résumé lines cut (exact birth date, teaching in Illinois
  1846-1853 and at Wheaton Seminary 1854-1862, first poems 1854, death in Boston April 17, 1893),
  replaced by "grew up to teach school and to write poems". Reason: §4.8 résumé trim.
- Era 07: Walker box birth day (October 7) trimmed to the year (résumé).

- Era 08: exact birth days in six boxes trimmed to the year (résumé); jockey re-gloss cut (era 05
  owns it); "Negro" re-glossed once in part 3 (Jack Johnson box), allowed by guideline 7.

- Era 10: the equal-pay complaint names three of the five players (Alex Morgan and Becky Sauerbrunn
  demoted into "five players ... among them"), §5.4. Hofferth re-introduced as a callback, not a
  second full introduction. Closing trimmed: the 1744 and 1791 baseball facts stay in their eras.

## Log
2026-10-27 | units 0-4 | dates, opening, eras 01-03 | validator 0 errors | punct 0/0
2026-10-27 | units 5-6 | eras 04-05, part1 done | validator 0 errors | punct 0/0
2026-10-27 | units 7-8 | eras 06-07, part2 done | validator 0 errors | punct 0/0
2026-10-27 | unit 9 | era 08 | validator 0 errors | punct 0/0
2026-10-27 | unit 10 | era 09 | validator 0 errors | punct 0/0
2026-10-27 | units 11-13 | era 10, closing, passes 2-3, hand-off | validator 0 errors x3 | punct 0/0 x3 | --check prose PASS
