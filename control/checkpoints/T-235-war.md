# CHECKPOINT T-235 | war | research | eras 5-10 (resumes T-232, which landed eras 1-4)

<!-- The director fills the header and the unit list before dispatch. The agent keeps
     everything else current, and commits and pushes after every unit. Write it for a
     stranger who has only this file and the repo. -->

STATUS: IN-FLIGHT (units 1-3 landed and verified by the director. T-235b owns units 4-6)
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

NOW:    T-235b working unit 6 (era 2000-today). Units 4-5 landed.
NEXT:   era 2000-today, then flags + workspace + final check

## Units

| # | unit | state | landed (commit / note) |
|---|------|-------|------------------------|
| 1 | era 05 1750-1800 | landed | 4 spans + 3 verified stories (washington, joseph-plumb-martin, deborah-sampson-war); bank §5 |
| 2 | era 06 1800-1850 | landed | 3 spans + 1 verified story (john-riley-san-patricios); bank §6 |
| 3 | era 07 1850-1900 | landed | 6 spans + 4 verified stories (amos-humiston, grant-lee, christian-fleetwood, cathay-williams); bank §7 |
| 4 | era 08 1900-1950 | landed | 7 spans + 4 verified stories (henry-gunther, benjamin-o-davis-jr, daniel-inouye, chester-nez-war); wwii-gi target replaced; bank §8 |
| 5 | era 09 1950-2000 | landed | 7 spans + 3 verified stories (ron-kovic, muhammad-ali-war, hugh-thompson); [VERIFY] 1973 resolved; bank §9 |
| 6 | era 10 2000-today | working | |

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
- https://sgp.fas.org/crs/natsec/RL32492.pdf : CRS RL32492 (2020), DoD official table of deaths for every war 1775-1991 incl. WWI, WWII, Korea, Vietnam, Gulf. USE THIS FOR ERAS 8-10 TOO. (congress.gov page returns 403; the fas.org PDF works; read it with python pypdf after `sys.modules['cryptography']=None`.)
Era 6 (cited in bank §6): house.gov 1812 vote; nps.gov/stsp invasion-of-washington; NPS TwHP Fort McHenry article; battlefields.org new-orleans; dos.fl.gov seminole-wars; senate.gov declarations-of-war/mexico; archives.gov treaty-of-guadalupe-hidalgo; nps.gov/articles/mexican-war-medicine.htm; tshaonline san-patricio-battalion; nps.gov/places/the-san-patricio-brigade.htm; NPS harney-re-examined-part-iv; americanheritage.com tragic-story-san-patricio-battalion; smithsonianmag San Patricios.
Era 7 (cited in bank §7): battlefields.org civil-war-casualties, gettysburg, amputations-and-civil-war, andersonville-prison, remember-fort-pillow, biographies christian-fleetwood / ulysses-s-grant / robert-e-lee; discovere.binghamton.edu civilwar-3826 (Hacker); smithsonianmag Fort Pillow and Wounded Knee; historynet Amos Humiston (Dunkelman); neh.gov incognito-in-the-infantry (Cathay Williams); acwm.org Lee as slaveholder; thenmusa.org buffalo-soldiers-2; history.state.gov milestones/1899-1913/war; militarytimes 2025 Wounded Knee medals.
- https://www.army.mil/article/65594/st_clairs_campaign_of_1791_a_defeat_in_the_wilderness_that_helped_forge_todays_u_s_army : St. Clair, Fallen Timbers

Era 8 (T-235b, all cited in bank §8): CRS Table 1 (WWI/WWII totals); Kramer New Yorker 2008 PDF at paulkrameronline.com (water cure, Glenn, Smith); archives.gov ww1 draft-registration + meuse-argonne; archivesfoundation.org (2.8M drafted); army.mil 210420 + kumc.edu Holmes (flu, dispute); Choctaw Nation code-talkers booklet PDF (Bloor memo); history.com armistice-last-american-death + westernfrontassociation.com (Gunther); mallhistory.org/items/show/407 (Hushka); NHHC Pearl Harbor fact sheet (via search; NHHC 503s); nps.gov uss-arizona-memorial; pacificwarmuseum.org Doris Miller; ibiblio hyperwar Liscome Bay war damage report; dday.org necrology-project; nationalww2museum.org battle-iwo-jima + medal-of-honor-recipient-daniel-inouye; nps.gov/articles/inouyeww2.htm; tuskegee.edu Haulman Nine Myths PDF; thenmusa.org Davis; guides.loc.gov chester-nez; intelligence.gov Navajo; densho (via search, 403); brookings Manhattan costs; docsteach Handy order; ahf.nuclearmuseum.org bombings; rerf.or.jp/en/faq; atomicarchive USSBS section_II; va.gov gi-bill.pdf (via search); history.com gi-bill-black-wwii-veterans.

Era 9 (bank §9): CRS Table 1 (Korea, Vietnam, Gulf); archives.gov vietnam-war casualty-statistics (1968: 16,899); VVMF 2025 names (via search, 403); usmcmuseum.com 4_chosin.pdf; wikisource Army No Gun Ri Review Executive_Summary; cbsnews report-korean-war-era-massacre-was-policy (Muccio letter); upi 2001 Clinton regret; SSS Vietnam lotteries page (copy at jaclynhughes.wordpress.com PDF; sss.gov URL 404s); history.com Calley March 29; warrantofficerhistory.org Thompson PDF; newmobility.com ron-kovic-reborn; hnn.us Kovic essay; history.com Ali April 28; justia/LOC Clay v. US; army.mil 235994 West Point women; history.com DADT repeal; history.state.gov gulf-war; va.gov RAC-GWVI 2008 report PDF.

## Decisions and known gaps

<!-- Facts left out rather than hedged. Disputes recorded. Anything a successor must not undo. -->
- Era 5 disputes recorded in bank: Fort William Henry death toll; prison-ship dead (NPS 11,500 vs ABT 8,000-12,000 POW); Sampson's wound (thigh/penknife from Mann 1797 vs Young's shoulder/breast); Martin's bleeding-feet line (NPS: may be postwar story); St. Clair split of killed/wounded.
- Era 6 disputes: New Orleans British dead 285 (ABT) to ~700; Dade survivors 1 (FL DOS) to 2-3; Riley's brand (one cheek or both; upside-down re-brand from a 1955 American Heritage account). War of 1812 disease deaths: no government figure, the circulating 15,000 was not used. Riley's death date not established, not supplied.
- Era 7 disputes: Civil War dead 620,000 (ABT) vs ~750,000, range 650,000-850,000 (Hacker 2011); Fort Pillow Black dead 182 (Smithsonian) to ~300; Buffalo Soldier Medals of Honor 17-23; Wounded Knee who fired first; USS Maine cause. Humiston's wound not recorded, not described. Cathay Williams's death date and Riley's not established, not supplied.
- Era 7 left out: the draft and the 1863 riots (not researched; audit-queue candidate); a diarrhea/dysentery death figure (only secondary sources seen); Humiston orphanage abuse (1876) kept in bank only.
- Hand-offs to T-235b are in workspace/war.md ("Hand-offs from T-235a").
- Era 8 disputes: WWI flu deaths 45,000 (army.mil) vs 24,664 hospital-admitted (Holmes); Gunther birth day June 5 or 6 (not given); Bonus Army size 10,000-20,000+ veterans vs ~43,000 with families; Liscome Bay dead (used 'about three-fourths'); D-Day 4,436/2,519 (foundation, current) vs 4,414/2,501; Hiroshima/Nagasaki RERF 90,000-166,000 / 60,000-80,000 vs USSBS lower; Tuskegee 'never lost a bomber' is false (Haulman: 27). Era 8 left out: an ordinary WWII draftee (wwii-gi slot replaced by Inouye; audit-queue candidate); Isaac Woodard; oil (energy).
- Era 9 disputes: No Gun Ri dead (Army could not count; Yongdong 248 killed/injured/missing; survivors ~400; verified 163) and the Muccio letter vs the Army's no-order finding; My Lai 347 (Army) vs 504 (memorial); Vietnam draftees 1.8-2.2 million; Wall 58,281 vs DoD 58,220; Ali refused 3 or 4 times (not counted); Soldier's Medal day (outline says March 1998); Gulf War illness cause is the RAC 2008 committee's finding. Era 9 left out: Agent Orange, Tet, POWs, atomic testing on islanders/troops, rape at My Lai (not verified from a source read), Grenada/Panama/Somalia.
- Era 5 left out: Native nations choosing sides in the Revolution, Sullivan 1779 (native-nations leads; not researched); treaties (america-world).

## Log

<!-- One line per save: date-time | unit | what landed | validator result -->
2026-09-26 | unit 1 era 1750-1800 | outline era 5 researched, bank §5, workspace checklist | validator 0 errors
2026-09-26 | unit 3 era 1850-1900 | outline era 7 researched, bank §7, workspace hand-offs | validator 0 errors
2026-09-26 | unit 2 era 1800-1850 | outline era 6 researched, bank §6 (+ CRS Revolution dispute added to §5) | validator 0 errors
2026-09-26 | unit 4 era 1900-1950 | outline era 8 researched, bank §8 (PART C) | validator 0 errors
2026-09-26 | unit 5 era 1950-2000 | outline era 9 researched, bank §9 | validator 0 errors
