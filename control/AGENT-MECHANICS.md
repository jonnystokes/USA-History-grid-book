# AGENT MECHANICS — what is actually true about sub-agents in this session

**Hands-on findings, 2026-09-07. Build: Claude Code 2.1.260, entrypoint
`claude-desktop`** (read from the `version` field on the newest record in this
session's own transcript — the CLI is not on PATH and `~/.claude.json` has no
version field). Everything here was tested in this build, not read in
documentation. Where the documentation and the machine disagree, the machine is
recorded. Version-gate every claim below.

---

## 1. The headline: a dead agent's work is NOT lost

**An agent killed mid-task cannot be resumed. Its research can be recovered in
full.** These are different questions and they have different answers.

Every sub-agent writes a complete transcript to
`~/.claude/projects/<project-key>/<sessionId>/subagents/agent-<agentId>.jsonl`,
alongside a small `.meta.json` giving its task description, agent type and spawn
depth. **That file survives the agent's death, is unaffected by compaction of the
main conversation, and contains every page the agent fetched.**

Measured on the two `america-world` research agents this project wrote off as a
"total loss" after both were killed by usage limits before writing a line:

| | attempt 1 | attempt 2 |
|---|---|---|
| transcript | 1,018,159 bytes | 979,168 bytes |
| web calls | 103 | 99 |
| distinct URLs | 623 | 740 |
| top sources | congress.gov (85), history.state.gov (46), loc.gov (41), archives.gov (27) | wikipedia (110), history.state.gov (20), guampedia (13) |

That is hours of primary-source research. It was declared destroyed, and then
**paid for twice more** with fresh agents. It was on disk the whole time.

### The salvage procedure

```bash
python tools/salvage_agent.py --list                 # every transcript, newest first
python tools/salvage_agent.py <agentId> -o out.md    # digest: task, reasoning, sources, raw material
python tools/salvage_agent.py <agentId> --urls       # just the source list (cheapest)
```

Tested end to end: the two dead agents above produced 358 KB digests carrying
*Downes v. Bidwell*, the unincorporated-territory doctrine, and 60+ mentions of
Guam. Hand the digest to a fresh agent as prior work. **That is a manual resume,
and it needs no tooling that does not already exist.**

⚠ **Transcripts expire.** `cleanupPeriodDays` defaults to 30 and is not set in
this config. Salvage promptly; do not assume last month's run is still there.

**So the rule after any agent death is: SALVAGE FIRST, RE-DISPATCH SECOND.** Never
re-run a research agent from zero without checking what the dead one already found.

---

## 2. What does not exist here (verified, not assumed)

- **`SendMessage` is not provisioned.** Verified by direct name-select of seven
  tools: `ListAgents`, `TaskStop`, `Workflow`, `Agent`, `Artifact`, `TaskOutput`
  all returned; `SendMessage` did not. **Therefore no sub-agent can be resumed by
  any route in this session.**
- This is despite the documentation referring to it repeatedly: `ListAgents`'s own
  description says "Lists agents you can `SendMessage` to", and the `Agent` tool's
  says "Use `SendMessage` with the agent's ID or name to continue a previously
  spawned agent." **The docs describe a tool this build does not have.** Do not
  plan around it.
- **The `Agent` tool has no `name` parameter.** Its full schema here is
  `description`, `isolation`, `model`, `prompt`, `run_in_background`,
  `subagent_type`. So "always name your agents so you can address them later" is
  not actionable in this build.
- **No `maxTurns` parameter** — but this is expected on every build and was my
  error to report as a finding. `maxTurns`, `tools`, `permissionMode`, `memory`,
  `hooks` and `effort` are **frontmatter fields in a custom agent definition
  file**, not per-call parameters. See §2b.
- **`fork` is gated behind a flag, not absent** — corrected 2026-09-07 after a
  second test. A `fork` spawn first returned *"Agent type 'fork' not found"*, but
  setting `env.CLAUDE_CODE_FORK_SUBAGENT=1` in `~/.claude/settings.json` made it
  available **mid-session, without a restart**. The tool description references
  `fork` behaviour while giving no hint that a flag is required. See §2d — and note
  that fork turned out to be the *expensive* path here, not the cheap one.

## 2b. Custom agent definitions do NOT hot-register (tested)

Wrote a valid `probe.md` with `maxTurns: 2` into **both** scopes — the session's
project root `C:/Users/jon/Projects/.claude/agents/` and user-level
`~/.claude/agents/` — and both spawns failed with *"Agent type 'probe' not found.
Available agents: claude, claude-code-guide, Explore, general-purpose, Plan,
statusline-setup."*

**Caveat that keeps this honest:** neither directory existed when this session
started, and the documented behaviour is that the watcher picks up new files only
if the directory already existed. So this test cannot distinguish "hot-reload is
broken" from "hot-reload requires a pre-existing directory."

**ANSWERED 2026-09-07, and the answer is the second half of the caveat.** The two
definitions I wrote (`probe`, `probe2`) DID eventually register — the runtime
announced them as newly available agent types later in the same session, without a
restart, some time after the files were written. So:

- **Custom agent definitions DO work on this build.** `maxTurns`, `tools`,
  `permissionMode`, `memory` and `hooks` frontmatter are all available via
  `.claude/agents/*.md`, in either the project or user scope.
- **They do not appear instantly.** Two spawns immediately after writing the files
  failed with "Agent type 'probe' not found". Registration arrived later. So a new
  definition is not usable in the moments after you write it — write it, then carry
  on with something else and use it later, or restart.
- Practical consequence: the controlled-interruption test (`maxTurns: 2`) is now
  available for near-zero cost whenever it is wanted, and agent definitions are a
  real way to hand a repeated role its own tool restrictions and turn budget.

## 2c. Addressability is one subsystem, not two missing pieces

The absent `name` parameter and the absent `SendMessage` tool are almost certainly
the same gap rather than two: an agent is made addressable by being named, and a
roster of addressable agents is pointless without naming. This build excludes the
subsystem as a unit. **Consequence: stop looking for a flag that enables
`SendMessage`. There isn't one.** And the `ListAgents` roster was never the
recovery index — it drops killed agents by design. **The filesystem is the index;
build it from the `.meta.json` files.**

## 2d. Fork works, inherits context — and costs 12x a cold spawn

Enabled with `env.CLAUDE_CODE_FORK_SUBAGENT=1`, a fork spawn **genuinely inherits
the parent conversation**: asked to name the project's finished chapter using only
what it already knew, it answered *"Native Nations (chapter 02), 12,826 words across
three part files"* with **zero tool calls**. The inherit-the-context path is real.

**But measure before using it.** Same session, measured:

| spawn | tokens | work done |
|---|---|---|
| `general-purpose` probe (`wc -l`) | 50,750 | 1 tool call, cold start |
| `general-purpose` probe (`echo`) | 53,681 | 1 tool call, cold start |
| **`fork`, one-line reply** | **621,107** | **0 tool calls**, inherited context |

**A fork costs roughly twelve times a cold spawn and did no work at all**, because it
carries the entire parent conversation. The external hypothesis was that fork would
be *cheaper* than a fresh spawn by sharing the prompt cache; on this build, deep in a
long session, the opposite is true by an order of magnitude. (Caveat: `subagent_tokens`
may count cache reads at full weight, so the billed cost may be lower than the raw
number — but the raw number is what is measurable here.)

**Fork's cost scales with the parent conversation's length.** Early in a session it
may be cheap; late in a long one it is ruinous. It is therefore a deliberate
per-task choice for work that genuinely needs the whole conversation — never a default.

**The flag is currently REVERTED.** `CLAUDE_CODE_FORK_SUBAGENT` may make *all* spawns
forks, and confirming that would cost another spawn; at 621k each the downside is far
worse than the information. Re-enable deliberately, use, then revert.

## 3. Roster behaviour

`ListAgents` shows **completed** agents (tested: a finished probe appeared with
status `completed`) but **killed agents disappear from it** — during the
three-agent kill earlier in this session, only the surviving running agents were
listed. So even if `SendMessage` existed, the agents you would most want back are
the ones the roster drops.

The roster is also short — it does not list every agent the session has ever
spawned. `tools/salvage_agent.py --list` reads the transcript directory directly
and sees **all** of them, including every dead one.

## 4. Cost floor — and the trap I walked into

Two trivial probe agents (one `wc -l`; one `echo`) cost **50,750** and **53,681**
tokens. That is the floor price of a spawn, before any real work.

**That floor is mostly system prompt plus the whole `CLAUDE.md` hierarchy, which
every non-Explore/Plan sub-agent loads.** Which means: writing findings into
`CLAUDE.md` taxes every future spawn. I did exactly that with the first version of
this investigation, then measured it — the project `CLAUDE.md` had reached 971
words, the hierarchy 2,204. **Trimmed to 469 and 1,702**, with detail moved here
and `CLAUDE.md` reduced to pointers.

**Rule: `CLAUDE.md` is a pointer file, not a knowledge base.** Anything an agent
needs only sometimes goes in a `control/` file it can choose to read. Anything one
specific agent must know goes in that agent's prompt, where it costs one paragraph
once instead of a whole document every time.

- Never spawn an agent for what a shell command answers.
- Wide fan-out multiplies the floor: five trivial agents burn a quarter-million
  tokens before doing anything.
- `Explore` and `Plan` skip `CLAUDE.md` and git status entirely — which is why they
  are cheap, and why they are the wrong choice for work that must survive.

## 4b. AUTOMATIC SALVAGE IS NOW LIVE (tested working)

Since resume is impossible here, automatic checkpointing is the entire recovery
story. A `SubagentStop` hook now copies every sub-agent transcript out of
`~/.claude` the moment its agent stops:

- Hook script: `~/.claude/hooks/salvage-subagent.py` (fails silently, always exits
  0 — a hook that errors is worse than one that does nothing)
- Wired in `~/.claude/settings.json` under `hooks.SubagentStop`, matcher `*`
- Archive: `~/.claude/agent-archive/<sessionId>/agent-<agentId>.jsonl`
- Log: `~/.claude/agent-archive/salvage-log.tsv`

**Tested end to end.** Baseline 13 archived; spawned one trivial agent; the log
gained exactly one row — `agent-a97e39466c472ad91.jsonl, 40090 bytes` — timestamped
8 seconds after the marker.

**And it fired without a restart. `settings.json` hooks are live mid-session in
2.1.260** — unlike agent definitions, which are not. That asymmetry is worth
remembering.

**Still unknown: whether `SubagentStop` fires when an agent is KILLED** rather than
completing normally. That is the case that matters most. The hook scans and copies
anything newer regardless of its payload, so it will catch a killed agent's
transcript on the *next* agent's stop even if it does not fire on the kill itself
— but a session whose last act is a mass kill could still lose the final
transcripts from the archive (never from `~/.claude` itself, until the 30-day
sweep). **Check `salvage-log.tsv` after the next kill.**

## 5. Nesting and types

Every agent this session spawned ran at `spawnDepth: 1` — sub-agents did not spawn
their own. Types actually used and confirmed working: `general-purpose`,
`Explore`, `claude-code-guide`. There are no project or user agent definitions on
this machine (`.claude/agents/` is empty in both scopes), so the available types
are the built-in list only.

## 6. What this means for how work is dispatched

The failure mode is specific and now well evidenced: **research is front-loaded,
writing is the payload, and an agent killed before its first write leaves nothing
in the repository.** The two dead `america-world` agents both died saying, in
effect, "now I have the full picture, let me begin" — after spending their entire
budget reading.

Three responses, in order of leverage:

1. **Make agents write early and often.** An agent that writes an outline in its
   first few turns and appends as it goes converts "killed before writing" into
   "killed with partial output on disk". This is the highest-leverage change and
   needs no tooling.
2. **Size the task to fit a window.** `america-world` died twice as a single task
   and landed first try when split in half (eras 1-5, eras 6-10, each to its own
   staging file, assembled by the director).
3. **One agent at a time** (Jon's standing instruction, 2026-09-07). Parallelism
   multiplies the number of payloads a single closing window destroys, and
   multiplies the 50k-token spawn overhead.

**Workflows resume; plain agents do not.** The `Workflow` tool takes
`resumeFromRunId` and replays completed `agent()` calls from cache. That makes
workflows the better vehicle when fan-out is genuinely wanted — but note the cache
replays *completed* agents; a partially-run agent still re-runs.

---

## 6b. Workflows — resume is real, with four edges that bite this project

Not re-tested this session; recorded from external research and from what this
session already observed. Treat as strong hypothesis, not measured fact.

1. **Same-session only.** The journal that makes `resumeFromRunId` work is tracked
   per session. After auto-compaction the journal can end up under the
   pre-compaction session directory, and resume then **silently misses the cache and
   restarts from the beginning with no error**. For a long book project that
   compacts, that is the difference between a cheap resume and paying twice without
   being told.
2. **I invalidated my own cache and did not realise.** Replay matches cached results
   by *positional call index*. I resumed a killed workflow by rewriting the script
   to skip the work that had already landed — which is exactly the edit that shifts
   positions and discards the cache. **The correct move is to leave earlier
   successful `agent()` calls untouched and in order, and let the cache skip them.**
3. **Only calls that finished with a real result get journaled**, so a usage-limit
   kill leaves that call cold and it re-runs. That is the behaviour you want.
4. **Infra failure can be recorded as content — the dangerous one for a book.** A
   documented case: verification agents all died on "You've hit your session limit",
   and the harness recorded those as *failed fact-checks*, placing 19 claims in a
   refuted array as though they had lost on the merits. **An agent killed mid-window
   can land in the output as a finding rather than as a gap.** Any workflow written
   here must distinguish infrastructure failure from result explicitly — a dead
   verifier means UNKNOWN, never REFUTED.

**Uniform fan-out is much cheaper than heterogeneous fan-out.** Agents sharing
model, effort, type, tools, schema and working directory build the same cached
prefix, and later agents are deliberately staggered so they read it rather than
each paying to process it. Four identically-configured chapter agents cost far less
than four differently-configured ones.

## 6c. Passive capture — do this at the NEXT usage-limit hit

Costs nothing, settles an open question that matters. When a limit lands, record:

1. Which agents died, and whether the main thread was idle at the time.
2. Whether any auto-continue line appeared.
3. **What the next `user`-role message in the session transcript actually is.**
   This is the whole question: if it is Jon's own last message replayed, then
   Desktop re-dispatches on reset — and a message that spawned several agents will
   spawn them all again into the fresh window. If it is a fixed continuation string,
   it does not. **One observation settles it.** Read it with:
   `python -c "import json;[print(d.get('type'),str(d.get('message',{}).get('content'))[:200]) for d in map(json.loads,open(r'<session>.jsonl',encoding='utf-8'))][-6:]"`
4. Then check `~/.claude/agent-archive/salvage-log.tsv` to see whether the
   `SubagentStop` hook fired on the kills.

## 6d. THE ECONOMICS — what resuming actually saves (measured)

Jon's goal is money, not tidiness: paying twice for the same thinking on Anthropic's
servers. The honest framing:

**You cannot re-attach a dead agent's prompt cache.** The cache is keyed to a prefix
that dies with the agent. Nothing recovers it. What survives is text on disk, so the
saving comes from *not redoing the work*, not from reusing cache.

Measured on this build:

| path | cost | note |
|---|---|---|
| Re-run a dead research agent cold | **~1,000,000 tok** | 128 tool calls, ~100 web fetches |
| Feed it the full salvage digest | ~90,000 tok | includes raw fetched pages |
| **Feed it the `--brief` payload** | **~12,000 tok** | conclusions + 632 sources, no raw dumps |
| A fork spawn | ~621,000 tok | inherits everything, did no work |
| A cold `general-purpose` spawn | ~50,000 tok | the floor |

**`--brief` is ~87% smaller than the full digest and roughly 1/80th of re-running.**
That is the cost-effective resume, and it is the default the drill now recommends.

**The one true cache-reuse mechanism is `Workflow resumeFromRunId`** — completed
`agent()` calls replay from the journal without re-running, so their cost is not paid
again. That is the only place where "resume cached work" is literally true. It is
worth preferring workflows for any fan-out that might be interrupted — provided
earlier `agent()` calls are left untouched, since the cache matches by position.

**Cheapest of all: don't lose it in the first place.** An agent instructed to write
early leaves its output on disk, and then there is nothing to resume. Two prose agents
killed at the moment of writing kept their files; two research agents killed before
writing kept nothing. That instruction is now in `control/AGENT-BRIEF.md`.

## 6e. Judging whether a dead agent's work stands — MY call, not a script's

**A write is almost never an agent's last act.** Normally it writes, then reports, or
writes again, or validates. So an agent whose final recorded action is a write was
cut off *before its next step*, whatever that was. **A completed write is not a
completed task**, and the tooling must never say otherwise — `--wrote` reports only
that the bytes on disk match the bytes sent.

**The only real signal that an agent believed it was finished is a closing report.**
Everything else is inference from the tail, and inference is a judgement call.

**Theory, UNCONFIRMED but consistent with everything observed:** the runtime appears
to let an in-flight tool call complete rather than severing it — every kill seen so
far shows a *completed* write followed by the error, never a half-written file. That
is encouraging but unproven. Always confirm with `--wrote`; never assume it.

### The procedure

1. `--wrote` — did the bytes land whole? (integrity)
2. `--tail` — what was it doing, and what would it plainly have done next? (intent)
3. **Then decide, reading the events yourself.** Not from a status word.

### What to hand the fresh agent

| situation | send | why |
|---|---|---|
| You can see exactly what is missing | `--brief` (~12k tok) | precise instruction, cheapest |
| **State is ambiguous** — died mid-something, can't tell how far it got | **the FULL digest** (~90k tok) | research, reasoning and raw material. Let the fresh agent work out where it was and finish. Paying 90k to avoid guessing is cheap against ~1M to redo, and far cheaper than a confident wrong guess that corrupts a chapter |

**When in doubt, send everything and let the next agent judge.** It has the full
record; a guess made by the director from a summary does not.

## 7. Not yet tested

- **Hard kill / power loss.** Force-quitting the app mid-agent would end this
  session, so it was not tested. Expected fallback: `claude --resume` from the
  project directory reads transcripts directly and finds sessions the Desktop
  sidebar may not list. **Unverified.**
- **Usage-limit auto-continue.** `autoContinueAtUsageLimit` is unset in
  `~/.claude.json`, and the Desktop checkbox is a separate control that cannot be
  read from here. What the Desktop actually sends on reset — a fixed continuation
  prompt, or a replay of the last user message — is **unknown and matters**: if it
  replays, a message that dispatched several agents would re-dispatch them all
  into the fresh window. Capture the evidence next time a limit hits.
- **Kill-mode asymmetry** (`TaskStop` vs `x` in `/tasks`) could not be
  distinguished, because resume is impossible either way without `SendMessage`.
- ~~Version number.~~ **Settled: 2.1.260**, entrypoint `claude-desktop`, read from
  the `version` field carried on every transcript record. (Older sessions on this
  machine span 2.1.197 through 2.1.260.)
- **Whether `SubagentStop` fires on a KILLED agent**, not just a completed one. See
  §4b — check the salvage log after the next kill.
- **Whether custom agent definitions register at session start.** Files are in place;
  §2b is a one-call test for the next session.
