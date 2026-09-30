# CHECKPOINT T-312 | america-world | prose | ONE writer, all 10 eras (part1, part2, part3)

STATUS: T-312 landed (director verified: PASS  america-world / prose)
VERIFY: python tools/project_state.py --check america-world --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/america-world/part1-before-1800.md (eras 1-5) · manuscript/america-world/part2-1800s.md (eras 6-7)
        · manuscript/america-world/part3-1900s-and-today.md (eras 8-10) · research/research-america-world.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    All 11 units done. Prose check PASS.
NEXT:   Director: commit; park items below.

## Research state before writing (2026-09-29)

PASS  america-world / research
measured: stage=RESEARCHED eras=10/10 stories=13 (v13 c0 t0) verify_tags=0 bank=22396w outline=10534w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-312 | done | 372w, 0 errors, 0/0 |
| 2 | era 02 1500s -> part1 | T-312 | done | 400w, 0 errors, 0/0 |
| 3 | era 03 1600s -> part1 | T-312 | done | 491w, 0 errors, 0/0 |
| 4 | era 04 1700-1750 -> part1 | T-312 | done | 785w, 0 errors, 0/0 |
| 5 | era 05 1750-1800 -> part1 | T-312 | done | 3019w, 0 errors, 0/0 (part1 self-review run) |
| 6 | era 06 1800-1850 -> part2 | T-312 | done | 1481w, 0 errors, 0/0 |
| 7 | era 07 1850-1900 -> part2 | T-312 | done | 2295w, 0 errors, 0/0 (part2 self-review run) |
| 8 | era 08 1900-1950 -> part3 | T-312 | done | 3065w, 0 errors, 0/0 |
| 9 | era 09 1950-2000 -> part3 | T-312 | done | 1877w, 0 errors, 0/0 |
| 10 | era 10 2000-today -> part3 | T-312 | done | 1616w, 0 errors, 0/0 |
| 11 | final: self-review, --punct, validator, prose check | T-312 | done | 15,577w total, 13 stories verified, PASS |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 06 | Florida 1818-19: who lived there, what Jackson did | PATCH | "PATCH 2026-09-29 (T-312): Florida, 1818 to 1819, and who lived there"
- 06 | Guadalupe Hidalgo: what the treaty says about Native nations | PATCH | "PATCH ... Article XI of the Treaty of Guadalupe Hidalgo"
- 06 | Mexican Cession nations by name | SEARCHED, NOT FOUND | "SEARCHED, NOT FOUND ... Mexican Cession"
- 06 | Louisiana Purchase nations by name | SEARCHED, NOT FOUND | "SEARCHED, NOT FOUND ... Louisiana Purchase"
- 07 | Alaska: whose land Sitka was, what US rule did | PATCH | "PATCH 2026-09-29 (T-312): Sitka was Tlingit land"

## OPEN (should be rare)

## Outline claims left out
- 05: Franklin "chose the costume on purpose ... the fame helped him get meetings and money" (bank has only that the French read the cap as rugged).
- 05: France "quietly sending money and gunpowder before it would sign anything" (bank heading only, no sourced detail).
- 05: "Americans disagreed furiously about which side to take" (1793), and "Americans were furious" after XYZ (no bank source).
- 05: Barbary "Once American ships sailed without the Royal Navy behind them" (no bank source).
- 05: Congress "argued about the cost for years while the men worked" (bank says only no navy, no money).
- 05: Saratoga's date (bank gives only December 1777 for the news reaching Vergennes).
- 05: the closing line "to the edge of war with both of Europe's great powers" kept only as the era zoom's plain "close to war with each".
- 07: Perry "Japan had kept nearly all foreign ships out for more than two hundred years" and "a letter of demands" (not in bank).
- 07: Liliʻuokalani "lived until 1917" (not in bank). The 1895 fine and the charge (misprision of treason) stay out: bank tags them unconfirmed.
- 07: the House vote count on the Newlands Resolution (bank has 209 or 290 to 91, unsettled).
- 06: Mexican-American War casualty totals (bank: not verified).
- 08: Haiti "a US military count at the time said 3,250" cacos killed (bank tags it search summary only, though its own note says to write it). Kept "more than 2,000, by some estimates" (CRS).
- 08: Dominican Republic: Wilson as the president who sent the Marines, and the 1,137 / 144 casualty counts (search summary only). Nicaragua: Taft as the president (search summary only).
- 08: Roosevelt Corollary, Lend-Lease, Hays Commission (all [VERIFY] or unsourced in bank).
- 08: which court convicted Albizu Campos of sedition, and when (bank gives neither; a Britannica page gave only AI-written summaries). Prose says "was later convicted of sedition".
- 08: the Haitian legislature's dissolution (bank names no one who did it).
- 09: first elected governors of Guam, USVI (1970) and American Samoa (1977): [VERIFY] in bank. Blair House casualties and names, the 1979 pardon, the 16-state count on the D.C. amendment, the Peace Corps executive-order number: all [VERIFY].
- 10: tariffs as policy from 2018 and 2025 (no source in bank). Davis v. Guam ([VERIFY]). Iranian dead (no count in bank). The Iran war's later course (ceasefire, renewed strikes): search summary only.

## Decisions and defects fixed
- 01: outline's triad "was there, was asked, or was told" rewritten as two plain clauses. Outline's cross-reference to another chapter ("this book tells it there") dropped: fourth wall.
- 02: outline's "Then the Frenchmen whose ships..." and Ribault "executed" passive: named Menéndez's men as the killers.
- 03: outline's closing line "The men who made that rule sat in a building he would never see" cut (performed). Lenape land named from the T-254 PATCH.
- 04: Nanfan "Six Nations people" wording changed to "Haudenosaunee people today" (in 1701 the league was five nations). Six Nations explained at its first use in era 05 (Tuscarora joined).
- 05: outline's "begged for help", "sent its first ministers to courts that had recently wanted them hanged" and similar performed lines cut. Outline's "He is usually described" hedge replaced by naming Britannica. Morocco "first" kept with its nuance. Institutions as actors (Congress, France, Britain, the treaty) repaired to delegates, senators, diplomats, or document verbs.
- 06-07: land erasure repaired: Seminole and escaped slaves in Florida, Article XI "savage tribes" and the Tohono O'odham in the Mexican cession, Tlingit land at Sitka and the 1869 shelling of Kake (all new PATCHes).
- 08: bank/outline defect: outline states Haiti's "US military count ... 3,250" cacos as fact while the bank tags it search summary only. Left out. Outline's "Balangiga ... It was the Army's worst single loss" kept (bank-sourced). Outline's Wilson story said Wilson's Marines occupied the Dominican Republic: only a search summary supports Wilson there, so the prose names Wilson only for Haiti.
- 08: Smith's order contains a semicolon in the bank's quotation. Split into two quotations at that point, no word changed.
- 08: bank NATO "first permanent military alliance ever" corrected per its own correction note to the Office of the Historian wording.
- 09: outline's "The rest stayed exactly where the Insular Cases had left them" and similar closing lines cut. Cuban Missile Crisis given from a new PATCH (bank had only the name).
- 10: outline era 10 was silent on the 2025-26 boat strikes, the Venezuela raid and the Iran war. Added from the war bank's read sources, copied into this bank as a PATCH. Outline's "China joined the WTO in December 2001" replaced by the WTO's own approval date.
- Parked items in the bank from exploration (Wilkes at Fiji, 1840) and war (Grant's quote on the Mexican war) not used: those chapters tell them with their own angle.

## TO PARK (for the director, burst runs only)
- `native-nations`: Tlingit at Sitka (Kiksadi fort burned by Baranov, 1804); USS Saginaw shelled and burned 28 of 29 Kake clan houses, early 1869; USRC Corwin destroyed most of Angoon, 1882 (Poulson, Alaska Historical Society). Florida 1818: Jackson's raid on Seminoles and escaped slaves (Office of the Historian). See this bank's T-312 PATCHes.
- `war`: no action needed. This chapter now names the 2025-26 boat strikes, the Venezuela raid and the Iran war briefly, from the war bank's sources.

## Log
- 2026-09-29 eras 01-03 written in part1 (372 / 400 / 491 words). validator 0 errors, --punct 0/0.
- 2026-09-29 era 04 written (785 words, 1 story). validator 0 errors, --punct 0/0.
- 2026-09-29 era 05 written (about 3,000 words, 3 stories). part1 self-review run and repairs applied. validator 0 errors (4 stories), --punct 0/0.
- 2026-09-29 era 06 written in part2 (1,481 words, 2 stories). Florida PATCH and Article XI PATCH used. validator 0 errors, --punct 0/0.
- 2026-09-29 era 07 written in part2 (2,295 words, 2 stories). Sitka/Kake PATCH used. Samoa deeds of 1900 and 1904 mentioned in one line only, full telling left to era 08 by the date rule. part2 self-review run. validator 0 errors (4 stories), --punct 0/0.
- 2026-09-29 eras 09 and 10 written in part3 (1,877 / 1,616 words, 3 stories). part3 self-review run. All three files: validator 0 errors, --punct 0/0. `--check america-world --stage prose`: PASS (10/10 eras written, 13 stories verified, 15,577 words).
- 2026-09-29 era 08 written in part3 (3,065 words, 2 stories). validator 0 errors, --punct 0/0. Bank PATCHes added for eras 09-10 (Cuban Missile Crisis; WTO/USMCA dates; 2025-26 military actions copied from the war bank's read sources).
