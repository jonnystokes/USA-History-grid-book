# CHECKPOINT T-256 | big-business | patch (bank write-up) + bank check | T-256a eras 1-7, T-256b eras 8-10

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check big-business --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/big-business.md · research/research-big-business.md · workspace/big-business.md

NOW:    (agent sets this)
NEXT:   T-256a: Unit 1.

## Measured before dispatch (2026-09-27)

FAIL patch: stories=14 (13 verified, 1 candidate, 0 target), 1 [VERIFY] tag, **bank 409w against
outline 6,759w**, validator 0 errors. DECISIONS #11: the outline's `hb-note` claims a full bank
exists, but it was never written. **The sources are inline in the outline, so the main job is a
write-up: every fact the outline states goes into the bank under its era, with its source, checked
against that source.** A fact whose source does not support it is corrected in the bank (with a
note) and in the outline.

Gate items:
- 13 stories marked `verified` with no bank behind them. Each needs its key facts in the bank.
- line 146 `franklin-tarbell` (candidate, era 7): Ida Tarbell's father, an independent oil
  producer ruined in the South Improvement fight.
- line 149: one `[VERIFY]` tag (in the Tarbell story).
- the bank must end larger than the outline.

Outline size by era: 1-5 about 2,060w, 6 about 630w, 7 about 1,510w, 8 about 1,220w,
9 about 1,150w, 10 about 1,070w. Hence the split.

## Units

| # | unit | agent | state | landed (note) |
|---|------|-------|-------|---------------|
| 1 | bank write-up + verify stories, eras 1-5 | T-256a | todo | |
| 2 | bank write-up + verify stories, eras 6-7, including Franklin Tarbell and the [VERIFY] | T-256a | todo | |
| 3 | bank check, eras 1-7 (hard subjects, actors, land) | T-256a | todo | |
| 4 | bank write-up + verify stories, eras 8-10 | T-256b | todo | |
| 5 | bank check, eras 8-10, perishables | T-256b | todo | |
| 6 | final: flags, bank >= outline, validator, both checks | T-256b | todo | |

## SUBJECT NOTES (from the director)

Registry angle: the scale of business and its clashes with government and the public: trusts,
regulation, lobbying, corporate power. Not: the daily job (`work-workers`), the whole economy
(`economy`). DECISIONS #12: film does not live here.

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the outline
and the neighbouring banks, especially `economy`, `work-workers`, `money`, `energy`,
`transportation`): chartered companies and enslaved labor (the Royal African Company, the Virginia
Company) · railroad land grants and whose land · Standard Oil's methods (rebates, the South
Improvement Company) · private armies against strikers (the Pinkertons at Homestead, company
guards at Ludlow) with the dead · companies that knew their product harmed people (asbestos,
leaded gasoline, tobacco) and who knew, when · the 2008 crisis and who ran the firms · 2000-today:
antitrust cases against the largest tech firms, dated.

Perishable: every 2000-today figure. Date each and refresh to 2026.

## Sources in hand

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

## Log
