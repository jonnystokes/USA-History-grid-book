# Polish task 1 (step 7): book-wide cleanups after the fixers (Opus)

You are the POLISHER on the History Book Project at C:\Users\jon\Projects\History-Book-Project-claude.
Nothing else is running; you may edit any chapter's part files and research banks, but only the sentences an item
touches. Read the three binding style files (control/general-writing-style-guide.md, control/writing-style-guide.md
incl. section 0, control/hard-subjects-policy.md) and control/DECISIONS.md #28-46 before you change a sentence.
Checkpoint: control/checkpoints/POLISH-1.md (create it; log each item as you finish it, so an interrupted run resumes).

ITEMS
1. Wikipedia named in the prose (grep -rn "Wikipedia" manuscript/): replace each with the underlying source it cites
   (open the cited page; bank it as a PATCH), or cut the fact if none can be found. Files today: crime-justice part2,
   immigration part3, sports-play part2 and part3, storytelling-evolution part2 and part3, styles part3.
2. "In plain words" (grep -rli "in plain words" manuscript/): remove the remaining one.
3. The control/AUDIT-QUEUE.md items whose text says "polish" or "Step 7 polish", for example: the Sally death counts in
   drugs-alcohol and economy (restore every count; say the report's stages add to 107 while it gives 109); the DC
   emancipation count (name both 2,989 and about 3,100 with their sources); the Spiro/Craig Mound names in art
   (confirm in a stronger source or keep credited); Attica and Wounded Knee "who did it" lines in crime-justice (official
   reports); land-environment thin sources; slavery-freedom (Kendi check; one plain sentence each on the 1964 and 1965
   laws); the native-nations Baird story movie= accent marks (correct only the accents, verify the film title).
   Work them in that order; skip any item a fixer already closed (check the prose first).

RULES: facts from the bank only (PATCH new sources first); never shrink the book; keep every marker line, era id,
story slug, status=, progress=, movie= (except the accent fix) and record key; no em dashes, no semicolons; no fourth
wall. After each file you edit: `node tools/validate_grid.js <file> --part` (0 errors) and `python tools/project_state.py
--punct <file>` (0/0). No git. Install nothing. Downloads only in your scratch subfolder (POLISH-1); never open a PDF
link in the browser pane. Write with Write or Edit, never a Bash heredoc.

Before you report, run `python tools/project_state.py --check <slug> --stage prose` for every chapter you edited (all
must PASS). Report in under 100 words: items done, items not done and why, and the check outputs (one line each).
