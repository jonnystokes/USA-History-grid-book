# T-771 structure pass: slavery-freedom (Chapter 24)

Brief: control/briefs/STRUCTURE-PASS.md. Fix checkpoint: control/checkpoints/T-730-reviewfix.md. Review: control/review/R14.md.
Baseline 2026-10-28: --check slavery-freedom --stage prose PASS (validator 0 x3, punct 0/0).

Blocked findings in T-730: 6 and 14 (heading on a marker line not changed). Finding 12's skip (strips do not
add to the card) is a rounding matter, not the grid rule: left. No other finding was held back by the grid rule.

## Findings

6. Two promises / Attucks: DONE. Split the span: new span "Crispus Attucks, 1770" (the Attucks paragraph, now
   opening on Attucks as the first person British soldiers killed) placed just before "Two promises of freedom
   in the Revolution", same era. Cut the fixer's "Before any promise." lead-in and its sentence ("A Black man
   died in the quarrel with Britain years before either side promised anything."): it only bridged Attucks
   into a span about promises, and the split makes it redundant. The promises span now holds only the point,
   Dunmore's promise, the Patriot promise and the count. Label "Two promises of freedom in the Revolution" kept:
   it now fits.
14. 13th Amendment / Five Tribes heading: DONE. Split the span: the two Five Tribes paragraphs are now their own
   span, "Slavery in the Five Tribes", right after the first, same era. The bold lead-in "The Five Tribes." cut
   (it would repeat the new label). The fixer's bridge (the Choctaw and Chickasaw forced west in the 1830s) kept:
   it now opens the span. First span relabeled "Combahee Ferry, Juneteenth and the 13th Amendment" ->
   "Combahee Ferry, the 13th Amendment and Juneteenth", so the label follows its paragraphs' order (T-730 moved
   the December 6 sentence up into the 13th Amendment paragraph, ahead of Juneteenth).
   Also in the new span: "the people their nations had enslaved" -> "the people held in slavery in their
   nations" (a nation as the actor, the same personification T-730 fixed in the paragraph above).

Card pointers: no card line names any span I split or relabeled ("Five minutes?" and "Can skip:" unchanged).
Other chapters and the back matter point to the 1850 to 1900 era, not to these labels.

## Director fact item

Smallpox vaccination "a shot" (era 7, "Freedom taken during the war", The camps): DONE. "They could vaccinate
people, giving them a shot that protects against the disease, and they could keep the sick away from the well"
-> "They could vaccinate people by scratching fluid from the sores of cowpox, a mild disease of cows, into the
skin. They could also keep the sick away from the well", as Chapter 26 and the glossary word it. Bank PATCH
2026-10-28 (T-771) in era 7: the health bank's line (era 06, Countway Library of Medicine, "Gilt by
Association") copied with its source, plus one search for the 1860s (Smithsonian, Eschner 2017: Civil War
soldiers cut the arm and coated the wound with lymph; not used in the prose, its wording is loose).

## Back-matter lines now wrong (not edited)

- control/backmatter/slavery-freedom.md line 92: "vaccinate: to give a shot that protects against a disease
  (1850 to 1900)". Suggest: "vaccinate: to scratch fluid from the sores of cowpox, a mild disease of cows, into
  the skin to protect a person against smallpox (1850 to 1900)", and a new line "cowpox: a mild disease of cows
  (1850 to 1900)".
- manuscript/_backmatter/02-glossary.md line 931: "cowpox ... (Chapter 26)". Chapter 24 now explains cowpox,
  so the chapter of first use may become Chapter 24 (director's call).
- Not caused by this task: control/backmatter/art.md line 76 also says "vaccination: a shot that protects a
  person from smallpox (1800 to 1850)", though the art chapter's prose already says scratched.

## Cuts (ARCHITECTURE-GUIDE section 2)

- Era 5: the "Before any promise." lead-in and its bridge sentence (redundant after the split).
- Era 7: the bold lead-in "The Five Tribes." (repeats the new label).

## Checks 2026-10-28

- validate_grid --part: part1 0 errors, part2 0 errors (part3 unchanged, 0 errors in --check).
- project_state --punct: part1 0/0, part2 0/0.
- project_state --check slavery-freedom --stage patch: PASS. --stage prose: PASS (manuscript 23,635w,
  validator 0 x3, 0 em dashes, 0 semicolons).
- Strips unchanged and still right by rule: era 5 2,039 words (10 min), era 7 6,458 words (32 min). Card
  still 110 minutes (22,095 prose words). Part files and bank stay pure CRLF.
