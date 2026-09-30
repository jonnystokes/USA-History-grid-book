# WORKLOG — append-only ledger of attempted work

**Append, never edit history.** One entry per task, written **before** the work
starts and closed **after** its check runs. A resuming session reads the tail of
this file, runs the verify command it names, and knows the truth in one command.

Read `control/RESUME.md` first if you have not this session.

## Entry format — copy this

```
### <YYYY-MM-DD HH:MM> | <task-id> | <what>
STATUS: IN-FLIGHT | DONE | FAILED | ABANDONED
VERIFY: python tools/project_state.py --check <slug> --stage <research|patch|prose>
EXPECT: <the artifacts that must exist when this is done>
NEXT:   <the single next action if this is interrupted>
RESULT: <paste the check's PASS/FAIL + measured line when closing>
```

Rules:
- `STATUS: IN-FLIGHT` is written **before** dispatching the sub-agent, not after.
- Close with the **pasted output** of the VERIFY command. Never with a summary of
  what an agent said it did.
- If the check fails, close as `FAILED` and open a fresh entry for the retry. Do
  not silently reuse an entry — the history of what was tried is the point.
- Interrupted with no close? That is fine and expected. The next session runs
  VERIFY and finds out.

---

### 2026-09-05 23:55 | T-000 | Establish resumable-state discipline
STATUS: DONE
VERIFY: `python tools/project_state.py` runs and prints 35 chapters; `control/RESUME.md`, `control/WORKLOG.md`, `CLAUDE.md` exist
EXPECT: tools/project_state.py · control/RESUME.md · control/WORKLOG.md · CLAUDE.md
NEXT:   n/a
RESULT: PASS — script prints 35 chapters | PARTIAL 1 | RESEARCHED* 19 | SEED 15;
        534 stories (350 verified, 72 candidate, 112 target); outline 111,729w;
        banks 148,282w; manuscript 0w. Four chapters flagged verified-but-unsourced:
        art-music, big-business, exploration, holidays.

---

## First measured baseline (2026-09-05)

Recorded here because it is the first time these numbers were derived rather than
asserted. Earlier prose docs disagree with this and are wrong where they do.

- **No chapter currently passes the research bar.** Even the three called
  "prose-ready" fail: `native-nations` has a `before-1500` era marked `full` with
  no story in it. That is a real gap, not a script quirk.
- **112 `target` + 72 `candidate` stories** across the book — the honest remaining
  research load, and a much better measure than "15 chapters left".
- **Four chapters** carry stories tagged `verified` whose text still says
  `[VERIFY]`: art-music (known), plus **big-business, exploration, holidays**
  (new — the earlier audits missed these two categories).
- `big-business` bank is 409 words against a 6,773-word outline — its `hb-note`
  claims a full bank that does not exist.
- `exploration` is `PARTIAL`, not `RESEARCHED`: 9 candidate stories remain.

## Open tasks, unstarted (see control/ROADMAP.md for the full plan)

| id | task | verify |
|---|---|---|
| T-001 | Fix the 4 chapters with verified-but-unsourced stories | `project_state.py` prints no `!` flags |
| T-002 | Make `tools/validate_grid.js` exit non-zero on errors | `node tools/validate_grid.js <bad file>; echo $?` prints non-zero |
| T-003 | Answer the 12 gating decisions (6 tone, 6 structural) | `control/hard-subjects-policy.md` exists; ROADMAP §1b answered in workspace files |
| T-004 | Research `america-world` (no bank at all; owns territories) | `--check america-world --stage research` |

---

### 2026-09-06 00:20 | T-002 | Make validate_grid.js exit non-zero on errors
STATUS: DONE
VERIFY: `node tools/validate_grid.js <file with errors>; echo $?` prints non-zero; clean file still prints 0
EXPECT: tools/validate_grid.js exits with the error count (capped) instead of always 0
NEXT:   n/a
RESULT: PASS - clean file exit=0; deliberately broken file exit=3 (3 errors); all 35
        outlines together exit=0. Counts errors across all files, capped at 100.

### 2026-09-06 00:20 | T-001 | Clear verified-but-unsourced story tags in 4 chapters
STATUS: DONE
VERIFY: python tools/project_state.py  (prints no `!` flags; art-music, big-business, exploration, holidays clean)
EXPECT: each falsely-verified story either demoted to target/candidate, or its [VERIFY] resolved from the bank
NEXT:   n/a
RESULT: PASS - project_state.py prints no `!` flags. verified 350->348, candidate 72->74.
        Judged individually rather than batch-demoted:
        - art-music/phillis-wheatley: unsourced one-liner -> status="candidate"
        - holidays/anna-jarvis: unsourced one-liner -> status="candidate"
        - exploration/jim-beckwourth: facts sourced in bank; the tag was an ERA-PLACEMENT
          question -> moved to workspace/exploration.md [VERIFY] queue, kept verified
        - big-business/john-w-holway: facts sourced inline; the tag was a prose-time
          quoting caveat -> moved to workspace/big-business.md [VERIFY] queue, kept verified
        Grid revalidated (exit 0) and BOOK-OUTLINE.md rebuilt.
        NOTE: big-business's bank is still 409w against a 6,773w outline - separate task.

### 2026-09-06 00:35 | T-003a | Gather context for the 12 gating decisions
STATUS: DONE
VERIFY: `control/DECISIONS.md` exists and lists all 12 with context + a recommendation each
EXPECT: control/DECISIONS.md (the brief Jon answers in one sitting)
NEXT:   awaiting Jon's answers -> then T-003b writes control/hard-subjects-policy.md and
        records the structural rulings in workspace/<slug>.md + chapter-registry.md
RESULT: PASS - control/DECISIONS.md exists, all 12 items with context and a
        recommendation each. KEY REFRAME: the six tone questions are not "whether" -
        AGENT-BRIEF.md:70 and project-notes.md:124 already rule that hard truths go in,
        and project-notes.md:118 deleted the old send-it-elsewhere rule. The style guide
        has no age rule but forbids both softening (hedges) and sensationalizing
        (adjectives, staged scenes). So all six collapse to one question: is
        outlines/native-nations.md:183 the floor or the ceiling. Also found: Ruby Bridges
        is double-booked (education.md:243 candidate + rights-movements must-appear), and
        the Ch12+Ch13 merge was already executed AND researched, so item 11 is a
        bank-writing task, not a decision.

### 2026-09-06 01:10 | T-003b | Record Jon's 12 rulings + restructure to 37 chapters
STATUS: DONE (interrupted mid-run by a usage limit; recovered 2026-09-06 10:0x)
VERIFY: python tools/project_state.py shows 37 chapters incl. art, music, storytelling-evolution;
        node tools/validate_grid.js outlines/*.md exits 0; control/hard-subjects-policy.md exists
EXPECT: outlines/{art,music,storytelling-evolution}.md + workspaces; control/hard-subjects-policy.md;
        chapter-registry/STATUS/ROADMAP/AGENT-BRIEF updated; art-music.md retired
NEXT:   n/a
RESULT: PASS - python tools/project_state.py prints 37 chapters; node tools/validate_grid.js
        outlines/*.md exits 0; BOOK-OUTLINE rebuilt at 37 chapters, 596 stories, 0 errors;
        control/hard-subjects-policy.md exists (151 lines, 7 sections).

        *** THE LESSON OF THIS ENTRY - read it before redoing interrupted work ***
        The usage limit killed 3 of 7 workflow agents. The workflow reported them as
        FAILED. But two of the three had already WRITTEN THEIR FILES before dying:
        outlines/art.md (335 lines), outlines/music.md (348), and
        outlines/storytelling-evolution.md (308) were all on disk, all validating clean,
        all with zero false status="verified". Only the reporting step was lost.
        A resuming session that trusted the FAILED label would have thrown away three
        good chapters and spent ~800k tokens rebuilding them.
        MEASURE FIRST, ALWAYS. "Agent failed" is a claim about an agent, not about the
        repository. Run project_state.py and look at the disk before redoing anything.

        Work completed under this task:
        - 35 -> 37 chapters: art (32), music (33), storytelling-evolution (34);
          styles/sports-play/holidays renumbered 35/36/37, slugs unchanged.
        - art-music retired to _reference/retired-art-music-2026-09-06/ with a README.
        - ~20 cross-references repointed; 5 parked-research notes split 2-3 ways
          (Berlin->music, Capra->storytelling-evolution, Ingalls books->art + TV->
          storytelling-evolution, Gladstone->storytelling-evolution, Zitkala-Sa's
          essays->art and her violin/opera->music).
        - control/hard-subjects-policy.md written; its rule 5 ("close on what people
          did") qualified with "where the record shows one" plus an explicit guard,
          because as written it could push an agent toward inventing a redemptive
          ending where the record has none - which ruling C forbids.
        - Rulings propagated to CLAUDE.md, RESUME.md, AGENT-BRIEF, grid-markers,
          project-notes, chapter-registry, STATUS, ROADMAP.
        - Dolly Parton (d. 25 Aug 2026, Rep. Burchett's statement) placed in music as
          status="candidate" on one source, with a research-target list.

### 2026-09-06 10:05 | T-003c | Verify the 4 chapters whose adversarial check died
STATUS: DONE
VERIFY: workflow wf_21f9fc9c-0a2 verdicts; then python tools/project_state.py shows no
        `!` flags and node tools/validate_grid.js outlines/*.md exits 0
EXPECT: workspace/{art,music,storytelling-evolution}.md created; adversarial verdicts on
        art, music, storytelling-evolution, sports-play (invented content, false verified,
        softening, padded eras)
NEXT:   n/a
RESULT: PASS - 7/7 agents completed. workspace/{art,music,storytelling-evolution}.md created.
        37 chapters, 596 stories, 0 validator errors, no `!` flags, BOOK-OUTLINE rebuilt.
        Verdicts: music PASSES. art, storytelling-evolution, sports-play FAIL on content
        defects (format was clean everywhere; 0 false status="verified" in any chapter).

        THE ADVERSARIAL PASS PAID FOR ITSELF - it found INVENTED CONTENT in
        storytelling-evolution, which is this project's worst defect class:
        - a FABRICATED source dispute ("sources give his death year as 1865 and 1867")
          about Ira Aldridge. No such dispute exists; he died 7 Aug 1867. The disputed
          field is his BIRTH year. An invented disagreement is as bad as an invented
          fact, and it was written in the house style so it read as careful.
        - "won an Academy Award in 1957 under a name that did not exist" - false. Robert
          Rich was a real person, a relative of one of the producers.
        - an untagged studio count ("Seven companies") where the standard count is eight.
        - a rendered record line claiming a performer personally struck, where only her
          union membership is supported.
        All four corrected. Also fixed: an "[Editorial: ...]" note written INSIDE a
        rendered era cell - only [VERIFY...] becomes a badge, so that instruction would
        have printed as body text to a child reader. Moved to the workspace file.

        FIXED BY THE VERIFIERS THEMSELVES (softening, restored from material already in
        the files): "Native workers under mission rule" -> "Native hands", with the
        labour system now required to be named; "museums began answering questions about
        how they got the things they own" -> the 1990 federal law that made them;
        "Africans brought to Virginia" -> "taken to Virginia by force ... and sold";
        "a color line down the middle" -> "Black players shut out of the white major
        leagues until 1947"; "leagues the majors refused to face" -> "the separate
        leagues Black players were confined to".

        MY OWN BUG, caught by a verifier: the sed that repointed art-music references
        mangled chapter-registry.md row 35 into "fine art (`artusic`)". Fixed.

        ~25 further findings need research and are queued in the four workspace files
        under "Verifier findings - 2026-09-06" (Ali's conviction, Smith and Carlos by
        name, CTE specifics, the 1900 census child-labour figure, the Pueblo religious
        leaders hanged in 1675, the African Grove raid, Smibert's and Chicano Park's
        dates, Irving Berlin missing from music).

---

## PHASE 4 BEGINS — prose. Jon: "Commence history book writing." (2026-09-06)

### 2026-09-06 | T-100 | native-nations prose, part 1 (before 1800) — THE VOICE SETTER
STATUS: DONE
VERIFY: node tools/validate_grid.js on the concatenated chapter (single part files WILL
        report missing eras until all three exist - that is expected, not a defect);
        then python tools/project_state.py --check native-nations --stage prose
EXPECT: manuscript/native-nations/part1-before-1800.md - eras before-1500, 1500s, 1600s,
        1700-1750, 1750-1800, mode="prose", progress="written", all stories verified
NEXT:   n/a
RESULT: PASS - manuscript/native-nations/part1-before-1800.md, 4,080 words of prose, 266 lines.
        5 eras (before-1500 .. 1750-1800), all progress="written", mode="prose", 5 stories all
        status="verified" (paquiquineo, metacom-native-nations, pope, canasatego, little-turtle),
        21 zoom blocks all closed, 0 [VERIFY] tags. Validator: 1 error, the expected
        "missing 5 eras" part-file message, nothing else.
        THE FIRST PROSE IN THE BOOK. Reviewed by the director, not just accepted: it defines
        nation/confederacy/tribute/obsidian/wampum at first use; states the pre-contact
        population dispute with named scholars (Ubelaker ~1.85m vs Dobyns ~18m) and refuses to
        settle it; attributes the Great Law to Haudenosaunee tradition rather than asserting it
        as record; Po'pay's block cites "By Pueblo accounts" for the knotted cords and ends on
        the Statuary Hall statue - a real fact, not a manufactured uplift.
        HONEST OMISSIONS the agent reported rather than writing around silently: era-4
        "dependence on trade goods grew" (nothing in the bank); the Condolence ceremony (bank
        never defines it); the causes of King Philip's War (not in the bank).
        *** ACOMA 1599 LEFT OUT ENTIRELY *** - the parked material carries [VERIFY] on the
        death toll, the trials and the sentences. The agent judged that naming the attack while
        dropping what was done to people would be exactly the compression the policy forbids.
        That is the right call, but the resolution is to VERIFY it, not to omit it permanently.
        Queued as T-102.

### 2026-09-06 | T-101 | america-world research (territories thread, no bank at all)
STATUS: FAILED - killed by the usage limit before writing anything
VERIFY: python tools/project_state.py --check america-world --stage research
EXPECT: rewritten outlines/america-world.md + new research/research-america-world.md
NEXT:   REDO from scratch - this one genuinely produced nothing
RESULT: FAIL - measured after the kill: america-world still stage=SEED, 6 stories, 3 target,
        bank_words=0, research/research-america-world.md does not exist. The agent died while
        still reading the control files. Unlike T-103/T-104, there is nothing to salvage.

### 2026-09-06 | T-102 | Verify the Acoma 1599 record so the chapter can carry it
STATUS: OPEN (not started)
VERIFY: research/research-native-nations.md has the Acoma death toll, the trials and the
        sentences sourced and [VERIFY]-free; then the 1500s era of the prose carries it
EXPECT: the massacre and the sentences stated plainly, or an explicit sourced statement that
        the figures are disputed and by whom
NEXT:   dispatch one research agent on this single question before native-nations is called DONE
RESULT:

### 2026-09-06 | T-103 | native-nations prose, part 2 (1800s)
STATUS: DONE (agent killed by the usage limit AFTER writing its file)
VERIFY: node tools/validate_grid.js on the concatenated chapter once all three parts exist
EXPECT: manuscript/native-nations/part2-1800s.md - eras 1800-1850, 1850-1900
NEXT:   n/a
RESULT: PASS - file written (24,128 bytes). No self-report: the agent was killed at the
        moment it said "I have everything I need. Writing the file now." NOT YET
        INDEPENDENTLY VERIFIED for content - see T-105.

### 2026-09-06 | T-104 | native-nations prose, part 3 (1900s and today)
STATUS: DONE (agent killed by the usage limit AFTER writing its file)
VERIFY: node tools/validate_grid.js on the concatenated chapter once all three parts exist
EXPECT: manuscript/native-nations/part3-1900s-and-today.md - eras 1900-1950, 1950-2000, 2000-today
NEXT:   n/a
RESULT: PASS - file written (30,649 bytes). No self-report (killed mid-report).
        Boarding-school passage confirmed present at the floor standard: the 973 children,
        the 74 burial sites, "soap for speaking Navajo". NOT YET INDEPENDENTLY VERIFIED - T-105.

        *** CHAPTER 02 native-nations IS COMPLETE - THE BOOK'S FIRST FINISHED CHAPTER ***
        Merged and validated as the viewer reads it: 1 chapter, 21 stories, 0 errors.
        10/10 eras progress="written", 21/21 stories status="verified", 0 [VERIFY] tags,
        12,401 words of prose.

### 2026-09-07 | T-105 | Independently verify native-nations prose (parts 2 and 3)
STATUS: DONE
VERIFY: an adversarial verifier per part reports 0 invented content, 0 softening, and the
        boarding-school passage at or above the floor
EXPECT: parts 2 and 3 checked the way art/music/storytelling-evolution were - those checks
        found FABRICATED content that read as careful scholarship
NEXT:   n/a
RESULT: PASS both parts. **NO FABRICATED CONTENT IN EITHER.** Every name, date, number,
        quote, law, case, treaty and film traces to the research bank. All six "sources
        disagree" statements in part 2 are genuine and in the bank - no invented dispute of
        the kind the culture-chapter check caught.
        Boarding-school floor met element by element: Pratt's words (in part 2, where the
        1879 founding belongs), the documented punishments, 417 schools / 37 states /
        1819-1969, at least 973 children dead, at least 74 burial sites at 65 schools,
        the report's own statement that the true number is higher, and the close on
        survival. Zero evaluative adjectives; no staged scenes.
        FIXED (agency restored, the book's core ruling in action):
        - Sand Creek: "About 230 people were killed" -> "The soldiers killed about 230 people"
        - Wounded Knee: "when the shooting began" -> "when the soldiers opened fire"
        - Boarding-school arrival: four agentless passives -> "The school cut the child's
          hair. It took the child's clothes... It forbade the child to speak the language
          of home."
        - Osage era zoom: "a law... was used to take that money and to kill more than sixty
          of the people who owned it" - a law kills nobody, and this hid the killers. Now
          names the 1921 guardianship law, the white guardians appointed by local courts,
          and that guardians and husbands stole (bank lines 200-201).
        - A banned balanced-clause figure in the Osceola block; an invented "30-odd years
          into a life the records do not date precisely"; a date error (twenty years -> 
          eleven, 1821-1832); "the land was not returned" contradicting the bank's own note
          that the IRA funded land recovery; "most of Tulsa" overstating the sources' "much".
        BANK GAPS queued in workspace/native-nations.md - the largest: **the 1970s IHS
        sterilizations of Native women are absent from the research bank entirely**, so the
        1950-2000 era cannot carry them. Needs a director call.

## PAUSE PROTOCOL (Jon, 2026-09-06) - recorded here because it cost a batch

When Jon says "pause": stop dispatching AND message every running sub-agent to stop
cleanly. He says it to prevent a hard crash, not to pause the conversation. On
2026-09-06 he said it with a few percent of the usage window left; three agents were
left running and all three were killed by the rate limiter minutes later - two of them
at the exact moment they were writing their files. Recorded in CLAUDE.md, control/RESUME.md
and agent memory.

### 2026-09-07 | T-101b | america-world research - REDO
STATUS: FAILED AGAIN - killed by the usage limit, second time, again before writing anything
VERIFY: python tools/project_state.py --check america-world --stage research
EXPECT: rewritten outlines/america-world.md + new research/research-america-world.md
NEXT:   see T-101c - the task is being SPLIT because it is too big for one agent per window
RESULT: FAIL - measured: still stage=SEED, 6 stories, bank_words=0, no research file. The agent
        died at "Now I have the full picture. Let me load the web tools and begin verification"
        - i.e. it had spent its whole budget reading and had not yet written a line.
        LESSON: this chapter is 10 eras from scratch PLUS a full research bank, and it has now
        died twice at the same point. That is a task-size problem, not bad luck. Splitting it.

### 2026-09-07 | T-102 | Verify the Acoma 1599 record so the chapter can carry it
STATUS: DONE
VERIFY: research/research-native-nations.md carries the Acoma death toll, trials and sentences
        sourced and [VERIFY]-free, OR an explicit sourced statement of what is disputed and by whom
EXPECT: the 1500s era of native-nations can then carry the attack and what was done to people
NEXT:   n/a
RESULT: PASS - research/research-native-nations.md lines 335-461 now carry a fully sourced
        Acoma section (file 368 -> 492 lines, nothing else touched). The massacre is now IN
        THE BOOK: a new span in the 1500s era of part1, and a matching span in the outline.
        Chapter is 12,822 words, 21 stories, 0 errors, 0 [VERIFY].
        WHAT THE RESEARCH SETTLED: sequence (Acoma had already given the act of obedience;
        Dec 1598 Juan de Zaldivar's party demanded food and was killed with 11-14 men; Onate's
        inquiry and the friars' declaration of a just war; Jan 1599 ~70 soldiers stormed and
        burned the pueblo); the sentence of Feb 12 1599 in full; Onate's own conviction on 12
        of 30 charges, banishment and fine.
        WHAT REMAINS GENUINELY DISPUTED, and is written into the book AS a dispute:
        - Death toll: ~300 (NM State Historian) / ~600 (Murrin) / 600-800 (Liebmann) / ~800
          (the All Pueblo Council of Governors' own figure) / ~1,500 (NPS). No count was ever
          made; the only eyewitness account is Villagra's 1610 epic poem. The book gives the
          range and says there is no agreement.
        - Whether the foot-cutting was carried out: Marc Simmons wrote that it was, then
          doubted it; John Kessell doubts it - no one-footed Acoma man appears in the records.
          The book states that the ORDER is in the record, that Onate was convicted for
          Acoma, and that the carrying-out is disputed by name.
        - The widely repeated figure of 24 men is in NYT 1998, AP and NPR but the agent could
          not trace it to any document, so the book does not use it.
        - The "toes not feet" reading rests on an Albuquerque Journal op-ed and letters, not
          scholarship. Not used.

### 2026-09-07 | T-101c | america-world research, SPLIT IN TWO (eras 1-5 and 6-10)
STATUS: DONE — the split worked; both halves landed on the first attempt
VERIFY: after assembly, python tools/project_state.py --check america-world --stage research
EXPECT: workspace/_staging-america-world-eras1-5.md + _eras6-10.md (outline fragments, hb-time
        blocks only, no hb-chapter line) and research/_staging-bank-america-world-eras1-5.md +
        _eras6-10.md; then the director assembles outlines/america-world.md and
        research/research-america-world.md and validates
NEXT:   two candidates remain -> ROADMAP Phase 3 patch, recorded in workspace/america-world.md
RESULT: PARTIAL PASS - the chapter is transformed but the gate correctly still FAILS.
        Was: the book's worst chapter - 2/10 eras, 6 stories, 4 eras empty, NO BANK AT ALL.
        Now: 10/10 eras, 13 stories (11 verified, 2 candidate, 0 target), bank 15,486w against
        an 8,931w outline, 0 [VERIFY] tags, validator 0 errors.
        --check FAILS only on the two honest candidates (james-leander-cathcart, whose birth
        year sources give as both 1765 and 1767; emilio-aguinaldo-america-world). That is the
        gate doing its job - neither was padded into a false "verified".
        THE TERRITORIES BEAT NOW RUNS IN EVERY ERA FROM 1850, as Jon ruled: the Guano Islands
        Act 1856; Alaska's Article III excluding "uncivilized native tribes"; the overthrow and
        the 21,269-signature Kue Petitions with the four named delegates; the Insular Cases in
        words a child can follow, stated as still law in 2026 and still contested; citizenship
        island by island; Guam occupied while its people were not citizens; Hawaii's statehood
        ballot with no independence option; Jayuya bombed; PROMESA; Vaello Madero; Fitisemanu.
        All three of the seed's `target` slots became real named people. No composites.
        THE SPLIT IS THE LESSON: two single-agent attempts died having written nothing. Split
        in half, both halves landed first try. For a from-scratch chapter, halve it.
        BOOK-OUTLINE rebuilt: 37 chapters, 603 stories, 0 errors, 171,093 words.

### 2026-09-07 | T-106 | Style/policy hardening after Jon caught a personification in MY prose
STATUS: DONE
VERIFY: grep the finished prose for institutions acting; control/hard-subjects-policy.md has
        section 3b; every writer-facing doc names both binding guides
EXPECT: personification fixed in the manuscript; clinical-word rule written; one-agent-at-a-time
RESULT: PASS. Jon caught "the law's actual job" in a message to him - personification, style
        guide 1.1, the FIRST rule in the guide. He asked how well the guide covers it and how
        well the writing agents follow it.
        FINDING: the guide covers it well (1.1 is the opening rule, with three worked examples
        and an explicit "nations are not characters"). Compliance in the finished prose is high
        - 12,822 words yielded only three instances. But one of the three WAS INTRODUCED BY MY
        OWN REPAIR: a verifier flagged agentless passives at the boarding-school arrival, I
        fixed them to "The school cut the child's hair", and an institution acting is still 1.1.
        Now reads "Staff cut the child's hair. They took the child's clothes..."
        Also fixed: "The treaty recognized/asked/raised" -> the United States and the
        negotiators; "The Act set/gave" -> Congress.
        THE LESSON, now written into the policy: 1.1 is most often broken WHILE REPAIRING
        SOMETHING ELSE. Check your fixes, not just the first draft.
        NEW: hard-subjects-policy.md section 3b - WHY we refuse to soften, in Jon's own words
        (understanding plus feeling is what makes an atrocity remembered and refused), and the
        CLINICAL-WORD RULE: sterilization, lobotomy, flogging and the like are containers a
        child cannot see inside. Say what it is, what it did to the person, and by what method.
        Honest and non-sexual, doctor's-report plain, never lurid, never guessed.
        Self-check extended from 6 questions to 8.
        Both binding guides now named in: AGENT-BRIEF read-first list, RESUME standard brief,
        templates/chapter-template.md, CLAUDE.md.
        Dispatch rule changed to ONE AGENT AT A TIME everywhere.

### 2026-09-07 | T-107 | Hands-on investigation of this session's agent mechanics
STATUS: DONE
VERIFY: control/AGENT-MECHANICS.md exists; python tools/salvage_agent.py --list runs;
        _reference/salvaged/ holds recovered digests of the two dead america-world agents
EXPECT: real tested findings written into the docs every future session reads
RESULT: PASS. Ran an investigation plan supplied by Jon from external research. Findings:

        *** THE BIG ONE: I WAS WRONG THAT DEAD AGENTS ARE A TOTAL LOSS ***
        Every sub-agent writes a full transcript to ~/.claude/projects/<key>/<sessionId>/
        subagents/agent-<id>.jsonl, which SURVIVES the agent's death and contains every
        page it fetched. The two america-world agents I declared destroyed held 103 and 99
        web fetches across 623 and 740 distinct URLs - congress.gov 85, history.state.gov
        46, loc.gov 41, archives.gov 27. I wrote that off and paid for it TWICE more.
        Built and tested tools/salvage_agent.py; both dead agents digested to 358 KB of
        usable research, carrying Downes v. Bidwell and the unincorporated-territory
        doctrine. Saved to _reference/salvaged/.
        NEW STANDING RULE: salvage first, re-dispatch second.

        CONFIRMED ABSENT: SendMessage. Direct name-select of 7 tools returned 6
        (ListAgents, TaskStop, Workflow, Agent, Artifact, TaskOutput); SendMessage did
        not. So NO sub-agent is resumable here by any route - despite ListAgents' own
        description saying "agents you can SendMessage to" and the Agent tool saying to
        use it for continuation. The docs describe a tool this build lacks.
        Also absent: Agent has no `name` and no `maxTurns` parameter, so "name your agents
        to address them later" and a controlled partial-completion test are both
        impossible here.

        MEASURED: a trivial probe agent (one wc -l) cost 50,750 tokens. That is the floor
        price of any spawn. ListAgents lists COMPLETED agents but drops KILLED ones - so
        even with SendMessage, the agents you most want back would be unaddressable.
        All agents ran at spawnDepth 1; no project or user agent definitions exist.

        NOT TESTABLE HERE: hard-kill/power-loss recovery (would end this session);
        usage-limit auto-continue behaviour (autoContinueAtUsageLimit unset; the Desktop
        checkbox is a separate control not readable from here) - and what Desktop sends on
        reset MATTERS, because if it replays the last user message, a message that
        dispatched several agents would re-dispatch them all into the fresh window;
        kill-mode asymmetry (moot without resume); exact version (claude CLI not on PATH,
        no version field in ~/.claude.json).

        PROPAGATED TO: control/AGENT-MECHANICS.md (new, full write-up), CLAUDE.md
        (auto-loaded), control/RESUME.md (salvage-first procedure), control/AGENT-BRIEF.md
        (WRITE EARLY - your work only survives if you have written it), README.md, and
        agent memory (dead-subagents-are-salvageable).

### 2026-09-07 | T-108 | Second-round agent mechanics tests (external plan, round 2)
STATUS: DONE
VERIFY: control/AGENT-MECHANICS.md sections 2b/2c/4b/6b/6c; ~/.claude/agent-archive/salvage-log.tsv
RESULT: PASS. Version SETTLED: 2.1.260, entrypoint claude-desktop, from the `version` field
        on transcript records. Corrections accepted: maxTurns is agent-definition FRONTMATTER,
        not a call parameter - my "impossible by schema" was wrong; and the missing `name`
        plus missing SendMessage are ONE subsystem, so there is no flag to hunt for.
        NEW TESTS: custom agent definitions did NOT register in either scope (project or
        user) - but neither directory existed at session start, so this cannot distinguish
        broken-hot-reload from needs-restart. Files are in place; next session settles it in
        one call by spawning subagent_type "probe". `fork` is NOT an accepted subagent_type
        despite the Agent tool description referencing it - second doc/build mismatch.
        *** AUTOMATIC SALVAGE IS LIVE *** SubagentStop hook -> salvage-subagent.py copies
        every transcript to ~/.claude/agent-archive/ on stop. Tested: baseline 13 archived,
        spawned one trivial agent, log gained exactly one row 8s later. IT FIRED WITHOUT A
        RESTART - settings.json hooks are live mid-session, unlike agent definitions.
        COST TRAP I CAUSED AND FIXED: the ~50k spawn floor is mostly the CLAUDE.md hierarchy,
        loaded by every non-Explore/Plan agent. I had just written this investigation INTO
        CLAUDE.md, taxing every future spawn. Trimmed 971 -> 469 words (hierarchy 2204 ->
        1702) and moved detail to control/AGENT-MECHANICS.md. CLAUDE.md is a pointer file.
        Also backed up all 13 transcripts (6.5 MB) to _reference/agent-transcripts-2026-09-07/
        because cleanupPeriodDays is unset and the 30-day sweep is live.
        Recorded for next limit hit: capture what the next user-role message is - if it is
        Jon's own last message replayed, Desktop re-dispatches on reset and a fan-out message
        would spawn everything again.

### 2026-09-07 | T-109 | resume_drill.py — the one command to run on any interruption
STATUS: DONE
VERIFY: python tools/resume_drill.py  (prints state, flags DIED agents, prints continuation brief)
RESULT: PASS. Jon asked whether a resume test was written and ready. It was not - salvage
        existed but there was no single drill. Now there is.
        Tested: correctly flagged all 4 agents that died mid-task (2x america-world research,
        2x native-nations prose) and distinguished them from 8 that completed. Generated the
        continuation brief for the most recent dead agent (122 tool calls recoverable).
        The drill answers, in order: what landed on disk / which agents died / which resume
        routes exist on this build / the exact paste-ready prompt for a fresh agent.
        Wired as step one in control/RESUME.md and pointed to from CLAUDE.md.

### 2026-09-07 | T-110 | Fork retest + discrepancy report
STATUS: DONE
VERIFY: control/AGENT-MECHANICS.md sections 2 and 2d; _reference/claude-code-2.1.260-desktop-discrepancy.md
RESULT: PASS, and it CORRECTED one of my findings. External research suggested fork was not
        fully dead. Right: setting env.CLAUDE_CODE_FORK_SUBAGENT=1 in settings.json made
        subagent_type "fork" available MID-SESSION with no restart (settings.json changes are
        live; .claude/agents/ files are not - that asymmetry holds).
        Fork DOES inherit the parent conversation: asked to name the finished chapter from
        context alone, it answered "Native Nations (chapter 02), 12,826 words across three
        part files" with ZERO tool calls.
        BUT THE COST INVERTS THE ADVICE: that one-line reply cost 621,107 tokens against
        ~50,000 for a cold general-purpose spawn. Fork is ~12x MORE expensive and did no work,
        because it carries the whole conversation. The hypothesis was that fork would be
        cheaper via shared prompt cache; on this build, deep in a long session, it is an order
        of magnitude worse. Fork cost scales with parent conversation length.
        FLAG REVERTED - it may make ALL spawns forks, and confirming would cost another spawn.
        Re-enable deliberately per task, then revert.
        Also drafted _reference/claude-code-2.1.260-desktop-discrepancy.md - a filable report
        of the SendMessage/name/fork documentation mismatch on claude-desktop 2.1.260, with
        the evidence and four suggested fixes.

### 2026-09-07 | T-111 | Make the resume path cost-effective (Jon's actual goal: money)
STATUS: DONE
VERIFY: python tools/resume_drill.py shows the cost table and recommends --brief
RESULT: PASS. Jon's goal is not to avoid restarting for its own sake - it is to stop paying
        twice for the same thinking. Honest finding: a dead agent's PROMPT CACHE cannot be
        re-attached; it dies with the agent. The saving comes from not redoing the work.
        Added salvage_agent.py --brief: conclusions + source list, WITHOUT raw fetched pages.
        49,703 bytes (~12k tokens) vs 358,061 (~90k) for the full digest - 87% smaller, and
        roughly 1/80th of the ~1,000,000 tokens re-running the agent cold would cost.
        Updated resume_drill.py: it now leads with a MEASURED COST TABLE and ranks the four
        routes by cost - Workflow resumeFromRunId (the only true cache reuse, completed calls
        replay free), salvage --brief (always available, the cheap path), fork (available via
        env flag but ~621k/spawn, usually wrong), SendMessage (absent, re-verify on new builds).
        The drill was written before the fork test; it is now current.

### 2026-09-07 | T-112 | Correction: there is no "pause message" to a sub-agent
STATUS: DONE
RESULT: Jon asked whether a pause message would be received between tasks and resumed later.
        It would not, and I had written the sloppy version into memory ("message every running
        agent to stop cleanly (SendMessage), or TaskStop where a clean stop is not possible").
        There is NO messaging to sub-agents on this build - no pause, no resume. TaskStop KILLS.
        Corrected in memory and control/RESUME.md. "Pause" now means: stop dispatching, then a
        stated per-agent judgement - LET IT FINISH if likely mid-write (killing it destroys the
        very output worth keeping), or TaskStop if it is still researching and will burn the
        window for nothing. The transcript survives either way and is salvageable.

### 2026-09-07 | T-113 | "Pause" simplified to its literal meaning (Jon)
STATUS: DONE
RESULT: Jon removed the pause-the-agents protocol. "Pause" now means only: stop what you are
        doing and wait. Running sub-agents are LEFT ALONE to finish or die with the window -
        no TaskStop. Rationale: there is no way to message them, TaskStop only kills, and an
        agent killed just before its write loses exactly the output worth keeping. Updated in
        agent memory and control/RESUME.md.

### 2026-09-07 | T-114 | Partial writes can no longer pass as finished work
STATUS: DONE
VERIFY: python tools/salvage_agent.py <id> --wrote ; --tail ; --event I
RESULT: PASS. Jon spotted a real hole: the drill asked "is it on disk?" and treated a file's
        existence as proof of completion. An agent killed mid-Write leaves a SHORT file that
        looks like success. Two new capabilities, both tested:
        --tail [N]: the last N events (default 8) - every thought, tool call and result -
          truncated to 300 CHARACTERS each (Jon's call: never lines, because one line can hold
          a whole base64 image or literal \n sequences), each showing "+N more chars" and an
          --event I to expand it in full. Ends with a verdict: REPORTED vs CUT MID-CALL /
          CUT AFTER RESULT / KILLED.
        --wrote: compares the bytes the agent SENT in each Write/Edit against the bytes now on
          disk, flagging SHORT! and MISSING!.
        Demonstrated on a real kill: agent a9ee417de68883152 shows [43] "I have everything I
        need. Writing the file now." -> [44] Write (24,564 more chars) -> [45] "File created
        successfully" -> [46] the kill. --wrote confirms sent 24,071 vs 24,446 on disk = ok.
        So it wrote FULLY and then died - now distinguishable from dying mid-write.
        The drill's question is now "[1] IS IT ON DISK - AND DID IT FINISH?" with a new
        section [2b] running --wrote automatically for every dead agent.

### 2026-09-07 | T-115 | "A write is not a finish" — the judgement moves to the director
STATUS: DONE
RESULT: Jon's correction, and it caught my tool overclaiming. --wrote had been printing "the
        files are complete" when all it measured was that a write landed intact. Those are
        different claims and the second is a judgement, not a measurement.
        THE RULE, now in the tooling and control/AGENT-MECHANICS.md 6e: a write is almost
        never an agent's last act - normally it writes, then reports, or writes again, or
        validates. An agent whose final recorded action is a write was cut off BEFORE its next
        step. A completed write is NOT a completed task. The only real signal that an agent
        thought it was done is a CLOSING REPORT.
        THEORY recorded as UNCONFIRMED (Jon's): the runtime appears to let an in-flight tool
        call finish rather than severing it - every kill observed shows a completed write then
        the error, never a half-written file. Encouraging, unproven, always verify with --wrote.
        TOOL CHANGES: finished_verdict() now returns EVIDENCE about the shape of the ending
        ("KILLED MID-ACTION", "KILLED AFTER A RESULT", "ENDED WITH A REPORT") and explicitly
        refuses to rule on completion. --wrote now says "Every write landed at the size it was
        sent. That is ALL this proves." and points at --tail. --tail ends by handing the
        decision to the reader with the three questions to ask.
        HANDOVER CHOICE is now a judgement too: --brief (~12k) when I can see exactly what is
        missing; the FULL digest (~90k) when the state is ambiguous - send the research, the
        reasoning and the raw material and let the fresh agent work out where it got to.
        Paying 90k to avoid guessing beats ~1M to redo, and beats a confident wrong guess.

---

## CHAPTER 06 city-building — prose. One agent at a time (Jon, 2026-09-07)

### 2026-09-07 | T-200 | city-building prose, part 1 (before-1500 .. 1750-1800)
STATUS: IN-FLIGHT
VERIFY: node tools/validate_grid.js on the concatenated chapter once all parts exist;
        single part files WILL report missing eras - expected, not a defect
EXPECT: manuscript/city-building/part1-before-1800.md - 5 eras, mode="prose",
        progress="written", all stories status="verified", 0 [VERIFY] tags
NEXT:   ON INTERRUPTION: python tools/resume_drill.py FIRST. Do not assume loss - measure.
        This agent is instructed to write INCREMENTALLY (era by era), so a kill should
        leave partial output on disk rather than nothing. Check --wrote and --tail, then
        judge whether to finish the gap or restart the part.
RESULT:

## ⏸ ACTIVE TEMPORARY PROTOCOL — "continue" gate (Jon, 2026-09-07)

**After EVERY sub-agent finishes: STOP. Report what it did. Wait for Jon to say
"continue" before dispatching the next one.** Do not chain agents.

Why: Jon is reading context-usage figures off the UI between agents, to learn how
large a sub-agent task can safely be for a given amount of remaining usage. The
figures are not visible to agents — he reads them, not me. I never need to measure
or estimate usage; I just stop and let him look.

**This is TEMPORARY.** Jon will say "decommission the continue protocol" to end it,
and may later say to reinstate it. Until he says otherwise, it is in force.
Not written to agent memory or CLAUDE.md on purpose — it is a temporary working
mode, not a standing preference, and CLAUDE.md is taxed on every spawn.

### 2026-09-07 | T-201 | validate_grid.js --part : stop training agents to ignore errors
STATUS: DONE
VERIFY: node tools/validate_grid.js --part <partfile>  -> 0 errors, exit 0
        node tools/validate_grid.js --part <bad file>  -> still reports and exits non-zero
RESULT: PASS. Jon caught a design flaw of mine. Part files hold 5 of 10 eras by design, so
        the completeness check always fired "missing 5 era(s)" and I had been telling agents
        "expect 1 error, ignore it". That is how an agent learns to wave through a REAL error -
        and it is worse since the validator now exits non-zero, so the false alarm also
        poisons any exit-code check.
        Added --part: suppresses ONLY the ten-era completeness check. Everything else stays
        at full strictness. Proven: part file with --part = 0 errors exit 0; a deliberately
        broken file with --part = 2 errors exit 2 (unknown era id, bad state). Whole-chapter
        validation unchanged - 37 outlines exit 0, merged native-nations 21 stories 0 errors.
        Updated templates/chapter-template.md and control/RESUME.md: EXPECT 0 ERRORS, never
        accept one as "expected".
        NOTE for future prompts: stop writing "the validator will report missing eras - that
        is expected" into agent briefs. Tell them to use --part.

        AMENDED 2026-09-07 (Jon): my replacement rule - "never accept an error as expected" -
        was too absolute and was itself wrong. An agent writing INCREMENTALLY will legitimately
        see errors mid-write; part 2's agent reasoned correctly that "the error is expected
        mid-write since era 07 is still open". A rule that must be broken teaches agents to
        ignore rules. The rule is now about the FINAL state: errors mid-write are normal and
        expected; the LAST run before reporting must be clean; and if an error survives to the
        end, fix it or state in the report what it is and why it was left. What is forbidden is
        shipping an error UNEXAMINED - the agent must decide about it and show its reasoning.

### 2026-09-07 | T-202 | Usage log started (Jon)
STATUS: DONE
RESULT: control/usage-log.tsv created. TSV so it can be analysed for patterns later: which
        KINDS of sub-agent task consume how much of a usage window. Backfilled 14 rows from
        this session's notifications (tokens/tool_uses/duration are in the notification; usage
        percentages are UI-only and come from Jon).
        First measured delta: city-building part1, 68% -> 81% = 13% for 2,814 words of prose,
        157,398 tokens, 51 tool calls, 25 incremental writes.
        Early shape of the data: spawn floor ~50k tokens; a focused research question (Acoma)
        cost 183k/90 calls; adversarial verification ~145k/30 calls; a fork spawn 621k for
        nothing. Two whole-chapter research attempts died before writing; the same work split
        in half landed first try both times.
        Protocol added to control/RESUME.md: log a row after every sub-agent.

### 2026-09-07 | T-203 | city-building prose, part 2 (1800-1850, 1850-1900)
STATUS: DONE
VERIFY: node tools/validate_grid.js --part manuscript/city-building/part2-1800s.md  (EXPECT 0)
EXPECT: manuscript/city-building/part2-1800s.md - 2 eras, mode="prose", progress="written",
        all stories status="verified", 0 [VERIFY] tags
NEXT:   n/a
RESULT: PASS - 4,076 words, 2 eras, 4 stories all verified, 0 [VERIFY] tags, --part validator
        0 errors exit 0, 8 incremental writes. Chapter now 7,186 words, 8 stories, 0 errors.
        THE AGENT CAUGHT ITSELF INVENTING. Unprompted, it reported: "I also caught and removed
        two numbers I had drafted from general knowledge rather than the bank (the aqueduct's
        per-mile fall, and the Croton River's distance north of the city), plus a gloss defining
        'Croton cocktails'." That is the no-invention rule working on the agent's own draft -
        plausible, checkable numbers that were NOT in the bank, removed before shipping.
        Six honest refusals against the outline: tenement dimensions (outline-only, not in the
        bank); the 1811 commissioners' "rivers gave air enough" rationale; Strong's first name
        as reform mayor - AND it flagged that this is a DIFFERENT Strong from the diarist
        George Templeton Strong, refusing to link them; the Croton labourers left unnamed with
        the prose SAYING they are unnamed rather than inventing a workforce; Strong's
        "amphibious life" quote (flagged unverified in the bank); SF vigilance committees.
        Disputes carried as disputes: Rochester's population as a 9,200/12,630 range; the
        "first skyscraper" question with the Jenney Myth scholarship and three rival buildings.
        Hard material handled per policy: cholera defined with the 1832 toll; marasmus DEFINED
        AS STARVATION with the method of wasting stated (clinical-word rule 3b working);
        Seneca Village's clearance including that land ownership was what qualified Black men
        to vote there.
        No personification hits. The 600 men at 6,000 jackscrews are named as the people who
        raised Chicago, not "the city raised itself".

### 2026-09-07 | T-204 | city-building prose, part 3 (1900-1950, 1950-2000, 2000-today)
STATUS: FAILED - killed at 99% usage, having written nothing. Nothing to salvage.
VERIFY: node tools/validate_grid.js --part manuscript/city-building/part3-1900s-and-today.md
        then the merged chapter: cat manuscript/city-building/part*.md > /tmp/cb.md and
        validate (all ten eras must be present once parts 1-3 exist)
EXPECT: manuscript/city-building/part3-1900s-and-today.md - 3 eras, completing chapter 06
NEXT:   *** JON WAS AT 99% WHEN THIS WAS DISPATCHED - AN INTERRUPTION IS LIKELY ***
        ON INTERRUPTION: python tools/resume_drill.py FIRST. This agent writes
        incrementally, so expect PARTIAL output on disk, not nothing. Then:
          python tools/salvage_agent.py <id> --wrote   (did the writes land whole?)
          python tools/salvage_agent.py <id> --tail    (what was it doing? what came next?)
        Then JUDGE - a write as its last act means its next step never happened. If the
        state is ambiguous, hand the FULL digest to a fresh agent, not --brief.
RESULT: FAIL, and the recovery procedure ran exactly as designed for the first time on a
        REAL interruption. Findings, in order:
        DRILL: "Files changed in the last hour: (nothing)". manuscript still 20,012 words -
        unchanged. So nothing landed.
        --wrote: "issued no Write/Edit calls."
        --tail: 5 events total. [1] "I'll start by reading the required files." [2] one Bash
        ls/wc call checking file sizes as instructed. [3] the listing came back. [4] killed.
        It never read a source file and never wrote a line.
        JUDGEMENT: NOTHING TO SALVAGE. The transcript holds one directory listing. Salvaging
        would be theatre. Relaunch from scratch - no brief, no handover.
        This is the honest negative case for the salvage tooling: it is worth everything when
        an agent died deep into research (2 of those cost ~100 web fetches each), and worth
        nothing when an agent died in its first 30 seconds. The drill distinguishes the two in
        three commands and about a second of work, which is the entire point.
        ALSO FIXED: the drill's tail output printed a literal "%s" instead of the agent id in
        its handover hint. Caught by running the procedure for real.

### 2026-09-07 | T-205 | city-building part 3 - RELAUNCH after the kill
STATUS: DONE
VERIFY: node tools/validate_grid.js --part manuscript/city-building/part3-1900s-and-today.md
        then merge parts 1-3 and validate the whole chapter (all ten eras)
EXPECT: manuscript/city-building/part3-1900s-and-today.md - 3 eras, completing chapter 06
NEXT:   n/a
RESULT: PASS. *** CHAPTER 06 CITY BUILDING IS COMPLETE - the book's second finished chapter ***
        Merged and validated as the viewer reads it: 1 chapter, 10/10 eras, 14 stories,
        0 errors, 0 [VERIFY] tags, 12,942 words.
        Part 3: 5,564 words, 6 stories. It reported going over the length guidance and said
        why - 23 outline blocks at ~240 words each - and that it trimmed ~300 words of
        flourish rather than cutting facts. That is the right trade, stated openly.
        SELF-CAUGHT INVENTIONS (five, unprompted): three embellishments in the Virginia Ali
        story (a segregation claim about 1950s Washington, "police and activists in the same
        room", customers climbing over the Metro works for five years - the bank supports
        none); a paragraph of its own reasoning about why office-to-housing conversion is
        hard; and an aphorism it had written, "Blight was a judgment, not a measurement".
        It also narrowed "1,776 feet, the year the Declaration of Independence was signed"
        to "a height chosen for the year 1776".
        PERSONIFICATION: it ran a dedicated 1.1 pass after drafting and repaired ~25
        instances - a city drinking, a law protecting, programs moving families, an
        expressway displacing, schools teaching, red lines choosing, a pandemic making.
        HARD MATERIAL, unsoftened: urban renewal named as the Housing Act of 1949 Title I
        WITH the mechanism (blight designation, eminent domain, demolition, land handed to
        developers), 1949-1974, ~2,000 neighborhoods, at least 300,000 families as the
        documented floor alongside the ~1.2 million estimate, 13 percent of the population
        and at least 55 percent of the displaced, Baldwin's 1963 words verbatim; I-94 through
        Rondo with both source counts as a range; HOLC grading with "infiltration" in the
        appraisers' own word plus the 2018 NCRC follow-up; restrictive covenants;
        kitchenettes; Levittown's whites-only sales.
        Four honest omissions: Buchanan v. Warley and the McMillan Plan (bank marks both
        "not re-verified"), Overtown Miami (unverified lead), Levittown's builder unnamed
        because the bank names no person.

## 🔍 DEBUG MODE ACTIVE — verbose recovery (Jon, 2026-09-07)

Stay in verbose/debug recovery mode: on every interruption run the FULL procedure and
narrate it, even when the answer is obvious. We are still collecting resume attempts to
learn how interruptions actually behave. Streamline only when Jon says so.

Attempts so far: 3 killed-after-write (work landed, reports lost) · 2 killed-deep-in-
research (~100 web fetches each, salvageable) · 1 killed-in-first-30-seconds (nothing to
salvage, relaunched clean). The third category is new as of T-204 and is the case where
the drill's value is telling you NOT to bother salvaging.

### 2026-09-07 | T-206 | Adversarially verify city-building part 3
STATUS: DONE
VERIFY: verifier reports 0 invented content, 0 unrepaired softening, format clean
EXPECT: an independent check of the largest and hardest part of chapter 06 - 5,564 words
        carrying urban renewal, redlining, the highways and who was kept out of the suburbs
NEXT:   n/a
RESULT: FAIL - 9 defects fixed by the verifier, 7 reported; director then fixed 4 more.
        Validator 0 errors throughout. Chapter still merges clean: 10 eras, 14 stories.

        *** THE HEADLINE: A GOOD SELF-REPORT IS STILL NOT EVIDENCE ***
        This writer self-caught five inventions and claimed ~25 personification repairs -
        the best self-report we have had. The independent pass still found nine more defects,
        and the personification claim DID NOT HOLD: survivors included the exact failure case
        policy 6b warns about ("New York's law of 1916 sorted the city into districts and set
        a formula"). Self-checking raises quality; it does not replace verification.

        ERRORS OF FACT the verifier caught:
        - "more than double any building in the United States" (Burj Khalifa). 2,717 ft vs
          1WTC's 1,776 = 1.53x - arithmetically false against a number three paragraphs later
          IN THE SAME FILE. *** IT WAS INHERITED FROM outlines/city-building.md *** so the
          error was in our own source. Director fixed the OUTLINE too, with a note, so it
          cannot propagate a third time.
        - Raker Act: Congress passed it Dec 6, Wilson signed Dec 19. The writer had changed
          the bank's verb "signed" to "passed" and kept the signing date.
        - The 300,000 families / 1.2 million Americans figures are the SAME displacement in
          different units (Cebul), not a floor and a higher estimate. The prose had implied
          the second was a bigger count.
        - Toronto 1969 -> 1968.
        Director then fixed the three reported errors of fact: an invented "forty years"
        span present in neither bank nor outline; "born about 1939" which contradicts "he was
        eight" in 1958 two lines later (the bank's own note wrongly claims this computes);
        and "61 percent of residents lost what they had" -> "Rondo's population fell by 61
        percent", which is what the sources actually say.
        Verified clean by the checker: the Baldwin quote verbatim and correctly dated 1963;
        NCRC 2018; the 400 cities / 1,200 projects / 2,000 neighborhoods / 13% / 55% set;
        Rondo's 80/600/700/300/one-in-eight; WPA totals; Cleveland's 876,050.
        Remaining reported items are judgement calls left for a later pass: five surviving
        personifications, four outline-but-not-bank phrases, and three style-guide closers.

### 2026-09-07 | T-207 | Adversarially verify city-building part 2
STATUS: DONE
VERIFY: verifier reports invented content, softening, personification, format
EXPECT: independent check of 4,076 words - cholera and the 1832 toll, the Chicago raising,
        the skyscraper dispute, the Old Law tenement, Seneca Village, the Moore baby
NEXT:   n/a
RESULT: FAIL - 10 defects fixed by the verifier, 8 reported; director then fixed 4 AT SOURCE.

        *** THE FINDING THAT CHANGES THE PLAN: OUR OWN SOURCES CARRY DEFECTS ***
        Three kinds, all real, all in one chapter:
        1. FACTUAL ERROR IN THE OUTLINE (found in part 3): "Burj Khalifa more than doubled
           anything in the U.S." - false, 2,717 vs 1,776 ft = 1.53x. A writer inherited it.
        2. A MANUFACTURED DISPUTE IN THE BANK: Rochester's 9,269 (1830 census) and ~12,630
           (1834) are two dated points on a RISING CURVE. The bank filed them under
           "Disputes" and said "state the range", so the writer correctly followed the
           source and produced the false line "somewhere between about 9,000 and about
           12,600". The bank made a true thing false by mis-framing it. Disputes entry #6
           withdrawn; the trap is now named in the entry so nobody re-adds it.
        3. AN ERASURE IN BOTH: the outline called the 1889 Oklahoma land run ground "empty
           prairie" and the bank "empty ground" - exactly the softening our own policy
           forbids, sitting in our own sources. *** THE WRITER OVERRODE IT UNPROMPTED ***
           and wrote "The ground thrown open that day was Native land, taken from the
           nations who held it." Both sources now corrected, with the old phrasing quoted
           so the correction is legible.
        Also: the bank dates an 1886 Mohawk ironworker job to the Victoria Bridge, completed
        1859 - flagged [VERIFY the bridge]; the writer had already sidestepped it by writing
        only "a bridge job".
        Reported and left for a later pass: four Olmsted claims that are in the outline but
        NOT the bank (Prospect Park, the Emerald Necklace, "dozens of places", farmer and
        journalist); "first large electric street railway anywhere" where the bank says
        "first successful large-scale"; a Riis-vs-Old-Law contradiction over which was the
        "first" tenement law; and the reform mayor Strong / diarist Strong name collision.
        Verified clean by the checker: Home Insurance Building 10 storeys / 138 ft / 1885;
        Lake Street raising 320 ft / 35,000 tons / 600 men / 6,000 jackscrews / five days;
        Williams' $125 for three lots on 27 Sept 1825; Agnes Mary Moore, 21 Apr 1869, five
        months, marasmus. Cholera and marasmus correctly defined per policy 3b.
        ROADMAP: new Phase 2b - audit the SOURCES, not just the prose. Every verifier brief
        must now say: if a defect traces to the outline or bank, SAY SO, or it propagates.

### 2026-09-07 | T-208 | Adversarially verify city-building part 1 (completes chapter 06 QA)
STATUS: DONE - 7 DEFECTS FOUND, chapter 06 QA complete (all 3 parts verified)
CORRECTION (2026-09-07, after compaction): this task was written into the ledger TWICE as
        IN-FLIGHT and NO AGENT EVER RAN. Jon force-stopped at 97% usage before the dispatch,
        deliberately, so a sub-agent would not start into an exhausted window. Both false
        IN-FLIGHT entries are collapsed into this one. There is no transcript to salvage and
        nothing was lost. LESSON: write IN-FLIGHT immediately before the Agent call, not
        before the paragraph that precedes it - the gap between the two is where a phantom
        entry comes from, and a phantom IN-FLIGHT sends the next session hunting for a dead
        agent that never existed.
VERIFY: verifier reports arithmetic/consistency, invented content, softening, personification,
        format; and says explicitly if any defect traces to the outline or the bank
EXPECT: independent check of 2,814 words - the last unverified part of chapter 06
NEXT:   dispatch the verifier. ON INTERRUPTION: full debug recovery - resume_drill.py, then
        --wrote and --tail, then judge and narrate. Do not streamline; still collecting
        resume attempts.
RESULT: Verifier ran clean on format (validator 0 errors with --part, 4 stories) and found
        SEVEN substantive defects, FIVE of them inherited from our own sources:
        1. "on an empty riverbank, before anybody lived there" (DC) - FALSE. Georgetown 1751
           and Alexandria 1749 stood inside the ten-mile square; the land was tobacco farms
           worked by enslaved people. The file's OWN Banneker camp at Jones Point is at
           Alexandria. SOURCE = outline ("designed its capital city from nothing, on an empty
           riverbank"); prose amplified it. This is the SECOND "empty land" erasure found in
           this chapter's sources - see T-207 on the Oklahoma land run.
        2. "Yellow fever killed people in Philadelphia in 1793" - the outline said THOUSANDS
           (~5,000 dead, ~10% of the city); the prose DELETED the quantity. SOURCE = prose
           regression. A rare case of prose softening what the outline said plainly.
        3. "largest earthen structure ever built in the Americas" - false; bank says largest
           PREHISTORIC. Fort Peck Dam is ~150x its volume. SOURCE = outline dropped the word,
           prose sharpened to "ever built".
        4. Chaco dated "between about 900 and about 1180" and "People left in the 1140s" four
           paragraphs apart - self-contradiction. SOURCE = bank carries both figures.
        5. New Amsterdam wall: colonists named as builders first, enslaved Africans arriving
           as a subordinate correction, nobody named as enslaver. SOURCE = bank wording; the
           OUTLINE OMITS the enslaved labour entirely and personifies ("New Amsterdam built").
           Prose improved on the outline but left agency inverted.
        6. "$5, the ordinary difference between a surveyor and his assistant" - bank says $2
           was normal assistant pay, a rate not a differential. SOURCE = prose.
        7. "for the next 250 years" and "a printed rulebook" (Spanish plazas) - not in bank.
           SOURCE = outline.
        Low confidence, noted not scored: "dismissed before a street of it was built";
        "about twenty-five other men" reading as ~26; a stale hb-note saying missing-era
        errors "are expected" (--part no longer produces them).
        CONFIRMED CLEAN by recomputation: 1565-1573=8yrs; ten-mile square = 40-mile perimeter;
        Banneker b. Nov 1731 = 59 in Feb 1791; Apr 1791-Feb 1792 = ~10 months; 1793 populations
        Phila 13k/Boston 12k/NY 11k/Charleston 8k; Cahokia 10-20k core, 14 acres, 50-acre
        plaza, 15-20k logs; Pueblo Bonito 650+ rooms; Chaco 150 rooms/23 kivas; $33,000;
        21 Jan 1801. Cahokia agrees with native-nations part1:25. Era ids unique, slugs
        globally unique, all blocks closed, movie attributes in sync.
        PHASE 2b CONFIRMED AGAIN: 5 of 7 defects came from the outline or the bank, not the
        writer. Auditing prose alone would have caught two.
        NEXT: fix pass on part 1 prose AND on outlines/city-building.md + research bank.

### 2026-09-07 | note | Custom agent definitions DO register (answers AGENT-MECHANICS 2b)
The probe/probe2 definitions written earlier became available as agent types later in the
same session, with no restart - but NOT immediately: two spawns right after writing the
files failed with "Agent type 'probe' not found". So definitions work on this build, with
a delay before registration. maxTurns/tools/permissionMode/memory/hooks frontmatter are
therefore all available. Recorded in control/AGENT-MECHANICS.md 2b.

### 2026-09-07 | T-209 | Fix city-building part 1 AND the outline/bank defects behind it
STATUS: IN-FLIGHT
VERIFY: node tools/validate_grid.js manuscript/city-building/part1-before-1800.md --part = 0
        errors, AND the same for outlines/city-building.md (no --part) = 0 errors; every one
        of T-208's 7 defects either fixed or explained; the DC "empty riverbank" erasure
        removed from BOTH the prose and outlines/city-building.md.
EXPECT: first fix pass that repairs SOURCES as well as prose (ROADMAP Phase 2b in practice).
        5 of the 7 defects live in outlines/city-building.md or research/research-city-building.md.
        The DC one needs a small amount of real research (Georgetown 1751 / Alexandria 1749 /
        who worked the land) added to the bank with citations, since the bank does not have it.
NEXT:   ON INTERRUPTION: full debug recovery - resume_drill.py, then --wrote and --tail, then
        judge and narrate. Do not streamline; still collecting resume attempts.
RESULT: DONE. All 7 defects fixed across THREE files (prose + outline + bank). Both validators
        clean: part1 --part = 0 errors / 4 stories; outlines/city-building.md = 0 errors /
        14 stories. Prose 3,253 -> 4,104 words, all of it sourced fact.
        1. DC erasure: researched from scratch (NPS, LOC, City of Alexandria, NMAAHC,
           emancipation.dc.gov), new sourced bank section at era 05. Prose now: "The ground
           they chose was not empty. Native towns had stood on it. Two tobacco ports were
           standing on it when they chose it. The rest of it was farmland, and the people
           working that farmland were enslaved." Nacotchtank named; Alexandria 1749 and
           Georgetown 1751 placed inside the ten-mile square with Jones Point in Alexandria;
           five proprietors named; 1790 census 245 enslaved on Notley Young's plantation,
           another account 260. Outline depersonified: Washington chose, Ellicott measured,
           L'Enfant drew.
        2. Yellow fever restored WITH scale and bodily course per policy 3b: ~5,000 dead
           1 Aug - 9 Nov 1793, ~1 in 10 of the city. 1798 left without a number - none found.
        3. Monks Mound: "prehistoric" restored in prose and outline; bank now carries the
           Fort Peck guard (814,000 vs 125.6M cubic yards).
        4. Chaco: prose now distinguishes the great-house span from when people left; bank
           and outline carry the distinction so the trap is not re-handed.
        5. New Amsterdam wall: "Africans held as property by the Dutch West India Company dug
           the trench for the wall that gave Wall Street its name." Stuyvesant and the court
           named as ordering it; the half-freedom of 25 Feb 1644 stated, including that the
           children stayed Company property.
        6. Banneker's pay: "$2 a day, which was an ordinary day's pay for an assistant.
           Andrew Ellicott was paid $5." Invented differential cut.
        7. "250 years" and "printed rulebook" cut from outline and prose; bank records why
           and forbids restoring them without a citation.
        Low-confidence items all actioned. Also fixed 1.1 personification slips found in
        passing: "wherever Spain planted a town", "Boston set a night watch", "the city
        answered".
        *** A THIRD "EMPTY LAND" ERASURE FOUND: OAK RIDGE. *** Outline said "Secret cities
        from nothing" / "on empty ridgeland". About 1,000 families (3,000-4,000 people) were
        removed from Wheat, Elza, Scarboro and Robertsville; 59,000 acres taken by declaration
        of taking in Oct 1942 at $46.86/acre, some notified by notices nailed to fence posts.
        Corrected in outline and bank. STILL WRONG IN THE PROSE: part3-1900s-and-today.md
        lines 23 and 97-98 - and part 3 had ALREADY PASSED verification (T-206). It passed
        because that pass predated Phase 2b and checked prose against sources rather than
        auditing the sources. See T-210.
        Bank now carries a standing rule: when a chapter has produced this move three times,
        assume a fourth - check every founding sentence for who was already on the ground.

### 2026-09-07 | T-210 | Fix the Oak Ridge erasure in city-building part 3
STATUS: SUPERSEDED - moved to control/AUDIT-QUEUE.md (3c) by the 2026-09-07 restructure.
        Auditing no longer happens between chapters. This is now Phase 3 work. The facts
        needed are already sourced, so it stays a pure edit whenever it is picked up.
VERIFY: no "empty ridgeland"/"empty ground"/"from nothing" left in
        manuscript/city-building/part3-1900s-and-today.md; the removals named with numbers;
        validator --part = 0 errors.
EXPECT: small, surgical - two sentences (lines 23 and 97-98) plus the span label "Secret
        cities from nothing". The facts are already sourced in research-city-building.md
        era 08 and outlines/city-building.md:190, so NO new research is needed.
WHY IT MATTERS: part 3 had already PASSED adversarial verification at T-206. It passed
        because that brief predated Phase 2b - it checked the prose against the sources
        instead of auditing the sources. A verified chapter is only as clean as the brief
        that verified it. The other 19 researched chapters have had NO source audit at all.
NEXT:   dispatch after Jon's continue.
RESULT:

### 2026-09-07 | DEFECT in our own tooling | project_state.py prose bar reads the WRONG FILE
Found while checking T-209. `--stage prose` requires stage == "WRITTEN", and stage is derived
from `progress=` flags read out of `outlines/<slug>.md` (project_state.py:133 scans the
OUTLINE; the manuscript is only word-counted at :148). Outlines correctly carry
progress="researched"; manuscripts carry progress="written". So the prose bar can never pass
for ANY chapter, no matter how finished. Measured proof: city-building's manuscript has 10/10
progress="written", 14 verified stories, 13,768 words, validator 0 errors - and the check
prints FAIL with "stage=WRITING". native-nations is in the same position.
IMPACT: the prose gate has never once been usable. Both finished chapters read as unfinished.
        The research and patch bars are unaffected - they are outline-and-bank measurements
        and read the right file.
DECISION NEEDED FROM JON before changing it, because this file is the project's definition of
done and editing it silently is exactly what the measure-don't-trust rule exists to prevent.

### 2026-09-07 | T-211 | RESTRUCTURE: three phases, and the writing guide becomes the instrument
STATUS: DONE - director work, no sub-agent
JON'S RULING: "Can we save all the major auditing till after we write the book?" Research
        everything (the outline is a product of research, not a separate stage), then write
        everything, then audit everything. Plus: "Have a powerful writing guide so we don't
        get too much bad writing, personification, and metaphors and such."
WHY:    for several sessions most agent runs were verify and fix, not book. Cost stopped
        tracking anything useful because unlike tasks were being averaged. And prevention has
        already beaten repair once, measurably: the city-building writer hit "empty prairie"
        in its own outline, recognised it as the erasure hard-subjects-policy.md forbids, and
        OVERRODE IT UNPROMPTED. A binding, specific guide changed the output at write time
        with no verifier in the loop.

CHANGED - tooling
  tools/project_state.py  THE PROSE GATE WAS BROKEN AND HAD NEVER ONCE PASSED. It derived
        stage from progress= flags read out of outlines/<slug>.md - where they correctly say
        "researched" and never say "written" - and it validated the OUTLINE instead of the
        manuscript. Both finished chapters measured FAIL. Now: chapter_state() scans
        manuscript/<slug>/*.md for eras, story statuses and [VERIFY] tags; derive_stage()
        reads ms_progress_written; the prose bar is written in manuscript terms; --check
        --stage prose validates every manuscript part with --part when there is more than one;
        validator() gained a part= argument; eras_no_story is suppressed in prose mode because
        it is an outline measurement and printing it there implied a fact never measured.
        VERIFIED: city-building PASS (10/10 written, 14/14 verified, 13,768w, 0 errors across
        3 files) and native-nations PASS (10/10, 21/21, 12,826w, 0 errors). Backup at
        tools/project_state.py.bak.
        LESSON: if a gate has never returned PASS for anything, suspect the gate.

CHANGED - the writing guide (control/writing-style-guide.md, 203 -> ~380 lines)
        It was written for general nonfiction and said NOTHING about the actual reader - no
        age, no reading level, no vocabulary ceiling - and nothing about the way current AI
        prose fails. Added:
        Sec 0  WHO IS READING THIS. Ages 8-15. Sentences 12-18 words, one idea each,
               paragraphs 3-6 sentences, shortest word that means it (with a swap list),
               hard words kept but defined in plain language at first use, and five things a
               reader this age cannot do.
        1.11   THE AI CADENCE - the longest new section, and the one that matters. Names ten
               specific moves and forbids each with an example: the triad, anaphora, the
               em-dash pivot, "not just X but Y", the fragment for emphasis, the closing
               reversal, escalating short sentences, the rhetorical question, conversational
               meta ("here's the thing"), antithesis pairs. Includes the shape test - look at
               consecutive sentences ignoring content; if you can hear a beat, rewrite - and a
               warning not to disguise a pattern instead of removing it.
        1.12   FORCED RHYTHM AND SOUND PATTERNING. No alliteration, rhyme or metre. The
               read-aloud test: performed vs explained.
        1.13   REGISTER MIXING - Jon's "1500s poetry mixed with modern information". Banned
               diction list. One plain present-day voice for all 37 chapters.
        1.14   WORDS TOO BIG FOR THE JOB, including nominalization, which is also where
               personification breeds (a nominalized action needs a subject and an institution
               is the nearest one to hand).
        2.6    KNOW WHAT YOU ARE TEACHING AND GET TO IT. Finish "the reader will understand
               ___" before writing a block; put the point in the first sentence or two; the
               two-question test. Establishes that WITHHOLDING A FACT FOR SUSPENSE IS A FORM
               OF SOFTENING, which links the style guide to the tone policy.
        Sec 4  SELF-AUDIT BEFORE YOU REPORT - seven concrete passes including a literal
               search for the tells. 3.1 rewritten: you are your own revision pass.
        Checklist extended 17 -> 23 items.

CHANGED - planning
  control/ROADMAP.md      rewritten around the three phases. Phase 1 folds the 15 gapped
        chapters in with the 17 unresearched. Phase 2 has no verify or fix agents. Phase 3
        splits into 3a structural/parsing, 3b language, 3c fact-and-source.
  control/AUDIT-QUEUE.md  NEW. Where a defect waits instead of being lost. Carries the Oak
        Ridge erasure in part 3 (in prose that already PASSED verification), the same erasure
        in research-migration.md:121 for a chapter not yet written, the reported-not-fixed
        items from chapter 06, the IHS sterilizations owed to native-nations, and seven defect
        pattern classes to sweep for - all seven found in city-building, which we had called
        complete and prose-ready.
  control/RESUME.md       three-phase section; a new standard WRITING brief; the prose bar
        corrected in the definitions-of-done table with a note on how it was broken; usage
        rules rewritten (categorise every row; a clean reading brackets the agent and nothing
        else).
  control/STATUS.md       header now says its plan is superseded and points at ROADMAP.
  CLAUDE.md               loaded into every sub-agent, so kept short: added the reading level,
        the no-AI-cadence rule, one-voice, know-what-you-are-teaching, and the three-phase
        model with "do not repair the source, name it".
  control/usage-log.tsv   T-209 marked + (contaminated by director work); marker legend
        extended; six task categories defined; the 12,000-tokens-per-point rule recorded as
        FALSIFIED by the first fix-type run.
  outlines/BOOK-OUTLINE.md  rebuilt - it was stale and still carried the pre-correction
        city-building text. Now 37 chapters, 603 stories, 171,907 words, 0 errors. The four
        remaining "empty land" hits are correction annotations quoting the old wording.

NOT CHANGED: control/AGENT-BRIEF.md - checked for references to the old interleaved model and
        found none; research is unaffected by the restructure.

NEXT:   Phase 1. First dispatch is a research agent, and it will be the FIRST clean row of a
        kind we have never measured. Bracket the reading tightly.
RESULT: All four control docs, the guide, CLAUDE.md and the tooling are consistent with the
        three-phase plan. Prose gate verified working on both finished chapters.

### 2026-09-07 | T-212 | Jon's ruling: Phase 3 is a READ, and language is audited by AI not by script
STATUS: DONE - director work, no sub-agent

JON, VERBATIM: "If phase 2 (writing the book) did a good job, then the audit phase will read
        everything and it will all be perfect and won't have to do anything. Phase 3 only has
        actions to take if Phase 2 hiccups or fails at understanding how to write following
        our rules." And: "We really don't want to use scripts to look for language patterns
        because AI is needed for that. Automated pattern matching is not going to do a very
        good job of catching everything but an AI reading it should catch every single one.
        Please have more confidence in yourself."

TWO RULINGS, both binding:

1. PHASE 3 IS CONFIRMATION, NOT PRODUCTION. Its expected result is a report saying the book
   is clean. Every finding is EVIDENCE THAT THE GUIDE OR THE BRIEF FAILED, and the fix belongs
   in the instruction as much as in the sentence - a defect that appeared once will have
   appeared in other chapters written under the same instructions. If Phase 3 turns into heavy
   repair, STOP and fix Phase 2's instructions rather than grinding through 37 chapters of
   cleanup. ROADMAP Phase 3 was rewritten from three "audits" into three READS.

2. LANGUAGE IS NOT PATTERN-MATCHABLE. Removed every instruction to sweep, grep or search for
   language defects. The argument, recorded because it is the reason and not just the rule:
   a search finds "empty prairie" and walks straight past "the land was open for the taking",
   which is the same erasure; a search for the em-dash finds every dash and not the ones used
   as a pivot; a word-length check finds long words, not the wrong ones. EVERY DEFECT THIS
   PROJECT HAS ACTUALLY CAUGHT WAS CAUGHT BY AN AI READING A SENTENCE AND UNDERSTANDING WHAT
   IT WAS DOING - the seven in city-building part 1, the three land erasures, the Chaco
   self-contradiction that is invisible sentence-by-sentence. Not one came from a script.
   The only mechanical checks that remain are about FILE SYNTAX, where the machine is
   genuinely authoritative: validate_grid.js and project_state.py --check. They verify that
   markers parse. They say nothing about whether the book is any good.

CHANGED
  control/ROADMAP.md         Phase 3 retitled "Read the finished book". New section stating
        that an AI reads it and a script does not, with the reasoning. 3a/3b/3c reframed as
        reads. Effort shape: Phase 3 is not estimated as production work, deliberately.
  control/AUDIT-QUEUE.md     header reframed - the items in it are LEGACY, predating the
        restructure, and are the only part of Phase 3 that is real work. Anything found beyond
        this file is new information about a Phase 2 failure. The seven defect classes are now
        "things to recognise while reading", each with the note that the next instance will be
        worded differently, which is exactly why a search will not find it.
  control/writing-style-guide.md  Section 4 item 3 was "Search your own text for the tells".
        Now "Read for the tells - do not search for them", keeping the string list as what to
        NOTICE rather than what to match, and saying plainly that no list anticipates every
        construction.

CORRECTION TO T-211 ABOVE: that entry describes AUDIT-QUEUE.md as holding "seven defect
        pattern classes to sweep for". It no longer does, and should not have. They are things
        to recognise while reading.

DIRECTOR NOTE: the grep instinct was reaching for a tool that produces a countable result
        instead of trusting a judgment. Worth remembering, because a script's output LOOKS
        like evidence - "0 matches" reads as proof of cleanliness when it is only proof that
        one spelling is absent. A read that finds nothing is worth more than a sweep that
        finds nothing, and the two are easy to confuse in a report.

NEXT:   Phase 1, first research dispatch, on Jon's word.

### 2026-09-08 | PHASE 1 BEGINS | Autonomous research run, one agent at a time
Jon: "decommission the continue order. Do one agent at a time, one after the other, till done,
doing the research phase." He is asleep; usage percentages will not be captured (log `?`).
QUEUE, in order. Split any chapter whose load looks bigger than one window.
  A1 education (67 VERIFY, 10 target)  - SPLIT: eras 1-7, then 8-10
  A2 rights-movements (26 VERIFY, 16 candidate, 5 target)
  A3 government-politics (22 VERIFY)   A4 religion (31 VERIFY, 10 candidate)
  B1 war  B2 health  B3 disasters  B4 crime-justice  B5 drugs-alcohol
  C1 art (115 VERIFY, empty bank)  C2 music (128 VERIFY, empty bank)
  C3 storytelling-evolution (65 VERIFY, empty bank)  C4 news-communication
  C5 sports-play  C6 styles  C7 holidays
  D1 exploration (bank reformat)   D2 big-business (bank write-up)
  Then the patch queue: america-world, energy, home-family, technology, elements, economy,
  money, marketplace, work-workers, food-farming, landmarks, land-environment, migration,
  transportation, slavery-freedom, immigration.

### 2026-09-08 | T-213 | Research education, ERAS 1-7 (before-1500 .. 1850-1900)
STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check education --stage research  -- WILL FAIL until
        eras 8-10 land (T-214). Judge T-213 by its own half: eras 1-7 have 0 target,
        0 candidate, 0 [VERIFY], every claim sourced in the bank.
EXPECT: split because the load is back-weighted - 12 [VERIFY] in eras 1-5 vs 55 in 6-10.
        Splitting at era 7 balances it at ~29 vs ~38. Bank is 822w against a 2,580w outline
        and must end the chapter >= it.
NEXT:   ON INTERRUPTION: resume_drill.py, then salvage_agent.py --tail and --wrote on the dead
        agent, judge where it stopped, hand a continuation brief to its replacement.
RESULT:

### 2026-09-08 | T-213 CLOSED | Research education eras 1-7 — KILLED by weekly usage limit
STATUS: PARTIAL - eras 1-2 landed, eras 3-7 not started. Superseded by T-214.
RESULT: Agent a1cdd677a2ac1023a, 67 events, 119,842 tokens, 31 tool uses, 409s. Killed AFTER
        a tool result (the "spare the rod" attestation chain), before acting on it.
        LANDED: bank 822 -> 2,026 words; outline 2,580 -> 3,275 words. All 4 writes confirmed
        whole by --wrote (7,577 + 115 bytes to the bank, 2,231 + 3,650 to the outline).
        era before-1500: correctly nothing to do - 0 stories, thin era, no documented
        individuals, which matches Jon's naming ruling.
        era 1500s: COMPLETE - its 1 [VERIFY] cleared, its story now verified.
        eras 1600s..1850-1900: UNTOUCHED. 66 [VERIFY] tags remain chapter-wide (was 67).
        UNWRITTEN RESEARCH IN THE TRANSCRIPT, confirmed but never committed to the bank:
          - Boston Latin School: founded 23 Apr 1635, first schoolmaster Philemon Pormort,
            with the town-meeting record wording ("On the 13th of the second month, 1635...")
          - The New England Primer: Benjamin Harris, printed between 1687 and 1690 per the
            American Antiquarian Society; earliest surviving copy; contents
          - "Spare the rod": Aelfric of Eynsham c.950-1010, Wycliffe Bible 1382, Samuel
            Butler's Hudibras 1662
        Digest written to workspace/handover-education-eras1-7.md (74 KB, 63 sources,
        25 gathered results, 5 reasoning blocks).

RESUME FINDING - SendMessage still does not exist, and this was the STRONGEST test yet.
        The transcript sits in THIS session's own directory
        (2964cba6-.../subagents/agent-a1cdd677a2ac1023a.jsonl), so we were in the spawning
        session with a resumable agent in scope, and ToolSearch still returned verbatim:
        "No matching deferred tools found." That kills the conditional-provisioning
        hypothesis - it is not about scope. Remaining candidates: env gating behind
        CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS, or absence from the deferred registry.
        Untested: setting that env var in ~/.claude/settings.json and restarting the app.

TOOLING BUG FIXED: salvage_agent.py --tail died with UnicodeEncodeError on a single "->"
        arrow, because Windows consoles default to cp1252 and fetched research is full of
        arrows, em dashes and accented names. It printed nothing after the crash - a recovery
        tool failing exactly when recovery was needed. stdout/stderr now reconfigured to
        utf-8 with errors="replace" at import. Verified working.

### 2026-09-08 | T-214 | Research education ERAS 3-5 (1600s, 1700-1750, 1750-1800)
STATUS: IN-FLIGHT
VERIFY: eras 3-5 end with 0 target, 0 candidate, 0 [VERIFY], every claim sourced in the bank.
        The chapter check will still FAIL - eras 6-10 remain. Judge by the three eras.
EXPECT: NARROWED from the planned 3-7. Evidence: agent 1 spent ~120k tokens to clear one and
        a half eras, much of it the fixed cost of reading the binding docs (AGENT-BRIEF
        13.7 KB, hard-subjects-policy 15.5 KB, style guide, grid-markers) which EVERY agent
        pays. Eras 3-7 would likely die the same way. Era 3's research is already in hand
        from the digest, so this should land comfortably.
NEXT:   Then eras 6-7, then 8-10.
RESULT: DONE, and the continuation worked. Agent a3772ba243cfe6bc3, 263,149 tokens, 112 tool
        uses, 23 min. Validator clean, files written incrementally throughout.
        MEASURED: bank 2,026 -> 10,733 words (bank now EXCEEDS outline, 10,733 vs 6,918 - a
        chapter-level bar met early). Outline 3,275 -> 6,918. [VERIFY] 66 -> 56. Stories
        17 -> 19, verified 6 -> 10.
        SOURCED: Boston Latin (opened 23 Apr 1635, town meeting 13 Apr, Philemon Pormort,
        record quoted); New England Primer (Harris 1687-90 per AAS, no surviving copy before
        1727); the spare-the-rod chain (Aelfric -> Wycliffe 1382 -> Skelton -> Hudibras, date
        left disputed); the 1642 and 1647 Massachusetts laws; Harvard 1636 and the Indian
        College; Natick and Monequassun; SPG 1701 and Bray Associates 1724; the Charleston
        school of 1743; South Carolina's Negro Act sec XLV; signature-based literacy figures;
        Jefferson's 1779 bill and "raked from the rubbish"; Land Ordinance sec 16; the girls'
        academies; the Williamsburg Bray School and Ann Wager.
        FIVE STORIES VERIFIED: Ezekiel Cheever, Caleb Cheeshahteaumuck, Christopher Dock,
        Ann Wager, Noah Webster (whose tag previously had NO bank behind it).
        TWO SEED ERRORS FIXED: the seed put anti-literacy laws in the 1600s (none existed;
        the first is 1740 and covers writing only), and placed Franklin's academy wholly in
        1700-1750 (Proposals 1749, school 1751).
        LEFT UNSETTLED, stated as disputed rather than hedged: whether the SPG bought Harry
        and Andrew; Indian College demolition 1695 vs 1698; Bray pupil counts.
        HANDED FORWARD: new PART A-FWD section in the bank (Webster's 1828 dictionary;
        Virginia's 1804/1819/1831 laws with wording; the lead on the Bray School's 86 named
        pupils).

*** DEFECT IN OUR OWN CHECK, found by this agent ***
        It reports that Horace Mann, Catharine Beecher, Booker T. Washington and John Dewey
        are tagged status="verified" with NOTHING in the bank behind them - and
        project_state.py's suspect_verified came back EMPTY. The check only flags a verified
        story whose own text still carries a [VERIFY] tag. A story that is confidently
        verified and simply unsourced passes silently. That is the art-music failure mode in
        a form our gate cannot see. All four sit in eras 6-7, so T-215 owns them. Whether the
        check can be strengthened is a real question - "is this claim in the bank" is a
        judgement, not a string match, which is exactly the case for an AI reading it.

### 2026-09-08 | T-215 | Research education ERAS 6-7 (1800-1850, 1850-1900)
STATUS: IN-FLIGHT
VERIFY: eras 6-7 end with 0 target, 0 candidate, 0 [VERIFY], every claim sourced. Chapter
        check still FAILs (eras 8-10 remain). Judge by the two eras.
EXPECT: 17 [VERIFY] and 6 stories. Carries the four confidently-verified-but-unsourced
        stories T-214 found: Horace Mann, Catharine Beecher, Booker T. Washington (Dewey is
        era 8, flag it forward). Bank already exceeds outline, so weight is not the issue -
        sourcing is. PART A-FWD in the bank holds leads it should use.
NEXT:   Then eras 8, 9, 10 - one at a time.
RESULT: KILLED by the session limit at the very last step, then FULLY RECOVERED BY SALVAGE.
        Agent a801153b91db2a97c, 289,814 tokens, 149 tool uses, 27 min. Its last words were
        "Now I'll rewrite the two eras in the outline."
        WHAT IT HAD DONE: bank 10,733 -> 23,360 words (+12,627, all era 6-7 research), written
        incrementally to the real file, so all of it survived. The OUTLINE was untouched -
        it had staged the rewrite in scratchpad files and died before merging.
        THE SALVAGE: scratchpad/eras67.md held a COMPLETE, FINISHED rewrite of both eras -
        271 lines, both hb-time blocks opened and closed, 8 stories ALL verified, ZERO
        [VERIFY] tags, all slugs globally unique. The agent had finished the job and was
        killed between writing the staging file and pasting it in.
        THE DIRECTOR MERGED IT - no replacement agent, no re-research. merge_eras67.py located
        the target block BY CONTENT not line number, asserted the span swallowed no other era,
        asserted the replacement was exactly two complete eras with balanced story blocks and
        no VERIFY tags, and kept a .bak-premerge. Replaced 76 lines with 271.
        RESULT: validator 0 errors, 21 stories. ERAS 1-7 ARE NOW COMPLETE - 0 [VERIFY],
        every story verified. Chapter: 39 [VERIFY] left (all in eras 8-10), 21 stories
        (15 verified, 1 candidate, 5 target), bank 23,360w vs outline 12,151w.
        The three unsourced-verified stories are resolved: Horace Mann, Catharine Beecher and
        Booker T. Washington are now sourced, alongside five new ones - Mary Swift, Sarah
        Roberts, Charlotte Forten, Zitkala-Sa and Josephine Foster.
        *** THIS IS THE FIRST TIME SALVAGE RECOVERED A WHOLE AGENT'S OUTPUT. *** 290k tokens
        of work reclaimed for the cost of one director merge. The transcript-and-scratchpad
        discipline paid for itself outright.
        LESSON FOR EVERY FUTURE BRIEF: staging the outline and merging at the end is what
        nearly lost this. Agents must edit the REAL outline file one era at a time, as soon
        as that era's research is done. That turns "died before the merge" into "two eras
        merged, one not".
        SendMessage retested in the same session with nothing restarted and a resumable agent
        in scope: "No matching deferred tools found." Conclusive for this build.

### 2026-09-08 | T-216 | Research education ERA 8 ONLY (1900-1950)
STATUS: IN-FLIGHT
VERIFY: era 8 ends with 0 target, 0 candidate, 0 [VERIFY], every claim sourced, and no
        verified story lacking bank backing. Chapter check still FAILs (eras 9-10 remain).
EXPECT: 9 [VERIFY], 3 stories (1 verified, 2 target). Carries JOHN DEWEY, the fourth
        confidently-verified-but-unsourced story T-214 found.
        SIZING: one era, deliberately. T-215 took 289k tokens for two eras with 17 [VERIFY]
        and only just failed to finish. Era 9 alone has 20 [VERIFY] and era 10 has 9, so the
        remaining work is three separate agents, not one or two.
NEXT:   era 9 (the biggest single era in the chapter), then era 10.
RESULT: DONE. Agent a0a9c93508a4c86d5, 322,657 tokens, 170 tool uses, 36 min. Validator clean.
        MEASURED: [VERIFY] 39 -> 29 (all 9 era-8 tags gone). Bank 23,360 -> 34,021 words.
        Outline -> 16,515. Stories 21 (17 verified, 1 candidate, 3 target).
        SOURCING QUALITY, notably primary: NCES "120 Years of American Education" tables
        2/9/12/13/14/19/20; THREE period school-board rulebooks read directly (San Francisco
        1910, New Haven 1910, Omaha 1909 - rattan and strap, witness required, monthly written
        return naming the child); Goldin's NBER paper checked against her own Table I;
        Terman's 1916 manual quoted word for word; four Supreme Court opinions read at Cornell
        LII (Buck, Pierce, Meyer, Gong Lum); the Meriam Report's own text.
        JOHN DEWEY: SOURCED, not demoted - sections 8a-8c now stand behind him (SIU chronology
        per date, Mayhew and Edwards for the school's size, his own two books). The other two
        era-8 stories were honest `target`s, so no false tags. All three era-8 stories now
        verified WITH bank sections behind them. That closes all four of the
        confidently-verified-but-unsourced stories found back at T-214.
        TARGETS FILLED: Mamie Garvin Fields (Pine Wood, a one-room school near Sumter, 1908,
        taught to 1943; papers at the Avery Research Center) and Sylvia Mendez.
        REFUSED TO INVENT: the "(target) a first-in-the-family high school graduate" slot is
        not fillable - nothing documents a named person of this era as that - so it replaced
        the slot rather than build a composite. Exactly right per the naming rule.
        LEFT UNSETTLED, stated in bank 8u rather than hedged in prose: the "desks bolted to
        the floor" claim (no period source; dropped and replaced with Dewey's own "these are
        all for listening"); no federal one-room-school count for 1900, so ~200,000 is
        labelled an estimate; the Rosenwald funding split; a sourced count of Black veterans
        refused college places.
        FOR THE AUDIT QUEUE - a cross-era date conflict it found and correctly did NOT touch:
        era 7 prints "180 normal schools by 1900" (Breitborde & Kolodny) while Labaree dates
        180 to 1910. One is wrong.
        ALSO: the workspace's 1800-1900 verify boxes are stale - the eras 6-7 agent resolved
        them but never ticked them. Chapter status line corrected (it still claimed eras 6-10
        were seed). New access blocks recorded: si.edu, guides.loc.gov, supreme.justia.com,
        oregonencyclopedia.org.
        HANDED FORWARD: PART D-FWD carries the one-teacher-school and special-education curves
        through 1990, the corporal-punishment sequence into Ingraham, the Buck v. Bell thread
        running to 1974, and the Warren sequence from Mendez 1947 to Brown 1954.

### 2026-09-09 | T-217 | Research education ERA 9 ONLY (1950-2000)
STATUS: IN-FLIGHT
VERIFY: era 9 ends with 0 target, 0 candidate, 0 [VERIFY], every claim sourced, no verified
        story lacking bank backing. Chapter check still FAILs (era 10 remains).
EXPECT: 20 [VERIFY] - the BIGGEST single era in the chapter - and 3 stories (2 target,
        1 candidate). Ruby Bridges belongs here per Jon's ruling. PART D-FWD in the bank
        holds threads era 8 prepared: Ingraham, Buck v. Bell to 1974, Mendez 1947 to Brown.
        SIZING NOTE: era 8 alone cost 322,657 tokens and 170 tool uses. Era 9 carries more
        than twice era 8's [VERIFY] load, so it is at real risk of being killed. The brief
        tells it to work strictly oldest-first and to write each item to the REAL files as
        soon as it is settled, so an interruption leaves a partial era rather than nothing.
NEXT:   finish era 9, then era 10.
RESULT: KILLED by the session limit, roughly HALF DONE, and nothing was lost.
        Agent a77febbdacccaece7, 267,936 tokens, 142 tool uses, 28 min. Last words: "Now the
        outline spans for this material."
        LANDED: era 9 [VERIFY] 20 -> 11. Bank 34,021 -> 41,415 words. Outline -> 20,808.
        Chapter candidates now 0. Verified 17 -> 18. RUBY BRIDGES IS DONE AND VERIFIED.
        SALVAGE VERDICT: NOTHING TO RECOVER - everything it produced is already on disk.
        Its four scratch files were checked line-by-line against both real files: o1.md was
        already merged into the outline (3/3 distinctive lines present), and chunk.md, a1.md
        and a2.md are bank content that had all landed (4/4 each). It wrote incrementally as
        instructed, which is exactly why there was nothing to rescue.

*** A FALSE POSITIVE IN OUR OWN SALVAGE TOOL - read this before trusting --wrote again ***
        --wrote reported "7 write(s) look INCOMPLETE ... treat those files as poison". THAT
        WAS WRONG. The agent reused two scratch FILENAMES (chunk.md, o1.md) for many
        successive writes, and --wrote compares each write's byte count against the file's
        CURRENT contents. Every earlier write to a reused name therefore looks short. The
        final write to each matched exactly (3866/3884 and 1832/1832) and the content was
        verified present in the real files.
        RULE: --wrote's SHORT! flag is only meaningful for a file written ONCE. When a
        filename appears more than once in its table, compare only the LAST write, and then
        confirm by checking whether the content actually reached the real files. Acting on
        that flag unexamined would have thrown away good work - the precise opposite of what
        the tool exists for.

### 2026-09-09 | T-218 | Research education, FINISH ERA 9 (1950-2000)
STATUS: IN-FLIGHT
VERIFY: era 9 ends with 0 target, 0 candidate, 0 [VERIFY]. Chapter check still FAILs (era 10).
EXPECT: 11 [VERIFY] and 2 target stories left, enumerated in the brief so the agent does not
        spend budget rediscovering them: Ingraham; the corporal-punishment ban sequence and
        the 1971 state; the first magnet school; segregation academies and named examples;
        the parochial enrollment peak; Minnesota's 1991 charter law and the first school;
        homeschooling prosecutions, its two roots, and the last state to legalise. Targets:
        a special-education student or parent, and a homeschooling family taken to court.
        Ruby Bridges is already done - leave her.
NEXT:   era 10, then education should finally PASS.
RESULT: DONE. Agent a5c510d484a9ea418, 241,056 tokens, 121 tool uses, 24 min. Validator clean.
        MEASURED: era 9 fully cleared. Chapter [VERIFY] 20 -> 9 (all remaining are era 10).
        Candidates 0, targets 3 -> 1. Verified 18 -> 20. Bank 41,415 -> 47,507 words.
        SOURCED: Ingraham v. Wright, 430 U.S. 651, decided 19 Apr 1977, 5-4, with the named
        children James Ingraham and Roosevelt Andrews, Drew Junior High, Dade County, Oct
        1970, the paddle, the hematoma, and White's dissent. The ban sequence (Gershoff &
        Font): New Jersey 1867 stood ALONE for 104 years; Massachusetts 1971; HI 1973, ME
        1975 ... WV 1994; then nothing until 2003. 27 states + DC by 1994, 23 states still
        lawful at century's end, 4% of schoolchildren hit in 1978. First magnet school:
        McCarver Elementary, Tacoma, autumn 1968. Segregation academies with named examples
        (Citizens' Council School No. 1, Jackson 1964). Catholic enrollment peak 1964-65 at
        5,601,000 in 13,249 schools, down to 2,475,439 by 1990-91. Minnesota's 1991 law
        (ch. 265, one-vote margin, 8-school cap) and City Academy, St Paul, autumn 1992,
        founder Milo Cutter. Homeschooling prosecutions: State v. Riddle (W.Va. 1981),
        Delconte (N.C. 1985), DeJonge (Mich. 1993). Roots: John Holt (GWS, Aug 1977) and
        Raymond and Dorothy Moore.
        REFUSED TO STATE WHAT THE RECORD WILL NOT CARRY: the "last state to legalise
        homeschooling" - Gaither and CRHE call it "fifty different stories" and name no last
        state, and the "all fifty by 1993" line traces only to HSLDA. Kept out rather than
        hedged. Also dropped as unsourced: the origin of the phrase "segregation academy",
        City Academy's exact opening day, a 2000 parochial figure.
        CORRECTIONS: the seed's "illegal in most states" premise overstates the record
        (Gaither: "illegal or dubious"); the parked "Massachusetts 1971 or 1972" hedge is
        resolved to 1971.
        *** A RESEARCH TRAP WORTH REMEMBERING: a fetch returned 1971/1973/1975 as
        1871/1873/1875. *** The agent caught it. A century-shifted date reads perfectly
        plausibly in a history book and no validator would ever see it.
        ADDED, unprompted and correctly: a span "The children who were not let in at all"
        (Mills 1972; P.L. 94-142; NCES Table 12) - era 9 had a special-education story slot
        and no span to hold it. Stories filled: Peter Mills, and Mark and Chris DeJonge.

### 2026-09-09 | T-219 | Research education ERA 10 (2000-today) - THE LAST ONE
STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check education --stage research SHOULD FINALLY PASS.
        This is the first chapter to complete under the three-phase plan.
EXPECT: 9 [VERIFY] and 1 target. Almost all of it is CURRENT-FIGURE work - NCLB 2001 and its
        2015 replacement, charter share, vouchers and ESAs, parochial and private enrollment
        now, homeschooling growth including the 2020 jump, how states check it, school
        calendar experiments, and the most recent suspension and expulsion figures. The
        ROADMAP's perishable-facts rule applies: every figure must carry its source year and
        must not be stale.
RESULT: *** PASS. EDUCATION IS COMPLETE - THE FIRST CHAPTER FINISHED UNDER THE THREE-PHASE
        PLAN. *** Agent a4293e810cadeada1, 276,478 tokens, 149 tool uses, 28 min.
        FINAL: 21 stories, ALL verified. 0 [VERIFY]. Bank 54,368w vs outline 26,723w.
        Validator 0 errors. stage=RESEARCHED.
        Every era-10 figure carries the year it describes AND its publication year, as the
        perishable-facts rule requires: NCLB = P.L. 107-110, approved 8 Jan 2002; replaced by
        the Every Student Succeeds Act, signed 10 Dec 2015. Charters 7.6% of public pupils
        2022-23 (NCES, Feb 2024 - no 2023-24 table exists). Private/parochial 4.7M, 9%, autumn
        2021 (pub. May 2024). Vouchers/ESAs 69 programmes, ~1,162,000 children 2024-25
        (EdChoice, LABELLED AS AN ADVOCATE - good practice). Homeschooling 2.8% in 2019 ->
        5.4-11.1% across 2020 -> 5.82% in 2022-23 and it stayed. State oversight: 12 states
        require no notice, 29 no assessment ever, 22 no records. Calendar: 180 days in 27
        states + DC; year-round schooling SHRANK 4.4% -> 2.5%; four-day week ~2,100 schools.
        Discipline from CRDC 2021-22, released Jan 2025, the newest that exists - and the
        outline SAYS the 2023-24 collection is still unpublished. ~24,500 children hit; Black
        boys 8% of enrolment but 22% of out-of-school suspensions and 21% of expulsions;
        disabled children 17%/29%/24%; Black children 15% of enrolment and 33% of school
        arrests. Source disagreement on the state count stated, not resolved.
        TARGET FILLED: Tabatha Rosproy, 2020 National Teacher of the Year, Winfield, Kansas.
        LEFT OUT because unsettled: whether testing or vouchers raise achievement; the exact
        May 2020 announcement date; a single agreed state count for corporal punishment; the
        federal student-debt total.
        FOUND: the APSAC alert says "Fifteen states" then lists fourteen - flagged in the bank
        so nobody reprints it. And a bad chapter cross-reference `medicine-health`, which is
        not a slug (the chapter is `health`). DIRECTOR FIXED that one directly - single
        occurrence, book-wide grep confirmed; education re-validated and still PASSes.

### 2026-09-09 | CHAPTER COMPLETE | education
Seven dispatches (T-213..T-219), three of them killed by usage limits, ~1.78M subagent tokens.
One kill was fully recovered by salvage (T-215's finished outline rewrite, merged by the
director with no replacement agent). Research state 5 clean -> 6.
SIZING LESSON, now evidence-backed: the sustainable load is roughly 9-11 [VERIFY] plus 2-4
stories per agent, at 240k-330k tokens each. Two eras with 17 [VERIFY] was too much and died
just short of finishing. Plan every remaining chapter against that number, not against
chapter boundaries.

### 2026-09-09 | T-220 | Research rights-movements ERAS 1-6 (before-1500 .. 1800-1850)
STATUS: IN-FLIGHT
VERIFY: eras 1-6 end with 0 target, 0 candidate, 0 [VERIFY]. Chapter check FAILs until 7-10.
EXPECT: chapter is a SEED - 26 [VERIFY] and 21 stories of which NOT ONE is verified (16
        candidate, 5 target). Bank 2,717w vs outline 1,530w. But ~18.9 KB of material is
        parked here from nine other chapters, so the groundwork is better than it looks.
        This slice: 8 [VERIFY], 6 stories. Eras 1-5 are nearly empty (2 stories, 1 tag) and
        may legitimately stay thin; era 6 carries most of the weight.
RESULT: KILLED by the session limit before it finished. Agent aa41f8911f1cd4ade, 152,745
        tokens, 43 tool uses, 8 min. Last words: "Now I'll write. Bank first, then the
        outline, era by era."
        LANDED: bank 2,717 -> 3,836 words (an "ERAS 1-6 RESEARCHED" section and a "The 1500s
        - thin on purpose" section); outline 1,530 -> 2,192 words of era-zoom prose.
        NOT DONE: no [VERIFY] tag cleared, no story upgraded. Outline structure identical.
        Digest: workspace/handover-rights-movements-eras1-6.md, 113 KB, 80 sources, 38
        gathered results - Anne Hutchinson's full trial sequence from NPS, coverture,
        Haudenosaunee clan mothers, Mary Dyer. Handed to T-221.

*** SECOND FALSE SIGNAL FROM --wrote IN TWO RECOVERIES - AND THIS ONE WAS DANGEROUS ***
        It printed "Agent aa41f8911f1cd4ade issued no Write/Edit calls", which reads as
        NOTHING WAS WRITTEN. That was false: the agent had appended ~1,100 words to the bank
        and ~660 to the outline entirely through BASH HEREDOCS and inline python. --wrote only
        ever inspected Write/Edit/NotebookEdit tool calls and was blind to all of it. Acting
        on that line unexamined would have discarded real work - the exact opposite of the
        tool's purpose. It was caught only because the director measured the files
        independently and found numbers that contradicted the tool.
        FIXED: cmd_wrote now scans Bash commands for >>, >, sed -i, tee and heredocs, prints
        them, and refuses to say "nothing was written" when any exist. Verified: it now
        reports 4 write-capable Bash calls for this agent and says DO NOT read this as
        'nothing was written'. Measure the files.
        THE RULE, now proven twice: --wrote is EVIDENCE, NOT A VERDICT. Always measure disk
        state with project_state.py independently. The first false signal (T-217) said good
        files were "poison"; this one said written work did not exist.

### 2026-09-09 | T-221 | Research rights-movements ERAS 1-6, CONTINUATION
STATUS: IN-FLIGHT
VERIFY: eras 1-6 end with 0 target, 0 candidate, 0 [VERIFY]. Chapter FAILs until 7-10.
EXPECT: 8 [VERIFY] and 6 stories, none yet done. Gets the 113 KB digest so it does not re-run
        80 sources of research already paid for. Early-era bank sections already written.
RESULT:





---

## 2026-09-09 — `education` era 9 (1950-2000) FINISHED (second era-9 agent)

The first era-9 agent was stopped by a usage limit with eleven `[VERIFY]` tags and two `target` story
slots left. All thirteen are now closed. Era 9 measures **0 `[VERIFY]`, 0 target, 0 candidate**;
`progress` is now `researched`. Validator: 0 errors. `project_state.py --check education --stage
research` still FAILs, correctly, on era 10, which is untouched and belongs to the next agent.

**Bank grew from 41,415 to 47,507 words.** New sections: **§9l** (corporal punishment), **§9m** (kinds
of school), **§9n** and **§9o** (homeschooling, and the DeJonge family), **§9p** (children excluded
from school, *Mills*, and P.L. 94-142).

**Three things later agents should know.**

1. **A verification trap.** A fetch of Gershoff and Font's state-ban table returned Massachusetts as
   **1871**, Hawaii **1873**, Maine **1875**. Asked to copy the digits verbatim, the same page gave
   **1971, 1973, 1975**. When a century looks surprising, demand the digits verbatim.
2. **A seed premise was wrong.** The seed said homeschooling was "illegal or effectively illegal in
   most states into the 1980s." Milton Gaither — the only scholar with a book-length history of it —
   writes that the old laws made it "either illegal or dubious," and the Coalition for Responsible
   Home Education says it was lawful everywhere but sometimes very tightly regulated. The outline now
   says what is documented: parents were prosecuted under compulsory-attendance laws, and three named
   families with court records are given.
3. **One of the eleven items could not be settled and was left out rather than hedged.** "The last
   state to legalise homeschooling, and the year" has no source behind it: the historians describe
   fifty separate stories and decline to name a last state. Reasoning and the route to settling it are
   in bank §9n and workspace/education.md.

**A span was added** — "The children who were not let in at all" — because era 9 had a `target` slot
for a special-education child and no span to hold one, and the 1975 Act, parked for era 9 by the era-8
agent, was missing from the chapter entirely.

**Access findings:** law.justia.com and leagle.com both 403; **case-law.vlex.com works** and was the
route to three opinions. encyclopediaofarkansas.net is Cloudflare-blocked. education.jhu.edu 403s.
mississippiencyclopedia.org truncates for WebFetch but `curl` plus a tag-strip returns whole entries.

### 2026-09-09 | T-226 | Research government-politics ERAS 1-8 (before-1500 .. 1900-1950)
STATUS: IN-FLIGHT
VERIFY: eras 1-8 end with 0 target, 0 candidate, 0 [VERIFY], and NO verified story without
        bank backing. Chapter FAILs until eras 9-10.
EXPECT: 10 [VERIFY] and 4 unfilled stories in this slice - right at the sustainable load.
        *** THE REAL RISK HERE IS THE OPPOSITE OF THE USUAL ONE. *** The chapter already
        claims NINE verified stories on a bank of 1,983 words. Nine properly sourced stories
        cannot fit in 1,983 words, so most of those tags are almost certainly standing on
        nothing - the education failure mode, at scale. The brief tells the agent to audit
        every inherited `verified` tag in its eras and demote what the bank does not carry.
        Bank must also grow past the outline (1,983 vs 1,330 now, both will rise).
NEXT:   eras 9-10 (12 [VERIFY], 1 target), then the chapter should PASS.
RESULT: DONE - killed during optional enrichment after the slice was already complete.
        Agent a2291dc2080d60800, 234,776 tokens, 109 tool uses, 19 min. Validator clean.
        MEASURED: eras 1-8 fully cleared - all 10 [VERIFY] gone, every story verified.
        Bank 1,983 -> 8,619 words (4.3x). Outline 1,330 -> 6,633. Stories 14, verified 9 ->
        13, candidates 0. Chapter now 12 [VERIFY] and 1 target, eras 9-10 only.
        THE UNSOURCED-VERIFIED AUDIT: it sourced rather than demoted. The bank going from
        1,983 to 8,619 words while verified went 9 -> 13 is consistent with real sourcing
        behind the inherited tags rather than tags left standing on nothing.
        Its last act was a Cloudflare "Just a moment..." challenge on blogs.loc.gov while
        chasing Haudenosaunee-and-the-Constitution material for era 1 - a thin era with no
        story and no tags, so enrichment, not the bar.
        NEW ACCESS BLOCK: blogs.loc.gov sits behind Cloudflare and returns a challenge page
        to curl even with a browser user-agent. Added to the do-not-waste-calls list.
        SALVAGE VERDICT: nothing to recover.

### 2026-09-10 | T-227 | Research government-politics ERAS 9-10 - LAST SLICE
STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check government-politics --stage research SHOULD
        PASS. Third chapter complete under the three-phase plan.
EXPECT: 12 [VERIFY] (9 in era 9, 3 in era 10) and 1 target story in era 10. Era 9's two
        stories arrive already tagged verified - audit them against the bank, as era 1-8's
        agent had to. Era 10 is current-figure work, so every figure carries the year it
        describes and its source year.
RESULT: *** PASS. GOVERNMENT-POLITICS COMPLETE - third chapter under the three-phase plan. ***
        Agent a8930fa31176d883d, 310,353 tokens, 187 tool uses, 30 min.
        FINAL: 14 stories all verified, 0 [VERIFY], bank 19,177w vs outline 11,283w.
        *** THE AUDIT INSTRUCTION PAID OFF: BOTH inherited era-9 `verified` tags were FALSE. ***
        thurgood-marshall and lyndon-b-johnson were ONE-LINE STUBS with zero bank backing -
        the bank's chapter research covered eras 3-8 only. Both now sourced (FJC, senate.gov,
        uscourts.gov, NPS) and rewritten as full story blocks. It also found eras 1 AND 2 at
        progress="seed" with no bank entry at all, sourced them, and fixed flags on eras
        1, 2, 9, 10.
        THIS IS NOW TWICE CONFIRMED: a `verified` tag in an unresearched chapter means
        nothing. Every future brief for a seed chapter must order the audit explicitly.
        FOUR ERRORS FOUND IN SOURCES: a fetched summary called Stewart a Rodriguez DISSENTER
        (he concurred); another called Espinoza 6-3 with Kagan in the majority (it is 5-4,
        checked against the slip opinion); NCES dates ESEA 12 April 1965 while the statute
        says 11 April; the famous Parents Involved line was joined by FOUR justices, not five
        - Kennedy's concurrence controls. Also: "Michigan, last state, 1993" hides People v.
        Bennett, decided the same day AGAINST non-religious homeschoolers.
        NOT SETTLED, kept out: the Freeman v. Giuliani jury figure (no government record
        carries it); the Haudenosaunee founding date; whether Trump named Ruby Freeman 18 or
        19 times (both figures appear in government records).
        TARGET FILLED: Wandrea ArShaye "Shaye" Moss, Fulton County election worker - sworn
        House testimony 21 June 2022 plus the Freeman v. Giuliani docket. Slug checked
        against all 630 in the book.

### 2026-09-10 | CHAPTER COMPLETE | government-politics
Two dispatches (T-226, T-227), one killed during enrichment. Research state 7 clean -> 8.
Batch A is now 3 of 4 done; only `religion` remains in it.



### 2026-09-10 | T-228 | Research religion ERAS 1-5 (before-1500 .. 1750-1800)
STATUS: IN-FLIGHT
VERIFY: eras 1-5 end with 0 target, 0 candidate, 0 [VERIFY]. Chapter FAILs until 6-10.
EXPECT: a TRUE from-scratch chapter - bank is 289 words against a 1,443-word outline, and NOT
        ONE of its 15 stories is verified. No inherited-tag audit needed here; there is
        nothing to audit. This slice: 8 [VERIFY], 5 stories.
        Planned split, at the sustainable load: 1-5 (8 tags, 5 stories), 6-8 (13 tags,
        4 stories), 9-10 (10 tags, 4 stories).
NEXT:   eras 5-7, then 8-10, then the chapter should PASS and Batch A is finished.
RESULT: PARTIAL - 4 of its 5 eras done. Agent a6a3aadc06e23edf6, 306,867 tokens, 101 tool
        uses, 28 min. Killed with era 5 (1750-1800) untouched.
        MEASURED: before-1500, 1500s, 1600s and 1700-1750 all cleared - 0 [VERIFY], 5 stories
        verified. Bank 289 -> 9,748 words (34x). Outline 1,443 -> 7,056. Validator clean.
        Bank already exceeds outline, so the weight bar is met for the whole chapter.
        Its last words were "Now the 1700-1750 outline cell" and that cell measures clean, so
        the write landed and it died after. Nothing to salvage.
        REMAINING: 26 [VERIFY], 6 candidate, 4 target across eras 5-10.

### 2026-09-10 | T-229 | Research religion ERAS 5-7 (1750-1800, 1800-1850, 1850-1900)
STATUS: IN-FLIGHT
VERIFY: eras 5-7 end with 0 target, 0 candidate, 0 [VERIFY]. Chapter FAILs until 8-10.
EXPECT: 11 [VERIFY] and 5 stories - at the sustainable load. Era 5 was left untouched by
        T-228 and is first.
NEXT:   eras 8-9, then era 10, then the chapter should PASS and Batch A is done.
RESULT: DONE. Agent ab3198b6878209d6c, 372,277 tokens, 176 tool uses, 38 min. Validator clean.
        MEASURED: eras 5-7 cleared. Bank 9,748 -> 21,264w, outline 7,056 -> 13,839. Stories
        verified 5 -> 10. Remaining: 15 [VERIFY], 2 candidate, 3 target, eras 8-10.
        SOURCED: the Virginia assessment fight with both sides named and dated (Henry's bill
        24 Dec 1784, Madison's Memorial June 1785, the statute 16/19 Jan 1786) - and it
        included WASHINGTON'S LETTER BACKING A RELIGIOUS TAX so the founders are not written
        as one voice. That is the honest-history instinct working without being asked.
        Massachusetts Article III's own text and Amendment XI 1833. Sunday schools as READING
        schools (First Day Society 1791; 43 schools / 5,970 pupils by 1818). The Philadelphia
        Bible riots 1842-44 with the "without note or comment" rule that banned the Douay.
        Boggs's extermination order and Haun's Mill - 18 killed, ~8,000 expelled, rescinded
        1976. Charles Colcock Jones's 1842 obedience verses set against Douglass's own account
        of Thomas Auld, the broken-up Sabbath school, and the whipping of Henny with the verse
        quoted over it. The 1883 Rules Governing the Court of Indian Offenses QUOTED, with
        rations withheld as the penalty, enforceable until 1978. The DOI 2024 count: 210 of
        417 boarding schools church-run, 132 Protestant / 77 Catholic / 5 other, 59 bodies.
        STORIES: Richard Allen, Absalom Jones, Charles Grandison Finney, Joseph Smith.
        Replaced the freedpeoples-minister target with GARRISON FRAZIER, because the 12 Jan
        1865 Savannah minutes document twenty ministers' ages, birthplaces, manumissions and
        congregation sizes plus Frazier's own words. Slugs checked against all 1,215.
        REFUSED TO FAKE A VOICE: it wanted a first-hand enslaved account of secret worship,
        found loc.gov's Born in Slavery Cloudflare-blocked, and would not quote an unnamed
        narrator. Left as a gap rather than an assertion. Same for Moody, the Salvation Army
        and the Social Gospel - named in the seed, unsourced, so kept OUT of the outline.
        CUT RATHER THAN HEDGED: the parochial-staffing/low-pay line.
        FOUND WRONG: the bank header claimed era 5 was researched when no era-5 section
        existed. LOC's rel07 gives 1815 for the AME founding and makes Jones a priest in 1795,
        both conflicting with the National Archives / Episcopal Archives dates the outline
        uses - flagged in 6h rather than silently picked.
        HANDED FORWARD: Nicholas Black Elk is already verified in 7e and native-nations left
        him open - a strong 1900-1950 slot. The 2022/2023/2024 church apologies are already
        verified for era 10.

### 2026-09-10 | T-230 | Research religion ERAS 8-9 (1900-1950, 1950-2000)
STATUS: IN-FLIGHT
VERIFY: eras 8-9 end with 0 target, 0 candidate, 0 [VERIFY]. Chapter FAILs until era 10.
EXPECT: 10 [VERIFY] and 4 stories. Inherits Nicholas Black Elk, already verified in bank 7e
        and left open by native-nations - a ready era-8 slot.
NEXT:   era 10 (5 tags, 1 target; its church-apology material is already verified), then the
        chapter should PASS and Batch A is finished.
RESULT: PARTIAL - era 8 complete, era 9 about half. Agent a466bc89fb4052aef, 306,460 tokens,
        160 tool uses, 32 min. Validator clean.
        MEASURED: era 8 cleared - 0 [VERIFY], 3 stories verified (it added two). Era 9 went
        5 -> 3 [VERIFY] with its 3 stories still unfilled. Bank 21,264 -> 27,554w, outline
        13,839 -> 16,407. Chapter now 8 [VERIFY], 1 candidate, 3 target.
        Nothing to salvage - it died writing an era-9 outline span, and era 9's measured
        state is consistent with the writes that landed.

### 2026-09-10 | T-231 | Research religion ERAS 9-10 - LAST SLICE
STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check religion --stage research SHOULD PASS. Fourth
        chapter complete, and Batch A finished.
EXPECT: 8 [VERIFY] and 4 stories. Era 10's church-apology material (2022/2023/2024) is
        already verified in bank 7e. Last agent on the chapter, so it also audits every era's
        progress= flag.
RESULT: *** PASS. RELIGION COMPLETE - fourth chapter, and BATCH A IS FINISHED. ***
        Agent a30c8cb662629d7db, 412,231 tokens, 202 tool uses, 42 min.
        FINAL: 18 stories all verified, 0 [VERIFY], bank 39,755w vs outline 22,144w.
        SOURCED: Epperson (1968) and Edwards v. Aguillard (1987) from the SCANNED U.S.
        Reports, with the amicus split showing religious bodies on BOTH sides - the same
        not-one-voice instinct the era 5-7 agent showed with Washington. The Kanawha County
        textbook fight 1974-77. Wisconsin v. Yoder (1972) including Frieda Yoder's OWN
        testimony and Douglas's partial dissent. The 1954 Pledge and 1956 motto statutes from
        the Statutes at Large. AIRFA 1978, Employment Div. v. Smith (1990), the 1994 peyote
        amendment. Bethel Baptist from the NPS National Historic Landmark nomination. Era 10
        with source years throughout: Pew (survey 2023-24, published Feb 2025), Gallup (2021),
        Carson v. Makin and Kennedy v. Bremerton (2022), Roake v. Brumley (5th Cir. en banc,
        20 Feb 2026), NCES 2024-113 (data 2022-23, published Sept 2024), CARA (1 Jan 2025),
        the John Jay report (2004), the Pennsylvania grand jury (2018).
        LEFT OUT RATHER THAN HEDGED: Kanawha casualty counts; Graham's Chattanooga rope story
        (memoir only); whether Louisiana's law is constitutional (NO COURT HAS SAID - exactly
        the right refusal); a state-by-state count of classroom-display laws. Alice Moore's
        denomination: two sources disagree, BOTH recorded.
        BIGGEST KNOWN GAP, flagged not faked: the evangelical political movement after 1979,
        unsourced and therefore unwritten. Mozert v. Hawkins County unreachable - openjurist,
        law.justia and CourtListener opinion pages all blocked.
        STORIES: billy-graham candidate->verified. civil-rights-congregation replaced by the
        REVIS FAMILY at Bethel - deacon James Revis and his daughters Laverne and Robbie, from
        the NHL nomination and BCRI oral histories. curriculum-objector-parent replaced by
        Jonas and Frieda Yoder. school-faith-dispute-account filled as Joseph Kennedy.
        Added Harpreet Singh Saini. All 18 slugs checked against 615 book-wide.
        FLAGS: eras 9 and 10 were progress="seed"; both fixed. All ten checked individually.
        THIRD CHAPTER RUNNING WHERE THE LAGGING-FLAG DEFECT APPEARED. The extra brief line is
        earning its place.
        FOUND WRONG: four stale cross-chapter LINE references in the bank (education.md:266-274,
        :86, :290-294; government-politics.md:82) pointed at the wrong lines - corrected.
        NOTE FOR PHASE 3: line-number cross-references rot every time a chapter is edited.
        Every completed chapter invalidates some of them. They should probably be slug-and-
        heading references instead. AUDIT ITEM.

### 2026-09-10 | BATCH A COMPLETE | education, rights-movements, government-politics, religion
Four chapters, 19 dispatches (T-213..T-231), 10 killed by usage limits, 3 of those fully
recovered by salvage rather than re-dispatch. Research state 5 clean -> 9 of 37.





### 2026-09-10 | BATCH B BEGINS | war, health, disasters, crime-justice, drugs-alcohol

### 2026-09-10 | T-232 | Research war ERAS 1-6 (before-1500 .. 1800-1850)
STATUS: IN-FLIGHT
VERIFY: eras 1-6 end with 0 target, 0 candidate, 0 [VERIFY]. Chapter FAILs until 7-10.
EXPECT: SHAPED DIFFERENTLY from Batch A. Only 4 [VERIFY] chapter-wide, but 13 stories and NOT
        ONE verified, on an outline of just 824 words against a 1,453-word bank. The low tag
        count is not progress - it means the outline is barely written. This agent must BUILD
        the outline out, not merely verify it. This slice: 3 tags, 4 stories.
        Planned split: 1-6 (4 stories), 7-8 (6 stories), 9-10 (3 stories). Stories are the
        cost driver, not tags.
RESULT:
        [Closed 2026-09-26 in the CLOUD from measurement. The agent never reported and its
        transcript stayed on Jon's PC.]
        PARTIAL. Eras 1-4 landed and eras 5-6 did not start. Measured:
        check FAIL, stage=PARTIAL, stories 14 (v2 c2 t10), [VERIFY] 1, bank 7,006w vs outline
        4,293w, validator 0 errors. Era flags: before-1500, 1500s, 1600s and 1700-1750 are
        "researched". Eras 5-10 are still "seed". The bank holds sections 1-4 (Crow Creek, Norris
        Farms, Mabila, Tiguex, Fort Caroline, Pequot, King Philip's War, Deerfield, and the
        John and Eunice Williams stories). Eras 1-3 carry no story; the bank's "story slot"
        sections say why. The remaining work is eras 5-10 and goes to T-233.

### 2026-09-26 | [CLOUD] PROJECT MOVED TO ANTHROPIC'S SERVERS
Jon uploaded the repo to GitHub (jonnystokes/USA-History-grid-book) to use a $100 cloud-usage
gift in Claude Code on the web. Branch: claude/gifted-volta-lfl54k. Never push to main.
SETUP: tools/env_check.py reports CLOUD or LOCAL. control/CLOUD-WORKFLOW.md holds the cloud
rules. control/TODO.md is the live plan. control/checkpoints/ holds per-task resume files, and
agents commit and push after every unit. CLAUDE.md, RESUME.md, README.md, AGENT-BRIEF.md and
writing-style-guide.md gained the environment switch. Nothing local was removed.
BLOCKER: the general style guide (C:\Users\jon\Projects\writing-style-guide.md) is not in the
repo. Jon is to add it as control/general-writing-style-guide.md.
WAITING: Jon's go-ahead on the plan in control/TODO.md.

### 2026-09-26 | [CLOUD] WRITING STYLE GUIDE VERSION 2 ADOPTED
Jon's instruction: Version 2 is an absolute requirement. It is installed at
control/general-writing-style-guide.md and binds both environments. The v1 file on Jon's PC is
superseded. The v2 header was changed from "not yet approved" to "the live guide".
POINTERS UPDATED: CLAUDE.md (rewritten to follow v2), control/writing-style-guide.md
(the amendment gained a "Version 2 rules with a fixed meaning in this book" section. Three of
its Strong examples broke v2 and were fixed), hard-subjects-policy.md §5, §6b and §7 (rules now
cited by heading, a new check 9 for punctuation, a warning on the v1-era "after" examples),
AGENT-BRIEF.md §1 and §9, RESUME.md's research and writing briefs and its prose bar,
ROADMAP.md, CLOUD-WORKFLOW.md, project-notes.md, templates/chapter-template.md,
tools/env_check.py.
GATE CHANGED: project_state.py's prose bar now requires 0 em dashes (U+2014) and 0 semicolons
in reader-facing manuscript text. Marker lines, hb-note blocks and HTML entities are excluded.
MEASURED AFTER THE CHANGE: native-nations prose FAIL (emdash=74 semicolon=40). city-building
prose FAIL (emdash=83 semicolon=23). Everything else in both chapters still meets the bar.
CONFLICTS RESOLVED IN THE AMENDMENT, FOR JON TO CONFIRM:
  (1) Passives. v2 allows one when the actor is unknown or does not matter. The book adds that
      when someone was harmed, the actor always matters: name the actor, or state that the
      records do not say.
  (2) Rhetorical questions. CLAUDE.md banned them outright. v2 allows one as a section opener
      answered by the next sentence. v2 governs mechanics, so v2's limit now applies.
  (3) Sentence length. The amendment's 12-18-word average stands. v2's "vary length by
      information" is added to it.
PARKED: AUDIT-QUEUE "Added 2026-09-26".

### 2026-09-26 | [CLOUD] DOCS CLEANED, OPTION B CHOSEN
Jon chose Option B (writing first, for the chapters that are ready) and asked for the docs to be
cleaned first. Em dashes and semicolons were removed from RESUME, AGENT-BRIEF, ROADMAP, README,
the policy (its quoted v1-era examples are kept as cited), grid-markers §7b and
VIEWER-CONTRACT §2. Added project_state.py --punct <file>, and a standard REVISION brief in
RESUME.md.
QUEUE: T-233 native-nations v2 revision (3 agents) -> T-234 city-building v2 revision
(3 agents) -> T-235 war eras 5-10 -> prose for the 9 chapters that pass research.

### 2026-09-26 | [CLOUD] T-233a | Revise native-nations PART 1 (eras 1-5) to style guide v2
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-233-native-nations.md
VERIFY: python tools/project_state.py --punct manuscript/native-nations/part1-before-1800.md
        must print 0/0. The validator (--part) must be clean. The chapter check FAILs until
        parts 2 and 3 are done.
BASELINE: 4,592 prose words, 28 em dashes, 9 semicolons.
EXPECT: the first test of how an agent applies v2. Watch for word loss (lossy summarization)
        and for the punctuation-swap shortcut.
RESULT: DONE (part 1). 214,939 tokens, 53 tool uses, 12.5 min. Six commits, one per era plus
        a whole-file review.
        MEASURED: --punct emdash=0 semicolon=0 · validator (--part) 0 errors · every marker line
        and record key identical to the pre-revision file · prose words 4,592 -> 5,352 (+17%),
        so no sign of lost facts. The words went up because hard words were defined and named
        actors were added.
        REPORTED: about 40 personifications and agentless passives repaired, about 25 cadence
        moves, about 20 hard words defined, 3 hedges attributed, 1 withheld fact moved to the
        front. BEYOND STYLE: 3 self-contradictions fixed (Cahokia end dates, Paquiquineo record,
        treaty timing). The Comanche were wrongly called a confederacy. The Acoma dispute was
        told from one side. Bank facts were added and are listed in the checkpoint.
        Director check: the Acoma section is VERIFIED in the bank (2026-09-07). The ROADMAP and
        AUDIT-QUEUE "do not write" flag was stale and is now marked resolved.
        PARKED: the Pueblos' account of an assault on an Acoma woman needs a ruling from Jon.

### 2026-09-26 | [CLOUD] T-233b | Revise native-nations PART 2 (eras 6-7) to style guide v2
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-233-native-nations.md (units 6-7)
VERIFY: python tools/project_state.py --punct manuscript/native-nations/part2-1800s.md must print
        0/0. The validator (--part) must be clean.
BASELINE: 3,697 prose words, 27 em dashes, 18 semicolons.
RESULT: DONE (part 2). 192,517 tokens, 30 tool uses, 11.5 min. Three commits.
        MEASURED: --punct 0/0 · validator (--part) 0 errors · markers and record keys identical ·
        prose words 3,697 -> 4,517 (+22%).
        REPORTED: about 40 institutions made to act, now naming people. About 15 agentless
        passives, where "the sources do not identify who" is now stated where the bank names
        no one (the Mankato hanging, Crazy Horse's killing, Zitkala-Ša, Joseph's promise). About
        12 cadence moves. About 30 hard words defined. BEYOND STYLE: the Removal Act was framed
        as an answer to Tecumseh's confederacy, which had ended by 1813. The school system was
        dated 1879 in one place, although federal schools date from 1819. Joseph's route was
        cut short (now up to about 1,700 miles, per the bank). "Massacre" was missing for Sand
        Creek and Wounded Knee.
        PARKED: the bank does not name the parties in Worcester v. Georgia.

### 2026-09-26 | [CLOUD] T-233c | Revise native-nations PART 3 (eras 8-10) to style guide v2
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-233-native-nations.md (units 8-10)
VERIFY: python tools/project_state.py --check native-nations --stage prose SHOULD PASS once
        this part lands, because it is the last part.
BASELINE: 4,537 prose words, 19 em dashes, 13 semicolons.
RESULT: *** PASS. native-nations is the FIRST CHAPTER FINISHED UNDER STYLE GUIDE V2. ***
        209,014 tokens, 32 tool uses, 12 min. Four commits.
        PASS  native-nations / prose
          measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=21 (verified 21)
          ms_verify_tags=0 emdash=0 semicolon=0 manuscript=15624w files=3 validator_errors=0
        Part 3 prose words 4,537 -> 5,755. Markers and record keys identical. The chapter went
        from 12,826 to 15,624 words across the three parts.
        BEYOND STYLE: orders in Native languages were credited to "the United States", although
        Choctaw soldiers began the practice in 1918. The Alcatraz occupiers were called
        "students", which the bank does not support. ICWA's "a large share" of children taken
        had been dropped. The pipeline was placed "above" the water supply, but the lake is the
        water supply.
        PARKED: the 1973 Wounded Knee deaths. The bank says "died", and the prose says "killed",
        by people the sources do not identify.
T-233 COMPLETE: 3 agents, 616,470 tokens in all, about 37 minutes.

### 2026-09-26 | [CLOUD] T-234a | Revise city-building PART 1 (eras 1-5) to style guide v2
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-234-city-building.md (units 1-5)
VERIFY: --punct manuscript/city-building/part1-before-1800.md prints 0/0. The validator
        (--part) must be clean.
BASELINE: 3,810 prose words, 12 em dashes, 5 semicolons.
RESULT: DONE (part 1). 177,452 tokens, 36 tool uses, 9 min. Five commits.
        MEASURED: --punct 0/0 · validator (--part) 0 errors · markers and record keys identical ·
        prose words 3,810 -> 4,375 (+15%).
        BEYOND STYLE: "Congress passed" the Residence Act on July 16, 1790, but the bank says
        Washington signed it that day. Chaco's "those two dates" came before the 1140s date
        had appeared. An unsourced "workmen" (L'Enfant's reburial) was removed.
        PARKED: 3 unsourced claims, the unnamed nations on the 1600s town sites, and the span
        label "Fire, the city killer". The brief now allows revising label= text.

### 2026-09-26 | [CLOUD] T-234b | Revise city-building PART 2 (eras 6-7) to style guide v2
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-234-city-building.md (units 6-7)
VERIFY: --punct manuscript/city-building/part2-1800s.md prints 0/0. The validator (--part) must
        be clean.
BASELINE: 4,238 prose words, 23 em dashes, 6 semicolons.
RESULT: DONE (part 2). 174,022 tokens, 23 tool uses, 10 min. Two commits.
        MEASURED: --punct 0/0 · validator (--part) 0 errors · markers and record keys identical
        apart from 3 revised span labels (now allowed) · prose words 4,238 -> 4,856 (+15%).
        BEYOND STYLE: two LAND ERASURES. San Francisco was "a stretch of empty coast", but the
        bank has about 200 people there in 1846. At the land run, the ground was "thrown open"
        with no one named. The bank names neither the nation nor the takers, and the prose now
        says so. Rochester's "fifteen years" was fourteen. "About 9,200" is now 9,269. An
        implied 1890 date for Roosevelt as police commissioner was removed.
        FINDING: about 20 claims in part 2 (and 3 in part 1) are NOT in the bank, including
        most of the Olmsted story. The prose was written partly from the outline's inline notes.
        The checkpoint lists them all. PARKED as one research-patch item.

### 2026-09-26 | [CLOUD] T-234c | Revise city-building PART 3 (eras 8-10) to style guide v2
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-234-city-building.md (units 8-10)
VERIFY: python tools/project_state.py --check city-building --stage prose SHOULD PASS once this
        last part lands.
BASELINE: 5,720 prose words, 48 em dashes, 12 semicolons. This is the largest part.
RESULT: *** PASS. city-building passes prose under style guide v2. Both previously written
        chapters now meet the new standard. ***
        PASS  city-building / prose
          measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=14 (verified 14)
          ms_verify_tags=0 emdash=0 semicolon=0 manuscript=16080w files=3 validator_errors=0
        Part 3 prose words 5,720 -> 6,849. Markers identical apart from 11 revised labels.
        BEYOND STYLE: Oak Ridge LAND ERASURE was still present ("empty ridgeland", "Secret cities
        from nothing"). It now carries the bank's removals: about 1,000 families, the named
        communities, and the 1942 taking. The 300,000-family figure applied to urban renewal
        only, but the prose had put it on the freeways too. "Downtowns lost more than half" is
        now Detroit's 48.6%. "Tens of millions" of empty office square feet understated 900
        million. Superlatives were removed.
        UNSETTLED: Anderson's age ("eight in 1958" against "approaching 83 in 2022"). Both are
        stated and attributed to Sahan Journal. The bank wrongly says they agree.
        FINDING: about 55 more claims are not in the bank, about 78 across the chapter. They are
        listed in the checkpoint.
T-234 COMPLETE: 3 agents, 528,000 tokens in all, about 30 minutes.

### 2026-09-26 | [CLOUD] OPTION B STEP 0 COMPLETE, NUMBER PROBE ADDED
native-nations and city-building both PASS prose under style guide v2 (T-233, T-234). Six
agents, about 1.14M tokens. Added tools/bank_coverage.py (report only). Its first result: it
detects thin banks but not the qualitative unsourced claims city-building had. A proposal
that writers take facts only from the bank is in AUDIT-QUEUE, awaiting Jon.

### 2026-09-26 | [CLOUD] T-235a | Research war ERAS 5-7 (1750-1800, 1800-1850, 1850-1900)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-235-war.md (units 1-3)
VERIFY: eras 5-7 end with progress="researched", 0 target, 0 candidate and 0 [VERIFY] in
        those eras. The chapter FAILs until eras 8-10 are done (T-235b).
EXPECT: about 6 stories. The policy's war ruling is individual scale.
RESULT: DONE (eras 5-7). Three commits. Measured per era: 1750-1800, 1800-1850 and 1850-1900
        are progress="researched", with 0 target, 0 candidate and 0 [VERIFY]. Chapter: stories
        16 (v10 c0 t6), 1 [VERIFY], bank 14,157w vs outline 9,523w, validator 0 errors. All the
        remaining targets and the tag are in eras 8-10.
        STORIES: Washington; Joseph Plumb Martin (replaces the private target); Deborah
        Sampson; John Riley of the San Patricios (lashing and branding told in full); Grant and
        Lee (including Lee having Wesley Norris whipped); Amos Humiston; Christian Fleetwood
        (USCT); Cathay Williams (Buffalo Soldiers).
        DISPUTES RECORDED: Civil War dead (620,000 vs 750,000), Revolution battle deaths,
        prison-ship dead, Sampson's wound, Fort Pillow's Black dead, Riley's brand.
        LEFT OUT RATHER THAN HEDGED: the 1863 draft, Humiston's wound, and Riley's and
        Williams's death dates.

### 2026-09-26 | [CLOUD] T-235b | Research war ERAS 8-10 - LAST SLICE
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-235-war.md (units 4-6)
VERIFY: python tools/project_state.py --check war --stage research SHOULD PASS.
EXPECT: 6 targets and 1 [VERIFY]. Hand-offs from T-235a are in workspace/war.md. This is the
        last agent on the chapter, so it also audits every era's progress= flag.
RESULT: *** PASS. war is researched. ***
        359,764 tokens, 185 tool uses, 27 min.
        PASS  war / research | stage=RESEARCHED eras=10/10 stories=19 (v19 c0 t0) verify_tags=0
        bank=22314w outline=14377w validator_errors=0
        STORIES: Henry Gunther, Benjamin O. Davis Jr., Daniel Inouye (fills the WWII GI slot. He
        was a volunteer, not a draftee, and says so), Chester Nez, Ron Kovic, Muhammad Ali, Hugh
        Thompson Jr., Pat Tillman, Tammy Duckworth. New slugs checked unique.
        RESOLVED: the 1973 [VERIFY]. The last draft call was Dec 7, 1972, and the draft authority
        expired June 30, 1973.
        DISPUTES RECORDED: WWI flu deaths, No Gun Ri, My Lai (347 or 504), Hiroshima and
        Nagasaki, the Tuskegee "never lost a bomber" claim (false), the Abbey Gate Afghan dead.
        LEFT OUT RATHER THAN HEDGED: rape at My Lai, Agent Orange, drones, ordinary WWII and
        post-9/11 veterans (workspace/war.md lists these as audit candidates).
        PERISHABLE: the 2026 Venezuela operation and Iran war are current to September 2026. One
        Iran figure came from a search summary because the Washington Post page returned 403.
        Re-check this material before prose.
T-235 COMPLETE: war research took 3 agents in all (T-232, T-235a, T-235b).

### 2026-09-26 | [CLOUD] T-236 | Add the Pueblos' Acoma account to native-nations part 1 (DECISIONS #14)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-236-native-nations-acoma.md
VERIFY: python tools/project_state.py --check native-nations --stage prose must still PASS.
RESULT: DONE. 89,852 tokens, 8 tool uses, under 1 min. Commit cc046c7. native-nations prose PASS.
        ADDED (part 1, era 1500s, before Zaldívar's killing): the All Pueblo Council of
        Governors' October 2023 statement, quoted exactly, that the soldiers "had demanded food
        and supplies, assaulted an Acoma woman, and forced allegiance to the Spanish crown."
        "Assaulted" is defined as "attacked her". The text states that the Council's statement
        gives no more detail.

### 2026-09-26 | [CLOUD] PHASE 2 WRITING BEGINS: immigration first
Order for the ready chapters, smallest outline first so the brief is tested cheaply:
immigration, science, elements, land-environment, economy, government-politics, war, religion,
education, rights-movements. The last four are very large and will need more than three parts.

### 2026-09-26 | [CLOUD] T-237a | Write immigration PART 1 (eras 1-5)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-237-immigration.md (units 1-5)
VERIFY: part file validates (--part) with 0 errors, --punct 0/0, eras 1-5 progress="written",
        every story verified. The chapter check FAILs until parts 2 and 3 exist.
EXPECT: the first chapter written under v2 plus the bank-only rule (#13). Watch the
        "outline claims not in the bank" list. Its length shows how far outline and bank diverge.
RESULT: DONE (part 1). Five commits. MEASURED: validator (--part) 0 errors · --punct 0/0 ·
        5/5 eras progress="written" · 6 stories, all verified · slugs unique · 3,573 prose words.
        Average sentence 13.1 words (reported).
        STORIES: Richard Frethorne, Anne Hutchinson, jewish-refugees-1654, John Peter Zenger,
        Alexander Hamilton, Toussaint.
        OUTLINE CLAIMS LEFT OUT (bank lacks them): 10. Much less drift than city-building had.
        DEFECTS FIXED IN PROSE: 5 personifications carried from the outline ("the colony put
        her on trial", "Portugal retook", "the Company overruled", "Britain shipped", "rice
        economy imported"). Two chronology slips.
        FOR JON: jewish-refugees-1654 is a group story in which only Jacob Barsimson is named.
        Does it stand under the named-people rule?
        BANK GAPS: no nation named for the land under St. Augustine, Plymouth or New Amsterdam.
        The bank does not say who fought the Haitian Revolution.

### 2026-09-26 | [CLOUD] T-237b | Write immigration PART 2 (eras 6-7)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-237-immigration.md (units 6-7)
VERIFY: part2-1800s.md validates (--part) with 0 errors, --punct 0/0, both eras written, every
        story verified.
RESULT: LANDED, BUT CONTENT GAP. 177,684 tokens, 26 tool uses, 7.6 min. MEASURED: validator 0
        errors · --punct 0/0 · 6 stories verified · 2,470 words (reported).
        STORIES: Jette Bruns, Patrick Kennedy and Bridget Murphy, Carl Schurz, Annie Moore, Irving
        Berlin, Wong Kim Ark.
        OUTLINE CLAIMS LEFT OUT: about 15. PERSONIFICATIONS FIXED: 6. A self-contradictory Castle
        Garden sentence in the bank was fixed in the prose.
        RULE SLIP: the writer supplied "Russian officials" as the issuers of the May Laws, which
        the bank does not give. That breaks DECISIONS #13 in a small way. Parked.
        THE PROBLEM: the bank has NOTHING on anti-Chinese violence or the nativist riots, no human
        causes for the Irish famine, no pogrom attackers or death counts, and no causes for the
        railroad deaths. The prose says "the sources for this chapter do not record why they
        died." That is honest under #13. For this reader it is also softening by omission.
        A bank can pass the research gate and still lack the hard parts of its subject.
        RESPONSE: T-238 patches the immigration bank on exactly these gaps (and pre-checks eras
        8-10). T-237b2 then revises part 2 from the patched bank. The writing brief now makes a
        hard-subject or central-cause gap BLOCKING: patch the bank, then write.

### 2026-09-26 | [CLOUD] T-238 | PATCH the immigration bank: hard-subject gaps, eras 6-10
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-238-immigration-bank.md (9 units, listed there)
VERIFY: immigration --stage research still PASSES. Each unit landed as a new bank subsection
        with named actors and sources.
NEXT AFTER: T-237b2 revises part 2 from the patched bank. Then T-237c writes part 3.
RESULT: DONE. 9 patch subsections appended, each pushed. immigration research still PASSES.
        Bank 17,351w.
        NOW IN THE BANK: Ursuline convent 1834 (13 arrested, 12 acquitted, 1 convicted and
        pardoned). Philadelphia 1844 (19 indicted, "only a handful" convicted). The famine's human
        causes (food exports per Kinealy, Russell refused to ban them, Trevelyan in his own words,
        the quarter-acre clause, 250,000 to 500,000+ evicted, 1 to 1.5 million dead). LA 1871, Rock
        Springs, Eureka, Tacoma, Seattle and Hells Canyon 1887 (almost no one punished). The
        railroad "1,200" is one 1870 newspaper's guess, another reported about 50, and the causes
        were avalanches and explosions. Pogroms 40-50 dead. Louisville 1855 (at least 22 dead, 5
        indicted, none convicted). Angel Island. Laughlin, Grant and Johnson behind the 1924 Act.
        Mexican Repatriation (500,000 to 2 million, about 60% US citizens). Operation Wetback (INS
        claimed 1.3 million, a historian estimates about 300,000, 88 heat deaths). The 2018
        separations (Sessions, 3,924 children). Border deaths 2018-2023. Enforcement figures to
        July 2026.
        CORRECTIONS NOTED IN THE BANK: famine "blight caused", railroad "~1,200 died", Know-Nothings
        belong in era 7.
        FLAG FOR JON: the Tung Trinh (Bolinao 52) block, dated 2026-07-23 and so older than the
        no-softening ruling, says the cannibalism during the drift is "deliberately omitted from
        the kids' prose". That is a sanitization decision.

### 2026-09-26 | [CLOUD] T-237b2 | Revise immigration PART 2 from the patched bank
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-237-immigration.md (units 6-7, revision pass)
VERIFY: part 2 validates, --punct 0/0, no "sources ... do not record" sentence left where the
        bank now has the fact. The famine, the riots, anti-Chinese violence, the railroad deaths
        and the pogroms are stated with named actors.
RESULT: DONE. 171,337 tokens, 28 tool uses, 6.4 min. Two commits.
        MEASURED: validator 0 errors · --punct 0/0 · era and story markers identical · 6 stories
        verified · prose 2,808 -> 5,296 words (reported).
        ADDED: a span on the 1834 and 1844 mobs (attackers, counts, acquittals and a pardon). The
        famine span now covers exports, Russell, Trevelyan, the quarter-acre rule, evictions and
        1-1.5 million dead. Bloody Monday. The railroad span covers pay, the 1867 strike, the
        causes of death and the 50-1,200 range. A span on anti-Chinese attacks 1871-1887 with
        each court outcome. The pogroms with attackers and counts. The May Laws are credited to
        Ignatiev and Alexander III, which replaces the unsupported "Russian officials".
        ONE "do not record" KEPT: the cause of the Berlin family's house fire (genuinely unknown,
        minor). The other genuine unknowns are stated once each.

### 2026-09-26 | [CLOUD] T-237c | Write immigration PART 3 (eras 8-10), the last part
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-237-immigration.md (units 8-10)
VERIFY: python tools/project_state.py --check immigration --stage prose SHOULD PASS.
HELD: the Tung Trinh / Bolinao 52 story is NOT written until Jon rules on the cannibalism
      omission. The writer leaves it out and lists it under BLOCKING GAPS. A small follow-up adds
      it after the ruling.
RESULT: *** PASS. immigration is the FIRST NEW CHAPTER written under v2 + the bank-only rule. ***
        209,287 tokens, 35 tool uses, 10 min.
        PASS  immigration / prose
          measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=20 (verified 20)
          ms_verify_tags=0 emdash=0 semicolon=0 manuscript=15288w files=3 validator_errors=0
        STORIES (part 3): Frank Capra, Doukenie Bacos, Lee Puey You, Antonio Garcia (bracero),
        Reinaldo Arenas, Sergey Brin, Giannis Antetokounmpo, the Lost Boys of Sudan. The
        tung-trinh story is HELD for Jon.
        DEFECTS FIXED: the outline's plans for eras 9 and 10 omitted Operation Wetback, the
        boat deaths and the separations. The outline minimized the Repatriation. The bank
        personified. The bank's Angel Island board contradicts itself.
        BLOCKING GAPS (small, "who did it"): the pirates, the mechanism of the 88 sunstroke deaths
        in 1955, Arenas's jailers, the killers of the Lost Boys' parents, the officer who shot
        Villegas González, the DHS official for the 2018 separations. -> T-239.
        CHECK: "Donald Trump president from January 20, 2025" rests on a DHS press-release title.
        The fact is correct. The bank needs a primary source for it.
T-237 COMPLETE: immigration written in 5 agents plus 1 bank patch (T-238).

### 2026-09-26 | [CLOUD] T-239 | immigration: fill the small "who did it" gaps (bank + part 3)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-239-immigration-gaps.md
VERIFY: immigration still PASSES both research and prose.
RESULT: DONE. 192,529 tokens, 87 tool uses, 13 min. Both checks PASS, and part 3 --punct is 0/0.
        BANK NOW HOLDS: the pirates were Thai fishermen (UPI citing a UN official, 1986; McCabe 2015).
        No pirate is named anywhere. 96 suspects were arrested and 1 sentenced to death. The 88
        braceros died after a roundup in 112-degree heat. Arenas was held by Cuban State Security
        at El Morro, then Villa Marista, and released in 1976. The Lost Boys' parents were killed
        by Sudanese government forces and government-armed muraheleen (PBS, HRW). Villegas
        González was shot by an unnamed ICE officer. Prosecutors declined to charge, and the
        Illinois State Police investigation was open in Sept 2026. The 2018 separations:
        McAleenan, Homan and Cissna memo of Apr 23, 2018, approved by Nielsen May 4, 2018. The
        Jan 20, 2025 inauguration is sourced to the JCCIC record.
        STILL HELD: the tung-trinh story, for Jon's ruling.

### 2026-09-26 | [CLOUD] PROCESS CHANGE: a pre-write bank check for every chapter
immigration needed a bank patch (T-238) and a revision (T-237b2) AFTER writing, plus a gap patch
(T-239). About 580k tokens went on rework. From now on each chapter starts with ONE pre-write
bank check. The agent compares the bank against the outline and the chapter's subject, finds
the missing hard subjects and missing actors, and appends them to the bank. Then the writers
write once. The brief is in RESUME.md, "Standard PRE-WRITE BANK CHECK brief".

### 2026-09-26 | [CLOUD] T-240a | science: pre-write bank check
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-240-science.md
VERIFY: science --stage research still PASSES. The patch sections are listed in the checkpoint.
RESULT: DONE. 17 PATCH blocks. science research PASS. Bank 5,879 -> 10,798w (outline 4,832w).
        FILLED: remains taken for race science (Morton, the Army Medical Museum, Hrdlička,
        NAGPRA, apologies, the 2025 count still held). Eugenics as science (Davenport, Laughlin,
        the ERO 1910-1939). Human radiation experiments (18 plutonium injections, 5 patients
        named, Trinity fallout, ACHRE, the apology, payments). Henrietta Lacks (1951, 2013,
        2023). Jefferson's race claims and replies. Agassiz's daguerreotypes (7 named, the
        settlement). Watson's statements. Named jobs for Mitchell and Goddard. Genome cost.
        PLACED ELSEWHERE: sterilizations (rights-movements), IQ tests (education), Laughlin's
        testimony (immigration), the NAGPRA campaign (native-nations), the bombs on Japan (war).
        UNKNOWABLE: illness and death counts from Trinity. NOT FOUND: a "hundreds of dollars"
        genome cost, and support for the outline's "within a generation" Darwin claim. Writers
        leave both out.

### 2026-09-26 | [CLOUD] T-240b | Write science PART 1 (eras 1-5)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-240-science.md (unit 2)
VERIFY: part1 validates (--part), --punct 0/0, 5 eras written, stories verified.
RESULT: DONE. MEASURED: validator 0 · --punct 0/0 · 5/5 written · 6 stories verified. About 3,250
        words (reported).
        STORIES: Kimmerer, Holm, Franklin, Bartram, Rittenhouse, Banneker.
        DEFECTS FIXED: the bank's sweeping "European science barely exists". The kite's location
        contradiction. The bank's evaluative "condescending" (the reply is quoted instead). The
        unsupported "Rittenhouse led". The personified "APS organized" and "France ran".
        OUTLINE CLAIMS LEFT OUT: about 20.
        BLOCKING GAPS (held for one end-of-chapter patch): Jefferson's race claim has no context
        in the bank (that he enslaved people, and how such claims defended slavery). Why the 1769
        transit was timed. Not blocking: no nation named for Cahokia or Chaco.
DIRECTOR: blocking gaps are now COLLECTED per chapter and closed by ONE patch-and-update agent
        after the last part. That is cheaper than one after each part.

### 2026-09-26 | [CLOUD] T-240c | Write science PART 2 (eras 6-7)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-240-science.md (unit 3)
VERIFY: part2 validates (--part), --punct 0/0, both eras written, stories verified.
RESULT: DONE. 160,469 tokens, 27 tool uses, 7 min. MEASURED: validator 0 · --punct 0/0 · 2/2 written
        · 6 stories verified · about 3,450 words (reported).
        SPANS: Silliman, Henry and Faraday, Morton's 867 skulls (sources, method, the Gould/Lewis
        dispute, Penn's 2021 apology), Maury (joined the Confederacy), Gray against Agassiz,
        Agassiz and Zealy's daguerreotypes (all seven people named, Lanier's suit, the Mar 11,
        2026 unveiling), Army Medical Museum skull collecting (Circular No. 2), Morrill and
        Hatch, Mitchell's 1878 eclipse.
        STORIES: Smithson, Henry, Mitchell, Gibbs, Michelson, Fleming.
        DEFECT FIXED: the bank's "not above robbing graves" softened the act. The prose now says
        "robbed graves". Four personifications were fixed. The outline's gnomic line and
        antithesis were dropped. Outline claims left out: 13.
        BLOCKING GAPS (6, collected): who used Morton's work to defend slavery, the grave-robbers,
        who killed the Dakota man, what Darwin's theory is, who stripped the seven people for the
        daguerreotypes, and who enslaved them.

### 2026-09-26 | [CLOUD] T-240d | Write science PART 3 (eras 8-10), the last part
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-240-science.md (unit 4)
VERIFY: science --stage prose SHOULD PASS. Then T-240e closes the collected blocking gaps.
RESULT: *** PASS. science passes prose. ***
        PASS  science / prose
          measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=25 (verified 25)
          ms_verify_tags=0 emdash=0 semicolon=0 manuscript=15888w files=3 validator_errors=0
        Part 3 is about 8,800 words, with 13 stories. Outline claims left out: 26. Defects
        fixed: institutions as actors, "billions to hundreds", "the universe got bigger". Two
        quotes containing em dashes were split with no word changed.
        BLOCKING GAPS for the chapter: about 18, listed in the checkpoint (who pulled Cade's
        teeth, Shaw, Allen's amputation, who decided against evacuating Trinity, who cut Lacks's
        cells, the Fernald, prisoner and Vanderbilt experiments, what Nazi eugenics was, why
        CO2 matters, plus the part 1 and part 2 gaps).
        RULE SLIP for audit: T-240b wrote identity glosses from general knowledge (Newton's first
        name, "Swedish botanist" and similar). These are small breaches of DECISIONS #13.

### 2026-09-26 | [CLOUD] T-240e | science: close the collected BLOCKING GAPS (bank + all 3 parts)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-240-science.md, section "BLOCKING GAPS"
VERIFY: science still PASSES research and prose. Each gap is marked closed or genuinely-unknown
        in the checkpoint.
RESULT: DONE. 264,127 tokens, 127 tool uses, 18 min. Prose and research both PASS.
        Manuscript 15,888 -> 17,340w. Bank 14,989w.
        21 gap entries: 17 closed and 4 partly closed, with the rest recorded GENUINELY UNKNOWN
        and the sources checked. Still unknown: who pulled Ebb Cade's teeth (ACHRE itself could not
        find out), who injected Stevens and Allen, who dug up the Philadelphia bodies (the Penn
        2021 report shows Morton got at least 14 himself), named proslavery users of Query XIV
        (Jefferson enslaving 600+ people is now in the prose), Hrdlička's other collectors, and
        who enslaved Alfred, Drana and Fassena.
        CORRECTIONS: Cade's injector is disputed (Howland against Dwight Clark), and the prose gives
        both. Simeon Shaw flew WITH his mother (ACHRE), where AHF said he was separated from her.
        PARKED: APS dates the first Transactions 1771, and the bank says 1773.
T-240 COMPLETE: science, 5 agents, about 1.01M tokens.

### 2026-09-26 | [CLOUD] T-241a | elements: pre-write bank check
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-241-elements.md
VERIFY: elements --stage research still PASSES.
RESULT: DONE. 205,622 tokens, 92 tool uses, 13 min. 14 PATCH blocks. Research PASS. Bank
        10,417 -> 16,639w.
        FILLED: the Radium Girls' company officials (von Sochocky, Roeder, Kelly) and named dead.
        NIST settlement terms and Donohue dates pinned, which closes 2 parked audit items. Uranium
        on Navajo land (AEC sole buyer, no warnings, Church Rock 1979, RECA 1990/2025). Lead
        (leaded-gas death counts x3, the bans, Flint 2014-2023). Mercury (Danbury hatters, the
        gold fields). Arsenic (Anaconda). Land taken (Cherokee gold, the 1842 Copper Treaty, the
        Black Hills). Forced and enslaved iron labor (Saugus, Maryland). An order error: the FTC
        acted before Byers died.
        FALSE FIRSTS CAUGHT: "nation's first mineral rush" (Georgia 1829 came earlier). The
        Phelps "first" is ORNL's claim. "First American industry that made a metal" is unsourced.
        UNKNOWABLE: the full Navajo death count, the supervisor who taught lip-pointing, the
        Church Rock dam official.
DIRECTOR: the writing brief now lives in control/briefs/WRITER.md.

### 2026-09-26 | [CLOUD] T-241b | Write elements PART 1 (eras 1-5)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-241-elements.md (unit 2)
RESULT: DONE. 163,118 tokens, 31 tool uses, 7 min. MEASURED: validator 0 · --punct 0/0 · 5/5 written ·
        2 stories verified (Priestley, Conrad Reed). 2,802 words.
        Covers Lake Superior copper (at least 9,500 years ago), the trade in turquoise and obsidian,
        Falling Creek and 1622, Saugus with about 400 Scottish prisoners forced to work, enslaved
        workers at the Baltimore Iron Works, Principio and Catoctin (the 2023 DNA study), the
        Iron Act, the Coinage Act.
        DEFECTS FIXED: the outline's false "first". "Colonists built" had hidden the enslaved
        labor. "Parliament's act banned" (personified).
        BLOCKING GAPS (3, collected): the cause of the 1622 attack, who captured and shipped the
        Scots and held their indentures, the owners of the three Maryland works and the treatment
        of the enslaved workers there.

### 2026-09-26 | [CLOUD] T-241c | Write elements PART 2 (eras 6-7)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-241-elements.md (unit 3)
RESULT: DONE. 156,158 tokens, 25 tool uses, 5 min. MEASURED: validator 0 · --punct 0/0 · 2/2 written ·
        1 story verified (the Halls). 2,357 words.
        Covers Georgia gold on Cherokee land (the Gold Lottery), Stuart's 1842 Copper Treaty with
        the Ojibwe, the Ontonagon Boulder (taken, and the 1991 request Smithsonian officials
        refused), gold-field mercury, the Danbury hatters, the Black Hills (1877, the 1980 ruling,
        the $2 billion the Sioux refused). Anaconda arsenic dates from 1902 and moves to part 3.
        DEFECTS FIXED: 2 false firsts, and institutions as actors.
        BLOCKING GAPS (4, collected): the actor for the 1838 Cherokee removal, the Danbury shop
        owners, named people poisoned by gold-field mercury, who drafted the 1876 agreement.

### 2026-09-26 | [CLOUD] T-241d | Write elements PART 3 (eras 8-10), the last part
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-241-elements.md (unit 4)
VERIFY: elements --stage prose SHOULD PASS.
RESULT: *** PASS. elements passes prose. ***
        248,910 tokens, 35 tool uses, 12.6 min.
        PASS  elements / prose | ms_eras=10/10 written=10/10 ms_stories=10 (verified 10)
        emdash=0 semicolon=0 manuscript=12908w files=3 validator_errors=0
        Part 3 is about 8,750 words with 7 stories. It covers the Radium Girls, lead, Danbury,
        Anaconda, Navajo uranium, Church Rock, RECA, Flint, and US element discoveries (Seaborg,
        Ghiorso, Hoffman, Phelps).
        DEFECTS FIXED: Phelps's "first" (now her lab's own words), the order of Byers's death
        against the FTC order, the radium "like calcium" simile, institutions as actors.
        BLOCKING GAPS for the chapter: 16 (3 + 4 + 9). -> T-241e.
DIRECTOR: the gap-closing brief now lives in control/briefs/GAPS.md.

### 2026-09-26 | [CLOUD] T-241e | elements: close the 16 collected BLOCKING GAPS
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-241-elements.md, "BLOCKING GAPS"
VERIFY: elements still PASSES research and prose.
RESULT: DONE. Prose and research PASS. Manuscript 12,908 -> 14,738w. Bank 22,017w. 7 PATCH blocks.
        16 gaps: 9 closed, 3 partly closed, 4 GENUINELY UNKNOWN with sources listed (Danbury owners
        in eras 7 and 8, named gold-field mercury victims, the Anaconda officials and count).
        CORRECTIONS: Catoctin "at least 270" is now 271 (from the Science paper itself). The
        Maryland figures are confirmed from Mount Clare. The Hueper line is sharpened from ACHRE.
        Earley's Flint role now rests on the 2016 Task Force report. The Legionnaires' count has a
        second official figure (87 cases, 10 deaths, Jan 13, 2016). Governor Bruce King's Church
        Rock role is journalism-grade and attributed to news accounts in the prose.
T-241 COMPLETE: elements, 5 agents.

### 2026-09-26 | [CLOUD] T-242a | land-environment: pre-write bank check (incl. Bears Ears refresh)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-242-land-environment.md
VERIFY: land-environment --stage research still PASSES.
RESULT: DONE. 13 PATCH sections. Research PASS. Bank 6,342 -> 14,053w.
        FILLED: the 1785 grid on land taken by Fort McIntosh (under duress, surveyors under army
        guard), Fallen Timbers and Greenville. The bison killing in the words of Sherman, Sheridan,
        Dodge, Delano and Miles, Grant's 1874 pocket veto, army ammunition. The Mariposa Battalion
        at Yosemite (1851) and the Yellowstone removals. The taking in numbers (railroad grants,
        Homestead, Morrill, Dawes). California's 1850 law against prairie fires. Glacier and the
        Blackfeet (Starvation Winter, the 1895 sale). The Yellowstone wolves. Love Canal, Warren
        County, Norco, Yosemite's last village (burned 1969), GAO 1983, UCC 1987, EO 12898. Denka
        in Cancer Alley, 2023-25.
        FALSE FIRSTS: the wolves as "first deliberate return", the pigeon as "first species seen go
        to zero on a known day".
        BEARS EARS current to 2026-09-26: the cut lands opened to mining on Sept 11, claims have
        been filed, and supporters sued in D.C. federal court on Sept 2. No ruling yet.
        UNVERIFIED: the source of Sheridan's 1875 "medal" speech (one source, labeled). The
        shooter of Tenaya's son is never named.

### 2026-09-26 | [CLOUD] T-242b | Write land-environment PART 1 (eras 1-5)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-242-land-environment.md (unit 2)
RESULT: DONE. MEASURED: validator 0 · --punct 0/0 · 5/5 written · 2 stories verified (Miantonomi,
        Ebenezer Mudgett) · 3,584 words.
        Covers Native land management (fire, the Three Sisters, beaver watersheds, bison, the Calusa
        watercourts), with no "wilderness/empty/virgin/untouched". De Soto's animals and European
        earthworms. The Koch 2019 reforestation estimate (labeled as one study). Land as property.
        The king's pines. The 1785 grid and the taking in order (Fort McIntosh under duress,
        Hutchins under army guard, Harmar, St. Clair, Fallen Timbers, Greenville 16,930,417 acres).
        DEFECTS FIXED: the outline had horses back "from 1493", but that voyage went to the
        Caribbean. The bank's "Hussey's boat killed a whale" (now the men aboard). Personification.
        BLOCKING GAPS (3, collected): who carried the 1500s epidemics and fought the wars, whose land
        the tobacco planters cleared, who killed Miantonomi and how.

### 2026-09-26 | [CLOUD] T-242c | Write land-environment PART 2 (eras 6-7)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-242-land-environment.md (unit 3)
RESULT: KILLED by the usage limit (session limit, reset 13:20 UTC). Jon's continue message arrived.
        SALVAGE (this container survived, so the transcript was readable): era 06 was committed
        (40dd051). Era 07 was written in ONE append (event 37), validated with 0 errors and 0/0
        punct, and then the agent died before its self-review and commit. The director committed
        the landed text. -> T-242c2 does a short continuation: self-review, record gaps, close.

### 2026-09-26 | [CLOUD] T-242c2 | Continue T-242c: self-review land-environment part 2, record gaps
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-242-land-environment.md (unit 3)
RESULT: DONE. 152,221 tokens, 19 tool uses, 5 min. MEASURED: validator 0 · --punct 0/0 · 4 stories
        verified · slugs unique.
        FINDING: the salvaged era was NOT complete, although it validated clean. It had 3 spans,
        and its summary stated bison, pigeon and Yellowstone facts that no span told. The
        continuation added spans from the bank (hide hunters, the officers' words, Delano, Grant's
        1874 pocket veto, Sheridan labelled single-source, the pigeon nestings, Yellowstone and the
        Tukudika, the forest reserves) and the frank-mayer and john-muir stories. It fixed 3
        personifications and 2 agentless passives.
        Outline claims left out: 11. BLOCKING GAPS: who killed To Tu Ya's uncle, and what force
        removed the Tukudika.
LESSON (now in CLOUD-WORKFLOW §4): a file that validates is not a finished file. After a
        kill, always send a continuation agent to check the era against its outline plan. Never
        close the unit from the validator alone.

### 2026-09-26 | [CLOUD] T-242d | Write land-environment PART 3 (eras 8-10), the last part
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-242-land-environment.md (unit 4)
VERIFY: land-environment --stage prose SHOULD PASS.
RESULT: *** PASS. land-environment passes prose (15 stories verified, 15,639w). ***
        Part 3 is about 5,300 words. It covers Roosevelt's 230M acres, Glacier and the Blackfeet
        (Marias 1870, the Starvation Winter, the 1895 sale), Hetch Hetchy, the last pigeons, the
        wolves poisoned 1914-26, the Dust Bowl as soil damage, the CCC, DDT, Yosemite 1969, the
        Cuyahoga, Love Canal (Hooker's deed, Whalen, Carter, 236+710 families), Warren County
        (Ward, the Burns family, Gov. Hunt), GAO 1983, UCC 1987 (Chavis), EO 12898, the wolves'
        return in 1995, Cancer Alley, Denka, land given back, and Bears Ears to 2026-09-26.
        DEFECTS FIXED: personification (Congress, states, Shell, agencies). "Hundreds of homes" is
        now the bank's "about 100". "Well blowout" is now "oil spill". An unsourced
        "first-of-its-kind" was dropped. Both Love Canal figures are given.
        Outline claims left out: about 25.
        BLOCKING GAPS (8): who lived on Roosevelt's lands, who ended the Blackfeet rights after
        1910, the Gila's people, who ordered the 1969 Yosemite eviction, the Cuyahoga and Santa
        Barbara polluters, the Love Canal home builders, the 1908 Bison Range taking, the count
        years. Chapter total with parts 1-2: 13. -> T-242e.

### 2026-09-26 | [CLOUD] T-242e | land-environment: close the 13 collected BLOCKING GAPS
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-242-land-environment.md, "BLOCKING GAPS"
VERIFY: land-environment still PASSES research and prose.
RESULT: DONE. 293,624 tokens, 155 tool uses, 19 min. Prose and research PASS. Manuscript 16,865w,
        bank 17,687w.
        13 gaps: 12 closed (7 in full, 5 in part). GENUINELY UNKNOWN with sources listed: To Tu Ya's
        uncle, the Tukudika removal force and numbers, the Glacier bacon suppliers and officials,
        who ordered the 1969 Yosemite eviction (the park historian says no record exists), the
        Cuyahoga oil's owner, the Love Canal home builders.
        CORRECTIONS: Miantonomi's death was ordered by the United Colonies commissioners, not by
        Connecticut alone. John Young was the Blackfeet agent from 1876, not 1879.
T-242 COMPLETE: land-environment, 6 agents (one killed and salvaged).

### 2026-09-26 | [CLOUD] T-243a | economy: pre-write bank check
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-243-economy.md
VERIFY: economy --stage research still PASSES.
RESULT: DONE. 7 PATCH blocks. Research PASS. Bank 6,398 -> 12,332w.
        FILLED: indentured servants (numbers, terms, headright, deaths, the switch to enslaved
        Africans). About 50,000 British convicts sold 1718-75. Rhode Island's slave trade (the Browns'
        Sally). Slavery as $3B of capital and who profited (named banks, bond sellers, JPMorgan
        predecessors, insurers, the Lehmans, Lowell). The Panic of 1819, and who paid in 1837.
        Sharecropping, Bailey v. Alabama, Alabama convict leasing (companies and deaths), 1873 and
        1893 job losses. Black unemployment, the Social Security exclusions (both accounts), AAA
        evictions. 2008 foreclosures and wealth loss by group.
        FALSE FIRST: the 1534 Cartier fur trade (1524 in Maine came first). "Lowest ever" for 1944
        should read "lowest in official records".
        PERISHABLE, dated Aug 2026 / Q2 2026: unemployment 4.1%, CPI 3.4%, GDP, the jobs mix, Fed
        wealth shares (top 10% 68.9%, bottom half 2.3%), with a correction note for the revised
        older Fed figures.

### 2026-09-26 | [CLOUD] T-243b | Write economy PART 1 (eras 1-5)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-243-economy.md (unit 2)
RESULT: DONE. MEASURED: validator 0 · --punct 0/0 · 5/5 written · 3 stories verified (Rolfe, Eliza Lucas
        Pinckney, Hamilton) · 3,414 words, average sentence 13.9 words.
        DEFECTS FIXED: Cartier's "first" became "one of the earliest". The New England slave trade
        was moved from the 1600s to the 1700s per the bank. The Manhattan purchase had no named
        seller, so it was left out (land erasure). Personification fixed. The Pinckney story now
        credits the Caribbean dye-makers and the enslaved workers. The unsourced "first Secretary"
        title was dropped. Outline claims left out: 17.
        BLOCKING GAPS (7, collected): who took Native people from Maine before 1524, whose land the
        headright acres were, the causes of death on the Sally and the convict ships, and others.

### 2026-09-26 | [CLOUD] T-243c | Write economy PART 2 (eras 6-7)
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-243-economy.md (unit 3)
RESULT: DONE. MEASURED: validator 0 · --punct 0/0 · 2/2 written · 3 stories verified (Philip Hone,
        Carnegie, Rockefeller) · about 4,350 words.
        Covers slavery as about $3B of capital, and who profited by name (planters' banks, Baring
        Brothers, Prime Ward and King, Hope and Co., JPMorgan Chase's 2005 report, New York Life,
        Aetna, the Lehmans, Lowell's Boston Associates). The panics of 1819, 1837, 1857, 1873 and
        1893 (Tompkins Square, Coxey). Sharecropping, Bailey v. Alabama, Alabama convict leasing
        (wardens, companies, state revenue, deaths).
        BANK DEFECT fixed in prose: the patch implies leasing began after the 13th Amendment, but it
        also dates Alabama's lease to 1846. Outline claims left out: about 14.
        BLOCKING GAPS (7 more, 14 in total): the Homestead land's Native owners, the 1819 debt
        jailings, the 1837 seizures, Bailey's sentencing court, the 1924 boiling-vat death,
        Coxey's arrest, the Homestead deaths.

### 2026-09-26 | [CLOUD] T-243d | Write economy PART 3 (eras 8-10), the last part
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-243-economy.md (unit 4)
VERIFY: economy --stage prose SHOULD PASS.
RESULT: *** PASS. economy passes prose (11 stories verified, 13,293w). ***
        Part 3 is about 4,950 words. It covers the crash, the Depression, the Bonus Army, Black
        unemployment, the New Deal, the Social Security exclusions (both accounts: Dubin names Byrd,
        Witte and Smith, DeWitt names Morgenthau), the AAA evictions and purge, 1944's 1.2% ("lowest
        in the official records"), the postwar boom, stagflation, Youngstown, the farm crisis,
        2008 by group, the Countrywide and Wells Fargo settlements, and figures dated to 2026.
        Stories: Ford, Benjamin Roth, Frances Perkins, Gerald Dickey, Ed Neufeldt.
        DEFECTS FIXED: GDP 104 -> 56B against "output down 30%" is now explained. A contradictory
        museum "20 percent" was dropped. "Sixfold" became the bank's "600 percent". The Fed shares
        use the revised Q2 2026 figures. The outline's "police shots" named a shooter the bank does
        not support. Personification and a closing reversal were removed. Outline claims left
        out: about 30.
        BLOCKING GAPS (5 more, 19 in total): Hushka and Carlson's shooters, the planters' actions
        against the STFU, the Youngstown decision-maker, the Carter/EDA official, 2008's named
        executives and regulators. -> T-243e.

### 2026-09-26 | [CLOUD] T-243e | economy: close the 19 collected BLOCKING GAPS
STATUS: IN-FLIGHT
CHECKPOINT: control/checkpoints/T-243-economy.md, "BLOCKING GAPS"
VERIFY: economy still PASSES research and prose.
RESULT: KILLED by the usage limit before its first commit. Measured afterwards: no commits, clean
        tree, 0 bank patches, 0 gaps marked. economy still PASSES prose and research.
        Re-dispatched from the start as T-243e2.
NOTE (Jon, 2026-09-26): the $100 cloud gift is used up, and Jon's own funding now pays. Jon said
        to finish this task and then HOLD. No further dispatches until Jon says so.

### 2026-09-26 | [CLOUD] T-243e2 | economy: close the 19 BLOCKING GAPS (re-dispatch of T-243e)
STATUS: CANCELLED. Jon stopped it at once. Nothing landed.
RESULT: Director error: T-243e had done nothing, so there was nothing to finish, and it should
        have gone to the queue rather than being re-run. Moved to TODO as not started.
        economy PASSES prose and research as it stands.

### 2026-09-26 | [CLOUD] CLEAN STOP (Jon: funding)
Nothing in flight. Next task when work resumes: T-243e (economy's 19 blocking gaps, not started).

### 2026-09-26 | [CLOUD] Open questions settled (Jon: "use the recommendation") | director edit
Applied by the director directly (small exact edits, no sub-agent, to save Jon's funding).
DECISIONS #15: the Tung Trinh / Bolinao 52 story is added to immigration part 3 (1950-2000), from
  the bank only. The cannibalism is stated once, in plain words, and defined. The bank does not
  give Tung Trinh's gender, so no pronoun is used (the director caught and removed one "She").
DECISIONS #16: jewish-refugees-1654 was converted from an hb-story to an hb-zoom span in part 1,
  with its text unchanged apart from the story-card records.
MEASURED: PASS immigration / prose, 20 stories verified, 16,174w, emdash=0 semicolon=0,
  validator 0 errors on both edited parts. Slug tung-trinh is unique.
STOPPED again after this, per Jon.

### 2026-09-26 | [LOCAL] T-244-prep | Process rebuilt for local work (director, no sub-agent)
STATUS: DONE
BRANCH: feature/local-cloud-code-homebrew (from main at e965921), for comparing efficiency with the cloud run.
RULINGS (Jon): DECISIONS #17 eight steps in strict order; #18 opus writes/researches/fixes, sonnet
  checks; #19 no GitHub, one local commit per sub-agent; #20 never shrink the book; #21 writers
  research their own gaps; #22 first three sonnet checks repeated with opus to calibrate.
DONE: cloud workflow archived to control/archive/cloud/ (not deleted). Briefs rebuilt in
  control/briefs/: RESEARCH (bank check merged in, SEARCHED NOT FOUND records), WRITER (2 per
  chapter, own gap research, slice tool), CHECKER, FIXER, GAPS (round 2), SALVAGE (sonnet), README
  (model policy). tools/slice_bank.py built and tested on all 37 banks. RESUME trimmed (old copy
  archived). ROADMAP, TODO, CLAUDE.md, README, AGENT-BRIEF, STATUS, AUDIT-QUEUE, usage-log header,
  checkpoint template updated. control/audit/CHECKER-CALIBRATION.md created.
MEASURED: project_state unchanged (7 WRITTEN, 5 RESEARCHED, 13 RESEARCHED*, 11 SEED, 1 PARTIAL).
  economy --stage prose still PASS.
NEXT: wait for Jon's go. Then T-244 migration patch (TODO step 1a).

### 2026-09-26 | [LOCAL] T-244 | migration: patch (1 target story) + bank check | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-244-migration.md
VERIFY: python tools/project_state.py --check migration --stage patch (and --stage research)
NOTE: first agent under the rebuilt local briefs (RESEARCH.md). Brief fourth-wall rule added first.
RESULT: DONE. PASS migration / patch and / research. stories 15 (v15 c0 t0), bank 9,871 -> 14,489w, outline 3,685w,
        validator 0. 240,774 tokens, 107 tool uses, 11.3 min (opus).
        Target filled: kimberly-rivers-roberts (Katrina, 2005; Trouble the Water, 2008).
        Bank check: PATCHes for Onate "first" (now "first overland"), Hartford, Tuscarora War, Shenandoah,
        Acadian expulsion, Kentucky, Cherokee removal (Scott; 1,000 to 8,000+), Choctaw/Creek/Chickasaw,
        Franklin & Armfield, Long Walk, Madley's California figures, Great Migration push and obstruction,
        Chicago 1919, the 1936 bum blockade (Chief James E. Davis), EO 9066 movement facts (rights-movements
        leads), Gretna bridge, Houston, Census Vintage 2025. SEARCHED NOT FOUND: 2.
        Weak points the agent flagged in the bank: 3 facts seen only in search-result summaries.

### 2026-09-26 | [LOCAL] T-245 | home-family: patch (2 candidates, 4 targets, kitchen thread) + bank check | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-245-home-family.md
VERIFY: python tools/project_state.py --check home-family --stage patch (and --stage research)
USAGE AT START: 7% of the 5-hour window (Jon, 2026-09-26; includes T-244 and director work).
RESULT: DONE. PASS home-family / patch and / research. stories 16 (v16 c0 t0), bank 5,703 -> 12,359w, outline
        3,887 -> 5,460w, validator 0. 332,647 tokens, 153 tool uses, 21.3 min (opus).
        Stories: Buffalo Bird Woman (moved to 1800-1850), Theodore and Patricia Bladykas (Levittown 1947), Clyde
        Ross, the Colfax homeschool family, Pierre Solon and Katty Familia (foreclosure), the Munoz family (2020).
        Kitchen thread sourced; the "petticoat fire" hazard is a myth and was dropped. Parked: fridge figures to
        technology, heating fuel and electricity to energy (both still validate 0). 1901 tenement-law claim
        corrected. Land, HOLC/FHA, Myers mob, Countrywide actors added. Perishables refreshed to 2025-26.
        SEARCHED NOT FOUND: 2. Unconfirmed (search summary only) tags: 8. Not done: frontier-cabin nations.

### 2026-09-26 | [LOCAL] T-246 | technology: patch (1 candidate, 3 targets) + bank check | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-246-technology.md
VERIFY: python tools/project_state.py --check technology --stage patch (and --stage research)
USAGE AT START: 14% (Jon). T-245 read 7% -> 14% (includes director work, marked +).
RESULT: DONE (2026-09-27). PASS technology / patch and / research. stories 23 (v23 c0 t0), bank 5,783 -> 12,098w,
        outline 3,597 -> 5,360w, validator 0. 315,496 tokens, 146 tool uses, 16.0 min (opus).
        Stories: Wayne Valliere (Ojibwe canoe builder), Joseph Jenks (Saugus, 1646 patent), Lee Felsenstein, Karla
        Ortiz (AI, 2023 Senate testimony). Bank check: Falling Creek workers and 27 dead, "first ironworks" dispute
        recorded, Baltimore Iron Works enslaved workers (Anthony), gin credit/injuries/profit/removals, Slater's
        child workers, Jo Anderson and the reaper, Ned and the 1858 patent ruling, 1913 industrial deaths,
        Robert Williams' false face-recognition arrest, Pew 2025-26 and Aug 2026 AI job-cut figures.
        SEARCHED NOT FOUND: 1 (Andersen v. Stability AI verdict; trial date disputed). Nothing parked elsewhere.
        4 [VERIFY] tags left in an old parked bank section -> WRITER brief now says [VERIFY] bank lines are not facts.
USAGE END: not captured (the 5-hour window reset before a reading).

### 2026-09-27 | [LOCAL] T-247 | energy: patch (2 candidates, 3 targets) + bank check | model opus
STATUS: KILLED (continued as T-247b)
CHECKPOINT: control/checkpoints/T-247-energy.md
VERIFY: python tools/project_state.py --check energy --stage patch (and --stage research)
USAGE AT START: 0% (Jon: fresh 5-hour window). This reading is clean: brackets director prep + the agent.
RESULT: KILLED when Jon's app restarted (not a usage limit). Measured: 1 bank PATCH landed (William Chadbourne,
        era 03); outline unchanged; energy still FAIL patch. Usage 0% -> 3% (includes director prep).
        Salvage: --brief digest was 179 words, so no sonnet salvage reader; the ~50 fetched URLs and the stop
        point went into the checkpoint's SALVAGE section. Continued as T-247b.

### 2026-09-27 | [LOCAL] T-247b | energy: continuation of T-247 | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-247-energy.md (read SALVAGE first)
VERIFY: python tools/project_state.py --check energy --stage patch (and --stage research)
USAGE AT START: 3% (Jon).
RESULT: DONE. PASS energy / patch and / research. stories 11 (v11 c0 t0), bank 5,078 -> 11,157w, outline
        4,187 -> 6,615w, validator 0. 318,226 tokens, 162 tool uses, 18.1 min (opus).
        Stories: William Chadbourne (verified from the landed PATCH), Pearl Yates (UNC record corrects HISTORY.com:
        a teacher, not a farmer's wife), Lafayette Houck (collier, era 07; the 1700-1750 collier slot removed as
        SEARCHED NOT FOUND, Collier Sam named in era 05 text), David Falconer (EPA photographer, 1973-74 gas lines),
        Cristian Pavon Pineda (2021 Texas freeze; carbon monoxide per autopsy). Bank check: Tewa land, enslaved and
        convict furnace labor, Avondale, Monongah (362 official, 500+), ~105,000 miners killed 1900-2025 (agent's
        sum of MSHA yearly figures), Ludlow, black lung, Upper Big Branch, dam removals (TVA, Grand Coulee,
        Garrison), TMI, pointers to Osage/Navajo/Dakota Access banks, EIA 2025-26 (2018: US passed Russia, not
        Saudi Arabia). Parked to work-workers and disasters (both validate 0).
        WRITER brief: ignore BOOK-OUTLINE.md in the slug-uniqueness grep (compiled copy).
USAGE END (T-247b): 9% (Jon). 3% -> 9% (includes director close and T-248 prep, marked +).

### 2026-09-27 | [LOCAL] T-248 | transportation: patch (1 target) + bank check | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-248-transportation.md
VERIFY: python tools/project_state.py --check transportation --stage patch (and --stage research)
USAGE AT START: 9% (Jon).
RESULT: DONE. PASS transportation / patch and / research. stories 17 -> 19 (v19 c0 t0), bank 4,764 -> 13,064w,
        outline 4,511 -> 6,684w, validator 0. 424,869 tokens, 194 tool uses, 25.0 min (opus).
        Stories: Barbara Ann Berwick (Uber, 2015 Labor Commissioner decision read in full), NEW Moses Grandy
        (enslaved canal-boat captain, 1843 memoir), NEW Irene Morgan (1944 arrest, 1946 ruling). All 16 older
        verified stories checked against the bank; 5 patched. Bank check: land (Seloy, Post Road paths, Great
        Warriors Path, Haudenosaunee, transcontinental nations), Erie pay and 1819 malaria (1,000 SICK, not dead),
        Dismal Swamp diggers, 85 of 113 Southern railroads built by enslaved workers, CP deaths "50 to 1,200, no
        count" (outline's "roughly 1,200 died" rewritten), land grants ~130M acres, crew death rates, Wells,
        Plessy, Freedom Rides (Connor's 15 minutes), 475,000 households displaced by highways, Engelhardt's I-85
        route (356 homes), car deaths 1913-2025, Grand Canyon 1956, Key Bridge 2024, Potomac 2025.
        "Firsts" fixed: Sprague (first successful), Fulton ("every major river" too broad).
        SEARCHED NOT FOUND: 3. Parked to work-workers (validates 0).
        ISSUE: the agent pip-installed pypdf unasked. Reported to Jon. briefs/README now says install nothing.
USAGE END (T-248): 16% (Jon). 9% -> 16% (includes director close and T-249 prep, marked +).

### 2026-09-27 | [LOCAL] T-249 | landmarks: patch (2 targets) + bank check | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-249-landmarks.md
VERIFY: python tools/project_state.py --check landmarks --stage patch (and --stage research)
USAGE AT START: 16% (Jon).
RESULT: DONE. PASS landmarks / patch and / research. stories 17 (v17 c0 t0), bank 5,060 -> 12,261w, outline
        4,653 -> 5,726w, validator 0. 294,099 tokens, 153 tool uses, 18.0 min (opus).
        Stories: Glenna Wallace (Eastern Shawnee chief, Octagon Earthworks, retired Sept 2026), John Collins
        ("Juan Calens", English prisoner, Castillo mason 19+ years; NPS 1942 and 1993). Older stories checked, gaps
        sourced. Bank check: Capitol payrolls (385 payments of $60/yr to owners incl. Thornton, Hoban), Black Hills
        actors (Custer 1874, 1876 ration cutoff, 1877 Act), Castillo forced Guale/Timucua/Apalache labor, St. Louis
        mounds destroyed (1869, 1904), Brooklyn Bridge 21/27/up to 40 dead, Quebec Bridge 75-76 (33 Kahnawake),
        Taft and Moton, EJI memorial, SPLC 2025 (2,086 standing, 415 removed), Pike reinstalled Oct 2025.
        SEARCHED NOT FOUND: 4. Unsourced outline claims flagged in the bank: 4. The agent also removed an outline
        line that spoke about the book itself ("the book does not invent people"): a fourth-wall break.
USAGE END (T-249): 22% (Jon). 16% -> 22% (includes director close and T-250 prep, marked +).

### 2026-09-27 | [LOCAL] T-250 | work-workers: patch (2 targets, 10 parked sections) + bank check | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-250-work-workers.md
VERIFY: python tools/project_state.py --check work-workers --stage patch (and --stage research)
USAGE AT START: 22% (Jon).
RESULT: DONE. PASS work-workers / patch and / research. stories 17 (v17 c0 t0), bank 8,486 -> 16,929w, outline
        4,123 -> 6,280w, validator 0. 341,392 tokens, 154 tool uses, 18.0 min (opus).
        Stories: Frank Lumpkin (Wisconsin Steel, 1980; $17M of $40M won), Raef Lawson (Grubhub; 2023 ruling,
        $24.75M settlement 2026). Avoided Dickey, Neufeldt (economy) and Berwick (transportation).
        Ten parked sections folded into eras 06-10. Bank check: 1877 strike, Haymarket, Pullman, Homestead,
        Lattimer, Lawrence, Ludlow, Memorial Day 1937, Duffy's Cut, Monongah, Hawks Nest (109 to ~1,000),
        Upper Big Branch, child labor 1890-1910 and Hammer v. Dagenhart, 2023 meatpacking children, runaway
        servants, braceros, pesticides, heat deaths, Amazon injuries, wage theft, Martin's Hundred and Lowell land.
        Radium Girls audit item resolved (AUDIT-QUEUE note added). SEARCHED NOT FOUND: 3. Several facts tagged
        unconfirmed (search summary only). Parked to disasters and health (both validate 0).
USAGE END (T-250): 27% (Jon). 22% -> 27% (includes director work, marked +).

### 2026-09-27 | [LOCAL] PARALLEL RUN (Jon: "launch five subagents at once", then away) | T-251 to T-255
One-time exception to one-at-a-time, on Jon's explicit instruction. Each agent writes only its own
chapter's files and checkpoint. Material for other chapters goes to its checkpoint's TO PARK
section, and the director files it after all five finish. Director verifies and commits each agent
as it finishes, and launches nothing further until Jon returns.
USAGE AT START: 27% (Jon), for all five together.

### 2026-09-27 | [LOCAL] T-251 | food-farming: patch (3 targets) + bank check | model opus | PARALLEL
STATUS: DONE
CHECKPOINT: control/checkpoints/T-251-food-farming.md
VERIFY: python tools/project_state.py --check food-farming --stage patch (and --stage research)
RESULT: DONE. PASS food-farming / patch and / research. stories 18 -> 17 (v17 c0 t0), bank 6,845 -> 13,721w,
        outline 4,895 -> 6,104w, validator 0. 335,753 tokens, 142 tool uses, 18.1 min (opus, parallel).
        Stories: Matthew Patten (1767 farm diary), Adelaide Wisdom Benjamin (WWII victory garden, National WWII
        Museum oral history). Lowcountry rice-grower slot removed (no named 1700-1750 grower: SEARCHED NOT FOUND),
        told as a group span. Bank check: Nauset seed corn 1620, Powhatan cornfields burned, Monticello rations,
        rice task system and land, pellagra and the 1915 prison experiment, no official Dust Bowl death count, AAA,
        1942 Japanese American farms, braceros, Pigford, pesticides, heat deaths, child farm labor, 2024-25 hunger,
        SNAP cut, H-2A. Corrections: Tudor's ice (180 tons shipped, ~100 arrived); "cheapest meat" unsourced.
        SEARCHED NOT FOUND: 2. TO PARK: 6 items (filed after the parallel run).

### 2026-09-27 | [LOCAL] T-252 | money: patch (2 targets) + bank check | model opus | PARALLEL
STATUS: DONE
CHECKPOINT: control/checkpoints/T-252-money.md
VERIFY: python tools/project_state.py --check money --stage patch (and --stage research)
RESULT: DONE. PASS money / patch and / research. stories 12 (all verified), bank 7,545 -> 14,572w, outline
        5,394 -> 7,377w, validator 0. 333,501 tokens, 164 tool uses, 22.0 min (opus, parallel).
        Stories: no named wildcat shopkeeper or 1970s household found (both SEARCHED NOT FOUND); slots replaced by
        Alpheus Felch (Michigan bank commissioner 1838-39, nails and glass under the coins) and Bruce Bent and
        Henry Brown (first money market fund; "broke the buck" 2008). Bank check: SC loans on enslaved people,
        Owen Sullivan hanged 1756, Louisiana notes on enslaved people, 1807 Treaty of Detroit land, Freedman's Bank
        (~61,000 depositors, 62% repaid, ~31,000 got nothing), 1930-33 losses $1.34B, Maggie Walker, Jesse Binga,
        Greenwood's $1.8M denied claims, S&L crisis, 489 failures 2008-13, 2023 runs, FTX, GENIUS Act.
        "First" fixed: Walker = first Black woman to found a US bank. SEARCHED NOT FOUND: 4. TO PARK: 5 items.
        FLAG FOR JON: the agent reports no chapter tells the 1921 Tulsa massacre (only money's bank loss angle).

### 2026-09-27 | [LOCAL] T-253 | marketplace: patch (3 targets, bank < outline) + bank check | model opus | PARALLEL
STATUS: DONE
CHECKPOINT: control/checkpoints/T-253-marketplace.md
VERIFY: python tools/project_state.py --check marketplace --stage patch (and --stage research)
RESULT: DONE. PASS marketplace / patch and / research. stories 17 (v17 c0 t0), bank 7,596 -> 15,720w, outline
        8,373 -> 10,386w, validator 0. 425,629 tokens, 234 tool uses, 27.9 min (opus, parallel).
        Stories: John Stewart (Dunbar prisoner, Springfield blacksmith, Pynchon ledgers), Emilia Lundberg (ration
        books, son's 2008 Rutgers oral history, paraphrased: quoting needs permission), Renica Turner (Amazon contract
        driver, NPR 2023; settlement approved May 2026). No clash with food-farming's Adelaide Wisdom Benjamin.
        Bank check: Wall Street slave market 1711-62, Christopher Seider shot 1770, the Weeping Time 1859, company
        stores and scrip, Franklin's Gazette ads (277 ads, 308+ people), Winslow's morphine syrup, 1974 ECOA,
        payday loans, driver heat deaths. 6 unsourced outline claims removed or replaced.
        SEARCHED NOT FOUND: 3. TO PARK: 10 items.
PARALLEL RUN COMPLETE: all five PASS research. Next: file the five checkpoints' TO PARK items.

### 2026-09-27 | [LOCAL] T-254 | america-world: patch (2 candidates) + bank check | model opus | PARALLEL
STATUS: DONE
CHECKPOINT: control/checkpoints/T-254-america-world.md
VERIFY: python tools/project_state.py --check america-world --stage patch (and --stage research)
RESULT: DONE. PASS america-world / patch and / research. stories 13 (v13 c0 t0), bank 15,486 -> 22,100w,
        outline 8,931 -> 10,534w, validator 0. 338,734 tokens, 162 tool uses, 20.7 min (opus, parallel).
        Stories: Cathcart verified from his memoir The Captives (1899), which corrected two bank lines (the Maria
        had 6 crew; the survivors went home at different times; notes beside the old lines). Aguinaldo verified
        (Office of the Historian, Army Historical Foundation). Bank check: Menendez's letter on Fort Caroline and
        Matanzas, Timucua and Lenape land, Louisbourg dead, 1783 and the Six Nations, 80,000-100,000 Mexicans in the
        1848 cession, Hawaii actors (Thurston, Dole, Stevens) and the Queen's trial, the water cure at Igbaras
        (Capt. Edwin Glenn), Haiti, DR and Nicaragua occupations, Ponce (Gov. Winship), Law 116 sterilizations
        (defined, method stated), Iran 1953, Guatemala 1954, Chile 1973. NATO "first" corrected.
        SEARCHED NOT FOUND: 1. TO PARK: items for health, war, slavery-freedom. Agent hit the heredoc bug.

### 2026-09-27 | [LOCAL] T-255 | slavery-freedom: patch (1 candidate, 1 target) + bank check | model opus | PARALLEL
STATUS: DONE
CHECKPOINT: control/checkpoints/T-255-slavery-freedom.md
VERIFY: python tools/project_state.py --check slavery-freedom --stage patch (and --stage research)
RESULT: DONE. PASS slavery-freedom / patch and / research. stories 24 (v24 c0 t0), bank 10,697 -> 18,074w,
        outline 6,355 -> 8,414w, validator 0. 353,955 tokens, 151 tool uses, 20.5 min (opus, parallel).
        Stories: Milla Granson verified from Haviland 1881 ("about 200" corrected to her word "hundreds"); target
        replaced by Joycelyn Davis (Africatown, descendant of Charlie Lewis; Smithsonian 2022, NatGeo 2019,
        Descendant 2022). All ten era-zoom lines rewritten (no em dash, no semicolon, actors named). Bank check:
        Middle Passage 13-19% deaths, Equiano, flogging and branding defined with method (1712 SC code, Douglass,
        Ricks ad), NY 1712 and 1741, German Coast 1811, Hemings, Jacobs, Celia, Peter ("The Scourged Back"),
        Memphis and New Orleans 1866, Colfax and Cruikshank, convict leasing, peonage, Choctaw and Chickasaw land.
        SEARCHED NOT FOUND: 3. Perishables: H.R. 40, Evanston, CA SB 518, Maryland override, park exhibits 2025-26.
        TO PARK: 3 items.

### 2026-09-27 | [LOCAL] Parallel-run TO PARK items filed (director, script)
STATUS: DONE
27 items from the T-251..T-255 checkpoints filed verbatim into 13 banks, one "## Parked from `<source>`
(2026-09-27, T-nnn)" section per source and target; items naming two chapters went to both; 1 coordination
note skipped. No outline touched. Re-measured: nothing regressed (native-nations and economy still PASS
prose). Book now: RESEARCHED 17, RESEARCHED* 1 (big-business), PARTIAL 1, SEED 11, WRITTEN 7.
OPEN FOR JON: the 1921 Tulsa massacre is told by no chapter. Parked to crime-justice and rights-movements.

### 2026-09-27 | [LOCAL] AUTONOMOUS MODE from here (Jon: "Non-Stop ... one sub agent at a time"; DECISIONS #24)
Parallel batch usage: 27% -> 60% for all five (logged). Tulsa ruling recorded (DECISIONS #23).

### 2026-09-27 | [LOCAL] T-256a | big-business: bank write-up + checks, eras 1-7 | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-256-big-business.md (units 1-3)
VERIFY: eras 1-7 of the bank written (the gate passes only after T-256b)
USAGE AT START: 60% (Jon).
RESULT: DONE. Units 1-3 landed. big-business already PASSES patch (bank 409 -> 14,209w vs outline 7,228w,
        v14 c0 t0, 0 VERIFY, validator 0). 434,879 tokens, 151 tool uses, 20.0 min (opus).
        Franklin Tarbell verified (Ida Tarbell's 1939 memoir, 1905 obituary); outline corrected (partner's suicide
        ~1892, home mortgaged 1893). Other outline corrections: lottery ban by James I, Sylla-Wright corporation
        counts, Lowell 1826, Biddle comparisons removed (SEARCHED NOT FOUND). PATCHes: Royal African Company
        (186,748 carried, 16,077 died, branding defined), Hancock and Apthorp's 1755 Acadian transports, Homestead
        dead by name, Seneca land at Big Tree, American Tobacco 1890. Workspace lists a Debs story the outline
        lacks (left for the writers). T-256b still needed: eras 8-10 stories have no bank behind them yet.

### 2026-09-27 | [LOCAL] T-256b | big-business: bank write-up + checks, eras 8-10, final | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-256-big-business.md (units 4-6)
VERIFY: python tools/project_state.py --check big-business --stage patch (and --stage research)
RESULT: DONE. PASS big-business / patch and / research. stories 14 (v14 c0 t0), bank 14,209 -> 25,538w, outline
        7,228 -> 8,669w, validator 0. 410,462 tokens, 209 tool uses, 26.1 min (opus).
        Eras 8-10 written up with CORRECTION notes: Taft's suits 75-99 (not 90), Standard Oil into 34, AT&T kept $34B,
        Walmart ~2.5x GM's peak, super PAC figures (Brennan Center), U.S. Steel "first billion" only by stock issued.
        Two self-referencing sentences removed. Added: La Follette committee, tobacco 1954-2006, Johns-Manville,
        GM and Nader, Bhopal, Enron, Purdue Pharma, tech antitrust cases (Amazon trial 29 Mar 2027). SEARCHED NOT
        FOUND: 1. Parked to drugs-alcohol and health (both validate 0).
        The agent ended with a background process still open. The director stopped it (TaskStop) after its files
        landed, so it could not write into health or drugs-alcohol during the ten-agent batch.
NOTE (Jon, while T-256b runs): the 5-hour window reset to 0%. After T-256b, launch TEN agents at once (one
batch), then return to one at a time. Checkpoints for the batch prepared: T-257 exploration (full, all eras),
T-258 government-politics (bank check, all eras), T-259a war 1-5, T-260a religion 1-5, T-261a education 1-5,
T-262a rights-movements 1-6 (bank checks), T-263a health, T-264a disasters, T-265a crime-justice,
T-266a drugs-alcohol (full research, eras 1-5). Ten distinct chapters, so no two agents share a file.

### 2026-09-27 | [LOCAL] TEN-AGENT BATCH (Jon: launch 10 at once, then back to one at a time) | T-257 to T-266a
USAGE AT START: 0% (Jon: window reset). Each agent writes only its own chapter; TO PARK filed after.

### 2026-09-27 | [LOCAL] T-257 | exploration: full, eras 1-10 | model opus | BATCH10
STATUS: PARTIAL
CHECKPOINT: control/checkpoints/T-257-exploration.md
VERIFY: python tools/project_state.py --check exploration --stage research
RESULT: KILLED by the usage limit (12:50 reset). Work landed and committed as partial. FAIL  exploration / research. Stopped at: Unit 1, era 06 (1800-1850), the big one: L&C, Sacagawea, York, Pike, Colter, Glass, Jedediah Smith, Bridger, Fremont, Wilkes. 5 candidates here.
        Salvage: 117 fetched URLs + stop point written into the checkpoint. Continuation queued (one at a time).

### 2026-09-27 | [LOCAL] T-258 | government-politics: bankcheck, eras 1-10 | model opus | BATCH10
STATUS: PARTIAL
CHECKPOINT: control/checkpoints/T-258-government-politics.md
VERIFY: python tools/project_state.py --check government-politics --stage research
RESULT: KILLED by the usage limit (12:50 reset). Work landed and committed as partial. PASS  government-politics / research. Stopped at: Unit 1 in progress: eras 1-7 written to bank; now eras 8-10 (web search quota hit at 12:50 reset; using WebFetch/curl)
        Salvage: 370 fetched URLs + stop point written into the checkpoint. Continuation queued (one at a time).

### 2026-09-27 | [LOCAL] T-259a | war: bankcheck, eras 1-5 | model opus | BATCH10
STATUS: DONE
CHECKPOINT: control/checkpoints/T-259-war.md
VERIFY: python tools/project_state.py --check war --stage research
RESULT: DONE. PASS  war / research. (finished before the limit; its final report was lost to the kill)

### 2026-09-27 | [LOCAL] T-260a | religion: bankcheck, eras 1-5 | model opus | BATCH10
STATUS: PARTIAL
CHECKPOINT: control/checkpoints/T-260-religion.md
VERIFY: python tools/project_state.py --check religion --stage research
RESULT: KILLED by the usage limit (12:50 reset). Work landed and committed as partial. PASS  religion / research. Stopped at: T-260a Unit 1: bank check eras 1-5 (reading slices, 2026-09-27)
        Salvage: 316 fetched URLs + stop point written into the checkpoint. Continuation queued (one at a time).

### 2026-09-27 | [LOCAL] T-261a | education: bankcheck, eras 1-5 | model opus | BATCH10
STATUS: DONE
CHECKPOINT: control/checkpoints/T-261-education.md
VERIFY: python tools/project_state.py --check education --stage research
RESULT: DONE. PASS  education / research. (reported normally)

### 2026-09-27 | [LOCAL] T-262a | rights-movements: bankcheck, eras 1-6 | model opus | BATCH10
STATUS: PARTIAL
CHECKPOINT: control/checkpoints/T-262-rights-movements.md
VERIFY: python tools/project_state.py --check rights-movements --stage research
RESULT: KILLED by the usage limit (12:50 reset). Work landed and committed as partial. PASS  rights-movements / research. Stopped at: T-262a Unit 1: eras 2-5 patched in the bank. Working era 6 (abolitionist mobs 1835-38, Maria Stewart, Crandall opponents, Seneca Falls backlash, ASD 1
        Salvage: 303 fetched URLs + stop point written into the checkpoint. Continuation queued (one at a time).

### 2026-09-27 | [LOCAL] T-263a | health: full, eras 1-5 | model opus | BATCH10
STATUS: PARTIAL
CHECKPOINT: control/checkpoints/T-263-health.md
VERIFY: python tools/project_state.py --check health --stage research
RESULT: KILLED by the usage limit (12:50 reset). Work landed and committed as partial. FAIL  health / research. Stopped at: T-263a Unit 1: era 03 1600s (research, then outline + bank)
        Salvage: 139 fetched URLs + stop point written into the checkpoint. Continuation queued (one at a time).

### 2026-09-27 | [LOCAL] T-264a | disasters: full, eras 1-5 | model opus | BATCH10
STATUS: PARTIAL
CHECKPOINT: control/checkpoints/T-264-disasters.md
VERIFY: python tools/project_state.py --check disasters --stage research
RESULT: KILLED by the usage limit (12:50 reset). Work landed and committed as partial. FAIL  disasters / research. Stopped at: T-264a Unit 1, era 04 (1700-1750): Cascadia 1700, Boston 1711, 1715 Spanish fleet hurricane, Charleston 1740 fire, NY 1741 fires (blame; slavery-freed
        Salvage: 133 fetched URLs + stop point written into the checkpoint. Continuation queued (one at a time).

### 2026-09-27 | [LOCAL] T-265a | crime-justice: full, eras 1-5 | model opus | BATCH10
STATUS: PARTIAL
CHECKPOINT: control/checkpoints/T-265-crime-justice.md
VERIFY: python tools/project_state.py --check crime-justice --stage research
RESULT: KILLED by the usage limit (12:50 reset). Work landed and committed as partial. FAIL  crime-justice / research. Stopped at: T-265a Unit 1, era 3 (1600s): bank partly written. Outline era 3 still seed. To do: Ratcliffe 1631, watch, punishments definitions, Sassamon trial 167
        Salvage: 165 fetched URLs + stop point written into the checkpoint. Continuation queued (one at a time).

### 2026-09-27 | [LOCAL] T-266a | drugs-alcohol: full, eras 1-5 | model opus | BATCH10
STATUS: PARTIAL
CHECKPOINT: control/checkpoints/T-266-drugs-alcohol.md
VERIFY: python tools/project_state.py --check drugs-alcohol --stage research
RESULT: KILLED by the usage limit (12:50 reset). Work landed and committed as partial. FAIL  drugs-alcohol / research. Stopped at: T-266a Unit 1, era 04 1700-1750 (research in progress)
        Salvage: 219 fetched URLs + stop point written into the checkpoint. Continuation queued (one at a time).

### 2026-09-27 | [LOCAL] RECOVERY after the ten-agent batch hit the usage limit (automated reset message)
Drill run. MEASURED: 2 of 10 finished (T-261a education, T-259a war; war's report was lost to the kill but
its checkpoint and check show DONE). 8 killed partway with about 2,900 lines on disk, all outlines validate 0.
Each chapter committed separately (partial ones as PARTIAL). Salvage: each partial checkpoint now has a
SALVAGE section (stop point, "treat that unit as possibly half-written", fetched URLs).
LESSON: ten Opus agents at once used the whole 5-hour window before any but two could finish, and they also
exhausted the web-search quota. Five at once fitted (27% -> 60%). Ten does not.
CONTINUATIONS, one at a time (Jon): T-258r, T-262r, T-260r, T-257r, T-263r, T-264r, T-265r, T-266r.

### 2026-09-27 | [LOCAL] T-258r | government-politics: continue the bank check (eras 8-10 left) | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-258-government-politics.md (read SALVAGE first)
VERIFY: python tools/project_state.py --check government-politics --stage research
RESULT: DONE. PASS  government-politics / research. measured: stage=RESEARCHED eras=10/10 stories=14 (v14 c0 t0) verify_tags=0 bank=29973w outline=11283w manuscript=0w validator_errors=0
        202475 tokens, 104 tool uses, 11.7 min (opus). Eras 8-10 bank check done (Guinn, Breedlove, Allwright, Teapot Dome, Box 13, VRA counts, Moss verdict, Jan 2025 pardons, Menendez, felony disenfranchisement 2024); era 7 secession closed. ~12 unconfirmed tags. Parked 5 items to crime-justice.

### 2026-09-27 | [LOCAL] T-262r | rights-movements: continue bank check eras 1-6 (era 6 left) | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-262-rights-movements.md
VERIFY: python tools/project_state.py --check rights-movements --stage research
RESULT: DONE. PASS  rights-movements / research. measured: stage=RESEARCHED eras=10/10 stories=25 (v25 c0 t0) verify_tags=0 bank=62860w outline=32606w manuscript=0w validator_errors=0
        183493 tokens, 89 tool uses, 9.5 min (opus). Era 6 written from scratch (the first agent saved none): Boston mob 1835, Lovejoy 1837, Pennsylvania Hall 1838, Maria Stewart, Crandall's opponents (Judson), women's removal petitions, gag rule, Seneca Falls (James Mott chaired day 2), deaf-school grants, Cayuga land. 2 searched-not-found. Parked Lovejoy to news-communication.
NOTE (Jon, during T-262r, usage 46%): after T-262r, burst of two, then one at a time. DECISIONS #25 (burst mode only on Jon's word).

### 2026-09-27 | [LOCAL] T-260r | religion: continue bank check eras 1-5 [BURST of 2] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-260-religion.md
VERIFY: python tools/project_state.py --check religion --stage research
RESULT: DONE. PASS  religion / research. measured: stage=RESEARCHED eras=10/10 stories=18 (v18 c0 t0) verify_tags=0 bank=48179w outline=22144w manuscript=0w validator_errors=0
        255032 tokens, 75 tool uses, 10.8 min (opus). Eras 4-5 done (1-3 had landed): Apalachee 1704 (Moore; counts hundreds to 4,300+), John Ury 1741, Stockbridge land, California missions from 1769 (no chapter had them: 85,840 baptisms vs 59,538 deaths, flogging defined), Kumeyaay 1775, Toypurina 1785, Gnadenhutten, Andrew Bryan's congregation whipped. 3 searched-not-found. TO PARK 5 (burst).

### 2026-09-27 | [LOCAL] T-257r | exploration: continue full research, from era 6 [BURST of 2] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-257-exploration.md
VERIFY: python tools/project_state.py --check exploration --stage research
RESULT: DONE. PASS  exploration / research. measured: stage=RESEARCHED eras=10/10 stories=35 (v35 c0 t0) verify_tags=0 bank=24308w outline=11139w manuscript=0w validator_errors=0
        462837 tokens, 150 tool uses, 29.4 min (opus). Eras 06-10 researched (06 from scratch), bank check all eras. All 9 candidates verified (35 stories). York, Sacagawea, Fremont's massacres, Beckwourth and Sand Creek, Henson with the four Inuit men, Minik, Columbia. ~15 unsupported firsts corrected. 3 searched-not-found. TO PARK 7 (burst).

### 2026-09-27 | [LOCAL] Burst-of-two done; TO PARK filed (director, script)
18 items from T-257, T-259, T-260 and T-261 checkpoints filed verbatim into 7 banks (america-world, crime-justice,
native-nations, rights-movements, science, slavery-freedom, war); each checkpoint's TO PARK header marked FILED.
Back to ONE AT A TIME (DECISIONS #25). Next: T-263r health.

### 2026-09-27 | [LOCAL] T-263r | health: continue full research eras 1-5 (from era 3) | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-263-health.md
VERIFY: python tools/project_state.py --check health --stage research
RESULT: LANDED. FAIL  health / research. measured: stage=PARTIAL eras=10/10 stories=18 (v12 c0 t6) verify_tags=3 bank=13062w outline=6615w manuscript=0w validator_errors=0
        313713 tokens, 140 tool uses, 24.4 min (opus). Eras 1-5 researched (era 3 from scratch). Stories: Samuel Fuller, Tryntje Jonas, Onesimus, Zabdiel Boylston, Elizabeth Phillips, Doctor Caesar, Benjamin Rush, Absalom Jones and Richard Allen. Epidemics 1616-1738, Fort Pitt blankets 1763 (actors named), Jack and Jackey, Doctors' Riot 1788. 4 searched-not-found, 2 firsts dropped. Era 1 has no story (allowed: no named person). Chapter FAIL expected until eras 6-10. TO PARK 8.

### 2026-09-27 | [LOCAL] T-264r | disasters: continue full research eras 1-5 [BURST of 5] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-264-disasters.md
VERIFY: python tools/project_state.py --check disasters --stage research
RESULT: LANDED. FAIL  disasters / research. measured: stage=PARTIAL eras=10/10 stories=12 (v4 c0 t8) verify_tags=5 bank=13121w outline=5234w manuscript=0w validator_errors=0
        303149 tokens, 114 tool uses, 17.3 min (opus). Eras 4-5 done (1-3 had landed) + bank check. Cascadia 1700, 1715 fleet hurricane (1,000 or 1,500), Boston 1711, Charleston 1700/1740 (relief to the wealthy), 1727 quake; era 5 now full; new story Will (freed 1796 after saving St. Philip's). Franklin candidate removed (city-building tells him). Castle Rock and Croatan corrections. 6 searched-not-found. Chapter FAIL expected until eras 6-10. TO PARK 2.

### 2026-09-27 | [LOCAL] T-265r | crime-justice: continue full research eras 1-5 [BURST of 5] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-265-crime-justice.md
VERIFY: python tools/project_state.py --check crime-justice --stage research
RESULT: LANDED. FAIL  crime-justice / research. measured: stage=PARTIAL eras=10/10 stories=10 (v6 c0 t4) verify_tags=2 bank=11791w outline=5607w manuscript=0w validator_errors=0
        323848 tokens, 110 tool uses, 14.0 min (opus). Eras 1-5 researched and bank-checked (era 3 finished). Stories: Philip Ratcliffe 1631, Rebecca Nurse, Quack and Cuffee 1741, Patrick Lyon 1798. Punishments defined with method (policy 3b), slave patrols, Virginia 1723 act, convict transport, debt jail, Boston Massacre trials, Conestoga 1763 (20 named, no prosecution), Walnut Street 1790. Chapter FAIL is expected: remaining gaps are eras 6-10 (T-265b). TO PARK 3 (burst).

### 2026-09-27 | [LOCAL] T-266r | drugs-alcohol: continue full research eras 1-5 [BURST of 5] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-266-drugs-alcohol.md
VERIFY: python tools/project_state.py --check drugs-alcohol --stage research
RESULT: LANDED. FAIL  drugs-alcohol / research. measured: stage=PARTIAL eras=10/10 stories=13 (v6 c1 t6) verify_tags=9 bank=11488w outline=5649w manuscript=0w validator_errors=0
        293054 tokens, 100 tool uses, 24.0 min (opus). Era 4 from scratch, era 5, bank check (1-3 had landed). Molasses Act, Boston taverns, Virginia 1705 treating law, Georgia rum ban and Tomochichi, Hamilton's 1744 tavern diary; drinking estimates 1770s/1790 vs NIAAA 2023, Rhode Island rum and the Sally, enslaved distillers, Hagler, Handsome Lake, Whiskey Rebellion. Stories: Hamilton, Rush, Philip Vigol. 4 searched-not-found. Background process stopped by director. Chapter FAIL expected until eras 6-10. TO PARK 5.

### 2026-09-27 | [LOCAL] T-259b | war: bank check eras 6-10 [BURST of 5] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-259-war.md
VERIFY: python tools/project_state.py --check war --stage research
RESULT: DONE. PASS  war / research. measured: stage=RESEARCHED eras=10/10 stories=19 (v19 c0 t0) verify_tags=0 bank=38551w outline=14377w manuscript=0w validator_errors=0
        430744 tokens, 188 tool uses, 23.4 min (opus). Eras 6-10 bank check: 24 PATCHes (draft exemptions, Creek War, Bad Axe, Sand Creek/Bear River/Marias, Union prison camps, Houston 1917, Port Chicago, Bataan, Tokyo firebombing, Korean and Vietnamese dead, POWs, Agent Orange, Castle Bravo, Haditha, Kabul 2021). My Lai corrected from the Peers report (175 to 400+, rape). New story candidates in the bank: Silas Soule, the Hofer brothers, Isaac Woodard. Two outline lines out of date (flagged). Bank 29,251 -> 38,551w. 1 searched-not-found. TO PARK listed.
NOTE (Jon, 20% usage): BURST OF 5 = T-263r health (already running; messaged to switch to TO PARK) + T-264r, T-265r,
T-266r, T-259b. Then back to one at a time.

### 2026-09-27 | [LOCAL] Burst of 5 done; TO PARK filed (director, script)
All five landed: T-259b war (PASS, war complete), T-263r health, T-264r disasters, T-265r crime-justice,
T-266r drugs-alcohol (eras 1-5 each; chapters FAIL until eras 6-10, as expected). T-266r ended with a
background process open: stopped by the director before filing. 28 parked items filed into 12 banks.
Back to ONE AT A TIME (DECISIONS #25).
NEXT (one at a time): T-260b religion 6-10 (split), T-261b education 6-10 (split x3), T-262b rights 7-10
(split x3), T-263b health 6-10, T-264b disasters 6-10, T-265b crime-justice 6-10 (Tulsa justice angle),
T-266b drugs-alcohol 6-10, then the 7 seeds: news-communication, art, music, storytelling-evolution,
styles, sports-play, holidays.

### 2026-09-27 | [LOCAL] T-263b | health: full research eras 6-8 (T-263c does 9-10) | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-263-health.md
VERIFY: python tools/project_state.py --check health --stage research
RESULT: LANDED. FAIL  health / research. measured: stage=PARTIAL eras=10/10 stories=21 (v18 c0 t3) verify_tags=1 bank=23853w outline=12121w manuscript=0w validator_errors=0
        390530 tokens, 175 tool uses, 26.1 min (opus). Eras 6-8 researched + bank check. Stories: Anarcha, Elizabeth Blackwell, Clara Barton, Hannah Ropes, Susan La Flesche Picotte, Josie Mabel Brown, Charles Pollard, Clara Maass. Sims (fistula and method defined), 1837 smallpox, freed people's smallpox, Tuskegee course of disease (CDC, Brandt 1978; DECISIONS #3), Guatemala (83 deaths). 2 searched-not-found. Chapter FAIL until eras 9-10 (T-263c). TO PARK 7.

### 2026-09-27 | [LOCAL] T-264b | disasters: full research eras 6-8 [BURST of 3+1] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-264-disasters.md
VERIFY: python tools/project_state.py --check disasters --stage research
RESULT: LANDED. FAIL  disasters / research. measured: stage=PARTIAL eras=10/10 stories=12 (v9 c0 t3) verify_tags=2 bank=26647w outline=11307w manuscript=0w validator_errors=0
        500877 tokens, 179 tool uses, 26.4 min (opus). Eras 6-8 + bank check. Stories: Rebecca Lamar (Pulaski 1838), Victor Heiser (Johnstown), Isaac Cline (Galveston, warning claim disputed), Hugh Kwong Liang (1906, segregated camp), Kate Alterman (Triangle trial), Clara Barton sourced. Blame and neglect: Sultana, Johnstown, Galveston forced burials, 1927 flood camps, Okeechobee coffins, St. Francis Dam. 8 searched-not-found. Chapter FAIL until eras 9-10. TO PARK 3+.

### 2026-09-27 | [LOCAL] T-265b | crime-justice: full research eras 6-8 [BURST of 3+1] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-265-crime-justice.md
VERIFY: python tools/project_state.py --check crime-justice --stage research
RESULT: LANDED. FAIL  crime-justice / research. measured: stage=PARTIAL eras=10/10 stories=11 (v9 c0 t2) verify_tags=1 bank=21418w outline=10973w manuscript=0w validator_errors=0
        350673 tokens, 158 tool uses, 21.0 min (opus). Eras 6-8 + bank check. Stories: Charles Williams (Eastern State no. 1), Henry Smith (burned at Paris TX 1893, no arrest; DECISIONS #2), Pinkerton, Ed Johnson (1906; conviction set aside 2000), Ness and Capone. Tulsa from the justice angle (DECISIONS #23: ~70 indicted mostly Black, only Chief Gustafson convicted, 2001 report, DOJ Jan 2025 review). McIntosh 1836, Dakota trials 1862, LA 1871, Rock Springs 1885, Haymarket, Lexow, Brown v. Mississippi, Scottsboro, Osage investigation, end of convict leasing. 2 searched-not-found. Chapter FAIL until eras 9-10. TO PARK 8.

### 2026-09-27 | [LOCAL] T-266b | drugs-alcohol: full research eras 6-8 [BURST of 3+1] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-266-drugs-alcohol.md
VERIFY: python tools/project_state.py --check drugs-alcohol --stage research
RESULT: LANDED. FAIL  drugs-alcohol / research. measured: stage=PARTIAL eras=10/10 stories=14 (v11 c0 t3) verify_tags=4 bank=22819w outline=11624w manuscript=0w validator_errors=0
        393808 tokens, 133 tool uses, 18.1 min (opus). Eras 6-8 + bank check. Stories: John B. Gough, John Tackett Goolrick (morphine after a war wound), Pemberton, Carry Nation (moved to era 8), Izzy Einstein. Portland Rum Riot 1855 (Neal Dow ordered the shooting), opium laws and the Chinese, Harrison Act, poisoned industrial alcohol (Lowman, Wheeler), jake leg, enforcement deaths (89 or ~1,000), first marijuana arrests. 6 VERIFY cleared, 5 searched-not-found. Chapter FAIL until eras 9-10. TO PARK: 7 chapters.
NOTE (Jon, 47%): burst of 3 more beside T-263b (messaged to switch to TO PARK): T-264b, T-265b, T-266b (eras 6-8 each).

### 2026-09-27 | [LOCAL] Burst of 4 done; TO PARK filed (director, script)
T-263b, T-264b, T-265b, T-266b all landed (eras 6-8; chapters PARTIAL until eras 9-10). Parked items filed into 12 banks, all validate 0.
Jon (69%): burst of two next: T-263c health 9-10 + T-265c crime-justice 9-10.

### 2026-09-27 | [LOCAL] T-263c | health: full research eras 9-10, completes the chapter [BURST of 2] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-263-health.md
VERIFY: python tools/project_state.py --check health --stage research
RESULT: DONE. PASS  health / research. measured: stage=RESEARCHED eras=10/10 stories=23 (v23 c0 t0) verify_tags=0 bank=33926w outline=17200w manuscript=0w validator_errors=0
        406002 tokens, 157 tool uses, 23.1 min (opus). Eras 9-10, chapter COMPLETE. Stories: Salk, Paul Alexander, Henrietta Lacks, the Relf sisters, Ryan White, Sandra Lindsay. Tuskegee end settled (Washington Star 25 Jul 1972; DuVal; suit 1973, settled 1974). COVID deaths 1,245,791 (19 Sep 2026), overdoses 66,937 (12 mo to Apr 2026), life expectancy 79.0 (2024), uninsured 26.7M (2025). Sterilization defined; surgeons unnamed in sources. 2 searched-not-found. TO PARK 8.

### 2026-09-27 | [LOCAL] T-265c | crime-justice: full research eras 9-10, completes the chapter [BURST of 2] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-265-crime-justice.md
VERIFY: python tools/project_state.py --check crime-justice --stage research
RESULT: DONE. PASS  crime-justice / research. measured: stage=RESEARCHED eras=10/10 stories=13 (v13 c0 t0) verify_tags=0 bank=28147w outline=15260w manuscript=0w validator_errors=0
        370245 tokens, 134 tool uses, 21.9 min (opus). Eras 9-10, chapter COMPLETE. Stories: Emmett Till, Clarence Earl Gideon, Kemba Smith, the Exonerated Five. Mapp, Miranda, Gault; death penalty 1972/1976 and yearly counts to 2026, 202-203 exonerations, Stinney; Attica; drug laws and who wrote them; BJS prison counts by race to 2023; Rodney King, Diallo, six killings 2014-2023 incl. George Floyd with outcomes; FBI 2025. 2 searched-not-found. TO PARK 6.
NOTE (Jon, 80%): PAUSE after T-263c and T-265c finish. No new dispatches until Jon says.

### 2026-09-27 | [LOCAL] PAUSED (Jon, 80%)
T-263c health and T-265c crime-justice done: both chapters now PASS research. Parked items filed into 10 banks
(all validate 0; finished chapters still PASS prose). Measured: RESEARCHED 21, WRITTEN 7, PARTIAL 2 (disasters,
drugs-alcohol), SEED 7. Nothing in flight. Queue in control/TODO.md.

### 2026-09-27 | [LOCAL] RESUMED (Jon): burst of 5

### 2026-09-27 | [LOCAL] T-264c | disasters: full research eras 9-10, completes the chapter [BURST5] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-264-disasters.md
VERIFY: python tools/project_state.py --check disasters --stage research
RESULT: DONE. PASS  disasters / research. measured: stage=RESEARCHED eras=10/10 stories=12 (v12 c0 t0) verify_tags=0 bank=35894w outline=16266w manuscript=0w validator_errors=0
        407738 tokens, 129 tool uses, 23.8 min (opus). Eras 9-10, chapter COMPLETE. Stories: Melvin Windsor (Air Florida 1982), Herbert Freeman Jr. (Katrina), Jesse Vazquez (Maria). Counts with whose count: Katrina 1,392 vs 1,833, Maria 64/2,975/4,645, Helene 250, Lahaina 102, Texas Hill Country 136. 9/11 illness deaths, Maui settlement, Eaton and Palisades fires, FEMA 2026. 2 searched-not-found. TO PARK 5.

### 2026-09-27 | [LOCAL] T-266c | drugs-alcohol: full research eras 9-10, completes the chapter [BURST5] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-266-drugs-alcohol.md
VERIFY: python tools/project_state.py --check drugs-alcohol --stage research
RESULT: DONE. PASS  drugs-alcohol / research. measured: stage=RESEARCHED eras=10/10 stories=14 (v14 c0 t0) verify_tags=0 bank=29862w outline=14971w manuscript=0w validator_errors=0
        354068 tokens, 142 tool uses, 18.4 min (opus). Eras 9-10, chapter COMPLETE. Nixon 1971 and its funding, LSD, crack and the 1986 law, MADD (Clarence Busch named), drinking age 21, 1953 end of the federal liquor ban on Native land, OxyContin 1996; overdoses by year to Apr 2026, fentanyl, Purdue and the Sacklers (Apr 2026 sentence, May 2026 shutdown), settlements, 24 legal-marijuana states and the Apr 2026 rescheduling, vaping. Stories: Jeffrey Wigand, Betty Ford, Nan Goldin. 4 searched-not-found. TO PARK 8.

### 2026-09-27 | [LOCAL] T-260b | religion: bank check eras 6-8 [BURST5] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-260-religion.md
VERIFY: python tools/project_state.py --check religion --stage research
RESULT: DONE. PASS  religion / research. measured: stage=RESEARCHED eras=10/10 stories=18 (v18 c0 t0) verify_tags=0 bank=55431w outline=22144w manuscript=0w validator_errors=0
        291684 tokens, 99 tool uses, 11.9 min (opus). Eras 6-8 bank check (bank only, outline untouched). California missions 1800-48 (Quintana, Olbes, Zalvidea, 1824 Chumash War, Estanislao), Mormons in Missouri (Haun's Mill 17 or 18), Carthage 1844 (9 indicted, 5 acquitted), Charlestown convent, Douglass on religion and slavery, Nauvoo on Sauk and Meskwaki land, Mountain Meadows (~120; killers named; Lee executed), Reynolds 1879, Order No. 11, Ghost Dance from Mooney 1896, Leo Frank, second Klan, 1940 attacks on Jehovah's Witnesses. 1 searched-not-found; 4 unsupported outline lines flagged. TO PARK 8.

### 2026-09-27 | [LOCAL] T-261b | education: bank check eras 6-7 [BURST5] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-261-education.md
VERIFY: python tools/project_state.py --check education --stage research
RESULT: DONE. PASS  education / research. measured: stage=RESEARCHED eras=10/10 stories=21 (v21 c0 t0) verify_tags=0 bank=66943w outline=29106w manuscript=0w validator_errors=0
        276031 tokens, 88 tool uses, 11.3 min (opus). Eras 6-7 bank check. State-by-state penalties for teaching enslaved people (Woodson 1915); Margaret Douglass jailed 1854 (constable, mayor, judge named); Freedmen's Bureau reports on attacks on schools; William Luke 1870; Tennessee statutes, Plessy, Cumming 1899; boarding schools from the 1819 Civilization Fund and Choctaw Academy, 2022 and 2024 federal report figures, 1893 ration act, 9 named Carlisle children; Morrill land (~10.7M acres, ~250 nations); Noyes Academy 1835; Webster 60M sourced. 3 searched-not-found. TO PARK 7.

### 2026-09-27 | [LOCAL] T-262b | rights-movements: bank check era 7 [BURST5] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-262-rights-movements.md
VERIFY: python tools/project_state.py --check rights-movements --stage research
RESULT: DONE. PASS  rights-movements / research. measured: stage=RESEARCHED eras=10/10 stories=25 (v25 c0 t0) verify_tags=0 bank=69945w outline=34259w manuscript=0w validator_errors=0
        293750 tokens, 104 tool uses, 14.5 min (opus). Era 7 bank check: 11 PATCHes. Wilmington coup 1898 (no chapter told it: Waddell, 500-2,000 men, 14-60 dead, no one charged) added as a span; Frances Thompson's 1876 arrest; allotment reformers and Dawes, Elk v. Wilkins; Ponca and Paiute removals with actors; Geary Act refusal; Yick Wo; Wong Kim Ark; Memphis 1892. Reconstruction violence pointed to slavery-freedom. 2 firsts removed, 2 searched-not-found. TO PARK listed.

### 2026-09-27 | [LOCAL] Burst of 5 done; TO PARK filed (director, script)
All five PASS: T-264c disasters and T-266c drugs-alcohol complete their chapters; T-260b religion 6-8,
T-261b education 6-7, T-262b rights-movements 7 bank checks landed. Parked items filed into 14 banks (all
validate 0; the 7 written chapters still PASS prose). One afterword item saved to AUDIT-QUEUE.
MEASURED: RESEARCHED 23 + WRITTEN 7 = 30 of 37 pass research. SEED 7 left.
Back to ONE AT A TIME.

### 2026-09-27 | [LOCAL] T-262c | rights-movements: bank check era 8 (LEADS Tulsa 1921) | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-262-rights-movements.md
VERIFY: python tools/project_state.py --check rights-movements --stage research
RESULT: DONE. PASS  rights-movements / research. measured: stage=RESEARCHED eras=10/10 stories=26 (v26 c0 t0) verify_tags=0 bank=76921w outline=36915w manuscript=0w validator_errors=0
        344607 tokens, 131 tool uses, 19.1 min (opus). Era 8 bank check; LEADS Tulsa 1921 (DECISIONS #23): DOJ Jan 2025 report read in full; 4 new spans (Greenwood before, the camps 4,000-6,000 held, the 7 Jun 1921 fire ordinance and B. C. Franklin, survivors' campaign 1997-2026 and graves search); new story viola-fletcher (2021 testimony). Red Summer 1919 (no chapter had it), Henry Gerber 1924, Mexican Repatriation, Isaac Woodard, Japanese American incarceration actors. 4 outline corrections, 4 unsourced lines removed. 1 searched-not-found. Pointers parked in crime-justice and war.
NOTE (Jon): PAUSE after T-262c finishes. No new dispatches until Jon says.

### 2026-09-27 | [LOCAL] PAUSED (Jon) after T-262c. Nothing in flight.

### 2026-09-27 | [LOCAL] RESUMED (Jon): burst of 5, five distinct chapters

### 2026-09-27 | [LOCAL] T-260c | religion: bank check eras 9-10 [BURST5] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-260-religion.md
VERIFY: python tools/project_state.py --check religion --stage research
RESULT: DONE. PASS  religion / research. measured: stage=RESEARCHED eras=10/10 stories=18 (v18 c0 t0) verify_tags=0 bank=60787w outline=22218w manuscript=0w validator_errors=0
        284961 tokens, 110 tool uses, 14.5 min (opus). Eras 9-10 bank check; religion's checks COMPLETE. Smith and Black (peyote), Lyng 1988, RFRA 1993/1997, eagle-feather rule; Atlanta Temple 1958, Arizona temple 1991, church arsons 1996-99; Waco (two reports; House 1996 on who fired first); Jonestown; bishops' May 2026 audit, SBC 2022 report; Sutherland Springs, Poway, Minneapolis, Grand Blanc; FBI 2025; Mahmoud v. Taylor 2025; Oak Flat 2026. Corrections: Oak Creek 7 dead (Punjab Singh), Texas Ten Commandments law upheld 9-8 on 21 Apr 2026, a self-reference rewritten. 1 searched-not-found. TO PARK 6.

### 2026-09-27 | [LOCAL] T-261c | education: bank check era 8 [BURST5] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-261-education.md
VERIFY: python tools/project_state.py --check education --stage research
RESULT: DONE. PASS  education / research. measured: stage=RESEARCHED eras=10/10 stories=21 (v21 c0 t0) verify_tags=0 bank=70528w outline=30013w manuscript=0w validator_errors=0
        214415 tokens, 79 tool uses, 9.3 min (opus). Era 8 bank check: 9 PATCHes. 1917 funding survey ($10.32 vs $2.89; county officers named), Lemon Grove 1931, Delgado v. Bastrop 1948, camp schools (Manzanar, Poston on Colorado River Indian land), 1920 attendance law, Carlisle to the War Department 1918, 1928 Senate hearing (Tilford Denver, Swanson Mowachean, principal named), Scopes textbook's race ranking, 1891 act confirmed. 2 searched-not-found. TO PARK 5.

### 2026-09-27 | [LOCAL] T-262d | rights-movements: bank check era 9 [BURST5] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-262-rights-movements.md
VERIFY: python tools/project_state.py --check rights-movements --stage research
RESULT: DONE. PASS  rights-movements / research. measured: stage=RESEARCHED eras=10/10 stories=26 (v26 c0 t0) verify_tags=0 bank=82295w outline=38970w manuscript=0w validator_errors=0
        306900 tokens, 117 tool uses, 16.8 min (opus). Era 9 bank check. Killers named with outcomes: De La Beckwith (1994), Neshoba (7 of 18 in 1967, Killen 2005), Birmingham (Chambliss, Blanton, Cherry), Fowler (2010), Reeb's attackers acquitted, Liuzzo (3 convicted, informant Rowe), Hamer's beaters acquitted, King (Ray, 1999 civil verdict, DOJ 2000). New spans: Stonewall and gay rights 1953-79 (the open gap), women's movement and ERA, Chicano movement (Salazar), Japanese American redress. 4 corrections incl. Claudette Colvin (d. 13 Jan 2026). TO PARK listed.

### 2026-09-27 | [LOCAL] T-270a | news-communication: full research eras 1-5 [BURST5] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-270-news-communication.md
VERIFY: python tools/project_state.py --check news-communication --stage research
RESULT: LANDED. FAIL  news-communication / research. measured: stage=PARTIAL eras=10/10 stories=19 (v10 c8 t1) verify_tags=5 bank=12519w outline=6321w manuscript=0w validator_errors=0
        452183 tokens, 225 tool uses, 29.0 min (opus). Eras 1-5 researched + bank check. 10 stories verified: Manteo, Benjamin Harris, Catua and Omtua, Anna Zenger, Elizabeth Timothy, Franklin, Isaac Bissell (not Israel), Paine, Mary Katharine Goddard, Matthew Lyon. John Peter Zenger story removed (told elsewhere; span prose here). 1673 post rider, Zenger verdict corrected, Common Sense counts, Sedition Act prosecutions, runaway and sale ads, Roanoke land. 5 searched-not-found. Chapter FAIL until eras 6-10. TO PARK 11.

### 2026-09-27 | [LOCAL] T-273a | holidays: full research eras 1-5 [BURST5] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-273-holidays.md
VERIFY: python tools/project_state.py --check holidays --stage research
RESULT: LANDED. FAIL  holidays / research. measured: stage=PARTIAL eras=10/10 stories=8 (v4 c1 t3) verify_tags=9 bank=8887w outline=6090w manuscript=0w validator_errors=0
        374030 tokens, 218 tool uses, 29.1 min (opus). Eras 1-5 researched + bank check. Native ceremonial calendars (Haudenosaunee Thanksgiving Address, Wampanoag, Green Corn per Bartram 1791, Hopi Soyal, First Salmon, Makahiki), St. Augustine and Onate thanksgivings with Matanzas, Plymouth 1621, the 1637 Pequot War thanksgivings, 1659 Christmas law, Pope's Night, Pinkster, Black governors, 1777 Fourth, Christmas for the enslaved. Stories: Bradford, Henry Wight, John Anderson. 4 searched-not-found. Chapter FAIL until eras 6-10. TO PARK 7.

### 2026-09-27 | [LOCAL] Burst of 5 done; TO PARK filed (director, script)
All five landed: T-260c (religion's checks complete), T-261c education 8, T-262d rights-movements 9 (all PASS);
T-270a news-communication 1-5 and T-273a holidays 1-5 (PARTIAL until eras 6-10). Parked items filed into 12
banks + research-storytelling-evolution.md created to hold one item; one afterword item to AUDIT-QUEUE.
All validate 0; the 7 written chapters still PASS prose. Back to ONE AT A TIME.

### 2026-09-27 | [LOCAL] T-262e | rights-movements: bank check era 10, last agent on the chapter | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-262-rights-movements.md
VERIFY: python tools/project_state.py --check rights-movements --stage research
RESULT: DONE. PASS  rights-movements / research. measured: stage=RESEARCHED eras=10/10 stories=26 (v26 c0 t0) verify_tags=0 bank=88107w outline=41091w manuscript=0w validator_errors=0
        319973 tokens, 119 tool uses, 15.8 min (opus). Era 10 bank check; rights-movements checks COMPLETE. Standing Rock (Dalrymple, Kirchmeier; 2023 and Jun 2026 rulings; permit back 2026; Greenpeace verdict cut to $345M), DACA (~455,000 Mar 2026), Minneapolis killings Jan 2026 (agents named, no charges), Women's March, Dobbs and state laws to Aug 2026, ERA, Stonewall monument, 2025-26 transgender actions and rulings, John Lewis bill, Louisiana 2026 map, DOJ dropping police suits 2025, 23 Sep 2026 integration-rule ruling. 3 new spans. Parked to native-nations and immigration.
NOTE (Jon): PAUSE after T-262e finishes. No new dispatches until Jon says.

### 2026-09-28 | [LOCAL] RESUMED after the usage reset (Jon: "Please continue"). One at a time.

### 2026-09-27 | [LOCAL] T-261d | education: bank check era 9 | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-261-education.md
VERIFY: python tools/project_state.py --check education --stage research
RESULT: DONE. PASS  education / research. measured: stage=RESEARCHED eras=10/10 stories=21 (v21 c0 t0) verify_tags=0 bank=75157w outline=31077w manuscript=0w validator_errors=0
        253287 tokens, 87 tool uses, 12.3 min (opus). Era 9 bank check: 9 PATCHes. Prince Edward (Wall, Crawford, Fitzpatrick; Almond's 1958 closings), Little Rock's closed year, New Orleans 1960 (Davis, Perez), Ole Miss 1962 (Guihard, Gunter; 75-300+ injured) as a new span, South Boston High (Phyllis Ellison), Hernandez v. Driscoll 1957, boarding schools after 1950 (Ronald and Willie B. Yazzie, 1968), ICWA 1978, paddling counts 1976-2000. 2 firsts removed. 2 searched-not-found. Pointers parked in rights-movements.

### 2026-09-27 | [LOCAL] T-261e | education: bank check era 10, last agent on the chapter | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-261-education.md
VERIFY: python tools/project_state.py --check education --stage research
RESULT: DONE. PASS  education / research. measured: stage=RESEARCHED eras=10/10 stories=21 (v21 c0 t0) verify_tags=0 bank=80695w outline=32417w manuscript=0w validator_errors=0
        295513 tokens, 131 tool uses, 15.5 min (opus). Era 10 bank check; education checks COMPLETE. School shootings (federal count 2021-22; Sandy Hook, Parkland, Uvalde from official reports incl. the 77 minutes and Arredondo; 2026 trials; Apalachee 2024), boarding-school reports and 2024 apology, book removals (PEN, ALA, EdWeek), Education Department 2025-26 (4,133 to 2,183 staff, Supreme Court order), NAEP 2022 and Sept 2025, corporal punishment 2021-22 newest national count, teacher pay 2024-25. 4 new spans. Pointer parked in crime-justice.

### 2026-09-27 | [LOCAL] T-270b | news-communication: full research eras 6-8 (T-270c does 9-10) | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-270-news-communication.md
VERIFY: python tools/project_state.py --check news-communication --stage research
RESULT: LANDED. FAIL  news-communication / research. measured: stage=PARTIAL eras=10/10 stories=22 (v19 c2 t1) verify_tags=1 bank=26459w outline=13737w manuscript=0w validator_errors=0
        478823 tokens, 187 tool uses, 27.9 min (opus). Eras 6-8 + bank check. Stories: Boudinot, Lovejoy, Douglass, Nellie Bly, Ida B. Wells, William Cooper Nell, Robert S. Abbott, Victor Berger, Murrow (Tarbell story removed: big-business tells it). Cherokee Phoenix press seized 1835, whites-only mail carrier law 1802-65, Charleston mail burning, Garrison mob, Civil War closures, Western Union, Wilmington 1898, 1917-18 mail bans and 2,000+ Espionage/Sedition cases, radio ownership, WWII censorship, camp newspapers. 6 searched-not-found. Chapter FAIL until eras 9-10.

### 2026-09-27 | [LOCAL] T-270c | news-communication: full research eras 9-10, completes the chapter | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-270-news-communication.md
VERIFY: python tools/project_state.py --check news-communication --stage research
RESULT: DONE. PASS  news-communication / research. measured: stage=RESEARCHED eras=10/10 stories=23 (v23 c0 t0) verify_tags=0 bank=35857w outline=18134w manuscript=0w validator_errors=0
        357246 tokens, 168 tool uses, 21.7 min (opus). Eras 9-10, chapter COMPLETE. Stories: Cronkite, Woodward and Bernstein (the 'brought down a president' line corrected), Jeff German (killed 2022 by the official he reported on), Darnella Frazier. WLBT license case, Pentagon Papers, fairness doctrine 1987, cable, journalists killed (Bolles, Guihard, five Vietnamese American journalists, Capital Gazette), Medill 2025 news deserts, platform owners, MIT 2018 false-news study, Press Freedom Tracker, 2025-26 public broadcasting cuts. 4 searched-not-found.

### 2026-09-27 | [LOCAL] T-273b | holidays: full research eras 6-8 (T-273c does 9-10) | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-273-holidays.md
VERIFY: python tools/project_state.py --check holidays --stage research
RESULT: LANDED. FAIL  holidays / research. measured: stage=PARTIAL eras=10/10 stories=8 (v6 c0 t2) verify_tags=3 bank=18333w outline=11312w manuscript=0w validator_errors=0
        402103 tokens, 152 tool uses, 20.0 min (opus). Eras 6-8 + bank check. Stories: Sarah Josepha Hale (rebuilt from sources), Jack Yates (Emancipation Park 1872), Anna Jarvis. Christmas under slavery and hiring day, NY 5 July 1827 parade, Albany's 1811 Pinkster ban, Juneteenth and Texas 1868 (379 killed), Norfolk 1866, Decoration Day origins unresolved, New Orleans 1891 (eleven named), Armistice Day, 1939-41 Thanksgiving fight. Corrections: Labor Day 28 Jun 1894, Columbus Day first 1934, Mother's Day law, Alabama 1836 rejected. 4 searched-not-found. Parked to immigration and crime-justice. Chapter FAIL until eras 9-10.

### 2026-09-27 | [LOCAL] T-273c | holidays: full research eras 9-10, completes the chapter | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-273-holidays.md
VERIFY: python tools/project_state.py --check holidays --stage research
RESULT: DONE. PASS  holidays / research. measured: stage=RESEARCHED eras=10/10 stories=9 (v9 c0 t0) verify_tags=0 bank=25975w outline=14586w manuscript=0w validator_errors=0
        337400 tokens, 113 tool uses, 15.2 min (opus). Eras 9-10, chapter COMPLETE. Stories: Liz Byrd (Wyoming Equality Day 1990), Frank James/Wamsutta (1970 speech, National Day of Mourning), Opal Lee (1939 mob burned her family's house). Monday Holiday Act 1968, King Day (votes, holdout states, Arizona 1990), Kwanzaa and Karenga's 1971 conviction stated, Plymouth 1997 arrests, Juneteenth counts, 2025 federal actions, 2026 fee-free days. 2 searched-not-found. TO PARK listed (burst).
NOTE (Jon): two more beside T-273c (messaged to switch to TO PARK): T-267a art 1-5, T-268a music 1-5.

### 2026-09-27 | [LOCAL] T-267a | art: full research eras 1-5 [BURST] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-267-art.md
VERIFY: python tools/project_state.py --check art --stage research
RESULT: LANDED. FAIL  art / research. measured: stage=PARTIAL eras=10/10 stories=30 (v10 c19 t1) verify_tags=83 bank=10933w outline=7097w manuscript=0w validator_errors=0
        371798 tokens, 187 tool uses, 23.3 min (opus). Eras 1-5 researched + bank check; research-art.md created (10,933w). Stories: Prince Demah, Phillis Wheatley (18 attesters counted), Loara Standish, Nathan Jackson (Tlingit carver), Bradstreet, John White, Henrietta Johnston, Smibert, Peale, Gilbert Stuart. Grave diggers named (Squier and Davis, Rogan, Pocola Mining at Spiro), kiva mask burnings, Acoma church labor, the Darnall portrait's chained boy, the Royalls, Lenape portraits before the Walking Purchase. White and Smibert firsts corrected. 7 searched-not-found. Chapter FAIL until eras 6-10 (83 VERIFY, 19 candidates there). TO PARK 10.

### 2026-09-27 | [LOCAL] T-268a | music: full research eras 1-5 [BURST] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-268-music.md
VERIFY: python tools/project_state.py --check music --stage research
RESULT: LANDED. FAIL  music / research. measured: stage=PARTIAL eras=10/10 stories=24 (v4 c19 t1) verify_tags=105 bank=7394w outline=9302w manuscript=0w validator_errors=0
        352279 tokens, 180 tool uses, 23.4 min (opus). Eras 1-5 researched + bank check; research-music.md created (7,394w). Stories: R. Carlos Nakai, Harry (fiddler, 1746 runaway notice), William Billings, Newport Gardner. Broken Flute Cave, Hopewell panpipes, Tlingit clan songs, 1565 Te Deum, Coast Miwok 1579, Bay Psalm Book, New Mexico mission music and 1675 arrests, Stono drums and the 1740 Negro Act s.36, Jefferson's Banjar, Tlingit songs 1791. 4 searched-not-found. Chapter FAIL until eras 6-10. TO PARK for six chapters.

### 2026-09-28 | [LOCAL] Burst of 3 done; TO PARK filed (director, script)
T-273c holidays (chapter COMPLETE), T-267a art 1-5, T-268a music 1-5 (both PARTIAL). Parked items filed into 14 banks,
all validate 0; the 7 written chapters still PASS prose. One art item to AUDIT-QUEUE. Measured: RESEARCHED 25 +
WRITTEN 7 = 32 of 37. Left: art 6-10, music 6-10, storytelling-evolution, sports-play, styles. ONE AT A TIME.

### 2026-09-27 | [LOCAL] T-267b | art: full research eras 6-7 | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-267-art.md
VERIFY: python tools/project_state.py --check art --stage research
RESULT: LANDED. FAIL  art / research. measured: stage=PARTIAL eras=10/10 stories=33 (v19 c13 t1) verify_tags=53 bank=21274w outline=11356w manuscript=0w validator_errors=0
        449516 tokens, 189 tool uses, 24.7 min (opus). Eras 6-7 + bank check. 6 candidates verified (Cole, Douglass, Homer, Edmonia Lewis, Tanner, Twain); new stories Dave Drake (enslavers named, inscriptions), Joseph Whiting Stock (disability thread), Howling Wolf (Sand Creek survivor, Fort Marion). Catlin (Four Bears, Osceola; sold 1852), Mohican land at Catskill, Fort Marion (Sheridan's order; ten dead named), Antietam show, moved Gettysburg body, Met Sundays 1891. 4 seed corrections. 6 searched-not-found. Parked to native-nations, slavery-freedom, education. Chapter FAIL until eras 8-10.

### 2026-09-27 | [LOCAL] T-267c | art: full research eras 8-9 (T-267d does era 10) | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-267-art.md
VERIFY: python tools/project_state.py --check art --stage research
RESULT: LANDED. FAIL  art / research. measured: stage=PARTIAL eras=10/10 stories=33 (v30 c2 t1) verify_tags=10 bank=31586w outline=16425w manuscript=0w validator_errors=0
        488559 tokens, 191 tool uses, 26.4 min (opus). Eras 8-9 + bank check. 11 candidates verified (O'Keeffe, Lange, Lawrence, Savage, Hurston, Martinez, Pollock, Warhol, Parks, Ringgold, Morrison). Savage's 1923 rejection and 1940 bulldozing, WPA denials and the Harlem Artists Guild, Lange's withheld camp photographs, Dorothy Dunn's school, CIA and abstract expressionism (officers' own 1995 statements plus doubters), Chicano Park, AIDS quilt, 1989-90 NEA fights. Florence Owens Thompson corrected; Armory 'first' cut. 4 searched-not-found. Parked to crime-justice, health, native-nations. Chapter FAIL until era 10.

### 2026-09-27 | [LOCAL] T-267d | art: full research era 10, completes the chapter | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-267-art.md
VERIFY: python tools/project_state.py --check art --stage research
RESULT: DONE. PASS  art / research. measured: stage=RESEARCHED eras=10/10 stories=34 (v34 c0 t0) verify_tags=0 bank=38467w outline=19199w manuscript=0w validator_errors=0
        339100 tokens, 141 tool uses, 17.4 min (opus). Era 10, chapter COMPLETE. Stories: Kehinde Wiley, Amy Sherald, Jeffrey Gibson (Venice 2024), Kelly McKernan. NAGPRA 2024 rule and NPS counts (29 May 2026), MFA Boston returned Dave Drake's jars Oct 2025, Rumors of War, Unmanned Drone, MONUMENTS, BLM Plaza removed Mar 2025, Beeple, AI suits to Sep 2026, 2025-26 federal arts cuts, Smithsonian orders. 4 searched-not-found. Parked to music and native-nations. OPEN FOR JON: allegations against Wiley (kept out of the outline, flagged in the bank).

### 2026-09-27 | [LOCAL] T-268b | music: full research eras 6-7 | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-268-music.md
VERIFY: python tools/project_state.py --check music --stage research
RESULT: LANDED. FAIL  music / research. measured: stage=PARTIAL eras=10/10 stories=25 (v10 c14 t1) verify_tags=75 bank=18047w outline=13561w manuscript=0w validator_errors=0
        383539 tokens, 151 tool uses, 20.8 min (opus). Eras 6-7 + bank check; Quinones story added to era 3. Verified: Stephen Foster, Francis Johnson, Ella Sheppard, Sousa, Scott Joplin. Douglass on what the songs meant (the 1836 Canaan hymn), Tubman's hymn signals, Drinking Gourd map claim recorded as disputed, Congo Square, blackface minstrelsy, the banjo's move, Fisk totals ($20,000-$150,000, dated), 1883 rules against Native dances, Carlisle band, first Native recordings 1890. 3 searched-not-found. Chapter FAIL until eras 8-10 (75 VERIFY, 14 candidates).

### 2026-09-27 | [LOCAL] T-268c | music: full research eras 8-9 (T-268d does era 10) | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-268-music.md
VERIFY: python tools/project_state.py --check music --stage research
RESULT: LANDED. FAIL  music / research. measured: stage=PARTIAL eras=10/10 stories=27 (v23 c3 t1) verify_tags=19 bank=29721w outline=20399w manuscript=0w validator_errors=0
        390166 tokens, 208 tool uses, 26.6 min (opus). Eras 8-9 + bank check. 13 verified: Bessie Smith, Armstrong, Maybelle Carter, Guthrie, Billie Holiday, Marian Anderson, DeFord Bailey (new), Elvis, Aretha Franklin, Dylan, DJ Kool Herc, Selena, Bernice Johnson Reagon (new). Who was paid: Thornton's $500 for Hound Dog, Crudup, the Lomax credit, Parker's 50%; DAR refusal; Strange Fruit and the 1930 Marion lynching; Anslinger and Holiday; payola; Motown; We Shall Overcome; 1985 lyrics hearing. 2 firsts cut, 3 searched-not-found. Dolly Parton block moved to era 10 for T-268d. TO PARK listed (burst).
NOTE (Jon asked for a burst of 6): only 3 safe tasks exist beside the running music agent (the last 3 seed chapters), so 4 run (DECISIONS #25 amended rule). Music messaged to switch to TO PARK.

### 2026-09-27 | [LOCAL] T-269a | storytelling-evolution: full research eras 1-5 [BURST] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-269-storytelling-evolution.md
VERIFY: python tools/project_state.py --check storytelling-evolution --stage research
RESULT: LANDED. FAIL  storytelling-evolution / research. measured: stage=PARTIAL eras=10/10 stories=23 (v7 c0 t16) verify_tags=46 bank=9528w outline=10388w manuscript=0w validator_errors=0
        381744 tokens, 197 tool uses, 22.6 min (opus). Eras 1-5 researched + bank check. 7 stories verified incl. Farfan's 1598 play (Manso people pressed into the cast), the Accomack Ye Bare and Ye Cubb court orders (court-watched claim dropped), Anthony Aston (new), Levingston and the indentured Staggs. Acoma range 300-1,500; kiva raids and mask burnings named to Posada, 1675 hangings to Trevino. 4 unsourced claims left out, 10 searched-not-found. Chapter FAIL until eras 6-10 (16 targets, 46 VERIFY). TO PARK 6. Agent briefly wrote to harness-issues.md outside its file list and repaired it.

### 2026-09-27 | [LOCAL] T-271a | sports-play: full research eras 1-5 [BURST] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-271-sports-play.md
VERIFY: python tools/project_state.py --check sports-play --stage research
RESULT: LANDED. FAIL  sports-play / research. measured: stage=PARTIAL eras=10/10 stories=15 (v2 c6 t7) verify_tags=60 bank=11030w outline=7167w manuscript=0w validator_errors=0
        450316 tokens, 246 tool uses, 28.6 min (opus). Eras 1-5 researched + bank check. Chunkey at Cahokia, stickball and lacrosse, dice games, clay toys; Timucua ball game, 1598 horseback games; game laws and fines, tobacco-stakes racing, Florida's 1676 ban on the Apalachee ball game; race meetings, cricket, cockfighting, gander pulling, 1744 Base-Ball rhyme; Fithian's journal, Valley Forge games, Pittsfield 1791. Stories: James Bullocke (1674), Austin Curtis (enslaved jockey, freed 1791). 3 unsupported claims removed, 9 searched-not-found. Chapter FAIL until eras 6-10 (60 VERIFY). TO PARK: music, crime-justice.

### 2026-09-27 | [LOCAL] T-272a | styles: full research eras 1-5 [BURST] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-272-styles.md
VERIFY: python tools/project_state.py --check styles --stage research
RESULT: LANDED. FAIL  styles / research. measured: stage=PARTIAL eras=10/10 stories=11 (v5 c2 t4) verify_tags=4 bank=8250w outline=5978w manuscript=0w validator_errors=0
        330357 tokens, 156 tool uses, 20.5 min (opus). Eras 1-5 researched + bank check. Stories: Hannah Lyman (fined 1676 for silk), Mary Ring's inventory, Jack (1745 runaway ad), Charity Clarke (1769), Washington's 1789 suit. Massachusetts clothing laws 1634-82, the 1740 Negro Act clothing clause verbatim, indigo and enslaved dye-makers, the 1786 tignon order, Cofitachequi pearls 1540, New Mexico blanket tribute, Plymouth and Northampton land. 8 searched-not-found. Chapter FAIL until eras 6-10. TO PARK 8.

### 2026-09-27 | [LOCAL] T-268d | music: full research era 10 incl. Dolly Parton, completes the chapter [BURST] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-268-music.md
VERIFY: python tools/project_state.py --check music --stage research
RESULT: DONE. PASS  music / research. measured: stage=RESEARCHED eras=10/10 stories=27 (v27 c0 t0) verify_tags=0 bank=37426w outline=22677w manuscript=0w validator_errors=0
        386872 tokens, 132 tool uses, 18.3 min (opus). Era 10, chapter COMPLETE. Dolly Parton's death confirmed beyond the Burchett statement (NPR, CNN, Spectrum, Wikipedia: cancer, Nashville, 25 Aug 2026, age 80; announced by nephew Bryan Seaver); story fully sourced (Here I Am, 2019); $1M COVID gift worded exactly. Taylor Swift, Kendrick Lamar, Zoe Keating. Napster to streaming (court-order claim corrected), per-stream pay, MMA 2018, AI suits to Sep 2026, Las Vegas and Astroworld, Kennedy Center closure. 2 searched-not-found. TO PARK for nine chapters.

### 2026-09-27 | [LOCAL] T-272b | styles: full research eras 6-8 [BURST] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-272-styles.md
VERIFY: python tools/project_state.py --check styles --stage research
RESULT: LANDED. FAIL  styles / research. measured: stage=PARTIAL eras=10/10 stories=13 (v11 c0 t2) verify_tags=0 bank=16654w outline=11994w manuscript=0w validator_errors=0
        319906 tokens, 152 tool uses, 21.9 min (opus). Eras 6-8 + bank check. Stories: Douglass (issued clothing, sailor disguise), Elizabeth Keckley, Levi Strauss and Jacob Davis (patent 139,121), Madam C. J. Walker, Wallace Carothers, Ann Lowe. Negro cloth and its mills, Northup on picking, Jacobs's dress, the Bloomer, Singer and Butterick, coal-tar dyes, SF queue ordinance, Carlisle clothes and hair, the 1902 hair order, Annie Malone, Bakelite, nylon, L-85, 1943 zoot suit attacks. 3 searched-not-found. Left for round 2: Native dress 1800-50, Art Deco, New Look. Chapter FAIL until eras 9-10. TO PARK 9.

### 2026-09-27 | [LOCAL] T-269b | storytelling-evolution: full research eras 6-7 [BURST] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-269-storytelling-evolution.md
VERIFY: python tools/project_state.py --check storytelling-evolution --stage research
RESULT: LANDED. FAIL  storytelling-evolution / research. measured: stage=PARTIAL eras=10/10 stories=24 (v14 c0 t10) verify_tags=31 bank=18352w outline=13012w manuscript=0w validator_errors=0
        382990 tokens, 118 tool uses, 16.4 min (opus). Eras 6-7 + bank check. Stories: William Alexander Brown and the African Theatre, Ira Aldridge, Edwin Forrest, William Henry Lane (new; Barnum billed him as John Diamond), Edwin Booth, Charlotte Cushman, Billy Kersands (own words via Tom Fletcher 1954). Astor Place (judge, sheriff, General Sandford; 18 to 31 dead), Wild West (Lakota wages, four named deaths, 1890 hiring ban, 23 Ghost Dance prisoners released to Cody), Tom shows in blackface, vaudeville, first films. 4 unsupported claims removed, 3 searched-not-found. Chapter FAIL until eras 8-10. TO PARK six chapters.

### 2026-09-27 | [LOCAL] T-271b | sports-play: full research eras 6-7 [BURST] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-271-sports-play.md
VERIFY: python tools/project_state.py --check sports-play --stage research
RESULT: LANDED. FAIL  sports-play / research. measured: stage=PARTIAL eras=10/10 stories=18 (v6 c6 t6) verify_tags=45 bank=19631w outline=10700w manuscript=0w validator_errors=0
        329262 tokens, 160 tool uses, 21.2 min (opus). Eras 6-7 + bank check. Stories: Tom Molineaux, Lucy Larcom, Moses Fleetwood Walker ('first' qualified by William Edward White 1879), Isaac Murphy (earnings; the house his widow lost). Knickerbocker rules 1845, who invented the Doubleday myth, the color line (1867, Anson, the 14 Jul 1887 vote 6-4), Cato 1839, McCoy killed 1842, Von Gammon 1897 and 8 football deaths, Boston sand gardens, child labor counts. 6 searched-not-found. Austin Curtis death date to AUDIT-QUEUE. Chapter FAIL until eras 8-10.

### 2026-09-27 | [LOCAL] T-269c | storytelling-evolution: full research eras 8-9 [BURST] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-269-storytelling-evolution.md
VERIFY: python tools/project_state.py --check storytelling-evolution --stage research
RESULT: LANDED. FAIL  storytelling-evolution / research. measured: stage=PARTIAL eras=10/10 stories=27 (v25 c0 t2) verify_tags=10 bank=30310w outline=16884w manuscript=0w validator_errors=0
        457309 tokens, 119 tool uses, 20.0 min (opus). Eras 8-9 + bank check. 11 verified: Chaplin, Micheaux, Anna May Wong, Hattie McDaniel, Bert Williams (new), Lilian St. Cyr/Red Wing (new), Lucille Ball, Lee Grant, Lorraine Hansberry, Sidney Poitier, Rita Moreno (new). 8 seed corrections (Great Train Robbery, Florence Lawrence, Production Code wording, Wilson quote disputed, Star Wars, VHS, three-camera, McDaniel's table in three accounts). 3 searched-not-found. Chapter FAIL until era 10. TO PARK for 8 chapters.

### 2026-09-27 | [LOCAL] T-272c | styles: full research eras 9-10, completes the chapter [BURST] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-272-styles.md
VERIFY: python tools/project_state.py --check styles --stage research
RESULT: DONE. PASS  styles / research. measured: stage=RESEARCHED eras=10/10 stories=16 (v16 c0 t0) verify_tags=0 bank=24824w outline=16797w manuscript=0w validator_errors=0
        357595 tokens, 141 tool uses, 18.4 min (opus). Eras 9-10, chapter COMPLETE. Stories: Charles and Ray Eames, Mary Beth Tinker, Rotchana Cheunchujit (El Monte, 1995), Francisco Tzul (LA garment worker, published interviews only), Andrew Johnson (2018; NJ CROWN Act). Jeans, Dacron 1951, Ann Lowe's 1953 gown, school hair cases, the Afro and the 1981 braids ruling, Air Jordans; Tazreen and Rana Plaza with US brands linked, LA piece pay and California's 2021 law, CROWN Act (~30 states, no federal law), textile waste, resale, end of de minimis. 4 searched-not-found. TO PARK listed.

### 2026-09-27 | [LOCAL] T-271c | sports-play: full research eras 8-9 [BURST] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-271-sports-play.md
VERIFY: python tools/project_state.py --check sports-play --stage research
RESULT: LANDED. FAIL  sports-play / research. measured: stage=PARTIAL eras=10/10 stories=19 (v17 c0 t2) verify_tags=17 bank=29337w outline=15756w manuscript=0w validator_errors=0
        400921 tokens, 172 tool uses, 25.4 min (opus). Eras 8-9 + bank check. Stories: Jack Johnson (new), Babe Ruth, Jackie Robinson, Jesse Owens, Babe Didrikson Zaharias, Josh Gibson, Carl Stotz and the first Little League boys, Ali (boxing side), Billie Jean King, Tubby Johnston, Chris Ernst; Thorpe as a span. 1905 football deaths named, 1910 riots (11-26 killed), who forced out Black jockeys (NBER), segregated pools, Title IX numbers, Pong to the 1994 ratings board. 8 searched-not-found. Chapter FAIL until era 10. TO PARK 6.

### 2026-09-27 | [LOCAL] T-269d | storytelling-evolution: full research era 10, completes the chapter [BURST] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-269-storytelling-evolution.md
VERIFY: python tools/project_state.py --check storytelling-evolution --stage research
RESULT: DONE. PASS  storytelling-evolution / research. measured: stage=RESEARCHED eras=10/10 stories=29 (v29 c0 t0) verify_tags=0 bank=37729w outline=20050w manuscript=0w validator_errors=0
        363056 tokens, 135 tool uses, 19.7 min (opus). Era 10, chapter COMPLETE (29 stories). Andy Serkis, Ashley Johnson, Alexandria Rubalcaba (background actor scanned on WandaVision), Ke Huy Quan. Streaming and theatres, Broadway's closure, #OscarsSoWhite and Academy counts, Weinstein (15 years, 23 Sep 2026), 2023 strikes and AI terms, 2024-25 games strike, AI performers, NO FAKES Act. Netflix first-series corrected. 3 searched-not-found. TO PARK 7 chapters.

### 2026-09-27 | [LOCAL] T-271d | sports-play: full research era 10, completes the chapter and step 1 [BURST] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-271-sports-play.md
VERIFY: python tools/project_state.py --check sports-play --stage research
RESULT: DONE. PASS  sports-play / research. measured: stage=RESEARCHED eras=10/10 stories=19 (v19 c0 t0) verify_tags=0 bank=37727w outline=18481w manuscript=0w validator_errors=0
        403768 tokens, 174 tool uses, 22.9 min (opus). Era 10, chapter COMPLETE. Stories: Kyle 'Bugha' Giersdorf, Rachael Denhollander. Screen time and ADHD only via named studies, phone bans by state, esports, concussions and the NFL settlement, Nassar (FBI agent W. Jay Abbott named from the DOJ IG report), NIL and the House settlement, transgender athlete laws, 2026 World Cup. Florida 'first' phone law removed. 3 searched-not-found. TO PARK 8 chapters.

### 2026-09-29 | [LOCAL] STEP 1 (RESEARCH) COMPLETE
T-269d storytelling-evolution and T-271d sports-play PASS. MEASURED: 37 chapters | RESEARCHED 30 | WRITTEN 7 |
stories 684, all verified, 0 candidate, 0 target | banks 1,033,830w. Every chapter passes --stage research.
All pending TO PARK sections filed (4 passes). MISTAKE FOUND AND FIXED: T-251..T-255's items had been filed on
2026-09-27 by the first script version, which did not mark sections FILED, so they were filed again; 26 exact
duplicate sections removed by script (dedupe_parks.py), verified, all outlines validate 0, the 7 written chapters
still PASS prose. One 'environment' item routed to land-environment by hand.
NEXT: STEP 2 (writing), per Jon: burst of 8.

### 2026-09-29 | [LOCAL] STEP 2 (WRITING) BEGINS: burst of 8 writer-A agents (Jon: 8-burst)

### 2026-09-27 | [LOCAL] T-301a | landmarks: writer A: eras 1-7 prose (part1 + part2) [BURST8] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-301-landmarks.md
VERIFY: python tools/project_state.py --check landmarks --stage prose
RESULT: LANDED. FAIL  landmarks / prose. measured: stage=WRITING ms_eras=7/10 written=7/10 ms_stories=9 (verified 9) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=7377w files=2 validator_errors=0
        263811 tokens, 74 tool uses, 12.5 min (opus). Writer A: part1 (eras 1-5) + part2 (eras 6-7), validator 0, punct 0/0. 9 stories. 7 gaps: 6 PATCHed, 1 not found. 20 outline claims left out, OPEN none. Fixed: unsupported San Miguel 'Tlaxcalan workers'/'burned' dropped, institution-as-actor lines, actors named (Gardiner 1831, Clark Mills, Daniel's troops 1702).

### 2026-09-27 | [LOCAL] T-302a | energy: writer A: eras 1-7 prose (part1 + part2) [BURST8] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-302-energy.md
VERIFY: python tools/project_state.py --check energy --stage prose
RESULT: LANDED. FAIL  energy / prose. measured: stage=WRITING ms_eras=7/10 written=7/10 ms_stories=7 (verified 7) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=6791w files=2 validator_errors=0
        309629 tokens, 117 tool uses, 18.8 min (opus). Writer A: part1 (3,768w) + part2 (3,620w), validator 0, punct 0/0, self-review run. 7 stories. 7 gaps PATCHed, 2 not found, 14 outline claims left out, OPEN none. Fixed: 'no draft animals' (dogs and the travois), NPS page names no nations, Schuyler engine source conflict (McCormick followed), who electrocuted the animals (Smithsonian followed), Kemmler's crime stated and 'gruesome' dropped, laws and taxes as actors replaced by people. Agent hit the heredoc bug again despite the brief line.

### 2026-09-27 | [LOCAL] T-303a | technology: writer A: eras 1-7 prose (part1 + part2) [BURST8] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-303-technology.md
VERIFY: python tools/project_state.py --check technology --stage prose
RESULT: LANDED. FAIL  technology / prose. measured: stage=WRITING ms_eras=7/10 written=7/10 ms_stories=13 (verified 13) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=8916w files=2 validator_errors=0
        346812 tokens, 167 tool uses, 21.1 min (opus). Writer A: part1 + part2 (~8,240w), validator 0, punct 0/0. 13 stories (Valliere, Jenks, Franklin, Whitney, Slater, Morse, McCormick/Deere with Jo Anderson, Bell, Nutt, Edison, Latimer, Woods, Tesla). 14 gaps PATCHed (3 partly confirmed and not written), 7 outline claim groups left out, OPEN none. Fixed: land named (Patapsco, Grand Detour, barbed wire), Jackson and Scott named for removal, museum 'violence' replaced by Northup's account, unsupported firsts removed, 4 quotes split at punctuation.

### 2026-09-27 | [LOCAL] T-304a | home-family: writer A: eras 1-7 prose (part1 + part2) [BURST8] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-304-home-family.md
VERIFY: python tools/project_state.py --check home-family --stage prose
RESULT: LANDED. FAIL  home-family / prose. measured: stage=WRITING ms_eras=7/10 written=7/10 ms_stories=9 (verified 9) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=6110w files=2 validator_errors=0
        274555 tokens, 92 tool uses, 13.5 min (opus). Writer A: part1 + part2 (eras 1-7), validator 0, punct 0/0, self-review run. 9 stories. 8 gaps PATCHed, 1 not found (Hallowell nation), 12 outline claims left out, OPEN none. Fixed: Menendez women 26 not 24, Tisquantum 'one of the last', Proverbs 13:24 quoted exactly, Knight 'alone' dropped, institution-as-actor lines.

### 2026-09-27 | [LOCAL] T-305a | transportation: writer A: eras 1-7 prose (part1 + part2) [BURST8] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-305-transportation.md
VERIFY: python tools/project_state.py --check transportation --stage prose
RESULT: LANDED. FAIL  transportation / prose. measured: stage=WRITING ms_eras=7/10 written=7/10 ms_stories=11 (verified 11) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=7616w files=2 validator_errors=0
        274200 tokens, 134 tool uses, 13.1 min (opus). Writer A: part1 (~2,800w, 3 stories) + part2 (~4,660w, 8 stories), validator 0, punct 0/0. 6 gaps PATCHed, 0 not found, 9 outline claims left out, OPEN none. Fixed: Grandy's ending, the Promontory rail crew (not Ten-Mile Day), Wells 'dragged', false 'first wheels', 1867 strike ending, institution-as-actor lines.

### 2026-09-27 | [LOCAL] T-306a | food-farming: writer A: eras 1-7 prose (part1 + part2) [BURST8] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-306-food-farming.md
VERIFY: python tools/project_state.py --check food-farming --stage prose
RESULT: LANDED. FAIL  food-farming / prose. measured: stage=WRITING ms_eras=7/10 written=7/10 ms_stories=7 (verified 7) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=6669w files=2 validator_errors=0
        254090 tokens, 90 tool uses, 11.1 min (opus). Writer A: part1 (4,680w, eras 1-5) + part2 (2,638w, eras 6-7), validator 0, punct 0/0, self-review run. 7 stories. 6 gaps PATCHed, 0 not found, 8 outline claims left out, OPEN none. Fixed: Oblinger quote was Uriah's, two indigo makers, personification. Prose FAIL expected until writer B.

### 2026-09-27 | [LOCAL] T-307a | migration: writer A: eras 1-7 prose (part1 + part2) [BURST8] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-307-migration.md
VERIFY: python tools/project_state.py --check migration --stage prose
RESULT: LANDED. FAIL  migration / prose. measured: stage=WRITING ms_eras=7/10 written=7/10 ms_stories=10 (verified 10) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=9162w files=2 validator_errors=0
        337738 tokens, 195 tool uses, 17.0 min (opus). Writer A: part1 + part2 (~8,900w), validator 0, punct 0/0. 10 stories (Onate with Acoma, Hooker, Broussard, Charles Ball, Rebecca Neugin, Brigham Young, Amelia Stewart Knight, Levi Savage, Laura Ingalls Wilder, Pap Singleton). 10 gaps PATCHed, 1 not found, 1 outline claim left out, 7 search-summary figures left unwritten, OPEN none. Fixed: Trail of Tears 'over 4,000' replaced by the sourced range, 'fleeing persecution' replaced by named attacks, 'empty ground'/'free for the taking' land erasure rewritten, Cahokia-London comparison and 'brutal' dropped. TO PARK listed.

### 2026-09-27 | [LOCAL] T-308a | money: writer A: eras 1-7 prose (part1 + part2) [BURST8] | model opus
STATUS: LANDED
CHECKPOINT: control/checkpoints/T-308-money.md
VERIFY: python tools/project_state.py --check money --stage prose
RESULT: LANDED. FAIL  money / prose. measured: stage=WRITING ms_eras=7/10 written=7/10 ms_stories=7 (verified 7) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=7359w files=2 validator_errors=0
        283086 tokens, 110 tool uses, 16.2 min (opus). Writer A: part1 (3,400w) + part2 (~4,000w), validator 0, punct 0/0, self-review run. 7 stories. 8 gaps PATCHed, 4 not found, 2 outline claims left out, OPEN none. Fixed: Potosi forced labor added where the outline said only 'Spain found silver', Bryan a former congressman in 1896, Bryan quote split at its semicolon, institution-as-actor lines.

### 2026-09-29 | [LOCAL] Writer burst of 8 done (writer A, eras 1-7) + TO PARK filed
All eight landed: landmarks, energy, technology, home-family, transportation, food-farming, migration, money.
Each: two part files, validator 0, punct 0/0, self-review run. Writer A cost 254k-347k tokens each (7-9k words).
Parked items filed into banks (all validate 0; written chapters still PASS prose); one bank-hygiene item to AUDIT-QUEUE.
Back to ONE AT A TIME: writer B (eras 8-10) for these eight chapters next, then writer A for the rest.

### 2026-09-27 | [LOCAL] T-301b | landmarks: writer B: eras 8-10 prose (part3), completes the chapter | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-301-landmarks.md
VERIFY: python tools/project_state.py --check landmarks --stage prose
RESULT: DONE. PASS  landmarks / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=17 (verified 17) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=12625w files=3 validator_errors=0
        277437 tokens, 117 tool uses, 15.6 min (opus). Writer B: part3 (5,287w), chapter PASSES prose. Eras 8-10: Lincoln Memorial (segregated crowd, Taft cut Moton's speech, Marian Anderson), Rushmore with the Black Hills takers named, Mohawk ironworkers, Golden Gate, Hoover Dam, Gateway Arch walkout and DOJ suit, WTC, Vietnam Veterans Memorial, 9/11 Memorial, Capitol marker, Montgomery memorials, Confederate monuments, 2026 President's House case, Sugarloaf Mound. 10 PATCH, 2 not found, 17 outline claims left out, OPEN none. Fixed: Moton speech 'vetted' (Taft ordered 500 words cut), Hoover CO deaths alleged by workers, Borglum 1923 not 1915.
NOTE (Jon): PAUSE after T-301b finishes. No new dispatches until Jon says.

### 2026-09-29 | [LOCAL] PAUSED (Jon) after T-301b. landmarks PASSES prose. Nothing in flight.
NOTE (Jon, 78%): run ONE agent (T-302b), then PAUSE.

### 2026-09-27 | [LOCAL] T-302b | energy: writer B: eras 8-10 prose (part3), completes the chapter | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-302-energy.md
VERIFY: python tools/project_state.py --check energy --stage prose
RESULT: DONE. PASS  energy / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=11 (verified 11) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=13122w files=3 validator_errors=0
        262255 tokens, 80 tool uses, 12.6 min (opus). Writer B: part3 (6,724w), chapter PASSES prose. Spindletop, Monongah and Ludlow, TVA/Hoover/Grand Coulee and the people moved, Osage murders (three counts), REA; Shippingport, Garrison Dam, 1969 mine law and black lung, 1973 embargo, TMI, Navajo uranium and Church Rock; fracking, Upper Big Branch, Dakota Access, 2025 mix, Texas 2021, Vogtle and restarts. 11 gaps PATCHed, 0 not found, 10 outline claims left out. Fixed: 'no new reactor for four decades' false (Watts Bar 2, 2016), Russia not Saudi Arabia, TVA and a law as actors, Garrison numbers, Monongah share.

### 2026-09-29 | [LOCAL] PAUSED (Jon) after T-302b. energy PASSES prose. Nothing in flight.
NOTE (Jon): T-302b used 78% -> 81% (3%, 262k tokens, 12.6 min): about half the cost per agent seen earlier in the week. Run ONE agent (T-303b), then PAUSE.

### 2026-09-27 | [LOCAL] T-303b | technology: writer B: eras 8-10 prose (part3), completes the chapter | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-303-technology.md
VERIFY: python tools/project_state.py --check technology --stage prose
RESULT: DONE. PASS  technology / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=23 (verified 23) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=14616w files=3 validator_errors=0
        261673 tokens, 81 tool uses, 13.7 min (opus). Writer B: part3 (~5,100w), chapter PASSES prose. Assembly line and 1913 deaths, radio/TV/plastics/tractors, ENIAC and the six programmers, transistor; the chip, PCs, ARPANET/web/GPS; smartphones, batteries, AI and its errors (NIST 2024, the 2023 ChatGPT invented-cases court case), Robert Williams. 4 gaps PATCHed, 0 not found, 7 outline claims left out. Fixed: police named in the Williams arrest, personification, the web's origin stated plainly.

### 2026-09-29 | [LOCAL] PAUSED (Jon) after T-303b. technology PASSES prose. Nothing in flight.
NOTE (Jon): T-303b used 81% -> 85% (4%). Burst of 3 finishers (4 fits but risky at 85%).

### 2026-09-27 | [LOCAL] T-304b | home-family: writer B: eras 8-10 prose (part3), completes the chapter [BURST3] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-304-home-family.md
VERIFY: python tools/project_state.py --check home-family --stage prose
RESULT: DONE. PASS  home-family / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=16 (verified 16) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=11162w files=3 validator_errors=0
        228235 tokens, 79 tool uses, 9.9 min (opus). Writer B: part3 (5,106w), chapter PASSES prose. Washday, water and power, refrigerators, Sears kits, the Rogarshevskys and TB (defined), redlining, kitchenettes, spanking advice, war-work moves; suburbs and whites-only sales, TV, divorce, working mothers, latchkey counts, homeschooling; bigger houses, 2008 (Countrywide, Mozilo), homelessness, 2020 at home. 2 PATCH, 0 not found, 7 outline claims left out. Fixed: unsupported outline words cut, Munoz misquote replaced, Myers figures, guessed author first names removed from its own PATCH.

### 2026-09-27 | [LOCAL] T-305b | transportation: writer B: eras 8-10 prose (part3), completes the chapter [BURST3] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-305-transportation.md
VERIFY: python tools/project_state.py --check transportation --stage prose
RESULT: DONE. PASS  transportation / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=19 (verified 19) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=13124w files=3 validator_errors=0
        242330 tokens, 74 tool uses, 12.3 min (opus). Writer B: part3, chapter PASSES prose. Model T, Lincoln Highway, Route 66, crash deaths, airmail and the Kelly Act, DC-3, Pullman porters, WWII, Irene Morgan; Interstates and the homes they took (I-85 Montgomery), Grand Canyon crash, 707, deregulation, Freedom Rides, Amtrak, containers; GPS, ride-hail and Prop 22, EVs, CAHSR, bridges, road deaths, Key Bridge, Potomac. 5 PATCH, 0 not found, 10 outline claims left out. Fixed: false firsts (Ideal X, McLean 'invented'), abstractions as actors.

### 2026-09-27 | [LOCAL] T-306b | food-farming: writer B: eras 8-10 prose (part3), completes the chapter [BURST3] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-306-food-farming.md
VERIFY: python tools/project_state.py --check food-farming --stage prose
RESULT: DONE. PASS  food-farming / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=17 (verified 17) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=12939w files=3 validator_errors=0
        241891 tokens, 68 tool uses, 10.8 min (opus). Writer B: part3 (~6,300w), chapter PASSES prose. 1906 food laws, pellagra, Hawaii plantations and the 1893 overthrow, tractors and hybrid corn, 1930s programs, attacks on the STFU, rationing, 1942 farm seizures, braceros, school lunch; consolidation, fast food, pesticides, Pigford, organic, 1980s crisis; obesity, food deserts, hunger and the SNAP cut, COVID in meat plants, H-2A and heat deaths, food sovereignty. 9 PATCH, 0 not found, ~20 outline claims left out. Fixed: bracero pay taken by US employers (not 'the government'), Jordan farm facts vs PBS, STFU attacks stated specifically.

### 2026-09-29 | [LOCAL] Burst of 3 done: home-family, transportation, food-farming PASS prose. 13 written. PAUSED; nothing in flight.
NOTE (Jon): burst of 3 used 85% -> 93% (~2.7% each). One agent (T-307b), then PAUSE.

### 2026-09-27 | [LOCAL] T-307b | migration: writer B: eras 8-10 prose (part3), completes the chapter | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-307-migration.md
VERIFY: python tools/project_state.py --check migration --stage prose
RESULT: DONE. PASS  migration / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=15 (verified 15) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=13392w files=3 validator_errors=0
        254687 tokens, 83 tool uses, 13.2 min (opus). Writer B: part3 (~4,290w), chapter PASSES prose (13,392w). Great Migration first wave (Georgia, Macon fee, Chicago 1919), Dust Bowl and the bum blockade, 1942 removal with DeWitt, Bendetsen and the Army named; second wave, Sun Belt, Relocation, return South; state moves dated, Katrina (Gretna, Houston), Maria. 9 PATCH, 1 not found, 2 outline claims left out. Fixed: Thompson was not a Dust Bowl migrant (moved 1920s); flagged and unconfirmed figures not written.

### 2026-09-29 | [LOCAL] PAUSED (Jon) after T-307b. migration PASSES prose. 14 written. Nothing in flight.
NOTE (Jon): one agent (T-308b), then STOP and explain the next phase.

### 2026-09-27 | [LOCAL] T-308b | money: writer B: eras 8-10 prose (part3), completes the chapter | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-308-money.md
VERIFY: python tools/project_state.py --check money --stage prose
RESULT: DONE. PASS  money / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=12 (verified 12) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=13170w files=3 validator_errors=0
        244995 tokens, 76 tool uses, 12.3 min (opus). Writer B: part3 (~6,200w), chapter PASSES prose (13,170w). Gold Standard Act 1900, Panic of 1907, Jekyll Island and the Fed, Black banks and Greenwood, 1930-33 runs, gold turn-in, deposit insurance, war bonds; Diners Club, ECOA 1974, ATM, 1971, Great Inflation, S&L; 2008, bitcoin, payday loans, 2021-26 inflation, FTX, 2023 runs, end of the penny. 5 PATCH, 0 not found, 4 outline claims left out. Fixed: savings lost two-thirds not a third, penny's end and 2008 guarantee given actors, personification, a fourth-wall line.

### 2026-09-29 | [LOCAL] STOPPED (Jon) after T-308b. money PASSES prose. 15 written. Nothing in flight.

### 2026-09-29 | [LOCAL] SINGLE-WRITER TRIAL (Jon): one writer per chapter for all ten eras, where the chapter fits.
Reason: one voice, no second read of the style guides. WRITER.md gained a "Single-writer mode" paragraph.
Trial: T-309 work-workers. USAGE AT START: 7% (Jon). Stop after it for Jon to measure.

### 2026-09-27 | [LOCAL] T-309 | work-workers: ONE writer, all 10 eras (single-writer trial) | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-309-work-workers.md
VERIFY: python tools/project_state.py --check work-workers --stage prose
RESULT: DONE. PASS  work-workers / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=17 (verified 17) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=14452w files=3 validator_errors=0
        362602 tokens, 149 tool uses, 20.3 min (opus). SINGLE-WRITER TRIAL: all 10 eras, 3 files, chapter PASSES prose (14,452w, 17 stories verified). 13 PATCH, 1 not found, 20 outline claims left out, OPEN none. Fixed: Martin's Hundred 73 (search-summary only) -> 'at least 58', branding defined with method, actors named (Philadelphia militia, Larry Payne's killing, James Earl Ray, employers who took the braceros' 10%), institutions as actors rewritten. Compare: two-writer chapters cost ~500-590k tokens; this cost 363k.

### 2026-09-29 | [LOCAL] Single-writer trial DONE. work-workers PASSES prose. 363k tokens vs ~500-590k for two writers. STOPPED for Jon.
NOTE (Jon): usage not measurable this window (other work). Burst of 3 single writers: T-310, T-311, T-312. The rest of the small group next window.

### 2026-09-27 | [LOCAL] T-310 | marketplace: ONE writer, all 10 eras [BURST3] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-310-marketplace.md
VERIFY: python tools/project_state.py --check marketplace --stage prose
RESULT: DONE. PASS  marketplace / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=17 (verified 17) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=13548w files=3 validator_errors=0
        358848 tokens, 123 tool uses, 18.6 min (opus). SINGLE WRITER: all 10 eras, chapter PASSES prose (13,548w, 17 stories). The Dalles, copper kettles, market days, Wall Street slave market, boycotts, Seider, Barnum and Joice Heth, Singer, department stores, Weeping Time, Winslow's syrup, mail order, Woolworth, company stores, rationing, malls, Walton, Bezos, Renica Turner. 9 PATCH, 0 not found, 20 outline claims left out. Fixed: captives traded at The Dalles, 'nothing carried a price' dropped, Heth's autopsy actors named (Barnum, Dr. David L. Rogers, 1,500 spectators), installment 'first' narrowed, company-store debt attributed.

### 2026-09-27 | [LOCAL] T-311 | big-business: ONE writer, all 10 eras [BURST3] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-311-big-business.md
VERIFY: python tools/project_state.py --check big-business --stage prose
RESULT: DONE. PASS  big-business / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=14 (verified 14) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=15949w files=3 validator_errors=0
        423896 tokens, 141 tool uses, 22.7 min (opus). SINGLE WRITER: all 10 eras, chapter PASSES prose (15,949w, 14 stories). Chartered companies incl. the Royal African Company (branding defined), Apthorp's slave trade, Tea Act, Bank of North America; incorporation laws, Dartmouth, Lowell, Bank War, railroads and land grants, trusts, Homestead, Sherman Act; mergers, 1911 breakups, Ludlow, leaded gasoline, SEC; GM, ITT, lobbying, tobacco, asbestos, Bhopal, Bell breakup; 2000-today dated. 11 PATCH, ~40 outline claims left out. Fixed: every bank CORRECTION followed, 'companies sent troops' given named actors, railroads-vs-governments narrowed, 'invented the trust' corrected, land added (Massachusett, Ojibwe at Mesabi, Pennacook).

### 2026-09-27 | [LOCAL] T-312 | america-world: ONE writer, all 10 eras [BURST3] | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-312-america-world.md
VERIFY: python tools/project_state.py --check america-world --stage prose
RESULT: DONE. PASS  america-world / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=13 (verified 13) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=15577w files=3 validator_errors=0
        437871 tokens, 179 tool uses, 23.1 min (opus). SINGLE WRITER: all 10 eras, chapter PASSES prose (~15,600w, 13 stories). Tordesillas, Matanzas, Breda, 1701 treaties, asiento, Louisbourg; Revolution diplomacy, 1783 and Six Nations land, Algiers; Louisiana, Guadalupe Hidalgo, guano islands, Alaska and Kake, Hawaii's overthrow and the 1897 petition, 1898, the Philippine war, Samoa; Insular Cases, torture in the Philippines, canal, occupations, Law 116 and Ponce, Cold War coups, statehood, nuclear tests, 9/11 to 2026. 7 PATCH, 2 not found, 23 outline claims left out. Fixed: institutions as actors, triad, land erasure eras 6-7, search-summary-only figures (Haiti 3,250; DR occupation) not stated as fact, 2025-26 added.

### 2026-09-29 | [LOCAL] Burst of 3 single writers done: marketplace, big-business, america-world PASS prose (359k, 424k, 438k tokens). Parked items filed into 7 banks (all validate 0; every written chapter still PASSES prose). 19 written. STOPPED.
NOTE (Jon): one writer. T-313 slavery-freedom, single-writer mode.

### 2026-09-27 | [LOCAL] T-313 | slavery-freedom: ONE writer, all 10 eras | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-313-slavery-freedom.md
VERIFY: python tools/project_state.py --check slavery-freedom --stage prose
RESULT: DONE. PASS  slavery-freedom / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=24 (verified 24) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=18673w files=3 validator_errors=0
        414225 tokens, 155 tool uses, 24.3 min (opus). SINGLE WRITER: all 10 eras, chapter PASSES prose (18,673w, 24 stories). Captivity vs slavery for life, Gualdape 1526, 1619 on Kecoughtan land, the Middle Passage, slave codes, flogging/branding/castration defined; NY 1712 and 1741, Stono, the Revolution, gradual abolition, Hemings; the domestic trade, revolts, the war, freedom, schools, Memphis/New Orleans/Colfax, convict leasing; Jim Crow and forced labor, the recorded voices, Roots, reparations, 2025-26 park cases. 26 PATCH (16 new, 10 parked), 1 not found, 7 outline claims left out. Fixed: institutions as actors ('the 13th Amendment ended slavery', 'Colfax killed'), source conflicts stated, 1790 census figure reconciled.
USAGE AT START (T-313): 70% (Jon). A clean single-writer reading: nothing else running.
USAGE (T-313, clean single writer): 72% -> 80% = 8% for a whole chapter (Jon corrected the start from 70 to 72). Similar to two writers per chapter (6-8%): single writers save tokens (~30%) but not much window percentage. Jon: one at a time for now. T-314 styles next.

### 2026-09-27 | [LOCAL] T-314 | styles: ONE writer, all 10 eras | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-314-styles.md
VERIFY: python tools/project_state.py --check styles --stage prose
RESULT: DONE. PASS  styles / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=16 (verified 16) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=16665w files=3 validator_errors=0
        369964 tokens, 137 tool uses, 18.0 min (opus). SINGLE WRITER: all 10 eras, chapter PASSES prose (16,665w, 16 stories). Native dress materials, Cofitachequi pearls, cochineal, dress laws, Mary Ring, Hannah Lyman, Pueblo blanket tribute, 1740 clothing law, indigo, homespun, tignon order; negro cloth, Northup, Douglass, Bloomer, Keckley, coal-tar dyes, Strauss and Davis, queue cutting, Carlisle; 1902 hair order, Walker, Carothers, Ann Lowe, L-85, zoot suit attacks, polyester, Eames, Tinker, hair cases, Air Jordans, El Monte, Rana Plaza, CROWN Act. 5 PATCH, 15 outline claims left out. Fixed: chapter number 35 not 33, institutions as actors, Pawnee move per Parks. Flag: Michael Eugene Thomas assault detail left out (AUDIT-QUEUE).

### 2026-09-29 | [LOCAL] Documentation sync (Jon: context at 88%, make sure everything is current)
TODO rewritten to the measured state (20 written, styles in progress, 16 to go, queue table, open Wiley question,
how writing runs now, after-step-2 plan, director tools). ROADMAP: step 1 marked complete; step 2 describes
single-writer mode and the per-chapter ordering rule. DECISIONS #26 (single-writer mode) and #27 (Jon sets the
agent count). briefs/README and RESUME updated. The director's helper scripts, previously only in a temporary
scratchpad, are now permanent in tools/ (director_task.py, file_parks.py, mk_writer_checkpoint.py,
mk_research_checkpoint.py, dedupe_parks.py). Memory: burst-mode and status-table notes updated.

### 2026-09-29 | [LOCAL] T-314 styles closed (PASS prose). 21 of 37 written. Nothing in flight.
Docs synced: TODO (21 written, queue), ROADMAP status line, AUDIT-QUEUE (Michael Eugene Thomas detail).
Jon is backing up the transcript folder before a pruning experiment (see the plan in conversation: prune a COPY with a
JSON-aware script, Sonnet reads a 300-character index, resume the copy with --fork-session; never touch the live file).

### 2026-09-29 | [LOCAL] T-315 | government-politics: ONE writer, all 10 eras | model opus
STATUS: DONE
CHECKPOINT: control/checkpoints/T-315-government-politics.md
VERIFY: python tools/project_state.py --check government-politics --stage prose
RESULT: DONE. PASS  government-politics / prose. measured: stage=WRITTEN ms_eras=10/10 written=10/10 ms_stories=14 (verified 14) ms_verify_tags=0 emdash=0 semicolon=0 manuscript=21902w files=3 validator_errors=0
        493106 tokens, 174 tool uses, 27.5 min (opus). SINGLE WRITER: all 10 eras, PASS prose (21,902w, 14 stories). 17 PATCH, 1 not found, 30 outline claims left out. Fixed: Mayflower location, fourth-wall lines dropped, actors named for removal and EO 9066.
AGENT: a07864183d94f58ed (salvage: python tools/salvage_agent.py a07864183d94f58ed --tail)
