# History Book Project

Working title: *A History of the United States*

Plain-language U.S. history for readers about ages 8–15. **35 subject chapters in 9 parts**, each covering the same ten time sections. Chapter length: as big as the material honestly supports — no caps, no fluff.

**Start here:** `control/RESUME.md` (how to resume after an interruption — read first) → `python tools/project_state.py` (the real state, measured) → `control/WORKLOG.md` (what was in flight) → `control/STATUS.md` (narrative tracker) → `control/ROADMAP.md` (the plan to finish) → `control/chapter-registry.md` (the 35 chapters, slugs, angles) → `control/AGENT-BRIEF.md` (how research is done) → `control/grid-markers.md` (the file format) → a chapter's `outlines/<slug>.md`.

**To read the book:** open `viewer/viewer.html` (**v2**, not the v1 backup) in a browser and drop in `outlines/BOOK-OUTLINE.md`, or the whole `outlines/` folder. Its parsing contract is `control/VIEWER-COMPAT.md` + `control/VIEWER-CONTRACT.md`; the spec it was built from is `control/VIEWER-SPEC.md`.

## Absolute rule

No invented facts. Research first. Write clearly. Do not change the facts.

## Folders

| Path | Role |
|------|------|
| `control/` | Rules and authorities: STATUS, ROADMAP, chapter-registry, AGENT-BRIEF, grid-markers, VIEWER-SPEC/COMPAT/CONTRACT, project-notes, writing-style-guide, SAMPLE |
| `viewer/` | The reading UI: `viewer.html` (**v2 — use this**) and `viewer-v1.html` (backup). **Line 89 of each is a 373 KB base64 image — never read the file whole** |
| `outlines/` | One grid outline per chapter (`<slug>.md`) + compiled `BOOK-OUTLINE.md` |
| `workspace/` | Per-chapter planning files (shared events, name checklists, verify-queues) — not parsed into the grid |
| `research/` | Verified fact banks (`research-<slug>.md`) |
| `manuscript/` | Finished chapter prose (written last) |
| `templates/` | `chapter-template.md` — the v3 prose skeleton; outlines start from `outlines/_TEMPLATE.md` |
| `tools/` | `salvage_agent.py` (**recover a dead sub-agent's research**), `project_state.py` (**the truth: measured state + `--check` gates**), `build_book_outline.py` (compile), `validate_grid.js` (parser check), `dedup_story_slugs.py` |
| `_reference/` | Archived v1/v2 work and superseded planning docs — **reference only, do not use as current**. Kept on Jon's PC only; not in the GitHub repo |
| `seed-files/` | Original seed dump — reference only. Kept on Jon's PC only; not in the GitHub repo |

See `control/RESUME.md` for the resume protocol, and run `python tools/project_state.py` for the measured per-chapter state.
