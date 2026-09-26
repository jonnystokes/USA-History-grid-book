# CHECKPOINT T-239 | immigration | bank patch + part 3 update | the small "who did it" gaps

STATUS: DONE (bank patched, part 3 updated, checks PASS)
VERIFY: python tools/project_state.py --check immigration --stage prose must still PASS, and
        --check immigration --stage research must still PASS.
FILES:  research/research-immigration.md (append) · manuscript/immigration/part3-1900s-and-today.md

## Units

| # | gap (from T-237c) | state | landed |
|---|------|-------|--------|
| 1 | Boat-people piracy: who the pirates were, as sources identify them | done | bank era 9 PATCH T-239 |
| 2 | Operation Wetback, 1955: the 88 sunstroke deaths. How they died (where deportees were left, the conditions) | done | bank era 9 PATCH T-239 |
| 3 | Reinaldo Arenas: who jailed him (named officials or the named body) | done | bank era 9 PATCH T-239 |
| 4 | Lost Boys of Sudan: who killed their parents and burned their villages, as sources state it | done | bank era 10 PATCH T-239 |
| 5 | Villegas González: the officer who shot him, or the agency and the outcome | done | bank era 10 PATCH T-239 |
| 6 | 2018 family separations: the DHS officials who carried out the policy (named) | done | bank era 10 PATCH T-239 |
| 7 | A primary source for "Donald Trump became president on January 20, 2025" | done | bank era 10 PATCH T-239 |

## Log
- 2026-09-26: gaps 1-7 appended to research/research-immigration.md as "PATCH 2026-09-26 (T-239)" (1-3 under era 9, 4-7 under era 10).
- 2026-09-26: part 3 prose updated: Operation Wetback sunstroke paragraph, Arenas story body, boat-people piracy paragraphs, new DHS-officials paragraph in the 2018 separations span, Trump swearing-in sentence, Villegas González lines plus follow-up paragraph, Lost Boys Who line and body. No marker, slug, status or key changed. tung-trinh not added.
- Checks: validate_grid --part 0 errors; --punct emdash=0 semicolon=0; --check immigration --stage prose PASS; --stage research PASS.
