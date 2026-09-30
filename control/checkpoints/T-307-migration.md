# CHECKPOINT T-307 | migration | prose | writer A: eras 1-7 (part1 + part2), writer B: eras 8-10 (part3)

STATUS: T-307b landed (director verified: PASS  migration / prose)
VERIFY: python tools/project_state.py --check migration --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/migration/part1-before-1800.md (eras 1-5) · manuscript/migration/part2-1800s.md (eras 6-7)
        · manuscript/migration/part3-1900s-and-today.md (eras 8-10) · research/research-migration.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    T-307b done (units 8-11). Self-review run and repairs applied. Prose check PASS.
NEXT:   T-307b: Unit 8. Create manuscript/migration/part3-1900s-and-today.md (eras 08-10), copying part2's
        header layout with file="part3". Match the voice of part1/part2. Do not re-explain the domestic slave trade,
        Indian Territory, the Homestead Act or the Exodusters (told in part2).

## Research state before writing (2026-09-29)

PASS  migration / research
measured: stage=RESEARCHED eras=10/10 stories=15 (v15 c0 t0) verify_tags=0 bank=14985w outline=3685w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-307a | done | 444w, validator 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-307a | done | 767w, validator 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-307a | done | 895w, validator 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-307a | done | 635w, validator 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-307a | done | 1229w, validator 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-307a | done | 2468w, validator 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-307a | done | 2536w, validator 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-307b | done | ~2040w, validator 0 errors, emdash=0 semicolon=0 |
| 9 | era 09 1950-2000 -> part3 | T-307b | done | ~790w, validator 0 errors, emdash=0 semicolon=0 |
| 10 | era 10 2000-today -> part3 | T-307b | done | ~1360w, validator 0 errors, emdash=0 semicolon=0 |
| 11 | final: self-review, --punct, validator, prose check | T-307b | done | part3 validator 0 errors, emdash=0 semicolon=0, PASS migration / prose |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 02 | Acoma 1599: who, what was done, how many | PATCH (copied from native-nations bank) | "PATCH 2026-09-29 (T-307a): Acoma, 1599"
- 03 | Roger Williams's move (outline item) | PATCH (copied from religion bank) | "PATCH ... Roger Williams's move to Providence"
- 04 | who lived on the southern Plains before the Comanche | PATCH (TSHA) | "PATCH ... who lived on the southern Plains"
- 05 | what was done to the Acadians, deaths at sea | PATCH (Canadian Encyclopedia) | "PATCH ... what was done to the Acadians"
- 06 | Thornton's 8,000 (was search-summary only) | PATCH (PDF read) | "PATCH ... Thornton's Cherokee figure confirmed"
- 06 | what "fleeing persecution" means for the Mormon Trail | PATCH (copied from religion bank) | "PATCH ... what 'fleeing persecution' means"
- 06 | whose land in Utah and the Willamette Valley | PATCH (Utah Historical Society; Oregon Encyclopedia) | "PATCH ... whose land the trail crowds entered"
- 07 | why the Exodusters left | PATCH (National Archives, Prologue) | "PATCH ... why the Exodusters left"
- 07 | whose land the 1889 run opened | PATCH (OHS x3) | "PATCH ... whose land the 1889 Land Run opened"
- 07 | which cession became the Unassigned Lands | SEARCHED, NOT FOUND | "SEARCHED, NOT FOUND 2026-09-29 (T-307a)"
- 07 | the Weeping Time (parked from marketplace) | PATCH (copied from marketplace bank) | "PATCH ... the Weeping Time"
- 08 | who attacked in Chicago 1919 | PATCH (copied from rights-movements bank) | "PATCH 2026-09-29 (T-307b): who attacked in Chicago, 1919"
- 08 | who carried out the 1942 removal, how | PATCH (Densho x2) | "PATCH ... who carried out the 1942 removal"
- 08 | who beat Joe Lee, Gladney trip | PATCH (NPR x2, American Conservative review) | "PATCH ... Ida Mae Brandon Gladney"; beaters unnamed
- 08 | Starling (outline claims not in bank) | PATCH (NPR x2, LitCharts) | "PATCH ... George Swanson Starling"; grove owners unnamed
- 08 | Thompson's route | PATCH (Wikipedia) | "PATCH ... Florence Owens Thompson's actual route"
- 09 | why Foster left, the drive | PATCH (NPR, LitCharts) | "PATCH ... why Robert Foster left"
- 09 | Relocation outcomes | PATCH (copied from native-nations bank) | "PATCH ... what Relocation led to"
- 10 | Robertses after Memphis, record label | PATCH (Spirituality & Practice, Rolling Stone, Salon, Gallery Podcast) | "PATCH ... the Robertses after Memphis"
- 10 | six months in Memphis, diplomas | SEARCHED, NOT FOUND | "SEARCHED, NOT FOUND 2026-09-29 (T-307b)"

## OPEN (should be rare)

## Outline claims left out
- era 03: "settlement crawls up the Chesapeake rivers" (not in the bank, low value, left out).
- era 10: Kimberly Roberts "six months in Memphis" and "no high school diplomas" (search summary only, SEARCHED, NOT FOUND).
- era 10: Houston Astrodome 25,000 (search summary only).

## Decisions and defects fixed
- Bank "over 4,000 died" (Trail of Tears) replaced in prose by the sourced range (NPS 1,000+ on the road to Thornton's 8,000).
- Bank "fleeing persecution" (Mormon Trail) was an abstraction: prose names Boggs's order, Haun's Mill, the Carthage killings.
- Bank "the era of open, free-for-the-taking land" (1890 frontier) was land erasure: prose says the land had belonged to Native nations.
- Bank "went from empty ground to towns" (Guthrie, Oklahoma City) rewritten without "empty".
- Bank's Cahokia "comparable in size to London" comparison dropped. "Brutal winter" (cattle) adjective dropped.
- Oñate "first" narrowed to "first known overland colony" (T-244 correction); Acoma told in the Oñate story at full weight with the range of dead and the sentences.
- Search-summary-only figures not written: Neoheroka 600/400 split, Tadman 60-70 percent, second Choctaw count, NMAI 250-450 miles, Bosque Redondo 2,500-3,500, Violet/Duke William, Oregon malaria toll.
- Era 05 spans put in date order (Acadians 1755 before the Wilderness Road 1775).
- Weeping Time (parked from marketplace) added to era 07 as a short span on the domestic trade in the 1850s. Destinations of the people sold are not in the sources and the prose says so.

- T-307b: Florence Owens Thompson was framed in bank and outline as a Dust Bowl migrant. Wikipedia shows she moved to California in the 1920s. Prose says so.
- T-307b: bank 'Texas and Florida each over half a million 2023-24' not written (T-244 correction). New Orleans 2025 city figure (third-party only) not written.
- T-307b: 1942 removal told with actors (DeWitt, Bendetsen, Army), which the T-244 PATCH left as a passive ('were removed').
- T-307b: Relocation told as paid moves (bank's 'the government moves' kept precise). Houston 'more than any other city' not claimed.

## PARKED EARLIER (FILED by the director)
- Oregon Trail computer game (bank sidebar, also parked in sports-play): not written here. The director decides which chapter carries it.
- Newport Gardner and Black New Englanders to Liberia, 1826 (parked from music): not written. It is emigration abroad, outside this chapter's angle. Possibly immigration or music.
- slavery-freedom: the Weeping Time now appears briefly in migration era 07 (forced-movement angle). slavery-freedom leads.
- native-nations / religion: this chapter now carries short versions of Acoma 1599 and the 1838-1846 Missouri/Illinois violence, copied from those banks. Check for overlap at audit.

## Log
- 2026-09-29 T-307a unit 1 (before-1500): 444 words, validator 0 errors, --punct emdash=0 semicolon=0. No gaps researched (bank complete for this era).
- 2026-09-29 T-307a unit 2 (1500s): 767 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH (T-307a) "Acoma, 1599" copied into bank era 2 from research-native-nations.md (verified there). Oñate "first" narrowed to "first known overland colony" per T-244 correction; Luna 1559 and St. Augustine 1565 stated.
- 2026-09-29 T-307a unit 3 (1600s): 895 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH (T-307a) "Roger Williams's move to Providence" copied into bank era 3 from research-religion.md (verified there). Hooker story carries the Suckiaug/Sequassen PATCH (T-244).
- 2026-09-29 T-307a unit 4 (1700-1750): 635 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH (T-307a) "who lived on the southern Plains before the Comanche came" (TSHA Handbook, Apache Indians, fetched). T-244 search-summary split (600 killed / 400 sold at Neoheroka) not written; DNCR's 950 used.
- 2026-09-29 T-307a unit 5 (1750-1800): 1229 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH (T-307a) "what was done to the Acadians, and the deaths at sea" (Marsh, Canadian Encyclopedia, fetched with curl). Violet / Duke William sinkings left unconfirmed and unwritten. Spans put in date order (Acadians 1755 first, then Wilderness Road 1775, then ordinances). part1 complete: 3970 words.
- 2026-09-29 T-307a unit 6 (1800-1850): 2468 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCHes (T-307a): Thornton 1984 confirmed on the PDF; "fleeing persecution" made specific (Boggs order, Haun's Mill, Carthage, Nauvoo exodus, copied from religion bank); whose land in Utah (Utah Historical Society x2) and the Willamette Valley (Oregon Encyclopedia, David Lewis). Left unwritten as search-summary only: Tadman 60-70 percent, the second Choctaw count (15,000 / 2,500), the 1830s malaria toll in Oregon.
- 2026-09-29 T-307a unit 7 (1850-1900): 2536 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCHes (T-307a): why the Exodusters left (Davis, Prologue 2008, National Archives); whose land the 1889 run opened (OHS x3); the Weeping Time copied from marketplace bank. SEARCHED, NOT FOUND: which cession became the Unassigned Lands. Not written (search summary only): NMAI 250-450 miles, water sources destroyed, 2,500-3,500 Bosque Redondo deaths.
- 2026-09-29 T-307b unit 8 (1900-1950): about 2,040 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCHes (T-307b): Chicago 1919 attackers (copied, rights-movements), 1942 removal actors (Densho), Gladney (NPR, American Conservative), Starling (NPR, LitCharts), Thompson route (Wikipedia). Added a short 1942 Japanese American removal span from the T-244 PATCH. Thompson told as a 1920s migrant, not a Dust Bowl refugee (bank framing corrected).
- 2026-09-29 T-307b unit 9 (1950-2000): about 790 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCHes (T-307b): Foster's reason and drive (NPR Tell Me More, LitCharts); Relocation poverty and communities (copied from native-nations bank). Relocation told as paid moves, not force (bank's own wording).
- 2026-09-29 T-307b unit 10 (2000-today): about 1,360 words, validator 0 errors, --punct emdash=0 semicolon=0. Every figure dated and sourced in plain words. Bank's 'Texas and Florida over half a million' not written (T-244 correction). New Orleans 2025 city figure (362,154, third-party only) not written; 2024 figure and Data Center metro 2025 figure used. PATCH: Robertses after Memphis. SEARCHED, NOT FOUND: six months and diplomas (left out).
- 2026-09-29 T-307b unit 11 (final): self-review run (cadence, institutions as subjects, passives, hard words, repeated-unit openings). About 25 repairs. part3 about 4,290 words. Final: validator 0 errors, emdash=0 semicolon=0, PASS migration / prose (13,388 words, 15 stories).
