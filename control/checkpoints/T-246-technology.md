# CHECKPOINT T-246 | technology | patch + bank check | eras 1-10

STATUS: DONE (director verified: patch PASS, research PASS)
VERIFY: python tools/project_state.py --check technology --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/technology.md · research/research-technology.md · workspace/technology.md

NOW:    finished
NEXT:   Director: close IN-FLIGHT, commit. Park candidates below.

## Measured before dispatch (2026-09-26)

FAIL patch: stories=23 (19 verified, 1 candidate, 3 target), 0 [VERIFY], bank 5,783w against
outline 3,597w (the bank passes the size bar, but it is thin for 23 stories), validator 0 errors.
The 1500s has no story (allowed). Gate blockers:

- line 29  `traditional-technique-practitioner` (target: a present-day practitioner of a traditional technique)
- line 60  `saugus-ironworker` (target, era 3). Lead: `research/research-elements.md` already
  holds sourced PATCHes on the Scottish prisoners of war who worked at Saugus (NPS, Durham
  University). Check whether a named one is documented. Reuse those sources, do not copy the
  elements chapter's angle: technology's angle is the works and the work.
- line 243 `lee-felsenstein` (candidate)
- line 283 `user-worker-changed-by-smartphone-ai` (target, 2000-today)

Each target must become a real, named, documented person whose story the bank sources, or be
handled honestly (never invent a name; an unnamed documented account becomes hb-zoom prose, and
the hb-story block is removed). Keep slugs unique across the book.

**Recent parking:** T-245 (home-family) parked refrigerator figures in this bank under a
"Parked from `home-family`" heading. Use them if they serve this chapter's angle.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | the candidate and the three targets | done | jenks, valliere, felsenstein, ortiz all verified |
| 2 | bank check, eras 1-5 | done | Falling Creek workers/dead/correction; Baltimore Iron Works enslaved labor; gin credit, labor, land; Slater child workers; life dates |
| 3 | bank check, eras 6-10 | done | Jo Anderson/reaper; Ned + 1858 AG ruling; 1913 industrial deaths; Selfridge 1908; Pew 2025/2026; Challenger AI cuts to Aug 2026; Robert Williams face-recognition arrest |
| 4 | final: flags, validator, both checks | done | all ten era-zoom lines rewritten (no em dash/semicolon, facts from bank); two span labels de-dashed; flags all researched; PASS patch + research |

## SUBJECT NOTES (from the director)

Registry angle: the tools and machines that changed how people lived and worked, the applied
invention. Not: the science behind it (`science`), vehicles (`transportation`), fuels
(`energy`), household life (`home-family`).

The bank is small for 23 stories. Check that each verified story's key facts are actually in
the bank. A story marked verified whose facts are not in the bank is a defect the gate may not
catch. Source it or report it.

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the bank): who
did the work at each early works (enslaved and bound labor, prisoners of war) · the cotton gin
and the expansion of slavery (who profited, how many people were enslaved as a result;
`slavery-freedom` leads the system) · factory machines and injuries or deaths to workers,
including children (`work-workers` leads the conditions) · inventions credited to one person
when others, including Black and women inventors, did documented work · weapons technology only
where this chapter's angle needs it (`war` leads) · 2000-today: surveillance, automation and job
loss, with dated figures.

Perishable: every 2000-today figure (smartphone ownership, AI use, jobs affected). Date each
figure and refresh to 2026 where a newer official figure exists.

## Sources in hand

## Gaps researched

## OPEN (should be rare)
- Older span/story notes (2026-08-08 text) still carry em dashes and semicolons as working-note punctuation; writers must not copy them.
- Parked 'kitchen inventions' section of the bank keeps its [VERIFY] tags (not used by outline).
- Andersen v. Stability AI trial date disputed (Sept 2026 vs Apr 2027); re-check before prose.

## Outline claims left out

## Decisions and defects fixed
- Slots renamed: traditional-technique-practitioner -> wayne-valliere; saugus-ironworker -> joseph-jenks; user-worker-changed-by-smartphone-ai -> karla-ortiz (all unique in outlines/).
- Falling Creek 'never shipped its iron' removed: DHR says iron made 1620, county page says furnace unfinished. Dispute recorded.
- 'first' collision: DHR calls Falling Creek first successful integrated ironworks, NPS calls Saugus first sustained integrated. Outline says Falling Creek first begun, Saugus first to run for years.
- Jenks patent date: May 10, 1646 (archive-dated petition, NPS) vs March 6, 1646 (Britannica per search summary).
- Eli Whitney Museum pounds figure (9,000 bales = 45,000 lb) is an arithmetic error; flagged in bank.

## Log
- Unit 4 DONE 2026-09-27. validator 0 errors. PASS --stage patch and --stage research (bank 12,098w vs outline 5,360w; 23 stories all verified).
- Unit 3 DONE. Bank PATCHes era 6 (Richmond Fed; Encyclopedia Virginia 1885 Anderson interview), era 6-7 life dates (Latimer House, NPS Edison), era 7 Ned/Invention of a Slave (Swanson, Columbia L. Rev. 2020), era 8 CDC MMWR 1999 industrial deaths + Selfridge (AFHF), era 10 Pew Mobile Fact Sheet 2025, Pew Americans and AI 2026, Challenger Aug 2026, ACLU/Michigan Public on Robert Williams. Outline: reaper bullets, new span 'who could own an invention', Selfridge line, 1913 deaths line, two new era-10 spans.
- Unit 2 DONE. Bank PATCHes: era 3 Falling Creek (Chesterfield County page; DHR says iron made 1620, conflicts with 'never shipped', outline fixed); era 4 Baltimore Iron Works (Mount Clare Museum: 42 of 89 enslaved at opening, 200+ by 1785, Anthony the blacksmith 1771, 55% returns); era 5 gin (Eli Whitney Museum: Greene credit dispute, picking quotas, gin injuries, Native removal 60,000/8,000), Slater child workers (NPS BLRV), Franklin/Whitney life dates (LOC). Outline: new span 'who worked the iron furnaces' (era 4); gin and Slater lines expanded.
- Unit 1 DONE. traditional-technique-practitioner -> `wayne-valliere` (NEA 2020 Heritage Fellow page). lee-felsenstein -> verified (CHM profile, CHM Community Memory blog, CHM 2016 press release). user-worker target -> `karla-ortiz` (Senate Judiciary written testimony PDF, July 12 2023; NYU JIPEL on Aug 12 2024 ruling). SEARCHED NOT FOUND: Andersen verdict (trial date disputed: Sept 2026 vs Apr 2027).
- Unit 1a DONE: saugus-ironworker target -> `joseph-jenks` (verified). Bank PATCH era 3 (Jenks; workforce, Pawtucket land, Scots, forge hazards). Outline: new span 'who did the work at Saugus' + story. Sources: NPS Robbins report ch.7 (08Chapter7-508x.pdf), NPS Jenks Blacksmith Shop, NPS TwHP lesson 30, NPS People page, SPOWS.
