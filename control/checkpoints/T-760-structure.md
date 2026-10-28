# CHECKPOINT T-760 | front matter + exploration (Chapter 1) | structure pass (DECISIONS #54)

STATUS: DONE (2026-10-28 11:00 AM)
BRIEF:  control/briefs/STRUCTURE-PASS.md
FIX CHECKPOINT: control/checkpoints/T-729-reviewfix.md
REVIEW: control/review/R01.md
FILES:  manuscript/_frontmatter/*.md, manuscript/_introduction/*.md, manuscript/exploration/part*.md (bank PATCH only if needed)
DIRECTOR FACT ITEMS: none

## Findings the old grid rule blocked (from T-729)

T-729 marks no finding "skipped because a span or story could not move, split or be relabeled". Its skips
(glossary promise, card questions above the anchor, one closer shape, White Sands and Walsh counts,
Beckwourth's mother, contents times) rest on director notes, ARCHITECTURE 4.1/4.5 or DECISIONS #32, not on
section 2, so they stay as T-729 left them. One fix was done in part for lack of a seam:

| # | era | finding (first words) | T-729 workaround | state | note |
|---|---|---|---|---|---|
| 35 | 6, 1800 to 1850 | "By 1840: The last rendezvous had" | By 1840 cut ("only story boxes follow it, no seam outside a box") | DONE (split and moved, By line back) | the source-of-the-Mississippi paragraph (Ozaawindib and Schoolcraft, 1832; not about trappers) left "Trappers and the fur trade, 1822 to 1840" and became its own span, "The source of the Mississippi, 1832", after Jim Bridger's box and before Charles Wilkes's, in date order and in the order the era opening lists the Native guides (Crow map, Mojave crossing, Ojibwe guide). The Trappers span now runs straight from the Arikara fight and the rendezvous into Glass, Smith and Bridger. The new span ends with a new By line at the seam, outside any box and any skippable span: "By 1840: The trappers had held their last rendezvous. Charles Wilkes's Navy crews had sailed in 1838 and were exploring the Pacific and the coast of Antarctica." Every fact restates the chapter (rendezvous 1825 to 1840, era opening's Navy squadron, Wilkes's box). It leaves out South Pass, the Great Salt Lake and the source of the Mississippi, which the closer's "In 1850" line lists (T-729's second reason for the cut). Cut: the bold lead-in "The source of the Mississippi." (the new heading says it). DECISIONS #54 names long spans; this 358-word span was split at its subject change because the move needed it, and nothing left the era |
| 35 (By 1810 half) | 6 | "the 1810 line sits under the Pikes Peak heading" | kept, build prints it at the seam | LEFT | checked: the HTML and Markdown builds print a span-opening By line above the span heading (build_full_book.py zoom_html, build_full_book_md.py), so it sits between Colter's box and the skippable Pikes Peak span |

Front matter: no spans or stories, so nothing there was blocked by section 2. No front-matter file changed (--punct 0/0 on all four anyway).

## Measures (build word rule: block lines not starting with # or >)

- era 6: 5,361 words before, 5,383 after, strip still "about 27 minutes"; chapter 21,901 words, card still 110
- era 6 stops: By 1810 after 2,418 words, By 1840 after 3,951, closer at about 5,269 (was By 1810 after 2,418, then about 2,830 words with no stop before the closer)
- card: "Five minutes?" and the four "Can skip:" names all match span labels; no duplicate labels (20 spans)

## Back matter

No line made wrong. control/backmatter/exploration.md glossary lines 72-73 (Indian agent, Lake Itasca) keep era "1800 to 1850"; the build sorts the glossary, so their place in the hand-off list does not matter.

## Log

<!-- file | what landed | validator | --punct -->
- baseline: validate_grid part2 0 errors, --punct 0/0, --check exploration --stage prose PASS; era 6 = 5,361 words by the build's rule (strip 27, safe below 5,500)
- exploration/part2-1800s.md | finding 35: Schoolcraft span split out and moved after Bridger, By 1840 line at its end | 0 errors | 0/0 (CRLF kept)
- part1, part3 unchanged: 0 errors, 0/0
- `python tools/project_state.py --check exploration --stage prose`: PASS (10/10 eras written, 35 stories verified, 0 em dashes, 0 semicolons, 23,571 words, validator 0 errors)
