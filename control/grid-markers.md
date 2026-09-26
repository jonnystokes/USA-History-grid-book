# Grid Markers — one machine-readable format for outlines AND the final book

**LOCKED, v3 (2026-07-23) · corrections 2026-09-05.** The format is unchanged; the 2026-09-05 pass fixed statements that did not match the shipped parser, each one verified against `viewer/viewer.html` (v2). Mechanical detail lives in `control/VIEWER-CONTRACT.md`, which outranks this file on parser behaviour.

**The grid.** The book is a **grid**: subjects across, time down, zoom in from era → span → story. The finished product is a program where you scroll **down through time**, slide **left and right through perspectives**, and **zoom in** to individual true stories.

**One format, two uses.** The **outline** files and the **final prose** files use the *same* markers, so the same parser renders either one as a grid. An outline is a *compressed book*: same cells, thinner contents. The only differences are `mode="outline"` vs `mode="prose"` and how much text sits inside each block.

Worked examples: `control/SAMPLE-chapter-format.md` (prose) and `outlines/_TEMPLATE.md` (outline). These are hand comments; a normal Markdown viewer hides them and shows clean text.

---

## 1. The markers at a glance

| Marker | Pairs? | Wraps | Attributes |
|--------|--------|-------|-----------|
| `hb-chapter` | no | top of each file | id, slug, title, part, mode, [file] |
| `hb-note` / `/hb-note` | yes | editor's dev-only notes | — |
| `hb-time:start` / `hb-time:end` | yes | one era section | id, order, chapter, label, state, progress |
| `hb-zoom` / `/hb-zoom` | yes | one block of narration | level, [label] |
| `hb-story:start` / `hb-story:end` | yes | one featured person | slug, name, movie, kind, status |

Inside a time section, every block of text lives in **either** an `hb-zoom` **or** an `hb-story` block — never loose.

## 2. Attribute reference (names chosen so nothing clashes)

- **hb-chapter** — `id` (chapter number, may change; **zero-padded, and the display sort key**) · `slug` (STABLE key, never changes; **repeating a slug merges the files into one chapter**) · `title` · `part` (1–9) · `mode` = `outline` \| `prose` · `file` (optional source-file stem)
  - ⚠ The viewer **reads only `id`, `slug` and `title`.** `mode`, `part` and `file` are stored or ignored and change nothing on screen — keep them for humans and for our own tools, but never rely on them to alter rendering.
- **hb-time** — `id` (era slug; **this is what identifies the row**) · `order` (`01`–`10`) · `chapter` (chapter slug) · `label` · `state` = `full` \| `thin` \| `empty` (did the subject exist?) · `progress` = `seed` \| `researched` \| `written` (how finished this cell is — the shading)
  - ⚠ `order` is **not** the sort key — the viewer uses its own hard-coded era table (§6) and ignores `order` entirely. Keep it accurate anyway for our tooling and for humans reading the raw file.
  - Only `state` is validated. `progress` is printed as a badge without checking, so a typo shows up as a badge with no styling rather than an error.
- **hb-zoom** — `level` = `era` \| `span` · `label` (optional; give one on spans)
- **hb-story** — `slug` (**globally unique across the whole book**, not just in the chapter) · `name` · `movie` (real film + year, or `""`) · `kind` = `famous` \| `ordinary` · `status` = `target` \| `candidate` \| `verified`
  - ⚠ Neither `kind` nor `status` is validated; each becomes a CSS class. An unknown value renders an unstyled badge silently — which is how five `art-music` stories sat falsely marked `verified`.
  - ⚠ `movie` is **never rendered**. The film styling comes from the `> **Movie:**` record line alone, and nothing cross-checks the two. Keep them in sync by hand.
- **hb-note** — none.

Three separate ideas, three separate names, no collision: **state** (did it exist) · **progress** (how done the cell is) · **status** (how firm a story is) · **mode** (outline vs prose).

## 3. hb-chapter — top of every file

```html
<!-- hb-chapter id="04" slug="immigration" title="Immigration to America" part="2" mode="outline" file="part1" -->
# Chapter 4: Immigration to America
```
Multi-file chapters repeat this line in each file (same id/slug/title/part/mode; own `file`). The parser groups every file by `slug`.

## 4. hb-note — editor's in-development notes (parsed OUT of the final product)

```html
<!-- hb-note -->
Angle: … · Keep out: … · Workspace: workspace/immigration.md
Anything here is development scaffolding, not book content. The final parser strips it.
<!-- /hb-note -->
```
Used for: the orientation block at the top of an outline; the intro and table of contents in the compiled file. **The final product removes every `hb-note` block.** Nothing inside one is ever shown to a reader.

## 5. hb-time — one era section (start/end pair)

```html
<!-- hb-time:start id="1600s" order="03" chapter="immigration" label="The 1600s" state="full" progress="seed" -->
## The 1600s
    …zoom and story blocks…
<!-- hb-time:end id="1600s" -->
```
- **A thin or empty era is a correct answer, never a problem to solve.** Jon's ruling
  2026-09-06: do not pad a cell to make it look full, and do not merge unlike subjects
  to avoid blank-looking cells. State what is true and move on.
- `state="empty"` → subject did not exist yet: one `hb-zoom level="era"` block with the honest sentence, no story. `state="thin"` → little to tell. `state="full"` (default) → all three zooms.
- `progress` shades the cell in the viewer: `seed` (bare outline) → `researched` (fleshed outline + verified bank) → `written` (final prose). An outline cell is usually `seed` then `researched`; a finished prose cell is `written`.
- A single era is **never** split across two files. ⚠ This is a rule, not a guarantee: a repeated era id **silently overwrites** the earlier one and everything in it is lost, with no error from the viewer or the validator.

## 6. Canonical time registry — IDENTICAL in every chapter

| order | id | label | | order | id | label |
|-------|-----|-------|-|-------|-----|-------|
| 01 | `before-1500` | Before 1500 | | 06 | `1800-1850` | 1800 to 1850 |
| 02 | `1500s` | The 1500s | | 07 | `1850-1900` | 1850 to 1900 |
| 03 | `1600s` | The 1600s | | 08 | `1900-1950` | 1900 to 1950 |
| 04 | `1700-1750` | 1700 to 1750 | | 09 | `1950-2000` | 1950 to 2000 |
| 05 | `1750-1800` | 1750 to 1800 | | 10 | `2000-today` | 2000 to Today |

## 7. hb-zoom — the three zoom depths

A section moves wide → close and may pull back out and in again. Blocks are a **flat sequence** in reading order; `level` gives depth.

| Zoom | Marker | What it holds |
|------|--------|---------------|
| **1 — the whole era** | `<!-- hb-zoom level="era" -->` … `<!-- /hb-zoom -->` | wide framing of the whole era. Every non-empty section opens with one. |
| **2 — a shorter span** | `<!-- hb-zoom level="span" label="…"> ` … `<!-- /hb-zoom -->` | a decade, movement, place, or law inside the era. Always give a `label`. |
| **3 — a single story** | `<!-- hb-story:start …>` … `<!-- hb-story:end …>` | one real documented person. This **is** zoom 3 — never wrap a story in `hb-zoom`. |

Reusing an `era` or `span` block after a story = the narrator pulling back out before the next story (the intended weave). Comments do not nest; keep blocks flat and let `level` carry depth.

## 7b. Parser-compatibility rules (the shipped viewer enforces these. Full list in `VIEWER-COMPAT.md`)
- Every `hb-*` marker sits **alone on its own line**, as a **single-line** comment. Attributes double-quoted, no `"` in values.
- **All ten eras present in every chapter**, including `state="empty"` ones. `chapter="…"` = the chapter **slug**.
- **Story slugs are globally unique across the whole book.** Same person in several chapters → suffix each with the chapter slug (`benjamin-franklin-technology`, `benjamin-franklin-money`).
- Chapter `id` stays zero-padded two digits (it is the sort key).
- Inside blocks: paragraphs, `**bold**`, `*italic*`, links, `> **Key:** value` records, and `- ` / `* ` bullets only (bullets need viewer **v2**). **No headings-as-content, no tables, no code blocks, no images, no nested or numbered lists, no HTML, and never a comment inside a block.**
- ⚠ **`> **Key:** value` records render only inside `hb-story`.** Put one in an `hb-zoom` and it is parsed and thrown away. It appears nowhere, with no error.
- ⚠ **An unclosed `hb-zoom` or `hb-story` is never reported** by the viewer or the validator. Its content is silently lost. Close every block, and close the last one before end of file.

## 8. hb-story: a featured person (zoom level 3)

```html
<!-- hb-story:start slug="annie-moore" name="Annie Moore" movie="" kind="famous" status="verified" -->
### Annie Moore
> **Who:** … · **When and where:** … · **Movie:** Title (Year)  ← only when a real film exists
…the story (prose) or the outline note…
<!-- hb-story:end slug="annie-moore" -->
```
- `movie` filled = a matching `> **Movie:**` blockquote line is present; `movie=""` = no Movie line. Never invented.
- `kind` = famous / ordinary (the book features both on purpose).
- `status` = **target** (a research target, not yet a named person — e.g. name reads "(target) an Irish famine immigrant") · **candidate** (named but not yet fully verified) · **verified** (facts confirmed). In finished prose every story is `verified`.

## 9. Outline vs prose — the only differences

| | Outline file (`mode="outline"`) | Final prose file (`mode="prose"`) |
|---|---|---|
| block contents | terse notes, bullet seeds, candidate names | full plain-language prose |
| `hb-time progress` | `seed` → `researched` | `written` |
| `hb-story status` | mix of target / candidate / verified | all `verified` |
| planning scaffolding | in `workspace/<slug>.md`, **not** in the file | not present |
| same markers, same parser | ✅ | ✅ |

So the **same viewer** renders `outlines/<slug>.md`, the compiled `outlines/BOOK-OUTLINE.md`, or a finished `manuscript/<slug>/…` file — a live compressed book that fills in over time.

## 10. Workspace files — the planning layer (not parsed into the grid)

Each chapter has `workspace/<slug>.md`: the editor's working file between research, outline, and final prose. It holds the **shared-events table, the famous-names checklist, the [VERIFY] queue, and open questions** — everything that would clutter the grid. It is never parsed as book content and never rendered in the viewer. Template: `workspace/_TEMPLATE.md`.

## 11. How the program reads the grid

- **Scroll down:** a chapter's sections by `order` 01→10 (across all its files).
- **Slide sideways:** every chapter's section with the same `order`, sorted by chapter `id`.
- **Coordinates:** `slug` × `order`. `slug` stable, `id` for display order.
- **Zoom:** walk each section's block sequence — `era` outer, `span` middle, `story` closest.
- **Shade cells** by `state` (empty/thin/full) and `progress` (seed/researched/written).
- **Story cards:** each `hb-story` with `name`/`kind`/`status`. ⚠ There is **no films list** in the shipped viewer, and the `movie` attribute is never displayed — a film reaches the reader only through its `> **Movie:**` record line.
- **Strip for final:** drop every `hb-note` block. ⚠ The shipped viewer does **not** do this: an era-level note renders behind the "Editor notes" toggle (off by default), and chapter- and book-level notes are parsed but never displayed at all. Stripping is a job for our build step, not the viewer.

## 12. Keeping markers correct

- Start chapters from the templates — `outlines/_TEMPLATE.md` for an outline, `templates/chapter-template.md` for prose (rebuilt for v3 on 2026-09-05). Markers come free.
- **No stamper is needed.** The retired `add_chunk_markers.py` existed to bolt v1 markers onto unmarked prose; in v3 the markers *are* the authoring container, so prose is written straight into them.
- Check every file with `node tools/validate_grid.js <file>` — but read the printed error count, **not** the exit status, which is always 0. And remember the validator never runs the renderer, so it cannot see any of the ⚠ items above.
- `##` / `###` headings are the human layer; the comments are the machine layer. Keep them saying the same thing.
