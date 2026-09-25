<!-- hb-chapter id="<NN>" slug="<slug>" title="<Title>" part="<P>" mode="prose" -->

# Chapter <NN>: <Title>

<!-- hb-note -->
**Angle:** <the one lens this chapter uses — from chapter-registry.md>
**Keep out:** <what belongs to neighbouring chapters, with slugs>
**Research bank:** `research/research-<slug>.md` · **Workspace:** `workspace/<slug>.md`
Editor's in-development note — not part of the final book; stripped by our build step.
<!-- /hb-note -->

<!-- ══ v3 PROSE TEMPLATE — rebuilt 2026-09-05. Copy to manuscript/<slug>/ and fill.
     Same markers as the outline; only the contents and three attributes change:
       mode="prose"  ·  every hb-time progress="written"  ·  every hb-story status="verified"

     WRITE: plain-language prose paragraphs for ages 8-15, per control/writing-style-guide.md
       (BINDING) and control/hard-subjects-policy.md (BINDING). Read both before writing.
     NO PERSONIFICATION (style guide 1.1): a law, act, treaty, school, agency, company or
       nation cannot do anything. Name the people who acted. This is the rule most often
       broken while FIXING a passive - "the child's hair was cut" repaired to "the school cut
       the child's hair" is still wrong; "staff cut the child's hair" is right.
     CLINICAL WORDS (policy 3b): sterilization, lobotomy, flogging, branding and the like must
       be defined in plain words at first use - what it is, what it did to the person, and by
       what method. If the record does not give the method, say that it does not.
       Blank line between paragraphs. Single newlines get joined into one paragraph.
     ALLOWED inside a block: paragraphs · **bold** · *italic* · [links](https://…) ·
       "> **Key:** value" records (hb-story ONLY) · "- " bullets (rare in prose).
     NEVER inside a block: headings · tables · code blocks · images · nested or numbered
       lists · raw HTML · any comment · [VERIFY] tags (they must all be resolved by now).
     GOTCHAS the validator cannot catch — see control/VIEWER-CONTRACT.md §3:
       · a record line inside an hb-zoom is silently thrown away — records live in stories
       · an unclosed hb-zoom/hb-story is never reported; its text vanishes
       · a repeated era id silently overwrites the earlier one
       · the movie="" attribute is never displayed; the "> **Movie:**" line is what shows
     CHECK: node tools/validate_grid.js <file>   (add --part if this file is ONE PART
       of a multi-file chapter, so the ten-era check does not fire).
       MID-WRITE, errors are normal and fine - a half-written file has open blocks and
       missing eras, and the validator is telling you the truth about it. Keep going.
       THE RUN THAT MATTERS IS YOUR LAST ONE: before you report, the file must
       validate at 0 errors.
       If an error remains at the end, either fix it or SAY IN YOUR REPORT what it is
       and why you left it. What is not acceptable is shipping an error unexamined -
       decide about it, and show your reasoning.
       The validator never runs the renderer, so a clean run is necessary and not
       sufficient. Then open the file in viewer/viewer.html (v2).
     Multi-file chapters: repeat the hb-chapter line in each file with its own file="partN",
       name the files part1-…, part2-… (they load in filename order), and never split one
       era across two files. Copy the ten id/order/label values EXACTLY from
       control/grid-markers.md §6. ══ -->

<!-- hb-time:start id="before-1500" order="01" chapter="<slug>" label="Before 1500" state="full" progress="written" -->
## Before 1500

<!-- hb-zoom level="era" -->
<The wide framing of the whole era, in finished prose. Two or three paragraphs that
set the scene honestly: what existed, what did not, who was here.>

<An empty era instead gets state="empty", this one era-zoom holding the honest sentence
about why there is nothing to tell, and no span and no story.>
<!-- /hb-zoom -->

<!-- hb-zoom level="span" label="<span label>" -->
<A shorter span inside the era — a decade, a movement, a place, a law. Give it a label.>
<!-- /hb-zoom -->

<!-- hb-story:start slug="<person-slug>-<chapter-slug>" name="<Name>" movie="" kind="ordinary" status="verified" -->
### <Name>

> **Who:** <one line> · **When and where:** <one line>
> **Movie:** <Real Title (Year)> ← this line ONLY when a real film exists, and then
> the movie attribute above must name it too. Never invent one.

<The story in full prose. A real, documented person. Every fact traceable to the
research bank. No invented dialogue, no invented feelings, no tidy endings that the
sources do not support.>
<!-- hb-story:end slug="<person-slug>-<chapter-slug>" -->

<!-- hb-zoom level="era" -->
<Optional: the narrator pulling back out after a story, before the next one. Blocks are
a flat sequence — never nest them.>
<!-- /hb-zoom -->
<!-- hb-time:end id="before-1500" -->

<!-- hb-time:start id="1500s" order="02" chapter="<slug>" label="The 1500s" state="full" progress="written" -->
## The 1500s
<!-- hb-zoom level="era" -->
<!-- /hb-zoom -->
<!-- hb-time:end id="1500s" -->

<!-- hb-time:start id="1600s" order="03" chapter="<slug>" label="The 1600s" state="full" progress="written" -->
## The 1600s
<!-- hb-zoom level="era" -->
<!-- /hb-zoom -->
<!-- hb-time:end id="1600s" -->

<!-- hb-time:start id="1700-1750" order="04" chapter="<slug>" label="1700 to 1750" state="full" progress="written" -->
## 1700 to 1750
<!-- hb-zoom level="era" -->
<!-- /hb-zoom -->
<!-- hb-time:end id="1700-1750" -->

<!-- hb-time:start id="1750-1800" order="05" chapter="<slug>" label="1750 to 1800" state="full" progress="written" -->
## 1750 to 1800
<!-- hb-zoom level="era" -->
<!-- /hb-zoom -->
<!-- hb-time:end id="1750-1800" -->

<!-- hb-time:start id="1800-1850" order="06" chapter="<slug>" label="1800 to 1850" state="full" progress="written" -->
## 1800 to 1850
<!-- hb-zoom level="era" -->
<!-- /hb-zoom -->
<!-- hb-time:end id="1800-1850" -->

<!-- hb-time:start id="1850-1900" order="07" chapter="<slug>" label="1850 to 1900" state="full" progress="written" -->
## 1850 to 1900
<!-- hb-zoom level="era" -->
<!-- /hb-zoom -->
<!-- hb-time:end id="1850-1900" -->

<!-- hb-time:start id="1900-1950" order="08" chapter="<slug>" label="1900 to 1950" state="full" progress="written" -->
## 1900 to 1950
<!-- hb-zoom level="era" -->
<!-- /hb-zoom -->
<!-- hb-time:end id="1900-1950" -->

<!-- hb-time:start id="1950-2000" order="09" chapter="<slug>" label="1950 to 2000" state="full" progress="written" -->
## 1950 to 2000
<!-- hb-zoom level="era" -->
<!-- /hb-zoom -->
<!-- hb-time:end id="1950-2000" -->

<!-- hb-time:start id="2000-today" order="10" chapter="<slug>" label="2000 to Today" state="full" progress="written" -->
## 2000 to Today
<!-- hb-zoom level="era" -->
<!-- /hb-zoom -->
<!-- hb-time:end id="2000-today" -->
