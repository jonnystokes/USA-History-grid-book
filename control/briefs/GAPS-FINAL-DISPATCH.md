# GAPS-FINAL dispatch: the last research leftovers, nine agents at once (2026-10-26)

Jon authorised a parallel burst on 2026-10-26 to close every item the step-7 fixers left under
NEEDS-RESEARCH and the open AUDIT-QUEUE polish items. The book is finished and passing; these are
loose ends. Each task below owns a disjoint set of chapters, so no two agents touch the same file.

## Rules for every task (read these, then `control/briefs/GAPS.md`)

- **Brief:** `control/briefs/GAPS.md` governs the work, including the "Read first" list. Model: opus.
- **The style guides are binding on every sentence you write or change (Jon, 2026-10-26).** Read
  `control/general-writing-style-guide.md` (Version 2) and `control/writing-style-guide.md` (the
  amendment) in full before you touch any prose, and `control/hard-subjects-policy.md`. Before you
  report, run Version 2's "Self-Review Before Reporting" and the amendment's §5 audit additions on
  every sentence you added or changed: no em dash, no semicolon, no personification, no passive
  without an actor, no big word, no AI cadence (triads, "not just X but Y", fragments, reversals),
  one plain present-day voice, the teaching point first. Also read the two or three sentences
  around each change and repair any rule break you notice there while you are in the passage.
- **Files you may edit:** only your chapters' `manuscript/<slug>/*.md`, `research/research-<slug>.md`,
  and your own checkpoint `control/checkpoints/<TASK>-gaps.md`. Nothing else. No git. No installs.
  Never edit WORKLOG, TODO, AUDIT-QUEUE, DECISIONS, outlines, or another chapter.
- **Checkpoint first.** Before any research, create `control/checkpoints/<TASK>-gaps.md` from
  `control/checkpoints/_TEMPLATE.md` with STATUS IN-FLIGHT, your item list as the units table (state
  `todo`), NOW and NEXT filled. Update it after every item: `CLOSED (<TASK>)`, `SEARCHED, NOT FOUND`,
  or `LEFT AS IS (reason)`. **If the checkpoint already exists when you start, you were interrupted:
  read it and carry on from NOW; do not redo closed items.**
- **Scratch:** your own folder `<scratchpad>/<TASK>/` only. Downloads (PDFs, pages) go there too.
  Never open a PDF link in the browser pane.
- **Budget per item:** a few good searches, not a hunt. Prefer government, court, archive, museum,
  university and named-historian sources. A `SEARCHED, NOT FOUND` already in the bank on the same
  question is settled unless the item gives a new lead. Never guess a name. Never invent a fact.
- **Prose changes are minimal.** Close a gap with the missing fact, in sentences that meet the style
  guide (0 em dashes, 0 semicolons, people as actors, plain words). Keep every marker line, slug,
  `status=`, `progress=`, `movie=` and record key. Never shrink the book. Never mention the book,
  research or agents in the prose. Items marked "optional" or "polish" that turn up nothing need no
  prose change at all; just bank the SEARCHED, NOT FOUND and mark the item.
- **Hard subjects:** `control/hard-subjects-policy.md` and DECISIONS #28-#46 bind. Plain words
  (rape, killed, enslaved), name who did it when the record does, never state an accusation against
  a living person as fact, credit a named source when accounts differ.
- **After each part file you change:** `node tools/validate_grid.js <file> --part` (0 errors) and
  `python tools/project_state.py --punct <file>` (0/0). Before reporting:
  `python tools/project_state.py --check <slug> --stage prose` for every chapter you touched. PASS required.
- **Pacing (Jon's standing rules).** Update the checkpoint before anything else after each item.
  Check the 5-hour window about a quarter, half and three-quarters of the way through, by feel:
  ToolSearch `select:mcp__ccd_session_mgmt__get_usage`, read only its `plan` part. Above 95%: no
  more research, finish the item in hand, update the checkpoint, report that you are not done, and
  stop. At the weekly limit: summary report and halt. No routine context checks.
- **Report** (under 200 words): per item one line (CLOSED / NOT FOUND / LEFT AS IS, with the source
  or the sources checked), any bank correction, then the `--check` outputs last. Do not paste prose.

---

## T-650: america-world, art, big-business

america-world:
1. part1 era 4 (Nanfan deed, 1701): the bank says "other writers dispute" the Haudenosaunee reading but names none. Prose says "Others read it differently." Name who disputes it (a court ruling or a named historian), or name the silent document (#45).
2. part3 era 9 (Jayuya and Utuado, October 1950): no count of people killed when the National Guard attacked the towns. Find a sourced count, or name the silent document.
3. part3 era 8 (Haiti cacos): the US military count of 3,250 is search-summary only. Confirm on a real page or drop it from the bank. Same for the Dominican "1,137 killed or wounded".
4. part2 era 7 (Samoa 1899): who renounced which claims in the Tripartite Convention is search-summary only; prose names only the three signers. Confirm from the treaty text (Yale Avalon or similar) and add one sentence if confirmed.
5. part2, Kake (AUDIT-QUEUE T-484): check that the sentence citing "one historian's account" now names the historian; if not, name from the bank or restate as plain fact.

art:
6. Toussaint L'Ouverture is named without a gloss (no bank line). Add a one-line bank entry and a short plain gloss in the prose where he is named. (Spiro names are settled: POLISH-1 kept them credited. Do not reopen.)

big-business:
7. Who sued Biddle for nearly $25 million, and who at Union Carbide India turned off the Bhopal scrubber (both SEARCHED, NOT FOUND earlier). One more try each with new leads only (court records for Biddle 1841; the Indian CBI charge sheet / 2010 Bhopal court judgment for the scrubber). Also check that no "(unconfirmed: search summary only)" PATCH fact is stated in the prose as fact (AUDIT-QUEUE T-460).

## T-651: city-building, crime-justice, disasters, drugs-alcohol

city-building:
1. part2 era 7 (F4): the 1889 Creek and Seminole payment amounts ($2.28 million, $1.91 million) rest on a blog and Wikipedia. Read 25 Stat. ch. 317 and ch. 412 (1889) directly (Library of Congress Statutes at Large, govinfo, or Oklahoma Historical Society) and bank the confirmed amounts or correct them.

crime-justice:
2. part2 (AUDIT-QUEUE T-476): Myrtle Vance (Paris, Texas, 1893): find the period sources' word for what was done to her; use "rape" in the prose if they support it (#31), else keep the current wording and bank the sources checked.
3. "Lower Agency" left unexplained (MNHS does not say what it was). Find what the Lower Sioux Agency was (a US government post on the reservation) from MNHS or NPS and add the plain gloss.
4. Eastern State / any other polish note in control/checkpoints/F7-crime-justice.md under NEEDS-RESEARCH: read the full line and act on it if it names a concrete gap.

disasters:
5. part2 era 7, Sea Islands 1893: "The records do not identify those politicians or newspaper writers by name" rests on a search that never opened Caroline Grego's work (JSH 2019 article; *Hurricane Jim Crow*, UNC Press 2022). Try to open Grego (Google Books preview, the JSH abstract, reviews quoting her); name them if she does, else name the silent document (#45).
6. Palisades Fire (AUDIT-QUEUE T-469): the prose gives the case status "as of" a date. Refresh to the status as of 2026-10-26 (retrial was set for Nov 2, 2026; the defendant is not convicted). State only what court records and major news report; never guilt.

drugs-alcohol:
7. Low priority: the messenger whipped in 1791 may be John Connor (search summaries; Founders Online did not load). Try Founders Online once more. If confirmed, bank it; change prose only if it already names an unnamed messenger where a name would be used.

## T-652: economy, education, energy, exploration

economy:
1. part2 era 6 (row 41): name the sources of the 1837 estimates: "a third of all workers had no jobs by the fall of 1837", wage cuts of 30 to 50 percent, the 343-of-850 bank count ("traceable to Hammond"), New York's 25 to 30 percent. Find the named historians (Bray Hammond 1957; Jessica Lepler 2013; Alasdair Roberts 2012) or primary records, bank them, and credit the figures in the prose per #37 (a plain sentence naming the source, not a parenthesis).

education:
2. part1 era 5: who granted the Young Ladies' Academy of Philadelphia its charter on 7 Jan 1792. Only Wikipedia names Pennsylvania / Gov. Thomas Mifflin. Find a primary or scholarly source (the 1794 *Rise and Progress of the Young Ladies' Academy*, Pennsylvania statutes, a journal article), then name the actor in the prose.
3. Bank correction (AUDIT-QUEUE T-482): the T-261b bank sentence says Black teachers "in every state ... faced the whip"; Louisiana and Alabama set only prison or fines. Correct the bank line and check the prose matches.

energy (both optional):
4. Garrison Dam: confirm the 152,360-acre figure and the "more than 300 families, 1,700 people, 80 percent" count on a real page (Three Affiliated Tribes, Army Corps, NPS, or a scholarly source). Prose uses neither; bank only.
5. The date of William Kemmler's killing of Tillie Ziegler (court page gives none; it was March 29, 1889 by most accounts). Confirm on a real page; add the year to the prose only if the sentence reads oddly without it.

exploration:
6. The Wilkes expedition as "the first" large US-government exploring voyage was cut (Smithsonian page returned 403). Try the Smithsonian Institution Archives or NOAA page again, or a scholarly source; restore the fact only if a real page supports it.
7. Boone torture detail (AUDIT-QUEUE T-462): the detail rests on a blog and a Substack. Confirm from a scholarly or primary source (Faragher's *Daniel Boone*, 1992; Draper manuscripts), or cut it from the prose and bank SEARCHED, NOT FOUND.

## T-653: food-farming, government-politics, health, holidays, home-family

food-farming:
1. A primary or scholarly source for the Kansas 1885-86 quarantine law's purpose (Texas fever). Bank it; credit in prose if the prose states the purpose.
2. Who arrested Ward Rodgers in January 1935 (Southern Tenant Farmers' Union, Marked Tree, Arkansas). Name the officers or body if the record does; else name the silent document.
3. Chavez (#46, AUDIT-QUEUE): confirm food-farming part 3 carries the March 2026 accounts about Cesar Chavez, credited, as work-workers and rights-movements do (copy the T-601 PATCH from research-work-workers.md if missing). Verify, do not rewrite if present.

government-politics:
4. part3 row 22 (era 9): the Department of Education IDEA history page refused fetch (403). Try again (curl to scratch), or find who kept the 1 million children with disabilities out of school before 1975 (state laws, school officials) in the 1975 House/Senate reports or PARC v. Pennsylvania / Mills v. Board of Education records, and name them.

health:
5. Puerto Rico sterilisation: the factories and hospitals that pressured women are named in no source found. Try Laura Briggs, *Reproducing Empire* (2002), and Iris López, *Matters of Choice* (2008), via Google Books preview or reviews. Name if found; else leave the prose and bank the sources checked.

holidays:
6. part1 era 5 (Fithian, Christmas 1773): was Nelson, "the Boy who makes my Fire", enslaved at Nomini Hall? Prose says "a boy Fithian counted among the 'Servants'". Check the Fithian journal edition (Farish 1943 / Colonial Williamsburg) or Nomini Hall scholarship; if a source confirms he was enslaved, restore "enslaved".

home-family (both low priority):
7. A source for the earth lodge "up to 30 people" figure (the NPS page gives 10 to 20); align the prose to the sourced figure if it still says 30.
8. A source naming who first used "cult of domesticity" (Barbara Welter's 1966 article is the usual answer, "Cult of True Womanhood"; Aileen Kraditor 1968 for "domesticity"). Bank it; credit in the prose only if the prose attributes the term.

## T-654: immigration, marketplace, migration, money

immigration:
1. part3 era 10: the Human Rights Watch / Physicians for Human Rights report (June 25, 2026) on deaths in ICE custody: what caused the five deaths from "traumatic causes", and who caused them. Download the full report to scratch and read it. State what it finds, credited to the report; never state guilt of a named living person as fact (#30/#38).

marketplace (both optional):
2. Franklin and Hall partnership end date (1766) is arithmetic from Smyth's "37 years", not a bank line. Find a source (Franklin Papers at Yale, the 1766 settlement) and bank it.
3. "railway houses" in the Heth exhibit list is rendered "railroad buildings" without a source defining the term. Find a definition or the original list; align the prose word to the source.

migration (both optional):
4. Who held Green Flake and Oscar Crosby in slavery: search summaries name James Flake and William Crosby. Confirm on a fetched page (Utah Division of State History, Century of Black Mormons database, Utah History Encyclopedia). Bank; name in prose if confirmed and the prose leaves them unnamed.
5. Winslow's own count of buildings burned at Grand-Pré (276 barns, 255 homes, 11 mills, one mass house), search summary only. Confirm from Winslow's journal (Nova Scotia Historical Society 1883, archive.org) or Parks Canada.

money:
6. part3 era 10, row 33 (Bent verdict, Nov 12, 2012): confirm from the SEC judgment, Bloomberg or the Washington Post whether the jury found Bruce Bent II negligent on one securities-law claim and the Reserve companies liable. If confirmed, add it beside "cleared of the fraud charges" in one plain sentence, credited.

## T-655: music, native-nations, news-communication, rights-movements

music:
1. part2 era 6, Stephen Foster's death: Wikipedia says he "may also have sought to kill himself". Find a named biographer (Ken Emerson, *Doo-Dah!*, 1997; JoAnne O'Connell 2016) on the January 1864 fall; if one says it, add "accounts differ" with names; if none does, leave the prose.
2. part3 era 8, DeFord Bailey: George D. Hay's 1945 sentence ("Like some members of his race and other races DeFord was lazy") is search summary only. Open Hay's *A Story of the Grand Ole Opry* (1945; archive.org) or a scholarly page quoting it (David Morton and Charles Wolfe, 1991), then quote the race remark exactly; keep the gist wording if the exact text cannot be opened.
3. PERISHABLE, part3 era 10: the Kennedy Center closure passage ("As of October 3, 2026, still closed, no date set") and the Suno/Udio cases ("As of late September 2026"). Refresh both to what is true as of 2026-10-26 with the date, from major news, and bank the sources.

native-nations:
4. part1 era 3: which nations lost or gained which lands in the Beaver Wars (vague sentence was cut; bank GAPS line). Find a scholarly or museum source (e.g. Ohio History Connection, Canadian Encyclopedia, a named historian) naming the nations pushed out (Wendat/Huron 1649, Erie, Neutral, Shawnee from the Ohio country) and bank it; restore one plain sentence if sourced.
5. part1 era 1: a reliable count of separate nations before 1500 and of languages; the current languages count rests on two teaching guides. Try Ives Goddard, *Handbook of North American Indians* vol. 17, or the Smithsonian / Endangered Languages Project; bank the stronger source and credit it in the prose per #37.

news-communication:
6. part3 era 9, Ole Miss riot 1962: prose says "a crowd"; find a source (the FBI/Justice Department account, Doyle's *An American Insurrection*, 2001, or NPS/Ole Miss archive) that names the crowd as white segregationists, and say so plainly if sourced.

rights-movements:
7. part3 era 9, Chicano Moratorium, 29 August 1970: name the other three dead besides Ruben Salazar (Lyn Ward, Angel Díaz, Gustav Montag are the usual names; confirm) and how each died, and who killed them where the record says (coroner's inquest, LA Times, UCLA Chicano Studies Research Center). #44 applies: name the killers if the record does.

## T-656: science, slavery-freedom, storytelling-evolution, styles, technology

science:
1. era 10: a named source for the spread of AI tools in labs in the 2020s (sentence cut; a Nature 2023 survey of researchers is the lead, page needed login). Find the Nature survey (Van Noorden and Perkel, Nature, Sept 2023; open-access news version) or another named survey; restore one sourced sentence crediting it.

slavery-freedom (PRIORITY, DECISIONS #32 amended):
2. part1 era 5: a published book or journal article by a named historian calling Jefferson's conduct toward Sally Hemings (and John Wayles's toward Elizabeth Hemings) rape. Leads: Annette Gordon-Reed's discussion of the question in *The Hemingses of Monticello* (2008) (she discusses the word rather than using it; report exactly what she says); Kendi, *Stamped from the Beginning* (2016), Part III, already SEARCHED, NOT FOUND via LitCharts only, try Google Books preview; Brenda Stevenson; Thomas Foster, *Rethinking Rufus* (2019); Jessica Marie Johnson is already banked from a newsletter essay. Then make the sentence match the evidence: "some historians, such as X, call it rape" with the names the sources support, keeping the plain facts (she was enslaved by him and could not refuse). Grep the whole manuscript for the same claim ("describe what he did as rape" and similar) and align every chapter that carries it (america-world, government-politics, home-family may). Report the exact wording you settled on.

storytelling-evolution:
3. part1 era 5: who "His Excellency and Lady" at the Valley Forge *Cato* (May 1778) were (the Washingtons), from an opened page (the Mount Vernon *Cato* page gave 403; try curl to scratch, Founders Online, or the NPS Valley Forge page). If confirmed, name them.
4. part1 era 3: the tavern spellings "Cowle's" and "Cole's" (Washington Post 1989, search summary only); cut from prose. Optional: confirm and bank only.

styles:
5. part3 era 8, Ann Lowe: did the plantation owner who was her great-grandfather enslave her great-grandmother? Try Margaret Powell's scholarship (Winterthur / Smithsonian Cooper Hewitt 2023 exhibition texts; Julia Faye Smith, *Something to Prove*, 2016). If a source says so, state it plainly under DECISIONS #32 (she was enslaved by him and could not refuse); else keep the prose.

technology:
6. part2 era 7 (row 24): what Benjamin Lathrop Brown's 2020 *Proceedings of the IEEE* study concludes about Bell and Gray (search summary: Bell and his lawyers did not copy Gray). Open the abstract (ieeexplore) or a page quoting it; if confirmed, add one plain sentence after the title, credited.

## T-657: war, work-workers

war:
1. part1 era 2 (EXTRA): was the Tiguex rape at Arenal, and was Juan de Villegas the man? Only Wikipedia / Legends of America say so. Try Flint and Flint, *Documents of the Coronado Expedition* (2005), the 1544 investigation testimony (Google Books preview; New Mexico History website). Prose no longer ties the rape to Arenal; bank what you find and restore the detail only if a real source supports it.
2. part1 era 3: Mashantucket reservation 1666 rests on Wikipedia ("created by the Connecticut Colony"); the tribe's history page returned 403. Try curl to scratch, or the Connecticut State Library / Pequot Museum pages. Confirm and bank.
3. part1 era 5 / part3 era 9: Gnadenhutten "no charges" and the Calley sentence reductions rest on Wikipedia (+ EBSCO for Calley). Find stronger sources (Ohio History Connection for Gnadenhutten; the Army's Peers report, the 1974 habeas ruling Calley v. Callaway, or the Nixon Library for Calley). Bank; prose stands.

work-workers:
4. era 9, braceros: who ended the program in 1964 (Congress let Public Law 78 expire December 31, 1964). Confirm on a real page (Library of Congress, UCLA Labor Center, Bracero History Archive) and name Congress as the actor in the prose if confirmed.
5. era 8, Hoover Dam: a named historian or primary record for reading the 42 "pneumonia" deaths as carbon-monoxide poisoning (Joseph Stevens, *Hoover Dam: An American Adventure*, 1988; Michael Hiltzik, *Colossus*, 2010; the 1930s Six Companies lawsuits). Credit the named historian in the prose per #37; prose now states it as a dispute.
6. era 5: the 1768 New York tailors' strike, a primary or scholarly source (Philip Foner, *History of the Labor Movement*, vol. 1; the New-York Journal 1768). If none supports it, say what the record shows and bank SEARCHED, NOT FOUND.
7. era 9, Wisconsin Steel: who ordered the March 1980 shutdown (Envirodyne's managers, or the lenders, Chase Manhattan). Try the Chicago Tribune archive, David Bensman and Roberta Lynch, *Rusted Dreams* (1987), and the 1980s court rulings. Name the actor if the record does.

## T-658: viewer polish (viewer/viewer.html only)

AUDIT-QUEUE T-643: the viewer itself inserts em dashes (record lines, the Next button). The zero-em-dash rule covers everything a reader sees. Also six story headings drop nicknames (shown from name=).

- **Files you may edit:** `viewer/viewer.html` only. Nothing else. Checkpoint `control/checkpoints/T-658-viewer.md`.
- **Line 89 of viewer.html is a 373 KB base64 image. Never read the file whole.** Use Grep for the em dash character (U+2014) and for the Next button markup, then Read with offset/limit around the hits, and Edit the exact lines. Check the byte count of line 89 is unchanged afterwards (`awk 'NR==89{print length($0)}' viewer/viewer.html` before and after).
- Replace each em dash the viewer renders with a plain alternative (a colon, a middle dot, or a comma, whichever reads best in that spot). Leave em dashes that appear only in code comments or in the base64 line.
- Nicknames: find where story headings are built from `name=` and why a nickname part is dropped (compare `control/VIEWER-CONTRACT.md` §2 and `control/grid-markers.md` for how name= carries nicknames); fix the heading builder so the full name shows. Verify on the six stories if you can identify them (grep manuscript/ for name= values containing a quoted nickname).
- Verify: `node tools/validate_grid.js outlines/BOOK-OUTLINE.md` still passes (unchanged); open the viewer in headless Chrome or node is not required; a static check that the HTML still parses (`node -e` reading the file and counting `<script>` open/close tags) is enough. Do not start a dev server.
- Report: each em dash site changed (line, before, after), the nickname fix, and the line-89 length check.
