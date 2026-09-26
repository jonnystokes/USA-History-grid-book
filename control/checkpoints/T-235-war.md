# CHECKPOINT T-235 | war | research | eras 5-10 (resumes T-232, which landed eras 1-4)

<!-- The director fills the header and the unit list before dispatch. The agent keeps
     everything else current, and commits and pushes after every unit. Write it for a
     stranger who has only this file and the repo. -->

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check war --stage research
BRIEF:  standard research brief (control/RESUME.md) + cloud lines (control/CLOUD-WORKFLOW.md §5).
        The LAST agent also gets the progress-flag line.
FILES:  outlines/war.md · research/research-war.md · workspace/war.md
PLAN:   T-235a = eras 5-7 (about 6 stories), T-235b = eras 8-10 (about 6 stories).
STATE AT START (2026-09-26): eras 1-4 progress="researched"; eras 5-10 progress="seed".
        Chapter: 14 stories (v2 c2 t10), 1 [VERIFY], bank 7,006w vs outline 4,293w.
        Eras 1-3 have no hb-story, because no named individual is documented. That is correct
        under the naming rule and is not a defect.
RULINGS THAT BIND THIS CHAPTER: hard-subjects-policy.md §6, war row: "Go to individual scale:
        the single soldier's wound and death, not only unit-and-number."

NOW:    T-235a working unit 2 (era 1800-1850). Plan: War of 1812, Seminole wars (military side), Mexican War; story John Riley (San Patricios) for the Mexican War slot.
NEXT:   era 1800-1850, then 1850-1900.

## Units

| # | unit | state | landed (commit / note) |
|---|------|-------|------------------------|
| 1 | era 05 1750-1800 | landed | 4 spans + 3 verified stories (washington, joseph-plumb-martin, deborah-sampson-war); bank §5 |
| 2 | era 06 1800-1850 | working | |
| 3 | era 07 1850-1900 | todo | |
| 4 | era 08 1900-1950 | todo | |
| 5 | era 09 1950-2000 | todo | |
| 6 | era 10 2000-today | todo | |

<!-- state: todo | working | landed | skipped (say why) -->

## Sources in hand

<!-- URL: what it settled. A successor re-reads these instead of re-searching. -->
Era 5 (all cited inline in research-war.md §5):
- https://www.battlefields.org/learn/articles/battle-monongahela-july-9-1755 : Braddock numbers
- https://founders.archives.gov/documents/Washington/02-01-02-0169 : 4 bullets, 2 horses
- https://www.battlefields.org/learn/french-indian-war/battles/siege-fort-william-henry : FWH
- https://www.nps.gov/mima/learn/historyculture/april-19-1775.htm : Lexington/Concord numbers
- https://www.nps.gov/articles/000/the-battle-of-bunker-hill.htm : Bunker Hill
- https://www.nps.gov/places/saratoga-surrender-site.htm : 5,895 surrendered
- https://www.loc.gov/item/today-in-history/october-19/ : Yorktown
- https://www.battlefields.org/learn/articles/american-revolution-faqs : 6,800 KIA, 17,000 disease
- https://www.nps.gov/articles/000/prison-ship-martyrs.htm : 11,500 prison ship dead
- https://www.battlefields.org/learn/articles/washington-inoculates-army : inoculation method
- https://www.nps.gov/vafo/learn/historyculture/valley-forge-history-and-significance.htm : VF deaths
- https://founders.archives.gov/documents/Washington/03-12-02-0628 : 2,898 barefoot
- https://www.nps.gov/people/joseph-plumb-martin.htm , https://www.battlefields.org/learn/articles/joseph-plumb-martin , https://www.nps.gov/articles/000/valley-forge-footwear-3.htm : Martin
- https://www.womenshistory.org/education-resources/biographies/deborah-sampson , https://www.masshist.org/object-of-the-month/objects/deborah-sampson-soldier-in-disguise-2005-03-01 , https://www.paulreverehouse.org/quitting-the-male-habit-paul-revere-and-deborah-sampsons-appeal-for-a-military-pension/ : Sampson
- https://www.army.mil/article/65594/st_clairs_campaign_of_1791_a_defeat_in_the_wilderness_that_helped_forge_todays_u_s_army : St. Clair, Fallen Timbers

## Decisions and known gaps

<!-- Facts left out rather than hedged. Disputes recorded. Anything a successor must not undo. -->
- Era 5 disputes recorded in bank: Fort William Henry death toll; prison-ship dead (NPS 11,500 vs ABT 8,000-12,000 POW); Sampson's wound (thigh/penknife from Mann 1797 vs Young's shoulder/breast); Martin's bleeding-feet line (NPS: may be postwar story); St. Clair split of killed/wounded.
- Era 5 left out: Native nations choosing sides in the Revolution, Sullivan 1779 (native-nations leads; not researched); treaties (america-world).

## Log

<!-- One line per save: date-time | unit | what landed | validator result -->
2026-09-26 | unit 1 era 1750-1800 | outline era 5 researched, bank §5, workspace checklist | validator 0 errors
