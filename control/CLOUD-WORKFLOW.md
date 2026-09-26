# CLOUD WORKFLOW: the rules when this project runs on Anthropic's servers

**Created 2026-09-26.** Jon moved the project from his Windows PC to GitHub so it can run
in Claude Code on the web. **This file applies only in the CLOUD environment.** On Jon's PC,
`control/RESUME.md` applies exactly as written, and this file can be ignored.

```bash
python tools/env_check.py      # prints CLOUD or LOCAL and which file to follow
```

Detection is automatic: the cloud harness sets `CLAUDE_CODE_REMOTE=true`. Windows means LOCAL.

**Everything in RESUME.md still holds in the cloud unless this file overrides it.** That
includes the three phases, the ledger, one agent at a time, the verify gate, the director
never reading chapter content, and the standard briefs. This file changes only what depends
on the machine.

---

## 1. What is different here

| Thing | LOCAL (Jon's PC) | CLOUD (this file) |
|---|---|---|
| Project root | `C:/Users/jon/Projects/History-Book-Project-claude` | `/home/user/USA-History-grid-book` (a fresh clone from GitHub) |
| General style guide | Version 1 at `C:\Users\jon\Projects\writing-style-guide.md`, **superseded 2026-09-26** | **Both environments:** `control/general-writing-style-guide.md` (Version 2, an absolute requirement) |
| What survives an interruption | Everything on disk | **Only what is committed and pushed to GitHub.** The container is deleted after inactivity. |
| Dead agents' transcripts | `~/.claude/projects/...` for ~30 days | Same path, but **only while this container lives.** A new session gets a new container and none of the old transcripts. |
| Salvage | `salvage_agent.py`, `resume_drill.py` | Work in the same container. After a container change, **the checkpoint file (§3) is the salvage.** |
| Interruption message | Jon's automation sends it | Jon types "continue" when the window resets (or a `send_later` check-in fires, §6) |
| Usage percentages | Jon reads them off the UI | Not visible to the agent. Log tokens, tool uses and minutes, and mark the % column `?`. |
| GitHub | n/a | GitHub MCP tools only. There is no `gh` CLI. |
| Branch | whatever Jon uses | **`claude/gifted-volta-lfl54k`**. Never push to `main`. Jon merges when he brings the work home. |
| Python | `python` | `python` and `python3` both work (3.x). Node 22 is on PATH. Chromium for Playwright is at `/opt/pw-browsers`. |
| Web research | open | Open through a proxy. loc.gov, archives.gov, nps.gov and wikipedia answer. **britannica.com returns 403**: cite another source. |

The commands in RESUME.md that start `cd C:/Users/jon/...` run here from the project root
with no `cd`.

---

## 2. The first minute of a cloud session

```bash
python tools/env_check.py                  # confirm CLOUD
git fetch origin claude/gifted-volta-lfl54k && git status
python tools/project_state.py              # the measured truth
ls control/checkpoints/                    # any task with an open checkpoint?
tail -60 control/WORKLOG.md                # the last entry
```

Then read `control/TODO.md` for the current plan and the next step.

- **The last WORKLOG entry is IN-FLIGHT:** run its VERIFY command. Then open
  `control/checkpoints/<task>.md`. It says exactly which unit the agent finished and which
  one it was on. Resume from there (§4).
- **The local branch is behind origin:** pull first. An agent may have pushed after the
  director's last commit.

---

## 3. The checkpoint protocol (every sub-agent, every task)

On Jon's PC a dead agent's transcript was the safety net. In the cloud that net vanishes with
the container. **The checkpoint file replaces it, and git makes it permanent.**

Each task gets one file: `control/checkpoints/T-<nnn>-<slug>.md`. The director creates it
from `control/checkpoints/_TEMPLATE.md` **before** dispatching, next to the IN-FLIGHT ledger
entry. The agent keeps it current.

**The agent's obligations, which go into every cloud brief (§5):**

1. **Break the task into units before starting.** Use one era for research or a patch, and
   one era or one part file for prose. List them in the checkpoint's unit table.
2. **Finish one unit, then save.** Write its content to the real files, validate, and update
   the checkpoint. The checkpoint records what landed, which sources were used, what was
   left out and why, and exactly what comes next. Then commit and push:
   ```bash
   git add outlines/<slug>.md research/research-<slug>.md manuscript/<slug>/ control/checkpoints/T-<nnn>-<slug>.md
   git commit -m "T-<nnn> <slug>: <unit> done"
   git push -u origin claude/gifted-volta-lfl54k
   ```
   If the push fails for a network reason, retry after 2, 4, 8 and 16 seconds. Use only
   `git add` with named paths, never `git add -A`.
3. **Keep a "Sources in hand" list** in the checkpoint for research tasks. Record the URLs
   already fetched and what each one settled. A successor then re-reads rather than
   re-searches. This is the cloud version of `salvage_agent.py --urls`.
4. **Before starting a new unit**, set the checkpoint's `NOW:` line to that unit and push.
   A successor then knows the unit may be half-written and checks it first.
5. **Never leave a unit half-saved without saying so.** If you notice you are near your
   limit, stop at a unit boundary, update `NOW:` and `NEXT:`, and push.

A task is resumable by a stranger when its checkpoint answers four questions: what is done,
what was the agent doing, what does it know that is not in the files yet, and what is next.
Write it for that stranger.

**The director's obligations:**
- Create the checkpoint and the IN-FLIGHT entry, commit and push **before** dispatching.
- On return, run the verify check. Then close the WORKLOG entry, set the checkpoint's
  `STATUS:` to `DONE` or `PARTIAL`, update `control/TODO.md`, add the usage-log row, and
  commit and push.
- Do not commit while an agent is running. Only one agent runs at a time, so the agent owns
  the working tree until it returns.

Checkpoints are useful on Jon's PC too. `AGENT-BRIEF.md` now asks for one in both
environments. Only the git push is cloud-only.

---

## 4. Resuming an interrupted task

1. `git pull` so you have whatever the dead agent pushed.
2. Run the task's VERIFY. **PASS** means it landed: close it and move on.
3. **FAIL:** read the checkpoint (a small control file, not chapter content). Then:
   - `NOW:` is a unit with no "landed" note: check that unit's markers in the file
     (`progress=` flags and `[VERIFY]` counts, via grep). Tell the new agent the unit may be
     half-written.
   - Dispatch a fresh agent with the **same brief plus one line**: *"This task was
     interrupted. Read `control/checkpoints/T-<nnn>-<slug>.md` first. Resume from its NEXT
     line. Do not redo units marked landed. Re-use its Sources in hand."*
   - If this container still holds the dead agent's transcript
     (`python tools/salvage_agent.py --list`), salvage it as RESUME.md says. That is a bonus,
     not the plan.
4. Keep the same T-number for the continuation, suffixed `b`, `c`, and so on (T-233b), so
   the ledger shows one task done in several goes.

---

## 5. The cloud brief: add these lines to every standard brief in RESUME.md

> **Cloud environment.** You are running on Anthropic's servers in a container that can be
> deleted without warning. Only what you commit and push survives. Your checkpoint file is
> `control/checkpoints/T-<nnn>-<slug>.md`. Read it first, keep it current, and commit and
> push after EVERY unit as it describes (branch `claude/gifted-volta-lfl54k`, `git add`
> with named paths only, never a push to main). A successor who has only your checkpoint and the
> files must be able to carry on without redoing your work.
> The general style guide is `control/general-writing-style-guide.md` (Version 2). If an
> older document mentions `C:\Users\jon\Projects\writing-style-guide.md`, read Version 2
> instead. That older file is superseded.
> britannica.com is blocked here. Cite another source.

Dispatch with the `Agent` tool, `subagent_type: general-purpose`, in the background, one at a
time. Agents cannot spawn further agents here (spawn depth 1).

---

## 6. Interruptions and the usage window

- The session stops when the usage limit is reached. The container may survive a short gap,
  but a long gap usually means a new container. **Plan for the new container.**
- When the window is about to close, follow RESUME.md's steps, then **commit and push**. A
  note that is not pushed does not exist.
- A `send_later` self-check-in can wake the session after a window resets. Use it only if
  Jon asks, because it spends usage.

---

## 7. Bringing the work back to Jon's PC

1. On GitHub, merge `claude/gifted-volta-lfl54k` into `main`, or pull the branch locally.
2. `python tools/env_check.py` reports LOCAL, and RESUME.md applies again unchanged.
3. The cloud-only file (this one) does no harm locally. `control/checkpoints/`,
   `control/TODO.md` and `control/general-writing-style-guide.md` (style guide Version 2)
   apply in both environments.
4. The WORKLOG entries made in the cloud are marked `[CLOUD]`. Their agent IDs point at
   transcripts that were never on the PC, so salvage will not find them. Their checkpoints
   hold what salvage would have given you.
