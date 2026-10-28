# CHECKPOINT T-772 | rights-movements (Chapter 25) | structure pass (DECISIONS #54)

STATUS: DONE
BRIEF:  control/briefs/STRUCTURE-PASS.md
FIX CHECKPOINT: control/checkpoints/T-710-reviewfix.md
REVIEW: control/review/R15.md
FILES:  manuscript/rights-movements/part3-1900s-and-today.md, research/research-rights-movements.md (PATCH)
DIRECTOR FACT ITEMS: 1 (Levittown lease, Clause 25's exception, bank line 45)
BASELINE: --check PASS, manuscript=57246w, validator 0 errors, punct 0/0 on all three parts

## Findings the old grid rule blocked (from T-710)

| T-710 # | era | finding (first words) | T-710 workaround | state | note |
|---|---|---|---|---|---|
| 17 | 4 and 8 | "Quakers changed their rules about slavery" | "spans cannot move", so cues in the era 4 and era 8 openers | LEFT | the reviewer's "move the late parts" would take the Quaker span (1754 to 1778) into era 5 and the Tulsa payments and Native vote spans past 1950: still forbidden (nothing leaves its era). No move inside the era helps: the Quaker span is already the era's last, and the Tulsa and Native vote spans finish their own stories where they stand. Cues kept; label fix already done |
| 1 | 10, 2000 to Today | "Federal immigration agents shot and killed" | reviewer's first option (own section) needed a split; T-710 used a bridge | DONE | SPLIT: "The DREAM Act and DACA, 2001 to 2026, and two killings in Minneapolis" became "The DREAM Act and DACA, 2001 to 2026" and a new span "Federal agents kill two citizens in Minneapolis, 2026". Bridge kept: the new span still opens on Operation Metro Surge (why immigration agents were there), and "The numbers." stays in the DACA span (DACA facts, and it glosses ICE before the new span uses it). CUT: the lead-in "Minneapolis, 2026." (the label now says it) |

Checked all 25 rows. No other T-710 finding was skipped or done in part because of the grid rule
(6 and 18 took the reviewer's second option because the bank lacked the fact, not because of the grid;
2's "The law that followed." paragraphs answer the finding where they stand, as the march's outcome).
Card lines ("Five minutes?" Selma span, "Can skip:" three spans) name none of the spans touched here:
all four quoted names still match their labels exactly.

## Director fact items

| item | state | note |
|---|---|---|
| Levittown lease, Clause 25 exception | DONE | Bank: PATCH 2026-10-28 (T-772) appended at the end of research-rights-movements.md, copied from research-home-family.md's T-727 PATCH (Long Island Press, February 9, 2022, the clause's own words; NYT 1997 for the quoted wording), plus a one-line pointer under the wrong line 45. Prose: the T-710 text left the exception out (true but incomplete). Era 9 "Levittown, 1957" now adds "The lease included one exception: servants who were not white could live in a house if they worked for the white family there." The paragraph (then 98 words) split before Shelley v. Kraemer |

## Back matter

No back-matter line is made wrong (glossary "Caucasian: white" still matches; no back-matter line names the split span).

## Log

<!-- file | what landed | validator | --punct -->
- part3 | 1 (split, label, lead-in cut), fact item (Levittown exception, paragraph split) | 0 errors | 0/0
- bank | PATCH 2026-10-28 (T-772) at the end, pointer line under line 45 (CRLF kept, quote byte-checked against home-family) | n/a | n/a
- measure_readability after: 55,859 words (card "about 280" still right: 279.3 rounded to five), 975 paras, avg 57.3, 6 over 90 (unchanged). Era strips untouched.
--check (after): PASS rights-movements / prose (validator 0 errors on all three parts, emdash 0, semicolon 0, manuscript 57,267 w).
