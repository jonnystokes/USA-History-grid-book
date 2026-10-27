# CHECKPOINT T-650 | america-world, art, big-business | gaps | GAPS-FINAL items 1-7

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check <slug> --stage prose (america-world, art, big-business)
BRIEF:  control/briefs/GAPS.md (dispatch: control/briefs/GAPS-FINAL-DISPATCH.md, section T-650)
MODEL:  opus
FILES:  research/research-{america-world,art,big-business}.md · manuscript/{america-world,art,big-business}/...

NOW:    all 7 items done; self-review repairs applied; all six checks PASS (2026-10-26 8:40 PM)
NEXT:   director: review and commit

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | america-world part1 era 4: Nanfan deed 1701, name who disputes the Haudenosaunee reading | landed | CLOSED (T-650): R. v. Ireland 1990 (Crown's argument, Gautreau J. rejected); PATCH era 4; prose para rewritten, validator 0, punct 0/0 |
| 2 | america-world part3 era 9: Jayuya and Utuado Oct 1950, count of people killed | landed | SEARCHED, NOT FOUND (town count); Time Nov 13 1950 opened: 4 policemen killed at Jayuya, 31 dead island-wide; prose names Time as the silent document; validator 0, punct 0/0 |
| 3 | america-world part3 era 8: Haiti cacos 3,250 and Dominican 1,137, confirm or drop from bank | landed | CLOSED (T-650): Omaha Daily Bee Oct 28 1920 (AP): Barnett told naval court 3,250 was an addition error, true count 2,250 (1,861 in 1919); bank corrected, prose adds Barnett count. 1,137 and 144 DROPPED (not confirmed; Fuller & Cosmas PDF refused). validator 0, punct 0/0 |
| 4 | america-world part2 era 7: Samoa 1899 Tripartite Convention, who renounced which claims | landed | CLOSED (T-650): treaty text, 31 Stat. 1878-1880 (Art. II), PATCH era 7; prose +2 sentences; validator 0, punct 0/0 |
| 5 | america-world part2: Kake, "one historian's account" names the historian? | landed | CLOSED (T-650), no change needed: line 123 introduces 'The historian Rebecca Poulson, writing for the Alaska Historical Society'; line 125 'Poulson calls the deaths accidental' |
| 6 | art: Toussaint L'Ouverture gloss + bank line | landed | CLOSED (T-650): Boston College Burns Library name record; bank line under Lawrence (era 08); prose gloss sentence in part3; validator 0, punct 0/0 |
| 7 | big-business: Biddle $25M suit, Bhopal scrubber, unconfirmed PATCH facts in prose (T-460) | landed | Biddle SEARCHED, NOT FOUND (Villanova catalog, HSP 403; Govan 1959 not online). Bhopal SEARCHED, NOT FOUND (2010 judgment PDF dead, not archived; CBI charge sheet not online; Cowley/CCPS 2015 lists convicted officials, not who). T-460 check: every T-460 '(unconfirmed)' line is either confirmed by T-487/T-616 or not in prose (Enron 22,000/$101B, not printed). No prose change. |

<!-- state: todo | working | landed | skipped (say why) -->

## Sources in hand

- https://www.rds.oeb.ca/CMWebDrawer/Record/362255/File/document : full text of R. v. Ireland (1990), item 1
- https://treaties.okstate.edu/treaties/nanfan-treaty-1701 : deed text, item 1
- https://time.com/archive/6886054/insurrection/ : Time Nov 13 1950, item 2
- https://nebnewspapers.unl.edu/lccn/sn99021999/1920-10-28/ed-1/seq-1/ocr : Omaha Daily Bee 1920, Barnett 2,250, item 3
- https://dheller.org/Timeline-files/US-Statutes/v31/treaties/Convention-Samoa-1899-b.pdf : Samoa convention text, item 4
- https://findingaids.bc.edu/agents/people/3791 : Toussaint gloss, item 6
- Akamai-blocked: marines.mil Fuller & Cosmas PDF (item 3)
- Cloudflare-blocked (for the main agent to open for Jon if wanted): https://collections.ubcic.bc.ca/s/fndds/item/11712

## Gaps researched

## Decisions and defects fixed

- Bank correction (america-world era 8): T-254's '3,250' US military count was an addition error; Barnett corrected to 2,250 in 1920. Dominican 1,137 / Marines 144 dropped.

## Log

- 2026-10-26 7:05 PM | item 1 | PATCH + prose america-world part1 | validator 0 errors | punct 0/0
- 2026-10-26 7:20 PM | item 2 | SEARCHED NOT FOUND + prose america-world part3 | validator 0 errors | punct 0/0
- 2026-10-26 7:40 PM | item 3 | PATCH + bank correction + prose america-world part3 | validator 0 errors | punct 0/0
- 2026-10-26 7:55 PM | items 4-5 | PATCH + prose america-world part2 (Samoa); Kake verified | validator 0 errors | punct 0/0
- 2026-10-26 8:05 PM | item 6 | bank line + prose art part3 | validator 0 errors | punct 0/0
- 2026-10-26 8:25 PM | item 7 | two SEARCHED NOT FOUND entries in research-big-business.md; no prose change |
- 2026-10-26 8:40 PM | self-review | root-metaphor and personification repairs (deed 'states'/'describes', Time's report 'does not state', Marines 'had recorded', Samoa signers as actors) | validators 0 | punct 0/0 | --check prose+research PASS x3
