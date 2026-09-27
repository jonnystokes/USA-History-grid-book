# SALVAGE brief: turn a dead agent's transcript into a continuation brief (model: sonnet)

An agent was killed mid-task, usually by the usage limit. Its transcript survives on disk. The
director has already run `python tools/salvage_agent.py <agentId> -o <digest file>` and names
the DIGEST, the TASK's CHECKPOINT and the task's FILES in the dispatch. Your job is reading, not
writing the book. **Change no file except the checkpoint's SALVAGE section.**

## Do this

1. Read the digest, the checkpoint and the original brief the dead agent had
   (`control/briefs/<BRIEF>.md`).
2. **Measure what landed.** Do not trust the transcript's claims. For each file the agent
   touched, check what is actually on disk: which eras exist, their `progress=` flags, and
   the last era's state. Use `grep -n "hb-time:start" <file>` and read the last era.
   **A file that validates is not a finished file:** an era can parse and still be half-written
   (T-242c). Compare the last era against the outline's plan for it.
   Run the task's VERIFY command from the checkpoint and record its output.
3. **Find what the agent knew that is not on disk yet:** sources fetched and what each settled
   (URL plus the fact), facts found but not written, decisions made, and the unit it was on.

## Write this into the checkpoint, under `## SALVAGE <date> (<dead agentId>)`

- **Landed:** unit by unit, measured, not claimed.
- **Stopped at:** the unit and, as closely as the transcript shows, the point inside it.
- **Half-written:** anything on disk that parses but is incomplete, and what is missing.
- **Sources in hand:** URL and what it settled, so the next agent re-reads instead of
  re-searching.
- **Do not redo:** units that landed.
- **NEXT:** the first thing the continuation agent should do.

Keep it under 500 words. Report in under 100 words, with the VERIFY output as your last line.
