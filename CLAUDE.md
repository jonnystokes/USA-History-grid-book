# History Book Project: instructions for any AI working here

## Which environment? Check first: `python tools/env_check.py`

- **LOCAL** (Jon's PC, where the project runs now): **read `control/RESUME.md` first.** It is
  short and tells you how to find the real state. Then `control/TODO.md`.
- **CLOUD** (Anthropic's servers, where `CLAUDE_CODE_REMOTE=true`): the cloud workflow is
  **archived** in `control/archive/cloud/` (2026-09-26). Read its README and ask Jon before
  doing any work.

This project is a 37-chapter, plain-language US history book for readers aged 8 to 15. It is
written as a grid of 37 subjects by 10 fixed eras, in an HTML-comment marker format that a
viewer parses.

**Every sub-agent spawned here loads this file, so it stays short.** The files it points to
contain the detail. Read them when they apply.

## The writing: three BINDING files, read in this order, in both environments

1. **`control/general-writing-style-guide.md`**, the Writing Style Guide, Version 2. It
   contains the general prose rules and their repairs. **Read it in full before you write or
   judge a sentence.** Jon adopted it on 2026-09-26 as an absolute requirement. It replaces
   Version 1 at `C:\Users\jon\Projects\writing-style-guide.md`. Its rules have headings and
   no numbers, so the bullets below cite them by heading.
2. **`control/writing-style-guide.md`**, this book's amendment. It covers the reader, the
   subject and the order. It governs the reader, the subject and the policy. Version 2
   governs prose mechanics.
3. **`control/hard-subjects-policy.md`**: no softening, never invent a name, define clinical
   words.

- **Jon's seven guidelines come first** (`control/writing-style-guide.md` §0, DECISIONS #28): the
  whole truth in plain words (rape, not assault), fit the age by clarity not omission, fun to read
  with real people and true detail, the director settles disagreements, no accusation against a
  living person told as fact, and **no big words anywhere** ("charged with a crime", not "indicted").
- **No language softening, ever.** That covers euphemism, minimization, downplaying,
  semantic abstraction, sanitization, gist extraction and lossy summarization. This book's
  reader does not know this history and cannot reconstruct what you left out. Anything
  softened becomes what the reader believes happened. `outlines/native-nations.md:183` is
  the floor.
- **Facts come from the research bank.** Every fact in the prose must be in
  `research/research-<slug>.md`. When the outline states something the bank does not, a
  writer may look it up with a few searches, add it to the bank as a PATCH, and then write it.
  If nothing is found, record `SEARCHED, NOT FOUND` in the bank and say plainly what the
  records do not say (DECISIONS #13, #21, `control/briefs/WRITER.md`).
- **Never invent a name.** When an account names a person, name the person. When a
  documented account names no one, tell it unnamed, in `hb-zoom` prose. `hb-story` blocks
  are for named people only. No composites.
- **No personification** ("Personification and Anthropomorphism"). A law, act, treaty,
  school or agency cannot do anything. Name the people. Writers break this rule most often
  *while repairing a passive*.
- **No reification and no passive without an actor** ("Reification", "Passives with a
  Missing or False Agent"). An abstraction does not act. When someone was harmed, name who
  did it, or state that the records do not say.
- **Zero em dashes and zero semicolons** in anything a reader of the book will see
  ("Forbidden Punctuation"). The prose gate counts both characters and fails a chapter on a
  single one.
- **Define clinical words** (policy §3b): sterilization, lobotomy, flogging. State what the
  word means, what it did to the person, and by what method.
- **Thin eras are correct.** Never pad a cell. Never merge unlike subjects to fill one.
- **Plain is not lurid.** No adjectives that tell the reader how to feel. No staged scenes.
- **Write for an 11-year-old** (amendment §1). Sentences average 12 to 18 words and carry
  one idea each. Use the shortest word that means the thing. Define every hard word in plain
  language at first use.
- **No AI cadence** ("The AI Cadence"). You are more likely to produce this failure than any
  other and less likely to notice it. The table under that heading lists each move with its
  repair: the triad, anaphora, the em-dash pivot, "not just X but Y", the fragment for
  emphasis, the closing reversal, and the rhetorical question. Read the draft aloud. If it
  sounds performed rather than explained, rewrite it.
- **One plain present-day voice** ("Register Breaks", amendment §2). A chapter about 1550
  uses the same voice as a chapter about 2020. Do not write "thus", "sought to", "would come
  to" or "little did they know".
- **State the teaching point first** ("The Teaching Point", and the 25-word rule in
  amendment §4). Withholding a fact for suspense is a form of softening.
- **Run "Self-Review Before Reporting"** from Version 2, then the amendment's §5 audit
  additions, before you report any writing as finished.

## The work: full rules in `control/RESUME.md` and `control/AGENT-MECHANICS.md`

**The project runs in eight steps, strictly in order** (DECISIONS #17): research, write,
audit the whole book, research round 2, writing round 2, audit, polish, done. Auditing is not
interleaved. If you find a defect in your own outline or research bank, **fix it in your
prose, name it in your report, and leave the source file alone.** The director parks the
defect in `control/AUDIT-QUEUE.md` for the audit.

**Briefs and models:** every sub-agent gets a brief from `control/briefs/` and an explicit
model (`control/briefs/README.md`): **opus** for research, writing and fixing, **sonnet** for
reading and checking. **No GitHub** unless Jon asks. The director makes one local commit after
each sub-agent. **Never shrink the book** (DECISIONS #20).

1. **Measure, never trust.** `python tools/project_state.py` reports the real state. Prose
   documents go stale. STATUS.md was once four weeks out of date, and every session
   inherited the error.
2. **A task is done when its check passes**, not when an agent says so:
   `python tools/project_state.py --check <slug> --stage <research|patch|prose>`.
3. **Log before you dispatch.** Write the `IN-FLIGHT` entry in `control/WORKLOG.md` first.
   Close it afterwards with the pasted check output.
4. **Run one sub-agent at a time.** The director never reads chapter content.
5. **Keep a checkpoint.** Every task has `control/checkpoints/T-<nnn>-<slug>.md`. The agent
   updates it after every unit, so a new agent can resume the task.
6. **When an agent dies, salvage before re-dispatching.** Read its checkpoint, and run
   `python tools/salvage_agent.py --list` while the transcript is still on this machine.
7. **Make agents write early and often.** An agent killed before its first write leaves
   nothing. An agent killed after it leaves its file.

## Hazards

- A clean run of `node tools/validate_grid.js` is necessary and not sufficient, because the
  validator never runs the renderer. `control/VIEWER-CONTRACT.md` §3 lists 25 failures the
  validator cannot see.
- In `viewer/viewer.html` (version 2 of the viewer, the one to use) and in
  `viewer-v1.html`, **line 89 is a base64 image of about 373,500 characters.** Never read
  either file whole. Check file sizes before reading anything here.
- Never mark a story `verified` unless the research bank sources it.

## The absolute rule of the book

No invented facts. Research first. Write clearly. Do not change the facts.
