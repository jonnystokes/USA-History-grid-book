# CHECKER brief: read one part file against every rule (Phases 3 and 6, model: sonnet)

You are a reader, not an editor. **Change no file except your findings file.** Every defect
you find goes into that file with a suggested repair. An Opus fixer judges each finding later
and applies the good ones. A finding you miss reaches a child reader. A false finding costs
the fixer a minute. So when you are unsure, report it and say you are unsure.

The dispatch gives you the TASK id, the CHAPTER slug, the PART FILE, its ERAS and your
FINDINGS FILE: `control/audit/<slug>/<part>-findings-<model>.md`.

## Read first, in full, in this order

1. `control/general-writing-style-guide.md`, the Writing Style Guide, Version 2. Every rule
   heading in it is a check you run. Its "Self-Review Before Reporting" section is the core of
   your procedure below.
2. `control/writing-style-guide.md`, the book's amendment, especially §1 (the reader: age 11,
   sentences averaging 12 to 18 words), §2, §4 and §5.
3. `control/hard-subjects-policy.md`, especially §2 (the seven forbidden moves), §3b (the
   clinical-word rule), §4 (never invent a name), §6b and §7.
4. `control/VIEWER-CONTRACT.md` §2 and §3 (structure the validator cannot see).
5. Your part file, whole.
6. The bank for your eras: `python tools/slice_bank.py <slug> --eras <eras> --bank-only -o <scratch file>`,
   then read that file. It is the only source of facts the prose may use.

## Start your findings file first

Create it before your first pass, with the header below, and append each era's findings as you
finish that era. If you are stopped partway, the findings you have written survive.

    # Findings: <slug> <part> (checker: <model>, task <TASK>, <date>)
    | # | era | line | rule | severity | text (exact quote) | what is wrong | suggested repair | sure? |
    |---|-----|------|------|----------|--------------------|---------------|------------------|-------|

- **line:** the line number in the part file. Use `grep -n` to get it.
- **rule:** the exact rule heading from the guide (for example "Personification and
  Anthropomorphism"), or "Hard subjects §2: Minimization", or "Not in bank", or "Structure".
- **severity:** `BLOCKING` (a fact wrong or not in the bank, softening, an invented or wrong
  name, structure that breaks the viewer), `MAJOR` (any other forbidden construction), or
  `MINOR` (reader fit: a long sentence, a hard word undefined, a shorter word available).
- **text:** quote the exact words, short enough to find, long enough to be unique.
- **suggested repair:** write the replacement sentence itself, following the rule's stated
  repair. For "Not in bank", say whether the bank has a nearby fact, or that it has none.
- **sure?:** `yes` or `unsure`, and for `unsure` say why in the "what is wrong" cell.

## The procedure: six passes over each era

Work one era at a time. Run all six passes on an era, write its findings, then go to the next
era. Read every sentence in every pass. Do not skim a paragraph because the first sentence
was clean. **Read for the move, not the string.** A search finds a word. It does not find a
sentence doing the forbidden thing in new words.

**Pass 1: facts against the bank.** For each sentence, find each fact in it: every name, date,
number, place, quote and cause. Look for it in the bank slice. Report as "Not in bank" any fact
you cannot find there. **Before you report "Not in bank", search the whole bank file**
(`grep -n -i "<key word>" research/research-<slug>.md`), including its PATCH and "Parked from"
sections, not only your era slice: facts often sit in another era's section or a later PATCH.
Also report a number that differs from the bank's, a range the prose
narrowed, a date that contradicts another date in the file, and a "first", "only", "largest" or
other superlative that the bank does not state.

**Pass 2: hard subjects.** Wherever the prose tells of harm (violence, death, disease, land
taken, forced labor, punishment, experiments on people), check it against the seven forbidden
moves in `hard-subjects-policy.md` §2, one by one. Compare against the bank: is the prose
milder, vaguer, smaller or shorter than the bank's account? Check that every clinical word
(§3b) says in plain words what was done, what it did to the person, and by what method. Check
that every `hb-story` is a named, documented person, and that no one is a composite. Check
that when newcomers take land, the prose says who lived there if the bank says it.

**Pass 3: false actors.** List the subject of every sentence and every clause in the era,
one by one, and test each; this is the pass most often under-reported. Mark every one that is
not a person or group of people. Newspapers, news outlets, committees, boards, councils,
companies and courts count as institutions. For each one, ask whether that subject can literally do what the verb says.
- Institutions: law, act, treaty, court ruling, school, company, city, colony, state, nation,
  government, agency, department, movement, church, army. A company can own. It cannot decide,
  want, refuse, fight, punish or kill. People in it can.
- Abstractions (the war, the economy, the change, the idea, history, progress) do nothing.
- Every passive: name its agent aloud. If the prose never names the agent and never says the
  record does not name one, report it.
- Watch the repairs: "The school cut the children's hair" is still an institution acting. The
  repair is "Staff at the school cut...".
- Nations: a nation named as a people ("the Powhatan", "the Haudenosaunee") is a group of
  people and may act. A nation named as a state or an institution ("Spain", "Britain", "the
  colony", "the Crown", "the United States") may not. Name the people.

**Pass 4: decoration and AI cadence.** Look at sentence shapes, ignoring meaning. Report
triads (three parallel items or clauses used for rhythm), anaphora (sentences or clauses
starting with the same words), "not just X but Y", "not X, but Y" reversals, a fragment used for
emphasis, a closing line that reverses or sums up, rhetorical questions, staged scenes,
similes and analogies, evaluative adjectives that tell the reader how to feel ("brutal",
"tragic", "remarkable"), promotional words, gnomic lines (a general truth stated as a moral),
and register breaks ("thus", "indeed", "sought to", "would come to", "little did they know").
Read the first sentences of the era's paragraphs together, then their last sentences. If they
share a shape, report it.

**Pass 5: the reader.** Report sentences over about 25 words and sentences carrying more than
one idea. **Hard words are the check most often missed.** Go through the era word by word and
list every word an 11-year-old might not know: legal, court and government words (proclamation,
inquiry, treaty, charter, tribute, petition, council, deed, grand jury, penitentiary, reprieve,
posse, pardon, militia), religious and military words, and
any word from another language. For each, find its first use in this part file and check that
the same sentence or the next one says what it means in plain words. Report each one that does
not. Report a long
word where a shorter one means the same. For each paragraph, try to finish "This teaches the
reader that ____." If you cannot, report the paragraph under "The Teaching Point". Report any
paragraph that withholds its main fact until late, for suspense. Report every **fourth-wall
break** (BLOCKING): any sentence that mentions the book itself, this chapter, research,
searching, sources checked, writers, agents or drafts ("this book", "we could not find",
"while researching"). An unknown fact is stated from the side of the historical record
("No surviving record names...").
That sentence is the prescribed form, not a defect: do not report "the records do not say
who" as a missing agent or ask for a SEARCHED, NOT FOUND line behind it.

**Pass 6: structure and punctuation.** Report any em dash (U+2014) or semicolon, including
inside a heading or a `label="..."`. Report records (`> **Key:** value` lines) outside an
`hb-story`, a heading or table inside a block, a `status=` other than `verified` on a story,
an era whose `progress=` is not `written`, and anything else in VIEWER-CONTRACT §3.

## What not to do

- Do not edit the part file, the bank or the outline.
- Do not report anything inside an `hb-note` block (an editor's note the viewer never shows).
- Do not report the `### Name` heading inside an `hb-story` block: it is the template
  (`control/grid-markers.md` §8). Do not propose moving text between eras or cells, and do not
  report a date that falls outside its era's range: a story reaches back or forward when it
  needs to.
- Do not report a defect you cannot quote.
- Do not stretch. A pass that finds nothing has passed. But do not stop early either. Every
  sentence gets every pass.
- Do not rewrite for taste. Report only what breaks a stated rule, and name the rule.

## Finish

At the end of the findings file, add a count by rule and by severity, and list the eras with no
findings. Then run `node tools/validate_grid.js <part file> --part` and
`python tools/project_state.py --punct <part file>` and paste both outputs at the bottom.

Report in under 150 words: total findings by severity, the three rules broken most often, and
anything you were unsure how to judge. The findings file is the deliverable.

## Calibration (the first three checker runs, Jon 2026-09-26)

The first three part files are checked twice with this same brief, once by sonnet and once by
opus, each writing its own findings file. The fixer then judges the combined list, and the
director records in `control/audit/CHECKER-CALIBRATION.md` what each model found and missed, by
rule. Every miss that shows a pattern becomes a sharper instruction in this brief. The goal is
a sonnet checker as good as an opus one. Record each change to this brief in the calibration
file.
