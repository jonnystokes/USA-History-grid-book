# T-757 review fix: How We Know, Movies, Answers (R25 findings)

Brief: control/briefs/BACKMATTER-EDIT.md rules + control/briefs/REVIEW-FIX.md "How to judge a finding".
Files: manuscript/_backmatter/01-how-we-know.md, 06-movies.md, 07-answers.md (and, for answer changes,
the chapter closing in manuscript/<slug>/part3-1900s-and-today.md and control/backmatter/<slug>.md).
Scratch: C:\Users\jon\AppData\Local\Temp\claude\C--Users-jon-Projects\c3422736-ab9a-4784-b707-6df665469603\scratchpad\T-757\
(t757_apply.py + t757_spec_*.txt hold every edit; t757_answers_check.py compares page, closings, hand-offs).

## Status: DONE

All 21 findings handled: 17 fixed in full, 4 in part (White Lion, movie labels, Ch 4/Ch 30 answers
skipped, Mabila/Arenal/Cepheid skipped), none skipped whole. All three back-matter
files, the 9 part files and the 9 hand-offs changed show --punct 0/0. validate_grid --part: 0 errors on the
9 part files. --check prose: PASS for city-building, landmarks, government-politics, crime-justice, war,
health, disasters, storytelling-evolution, sports-play. Answers page vs closings: 0 mismatches (all 111).

## How We Know What Happened

1. Horse-bone study chapter: FIXED. The study is in Chapter 2 and Chapter 5 (and 10). The page now names
   Chapters 2 and 5, in its own short paragraph, and words the result as the Ch 5 answer does ("as the nations'
   own histories say"), which drops "showed ... were right" (both chapters say the timing is not settled).
   Answers page needs no change (the study is the Ch 5 answer).
2. Hoover Dam certainty: FIXED. "Many historians think" removed (the landmarks bank corrects it to "workers
   alleged"). Now: workers blamed the deaths on carbon monoxide (the Ch 12 and Answers wording), the count leaves
   out deaths from heat and sickness, so the true number is higher than 96 and nobody knows exactly how many.
   Pneumonia glossed "a sickness of the lungs" (Ch 12's gloss).
3. Hugh Gwyn sentence: FIXED ("three servants who had run away together from their master, Hugh Gwyn").
4. John Punch wording: FIXED. "Historians count that ruling as the first known sentence of lifetime slavery in
   Virginia, because Punch had to serve until he died and his master could sell him or give him away" (Ch 24
   story and bank: "his assigns" = anyone the master sold or handed him to).
5. 1619 names: FIXED by narrowing to "No record made in 1619 names any of the Africans who landed that year."
   No bank has an Angelo/Angela line, so no clause about the 1624-25 lists.
6. White Lion English vs Dutch: FIXED IN PART. Added "which had sailed from the Netherlands" (Ch 19 and
   Encyclopedia Virginia in the banks). Rolfe's own "Dutch" wording is in no bank or chapter: not quoted.
7. Archives and Bureau of Reclamation: FIXED ("archives, the places where old papers are kept"; "the Bureau of
   Reclamation, the federal office that runs the dam", Ch 12's words).
8. Closing triad: FIXED (cut; the page ends on the line about new evidence).

## Movies

1. Age note: FIXED. Intro: "Some of these were made for adults, so check each one's rating and ask a grown-up
   before you watch it."
2. Documentary or drama: FIXED IN PART. 36 entries relabeled "drama" or "documentary" where the story box or the
   research bank supports it (actors named, "feature film" set against "documentary" in the banks, or the bank
   says documentary). Left as the box gives them, with no label in box or bank: 12 Years a Slave, Apollo 13,
   Good Night and Good Luck, Kemba, Lincoln, Man in the Wilderness, The Revenant, Inside Bill's Brain (series),
   Izzy and Moe (a comedy, actors named), Marian Anderson concert film (real footage, says so). The invented-
   parts notes the boxes give were already on the page.
3. The 1915 Birth of a Nation: FIXED. New line from Ch 34's span: a drama by D. W. Griffith that showed Klan
   members lynching a Black man and stopping Black men from voting; after it opened in Atlanta, William J.
   Simmons started the Klan again (Chapter 34). The Nat Turner box names it. 158 lines now.
4. Subjects: FIXED. Bolinao 52 (the 1988 refugee boat, Tung Trinh one of its 52 survivors), Citizen Jane (Jane
   Jacobs's fights with Robert Moses), Seeking the Greatest Good (Gifford Pinchot), all from their boxes/banks.
5. Chavez accounts: FIXED. Both lines now say they came out before March 2026, when the New York Times reported
   that Chavez had sexually abused two girls and Huerta said he had raped her (the Ch 14 Chavez-Huerta box).
6. Sort note: FIXED. Intro: a title that begins with "The" or "A" is sorted by its next word.

## Answers to the Chapter Questions

1. Ch 27 Q1 too long: FIXED (138 to 77 words): opens "Some worked, some failed and some are still being
   tested", then the span of rules, one example each (gas smell, 1838 steamboat law, FEMA's future debated in
   late September 2026). Every dropped item is told in the Ch 27 body.
2. Ch 34 Q1 too long: FIXED (107 to 69 words): pattern first (church leaders and lawmakers early, for religion
   and morals), four examples kept. Ch 4 Q2 and Ch 30 Q2: SKIPPED, each already runs in order by who and how,
   and trimming would cut real facts.
3. Ch 5 horse study vs How We Know: FIXED on the How We Know page (HWK 1).
4. Ch 20 New Jersey 1807: FIXED ("women and free Black men", as Ch 20's body and the Ch 25 answer say).
5. Ch 12 killings: FIXED (Dylann Roof, James Alex Fields Jr., Derek Chauvin and their victims named, Ch 12's
   verbs; all three convicted).
6. Unmet names: FIXED IN PART. Burgesses (Ch 20: "Virginia's lawmakers"), Conestoga (Ch 21: "killing twenty
   Conestoga people"), Gnadenhutten (Ch 22: "killing 96 Christian Lenape and Mohican people at Gnadenhutten in
   1782"). SKIPPED: Mabila and Arenal (read as places where the named men killed), Cepheid (the line says it is
   a star and what its blink shows).
7. Ch 6 covenants: FIXED ("rules called covenants ... to bar Black buyers").

Also done to keep the page and the closings word for word: four answers T-751 had edited on the page only
(Ch 21 Q3 Tulsa/Greenwood, Ch 22 Q3 Lieutenant William Calley, Ch 26 Q3 researchers must get consent, Ch 36 Q1
Abner Doubleday) were carried into their closings and hand-offs; Ch 21's "the chapter tells" became "the
chapter describes". The disasters hand-off's Ch 27 Q3 drift ("most went") was aligned. Left alone: hand-offs
for Ch 2 Q3, Ch 18 Q2 and Ch 30 Q2 lack the page's italics (formatting only, files not touched).
