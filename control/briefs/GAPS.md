# GAPS brief: second-round research and writing (Phases 4 and 5, model: opus)

The dispatch gives you the TASK id, the CHAPTER slug, the CHECKPOINT and the list of items.
Use this only after the whole book is written and audited. By then the writers have researched
most gaps themselves (WRITER.md). This round takes what is left:

- items a writer marked **OPEN** in its checkpoint,
- audit findings the fixer marked **NEEDS-RESEARCH**,
- outline claims left out that the audit judged the chapter needs.

## Read first

`control/AGENT-BRIEF.md` §3 (no invented facts, source preferences) ·
`control/hard-subjects-policy.md` (BINDING) · `control/general-writing-style-guide.md`
(Version 2, BINDING, read in full) · `control/writing-style-guide.md` (the amendment, BINDING) ·
the checkpoint's list of items, which names the era and passage for each.

## For each item

1. **Check the bank first.** A `SEARCHED, NOT FOUND` entry on the same question means it is
   settled. Search again only if the item gives a new lead.
2. **Research.** Named people or named bodies, what was done, why, the outcome. Prefer
   government reports, court records, museum, university and archive sources. Never guess a
   name. Give it a few good searches, not an open-ended hunt.
3. **Append** to `research/research-<slug>.md` under the right era, as
   `### PATCH <date> (<TASK>): <topic>` with an inline source per fact, or as
   `### SEARCHED, NOT FOUND <date> (<TASK>): <question>` with the sources checked.
4. **Update** the matching passage in the part file from the bank. Change nothing else. The new
   sentences meet Version 2 in full: zero em dashes and semicolons, people as actors, clinical
   words defined. Keep every marker line, slug, status and record key exactly as it is. A gap is
   closed by the missing fact, not by a new paragraph of background. When the fact was not
   found, write it as a history book would ("No surviving record names..."). Never mention
   the book, research, searching or agents in the prose.
5. **Mark** the item in the checkpoint as `CLOSED (<TASK>)` or `SEARCHED, NOT FOUND`.

## Checks and saving

After each part file changes: `node tools/validate_grid.js <file> --part` and
`python tools/project_state.py --punct <file>` (0/0). Update the checkpoint after each item.
No git. Before you report, run `python tools/project_state.py --check <slug> --stage prose` and
`--stage research`. Both must PASS.

## Report

Under 200 words: items closed and not found (with counts), one line per hard-subject item not
found with the sources checked, and any correction to existing bank text. Paste both check
outputs last.
