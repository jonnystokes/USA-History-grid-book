# CHECKPOINT T-254 | america-world | patch + bank check | eras 1-10

STATUS: DONE (director verified: patch PASS, research PASS). TO PARK pending.
VERIFY: python tools/project_state.py --check america-world --stage patch   (and --stage research)
BRIEF:  control/briefs/RESEARCH.md, MODE patch
MODEL:  opus
FILES:  outlines/america-world.md · research/research-america-world.md · workspace/america-world.md

NOW:    finished
NEXT:   director: run both checks, commit, file TO PARK.

## PARALLEL RUN (Jon, 2026-09-27): five agents at once

This agent runs at the same time as four others (T-251 to T-255, one chapter each). **Write only
your own chapter's three files and this checkpoint.** Do NOT edit any other chapter's outline,
research bank or workspace, even to park material there: another agent may be writing to it at
the same moment. Instead, list anything that belongs to another chapter under "TO PARK" below
(target chapter, era, the sourced text to add). The director files it after all five finish.
Reading other chapters' banks is fine.

## Measured before dispatch (2026-09-27)

FAIL patch: stories=13 (11 verified, 2 candidate, 0 target), bank 15,486w vs outline 8,931w, 0 [VERIFY], validator 0 errors. Gate blockers:

- line 190 `james-leander-cathcart` (candidate, 1750-1800): an American sailor enslaved in Algiers who wrote an account.
- line 296 `emilio-aguinaldo-america-world` (candidate, famous): the Philippine leader.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | the open story slots | done | cathcart + aguinaldo verified; bank PATCHes in 5.6 and era 07; --stage patch PASS |
| 2 | check that each verified story's key facts are in the bank; source any that are not | done | grep of ~70 outline facts: gaps were Kondiaronk (b.1649, Notre-Dame funeral) and Liliuokalani 1895 trial/upstairs room. PATCHes added (era 04, era 07) incl. Hawaii 1887-1895 actors (Dole, Thurston, Stevens, Willis) from history.house.gov |
| 3 | bank check, eras 1-5 | done | PATCHes: Menendez letter (132+10 throats cut, hands tied, 16 spared, Timucua land); Lenape land; Louisbourg deaths (~130 siege + 561 winter, ~1,200 Pepperrell); 1783 treaty & Six Nations (clears unverified #11); XYZ/Convention 1800 (no $ figures, no signing date) |
| 4 | bank check, eras 6-10 | done | PATCHes: Mexican cession people (80k-100k); water cure (Glenn, Ealdama, Igbaras, Kramer); occupations Haiti/DR/Nicaragua (Wilson, Taft, Somoza, Sandino, >2,000-3,250 cacos); Ponce/Winship; sterilization defined (Law 116, 97 forced, 1/3 by 1968, 41% 1982); NATO wording correction; Marshall >$12bn; coups Iran/Guatemala/Chile with actors and Pinochet toll 3,216; perishables (Costs of War, Guantanamo, FOMB firings + injunction). 1 SEARCHED NOT FOUND (Nicaraguan dead). |
| 5 | final: flags, validator, both checks | done | outline: 52 cells rewritten with new facts and zero em dashes/semicolons in book prose; new spans: Law 116 sterilization (era 08), coups (era 09); all 10 eras progress=researched; validator 0 errors; patch PASS, research PASS (bank 22100w vs outline 10492w) |

## SUBJECT NOTES (from the director)

Registry angle: dealings with the rest of the world: diplomacy, alliances, treaties, empire, global influence. Carries the territories thread (Hawaii, Alaska, Puerto Rico, Guam, Samoa, the Philippines). Not: the fighting itself (`war`), the peoples of Alaska and Hawaii as nations (`native-nations`). The bank was built by two half-agents as staging files: check the joins between eras 5 and 6. Hard subjects (prompts; check the bank): the overthrow of Hawaii's queen in 1893 (who acted, the troops) · the Philippine-American War dead (with ranges and whose count) and the water cure · occupations of Haiti, Nicaragua and the Dominican Republic (who ordered, deaths) · Puerto Rico: the Ponce massacre (1937), the sterilizations (define the word, per policy 3b) · Cold War coups the US backed (Iran 1953, Guatemala 1954, Chile 1973) with named actors · the territories' status today, dated.

Each open slot must become a real, named, documented person whose story the bank sources, or be
handled honestly (never invent a name; an unnamed documented account becomes hb-zoom prose, and
the hb-story block is removed). Before choosing a person, search `outlines/` and `manuscript/`
so no other chapter already tells them (ignore `outlines/BOOK-OUTLINE.md`, a compiled copy).
Keep slugs unique across the book.

Perishable: every 2000-today figure. Date each and refresh to 2026 where a newer official figure
exists.

## PARKED EARLIER (FILED by the director)
- **health, era 1900-1950 and 1950-2000:** the Puerto Rico Law 116 sterilization material. Copy the bank section "PATCH 2026-09-27 (T-254): sterilization of Puerto Rican women (\"la operación\")" from research/research-america-world.md (sources: HNN / Jaquira Díaz; DIG podcast with Briggs and López cited). Health owns the medicine and clinics; america-world keeps the US-appointed-government angle.
- **war, era 1500s:** Menéndez's own letter to Philip II, 15 Oct 1565 (trans. Eugene Lyon), https://earlyfloridalit.net/pedro-menendez-de-aviles-letter-to-king-philip-ii/ : 132 throats cut at Fort Caroline plus 10 next day; "I had their hands tied behind them and put them to the knife"; 16 spared (12 Breton seamen, 4 craftsmen). war's bank 2.4 has the NPS counts but may lack the letter. Copy from america-world bank era 02 PATCH.
- **war, era 1900-1950:** the water cure at Igbaras (Kramer, New Yorker, author's PDF) and Waller's shooting of eleven guides. Copy from america-world bank era 08 PATCH "the water cure".
- **slavery-freedom, era 1750-1800 (optional):** Cathcart's first-hand account of enslavement in Algiers (bastinado, 9 of 21 dead). Copy from america-world bank era 05 PATCH.

## Sources in hand
- Cathcart, *The Captives* (1899), full text https://archive.org/download/captives00cathrich/captives00cathrich_djvu.txt : birth 1 June 1767, Maria crew of 6, 21 Americans taken 1785 (9 died, 12 home at different times), bastinado 28 blows, rise to chief Christian clerk, left Algiers 8 May 1796.
- Dartmouth agent record https://archives-manuscripts.dartmouth.edu/agents/people/7507 : dates, consular posts.
- LOC finding aid + loc.gov item: Cloudflare/403, unreadable by tools.
- Britannica Aguinaldo (curl works where WebFetch 403s): full bio. Office of the Historian /milestones/1899-1913/war : casualties, "burned villages ... torture". armyhistory.org Funston capture: method, 2 guards killed, Apr 19 1901 proclamation.

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed
- Bank defect NOT fixed (per brief, do not rewrite bank text): era 08 "Puerto Rico between the wars" bullets and heading, and "Guam under Japanese occupation" heading, appear twice (a join artifact from the two half-agents). Harmless duplication. Director may dedupe at audit.
- NATO: bank/outline said "first permanent military alliance the US ever joined in peacetime"; Office of the Historian says "first peacetime military alliance ... outside of the Western Hemisphere". Correction note in bank; outline fixed.
- Bank said Cathcart "and twenty other sailors" were enslaved from the Maria, and that he sailed home "with twelve surviving members of the original crew". His own list: Maria crew was 6, the 21 were from two ships, the 12 survivors went home at different times. Correction notes added beside the old lines (old text kept); outline story rewritten.

## Log
- 2026-09-27 Unit 5 done. Both checks PASS.
- 2026-09-27 Unit 4 done.
- 2026-09-27 Unit 4 in progress: era 8 PATCHes landed (Haiti/DR/Nicaragua occupations with actors and counts, Ponce/Winship, PR sterilization defined, NATO/Marshall corrections) and era 9 coups (Iran, Guatemala, Chile). Next: water cure source, era 6-7 land/nations, era 10 perishables.
- 2026-09-27 Unit 3 done.
- 2026-09-27 Unit 2 done.
- 2026-09-27 Unit 1 done. patch check PASS (v13 c0 t0, bank 17062w vs outline 9222w).
