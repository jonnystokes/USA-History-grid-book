# GAPS brief: close a chapter's collected BLOCKING GAPS (bank patch + prose update)

The director's dispatch gives you the TASK id, the CHAPTER slug and the CHECKPOINT. The chapter
is written and passes its checks. Its writers listed BLOCKING GAPS in the checkpoint. Each is a
place where the research bank names a harm or a central cause but not who did it, what was
done or why, so the prose had to use a passive or leave the point out. Your job is to close them.

## Read first

`control/AGENT-BRIEF.md` §3 (no invented facts, source preferences) · `control/hard-subjects-policy.md`
(BINDING) · `control/general-writing-style-guide.md` (Version 2, BINDING, read in full) ·
`control/writing-style-guide.md` (the book's amendment, BINDING) · the checkpoint's
"BLOCKING GAPS" section, which names the era and the passage for each gap.

## For each gap

1. **Research.** Find what reliable sources say: named people or named bodies, what was done,
   why, the outcome. Prefer government reports, court records, museum, university and archive
   sources. britannica.com is blocked in the cloud. Never guess a name. Where sources genuinely
   do not name anyone, record which sources you checked and what they do say.
2. **Append** to `research/research-<slug>.md` under the right era as
   `### PATCH <date> (<TASK>): <topic>`, with an inline source per fact. Do not rewrite existing
   bank text. If it is wrong, add a correction note beside it.
3. **Update** the matching passage in the right part file. Replace the passive or the missing
   point with what the bank now holds. Change nothing else. Every fact must come from the bank
   (DECISIONS #13). The new sentences meet Version 2 in full: zero em dashes and semicolons,
   people as actors, clinical words defined. Keep every marker line, slug, status and record key
   exactly as it is. A gap is closed by the missing fact, not by a new paragraph of background.
4. **Mark** the gap in the checkpoint as `CLOSED (<TASK>)` or
   `GENUINELY UNKNOWN (sources checked: ...)`.

Non-blocking entries are worth closing too if the sources are quick to find.

## Checks and saving

After each part file changes: `node tools/validate_grid.js <file> --part` and
`python tools/project_state.py --punct <file>` (0/0). Commit and push after each gap or small
group of gaps, with `git add` on named paths only (the bank, the part file, the checkpoint), to
`claude/gifted-volta-lfl54k`. Never push to main. Retry a failed push after 2, 4, 8 and 16 seconds.
Before you report, run `python tools/project_state.py --check <slug> --stage prose` and
`--stage research`. Both must PASS.

## Report

Under 200 words: gaps closed and genuinely unknown (with counts), one line per unknown with the
sources checked, and any correction to existing bank text. Paste both check outputs last.
