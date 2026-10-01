# Findings: transportation part1-before-1800 (checker: sonnet, task T-363, 2026-09-30)
| # | era | line | rule | severity | text (exact quote) | what is wrong | suggested repair | sure? |
|---|-----|------|------|----------|--------------------|---------------|------------------|-------|
| 1 | 1 | 19 | Metadiscourse / Reification | MINOR | "Historians explain the missing wheel this way." | A lead-in that announces the next sentence. "The missing wheel" is also an abstraction, and the same paragraph says Mesoamerican toys had wheels. | Start with the fact: "A cart needs an animal to pull it, and north of Mexico there was none." | yes |
| 2 | 1 | 23 | Not in bank | MINOR | "Native nations built and kept up long trails" | The bank says Native nations followed, widened and kept up the Natchez Trace and that the Great Trail was their footpath network. It does not say they built the trails in general. | "Native nations used, widened and kept up long trails, and many of those trails had names." | unsure (a mild generalization) |
| 3 | 1 | 23 | Oversized Words and Nominalization (hard word) | MINOR | "Algonquian-speaking and Iroquoian-speaking peoples" | Two language-family names an 11-year-old does not know, with no explanation. | "Peoples who spoke Algonquian or Iroquoian languages (two large families of related languages) used it..." | yes |
| 4 | 1 | 23 | Not in bank | MINOR | "the mid-Atlantic coast" | The bank says "the mid-Atlantic," not the coast. "Mid-Atlantic" is also an undefined term. | "between New England, the middle of the Atlantic states and the Great Lakes" | unsure |
| 5 | 1 | 25 | AI Cadence (anaphora) | MINOR | "for trade, for travel, for war, and for diplomacy" | Four items in a row, each opening with "for." The bank lists the four uses, so they carry facts, but the "for" repeat is a beat. | "They used them to trade, to travel, to fight and to hold talks between nations." | unsure |
| 6 | 1 | 27 | Unanchored Comparatives | MINOR | "People carried goods very long distances" | "Very long" gives no figure. The next sentence has one (Great Lakes to the Gulf Coast). | Merge: "As early as 6000 BC, people carried seashells and copper between the Great Lakes and the coast of the Gulf of Mexico." | yes |
| 7 | 1 | 31 | Not in bank | MINOR | "People built two main kinds of boat" | The bank lists dugouts and birchbark canoes but does not say they were the only two main kinds. | "People built dugout canoes and birchbark canoes for the rivers and lakes." | unsure |
| 8 | 1 | 31 | Oversized Words (hard word) | MINOR | "the Eastern Woodlands and the Southeast" | Region names with no explanation. | "the forests of the eastern part of the continent and the Southeast" | unsure (proper region names) |
| 9 | 1 | 33 | Not in bank | MINOR | "in every size from one-person boats up to large canoes" | The bank says the canoes ranged from solo boats to large freight canoes, not "every size." | "from one-person boats up to large canoes that carried freight" | unsure |

## Era 1 passes
Pass 2: no harm told, nothing to check. Pass 3: no false actors. Pass 6: clean.

| # | era | line | rule | severity | text (exact quote) | what is wrong | suggested repair | sure? |
|---|-----|------|------|----------|--------------------|---------------|------------------|-------|
| 10 | 2 | 45 | Not in bank / date contradicts another date | BLOCKING | "Spanish sailors brought horses back to the Americas in the 1500s." | The bank and line 49 date Columbus's horses to 1493, which is the 1400s. Only the mainland horses (1540) are in the 1500s. "Sailors" is also not in the bank (Columbus, then soldiers with Coronado). | "Spanish ships carried horses back to the Americas in 1493, and Spanish soldiers took them onto the mainland of North America in 1540." | yes |
| 11 | 2 | 45 | Not in bank | MINOR | "Spanish colonists built a port at St. Augustine" | The bank says Menéndez landed at Seloy and made the chief's house a fort, and that St. Augustine is a port. It does not say they built a port. | "In 1565 Spanish colonists settled at St. Augustine, in Florida, in a town of the Timucua people, and it became a port." | unsure |
| 12 | 2 | 45 | Not in bank | MINOR | "Most people living here still traveled on foot, by canoe and along trails." | No figure or source in the bank for what "most people" did in the 1500s. | Cut it, or "Native nations continued to travel on foot, by canoe and along trails." (bank has no source for 1500s travel) | unsure |
| 13 | 2 | 45 | AI Cadence (anaphora) | MINOR | "In 1565 Spanish colonists built ... In 1598 Spanish colonists led by" | Two sentences open with the same words. | Merge: "In 1565 Spanish colonists settled at St. Augustine ..., and in 1598 colonists led by Juan de Oñate brought 83 wagons and carts north into Pueblo land." | unsure |
| 14 | 2 | 51 | Hard subjects §2: Euphemism / Downplaying | MAJOR | "He wrote that the Timucua received the Spanish well and gave them a large house belonging to their chief" | The bank states in its own words that "the Spanish took over the chief's council house and made it their first fort." The prose tells only the Spanish priest's side (that it was given) and never says the Spanish took over the chief's house. | "Father ... wrote that the Timucua received the Spanish well and gave them a large house belonging to their chief. The Spanish took over the chief's house, and two captains, Patiño and San Vicente, had a ditch, a moat and a wall of earth built around it. It became the first Spanish fort there." | unsure (the bank's "took over" is its own summary, with the priest's letter as the only account) |
| 15 | 2 | 51 | Passives with a Missing or False Agent | MINOR | "had a ditch, a moat and a wall of earth built around the house" | Who dug and built is not named, and the bank does not say. | "...had workers build" is not in the bank. Either keep and add "The record does not say who did the digging," or leave it. | unsure |
| 16 | 2 | 53 | Fourth wall / The Reader | MINOR | "Sources give different counts of the people who came with Menéndez." | "Sources" can read as the book's research sources. Guideline 4 says to state that the accounts differ. | "Accounts differ on how many people came with Menéndez." | unsure |
| 17 | 2 | 53 | The Teaching Point | MINOR | "St. Augustine is the oldest European settlement and port in the continental United States" | The paragraph does two jobs (the count dispute, then the port's rank) and the rank sentence is 23 words. "Continental" is a big word. | Split into two paragraphs. "St. Augustine is the oldest European settlement and port on the mainland of the United States that people have lived in without a break." | yes |
| 18 | 2 | 49 | Oversized Words | MINOR | "Coronado's expedition of 1540 to 1542" | "Expedition" is a big word and "Coronado" is not introduced. | "Francisco Vásquez de Coronado's march north in 1540 to 1542" (the name is not in the bank, so "the Spanish army led by Coronado" is safer). | unsure |
| 19 | 2 | 55 | Oversized Words (hard word) | MINOR | "the column reached the Rio Grande" | "Column" in the sense of a line of travelers is not defined. | "the line of wagons and people reached the Rio Grande" | yes |
| 20 | 2 | 55 | Information Order | MINOR | "Oñate claimed New Mexico for Spain in a ceremony the Spanish called La Toma" | The claim comes a paragraph before the sentence saying Pueblo peoples already lived there, so a reader meets "claimed for Spain" with no word on who lived on the land. | Add to the same paragraph: "The Pueblo peoples already lived there." | unsure |

## Era 2 passes
Pass 6: clean.

| # | era | line | rule | severity | text (exact quote) | what is wrong | suggested repair | sure? |
|---|-----|------|------|----------|--------------------|---------------|------------------|-------|
| 21 | 3 | 65 | Not in bank | MINOR | "In 1631 the colony's leaders licensed a rowed ferry" | Which colony is not named, and the bank says the Court of Assistants chartered it. | "In 1631 the Massachusetts Court of Assistants gave Edward Converse a license to run a rowed ferry across Boston's harbor." | unsure |
| 22 | 3 | 65 | Not in bank | MINOR | "along paths that Native people had made long before" | The bank backs this for the lower road (Pequot Path) and the upper road, but the upper-road line is marked "unconfirmed: search summary only," and the first rider in 1673 took the upper route. | Keep, or "along paths that Native people had used long before." Fixer to decide. | unsure |
| 23 | 3 | 71 | Not in bank | MINOR | "Much of that road followed Native paths." | The bank says "Parts followed existing Native paths." "Much" widens the range. | "Parts of that road followed Native paths." | unsure |
| 24 | 3 | 82 | Personification and Anthropomorphism | MAJOR | "the court record that licensed it still exists" | A record cannot license anything. The court's members did. | "...and the record of the court order that licensed it still exists." Or "The Massachusetts Court of Assistants licensed it, and the court's record still exists." | yes |
| 25 | 3 | 84 | Defined Terms | MINOR | "first chartered public transportation" (and "licensed," lines 65, 79, 82) | The story says "licensed" and "chartered" for the same act. The bank says "chartered." | Pick one term and use it in the era summary, the Who line and the text. | unsure |
| 26 | 3 | 86 | Oversized Words (hard word) | MINOR | "one of the English Protestants who settled Massachusetts" | "Puritan" is defined with another hard word, "Protestants." | "a Puritan, a member of a strict English Christian group that settled Massachusetts" | unsure |

## Era 3 passes
Pass 2: no harm told, and the bank assigns the taking of Pequot, Narragansett and Nipmuc land to other chapters. The prose names who made the paths. Pass 6: clean.

| # | era | line | rule | severity | text (exact quote) | what is wrong | suggested repair | sure? |
|---|-----|------|------|----------|--------------------|---------------|------------------|-------|
| 27 | 4 | 94 | Not in bank | BLOCKING | "The first stage lines started carrying passengers in New Jersey in 1706." | The bank has a 1706 patent (legal right) to Hugh Huddy, not a start of passenger service. "First" is not in the bank. Line 108 says only that officials gave a patent. | "In 1706 New Jersey officials gave Hugh Huddy a patent to run a stage line." | unsure (bank heading says "Stage lines begin") |
| 28 | 4 | 100 | Not in bank | MINOR | "until the railroads came" | The bank says the wagon was dominant "into the railroad era." "Until" says it stopped. | "People in the East used it as their main freight wagon into the age of railroads." | unsure |
| 29 | 4 | 100 | Not in bank | MINOR | "to haul farm goods to Philadelphia" (line 94) | The bank says freight, not farm goods. | "to haul freight to Philadelphia" | unsure |
| 30 | 4 | 102 | Oversized Words | MINOR | "a mob of men from Paxton township" | "Township" is a hard word. | "from the town of Paxton" or "from Paxton, a township (a local area of government)" | unsure |
| 31 | 4 | 102 | Not in bank | MINOR | "about 57 of these men attacked" | Only one source (Encyclopedia.com) gives 57. The bank's other sources give no count. The prose states it as the number. | "About 57 of these men attacked Conestoga Manor, by one count." | unsure |
| 32 | 4 | 104 | Oversized Words (hard word) | MINOR | "locked the Conestoga survivors in the county workhouse" | "Workhouse" is not explained, and the reader will not know it was a jail-like building. | "...in the county workhouse, a building used as a jail" (the bank does not say what it was used for, so check before keeping) | unsure |
| 33 | 4 | 104 | Fourth wall / The Reader | MINOR | "Sources count 14 or 16 people killed that day." and line 102 "(sources give both dates)" | "Sources" can read as the book's research. Guideline 4 says to state that the accounts differ. | "Accounts count 14 or 16 people killed that day." and "(accounts give both dates)" | unsure |
| 34 | 4 | 112 | Hard subjects §2: Minimization / Lossy summarization | MAJOR | "Iroquois leaders gave up their use of the path and their claims in the Shenandoah Valley." | Land taken is stated with no recipient and no mention that the two sides understood the treaty differently. The bank records that the Iroquois understood they gave up only the valley east of the Alleghenies, while the Virginians claimed more, including Ohio Valley land. | "In the Treaty of Lancaster of 1744, Iroquois leaders and officials of Virginia, Maryland and Pennsylvania agreed that the Iroquois would give up their use of the path and their claims in the Shenandoah Valley. The two sides did not agree on how much land that covered. The Iroquois understood it as the valley east of the Allegheny Mountains. The Virginians claimed more, including land in the Ohio Valley." | unsure (the bank marks the signers and the dispute "unconfirmed: search summary only") |
| 35 | 4 | 112 | Fourth wall / The Reader | MINOR | "Sources give its length as about 730 miles or almost 800 miles" | "Sources" as in the book's research. | "Accounts give its length as about 730 miles or almost 800 miles, depending on where the count ends." | unsure |
| 36 | 4 | 112 | The Teaching Point | MINOR | "The Great Wagon Road ran from Philadelphia ... In the Treaty of Lancaster of 1744" | One paragraph holds the road's route, its length, its use, the Native path under it and a treaty. | Split in two: the road's route and length, then the Native path and the treaty. | unsure |
| 37 | 4 | 114 | Not in bank | MINOR | "He called out the "Labouring Male Titheables" who lived on or near the road." | The bank's quote says he "was usually assigned all" of them. "Called out" and "all" without "usually" change the claim. | "The overseer was usually assigned all the "Labouring Male Titheables" who lived on or near the road." | unsure |
| 38 | 4 | 114 | Claims That Can Be Checked / Hard subjects §2: Minimization | MAJOR | "These men brought their own tools, wagons and teams of animals" | "These men" includes the enslaved men named one sentence earlier, who owned no wagons. The bank's quote is about tithables as a group, and a search summary says the head of the household paid the tax for everyone in it. The prose gives enslaved men tools and wagons and hides who forced them to work. | "The county court's orders required tithables to supply their own tools, wagons and teams, and to work six days a year on the roads. Enslaved men worked the road under these orders. The records do not say whether their owners supplied the tools and teams." (check the last sentence against the bank before keeping) | unsure |
| 39 | 4 | 114 | Not in bank / softening | MINOR | "they included free men and enslaved men 16 and older" | The bank (Virginia Places) says enslaved women 16 and older were also taxed. The prose lists only men, so the reader thinks tithables were only men. | "They included free men 16 and older and enslaved men and women 16 and older. The road work fell on the men." | unsure |
| 40 | 4 | 114 | Oversized Words (hard word) | MINOR | "Tithables were the people counted for a tax on each person" | "Tithables" and "titheables" are two spellings, one in quotes. "Overseer" and "highways" are fine. The definition is correct. Fine to keep. | Optional: "head tax" for "a tax on each person." | unsure |
| 41 | 4 | 123 | Oversized Words | MINOR | "an eyewitness record" (line 125) | "Eyewitness" is fine but the bank's "best" is dropped (good). No change needed. | none | n/a |

## Era 4 passes
Pass 2: the Paxton killings are told plainly (killed, three men, two women and a boy) with actors named. Pass 6: clean.

| # | era | line | rule | severity | text (exact quote) | what is wrong | suggested repair | sure? |
|---|-----|------|------|----------|--------------------|---------------|------------------|-------|
| 42 | 5 | 133 | Not in bank | MINOR | "After 1750, investors began paying to build roads" | The bank dates the first turnpike to 1792. Nothing in the bank puts investors' road-paying at 1750. | "In 1792, investors began paying to build roads and charging travelers a fee to use them." | unsure |
| 43 | 5 | 133 | Oversized Words (hard word) | MINOR | "investors" (also line 139) | "Investors" is a money word an 11-year-old may not know. | "people who put money into" or define it at first use | unsure |
| 44 | 5 | 141 | Personification and Anthropomorphism / Reification | MAJOR | "its success started a wave of toll-road building" | An abstraction (success) acts, and "wave" is a metaphor. | "The historian Charlene Mires writes that other states built many more toll roads after the Lancaster Turnpike succeeded." | unsure (the bank's wording is "Pennsylvania inspired the wave of toll road construction with the success of the Lancaster Turnpike") |
| 45 | 5 | 141 | Information density | MINOR | "The Lancaster Turnpike was the country's first long-distance engineered toll road." | Repeats the claim already made in lines 133 and 137. | Cut line 133's "first ... of this kind" or this sentence. | unsure |
| 46 | 5 | 139 | Fourth wall / The Reader | MINOR | "Sources disagree on when it opened." | "Sources" as in the book's research. | "Accounts differ on when it opened." | unsure |
| 47 | 5 | 139 | Not in bank | MINOR | "The builders gave it a surface of broken stone and gravel." | The bank has the surface, but "the builders" is a vague agent. The bank's own count has no builders named. | "The company had it covered with broken stone and gravel." | unsure |
| 48 | 5 | 154 | Not in bank | MINOR | "The builder of the first American steamboats" | The bank says Fitch had the first working, scheduled steamboat and the first scheduled passenger service. It does not say he built the first American steamboats. | "The builder of a working steamboat and the first scheduled steamboat service for paying passengers." | unsure |
| 49 | 5 | 158 | The AI Cadence (closing reversal) | MINOR | "Robert Fulton's steamboat began running on the Hudson River in 1807, and Fulton built the first steamboat business that lasted." | The Fitch story ends on a contrast with another man. The facts are in the bank, but the line is a closing turn, and it moves the story off Fitch. | Move the Fulton fact up into the paragraph about the business failing: "Fitch died in 1798. Robert Fulton's steamboat began running on the Hudson River in 1807, and Fulton built the first steamboat business that lasted." Or end on "Fitch died in 1798." | unsure |
| 50 | 5 | 156 | Not in bank | MINOR | "Too few people bought tickets to pay for running it." | The bank says "thin ridership." "To pay for running it" adds a reason. | "Too few people bought tickets." | unsure |
| 51 | 5 | 145 | Not in bank | MINOR | "These were the men meeting in Philadelphia that summer to write the Constitution of the United States." | A plain definition of the convention, not an event fact, so allowed. Noted only because the bank is silent. | none | n/a |

## Era 5 passes
Pass 2: no harm told. The prose says the records do not name who broke the stone (the prescribed form). Pass 6: clean.

## Counts

51 rows. Rows 40, 41 and 51 are notes with no change needed, so 48 defects:
- BLOCKING: 2 (rows 10, 27)
- MAJOR: 5 (rows 14, 24, 34, 38, 44)
- MINOR: 41

By rule (approximate):
- Not in bank: about 22
- Oversized Words (hard word): about 10
- "Sources" read as the book's research (Fourth wall / The Reader): 5 (rows 16, 33, 35, 46, plus row 33's second quote)
- The Teaching Point: 2
- Personification / Reification: 2 (rows 24, 44)
- Hard subjects §2: 3 (rows 14, 34, 38)
- AI Cadence: 3 (rows 5, 13, 49)
- Other: Defined Terms, Information Order, Metadiscourse, Passives, Information density

Validator and punctuation output:
- `node tools/validate_grid.js manuscript/transportation/part1-before-1800.md --part`: "1 chapters, 3 stories, 0 errors"
- `python tools/project_state.py --punct manuscript/transportation/part1-before-1800.md`: "emdash=0 semicolon=0"

Eras with no findings: none. All five eras have at least one finding. Era 1 has no hard-subject findings.

