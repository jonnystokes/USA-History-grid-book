# AUDIT QUEUE — defects parked for Phase 3

> **2026-09-26:** the plan is now eight steps (`control/ROADMAP.md`). "Phase 3" below means
> **step 3, the audit**. This file's items join the sonnet checkers' findings, and the opus
> fixer applies them in step 5. Gaps that need new research go to step 4
> (`control/briefs/GAPS.md`). Writers' own gap research is recorded in the banks as PATCH and
> `SEARCHED, NOT FOUND` entries, not here.

**Created 2026-09-07** when the project moved to three phases (research → write → audit).
Auditing no longer happens between chapters. This file is where a known defect waits so that
Phase 3 finds it instead of losing it.

## How to use this file

**Writers:** if you hit a defect in your own outline or research bank — softening, a false
comparison, a manufactured dispute, personification, a fact that contradicts itself — you
**fix it in your prose**, you **name it in your report**, and the director appends it here.
Do not stop to repair the source. That is Phase 3 work and it is not yours.

**The director:** append every such item, with enough detail that an auditor can act on it
without re-reading the conversation. File, line, the exact wrong text, what is wrong with it.

**Phase 3:** these are **legacy items**. They predate the 2026-09-07 restructure and would need
doing however well Phase 2 goes, so they are the one part of Phase 3 that is real work rather
than confirmation. Do them, then read the book.

**Anything you find beyond this file is new information about a failure in Phase 2** — the
guide or the brief did not do its job. Fix the sentence, and fix the instruction that let it
through, because a defect that appeared once will have appeared in other chapters written under
the same instructions.

**Read for these. Do not grep for them.** Every defect this project has caught was caught by an
AI reading a sentence and understanding what it was doing. A search finds "empty prairie" and
walks past "the land was open for the taking".

Sections match the ROADMAP's three audits: **3a structural**, **3b language**, **3c fact and
source**.

---

## 3a — Structural / parsing

- ~~`outlines/BOOK-OUTLINE.md` is a stale compiled artifact.~~ **Rebuilt 2026-09-07** —
  37 chapters, 603 stories, 171,907 words, validator 0 errors. The four remaining hits for
  "empty riverbank / empty prairie / empty ridgeland" are the correction annotations
  quoting the old wording, not live text. **Rebuild it again at audit time** with
  `python tools/build_book_outline.py`; never hand-edit it.
- **`tools/validate_grid.js` is a copy-paste duplicate of the viewer's `parseGrid`.** Re-diff
  the two during the audit. They can drift silently and nothing would report it.
- **The validator never runs the renderer.** `VIEWER-CONTRACT.md` §3 lists 25 failures it
  cannot see. A clean run is necessary, not sufficient — the audit has to open the book.

## 3b — Language

- **Style-guide violations in the 16 outlines researched before 2026-08-08.** Teaser openings
  that withhold facts, em-dash pivots. Writers are instructed to fix these in the prose as
  they go, so by Phase 3 the *prose* should be clean and the *outlines* will not be. Decide
  then whether outlines matter enough to repair.
- **Voice consistency across 37 chapters written by dozens of agents** has never been checked,
  because until now only two chapters existed.
- **`writing-style-guide.md` §1.11–1.14 and §2.6 postdate the two finished chapters.**
  `native-nations` and `city-building` were written against the older, weaker guide. They pass
  every check we have, but they were never examined for the AI cadence, sound patterning,
  register mixing, or the teaching-point test. **Audit them against the new sections.**

## 3c — Fact and source

### Known erasures, unfixed

- **`manuscript/city-building/part3-1900s-and-today.md`** — the Oak Ridge erasure, in three
  places, in prose that **already passed adversarial verification** (T-206):
  - line 23: "put up whole cities on empty ground and kept them off the maps"
  - line 97: the span label `Secret cities from nothing`
  - line 98: "began building a city for the Army on empty ridgeland in eastern Tennessee"

  The ridgeland was not empty. About 1,000 families were removed from Wheat, Elza, Scarboro
  and Robertsville; the Army Corps filed a declaration of taking in October 1942 for about
  59,000 acres at an average $46.86 an acre; some families were told by notices nailed to
  their fence posts. Accounts of the number of people differ — Tennessee Encyclopedia says
  roughly 4,000, others more than 3,000; state the range. **The facts are already sourced** in
  `research/research-city-building.md` era 08 and `outlines/city-building.md:190`, so this
  needs no research, only the edit.

- **`research/research-migration.md:121`** — "**Guthrie** and **Oklahoma City** went from
  **empty ground** to towns of about 10,000–15,000 people that same day." Same erasure, in the
  chapter that *leads* the 1889 land run. The line does add "The land had been taken from
  Native nations" and then defers the injustice to Ch17, which is the deferral pattern the
  policy also forbids. `city-building`'s version was corrected on 2026-09-07; this one was not,
  and `migration` has not been written yet, so it will propagate unless a writer catches it.

**The standing rule this produced:** `city-building` generated this same move three times —
the 1889 land run, the federal district, Oak Ridge. When a chapter produces it once, check
every founding sentence in that chapter for who was already on the ground.

### Reported-but-not-fixed, from the chapter 06 verification passes

- Four Olmsted claims that are in `outlines/city-building.md` but **not** in the bank:
  Prospect Park, the Emerald Necklace, "dozens of places", and his having been a farmer and a
  journalist.
- "first large electric street railway anywhere" in the outline, where the bank says "first
  successful large-scale".
- A Riis-versus-Old-Law contradiction over which was the "first" tenement law.
- A name collision between the reform mayor Strong and the diarist Strong.
- The bank dates an 1886 Mohawk ironworker job to the Victoria Bridge, completed 1859 —
  flagged `[VERIFY the bridge]`. The writer sidestepped it by writing only "a bridge job".

### Content decisions still owed

- **The 1970s Indian Health Service sterilizations are absent from the `native-nations` bank.**
  Jon ruled they go in, under the clinical-word rule in `hard-subjects-policy.md` §3b — say
  what the operation was, what it did to the person, and by what method, and say so if the
  record does not give the method. Research is queued in `workspace/native-nations.md`.
  `native-nations` prose is already written, so this is an insertion into a finished chapter.
- **Oñate / Acoma death toll and sentences: RESOLVED.** The native-nations bank verified the
  Acoma section on 2026-09-07, with the death-toll spread and the sentences attributed to named
  sources. This entry was stale until 2026-09-26. T-233a wrote from that verified section.
- **~140 per-chapter open questions** in the `workspace/<slug>.md` files under "Open questions
  for the director". These were always meant to be answered in each chapter's turn.

### Seven kinds of defect, all found in one chapter

Every one of these came out of `city-building`, which was one of the three chapters we
considered complete and prose-ready. They are here as **things to recognise while reading**,
not as search terms. The example phrasing is how it happened to appear once; the next instance
will be worded differently, which is exactly why a search will not find it.

1. **Land erasure.** The ground described as empty, unsettled, unclaimed, opened, or available
   when people were on it and it was taken. Ask of every founding sentence: **who was already
   there?** The three instances in this chapter read "empty prairie", "empty riverbank" and
   "empty ridgeland", but the move survives any wording — "open for the taking", "nothing but
   grass", "the first people to build there".
2. **False comparison or superlative.** "More than doubled", "first", "largest", "only",
   "never before". **Recompute every one.** The Burj Khalifa claim ("more than doubled anything
   in the U.S.") was false at 1.53x and contradicted a number three paragraphs later in its own
   file.
3. **Manufactured dispute.** Two dated points on a rising curve presented as a disagreement.
   Rochester's 9,269 (1830 census) and ~12,630 (1834) became "somewhere between about 9,000 and
   about 12,600" in finished prose — false, and produced by following the bank correctly. Ask
   whether the two figures actually conflict or just have different dates.
4. **Self-contradiction across a few paragraphs.** Chaco appeared as "about 900 to about 1180"
   and "people left in the 1140s" four paragraphs apart, because the bank carried both. Only a
   read catches this; each sentence is fine alone.
5. **Dropped qualifier.** The bank said "largest **prehistoric** earthen structure"; the outline
   dropped the word and the prose sharpened it to "ever built", which is false. Check a
   superlative against what the source actually claimed.
6. **Unsourced specific.** "For the next 250 years", "a printed rulebook" — stated in the
   outline with nothing behind them in the bank. A confident detail is not a sourced one.
7. **Inverted agency.** An institution named as the actor, the people who did the work arriving
   as a subordinate clause, and nobody named as having compelled them. Ask: **who actually did
   this, and who made them?**

---

## Added 2026-09-26: Writing Style Guide Version 2

- **The two finished chapters were written under v1 and fail v2.** The prose gate now counts
  em dashes and semicolons. `native-nations` has 74 em dashes and 40 semicolons. `city-building`
  has 83 em dashes and 23 semicolons. Punctuation is only the part a machine can count. A
  full v2 read (root metaphors, reification, patient-verb agreement, modal ambiguity, repeated
  units, the dry side) has not been done. The TODO proposes doing it now as Phase 2 work,
  because the gate fails without it.
- **The outlines contain about 2,872 em dashes.** Writers must not copy the punctuation. No
  outline is being repunctuated, because outlines are working files and the prose gate
  guards the book.
- **The "after" examples in `hard-subjects-policy.md` §2 are v1-era text.** They include em
  dashes, semicolons, "the Colfax Massacre ... killed" and "an 1891 law let the government".
  A note now tells writers to copy their completeness and not their construction. Rewriting
  them needs the sources, so it waits for the audit.
- **Control documents still contain em dashes and semicolons.** CLAUDE.md, the amendment and
  the new cloud files are clean. RESUME.md, AGENT-BRIEF.md, ROADMAP.md and the policy's
  remaining semicolons are not. Writers read them, so a cleanup pass is cheap and useful.
- **RULED: IT GOES IN (Jon, 2026-09-26, DECISIONS #14). Queued as task T-236.** Acoma, 1598 (from T-233a, 2026-09-26). The All Pueblo Council of Governors' account says
  Zaldívar's soldiers "assaulted an Acoma woman" (bank, Acoma section). The bank leaves whether
  and how the book states this to the director. The revised part 1 does not include it. Jon to
  rule under `hard-subjects-policy.md`. The Pueblos' own statement is a named source.
- **Worcester v. Georgia (from T-233b, 2026-09-26).** The native-nations bank does not name the
  parties (Samuel Worcester and the State of Georgia) or who acted in the case. Part 2 was
  written without them. Research item: add a sourced line to the bank, then the prose can
  name them.
- **Wounded Knee 1973 deaths (from T-233c, 2026-09-26).** The native-nations bank (line ~232)
  says two occupiers "died". The prose says they were "killed", and that the sources do not
  identify who killed them. "Died" would soften it. "Killed" goes beyond the bank's wording.
  Research item: source who the two men were and how they died, then make the bank and the
  prose agree.
- **city-building part 1 (from T-234a, 2026-09-26).**
  - Three claims in the prose are not in the bank: "copied for two hundred years", "London,
    hundreds of thousands" and "fire companies for a hundred years". Source them or cut them.
  - The bank does not name the Native nations on the sites of the 1600s towns. Research item.
  - The span label "Fire, the city killer" personifies fire. The agent could not edit marker
    lines. The revision brief now allows `label=` edits. This label is a one-line fix.
- **city-building: the bank is thinner than the prose (from T-234b, 2026-09-26).** About 23
  claims in parts 1 and 2 are not in `research/research-city-building.md`, including most of
  the Olmsted story (an `hb-story` marked verified). Each one is listed in the "Decisions and
  known gaps" section of `control/checkpoints/T-234-city-building.md`. The earlier writer
  took them from the outline's inline notes. This needs a research patch: source each claim
  into the bank, or cut it from the prose. It also argues for checking whether other
  chapters' outlines carry claims their banks lack before those chapters are written.
  Other items from part 2: the bank names no Native nation at Rochester, Chicago, San Francisco
  or the land-run lands, and no one who took them. The bank calls marasmus "severe
  malnutrition" and the prose says "starvation" (both kept).
- **city-building part 3 (from T-234c, 2026-09-26).** About 55 more claims are not in the bank,
  about 78 across the chapter. See the city-building bank-gap item above. Also, Anderson's age:
  "eight in 1958" and "approaching 83 in 2022" cannot both be true. The bank says they agree.
  The prose states both, attributed to Sahan Journal. Resolve it from the source.
- **RULED YES by Jon, 2026-09-26 (DECISIONS #13). Now in the writing brief and CLAUDE.md.** Writers take facts from the bank, not the outline. The
  city-building gap came from prose written off the outline's inline notes. A number probe
  (`tools/bank_coverage.py`) cannot detect it, because the missing claims are qualitative. The
  prevention is one brief line: "Every fact in your prose must be in the research bank. When
  the outline states something the bank does not, do not write it. List it in your report."
  That may make some chapters thinner. It also makes every sentence traceable. Awaiting
  Jon's ruling before the Phase 2 writing agents start.
- **war (from T-235b, 2026-09-26).** Topics left out rather than hedged: rape at My Lai, Agent
  Orange, drones, and ordinary WWII and post-9/11 veterans (see `workspace/war.md`).
  PERISHABLE: the 2026 Venezuela operation and Iran war figures. One of them came from a search
  summary (the Washington Post page returned 403). Re-verify before prose.
- **immigration part 1 (from T-237a, 2026-09-26).** The bank names no Native nation for the land
  under St. Augustine, Plymouth or New Amsterdam, and does not say who fought the Haitian
  Revolution. A few word definitions ("loblollie", "Venerable") are not in the bank. Ten outline
  claims were left out under DECISIONS #13 (listed in `control/checkpoints/T-237-immigration.md`).
  **Question for Jon:** `jewish-refugees-1654` is an hb-story about a group, with only Jacob
  Barsimson named. Does it stand, or should it become hb-zoom prose?
- **science (from T-240b-e, 2026-09-26).** The APS's first Transactions: APS says 1771, the bank
  says 1773, and the prose was left as it was. Part 1 carries a few identity glosses from general
  knowledge, not the bank (Newton's first name, "Swedish botanist" and similar), which are small
  breaches of DECISIONS #13. About 59 outline claims were left out across the three parts
  (listed in the checkpoint).
- **Rulings 15 and 16 applied (2026-09-26).** Two source files are now out of date and should be
  corrected in the audit phase. `outlines/immigration.md` still says the Tung Trinh cannibalism
  is "kept out of the prose", and `research/research-immigration.md` (about line 484) says
  "deliberately omitted". Both are overruled by DECISIONS #15. The outline still lists
  `jewish-refugees-1654` as an hb-story, but the prose now tells it as a span (DECISIONS #16).


---

## Notes added during step 1 (2026-09-27)

- **Radium Girls audit item** (parked in `research/research-elements.md` as "AUDIT ITEM parked from
  `rights-movements` era 8"): T-250 resolved it in `research/research-work-workers.md` era 08
  PATCH from the National Archives (1928 settlement: $10,000, some sources $15,000; $600 annuity;
  medical costs; June 8, 1928. Donohue dates corrected). The audit should carry the corrected
  facts into `elements` and `rights-movements` wherever they differ.
