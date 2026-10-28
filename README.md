# History Book Project

Working title: *A History of the United States*

Plain-language U.S. history for readers about ages 8–15. **37 subject chapters in 9 parts**, each covering the same ten time sections. Chapter length: as big as the material honestly supports, with no caps and no fluff.

**Which environment?** Run `python tools/env_check.py`. The project runs on Jon's PC (LOCAL): follow the path below. The cloud workflow (Anthropic's servers) is archived in `control/archive/cloud/`. Read its README and ask Jon before working online.

**The plan** (2026-09-26): eight steps in order: research, write, audit, research round 2, writing round 2, audit, polish, done (`control/ROADMAP.md`). Sub-agents get briefs from `control/briefs/`, with opus for research, writing and fixing and sonnet for checking (`control/briefs/README.md`).

**Start here:** `control/RESUME.md` (how to resume after an interruption, read first) → `python tools/project_state.py` (the real state, measured) → `control/TODO.md` (the live plan) → `control/WORKLOG.md` (what was in flight, read the tail) → `control/STATUS.md` (narrative tracker) → `control/ROADMAP.md` (the plan to finish) → `control/chapter-registry.md` (the 37 chapters, slugs, angles) → `control/AGENT-BRIEF.md` (how research is done) → `control/grid-markers.md` (the file format) → a chapter's `outlines/<slug>.md`.

**To read the book:** open `book/history-book.pdf`, or `book/history-book.md` (the same book as one Markdown file with a linked contents list). Both are built from `manuscript/` (DECISIONS #48). The grid viewer is retired as the reading format. It stays as a tool for the research-stage outlines: open `viewer/viewer.html` (**v2**, not the v1 backup) and drop in `outlines/BOOK-OUTLINE.md` alone. Its parsing contract is `control/VIEWER-COMPAT.md` + `control/VIEWER-CONTRACT.md`.

## Absolute rule

No invented facts. Research first. Write clearly. Do not change the facts.

## Folders

| Path | Role |
|------|------|
| `control/` | Rules and authorities: STATUS, ROADMAP, chapter-registry, AGENT-BRIEF, grid-markers, VIEWER-SPEC/COMPAT/CONTRACT, project-notes, general-writing-style-guide (style guide v2), writing-style-guide (the book's amendment), TODO, SAMPLE |
| `control/briefs/` | The sub-agent briefs (RESEARCH, WRITER, CHECKER, FIXER, GAPS, SALVAGE) and the model policy in its README |
| `control/audit/` | Checker findings per chapter, and the sonnet-against-opus checker calibration |
| `control/archive/` | Archived, not in force: the cloud workflow (`cloud/`) and the full pre-trim RESUME |
| `book/` | **The book as readers get it:** `history-book.pdf` and `history-book.md`, built from `manuscript/` (DECISIONS #48) |
| `viewer/` | The grid viewer, retired as the reading format (DECISIONS #48) and kept as a tool: `viewer.html` (**v2, use this**) and `viewer-v1.html` (backup). **Line 89 of each is a 373 KB base64 image. Never read the file whole** |
| `outlines/` | One grid outline per chapter (`<slug>.md`) + compiled `BOOK-OUTLINE.md` |
| `workspace/` | Per-chapter planning files (shared events, name checklists, verify-queues), not parsed into the grid |
| `research/` | Verified fact banks (`research-<slug>.md`) |
| `manuscript/` | Finished chapter prose (written last) |
| `templates/` | `chapter-template.md`, the v3 prose skeleton. Outlines start from `outlines/_TEMPLATE.md` |
| `control/checkpoints/` | Per-task resume files kept by sub-agents (template: `_TEMPLATE.md`) |
| `tools/` | `env_check.py` (**CLOUD or LOCAL?**), `slice_bank.py` (**one chapter's eras of the outline and bank, so agents read only what they need**), `salvage_agent.py` (**recover a dead sub-agent's research**), `project_state.py` (**the truth: measured state + `--check` gates**), `build_book_outline.py` (compile), `validate_grid.js` (parser check), `dedup_story_slugs.py` |
| `_reference/` | Archived v1/v2 work and superseded planning docs, **reference only, do not use as current**. Kept on Jon's PC only, not in the GitHub repo |
| `seed-files/` | Original seed dump, reference only. Kept on Jon's PC only, not in the GitHub repo |

See `control/RESUME.md` for the resume protocol, and run `python tools/project_state.py` for the measured per-chapter state.
