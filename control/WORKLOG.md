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
RESULT:
