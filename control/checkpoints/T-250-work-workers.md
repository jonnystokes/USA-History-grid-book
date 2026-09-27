# CHECKPOINT T-250 | work-workers | patch + bank check | eras 1-10

STATUS: DONE (director verified: patch PASS, research PASS)
VERIFY: python tools/project_state.py --check work-workers --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/work-workers.md · research/research-work-workers.md · workspace/work-workers.md

NOW:    finished
NEXT:   director: commit. Later audit: see OPEN.

## Measured before dispatch (2026-09-27)

FAIL patch: stories=17 (15 verified, 0 candidate, 2 target), 0 [VERIFY], bank 8,486w against
outline 4,123w, validator 0 errors. Before 1500, the 1500s and 1750-1800 have no story
(allowed). Gate blockers:

- line 240 `laid-off-industrial-worker` (target, 1950-2000): a laid-off steel or auto worker.
  Avoid repeating another chapter's story: `economy`'s finished prose already tells Gerald
  Dickey (Youngstown). Search `outlines/` and `manuscript/` for the person before choosing
  (ignore `outlines/BOOK-OUTLINE.md`, a compiled copy).
- line 267 `gig-driver` (target, 2000-today). T-248 parked Barbara Ann Berwick in this bank,
  but `transportation` already carries her as the story `barbara-berwick`. Prefer a different
  named, documented app driver, told from the job's angle (pay, hours, classification). If no
  other is documented, AGENT-BRIEF §7 allows a shared person with a chapter-suffixed slug, told
  only through this chapter's angle, with a `Shared with:` line.

Each must become a real, named, documented person whose story the bank sources, or be handled
honestly (never invent a name; an unnamed documented account becomes hb-zoom prose, and the
hb-story block is removed). Keep slugs unique across the book.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | the two target stories | done | `frank-lumpkin` (era 09, Wisconsin Steel 1980) and `raef-lawson` (era 10, Grubhub) written, verified, bank PATCHes under eras 09 and 10. --stage patch PASS. |
| 2 | fold in the parked sections that serve this chapter (ten are listed at the end of the bank) | done | pointer PATCHes eras 06-10, outline span bullets added |
| 3 | bank check, eras 1-5 | done | 02 Acoma pointer, 03 servants/runaways/Martin's Hundred land |
| 4 | bank check, eras 6-10 | done | see Log; perishables refreshed |
| 5 | final: flags, validator, both checks | done | all progress=researched, validator 0, patch PASS, research PASS |

## SUBJECT NOTES (from the director)

Registry angle: the daily job: what work was like, who did it, pay, hours, safety, unions and
strikes. Check the registry for the exact line and neighbours (`economy` for the economy as a
whole, `slavery-freedom` for the system of slavery, `immigration` for arrival).

The bank has ten "Parked from" sections left by other chapters' agents. Unit 2 reads them and
brings what serves this chapter into its eras (as PATCHes or by pointing the outline to them).
Do not rewrite their text.

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the bank):
enslaved and indentured labor as work (hours, punishment, who owned and who profited) · child
labor (ages, hours, deaths, who employed them, the laws and who fought them) · workplace deaths
(Triangle 1911: the owners, the locked doors, 146 dead; mines; the Hawks Nest tunnel, 1930s,
with the contractor and the disputed count) · violence against strikers (Haymarket, Homestead
1892, Pullman 1894, Ludlow 1914, Memorial Day 1937: who fired, who ordered, the dead) · farm
workers (the bracero program, the UFW, pesticides) · 2000-today: wage theft, heat deaths,
warehouse injuries, gig classification, with dated figures.

Perishable: every 2000-today figure (union membership, minimum wage, workplace deaths, gig
figures). Date each figure and refresh to 2026 where a newer official figure exists (BLS is the
default source).

## Sources in hand
- Ninth Circuit, Lawson v. Grubhub, 13 F.4th 908 (2021) PDF, cdn.ca9.uscourts.gov: Lawson's hours, blocks, termination, procedural history.
- govinfo.gov USCOURTS-cand-3_15-cv-05128-18 (Dkt. 449, March 13, 2026): 2023 ABC ruling, $24.75M settlement terms.
- Gizmodo March 31, 2023 ($65.11); Courthouse News July 30, 2026 (final approval, 60,000 drivers, $10,000 award).
- Chicago History Museum finding aid (CARLI): Lumpkin 1916-2010, closed March 28 1980, $14.5M 1988. CPL blog 2025: 3,300 workers, bounced checks, $17M of $40M. People's World obituary 2010 (partisan, labeled). Chicago History Museum blog 2024 (600 dead by 1987).

## Gaps researched

## OPEN (should be rare)
- Several facts carry (unconfirmed: search summary only): 1877 national toll ~100, Hammer 5-4 vote and sons' names, Lawrence LoPizzo details, UFW pesticide contract dates, minimum-wage 2009 date (no DOL page opened), Amazon's response. Audit may confirm.
- Hawks Nest: company count 109 is search-summary only.

## Outline claims left out

## Decisions and defects fixed
- Radium Girls AUDIT ITEM (from rights-movements) resolved: National Archives blog confirms $10,000 (some sources $15,000), $600 annuity, medical costs, Settlement Agreement June 8, 1928. Donohue: collapse Feb 10 1938, award April 5, appeal thrown out July 6, died July 27, final victory Oct 1938.
- Era 10 union figure updated to 2025 (10.0%, 14.7M); OSHA line updated to CFOI 2024 (5,070). Era 10 self-referential 'current through 2026' lines removed.

## Log
- 2026-09-27 Bank PATCHes now in eras 02, 03, 06, 07, 08, 09, 10 (unit 2 folds + units 3/4 bank check). Perishables refreshed: BLS union 2025 (10.0%, 14.7M), CFOI 2024 (5,070), heat rule status, Starbucks/ALU 2026. Next: outline spans for the new material, then unit 5.
- 2026-09-27 Units 2+4 merged by era: era 07 and era 08 PATCHes written to bank (parked items folded; 1877 strike, Haymarket/Pullman actors, Lattimer, child-labor numbers; Lawrence, Keating-Owen/Hammer, Hawks Nest, Memorial Day 1937, braceros 10%, Radium audit item RESOLVED via National Archives). Next: eras 09, 10, then 01-06, then outline spans.
- 2026-09-27 Unit 1 done. Barbara Berwick not reused (transportation's). Dickey/Neufeldt avoided (economy's).
