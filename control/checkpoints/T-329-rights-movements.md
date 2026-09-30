# CHECKPOINT T-329 | rights-movements | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-9 (part3), writer C: era 10 (part3) + final

STATUS: T-329b landed (director verified: FAIL  rights-movements / prose)
VERIFY: python tools/project_state.py --check rights-movements --stage prose   (passes only after writer C)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/rights-movements/part1-before-1800.md (eras 1-5) · manuscript/rights-movements/part2-1800s.md (eras 6-7)
        · manuscript/rights-movements/part3-1900s-and-today.md (eras 8-10) · research/research-rights-movements.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-329b done; self-review of eras 8-9 complete
NEXT:   T-329c: unit 10

## Research state before writing (2026-09-29)

PASS  rights-movements / research
measured: stage=RESEARCHED eras=10/10 stories=26 (v26 c0 t0) verify_tags=0 bank=89988w outline=41091w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-329a | done | 523w, validator 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-329a | done | 582w, validator 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-329a | done | 1856w, validator 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-329a | done | 791w, validator 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-329a | done | 2088w, validator 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-329a | done | 4413w, validator 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-329a | done | 9340w, validator 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-329b | done | about 11,570w, validator 0 errors, emdash=0 semicolon=0 |
| 9 | era 09 1950-2000 -> part3 | T-329b | done | about 9,580w, validator 0 errors, emdash=0 semicolon=0 |
| 10 | era 10 2000-today -> part3 | T-329c | todo | |
| 11 | final: self-review, --punct, validator, prose check | T-329c | todo | |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- era 1 | wampum definition, five nations, date range, location | PATCH (copied from research-education + onondaganation.org/history) | PATCH 2026-09-30 (T-329a): wampum, the five nations...
- era 3 | who the Quakers were; Dyer 1657 jailing; William Penn | PATCH (Famous Trials; copied LOC via research-religion) | PATCH 2026-09-30 (T-329a): who the Quakers were...
- era 5 | Declaration equality sentence | PATCH (National Archives) | PATCH 2026-09-30 (T-329a): the Declaration's equality sentence
- era 6 | Lovejoy killing and the Alton trials (who was charged, verdicts) | PATCH (Lincoln, Alton Trials 1838, full text; EWB) | PATCH 2026-09-30 (T-329a): Elijah Lovejoy's death...
- era 6 | who Frederick Douglass was | PATCH (copied from research-slavery-freedom) | PATCH 2026-09-30 (T-329a): Frederick Douglass...
- era 2 | when/where Las Casas gave up his encomienda | PATCH (Encyclopedia.com / EWB: Cuba, 1514) | PATCH 2026-09-30 (T-329a): when and where Las Casas gave up his encomienda
- era 8 | Tulsa grand jury, Rowland arrest, deputizing | PATCH (copied from research-crime-justice, DOJ 2025 and Ellsworth OHS) | PATCH 2026-09-30 (T-329b): Tulsa 1921, the arrest...
- era 8 | NAACP founders and signers (was search summary only) | PATCH (naacp.org Our History) | PATCH 2026-09-30 (T-329b): the NAACP founders
- era 8 | Black women's vote after 1920 | PATCH (NPS) | PATCH 2026-09-30 (T-329b): Black women's vote after 1920
- era 8 | definition of eugenics, 30 states / 60,000 | PATCH (NHGRI) | PATCH 2026-09-30 (T-329b): what eugenics was
- era 8 | Radium Girls two-year limit (was search summary only) | PATCH (History.com); 1928 hearing dates still unconfirmed, left out | PATCH 2026-09-30 (T-329b): the Radium Girls' two-year limit
- era 8 | who shot James Wakasa and what happened to him | PATCH (JANM, Discover Nikkei) | PATCH 2026-09-30 (T-329b): who shot James Wakasa
- era 8 | Night of Terror account: whose log | PATCH CORRECTION (Stevens, Jailed for Freedom: it is Lucy Burns's) | PATCH 2026-09-30 (T-329b): CORRECTION
- era 8 | Randle still living? | PATCH (search: no death report) | PATCH 2026-09-30 (T-329b): Lessie Benningfield Randle
- era 8 | Pearl Harbor, Pullman porters, "feeble-minded" | PATCH (copied from war, work-workers, education banks) | PATCH 2026-09-30 (T-329b): two context facts
- era 9 | Freedom Riders' number and departure (was search summary) | PATCH (NPS: eleven, 4 May 1961) | PATCH 2026-09-30 (T-329b): the Freedom Riders' departure
- era 9 | who led the Anniston mob; anyone punished | SEARCHED, NOT FOUND | SEARCHED, NOT FOUND 2026-09-30 (T-329b): who led the Anniston mob
- era 9 | first Christopher Street march 1970 (was search summary) | PATCH (NYC LGBT Historic Sites) | PATCH 2026-09-30 (T-329b): the first Christopher Street Liberation Day March
- era 9 | Title IX sponsors and renaming (was search summary) | PATCH (NPS Patsy Mink; House History) | PATCH 2026-09-30 (T-329b): Title IX's sponsors
- era 9 | five Brown cases (was search summary) | PATCH (NPS) | PATCH 2026-09-30 (T-329b): the five Brown cases
- era 9 | Relf and Willowbrook details for a span | PATCH (copied from research-health) | PATCH 2026-09-30 (T-329b): the Relf sisters and Willowbrook
- era 9 | what the Citizens' Council was | PATCH (Mississippi State University Libraries) | PATCH 2026-09-30 (T-329b): what the Citizens' Council was

## OPEN (should be rare)

## Outline claims left out
- era 2: the outline's summaries of the two Valladolid cases ("by nature fit to be ruled by force", "theft and murder") are not in the bank. Prose states only the question and who argued which side.
- era 2: "A rule written in Spain did not reach a mine in the Indies" (a line built to land, no source).
- era 6: "societies against drink" (temperance as a training ground for women organizers): nothing in the bank for 1800-1850.
- era 6: Sarah Roberts's age (5) not in this bank; left out.
- era 7: Charlotte E. Ray's "C. E. Ray" application story: bank marks it unconfirmed; left out.
- era 7: Waddell's 7 November 1898 speech and the "75 masked men" at the Memphis jail: unconfirmed search summaries; left out.
- era 8: 1928 Radium Girls hearing dates and September adjournment (search summary only); left out.
- era 8: outline's "The famous marches of the 1960s used ideas that were already old" and "It was a respectable opinion at the time. Universities taught it" (eugenics): no source; left out.
- era 8: outline's Alice Paul claim that all suffrage prisoners were freed after five weeks: bank says only that Paul was; prose says that.
- era 8: Clara Lemlich (parked, work-workers' event), restrictive covenants (case unverified), MS St. Louis and quotas (not organizing): not used.
- era 9: Anniston mob size, chains and iron rods, door held shut (search summary only); left out.
- era 9: Stonewall marches in other cities on 27-28 June 1970 (not confirmed); left out. Named Stonewall participants: not sourced; left out.
- era 9: Evers funeral and Spingarn Medal (search summary only); Kameny's degree and war service (search summary); Pauli Murray co-writing NOW's statement (search summary); left out.
- era 9: Capitol Crawl date (NPS July 1990 vs common 12 March 1990): no date given.
- era 9: flight attendants (Roads, Banks: "verify details"), Reinaldo Arenas, urban renewal and redlining figures: not used.
- era 9: outline's "four movements running at once" span folded into the era zoom; farmworkers named in one sentence; Alcatraz and Wounded Knee given one short span with the fish-ins (parked, sourced).
- era 7: Harlan's third quoted sentence ("arouse race hate") not used. Two Harlan quotations carry the dissent.

## Decisions and defects fixed
- era 3: outline gave no year for Dyer's gallows reprieve; bank PATCH settles 27 October 1659 (Endecott's order of 26 Oct). Used.
- era 3: outline said four meetings "put off deciding"; kept, and Germantown land named as Lenape (bank SNF wording).
- era 3: Blackstone moved from era 3 to era 5 (Abigail Adams story), where his 1765-1769 date belongs.
- era 4: outline "roughly eighty-six years" and "about twenty years after" corrected from bank PATCH: 1776 ban, 1778 first disownments, 88 years.
- era 5: outline stated the 1807 New Jersey party motive as settled; bank records a dispute (NPS vs NJ Historical Commission vs MoAR). Prose states the agreement (party advantage and a fraud scandal) and the disagreement.
- era 5: outline's "An organization outlives the people who start it" dropped: the 1775 society stopped meeting in November 1775 and revived in 1787. Dinah Nevil's case (the society's founding case) added from bank PATCH.
- era 5: quotations containing em dashes (Abigail and John Adams) split at the dash, no word changed. Hutchinson church charge split at its semicolon.
- era 1-5: every cross-reference to other chapters in the outline (`slavery-freedom` carries...) removed from prose (fourth wall).
- era 6: outline "In 1819 Congress gave it 23,000 acres" kept at 1819 (bank PATCH); state money given as $5,000 in October 1816, not an 1819 annual grant. Whose Alabama land: bank SNF, prose says the records do not say.
- era 6: outline's Lovejoy lines ("five bullets", "found not guilty") rested on Wikipedia only. New PATCH from the 1838 court report (Lincoln, *Alton Trials*): the defenders were prosecuted first; eleven mob members were tried only for riot and the press, and acquitted 20 January 1838; no one was charged with the killing. Prose now says exactly that.
- era 6: outline's "Oberlin ... first college to make that a policy" kept as bank states; Oberlin land added (AMAM wording). Seneca Falls land added (Cayuga). Betsy Love's court reason #3 attributed to the NPS account (it may be NPS's words, not the court's).
- era 6: Maria Stewart's NPS quotation contains an em dash; paraphrased. Declaration of Sentiments "education" grievance split at its dash.
- era 7: outline blockquote lines ("> ...") in the Anthony and Tape stories would render as record continuations in the viewer; rewritten as prose paragraphs. Anthony's exchange split at every em dash, no word changed.
- era 7: *Sex in Education; or, ...* title contains a semicolon; prose gives the title and the subtitle separately.
- era 7: outline's Boston 1855 and Wilmington 1898 were separate; kept separate spans (Boston moved into date order after the Truth story).
- era 7: outline "the only time the United States wrote one named nationality out of citizenship" not used; Britannica's wording used (bank PATCH). Standing Bear "first to sue" not used.
- era 7: outline said Sojourner Truth "met President Lincoln" in the same sentence as the streetcar case with a stray "also and"; rewritten. Streetcar injury left out (unconfirmed).
- era 7: outline's line "So the most quoted sentence any Black American woman said..." was a closing line built to land; replaced with the facts (Gage's version from memory, dialect, thirteen vs five children, NWHM's word).
- era 7: Haudenosaunee-to-suffragists link (Stanton 1891, Gage 1893) added as a short span, handed forward from the era-1 research agent; it ties back to era 1's clan mothers.
- era 7: Ward v. Flood told inside the Tape story as the precedent the Tapes faced (named people, from the decision text).
- era 8: bank and outline attributed the Night of Terror log ("Seized by guards from behind...", handcuffed to the bars) to Alice Paul. Jailed for Freedom shows it is Lucy Burns's log. Prose attributes it to Burns. CORRECTION PATCH in bank. The outline span still says Paul (audit item).
- era 8: outline "no white person went to prison" rewritten to follow the sources: grand jury indicted about 70 men, many of them Black Greenwood leaders; no white man went to prison for the killings or burning; Gustafson convicted of dereliction and removed.
- era 8: added spans from the bank not in the outline: Sanger (era-7 Comstock handoff), Marian Anderson 1939, Elizabeth Peratrovich 1945, Native organizations 1911-1944 (parked), Anthony's death 1906, Wells's death 1931, Alpha Suffrage Club 1913, Dyer silent march 1922.
- era 8: every cross-chapter pointer in the outline removed from prose.
- era 9: outline's thirteen Freedom Riders corrected to NPS's eleven (PATCH). Prince Edward Kennedy quotation split at its em dash, no word changed. McLaurin quotation split at its semicolons.
- era 9: outline's "Twenty-one men were arrested... No Mississippi jury convicted anyone... until 2005" kept; outline's "a young man named Jimmie Lee Jackson" given his age, 26 (bank PATCH).
- era 9: added from the parked bank sections: Levittown and the Myers family (1957), Greensboro counter opened 25 July 1960, Memphis sanitation strike inside the King story, Percy Green's Arch climb (1964), fish-ins and the Boldt decision (1974), Warren County (1982).
- eras 8-9: institution-as-actor sentences repaired in the self-review (NAACP, FBI, Army, Congress, companies, boards, states); courts kept as "the Supreme Court ruled", matching part2.

## TO PARK (for the director, burst runs only)

## HANDOFF from T-329a to writers B (eras 8-9) and C (era 10)
Files: part1-before-1800.md (eras 1-5), part2-1800s.md (eras 6-7). Voice: plain, dated, actor named in every harm; no cross-chapter pointers in prose; stories open with their teaching point in the first two sentences.
**Terms already defined (do not define again):** rights movement (era 1); coverture, feme covert, feme sole (era 3); heresy, blasphemy, banished, magistrate, General Court (era 3); whipping, ear cropping, tongue bored with a hot iron (era 3); charter (era 2); denounce, disown/disownment, apostate (era 4); abolitionist (era 3); petition, boycott, segregated (era 6); insane in the 1800s sense, poorhouse, memorial (era 6, Dix); suffrage, disfranchised (era 7); lynching (era 7, Wells); habeas corpus (era 7, Standing Bear); allotment (era 7); deported (era 7, Geary Act); transgender (era 7, Frances Thompson); bar / admitted to the bar, lobbied (era 7); Freedmen's Bureau (era 7); public conveyances (era 7); the 13th, 14th (citizenship, equal protection) and 15th Amendments (era 7).
**Threads that continue after 1900 (era 8 picks up):**
- Women's vote: NAWSA formed 1890 (merger); Minor v. Happersett left only an amendment; Mott (d. 1880) and Stanton (d. 1902) death years are in the bank but not printed in prose. Anthony's death and the 19th Amendment are era 8's.
- Ida B. Wells: last seen 1895 (A Red Record, marriage). Era 8 has the 1909 NAACP founding and the 1913 procession; her death day is disputed (NPS 25 March vs NWHM 15 March 1931).
- Comstock Act (1873) still in force: Sanger era 8. Clarke 1873 and Jacobi answered.
- Plessy v. Ferguson (1896) stands until Brown 1954; the "organized test case" pattern (Anthony 1872, Tapes 1884, Comité 1892) is set up for the NAACP legal campaign.
- Chinese exclusion: extended 1892, permanent 1902, repealed 1943 (stated in era 7). Wong Kim Ark 1898 told.
- Native citizenship: Elk v. Wilkins (1884) told; the Indian Citizenship Act 1924 is era 8's. Dawes Act and the 138 to 48 million acres (1887-1934) stated.
- Disability: the deaf school (1817) and Dix's asylums (13 in 1843, 123 by 1880) stated; the bank flags that those institutions later held disabled people for life (era 8-9 material). Benjamin and Sarah Lay (era 4) described by body only, not diagnosed.
- LGBTQ: Frances Thompson (1876) is the first fact in the thread.
- Boston schools: 1855 law told, with NPS's note that segregation policies continued.
- Wyoming kept women's vote at statehood 1890; Utah regained it 1896.

## HANDOFF from T-329b to writer C (era 10)
File: part3-1900s-and-today.md already holds eras 8 and 9 (hb-chapter line, heading and hb-note naming eras 08-10 are in place). Append era 10 after `<!-- hb-time:end id="1950-2000" -->`.
**Terms already defined in eras 8-9 (do not define again):** picket, hunger strike, forcible feeding, filibuster, abridged, ratify, deputize, grand jury, dereliction of duty, exonerated, martial law, National Guard, eugenics, sterilize, salpingectomy, tubal ligation, hysterectomy, statute of limitations, executive order, curfew, court-martial, manslaughter, vacated, dissent, friend-of-the-court brief, gay, charter, warrant, literacy test, pacifist, chain gang, vagrancy, homicide, felony conspiracy, blackjack, sharecropper, union, relief, domestic worker, inherently, dissident.
**Threads that continue into era 10:**
- Tulsa: the survivors' span in era 8 already runs to 2026 (2024 dismissal, Van Ellis d. 2023, Fletcher d. 24 Nov 2025, Randle last known survivor in 2026 unpaid, 55 remains, C. L. Daniel and James Goings). Do not retell. The Greenwood Trust (June 2025) and the DOJ review (Jan 2025) are not told in era 8.
- Equal Rights Amendment: era 9 ends at the 1982 deadline, three states short. Nevada 2017, Illinois 2018, Virginia January 2020 are era 10's.
- Voting Rights Act: era 9 states preclearance; Shelby County v. Holder (2013) is era 10's.
- Federal anti-lynching law: never passed in eras 8-9; the Emmett Till Antilynching Act (2022) is era 10's.
- ADA signed 26 July 1990; what happened to it afterwards is era 10's. Judy Heumann d. 2023 already stated.
- Claudette Colvin d. 13 January 2026 already stated in the Rosa Parks story. Rustin pardon 2020 and Obama medal 2013 already stated. Korematsu 1983 and redress 1988-1990 stated.
- Title IX: era 9 gives the 2012 and 2013-14 figures; era 10 carries later rulings.
- Stonewall: 1969 and the 1970 march told; the 2016 national monument is unconfirmed in the bank.

## Log
- 2026-09-30 T-329a unit 1 landed: part1 era 01, 523w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 2 landed: part1 era 02, 582w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 3 landed: part1 era 03, 1856w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 4 landed: part1 era 04, 791w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 5 landed: part1 era 05, 2088w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 6 landed: part2 era 06, 4413w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 7 landed: part2 era 07, 9340w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329b unit 8 landed: part3 era 08, about 11,570w (after self-review), validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329b unit 9 landed: part3 era 09, about 9,580w, validator 0 errors, --punct emdash=0 semicolon=0. Self-review of eras 8-9 run and repairs applied.
