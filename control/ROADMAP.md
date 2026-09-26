# ROADMAP: from here to a finished book

**Restructured 2026-09-07 on Jon's instruction.** The project runs in **three phases, in
order**: research everything, write everything, then audit everything. Auditing is no longer
interleaved with production. The previous five-phase version, with per-chapter verification
and defect-repair passes between chapters, is superseded. What it produced is preserved in
`control/AUDIT-QUEUE.md` and in the WORKLOG.

Numbers here are measured by `python tools/project_state.py`, not inherited from prose.
Re-measure before trusting any of them.

---

## Why the shape changed

For several sessions the work was: write a chapter part, verify it with an agent, fix what
the verifier found, verify the fix. It produced good chapters. It also meant that most agent
runs were spent on editing rather than on the book, and cost stopped tracking anything useful
because unlike tasks were being averaged together.

Two things make the new shape work:

1. **Prevention beats repair, and we have evidence.** The `city-building` writer hit the
   phrase "empty prairie" in its own outline, recognised it as the erasure
   `hard-subjects-policy.md` forbids, and **overrode it unprompted**. A binding, specific
   guide changed the output at write time with no verifier involved.
2. **The guide got much stronger.** `control/writing-style-guide.md` gained Section 0 (who
   the reader is and at what reading level), §1.11–1.14 (the AI cadence, sound patterning,
   register mixing, oversized words), §2.6 (know what you are teaching and get to it), and
   Section 4 (the self-audit every writer runs before reporting).

**The accepted cost:** defects propagate. A wrong fact in a bank reaches the prose and is
fixed once, at the end, in a pass built for it, instead of being chased chapter by chapter.
Known ones are parked in `control/AUDIT-QUEUE.md` so the audit phase finds them.

---

## Where the book actually is (measured 2026-09-07)

| Measure | Value |
|---|---|
| Chapters | **37**, all with valid ten-era grid outlines |
| Compiled outline | 603 stories, **138,428 words** |
| Research banks | **168,283 words** |
| Research complete | **5** clean · **13** with gaps · **16** seeds · 1 partial |
| Finished prose | **25,743 words** in `native-nations` and `city-building`. Both passed `--stage prose` under style guide v1 and both FAIL it under v2 (2026-09-26: em dashes and semicolons) |
| Remaining prose | **~300,000 words**, 35 chapters |
| Unique `[VERIFY]` tags | ~600 across outlines and banks |

---

## PHASE 1: Research everything (17 chapters)

**The outline is a product of research, not a separate stage.** One agent per chapter
produces `research/research-<slug>.md` and `outlines/<slug>.md` together.

Gate: `python tools/project_state.py --check <slug> --stage research`

**Batch A: verification, not discovery (4).** Rich seeds are already in place. The work is
clearing queues. `education` (67 `[VERIFY]` items, the richest seed in the book) ·
`rights-movements` (18.9 KB parked from nine chapters) · `government-politics` · `religion`.

**Batch B: build on parked material (5).** Each has 7.5–8.4 KB of hand-offs from other
agents. `war` · `health` · `disasters` · `crime-justice` · `drugs-alcohol`.
`hard-subjects-policy.md` is binding on all five and matters most here.

**Batch C: from scratch (7).** The three culture chapters have no research at all.
Their banks are empty files: **`art`** (115 `[VERIFY]`, 26 candidates) · **`music`** (128
`[VERIFY]`, 21 candidates. Dolly Parton is its flagship modern story and needs real sourcing) ·
**`storytelling-evolution`** (65 `[VERIFY]`, 22 targets). Then `news-communication`,
`sports-play`, `styles`, `holidays`.

**`america-world` is NOT in this batch any more** (corrected 2026-09-08). The old plan called
it unresearched with no bank. It was researched by the two split agents and now measures
`RESEARCHED*` with a 15,486-word bank, 13 stories, 0 targets and 2 candidates. It needs a
small **patch**, not research. It still carries the territories thread, so do it early.
`native-nations` owns the peoples and `land-environment` gets one assigned story.

**Batch D: bank cleanup (2, cheap).** `exploration` (reformat the seven-section bank to ten
eras, add per-fact citations, flip `progress` flags) · `big-business` (write the bank up from
the outline's inline sources).

**Also in this phase: the 15 gapped chapters.** Roughly 20 unfilled story slots plus sourcing
debt, worst first: `energy` (5 of 11 stories unverified, bank smaller than its outline) ·
`home-family` (6 unfilled of 16, and both 2000-today stories are placeholders) · `technology`
(3 unfilled + 1 candidate) · **the kitchen thread** (director-added, spans home-family,
technology and energy, entirely unsourced, so fix it once across all three) · `elements` ·
`economy` and `money` (verified but skeletal) · `marketplace` (largest outline, thinnest
backing) · `work-workers`, `food-farming`, `landmarks` · `land-environment` (blocked only on
re-verifying Bears Ears).

Gate for these: `--stage patch`.

**Phase 1 ends when all 37 chapters pass `--stage research` or `--stage patch`.**

---

## PHASE 2: Write the book (~300,000 words, 35 chapters)

One agent per chapter, or per part for a long one, writing directly into v3 `mode="prose"`
markers. No verification agents. No fix agents. The writer's own Section 4 self-audit is the
quality control, and the check is the gate.

Gate: `python tools/project_state.py --check <slug> --stage prose`
(Fixed 2026-09-07. It now measures the manuscript. It previously read the outline's
`progress` flags and could never pass for any chapter.)

**Every writing agent reads, before writing a word:**
- `control/general-writing-style-guide.md`, the Writing Style Guide, Version 2. **BINDING**
  (Jon, 2026-09-26: an absolute requirement), and the main instrument. Read all of it.
- `control/writing-style-guide.md`, **BINDING**: the book's amendment (reader, subject,
  policy, audit additions).
- `control/hard-subjects-policy.md`, **BINDING**. No softening. Never invent a name.
- `control/grid-markers.md` §7b and `control/VIEWER-CONTRACT.md` §2.
- Its own `outlines/<slug>.md` and `research/research-<slug>.md`.

**Standing obligations during this phase:**

- **Override a bad source and say so.** If the outline or bank contains softening, a false
  comparison, a manufactured dispute, or personification, the writer fixes it in the prose and
  names it in its report. It does **not** stop to repair the source. That is audit-phase work.
  Anything named this way goes into `control/AUDIT-QUEUE.md`.
- **Style repair at write time.** The 16 outlines researched before the 2026-08-08 tightening
  carry teaser openings and em-dash pivots. Fix them in the prose as you go.
- **Refresh the perishable facts** in the chapter being written, not before. Live items:
  Bears Ears (July 2026 reduction to ~121,100 acres, litigation promised, current only to
  Aug 2026) · corporal-punishment counts · CAHSR and FHWA infrastructure numbers · H-2A
  farm-labor figures (FY2024) · element 120 (no discovery as of 2026) · nuclear restarts and
  SMRs · gig-work litigation (Pew data is Aug 2021) · federal privacy law status ·
  Confederate monument removals · wolf delisting · Oñate/Acoma death toll and sentences
  (RESOLVED: verified in `research/research-native-nations.md` on 2026-09-07).

**Order:** the researched-and-clean chapters first, then the patched ones, then the newly
researched. `native-nations` and `city-building` are done and set the house voice.

**Phase 2 ends when all 37 chapters pass `--stage prose`.**

---

## PHASE 3: Read the finished book

**What this phase is, exactly (Jon, 2026-09-07):** *"If phase 2 did a good job, then the audit
phase will read everything and it will all be perfect and won't have to do anything. Phase 3
only has actions to take if Phase 2 hiccups or fails at understanding how to write following
our rules."*

So Phase 3 is **a read-through, not a repair stage**. It is the confirmation that Phase 2
worked. Its expected result is a report saying the book is clean. **Every finding is evidence
that the guide or the brief failed**, and the fix belongs in the guide as much as in the
sentence, because a defect that appeared once will appear in other chapters written under the same
instructions.

Budget it as reading. If it turns into heavy repair, stop and fix Phase 2's instructions
rather than grinding through 37 chapters of cleanup.

### How this phase is done: an AI reads it. Not a script.

**Language cannot be audited by pattern matching, and we will not try.** A search finds
"empty prairie" and walks past "the land was open for the taking", which is the same erasure.
A search for the em dash character finds em dashes, not em-dash *pivots*. (Since 2026-09-26 the em dash is banned outright, and the prose gate counts it. The pivot still has to be read for, because a writer can build the same move with a colon or a period.) A word-length check finds long words,
not the ones that were the wrong choice. Every defect this project has actually caught was
caught by an AI reading a sentence and understanding what it was doing.

An AI reading carefully against the two style guides should catch every instance. Reading
is the instrument. Trust it and give it the attention the job needs.

The **only** mechanical checks that stay are the ones about file syntax, where the machine is
genuinely authoritative: `node tools/validate_grid.js` and
`python tools/project_state.py --check`. Those verify that markers parse. They say nothing
about whether the book is any good, and they are not to be confused with the read.

### The three reads

Keep them separate. They need different attention and produce different kinds of finding.

**3a: Structure.** Does every file parse and render? Run the validator and the checks first,
because they are cheap and they are the one place automation is right. Then read for what they
cannot see: the 25 silent failures in `VIEWER-CONTRACT.md` §3: records stranded in an
`hb-zoom`, unclosed blocks, duplicate era ids, headings or tables inside blocks, `movie`
attributes out of sync with their blockquote lines. Ends with the whole book open in
`viewer/viewer.html` (v2), looked at.

**3b: Language.** Read every chapter against the Writing Style Guide, Version 2
(`general-writing-style-guide.md`) and the book's amendment (`writing-style-guide.md`).
Check "The AI Cadence", "Forced Rhythm and Sound Patterning", "Register Breaks", "Oversized
Words and Nominalization", "Personification and Anthropomorphism", and "The Teaching Point" (what is this teaching, and how
fast does it get there?). Plus the thing only a full read can judge: **one voice across 37
chapters written by dozens of agents.**

**3c: Fact and source.** Read for what the sources got wrong and the writers inherited.
`city-building` alone produced three land erasures, a false comparison, a manufactured
dispute, and a date that contradicted itself four paragraphs later, all sitting in our own
outline and bank. That is what to read for. Do not look for a phrase. Look for **who was
already there, what the number actually says, and whether the two dates can both be true.**

`control/AUDIT-QUEUE.md` holds the items already known, and they are legacy. They predate the
restructure and would need doing however well Phase 2 goes. Everything else this phase finds
is new information about a failure in Phase 2.

Then: the afterword `how-we-know` (not a grid chapter, no eras) · full-book build ·
Jon's analysis-AI audit pass · final render.

---

## Effort shape

Roughly 17 research + ~15 patch + 35 prose agents. Then a read.

Phase 3 is **not** estimated as production work, and that is deliberate. If the guide does its
job, the read is the last thing that happens and it finds nothing.

**Cost measurement:** `control/usage-log.tsv` now categorises every run by kind (`research`,
`write-prose`, `verify`, `fix`, `audit`, `tooling`) and marks readings that include director
work. Four clean `verify` rows exist and nothing else. Do not size tasks off it until each
category has at least two clean rows. A reading must bracket the agent and nothing else.
