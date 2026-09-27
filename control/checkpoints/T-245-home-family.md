# CHECKPOINT T-245 | home-family | patch + bank check | eras 1-10

STATUS: DONE (director verified: patch PASS, research PASS)
VERIFY: python tools/project_state.py --check home-family --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/home-family.md · research/research-home-family.md · workspace/home-family.md
        (parking only: research/research-technology.md, research/research-energy.md)

NOW:    finished 2026-09-26
NEXT:   director: commit; see OPEN.

## Measured before dispatch (2026-09-26)

FAIL patch: stories=16 (10 verified, 2 candidate, 4 target), 0 [VERIFY], bank 5,703w against
outline 3,887w, validator 0 errors. STATUS.md calls it the lowest source density in the book.
Gate blockers are the six unfilled stories:

- line 25  `buffalo-bird-woman-home-family` (candidate, era 1 area)
- line 201 `levittown-family` (candidate, the Bladykas move-in)
- line 237 `mortgage-denied-family` (target)
- line 241 `early-homeschooling-family` (target)
- line 266 `foreclosure-family` (target, 2000-today)
- line 270 `school-at-home-household` (target, 2000-today, the 2020 school-at-home year)

Each target must become a real, named, documented person or family whose story the bank sources,
or be handled honestly as AGENT-BRIEF and the hard-subjects policy direct (never invent a name;
an unnamed documented account becomes hb-zoom prose, and the hb-story block is removed). Keep
slugs unique across the book.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | the two candidates: source and verify, or handle honestly | done | both verified; BBW moved to 1800-1850 |
| 2 | the four targets (eras 9-10) | done | Clyde Ross; Colfax family; Solon/Familia; Munoz family. New slugs: clyde-ross-home-family, colfax-family-homeschool, solon-familia-foreclosure, munoz-family-2020 |
| 3 | the kitchen thread (see notes) | done | cookstove re-sourced (Alice Ross); petticoat-fire claim is a myth (Theobald); washday (NPS Fort Scott); Census water/power/plumbing/fridge figures (Cardia NBER 2008; Census plumbing table; Lutz LBNL 2004). Outline era-06 stove span and era-08 span rewritten. Parked to technology (fridge %) and energy (heating fuel, electricity %). |
| 4 | bank check, eras 1-5 | done | land: Seloy/Timucua (1565), Patuxet/Wampanoag (search summary), Lenape at New Sweden; frontier-cabin nations and Hallowell NOT researched (noted) |
| 5 | bank check, eras 6-10 | done | slave-trade actors+counts (from slavery-freedom bank), Dakota land (Walnut Grove, Devils Lake), 1901 law corrected + actors, boarding-school laws/counts (from native-nations bank), HOLC/FHA map-makers, Myers mob, Countrywide/Fremont, perishables refreshed |
| 6 | final: flags, bank >= outline, validator, both checks | done | PASS patch, PASS research; bank 12,359w vs outline 5,460w |

## SUBJECT NOTES (from the director)

Registry angle: the house and the household: where Americans lived, who lived together, daily
life inside, including housing (cabin, tenement, mortgage, suburb). Not: city growth
(`city-building`), household appliances as inventions (`technology`). The workspace's shared-
events table gives the lead chapter for each shared event. Follow it.

**The kitchen thread.** An old note says a "kitchen thread" spans home-family, technology and
energy and is "entirely unsourced". No file defines it further. Treat it as: every claim in this
outline about the kitchen and household work (the hearth, cookstoves, iceboxes and
refrigerators, electric and gas appliances, washday, the kitchen after electrification) must be
sourced in this bank from this chapter's angle (what it did to daily life in the home, and who
did the work). Where the material is really about the invention (`technology`) or the power
supply (`energy`), park a short sourced note in that chapter's bank under a
"## Parked from `home-family` (2026-09-26, T-245)" heading. Do not edit their outlines.

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the bank):
enslaved households and families separated by sale (as household life, `slavery-freedom` leads
the system) · Native homes and children taken to boarding schools (as household loss,
`native-nations` and `education` lead) · redlining and restrictive covenants: who drew the maps
and who wrote the rules (HOLC, FHA officials, Levitt's whites-only sales) · tenement conditions
and deaths · domestic violence and child labor inside the home where the chapter touches them ·
the 2008 foreclosures (who made the loans) · homelessness.

Perishable: every 2000-today figure (household size, home ownership rates, homelessness counts,
foreclosure numbers). Date each figure and refresh to 2026 where a newer official figure exists.

## Sources in hand
- Waheenee (1921), Gutenberg 67133: BBW birth, mothers, lodge, smallpox deaths, 'house with chimneys'.
- nps.gov/knri Junior Ranger PDF: BBW 1839-1932, Wilson 1906-18.
- history.nd.gov Like-A-Fish-Hook: village by 1845, emptied late 1880s by allotment, flooded mid-1950s.
- ndstudies.gov gr8 smallpox 1837: St. Peters, June 18 1837, Chardon, 2,000 -> 138 Mandans.
- Getty/Newsday caption: Theodore and Patricia Bladykas, twins Patricia Ann and Betty Ann.
- nypan.org reproduction of Coates 2014 (Clyde Ross); chicagoreporter.com CBL; billmoyers.com 2014.
- thecrimson.com 1989-03-16 (Colfax); theava.com/archives/233213 (David Colfax obit).
- npr.org/transcripts/132146568 (Solon/Familia, Fremont, Wells Fargo); /907600197 (Munoz); /906952103 (Huballah). NPR pages time out in WebFetch; curl with a browser UA works.
- Patch Levittown; Encyclopedia.com Levitt (1954 Sat Eve Post quote).

## Gaps researched
- SEARCHED, NOT FOUND: 97 Orchard owner at the 1935 eviction; Clyde Ross's loan officer/bank.
- Homeschool 'how much lasted' partly settled (NCES 2023).

## OPEN (should be rare)
- Older outline cells (bullets, story records, Shared-with lines) still carry em dashes and semicolons. Era-zoom lines and all new/edited prose are clean. Writers must not copy that punctuation.
- Multigenerational figure (Pew 2021 data) not refreshed.

## Outline claims left out
- Era 10: 'New houses came wired for internet-connected locks, thermostats, and speakers' (no bank source) removed.
- Era 07 tenement: 'the 1901 law forced ... a toilet inside' corrected (new buildings: toilet per apartment; old: one per two families).
- Era 06 cookstove: 'by the Civil War the open hearth was mostly gone' not in the opened source; replaced.
- Kitchen-thread 'clothing catching fire was a real documented hazard' is a myth (Theobald); not used.

## Decisions and defects fixed
- BBW story moved from before-1500 to 1800-1850 (her documented household is the 1840s lodge). Before 1500 now has no story (allowed; derive_stage note).
- Levittown story renamed to Theodore and Patricia Bladykas, verified.

## Log
- Units 4-6 done 2026-09-26. Both gates PASS.
- Unit 3 done.
- Unit 1 done 2026-09-26. Validator 0 errors.
- Unit 2 done. --stage patch now PASS (v16 c0 t0, bank 8483w vs outline 4873w).
