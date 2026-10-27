# READER-REVIEW dispatch: one read of the whole book, then one fix pass (2026-10-27)

Jon's instruction: once the chapters are done, Sonnet readers read the whole book and say where it
does not flow, with its readers in mind (8 to 15, many with ADHD). Their findings get ONE
improvement pass, then the book goes to the PDF. No second review, no loop.

## The groups

`python tools/review_extract.py <GROUP>` cuts each group's chapters from a fresh build into
`build/review/<GROUP>.md`. A group starts as soon as all of its chapters have passed the prose gate.

| Group | Reads | | Group | Reads |
|---|---|---|---|---|
| R01 | front matter, introduction, ch 1 | | R14 | ch 24 slavery-freedom |
| R02 | ch 2 native-nations, ch 3 land-environment | | R15 | ch 25 rights-movements |
| R03 | ch 4 immigration, ch 5 migration | | R16 | ch 26 health, ch 27 disasters |
| R04 | ch 6 city-building, ch 7 home-family | | R17 | ch 28 drugs-alcohol |
| R05 | ch 8 technology, ch 9 science | | R18 | ch 29 religion |
| R06 | ch 10 energy, ch 11 transportation | | R19 | ch 30 education |
| R07 | ch 12 landmarks, ch 13 elements | | R20 | ch 31 news-communication |
| R08 | ch 14 work-workers, ch 15 food-farming | | R21 | ch 32 art |
| R09 | ch 16 economy, ch 17 money | | R22 | ch 33 music |
| R10 | ch 18 marketplace, ch 19 big-business | | R23 | ch 34 storytelling-evolution, ch 35 styles |
| R11 | ch 20 government-politics | | R24 | ch 36 sports-play, ch 37 holidays |
| R12 | ch 21 crime-justice | | R25 | back matter (after it is assembled and edited) |
| R13 | ch 22 war, ch 23 america-world | | | |

Readers: model sonnet, brief `control/briefs/READER-REVIEW.md`, output `control/review/<GROUP>.md`.

## The fix pass

One REVIEW-FIX agent per review group (model opus, brief `control/briefs/REVIEW-FIX.md`), task
ids T-710 onward, started as soon as its group's review file lands. One agent per group, not per
chapter, so the guides are read 24 times instead of 37 (Jon, 12:30 PM 2026-10-27: no hurry, be
fuel-efficient, many agents at once is fine). R01's agent also takes the front-matter findings;
R25's findings get one agent. Each part of the book gets one read and one fix, then stops.

## Order of the rest

1. All chapters through the readability edit; all 37 hand-offs in `control/backmatter/`.
2. Reviews and fixes for the chapters (above), as each group is ready.
3. `python tools/build_backmatter.py`, then the BACKMATTER-EDIT agents (model opus).
4. R25 reads the back matter; one fix agent applies its findings.
5. `python tools/build_full_book_md.py` and `python tools/build_full_book.py --pdf`; copy to book/.
