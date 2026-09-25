# VIEWER-CONTRACT — what the shipped viewer actually reads

Derived 2026-09-05 by reading the viewer's JavaScript. **Revised the same day** after
the true **v2** build arrived from the laptop: the first pass analysed
`viewer-v1.html` by mistake (the file recovered from the Desktop was byte-identical
to v1 — MD5 `5e64c214…`), so its conclusions about bullets, comments and `[VERIFY]`
were wrong. Everything below now describes **`viewer/viewer.html` (v2, 498,203
bytes, banner "v2, 2026-08-07: bullet lists, comment-stripping, [VERIFY] tags")**.

Current layout: `viewer/viewer.html` (v2, use this) · `viewer/viewer-v1.html`
(backup, pre-v2 rendering). `tools/validate_grid.js` contains a copy of `parseGrid`
that is **identical in v2** (`RE_MARK` verified character-for-character).

Structural parsing (§1) is the same in both builds. Only the Markdown renderer
(`mdBlock`/`inline`) changed, so §1 held up; §2 and §3 are the parts that were
corrected.

⚠ **Line 89 of either viewer is a single ~373,500-character base64 image**, ~75% of
the file. Never read the file whole; read around it in ranges and truncate greps.

---

## 1 · Parsing rules — what the viewer looks for, mechanically

### 1.1 The two regexes

```js
const RE_MARK = /^\s*<!--\s*(\/?)(hb-[a-z]+)(:start|:end)?\s*([\s\S]*?)\s*-->\s*$/;
const RE_ATTR = /([\w-]+)\s*=\s*"([^"]*)"/g;
```

Consequences:
- A marker must occupy a **whole line** (leading/trailing whitespace only). Any other
  character on the line and `RE_MARK` fails; the line is buffered as block text and
  rendered as escaped literal prose.
- The name is `hb-` + **lowercase ASCII letters only**. `hb-Time`, `hb-time2`,
  `hb-my-marker` do not match and are treated as prose.
- Multi-line HTML comments are never markers.
- Attributes: **double quotes only**. `id='1600s'` is invisible to `RE_ATTR`.
- Attribute values may not contain `"` and may not contain `-->`.
- Attribute order is free; unknown keys are collected and ignored.

### 1.2 Open vs close

```js
const opening = se===':start' || (!se && !slash && (name==='hb-note'||name==='hb-zoom'));
const closing = se===':end'   || (!!slash);
```

`closing` is computed and **never used**. Every marker branch is `if(opening){...}else{...}`,
so "not opening" means "close".

| Marker | Opens on | Closes on |
|---|---|---|
| `hb-chapter` | always (no open/close concept) | n/a |
| `hb-note` | `<!-- hb-note -->` or `hb-note:start` | `<!-- /hb-note -->` or `hb-note:end` |
| `hb-time` | `hb-time:start` **only** | anything else, incl. bare `<!-- hb-time … -->` |
| `hb-zoom` | `<!-- hb-zoom … -->` or `hb-zoom:start` | `<!-- /hb-zoom -->` or `hb-zoom:end` |
| `hb-story` | `hb-story:start` **only** | anything else, incl. bare `<!-- hb-story … -->` |

Any other `hb-*` name (e.g. `hb-end`, `hb-section`) matches `RE_MARK`, falls through every
branch, and is **silently deleted** — the line vanishes and no error is raised. There is no
`hb-end` handling of any kind.

### 1.3 Per-marker attribute contract

**`hb-chapter`** — no required attribute; everything has a fallback.
- `id` — display (`Lens 01`) and sort key, via `localeCompare` on strings.
- `slug` — identity. Repeating a slug **merges into the first chapter object**; the second
  file's `id`, `title`, `mode` are discarded.
- `title` — displayed on the lens plate.
- `mode` — stored, **never read anywhere else in the file**.
- `part`, `file` — **never read, never stored**.
- No values validated. Nothing throws.

**`hb-note`** — reads no attributes. Destination depends on position: before any chapter →
book note; after `hb-chapter` but outside an era → chapter note (accumulates); inside an era
→ that era's note (**last one wins**). Only the era note is ever rendered, and only when the
"Editor notes" toggle is on. Chapter and book notes are stored and **never displayed**.

**`hb-time`**
- `id` — **required in practice**; must be one of the ten canonical ids or it errors.
- `chapter` — optional; errors only if present AND ≠ current chapter slug.
- `label` — optional; falls back to the canonical label.
- `state` — optional, default `full`; **validated** against `full|thin|empty`.
- `progress` — optional, default `''`; **not validated**; rendered verbatim as a badge.
- `order` — stored and **never read**. Row order comes from the hard-coded `ERAS` table.
- On close, an `id` mismatch errors; a close with no `id` is fine.

**`hb-zoom`**
- `level` — optional, default `era`; **validated** against `era|span`.
- `label` — optional; rendered only for `level="span"`. Ignored for `era`.
- Does **not** push the stack, so an unclosed zoom is never reported.

**`hb-story`**
- `slug` — optional; an empty slug is **skipped by the uniqueness check**.
- `name` — optional; used for the fold label and story heading.
- `movie` — stored and **never rendered**. Film styling comes from the `> **Movie:**` record
  line, not this attribute. Nothing cross-checks them.
- `kind` — **not validated**; emitted as `class="badge kind-…"`. CSS exists only for
  `kind-famous` (indigo) and `kind-ordinary` (brick).
- `status` — **not validated**; emitted as `class="badge status-…"`. CSS exists only for
  `status-verified` (forest), `status-candidate` (ochre), `status-target` (slate).
- Does **not** push the stack.

### 1.4 Structural rules actually enforced

- **Hard-coded era list** (`const ERAS`, ~line 1437): `before-1500`, `1500s`, `1600s`,
  `1700-1750`, `1750-1800`, `1800-1850`, `1850-1900`, `1900-1950`, `1950-2000`,
  `2000-today`. Grid rows are always these ten in this order regardless of file contents.
- **Completeness**: every chapter is checked for all ten era ids; missing ones error.
- **Unclosed blocks**: only `hb-note` and `hb-time` push the stack, so only those are
  reported. `stack.pop()` is untyped — a `/hb-note` can pop a `time` entry and hide a real
  unclosed-section error.
- **Story slug uniqueness** is checked **globally across the whole book**, not per chapter.
- **No nesting is supported.** Blocks are a flat sequence; opening a block flushes the
  previous one. No nesting or ordering checks exist.
- **Chapter order**: `localeCompare` on the `id` string.
- **Multi-file loading**: `.md`/`.markdown`/`.txt` only, sorted by name, joined with `\n\n`,
  parsed as one document.
- **Nothing throws.** Every problem is either an entry in `errs` (side panel; the file still
  renders) or silent. The only abort is a file with no `hb-chapter` markers.

---

## 2 · Writing rules — the do/don't checklist

### Markers
- DO put every marker alone on its own line as a single-line `<!-- … -->` comment.
- DO use only lowercase letters after `hb-`.
- DO double-quote every attribute value. DON'T use single quotes.
- DON'T put `"` or `-->` inside an attribute value.
- DO write `hb-time:start`/`hb-time:end` and `hb-story:start`/`hb-story:end`.
  DON'T write a bare `<!-- hb-time … -->` — it silently *closes*.
- DO write `<!-- hb-zoom … -->` … `<!-- /hb-zoom -->` and `<!-- hb-note -->` … `<!-- /hb-note -->`.
- DON'T invent new `hb-*` marker names — they are silently deleted.

### Structure
- DO give every chapter all ten canonical eras, exactly once each.
- DON'T repeat an era id inside one chapter or across part files — the second silently
  overwrites the first, with no error.
- DO keep every zoom/story block **inside** an `hb-time` section; blocks outside one are
  silently discarded.
- DO close every zoom and story block explicitly, and close the last one before EOF.
- DO keep chapter `id` zero-padded to two digits.
- DO make story slugs unique across the whole book.
- DO set `chapter="…"` to the chapter **slug**, or omit it.

### Content inside blocks
Supported by `mdBlock` / `inline`:
- Paragraphs, separated by blank lines. **Single newlines are joined with a space.**
- `**bold**` — no `*` may appear inside.
- `*italic*`.
- `[text](https://…)` links and bare `http(s)://…` autolinks.
- `> **Key:** value` records; continuation lines `> more` append to the previous value.
  A key matching `/movie|film/i` gets the `.film` (indigo) class.
  **Records render only inside `hb-story` blocks.**
- **Bullet lists (v2):** `- item` or `* item` → `<ul class="md-list">`, one `<li>` per line.
  A bullet run ends at a blank line, a paragraph line, or a `>` record.
- **`[VERIFY…]` tags (v2):** rendered as `<span class="vtag">` ochre badges. Fine in
  outline mode; **must still be gone from finished prose** — the badge is a review aid,
  not book content.

Not supported — do not write these:
- `#`–`######` headings inside blocks (silently discarded).
- Nested lists (the inner level flattens — indentation is stripped by `l=raw.trim()`).
- Numbered lists (`1. item` renders as a literal paragraph).
- Tables (render as one literal run-on line).
- Fenced or indented code blocks.
- Images (render as a stray `!` plus a link).
- Raw HTML of any kind (escaped, shown literally).
- **Multi-line** comments inside blocks (they leak as visible text; single-line ones are
  dropped safely in v2).

---

## 3 · Silent-failure list

No error message anywhere for any of these:

1. ~~Bullets collapse.~~ **Fixed in v2** — bullets render as real lists. (In
   `viewer-v1.html` they collapse into a run-on paragraph; the compiled outline has 796
   bullet lines, so never review outlines in the v1 backup.)
2. **Tables and code blocks** become one literal run-on paragraph.
3. **Headings inside blocks vanish.** (`##Heading` without a space is *not* discarded and
   renders literally.)
4. **A `>` line that isn't a `**Key:** value` record and comes before any record is dropped
   entirely.**
5. **`> **Key:** value` records inside an `hb-zoom` are parsed and thrown away** — the zoom
   branch keeps only `html`.
6. ~~Non-`hb-` comments inside a block leak as visible escaped text.~~ **Fixed in v2** —
   any line matching `^<!--…-->$` is dropped. Multi-line comments still leak.
7. **Unknown `hb-*` markers inside a block are deleted silently**, and the text above and
   below them merges into one block.
8. **`hb-note` inside a zoom/story block destroys everything buffered so far** — opening the
   note clears the buffer while the block is still open.
9. **A duplicate era id silently overwrites the earlier era**, losing all its content.
10. **A duplicate chapter slug merges into the first chapter**, discarding the second's
    `id`/`title`/`mode`.
11. **A block left open at EOF is lost** — nothing flushes at end of input.
12. **A zoom/story block outside any `hb-time` section is discarded.**
13. **An unclosed `hb-zoom` or `hb-story` is never reported.**
14. **`stack.pop()` is untyped**, so a mispaired `/hb-note` can mask a genuine unclosed section.
15. **`<!-- /hb-chapter -->` creates a phantom empty lens** named `lens-N`.
16. **Single-quoted attributes silently fall back to defaults** — `level='span'` → `era`;
    `state='thin'` → `full`; `id='1600s'` → `undefined`.
17. **Unknown `kind`/`status`/`progress` values are accepted** and emit a CSS class with no
    matching rule — badge renders in the default colour, no warning.
18. **`movie` attribute vs `> **Movie:**` line are never cross-checked.**
19. **`order`, `mode`, `part`, `file` are inert.**
20. **`**bold *inner* end**` fails** — the bold pattern forbids `*` inside.
21. **A bare URL immediately followed by `"`, `'` or `>` is not linked.**
22. **Multi-line HTML comments leak fully as text.**
23. **A marker sharing a line with any other character is prose**, and its block never opens.
24. **Chapter ordering is a string compare** — an unpadded `id="2"` sorts after `id="10"`.
25. Non-`.md`/`.markdown`/`.txt` files in a dropped folder are silently skipped.

---

## 4 · Disagreements with the existing docs and the validator

### VIEWER-COMPAT's v2 claims are correct — verified in the real v2

An earlier revision of this file said they were false. That was an analysis of
`viewer-v1.html`, mistaken for the shipped build. In `viewer/viewer.html` (v2):

| VIEWER-COMPAT claim | Verified in v2 |
|---|---|
| "Bullet lists render as real lists (`- item` → `<ul class="md-list">`)" | **TRUE.** `flushL()` emits `<ul class="md-list">`; CSS at lines 692–693. |
| "Stray single-line comments inside blocks are dropped" | **TRUE, and broader than claimed** — `if(/^<!--[\s\S]*-->$/.test(l)) return;` drops *any* whole-line comment, not just `hb-` ones. Multi-line comments still leak. |
| "`[VERIFY…]` tags styled as small ochre badges" | **TRUE.** `.replace(/\[VERIFY([^\]]*)\]/g,'<span class="vtag">…')`. |

Still inaccurate in VIEWER-COMPAT:

| Claim | Reality |
|---|---|
| §7 "every block must be closed by end of input" | Only `hb-note` and `hb-time` push the stack; an unclosed `hb-zoom`/`hb-story` is never reported and its content is lost. |
| Source path `Desktop/viewer.html` | Stale — the viewers live in `viewer/`. |

### `grid-markers.md`

| Claim | Reality |
|---|---|
| §2 `mode` = outline\|prose, presented as meaningful | Stored, **never read**; changes nothing rendered. |
| §2 `order` "the sort key" | Inert. Row order is the hard-coded `ERAS` array. |
| §2 `part`, `file` | Never parsed. |
| §2 story `slug` "unique in chapter" | Uniqueness is enforced **globally across the book**. (§7b and VIEWER-COMPAT §8 have this right.) |
| §5 "an era is never split across two files" | True as a rule, **unenforced** — the second silently overwrites. |
| §7b "bullets only" inside blocks | Bullets do not render as bullets. |
| §11 "Films list: every non-empty `movie`" | There is no films list in this viewer. |
| §11 "Strip for final: drop every `hb-note`" | Not dropped — era notes render behind the "Editor notes" toggle; chapter/book notes are retained but unreachable. |

### `tools/validate_grid.js`

Contains a **verbatim copy** of `ERAS`, `RE_MARK`, `RE_ATTR`, `attrs` and `parseGrid` from
the viewer, plus a CLI driver. For the structural layer it is exactly as strict as the
viewer — no more, no less.

It is **effectively far more lenient**, because it never calls `mdBlock`, `inline` or
`cellHTML`. It reports 0 errors for: bullets, tables, code blocks, images, raw HTML,
headings in blocks, records inside a zoom, a blockquote before any record, non-`hb-`
comments in blocks, unknown `hb-*` markers, an `hb-note` opened inside a block, duplicate
era ids, unclosed zoom/story, single-quoted attributes, and unknown `kind`/`status`/`progress`
values.

**Because `parseGrid` is duplicated by copy-paste, the two can drift. Re-diff after any
viewer edit.**

### UNKNOWN

- Whether a true "v2" viewer with bullet and VERIFY support exists elsewhere. VIEWER-COMPAT
  describes behaviour this file lacks; it may document a build that was never copied into
  the repo, or one that was lost. Not determinable from here.
