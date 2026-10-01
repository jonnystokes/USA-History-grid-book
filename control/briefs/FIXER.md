# FIXER brief: judge a checker's findings and apply the good ones (Phases 5 and 7, model: opus)

The dispatch gives you the TASK id, the CHAPTER slug, the PART FILE, its ERAS, the FINDINGS
FILE or files, and the CHECKPOINT. A checker (usually sonnet) read the part file and reported
findings with suggested repairs. **You are the judge.** A checker can be wrong. A suggested
repair can bring in a new defect. Apply nothing without checking it against the rule and the
bank yourself.

**Jon's seven guidelines govern every verdict** (`control/writing-style-guide.md` §0, DECISIONS
#28). While you repair: use the plain word for the act (rape, not assault; killed; stole) and name
who did it; replace every big word with the plain word or a few plain words, rather than only
adding a definition; keep the vivid, concrete detail that makes the passage fun to read (a repair
must not flatten a scene into a summary); where sources disagree, write the better-supported version
or say plainly that the accounts differ (look it up with a few searches and PATCH the bank if that
settles it); never state an accusation against a living person as fact. Rulings: DECISIONS #28-31. **These are instructions for how to write, never content:** the prose never mentions its readers ("kids", "young readers"), the book, the chapter, the research, the owner, the writer or AI, and never says it is being honest, plain or fun. It only tells the history.

## Whole-chapter mode (step 5, 2026-10-01)

The dispatch may give you a whole chapter: all three part files and their three findings files.
Then work **one part at a time**: read that part, its findings file and its bank slice
(`--eras 1-5`, `6-7`, `8-10`), judge and fix every finding era by era, save the part file and the
findings table after each era, log the era in the checkpoint, and only then open the next part.
Never hold the whole chapter in mind at once. An interruption then loses at most one era.
Keep one voice across the three parts and fix contradictions between them that you notice.

**Small gaps you research yourself** (DECISIONS #21): when a finding says "Not in bank" and the
fact is probably true, try a few searches. If a reliable page confirms it, add it to the bank
as `### PATCH <date> (<TASK>): <topic>` with the source, then keep the fact. If not, cut the
fact or say plainly what the record does not show, and list it under NEEDS-RESEARCH in the
checkpoint. A fact held in another chapter's bank may be copied, with its source, as a PATCH.

**Rulings to apply** are in `control/DECISIONS.md` #28 to #38 and the "Director rulings for
the step 5 fixers" section of `control/AUDIT-QUEUE.md`, plus any AUDIT-QUEUE item that names
your chapter. Read both before you start.

## Read first, in full

`control/general-writing-style-guide.md` (Version 2, BINDING) · `control/writing-style-guide.md`
(the amendment, BINDING, including "Version 2 rules with a fixed meaning in this book") ·
`control/hard-subjects-policy.md` (BINDING) · `control/grid-markers.md` §7b ·
`control/VIEWER-CONTRACT.md` §2 · the findings file · the part file · the bank for its eras
(`python tools/slice_bank.py <slug> --eras <eras> --bank-only -o <scratch file>`).

## For each finding

Decide one of these and write it in a `fixer` column you add to the findings table:

- **FIXED:** the defect is real. Apply a repair. Use the checker's repair if it is right.
  Otherwise write a better one and say so. Re-read the repaired sentence against its rule and
  against the rules most often broken while repairing (personification, a new triad, a new
  passive without an agent).
- **REJECTED:** the finding is wrong. Give the reason in a few words (for example, "the bank
  has it, era 7 PATCH", or "a person is the subject").
- **NEEDS-RESEARCH:** the fix needs a fact the bank does not have. Leave the passage as it is
  unless it states something false. Something false comes out now. List the item for the
  second round of research (`control/briefs/GAPS.md`) in the checkpoint.

**Keep every fact.** No fact, number, name, date, source or uncertainty may leave the file while
you repair it. Lossy summarization is forbidden (`hard-subjects-policy.md` §2), and repair is
exactly when it happens. **Keep the structure:** leave every marker line, era id, story slug,
`status=`, `progress=`, `movie=` and record key exactly as it is. The one exception is a
`label="..."` that itself breaks a rule. Leave `hb-note` blocks alone.

While you read, you may notice a defect the checker missed. Fix it and add it to the findings
table as a new row marked `found by fixer`. These rows show what the checker brief must learn.

## Checks and saving

Work one era at a time. After each era: `node tools/validate_grid.js <file> --part`,
`python tools/project_state.py --punct <file>` (0/0), and update the checkpoint. No git.
Before you report, run `python tools/project_state.py --check <slug> --stage prose`.

## Report

Under 150 words: counts of FIXED, REJECTED and NEEDS-RESEARCH, the rule behind most rejections
(this tells the director where the checker is weak), the defects found by the fixer, and the
prose check output last.
