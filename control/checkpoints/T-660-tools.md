# CHECKPOINT T-660 | tools | build plumbing | opening/closing placement, front and back matter, reading times

STATUS: IN-FLIGHT (agent finished; director sets DONE)
VERIFY: python tools/build_full_book.py and tools/build_full_book_md.py to build/ ; diff build/history-book.md book/history-book.md
BRIEF:  control/briefs/READABILITY-DISPATCH.md section "T-660: tools"
MODEL:  opus
FILES:  tools/build_full_book.py · tools/build_full_book_md.py · (tools/validate_grid.js only if needed)

NOW:    finished, reported
NEXT:   nothing for T-660. Director: decide FRONT_BEFORE_INTRO; card-time WARNs go to the writers

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | read guides and scripts | landed | baseline: unmodified scripts copied to scratch T-660/old, output to T-660/oldout; oldout md == book md byte for byte; HTML build 6 pre-existing story-name warnings, MD 0 |
| 2 | chapter opening / closing placement (HTML + MD) | landed | load_chapter() in build_full_book.py lifts the cards; both builds render them |
| 3 | front matter (_frontmatter/NN-*.md) | landed | load_matters(); ids front-<stem>; listed in contents |
| 4 | back matter (_backmatter/NN-*.md) | landed | ids back-<stem>; after chapter 37; listed in contents |
| 5 | reading times (optional) | landed | contents reads the card; computed time checked, WARN on mismatch |
| 6 | test: builds to build/, book/ untouched, diff | landed | see Log |

## Decisions and defects fixed

- CONFLICT: dispatch item 2 puts front matter BEFORE the introduction; ARCHITECTURE-GUIDE §6 puts the introduction first. Following the dispatch, behind one constant FRONT_BEFORE_INTRO in build_full_book.py so the director can flip it.
- Reading time in the contents comes from the opening card ("about N minutes"), so no diff until writers land. Computed time (words/200 rounded to 5, measure_readability word rule) is checked against the card: a WARN if they differ.

## Log
- 2026-10-26 ~10:15 PM | test on pre-writer manuscript | new MD build == book/history-book.md byte for byte; HTML differs from old-script HTML only in CSS; warnings 6 (same 6 story-name ones) / 0
- 2026-10-26 ~10:20 PM | fixture test (scratch T-660/fixture_test.py, copy of manuscript) | opening under chapter heading, closing after era 10, misplaced card WARN + left in place, front 01-03 + intro + back 01 in order and in contents, bad name and missing heading WARN
- 2026-10-26 ~10:22 PM | live builds after T-661/662/663 cards landed | diff vs book: TOC time lines + writers' prose only; 3 new WARNs, all card-time mismatches (exploration 115 vs 100, government-politics 135 vs 130, holidays 95 vs 90); book/ hashes unchanged
