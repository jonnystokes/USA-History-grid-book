# CHECKPOINT T-253 | marketplace | patch + bank check | eras 1-10

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check marketplace --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/marketplace.md · research/research-marketplace.md · workspace/marketplace.md

NOW:    (agent sets this)
NEXT:   Unit 1.

## PARALLEL RUN (Jon, 2026-09-27): five agents at once

This agent runs at the same time as four others (T-251 to T-255, one chapter each). **Write only
your own chapter's three files and this checkpoint.** Do NOT edit any other chapter's outline,
research bank or workspace, even to park material there: another agent may be writing to it at
the same moment. Instead, list anything that belongs to another chapter under "TO PARK" below
(target chapter, era, the sourced text to add). The director files it after all five finish.
Reading other chapters' banks is fine.

## Measured before dispatch (2026-09-27)

FAIL patch: stories=17 (14 verified, 0 candidate, 3 target), bank 7,596w vs outline 8,373w (the bank is SMALLER than the outline, so the gate fails on size too: grow the bank past the outline), 0 [VERIFY], validator 0 errors. Gate blockers:

- line 65 `documented-1600s-store-customer` (target): a customer named in a 1600s account book.
- line 253 `ration-book-shopper` (target, 1900-1950): a documented shopper under rationing. `food-farming` (T-251) has a ration-book household target at the same time: pick a different person, and tell it from the shopping angle.
- line 350 `delivery-worker-marketplace` (target, 2000-today): a documented last-mile delivery driver. Avoid Raef Lawson (`work-workers`) and Barbara Ann Berwick (`transportation`).

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | the open story slots | todo | |
| 2 | check that each verified story's key facts are in the bank; source any that are not | todo | |
| 3 | bank check, eras 1-5 | todo | |
| 4 | bank check, eras 6-10 | todo | |
| 5 | final: flags, validator, both checks | todo | |

## SUBJECT NOTES (from the director)

Registry angle: buying and selling in daily life: stores, mail-order, malls, online shopping, advertising, credit, consumer culture. Not: money as a system (`money`), the macro economy (`economy`). This chapter has the largest outline of the patch group and a bank smaller than it: check that every verified story and every outline claim is in the bank. Hard subjects (prompts; check the bank): the slave trade as a market (auctions, advertisements for people, who sold) · stores that refused Black customers and the sit-ins (`rights-movements` leads the movement) · company stores and scrip · false advertising and patent medicines that harmed people · predatory credit · 2000-today: warehouse and delivery injuries, dated.

Each open slot must become a real, named, documented person whose story the bank sources, or be
handled honestly (never invent a name; an unnamed documented account becomes hb-zoom prose, and
the hb-story block is removed). Before choosing a person, search `outlines/` and `manuscript/`
so no other chapter already tells them (ignore `outlines/BOOK-OUTLINE.md`, a compiled copy).
Keep slugs unique across the book.

Perishable: every 2000-today figure. Date each and refresh to 2026 where a newer official figure
exists.

## TO PARK (for the director to file after the parallel run)

## Sources in hand

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

## Log
