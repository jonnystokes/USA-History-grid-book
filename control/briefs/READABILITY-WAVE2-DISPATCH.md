# READABILITY dispatch, wave 2: the other 34 chapters (2026-10-27, DECISIONS #53)

Jon's instruction: as many agents at once as the harness allows (about 20), every agent on Opus
(Jon, 7:21 AM 2026-10-27: Fable is out for the week). All 34 tasks start fresh.

## Rules for every task

- Brief: `control/briefs/READABILITY.md`, including the two pilot fixes and the back-matter
  hand-off added 2026-10-27. Read its "Read first" list in full, in order, before touching prose.
- Edit only your chapter's `manuscript/<slug>/part*.md`, its bank for a PATCH, your checkpoint
  `control/checkpoints/<TASK>-readability.md`, and your hand-off `control/backmatter/<slug>.md`.
  No git. No installs. No sub-agents. Scratch in your own scratchpad subfolder.
- Checkpoint first; resume from it if it exists. Checks as the brief says. `--check <slug>
  --stage prose` must PASS before you report.
- Pilot results to match: exploration went from 84 paragraphs over 90 words to 6 and from 29% of
  paragraphs opening with a date to under 1%, without losing a fact. Read
  `control/REPORT-PILOT-2026-10-26.md` "What I read, and what I think" for what worked.
- **Your own context window.** A big chapter (rights-movements is 55,000 words) can fill it. Work
  era by era, never hold the whole chapter in your head, save after every era, and if you sense
  your context is getting heavy (you have read far more than you meant to, or the conversation is
  very long), finish the era in hand, update the checkpoint, and report that you stopped and where.
  The director resumes the task from the checkpoint. Do not run out mid-era.
- Report as the brief says, under 300 words, no prose pasted.

## Task list

First three:

| Task | Chapter | Words |
|---|---|---|
| T-670 | migration | 13,984 |
| T-671 | crime-justice | 26,201 |
| T-672 | sports-play | 23,535 |

Fresh writers, wave 2a (launched together, biggest first):

| Task | Chapter | Words |
|---|---|---|
| T-673 | rights-movements | 54,849 |
| T-674 | education | 44,320 |
| T-675 | religion | 39,038 |
| T-676 | art | 28,296 |
| T-677 | music | 25,427 |
| T-678 | war | 23,979 |
| T-679 | disasters | 23,746 |
| T-680 | news-communication | 23,187 |
| T-681 | storytelling-evolution | 23,109 |
| T-682 | health | 20,820 |
| T-683 | drugs-alcohol | 20,402 |
| T-684 | slavery-freedom | 20,268 |
| T-685 | native-nations | 19,446 |
| T-686 | styles | 18,601 |
| T-687 | immigration | 18,326 |
| T-688 | land-environment | 17,891 |
| T-689 | science | 17,866 |

Fresh writers, wave 2b (launched as 2a agents finish):

| Task | Chapter | Words |
|---|---|---|
| T-690 | city-building | 17,673 |
| T-691 | big-business | 17,419 |
| T-692 | america-world | 17,276 |
| T-693 | elements | 16,254 |
| T-694 | work-workers | 15,995 |
| T-695 | technology | 15,577 |
| T-696 | economy | 14,981 |
| T-697 | marketplace | 14,423 |
| T-698 | energy | 14,287 |
| T-699 | food-farming | 14,166 |
| T-700 | money | 14,046 |
| T-701 | landmarks | 13,615 |
| T-702 | transportation | 13,357 |
| T-703 | home-family | 11,636 |

Known trouble spots, from the measurements (`python tools/measure_readability.py <slug>` gives the
rest): rights-movements has a 12,863-word era (1900 to 1950) that needs five or six "By" lines and
a 683-word median story box; education's longest era is 10,062 words and its average paragraph 87;
religion has 24 "you" already in its prose (check each: the narrator belongs in furniture, not the
body); art has 33 stories, 8 over 400; music, news-communication and sports-play run 8 to 9
attributions per thousand words; drugs-alcohol and land-environment open a third of their
paragraphs with a date; chapter 4, immigration, repeats chapter 2's opening paragraph and retells
Leif Erikson (cut to a callback, ARCHITECTURE-GUIDE §5.12).

The pilot writers also set each chapter's reading time from `measure_readability.py` (words / 200,
rounded to 5); the build warns on a mismatch.
