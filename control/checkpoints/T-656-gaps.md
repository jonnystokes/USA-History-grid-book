# CHECKPOINT T-656 | science, slavery-freedom, storytelling-evolution, styles, technology | gaps | GAPS-FINAL items 1-6

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check <slug> --stage prose (and --stage research) for each touched slug
BRIEF:  control/briefs/GAPS.md + control/briefs/GAPS-FINAL-DISPATCH.md (section T-656)
MODEL:  opus
FILES:  research/research-{science,slavery-freedom,storytelling-evolution,styles,technology}.md · manuscript/<those slugs>/... · (item 2 only: the matching Hemings sentence in other chapters' manuscript files, listed below)
SCRATCH: C:\Users\jon\AppData\Local\Temp\claude\C--Users-jon-Projects\60b4fd0b-3ca5-4e19-ac34-4e7802a1ccd8\scratchpad\T-656\

NOW:    all six items done; final --check prose and research PASS on all five slugs (2026-10-26)
NEXT:   director review (see Decisions: Gordon-Reed sentence in the Hemings passage)

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 2 | slavery-freedom part1 era 5: named historians calling Jefferson/Hemings (and Wayles/E. Hemings) rape; book-wide grep and align | CLOSED (T-656) | Kendi's own text checked (IA full-text search): "more or less forced", "began a sexual relationship", no "rape": LitCharts wording was not his (bank correction). Gordon-Reed 2008 argues love/consent per Foner's NYT review; Morgan 1999 and Walker 2009 reject the label; Foner: record silent. Johnson stays the only named historian calling it rape. Prose: new 4-sentence paragraph "Historians disagree...". Wayles: SEARCHED, NOT FOUND. Book-wide grep: only slavery-freedom carries the claim, no other file edited. Bank PATCH + SNF T-656 in research-slavery-freedom.md era 5. validator 0, punct 0/0, --check prose+research PASS |
| 1 | science era 10: named survey for AI tools in labs (Nature 2023, Van Noorden and Perkel) | CLOSED (T-656) | Nature news feature 27 Sep 2023 (Nature 621, 672-675): standfirst + opening sentence readable without login. New 3-sentence paragraph in part3 era 10 protein zoom crediting Van Noorden and Perkel. Bank PATCH T-656 era 10. validator 0, punct 0/0, --check PASS |
| 3 | storytelling-evolution part1 era 5: "His Excellency and Lady" at Valley Forge Cato = the Washingtons? | CLOSED (T-656) | Nancy K. Loane, Following the Drum (2009), IA full-text snippet: "May 11 Martha Washington and her husband attended the camp production of ... Cato". Prose adds one sentence crediting Loane (attendance only, she is not shown glossing the title). Bank PATCH era 5. validator 0, punct 0/0 |
| 4 | storytelling-evolution part1 era 3: tavern spellings Cowle's / Cole's (optional, bank only) | CLOSED (T-656), bank only | "Cole's Tavern" confirmed as the later name (John Cole kept Fowkes's tavern): Henry A. Wise 1962 and R. L. Johnson 1989 via IA full-text, both resting on Whitelaw 1951. "Cowle's": SEARCHED, NOT FOUND. No prose change |
| 5 | styles part3 era 8: Ann Lowe great-grandfather enslaved great-grandmother? | CLOSED (T-656) | Judith Thurman, New Yorker 2021 (curl): "Georgia's father owned the plantation where she and her enslaved mother worked as seamstresses." Prose: 3 sentences under #32 (enslaved on an Alabama plantation, owner was great-grandfather, held her as property, could not refuse; their daughter Georgia was Ann's grandmother). Bank PATCH in Ann Lowe section. validator 0, punct 0/0, --check PASS |
| 6 | technology part2 era 7 row 24: Brown 2020 Proc. IEEE on Bell and Gray | CLOSED (T-656) | Abstract via OpenAlex: three sets of evidence (correspondence, notes from a Bell associate, engineering details) show Bell and his attorneys did not plagiarize Gray. Prose adds 2 sentences after the title. Bank PATCH. validator 0, punct 0/0, --check PASS |

## Other chapters' files edited (item 2 only)

None. The grep found the claim only in slavery-freedom part 1.

## Sources in hand

- https://ericfoner.com/reviews/100508nyt.html : Foner's NYT review of Gordon-Reed 2008 (what she argues; record silent)
- Internet Archive full-text search API (archive.org/services/search/beta/page_production/?service_backend=fts&user_query=...): snippets of Kendi 2016, Lewis and Onuf 1999 (Morgan), Walker 2009. Script: scratch T-656/fts.py

## Gaps researched

## Decisions and defects fixed

- Item 2: the Hemings passage now reports the dispute (#28 rule 4): Johnson calls Jefferson a rapist, Gordon-Reed argued the two loved each other (as Foner's review reports her 2008 book), Foner answered that neither left a record of their feelings. The plain facts before it are unchanged. Director may prefer to drop the Gordon-Reed and Foner sentences and keep only Johnson.
- Bank correction: Kendi 2016 does NOT say "raping"; LitCharts's wording was the guide's own (earlier T-483/T-617/T-640 lines). Kendi: "more or less forced to settle for the overtures of a sexually aggressive forty-four-year-old".

## Log

- 2026-10-26 | item 6 | technology part2 era 7 + bank PATCH | validator 0 | punct 0/0 | all five slugs --check prose+research PASS
- 2026-10-26 | item 5 | styles part3 era 8 + bank PATCH | validator 0 | punct 0/0 | --check PASS
- 2026-10-26 | items 3-4 | storytelling-evolution part1 era 5 sentence + bank PATCHes eras 3 and 5 | validator 0 | punct 0/0 | --check prose+research PASS
- 2026-10-26 | item 1 | science part3 era 10 + bank PATCH | validator 0 | punct 0/0
- 2026-10-26 | item 2 | slavery-freedom part1 era 5 paragraph + bank PATCH/SNF | validator 0 errors | punct 0/0
