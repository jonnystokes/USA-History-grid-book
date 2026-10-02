# CHECKPOINT F5 | sports-play | step 5 fixer, whole chapter

STATUS: T-467 landed (director verified: PASS  sports-play / prose)
BRIEF:  control/briefs/FIXER.md (whole-chapter mode)
FILES:  manuscript/sports-play/part1|part2|part3 + control/audit/sports-play/part1|2|3-findings-sonnet.md
        + research/research-sports-play.md (PATCH entries only)

NOW:    done
NEXT:   none (director: commit)

## Units
| part | eras | state | FIXED / REJECTED / NEEDS-RESEARCH | words before -> after |
|---|---|---|---|---|
| part1 | 1-5 | done | 91 / 1 (partial, #35) / 0, +6 found by fixer | 6482 -> 7182 |
| part2 | 6-7 | done | 75 / 2 / 2, +3 found by fixer | 4979 -> 5493 |
| part3 | 8-10 | done | 110 / 1 / 0, +7 found by fixer | 11565 -> 12233 |

(word counts: wc -w + 1, matching the director's figures)

## NEEDS-RESEARCH
- part2 era 7, Boston sand garden: 1886 (Lee 1902) or 1885 (search summaries only)? Prose gives 1886 only.
- part2 era 6, Cato (1839): did Campbell free him (NKAA) or did he stay enslaved and buy his wife's freedom (search summary only)? Prose now gives only the NKAA account.
- (round 2, optional) Pittsfield 1791 bylaw: the fine (five shillings) and the day (5 Sept 1791) rest on search summaries (Protoball 403). Prose leaves both out.

## PATCHes added (research-sports-play.md, end of era 05)
- Austin Curtis: petition 5 Dec 1791, name change, horses hidden from British raiders, trainer, land, family (International Museum of the Horse citing Mooney 2014). Death date settled as 10 Dec 1807 (obituary "10th ult.", 5 Jan 1808) — AUDIT-QUEUE item done.
- Pittsfield bylaw, game list confirmed (SABR).
- Hawaii 1779 not yet a kingdom (kingdom from 1795).
- Continental Association = ban on British imports from 1 Dec 1774 (copied from research-styles.md).
- Era 06: Dancing Rabbit Creek negotiators, the choice put to the Choctaw, 15,000 moved / 2,500 dead; Lucy Larcom's job and later life (NPS).
- Era 07: International League after 1887 (Grant and Walker on old contracts, Walker to 1889, then none until Robinson 1946).
- Era 09: Cosell's $90,000 question (Retro Report transcript); Ali's all-white jury in Houston (Wikipedia, Clay v. United States).

## Log
- part1 era 1: 19 findings, all FIXED, 1 found by fixer (Bureau of American Ethnology unexplained). validate 0 errors, punct 0/0.
- part1 era 2: 7 FIXED, 1 fbf (lance). Checks clean.
- part1 era 3: 22 FIXED, 1 partly REJECTED (#35, six men is right), 2 fbf. Lawes oatmeal punishment and the full 1680 law added. Checks clean.
- part1 era 4: 14 FIXED. Checks clean.
- part1 era 5: 29 FIXED, 2 fbf, 4 PATCHes. Austin Curtis story expanded from the PATCH; 1807 kept. Checks clean. PART 1 DONE.
- part2 era 6: 41 FIXED, 1 REJECTED (#21), 1 NEEDS-RESEARCH (#24 Cato), 2 fbf, 2 PATCHes (Dancing Rabbit Creek, Larcom). "moved the Choctaw" now "forced". Checks clean.
- part2 era 7: 34 FIXED, 1 REJECTED (#64), 1 NEEDS-RESEARCH (#71), 1 fbf, 1 PATCH (International League after 1887, settles the Walker contradiction). Checks clean. PART 2 DONE.
- part3 era 8: 45 FIXED (incl. #76 for era 8), 1 REJECTED (#38), 4 fbf. British spellings fixed in all three parts. Checks clean.
- part3 era 9: 31 FIXED, 2 fbf, 1 PATCH (Cosell's $90,000 words, Ali's jury). Span openings varied (#76 done for eras 8-9). Checks clean.
- part3 era 10: 34 FIXED, 1 fbf. Nassar's crime now named with the bank's legal charge and USA Today's "raping" (DECISIONS #31). Checks clean. PART 3 DONE.
- Final: python tools/project_state.py --check sports-play --stage prose -> PASS (manuscript=23406w, 19 stories verified, emdash=0 semicolon=0, validator 0 errors).
