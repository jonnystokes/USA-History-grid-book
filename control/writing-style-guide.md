# Writing Style Guide: US History Book (the book's amendment)

## Required reading first

**You must read `control/general-writing-style-guide.md` (Writing Style Guide, Version 2)
in full before you write or judge a sentence of this book.** It is required, and this file
does not summarise it. Jon adopted Version 2 on 2026-09-26 as an absolute requirement, in
both environments. It replaces Version 1 (`C:\Users\jon\Projects\writing-style-guide.md`).

Version 2 contains the prose rules and their repairs. Its rules are grouped by defect under
headings and carry no section numbers, so cite a rule by its heading, for example "The AI
Cadence" or "Passives with a Missing or False Agent". Every rule states the defect and the
repair.

This file contains only what is specific to this book: the reader, the subject, and the
policy. **Where the two files disagree, this file governs the reader, the subject and the
policy. Version 2 governs prose mechanics.**

## 0. Jon's seven guidelines (2026-09-30, DECISIONS #28): read these first

Jon: "Think of this as your own kids. How would you want them raised, knowing the truth? They
should know how bad it was, and it should also be fun to read." These govern every other rule
in this file and in the hard-subjects policy.

1. **The whole truth, plainly.** Use the plain word for the act: rape (never "assault"),
   murder, killed, enslaved, stole, burned alive. Name who did it. Give the numbers. No modern
   softening ("mistreated", "relocated", "passed away", "incident"). A reader who later learns
   more must never find it was worse than this book said.
2. **Fit the age by clarity, not by leaving things out.** One plain sentence for the act, the
   word explained, then move on. No gore, no lingering, no horror-movie detail.
3. **Make it fun to read.** Real people, concrete detail, surprising true facts, people's own
   words, humor where history is funny. When you repair a sentence, keep its vivid detail; do
   not flatten it into a summary. Never invent anything to make it livelier.
4. **When sources disagree,** the director decides, or an opus agent checks the primary
   sources first. Write the better-supported version. If it is genuinely unsettled, say
   plainly that the accounts differ, and give each.
5. **Living people:** state what courts and records show. Never tell an accusation as fact.
   No hero profile (`hb-story`) for a person whose conduct is in open dispute.
6. **The director decides and reports.** Calls are logged in `control/DECISIONS.md`.
7. **No big words anywhere.** Use the word an 11-year-old would use. If no single plain word
   exists, spell it out in a few plain words: "charged with a crime", not "indicted";
   "lawmakers", not "legislature"; "later", not "subsequently". A hard word stays only when
   it is the subject itself (a disease, a law's name, a word people of the time used), and
   then it is explained in plain words right there, the first time it appears in each part
   file (a reader may open any era).

### Version 2 rules with a fixed meaning in this book

- **Zero em dashes and zero semicolons** in anything a reader of the book will see: the
  prose, the headings and the story blocks. `python tools/project_state.py --check <slug>
  --stage prose` counts both characters and fails the chapter on a single one. The outlines
  and research banks contain thousands of em dashes. A writer must not copy that punctuation
  into the prose.
- **Passives.** Version 2 allows a passive when the actor is unknown or does not matter to
  the reader ("the bridge was built in 1893"). In this book, `hard-subjects-policy.md` adds
  a condition. When someone was harmed, killed, moved, taken, or punished, the actor always
  matters. Name the actor. When the sources do not name one, write that the records do not
  say who did it.
- **Repeated units.** A grid of 37 chapters by 10 eras, plus story blocks, is a set of
  repeated units. Version 2's rule "Repeated units must not share a shape" (under "Writing
  the Reader Will Act On") applies to every era cell and every story block. Read the first
  sentences of a chapter's ten eras together, then their last sentences. If they sound
  alike, rewrite them.
- **Rhetorical questions.** Version 2 allows a question as a section opener when the next
  sentence answers it, and never in two consecutive sections. That limit applies here. A
  question anywhere else is a defect.
- **Mode.** This book is narrative and analytical history. Version 2's instructional
  requirements (imperatives, one action per step) do not apply to its prose. Its root
  metaphors do apply wherever the prose refers to the book itself.

Also binding, and also not summarised here: `control/hard-subjects-policy.md`.

---

## 1. The Reader

This section outranks anything in either file that conflicts with it.

### 1.1 Who they are

Ages 8 to 15. They do not know this history. They cannot tell when you have left
something out, so anything you soften becomes what they believe happened. That is
why `control/hard-subjects-policy.md` is binding, and why it is not in tension
with writing plainly. Hard facts and plain words go together. They are not a
trade.

They are reading to **learn something**, not to admire the prose. Every sentence
that makes them work harder without teaching them more is a sentence that failed.

### 1.2 Reading level

Aim at a competent 11-year-old and the 8-year-old will follow most of it while
the 15-year-old is not insulted. Concretely:

- **Sentences average 12–18 words.** The information sets each sentence's length, so
  lengths vary (Version 2, "The Reader"). A 40-word sentence needs a reason.
- **One idea per sentence.** Two clauses maximum. If you need three, use two
  sentences.
- **Paragraphs of 3–6 sentences.**
- **Prefer the shorter word every time it means the same thing.** Not "utilize"
  but "use". Other pairs: "subsequently" becomes "then" or "later", "in the vicinity
  of" becomes "near", "demonstrate" becomes "show", "sufficient" becomes "enough",
  "numerous" becomes "many", "commenced" becomes "began", "residence" becomes "home",
  "obtain" becomes "get", "purchase" becomes "buy", "construct" becomes "build",
  "approximately" becomes "about", and "prior to" becomes "before".
- **Active voice by default.** "Congress passed the law" is not a fix. That is
  personification. "The men in Congress voted the law through" is a fix.

### 1.3 Hard words you must keep

**First try to replace the word (§0 rule 7).** Most legal and government words can be
spelled out in a few plain words, and should be: "charged with a crime" for "indicted",
"a group of citizens who decide whether there is enough proof for a trial" for "grand
jury" when the sentence does not need the name. Only some words cannot be swapped without
losing the fact: the clinical words in `hard-subjects-policy.md` §3b, the proper names of
things (laws, cases, places), and words that are the subject of the passage. **Keep those and
define them on first use in each part file, in the same sentence or the next one, in plain
words.**

**Weak:** "The commissioners authorized a declaration of taking."
**Strong:** "Army lawyers filed a paper called a declaration of taking. Under it,
federal officials could take the land right away and argue about the price later."

Put the definition in the same sentence as the term or in the next one. The reader cannot go
on without it.

### 1.4 What a reader this age cannot do

- They cannot hold an unexplained term for three paragraphs waiting for it to be
  defined.
- They cannot resolve a pronoun whose subject was two sentences ago behind
  another noun.
- They cannot reconstruct a timeline from scattered dates. Give dates in order.
- They cannot tell that an unfamiliar word is unimportant, so an undefined one
  stops them.
- They cannot infer what you decided not to say.

---

## 2. How the General Rules Land in This Book

The rules are in the general guide. These are the forms they take here, drawn
from real defects in finished chapters.

**Personification.** The institutions are the trap: a law, act, treaty, school,
company, city, colony, nation, agency, department or movement cannot want,
decide, seek, struggle or demand. Name the people.

- **Weak:** "The economy struggled to recover from the panic."
  **Strong:** "Bank officers called in loans. Owners who could not repay closed
  their shops, and in the industrial cities fifteen percent of workers lost their jobs."
- **Weak:** "The Constitution believed in limited government."
  **Strong:** "The framers designed the Constitution to limit federal authority."
- **Weak:** "The factory system demanded a new kind of worker."
  **Strong:** "Factory owners required workers who could operate machines on
  fixed schedules."

Nations are not characters. "France sought revenge" hides which minister, which
faction, which assembly. This rule is broken most often **while repairing a
passive**, because the repair needs a subject and an institution is the nearest
one to hand.

**Register.** The archaic direction is the live risk in a book about early
periods, where the subject seems to invite it. Banned outright: "thus", "indeed",
"sought to", "would come to", "was to become", "in the fullness of time", "little
did they know", "a people", "these were the men who", "and so it was that", "the
land itself", inverted word order ("Great were the changes"), and the historical
present used for drama.

- **Weak:** "Thus did the settlers come to that shore, seeking what they could
  not find at home, and the land they found was not empty."
  **Strong:** "The settlers landed in 1620. They were looking for farmland and
  for the right to run their own church. People were already living there."

A chapter about 1550 is written in the same voice as a chapter about 2020. The
subject changes. The voice stays the same.

**Analogies.** Comparisons between periods are allowed and carry information:
"the Panic of 1893 resembled the Panic of 1873 in its banking structure but
differed in its labor response." Comparisons to modern unrelated things are not:
"the Articles of Confederation were like a beta version of the Constitution."

**Cadence.** The forms and their repairs are in the general guide. The two that
recur here:

- **The triad.** "They came for land, for freedom, and for a chance to begin
  again" becomes "They came for land. Most were farmers who could not get land at
  home."
- **The closing reversal.** "And that changed everything." "Nothing would be the
  same." Cut it, and if it held a fact, move the fact to the front of the
  paragraph.

**Sound.** The read-aloud test for this book: if it sounds like a knowledgeable
person explaining something to a kid at a kitchen table, it is right. If it
sounds performed, it is wrong.

---

## 3. Order and Mode

**Chronology is the default.** When you depart from it, for a thematic section, a
biographical sketch or an analytical interlude, signal the departure clearly and
return to chronology when it ends. A reader this age cannot rebuild a timeline
from scattered references.

**Narrative and analytical modes both work here, and neither borrows from
fiction.** A narrative passage reconstructs its scenes from evidence and signals
the evidentiary basis when it is uncertain: "according to his letters", "witness
accounts differ on whether". An analytical passage states its interpretation and
then demonstrates the basis. Do not mix the two inside a section without
signalling the change.

---

## 4. Teaching Point: the Numbers for This Book

The general guide requires you to finish "after reading this, the reader will
understand ____" before writing a block, and to get to the point fast. For this
book those are measured:

**The two-question test, applied to every block:**

1. What is this teaching?
2. How many words before it gets there?

If the answer to 1 is vague, cut or rewrite the block. **If the answer to 2 is
more than about twenty-five words, move the point to the front.**

- **Weak:** "In the spring of 1889, thousands of people gathered at a line drawn
  across the prairie. Wagons stretched to the horizon. At noon a gun fired. What
  followed would build a city in a single day."
- **Strong:** "On April 22, 1889, President Benjamin Harrison opened about 1.9
  million acres to settlers by proclamation. US officials had taken the land from
  Native nations. About 50,000
  people raced in at noon. By nightfall Guthrie was a town of about 10,000."

Withholding a fact to create suspense is a form of softening.

---

## 5. Audit Additions

Run Version 2's "Self-Review Before Reporting" first. Then these three, which are
specific to this book:

1. **Find every institution that is the subject of a verb.** Law, act, treaty,
   school, company, city, colony, nation, agency, department, movement. Each is a
   personification defect unless the verb is something it can literally do: a
   company can *own*. It cannot *decide* or *want*.
2. **Read for softening, do not search for it.** A search finds the string and
   misses the move. It will never find "the land was open for the taking", which
   is the same erasure as "empty prairie". You can recognise these when you read.
   A pattern match cannot.
3. **Find every hard word you kept** and check it is defined in plain words at
   first use, including the clinical ones governed by `hard-subjects-policy.md`
   §3b.

---

## 6. Checklist Additions

The general guide's checklist applies in full. Add these four:

1. **Reader fit:** sentences 12–18 words, one idea each, the shortest word that
   means it, every hard word defined at first use?
2. **Softening:** is any fact softened, abstracted, or summarised away? The
   reader cannot reconstruct what you left out.
3. **Institutions:** is a law, act, agency or nation the subject of a verb it
   cannot perform?
4. **Chronology:** is the timeline clear, and are the dates in order?
