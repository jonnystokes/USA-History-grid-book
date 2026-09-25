# STATUS — what is done, what is next

**Rewritten 2026-09-05** from a full audit of the tree. The previous version was
~4 weeks stale and wrong in both directions: it undercounted the outline by more
than half and listed two finished chapters as untouched seeds. Every number here
was measured, not inherited.

⚠ **The numbers in this file are a narrative snapshot and will go stale.** For
the real state run `python tools/project_state.py` — it measures every chapter
from the files. Where the two disagree, the script is right. Start any session
with `control/RESUME.md`.

⚠ **The plan in this file is superseded (2026-09-07).** The project now runs in three
phases — **research everything → write everything → audit everything** — with no auditing
interleaved between chapters. `control/ROADMAP.md` is the plan; this file is narrative
background only. Defects found while writing are parked in `control/AUDIT-QUEUE.md`, not
fixed on the spot.

**Two chapters are finished and pass `--check --stage prose`:** `native-nations` (12,826
words) and `city-building` (13,768 words). Both were written against the pre-2026-09-07
style guide, so they are queued for a language audit against its new sections.

**The twelve gating decisions are answered** (2026-09-06) — see `control/DECISIONS.md`
for the rulings and `control/hard-subjects-policy.md` for the binding tone rules.
Research is no longer blocked on Jon.

**The plan to finish lives in `control/ROADMAP.md`.** This file is the live
tracker; the roadmap is the sequence. Update the row every time a chapter moves
a stage. Designed so work can stop and restart at any point without losing the
thread.

## The viewer is back — compatibility is a hard contract

**`viewer/viewer.html` (v2)** — restored 2026-09-05 from the laptop import, with
`viewer/viewer-v1.html` beside it as the backup. **Every file we produce must pass
it.** Contract: the code-derived `control/VIEWER-CONTRACT.md` (authoritative) and
`control/VIEWER-COMPAT.md`.

Its v2 rendering is confirmed present: bullet lists (`<ul class="md-list">`),
whole-line comment stripping, and `[VERIFY…]` ochre badges. **Use v2, never the v1
backup, to review outlines** — v1 predates all three, so the 796 bullet lines in
`outlines/BOOK-OUTLINE.md` collapse into run-on paragraphs there.

⚠ **Line 89 of either viewer is a ~373,500-character base64 image.** Never read
either file whole; read around that line and truncate greps.

Validate any file with `node tools/validate_grid.js <file>` (0 errors required).
**Caution: the validator always exits 0, even when it reports errors** — read the
printed count, never the exit status, and do not build a loop or CI check on its
exit code until that is fixed.

Key rules: own-line single-line markers · all ten eras per chapter ·
`chapter=` = slug · globally unique story slugs (chapter-suffix shared people;
`tools/dedup_story_slugs.py`) · no comments inside blocks · prose/bullets only
inside blocks.


## Where the book stands

| Measure | Value |
|---|---|
| Chapters | **37** (was 35 — see `control/DECISIONS.md`), all with valid ten-era grid outlines |
| Compiled outline | **534 stories, 140,833 words** |
| Grid validation | 37/37 files clean, 0 errors |
| Research complete | **20 of 37** |
| Research remaining | **17** (the 15, minus art-music, plus art + music + storytelling-evolution) |
| Finished prose | **0 words** — `manuscript/` is empty |
| Open director decisions | **~140** — the 12 gating ones are RULED (`control/DECISIONS.md`); the rest are per-chapter housekeeping |
| Unique `[VERIFY]` tags | **128** (100 outlines, 28 banks) |

Prose scale: the v1 `exploration` chapter ran 9,047 words, so 35 chapters is
**~300,000–315,000 words**. That is the bulk of the remaining project.

## Pipeline

`SEED` → `RESEARCHED` (agent filled the outline + wrote the research bank) →
`APPROVED` (Jon reviewed the outline) → `WRITTEN` (ship-quality prose) → `DONE`
(Jon approved the prose)

`RESEARCHED*` below means researched with known gaps — unfilled story slots or a
bank that does not cover its outline. Those are patched in ROADMAP Phase 3.

## How the work runs

One **research sub-agent per chapter**. Each reads `control/AGENT-BRIEF.md`,
replaces `outlines/<slug>.md` with a full outline, and writes
`research/research-<slug>.md`. The director reads only the outline file, then
updates this tracker.

Director loop after each agent: `node tools/validate_grid.js outlines/<slug>.md`
→ `python tools/build_book_outline.py` → validate compiled → flip the row here.

## Chapters

| # | slug | Stage | Notes |
|---|------|-------|-------|
| 01 | exploration | **RESEARCHED** (corrected 2026-09-05) | Was wrongly listed SEED. 34 stories, 25 verified, 0 targets, 1 VERIFY, 18.7 KB bank. Bank is in the old 7-section format — reformat to ten eras, add per-fact citations, flip `progress` flags |
| 02 | native-nations | **RESEARCHED — COMPLETE** | Prose-ready. 21 verified stories, bank 11.7k w (1.65× outline), all 10 eras full; 12 disputes logged honestly. Open: boarding-school prose depth; Alaska Native / Hawaiian vs territories split |
| 03 | land-environment | **RESEARCHED\*** | Content complete, no placeholders. Blocked only on re-verifying **Bears Ears** (Jul 2026 proclamation, litigation promised). Territories land-story gap open |
| 04 | immigration | **RESEARCHED\*** | 21 stories; bank still lacks a specific indentured-servant record; before-1500 and 1500s cells thin (114 w / 86 w). Trim approval pending |
| 05 | migration | **RESEARCHED\*** | 15 stories; `recent-mover` unfilled; 1900–1950, 1950–2000, 2000-today all thin for the chapter's own core century |
| 06 | city-building | **RESEARCHED — COMPLETE** | Prose-ready. 14 verified, no placeholders. 7 director Qs outstanding |
| 07 | home-family | **RESEARCHED\*** — weak | 4 targets + 2 candidates of 16 unfilled; both 2000-today stories are placeholders; lowest source density in the book; carries part of the unsourced kitchen thread |
| 08 | technology | **RESEARCHED\*** | 23 stories but 3 unfilled slots + 1 candidate; kitchen-thread items parked unsourced |
| 09 | science | **RESEARCHED — COMPLETE** | Prose-ready. 25 verified, no placeholders, every era carries a story |
| 10 | energy | **RESEARCHED\*** — weakest | Only 6 of 11 stories verified; 3 targets, 2 candidates; two eras have no story; bank smaller than the outline. Navajo uranium ownership question unresolved |
| 11 | transportation | **RESEARCHED\*** | 1 unfilled slot; bank (4,613 w) smaller than the outline it backs (5,255 w). 7 director Qs |
| 12 | landmarks | **RESEARCHED\*** | 2 unfilled slots incl. all of the 1500s; 1800–1850 thin (284 w); bank < outline |
| 13 | elements | **RESEARCHED\*** | 10 stories, but the first five eras (before-1500 → 1800–1850) carry **no** individual stories. Element 120 current through 2026 |
| 14 | work-workers | **RESEARCHED\*** | 2 unfilled slots (1950–2000, 2000-today); 1750–1800 thin with no story; 1900–1950 overloaded at 7 — trim approval pending |
| 15 | food-farming | **RESEARCHED\*** | 3 unfilled slots (lowcountry rice grower, farm daybook, ration-book household) |
| 16 | economy | **RESEARCHED\*** | No placeholders but only 11 stories; six eras carry exactly one — thinnest verified roster with no gaps declared |
| 17 | money | **RESEARCHED\*** | 2 unfilled slots; 12 stories, six eras carry exactly one |
| 18 | marketplace | **RESEARCHED\*** | Largest outline (9,317 w), thinnest backing (7,470 w bank), 3 unfilled slots |
| 19 | big-business | **RESEARCHED** (corrected 2026-09-05) | Was wrongly listed SEED. 14 stories / 13 verified, `progress="researched"` ×10, sources inline, 9/10 eras with real content (2 honestly empty). **Its `hb-note` claims a full bank that does not exist** — write the bank up from the outline |
| 20 | government-politics | SEED-RICH | 7/10 eras seeded, 22 VERIFY, 8 targets, 6 KB parked from immigration/food-farming/money. Work is verification, not discovery. Owns part of the territories question |
| 21 | crime-justice | SEED-THIN | 1/10, 14 targets, 2.5 KB parked. **Gated on the hard-subjects tone policy** (lynching, convict leasing) |
| 22 | war | SEED-THIN+ | 2/10, 22 targets, **0 verified stories**, 7.5 KB parked from 5 chapters. Gated on tone policy + the Civil War split ruling |
| 23 | america-world | SEED-THIN — **worst** | 2/10, 6 stories, 4 eras `state="empty"`, **no research bank file at all**. Carries the **territories** thread, the book's largest coverage hole. Research this first |
| 24 | slavery-freedom | **RESEARCHED\*** | 24 stories; `africatown-descendant` unfilled, `milla-granson` still a candidate; 1900–1950 and 1950–2000 marked full on one story each. Eras 6–7 carry seven blocks — trim approval pending |
| 25 | rights-movements | SEED-RICH | MAJOR. 5/10 eras, 26 VERIFY, 10 targets, 0 verified stories — but the **largest parked bank in the book** (18.9 KB from 9 chapters). Mostly assembly, not discovery |
| 26 | health | SEED-THIN | 2/10, 14 targets, 8.4 KB parked from 5 chapters. Gated on tone policy (Tuskegee, 1918 flu) |
| 27 | disasters | SEED-THIN | 1/10, 18 targets, 8 KB parked from 6 chapters (strong material: Camp Fire, Triangle) |
| 28 | drugs-alcohol | SEED-THIN | 0/10, 16 targets, 2.8 KB parked. Gated on tone policy (addiction, overdose) |
| 29 | religion | SEED-RICH | 7/10, 31 VERIFY, 10 targets, 1.9 KB parked. Open: how Native spiritual traditions are described |
| 30 | education | SEED-RICH — richest | Jon's school-system spine fully placed; 8/10 eras richly seeded, 3,715 w. **67 [VERIFY] items** and 20 targets — the work is clearing that queue |
| 31 | news-communication | SEED-THIN | 0/10 verified, 11 candidate stories, 5.4 KB parked |
| 32 | art | SEED-THIN | **New 2026-09-06** — the art half of the split art-music: painting, sculpture, photography, writing. Film and theatre left for `storytelling-evolution`, music for `music` |
| 33 | music | SEED-THIN | **New 2026-09-06** — split out of art-music on Jon's ruling (music is not physical art). Flagship modern story: **Dolly Parton**, d. 25 Aug 2026, `candidate` on one source (Rep. Burchett's statement) with a long research-target list |
| 34 | storytelling-evolution | SEED-THIN | **New 2026-09-06** — acting and story: oral and Native performance traditions, theatre, minstrel and vaudeville stages, silent film, radio drama, TV, New Hollywood, video games, AI performance. Not called "Film": early filmed drama was a recorded stage play |
| 35 | styles | SEED-THIN | 1/10, 7 stories — thinnest story set in the book |
| 36 | sports-play | SEED-THIN | 2/10, 12 targets. Remit widened 2026-09-06: what children and adults do to entertain themselves and how it changed — outdoor play through to phones and gaming. The ADHD question is contested research, never an assertion |
| 37 | holidays | SEED-THIN | 0/10, 12 VERIFY, 10 targets, 2 KB bank |

**Afterword** `how-we-know` — not started; not a grid chapter (no eras).

## Immediate to-do (ROADMAP Phase 0 + 1)

1. Fix `art-music`'s five false `verified` tags — a clean validator run hides them.
2. Make `tools/validate_grid.js` exit non-zero on errors.
3. ✅ Done 2026-09-05 — `templates/chapter-template.md` rebuilt as a v3 prose
   skeleton (validates clean), and `control/grid-markers.md` corrected against
   the shipped parser. No v3 stamper is needed: in v3 the markers are the
   authoring container, so prose is written directly into them.
4. **Answer the 12 gating decisions** — six hard-subject tone rulings and six
   structural splits. They block five unresearched chapters. See ROADMAP §1a/1b.

## Research order

**america-world** (territories, no bank) → the tone-policy batch (war, health,
crime-justice, drugs-alcohol, disasters) → the verification batch (education,
rights-movements, government-politics, religion) → the from-scratch remainder
(art-music, news-communication, sports-play, styles, holidays) → bank cleanup
(exploration, big-business).

## Style enforcement (Jon, 2026-08-08) — still live

Jon caught style-guide violations in researched outlines (teaser openings that
withhold facts for effect; em-dash pivots). Two-part fix, unchanged:

1. **Forward:** AGENT-BRIEF §9 tightened — the style guide BINDS outline
   era-zoom/span sentences, not just prose. Test: could the line drop into the
   finished book unchanged? Every research agent gets this.
2. **Repair at write time:** the 16 outlines researched before that date get
   their style violations fixed **during Phase 4**, chapter by chapter, as each
   is written. No separate fix pass.

## Format: grid v3

All 35 outlines are in the v3 grid-marker format (`control/grid-markers.md`):
`hb-chapter mode="outline"`, ten `hb-time` sections each with `hb-zoom`
(era/span) + in-cell `hb-story` blocks, `state`/`progress`/`status` attributes,
one `hb-note` orientation block. Planning scaffolding lives in
`workspace/<slug>.md` (35 files). The SAME parser reads a single outline, the
compiled outline, or finished prose.

## Master outline (build artifact)

`outlines/BOOK-OUTLINE.md` — all 35 chapters combined, grid-parseable,
regenerate any time:

```
python tools/build_book_outline.py
```

Never edit it directly; edit `outlines/<slug>.md` and rebuild. Rebuilt
2026-09-05: **35 chapters, 534 stories, 140,833 words, 0 errors.** It had been
stale by 6 stories. Rebuild after every research agent finishes.

## Infrastructure

- ✅ Research banks renamed to slug names; one legacy file remains by design:
  `research-ch17-prejudice.md`, split three ways by the slavery-freedom agent.
- ✅ Old v1 stamper retired to `_reference/`; `node tools/validate_grid.js` is
  the validator now.
- ✅ Story-slug dedup tool: `tools/dedup_story_slugs.py`. **Gap:** it globs only
  `outlines/` and skips BOOK-OUTLINE and _TEMPLATE, so it will not police slug
  uniqueness once prose lands in `manuscript/`.
- ✅ `templates/chapter-template.md` rebuilt for v3 prose (2026-09-05).
- ❌ `tools/validate_grid.js` always exits 0.
- ❌ No builder equivalent to `build_book_outline.py` for a prose manuscript.
- ~128 `[VERIFY]` tags outstanding — research agents resolve these as they go.

## Reading order for a fresh session

`STATUS.md` (here) → `control/ROADMAP.md` → `control/chapter-registry.md` →
`control/AGENT-BRIEF.md` → the chapter's `outlines/<slug>.md`.
