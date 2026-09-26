# CHECKPOINT T-237 | immigration | prose (Phase 2, first new chapter) | 10 eras, 3 part files

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check immigration --stage prose
        (per part: node tools/validate_grid.js <file> --part · python tools/project_state.py --punct <file>)
BRIEF:  standard WRITING brief (control/RESUME.md) + cloud lines (control/CLOUD-WORKFLOW.md §5)
SOURCES (read-only): outlines/immigration.md (the plan) · research/research-immigration.md (THE ONLY
        source of facts, DECISIONS #13) · workspace/immigration.md
MODEL:  manuscript/native-nations/ and manuscript/city-building/ are finished v2 chapters.
        Copy their file layout: an hb-chapter line with mode="prose" part="2" file="partN", an
        hb-note naming the file's eras, then the hb-time sections.
PLAN:   T-237a = part1-before-1800.md (eras 1-5), T-237b = part2-1800s.md (eras 6-7),
        T-237c = part3-1900s-and-today.md (eras 8-10).

NOW:    T-237a writing part1 era 1750-1800.
NEXT:   write part1 era 1750-1800 (append to manuscript/immigration/part1-before-1800.md).

## Units

| # | unit | state | landed (commit / note) |
|---|------|-------|------------------------|
| 1 | part1 era before-1500 (thin) | landed | file created, era written |
| 2 | part1 era 1500s (thin) | landed | era written |
| 3 | part1 era 1600s | landed | 6 spans + stories frethorne, hutchinson, jewish-refugees-1654 |
| 4 | part1 era 1700-1750 | landed | 4 spans + story zenger |
| 5 | part1 era 1750-1800 | working | |
| 6 | part2 era 1800-1850 | todo | |
| 7 | part2 era 1850-1900 | todo | |
| 8 | part3 era 1900-1950 | todo | |
| 9 | part3 era 1950-2000 | todo | |
| 10 | part3 era 2000-today | todo | |

## Outline claims NOT in the bank (left out, per DECISIONS #13)

<!-- The claim, the outline line, and where it would have gone. -->

- "small and often in danger" (St. Augustine, outline 1500s span, line 30). Bank does not say it. Left out of 1500s span.
- Hutchinson "to worship as they believed" and "on trial ... for her religious meetings" (outline line 44). Bank gives only "following minister John Cotton to Boston" and "tried November 1637 and banished". Left out.
- Frethorne "bound to Martin's Hundred plantation" (outline line 48): bank says only "at Martin's Hundred". Written as "worked at a place called Martin's Hundred".
- Zenger "the poor refugee boy" and "1735 acquittal began press freedom in America" (outline line 66). Bank gives only the 1735 seditious-libel acquittal. Left out.

## Defects in the outline or bank, fixed in the prose (go to AUDIT-QUEUE)

- Glosses from general knowledge, not in the bank (word definitions only, no historical claim): "Norse" = sailors from northern Europe; Newfoundland "in what is now Canada"; land bridge = dry ground joining Asia to North America.
- LAND ERASURE GAP (bank): bank section 2 does not name the Native nation on whose land Menendez built St. Augustine, and section 3 names only the Powhatan for the 1600s colonies (no Wampanoag for Plymouth, no nation for Massachusetts Bay, New Amsterdam, Maryland or Pennsylvania). Prose states "on Native land" from the bank's general lines. Audit should add the nations to the bank.
- PERSONIFICATION (outline 1600s, line 44): "The colony she joined ... put her on trial". Prose: "she was tried in Massachusetts and banished. The sources used here do not name her judges." Bank should name the court (General Court, Winthrop presiding) in audit.
- PERSONIFICATION (bank s3/s4 and outline line 52): "Portugal retook Dutch Brazil", "the Dutch West India Company overruled him". Prose: "Portuguese forces took it back", "Officials of the Dutch West India Company ... overruled him".
- CHRONOLOGY (outline 1700-1750 span, line 62): Huguenots "after 1685" sit in 1700-1750, but the bank says the 1,500 to 2,000 arrived by 1700. Moved to the 1600s era.
- POLICY QUESTION: jewish-refugees-1654 is a group story; only Jacob Barsimson is named. Kept as hb-story per brief (same slug/name). Director may want it as hb-zoom (policy s4: hb-story is named people only).
- Siwanoy attack on Hutchinson: bank gives no reason or land context. Prose says the sources used here give no reason. Audit gap.
- 1619 captors unnamed in bank: prose says "Captors whom the sources do not name".
- Glosses (1600s, general knowledge, not bank): loblollie = thin porridge; privateer; Puritans = English Protestants who disagreed with how the Church of England was run; Archbishop of Canterbury = head of the Church of England; Quakers = Society of Friends; Edict of Nantes = law that had let French Protestants worship in France; West Indies.
- Jamestown: bank says only "conflict with the Powhatan". Prose says the Powhatan people already lived on the land around Jamestown (land-erasure rule).
- PERSONIFICATION (bank s4): "South Carolina Lowcountry rice economy ... imported" Africans. Prose names rice planters as buyers. Sullivan's Island: bank uses agentless "were held"; prose says the sources used here do not name who held them.
- Convict transport: "Britain shipped" (outline line 62) is personification. Prose: "Under a British law of 1718 ... convicts were shipped" plus "The sources do not say who shipped and sold them."
- ADDED from bank (not in outline): 1700-1750 forced-arrival span (Charleston, Sullivan's Island, SlaveVoyages scale figures). Kept short per slavery-freedom lead.
- Glosses (1700-1750): Palatinate = region along the Rhine; Presbyterians; backcountry; apprentice; seditious libel; emigrate; quarantine; Lowcountry.
- Glosses (1500s): continental US = states other than Alaska and Hawaii; feast day; missionary.

## Log

<!-- date-time | unit | words | validator | --punct -->
- 2026-09-26 | 1 before-1500 | ~230 prose | 0 errors (--part) | emdash=0 semicolon=0
- 2026-09-26 | 2 1500s | ~380 prose | 0 errors (--part) | emdash=0 semicolon=0
- 2026-09-26 | 4 1700-1750 | ~800 prose | 0 errors (--part), 4 stories total | emdash=0 semicolon=0
- 2026-09-26 | 3 1600s | ~1,450 prose | 0 errors (--part), 3 stories | emdash=0 semicolon=0
