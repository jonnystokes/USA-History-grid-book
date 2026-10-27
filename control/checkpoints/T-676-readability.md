# CHECKPOINT T-676 | art | readability | the whole chapter (opening, eras 1 to 10, closing)

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check art --stage prose
BRIEF:  control/briefs/READABILITY.md (dispatch: control/briefs/READABILITY-WAVE2-DISPATCH.md, T-676)
MODEL:  opus
FILES:  manuscript/art/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md (bank research/research-art.md only for a PATCH) · hand-off control/backmatter/art.md

NOW:    nothing. All units landed 2026-10-27; prose gate PASS.
NEXT:   carry on from the first unit whose state is not "landed". Era bodies are replaced whole with
        the scratch script splice.py (scratchpad T-676), which refuses to write if a story marker changed.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | chapter opening (part1) | landed | opening block as first block of era 1: card (minutes set at 145, confirm at the end), spine, Dave Poem Jar anchor, turn, 3 questions, five minutes, can skip |
| 2 | era 01 before-1500 (part1) | landed | strip; summary led by its through-line; pottery span relabeled as a question, archaeologist gloss folded; petroglyph/pictograph glosses folded into one sentence; ceremony gloss cut (a child knows it); quarry gloss folded; 9 bold lead-ins; "Who dug" relabeled as a question, the 150-word Spiro paragraph split, 2 dates moved off the front, the 37-word La Vere quote split into two pieces under 25 words (same words); Nathan Jackson: hook, Who line rewritten, clan gloss folded, timing dispute turned into a Not known line, 3 lead-ins, 2 dates off the front. Cuts: "A ceremony is a set of religious acts..." (a child knows the word); "and is called the Birger figurine" (now the lead-in). No closer (under 2,500) |
| 3 | era 02 1500s (part1) | landed | strip; summary led by its through-line; Le Moyne span relabeled "How Le Moyne lost his Florida drawings" and led by the answer, 95-word paragraph split, 2 lead-ins, date off the front; John White: hook (seventy watercolors), Who line says why he matters, "probably born in Cornwall" moved to the When line, engraving gloss folded, 4 lead-ins, last long paragraph split, 2 dates off the front. Stays at about 470 words: it carries both the watercolors and the 1587 killings, all sourced. No cuts |
| 4 | era 03 1600s (part1) | landed | strip; summary led by its through-line, friar gloss folded; 3 lead-ins in the portraits span; Loara: hook (her stitched name), verse lead-in; books span: 2 dates off the front, psalm and pence glosses folded; Bradstreet: hook, résumé lines compressed into one sentence, the Woodbridge/Gordon question given two lead-ins; Acoma 1598-99 shortened with a callback to Chapter 2, which owns the full telling, every harm kept in plain words (DECISIONS #36), rape gloss folded; church: lead-in, date off the front, the two hedges turned into one Not known line; masks: Posada sentence re-led, prayer-stick gloss cut; Treviño and Po'pay dates off the front. Cuts: "Accounts differ on the number" (the range says it); "prayer sticks, which are sticks made for prayers" (the gloss repeated the word) |
| 5 | era 04 1700-1750 (part1) | landed | strip; summary led by its through-line (money from slavery and Native land), split; painters span: Kühn date off the front; Johnston: hook (pastels, pirates), pastel gloss folded, the 110-word France paragraph split in three, 2 lead-ins, dates off the front; Smibert: hook (the upstairs copies), Faneuil Hall line moved into the Boston paragraph, one lead-in, split; slavery span: 2 lead-ins, both paragraphs re-led and split; Lenape span re-led, the 170-word Walking Purchase paragraph split in two with lead-ins; baskets: double-woven gloss folded, date off the front. Cuts: Johnston "born in northern France in about 1674" and her death date (both in the When line); Smibert "His father was a wool dyer" and "He married Mary Williams in 1730" (résumé, nothing depends on them) |
| 6 | era 05 1750-1800 (part1) | landed | strip; summary led by its through-line; London span re-led (Copley), Wright lead-in; Peale: hook (paid with two people), the ambiguous "He" after Washington fixed, Who line names Moses Williams's slavery, 3 lead-ins, dates off the front, the 1849/1854 sale merged into the museum paragraph; Demah: hook (his signature), "genius" and "Negro" glosses folded, 4 lead-ins; Wheatley: hook (the 18 men), the two quote glosses put in parentheses after the quote, 2 lead-ins, 3 dates off the front; Johnson paragraph split, lead-in; Stuart: hook, birth line cut from the body (in the When line), lead-in, 3 dates off the front. Wheatley stays at about 410 words because the 18 men's statement is quoted whole. No cuts beyond Stuart's repeated birth sentence. Part 1 validator 0 errors, punct 0/0 |
| 7 | era 06 1800-1850 (part2) | landed | strip; summary led by its through-line, federal gloss kept (first use), split; Moses Williams and Joshua Johnson turned into callbacks to the era 5 telling (only the new facts kept: the physiognotrace, no chance to paint, the 1803-05 silhouettes, the 1796-1824 directories); 2 Academy lead-ins, life-class gloss folded; road span: 2 lead-ins, limner and apprentice glosses folded, Phillips split; Stock: hook, patronage gloss in parentheses, 2 lead-ins; Hudson span led by the land question, 3 lead-ins, Stockbridge paragraph split, "After an 1822 treaty" re-led; Cole: hook (Noah), 2 lead-ins, the 190-word Oxbow paragraph split, patron gloss folded; "By 1840" line at the seam before Catlin; Catlin: 6 lead-ins, Osceola and gallery paragraphs split, truce gloss folded, 4 dates off the front; Audubon split in three with a lead-in; Dave: hook, 5 lead-ins, both hedges turned into Not known lines, the 1818 and survey paragraphs split; photography: daguerreotype gloss folded, split, lead-in; Douglass: hook (160 vs 126), the count merged into one place, two quote glosses in parentheses, 2 lead-ins; closer "By 1850" with three bullets. Cuts: Stock "the third of twelve children" (résumé); Cole "born in England in 1801" (When line); Douglass's birth sentence trimmed to "born into slavery in Maryland" and the repeated count paragraph merged. Dave stays at about 760 words: the mortgage, the four enslavers, the sale, the family sold, the leg, the verses and the count are all sourced and none is résumé |
| 8 | era 07 1850-1900 (part2) | landed | strip; summary led by its through-line (cheap pictures and print, artists abroad or imprisoned), split; writers: Whitman re-led, dime-novel lead-in; Duncanson split with a lead-in; Civil War dead: 3 lead-ins, Devil's Den split, sharpshooter and door-yard glosses folded, the closing hedges turned into a Known / Not known pair; Homer: hook, lithography gloss folded, birth sentence cut; Edmonia Lewis: hook (the 100 plaster copies), Who line says why she left, 5 lead-ins, 4 long paragraphs split, bust gloss folded, two quote glosses in parentheses; "By 1866" line at the seam before the West span; West: 2 lead-ins, Ahwahneechee split, reservation re-gloss cut; museums span relabeled "Why was the Met closed on Sundays?" and led by the answer; Fort Marion: 6 lead-ins, 5 paragraphs split, the 40-word Making Medicine quote split in two pieces under 25 words (same words), NCA gloss folded, tuberculosis re-gloss cut; Howling Wolf: hook, 2 lead-ins, the Dawes acreage given its difference (90 million acres, arithmetic on the two figures already there); Cassatt split, Eakins re-led so the cause comes before the resignation; Twain: hook, 2 lead-ins, birth and death lines cut from the body (When line); Tanner: hook, 2 lead-ins, crucified gloss in parentheses, death line cut (When line); Shaw: 2 lead-ins, split; closer "By 1900" as a before/after pair. Edmonia Lewis stays at about 690 words: the beating, the poisoning charge, the theft charge and the lost statue are all sourced scenes. Cuts: the three résumé death/birth lines named above, the third tuberculosis gloss, the second reservation gloss |
| 9 | era 08 1900-1950 (part3) | landed | strip; summary led by its through-line (what counts as art, the government paying artists), split; Armory: armory gloss folded into the place, arson gloss folded, 2 lead-ins; O'Keeffe: hook, birth sentence cut (When line), lead-in; Native artists: De Cora re-led so the man who took her is the actor (her own account), boarding-school gloss folded, Studio paragraphs split, authentic gloss in parentheses, the 29-word Montoya quote split in two pieces, 3 lead-ins, the Board and river-cane sentences re-led off their dates; Martinez: hook (smoke and manure), archaeologist re-gloss cut, 2 lead-ins, date off the front; "By 1932" line at the seam before Harlem; Harlem: renaissance, mural, lynching and segregation glosses folded, one lead-in per person, Douglas split; Savage: hook (the harp), Who line says why she matters, birth sentence cut, 3 lead-ins, Harp paragraph split, licked/kicked note in parentheses, death line cut (When line); Hurston: hook ($943.75), folklorist and incorporated and royalty glosses folded, 3 lead-ins, Kossola paragraph split; federal art span relabeled "Who did the government pay to make art?" and led by the answer, 5 lead-ins, 4 paragraphs split, dates off the front; Lawrence: hook, 2 lead-ins, split; "By 1941" line before the hunger span; hunger span: re-led off "In the 1930s", 3 lead-ins, the 38-word Thompson quote split in two pieces under 25 words, EO 9066 re-led; Lange: hook, 2 lead-ins, birth sentence cut; Steinbeck: libel gloss folded, split with 2 lead-ins; Wilder's 2018 award cut to a pointer to era 10, which tells it in full; abroad span: sealed-bid gloss folded, lead-in; closer "By 1950" with one number and a comparison ($23.50 a week against $3,000 for Nighthawks). Augusta Savage stays at about 500 words: Fontainebleau and the lost Harp are both full scenes. Cuts: O'Keeffe, Savage, Hurston, Lange birth lines (When lines carry them); "Decades later, readers criticized how the books show Native and Black people" (told in full in era 10) |
| 10 | era 09 1950-2000 (part3) | landed | strip; summary led by its through-line (the fights came into the open), split, AIDS glossed once here; abstract span re-led, abstract gloss folded; Pollock: hook (his 1947 words), 2 lead-ins, dates off the front; CIA: Cold War gloss folded into one sentence, the 32-word Braden quote split in two pieces (same words), the closing hedge turned into a Not known line, 2 lead-ins; books span: Frank and Black-writers paragraphs re-led, Ruby Bridges split with a lead-in; Parks: hook (Ella Watson), birth line folded into "grew up in Fort Scott", lead-in, death line cut; Pop: 2 lead-ins, 3 dates off the front; Warhol: hook ("money"), silkscreen process folded into the sentence, 2 lead-ins; "By 1973" line at the seam before the protest span; protest span: 5 lead-ins, Wall of Respect, Barrio Logan and Michael Stewart split, graffiti and pornography glosses folded, dates off the front; Ringgold: hook, 2 lead-ins, birth and death lines cut; Native span: the 31-word Howe and 29-word Boney quotes split in two pieces each, 4 lead-ins, the IACA sentence re-worded so the law is not the actor, NAGPRA re-led; the Spiro paragraph (a retelling of era 1) cut to one callback sentence; Wilson's Darnall portrait cut to a callback, split; quilt: AIDS re-gloss cut, re-led; NEA: obscene/blasphemous glosses folded, 2 lead-ins, 2 dates off the front; Morrison: hook, 3 lead-ins, birth and death lines cut; closer "By 2000" with a question left open for era 10. Cuts: Krasner's birth and death dates (résumé of a person outside the box's subject); the era 9 retelling of the Spiro dig (diggers' names, the third destroyed, the thousands sold: era 1 tells them in full); the second AIDS definition; the repeated Darnall description |
| 11 | era 10 2000-today (part3) | landed | strip; summary led by its through-line, split; camera span re-led; portraits span split, Walker gloss folded, 2 lead-ins; Sherald: hook (the cancelled show), Who line names the cancellation, heart and transgender glosses folded, 5 lead-ins, 3 paragraphs split, birth line cut; statues: Confederacy re-led, 3 lead-ins, Wiley and Charlottesville paragraphs split, chief-justice gloss kept, MONUMENTS re-led; murals: Floyd re-led and the conviction moved after "In the weeks after the murder" (the old order made "the weeks after" point to the 2021 conviction), Bowser and Clyde re-led; "By 2025" line at the seam before the museums span; museums span: 5 lead-ins, 4 paragraphs split, lucre gloss in parentheses; Gibson: hook, Biennale/queer/curator glosses folded, 4 lead-ins, cuts below; prices: one in-chapter comparison added ($1,000 for all 32 soup cans, era 9), Beeple lead-in, split; AI span: 2 lead-ins, Thaler split, dates off the front; McKernan: hook (12,000 prompts), 3 lead-ins, date off the front; books: 3 lead-ins, PEN/ALA split, stereotype gloss folded; public money: split, lead-in, the order "stated"; closer "By today" with three dated bullets. Gibson cuts: birth and father's-job sentences (When line has the places), the body's repeat of the Who line's nation membership, and the repeated "speaking of the chief of the Mississippi Band" tail |
| 12 | chapter closing (part3) | landed | three questions answered word for word, what changed, five dates (all in the chapter), Not known, Where to go (MFA Boston, Dave's 1857 jars), Next: Chapter 33, Music. About 300 words, a little over the 280 target because question 1 needs both Demah and Dave |
| 13 | back-matter hand-off control/backmatter/art.md | landed | six sections; 190 glossary terms, 33 people, 15 dates, 30 places, 11 movies (all documentaries or a feature with no accuracy note in the box), 3 questions |
| 14 | second pass, whole chapter | landed | split 44 more paragraphs at their seams and re-led 24 date-first ones; varied the era first sentences (eras 5 to 10 had shared "in these fifty years, while" shapes) and two closers; glossed "trustees" and "curator" at true first use (eras 5 and 7), "prosecutors" became "government lawyers"; card set to 150 minutes (build count 30,127 words) and strips from measure_readability era sizes |

## SUBJECT NOTES (decided before writing, 2026-10-27)

**Measured before:** 28,296 words, 355 paragraphs, average 79.7 words, 119 over 90, 30.4% date-first,
attributions 5.1/1k, longest era 5,024 (1900-1950), 5 eras over 4,000, 33 stories (median 328, 8 over 400).

**Spine:** Who was allowed to make art in America, who got paid for it, and who ended up owning it
has always depended on who held power.

**Anchor:** Dave's Poem Jar. In 1857 the enslaved potter Dave cut "I made this Jar = for cash / Though
its called Lucre trash" into a jar sold for the profit of Lewis J. Miles. On October 29, 2025, the
Museum of Fine Arts in Boston gave his descendants ownership of it and one other 1857 jar (era 10 span
"What museums hold, and what goes back"; Dave's box in era 6).

**Three questions (repeat word for word in the closing):**
1. How did enslaved artists make art, and who got paid for it?
2. Who decided what counted as art, and who got to see it?
3. Why are museums giving back things they once took?

**Five minutes?** "Photographs of hunger, and photographs of the camps" in 1900 to 1950 (Florence
Owens Thompson: unpaid, unnamed, "I can't get a penny out of it"; Lange's camp photographs held back).

**Can skip:** "Portrait painters in the colonies" (1700 to 1750), "Writers" (1800 to 1850),
"Painters of the 1930s and 1940s" (1900 to 1950), "A camera in every pocket" (2000 to Today).
Nothing later depends on them (Kühn and Hesselius are re-introduced where their paintings appear).

**Furniture plan:** strips on all ten eras. "By" lines in the five eras over 4,000 words (06 to 10),
one or two each at span seams. Era closers on eras 06 to 10 (all over 2,500); eras 01 to 05 are under
2,500 and get none. Closers rotate shape: three bullets / before-after / one number / an open question.

**Repetition to cut to callbacks (§5.12 and inside the chapter):**
- Acoma 1598-99 (era 3): Chapter 20 owns the full telling. Keep every harm in plain words (DECISIONS
  #36: the rape in the Acoma account, the killings, the foot sentence and forced labor, the dispute)
  in a shorter passage with a callback; keep the church-building in full (this chapter's angle).
- Spiro dig retold in era 9 ("Native artists and Native objects"): era 1 owns it; cut to a callback.
- Moses Williams and Joshua Johnson told twice (era 5 and era 6): keep the second as a short callback.
- Repeated glosses (archaeologist, tuberculosis, Protestants, AIDS, double-woven basket, boarding
  school): explain once; re-gloss at most once where a later era would be lost.

**Hard subjects to keep intact:** Spiro graves and 600 remains; Acoma; Treviño's hangings and whippings;
Kühn's collared boy; Royall slave trade; Walking Purchase; Peale paid in people, Moses Williams held;
Prince Demah; Wheatley kidnapped; Audubon sold people; Dave (mortgaged, family sold, leg amputated);
smallpox 1837 and Osceola's head; Fort Marion prisoners and the dead named; Sand Creek; Edmonia Lewis
beaten; Japanese American camps; Michael Stewart; Breonna Taylor; George Floyd; Heather Heyer.

## Sources in hand

None needed so far: every furniture sentence restates the chapter.

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

## Cuts (each with its reason)

Every cut is also named in its unit row above. Summary:
- Résumé lines in story boxes, all still carried by the When line or not needed by the scene: birth or death sentences for Johnston, Stuart, Cole, Homer, Twain, Tanner, O'Keeffe, Savage, Hurston, Lange, Parks, Ringgold, Morrison, Gibson; Smibert's father's trade and his marriage; Stock's place among twelve children; Krasner's birth and death dates; Gibson's father's job.
- Repeated glosses (guideline 7 as reworded): ceremony (a child knows it), prayer sticks, the third tuberculosis, the second reservation, the third archaeologist, the second AIDS.
- Repetitions inside the chapter cut to callbacks: Moses Williams and Joshua Johnson in era 6 (told in era 5); the Spiro dig in era 9 (told in era 1); the Darnall portrait in era 9 (told in era 4); Wilder's award in era 8 (told in era 10); Douglass's photo count told twice in his box.
- Across chapters: Acoma 1598-99 shortened with a callback to Chapter 2 (Native Nations owns it), every harm kept in plain words.
- The anchor's last sentence (the family lent one jar back and sold the other) moved out of the opening; era 10 keeps it.

## Decisions and rules broken on purpose

- Nine story boxes stay over 400 words: John White (about 530: the paintings and the 1587 killings), Prince Demah (410), Phillis Wheatley (420: the 18 men's statement quoted whole), Dave (about 750), Edmonia Lewis (about 710), Augusta Savage (about 550), Zora Neale Hurston (430), Amy Sherald (about 490: Breonna Taylor and the cancelled show), Jeffrey Gibson (about 420). Each is a chain of sourced scenes, none a résumé.
- The closing runs about 300 words, over the 280 target.
- The "Not known" lines in story boxes sometimes take two sentences where the two accounts must both be named (Dave's leg).

## Log

- 2026-10-27 | opening + era 1 | landed | validator 0 | punct 0/0
- 2026-10-27 | eras 2 to 5 | landed one by one | validator 0 each | punct 0/0
- 2026-10-27 | eras 6, 7 | landed | validator 0 | punct 0/0
- 2026-10-27 | eras 8, 9, 10 + closing | landed | validator 0 | punct 0/0
- 2026-10-27 | second pass + minutes + hand-off | landed | validator 0 all three | punct 0/0 | --check art --stage prose PASS
- Measured after: 30,127 words, 565 paragraphs, average 53.3, 8 over 90 (3 are list blocks and the opening's turn), 0.2% date-first, attributions 5.0/1k, longest era 5,288, 33 stories (median 333, 9 over 400)
