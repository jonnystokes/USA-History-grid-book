# ARCHIVED: the cloud workflow (Anthropic's servers), paused 2026-09-26

**Nothing in this folder is in force.** The project ran in Claude Code on the web from
2026-09-26 until the $100 cloud credit ran out the same day. Work then moved back to Jon's PC,
and on Jon's instruction these files were archived rather than deleted, so they can be restored
if the project ever runs online again.

## What is here

| File | What it was |
|---|---|
| `CLOUD-WORKFLOW.md` | The cloud rules: container paths, commit and push after every unit, branch `claude/gifted-volta-lfl54k`, checkpoints as the salvage |
| `briefs/WRITER.md`, `briefs/BANKCHECK.md`, `briefs/GAPS.md` | The three briefs as they stood, with their cloud commit-and-push sections |
| `checkpoints/_TEMPLATE.md` | The checkpoint template with the push instructions |
| `TODO-at-cloud-stop-2026-09-26.md` | The TODO as it stood at the clean stop |

## How to restore it if work goes online again

1. **Ask Jon first.** He decides whether the project runs online, and on which branch. The
   branch named in these files was merged and should not be reused without his say.
2. Copy `CLOUD-WORKFLOW.md` back to `control/`. `tools/env_check.py` already detects the cloud
   (`CLAUDE_CODE_REMOTE=true`) and points here.
3. **Do not copy the old briefs back over the live ones.** The live briefs in `control/briefs/`
   were rewritten on 2026-09-26 with rules the cloud versions lack: the research agent does the
   bank check, writers research their own gaps, two writer agents per chapter,
   `tools/slice_bank.py`, and the model policy. Instead, add the cloud saving section to each
   live brief. The text to add is `CLOUD-WORKFLOW.md` §5, plus "commit and push after every
   unit" from §3.
4. Update the branch name everywhere to the one Jon names.

## What the cloud run taught, still true locally

- The checkpoint file (one per task, updated after every unit) is what makes an interrupted task
  resumable by a stranger. It stays in the local workflow.
- A file that validates is not a finished file. A killed agent can leave an era that parses and is
  half-written (T-242c). The continuation agent checks the last era against the outline's plan.
