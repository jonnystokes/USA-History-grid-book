# CHECKPOINT T-658 | viewer | fix | viewer/viewer.html polish (em dashes, nicknames)

STATUS: IN-FLIGHT (agent finished, director to set DONE)
VERIFY: node tools/validate_grid.js outlines/BOOK-OUTLINE.md ; static <script> tag count ; line 89 length = 373508
BRIEF:  control/briefs/GAPS-FINAL-DISPATCH.md (section T-658)
MODEL:  opus
FILES:  viewer/viewer.html only

NOW:    finished, all three units landed
NEXT:   nothing; director reviews and commits

Line 89 length before: 373508

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | em dashes rendered by the viewer | landed | 14 sites: lines 6,756,790,840,855,1592,1603,1725(record lines, now colon),1759(Next, now colon),2329,2369,2389,2404,2621. Left: CSS/JS comments 173,204,217,233,289,1432 and demo hb-note test data 892-1283 |
| 2 | story headings drop nicknames from name= | landed | mdBlock keeps first ### heading as head; story fold + story-name show head || b.name. Six stories now show the nickname |
| 3 | verify (validator, script tags, line 89) | landed | line 89 = 373508 before and after; 2 <script>/2 </script>; inline engine script parses (new Function); BOOK-OUTLINE validator 0 errors, 684 stories |

## Decisions and defects fixed

- Cause of the nickname drop: attributes cannot hold double quotes, so name= omits or single-quotes the nickname; the ### heading holds it, but mdBlock threw headings away. All 684 story headings equal name= except those six, so preferring the heading is safe (tools/build_full_book.py already does the same).
- Empty placeholders (tEra, searchCount, fQuota) now show a middle dot instead of an em dash.

## Log
- 2026-10-26 | units 1-3 | viewer.html edited, verified | validator 0 errors | line 89 unchanged
