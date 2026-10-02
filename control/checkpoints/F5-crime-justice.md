# CHECKPOINT F5 | crime-justice | step 5 fixer, whole chapter

STATUS: T-476 landed (director verified: PASS  crime-justice / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/crime-justice/part1|part2|part3 + control/audit/crime-justice/part1|2|3-findings-sonnet.md
        + research/research-crime-justice.md (PATCH entries only)

NOW:    T-476 done 2026-10-02
NEXT:   nothing (director: commit and close)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | DONE | 80 FIXED / 11 REJECTED / 0 NEEDS-RESEARCH, 9 found by fixer | 7805 -> 8762 (wc -w) |
| part2 | 6-7 | DONE (light pass #28-38) | 13 bare cites -> sentences, 7 search-side 'sources do not' -> 'No record names', 7 big words, 1 'many historians' | 6145 -> 6251 |
| part3 | 8-10 | DONE | 118 FIXED / 10 REJECTED / 0 NEEDS-RESEARCH, 4 found by fixer | 11161 -> 12089 (wc -w) |

## NEEDS-RESEARCH
- none. Every 'not in bank' gap was closed by a PATCH or the fact was cut or stated as the record gives it.
- Note for round 2 (not blocking): part 2 Myrtle Vance 'sexually attacked' stays until the newspapers' own word is found (#31 'rape' only where the record says rape).

## PATCHes added (research/research-crime-justice.md)
- era 2: "Acoma, the harms native-nations states" (copied from native-nations bank, #36)
- era 3: "Ratcliffe's sentence was carried out, and Chickatabut paid" (Winthrop's journal); "the Quakers' ears, 1658, reconciled with the religion bank"; "Rebecca Nurse's excommunication, and the 1957 apology"
- era 4: "Cuffee's owner was Adolph Philipse, and the jury's verdict" (corrects the bank)
- era 5: "To Counterfeit is Death" (copied from money bank); "the soldiers' branding, 14 December 1770, confirmed" (Boston Gazette via J. L. Bell; Sheriff Stephen Greenleaf); "Patrick Lyon, details from Avery's page"
- era 8: "era 8 facts copied from other banks or confirmed" (Tulsa camps from rights-movements #36; Teapot Dome bribe; Prohibition dates; Brown v. Mississippi charge; Scottsboro at Paint Rock)
- era 9: "era 9 details confirmed (Till's store, Diallo's death, Michael Stewart)"
- era 10: "era 10 ages, deaths and names confirmed" (Brown, Garner, Taylor, Floyd, Nichols, Rice, Menendez, Danziger vacatur, Bourgeois, Robb Elementary, Proclamation 10887)

## Log
- 2026-10-02 T-476 part1 era 1: rows 1-12 judged (10 FIXED, 2 REJECTED). Validator 0 errors, punct 0/0.
- 2026-10-02 T-476 part1 era 2: rows 13-22 judged (8 FIXED, 2 REJECTED) + F1 found by fixer. Acoma: "serve" -> slave (#34), soldiers killed men, women and children, elders enslaved to Plains Apache (#36). Validator 0 errors, punct 0/0.
- 2026-10-02 T-476 part1 era 3: rows 23-50 judged (26 FIXED, 2 REJECTED) + F2-F5 found by fixer (bare parenthesis cites #37, Tarter's treason, Tobias's pledge). AUDIT-QUEUE Quaker ear item reconciled. Validator 0 errors, punct 0/0.
- 2026-10-02 T-476 part1 era 4: rows 51-68 judged (17 FIXED, 1 REJECTED) + F6 found by fixer. Bank error fixed: Cuffee's owner was Adolph Philipse. Validator 0 errors, punct 0/0.
- 2026-10-02 T-476 part1 era 5: rows 69-91 judged (18 FIXED, 5 REJECTED) + F7-F9. PART 1 DONE: 80 FIXED, 11 REJECTED, 0 NEEDS-RESEARCH, F1-F9 found by fixer. Words 7805 -> 8762. Validator 0 errors, punct 0/0.
- 2026-10-02 T-476 part2 light pass eras 6-7 done (summary appended to part2-findings-sonnet.md). Validator 0 errors, punct 0/0.
- 2026-10-02 T-476 part3 era 8: rows 1-45 and 128 judged (46 FIXED, 0 REJECTED) + F1-F2. Springfield 'driven out', Knox boiling vat, bare cites, Tulsa plain words. Validator 0 errors, punct 0/0.
- 2026-10-02 T-476 part3 era 9: rows 46-80 judged (33 FIXED, 2 REJECTED). Michael Stewart's death now told plainly (beaten unconscious, hogtied). Validator 0 errors, punct 0/0.
- 2026-10-02 T-476 part3 era 10: rows 81-127 judged (39 FIXED, 8 REJECTED with research) + F3-F4. PART 3 DONE: 118 FIXED, 10 REJECTED, 0 NEEDS-RESEARCH, F1-F4. Words 11161 -> 12089.
- 2026-10-02 T-476 final: `python tools/project_state.py --check crime-justice --stage prose` PASS (manuscript=25703w, 13 stories verified, emdash=0 semicolon=0, validator 0 errors on all three parts).
