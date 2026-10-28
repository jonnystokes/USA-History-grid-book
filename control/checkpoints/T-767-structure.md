# CHECKPOINT T-767 | economy (Chapter 16), money (Chapter 17) | structure pass after R09 / T-724

STATUS: DONE (3 findings done, 1 considered and left; both chapters PASS --stage prose)
BRIEF:  control/briefs/STRUCTURE-PASS.md (DECISIONS #54)
FIX CHECKPOINT: control/checkpoints/T-724-reviewfix.md · REVIEW: control/review/R09.md
FILES:  manuscript/economy/part3-1900s-and-today.md; manuscript/money/part1-before-1800.md,
        part3-1900s-and-today.md (part2 read, not changed). No bank changed, no back matter changed.
VERIFY: python tools/project_state.py --check economy --stage prose
        python tools/project_state.py --check money --stage prose
Director fact items: none.

## Findings blocked by the old grid rule

| finding | era | state | what and why |
|---|---|---|---|
| Ch16 #24 (removals to Mexico under a heading about Black workers) | 1900 to 1950 | DONE | label "Last hired, first fired" reworded to "Pushed out when jobs ran short", which names what both halves share (Black workers fired first; families forced to Mexico, blamed for taking scarce jobs). "last hired, first fired" stays in the second sentence, so the glossary term still fits. T-724's reason sentence and the lead-in "Forced to Mexico." kept: they mark and explain the second half. Not split: the span is 226 words. No card line names it |
| Ch17 #4 (gold paragraphs inside the runs, holiday and insurance span) | 1900 to 1950 | DONE | split: "1930 to 1933: the runs, the holiday and deposit insurance" (585 words, the chapter's longest span) now ends at deposit insurance (469 words). The two gold paragraphs are a new span, "What happened to Americans' gold?" (114 words), placed after the Lobsiger story, so the five-minute route (the span, then "The Lydia Lobsiger story follows it") runs runs, holiday, insurance, first insurance check, with nothing between. T-724's workaround: lead-in "The gold." cut (the label replaces it); its bridge "In the same months, Roosevelt and members of Congress took gold out of Americans' hands." now answers the question label: "... in 1933 and 1934." (both dates are in the span). The named span keeps its label, so the card line is unchanged and still exact |
| Ch17 #22 (heading "Paper money lent against land and people") | 1700 to 1750 | DONE | label reworded to "Loans against land and enslaved people": the text gives the colony's public land bank lending paper money on land, then private bonds and mortgages on land and on enslaved people. The old label said paper money was lent against people, and the bank says no source ties the land bank to loans on enslaved people (PATCH T-724). Era 4 lead: "which had no banks" now "which had no private banks", because since T-724 the span opens on the public land bank of 1712 (bank: "There were no banks in colonial South Carolina", CCPL, plus the T-724 PATCH). No card line names it |
| Ch17 #18 (the motto: "give the motto its own heading") | 1850 to 1900 | LEFT | T-724 gave it the bold lead-in "In God We Trust." and cut the later dates. DECISIONS #54 allows splitting a long span, and "Greenbacks" is 321 words, about the chapter's median; a split would leave a two-paragraph span. The lead-in already marks the change of topic |

Cuts: "**The gold.** In the same months," (a bridge for the old rule). No fact cut.
Era strips and card times unchanged: money era 8 went from 2,241 to 2,239 words (still about 11
minutes), era 4 from 760 to 761 (still 4); the economy edit changed only a label.
Back matter: no line needs changing. No back-matter line names a span label; the glossary's
"last hired, first fired" (control/backmatter/economy.md line 140) still matches the text.

## Log

- Read the brief, ARCHITECTURE-GUIDE, both style guides, the hard-subjects policy, T-724's checkpoint,
  R09.md and the passages (economy era 8 whole; money eras 1 to 8 whole). Word counts before and
  after edits, and a card-name check, from a scratch counter (T-767 scratch folder).
- Checks after every saved file: validate_grid.js --part 0 errors, --punct emdash=0 semicolon=0
  (economy part3, money part1, money part3). Card names: all 5 economy and 4 money names match a span.
- Final (2026-10-28 10:58 AM):
    PASS  economy / prose  (manuscript=16715w, validator 0 errors, emdash=0 semicolon=0)
    PASS  money / prose    (manuscript=15022w, validator 0 errors, emdash=0 semicolon=0)
