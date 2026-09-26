# BANKCHECK brief: the pre-write bank check (runs before a chapter's writers)

The director's dispatch gives you the TASK id, the CHAPTER slug and the CHECKPOINT. You append
to `research/research-<slug>.md` only. You do not touch the outline or the manuscript.

## Why

DECISIONS #13: every fact in the prose must come from the research bank. When the bank lacks
the hard parts of a subject, or never says who did something, the writers can only use a
passive or leave the point out. This check fills the bank first, so the writers write once.

## Read first

`control/AGENT-BRIEF.md` (§3, no invented facts, and the source preferences) ·
`control/hard-subjects-policy.md` (BINDING) · `control/chapter-registry.md` (the chapter's angle
and what belongs to its neighbours) · `outlines/<slug>.md` · `workspace/<slug>.md` · the whole of
`research/research-<slug>.md` · the checkpoint, whose SUBJECT NOTES name candidate hard subjects
and any perishable facts to refresh.

## Find

1. Hard subjects the chapter must cover that the bank does not: violence, deaths, expulsions,
   land taken, people poisoned, exploited or experimented on, and who did it. Decide each
   subject's owner with the registry. Note anything that belongs elsewhere in one line.
2. Events in the bank with no named actor, cause or count.
3. Outline claims the writers will need that the bank lacks, including any "first" or superlative.
4. Perishable facts named in the checkpoint: re-verify them as current to today's date.

## For each gap

Research it, then APPEND it under the right era as `### PATCH <date> (<TASK>): <topic>`, with an
inline source per fact, named actors, and numbers with their ranges and whose count each is.
Where sources disagree, record every figure. Where something is genuinely unknowable, record which
sources you checked. Prefer government, court, museum, university and archive sources.
britannica.com is blocked in the cloud. For 2000-today, date every figure. Do not rewrite
existing bank text. If it is wrong, add a correction note beside it. Keep the scope proportionate:
aim at the gaps a writer would hit, and stop when they are covered.

## Saving

Write each gap into the bank as soon as it is researched, list it in the checkpoint's
"Gaps found and filled (unit 1)", then commit and push the bank and the checkpoint (named paths
only) to `claude/gifted-volta-lfl54k`. Retry a failed push after 2, 4, 8 and 16 seconds. Never
push to main. When done, mark unit 1 `landed` and set NEXT as the dispatch says. Before you
report, run `python tools/project_state.py --check <slug> --stage research`. It must still PASS.

## Report

Under 150 words: gaps filled (one line each), anything placed elsewhere, unsupported "firsts",
perishable facts refreshed, anything genuinely unknowable. Paste the research check output last.
