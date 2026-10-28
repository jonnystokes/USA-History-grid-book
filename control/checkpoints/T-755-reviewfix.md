# T-755 review fix: People (manuscript/_backmatter/04-people.md)

Findings: control/review/R25.md, section "## People" (15 findings). Every fix checked against the
chapter's story box. Only 04-people.md edited.

## Findings

1. Hugh Thompson Jr.: FIXED. Line now says he landed to stop the soldiers from killing unarmed
   villagers (Ch 22 box). Glossary My Lai entry: skipped, not my file.
2. Harms with no actor: FIXED all seven named lines from their chapters. Frank James (Massachusetts
   officials planning the Pilgrims' 350th anniversary stopped his speech, Ch 37), Elias Boudinot (a
   group of Cherokee who supported John Ross stabbed him, Ch 31), Estevanico twice (the people of
   Hawikuh killed him, Ch 1 and Ch 24), Fannie Lou Hamer (state highway patrolmen made two prisoners
   beat her, Ch 25), Martin Luther King Jr. (James Earl Ray pleaded guilty, Ch 25), Radium Girls
   (supervisors told them to lip-point and said the paint was safe, Ch 13).
3. Thomas Hancock era: SKIPPED. His box sits in Ch 19's 1700 to 1750 era, so the label is where the
   reader finds him.
4. Cesar Chavez: FIXED. Names The New York Times, Debra Rojas and Ana Murguia, and Huerta's own
   statement (Ch 14). Note beside the films: skipped, Movies page is not my file.
5. Mélisande Short-Colomb: FIXED. GU272 glossed from Ch 24 (272 enslaved people the Maryland Jesuits
   sold in 1838, in part to keep Georgetown College going).
6. Cristian Pavón Pineda: FIXED, but not as the reader guessed. Ch 10 says early reports blamed the
   cold and police later said an autopsy found carbon monoxide poisoning. The line says both.
7. Carrie Buck and the Relf sisters: FIXED. Both lines now say sterilized meant an operation so they
   could never have children, and name who did it (Dr. John H. Bell, Ch 25; surgeons, Ch 26).
   Also "the Supreme Court allowed" became "the Supreme Court's justices allowed".
8. Charles Willson Peale: FIXED. A Maryland planter paid him with two enslaved people, Scarborough
   and Lucy (Ch 32).
9. Franklin and other repeated names: SKIPPED. The format rule keeps one line per person per
   chapter, and each line already carries its own role.
10. Enslavers not named: FIXED where the chapter says it: Jefferson (Ch 12), Washington (Ch 20),
    Eliza Lucas Pinckney (Ch 15 and Ch 16). SKIPPED Washington's Ch 22 and Ch 35 lines: those
    chapters do not say it.
11. Levi Savage: FIXED. Sub-captain, one of the leaders under the captain (Ch 5).
12. José Luis Vaello Madero: FIXED. Reason added from Ch 23. Also "the United States government
    sued" became "Lawyers for the United States government sued".
13. Harriot and Hariot: PARTLY FIXED. Joining them breaks the format rule (one reference per line,
    each name matches its own box). Instead the Hariot line now comes first (A to Z), both lines give
    the other spelling in brackets, and both call him a mathematician (Ch 26 box: mathematician and
    scientist).
14. Columbus and Dave era labels: SKIPPED. Both boxes sit in the eras the lines give (Ch 1 The
    1500s, Ch 32 1800 to 1850).
15. Alex Haley: FIXED. Split into two sentences, naming who challenged the research (experts who
    trace family histories through records, Ch 24).

## Checks

- Entries 734 before and after, lines 809 before and after.
- Every bullet ends with exactly one (Chapter N, era) reference (format script in scratch).
- All 734 lines link to a story box with the build's own matcher (read-only, no build run).
- `python tools/project_state.py --punct manuscript/_backmatter/04-people.md`:
  emdash=0 semicolon=0

Status: DONE.
