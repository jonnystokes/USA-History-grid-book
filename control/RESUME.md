# RESUME: read this first, every session, no exceptions

> **ENVIRONMENT SWITCH (added 2026-09-26).** Run `python tools/env_check.py` first.
> **LOCAL** (Jon's PC): this file applies exactly as written.
> **CLOUD** (Anthropic's servers, Claude Code on the web): read `control/CLOUD-WORKFLOW.md`
> first. It overrides this file only where the machine differs: paths, the general style
> guide's location, git persistence, and checkpoint files in place of transcript salvage.
> Everything else here still binds. The live plan is `control/TODO.md` in both environments.

You are continuing a long project that **will** be interrupted: a 5-hour or weekly
usage window closes, or your context compacts and you lose the thread mid-task.
This file exists so that costs you minutes, not a day's work.

**The rule that makes it work: never trust a written claim about state. Measure it.**
STATUS.md was once four weeks stale and wrong in both directions, and every session
that read it inherited the error. Prose describes intent. Only the files are true.

---

## The first 60 seconds of any session

Run this. It reads no chapter content and costs almost nothing:

```bash
cd C:/Users/jon/Projects/History-Book-Project-claude && python tools/project_state.py
```

That prints the real stage of all 37 chapters, measured from the files. Then read
the **last entry** of `control/WORKLOG.md`, the append-only ledger of what was
being attempted when the session ended.

If the last entry is `STATUS: IN-FLIGHT`, a task was interrupted. Run the verify
command written in that entry:

```bash
python tools/project_state.py --check <slug> --stage <research|patch|prose>
```

- **exit 0 / PASS:** the work landed before the interruption. Close the entry
  (`STATUS: DONE`) and move on. Do not redo it.
- **exit 1 / FAIL:** the work did not land, or landed partially. The printed
  "measured:" line tells you exactly how far it got. Redo that one task.

That is the whole recovery procedure. It works after a compaction, after a
window reset, and for a brand-new session with no memory of this project at all.

---

## Why the verify command is the only proof

A sub-agent reporting "I completed the research for `war`" is a claim. Four
chapters in this book carry stories tagged `status="verified"` whose own text
still says `[VERIFY]`. That claim was false, and no validator could catch it.
`project_state.py --check` is not a claim. It re-derives the answer from disk and
exits non-zero if the bar is not met.

So: **a task is done when its check passes. Not when an agent says so, not when
the ledger says so.** If the two disagree, the check wins and the ledger is wrong.

`node tools/validate_grid.js` now exits with its error count (fixed 2026-09-06), but
it never runs the renderer, so a clean run is necessary and not sufficient. See
`control/VIEWER-CONTRACT.md` §3. `project_state.py --check` runs it and reads the
printed count, which is the reliable path.

---

## The definitions of done

| Stage | `--stage` | Bar |
|---|---|---|
| Research a chapter | `research` | 10/10 eras researched · 0 `target` · 0 `candidate` · no verified-but-unsourced story · bank ≥ outline words · 0 `[VERIFY]` tags · validator 0 errors on the outline |
| Patch a gapped chapter | `patch` | 0 `target` · 0 `candidate` · no verified-but-unsourced story · bank ≥ outline words · validator 0 errors on the outline |
| Write prose | `prose` | **measured from `manuscript/<slug>/*.md`:** 10/10 eras `progress="written"` · every manuscript story `verified` · 0 `[VERIFY]` tags · 0 em dashes and 0 semicolons (style guide v2, added 2026-09-26) · ≥ 3,000 words · validator 0 errors on every part (with `--part` when there is more than one) |

These bars live in `tools/project_state.py` (`DONE`). Change them there, never by
arguing with them in prose.

**The prose bar was broken until 2026-09-07 and had never once passed.** It derived the stage
from `progress=` flags read out of `outlines/<slug>.md`, where they correctly say `researched`
and never say `written`, and it validated the outline instead of the manuscript. Two finished
chapters measured as FAIL. If a gate has never returned PASS for anything, suspect the gate.

---

## How work is dispatched (context discipline)

The director (you) **never reads chapter content**. That is what burns context
and what compaction then destroys. One chapter is one sub-agent. The director:

1. picks the next chapter from the ROADMAP order,
2. appends an `IN-FLIGHT` entry to `control/WORKLOG.md` **before** dispatching,
3. dispatches one sub-agent with the standard brief (below),
4. on return, ignores the agent's prose and runs the check,
5. closes the ledger entry with the measured result.

Steps 2 and 5 are what survive the interruption. Step 4 is what keeps the book
honest. Never skip either because a task seemed small.

**Batch size: ONE agent at a time.** Jon's instruction, 2026-09-07. Parallel batches burn
a tight usage window faster and make recovery harder. After an interruption there is one
agent to check on and resume, not five. Dispatch one, verify it with the check command,
close its ledger entry, then dispatch the next.

**Size the task to fit a window.** `america-world` was attempted twice as a single agent
and both attempts were killed having written nothing. They spent their whole budget
reading. Split in half, both halves landed first try. For a from-scratch chapter, halve it:
eras 1-5 and 6-10, each writing to its own staging file, and assemble them yourself.

### The three phases (restructured 2026-09-07)

**Research everything → write everything → audit everything.** In that order. Auditing is
**not** interleaved. There are no verification agents and no fix agents between chapters any
more. A writer that finds a defect in its own source fixes it in the prose, names it in its
report, and the director parks it in `control/AUDIT-QUEUE.md` for Phase 3. Full plan in
`control/ROADMAP.md`.

This means **the style guides are the main quality instrument**, not a reference. Since
2026-09-26 there are two: **`control/general-writing-style-guide.md`** (the Writing Style
Guide, Version 2, which Jon made an absolute requirement) and **`control/writing-style-guide.md`**
(this book's amendment: the reader, the subject, the policy). Version 2's rules have headings
and no numbers. The ones a writer needs most are "The Reader", "The AI Cadence", "The
Teaching Point", "Forbidden Punctuation" (zero em dashes, zero semicolons) and "Self-Review
Before Reporting". A writing agent that has not read both files in full has not been briefed.

### Standard sub-agent brief

Every research/patch agent gets, verbatim:

> Validate with `node tools/validate_grid.js <file>`. Add `--part` when the file is
> one part of a multi-file chapter. **Errors mid-write are normal** (an unfinished file
> genuinely has open blocks). **The run that counts is your last one, and it must be
> clean.** If an error survives to the end, fix it or say in your report what it is and
> why you left it. The thing to avoid is shipping one unexamined.
> Read `control/AGENT-BRIEF.md`, `control/hard-subjects-policy.md` (BINDING),
> `control/general-writing-style-guide.md` (Writing Style Guide Version 2, BINDING, read in
> full), `control/writing-style-guide.md` (the book's amendment, BINDING. Personification is
> the rule most often broken), `control/grid-markers.md` §7b and `control/VIEWER-CONTRACT.md` §2 before
> writing anything. You are producing
> `outlines/<slug>.md` and `research/research-<slug>.md` for ONE chapter.
> Your work is judged by `python tools/project_state.py --check <slug> --stage <stage>`.
> Run it yourself before you report, and paste its output as your last line.
> Do not mark a story `status="verified"` unless the research bank sources it.
> A false tag is worse than an honest `target`.
> Check file sizes before reading. Never read `viewer/*.html` whole (line 89 is a
> 373 KB base64 image).

**The LAST agent on a chapter gets one extra line**, added 2026-09-09 after it blocked a
check by itself:

> Before you report, check that EVERY era's `progress=` flag matches its real state. Agents
> clear the `[VERIFY]` tags and verify the stories and forget the era's own flag. A single
> era left at `progress="seed"` will fail the chapter check on its own, no matter how
> finished the content is. Fix the flag. Do not touch another era's content.

Agents report **under 200 words plus the check output**. The director reads that
and nothing else.

### Standard WRITING brief (Phase 2)

Every prose agent gets, verbatim:

> Read these before writing a word, in this order:
> `control/general-writing-style-guide.md`, the Writing Style Guide, Version 2. **BINDING,
> an absolute requirement, and the main instrument of this phase. Read all of it.** "The
> Reader" states who you are writing for. "The AI Cadence" names the patterns you are most
> likely to produce and least likely to notice. Assume you will produce them, and work
> against them. "The Teaching Point" is the positive standard: know what you are teaching and
> state it first. "Forbidden Punctuation" allows zero em dashes and zero semicolons, and the
> prose gate counts both. **"Self-Review Before Reporting" is a review you must actually run,
> repairing every defect it finds, before you report.**
> `control/writing-style-guide.md`, **BINDING**: this book's amendment. It covers the reader
> (age 11, sentences averaging 12 to 18 words), the subject, the policy, and its own audit
> additions in §5.
> `control/hard-subjects-policy.md`, **BINDING.** No softening of any kind. Never invent a
> name. Define clinical words in plain language at first use.
> `control/grid-markers.md` §7b · `control/VIEWER-CONTRACT.md` §2 · your own
> `outlines/<slug>.md` and `research/research-<slug>.md`.
>
> **If your outline or research bank contains a defect (softening, a false comparison, a
> manufactured dispute, personification, a fact that contradicts itself), fix it in your
> prose and NAME IT in your report. Do not stop to repair the source file.** That is
> audit-phase work and it is not yours. This has happened repeatedly and it is expected:
> `city-building`'s outline described land taken from Native nations as "empty prairie", and
> the writer overrode it unprompted. Do that.
>
> Write incrementally: create the file early and append, so an interruption leaves partial
> output rather than nothing.
> Validate with `node tools/validate_grid.js <file>`, adding `--part` when the file is one
> part of a multi-file chapter. **Errors mid-write are normal.** An unfinished file genuinely
> has open blocks. **The run that counts is your last one, and it must be clean.** If an error
> survives, fix it or say what it is and why you left it.
> Your work is judged by `python tools/project_state.py --check <slug> --stage prose`. Run it
> yourself and paste its output as your last line.
> Check file sizes before reading. Never read `viewer/*.html` whole (line 89 is a 373 KB
> base64 image).

---

## After every sub-agent: log its usage

Append one row to `control/usage-log.tsv`. The notification gives you
`subagent_tokens`, `tool_uses` and `duration_ms`. Jon reads the usage percentages off
the UI and tells you them (agents cannot see those). Over time this shows which KINDS
of sub-agent task cost how much of a window, so tasks can be sized to fit one.

**Two rules, both learned the hard way (2026-09-07):**

1. **Categorise every row** in the `kind` column: `research`, `write-prose`, `verify`, `fix`,
   `audit`, `tooling`. Cost correlates with the kind of work, not with a book-wide average.
   Four `verify` runs came in at 9–14% each. The one `fix` run looked completely different.
2. **A clean reading brackets the agent and nothing else.** If the director did work between
   the two percentage readings (sweeps, ledger writes, reading code, asking Jon a question),
   the row measures that stretch, not the agent. Mark it `+` and do not size anything off it.

Markers: no marker = trustworthy · `~` approximate, treat as an upper bound · `+` contaminated
by director work, the agent's share is lower · `?` not captured.

**Do not use the log for sizing until each category has at least two clean rows.** As of
2026-09-07 there are four clean `verify` rows and nothing else. An early "12,000 tokens per
1% of a window" rule was derived from those four and was falsified by the first `fix` run.

## When an interruption is reported: RUN THE DRILL FIRST

```bash
python tools/resume_drill.py
```

One command. It measures what actually landed on disk, lists every sub-agent
transcript and flags which ones died mid-task, states which resume routes exist on
this build, and prints a ready-to-paste continuation brief for the most recent dead
agent. **Run it before deciding anything.** Three times in this project an agent
reported as "failed" had already written its files.

## When a sub-agent dies: SALVAGE BEFORE YOU RE-DISPATCH

**A dead agent's research is not lost.** Its full transcript, including every page
it fetched, survives on disk at
`~/.claude/projects/<key>/<sessionId>/subagents/agent-<agentId>.jsonl`.

```bash
python tools/salvage_agent.py --list              # every transcript, newest first
python tools/salvage_agent.py <agentId> -o out.md # digest it, hand to a fresh agent
```

Two `america-world` agents were written off as a "total loss" and re-run twice.
Their transcripts held 103 and 99 web fetches across 623 and 740 URLs, from congress.gov,
loc.gov, archives.gov. All of it recoverable. **Never re-run a research agent from
zero without salvaging the dead one first.** Transcripts expire in ~30 days.

Full findings: `control/AGENT-MECHANICS.md`.

## AUTONOMOUS MODE: in force from 2026-09-08

**The "stop after every sub-agent and wait for continue" protocol is DECOMMISSIONED.**
Jon's instruction: *"Do one agent at a time, one after the other, till done, doing the
research phase. Don't stop communicating with me till then."*

So: dispatch, verify with the check, close the ledger entry, dispatch the next. **Do not stop
to ask.** Keep reporting after each agent so there is a trail to read. One agent at a time
still holds. Never run a parallel batch.

Jon may be asleep. **Usage percentages will not be captured.** Log those rows with `?` and do
not treat their absence as a problem.

### The automated interruption message

Jon has an automation that sends, verbatim:

> *I hit my usage limit while you were working, but it has reset now. Please continue from
> where you left off.*

**That message means a window closed while a sub-agent was running.** It is not a new task.
When it arrives:

1. `python tools/resume_drill.py` measures what landed on disk, lists transcripts, flags
   which died mid-task. **Run it before deciding anything.**
2. `python tools/salvage_agent.py <agentId> --tail` and `--wrote` on the dead agent show its last
   tool calls and its thinking. This is what tells you WHERE it stopped.
3. **Judge, do not automate the judgement.** Three cases:
   - **Barely started** (still reading, no writes) → dispatch a fresh agent, same brief.
   - **Partway through writing** → digest its transcript and hand the digest to a new agent as
     a continuation brief, so it resumes instead of restarting. `salvage_agent.py <id> -o
     out.md` produces the digest. Decide yourself how much of it to pass on.
   - **Finished writing but never reported** → run the check. Three times in this project an
     agent reported as failed had already written its files.
4. Then carry on down the queue.

**A killed agent's work is never lost.** Its full transcript, every page it fetched, survives
at `~/.claude/projects/<key>/<sessionId>/subagents/agent-<agentId>.jsonl` for ~30 days. Two
`america-world` agents were written off as a total loss and re-run twice. Their transcripts
held 103 and 99 web fetches the whole time. **Never re-run a research agent from zero without
salvaging the dead one first.**

## When Jon says "pause"

**Stop what you are doing and wait.** No new dispatches, no new actions. Say what state
things are in.

**Leave running sub-agents alone** (Jon, 2026-09-07). Let them finish or die with the
window. There is no way to message them anyway, and `TaskStop` only kills. An agent
killed just before its write loses exactly the output worth keeping. Their transcripts
survive regardless and are salvageable.

## When a window is about to close

You usually get warning. Spend it on the ledger, not on one more chapter:

1. Append or update the `IN-FLIGHT` entries for anything running.
2. Write one line per in-flight task saying what the *next* action is.
3. Do not start a new sub-agent you cannot verify before the window ends.

## When context is about to compact

Same thing, plus: the ledger and `project_state.py` are the memory. Anything you
know that is not in a file is about to be lost, so put it in a file. A fact worth
keeping goes in `control/`. A decision by Jon goes in the relevant `workspace/<slug>.md`
and in the ledger.

---

## Where everything lives

| Need | File |
|---|---|
| Real state, measured | `python tools/project_state.py` |
| What was in flight | `control/WORKLOG.md` (tail) |
| The plan and its order | `control/ROADMAP.md` |
| Per-chapter narrative notes | `control/STATUS.md` (descriptive only. Numbers there may be stale) |
| How research is done | `control/AGENT-BRIEF.md` |
| **Tone rules (binding)** | `control/hard-subjects-policy.md` (no softening, never invent a name) |
| Jon's twelve rulings | `control/DECISIONS.md` |
| The file format | `control/grid-markers.md` |
| What the viewer really does | `control/VIEWER-CONTRACT.md` |
| Prose skeleton | `templates/chapter-template.md` |
| Jon's open decisions | `workspace/<slug>.md`, "Open questions for the director" |
