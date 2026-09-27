# RESUME: read this first, every session

This project **will** be interrupted: a usage window closes, or context compacts mid-task.
This file makes that cost minutes, not a day. **The rule: never trust a written claim about
state. Measure it.** STATUS.md was once four weeks stale, and every session that read it
inherited the error.

Trimmed 2026-09-26. The full earlier version, with its history and the old brief texts, is
at `control/archive/RESUME-before-2026-09-26-trim.md`. The cloud workflow is archived in
`control/archive/cloud/` (read its README before any online session, and ask Jon).

---

## The first minute of any session

```bash
python tools/env_check.py          # LOCAL is expected. CLOUD: stop and read control/archive/cloud/README.md
python tools/project_state.py      # the real stage of all 37 chapters, measured
tail -60 control/WORKLOG.md        # the last entry
```

Then read `control/TODO.md` (the live plan and the next step).

If the last WORKLOG entry is `STATUS: IN-FLIGHT`, run the VERIFY command in it:

- **PASS:** the work landed before the interruption. Close the entry. Do not redo it.
- **FAIL:** the "measured:" line says how far it got. Read the task's checkpoint, then follow
  "When an agent dies" below.

## The definitions of done

| Stage | `--stage` | Bar |
|---|---|---|
| Research | `research` | 10/10 eras researched · 0 `target` · 0 `candidate` · no verified-but-unsourced story · bank ≥ outline words · 0 `[VERIFY]` · validator 0 errors on the outline |
| Patch | `patch` | 0 `target` · 0 `candidate` · no verified-but-unsourced story · bank ≥ outline words · validator 0 errors |
| Prose | `prose` | from `manuscript/<slug>/*.md`: 10/10 eras `written` · every story `verified` · 0 `[VERIFY]` · 0 em dashes · 0 semicolons · ≥ 3,000 words · validator 0 errors on every part |

The bars live in `tools/project_state.py` (`DONE`). Change them there, never by arguing with
them in prose. **A task is done when its check passes,** not when an agent or the ledger says so.
A clean `validate_grid.js` run is necessary and not sufficient (`VIEWER-CONTRACT.md` §3).

## The plan: eight steps, in order (Jon, 2026-09-26, DECISIONS #17)

1. **Research** every chapter, feature complete. The bank check is part of it.
2. **Write** every chapter, feature complete. Writers research their own small gaps.
3. **Audit** the whole book: sonnet checkers read, report findings, and edit nothing.
4. **Research round 2:** only the gaps that writing and auditing found.
5. **Writing round 2:** opus fixers apply the audit findings and fill those gaps.
6. **Audit** again, to confirm.
7. **Polish.**
8. **Done.**

No step starts until the one before it is finished for the whole book. Detail and the chapter
order are in `control/ROADMAP.md`.

## How work is dispatched

The director (you) **never reads chapter content.** That burns context, and compaction then
destroys it. For each task:

1. Pick the next task from `control/TODO.md`.
2. Create its checkpoint from `control/checkpoints/_TEMPLATE.md`, and append an `IN-FLIGHT`
   entry to `control/WORKLOG.md` **before** dispatching.
3. Dispatch **one** sub-agent (`general-purpose`, in the background) with the brief from
   `control/briefs/` and **the model the policy names** (`control/briefs/README.md`): opus for
   research, writing and fixing, sonnet for checking and salvage reading. Always set `model`.
4. On return, ignore the agent's prose and **run the check.**
5. Close the WORKLOG entry with the measured result, add the usage-log row, update TODO.
6. **Make one local commit** of that agent's work (DECISIONS #19), by named paths, with the
   stats in the message:
   `T-<nnn> <slug>: <what landed> [<model>, <tokens> tokens, <tool uses> tools, <minutes> min]`
   **No push, pull or any GitHub step unless Jon asks.**
7. Next task.

**One agent at a time,** always (Jon, 2026-09-07). **Size each task to fit a window:** an agent
that spends its budget reading dies with nothing written. Use `python tools/slice_bank.py <slug>
--eras <a-b> --summary` to see how many words a task must read. As a rule of thumb, split a
task when its outline and bank slice pass about 25,000 words.

**Autonomous mode** (Jon, 2026-09-08): once Jon says to run, dispatch, verify, close and
dispatch the next without stopping to ask, reporting after each agent. Stop when Jon says
"pause" or "stop", and when a phase ends.

## The usage log

After every sub-agent, append a row to `control/usage-log.tsv`. The completion notice gives
`subagent_tokens`, `tool_uses` and `duration_ms`. Put the model in the `agent_type` column
(`general-purpose/opus`). Jon reads usage percentages off the UI when he is present. Log `?`
when he is not. The header of the file explains the markers. **Every row gets its tokens.**
Sizing decisions rest on them.

## When an interruption is reported: run the drill first

Jon's automation sends: *"I hit my usage limit while you were working, but it has reset now.
Please continue from where you left off."* That means a window closed while an agent ran.

```bash
python tools/resume_drill.py       # what landed, which transcripts died, a draft continuation brief
```

Three times in this project an agent reported as failed had already written its files.

## When an agent dies: salvage before you re-dispatch

Its full transcript, every page it fetched, survives for about 30 days at
`~/.claude/projects/<key>/<sessionId>/subagents/agent-<agentId>.jsonl`.

```bash
python tools/salvage_agent.py --list                 # every transcript, newest first
python tools/salvage_agent.py <agentId> --tail       # its last actions
python tools/salvage_agent.py <agentId> -o out.md    # a digest
```

Then judge:
- **Barely started** (still reading, nothing written): dispatch a fresh agent, same brief.
- **Partway through writing:** dispatch a **sonnet** reader with `control/briefs/SALVAGE.md` on
  the digest. It writes a measured SALVAGE section into the checkpoint. Then dispatch an opus
  continuation agent with the same brief plus: *"This task was interrupted. Read the
  checkpoint's SALVAGE section first and resume from its NEXT line. Do not redo landed units."*
  Keep the T-number and add a suffix (T-243e2).
- **Finished writing, never reported:** run the check.

**A file that validates is not a finished file.** A killed agent can leave an era that parses
and is half-written (T-242c). **Never re-run a research agent from zero without salvaging the
dead one first.** Two `america-world` agents were written off while their transcripts held 103
and 99 web fetches. Mechanics: `control/AGENT-MECHANICS.md`.

## When Jon says "pause"

Stop and wait. No new dispatches. Say what state things are in. **Leave running agents alone**
(Jon, 2026-09-07). An agent killed just before its write loses the output worth keeping.

## When a window is about to close, or context is about to compact

Spend the time on the ledger, not one more task: update the `IN-FLIGHT` entries and the
checkpoints with the next action, update TODO, and do not start an agent you cannot verify.
Anything you know that is not in a file is about to be lost. Decisions by Jon go into
`control/DECISIONS.md`, the relevant `workspace/<slug>.md`, and the ledger.

---

## Where everything lives

| Need | File |
|---|---|
| Real state, measured | `python tools/project_state.py` |
| The live plan and next step | `control/TODO.md` |
| What was in flight, what happened | `control/WORKLOG.md` (read the tail only, it is large) |
| The plan and its order | `control/ROADMAP.md` |
| The briefs and the model policy | `control/briefs/README.md` |
| One chapter's eras only | `python tools/slice_bank.py <slug> --eras <a-b>` |
| The writing rules (binding) | `control/general-writing-style-guide.md` (v2), `control/writing-style-guide.md`, `control/hard-subjects-policy.md` |
| How research is done | `control/AGENT-BRIEF.md` |
| Jon's rulings | `control/DECISIONS.md` |
| Known defects waiting for the audit | `control/AUDIT-QUEUE.md` |
| Checker calibration | `control/audit/CHECKER-CALIBRATION.md` |
| The file format and the viewer | `control/grid-markers.md`, `control/VIEWER-CONTRACT.md` |
| Sub-agent mechanics and salvage | `control/AGENT-MECHANICS.md` |
| Per-chapter notes and open questions | `workspace/<slug>.md` |
| Archived: cloud workflow, old RESUME | `control/archive/` |
