# Project Notes

Working notes for the book. Not part of the book itself.

## Absolute rule: no invented facts

- Never invent stories, dialogue, scenes, numbers, motives, or details.
- Never fill gaps with assumptions. If a fact is not known, say it is not known, or omit it.
- Research first (online sources, code/library docs as relevant). Write only what research supports.
- Writing may make researched facts clear and readable. Writing may not change the facts.
- Featured person stories are true accounts from research, not fiction written to sound good.

## Project layout (working files)

`seed-files/` is **reference only**. Do not edit it for active work. Active copies live here:

| Folder | Contents |
|--------|----------|
| `control/` | Project notes, writing style guide, table of contents |
| `templates/` | `chapter-template.md` — the v3 **prose** skeleton (rebuilt 2026-09-05). Outlines start from `outlines/_TEMPLATE.md` instead |
| `research/` | Research notes by chapter |
| `outlines/` | Short outlines (list form) |
| `manuscript/` | Written chapter drafts |

## Who this book is for
- Readers with little formal education, ages about 8 to 15.
- Use simple, common words. Avoid words a young or new reader would have to look up (for example, "vice"). Keep an eye on longer words like "recreation."

## Writing rules
Follow the Writing Style Guide, Version 2 (`control/general-writing-style-guide.md`), and the book's amendment (`control/writing-style-guide.md`). Together they are the authority for prose.

Core reminders (see the full guide for detail and examples):
- No personification. Non-living things (nations, economies, documents, ideas) do not act, want, or feel. Name the people who act.
- No metaphors or rhetorical decoration. Say things plainly. Avoid AI "poetry" cadence, forced rhythm, or rhyme.
- No promotional or evaluative adjectives ("great," "dramatic," "remarkable," "devastating," "brilliant"). Let the facts carry the weight.
- No hedges ("may have," "generally believed"). State claims directly, or name who holds a view and on what basis.
- No gnomic statements (proverb-like "timeless truths").
- No imported analogies. Do not explain a historical event by comparing it to an unrelated modern thing.
- No staged scenes ("imagine you are a farmer in 1786").
- No self-commentary. Do not describe what the text is doing. Do not break the fourth wall or talk about the book, the chapters, or the reader. Do not cross-reference other chapters inside the prose.
- Anchor comparatives with numbers ("grew 35 percent," not "grew much faster").
- Name specific agents where possible.
- Use words precisely (a revolution is not a reform; a depression is not a recession).
- No fluff. Every sentence should carry a fact, a cause, or a supported inference.
- Default to chronological order.

### Person stories and interest
History prose stays plain and direct. Featured person stories may be more engaging when the material calls for it (danger, a hard choice, a clear sequence of actions). That is fine only when it serves the story and the facts. Do not add rhythm, rhyme, or decoration just to sound literary.

## How a time section is built: three zooms (Jon, 2026-07-23)

Every time section moves from wide to close, and may move back and forth as the material calls for it:

1. **Zoom 1 — the whole era.** The narrator opens wide: what this stretch of time was like for this subject across the whole land, what existed and what did not, who was already here.
2. **Zoom 2 — shorter spans inside the era.** Closer in: a decade, a movement, a place — the narrator still telling, but tighter.
3. **Zoom 3 — individual stories.** All the way in: real people, real situations, drawn only from research. Never invented.

The narrator may step back out to zoom 1 or 2 after a story and then dive in again. Alternating is encouraged where it serves the reader; the rule is only that each section *starts* wide and *does* reach the individual level.

**Why:** the finished product is a program where the reader scrolls down through time and sideways through perspectives — a large interactive grid. Right now we are writing the story data that fills it. Machine structure: `control/grid-markers.md`.

## Two kinds of writing: history and a person's story
The book mixes two things, and they should feel different:
- History: the sweep of what happened and the state of the whole land at each time. Written as flowing prose.
- A person's story: a featured explorer. Set it off from the history so the reader can tell a story is starting.

Format for a featured person's story:
- A horizontal rule to break from the history around it.
- A heading with the person's name.
- A short metadata box (a blockquote) with:
  - **Who:** one line saying who they were and what they are known for.
  - **When and where:** the time period and the place.
  - **Movie:** the title and year, only if a real movie about them exists. Leave it out if there is none.
- Then the story, in the book's plain style.

Use featured stories for the standout individuals. Keep brief figures and connective facts in the flowing history prose.

## Show the whole land, including what was NOT there
In every time section, describe the state of the whole land, not just the main subject:
- How much was Native land, how much was settled by newcomers, how much was still unknown or unmapped.
- What existed and what did not exist yet.
- The "void" the explorers were moving into: the wild, unmapped country, and who and what was already there before the newcomers arrived.

## Structure
- **Thin eras are correct, not a defect (Jon, 2026-09-06).** A chapter whose subject
  barely existed in an early era gets a short honest cell and one true sentence.
  Never pad, and never merge unlike subjects just to avoid sparse cells. "No reason
  to combine things that are very different just because you don't want any blank
  pages."
- **37 chapters in 9 parts.** The authoritative list, slugs, angles, and keep-outs are in **`control/chapter-registry.md`**. Live status per chapter: **`control/STATUS.md`**. (The 27→35 restructure is complete; its old plan is archived in `_reference/superseded-planning-docs/`.)
- **Chapter length: as big as the material honestly supports — no word caps, no tiers, and no fluff.** A chapter ends when the verified material is used up. A thin era gets two honest sentences, not a padded page.
- Every chapter uses the same ten time sections, in the same order:
  1. Before 1500
  2. The 1500s
  3. The 1600s
  4. 1700 to 1750
  5. 1750 to 1800
  6. 1800 to 1850
  7. 1850 to 1900
  8. 1900 to 1950
  9. 1950 to 2000
  10. 2000 to Today
- The 1700s, 1800s, and 1900s are split into 50-year halves because more happened in them and more of it is known. The earlier centuries are kept whole because they are thinner for most subjects.
- This keeps every chapter the same shape, so the book lines up like a grid: scroll down through one subject over time, scroll sideways to see other subjects at the same time.
- In "Before 1500," focus on what Native peoples did related to the subject. If the subject did not exist yet, it is okay to say there is not much to tell.
- If a chapter grows too large for one file, split it into parts (for example, before 1800, the 1800s, and the 1900s and today).
- Every outline and (later) prose file carries hidden `hb-*` grid markers so code can pull any era from any chapter and render the grid. **Spec: `control/grid-markers.md` (v3, LOCKED); hand-off for the viewer: `control/VIEWER-SPEC.md`.** Outlines and the final book use one marker language.

## Key principle: one event, many chapters
- The same event or person can appear in more than one chapter, each time told from that chapter's subject.
- Example: the Gold Rush shows up in Exploration (searching new country), Migration West (the crowds moving in), Economy (mining and money), and possibly others. Each chapter tells only its own angle.
- Example: space in Exploration covers the journeys and discovery (who went, where, what they found). Rockets, machines, and scientific results belong mainly in Science. Write the current chapter from its own perspective only.
- When material would also fit another chapter, note that overlap in a notes file (this file or a chapter research/notes file) so later chapters can pick it up from the right angle.

### Research phase: capture stories for other chapters
- While researching the chapter in hand, if you find a strong true story that also fits another chapter well, **document it**.
- You may create or add to research files for chapters not yet started (e.g. `research/research-migration.md`) so good material is not lost.
- Do not write those other chapters yet. Park facts and story leads under the right chapter research file, tagged by time section when possible.
- Still write the current chapter only from its own subject angle.

## Cross-chapter decisions
- **Full-sweep rule, SOFTENED (2026-07-23):** every chapter must **account for** all ten eras — not necessarily fill them. If the subject did not exist yet, say so plainly in a sentence or two and describe what stood in its place. **Do not pad**; readers notice padding faster than absence.
- **The "injustice home" rule is DELETED (2026-07-23):** every chapter owns its own hard parts. Slavery and Freedom (24) and Rights and Movements (25) tell their subjects directly; they do not absorb other chapters' darkness. The two-angle technique may still be used for a single event when both angles are substantial, but it is no longer policy.
- **Event ownership:** every major event has exactly ONE owning chapter; all others get at most one cross-referencing sentence. See `control/event-ownership.md`.
- **Who gets a story (Jon, 2026-07-23) — BOTH:**
  1. **Every famous story a reader would meet in school must be here.** Do not leave out the well-known people and events in favor of obscure ones. Completeness first.
  2. **Then add ordinary people** — at least one per chapter who was not famous. The famous names are the backbone; the ordinary lives are what makes this book different.
- **Movies:** not every featured person needs one. **Anyone who does have a real film or documentary gets it named** in the Movie line (title + year). Never invent one; leave the line out when none exists.
- **Nothing improper gets filtered out (Jon, 2026-07-23):** where leaving out the injustice, cruelty, or hard truth of a story would make the telling improper or dishonest, it goes in — told plainly, at the reader's level, in whatever chapter the story lives.
- **Boundary-year rule:** an event belongs to the era containing its date; era starts are inclusive (1900 → the 1900–1950 section). Say whether a date is founding or fame.
- **Thread checklist** (lenses to check per chapter, not chapters of their own): Native continuity past 1900 · disability · class and poverty · region · rural and small-town · territories (Hawaii, Alaska, Puerto Rico, Guam, Samoa, the Philippines) · language · LGBTQ · children and the elderly.
- **"2000 to Today" is current through 2026;** state the cutoff and revisit yearly.
- **Original full-sweep principle (still true):** a chapter must not be one period wearing a chapter name. Applied to Part 1: it is now **1 Exploration and Discovery · 2 Immigration to America · 3 Migration Across America · 4 City Building** — four full-sweep chapters (find the land → come to it → move across it → build on it). "Migration West" (period-bound) was dropped; Immigration and Migration are each their own big chapter. Apply this test to every chapter.
- **Enslaved Africans, two angles (2026-07-23):** the forced migration is told in BOTH Ch2 Immigration and Ch17 Racial and Gender Prejudice, written differently enough not to overlap. Ch2 = the migration/arrival (origins, routes, the Middle Passage as a journey, ports, numbers, destinations, plus later voluntary African/Caribbean immigration). Ch17 = the system and injustice (slave codes, resistance, abolition, emancipation, Jim Crow, civil rights). Ch2 uses migration vocabulary; Ch17 uses rights/injustice vocabulary; neither re-narrates the other. See `outlines/ch02-immigration-outline.md`, `research/research-immigration.md`, `research/research-ch17-prejudice.md`.

## Deprecated material
- `DEPRECATED-01-overview.md` is a failed earlier learning attempt. Do not use it for writing, structure, or style.

## Workflow
- Pick a chapter, then build and iron out the outline first (outline may be built in tandem with research).
- Do the research and save it to a file before writing.
- Only write the full chapter when told to.
- **Status words:** *researched* → *outlined* → **written** (finished, ship-quality prose — never rough "draft" text) → **done** (owner-reviewed and approved).
- **Outline-first, whole book (Jon, 2026-07-23):** basic outlines for ALL chapters come first (`outlines/book-outline.md`), then research grows them, then prose. Easier to reshape the book while it is still an outline.
- **Sub-agent research phase (Jon, 2026-07-23):** run the research phase as ONE sub-agent per chapter — each verifies facts, grows that chapter's section of `book-outline.md`, and writes the chapter's `research/` bank. This keeps the main thread lean so the book can reach the finish line without compaction wiping detail; the on-disk outline + banks are the real memory. One agent at a time.

## Ideas and notes for later
- Possible new chapter: Communication. Would cover the U.S. Postal Service, the Pony Express, the telegraph, the telephone, radio, television, the internet, and more. The same communication tools can also appear in the Technology chapter and the Transportation chapter, each from its own angle.
- Space and the Moon landing overlap between Exploration and Science. Decide the main home, or split by angle (Exploration tells the journeys; Science tells the machines and discoveries).
