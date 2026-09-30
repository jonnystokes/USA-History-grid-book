# WRITER dispatch: the director's prompt and cycle (step 2)

The director's side of a writing task. The writer's rules are in `WRITER.md`; this file is the
prompt that points a writer at them, so a fresh director session can dispatch the next chapter
without reconstructing it. Used for T-315 to T-322 (2026-09-29/30).

## The cycle, one chapter

```bash
python tools/mk_writer_checkpoint.py T-3nn:<slug>:single      # omit :single for writer A / B
STAGE=prose python tools/director_task.py open T-3nn <slug> T-3nn "ONE writer, all 10 eras"
# launch the Agent (general-purpose, model opus, background) with the prompt below
# append to WORKLOG: AGENT: <id> (salvage: python tools/salvage_agent.py <id> --tail)
# on completion (tokens, tool uses, ms come from the notification):
STAGE=prose python tools/director_task.py close T-3nn <slug> T-3nn <tokens> <tools> <ms> "<one line>" manuscript/<slug>
# check the checkpoint's TO PARK section (file_parks.py if non-empty), queue audit items,
# update TODO + ROADMAP counts, commit, next chapter.
```

## Sizing (measured 2026-09-30)

| Slice (outline + bank words) | Mode | Evidence |
|---|---|---|
| up to ~60k | ONE writer, bank read in three slices (1-5, 6-7, 8-10) | war 54k: 448k tokens, 19 min, 20.1k tokens per 1,000 words |
| above ~60k (the giants) | split along era lines, still the same three files | two writers cost ~25% more per word (disasters) |

## The prompt (fill the angle-brackets)

```
You are a WRITER on the History Book Project at C:\Users\jon\Projects\History-Book-Project-claude (Windows; use forward-slash paths in the Bash tool, or PowerShell).

TASK: T-3nn | CHAPTER: <slug> | MODE: SINGLE-WRITER (you write the whole chapter, all ten eras)
PART FILES, in order: manuscript/<slug>/part1-before-1800.md (eras 1-5), manuscript/<slug>/part2-1800s.md (eras 6-7), manuscript/<slug>/part3-1900s-and-today.md (eras 8-10)
CHECKPOINT: control/checkpoints/T-3nn-<slug>.md (all 11 units are yours)

You are the only agent running. You may add PATCH and SEARCHED, NOT FOUND entries to research/research-<slug>.md. Do not edit the outline or any other chapter's files. Keep scratch files in your own subfolder of the scratchpad, named T-3nn.

Registry angle: <from control/chapter-registry.md: what it covers, and what belongs to other chapters>. <Any DECISIONS ruling or parked material that applies. Hard-subjects note where relevant.>

This chapter's research is large (about <N> words of outline and bank). Budget your reading: read the bank one part at a time, as below, and do not re-read the whole slice for each era.

First read your brief, control/briefs/WRITER.md, in full, and follow it exactly, including its "Single-writer mode" paragraph: the three binding style files to read in full before writing a word, the file layout, facts from the bank only, researching your own small gaps (PATCH into the bank first, then write; after a few searches, record SEARCHED, NOT FOUND and write the passage honestly from what is known), never breaking the fourth wall, the checks and the report. Read eras 1-5 with `python tools/slice_bank.py <slug> --eras 1-5 -o <scratch file>`, eras 6-7 with `--eras 6-7` when you reach part 2, and eras 8-10 with `--eras 8-10` when you reach part 3. Use manuscript/science/part1-before-1800.md as the model of layout. Keep one voice across all three files, let later eras build on what earlier eras explained, and never repeat an explanation. Thin eras are correct: never pad. For 2000-today, give the year of every figure and name its source in plain words.

Write one era at a time, and save the file after each era. Before each era set NOW in the checkpoint; after EACH era (not in batches) log its words, validator and --punct in the checkpoint. If this session is cut off, the next writer resumes from that log. Run the self-review from the style guide on each file when you finish it.

If web search or fetch fails with a limit error, do not stop: write the honest shorter version from the bank, list the question in the checkpoint under OPEN, and note it in your report.

If you find a checkpoint that already shows finished units (a previous writer was interrupted), do not redo them: read the landed files, check the last unit is complete, and continue from NEXT.

No git. Install nothing (pypdf is available). Write text with the Write or Edit tool, never a Bash heredoc. Check file sizes before reading; never read viewer/*.html whole.

Before you report, run `node tools/validate_grid.js <file> --part` on all three files (0 errors each), `python tools/project_state.py --punct <file>` on all three (zero em dashes and semicolons), and `python tools/project_state.py --check <slug> --stage prose` (must PASS). Paste those outputs as your last lines. Report in under 200 words as the brief says.
```

## After an interruption

Run `python tools/resume_drill.py`, then for the IN-FLIGHT entry run its VERIFY line. If it fails, read
the checkpoint's units table and log: the landed eras stand. Dispatch a continuation writer with the
SAME prompt, the same checkpoint, and the task id plus a suffix (T-3nn-r). The prompt's "If you find a
checkpoint that already shows finished units" paragraph makes it resume from NEXT. Before that, check
the last logged era is complete in the file (its closing markers validate and its word count matches
the log); a half-written era past the log is rewritten by the continuation writer, not kept.
