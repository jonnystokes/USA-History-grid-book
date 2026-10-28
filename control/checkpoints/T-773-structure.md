# CHECKPOINT T-773 | health (Chapter 26) and disasters (Chapter 27) | structure pass after R16

STATUS: DONE
BRIEF:  control/briefs/STRUCTURE-PASS.md
FIX CHECKPOINT: control/checkpoints/T-711-reviewfix.md
REVIEW: control/review/R16.md
FILES:  manuscript/health/part1-before-1800.md, manuscript/health/part3-1900s-and-today.md,
        research/research-health.md,
        manuscript/disasters/part1-before-1800.md, research/research-disasters.md
VERIFY: python tools/project_state.py --check health --stage prose
        python tools/project_state.py --check disasters --stage prose

## Blocked findings in T-711 (skipped or done in part because of the old grid rule)

| chapter | # | era | finding (first words) | state | why |
|---|---|---|---|---|---|
| health | 19 | 1950 to 2000 | "In the Relf sisters' case, a" | done | T-711 note: "box not moved (stories stay in place)". Span "Sterilized without consent, the 1970s" split after the Relf ruling paragraph. The Relf box now sits between the halves, beside the ruling. New second span: "Native and Puerto Rican women" (Indian Health Service, Norma Jean Serena, Puerto Rico). The T-711 clause that introduces the sisters and the two named bans stay, because the span is still read before the box |

No other T-711 row was blocked by the grid rule. Disasters had none.

## Other T-711 rows looked at, not grid-blocked (left)

| chapter | # | state in T-711 | why left |
|---|---|---|---|
| health | 12 | fixed (gloss) | not blocked: penicillin is glossed at first use. Moving "Penicillin, 1942" before the 1932 Tuskegee span would break the era's date order |
| health | 6 | fixed | Jones and Allen are introduced in the span before the Rush box and their own box. No move needed |
| health | 22 | skipped | hard-subjects policy (the Tuskegee figures are the toll), not the grid rule |
| health | 16, disasters 25 | fixed | By lines already sit in their own era blocks before the span headings |
| disasters | 13, 14 | fixed (part) | partial because no figure may be cut (hard-subjects policy), not the grid rule |

## Director fact item

| item | state | source |
|---|---|---|
| Jamestown Starving Time count | done | health: food-farming bank era 03 line 48 with its source line (Historic Jamestowne, Encyclopedia Virginia, Britannica, Percy) copied into research-health.md as PATCH T-773, with McCartney (EV, "only 60 men and women, out of 240") and Glover (EV, the 1609 fleet: eight of nine ships reached Jamestown in late August 1609) copied from the disasters bank |
| same count, disasters | done (beyond the dispatch's words) | disasters said "Counts of the colonists differ" and gave "By May 1610 about 60 were alive" right after the 500, which reads as 60 of 500. Now: about 500 in Virginia, McCartney's 240 of them in the fort, about 60 of those 240 alive by May 1610. Both figures were already in the disasters bank. Note added there as PATCH T-773 |

## Cuts (ARCHITECTURE-GUIDE section 2)

- health, Relf box, last sentence: "The judge barred federal money for sterilizing people against their will, and barred doctors from threatening to cut off welfare money." The span directly above the box now states both bans, with the doctors' threats named in the sentence before. Nothing lost. The box gains the case name, *Relf v. Weinberger* (bank line 810, SPLC).
- disasters, "How many died.": "Counts of the colonists differ." and "Other counts record" cut. The director ruled that the two counts describe the colony and the fort and are not a dispute.

## Back matter

- control/backmatter/health.md line 32 (glossary, Starving Time: "when only about 60 of about 240 colonists lived"): still true, because the 240 is the fort count, but less exact than the chapter now is. Suggested if the director wants it: "when only about 60 of the about 240 colonists in the fort lived". Not edited.
- control/backmatter/health.md line 200 (people index, the Relf sisters, 1950 to 2000): still right. The box stays in its era.
- No disasters back-matter line changed meaning.

## Word-count guard

health opens with "about 115 minutes": 22,505 words by the build's count before, band 22,500 to 23,500. Now 22,520, card still right.
disasters "about 130 minutes": 25,694 before, now 25,693, card still right.
Card names (Five minutes?, Can skip:) all match a span exactly in both chapters. No card names a span I changed.

## Log

<!-- file | what landed | validator | --punct -->
research-health.md | PATCH 2026-10-28 (T-773) at the end of era 03: food-farming line 48 with its source line, McCartney 60 of 240 and Glover's 1609 fleet copied from the disasters bank, the director's reading | n/a | n/a
health/part1 | Jamestown, 1607: last paragraph now says eight ships came in August 1609, about 500 in Virginia and about 240 in the fort when the winter of 1609 to 1610 began, about 60 of those 240 alive by spring, "That winter is called the Starving Time" (25 words became 54, opens on the ships, not on a date) | 0 errors | 0/0
health/part3 | finding 19: span split, Relf box moved up between the halves, second half labeled "Native and Puerto Rican women", box's repeat of the two bans cut, box names *Relf v. Weinberger* | 0 errors | 0/0
disasters/part1 | "Why Jamestown starved, 1609 to 1610": "How many died." paragraph matched to the director's reading (33 words became 32) | 0 errors | 0/0
research-disasters.md | PATCH 2026-10-28 (T-773) after the T-320a count note: the director's reading and the new prose wording | n/a | n/a
all six part files | re-run after the last edit | 0 errors each | 0/0 each
health --check prose: PASS (23,708 words, 23/23 stories verified, 0/0, validator 0 errors)
disasters --check prose: PASS (26,392 words, 12/12 stories verified, 0/0, validator 0 errors)
