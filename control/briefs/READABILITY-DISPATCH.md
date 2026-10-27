# READABILITY dispatch: the pilot wave (2026-10-26, DECISIONS #53)

Jon authorised as many agents at once as the work needs. Five run in the pilot wave, each owning
disjoint files. Each keeps a checkpoint and is resumed after a usage reset. The director reads the
results and Jon reads the pilot chapters before the other 34 start.

## Rules for every task

- Your brief is `control/briefs/READABILITY.md` unless your section names another. Read its
  "Read first" list in full, in order, before touching any file.
- Edit only the files your section names, plus your own checkpoint. No git. No installs. No
  sub-agents. Scratch files go in your own folder of the scratchpad, named after your task.
- Checkpoint first; resume from it if it exists. Checks as the brief says. Pacing as the brief says.
- The style guides bind every sentence you add or change. Read the two or three sentences around
  each change and repair any rule break you notice there.
- Report as the brief says. Do not paste prose into the report.

---

## T-660: tools (build and front/back matter plumbing). Model: opus.

Files: `tools/build_full_book.py`, `tools/build_full_book_md.py`, `tools/validate_grid.js` only if
needed (prefer not), checkpoint `control/checkpoints/T-660-tools.md`. Read `ARCHITECTURE-GUIDE.md`
§4.1, §4.2, §6 and `VIEWER-CONTRACT.md` §2 first. No prose edits.

1. **Chapter opening and closing placement.** A zoom block with `label="Chapter opening"` that is
   the first block of era 1 renders under the chapter heading, before the first era heading. A zoom
   block with `label="Chapter closing"` that is the last block of era 10 renders after the last era.
   Both in the HTML and the Markdown builds. Any other block is unchanged.
2. **Front matter.** The build reads, in order, every `manuscript/_frontmatter/NN-*.md` file (NN =
   two digits) before the introduction, each as its own section with its `#` heading, and lists
   them in the contents. The introduction file `manuscript/_introduction/how-we-know.md` keeps its
   slot after them (T-664 is rewriting its content; its filename stays).
3. **Back matter.** The build reads every `manuscript/_backmatter/NN-*.md` after chapter 37, same
   treatment, listed in the contents. The folders may be empty or missing today: handle that.
4. **Reading times.** Optional, only if simple: when rendering a chapter, compute its word count and
   expose it so the contents line can carry "about N minutes" (words / 200, rounded to 5). If the
   writers already put the time in the opening block, the contents may read it from there instead.
   Do not spend long on this; the prose carries the times.
5. **Test** on the current manuscript: both builds run without new warnings, `book/` is NOT
   overwritten (write to `build/` only), and a diff of `build/history-book.md` against
   `book/history-book.md` shows only the intended differences (none, until writers land).
6. Report: what changed in each script, how the opening and closing are detected, and the test
   result. Do not run the PDF.

## T-661: exploration (chapter 1). Model: fable.

Brief `READABILITY.md`. Files `manuscript/exploration/part*.md`, checkpoint
`control/checkpoints/T-661-readability.md`. Known trouble spots from the director's and DeepSeek's
reads: the era 1 definitions in a row (obsidian, archaeologists, chert); "Sailing the coasts, 1497
to 1542" is four explorer biographies in a row; 35 story boxes, 14 over 400 words, median 355; the
longest era is 5,383 words; one paragraph in 3.5 opens with a date; the Lewis and Clark Movie line
recommends *The Far Horizons* (1955) with no warning that it invents a romance; Sacagawea's death
is told as "nobody knows" when the 1812 record is stronger (ARCHITECTURE-GUIDE §5.7).

## T-662: government-politics (chapter 20). Model: fable.

Brief `READABILITY.md`. Files `manuscript/government-politics/part*.md`, checkpoint
`control/checkpoints/T-662-readability.md`. Trouble spots: era 1 opens with three governments in
a row (Haudenosaunee, Pueblo, Cahokia); the Oñate paragraph (about 330 words, six ideas, four
"He ..." sentences in a row, seven numbers); part 3 is 13,389 words with a 4,608-word era;
attribution 8.7 per thousand words; the median story box is 568 words and 10 of 14 run over 400;
average paragraph 86 words, 120 over 90.

## T-663: holidays (chapter 37). Model: fable.

Brief `READABILITY.md`. Files `manuscript/holidays/part*.md`, checkpoint
`control/checkpoints/T-663-readability.md`. Trouble spots: era 1 is seven ceremonies in a row; the
first two eras define seven terms ("time immemorial", "fasted", "Mass", "friar", "perpetually",
"epidemic", "saint's feast day"); attribution 9.1 per thousand; the five towns claiming the first
Memorial Day are given equal weight (§5.7); 4 of 9 story boxes over 400 words.

## T-664: the introduction and front matter. Model: fable.

Brief: `READABILITY.md` for the rules, with this section replacing its "What you may touch" and
"Process". Files: `manuscript/_introduction/how-we-know.md` (rewrite in place; the filename stays),
new files under `manuscript/_frontmatter/` and `manuscript/_backmatter/` (create the folders),
checkpoint `control/checkpoints/T-664-frontmatter.md`. Read `ARCHITECTURE-GUIDE.md` §3 and §6
first, then the whole current introduction, then `control/chapter-registry.md` (the 37 chapters,
their parts, their angles) and the chapter heading lines of `book/history-book.md` (its contents
list, lines 1 to 85) so the front matter describes the real book.

1. **`manuscript/_introduction/how-we-know.md`** becomes the real introduction: under 300 words,
   one or two paragraphs, titled "How This Book Works". What the book is, how the grid works (37
   subjects, the same ten eras in every one, read a subject straight through or one era across all
   37), how to use the furniture (the card at the top of each chapter, the era strips with reading
   times, the "can skip" lists, the glossary at the back), and one sentence on where the facts come
   from. The narrator may say "you". No examples, no method essay.
2. **`manuscript/_frontmatter/01-before-you-start.md`** (about 150 words): the contract. The
   size, that order does not matter, that skipping is normal, what the bold lines and boxes are,
   what to do when a page feels heavy.
3. **`manuscript/_frontmatter/02-four-ways-to-read.md`** (about 300 words): the reading paths
   with honest times, computed from the real word counts (`python tools/measure_readability.py`
   gives chapter words; the book total is in `control/WORKLOG.md`'s last entry). A bullet list, not a
   table (the parser has no tables).
4. **`manuscript/_frontmatter/03-ten-minute-history.md`** (about 900 words): ten beats, one per
   era, about 90 words each, the through-line of the whole country in that era. Every fact must be
   in some chapter's bank; cite the chapter in your checkpoint, not in the prose. This is the one
   piece of real history you write: take it slowly and check every claim against a bank.
5. **`manuscript/_backmatter/01-how-we-know.md`**: the current introduction's method essay, moved
   here and cut to about 1,200 words. Keep the three kinds of uncertainty and the best three or four
   examples (John Punch 1640, Amelia Stewart Knight, Jane at Jamestown, the Hoover Dam count). Drop
   the examples the chapters already tell in full. Keep every fact you keep exact.
6. Checks: `python tools/project_state.py --punct <file>` 0/0 on every file. Plain Markdown, `#`
   title and `##` sections only, no markers. Report the word count of each file and the reading
   paths you computed.
