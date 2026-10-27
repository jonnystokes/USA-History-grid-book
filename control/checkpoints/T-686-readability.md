# CHECKPOINT T-686 | styles | prose (readability edit, second edition) | whole chapter

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check styles --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md)
MODEL:  opus
FILES:  manuscript/styles/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md · research/research-styles.md (PATCH only)

NOW:    done; report sent
NEXT:   nothing; the director checks and commits

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 0 | chapter opening | landed | anchor Hannah Lyman 1676; minutes 95 (recheck at end) |
| 1 | era 01 | landed | strip; through-line first; 1 question label; 3 paras split; 2 bold lead-ins; yucca and loom glosses inline; no cuts |
| 2 | era 02 | landed | strip; through-line first; pearl-count paragraph split from the scene; 3 lead-ins; 2 date-first openings fixed; no cuts |
| 3 | era 03 | landed | strip; through-line first; Puritan span label a question; dress-law span split to 7 paras with lead-ins; Mary Ring and Hannah Lyman reshaped with hooks (Lyman ~560 words: kept long, the deed, the war and the court counts are the context the hard-subjects policy needs); slashes and gloss sentences folded inline; no cuts |
| 4 | era 04 | landed | strip; through-line first; wig span label a question; Section 40 quote split into two under 25 words; 5 paras split; Jack box reshaped (hook, ad, clothes); duplicate constable gloss cut from the span; indigo export rise given a comparison (about 26 times); no cuts |
| 5 | era 05 | landed | strip; through-line first; tignon span label a question answered in sentence 2; Charity Clarke and Washington boxes reshaped with hooks, résumé lines moved to the end; 1775 indigo given a comparison (more than seven times 1748); 6 date-first openings fixed; no cuts |
| 6 | era 06 | landed | strip; through-line first; ready-made span label a question; Northup and the clothing-share paragraphs split; duplicate petticoat and corset glosses cut from the span; Douglass box reshaped with hook and lead-ins (~560 words: kept long, both halves, the childhood shirt and the sailor disguise, are this chapter's subject); 4 date-first openings fixed; no cuts |
| 7 | era 07 | landed | strip; through-line first; coal-tar span label a question; Keckley box reshaped, her own words as hook (~640 words: kept long, rape, freedom and the White House are each needed); Strauss/Davis box opens on the woodcutter's wife, birth résumé moved to the end, repeated patent and rivet glosses cut; one-line callback to Chapter 2 for the boarding schools; 7 date-first openings fixed; era ends at about 2,470 words, so no closer |
| 8 | era 08 | landed | strip; through-line first; Jones quote cut to 18 words; Triangle paragraph split with lead-in; Walker box opens on her hair falling out, birth lines moved after; Carothers box opens on Berchet's half ounce; Lowe box opens on the uncredited Oscar gown; duplicate commissioner gloss cut; U.S. to US; era ends at about 2,455 words, so no closer; no cuts |
| 9 | era 09 | landed | strip; through-line first; Ann Lowe gown span label a question; era closer "By 2000" (three bullets); Eames box reordered to open on the war splints, birth and death lines moved to the end; Tinker box hook; Pawnee, Dallas, Lowe money, El Monte and Martin paragraphs split; removal, discrimination, bankruptcy glosses inline; 11 date-first openings fixed; no cuts |
| 10 | era 10 | landed | strip; through-line first; two question labels (where clothes come from, CROWN Act); Tazreen, Walmart, Delaware case, LA pay and Landor paragraphs split; locs glossed once in the summary, repeat cut from the span; Tzul box opens on the Kathie Lee Gifford labels; Andrew Johnson hook on the 90 seconds; 1960 to 2018 cloth waste given a comparison (more than nine times); 10 date-first openings fixed; no cuts |
| 11 | chapter closing | landed | questions word for word; five dates all in the chapter; Not known = 1740 seizures unrecorded; Where to go = Mount Vernon coat; Next = Chapter 36 Sports and Play |
| 12 | back-matter hand-off | landed | control/backmatter/styles.md |

## SUBJECT NOTES

**Spine:** From the first colonial dress laws to the CROWN Act, Americans with power made rules about who could wear what, and much of the cloth came from people who were enslaved, held captive or paid by the piece.

**Three questions:**
1. Why did lawmakers and officials make rules about other people's clothes and hair?
2. Who made the cloth Americans wore?
3. Which new materials changed what Americans wore?

**Anchor:** Hannah Lyman, about 16, fined 10 shillings by the Hampshire County court in 1676 for wearing silk "in a flaunting manner", wearing it even when she "stood presented" (era 3 story box).

**Five minutes:** "Cotton picked in the South, woven in the North" in 1800 to 1850.
**Can skip:** "Wigs in Williamsburg, 1769 to 1775", "The Federal style, 1780 to 1820", "Shirtwaists and the Gibson Girl, 1890s" (labels kept plain and unchanged so the list stays true).

**"By" lines:** none needed (no era over 4,000 words; longest 1950 to 2000 at about 3,076).
**Era closers:** 1950 to 2000 (over 2,500). Eras 6 to 8 sit at 2,050 to 2,450: a closer only if the edited era passes 2,500. Era 10 carries the chapter closing instead.
**Question labels planned (never two in a row):** era 1 feathers span, era 3 Puritan colors, era 4 wigs, era 5 tignon, era 6 ready-made, era 7 coal tar, era 9 Ann Lowe's gown, era 10 where the clothes come from and the CROWN Act.
**Next line:** Chapter 36, Sports and Play (its spine: who was allowed to play).
**Where to go:** Mount Vernon holds Washington's 1789 brown wool coat (in the chapter: came to the collection in 1933).
**Gloss repeats to fix:** petticoat and corset (era 6 twice), constable (era 4 twice), slashes (era 3 twice), patent (era 7 twice), locs (era 10 twice). "U.S." to "US" in era 8.

Before (measure_readability.py styles): words 18601, paras 273, avg_para 68.1, over90 45, date_first 20.5%, def/1k 1.2, attr/1k 6.5, also/1k 1.8, you 4, longest_era 3076, eras>4000 0, stories 16, story_med 322, stories>400 4.

## Decisions and cuts

## Log
2026-10-27 | opening + era 01 | landed | validator 0 | punct 0/0
2026-10-27 | era 02, era 03 | landed | validator 0 | punct 0/0
2026-10-27 | era 04, era 05 | landed | validator 0 | punct 0/0
2026-10-27 | era 06, era 07 | landed | validator 0 | punct 0/0
2026-10-27 | era 08 | landed | validator 0 | punct 0/0
2026-10-27 | era 09 | landed | validator 0 | punct 0/0
2026-10-27 | era 10, closing, hand-off | landed | validator 0 x3 | punct 0/0 x3 | --check styles --stage prose PASS

## Self-review notes
- Reading time: 19,536 words (measure_readability) -> about 100 minutes; the build's load_chapter agrees (no warning). Era strips match words/200.
- Era first sentences read together: all differ in shape; eras 7 and 8 reworded so they do not share an ending ("after 1850" / "Chemists made...").
- Glosses now inside the sentence everywhere, story boxes included (parentheses after quotations for archaic words, per ARCHITECTURE-GUIDE 5.10).
- Repeats cut: petticoat and corset (era 6 span), constable (era 4 span), slashes (era 3), patent and rivet (era 7 box), locs (era 10 span), commissioner (era 8 span), kersey (era 6, third gloss). Duplicate Mary Ring death date folded.
- Comparisons added from the chapter's own numbers only: indigo exports about 26 times (1745-46 to 1748), 1775 more than seven times 1748, cloth thrown away 2018 more than nine times 1960.
- One body callback added: "Chapter 2, Native Nations, tells the full story of the boarding schools." (era 7, Carlisle).
- Quotations over 25 words split or cut to the quoted part: Section 40 of the 1740 act (two quotes), Jones's 1902 letter (18 words).
- Rules broken on purpose: none. Story boxes over 400 kept long for a reason: Hannah Lyman (land, war and court context), Douglass (childhood clothes and sailor disguise), Keckley (rape, freedom, White House), Eames (424, the design and credit story).
- Not improved: attribution stays about 6.3 per 1,000 words, because most of what remains is disputed counts, witnesses or historians' readings (DECISIONS #37, #45). Three over-90 "paragraphs" are furniture (the opening turn at 103 words, the era 9 closer and the closing block, which the measure joins into one).
- No facts added, none removed; no worked passage collapsed.
