# CHECKPOINT T-329 | rights-movements | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-9 (part3), writer C: era 10 (part3) + final

STATUS: T-329a landed (director verified: FAIL  rights-movements / prose)
VERIFY: python tools/project_state.py --check rights-movements --stage prose   (passes only after writer C)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/rights-movements/part1-before-1800.md (eras 1-5) · manuscript/rights-movements/part2-1800s.md (eras 6-7)
        · manuscript/rights-movements/part3-1900s-and-today.md (eras 8-10) · research/research-rights-movements.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-329a done; self-review of part2 complete
NEXT:   T-329b: unit 8

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
| 8 | era 08 1900-1950 -> part3 | T-329b | todo | |
| 9 | era 09 1950-2000 -> part3 | T-329b | todo | |
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

## OPEN (should be rare)

## Outline claims left out
- era 2: the outline's summaries of the two Valladolid cases ("by nature fit to be ruled by force", "theft and murder") are not in the bank. Prose states only the question and who argued which side.
- era 2: "A rule written in Spain did not reach a mine in the Indies" (a line built to land, no source).
- era 6: "societies against drink" (temperance as a training ground for women organizers): nothing in the bank for 1800-1850.
- era 6: Sarah Roberts's age (5) not in this bank; left out.
- era 7: Charlotte E. Ray's "C. E. Ray" application story: bank marks it unconfirmed; left out.
- era 7: Waddell's 7 November 1898 speech and the "75 masked men" at the Memphis jail: unconfirmed search summaries; left out.
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

## Log
- 2026-09-30 T-329a unit 1 landed: part1 era 01, 523w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 2 landed: part1 era 02, 582w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 3 landed: part1 era 03, 1856w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 4 landed: part1 era 04, 791w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 5 landed: part1 era 05, 2088w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 6 landed: part2 era 06, 4413w, validator 0 errors, --punct emdash=0 semicolon=0.
- 2026-09-30 T-329a unit 7 landed: part2 era 07, 9340w, validator 0 errors, --punct emdash=0 semicolon=0.
