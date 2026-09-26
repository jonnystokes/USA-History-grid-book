# TODO: the live plan and the current step

**Keep this file current.** Update it whenever a task starts or closes, whenever Jon makes a
decision, and before any window closes. Commit and push it with the ledger. It is the
director's to-do list. The measured truth is still `python tools/project_state.py`, and the
record of what happened is still `control/WORKLOG.md`.

Last updated: 2026-09-26 (CLOUD, session 1)

---

## NOW

**Waiting on Jon**: the go-ahead on the plan below and the choice of order.

## DONE this session

- [x] Cloud environment surveyed. Python 3, Node 22, Chromium and web access work.
      britannica.com returns 403.
- [x] `tools/env_check.py` detects CLOUD or LOCAL.
- [x] `control/CLOUD-WORKFLOW.md` holds the cloud rules. CLAUDE.md, RESUME.md and README
      point to it through the environment switch.
- [x] Checkpoint protocol written: `control/checkpoints/`. Every agent commits and pushes
      after every unit.
- [x] T-232 (war eras 1-6) closed as PARTIAL from measurement. Eras 1-4 landed, and eras 5-6
      did not start.
- [x] **Writing Style Guide Version 2 installed** as `control/general-writing-style-guide.md`.
      It is binding in both environments and supersedes v1. CLAUDE.md, the amendment, the
      policy, AGENT-BRIEF, RESUME's briefs and the ROADMAP now cite it by rule heading. The
      prose gate now fails a chapter on any em dash or semicolon.
- [x] Measured result: **both finished chapters now FAIL `--stage prose`.** native-nations
      has 74 em dashes and 40 semicolons. city-building has 83 em dashes and 23 semicolons.
      They were written under v1.

## THE QUEUE (once Jon approves)

The phase order in ROADMAP.md is research everything, then write everything. **Jon to
choose:**

### Option A: the roadmap as written (research first)
1. **T-233 war eras 5-10** (resumes T-232). This needs 1-2 agents: eras 5-7, then 8-10.
2. Batch B: `health`, `disasters`, `crime-justice`, `drugs-alcohol`. These are seeds, with
   about 2 agents each.
3. Batch C: `art`, `music` and `storytelling-evolution`, which have empty banks and 65-128
   `[VERIFY]` tags each, 2-3 agents each. Then `news-communication`, `sports-play`,
   `styles` and `holidays`.
4. Batch D: `exploration` and `big-business` bank cleanup.
5. The 13 `RESEARCHED*` chapters get patched: `--stage patch`.
6. Only then, Phase 2 writing.

### Option B: writing first, for the chapters that are ready (recommended)
0. **v2 revision of the two finished chapters** (`native-nations`, `city-building`), at one
   agent per part file, six in all. This gets them back to PASS. It also tests how agents
   apply v2 before 27 new part files are written under it. The revision is a full v2
   read-and-repair, not a punctuation swap.
1. **T-233 war eras 5-10.** It is half done, so finish it.
2. **Write prose for the 9 chapters that already pass `--stage research`.** These go in
   three part files each (eras 1-5, 6-7, 8-10), like the two finished chapters, at one agent
   per part: `land-environment` · `immigration` · `science` · `elements` · `economy` ·
   `government-politics` · `rights-movements` · `religion` · `education`.
   (The last four are very large. Their parts may need splitting further.)
3. Then return to research as in Option A.

Why B: the $100 of cloud usage may not reach the end of all research. B turns work that is
already paid for into finished chapters first. A finishes the foundation first but may end
with no new prose. Each research agent on this project has used about 300-400k tokens.

## Per-agent routine (cloud)
1. Checkpoint from `_TEMPLATE.md` + IN-FLIGHT ledger entry + TODO update → commit + push.
2. Dispatch one agent: the standard brief + the cloud lines (CLOUD-WORKFLOW §5).
3. On return, run the verify check → close the ledger entry and checkpoint → usage row →
   TODO → commit + push.
4. Next.
