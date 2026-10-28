# CHECKPOINT T-769 | government-politics (Chapter 20) | structure pass (DECISIONS #54)

STATUS: DONE (check PASS, see the end)
BRIEF:  control/briefs/STRUCTURE-PASS.md
MODEL:  opus
FIX CHECKPOINT: control/checkpoints/T-716-reviewfix.md
REVIEW: control/review/R11.md
FILES:  manuscript/government-politics/part1-before-1800.md, part2-1800s.md, part3-1900s-and-today.md,
        research/research-government-politics.md (PATCH and the two corrected lines only)
VERIFY: python tools/project_state.py --check government-politics --stage prose

NOW:    finished
NEXT:   nothing for this task; one back-matter hand-off line to look at (see "Back matter")

## Which T-716 findings the old rule shaped

T-716 marked every finding FIXED and none "could not move" or "no splits". Its one "in part"
(15) was for a hard-subjects reason. Read against REVIEW-FIX ("never change a marker line"),
two fixes stopped at a run-in label where a span label was the real need (16, 10), and three
more asked something that a move, split or relabel could now touch (20, 15, 12). Each judged:

| T-716 # | era | finding (first words) | T-716 workaround | state | note |
|---|---|---|---|---|---|
| 16 | 8, 1900 to 1950 | "In the school year 1919-20, local" | California paragraph under the run-in label "Ending segregated schools." inside "School law: who decides, and who pays" | DONE (split and moved) | new span "Ending California's law on segregated schools, 1947", placed after "Poll taxes and the white primary" and before the 1948 span, so 1944, 1947, 1948 run in order into the closer's 1954 pointer. Run-in label cut (the span label says it). The school span now ends on "Who pays." and matches its label |
| 10 | 10, 2000 to Today | "A map drawn by race is" | run-in label renamed "Asking permission.", but the span label "Money and maps" still did not cover Shelby County | DONE (split) | new span "Asking permission to change voting rules, 2013" right after "Money and maps" (the election-law rulings stay together). Run-in label cut (the span label says it) |
| 20 | 3, The 1600s | "Royal judges in Mexico City tried" | verdict moved first, label kept | LEFT | T-716 fixed it in full. The label is answered in the first sentences, and the Acoma account is what the Acoma guilty count rests on. A split would set a 1598 span after a 1614 one |
| 15 | 8, 1900 to 1950 | "George Washington had served two terms," | bridges; camps kept in the box (hard-subjects) | LEFT | the half T-716 skipped was skipped for the hard-subjects policy, not the grid rule: the bank says EO 9066 must not be softened in his story. The bridges still help. "The courts and the camps" span already follows the box |
| 12 | 3, The 1600s | "In the summer of 1619 Governor" | span kept as the body's telling | LEFT | not a grid-rule fix. The span is the body's telling, the opening anchor restates it as the guide asks |

Also read and left: 14 (Lincoln box, Thirteenth Amendment). T-716 used the review's own bridge
option; no marker line was in the way.

## Director fact items

| # | bank line | wrong | right figure and source | state |
|---|---|---|---|---|
| 1 | era 10, "What this thread is for" ("about 3.6 million") | names D.C. but leaves it out of the sum; calls residents "citizens and nationals" | 4,313,440, about 4.3 million (Census 2020: D.C. 689,545, Puerto Rico 3,285,874, four island areas 338,021) | DONE: wrong words struck, right figure and sources in a CORRECTED note on the line, PATCH 2026-10-28 (T-769) at the end of the bank |
| 2 | era 10, "The Capitol was attacked" ("140 ... 80 ... 114 reported injuries") | joins two 2022 GAO reports that counted different things (GAO-22-105001: about 140 assaulted, about 80 Capitol Police. GAO-22-104829: about 114 Capitol Police "who reported injuries") | at least 174 assaulted, 114 Capitol Police and 60 D.C. police (GAO-23-106625, page 1) | DONE: same form. $1.5 million damage confirmed in both 2022 reports, kept |

The prose already had both right figures (T-716), so no prose change was needed for either item.

## Cuts

- Part 3, 1948 span: "Segregation means keeping people of different races apart." The move put it
  about 250 words after "Segregated schools kept children of different races apart." (ARCHITECTURE
  5.5, one gloss per chapter.)
- Part 3: the run-in labels "Ending segregated schools." and "Asking permission." (each now a span label).

## Back matter

- `control/backmatter/government-politics.md` line 273, "segregation: keeping people of different
  races apart (1900 to 1950)": era 8 no longer states that gloss word for word. It now glosses the
  word once, as line 238 has it ("segregated schools"). The book glossary
  (`manuscript/_backmatter/02-glossary.md` line 3403) credits "segregation" to Chapter 1, so the
  printed glossary does not change. Not edited (brief).
- No back-matter line names a span I split, and none carries 3.6 million or the 2022 GAO counts.

## Sources in hand (fetched 2026-10-28 with WebFetch, PDFs read with pdftotext)

- GAO-22-105001, 17 February 2022, page 1: "assaults on approximately 140 police officers, including
  about 80 U.S. Capitol Police (Capitol Police) officers, and about $1.5 million in damages".
- GAO-22-104829, 7 March 2022, page 1: "about 114 U.S. Capitol Police (Capitol Police) officers who
  reported injuries, and caused about $1.5 million in damages".
- GAO-23-106625, 28 February 2023, page 1: "assaults on at least 174 police officers, including 114
  Capitol Police and 60 D.C. Metropolitan Police Department officers."
- Census Bureau island areas story (October 2021): Guam 153,836, U.S. Virgin Islands 87,146, American
  Samoa 49,710, Northern Mariana Islands 47,329, "just under 339,000" (sum 338,021).

## Log

<!-- file | what landed | validator | --punct -->
- Started 2026-10-28. Guides, brief, R11, T-716 and the whole chapter read. Baseline: 3 part files
  0 errors, punct 0/0.
- part3 | 16: new span "Ending California's law on segregated schools, 1947" between "Poll taxes and
  the white primary" and the 1948 span, run-in "Ending segregated schools." cut; 1948 span's
  "Segregation means keeping people of different races apart." cut (now defined one span earlier).
  10: new span "Asking permission to change voting rules, 2013" after "Money and maps", run-in
  "Asking permission." cut | validator 0 errors | punct 0/0 | card names: 5 of 5 match one span each,
  no duplicate labels (80 spans, was 78).
- bank | both lines corrected in place (struck words, CORRECTED 2026-10-28 notes), PATCH 2026-10-28
  (T-769) appended with the three GAO quotes and the Census sum. CRLF kept. Sums checked by script:
  4,313,440, 3,623,895, 338,021, 174.
- Parts 1 and 2 not changed (hashes as at start). Era strips, card, closing answers not touched.
- Check: `python tools/project_state.py --check government-politics --stage prose`
  PASS  government-politics / prose. measured: ms_eras=10/10 written=10/10 ms_stories=14 (verified 14)
  emdash=0 semicolon=0 manuscript=28979w files=3 validator_errors=0. part1, part2, part3: 0 errors.
