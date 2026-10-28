# CHECKPOINT T-770 | war (Chapter 22) and america-world (Chapter 23) | structure pass after R13

STATUS: DONE (3 findings done, 1 left on purpose; both chapters PASS --stage prose)
BRIEF:  control/briefs/STRUCTURE-PASS.md
FIX CHECKPOINT: control/checkpoints/T-728-reviewfix.md
REVIEW: control/review/R13.md
FILES:  manuscript/war/part1-before-1800.md, manuscript/war/part3-1900s-and-today.md,
        manuscript/america-world/part3-1900s-and-today.md (no bank, back-matter or card change)
DIRECTOR FACT ITEMS: none

## Findings the old grid rule blocked (from T-728)

| chapter | finding | era | state | note |
|---|---|---|---|---|
| war | 9, Mabila | The 1500s | DONE | split "De Soto's march, 1539 to 1543" before its last paragraph; the new span "The end of the march, 1542 and 1543" (de Soto's death, the boats, the 311) now follows "How the battle at Mabila began", so the era runs 1539, 1540, 1542 to 1543 in order. The split serves order, not length. CUT: the T-728 bridge ", a year and a half before de Soto died" (redundant now) and the lead-in "The end of the march." (now the label) |
| war | 19, sickness in the camps | 1850 to 1900 | LEFT | T-728 already gave it its own lead-in, "What killed them.", in the era's opening block, right after the death counts and tied to the 224,097. The rule lets a long span split; it does not turn part of an era block into a span, and doing so would move the answer to question 1 out of the era's opening and split one counting passage in two |
| war | 22, Wounded Knee medals under "Who may serve" | 2000 to Today | DONE | split the span: "Who may serve" keeps Don't Ask Don't Tell, women in combat and the transgender ban; new span "The Wounded Knee medals and the Defense Department's name" holds the two paragraphs that are not about who may serve. CUT: the lead-in "The Wounded Knee medals." (now the label); KEPT: T-728's "The department's name." (marks the second topic) |
| america-world | 23, "The capital, the canal and an apology" | 1950 to 2000 | DONE | split: new span "Washington, D.C., and the vote" (the two D.C. paragraphs, after the territories spans); the rest relabeled "The Panama Canal and an apology to Native Hawaiians". KEPT: T-728's tie sentence (D.C. not a state, no vote for president until 1961, like the territories). CUT: the lead-ins "The capital." and "The canal." (now in the labels); "An apology." kept |

No other T-728 finding was skipped or done in part for a structural reason.

## Card lines and back matter

- No "Five minutes?" or "Can skip:" line in either chapter names a span this pass touched, so no card
  line changed. Every name on both cards still matches a span label.
- No back-matter line needs changing: control/backmatter/war.md line 190 ("October 18, 1540: the
  battle at Mabila") links to the era, and Mabila is still in era 2.
- Strips unchanged and still right: war era 2 1,730 words (9 minutes), war era 10 13 minutes,
  america-world era 9 2,422 words (12 minutes). Cards unchanged: war about 130, america-world about 90.

## Checks

- After every save: validate 0 errors, punct 0/0 (war part1, war part3, america-world part3).
- `python tools/project_state.py --check war --stage prose`: PASS (27,731 words, validator 0).
- `python tools/project_state.py --check america-world --stage prose`: PASS (18,533 words, validator 0).

## Log

- Started: brief, ARCHITECTURE-GUIDE (sections 2 and 4), both style guides, hard-subjects policy,
  T-728 checkpoint and R13.md read. Baseline --check: war PASS (27,749 words), america-world PASS
  (18,537 words).
- war part1 saved (Mabila): validate 0 errors, punct 0/0.
- war part3 saved (Who may serve split): validate 0 errors, punct 0/0.
- america-world part3 saved (D.C. split, relabel): validate 0 errors, punct 0/0.
