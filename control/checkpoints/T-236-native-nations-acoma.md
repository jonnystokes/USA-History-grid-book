# CHECKPOINT T-236 | native-nations | prose fix | Acoma account (DECISIONS #14)

STATUS: LANDED
VERIFY: python tools/project_state.py --check native-nations --stage prose (must still PASS)
FILES:  manuscript/native-nations/part1-before-1800.md (the Acoma passage, era 1500s)
SOURCE: research/research-native-nations.md line ~352: the All Pueblo Council of Governors,
        press release, Oct. 6, 2023: the soldiers "had demanded food and supplies, assaulted an
        Acoma woman, and forced allegiance to the Spanish crown."
RULING: Jon, 2026-09-26: it goes in, attributed to the Council.

NOW:    done. Prose check PASS.
NEXT:   none.

## Units

| # | unit | state | landed (commit / note) |
|---|------|-------|------------------------|
| 1 | Acoma account added to part 1 | landed | this commit; validator 0 errors, punct 0/0, prose PASS |

## Log
- 2026-09-26: unit 1 landed. Added after "...with a party of soldiers and demanded food.":
  "The All Pueblo Council of Governors, a council of the leaders of the Pueblo nations, said in October 2023 that the soldiers "had demanded food and supplies, assaulted an Acoma woman, and forced allegiance to the Spanish crown." Assaulted means the soldiers attacked her. The Council's statement does not give more detail. Forcing allegiance to the Spanish crown means the soldiers made the Acoma promise loyalty to the king of Spain."
  Smoothing: "The Acoma killed him" became "Then the Acoma killed Zaldivar". The Council's definition moved to its new first mention, so the death-toll paragraph now reads "The All Pueblo Council of Governors uses the figure...".
