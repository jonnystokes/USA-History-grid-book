# CHECKPOINT T-330 | art | prose | ONE writer, all 10 eras (part1, part2, part3)

STATUS: T-330 landed (director verified: PASS  art / prose)
VERIFY: python tools/project_state.py --check art --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/art/part1-before-1800.md (eras 1-5) · manuscript/art/part2-1800s.md (eras 6-7)
        · manuscript/art/part3-1900s-and-today.md (eras 8-10) · research/research-art.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    finished. All 11 units done.
NEXT:   director: commit; Jon to rule on the Kehinde Wiley block.

## Research state before writing (2026-09-29)

PASS  art / research
measured: stage=RESEARCHED eras=10/10 stories=34 (v34 c0 t0) verify_tags=0 bank=38757w outline=19199w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-330 | done | 1639w, 0 errors, 0/0 |
| 2 | era 02 1500s -> part1 | T-330 | done | 2253w file, 0 errors, 0/0 |
| 3 | era 03 1600s -> part1 | T-330 | done | 3468w file, 0 errors, 0/0 |
| 4 | era 04 1700-1750 -> part1 | T-330 | done | 4617w file, 0 errors, 0/0 |
| 5 | era 05 1750-1800 -> part1 | T-330 | done | 6439w file, 0 errors, 0/0 |
| 6 | era 06 1800-1850 -> part2 | T-330 | done | 3757w file, 0 errors, 0/0 |
| 7 | era 07 1850-1900 -> part2 | T-330 | done | 7590w file, 0 errors, 0/0 |
| 8 | era 08 1900-1950 -> part3 | T-330 | done | 4571w file, 0 errors, 0/0 |
| 9 | era 09 1950-2000 -> part3 | T-330 | done | 8434w file, 0 errors, 0/0 |
| 10 | era 10 2000-today -> part3 | T-330 | done | 12507w file, 0 errors, 0/0 |
| 11 | final: self-review, --punct, validator, prose check | T-330 | done | 26406w chapter, 0/0/0 errors, 0/0 punct, PASS |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 01 | Is Nathan Jackson still living? | PATCH (no obituary; unconfirmed summaries) | Bank check eras 01-05
- 03 | Freake portrait: baby added later, museum | PATCH (Worcester catalogue opened) | Bank check eras 01-05
- 05 | Sons of Liberty, Whitefield glosses | PATCH (copied from other banks) | Bank check eras 01-05
- 06 | Removal Act, Trail of Tears, smallpox, 1832 vaccination exclusion, Four Bears speech, Douglass escape | PATCH (other banks) | before Era 08 heading
- 07 | Subscription book (door to door) | PATCH (Cambridge Mark Twain in Context opened) | same
- 07 | Tukudika removal by Norris; Dawes Act | PATCH (other banks) | same
- 07 | Fort Marion headstones | PATCH (from era 10 SNF wording) | Bank check eras 08-10 prose pass
- 08-10 | Ten story films | PATCH (pages opened; two details left unconfirmed) | Bank check eras 08-10 prose pass
- 08 | EO 9066 actors; FWP count; Kossola/Clotilda | PATCH (other banks) | same
- 09 | Warhol start and silkscreen; Margaret Garner; Stewart autopsy | PATCH (Wikipedia opened; crime-justice bank) | same
- 10 | Smithsonian order quote; Sajet firing | PATCH (whitehouse.gov, Spokesman-Review opened) | same
- No new SEARCHED, NOT FOUND entries were needed. Existing SNF entries were written as the bank prescribes.

## OPEN (should be rare)

## Outline claims left out
- About 30, all listed in the Log lines per era: e.g. Mesa Verde 1180 date, 25,000 petroglyphs, Le Moyne 'only one picture', White's 1587 attack (disasters), Wheatley 1772 exam date, Copley's Revere, Patience Wright spying, Douglass Jr. passport, King Shotaway play, Met's 1891 Sunday date, Tanner 'M. Tanner' line, Howling Wolf's Boston treatment, Savage 'kicked' quote, post office murals count, Peixotto letter, de Kooning/Rothko/Motherwell, Greenberg 1948 quote, Parks's Life subjects, Obamas' 20 portfolios and $500,000, LACMA stop, MONUMENTS 19 artists, BLM replacement murals, McKernan 30% income, Sherald grisaille, Kennedy Center (music), Federal furniture (styles), Gustavus Vasa play (theatre).

## Decisions and defects fixed
- Defects in sources fixed in prose (sources left alone): outline's 'Mesa Verde 1180' (search summary) replaced by NPS range; outline's 'Pueblo people use petroglyphs in ceremonies' kept to NPS wording; outline's 'Catlin often took objects' corrected to 'sometimes'; Savage beating quote disputed in bank, replaced with plain statement; outline's 'Dunn/Studio', 'Harlem-is first' kept attributed; Kühn 'earliest enslaved African' kept attributed to an art-history website; Mapplethorpe photographs described as 'sexual' in the outline but not in the bank, dropped; 'Tukudika forced onto reservations' given its actor (Norris and the Fort Washakie agent); Eakins and several institution-as-actor lines repaired with named people or officials.
- KEHINDE WILEY: the story block (era 10, slug kehinde-wiley) is written from the bank's facts about his life and work only. The 2024 accusations (bank era 10, director's note) are left out entirely, per the dispatch. The Wiley block AWAITS JON'S RULING. Everything about Wiley sits in that one block and the span that mentions the Obama portraits. Rumors of War is told inside his block, not in the Confederate-statues span.

## TO PARK (for the director, burst runs only)

## Log
- 2026-09-30 era 01 before-1500 landed in part1: file 1639 words, validator 0 errors, --punct emdash=0 semicolon=0. PATCH: Nathan Jackson still living (bank check eras 01-05). Mesa Verde 1180 date and 25,000 petroglyph count left out (search summary only).
- 2026-09-30 unit 2 landed in manuscript/art/part1-before-1800.md: file 2253 words, validator: === part1-before-1800.md : 1 chapters, 2 stories, 0 errors | C:/Users/jon/Projects/History-Book-Project-claude/manuscript/art/part1-before-1800.md: emdash=0 semicolon=0. Era 02 1500s. No new research. Le Moyne 'only one surviving picture' and White's 1587 Dasamonquepeuc attack left out (search summary only / bank assigns to disasters).
- 2026-09-30 unit 3 landed in manuscript/art/part1-before-1800.md: file 3468 words, validator: === part1-before-1800.md : 1 chapters, 4 stories, 0 errors | C:/Users/jon/Projects/History-Book-Project-claude/manuscript/art/part1-before-1800.md: emdash=0 semicolon=0. Era 03 1600s. PATCH: Freake portrait confirmed on Worcester Art Museum catalogue (baby added later, Mary born May 6 1674). Gustavus Vasa play (parked) left out as theatre.
- 2026-09-30 unit 4 landed in manuscript/art/part1-before-1800.md: file 4617 words, validator: === part1-before-1800.md : 1 chapters, 6 stories, 0 errors | C:/Users/jon/Projects/History-Book-Project-claude/manuscript/art/part1-before-1800.md: emdash=0 semicolon=0. Era 04 1700-1750. No new research. Governor's name for the 1725 baskets left unprinted (disputed in bank). Silver collar detail left out (search summary only). Fred Wilson 1992 kept for era 09.
- 2026-09-30 unit 5 landed in manuscript/art/part1-before-1800.md: file 6439 words, validator: === part1-before-1800.md : 1 chapters, 10 stories, 0 errors | C:/Users/jon/Projects/History-Book-Project-claude/manuscript/art/part1-before-1800.md: emdash=0 semicolon=0. Era 05 1750-1800. PATCH: Sons of Liberty and Whitefield glosses copied from news-communication and religion banks. Left out: Wheatley examination date 1772 (search summary only), Copley's Revere portrait (search summary), Peale's Native objects (not in bank line), Patience Wright spying, Stuart nickname, Peale admission price, Federal furniture (styles).
- 2026-09-30 part1 self-review run (Version 2 + amendment 5 + policy 7): fixed a metadiscourse line, two institution-as-thinker lines (Pilgrim Hall), an unsourced 'red', elders not ministers, Moses Williams held unfree wording. part1 final: 0 errors, emdash=0 semicolon=0.
- 2026-09-30 unit 6 landed in manuscript/art/part2-1800s.md: file 3757 words, validator: === part2-1800s.md : 1 chapters, 4 stories, 0 errors | C:/Users/jon/Projects/History-Book-Project-claude/manuscript/art/part2-1800s.md: emdash=0 semicolon=0. Era 06 1800-1850. PATCHes: removal act and Trail of Tears, smallpox definition, 1832 vaccination program that left out the Mandan, Four Bears's speech, Douglass escape (copied from native-nations, health, slavery-freedom banks). Left out: Douglass Jr. passport (SNF in bank), King Shotaway play (theatre), Dave's first 'Concatination' jar (search summary), Moses Williams dates beyond bank.
- 2026-09-30 unit 7 landed in manuscript/art/part2-1800s.md: file 7590 words, validator: === part2-1800s.md : 1 chapters, 9 stories, 0 errors | C:/Users/jon/Projects/History-Book-Project-claude/manuscript/art/part2-1800s.md: emdash=0 semicolon=0. Era 07 1850-1900. PATCHes: subscription book (Cambridge, Mark Twain in Context), Tukudika removal by Norris, Dawes Act (copied from land-environment and native-nations banks). Left out: Met first Sunday date 1891 (search summary only), Tanner 'M. Tanner' line (SNF), Fort Marion sale prices, Howling Wolf's Boston eye treatment and 1927 date details not in bank.
- 2026-09-30 part2 self-review run: rewrote the era 06 writers span (date anaphora), relabelled an unsourced span label, varied era openings across eras 04, 06, 07, removed a repeated landscape definition. part2 final: 0 errors, emdash=0 semicolon=0.
- 2026-09-30 before era 08: PATCHes added (films for eras 08-10 stories, confirmed on opened pages; EO 9066 actors and FWP count copied from rights-movements and slavery-freedom banks; Fort Marion headstone plan line added to era 07).
- 2026-09-30 unit 8 landed in manuscript/art/part3-1900s-and-today.md: file 4571 words, validator: === part3-1900s-and-today.md : 1 chapters, 6 stories, 0 errors | C:/Users/jon/Projects/History-Book-Project-claude/manuscript/art/part3-1900s-and-today.md: emdash=0 semicolon=0. Era 08 1900-1950. PATCHes: films (8-10), EO 9066 and DeWitt, FWP count, Kossola/Clotilda. Left out: Savage 'kicked/licked' quote (wording disputed; used 'almost whipped all the art out of me'), Peixotto letter (search summary), post office murals still hanging (SNF), Harp 5 million visitors (search summary), Lange 'Impounded' stamp (search summary), Abiquiu land grant (search summary), Ashcan painters (cut in bank).
- 2026-09-30 unit 9 landed in manuscript/art/part3-1900s-and-today.md: file 8434 words, validator: === part3-1900s-and-today.md : 1 chapters, 11 stories, 0 errors | C:/Users/jon/Projects/History-Book-Project-claude/manuscript/art/part3-1900s-and-today.md: emdash=0 semicolon=0. Era 09 1950-2000. PATCHes: Warhol's start and silkscreen, Margaret Garner (Wikipedia, opened), Stewart medical examiner (crime-justice bank). Left out: de Kooning, Rothko, Motherwell (not in bank), Greenberg 1948 quote (search summary), Mapplethorpe NEA amount, Alfred Young Man quote (SNF), Parks's Life subjects (not in bank), Chicano Park landmark 2016 (era 10 note only).
- 2026-09-30 unit 10 landed in manuscript/art/part3-1900s-and-today.md: file 12507 words, validator: === part3-1900s-and-today.md : 1 chapters, 15 stories, 0 errors | C:/Users/jon/Projects/History-Book-Project-claude/manuscript/art/part3-1900s-and-today.md: emdash=0 semicolon=0. Era 10 2000-today. PATCHes: Smithsonian order quote and Sajet firing confirmed (whitehouse.gov, Spokesman-Review). Wiley block from life and work only (Decisions). Left out: Obamas' choice from 20 portfolios and $500,000 funding (search summary), LACMA tour stop (search results only), MONUMENTS 19-artist count (search summary), BLM Plaza replacement murals (search summary), McKernan 30% income loss (search summary), Sherald grisaille (search summary), Kennedy Center (parked to music), Denver museum hall (search summary).
- 2026-09-30 unit 11 final: part3 self-review (institution-as-actor repairs, era 08 opening varied), all three validators 0 errors, --punct 0/0 each, prose check PASS (26406 words, 34 stories verified).
