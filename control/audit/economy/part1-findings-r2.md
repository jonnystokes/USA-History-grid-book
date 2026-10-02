# Findings: economy part1-before-1800 (checker: sonnet, task T-520, 2026-10-02)

| # | era | line | rule | severity | text (exact quote) | what is wrong | suggested repair | sure? |
|---|-----|------|------|----------|--------------------|---------------|------------------|-------|
| 1 | 2 | 41 | Not in bank | MINOR | "The Spanish king paid for it from his treasury. He did not set it up to make a profit." | Bank says only "military posts paid for by the crown, not profit-making colonies." "His treasury" is not in the bank. "He did not set it up" gives the king a motive and the founding, which the bank does not state. "Treasury" is also a harder word. | "The Spanish crown paid for it. It was a military post, not a business meant to make money." | unsure (small inference) |
| 2 | 3 | 53 | Reader (Pass 5: long sentence) | MINOR | "Indentured servants from England, people who signed contracts to work for a master for a set number of years, did the early work in the tobacco fields." | 29 words, with a definition packed in the middle. | "Indentured servants from England did the early work in the tobacco fields. They had signed contracts to work for a master for a set number of years." | yes |
| 3 | 3 | 82 | Hard subjects §2: Minimization | MAJOR | "Some women servants were also attacked sexually." | Bank: "Other female servants were victims of sexual assault." The prose is vaguer than its source ("attacked sexually" names no act) and names no actor, which the policy requires ("write that the records do not say who did it"). Bank says the entry does not use the word rape, so under DECISIONS #32 amended, "rape" may not be asserted in the book's voice without a source. | "Other women servants were forced into sex. The records do not say by whom or how many." (Or, if a source for the word is added to the bank, "were raped.") | unsure (rape wording needs the director's call) |
| 4 | 3 | 82 | Not in bank | BLOCKING | "officers of the local church sold her to work two more years, and the church kept the money." | Bank gives "sold by the Churchwardens for two yeares for the good of the parish." It does not say the church kept the money. Nearest bank fact: the sale was "for the good of the parish." | "...officers of the local church sold her to work two more years, for the good of the parish." | unsure (probable inference from "for the good of the parish") |
| 5 | 3 | 82 | Hard subjects §2: Lossy summarization | MINOR | "Virginia's lawmakers wrote a second law in December 1662 about a woman servant "gott with child by her master."" | Bank states "The woman, not the master, was sold." The prose never says the father was not punished, so a child reader does not see who the law fell on. | Add: "Under this law the woman was sold. The master, who was the father, was not." | unsure |
| 6 | 3 | 82 | Hard subjects §2: Lossy summarization | MINOR | "They also added years when a woman servant became pregnant." | The 1662 law in the bank applies to a child born outside marriage ("haveing a bastard"). "Became pregnant" is wider than the law. | "They also added years when a woman servant had a child outside marriage." | unsure |
| 7 | 3 | 84 | Not in bank | MINOR | "ran the colony in its first years" | Bank says only that the Virginia Company of London was a group of investors who hoped to profit, and that its first contract form ran 1609 to 1619. It does not say the company ran the colony. | "...a group of investors in England, owned the colony's first settlement." (or cut "ran the colony in its first years") | unsure |
| 8 | 3 | 92 | Reader (Pass 5: hard word) | MINOR | "being baptized as a Christian did not free anyone" | "Baptized" is a religious word, not defined. | "being baptized, which means welcomed into the Christian church with a ceremony, did not free anyone." | yes |
| 9 | 4 | 108 | Passives with a Missing or False Agent | MAJOR | "the work of enslaved people who were paid nothing" | Who paid nothing is not named. When someone is harmed, the policy requires the actor. | "the work of enslaved people, whom their owners paid nothing." | unsure (bank has the same wording) |
| 10 | 4 | 112 | Reader (Pass 5: undefined term) | MINOR | "wheat and flour from the middle colonies" | "Middle colonies" is a term of art, never defined, and the reader cannot tell which colonies it means. | "...from the middle colonies, such as Pennsylvania and New York" (check the bank first: it does not name them, so this may need a PATCH) | unsure |
| 11 | 4 | 122 | Fourth wall / Pass 5 | MAJOR | "Their account gives no count of those children's deaths in the early 1700s." | Talks about the historians' account and what it lacks, which reads as a comment on sources checked. The prescribed form speaks from the record's side ("No surviving record gives a count..."). Decision #37 allows naming who counted, but this sentence is about a missing count. | "No count of those children's deaths in the early 1700s survives." (If the director judges the current form allowed under #37, ignore.) | unsure |
| 12 | 4 | 139 | Reader (Pass 5: long sentence) | MINOR | "Under the act, a judge could send a person convicted of one of the less serious felonies to the colonies for seven years, instead of hanging them." | 28 words, two ideas. Also "instead of hanging them" attaches only to the seven-year term, and the 14-year sentence next sentence loses it. | "Under the act, a judge could send a person convicted of a less serious felony to the colonies for seven years instead of hanging them. For worse crimes, a judge could send a person for fourteen years." | yes |
| 13 | 4 | 139 | Reader (Pass 5: undefined term) | MINOR | "passed the Transportation Act. A felony is a serious crime." | The act's name uses "transportation" in an old sense (sending convicts away) that is not explained. | "...passed the Transportation Act, a law about sending convicts away to the colonies." | unsure |
| 14 | 4 | 151 | End When the Information Ends | MINOR | "The merchants who sent out these ships made their money by buying and selling human beings." | Closing line restates the loop just described (rum traded for captive people, captives sold, sugar back). | Cut it, or move the fact to the front: "Merchants who sent out these ships made their money by buying and selling human beings." | unsure |
| 15 | 4 | 149 | Not in bank | MINOR | "That year members of Congress voted to ban bringing captive Africans into the United States." | Bank says only "the U.S. ban of 1807." Who passed it and what it banned are not stated. | "That year the United States banned bringing captive Africans into the country." (or add the fact to the bank) | unsure |
| 16 | 5 | 171 | Passives with a Missing or False Agent | MAJOR | "Another woman was left for dead on the day the ship sailed." | The report's words are also agentless. Who left her is not named. The policy says to state that the record does not say. | "The record does not say who left another woman for dead on the day the ship sailed." | unsure (bank has no agent) |
| 17 | 5 | 171 | Claims That Can Be Checked | MINOR | "Nineteen died before the ship left Africa." ... "In all, the historians who wrote Brown University's report count at least 109 deaths among the 196." | The figures shown (19, one left for dead, 68, 20) add to 108 or 107, not 109. Bank notes "The report's itemized numbers do not add to 109; the report gives 'at least 109' as its total." The prose hides the gap, so a reader who adds finds an error. | "The report gives a total of at least 109 deaths among the 196, more than the numbers above add up to." | unsure |
| 18 | 5 | 173 | Passives with a Missing or False Agent | MINOR | "The survivors were so sick that some were sold for £5." | Who sold them is not named (the crew or Hopkins). | "...that Hopkins's crew sold some for £5" if the director accepts the crew as seller, otherwise "No record names who sold them." | unsure |
| 19 | 5 | 175 | Personification and Anthropomorphism | MINOR | "his ship *Hope* took 229 Africans from the Gold Coast of Africa" | A ship cannot take people. His crew did. Also softens who acted. | "his crew took 229 Africans aboard the *Hope* on the Gold Coast of Africa" | unsure (the bank has the same phrase) |
| 20 | 5 | 175 | Reader (Pass 5: hard word) | MINOR | "owning, fitting out or sailing on ships" | "Fitting out" is unexplained. | "owning, equipping or working on ships" | yes |
| 21 | 5 | 201 | Not in bank | BLOCKING | "A defender inside the house shot and killed their leader, James McFarlane." | Bank: "the rebel leader James McFarlane was shot and killed". It does not say who shot him or that it was a defender inside the house. | "James McFarlane, the rebels' leader, was shot and killed." (Nearest bank fact: he was shot and killed.) | yes |
| 22 | 5 | 203 | Not in bank | MINOR | "broke into houses at night" and "People there called it "the Dreadful Night."" | Bank puts "the Dreadful Night" in quotes but does not say people there called it that, and "at night" is inferred from the name. | "...broke into houses and arrested about 150 people. The event is known as "the Dreadful Night."" | unsure |

## Count by severity

22 findings: BLOCKING 2 (rows 4, 21), MAJOR 4 (rows 3, 9, 11, 16), MINOR 16.

## Count by rule

- Not in bank: 6 (rows 1, 4, 7, 15, 21, 22)
- Reader (Pass 5): 6 (rows 2, 8, 10, 12, 13, 20)
- Passives with a Missing or False Agent: 3 (rows 9, 16, 18)
- Hard subjects section 2: 3 (rows 3, 5, 6)
- Fourth wall: 1 (row 11)
- Personification and Anthropomorphism: 1 (row 19)
- End When the Information Ends: 1 (row 14)
- Claims That Can Be Checked: 1 (row 17)

## Eras with no findings

Era 1 (before-1500): none. Pass 1 to 6 clean against the bank. Em dashes 0, semicolons 0.

## Validator and punctuation output

    === part1-before-1800.md : 1 chapters, 3 stories, 0 errors

    manuscript/economy/part1-before-1800.md: emdash=0 semicolon=0
