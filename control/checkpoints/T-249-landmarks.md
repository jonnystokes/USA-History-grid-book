# CHECKPOINT T-249 | landmarks | patch + bank check | eras 1-10

STATUS: DONE (director verified: patch PASS, research PASS)
VERIFY: python tools/project_state.py --check landmarks --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/landmarks.md · research/research-landmarks.md · workspace/landmarks.md

NOW:    finished.
NEXT:   director: commit, close IN-FLIGHT.

## Measured before dispatch (2026-09-27)

FAIL patch: stories=17 (15 verified, 0 candidate, 2 target), 0 [VERIFY], bank 5,060w against
outline 4,653w (barely above the size bar, and thin for 17 stories), validator 0 errors.
The 1500s has no story (allowed). Gate blockers:

- line 30 `tribal-preservation-officer` (target, era 1 area): a named tribal historic
  preservation officer (or similar documented steward) at a mound or great-house site.
- line 59 `castillo-builder` (target): a laborer who built the Castillo de San Marcos at
  St. Augustine (1672-1695). Check `research/research-transportation.md` and
  `research/research-city-building.md`, which may hold sourced St. Augustine material.

Each must become a real, named, documented person whose story the bank sources, or be handled
honestly (never invent a name; an unnamed documented account becomes hb-zoom prose, and the
hb-story block is removed). Keep slugs unique across the book (ignore `outlines/BOOK-OUTLINE.md`,
a compiled copy).

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | the two target stories | done | glenna-wallace (era 1, new Hopewell span) + john-collins-castillo (era 3, new 'Who cut the stone' span); slugs replaced; bank PATCHes in eras 01 and 03; --stage patch PASS (bank 7,543w / outline 5,335w) |
| 2 | check that each of the 15 verified stories' key facts are in the bank; source any that are not | done | gaps sourced: Jefferson/Virginia Capitol (era 5), Bartholdi dates (era 7), Lincoln Memorial/Taft/Moton, Rushmore NPS facts + Black Hills actors (Custer, 1876 ration cutoff, Manypenny, 1877 Act, 17.1M+5%), Borglum Stone Mountain dismissal (NPS), Quebec Bridge 75/76 dead, 33 Kahnawake (era 8). Unsourced outline bits flagged in bank: Monticello 'half-built', Bartholdi 'saw it lit', Stone Mountain '1915' |
| 3 | bank check, eras 1-5 | done | Mesa Verde 26 tribes, Castillo labor + Seloy land, Alamo residents (SNF: church builders), Capitol payrolls, Virginia Capitol (SNF: enslaved builders) |
| 4 | bank check, eras 6-10 | done | Brooklyn Bridge 21/27/40 named dead, St. Louis mounds, Lincoln Memorial Taft/Moton, Rushmore/Black Hills actors, Quebec Bridge, Confederate monuments 2025, EJI memorials, 2012 Capitol marker |
| 5 | final: flags, validator, both checks | done | all 10 eras progress=researched; validator 0 errors; patch PASS, research PASS (bank 12,188w / outline 5,726w) |

## SUBJECT NOTES (from the director)

Registry angle: notable built structures and monuments. Not: cities as a whole
(`city-building`), houses (`home-family`).

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the bank):
who built each landmark (enslaved people at the White House and the Capitol, with the payments
recorded to their enslavers; forced Native labor at Spanish missions and forts; workers killed
building bridges, dams, skyscrapers and Mount Rushmore, with sourced counts) · whose land each
landmark stands on (Mount Rushmore and the Black Hills, the 1868 treaty and the 1980 ruling;
Devils Tower/Bear Lodge; mound sites destroyed by farmers and builders) · monuments to the
Confederacy (who paid for and put them up, when, and the removals, with dated counts) ·
memorials to violence (the National Memorial for Peace and Justice, the lynchings it records).

Perishable: every 2000-today figure (Confederate monument counts and removals, memorial
openings, renamings). Date each figure and refresh to 2026 where a newer figure exists.

## Sources in hand
- Manucy, The Building of Castillo de San Marcos (NPS 1942/1961), Gutenberg 47216: Castillo labor, Collins, costs, dates. NPS Handbook 149 (1993) part 2 on penelope.uchicago.edu: corroborates. NPS casa African Americans timeline: 1687 freedom seekers.
- American Indian Magazine (Hancock, 2025/26), NPS HCE inscription article, Court News Ohio 2022-12-07, Ideastream 2024-08-01, OHC Wallace profile, WYSO 2026-09-15 (Wallace retired, Samples chief).

## Gaps researched

## OPEN (should be rare)
- none

## Outline claims left out
- Not removed from the outline, but flagged unsourced in the bank: Monticello 'half-built', Bartholdi 'saw it lit', Stone Mountain '1915', 'speech vetted'. Existing outline prose still has em dashes (pre-V2 text, writers rewrite); all text added in T-249 has none.

## Decisions and defects fixed
- Era-1 line 'the book does not invent people' (self-reference) replaced with the Mesa Verde descendants line.
- Wikipedia's 2024 date for the Hopewell listing corrected to 2023 in the bank.

## Log
- 2026-09-27 Units 3/4 mostly landed: Capitol payrolls (Allen 2005: 385 payments, $60/yr to owners incl. Thornton, Scott, Hoban; 2012 marker), St. Louis mounds leveled (Big Mound 1869, 16 in 1904) + Osage Sugarloaf 2025 (Andrea Hunter THPO), Confederate monuments (UDC, two peaks, SPLC 2025: 2,086 standing/415 removed; Pike reinstalled Oct 2025; Arlington memorial back 2027; Charlottesville Lee melted 2023; Heyer/Fields), Peace and Justice memorial 2018 + Freedom Monument park 2024. --stage research PASS (bank 11,510w).
- 2026-09-27 Unit 1 done. Validator 0 errors. Perishable: Wallace retired Sept 2026 (written as chief 2006-2026).
