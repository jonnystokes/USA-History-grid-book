# CHECKPOINT T-774 | education (Chapter 30) | structure pass

STATUS: DONE (--check education --stage prose PASS, 46139w, validator 0 errors, 0 em dashes, 0 semicolons)
BRIEF:  control/briefs/STRUCTURE-PASS.md
FIX CHECKPOINT: control/checkpoints/T-713-reviewfix.md
REVIEW: control/review/R19.md
FILES:  manuscript/education/part2-1800s.md, part3-1900s-and-today.md (part1 and the bank not touched)
BASELINE: --check education --stage prose PASS (46139w), validator 0 errors and --punct 0/0 on all three parts.
Director fact items: none.

## Blocked findings (T-713 numbering = order in R19.md)

| # | finding | state | what and why |
|---|---------|-------|--------------|
| 8 | By-lines run backward (eras 7, 8, 10) | done | Era 8: the fixer's By 1945 line stays. Putting the 1948 line back would mean moving the four spans dated 1928 to 1944 in front of "Separate schools", which splits the camps span from the Mendez box it leads into. Moved instead: the Dewey span and box (1896 to 1904), which sat after By 1920 and Carlisle, now come after the Nebraska span and before "Who could hit a child". Era 7: "A teacher jailed in Norfolk, 1854" moved from after By 1870 and the Forten box to second in the era, after "When school became the law". Era 10: "The school buildings close, 2020" and the Rosproy box moved from after By 2024 to just before "Teaching at home: the 2020 jump", whose 2020 paragraph already pointed back to the closings. The gloss "Education Week, a newspaper about schools" moved from the shootings span to the closings span, its new first use in the era. |
| 8, left | spans that run across their era | left | Carlisle (era 7), "Separate schools" and the disabled-children span (era 8) cover the whole era, so any place after a By-line steps back. Era 9's Ruby Bridges box and the 1962 university span sit after By 1964: moving them in front would split Little Rock and Virginia again, and moving the line after them would make the stretches about 2,800 and 800 words instead of about 1,800 each. Era 8's Carlisle span (1914 to 1918) after By 1920 left for the same balance reason: moving the line after it would make the stretches about 2,800 and 500 words instead of about 2,100 and 1,200. |
| 19 | label says prayer, text says religious teaching | done (part) | Label now "Religious teaching in a Nebraska school, 1902", the text's own words. What Freeman objected to is still not in the bank (it says only "religious instruction"), so the text still does not say. |
| 20 | Sputnik law splits Little Rock and Virginia | done | "Science and languages: the 1958 law" moved from between Little Rock and Virginia to just before "Federal money for poor children's schools, 1965". By 1972, which already named science teaching and student loans, now sums up its own stretch. The fixer's bridge "Officials in Virginia made the same choice as Faubus." kept: with the two closing stories side by side it is a plain eight-word link to the span just before. |

## Other checks
- Cuts: none. Nothing shrank (46139 words before and after).
- Card pointers: no card-named span was touched. All five quoted names ("Punished for speaking Spanish", "The academies", "Catholic schools become a system", "The school year and the school day", "The last one-room schools") match their labels exactly (script check).
- Closing answers, five dates, era strips: untouched.
- Back matter: no line made wrong. control/backmatter/education.md gives each person and term an era only, and every move stayed inside its era. Its 1850-1900 glossary group (optics, misanthrope, constable, lines 130 to 132) no longer follows the chapter's order, since constable (Norfolk) now comes first. The book glossary is alphabetical, so nothing reads wrong.
- The old label "A school prayer case in Nebraska, 1902" is quoted nowhere else (grep of manuscript and control/backmatter).

## Log
<!-- file | what landed | validator | --punct -->
- part2 | F8 era 7: Norfolk span moved to second place in the era (after "When school became the law", before the Morrill Acts); same 533 lines, same bytes | 0 errors | 0/0
- part3 | F8 era 8: Dewey span and box moved to after the Nebraska span, before "Who could hit a child". F20: Sputnik span moved to just before "Federal money for poor children's schools, 1965". F8 era 10: closures span and Rosproy box moved to after "Choosing a school", before "Teaching at home: the 2020 jump"; the "Education Week, a newspaper about schools" gloss moved with them to its new first use (from the shootings span). F19: label now "Religious teaching in a Nebraska school, 1902". 1119 CRLF lines before and after | 0 errors | 0/0
- final | python tools/project_state.py --check education --stage prose: PASS (46139w, validator 0 errors on all three parts, 0 em dashes, 0 semicolons)
