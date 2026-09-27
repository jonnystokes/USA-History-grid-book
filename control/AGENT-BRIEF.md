# Agent Brief: read this before researching any chapter

You are researching **one chapter** of *A History of the United States*, a plain-language history for readers about **ages 8–15**. You will replace that chapter's seed outline with a **full, deeply researched outline**, and write its research bank. **You do not write chapter prose.**

### Standing warnings (added 2026-09-05 after a full-project audit)

- **Never mark a story `status="verified"` until it is actually sourced in the
  research bank.** An audit found stories tagged `verified`
  while still one-line stubs carrying `[VERIFY]` (art-music, big-business,
  exploration, holidays, all fixed 2026-09-06). The validator cannot catch
  this, so a false tag silently becomes a false fact later. `target` and
  `candidate` are honest. A premature `verified` is not.
- **A bank that is smaller than the outline it backs is a red flag,** not a
  finish line. Several chapters shipped that way and now need patching.
- **`viewer/viewer.html` (v2) and `viewer/viewer-v1.html`: line 89 of each is a
  ~373,500-character base64 image.** Never read either whole. Read around it in ranges.
- `node tools/validate_grid.js` now exits non-zero on errors (fixed 2026-09-06),
  but it never runs the renderer. A clean run is necessary, not sufficient. See
  `control/VIEWER-CONTRACT.md` §3. Better: `python tools/project_state.py --check
  <slug> --stage research`, which is the bar your work is judged by.
- Current state and what is gating your chapter: `control/STATUS.md` and
  `control/ROADMAP.md`.

### WRITE EARLY: this is how your work survives

You may be killed mid-task by a usage limit, without warning. Agents that spend their
whole budget researching and write at the very end **leave nothing behind**: two
research agents on this project died that way, each after ~100 web fetches, having
written not one line. Agents that had already written their files lost only their
final report, and their work was kept.

So: **write a file within your first few turns and keep appending to it.** A partial
outline on disk beats a perfect plan in your head. Do not save the writing for last.

**Keep a checkpoint (added 2026-09-26, both environments).** If the director gives you a
checkpoint file (`control/checkpoints/T-<nnn>-<slug>.md`), read it first and keep it current.
Work one unit (one era) at a time. After each unit, record in the checkpoint what landed, the
sources you used, what you left out and why, and what comes next. A new agent that has only
that file and the repo must be able to carry on without redoing your work. Do not use git.
The director commits your work once you finish.

**Your dispatch brief is `control/briefs/RESEARCH.md`** (2026-09-26). It adds the bank check
that ends every research task, and the `SEARCHED, NOT FOUND` record for questions the sources
cannot answer. For a large bank or outline, read only your eras with
`python tools/slice_bank.py <slug> --eras <a-b>`.

### Two rulings from Jon (2026-09-06) that outrank your instincts

- **No language softening, ever.** Euphemism, minimization, downplaying, semantic
  abstraction, sanitization, gist extraction, lossy summarization are all forbidden.
  The last two are the dangerous ones: they enter *mechanically* when you compress
  under context pressure, without anyone deciding to soften anything. This book's
  reader does not already know this history and cannot reconstruct what you left
  out, so whatever you soften simply becomes what they believe happened.
  Full rules and worked examples: **`control/hard-subjects-policy.md`**. Read it
  before writing any cell about violence, death, disease, or cruelty.
- **Thin eras are correct.** A subject that barely existed in an early era gets a
  short honest cell (`state="thin"` or `"empty"`) and one true sentence. **Never pad
  a cell to make it look full**, and never merge unlike material to avoid a sparse
  one. Science does not move as much in the 1500s as in the 1900s, and the grid is
  supposed to show that. An empty-looking cell that is honest is a finding, not a
  failure.
- **Never invent a name.** Named account → name it and say plainly what happened.
  Documented but unnamed → tell it unnamed ("this happened to children at these
  schools"). Unnamed material goes in `hb-zoom` prose. `hb-story` blocks are for
  named people only. Never build a composite person.

---

## 1. What this book is

**A grid.** 37 subject chapters (the perspectives) × 10 fixed time sections (the eras). The finished product is a program where a reader scrolls **down through time** and **left and right through perspectives**. You are producing the story data for one column of that grid.

Read first: **`control/hard-subjects-policy.md` (BINDING: no softening, never invent a name, and the clinical-word rule)** · **`control/general-writing-style-guide.md` (Writing Style Guide Version 2, BINDING, read in full)** · **`control/writing-style-guide.md` (this book's amendment, BINDING. Personification is the rule most often broken, including while repairing a passive)** · `control/chapter-registry.md` (your chapter's angle and its neighbours) · `control/project-notes.md` (rules) · `control/grid-markers.md` (structure) · your chapter's seed file in `outlines/`.

## 2. The ten eras: every chapter, always in this order

`01 before-1500` Before 1500 · `02 1500s` The 1500s · `03 1600s` The 1600s · `04 1700-1750` 1700 to 1750 · `05 1750-1800` 1750 to 1800 · `06 1800-1850` 1800 to 1850 · `07 1850-1900` 1850 to 1900 · `08 1900-1950` 1900 to 1950 · `09 1950-2000` 1950 to 2000 · `10 2000-today` 2000 to Today

**Account for all ten. Do not pad.** Many chapters will have eras where genuinely nothing happened from their angle. **That is expected and fine.**

**Jon's rule for empty eras (2026-07-23): say so plainly and move on.** Write the honest sentence, such as "There were no factories in this land yet" or "Nobody here was buying or selling this way yet", and stop. You *may* add one line on what stood in its place, or on something happening elsewhere in the world that would later reach America (for example, a European trading company that would one day send ships here). But **Jon prefers the straightforward statement over a clever reach.** Never stretch, never pad, never invent significance. An honest empty cell is better than a padded one, and the reader will trust the book more for it.

**Boundary rule:** an event belongs to the era containing its date. Era starts are inclusive (1900 → the 1900–1950 section, not 1850–1900).

## 3. THE ABSOLUTE RULE: no invented facts

- Web-verify **every** date, number, name, and place before writing it down. Name a source inline for each fact.
- Where sources disagree or give a range, **state the range and the disagreement**. Never resolve a dispute by picking one silently.
- If something is not known, say it is not known. Never fill a gap with a guess.
- Prefer government, museum, and academic sources: Library of Congress, National Archives, Census Bureau, National Park Service, Smithsonian (incl. NMAI and NMAAHC), NASA/NOAA/USGS, university history sites, Encyclopaedia Britannica, subject archives. Journalism is fine for recent or thinly documented items. Label it. (In the CLOUD environment britannica.com is blocked.)

## 4. How each time section is built: three zooms

Every era section moves from wide to close, and may move back and forth:

1. **Zoom 1: the whole era.** What this stretch of time was like for your subject across the whole land: what existed, what did not exist yet, who was already here.
2. **Zoom 2: shorter spans inside it.** A decade, a movement, a place or a law, told the same way but tighter.
3. **Zoom 3: individual stories.** Real people in real situations, from research only.

Your outline must supply material for all three levels in every era, not just a list of events. Label each era's outline material by zoom level so the writer knows what belongs where:
- **Zoom 1 (era):** the wide framing of the whole era, one opening paragraph's worth.
- **Zoom 2 (span):** the shorter spans inside it (decades, movements, places, laws), each a labeled chunk.
- **Zoom 3 (story):** the individual documented people/situations.

When the prose is later written, these map to grid markers (see `control/grid-markers.md` and the worked example `control/SAMPLE-chapter-format.md`): Zoom 1 → `hb-zoom level="era"`, Zoom 2 → `hb-zoom level="span" label="…"`, Zoom 3 → `hb-story` blocks. You are writing the outline, not the marked-up prose, but knowing the target structure keeps your material sortable. Flag any era as `state=empty` (subject did not exist) or `state=thin` (little to tell) in your Thin-eras section.

## 5. Stories: BOTH, in this priority

1. **Every famous story a reader would meet in school must be present.** Do not trade well-known people and events for obscure ones. Completeness first.
2. **Then add ordinary people:** at least one per chapter who was not famous, whose life is genuinely documented (a diary, an oral history, a court record, an interview). This is what makes the book different.

For each featured person, supply: **Who** (one line), **When and where**, and **Movie**: the real film or documentary with year **only if one actually exists**. Verify it. Never invent a film. Omit the line when there is none. Note whether a doc is about the person or just the topic.

## 6. Nothing improper gets filtered out

Where leaving out the injustice, cruelty, or hard truth of a story would make the telling dishonest, **it goes in**, plainly, at a young reader's level, in your chapter. Your chapter owns its own hard parts. There is no separate chapter that absorbs difficulty for you.

## 7. Cross-chapter protocol: perspectives without overlap

**The same event appearing in several chapters is the point of this book, not a bug.** The transcontinental railroad genuinely belongs in Transportation (the line), Migration (the settlers it carried), Economy (what it did to prices), Big Business (the land grants), Work and Workers (conditions on the line), Immigration (the Chinese workers' arrival), and Native Nations (what it cost the Plains nations). Seven true perspectives.

So the rule is **not** "one chapter owns it." The rule is:

- **Tell the event fully, but only through your chapter's angle** (see the registry).
- **Never repeat another chapter's material.** Before writing an event, check the registry for which neighbours also touch it, and note in your outline what *their* slice is so the writer avoids duplicating it.
- Add a line under each shared event: `Shared with: <slug> (their angle) · <slug> (their angle)`.
- **When you find strong verified material that belongs to another chapter, park it** in that chapter's research file (`research/research-<slug>.md`, create it if needed), tagged by era. Do **not** write that chapter's outline.

## 8. Threads to check (lenses, not chapters)

Run this checklist against your chapter and include what genuinely applies. Do not force it:
Native continuity **past 1900** (easily dropped once "the frontier closes". Keep it) · disability · class and poverty · region (South, West, Appalachia, Midwest, New England) · rural and small-town life · **territories** (Hawaii, Alaska, Puerto Rico, Guam, Samoa, the Philippines, currently near-absent from the whole book) · language · LGBTQ · children and the elderly.

## 9. Voice: THE STYLE GUIDE BINDS THE OUTLINE TOO (tightened 2026-08-08 after violations)

Read `control/general-writing-style-guide.md` (Version 2) and `control/writing-style-guide.md` (the book's amendment), and apply them to **every sentence you write in the outline**, not just future prose. Bullets may be terse. Any era-zoom or span text you write as sentences IS miniature book prose and follows the guide in full. Specifically banned (all found in real outline violations):
- **Teaser sentences that withhold the facts.** "It took two tries, and one ended in an attack" forces the reader to hunt for what attack. Say it: "The Powhatan destroyed the first ironworks in the attacks of 1622."
- **Em dashes and semicolons, in any sentence written as book prose.** Style guide Version 2 (2026-09-26) forbids both characters outright. Use a period, a comma, a colon or parentheses. Balanced-clause flourishes ("one ended in X, one ran for Y") are also banned. Use plain declarative sentences instead. Terse bullets and bank citations are working notes and are exempt.
- Personification, metaphor, "poetic" cadence, evaluative adjectives, hedges, staged scenes, self-commentary are all banned by the guide.
The test for every era-zoom line: **could it drop into the finished book unchanged?** If not, rewrite it plainly. Flag anything hard to say plainly for an 8–15 reader and suggest the plain wording.

## 10. What you deliver

**(a) The chapter outline:** overwrite `outlines/<slug>.md`, following `outlines/_TEMPLATE.md`, the marker spec `control/grid-markers.md`, **and the parser contract `control/VIEWER-COMPAT.md`** (the viewer program is already built, and the checklist at the bottom of that file is mandatory: own-line markers, all ten eras, globally-unique story slugs with chapter suffixes for shared people, no comments inside blocks, prose/bullets only) **exactly**. It is grid-format: `hb-chapter` (mode="outline"), an `hb-note` orientation block, then all ten eras as `hb-time` sections with `hb-zoom` (era/span) and `hb-story` blocks. Keep cells **terse**. This is the compressed book, not the prose. Set each era's `state` (full/thin/empty) and `progress` (`seed`→`researched` as you finish it). Put story candidates **in their era** as `hb-story` blocks with `status` (target/candidate/verified). Keep no separate people list. This is the primary deliverable and the main file the director reads.

**(b) The workspace file:** create or extend `workspace/<slug>.md` from `workspace/_TEMPLATE.md`: the **shared-events table, the famous-names checklist, the [VERIFY] queue, open questions, and the cross-chapter parking log.** All planning scaffolding goes here, NOT in the outline. This keeps the outline a clean grid.

**(c) The research bank:** create or extend `research/research-<slug>.md` with the verified facts and inline sources behind every outline line, plus a "Sources used" list and a "Coverage / status log."

**(d) Parked cross-chapter finds** go into the right `research/research-<slug>.md` files, and log them in your workspace file.

## 11. Report back (keep it short, because the files are the deliverable)

Which eras are covered and which are genuinely thin · your strongest featured people (and any verified movies) · the famous school-history names you made sure are present · notable factual disputes you hit · shared events and whose angle is whose · which cross-chapter files you added to · anything the director should decide.

## 12. Do not

Write chapter prose · invent a fact, a person, a quote, or a film · renumber chapters · edit another chapter's outline · pad a thin era · silently resolve a source dispute · drop the famous names in favour of clever obscure ones.
