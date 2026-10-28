# T-777 structure pass: music (Chapter 33)

Brief: control/briefs/STRUCTURE-PASS.md. Fix checkpoint: control/checkpoints/T-733-reviewfix.md.
Review: control/review/R22.md. Status: DONE. Only part3-1900s-and-today.md changed. The bank is unchanged.

T-733 left two findings undone because of the old grid rule, both parts of F20 (review line 24).
Nothing else in T-733 was skipped or done in part for a grid reason (F10's total was skipped on the
reading-time rule, not the grid).

## Findings

- F20a, the 1978 act's own heading (era 9): DONE. Split "Woodstock, music television, compact discs
  and the lyrics hearing" in two. The new last span is "Native ceremonies and a 1978 law". The old label
  still fits the first span, so it stays. Left in place (not moved): it follows the lyrics hearing, the
  other passage about officials and music. The era's spans run by topic, not by year, so moving it
  would gain nothing. Kept T-733's bridge "Many Native songs belong to religious ceremonies" (it says
  why the law is in a music chapter). Cut the lead-in "The 1978 act." because the heading replaces it.
  "That year members of Congress passed" became "In 1978 members of Congress passed": the nearest
  year before it was 1883.
- F20b, the three-topic heading "Native songs, Hawaiian guitar and a new songwriter" (era 8): DONE.
  Split into three spans, one topic each, in the same order: "The Carlisle band and Native songs on
  wax", "The Hawaiian steel guitar", "Irving Berlin, who owned his songs". That is two splits of the
  one span. Each split makes two spans, nothing left the era, and nothing merged or was removed. Not
  moved: Berlin must stay just before Woody Guthrie's story ("An answer to Berlin"), and the bank links
  the steel guitar to no other span. Cut the lead-ins "The steel guitar." and "A new songwriter."
  because the headings replace them. Kept "Songs on wax." (it marks the turn from the band to the
  recordings). "By 1939:" stays where it was, now the end of the Berlin span, before Guthrie's story.

## Card, strips, back matter

- Card lines: none names a changed label. All five quoted names still match a span label exactly
  (checked by script, since the build's card check runs only inside the build).
- Era strips: unchanged and still right. Era 8 has 5,820 words (29.1 minutes, strip 29). Era 9 has
  4,342 (21.7, strip 22). Card total still 135 (27,261 measured words).
- Back matter: no line affected. No back-matter file names span labels.
- FYI, not back matter: outlines/music.md:416 and outlines/BOOK-OUTLINE.md:15516 still carry the old
  era 8 label in their marker lines. They are outlines, so I left them alone.

## Director fact items

None in the dispatch.

## Checks

- `node tools/validate_grid.js manuscript/music/part3-1900s-and-today.md --part`: 0 errors.
- `python tools/project_state.py --punct manuscript/music/part3-1900s-and-today.md`: emdash=0 semicolon=0.
- `python tools/project_state.py --check music --stage prose`: PASS (28,876 words, validator 0 errors).
