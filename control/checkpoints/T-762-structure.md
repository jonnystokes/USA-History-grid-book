# CHECKPOINT T-762 | immigration (Chapter 4), migration (Chapter 5) | structure pass + director fact items

STATUS: DONE (immigration PASS, migration PASS)
BRIEF:  control/briefs/STRUCTURE-PASS.md
FROM:   control/checkpoints/T-723-reviewfix.md, control/review/R03.md
FILES:  manuscript/immigration/part2-1800s.md, manuscript/migration/part2-1800s.md,
        manuscript/migration/part3-1900s-and-today.md, research/research-migration.md (3 PATCHes)
SCRATCH: C:\Users\jon\AppData\Local\Temp\claude\C--Users-jon-Projects\c3422736-ab9a-4784-b707-6df665469603\scratchpad\T-762\

## Findings the old grid rule blocked or forced a workaround on

| chapter, finding | state | why, in a few words |
|---|---|---|
| Ch 4 #15 (R03 #17), era 7, "Jews from the Russian Empire, and others from southern and eastern Europe" | done: split | heading could not change before; the span opened on the others and ran 600 words on the Jews. Now "Italians, Poles, Hungarians and Greeks" (why they came, many went home) and "Jews from the Russian Empire" (pogroms, May Laws). The bridge sentence became the second span's opener, reworded to stand alone ("came running from riots ... Unlike many of the peasants who came to earn money, they came as families and planned to stay"). No card line names either label. |
| Ch 5 #3 (R03 #3), era 7, Plains example inside "The Long Walk of the Navajo, 1864" | done: split | T-723 had to put the Lakota paragraph under a Navajo label with the lead-in "On the Plains."; now its own span "Reservations on the Plains", lead-in cut, first sentence says "many nations of the Great Plains" (bank line 270), paragraph split at its seam (was 105 words). No card line names it. |
| Ch 4 #11 (R03 #13), era 8, "At home." in "Eugenics and the men behind the 1924 law" | left as is | the bridge is the reviewer's own fix, not a workaround; the sterilization part is Laughlin's model law, so the label still covers it, and a span of its own would set an off-subject topic apart in Chapter 4 |
| Ch 5 #18 (R03 #18), era 7, "Still on the trail." before the Amelia Stewart Knight box | left as is | the bridge still helps; Knight (1853) is the era's earliest event and the handcart span after her continues the trail, so no better place in era 7. The diary line is still missing: not in the bank and not a director item |
| Ch 5 #14, #15; Ch 4 #19 (pointers back to the opening or to the next box) | left as is | marked fixed by T-723; the pointers still help and no move improves them |

## Director fact items

| item | state | source, and what changed |
|---|---|---|
| 1a. Ch 5 #1, the reason officials stated for the Japanese American removal | done | No bank had it (checked government-politics T-315, rights-movements T-262c/T-639, war, crime-justice, immigration). Found: the order's own opening words (National Archives transcript of EO 9066) and the 1983 commission's "not justified by military necessity" (House History, "Long Road to Redress"). PATCH in research-migration.md section 8. Prose: new "The reason given." paragraph (protection against spying and damage done on purpose; the order identifies no group), DeWitt's orders "aimed at one group", and the 1983 sentence now gives "was not justified by military necessity," glossed. Plain words used instead of "espionage" and "sabotage", so the glossary's "(Chapter 31)" lines stay right. |
| 1b. Ch 5 #17, Relocation's stated aim (the dispatch names #17 with #1) | done | National Archives, "Bureau of Indian Affairs Records: Urban Relocation" and the Archives lesson page. PATCH in section 9. Prose: new "The aim." paragraph (1951 offices in Denver, Salt Lake City and Los Angeles to help people find jobs in cities; the Archives calls Relocation part of termination; termination's backers aimed to make Native people live like most other Americans). |
| 2. Ch 5 #10, Philadelphia "500 percent" and New York 152,000 to 328,000 | done | Census Bureau Working Paper 76 (Gibson and Jung, 2005), Tables 14, 23, 33, 39. Chicago +148% and Detroit +611% stand. Philadelphia 1910-1920 was +59% (84,459 to 134,229), not 500. New York 152,467 to 327,706 is 1920 to 1930; 1910-1920 was +66%. PATCH with the correction in section 8. Prose: "New York's and Philadelphia's grew by more than half" (1910-1920) and "New York's Black population more than doubled" in the 1920s, "from about 152,000 to about 328,000". Philadelphia's 500 percent stays out. |

## Outside my files (for the director, not changed)
- manuscript/city-building/part3-1900s-and-today.md line 101: "Philadelphia's rose about 500 percent, and New York's roughly doubled." Wrong by the Census tables (see the T-762 PATCH in research-migration.md). research/research-city-building.md line 325 cites the migration bank for the same figures. outlines/migration.md line 160 and outlines/BOOK-OUTLINE.md line 1583 carry them too.
- Back matter: no line made wrong (glossary, timeline, answers and control/backmatter checked for the changed labels and figures).

## Checks
- validate_grid --part: 0 errors on the three saved files. --punct: 0/0 on each.
- Card names still resolve (build's own index_chapter, run read-only): both cards' "Five minutes?" and "Can skip:" names link. Card times by the build's rule: immigration 100 (card 100), migration 75 (card 75).
- PASS immigration / prose (manuscript=21167w, validator 0 errors, emdash=0 semicolon=0). PASS migration / prose (manuscript=16498w, validator 0 errors, emdash=0 semicolon=0). PASS migration / patch and / research.
- No cuts.
