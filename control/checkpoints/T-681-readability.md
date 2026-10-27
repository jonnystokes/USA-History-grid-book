# CHECKPOINT T-681 | storytelling-evolution | readability | the whole chapter (opening, eras 1 to 10, closing)

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check storytelling-evolution --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md, T-681)
MODEL:  opus
FILES:  manuscript/storytelling-evolution/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md (bank research/research-storytelling-evolution.md only for a PATCH) · hand-off control/backmatter/storytelling-evolution.md

NOW:    nothing. All 13 units landed, 2026-10-27.
NEXT:   the director reads the report. If anything is reopened, every unit in the table is landed; start from the unit named.

Method: each era is rewritten in a scratch file (scratchpad T-681/eraNN.md) and spliced between its
hb-time markers by scratchpad T-681/splice.py, which refuses the splice if any hb-story marker line
changes, if the span count changes, or if an em dash or semicolon is in the new prose.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | chapter opening (part1, first block of era 1) | landed | opening card written as the first block of era 1 (spine, Accomack anchor, turn, three questions, five minutes, can skip); reading time 125 provisional, reset at the end |
| 2 | era 01 before-1500 (part1) | landed | strip; summary re-led on the through-line (acting was part of religion); first span relabeled as a question answered in its first sentence; 4 paragraphs over 90 split; lead-ins Yupik masks, Haudenosaunee masks, Tlingit crests, Casa Rinconada; "ancestral" replaced by plain words; archaeologists glossed inside the sentence; two attributions dropped (Archaeological Conservancy date, Thunen on plazas, Chaco Research Archive), facts kept. No cuts. No closer (about 1,000 words) |
| 3 | era 02 1500s (part1) | landed | strip; summary re-led (the first play was acted the day Onate claimed the land, and Native people were made to act in it); span relabeled "The play at the river, 1598"; 5 paragraphs split; 6 lead-ins; friars and baptism glossed inside sentences; rape explained inside the sentence; Farfan box: hook, speech moved first as the scene, the muster gloss replaced by plain words (cut the term "passing muster"/"muster roll": the facts stay); Acoma kept whole (see SUBJECT NOTES). No closer |
| 4 | era 03 1600s (part1) | landed | strip; summary re-led (people with power tried to stop acting); 1665 span relabeled; Parliament quote glosses folded into one meaning sentence (cut the second quoted phrase list "Public Calamities", "Seasons of Humiliation", "sad and pious Solemnity": same meaning as the quote kept); John Fawsett demoted to "the king's attorney" (names rule, he does nothing else in the chapter); Darby box: hook, arrest order first, closing hedge made a Not known line; Pueblo span: 3 lead-ins, 2 splits, Zotigh demoted to "the Smithsonian's account"; American Battlefield Trust attribution dropped (uncontested). No closer |
| 5 | era 04 1700-1750 (part1) | landed | strip; summary re-led (the first theatres, and two of the first actors were not free), Aston moved out of the summary (his span keeps him); Whitefield span relabeled as a question answered in its first sentence (Franklin's 30,000); 4 splits, 6 lead-ins; "indentured servant" glossed inside the sentence; Aston box: hook (his own words), preface/exciseman/publican/player glosses folded; Levingston box: hook; Pinkster: the "possibly as early as 1749" hedge resolved by the Hercules fact already there. Cuts: "Charles Shepheard's" tavern name demoted to "a tavern on Broad Street" (names rule); "A shilling was a unit of money" (a child can read it from "cost"). No closer |
| 6 | era 05 1750-1800 (part1) | landed | strip; summary split in two and re-led on the through-line (paid actors arrived, lawmakers passed laws against plays); "Laws against plays" relabeled "Why lawmakers banned plays", answered in its first sentences; 1752 span relabeled; 6 splits, 7 lead-ins; impiety, peculiar/morals, Sons of Liberty, extravagance/dissipation glossed inside sentences; "is said to have read it" given its basis ("By one account"); hooks on all four boxes. Cut: the Britannica sentence calling Jonathan "the predecessor of many such" (it restated the sentence before it). No closer (about 1,900 words) |
| 7 | era 06 1800-1850 (part2) | landed | strip; summary split in three and re-led (white audiences paid for blackface while Black Shakespeare actors were attacked and arrested), "Blackface." lead-in; Astor span relabeled with the date at the end; 9 paragraphs split, 12 lead-ins; caricature, segregation, playbill glossed inside sentences; the Astor death counts gathered into one "The dead." paragraph after a single "at least 22" up front; all four boxes hooked; Lane: closing hedge made a Not known line. Cuts: in the Brown box, the retelling of the break-in and the arrests (told in full in the span just above; one clause keeps the link); in the Aldridge box, the second gloss of discrimination (glossed in the era summary); in Forrest, "She got the divorce" (repeats "won their divorce case"). Closer "By 1850": three bullets |
| 8 | era 07 1850-1900 (part2) | landed | strip; summary re-led (the biggest touring shows told Black and Native stories, and white showmen decided how), "Other stages." lead-in, Booth sentence re-led off the date; three spans relabeled (two promises, one question "What did the first films show?" answered in its first sentence); 11 splits, 14 lead-ins; Negro, culls, colored, typhoid/smallpox, Ghost Dancers, reservation glossed inside sentences; all three boxes hooked, Booth box opens on the Jersey City rescue. No cuts. Closer "By 1900": before/after pair |
| 9 | era 08 1900-1950 (part3) | landed | strip; summary re-led (acting moved onto film and radio and the people in charge kept the minstrel parts; the minstrel stage re-glossed once for a reader opening here), "Who played whom." lead-in; three spans relabeled (Birth of a Nation and Wounded Knee with the date last, the contracts span as a promise answered first); about 16 splits, 25 lead-ins; lynch, miscegenation, petition, communism, dictator, sentiments glossed inside sentences; "By 1915" (end of the Wounded Knee span) and "By 1934" (end of the Code span); all six boxes hooked. Cuts: in Bert Williams, the stand-alone glosses of minstrel shows and vaudeville (both glossed in the era summary); "Colored was a word of that time" at the NAACP (glossed in era 7) and "Negro was a word of that time" at the Negro Theatre Units (glossed in era 7, and "companies of Black actors" explains it); the Library of Congress credit on the Chicago ban date (uncontested). Closer "By 1950": one number (40 million listeners) against the 700,000 petitions |
| 10 | era 09 1950-2000 (part3) | landed | strip; summary split in four and re-led (the fight over who could act turned political after 1947; communism re-glossed once for a reader opening here), lead-ins "Live and on film." and "The parts on offer."; blacklist span relabeled as a question answered first, Brando span relabeled as a promise answered in its first sentence; about 14 splits, 22 lead-ins; Robeson's 41-word quotation split into two quotations under 25 words (same words); stoolie, B movies, restrictive covenant, tomahawk chop, stereotype glossed inside sentences; all six boxes hooked. Cut: the second gloss of "stereotype" in the Moreno box (glossed in the span just before). Closer "By 2000": one open question (would game actors be paid like film actors), answered in era 10 by the 2016 and 2024 strikes |
| 11 | era 10 2000-today (part3) | landed | strip; summary split in three and re-led (the newest fight is over computer copies of actors), lead-ins "Screens and seats." and "Who is on screen."; about 15 splits, 25 lead-ins; "By 2021" (end of the YouTube span) and "By 2023" (end of the Weinstein span); background actors, refugees, harassment/assault/rape (rape re-glossed once for a reader opening here) folded into sentences; "local courts put" made "local judges put"; all four boxes hooked. Cut: the second gloss of AI in the video game strike span (glossed in the 2023 strikes span just before). Closer "By today": three bullets, then "Next" points to the closing |
| 12 | chapter closing (part3, last block of era 10) | landed | closing written as the last block of era 10: the three questions word for word with answers, What changed, five dates (April 30, 1598 / 1821 / 1828 / February 8, 1915 / July 14, 2023, all in the chapter), Not known (the title and script of the 1598 play), Where to go (Ford's Theatre), Next: Chapter 35, Styles |
| 13 | self-review (§8), checks, measure, back-matter hand-off, report | landed | second pass: 12 more paragraphs split (84 over 90 before, 2 after, both the closing's bullet lists); 22 date-first paragraphs re-led (25.3% to 1.2%); the ten era first sentences re-read together and four reshaped so they no longer share "in these fifty years" (eras 4, 5, 6, 7), the same for three closers; three hooks cut to 12 words; strips set from era_sizes (6, 6, 6, 7, 9, 15, 15, 24, 17, 26) and the card from measure_readability (24,860 words, 125 minutes); validator 0 errors on all three parts, --punct 0/0, --check prose PASS; hand-off control/backmatter/storytelling-evolution.md written |

<!-- state: todo | working | landed | skipped (say why) -->

## SUBJECT NOTES (the plan, written before any edit)

**Before (measure_readability, 2026-10-27):** words 23109, paras 312, avg_para 74.1, over90 84,
date_first 25.3%, def/1k 1.6, attr/1k 6.1, also/1k 1.5, you 16 (all inside quotations: Vukelich,
Talmadge, the sheriff, Ziegfeld, Farber), longest era 4567, eras>4000 2, stories 29, story median
292, stories>400 1.
Per-era words (era_sizes): 1: 1001 · 2: 1224 · 3: 1144 · 4: 1461 · 5: 1834 · 6: 2836 · 7: 2910 ·
8: 4567 · 9: 3308 · 10: 4480.

**Chapter number:** 34 of 37 (control/chapter-registry.md). Next: Chapter 35, Styles.

**Spine:** People here have acted out stories for centuries, and in every era someone fought over
who was allowed to act, whom an actor could play, and who owned the performance.
(Every era carries it: Haudenosaunee mask rules and Ojibwe telling seasons; the Manso made to act
in 1598; the 1665 court case and the burned Pueblo masks; Sewall and the servant actors; the
anti-theatre laws and Congress; the African Theatre arrests and blackface; the Tom shows, the Wild
West and the 1883 dance rules; blackface film, the Code and Anna May Wong; the blacklist and "Who
was allowed to play whom"; #OscarsSoWhite, scans and digital replicas.)

**Three questions:**
1. Who tried to stop Americans from acting, and why?
2. Why did white actors play Black, Asian and Native people for so long?
3. Who controls a computer copy of an actor's face and voice?

**Anchor:** the Accomack County court orders of 1665 (era 3): three men acted *Ye Bare and Ye
Cubb* on August 27, 1665; on November 16 the judges ordered them to come back "in those
habilemts that they then acted in", with the script; in January 1666 the judges found them not
guilty and made the man who reported them, Edward Martin, pay the costs. The orders are the only
record of the play. All already in the chapter.

**Five minutes?** "The African Theatre, New York, 1821 to 1823" in 1800 to 1850 (about 600 words).

**Can skip:** "Places built to hold a crowd" (era 1), "Shakespeare on the rivers" (era 6), "Big
openings and home video" (era 9), "YouTube and TikTok" (era 10). Nothing later depends on them.

**Reading time:** words / 200 rounded to 5, set at the end from measure_readability (expect about
120 to 125 minutes). Strips from era_sizes / 200.

**"By" lines:** era 8 (4,567 words): two, before Bert Williams ("By 1915") and before "Plays on the
radio" ("By 1934"). Era 10 (4,480 words): two, before "Who is on screen" and before "The 2023
strikes". No others (era 9 is 3,308).

**Era closers (eras over 2,500 words):** eras 6, 7, 8, 9, 10, rotating the middle: era 6 three
bullets; era 7 a before/after pair; era 8 one number with a comparison; era 9 one question left
open and answered in era 10; era 10 three bullets, then the chapter closing. Eras 1 to 5 get the
strip only (all under 2,500).

**Span labels:** about half become a question or a promise, never two questions in a row, each
answered in the first two sentences under it.

**Story boxes:** all 29 get a bold hook. Cut résumé lines where the record lines carry them.
Fold stand-alone glosses into sentences ("Passing muster means...", "Minstrel shows were...",
"Vaudeville was..." in Bert Williams, which repeat earlier glosses).

**Repeated glosses to cut to one per chapter (guideline 7):** stereotype (twice in era 9),
AI (twice in era 10), minstrel and vaudeville (re-glossed in era 8 summary and Bert Williams),
"Colored" and "Negro" (each glossed twice), communism (era 8 and era 9: era 9 may keep one short
re-gloss). Rape is explained once, inside the sentence, at Acoma (era 2), and again once in era 10
(a reader opening era 10 needs it, and #31 asks for it per part file).

**Hard subjects to keep whole:** Acoma 1598 to 1599 (feet cut off, enslavement, the girls taken,
the disputed 24), the Pueblo leaders hanged and whipped in 1675, the 1766 crowd that beat an actor
and killed a child, Astor Place (22 to 31 dead), the Birth of a Nation lynching and Klan murders,
Wounded Knee 1890, the boarding schools (973), the Osage murders, Weinstein (courts only, #43,
rule 5: he is convicted, so courts and records are stated; nothing beyond them).

**Choice not to cut:** the Acoma span (era 2) is also told in Chapter 20, but here it is the same
men who staged the first play, and #36 forbids a softer version. It stays whole, split into short
paragraphs.

## Decisions and defects fixed

- Span labels changed (allowed by ARCHITECTURE-GUIDE 4.6; the pilot did the same): "Who is inside the mask?", "The play at the river, 1598", "A play, a complaint and a court, 1665", "How far could one preacher's voice carry?", "Why lawmakers banned plays", "The first touring company, 1752", "The Astor Place riot, May 10, 1849", "A novel against slavery, acted in blackface", "The actor who shot Lincoln", "How vaudeville began", "What did the first films show?", "The Birth of a Nation, 1915", "Wounded Knee acted again, 1913", "How a seven-year contract ran longer", "Who lost work in the blacklist?", "Why Brando refused his Oscar, 1973". No two question labels in a row. The four "can skip" labels are unchanged.
- No story slug, status, movie record or era marker changed (splice.py compared every hb-story marker line before writing).
- Kept on purpose: the Acoma span whole (see SUBJECT NOTES); the Weinstein court record in full (living, convicted: courts and records only); the Astor Place chain of who gave the order to fire (hard-subjects rule: name the actor).
- Stories over 400 words (measure_readability: 2): left long on purpose; they are scene chains (McDaniel's award night and her house and grave; Ke Huy Quan's refugee journey and return), nothing résumé-shaped left to cut.
- Attribution stays at 5.7 per thousand: most of what is left is contested counts (Astor Place, Acoma, Osage), quoted witnesses, or Britannica and the reference books quoted word for word.

## Cuts (each with its reason)

- Era 2: the term "passing muster" / "muster roll" in the Farfán box (replaced by plain words; the facts stay).
- Era 3: the second quoted phrase list from the 1642 order ("Public Calamities", "Seasons of Humiliation", "sad and pious Solemnity"), same meaning as the quotation kept; John Fawsett's name (demoted to "the king's attorney", names rule).
- Era 4: Charles Shepheard's name on the Charleston tavern (names rule); "A shilling was a unit of money" (a child reads it from "cost").
- Era 5: the Britannica sentence on Jonathan as "the predecessor of many such" (restated the sentence before it).
- Era 6: in the Brown box, the retelling of the break-in and arrests (told in full in the span just above); in the Aldridge box, the second gloss of discrimination; in Forrest, "She got the divorce" (repeats "won their divorce case").
- Era 8: stand-alone glosses of minstrel shows and vaudeville in Bert Williams (both glossed in the era summary); the "Colored" gloss at the NAACP and the "Negro" gloss at the Negro Theatre Units (both glossed in era 7); the Library of Congress credit on the Chicago ban date.
- Era 9: the second gloss of "stereotype" (Moreno box).
- Era 10: the second gloss of AI (video game strike span).

## Log

- 2026-10-27 | units 1 to 6 (part1) | opening and eras 1 to 5 spliced | validator 0 errors | punct 0/0
- 2026-10-27 | units 7 and 8 (part2) | eras 6 and 7 spliced | validator 0 errors | punct 0/0
- 2026-10-27 | units 9 to 12 (part3) | eras 8 to 10 and the closing spliced | validator 0 errors | punct 0/0
- 2026-10-27 | unit 13 | second pass, date-first and era-first-sentence fixes, hand-off | --check prose PASS
- After: words 24860, paras 484, avg_para 51.4, over90 2, date_first 1.2%, def/1k 0.6, attr/1k 5.7, also/1k 1.3, you 22 (furniture and quotations), longest era 5117, stories 29, story median 301, stories>400 2.
