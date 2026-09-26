# History Book Project — instructions for any AI working here

## Which environment? Check first: `python tools/env_check.py`

- **CLOUD** (Anthropic's servers; `CLAUDE_CODE_REMOTE=true`): read **`control/CLOUD-WORKFLOW.md`**
  first, then `control/TODO.md`. RESUME.md still applies wherever CLOUD-WORKFLOW does not
  override it. Only what is committed and pushed survives here.
- **LOCAL** (Jon's PC): **read `control/RESUME.md` first.** It is short and tells you how to find the real state.

A 37-chapter plain-language US history book for ages 8–15, written as a grid (37
subjects × 10 fixed eras) in an HTML-comment marker format a viewer parses.

**This file is loaded into every sub-agent spawned here, so it stays short.** Detail lives
in the files it points to; read those when they apply.

## The writing — three BINDING files, read in this order

1. **`C:\Users\jon\Projects\writing-style-guide.md`** (LOCAL) or **`control/general-writing-style-guide.md`**
   (CLOUD, the repo copy) — the general prose rules and their repairs. **Required in full before you write or judge a sentence.** Section numbers in the
   bullets below refer to it.
2. **`control/writing-style-guide.md`** — this book's amendment: the reader, the subject, the
   order. It wins over the general file on the reader, the subject and the policy; the general
   file wins on prose mechanics.
3. **`control/hard-subjects-policy.md`** — no softening, never invent a name, define clinical words.

- **No language softening, ever** — euphemism, minimization, downplaying, semantic
  abstraction, sanitization, gist extraction, lossy summarization. This book's reader does
  not know this history and cannot reconstruct what you left out, so anything softened
  becomes what they believe happened. `outlines/native-nations.md:183` is the floor.
- **Never invent a name.** Named account → name it. Documented but unnamed → tell it
  unnamed, in `hb-zoom` prose. `hb-story` blocks are named people only. No composites.
- **No personification** (general guide §1.1). A law, act, treaty, school or agency cannot do
  anything — name the people. Most often broken *while repairing a passive*.
- **No reification or agentless passives** (general guide §1.15, §1.16). An abstraction is not
  a thing that acts, and every passive names an actor who could perform the action.
- **Define clinical words** (policy §3b): sterilization, lobotomy, flogging. Say what it
  is, what it did to the person, and by what method.
- **Thin eras are correct.** Never pad; never merge unlike subjects to fill a cell.
- Plain is not lurid: no adjectives telling the reader how to feel, no staged scenes.
- **Write for an 11-year-old** (project amendment §1): sentences 12–18 words, one idea each,
  the shortest word that means it, every hard word defined in plain language at first use.
- **No AI cadence** (general guide §1.11 — the failure you are most likely to produce and least
  likely to notice): no triads, no repeated sentence openings, no em-dash pivots, no "not just
  X but Y", no fragments for emphasis, no closing reversals, no rhetorical questions. Each move
  there comes with its repair. Read it aloud; if it sounds performed rather than explained,
  rewrite it.
- **One plain present-day voice** (general guide §1.13, project amendment §2). A chapter about
  1550 sounds like a chapter about 2020. No "thus", "sought to", "would come to", "little did
  they know".
- **Know what you are teaching and get to it** (general guide §2.6, and the 25-word rule in
  project amendment §4). Withholding a fact for suspense is a form of softening.

## The work — full rules in `control/RESUME.md` and `control/AGENT-MECHANICS.md`

**Three phases, in order: research everything → write everything → audit everything.**
Auditing is not interleaved. If you find a defect in your own outline or research bank, **fix
it in your prose, name it in your report, and do not repair the source file** — the director
parks it in `control/AUDIT-QUEUE.md` for the audit phase.

1. **Measure, never trust.** `python tools/project_state.py` gives the real state. Prose
   docs go stale — STATUS.md was once four weeks wrong and every session inherited it.
2. **A task is done when its check passes**, not when an agent says so:
   `python tools/project_state.py --check <slug> --stage <research|patch|prose>`.
3. **Log before you dispatch.** `IN-FLIGHT` entry in `control/WORKLOG.md` first, closed
   with the pasted check output after.
4. **One sub-agent at a time**, and the director never reads chapter content.
5. **When an agent dies, salvage before re-dispatching** — `python
   tools/salvage_agent.py --list`. A killed agent cannot be resumed in this build, but its
   full transcript survives on disk. Two agents were once written off as lost and re-run
   twice; their research was recoverable the whole time.
6. **Make agents write early and often.** An agent killed before its first write leaves
   nothing; one killed after leaves its file.

## Hazards

- `node tools/validate_grid.js` never runs the renderer, so a clean run is necessary, not
  sufficient — `control/VIEWER-CONTRACT.md` §3 lists 25 silent failures.
- `viewer/viewer.html` (v2 — use this) and `viewer-v1.html`: **line 89 of each is a
  ~373,500-character base64 image.** Never read either whole. Check file sizes before
  reading anything here.
- Never mark a story `verified` unless the research bank sources it.

## The absolute rule of the book

No invented facts. Research first. Write clearly. Do not change the facts.
