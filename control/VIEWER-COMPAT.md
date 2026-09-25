# Viewer Compatibility — the real parser's contract

**Source of truth: the code in `viewer/viewer.html` (v2).** Analyzed 2026-08-07 from the original; the file went missing from the Desktop; the copy recovered there turned out to be v1, and the true v2 was restored from the laptop import on 2026-09-05. Both now live in `viewer/` inside the repo so they cannot go missing again. A code-derived companion, `control/VIEWER-CONTRACT.md`, records what the parser mechanically does; where the two disagree, VIEWER-CONTRACT wins.

Everything the book produces MUST satisfy this. `grid-markers.md` describes the format; this file records what the shipped parser actually enforces and tolerates. Verified end-to-end: `outlines/BOOK-OUTLINE.md` and `demo/DEMO-BOOK-OUTLINE.md` both parse with **0 errors**.

⚠ **Line 89 of either viewer is a single ~373,500-character base64 image** (~75% of the ~497 KB file). Never read the file whole — read around that line in ranges, and pipe any grep through a truncator.

## Hard requirements (parser errors if violated)
1. **Every `hb-*` marker sits alone on its own line, as a single-line comment.** The parser matches line-by-line (`^\s*<!-- … -->\s*$`). A marker sharing a line with anything else is misread; a multi-line hb comment is not a marker.
2. **Attributes are double-quoted** (`key="value"`); values may not contain `"`. Order free; unknown attributes ignored.
3. **Era ids must be exactly the canonical ten** (`before-1500` … `2000-today`); anything else errors.
4. **Every chapter must contain all ten eras** — including `state="empty"` ones. Missing eras error.
5. **`chapter="…"` on `hb-time:start` must equal the chapter's slug** (not its number).
6. `state` ∈ full|thin|empty · `hb-zoom` `level` ∈ era|span. Anything else errors.
7. **Closers must match openers:** `hb-time:end id` and `hb-story:end slug` are checked when present. **Correction (2026-09-05): only `hb-note` and `hb-time` are tracked on the stack — an unclosed `hb-zoom` or `hb-story` is never reported, and its content is silently lost.**
8. **Story slugs are GLOBALLY unique across the whole book** (not just per chapter). Same person in several chapters = distinct slugs. **Convention: suffix with the chapter slug** (`benjamin-franklin-technology`, `benjamin-franklin-money`). `tools/dedup_story_slugs.py` enforces this mechanically.

## Silent behaviors (no error, but shape the output)
9. **Chapters sort by `id` string compare** → ids must stay zero-padded two digits (`01`…`35`).
10. **`order` on hb-time is ignored** (the viewer uses its own era table). Keep it anyway for other tools.
11. **`part` and `file` attributes are ignored.** Multi-file chapters merge by `slug`; when several files are loaded they're sorted by FILENAME and concatenated, so name part files `part1-…`, `part2-…` to keep order.
12. **`hb-note` placement decides meaning:** before any chapter → book intro note; after `hb-chapter`, outside an era → chapter note (multiple accumulate); inside an era → that era's note (LAST one wins — use at most one per era).
13. **`progress` is displayed as a badge, not validated** — stick to seed|researched|written.
14. **`kind` and `status` drive badge colors** (famous=indigo, ordinary=brick; verified=green, candidate=ochre, target=slate).
15. **A record line `> **Movie:** …` gets film styling** (key matched by /movie|film/i). Keep the movie attribute AND the blockquote line in sync.

## The Markdown subset inside blocks (all a block's text gets this and only this)
- Paragraphs (blank-line separated) · `**bold**` · `*italic*` · `[text](http…)` links and bare URLs · blockquote records `> **Key:** value` (continuation `> more` appends to the last record) · bullet lists `- item` / `* item` (v2). **Records only render inside `hb-story` — inside an `hb-zoom` they are parsed and thrown away.**
- **Headings inside blocks are DISCARDED** (`#`–`######`) — the `##`/`###` headings next to markers are for humans; the attributes are authoritative. Never put content in a heading.
- **No tables, no code blocks, no images, no nested lists** — they render as literal text. Write prose (or bullets in outline mode).
- **Never put an HTML comment inside a zoom/story/note block.** (v2 drops single-line ones defensively; v1 rendered them as visible text. Multi-line comments inside blocks WILL leak as text.) Teaching/editor comments belong between blocks or in `hb-note`.
- Raw HTML is escaped and shows literally — don't write HTML in prose.
- `[VERIFY…]` tags render as small ochre badges (v2) — fine in outline mode, must be GONE from written prose.

## Loading model
Open/drop one or more `.md`/`.markdown`/`.txt` files — they're sorted by name, concatenated, parsed as one book. The compiled `BOOK-OUTLINE.md` alone, the whole `outlines/` folder, or `demo/DEMO-BOOK-OUTLINE.md` all work.

## v2 changes I made to the viewer — all three verified present (2026-09-05)

The real v2 arrived from the laptop and is now `viewer/viewer.html`; `viewer/viewer-v1.html`
is the backup. All three enhancements confirmed in the code:

1. **Bullet lists render** as real lists — `flushL()` emits `<ul class="md-list">`, CSS at
   lines 692–693. Outline mode is full of them (796 lines in the compiled outline).
2. **Stray single-line comments inside blocks are dropped** — `if(/^<!--[\s\S]*-->$/…)
   return;`, which is broader than originally described: it drops *any* whole-line comment,
   not only `hb-` ones. **Multi-line comments still leak as text.**
3. **`[VERIFY…]` tags styled** as ochre `<span class="vtag">` badges.

All three are additive; nothing that parsed before parses differently now.

⚠ **Never review outlines in `viewer-v1.html`** — it predates all three, so bullets collapse
into run-on paragraphs and VERIFY tags show as raw brackets.

## Fixes applied to OUR side after testing against the parser
- `build_book_outline.py` no longer emits one-line `hb-note` anchor wraps (they registered as 35 unclosed notes); anchors are now bare lines the parser ignores.
- 22 story slugs that appeared in multiple chapters were suffixed per chapter (`tools/dedup_story_slugs.py`); rule added to the spec.

## Checklist for every future file (agents: run through this)
Own-line single-line markers · all ten eras present · `chapter=` = slug · globally-unique story slugs (chapter-suffix when shared) · movie attr ↔ Movie line in sync · no comments inside blocks · no headings-as-content · prose/bullets only · zero-padded chapter ids · after building: `python tools/build_book_outline.py` must still parse error-free.
