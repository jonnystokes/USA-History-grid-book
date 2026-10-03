# Step 7 fixer: the common instructions (read in full; your dispatch gives TASK, CHAPTER, PARTS, EXTRA)

You are the FIXER (step 7, the final fixes) on the History Book Project at
C:\Users\jon\Projects\History-Book-Project-claude (Windows; use forward-slash paths in the Bash tool, or PowerShell).

- PART FILES: manuscript/<CHAPTER>/part1-before-1800.md, part2-1800s.md, part3-1900s-and-today.md (only the PARTS
  your dispatch names, if it names some).
- FINDINGS FILES: control/audit/<CHAPTER>/partN-findings-r2.md (the second independent audit). The round-1 files
  *-findings-sonnet.md are already resolved: leave them alone.
- CHECKPOINT: control/checkpoints/F7-<CHAPTER>.md (update NOW, the Units table, NEEDS-RESEARCH and the Log as you go).
- You may add PATCH entries to research/research-<CHAPTER>.md. Do not edit the outline or any other chapter's files.
  Scratch files only in your own scratchpad subfolder named after your TASK; downloads only there; never open a PDF
  link in the browser pane.
- If your dispatch says another fixer shares this chapter (a split giant): touch only your own part files and your
  own findings rows; re-read the bank and the checkpoint immediately before every edit to them, and append, never
  rewrite, other agents' sections.

Read your brief, control/briefs/FIXER.md, in full and follow it exactly, including its "Whole-chapter mode" section:
one part at a time, era by era, saving the part file and its findings table after each era; small gaps researched
yourself and banked as PATCHes (or cut if unsourced and unfindable). Read the three binding style files in full first,
including control/writing-style-guide.md section 0 (Jon's seven guidelines: the whole truth in plain words, no big
words anywhere, fun to read, never breaking the fourth wall), and control/DECISIONS.md #28-46, plus the AUDIT-QUEUE
items naming your chapter and its "Step 7 sweeps" line.

Book-wide sweeps, whether or not a finding names them: remove every "In plain words" (it announces the book's
manner); never print a slur (#35, #39); period terms like "Negro" stay only inside quotes and names, explained once
in plain words (#40); "died" alone is softening where people were killed (#44); no unnamed "historians" or "sources
say" (#32, #37); "No surviving record names..." only where the bank shows a real search, otherwise name the silent
document (#45).

Judge every finding (FIXED / REJECTED with reason / NEEDS-RESEARCH). A checker can be wrong; a repair can bring in a
new defect. Fix defects the checker missed and add them as rows marked `found by fixer`. Keep every fact. Never
shrink the book to make it tidier. Keep every marker line, era id, story slug, status=, progress=, movie= and record
key exactly. A fact tagged "(unconfirmed: search summary only)" is not a fact until you confirm it on a real page.

After each era: `node tools/validate_grid.js <file> --part` (0 errors) and `python tools/project_state.py --punct
<file>` (0/0). No git. Install nothing. Write with the Write or Edit tool, never a Bash heredoc. Check file sizes
before reading.

Before you report, run `python tools/project_state.py --check <CHAPTER> --stage prose` (must PASS). Report in under
120 words: per part, FIXED / REJECTED / NEEDS-RESEARCH and found-by-fixer counts; the EXTRA item's result; anything
the director must decide; and the prose check output last.
