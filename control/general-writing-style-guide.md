# Writing Style Guide, Version 2

**Status.** Version 2 is the live guide. The owner adopted it on 2026-09-26 as an absolute
requirement. Version 1 (`C:\Users\jon\Projects\writing-style-guide.md` on the owner's
computer) is superseded for this book. In this project, this file is
`control/general-writing-style-guide.md`. The book's own amendment is
`control/writing-style-guide.md`. The two files have different names and different jobs.

**Scope.** This guide governs non-fiction writing: explanatory, instructional,
reference, and analytical. Fiction, poetry, and drama are out of scope. When a
project supplies its own style guide, that guide governs project rules,
and this guide governs the prose.

**Self-reference.** This guide must follow its own rules. Every requirement here
applies to this file. Any AI that edits this guide must apply every rule to the
guide itself before reporting the work as finished.

**How to find a rule.** The rules are grouped by defect. Nothing here is numbered
and nothing here is a sequence. An AI must be able to open this guide at the
relevant defect, read the rule and its repair, and act on it without reading the
rest of the guide.

---

## Core Requirements

Every sentence must convey a fact, an event, a causal relationship, a process, an
instruction, or a reasonable inference from evidence. A sentence that performs
wisdom, decorates the page, stages a scene for effect, or comments on its own
importance must be recast or removed.

The question to answer is "What happened, how does it work, and why?" The text
must state the answer. It must not perform the answer.

Every rule below states the defect and the repair. A rule that only states what
to avoid leaves the writer to invent a replacement. The replacement is then the
same defect in a new form. Where several repairs apply, they appear together and
the writer chooses the one that preserves the most information. Deletion is
always available as a repair. A sentence that states no fact, no instruction, and
no inference must be deleted.

### The Quotable-to-Usable Test

The writer must apply one test to every sentence that stands out: **if it sounds
quotable, rewrite it until it is usable.** A sentence is usable when the reader
can extract an action to take, a value to check, or a constraint to obey. A
sentence that states only a feeling must be rewritten.

This test identifies defects that no other rule in this guide names, because a
sentence can satisfy every prohibition and still give the reader nothing to act
on.

- **Weak:** "A house is the sum of thousands of small decisions."
- **Strong:** "A build produces thousands of recorded decisions. This book states
  where each one is recorded."

### When Two Rules Conflict

When two rules in this guide conflict, the writer must apply the rule that
preserves more information. When both rules preserve the same information, the
writer must choose the rule that produces the clearer sentence, and must report
the choice to the user rather than leaving it unexplained. The writer must not
embed the explanation in the draft, because a note written for the user then
ships to the reader.

### The Reader

Before writing, the writer must decide who the reader is and what the reader
already knows. Where this section conflicts with anything below, the writer must
apply this section.

- **Name the reader.** The reader's age, background, and reason for reading
  determine every other choice. The writer must write for one specific reader,
  not an average.
- **Write no run-on sentences.** A sentence that joins clause to clause until the
  reader loses track of the subject must be split. A sentence the reader must
  re-read to find the verb is a run-on. The writer must keep one idea per
  sentence and must use paragraphs of a few sentences. A long sentence requires a
  reason, and the reason must be that the information needs the length.
- **Vary sentence length.** A run of sentences at the same length produces a beat,
  which the reader hears instead of the content. Sentence length must follow the
  information.
- **Use the shorter word** every time it means the same thing. Use "use," not
  "utilize." Use "show," not "demonstrate." Use "before," not "prior to." Use
  "enough," not "sufficient." Use "many," not "numerous."
- **Define hard words on first use.** The writer must define a hard word in plain
  language in the same sentence or the next one. Technical, legal, and specialist
  terms that cannot be replaced by a plain word must stay, and must be explained
  immediately. An undefined term stops the reader at that point in the text.
- **Do not assume the reader can fill gaps.** The reader cannot hold an undefined
  term across several paragraphs, resolve a pronoun whose subject appeared
  sentences earlier, or reconstruct a timeline from scattered references. The
  reader cannot infer what the writer decided not to say.

### Voice in Instructional Writing

A consistent voice is allowed in instructional writing. A terse cookbook, a dry
manual, and an opinionated guide are all acceptable. The voice must be
consistent, must not obscure information, and must not perform. A terse,
declarative voice is not a violation, because terseness removes words without
removing facts. A voice that changes register within a passage is a violation.

---

## Forbidden Constructions: False Actors

### Root Metaphors

A **root metaphor** is the underlying model a writer works from when thinking
about the subject. The writer applies it without deciding to. Repairing
personification and reification one sentence at a time does not stop the writer
producing twenty more, because the writer still works from the same model. The
writer must correct the model.

These root metaphors govern all writing under this guide.

**A document is a structured reference, not a person and not a conversation,
because the reader looks things up in it rather than listening to it.** A book, a
chapter, a section, a table, and an entry perform no actions. They do not carry,
answer, say, tell, give, touch, travel, hold, want, need, cover, or have jobs.
When a document element is the subject, the writer must use one of these verbs:
contains, lists, states, specifies, defines, describes, includes, provides,
records, identifies, documents.

- **Weak:** "This book has four jobs." **Strong:** "This book serves four functions."
- **Weak:** "The chapter carries the code sections." **Strong:** "The chapter lists
  the code sections."

**Information is present or absent. It does not move.** Information does not
travel, get handed over, or go into a binder.

- **Weak:** "The citations travel with the chapter." **Strong:** "The chapter
  includes the citations."
- **Weak:** "What goes into the binder." **Strong:** "The binder contents."

**The reader is an agent performing tasks, not a guest in a scene.** Imperatives
addressed to the reader are the normal instruction form and are always allowed.
Staged scenes of the reader are forbidden. The writer must describe the property
of the document and let the use follow from it.

- **Weak:** "Open one chapter while working on that system." **Strong:** "Each
  chapter functions as a standalone reference for its system."

**Subjects that are not document elements.** The approved verb list governs
document elements. It does not govern every subject. A living person takes the
ordinary range of verbs, including wanting, deciding, and refusing, because a
person does those things. A physical thing or a process takes a verb naming what
physically happens, which the technical-verb exception under Personification
defines. An institution, an abstraction, or a material takes neither, and the
writer must name the people or state the mechanism.

**When two root metaphors conflict.** A document cannot be both a structured
reference and a container. When a sentence draws on two models, the writer must
keep the structured-reference model and discard the other, because a reader who
looks something up needs to know where it is stated rather than what it sits
inside. The writer must apply the approved verb list to every case where the
subject is a document element, and must use one model throughout a passage rather
than alternating between two.

### Personification and Anthropomorphism

**Anthropomorphism** is the attribution of human traits to non-human entities.
**Personification** is the subtype that gives human qualities, actions, or agency
to non-living things.

The writer must not attribute human qualities, actions, or agency to non-living
things. Institutions, nations, economies, documents, ideas, systems, and abstract
forces do not think, feel, want, decide, struggle, or die. People within them do
those things. The writer must name the people, or name the thing and use a verb
it can literally do.

- **Weak:** "The policy struggled to take hold."
- **Strong:** "Officials delayed enforcing the policy. Few businesses complied."

The same rule covers physical objects and materials. This form is harder to
notice than the institutional form, because the sentence sounds practical.
Ingredients, tools, machines, and parts have no wishes and no character.

- **Weak:** "The dough wants a longer rest." **Strong:** "Rest the dough an hour."
- **Weak:** "Flour does not measure honestly." **Strong:** "A cup of flour varies
  by up to a fifth, depending on how it was scooped."
- **Weak:** "Fillings are loose because they forgive." **Strong:** "Small changes
  to a filling do not affect the result."
- **Weak:** "The gel refuses to hold a fold." **Strong:** "The fold opens because
  the gel is too wet."

**The pathetic fallacy** is the subtype of personification that assigns emotion or
moral quality to an object or to nature: honest flour, stubborn dough, a generous
oven, a cruel winter. Adverbs and adjectives produce the pathetic fallacy as often
as verbs do. The writer must check verbs, adverbs, and adjectives.

The verb classes that produce it:

- **Wanting:** wants, needs, likes, prefers, demands, insists, asks for, calls for.
- **Refusing:** refuses, resists, fights, punishes, struggles, gives up, tolerates.
- **Knowing:** knows, decides, judges, remembers, waits, forgives, behaves,
  cooperates.

A non-living thing performs none of these actions. The writer must also not cast
an object as an opponent or a colleague: "X is the enemy," "the stout does the
heavy lifting," "the leaf does three jobs." The writer must state the mechanism
instead.

**Allowed: technical verbs.** Technical verbs are allowed when they describe real,
measurable behavior of a thing ("the beam carries the load," "the pump moves the
fluid," "the yeast consumes the sugar"). The test is not whether the verb sounds
physical. The test is whether the thing named could perform that action with no
mind and no hands. "The seasoning carries the dish" fails that test. Seasoning
carries nothing.

**Allowed: the reader.** In explanatory writing, "the reader" may be treated as an
agent, since the reader is the intended audience. "The reader must not reconstruct
the order" is acceptable. "The dough wants to rest" is not.

When the writer repairs a passive sentence, the writer often makes an abstraction
the new subject. The writer must check every repaired sentence for it.

**Repairs.**

- **Name the human who acts.** "The committee wanted" becomes "three members
  argued for."
- **State the physical mechanism.** "The dough fights you" becomes "the gluten
  contracts, so the dough shrinks back as you roll it."
- **Turn it into an instruction.** "The dough wants an hour" becomes "rest the
  dough an hour." This repair suits instructional writing, because it converts a
  claim about a thing's wishes into an action.
- **Delete it.** If the sentence only assigned a feeling and no fact survives the
  repair, the sentence was decoration and must be deleted.

### Reification

**Reification**, also called **hypostatisation**, is the treatment of an
abstraction as a concrete thing that can be owned, located, counted, or made to
act. Reification appears in a linking verb: *X is the Y*, or *X is not a Y*.

The writer must not treat an abstraction as a thing that exists and acts.

- **Weak:** "Wet hands are the whole technique, and the reward is a flavour no
  wheat dough reaches."
- **Strong:** "Keep your hands wet. Corn masa tastes of corn in a way wheat cannot."
- **Weak:** "Resting is not a delay, it is a step."
- **Strong:** "Rest the dough. Unrested dough shrinks back as you roll it."

**A definition is not reification.** A definition uses the copula to state what a
term means. A copular identity slogan uses the copula to equate a concrete thing
with an abstraction for effect. "Anaphora is a set of consecutive sentences
opening with the same shape" defines a term and is required. "This book is the
plan" equates a book with an abstraction and is forbidden, because the book
documents the plan rather than being it. The writer must distinguish the two uses
before rewriting any sentence built on "is."

**The copular identity slogan** equates two related things for memorability and
trades accuracy for shape. "This book is the plan." "The site is the first
decision." The two things stand in a relationship, and the copula asserts instead
that they are the same thing. The writer must state the relationship.

- **Weak:** "This book is the plan." **Strong:** "This book documents the plan."
- **Weak:** "The site is the first decision." **Strong:** "The site determines the
  foundation type, which the owner decides before anything else."

**Shorthand for the guide's own furniture.** In this guide and in any document
that states rules, "the rule states" means "the text of the rule states," and
"the pattern appears" means "the pattern appears in the draft the writer
produced." That shorthand is allowed when the meaning is clear and when the verb
comes from the approved list under Root Metaphors. A document that states rules
also takes the normative verbs requires, forbids, allows, permits, and governs,
because those name what the text of the rule does rather than an intention it
holds. The shorthand is not allowed with verbs of intention, such as "the rule
wants" or "the pattern insists."

Reification takes these habits:

- **The abstraction as object.** "The difference," "the point," "the trick," "the
  secret," "the reward," "the proof," "the whole idea." Each phrase names a thing
  that does not exist. The writer must state what happens instead.
- **The denial frame.** "X is not optional," "not decoration," "not fussiness."
  In each, the writer asserts importance and withholds the reason. The writer
  must give the reason. A denial is allowed when the sentence that follows states the
  reason: "The vodka is not decoration. The alcohol boils off, so the dough
  absorbs less fat." A denial that stands alone is forbidden.
- **The counted abstraction.** "Three rules carry the category." "Two approaches,
  and no middle ground." Rules carry nothing. There is no ground. The writer must
  state the things themselves.

**Repairs.**

- **State the event instead of the abstraction.** "The difference between a good
  one and a great one" becomes "fried hot, it browns before it flakes."
- **Give the reason the denial frame withheld.** "The vodka is not decoration"
  becomes "the alcohol boils off, so the dough absorbs less fat."
- **Replace the counted abstraction with the things themselves.** "Three rules
  carry the category" becomes the rules, as a list.
- **Delete the sentence.** The sentence that follows it states the real content.

### Passives with a Missing or False Agent

The **passive voice** is a construction in which the grammatical subject receives
the action rather than performing it. A passive is allowed when the actor is
obvious or when the actor does not matter to the reader. A passive fails when the
agent is missing and when the agent is false.

**The missing agent.** With no actor named, the reader takes the grammatical
subject as the one acting. "Fillings are given loosely" reads as though the
fillings perform the giving. The writer must name the actor or use the imperative.

- **Weak:** "Fillings are given loosely." **Strong:** "Measure fillings loosely."
- **Weak:** "The air is pushed out before sealing." **Strong:** "Press the air out
  before sealing."

**The false agent.** A *by* phrase that names something incapable of the action.
"Syrup is absorbed by the temperature difference" makes a difference absorb syrup.
The writer must name the real actor and the real mechanism: "Hot pastry absorbs
cold syrup."

A passive also hides who judged, who decided, and who is accountable: "is judged
by," "is considered," "is regarded as," "was determined." The writer must say who.

**Repairs.**

- **Use the imperative** in anything the reader acts on. This repair is shorter
  than the alternatives and removes the question of agency.
- **Name the actor and make it the subject.** "The evaluator digs test pits."
- **Name the mechanism** where the actor is a process rather than a person: "hot
  pastry absorbs cold syrup."
- **Keep the passive** when the actor is unknown or does not matter, and the
  subject is the thing the sentence is about: "the bridge was built in 1893." The
  defect is a passive with no nameable actor. A passive with a nameable actor is
  allowed.

### Modal Ambiguity

**Modal ambiguity** is a requirement attributed to an abstraction rather than
issued by a person, a code, or a manufacturer. The sentence states that something
is required without stating who requires it, so the reader cannot tell whether it
is law, trade practice, or the writer's preference.

- **Weak:** "Service systems carry the opposite requirement: routed for access."
- **Strong:** "The plumbing code requires access to every cleanout. Route the
  drain lines so the cleanouts stay reachable."

The reader acts differently depending on the source. Breaking a code requirement
can fail an inspection, and ignoring a manufacturer's instruction can void a
warranty. A reader who ignores the writer's preference risks neither. The writer
must state which one applies.

**Repairs.**

- **Name the source and the action.** State which code, which manufacturer, or
  which person requires it, then state what the reader does.
- **Convert it to an imperative** when the requirement is the writer's and the
  reader acts on it directly.
- **State the consequence** when no authority requires it and the writer is
  describing a result rather than a rule.

### Patient-Verb Agreement

When one subject governs several verbs, every verb must accept that subject's
category. Information nouns take information verbs: recorded, reviewed, revised,
communicated, understood. Physical nouns take work verbs: built, inspected,
repaired, replaced. Attaching a work verb to an information noun produces a
sentence that reads as fluent and states nothing.

- **Weak:** "Recorded decisions can be built, inspected, and repaired by people
  other than the person who made them."
- **Strong:** "With the record, a contractor can build what the decision
  specifies, an inspector can check the built work against it, and a future owner
  can repair the result without guessing at the original intent."

In the weak sentence the writer omitted the work product and applied the work
verbs to the record. A decision cannot be built.

**Repairs.**

- **Supply the missing object.** Name the thing the work verbs apply to, then
  attach them to it.
- **Split the sentence by category.** Give the information noun its own verbs and
  the physical noun its own verbs.
- **Delete the verb that does not fit.** When the mismatched verb adds no fact,
  removing it costs nothing.

---

## Forbidden Constructions: Decoration

### Rhetorical Schemes

**Antithesis** is a balanced pair of opposed statements. **Chiasmus** is a
reversed grammatical structure in two parallel clauses. **Isocolon** is a set of
parallel clauses of equal length and structure.

The writer must not use these figures. They produce sentences that sound finished
and state less than a direct sentence of the same length. They belong in oratory
and in literature, not in explanatory writing.

- **Weak:** "Costs fell in the cities and rose in the countryside."
- **Strong:** "Urban rents dropped 4 percent while rural land values rose 2 percent."

The test: if the writer can restate the sentence with more specific information in
the same number of words or fewer, the figure was decoration.

**A list is not a rhetorical scheme.** A list states items. A rhetorical scheme
arranges items for effect. A list of items that all carry information is allowed,
and the triad rule under The AI Cadence requires the writer to keep a real triad
as a list. The writer must distinguish the two by asking whether removing one item
would remove a fact. If it would, the items form a list. If it would only shorten
the rhythm, the items form a scheme.

**A list inside a sentence stays inside the sentence.** When every item in a run
of items carries a fact, the writer must not restructure the sentence into a
bulleted list. That change is formal rather than informational, and it disguises
the pattern rather than removing it.

**Repairs.**

- **Replace the balance with the figures it stood in for.** The pairing states
  neither figure.
- **Keep the half that carries information and cut the other half.** When only one
  side of the pair is true, keep that side.
- **Make it a list** when both halves are real and parallel. A two-item list
  states the symmetry without asserting that the symmetry means something.
- **Delete it.** When neither half of the pair states a fact, nothing survives.

### Gnomic Declaratives

A **gnomic declarative** is a statement of a timeless truth in the shape of a
proverb. It tells the reader what to think about a subject instead of showing what
happened.

The writer must not use gnomic declaratives. When a lesson follows from evidence
the text has provided, the writer must state the lesson plainly after the
evidence. A proverb must not stand in for evidence.

- **Weak:** "Necessity is the mother of invention."
- **Strong:** "When the supplier stopped shipping parts, the team machined its own."

**Repairs.**

- **Replace the proverb with the evidence behind it.** State the specific case that
  produced the belief.
- **State the lesson after the evidence, in plain words,** when the lesson is the
  writer's to draw.
- **Delete it.** A proverb with no evidence behind it states nothing the writer
  verified.

### Admonitory Declaratives

An **admonitory declarative** is a true statement delivered in the cadence of a
warning. The fact is correct, but the sentence takes the shape of a proverb, so
the reader takes it as received wisdom rather than as a finding the writer can
support. It differs from the gnomic declarative, which asserts something the
writer never verified.

- **Weak:** "No thickness of material elsewhere compensates for the gap."
- **Strong:** "A thermal bridge conducts heat around the insulation. Insulation
  added elsewhere does not reduce the loss at the bridge."

**Repairs.**

- **Restate it as a definition and its consequence.** Name the thing, then state
  what follows from it.
- **Give the measurement** the warning stood in for.
- **Delete it** when the same fact appears elsewhere in plain form.

### Explanatory Analogies and Similes

The writer must not explain one thing by comparing it to an unrelated thing. The
comparison adds a second object the reader must hold in mind, and it
oversimplifies both objects. A comparison inside the same domain is allowed when
it carries information.

- **Weak:** "The framework was like a blueprint for the software."
- **Strong:** "The framework lists the required components and the order they load."

A simile is allowed only when it fixes a property the reader can act on. "Folded
in thirds, like a letter" names a shape. "It bubbles up like a pillow" names
nothing and is decoration. When the comparison can be deleted without losing an
instruction, the writer must delete it.

**Repairs.**

- **State the mechanism of the actual thing** in ordinary words. This repair states
  the mechanism in fewer words than the analogy uses.
- **Swap the outside comparison for one inside the domain** when the comparison
  carries information: "the Panic of 1893 resembled the Panic of 1873 in its
  banking structure."
- **Keep the simile and add the property it only implied** when it names a shape or
  a motion the reader must copy.
- **Delete it.**

### Staged Scenes

The writer must not stage hypothetical scenes and must not address the reader as
though the reader stands somewhere else. The writer must not ask the reader to
imagine a situation that the writer can describe.

- **Weak:** "Imagine yourself a farmer in western Massachusetts in 1786, watching
  the sheriff ride up the lane."
- **Strong:** "Courts in western Massachusetts heard 3,000 debt cases in 1786. A
  farmer who lost one could be jailed or have his land sold."

**Repairs.**

- **State the conditions the scene dramatised**, with figures.
- **Use a real instance instead of a hypothetical one.** A named person on a known
  date gives the reader the same detail and can be checked.
- **Delete the scene.** The remaining sentences state what the writer verified.

### Forced Rhythm and Sound Patterning

The writer must not choose a word for its sound next to neighbouring words. No
alliteration, no internal rhyme, no metrical regularity, no assonance. A patterned
sentence is harder to read for information than a plain sentence, because the
reader attends to the pattern as well as to the meaning.

- **Weak:** "Steel and steam and sweat built the city."
- **Strong:** "Workers raised the city's frame in steel. Steam engines lifted it."

**The read-aloud test.** The writer must read the paragraph out loud. If it sounds
performed, the paragraph is wrong. If it sounds like a knowledgeable person
explaining something clearly, the paragraph is right.

**Repairs.**

- **Swap the patterned word for the plain word**, even when the plain word is
  duller than the patterned one.
- **Break the metre by adding the specific detail** the rhythm stood in for: a
  number, a name, a date.
- **Reorder the sentence** so that the stressed words fall where the meaning is
  rather than where the beat is.

### The AI Cadence

Fluency and clarity are different properties. AI writing produces a house style
that is rhythmic and empty, and it reads as competent. Each sentence looks correct
when read alone, and the defect becomes visible only across several sentences,
which is why the writer working inside the draft misses it. The writer must assume
this cadence will appear in the draft and must work against it.

A **triad** is three items, clauses, or sentences in a row, added for rhythm rather
than for information. **Anaphora** is a set of consecutive sentences or clauses
opening with the same word or the same shape.

The following moves are forbidden. The third column states the repair. When the
sentence states nothing beyond the move, the writer must delete the sentence.

| Move | Definition | Repair |
|---|---|---|
| **The triad** | Three items, clauses, or sentences in a row because three sounds finished | Keep the items that carry information, whatever number that leaves. Cut the item added for rhythm. When every item carries information, the items form a list and must stay as they are. |
| **Anaphora** | Consecutive sentences opening with the same word or shape | Merge them into one sentence that states the shared subject once, then states the differences. "They built the roads. They dug the canals." becomes "The same crews built the roads and dug the canals, mostly Irish labourers paid about a dollar a day." |
| **The em-dash pivot** | A dash that sets up a reversal or a punchline | Replace the dash with a period. Let the second half stand as a plain statement. If the reversal was the only content, cut it. |
| **"Not just X, but Y"** | Also "It wasn't about A. It was about B." | Delete the X half. State Y with its specifics. The denied half was never the claim. |
| **The fragment for emphasis** | A deliberate non-sentence dropped in for weight | Attach it to the sentence before it or after it, or give it a verb. If it survives neither repair, it states emphasis and no fact. Cut it. |
| **The closing reversal** | A paragraph that ends on a turn or on a line built to land | End on the last fact instead. If the turn contained a fact, move that fact to the front of the paragraph. |
| **Escalating short sentences** | A run of clipped sentences building to a beat | Combine them into sentences of unequal length, set by the information rather than by the rhythm. |
| **The rhetorical question** | "What made it work?" | Write the answer as a statement. A question is allowed as a section opener when the next sentence answers it. The writer must not open consecutive sections with questions. |
| **Conversational meta** | "Here's the thing." "But there's a catch." | Delete the phrase. Start with the content. This move is metadiscourse in a friendly voice. |
| **Antithesis pairs** | "Not by force, but by law." | Give the figures the balance stood in for, or keep the true half. See Rhetorical Schemes. |

**The test.** The writer must read the passage and examine the shape of
consecutive sentences, ignoring their content. If the sentences are the same
length, the same construction, or if the writer can hear a beat, the passage must
be rewritten. Good explanatory prose has an irregular shape because sentence
length is set by the information, not by the rhythm.

**A caution.** The writer must not fix a triad by making it a pair. The writer must
not fix an anaphora by varying the opening word while keeping the parallel
structure. Remove the pattern. Do not disguise it.

---

## Forbidden Constructions: Weak and Inflated Claims

### Hedged Predicates

A **hedge** is a word or phrase that weakens a claim and hides the evidence.

The writer must state claims directly. Hedges that obscure, such as "may have
been" and "it is generally believed," must not appear.

- **Weak:** "The change may have contributed to the decline."
- **Strong:** "Three studies found the change contributed to the decline. Two found
  no effect."

The writer must state conditions, not frequencies, where no measurement supports
the frequency. "Usually," "often," "typically," and "in most cases" are hedges
unless a measurement supports them. The writer must replace the frequency word
with the condition under which the statement holds.

A qualification that informs is allowed. A hedge obscures the evidence. A
qualification states it.

**The deontic hedge.** A second kind of hedge softens an instruction rather than a
fact. "The dough may be rested overnight" grants permission where a requirement
was meant. When the statement is a requirement, the writer must write it as one:
"Rest the dough overnight." When the step is optional, the writer must state what
the option produces: "An overnight rest makes the dough easier to roll thin."

**Repairs.**

- **Assert it.** When the writer believes the claim, the writer must state it
  without a softening word.
- **Name who holds the view and on what basis.** "Three studies found" replaces "it
  is generally believed."
- **State the real condition.** Where the uncertainty is genuine, name what the
  outcome depends on: the jurisdiction, the edition, the equipment, the site.
- **Cut the claim.** If a claim requires a hedge, the evidence for the claim is
  incomplete.

### Contrastive Negation

**Contrastive negation** is the denial of something the text never asserted. The
sentence implies a position the writer is rejecting, and the reader has to
reconstruct a claim nobody made.

- **Weak:** "There is no wood framing in the structural system."
- **Strong:** "The structural system is concrete and steel."

Contrastive negation differs from the denial frame. In the denial frame the
writer asserts importance and withholds the reason. In contrastive negation the
writer argues with a reader who holds a position the text never stated. In both, a
negation stands where a fact belongs.

A negation is allowed when the reader arrives holding the belief being corrected
and the writer has stated that belief. "Many owners assume a shed needs no permit. The code specifies a
size above which a permit is required" corrects a belief the reader already has.

**Repairs.**

- **State what is there.** Name the material, the method, or the value, rather than
  naming what is absent.
- **State the belief before correcting it** when the correction is the point.
- **Delete it.** A negation of something nobody claimed states nothing.

### Unanchored Comparatives

A comparative without a reference point cannot be checked or acted on. "More,"
"less," "faster," "better," and their variants must name what they compare to, and
must give a number where a number exists.

- **Weak:** "Growth was much faster than before."
- **Strong:** "Growth was 12 percent this year, against 4 percent last year."

**Repairs.**

- **Give both figures:** the value, and the value it is measured against.
- **Name the standard or the threshold** when no number exists: "above the code
  minimum of 7 feet."
- **Name the mechanism instead of the scale.** "Cheaper" becomes "it needs no
  second pump."
- **Cut the comparison.** The writer must never invent a number to satisfy this
  rule. An invented figure is a worse defect than a vague phrase.

### Evaluative Adjectives

The writer must describe what happened and must not tell the reader how to feel
about it. When the facts support the adjective, the adjective is unnecessary. When
the facts do not support it, the adjective cannot make the case.

- **Weak:** "The response was disastrous."
- **Strong:** "The response arrived three weeks late. By then 40 percent of the
  crop was lost."

**Repairs.**

- **Replace the adjective with the measurement** that prompted it.
- **Replace it with the consequence:** what happened to someone as a result.
- **Attribute the judgment** when the judgment is itself the fact: "the inspector
  called the response inadequate."
- **Delete the adjective.** The facts in the sentence state the case without it.

### Promotional Language

The writer must not sell the subject to the reader. The words "fascinating,"
"remarkable," "incredible," and "extraordinary" must not appear. The writer must
not promise that what follows will be exciting or important. Importance is shown
by the content, not asserted in advance.

- **Weak:** "The election of 1800 was one of the most dramatic moments in the
  nation's history."
- **Strong:** "Jefferson and Burr each received 73 electoral votes. The tie sent
  the election to the House, which took 36 ballots to choose a president."

A second form sells a property of the work by showing a pleasant outcome instead
of naming the mechanism: "you can hand one chapter to a contractor and have a
useful conversation."

**Repairs.**

- **Open with the strongest fact** and let the fact do the work.
- **State the property and the mechanism** that produces it: "each chapter includes
  its own code citations, so it can be read alone."
- **Delete the promise.** The reader must read that sentence before reaching the
  content, and it states nothing.

---

## Forbidden Constructions: Voice and Diction

### Metadiscourse

**Metadiscourse** is text that explains what the text is doing while it is doing
it. The writer must perform the function without narrating the performance.

- **Weak:** "This section will explore the causes of the shortage."
- **Strong:** Begin with the first cause.
- **Weak:** "It is important to understand that..."
- **Strong:** Remove the phrase. If the point is important, the content shows it.

Brief functional transitions are allowed ("By 1850, however..."). Self-referential
transitions are not.

**Repairs.**

- **Delete the phrase and start with the content.** The reader must read the
  self-referential phrase before reaching the working sentence.
- **Convert it into a heading.** "This section explains the causes of the shortage"
  becomes a heading reading "Causes of the shortage," which lets the reader
  navigate without narrating the text.
- **Convert it into a fact.** "It is important to understand that the levee was
  underfunded" becomes "The levee had received no maintenance funding since 1987."

### Register Breaks

**Register** is the voice or tone of the writing, determined by audience and
purpose. The writer must decide the register and hold it. One plain, present-day
voice runs through the whole work, and that voice stays the same across every
subject.

Register breaks occur upward and downward. Both are defects.

**Upward, into the literary or archaic.** The writer must not use "thus,"
"indeed," "sought to," "would come to," "little did they know," "in the fullness
of time," inverted word order, or the historical present used for drama.

- **Weak:** "Thus did the settlers come to that shore, seeking what they could not
  find at home."
- **Strong:** "The settlers landed in 1620. They wanted farmland and the right to
  run their own church."

**Downward, into the chatty, comic, or promotional.** A joke, a wink, an aside to
the reader, or a line of advertising copy breaks a plain register as an archaism
does. "Ketchup is not optional." "Accept that the first three will be ugly."
"Worth crossing town for." "The best of its kind anywhere."

A wry or personal register is an allowed choice, and the register must then run
through the whole work rather than appear every few pages. Mixed register reads as
unreliability, because the reader cannot determine which sentences to take
literally. The test: if a line requires a different tone of voice to read aloud,
the line is a register break and must be revised.

**Repairs.**

- **Keep the information and drop the performance.** "Ketchup is not optional"
  becomes "served with tomato sauce."
- **Replace the archaism with its plain equivalent.** "Sought to" becomes "tried
  to." "Would come to" becomes "later."
- **Move the line to a part of the work where that register is the rule**, such as
  a preface written in the author's own voice.
- **Commit to the register everywhere** when the writer wants the personal voice. A
  consistent wry book is acceptable, because the reader learns the voice and reads
  every sentence through it. A plain book with jokes scattered through it gives the
  reader no such rule.
- **Delete the line.**

### Semantic Bleaching

**Semantic bleaching** is the replacement of a concrete referent with an
evaluative abstraction, which implies a fact instead of stating it. The sentence
sounds specific and names nothing the reader can point at.

- **Weak:** "The long-life target is the part of the house that is difficult or
  destructive to replace."
- **Strong:** "The foundation, the framing, the roof structure, and the buried
  drain lines cannot be replaced without demolition."

The test: the writer must ask what the reader would point at. When answering takes
another sentence, the writer replaced a list with the abstraction.

**Repairs.**

- **Name the things.** Replace the abstraction with the items it stands for.
- **State the measurable property** when the category is real: "anything that
  requires demolition to reach."
- **Delete it** when the sentence that follows already names the things.

### Oversized Words and Nominalization

Every long word that has a short synonym is a defect. Every abstract noun that
could be a verb is a defect. **Nominalization** is the conversion of a verb into a
noun, which then needs a weak verb beside it.

**Repairs.** The writer must turn the noun back into its verb, which removes the
weak verb beside it. Where a long word has no short synonym, the writer must keep
it and define it. Where an abstract noun names nothing that anyone can point at,
the writer must cut it and name the thing itself.

- "Made a decision" becomes "decided."
- "Provided assistance" becomes "helped."
- "Reached an agreement" becomes "agreed."
- "The implementation of the policy resulted in the displacement of numerous
  families" becomes "About a thousand families had to leave their farms."

Nominalization also produces personification, because a nominalized action
requires a subject, and an institution is the nearest available subject.

---

## Forbidden Punctuation

### The Em Dash

An **em dash** is the long dash character, Unicode U+2014. In plain terms, it is
the dash that is longer than a hyphen and longer than an en dash. The writer must
not use it. The em-dash pivot is one of the AI cadence moves, and the writer
reaches for that move when the character is available.

The writer must replace every em dash with a period, a comma, a colon, or
parentheses. When none of those work, the writer must restructure the sentence.

- **Weak:** the words "The plan was simple," then an em dash, then "and it failed
  completely."
- **Strong:** "The plan was simple. It failed in the first month."

This guide contains no em dash characters, including in its examples. An AI
checking the guide can search for U+2014 and must find zero matches. The writer
must run the same search on every draft the writer produces. The draft must return
zero matches for U+2014 and zero matches for U+003B.

### The Semicolon

A **semicolon** is the punctuation mark at Unicode U+003B, which joins two
independent clauses. In plain terms, it is the mark that looks like a comma with a
dot above it. The writer must not use it. The semicolon appears in formal,
performed prose, and it is difficult to type on a standard keyboard.

The writer must replace every semicolon with a period and a new sentence, or with
a comma when the clauses are short and closely related. In a list, the writer must
replace semicolons with separate sentences or with a bulleted list.

- **Weak:** the words "Each sentence looks fine alone," then a semicolon, then "the
  damage is in the pattern."
- **Strong:** "Each sentence looks correct alone. The defect appears in the
  pattern."

This guide contains no semicolon characters, including in its examples. An AI
checking the guide can search for U+003B and must find zero matches.

---

## Structural Requirements

### Claims That Can Be Checked

Every factual claim must be traceable to evidence. Not every sentence requires a
citation, and the text must not assert what cannot be supported.

- **Weak:** "Many people opposed the war."
- **Strong:** "Anti-war petitions gathered 50,000 signatures in Boston and New York
  in the first six months."

**Repairs.** Give the figure and its source, name the specific instance behind the
claim, state what is known and what is not known, or cut the claim. The writer must
never invent a figure to satisfy this rule.

### Precise Words

The writer must choose the word that matches the thing, not the word that sounds
more dramatic or more restrained than the evidence supports. A "revolution" is not
a "reform." A "depression" is not a "recession."

**Repair.** Use the narrower word when the evidence supports it. When the evidence
does not support it, state the evidence and let the reader see the ambiguity
rather than choosing a label the evidence does not support.

### Genre Consistency

The writer must decide what kind of writing this is and stay in it. Narrative,
analytical, instructional, and reference modes each allow different moves. The
writer must not mix them within a section without signalling the transition.

**Repairs.** Move the out-of-mode passage into a section of its own, mark the
change with a heading or with a plain sentence that states what follows, or
rewrite the passage in the mode of the surrounding section.

### Information Order

The writer must put evidence next to the claim it supports. The writer must
introduce a person, a term, or a concept where it is first used, not pages later.
The reader must not hold an unexplained term in memory while reading further.

**Repairs.** Move the explanation to the first mention, put a one-line definition
at the first mention and the full treatment where it stands, or delay the first
mention until the explanation is due.

### Defined Terms

Once the writer introduces a term, the writer must use it the same way throughout.
The writer must not switch to a near-synonym unless the switch marks a
distinction. The reader must not guess whether two terms mean the same thing.

**Repairs.** Pick one term and replace every variant with it, or state the
distinction at the first place both terms appear. Variation for its own sake is a
defect in this rule.

### The Teaching Point

Before writing any block, the writer must finish this sentence in plain words:
*"After reading this, the reader will understand ____."* If the writer cannot
finish it, the block is not ready. If finishing it takes more than one sentence,
the block is doing two jobs and must be split.

The point must appear in the opening sentences rather than at the end as a reveal,
because explanatory writing is read in fragments and often abandoned part way.
Withholding a fact to create suspense is a form of softening. The writer who
withholds it leaves a reader who stops halfway with less than the truth.

**Repairs.** Move the last sentence of the block to the front and check whether it
states the point, split the block when it teaches two things, or cut the block
when the writer cannot state what it teaches. When the reader must work through
scene-setting, background, or throat-clearing before reaching the point, the
writer must move the point in front of them.

### End When the Information Ends

The writer must stop when the content stops. A summary that restates the section,
a callback to an earlier passage, and a closing line written to land are the same
defect at different scales. The closing reversal rule under The AI Cadence
identifies the sentence-level form. This rule identifies the paragraph-level form.

A summary is allowed when the reader uses it as a reference, such as a checklist
or a set of values gathered from a long chapter into one place. A summary that
restates the same content in the same order is not a reference.

**Repairs.** Cut the closing paragraph and end on the last fact, convert it into a
reference the reader acts on, or move a fact forward when the closing paragraph
states one the body did not.

### Writing the Reader Will Act On

Recipes, manuals, procedures, runbooks, and reference entries take extra
requirements. The reader of these holds something, works mid-task, and looks back
at the page between actions.

**Every sentence must instruct, inform, or warn.** A sentence that does none of
the three must be cut. The writer must apply this test first, because decoration,
anthropomorphism, and register breaks fail it, and cutting them here saves work
under the other rules.

**The writer must use the imperative, one action per step.** "Press the air out,"
not "the air is pushed out" and not "you will want to press the air out." The
writer must put the condition before the action, so the reader learns whether the
step applies before reading how to do it: "When the edges lift, turn it."

**The writer must give numbers, not adjectives.** "A hot oven" is not a setting.
Where a number exists, the number replaces the adjective. Where no number exists,
the writer must name the observable sign: "until the edges lift," "until a skewer
comes out clean."

**A passage about risk must state what the reader does about it.** Naming a hazard
without naming the response leaves the reader alarmed and unable to act. The
response is a check to perform, a person to call, a value to record, or a decision
to make. The writer must vary how the response is worded, because a work in which
every risk passage ends the same way produces the defect named in the next rule.

**Repeated units must not share a shape.** Reference works repeat a structure.
Repetition makes any verbal habit noticeable. If every entry opens with a sentence
fragment, or every entry closes on a maxim, the reader perceives the template
instead of the content and recognises the work as generated. The writer must vary
the opening by information, not by decoration. The writer must check by reading
the first sentence and the last sentence of a run of consecutive entries with the
middles covered. If they sound alike, the writer must rewrite the entries. The
writer must also watch for a stock phrase reused across entries, because in a long
work the reader meets that phrase repeatedly in one sitting.

**Repairs for shared shape.** Start each entry with the fact most specific to it,
rewrite the openings that are fragments into full sentences, or move a repeated
point into the shared front matter or back matter and reference it rather than
restating it in every entry.

---

## The Two Ways to Fail

Every rule in this guide forbids decoration. A writer who applies those rules
without judgment removes every specific word and produces prose that states
nothing. The writer must check for that failure as well. The middle column is what
a writer produces after over-correcting.

| Too decorated | Too dry | Target |
|---|---|---|
| The land gets a vote. | Site conditions constitute a controlling input to feasibility determination across multiple project dimensions. | The site sets the foundation cost, the septic location, and the truck access. Verify each before making an offer. |
| Inspections are not interruptions. They are checkpoints. | Inspection events gate progression between construction phases per the adopted administrative provisions. | Inspections are scheduled checkpoints. Concrete cannot be poured and walls cannot be closed until the matching inspection passes. |
| Never bury a code question in concrete. | Unresolved compliance items should be remediated prior to concrete placement to avoid rework costs. | Resolve code questions before the pour. A misplaced sleeve found after the concrete cures requires demolition. |

**Diagnostics for the dry side.** The writer must check for these, because no rule
above names them.

- A sentence that chains noun phrase to noun phrase is a list written as a
  sentence. The writer must break it into a list or cut items.
- An abstract-noun stack such as "erosion-control obligations," "feasibility
  determination," or "compliance posture" names no physical thing. The writer must
  name the physical thing.
- A passage about buying, hiring, or building that states no figure is incomplete.
  The writer must add the figure or state why no figure exists.
- A sentence the reader must re-read to find the verb is a run-on. The writer must
  split it.

**Add specifics before changing phrasing.** When a passage is flat, the
repair is a number, a product name, a source citation, or a measurement. The
repair is never phrasing alone. A writer who rewrites a flat sentence without
adding a specific produces a second flat sentence.

## Writing Process

**The first draft is not the final draft.** The first draft will contain
personification, hedges, evaluative adjectives, metadiscourse, and cadence
defects. These are byproducts of getting ideas onto the page. The writer removes
them in the revision pass. No separate editor stands between the writer and the
finished work, so the writer must run the self-review below before reporting
anything as finished.

**Read every sentence and ask what it does.** When a sentence conveys a fact, a
process, a cause, or a reasonable inference, the writer keeps it. When a sentence
exists to show enthusiasm, set a tone, decorate a transition, or tell the reader
what to think, the writer must recast it or cut it.

Recasting means one of these actions. Put the fact the sentence only implied in its
place. Merge it into the sentence beside it. Demote it to a clause inside that
sentence. Delete it. When none of them leaves anything, the sentence was
decoration and the writer must delete it.

**Test information density.** A sentence that can be removed without changing what
the surrounding sentences convey must be removed. A paragraph that restates the
previous paragraph in different words must be merged or cut.

**Prefer specific agents.** "The company decided" is weaker than "the plant manager
ordered the line stopped." "The public turned against the plan" is weaker than
"enrollment fell by half." Specificity means grounding claims in observable facts.
It does not require naming every person involved.

**Order the material so the reader can follow it.** In sequential or chronological
material, order is the default. When the writer departs from it for a thematic or
analytical passage, the writer must signal the departure and the return. The reader
must not reconstruct the order from scattered references.

**When the evidence is mixed, say so.** The writer must state which parts are
settled and which parts are not. "The evidence is mixed" is more useful to the
reader than false certainty, and more useful than a vague "it is complex."

---

## Self-Review Before Reporting

Before reporting work as finished, the writer must perform the following review.
Each check below identifies one kind of defect, and the repair is stated in the
section that defines that defect. The writer must not stop at finding the defect.
The writer must apply the repair, then re-read the sentence to confirm that the
repair did not introduce a different defect. A repair introduces a new defect when
the writer replaces a construction without checking the replacement.

The writer must read a page aloud and determine whether it sounds performed or
explained.

The writer must examine sentence shapes, ignoring meaning, and identify any
triads, anaphora, or beat.

The writer must read for the tells, not search for them, because a search finds
the string but not the move. The writer must notice dashes doing a reversal, "not
just," "wasn't just," "more than a," "thus," "indeed," "sought to," "would come
to," "little did," "here's the thing," and every construction like them that no
list predicted.

The writer must pick paragraphs at random and finish the sentence "This teaches
the reader that ____." If the sentence cannot be finished, the paragraph must be
revised.

The writer must find every institution that is the subject of a verb and verify
that the verb is something the institution can literally do.

The writer must find every sentence whose subject is a document element and verify
that the verb appears on the approved list under Root Metaphors.

The writer must find every subject that governs more than one verb and verify that
every verb accepts that subject's category.

The writer must apply the quotable-to-usable test to every sentence that stands
out. A sentence that sounds quotable must be rewritten until the reader can
extract an action, a value, or a constraint.

The writer must check for dryness. The writer must find chains of noun phrases,
abstract-noun stacks, and passages about buying, hiring, or building that state no
figure. A passage that passes every other check and still reads as flat is a
dry-side defect, and the repair is a specific rather than a rephrasing.

The writer must find every long word and check whether a shorter word means the
same thing.

The writer must find every hard word that was kept and confirm that it is defined
in plain words at first use.

The writer must scan for the verb classes under Personification (wants, needs,
likes, prefers, refuses, resists, fights, knows, decides, judges, waits, forgives)
and verify that no non-living subject is the agent.

The writer must find every "is the" and "is not a" and ask whether the thing named
exists outside the sentence.

The writer must find every passive and name its agent aloud. If the agent cannot
be named, or if the named agent could not perform the action, the sentence must be
rewritten.

The writer must find every em dash and every semicolon and remove them.

The writer must read lines aloud at intervals through the work, in the register the
writer chose for the work. Any line that requires a different voice must be
revised.

The writer must read the first sentences of a run of repeated units together, then
their last sentences. If they share a shape, the units must be revised.

The writer must apply each repair as part of this review. The writer must not
report a defect without repairing it, and must not report the review as complete
until every repair has been applied and the repaired sentence has been re-read
against the rule it was repaired under.

A check that finds no defect has passed. The writer must not stretch to find
problems.

---

## Requirements Reference

**Reader fit.** The writer must match the reading level, define hard words on first
use, and use the shortest word that means the thing.

**Run-on sentences.** The writer must split any sentence the reader has to re-read
to find the verb, and must let the information set sentence length.

**Root metaphors.** A document is a structured reference. Information is present or
absent and does not move. The reader is an agent performing tasks. A document
element takes only these verbs: contains, lists, states, specifies, defines,
describes, includes, provides, records, identifies, documents.

**Personification.** The writer must not make non-living things act like people,
want, refuse, know, or carry moral qualities. The reader may be treated as an
agent.

**Reification.** The writer must not treat an abstraction as a thing that exists
and acts. A definition that states what a term means is not reification.

**The copular identity slogan.** The writer must not equate two related things with
"is" for memorability. State the relationship.

**Patient-verb agreement.** Every verb governed by one subject must accept that
subject's category. Information nouns take information verbs. Physical nouns take
work verbs.

**Modal ambiguity.** The writer must name who requires a requirement: a code, a
manufacturer, or the writer.

**The quotable-to-usable test.** The writer must rewrite a sentence that sounds
quotable until the reader can extract an action, a value, or a constraint from it.

**The two ways to fail.** The writer must check for decoration and for dryness.
Noun-phrase chains, abstract-noun stacks, and passages with no figures are the
dry-side defects.

**Specifics before style.** When a passage is flat, the repair is a number, a
name, a citation, or a measurement, never phrasing alone.

**Agents in passives.** The writer must name the actor in every passive sentence,
and that actor must be able to perform the action.

**Rhetorical decoration.** The writer must not write sentences that sound quotable
rather than informative.

**Gnomic truths.** The writer must not tell the reader what to think instead of
stating what happened.

**Admonitory declaratives.** The writer must not deliver a true fact in warning
cadence. State the definition and its consequence.

**Contrastive negation.** The writer must not deny what the text never asserted.
State what is there.

**Imported analogies.** The writer must not use unrelated comparisons. A simile is
allowed only when it fixes a property the reader can act on.

**Staged scenes.** The writer must not ask the reader to imagine instead of stating
what happened.

**Sound patterning.** The text must contain no alliteration, no rhyme, and no
sentences with a beat.

**AI cadence.** The text must contain no triads, no anaphora, no em-dash pivots, no
"not just X but Y," no fragments for emphasis, no closing reversals, and no
rhetorical questions.

**Hedges.** Claims must be stated directly. Frequency words must not stand in for
conditions.

**Unanchored comparatives.** "More," "less," and "faster" must have numbers or
referents.

**Evaluative adjectives.** An adjective must not replace the fact.

**Promotional language.** The writer must not sell the subject to the reader.

**Self-commentary.** The writer must not write sentences that state what the text
is doing.

**Semantic bleaching.** The writer must not replace a concrete referent with an
evaluative abstraction. Name the things.

**Register.** The voice must be constant, in both directions. No archaism. No joke,
wink, or sales line.

**Word size.** The text must contain no long word where a short word means the same
thing, and no nominalization.

**Punctuation.** The text must contain no em dashes and no semicolons.

**Claim anchoring.** Each factual claim must be traceable to evidence.

**Precision.** Each word must match the thing it names.

**Genre consistency.** The writer must keep each section in one mode.

**Information order.** The sequence must be clear, and evidence must sit beside the
claim it supports.

**Defined terms.** Each term must be used the same way throughout.

**Information density.** No sentence may be removable without loss.

**Specific agents.** The actors must be named where possible.

**Evidence quality.** Where the evidence is mixed, the writer must say so.

**Teaching point.** The writer must be able to finish "This teaches the reader that
___" for every block, and the point must arrive in the opening sentences.

**Withheld facts.** Nothing may be held back to create suspense.

**End when the information ends.** No summary that restates, no callback, no
closing line written to land.

**Action test.** In instructional writing, every sentence must instruct, inform, or
warn, and every risk passage must state what the reader does.

**Repeated units.** Parallel entries must open and close in different shapes.

**Self-reference.** Every requirement above applies to this guide.
