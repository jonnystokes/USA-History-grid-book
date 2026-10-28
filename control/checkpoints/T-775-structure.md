# CHECKPOINT T-775 | news-communication (Chapter 31) | structure pass (DECISIONS #54)

STATUS: DONE (2 of 2 blocked findings done: #21 moved, #23 split)
BRIEF:  control/briefs/STRUCTURE-PASS.md
FIX CHECKPOINT: control/checkpoints/T-732-reviewfix.md
REVIEW: control/review/R20.md
FILES:  manuscript/news-communication/part2-1800s.md, part3-1900s-and-today.md (bank unchanged: no fact added)
DIRECTOR FACT ITEMS: none
BASELINE: --check PASS, manuscript=26230w, validator 0 errors, punct 0/0 on parts 2 and 3

## Findings the old grid rule blocked (from T-732)

| T-732 # | era | finding (first words) | T-732 workaround | state | note |
|---|---|---|---|---|---|
| 21 | 6, 1800 to 1850 | "The penny press, 1833" | SKIPPED the move, cue "as Garrison did" in the Lovejoy box | DONE | span moved to after the Lovejoy box, before the telegraph span: Garrison span and Lovejoy box now run together, and the penny press (The Sun) sits next to the telegraph span that names The Sun's owner, the same order as the era opener (one cent, then the wire). Not moved before Freedom's Journal: that would put 1833 before 1827 and break the mail span's hand-off ("no Black American ... could carry the mail") into the first Black-owned paper. Cue CUT as redundant: "as Garrison did, but" (box now opens "Elijah Lovejoy wrote against slavery in a state where slavery was legal."). Label kept |
| 23 | 9, 1950 to 2000 | "Members of Congress set up the" | opener line only, "no splits" | DONE | span "Public broadcasting, the fairness rule, cable news and talk radio, 1967 to 1996" split in two, by exact lines: "The fairness rule and talk radio, 1949 to 1988" (the rule from 1949, upheld 1969, the 1987 veto and end, Limbaugh 1988) then "Public broadcasting and cable news, 1967 to 1996" (CPB/PBS/NPR, CNN, Fox News), so each span teaches one thing; this order keeps start dates in order (1949, 1967, then the internet's 1969) and puts cable news just before the internet span, as the era opener's last sentence has them. CUT as redundant: T-732's opener "Lawmakers, federal officials and owners changed who paid for the news ..., between 1967 and 1996" (written to tie five topics; the two labels now name the threads) and the "**The fairness doctrine.**" lead-in (it sat right under a label naming the rule; the sentence still names the doctrine). CNN and Fox paragraphs joined into one cable-news paragraph (33 + 25 words, now 58). No sentence added, no fact cut |

No other T-732 finding was skipped or done in part because of the grid rule (checked all 25 rows).
Card lines ("Five minutes?" WLBT span, "Can skip:" four spans) name none of the spans touched here.

## Log

<!-- file | what landed | validator | --punct -->
- part2 | #21: penny press span moved by exact lines (script, CRLF kept), Lovejoy cue cut | 0 errors | 0/0
- part3 | #23: span split by exact lines (script, CRLF kept), opener and duplicate lead-in cut, CNN and Fox paragraphs joined | 0 errors | 0/0
- strips and card unchanged and still right: era 6 3,317 words (16.6, "about 17"), era 9 3,551 (17.8, "about 18"), chapter 25,049 by measure_readability (125.2, "about 125"). Card lines name none of the touched spans; all five card-named labels still exist exactly once
- back matter: no line affected (it tags terms and people by era, not by span; closing answers untouched)
- measure_readability after: 25,049 words, 491 paras, avg 51.0, over-90 5, date-first 0.0
--check: PASS news-communication / prose (validator 0 errors on all three parts, emdash 0, semicolon 0, manuscript 26,198 w by project_state)
