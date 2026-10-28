# CHECKPOINT T-781 | cross-chapter leftovers | health, art, sports-play, city-building, food-farming, hand-offs

STATUS: DONE (5 of 5 items; every --check PASS)
FILES:  manuscript/health/part2-1800s.md, manuscript/art/part2-1800s.md,
        manuscript/sports-play/part1-before-1800.md, manuscript/city-building/part3-1900s-and-today.md,
        manuscript/food-farming/part3-1900s-and-today.md,
        research/research-health.md, research/research-art.md, research/research-sports-play.md,
        research/research-city-building.md (PATCH and line corrections),
        control/backmatter/work-workers.md, food-farming.md, slavery-freedom.md, art.md, health.md
VERIFY: python tools/project_state.py --check <slug> --stage prose, for health, art, sports-play,
        city-building, food-farming (also run for work-workers and slavery-freedom, whose hand-offs changed)
SCRATCH: C:\Users\jon\AppData\Local\Temp\claude\C--Users-jon-Projects\c3422736-ab9a-4784-b707-6df665469603\scratchpad\T-781\
         (t781_eras.py: era words and strips; before.txt and after.txt; t781_convention.py: strip rule survey)

## Items

| # | item | decision | state |
|---|------|----------|-------|
| 1 | Lewis Cass and the Mandan (ch 26 vs ch 32) | Health is right. ND Studies, Section 2 "Smallpox Among Indian Tribes" (State Historical Society of North Dakota, read with curl 2026-10-28): "Cass specifically excluded the Mandans, Hidatsas, and Arikaras". The same page gives his reasons, so health's "do not give his reason" was wrong too. Wikipedia IVA and ND Section 3 use passives and name no one. They do not contradict it | DONE |
| 2 | Cahokia's end in sports-play | follow the T-763 ruling (NPS, National Geographic): most people gone by about 1350, empty by about 1400 | DONE |
| 3 | Great Migration city figures in city-building | follow the T-762 Census table (Working Paper 76): Philadelphia about 59 percent and New York about 66 percent (1910 to 1920), New York more than doubled in the 1920s | DONE |
| 4 | five hand-off lines | match the chapters' current text | DONE |
| 5 | food-farming era 10 strip | 2,083 words (closing card counted, as the chapter's own era 1 strip counts its card) = 10.4, so about 10 minutes | DONE |

## Log

<!-- file | what landed | validator | --punct -->
- research-health.md | PATCH 2026-10-28 (T-781) at the end of era 06: ND Studies Section 2 quotes (Cass decided, Cass excluded the three, his two reasons, Document 1, Dougherty 1833, Clark 1838), the 1837-epidemic Wikipedia line, ruling | - | -
- health part2 | era 06 line 39: "The accounts of the program do not give his reason." replaced by "He believed the fur trade on the upper Missouri was no longer worth much to the United States. He also said that the treaties the three nations had signed in 1825 described them as hostile to the country and its citizens." (self-review: "marked them" -> "described them", a document verb on the approved list) | 0 errors | 0/0
- research-art.md | PATCH 2026-10-28 (T-781) after the T-330 era 06 PATCH: ND Studies Section 2 quote copied from the health bank, ruling | - | -
- art part2 | era 06 line 129: "were kept out of it. The records do not name the officials who left them out." -> "He left the Mandan, the Hidatsa and the Arikara of the upper Missouri out of it." | 0 errors | 0/0
- sports-play part1 | era 01 line 55: "say Cahokia declined around 1500, and that people went on playing chunkey" -> "Most of Cahokia's people had left the city by about 1350, and it was empty by about 1400. Staff at the Jefferson Patterson Park and Museum in Maryland say that people across North America went on playing chunkey after that." (the museum stays named, so back-matter places line 223 stays true) | 0 errors | 0/0
- research-sports-play.md | line 44-47 no longer states the 1500 date as fact; PATCH 2026-10-28 (T-781) after the chunkey bullets, NPS and National Geographic copied from the city-building bank with their source lines | - | -
- research-city-building.md | T-763 PATCH "Still carrying" line marked fixed by T-781 | - | -
- city-building part3 | era 08 line 101: "Philadelphia's rose about 500 percent, and New York's roughly doubled." -> "Philadelphia's rose about 59 percent, and New York's about 66 percent. In the 1920s New York's Black population more than doubled." | 0 errors | 0/0
- research-city-building.md | era 08 line 325 corrected; PATCH 2026-10-28 (T-781) after the Great Migration bullets, the Census Working Paper 76 figures copied from the migration bank's T-762 PATCH with its source line | - | -
- control/backmatter | work-workers.md 22 loblollie "thin" -> "thick"; food-farming.md 18 Starving Time = about 500 in the colony, about 240 of them in the fort, about 60 of those still alive by spring; slavery-freedom.md 92 and art.md 76 vaccinate/vaccination = fluid from cowpox sores scratched into the skin, protecting against smallpox (each in its chapter's words); health.md 32 "colonists in the fort" | - | 0/0 (no em dash or semicolon written)
- food-farming part3 | era 10 strip "about 11 minutes" -> "about 10 minutes" (strip only) | 0 errors | 0/0
- strips and cards after the edits (scratch after.txt): health era 06 2,453 words = 12.3, strip 12 right; art era 06 4,346 words without headings = 21.7, strip 22 right; sports-play era 01 1,121 words without the opening card = 5.6, strip 6 right; city-building era 08 3,653 = 18.3, strip 18 right. Cards unchanged and still right: health 115, art 155, sports-play 125, city-building 90, food-farming 75. No chapter closing touched
- noticed, not changed (for the director): era strips across the book follow two rules. Of 74 era 1 and era 10 strips, 45 leave the opening or closing card out of the count, 20 count it, and 9 match neither (art 10, drugs-alcohol 10, exploration 01, food-farming 10 before this fix, government-politics 10, money 10, religion 01 and 10, war 10). Art's era 06 and era 07 strips (22 and 23) match a count without headings and story records (the build's block_words rule), where most chapters count every line. Scratch t781_convention.py prints the table
--check: PASS health / prose (validator 0 errors, emdash 0, semicolon 0, manuscript 23,739 w)
--check: PASS art / prose (validator 0 errors, emdash 0, semicolon 0, manuscript 33,097 w)
--check: PASS sports-play / prose (validator 0 errors, emdash 0, semicolon 0, manuscript 26,160 w)
--check: PASS city-building / prose (validator 0 errors, emdash 0, semicolon 0, manuscript 19,236 w)
--check: PASS food-farming / prose (validator 0 errors, emdash 0, semicolon 0, manuscript 16,157 w)
--check: PASS work-workers / prose and PASS slavery-freedom / prose (hand-offs only; chapters unchanged)
