# CHECKPOINT T-332 | crime-justice | audit (calibration run 2) | part2-1800s.md, eras 6-7

STATUS: T-332f landed (director verified: PASS  crime-justice / prose)
BRIEF:  control/briefs/CHECKER.md (sharpened after run 1)
RUN:    T-332s sonnet checker -> control/audit/crime-justice/part2-findings-sonnet.md
        T-332o opus checker (same brief) -> control/audit/crime-justice/part2-findings-opus.md
        T-332f opus fixer (FIXER.md) judges both files, applies, adds "found by fixer" rows
RECORD: control/audit/CHECKER-CALIBRATION.md, run 2

NOW:    T-332f
NEXT:   director fills calibration run 2, then T-333 (government-politics part3)

## Log
- T-332s sonnet: 89 findings (12 B / 5 M / 72 m), 222k tokens, 17 tools, 8.4 min.
- T-332o opus: 79 findings (7 B / 17 M / 55 m), 195k tokens, 24 tools, 7.4 min.
- T-332f fixer: bank PATCH 2026-09-30 (T-332f) x3 added (Nat Turner dates and hanging, from slavery-freedom; Westinghouse and hatchet, from energy; draft riots end and toll plus "lynched", from war).
- T-332f era 06 (1800-1850) prose repairs applied. validate_grid --part: "1 chapters, 3 stories, 0 errors". --punct: emdash=0 semicolon=0. Findings tables not yet annotated.
- T-332f era 07 (1850-1900) prose repairs applied. validate_grid --part: "1 chapters, 3 stories, 0 errors". --punct: emdash=0 semicolon=0.
- T-332f findings annotated: sonnet 89 rows = 75 FIXED, 11 REJECTED, 3 NEEDS-RESEARCH (FIXED rows #69 and #82 carry a rejected part). Opus 79 rows = 77 FIXED, 1 REJECTED, 1 NEEDS-RESEARCH (#78) + #40 part. 6 "found by fixer" rows (80-85) and the calibration summary added to the opus file.
- T-332f GAPS for research round 2 (control/briefs/GAPS.md): (1) what the Eastern State iron gag did to the body; (2) what the doctors did with the Mankato bodies (dissection?); (3) what Hull House was, and when Julia Lathrop toured the jails; (4) what the "Lower Agency" was (Dakota trials); (5) the scope of Michigan's 1846 law (murder only? treason kept?), now written as "end the death penalty"; (6) a source describing King's ride out of Paris "on a rail".
- T-332f final: python tools/project_state.py --check crime-justice --stage prose -> PASS  crime-justice / prose.
