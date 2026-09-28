# TODO: the live plan and the current step

**Keep this file current.** Update it whenever a task starts or closes, whenever Jon makes a
decision, and before any window closes. The measured truth is `python tools/project_state.py`.
The record of what happened is `control/WORKLOG.md`. The TODO as it stood when the cloud run
stopped is archived at `control/archive/cloud/TODO-at-cloud-stop-2026-09-26.md`.

Last updated: 2026-09-26 (LOCAL, Jon's PC, branch `feature/local-cloud-code-homebrew`)

---

## NOW

NOW-RUNNING: T-267c art (full research eras 8-9; T-267d does era 10)
**ONE AT A TIME.** 32 of 37 chapters pass research (25 researched + 7 written).
Left in step 1:
- **art** eras 6-10 (T-267b; 83 [VERIFY], 19 candidates there: split 6-7 and 8-10).
- **music** eras 6-10 (T-268b; ~105 [VERIFY], 19 candidates; DOLLY PARTON in era 10; split 6-7 and 8-10).
- **storytelling-evolution** (T-269a/b/c, full), **sports-play** (T-271a/b, full), **styles** (T-272a/b, full).
Then STEP 2 (writing).

## Standing rules from 2026-09-26 (details in DECISIONS)

- Eight steps, strictly in order: research, write, audit, research round 2, writing round 2,
  audit, polish, done (#17).
- Opus for research, writing and fixing. Sonnet for checking and salvage reading (#18).
- No GitHub unless Jon asks. One local commit after each sub-agent, with its stats (#19).
- Never shrink the book (#20).
- Writers research their own small gaps (#21).
- The first three sonnet checker runs are repeated with opus to calibrate the checker (#22).
- Work is on branch `feature/local-cloud-code-homebrew`, so Jon can compare this run's
  efficiency with the cloud session's.

## STEP 1: Research everything (ROADMAP step 1)

Brief `control/briefs/RESEARCH.md`, model opus, one agent at a time. Size each task with
`python tools/slice_bank.py <slug> --eras <a-b> --summary` before dispatch.

### 1a. Patch the RESEARCHED* chapters (mode `patch`)
- [x] T-244 `migration` (PASS research, 241k tokens, 11 min)
- [x] T-245 `home-family` (PASS research, 333k tokens, 21 min)
- [x] T-246 `technology` (PASS research, 315k tokens, 16 min)
- [x] T-247 `energy` (PASS research; killed once by an app restart, finished as T-247b, 318k tokens, 18 min)
- [x] T-248 `transportation` (PASS research, 425k tokens, 25 min)
- [x] T-249 `landmarks` (PASS research, 294k tokens, 18 min)
- [x] T-250 `work-workers` (PASS research, 341k tokens, 18 min)
- [x] T-251 `food-farming` (PASS research, 336k tokens, 18 min, parallel)
- [x] T-252 `money` (PASS research, 334k tokens, 22 min, parallel)
- [x] T-253 `marketplace` (PASS research, 426k tokens, 28 min, parallel)
- [x] T-254 `america-world` (PASS research, 339k tokens, 21 min, parallel)
- [x] T-255 `slavery-freedom` (PASS research, 354k tokens, 21 min, parallel)
- [x] T-256 `big-business` (PASS research; a+b, 845k tokens, 46 min)

The kitchen thread spans home-family, technology and energy. Brief T-245 to settle it once and
park the pieces for the other two.

### 1b. `exploration` (mode `full`, PARTIAL)
- [ ] T-257

### 1c. Bank check the chapters that pass research (mode `bankcheck`)
- [ ] T-258 `government-politics`
- [ ] T-259 `war`
- [ ] T-260 `religion` (split by eras)
- [ ] T-261 `education` (split by eras)
- [ ] T-262 `rights-movements` (split by eras)

### 1d. Seeds with parked material (mode `full`, eras 1-5 then 6-10)
- [ ] T-263 `health` · [ ] T-264 `disasters` · [ ] T-265 `crime-justice` · [ ] T-266 `drugs-alcohol`

### 1e. From scratch (mode `full`)
- [ ] T-267 `art` · [ ] T-268 `music` · [ ] T-269 `storytelling-evolution`
- [ ] T-270 `news-communication` · [ ] T-271 `sports-play` · [ ] T-272 `styles` · [ ] T-273 `holidays`

T-numbers are provisional. A task split in two takes suffixes (T-263a, T-263b).

## Later steps

- STEP 2 writing (30 chapters): see ROADMAP.
- STEP 4 (research round 2) already holds **T-243e: economy's 19 blocking gaps**, collected by
  its cloud writers before writers researched their own gaps. List in
  `control/checkpoints/T-243-economy.md`.

## DONE (this session, 2026-09-26, local)

- [x] Branch `feature/local-cloud-code-homebrew` created from `main`.
- [x] Cloud workflow archived in `control/archive/cloud/`, not deleted.
- [x] Briefs rewritten for local work: RESEARCH (bank check merged in), WRITER (2 per chapter,
      does its own gap research), CHECKER, FIXER, GAPS, SALVAGE, with the model policy in
      `control/briefs/README.md`.
- [x] `tools/slice_bank.py` built and tested on all 37 banks.
- [x] RESUME.md trimmed (full old version archived). ROADMAP rebuilt as eight steps.
