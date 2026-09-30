# CHECKPOINT T-331 | native-nations | audit (calibration run 1) | part1-before-1800.md, eras 1-5

STATUS: T-331f landed (director verified: PASS  native-nations / prose)
BRIEF:  control/briefs/CHECKER.md
RUN:    T-331s sonnet checker -> control/audit/native-nations/part1-findings-sonnet.md
        T-331o opus checker (same brief) -> control/audit/native-nations/part1-findings-opus.md
        T-331f opus fixer (FIXER.md) judges both files, applies, adds "found by fixer" rows
RECORD: control/audit/CHECKER-CALIBRATION.md, run 1

NOW:    T-331f landed (fixer reports PASS; director to verify)
NEXT:   director fills CHECKER-CALIBRATION run 1, then T-332 (crime-justice part2)

## Log
- T-331s sonnet: 101 findings (23 B / 23 M / 55 m), 248k tokens, 27 tools, 10.2 min.
- T-331o opus: 85 findings (10 B / 25 M / 50 m), 211k tokens, 28 tools, 8.2 min.
- Director rulings given to T-331f (flagged by both checkers as director calls): (1) Acoma 1598: state the Pueblos'
  account plainly and attributed, "rape" defined in plain words, killers named per bank; "assaulted" alone is
  softening. Jon to review this ruling. (2) pointer-only facts from other banks: copy with source as a PATCH first,
  or reject as belonging to the other chapter. (3) missing stories: add only if bank and outline support them.
  (4) a nation named as a people may act; a state or institution may not. (5) hb-note editor notes are left alone.
- T-331f era 1 (before-1500) done: triads cut, unsourced claims cut or sourced (Celilo, Cahokia PATCH from ch03 bank),
  Pueblo defined, Great Law wording to bank, 1722/1744 repeats cut (told in era 4). validate: 1 chapters, 5 stories,
  0 errors. punct: emdash=0 semicolon=0. GAPS: "hundreds of nations" and "hundreds of languages" (no source in bank);
  location of the five nations' homeland (cut "East of the Great Lakes").
- T-331f era 2 (1500s) done: PATCH (Hymahi and Coronado from energy bank, 1572 reprisal from education bank,
  definitions); de Soto acts named; 1572 hangings and Alonso de Olmos added; Acoma: rape stated per ruling 1,
  Zaldívar's soldiers named as killers, prisoners ~500/507, elderly enslaved to Plains Apache, PBS slave-market
  view, fine and pardon dispute; accents restored; "sources" wording to records/accounts/named source.
  validate: 1 chapters, 5 stories, 0 errors. punct: emdash=0 semicolon=0. GAPS: what Coronado's expedition did
  to the Pueblo and Plains nations.
- T-331f era 3 (1600s) done: PATCH (Treviño 1675 and the runners from news-communication bank, Deer Island from
  education bank); New Mexico force vs coastal permission; "wars began" named; Tsenacommacah wording to bank;
  wampum repeat cut; Covenant defined; Mystic "surrounded" cut; Hartford victors named; Metacom war killers named;
  Deer Island paragraph; Bermuda fix; head "cut from his body"; Treviño arrests before the revolt; languages named;
  Po'pay story: towns to people, "as planned" corrected, runners Omtua and Catua named; horse close cut.
  catua-and-omtua block NOT added (belongs to news-communication, outline does not place it here).
  validate: 1 chapters, 5 stories, 0 errors. punct: emdash=0 semicolon=0. GAPS: who cut off Metacom's head; Beaver
  Wars nations and lands; raiders of the Pueblos 1680-92; encomienda tribute from a stronger source.
- T-331f era 4 (1700-1750) done: era zoom to bank (no "high price", Tuscarora dispossession named, Canasatego-only
  claim); raiders line to "records"; "walked" to "moved"; Spanish guns wording; Comanche triad cut, raid defined;
  unsourced council customs cut; union advice told once (story); July 4 coincidence cut. Also era 2 fixer finds:
  "inquiry" defined. validate: 1 chapters, 5 stories, 0 errors. punct: emdash=0 semicolon=0. GAPS: treaty-council
  customs (turns, clerks, printers) with a source; whom the Comanche raided.
- T-331f era 5 (1750-1800) done: PATCH (Fort Pitt from health bank, Conestoga from crime-justice bank, definitions);
  era zoom rewritten (empire defined, "in centuries", no "thirteen years", confederacy's fighters); repeats cut
  (second-empire line, largest-defeat x2); Fort Pitt and Conestoga paragraphs added in date order; Proclamation
  misstatement removed, proclamation and treaty law defined; Brant sentence split; Conotocaurius order clarified;
  Delaware name tied to the treaty; safe passage plain; gnomic lines cut; confederacy aim to bank; Greenville names
  Wayne and the United States. validate: 1 chapters, 5 stories, 0 errors. punct: emdash=0 semicolon=0.
  Process slip: one paragraph move was done with a short python heredoc instead of Edit (content checked after).
  GAPS: who built treaty law on the Proclamation.
- T-331f DONE: fixer column added to both findings files; 3 "found by fixer" rows and the calibration summary
  at the end of part1-findings-opus.md. Sonnet 101: 79 FIXED / 18 REJECTED / 4 NEEDS-RESEARCH. Opus 85: 78 / 5 / 2.
  Unique real defects 99: sonnet 78, opus 77, both 59, fixer only 3. Bank PATCHes (T-331f) in eras 1, 2, 3, 5 and
  the Acoma ruling note. Check: PASS  native-nations / prose (validator 0 errors, emdash=0 semicolon=0).
  GAPS list for round 2 (control/briefs/GAPS.md): hundreds of nations and languages before 1500; the five nations'
  homeland; Coronado's effect on the Pueblo and Plains nations; who cut off Metacom's head; Beaver Wars nations and
  lands; raiders of the Pueblos 1680-92; encomienda tribute (stronger source); treaty-council customs; whom the
  Comanche raided; who built treaty law on the Proclamation.
