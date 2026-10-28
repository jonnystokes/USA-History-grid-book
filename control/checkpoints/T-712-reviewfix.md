# CHECKPOINT T-712 | storytelling-evolution (Chapter 34), then styles (Chapter 35) | review fix pass for R23

STATUS: DONE (both chapters --check PASS)
BRIEF:  control/briefs/REVIEW-FIX.md
REVIEW: control/review/R23.md (25 findings for storytelling-evolution, 25 for styles)
FILES:  manuscript/storytelling-evolution/part1-before-1800.md, part2-1800s.md, part3-1900s-and-today.md,
        control/backmatter/storytelling-evolution.md,
        manuscript/styles/part1-before-1800.md, part2-1800s.md, part3-1900s-and-today.md,
        control/backmatter/styles.md
VERIFY: python tools/project_state.py --check storytelling-evolution --stage prose
        python tools/project_state.py --check styles --stage prose
SCRATCH: apply.py (exact once-only replacement, keeps CRLF), eras.py (era minutes), edit files e34*.txt, e35*.txt in the T-712 scratch folder

## Storytelling Evolution findings (numbered in the order of R23.md)

| # | era | finding (first words) | state | note |
|---|-----|-----------------------|-------|------|
| 1 | The 1600s | "William Darby is one of the" (boxes retell text) | fixed | Darby: arrest, security, verdict repeats cut, hook now authorship; Warren: span keeps governor and ban, box keeps Spy, titles, unsigned; Brown: tea garden, Richard III, playbill repeats cut; Forrest: hiss and riot repeat cut; Serkis: on-set repeat cut; Rubalcaba: contract terms cut to a clause; also Levingston, Ball, Johnson small repeats cut |
| 2 | 2000 to Today | "Reporters at The New York Times" | fixed | point first (actresses accused, juries convicted); every verdict kept; day dates cut to years; Farrow, Bragg named by role |
| 3 | 1850 to 1900 | "In July 1890 No Neck told" | fixed | date order 1883, 1885, 1887, 1890, July 1890, Dec 1890, 1891; No Neck joined; investigation tied to the 1889 to 1890 tour; Standing Rock sentence split |
| 4 | 1750 to 1800 | "Douglass built a theatre in Philadelphia" | skipped | how plays went on after the 1759 law is not in the bank, and "records silent" would be untrue; era lead now says "Even so" |
| 5 | 1750 to 1800 | "The first plays by American writers" | fixed | lead gives 1767 first American play, 1787 Yankee comedy |
| 6 | closing | "banned plays as wasteful or bad" | fixed | Accomack case added (record gives no reason); Massachusetts reason; Congress "promised to discourage", "asked the states to stop"; rival manager for the arrests; "heathen rites"; backmatter Q1 in step |
| 7 | The 1500s | "Oñate's soldiers acted a second play" | fixed | spans not moved (grid rule); back-in-time signal, Tewa glossed, trial marked "years later" |
| 8 | The 1500s | "About eight months after the play" | fixed | bridge: the play's kneeling Pueblo characters vs what the soldiers did at Acoma |
| 9 | The 1600s | "A man named Edward Martin reported" | fixed | record gives charge only as "acting a play"; says no more |
| 10 | 1800 to 1850 | "He told General William Hall, 'You" | fixed | Hall commanded on the spot; Sandford brought the soldiers |
| 11 | 1800 to 1850 | "Its hero is Metacom, a leader" | fixed | Metamora stands for Metacom (King Philip); then Metamora only |
| 12 | 1900 to 1950 | "Later researchers, among them Jefferson Pooley" | fixed | finding first (panic far smaller, "a myth"), then the 2 percent and no news-broadcast answers |
| 13 | 1900 to 1950 | "Officials in the state of Ohio" | fixed | one count (twelve mayors), dated examples in order, "most let it play" once |
| 14 | 2000 to Today | "The cattleman William Hale ordered the" | fixed | told through Mollie; relations named, no loose "her" |
| 15 | 2000 to Today | "By 2019 the members were 32" | fixed | point first; 75 percent used once; clause on why 13.5 percent and 29 films with none both hold |
| 16 | 2000 to Today | "They bought about 780 million tickets" | fixed | point first; tickets down 5 percent but spending up because average ticket cost more (arithmetic of the figures); day dates cut |
| 17 | 1900 to 1950 | "FBI agents under J. Edgar Hoover" | skipped | reason for the FBI case and the permit is not in the bank; "records give none" would be untrue |
| 18 | 1900 to 1950 | "They billed themselves under a stage" | fixed | name paired "Real" with an insult; told audiences they were real Black men |
| 19 | 1800 to 1850 | "No record states the cause of" | fixed | "Historians think" (bank: historians' inference) |
| 20 | 1700 to 1750 | "That play does not survive." | fixed | Charleston play is a different play from The Fool's Opera |
| 21 | 1700 to 1750 | "Williamsburg stands on land that the" | fixed | run-in labels "Whose land." and "The Etiwan."; Algonquian glossed |
| 22 | Before 1500 | "Medicine societies among the Haudenosaunee use" | fixed | Haudenosaunee glossed in era lead; policy gives no more on "medicine society" |
| 23 | 1800 to 1850 | "Next: After 1850 white actors in" | fixed | Next lines of eras 6 to 9 now give a new fact from the next era; closing Next says rules about clothes and hair, and who made the cloth |
| 24 | card | "Five minutes? Read 'The African Theatre" | fixed | pointer names the two stories; strips recomputed (eras 1, 2 now 7, era 7 now 16), card about 135 = strip sum 134 |
| 25 | 1900 to 1950 | "By 1915: Hollywood had its first" | fixed | By 1915 uses the 1915 free-speech ruling; era 10 By lines now By May 2026 and By September 2026, in order |

Cuts (DECISIONS #52, all repeats of the text just above or day-level dates): Darby box 2 sentences; Warren span 2 sentences, box 1; Brown box 2; Forrest box 1; Serkis box 1; Rubalcaba box 2 to a clause; Levingston, Ball, Johnson box 1 clause each; Weinstein day dates (events all kept); streaming day dates.

Backmatter storytelling-evolution: Q1 answer in step; glossary adds Tewa, actour, Algonquian.

## Log

<!-- file | what landed | validator | --punct -->
- part1-before-1800.md | 16 edits + card and strips | 0 errors | 0/0
- part2-1800s.md | 12 edits + strip | 0 errors | 0/0
- part3-1900s-and-today.md | 30 edits | 0 errors | 0/0
- backmatter/storytelling-evolution.md | 4 edits | n/a | 0/0
- --check storytelling-evolution --stage prose: PASS (manuscript=27027w, validator 0 errors)

## Styles findings (numbered in the order of R23.md)

| # | era | finding (first words) | state | note |
|---|-----|-----------------------|-------|------|
| 1 | The 1600s | "Charged with wearing silk, she wore" | fixed | box kept on Hannah: new hook and the charge's "public humiliation" days (new to the opener); land, war, Stoddard and the March 1676 court moved into the dress-law span |
| 2 | The 1600s | "A first offense brought a warning" | fixed | 1675 law lowered a repeat fine to 10 shillings; Holton fined 10 as a repeat offender |
| 3 | 1750 to 1800 | "American cabinetmakers, the skilled makers of" | fixed | spans kept (grid rule); card says the chapter looks at furniture in two eras; Federal span opens on styles in homes and leads with the English pattern books |
| 4 | 2000 to Today | "He was paid a few cents" | fixed | "a few cents for each piece of the sewing work, about a dollar for each finished item"; LA Apparel paid $15 by the hour vs $5.50 piece pay in small shops |
| 5 | The 1600s | "Seven married women of Northampton faced" | fixed | one count (35 married women, five towns), the Northampton seven; town-by-town counts cut |
| 6 | 1950 to 2000 | "The Pawnee Nation once lived in" | fixed | removal history moved after the boys' story, labeled |
| 7 | 1900 to 1950 | "He held her as his property," | partly fixed | Georgia's father now stated plainly; "rape" not used: DECISIONS #32 needs a source that uses the word, and the bank's sources do not |
| 8 | 1900 to 1950 | "Annie Turnbo made a hair product" | fixed | both names at first mention for each woman; clause on the near-identical product name |
| 9 | closing | "Churro wool after 1598, dyes made" | fixed | a clause per material; Bakelite swapped for artificial silk; backmatter Q3 in step |
| 10 | card | "From the first colonial dress laws" | fixed | CROWN Acts glossed in the spine; preview lists cut to a few items; five-minute pointer adds the section after it |
| 11 | 2000 to Today | "Guards at a prison in Louisiana" | fixed | lead sentence: religious-freedom law, not a CROWN Act |
| 12 | The 1600s | "Most of the Pueblo peoples rose" | fixed (Ch34 side) | Ch34 now says "Ohkay Owingeh, the pueblo the Spanish called San Juan"; Ch35 keeps San Juan Pueblo because Ohkay Owingeh is not in the styles bank |
| 13 | 1800 to 1850 | "He woke up alone in the" | fixed | slave pen defined first, then "stood near the US Capitol" |
| 14 | The 1500s | "The accounts give different amounts." | fixed | one sentence, 200 to 392 pounds; arroba dropped |
| 15 | 1700 to 1750 | "Many of those cloths were coarse," | fixed | law's list kept; "all cheap, many coarse" once; two terms defined |
| 16 | 1900 to 1950 | "The order banned hoods, capes and" | fixed | reason first (save cloth and workers' time for the war); three examples |
| 17 | 1950 to 2000 | "James David Martin, 17, killed Michael" | fixed | bridge sentence; Atlanta and Chicago police counts stated, one city each |
| 18 | 2000 to Today | "Counts of the dead run from" | fixed | more than 1,100 dead, 1,134 (Clean Clothes Campaign); injured range once; one count (17) for the plans |
| 19 | 1800 to 1850 | "Godey's Lady's Book was a magazine" | fixed | point first (showed readers the latest dresses); two circulation numbers |
| 20 | Before 1500 | "At Cahokia, archaeologists found a copper" | fixed | one sentence on what the workshop held |
| 21 | The 1500s | "A French group led by René" | fixed | Fort Caroline cut from the lead, with the dagger sentence (the span keeps the dagger) |
| 22 | 1750 to 1800 | "George Washington took the oath as" | fixed | box opens on his April 8 letter |
| 23 | Before 1500 | "The art is much older than" | fixed | museum pieces from the 1830s on; quillwork older, before Europeans |
| 24 | Before 1500 | "Red ochre is a mineral made" | fixed | ochre the mineral, red ochre the red kind |
| 25 | 1850 to 1900 | "Davis and Levi Strauss & Co." | fixed | the suit said Elfelt and others used the patented rivets without permission |

Also: era strips 1 (5 to 7) and 10 (12 to 14) were stale; corrected. Card stays about 100 (strip sum 101).

Cuts (DECISIONS #52): Cahokia workshop size and find dates; Fort Caroline and the lead's dagger sentence; Hakluyt's "fourteen rows", the arroba and the 350-pound conversion; definitions of calicoes, garlix, kersey, duffel in era 4 (kersey defined in era 3); 1673 town counts; March 1676 breakdowns; L-85 scarves, sleeve cuffs, pleats; Godey's $8,000 and 40,000; Rana Plaza 1,129 and 1,136 counts; "14 other" companies; the Hannah box paragraph that repeated the opener.

Backmatter styles: ochre entry reworded; arroba, garbe and pleats entries removed (terms gone); "public humiliation" added; Q3 answer in step.

- styles part1 | 15 edits | 0 errors | 0/0
- styles part2 | 3 edits | 0 errors | 0/0
- styles part3 | 19 edits | 0 errors | 0/0
- storytelling-evolution part1 | Po'pay (finding 12) | 0 errors | 0/0
- backmatter/styles.md | 6 edits | n/a | 0/0
- --check styles --stage prose: PASS (manuscript=20507w, validator 0 errors)
- --check storytelling-evolution --stage prose: PASS (manuscript=27034w, validator 0 errors)
