# VIEWER SPEC — build the grid viewer for "A History of the United States"

**Hand this whole file to the AI that builds the viewer program. It is self-contained.** For live test data, also give it `outlines/BOOK-OUTLINE.md` (all 35 chapters in one file) and any `outlines/<slug>.md`. Two worked example files exist too: `control/SAMPLE-chapter-format.md` (prose) and `outlines/_TEMPLATE.md` (outline) — optional, this spec embeds a complete example below.

---

## 1. What you are building

A history book laid out as an **interactive grid**:
- **Columns = 35 subject chapters** (Immigration, Slavery and Freedom, Technology, …). Each is one *angle* on American history.
- **Rows = 10 fixed time eras**, always the same, in this order: Before 1500 · The 1500s · The 1600s · 1700 to 1750 · 1750 to 1800 · 1800 to 1850 · 1850 to 1900 · 1900 to 1950 · 1950 to 2000 · 2000 to Today.

The reader can:
- **Scroll down** a column → one subject across all ten eras.
- **Slide left/right** → one era across all 35 subjects (what everything was doing at that moment).
- **Zoom into a cell** → three depths: the whole era (wide) → a shorter span → an individual true story.

The source is **Markdown files with HTML-comment markers**. The markers are the machine layer; the visible `##`/`###` headings and prose are the human layer. Same file works in a normal Markdown viewer (comments hide) and in your program (comments parsed).

**One format, two stages.** The same markers describe the current **outline** (`mode="outline"`, terse) and the eventual finished **prose** (`mode="prose"`, full text). Your parser handles both identically; a `progress` attribute tells you how finished each cell is, so you can shade the grid and literally watch the book fill in.

---

## 2. The data model your parser should output

```
Book
 └─ chapters[]           (one per file-group, keyed by slug)
     ├─ id               "04"        chapter number (may change; do not key on it)
     ├─ slug             "immigration"   STABLE key — group and key on this
     ├─ title            "Immigration to America"
     ├─ part             "2"         which of 9 book parts
     ├─ mode             "outline" | "prose"
     └─ sections[]       (the ten eras, order 01–10)
         ├─ id           "1600s"     era slug (stable, same in every chapter)
         ├─ order        "03"        01–10 — SORT ROWS BY THIS, never parse the label
         ├─ label        "The 1600s"
         ├─ state        "full" | "thin" | "empty"        did the subject exist?
         ├─ progress     "seed" | "researched" | "written"   how finished this cell is
         └─ blocks[]     (reading order; a flat sequence)
             ├─ {type:"zoom",  level:"era"|"span", label?, text}
             └─ {type:"story", slug, name, movie, kind:"famous"|"ordinary",
                               status:"target"|"candidate"|"verified", text}
notes[]  = every hb-note block's text (development-only; DROP for the reader view)
```

---

## 3. The markers (complete)

| Marker | Form | Attributes |
|--------|------|-----------|
| chapter declaration | `<!-- hb-chapter id="04" slug="immigration" title="…" part="2" mode="outline" file="part1" -->` | id, slug, title, part, mode, file(optional) |
| editor note (drop for readers) | `<!-- hb-note --> … <!-- /hb-note -->` | none |
| time section | `<!-- hb-time:start id="1600s" order="03" chapter="immigration" label="The 1600s" state="full" progress="seed" --> … <!-- hb-time:end id="1600s" -->` | id, order, chapter, label, state, progress |
| zoom block | `<!-- hb-zoom level="era" --> … <!-- /hb-zoom -->` and `<!-- hb-zoom level="span" label="…"> … <!-- /hb-zoom -->` | level, label(optional) |
| story block | `<!-- hb-story:start slug="annie-moore" name="Annie Moore" movie="" kind="famous" status="verified" --> … <!-- hb-story:end slug="annie-moore" -->` | slug, name, movie, kind, status |

**Attribute value sets:** `mode` = outline\|prose · `state` = full\|thin\|empty · `progress` = seed\|researched\|written · `level` = era\|span · `kind` = famous\|ordinary · `status` = target\|candidate\|verified · `movie` = a real film "Title (Year)" or empty string.

---

## 4. Parsing rules

1. **Read all files. Group by `slug`** (a chapter may be split across several files, each repeating `hb-chapter`; the compiled `BOOK-OUTLINE.md` has all 35 in one file — same rules).
2. **A time section** is everything between `hb-time:start` and its matching `hb-time:end` (match on `id`). A single era is never split across files.
3. **Order rows by the `order` attribute (01–10)**, never by parsing the label text.
4. **Inside a section, walk blocks in reading order.** Each block is a `hb-zoom … /hb-zoom` pair (type `zoom`, with `level`) or a `hb-story:start … hb-story:end` pair (type `story`). The text inside is the cell content.
5. **Zoom depth** comes from the block: `era` = outer, `span` = middle, `story` = innermost. Blocks are a flat list; the same section may have several `era`/`span` blocks (the narrator zooming back out between stories) — that is intentional, keep them in order.
6. **`hb-note` blocks** are development-only. Collect them into `notes[]` if you want, but **drop them from the reader-facing render** (they hold the intro, table of contents, and editor notes). To produce the clean book, delete every `hb-note … /hb-note` span.
7. The `##` heading after `hb-time:start` and the `###` heading after `hb-story:start` duplicate the `label`/`name` — use either; the marker attributes are authoritative.
8. **Be lenient:** attribute order is not guaranteed; treat missing `state` as `full`, missing `progress` as `seed`; ignore unknown attributes; markers are standard HTML comments so a comment-tolerant parse (or a regex over `<!-- … -->`) works.

---

## 5. Building the grid UI (suggested)

- **Grid:** 35 columns × 10 rows. Cell = (chapter `slug`, era `order`).
- **Scroll down** = fix a column, walk `order` 01→10. **Slide sideways** = fix an `order`, walk chapters by `id`.
- **Shade cells** by `state` (empty = greyed/collapsed, thin = light, full = normal) and by `progress` (seed → researched → written) so the reader/author sees how complete the book is — a live heatmap.
- **Zoom control per cell:** level 1 shows only `era` text; level 2 adds `span` blocks; level 3 reveals `story` blocks as cards.
- **Story cards** from each `story` block: `name`, a `kind` badge (famous/ordinary), a `status` badge (target/candidate/verified — mostly relevant while the book is still an outline), and, when `movie` is non-empty, a film link/label.
- **Films view:** collect every non-empty `movie` across the book.
- **Reader (final) mode:** drop all `hb-note`; render prose straight; hide `status`/`progress` chrome.

---

## 6. Complete worked example (every scenario)

This is a full, self-contained chapter file in **prose** mode. It shows: an empty era, a thin era, a full era with one story, a full era with multiple stories and the narrator zooming back out, a story WITH a film and one WITHOUT, and the multi-file note. (Outline mode is identical markers with `mode="outline"`, terser text, `progress="seed"`, and story `status` of target/candidate/verified.)

```markdown
<!-- hb-chapter id="04" slug="immigration" title="Immigration to America" part="2" mode="prose" file="part1" -->
# Chapter 4: Immigration to America

<!-- hb-note -->
Editor note — dropped for readers. Angle: arrival from other lands to stay.
<!-- /hb-note -->

<!-- EMPTY ERA: subject did not exist. state="empty", one era-zoom, no story. -->
<!-- hb-time:start id="before-1500" order="01" chapter="immigration" label="Before 1500" state="empty" progress="written" -->
## Before 1500
<!-- hb-zoom level="era" -->
No one came to this land from across the ocean to stay in this age; immigration had not begun.
<!-- /hb-zoom -->
<!-- hb-time:end id="before-1500" -->

<!-- THIN ERA: a little to tell. state="thin". -->
<!-- hb-time:start id="1500s" order="02" chapter="immigration" label="The 1500s" state="thin" progress="written" -->
## The 1500s
<!-- hb-zoom level="era" -->
Ships from Europe reached these shores, but almost no one came to stay.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="St. Augustine" -->
The one lasting exception: the Spanish founded St. Augustine in 1565.
<!-- /hb-zoom -->
<!-- hb-time:end id="1500s" -->

<!-- FULL ERA, MULTIPLE STORIES, NARRATOR ZOOMS BACK OUT, one film + one none. -->
<!-- hb-time:start id="1950-2000" order="09" chapter="immigration" label="1950 to 2000" state="full" progress="written" -->
## 1950 to 2000
<!-- hb-zoom level="era" -->
In 1965 the country reopened its doors, and the people who came changed.
<!-- /hb-zoom -->
<!-- hb-story:start slug="tung-trinh" name="Tung Trinh and the Bolinao 52" movie="Bolinao 52 (2008)" kind="ordinary" status="verified" -->
### Tung Trinh and the Bolinao 52
> **Who:** A Vietnamese refugee who survived a lost boat at sea.
> **When and where:** The open sea near the Philippines, 1988.
> **Movie:** Bolinao 52 (2008), a documentary.
In 1988, Tung Trinh was one of 110 people who fled Vietnam by boat; only 52 survived.
<!-- hb-story:end slug="tung-trinh" -->
<!-- hb-zoom level="span" label="the 1986 law" -->
Late in the century the country also faced people living in it without legal permission.
<!-- /hb-zoom -->
<!-- hb-story:start slug="reagan-amnesty-worker" name="(target) a legalized farmworker" movie="" kind="ordinary" status="target" -->
### (target) a legalized farmworker
Research target — a documented person legalized under the 1986 act. [in outline mode a story can be an unfilled target]
<!-- hb-story:end slug="reagan-amnesty-worker" -->
<!-- hb-time:end id="1950-2000" -->

<!-- ── THE SAME MARKERS IN OUTLINE MODE (mode="outline") — terser cells, progress seed/researched,
     and stories can be verified, candidate, or target. This is the "compressed book" the grid
     shows today; it swells to prose (mode="prose") later, no parser change. ── -->
<!-- hb-chapter id="24" slug="slavery-freedom" title="Slavery and Freedom" part="6" mode="outline" -->
# Chapter 24: Slavery and Freedom
<!-- hb-time:start id="1800-1850" order="06" chapter="slavery-freedom" label="1800 to 1850" state="full" progress="researched" -->
## 1800 to 1850
<!-- hb-zoom level="era" -->
The cotton boom; the domestic slave trade moves a million people; daily life and resistance under slavery.
<!-- /hb-zoom -->
<!-- hb-story:start slug="harriet-tubman" name="Harriet Tubman" movie="Harriet (2019)" kind="famous" status="verified" -->
### Harriet Tubman
Escaped slavery, then returned many times to lead others to freedom. [outline seed]
<!-- hb-story:end slug="harriet-tubman" -->
<!-- hb-story:start slug="nat-turner" name="Nat Turner" movie="" kind="famous" status="candidate" -->
### Nat Turner
Led an 1831 uprising — candidate story, details still to verify. [outline seed]
<!-- hb-story:end slug="nat-turner" -->
<!-- hb-time:end id="1800-1850" -->
```

That single example exercises **every marker and every attribute value**: `hb-chapter` (both `mode`s), `hb-note`, `hb-time` (state empty/thin/full, progress written/researched), `hb-zoom` (era + span), `hb-story` (movie present + empty, kind famous + ordinary, status verified + candidate + target).

**Multi-file chapters:** a long chapter splits into `part1`/`part2`/`part3` files, each repeating the `hb-chapter` line (same slug) and holding a contiguous subset of the ten eras. Your parser merges by slug and orders by `order`. A single era is never split.

---

## 7. Test data in the repo

- `outlines/BOOK-OUTLINE.md` — all 35 chapters compiled into one grid-parseable file (regenerate with `python tools/build_book_outline.py`). Today every cell is `mode="outline"`, `progress="seed"`; as chapters get researched and written, cells advance to `researched`/`written` and fill with prose. Build your parser against this and it will keep working through the whole project.
- Individual `outlines/<slug>.md` — one chapter each, same format.
- `control/grid-markers.md` — the authoritative marker spec (this file is the friendly summary of it).

## 8. Edge cases to handle
- Empty section: era-zoom only, no story. · Thin section: short. · Section with no `span`, or several. · Multiple stories per era. · Repeated `era`/`span` blocks mid-section (zoom back out). · `movie=""` vs a real title. · Story `status="target"` with a placeholder `name` beginning "(target)". · Attribute order not fixed; unknown attributes possible; treat missing `state`→full, `progress`→seed. · `hb-note` may appear anywhere (top of file, or the compiled file's intro/TOC) — always droppable.
