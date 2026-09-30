# Sub-agent briefs: which brief, which model

Rewritten 2026-09-26 for Jon's PC. The cloud versions are archived in `control/archive/cloud/`.
The director's dispatch message names the TASK id, the CHAPTER slug, the ERAS or PART, the
CHECKPOINT and anything specific to the task. Everything else is in the brief, and the dispatch
tells the agent to read it first.

## The model policy (Jon, 2026-09-26, DECISIONS #18)

- **Writing, rewriting, fixing and research:** the smartest model available, and never a
  higher tier than the director's own model. Today that is Opus 5.5, so pass `model: "opus"`.
- **Reading and checking only** (auditing prose against the rules, digesting a dead agent's
  transcript): the latest Sonnet, so pass `model: "sonnet"`. A checker reports every issue with
  a suggested repair. It never edits. An Opus agent makes the corrections later.
- **Scripts still run** (`project_state.py`, `validate_grid.js`, `--punct`). The AI read finds
  what scripts cannot, and the scripts catch what a reader can miss. Neither replaces the other.

Always set `model` explicitly. An omitted model inherits the director's, which is the expensive
default.

| Brief | Used for | Model | Phase |
|---|---|---|---|
| `RESEARCH.md` | Full research, patch, or bank check of one chapter (the bank check is now part of every research task) | opus | 1 and 4 |
| `WRITER.md` | Writing a chapter's prose: one writer for the whole chapter where it fits (single-writer mode), 2+ for large chapters, researching its own small gaps | opus | 2 |
| `CHECKER.md` | Reading one part file against every rule and the bank, and reporting findings with suggested repairs | sonnet (the first 3 runs also opus, to calibrate) | 3 and 6 |
| `FIXER.md` | Judging a checker's findings and applying the good ones | opus | 5 and 7 |
| `GAPS.md` | Second-round research and writing on the gaps that writing and auditing found | opus | 4 and 5 |
| `SALVAGE.md` | Reading a dead agent's transcript digest and writing a continuation brief | sonnet | any |

## Rules that apply to every brief

- **No GitHub, and no git.** Agents do not commit, push, pull or branch. The director makes one
  local commit after each sub-agent finishes, which records that agent's work (DECISIONS #19).
- **Install nothing.** No pip, npm or other installs, and no system changes. If a tool is missing,
  work around it or report it. (Added 2026-09-27 after T-248 pip-installed `pypdf` unasked. Jon
  was told. `pypdf` is now available in the user Python for reading PDFs.)
- **Scratch files go in your own subfolder** of the scratchpad, named after your task (for
  example `scratchpad/T-271b/`). In a burst, agents share one scratchpad, and on 2026-09-28 one
  agent's helper script overwrote another's.
- **One agent at a time** unless Jon calls a burst (DECISIONS #25).
- **Checkpoint after every unit** in `control/checkpoints/T-<nnn>-<slug>.md`. A stranger with
  only the checkpoint and the files must be able to carry on.
- **Write early and often.** An agent killed before its first write leaves nothing.
- **Check file sizes before reading.** Never read `viewer/*.html` whole (line 89 is a 373 KB
  base64 image).
- **Read only your eras when a file is large:** `python tools/slice_bank.py <slug> --eras <a-b>`
  prints your eras of the outline and the bank, including "Parked from" sections and any
  untagged section, so nothing is lost. Add `-o <file>` to save it and `--summary` to see sizes.
- **Never shrink the book** (DECISIONS #20). Savings come from overhead, never from length or
  coverage. Chapters run as long as the material honestly supports.
