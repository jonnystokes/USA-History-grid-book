# CHECKPOINT T-711 | health (Chapter 26), then disasters (Chapter 27) | review fix pass for R16

STATUS: DONE
BRIEF:  control/briefs/REVIEW-FIX.md
REVIEW: control/review/R16.md (25 findings for health, 25 for disasters)
FILES:  manuscript/health/part1-before-1800.md, part2-1800s.md, part3-1900s-and-today.md,
        control/backmatter/health.md,
        manuscript/disasters/part1-before-1800.md, part2-1800s.md, part3-1900s-and-today.md,
        control/backmatter/disasters.md
VERIFY: python tools/project_state.py --check health --stage prose
        python tools/project_state.py --check disasters --stage prose

## Health findings (numbered in the order of R16.md)

| # | era | finding (first words) | state | note |
|---|-----|-----------------------|-------|------|
| 1 | 1700 to 1750 | "The minister Cotton Mather led the" | fixed | opening anchor paraphrased (the box keeps Onesimus's words), Era 4 intro retelling cut, span keeps its one-line pointer |
| 2 | The 1600s | "In general, about 3 of every" | fixed | 3 in 10 called the general rate, a single epidemic could be higher or lower |
| 3 | 1700 to 1750 | "By the end of the epidemic," | fixed | span says 287 in all, most by Boylston; box says his 242-248 of the 287 |
| 4 | 1900 to 1950 | "The ambulance brought four sick men" | fixed | added her own line from the bank: the ambulance 'would bring us four live ones and take out four dead ones' |
| 5 | 1750 to 1800 | "They buried several hundred people and" | fixed | box now quotes their 'never received, nor never asked any compensation' (bank), inside their answer to Carey |
| 6 | 1750 to 1800 | "Jones and Allen's account does not" | fixed | paragraph split, Jones and Allen introduced where first named |
| 7 | 1800 to 1850 | "Over the next two months he" | fixed | Ann's baby named in each sentence, 'Kenny does not say whether Ann's baby lived' (bank), then the blame, plus the blamed nurse (bank); Frances's baby separate |
| 8 | 1800 to 1850 | "One count gives twelve women and" | fixed | seven known by name (Sims 3 + Bozeman 4), total not settled: twelve by one count, museum's six or seven unnamed |
| 9 | Before 1500 | "Their results support the idea that" | fixed | split into short sentences, DNA glossed, non-venereal glossed |
| 10 | 1800 to 1850 | "The operations went on for about" | fixed | CUT: box sentences that repeated the section (no drug, knees and elbows, enslaver sent her, the small hospital); kept the two holes, her age, the 1849 bladder closing, the unknown fate; Who line still says nothing for the pain |
| 11 | The 1500s | "Only 15 of the 80 Spaniards" | fixed | opens 'The islanders watched most of the Spaniards die', and the Native man's argument now ties back to it (bank wording) |
| 12 | 1900 to 1950 | "Accounts differ on when penicillin became" | fixed | short gloss at first use (Era 8 intro) and a few-word reminder in the Tuskegee span, the card's entry point; the 1942 span keeps the full definition |
| 13 | Opening | "Cotton Mather, a Boston minister, wrote" | fixed | smallpox glossed in the opening anchor (fever and blisters, often killed) |
| 14 | 1750 to 1800 | "When Caesar died, he owned an" | fixed | estate of 62 pounds added (bank); 'record does not give her name' checked against Butler 2021, the bank's own source, which calls her 'unidentified' |
| 15 | 1950 to 2000 | "Another doctor, Chester Southam, injected HeLa" | fixed | second pass: bank PATCH T-711 (Wikipedia, Southam): he did not tell the people he injected that the cells were cancer cells, prisoners hardly free to refuse, Regents' finding and a year's probation; two new box paragraphs; glossary adds Board of Regents, the finding words, probation |
| 16 | 1900 to 1950 | "By 1920: Army doctors had proved" | fixed | By 1920, By 1955, By 1965 moved out of the spans into their own unlabeled era blocks before the span headings (as in native-nations' 1600s), so none sits under a heading or in a skippable span |
| 17 | Opening | "Five minutes? Read" | fixed | card names both Tuskegee spans (775 + 351 words, about 5.6 minutes) |
| 18 | 1900 to 1950 | "Officials took her back to the" | fixed | second pass: bank PATCH T-711 (Wikipedia, Mallon): released February 1910 on a written promise not to cook; cook at Sloane Maternity Hospital as Mary Brown from October 1914; early 1915, 25 sick and 2 dead; found and sent back March 1915 |
| 19 | 1950 to 2000 | "In the Relf sisters' case, a" | fixed | sisters introduced in a clause, the two barred practices named; box not moved (stories stay in place) |
| 20 | 1950 to 2000 | "They awarded her $17,000. The same" | fixed | award tied to the taking of her children; consent finding set out on its own beside her statement |
| 21 | Before 1500 | "Smallpox, measles, influenza, mumps, chickenpox, cholera," | fixed | list split, the five the chapter follows first; all twelve names kept |
| 22 | 1900 to 1950 | "Only 16 of every 100 infected" | skipped | hard-subjects policy: the Tuskegee figures are the documented toll; cutting them is gist extraction |
| 23 | 1850 to 1900 | "When President James Garfield was shot" | fixed | Era 7 intro now says the doctors who examined his body found it full of infection |
| 24 | The 1600s | "Surgeons worked in the town too." | fixed | point first, rule years kept in one phrase, 1957 article year dropped (author still named); Era 5 restates the 1658 place |
| 25 | 1950 to 2000 | "Inspectors drove at high speed to" | fixed | Ku Klux Klan glossed at first use |

## Disasters findings (numbered in the order of R16.md)

| # | era | finding (first words) | state | note |
|---|-----|-----------------------|-------|------|
| 1 | The 1600s | "Another wave swept all four off" | fixed | the four on the rock named (Thacher, Mary, Avery, Avery's son), bank line 136 |
| 2 | The 1500s | "The colonists he led landed in" | fixed | CUT: box sentences repeating the section (landing, hurricane, seven ships); box now says Nanipacana was the first search party's town and Sauz led a second group of 200 (bank: two groups); '150 settlers to Havana' moved into the section; refusal paragraph gets a lead-in instead of a date |
| 3 | 1800 to 1850 | "What became of Charles. Charles Lamar" | fixed | CUT: the Wanderer paragraph (487 bought, about 409 lived, six trials) is told in full in Chapter 24; one callback sentence kept after Charles survives; box now ends on Rebecca |
| 4 | 1850 to 1900 | "Who got the food. Red Cross" | fixed | section now states the Red Cross's own count (about 30,000 homeless helped, most of them Black, bank) and that Tillman's collection followed press claims of 'discrimination against white sufferers' (bank); box agrees |
| 5 | Closer | "After many of these disasters someone" | fixed | Q1 answer now gives a verdict by group: went into use fast (gas smell), failed (1838 law, Triangle door, Eastland lifeboats, Katrina floodwalls), still being tested (Kerr County sirens, FEMA); backmatter Q1 answer matched |
| 6 | 1700 to 1750 | "New York officials said that enslaved" | fixed | second pass: bank PATCH T-711 copied from slavery-freedom (NY Courts) and crime-justice (Linder) banks, plus Wikipedia: historians disagree whether any plot existed; Burton offered an end to her service and money; witnesses promised their lives; Quack and Cuffee had no lawyers; pointer to Chapter 24 kept |
| 7 | 2000 to Today | "In an October 2024 report, federal" | fixed | 'accidental' glossed (no one set it on purpose); investigators found the downed lines started it but held no one responsible (bank, NPR); capital and inherited-homes sentences moved up and tied to what the fire destroyed |
| 8 | 1950 to 2000 | "A later study counted 692 deaths" | fixed | 692 is the whole summer (June 21 to August 10, bank); the study found some heat deaths were people who would have died later that summer (bank: mortality displacement) |
| 9 | 1900 to 1950 | "Isaac Cline took charge of the" | fixed | 1889 office described as the Galveston weather office under the Army's Signal Service, passed to the Weather Bureau in 1890 (Era 7 facts) |
| 10 | 1900 to 1950 | "They put that blame on three" | fixed | jury's reason given: the public policy blame went to the people the chief engineer answered to, the public among them (bank, verdict text) |
| 11 | 2000 to Today | "At Memorial Medical Center, 45 bodies" | fixed | setting added before the arrests: patients, visitors and workers trapped in the hospital during the flood (bank, PATCH T-320b) |
| 12 | 2000 to Today | "A 15-million-dollar repair had been approved" | fixed | second pass: bank PATCH T-711 (AP, NPR, Thornton Tomasetti, REBusiness Online, NIST): June 2022 settlement (nearly $1 billion from 20 defendants, none admitting wrongdoing, $96 million to owners), May 2022 state inspection and reserve law, NIST's June 2026 findings; criminal charges SEARCHED, NOT FOUND, so not stated; glossary adds defendants and NIST |
| 13 | 1900 to 1950 | "Between 6,000 and 8,000 people died" | fixed (part) | destruction figures moved to the flood paragraph; list explained as printed in early October, months before the last body was found; no figure cut |
| 14 | 1850 to 1900 | "The count of the dead was" | fixed (part) | split into 'The dead' and 'Who was left', final toll first; no count cut: the children, widows and orphans are the toll (hard-subjects policy) |
| 15 | The 1500s | "The Stahle team writes that the" | fixed | Stahle sentence now says hunger brought the Croatan to the empty town (bank: need for food) |
| 16 | 2000 to Today | "Inspectors of Tennessee's workplace safety agency" | fixed | agency's grounds added: the company had 'exercised reasonable diligence' (bank) |
| 17 | 2000 to Today | "In the week before July 18," | fixed | sirens now said to be six new ones by July 2026, three sounded to warn people when floods came again (bank, AP July 18, 2026) |
| 18 | 2000 to Today | "He gave no evidence." | fixed | 'He gave no evidence' replaced by the official count of 2,975, standing since August 28, 2018 (bank); section ends on the count |
| 19 | Closer | "Over ten eras, help after a" | fixed | What changed adds the Era 10 turn: FEMA slow at Katrina, failures admitted after Maria, Maui's sirens silent |
| 20 | 1950 to 2000 | "Six people were holding on to" | fixed | CUT: box's repeats of 'six people' and of the search for the man who passed the line; Windsor's own part and his words about that passenger kept |
| 21 | 2000 to Today | "Rinderknecht's federal trial ended on June" | fixed | CUT: date wall of the open case (June 26, August 19, October 22, 29, November 2, Judge Hwang, the dropped third charge) cut to where the case stands: hung jury 10 to 2 for not guilty, recharged with arson, pleaded not guilty, not convicted as of October 26, 2026 |
| 22 | 1850 to 1900 | "Clara Barton founded the American Red" | fixed | CUT: box's founding and Michigan sentences and the 1904 resignation, told in the section and in Chapter 26; callback to Chapter 26 added; Johnstown details and a Sea Islands line kept |
| 23 | The 1600s | "Tree rings show that the colonists" | fixed | CUT: salt-water and malnutrition sentences, told in Chapter 26, replaced by a callback naming Chapter 26; drought, relief fleet, hurricane and killing kept; 104/38 stays in the era intro; glossary 'malnutrition' removed |
| 24 | 1950 to 2000 | "Forecasters warned the whole Louisiana coast" | fixed | warning told once, in the span; era intro keeps only the toll; span opens on names, toll moved to the surge paragraph |
| 25 | 1900 to 1950 | "By the end of 1911: Thousands" | fixed | By the end of 1911, By 1929 and By 2018 moved out of the spans into their own unlabeled era blocks before the span headings; By 1929 no longer inside a skippable span |

## Log

<!-- file | what landed | validator | --punct -->
health/part1 | findings 1 2 3 5 6 9 11 13 14 17 21 24 | 0 errors | 0/0
health/part2 | findings 7 8 10 23 | 0 errors | 0/0
health/part3 | findings 4 12 16 18 19 20 25 (15, 22 skipped) | 0 errors | 0/0
health backmatter | smallpox first gloss moved to Before 1500 ('in general' added), DNA and Ku Klux Klan added
health --check prose: PASS (23,571 words, 23/23 stories verified, 0/0)
disasters/part1 | findings 1 2 6 15 23 | 0 errors | 0/0
disasters/part2 | findings 3 4 14 22 | 0 errors | 0/0
disasters/part3 | findings 5 7 8 9 10 11 12 13 16 17 18 19 20 21 24 25 | 0 errors | 0/0
disasters backmatter | 'malnutrition' removed (term cut with the Jamestown callback), Q1 answer matched to the closing
disasters --check prose: PASS (26,189 words, 12/12 stories verified, 0/0)
second pass (director's note) | health 15 18, disasters 6 12 | banks PATCHed (T-711) | health/part3, disasters/part1, disasters/part3: 0 errors, 0/0 | both --check PASS
