# CHECKPOINT T-326 | health | prose | ONE writer, all 10 eras (part1, part2, part3)

STATUS: T-326 landed (director verified: PASS  health / prose)
VERIFY: python tools/project_state.py --check health --stage prose   (passes only after writer B)
BRIEF:  control/briefs/WRITER.md
MODEL:  opus
FILES:  manuscript/health/part1-before-1800.md (eras 1-5) · manuscript/health/part2-1800s.md (eras 6-7)
        · manuscript/health/part3-1900s-and-today.md (eras 8-10) · research/research-health.md (PATCH and
        SEARCHED, NOT FOUND entries only) · this checkpoint

NOW:    done
NEXT:   none. All 11 units done. PASS health / prose (19504w, 23 stories).

## Research state before writing (2026-09-29)

PASS  health / research
measured: stage=RESEARCHED eras=10/10 stories=23 (v23 c0 t0) verify_tags=0 bank=35059w outline=17200w manuscript=0w validator_errors=0

## Units

| # | unit | writer | state | landed (words, validator, --punct) |
|---|------|--------|-------|------------------------------------|
| 1 | era 01 before-1500 -> part1 | T-326 | done | file 817w, 0 errors, emdash=0 semicolon=0 |
| 2 | era 02 1500s -> part1 | T-326 | done | file 1876w, 0 errors, emdash=0 semicolon=0 |
| 3 | era 03 1600s -> part1 | T-326 | done | file 3865w, 0 errors, emdash=0 semicolon=0 |
| 4 | era 04 1700-1750 -> part1 | T-326 | done | file 5076w, 0 errors, emdash=0 semicolon=0 |
| 5 | era 05 1750-1800 -> part1 | T-326 | done | file 6825w, 0 errors, emdash=0 semicolon=0 |
| 6 | era 06 1800-1850 -> part2 | T-326 | done | file 1980w, 0 errors, emdash=0 semicolon=0 |
| 7 | era 07 1850-1900 -> part2 | T-326 | done | file 3439w, 0 errors, emdash=0 semicolon=0 |
| 8 | era 08 1900-1950 -> part3 | T-326 | done | file 3569w, 0 errors, emdash=0 semicolon=0 |
| 9 | era 09 1950-2000 -> part3 | T-326 | done | file 7937w, 0 errors, emdash=0 semicolon=0 |
| 10 | era 10 2000-today -> part3 | T-326 | done | file 9380w, 0 errors, emdash=0 semicolon=0 |
| 11 | final: self-review, --punct, validator, prose check | T-326 | done | PASS health / prose, 19504w, 3 files 0 errors, 0/0 |

## Gaps researched

<!-- era | question | PATCH (found) or SEARCHED, NOT FOUND | bank heading -->
- 06 | Sims and enslaved infants | PATCH (Kenny 2007 abstract) | "PATCH 2026-09-30 (T-326): Sims and enslaved infants with neonatal tetanus"
- 08 | Radium Girls 1928 settlement terms | PATCH (copied from work-workers bank, National Archives) | "PATCH 2026-09-30 (T-326): the dial painters' 1928 settlement"
- 09 | who took Norma Jean Serena's children | PATCH (NARA 2022) | "PATCH 2026-09-30 (T-326): who took Norma Jean Serena's children"
- 06 | method and deaths of the infant operations | SEARCHED, NOT FOUND | "SEARCHED, NOT FOUND 2026-09-30 (T-326): What exactly did Sims do to the enslaved infants"

## OPEN (should be rare)
- None. Round-2 candidate: the method and death count of Sims's operations on enslaved infants (only Wikipedia opened; Kenny 2007 full text not reached). Prose states only that he operated on them.

## Outline claims left out
- 0 outline claims dropped. Bank items not used: Agent Orange (war leads), Chicago 1995 heat wave (disasters), WTC illness deaths, EVALI, ADHD/obesity pointers, Joice Heth dissection 1836, Jefferson/Carey pointers already covered.

## Decisions and defects fixed
- Outline era 07 zoom "New York's new health board ordered": personification, written as "Officers of ... board".
- Outline era 06 "Smallpox is a virus that covers the body": disease equated with its cause, rewritten (and not re-defined, era 03 defines it).
- Outline era 05 zoom "a law that paid for sailors' medical care": law as actor, span names Adams, Congress and federal officials.
- Outline era 01 Tuberculosis/syphilis lines: no first names added beyond the bank (Vågene, Lallo, Steward etc. surnames only).
- Outline era 09 "Reporters exposed ... officials ended it": DuVal named from the Heller PATCH.
- Era 09 Norma Jean Serena added from the bank, with the jury's consent finding stated and the child-removal actors named (new PATCH).
- Jamestown: Earle's typhoid claim left out (search-summary only in bank).
- Self-review run on each file (era openers varied, institutions as actors repaired, one contrastive negation, unsourced inferences removed). Average sentence length 13.2 to 14.3 words, none over 35.

## TO PARK (for the director, burst runs only)

## Log
- 2026-09-30 era 01 landed: part1 at 817w, validator 0 errors, --punct emdash=0 semicolon=0. No new research.
- 2026-09-30 era 02 landed: part1 at 1876w, validator 0 errors, --punct 0/0. Story thomas-harriot. Used the bank's SEARCHED, NOT FOUND wording for de Soto. No new research.
- 2026-09-30 era 03 landed: part1 at 3865w, validator 0 errors, --punct 0/0. Stories samuel-fuller, tryntje-jonas. Jamestown: used Blanton (opened) only, left out Earle's typhoid claim (bank tags it search-summary only). No new research.
- 2026-09-30 era 04 landed: part1 at 5076w, validator 0 errors, --punct 0/0. Stories onesimus, zabdiel-boylston, elizabeth-phillips. Bomb date 14 Nov 1721 taken from the bank's parked news-communication pointer (Crawford, PMC3865953). No new research.
- 2026-09-30 era 05 landed: part1 at 6825w, validator 0 errors, --punct 0/0. Stories doctor-caesar, benjamin-rush, jones-and-allen. Self-review of part1 run (era openers varied, one contrastive negation and two unsourced inferences repaired). No new research.
- 2026-09-30 era 06 landed: part2 created, 1980w, validator 0 errors, --punct 0/0. Stories anarcha, elizabeth-blackwell. Research: 1 PATCH + 1 SEARCHED, NOT FOUND (Sims and enslaved infants, Kenny 2007). Awl method and death count left out (only Wikipedia opened).
- 2026-09-30 era 07 landed: part2 at 3439w, validator 0 errors, --punct 0/0. Stories clara-barton-health, hannah-ropes, susan-la-flesche-picotte. Mahoney kept in span (no story in outline). No new research. Self-review of part2 run.
- 2026-09-30 era 08 landed: part3 created, 3569w, validator 0 errors, --punct 0/0. Stories clara-maass, josie-mabel-brown, charles-pollard. PATCH: 1928 dial-painter settlement copied into the health bank from research-work-workers.md (National Archives). Guatemala written per the Commission correction (children and leprosy patients tested, not exposed). Tuskegee bodily course written from CDC and Brandt.
- 2026-09-30 era 09 landed: part3 at 7937w, validator 0 errors, --punct 0/0. Stories henrietta-lacks, jonas-salk, paul-alexander, relf-sisters, ryan-white. PATCH: who took Norma Jean Serena's children (NARA 2022 reopened). Serena case added from the bank (named doctors, caseworker, jury finding of consent stated).
- 2026-09-30 era 10 landed: part3 at 9380w, validator 0 errors, --punct 0/0. Story sandra-lindsay. Every figure carries its year and source. No new research.
- 2026-09-30 unit 11: validator 0 errors on all three files, --punct 0/0 on all three, PASS health / prose (manuscript=19504w, 23 stories verified).
