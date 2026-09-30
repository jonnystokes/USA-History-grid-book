# CHECKER dispatch: the director's prompt and cycle (step 3 audit)

The checker's rules are in `CHECKER.md`. This is the director's side, so a fresh session can run the
next file without reconstructing anything. Calibration (T-331 to T-333) is recorded in
`control/audit/CHECKER-CALIBRATION.md`; its verdict: sonnet alone, one read per file now, step 6 is
the second read.

## The cycle, one part file

```bash
python tools/audit_status.py                       # progress and the next file
python tools/audit_status.py --mk <slug>           # once per chapter: control/checkpoints/A3-<slug>.md
STAGE=prose MODEL=sonnet python tools/director_task.py open T-3nn <slug> A3 "CHECKER sonnet, <partN>"
# launch the Agent (general-purpose, model sonnet, background) with the prompt below
# append to WORKLOG: AGENT: <id> (salvage: python tools/salvage_agent.py <id> --tail)
# on completion:
STAGE=prose MODEL=sonnet python tools/director_task.py close T-3nn <slug> A3 <tokens> <tools> <ms> "<counts>" control/audit/<slug>
```

The checker changes no chapter file, so the prose check always passes; the deliverable is the findings
file. `audit_status.py` counts a findings file as FINISHED when the validator output is pasted at its
end. A PARTIAL file (interrupted checker) is finished by re-dispatching the same prompt: the brief
has the checker append era by era, and the prompt tells it to continue from the last era written.

## The prompt (fill the angle-brackets)

```
You are a CHECKER on the History Book Project at C:\Users\jon\Projects\History-Book-Project-claude (Windows; use forward-slash paths in the Bash tool, or PowerShell).

TASK: T-3nn | CHAPTER: <slug> | PART FILE: manuscript/<slug>/<part>.md | ERAS: <a-b>
FINDINGS FILE: control/audit/<slug>/<partN>-findings-sonnet.md
MODEL: sonnet.

Read your brief, control/briefs/CHECKER.md, in full and follow it exactly: the files to read first, in order and in full; starting the findings file before your first pass; the six passes over each era, every sentence in every pass; writing each era's findings as you finish it; and the finish and report. Get your bank slice with `python tools/slice_bank.py <slug> --eras <a-b> --bank-only -o <scratch file>` (keep scratch files in your own subfolder of the scratchpad, named T-3nn).

If the findings file already exists (an earlier checker was interrupted), do not start over: read it, keep every row, and continue from the first era that has no findings written.

You are a reader, not an editor. Change no file except your findings file. No git. Install nothing. Write the findings file with the Write or Edit tool, never a Bash heredoc. Check file sizes before reading; never read viewer/*.html whole (use the VIEWER-CONTRACT.md sections the brief names instead).

Report in under 150 words as the brief says.
```

## Measured (calibration runs)

About 220k-270k tokens and 8-10 minutes per part file; 90-160 findings per file, 6-12% of them false after
the brief changes. The fixer (step 5) judges them all.
