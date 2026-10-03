# Findings: migration part1-before-1800 (checker: sonnet, task T-548, 2026-10-02)

Second independent read. Bank slice read in full; whole bank searched before every "Not in bank".

| # | era | line | rule | severity | text (exact quote) | what is wrong | suggested repair | sure? |
|---|-----|------|------|----------|--------------------|---------------|------------------|-------|
| 1 | 1 | 25 | Defined Terms / Information Order | MINOR | "The main explanations are drought, floods, and a shortage of wood and food." | "drought" is used here, but its definition comes two paragraphs later (line 27). | Define at first use: "drought, which is a long time with little or no rain, floods, and a shortage of wood and food." Then drop the definition at line 27. | yes |
| 2 | 1 | 25 | Not in bank | MINOR | "Accounts differ about which of these mattered most." | Bank says only that there is "no single settled cause". "Which mattered most" is a narrower claim. | "No one cause is settled." | unsure (small stretch) |
| 3 | 1 | 27 | Claims That Can Be Checked | MINOR | "By about 1200 most of them had gone." | Bank says "largely abandoned by the end of the 1100s". "About 1200" is a nearby but different date. | "By the end of the 1100s most of them had gone." | unsure |
| 4 | 1 | 31 | Defined Terms | MINOR | "The Navajo call themselves the Diné. Their long move south is called the Athabascan migration, or the Dené migration." | Diné and Dené differ by one letter and the text does not say they are different words (Dené is the wider name for the language family). A reader will think it is a typo. | State the difference or use one: "...is called the Athabascan migration." | unsure (bank uses both without explaining) |
| 5 | 1 | 37 | The AI Cadence (triad, anaphora) | MINOR | "A family went where the fish were running, where the animals were, or where the plants were ready to pick." | Three parallel "where" clauses. The items are real, so it may be a list, but the repeated opening makes a beat. | "A family went to the rivers when the fish were running, followed the animals, and came back for the plants when they were ready to pick." (or cut one item) | unsure (real list) |
| 6 | 1 | 23 | Oversized Words | MINOR | "Some estimates put as many as 50,000 people" | "estimates" is a word to swap (also at line 76). | "Some guesses put the number as high as 50,000." | yes |
| 7 | 2 | 47 | Reader fit (sentence length) | MINOR | "Then, in 1598, Juan de Oñate led Spanish colonists, with their families, wagons and herds, north over land into what is now New Mexico, to stay." | 31 words, several ideas, and "north over land" is awkward. | "Then, in 1598, Juan de Oñate led Spanish colonists north into what is now New Mexico. They came with their families, wagons and herds, and they meant to stay." | yes |
| 8 | 2 | 53 | The AI Cadence (closing reversal) / Contrastive Negation | MINOR | "In the 1500s, horses did not yet change how people lived on the Great Plains. Horses changed life on the Plains in the next century." | A denial followed by a flip. The second sentence repeats the 1600s era summary. | Keep one: "Horses did not change life on the Great Plains until the 1600s." | yes |
| 9 | 2 | 53 | Oversized Words | MINOR | "Spanish expeditions then brought horses onto the mainland." | "expedition" is not explained at first use (also "Coronado's expedition"). | "Spanish explorers' parties then brought horses onto the mainland." or define: "an expedition, a group sent to explore." | yes |
| 10 | 2 | 61 | Not in bank | MINOR | "The people of Chaco Canyon had joined these Pueblo communities about 400 years earlier." | Bank gives 1140 and "end of the 1100s". "About 400 years" is the checker's arithmetic, and Chaco's people joined many Pueblo communities, not specifically the ones Oñate met. | "Pueblo peoples had lived there for centuries. Families from Chaco Canyon had joined them after the droughts of the 1100s." | unsure |
| 11 | 2 | 63 | Reader fit (sentence length) | MINOR | "In 1559 Tristan de Luna y Arellano brought about 1,500 soldiers, colonists, enslaved people and Aztec allies in 11 ships to Pensacola Bay, in what is now Florida." | 29 words. | Split after "Pensacola Bay": "...in 11 ships to Pensacola Bay, in what is now Florida. They included soldiers, colonists, enslaved people and Aztec allies." | yes |
| 12 | 2 | 72 | The AI Cadence (anaphora) | MINOR | "His column had about 400 men... It had 83 wagons and carts. It also drove more than 7,000 head of livestock" | Three consecutive sentences open with His column/It/It. | Merge: "His column had about 400 men, 130 of them with families, and 83 wagons and carts. It also drove more than 7,000 head of livestock." | yes |
| 13 | 2 | 72 | Not in bank | MINOR | "which means farm animals such as cattle and horses." | Bank gives "head of livestock" with no kinds. | "which means farm animals." | unsure (plain definition, but the examples are specific) |
| 14 | 2 | 74 | Not in bank | MINOR | "Enslaved people also walked in the column." | Bank says enslaved people were among the colonists, nothing about walking. | "Enslaved people were also part of the colony." | unsure |
| 15 | 2 | 76 | Not in bank | BLOCKING | "That council speaks for the leaders of the Pueblo nations." | Nothing in the bank says what the All Pueblo Council of Governors is or who it speaks for (grep whole bank: no description). | Delete, or add a sourced description to the bank first. | unsure (it may be plain background, but it is a specific claim about an organization) |
| 16 | 2 | 76 | Personification and Anthropomorphism | MAJOR | "it is the number the All Pueblo Council of Governors uses." | A council (institution) "uses" a number. Named people are not given. | "...and it is the number Pueblo leaders gave in a 2023 statement." (bank: APCG press release, Oct. 6, 2023) | yes |
| 17 | 2 | 76 | Reader fit (paragraph) | MINOR | The whole paragraph beginning "In December 1598 Oñate's nephew" | About 14 sentences carrying a raid, a rape, a battle, a count dispute and the council. Over the 3-6 sentence limit, and it buries the count dispute. | Split at "In January 1599" and at "Nobody counted". | yes |
| 18 | 2 | 78 | Personification and Anthropomorphism | MAJOR | "AP, NPR and the Pueblos say it was the right foot." | News outlets (AP, NPR) "say". Name the people. | "Reporters at AP and NPR, and Pueblo leaders, say it was the right foot." | yes |
| 19 | 2 | 78 | Personification and Anthropomorphism | MAJOR | "The National Park Service counts about 70 Acoma girls ... The Park Service says that probably none of them ever came home." | An agency counts and says. | "A National Park Service web page on the Camino Real states that about 70 Acoma girls were sent... and that probably none ever came home." | yes |
| 20 | 2 | 78 | Not in bank | MINOR | "Two historians who studied the records, Marc Simmons and John Kessell, doubt" | Bank does not say they "studied the records". It also says Simmons first wrote that the amputations took place and later came to doubt it. | "Two historians, Marc Simmons and John Kessell, doubt that the feet were ever cut off. Simmons had once written that they were." | unsure |
| 21 | 2 | 78 | Reader fit (sentence length) | MINOR | "In February 1599 Oñate sentenced the men over 25 to have a foot cut off and to be forced to work as slaves for twenty years." | 27 words, two punishments in one sentence. | "In February 1599 Oñate sentenced the men over 25 to have a foot cut off. He also sentenced them to twenty years as slaves." | yes |
| 22 | 3 | 94 | Hard subjects §2: Lossy summarization | MINOR | "The Pueblo peoples of what is now New Mexico rose up against Spanish rule." | The reader never learns why. The native-nations bank (line 88) has the 1675 arrests, whippings and hangings of Pueblo religious leaders. Not in this chapter's bank. | Add a sourced PATCH and one sentence, or leave as is. | unsure |
| 23 | 3 | 102 | Information Density | MINOR | "Riders from peoples such as the Comanche, Lakota and Cheyenne could follow the buffalo herds farther and faster than hunters on foot." | Repeats line 86 nearly word for word ("travel farther and faster than on foot, and they could follow the buffalo herds"). | Cut one of the two. | yes |
| 24 | 3 | 106 | Hard subjects §2: Euphemism | MINOR | "two English ministers left the colony of Massachusetts Bay" | Williams was ordered out (line 108 says so). "Left" is milder for him. | "two English ministers moved out of Massachusetts Bay, one by choice and one ordered out" or "Hooker left... and Roger Williams was ordered out." | unsure (line 108 corrects it) |
| 25 | 3 | 108 | Personification / Defined Terms | MINOR | "A deed is a paper that hands over land." | A paper "hands over". Same sentence repeats word for word at line 121. | "A deed is a signed paper that says land now belongs to someone else." Define once. | yes |
| 26 | 3 | 119 | Not in bank / Precise Words | MAJOR | "John Winthrop, the governor of Massachusetts Bay, wrote about the departure" | Bank says "Governor John Winthrop's journal". Winthrop was governor in other years, but Henry Vane was governor in May 1636 (the checker's own knowledge, not the bank's). | "John Winthrop, a leader of Massachusetts Bay, wrote about the departure in his journal on May 31, 1636" | unsure (matches the bank's title) |
| 27 | 4 | 133 | Not in bank | MINOR | "the Comanche moved in on horseback" | Bank (era 4) says only that the Comanche moved onto the southern Plains by the early 1700s. | "the Comanche moved onto the southern Plains." | unsure |
| 28 | 4 | 139 | Oversized Words / Defined Terms | MINOR | "The Scots-Irish were Protestant families from Scotland" | "Protestant" is not explained. | "Protestant (a kind of Christian) families from Scotland" | yes |
| 29 | 4 | 151 | Personification and Anthropomorphism | MAJOR | "North Carolina's state history office counts 950 Native people killed or captured" | An office counts. Also the bank source is the NC Department of Natural and Cultural Resources, not a "history office". | "A North Carolina state history page lists 950 Native people killed or captured at Neoheroka. It lists about 1,000 Tuscarora sold into slavery during the whole war." | yes |
| 30 | 4 | 153 | Not in bank | MINOR | "which means the Oneida spoke for them and backed their joining." | Explanation of "sponsored" is not in the bank. | "The Oneida nation sponsored them, meaning they helped the Tuscarora join the Haudenosaunee league." (or leave undefined) | unsure |
| 31 | 4 | 159 | Root Metaphors | MINOR | "The Handbook of Texas, a history reference, says that by 1700" | A document element "says". Approved verbs: states, records, describes. | "The Handbook of Texas, a history reference, states that..." | yes |
| 32 | 5 | 167-169 | Chronology (amendment §6) | MINOR | Era summary runs 1775, then 1783, then "Farther north... 1755", then 1785 and 1787 | Dates out of order. | Put the Acadians (1755) first, or add "Earlier, in 1755,". | yes |
| 33 | 5 | 173 | Not in bank | MINOR | "Charles Lawrence was the colony's lieutenant governor, the top British official there." | Bank gives only the title. A lieutenant governor ranks below a governor, so "top" may be wrong. | "...the colony's lieutenant governor, a high British official there." | unsure |
| 34 | 5 | 177 | Hard subjects §2: Lossy summarization | MAJOR | "Soldiers would surround the churches on a Sunday morning ... Then they would break the earth walls ... and burn their houses and crops." | Only the plan is told, in "would" form. The reader cannot tell whether the burning happened. The bank has only Morris's plan (Marsh), nothing on what was carried out. | State what the record shows and mark the rest: "Morris devised a plan... The bank does not confirm..." must be written from the record side, or add a sourced PATCH on what was burned. | unsure (bank gap) |
| 35 | 5 | 179 | Oversized Words | MINOR | "In French the expulsion is called Le Grand Derangement" | "expulsion" is a big word and is not explained here. | "In French the forced removal is called Le Grand Derangement, the great upheaval." | yes |
| 36 | 5 | 181 | Claims That Can Be Checked | MINOR | "Other sources say as many as half of those forced out died." | "Other sources" names no one. Bank is also vague here ("some sources"). | Name the source if one can be found, else "Some counts say as many as half." | unsure |
| 37 | 5 | 185 | Passives with a Missing or False Agent | MINOR | "seven ships paid for by the Spanish government carried 1,596 Acadians" | An institution pays. | "Spanish officials paid for seven ships that carried 1,596 Acadians from Nantes, in France, to Louisiana." | yes |
| 38 | 5 | 198 | Personification and Anthropomorphism | MAJOR | "That year the Treaty of Paris, a peace agreement, ended the war between Britain and France." | A treaty ends a war (a law acting in the world). | "That year Britain and France signed the Treaty of Paris, a peace agreement that ended their war." | yes |
| 39 | 5 | 200 | Reader fit (sentence length) | MINOR | "On April 8, 1765, colonial officials named him a militia captain, an officer over citizen soldiers, and the commander of the" | 27 words. | Split after "citizen soldiers". | yes |
| 40 | 5 | 202 | Reification | MINOR | "The title honors a person who mattered in Canada's history." | A title honors. | "A National Historic Person is someone the Canadian government names as important to Canada's history." | yes |
| 41 | 5 | 208 | Not in bank | MINOR | "Transylvania Company, a business that bought land to sell to settlers." | Bank does not describe the company's business. | Cut the clause, or add a sourced fact. | unsure |
| 42 | 5 | 210 | Personification / Root Metaphors | MINOR | "The Tennessee Encyclopedia calls the Cherokee claim the strongest of these." | A document "calls". | "The Tennessee Encyclopedia describes the Cherokee claim as the strongest of these." | yes |
| 43 | 5 | 210 | Not in bank | MINOR | "It was an order from the British king that banned private buyers from buying Native land." | Bank says the Royal Proclamation "banned private purchase of Native land", with no "order from the king". Also "banned buyers from buying" repeats. | "It banned private purchase of Native land." | unsure |
| 44 | 5 | 214 | Hard subjects §2: Gist extraction | MINOR | "In the 1790s those nations and the settlers fought each other." | One plain line for a war in which the bank has no figures. The bank hands the war to another chapter (war, native-nations). | Keep if hand-off is intended. | unsure |
| 45 | 5 | 216 | Reification | MINOR | "That grid is why so much of the American countryside is laid out in squares today." | "That grid is why" equates a thing with a reason. | "Because of that grid, much of the American countryside is laid out in squares today." | yes |

## Counts

By severity: BLOCKING 1, MAJOR 7 (items 16, 18, 19, 26, 29, 34, 38), MINOR 37. Total 45.

By rule: Personification and Anthropomorphism 5 (plus related Root Metaphors, Passives, Reification 5 more); Not in bank 10; Reader fit / Oversized Words 11; Cadence/Information Density 4; Hard subjects 4; Other 6.

Eras with no findings: none. All five eras have at least one MINOR.

Pass 6: no em dashes, no semicolons, records only inside stories, all stories `verified`, all eras `written`.

## Tool output

```
=== part1-before-1800.md : 1 chapters, 3 stories, 0 errors
manuscript/migration/part1-before-1800.md: emdash=0 semicolon=0
```

## Fixer verdicts (T-619, 2026-10-03)

The `fixer` column for the table above, keyed by finding #.

| # | fixer |
|---|---|
| 1 | FIXED: drought defined at first use, later definition dropped |
| 2 | FIXED: "No single cause has been settled." |
| 3 | FIXED: "By the end of the 1100s" |
| 4 | FIXED: "or the Dené migration" cut (unexplained near-duplicate of Diné) |
| 5 | FIXED: one sentence listing fishing places, hunting grounds and plant spots, no repeated "where" |
| 6 | REJECTED: "estimate" is an everyday school-math word, and the alternatives ("guesses") misstate the evidence |
| 7 | FIXED: split as suggested |
| 8 | FIXED: one sentence, "in the next century, the 1600s" |
| 9 | FIXED: expedition defined at first use ("groups of men sent out to explore") |
| 10 | FIXED: "Families from Chaco Canyon had joined the Pueblo communities after the droughts of the 1100s, about 400 years earlier." |
| 11 | FIXED: split |
| 12 | FIXED: merged |
| 13 | FIXED: "farm animals. Horses were among them." (horses in bank era 2) |
| 14 | REJECTED: bank SEARCHED, NOT FOUND (T-244) gives the wording "Enslaved people walked in the column" |
| 15 | FIXED: PATCH 2026-10-03 (T-619) from apcg.org; prose now says its members are the 20 Pueblo nations of New Mexico and Texas |
| 16 | FIXED: "Pueblo leaders gave that number in a 2023 statement from the All Pueblo Council of Governors" |
| 17 | FIXED: paragraph split into four |
| 18 | FIXED: "Reporters for AP and NPR, and Pueblo leaders, say" |
| 19 | FIXED: "A National Park Service page on the Camino Real states ... The same page states" |
| 20 | FIXED: "studied the records" cut, "Simmons had once written that they were" added |
| 21 | FIXED: split |
| 22 | FIXED: PATCH 2026-10-03 (T-619) copies Treviño's 1675 arrests, hangings and whippings from the native-nations bank; one short paragraph added |
| 23 | FIXED: repeated sentence cut, the change kept with the nations named |
| 24 | FIXED: "Thomas Hooker chose to go ... Roger Williams, did not choose" |
| 25 | FIXED: "a signed paper that says who owns a piece of land", defined once |
| 26 | FIXED: "a leader of Massachusetts Bay" |
| 27 | REJECTED: bank era 3 lists the Comanche among the mounted peoples |
| 28 | FIXED: Protestant defined |
| 29 | FIXED: "History pages from North Carolina's state government list" |
| 30 | FIXED: definition trimmed to "the Oneida backed their joining" |
| 31 | FIXED: "states" |
| 32 | FIXED: era summary reordered, 1755 first |
| 33 | FIXED: "one of the top British officials there" |
| 34 | FIXED: PATCH 2026-10-03 (T-619), Landscape of Grand Pré: soldiers burned many houses, barns and churches, about 700 buildings around the Minas Basin; stated after the plan |
| 35 | FIXED: "forced removal" |
| 36 | FIXED: "Other counts put the dead at as many as half" |
| 37 | FIXED: Spanish officials paid |
| 38 | FIXED: Britain and France signed |
| 39 | FIXED: split |
| 40 | FIXED: "Canadian officials give that title to people who were important in Canada's history." |
| 41 | FIXED: PATCH 2026-10-03 (T-619), NCpedia: "a business formed to buy up wild land and open it to settlers" |
| 42 | FIXED: "describes" |
| 43 | FIXED: "order from the British king" cut |
| 44 | REJECTED: the war is told in `war` and `native-nations`, and the bank has no more for this chapter |
| 45 | FIXED: "Because of that grid" |
| F1 | found by fixer, era 4, softening: "Apache groups there moved south" (bank: "fled southward") -> "many Apache there fled south"; "Comanche moved in on horseback and took control" |
| F2 | found by fixer, era 4, #45: "The records do not name who bought them" (bank: the sources checked) -> "Those state pages do not name who bought them." |
| F3 | found by fixer, era 3, #45: "The surviving sources do not say what Sequassen's people received" -> "The histories of the deed do not say" |
| F4 | found by fixer, era 3, personification: "what Native nations have long said" -> "what Native people have long said in their nations' own histories" |
| F5 | found by fixer, era 2, personification: "The Pueblos count 60 children" -> "Pueblo leaders count" |

Counts: FIXED 41, REJECTED 4, NEEDS-RESEARCH 0, found by fixer 5.
