# CHECKPOINT T-768 | marketplace (Chapter 18) and big-business (Chapter 19) | structure pass after R10

STATUS: DONE (one finding moved and split, one left because it crosses eras, the fact item settled; both chapters PASS --stage prose)
BRIEF:  control/briefs/STRUCTURE-PASS.md (DECISIONS #54: within one era, a span or story may move, a long span may split, a label may be reworded)
INPUTS: control/checkpoints/T-720-reviewfix.md, control/review/R10.md
FILES:  manuscript/marketplace/part3-1900s-and-today.md, manuscript/big-business/part3-1900s-and-today.md,
        research/research-big-business.md (PATCH only)

## Findings T-720 left undone or done in part because of the old grid rule

| chapter | finding (R10) | state | why |
|---|---|---|---|
| 18 | 1900 to 1950, "Woolworth's stores had lunch counters" (T-720 #7: "bridge instead of a move") | DONE | Split the two lunch-counter paragraphs out of "The chain store at full size" into a new span "Woolworth's lunch counter, 1960" and moved it, inside era 8, to just after "The catalog under Jim Crow". The reader now meets the Woolworth box (how the chain grew) and the Jim Crow definition before the sit-in, and the old span's label now fits what it holds (the A&P). The split is for a subject change, not length: the old span held two subjects and the second had to follow the box. The bold lead-in "The lunch counter." was cut (the label carries it). T-720's bridge "the rule was still in force in 1960" kept: the paragraphs still sit in 1900 to 1950, because the move the reviewer offered first (to 1950 to 2000) crosses eras and stays forbidden. |
| 18 | The 1500s, "Native traders chose carefully" (T-720 #21: "spans do not move") | LEFT | The move the reviewer asked for, the 1670 Hudson's Bay Company paragraph to the 1600s, crosses eras, which DECISIONS #54 still forbids. The era has one span, so no move inside it helps. T-720's bridge ("One fur-trading company, the Hudson's Bay Company, began in 1670") stays. |

Checked and not grid-blocked (no change): ch 18 #13 Bezos box (done in part for DECISIONS #33, not the grid rule); ch 18 #25 "Shopping on television." (the reviewer asked for a bold label, which T-720 added); ch 18 #9 Pynchon deed and #22 Lewis and Clark (fixed by a cut and a bridge, both still sound); ch 19: every finding fixed in full, none blocked (#8 Johns-Manville answered its span label's question instead of renaming the span).

Card pointers: no card line names "The chain store at full size" or the new label. Chapter 18's card names "The ledger", "Barnum's American Museum", "The franchise", "Buying secondhand clothes", and Chapter 19's names "Homestead, 1892", "The Hudson's Bay Company, 1670 to 1825", "Who ran the corporations? 1932", "What was a conglomerate?". All still match their labels exactly.

## Director fact item

| chapter | item | state | source |
|---|---|---|---|
| 19 | GM "largest private employer" in 1979 (AP) against the Bell System's million workers | DONE | Settled: the Bell System employed more. AT&T, 1979 Annual Report, "Employee Matters": "At year's end the Bell System employed 1,029,905 people, an increase of 4.7 per cent over 1978." GM had 618,365 in the US and 853,000 worldwide (AP), fewer by either count. Encyclopedia.com (nearly a million by 1966, 1.09 million at the start of 1984) and Benton Williams, Journal of Policy History 2008 (AT&T "then the world's largest private-sector employer" in 1973) agree. PATCH under the GM "Workers" line of research-big-business.md, with a CORRECTION that the AP's "largest private employer" is not used. Prose: the AP clause cut from the "A billion dollars." paragraph; a new paragraph "**Workers in 1979.**" (GM 618,365 in the US, the Bell telephone system more, 1,029,905 at the end of 1979 by AT&T's own count) placed at the end of the "General Motors" span, after the Corvair (1969), so the span keeps its date order; the era 9 summary's "about a million in the early 1980s" made "more than a million that year" (1979), so both lines compare the same year. |

## Back matter

No back-matter line changes. Big-business back matter has no entry for GM's workforce or "largest private employer" (the marketplace glossary's "largest private employer" belongs to the Walmart box and stays true). The moved lunch-counter paragraphs hold no glossary term and stay in 1900 to 1950, so no era of first use changes. The only other files naming "The chain store at full size" are the director's build outputs (build/history-book.md, book/history-book.md and .pdf), which the next build regenerates.

## Not changed

Chapter closings, era strip minutes, card lines (none named a changed label). Word counts: marketplace 16,180 to 16,177 (the cut lead-in "The lunch counter."), big-business 19,409 to 19,419; no strip or card total moves at five-minute rounding.

## Log

<!-- file | what landed | validator | --punct -->
- marketplace part3 | lunch-counter span split and moved in era 8 | 0 errors | 0/0
- research-big-business.md | PATCH: Bell System 1,029,905 at the end of 1979 (AT&T 1979 annual report), with Encyclopedia.com and Williams 2008; CORRECTION on the AP claim | (bank) | (bank)
- big-business part3 | AP claim cut; "Workers in 1979." paragraph at the end of the "General Motors" span; era 9 summary same-year comparison | 0 errors (x2, before and after the paragraph move) | 0/0 (x2)
- --check: PASS marketplace / prose (validator 0 errors x3, emdash 0, semicolon 0, manuscript 16,177 w, 17 stories verified)
- --check: PASS big-business / prose (validator 0 errors x3, emdash 0, semicolon 0, manuscript 19,419 w, 14 stories verified)
