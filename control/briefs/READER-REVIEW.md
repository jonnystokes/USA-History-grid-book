# READER-REVIEW brief: read part of the finished book as its readers will (model: sonnet)

The dispatch gives you a GROUP name and a list of chapters (or the front and back matter). Read
them start to finish, in book order, in `build/review/<GROUP>.md`: your chapters only, cut from the
whole book for you. Read it with offset and limit, about 300 lines at a time, from the first line to
the last, skipping nothing. You are a reader, not an editor: you change nothing in the manuscript.

## Who reads this book

A plain-language history of the United States for readers aged 8 to 15, and for any adult who
wants the whole story told straight. Many readers have ADHD or find long reading hard: they lose
the thread in long paragraphs, skip walls of dates, need to know early why a section matters,
and come back after a break needing to find their place. Some read one subject start to finish;
some read one era across all 37 subjects; some open a chapter at random. The book tells hard
history without softening it (rape, not assault; who did it, by name). That is policy, not a
flaw: never report plain words about violence as a problem.

How the book is built, so you can judge it: every chapter opens with a card (a one-line spine,
three questions, "Five minutes?", "Can skip"), each era opens with a strip
(`Era 6 of 10 · 1800 to 1850 · about 9 minutes`), long eras carry "By 1830, ..." lines, story
boxes about named people open with a hook, and each chapter closes by answering its three
questions. A narrator speaks in the furniture (cards, strips, closers), not in the history itself.

## What to look for

Read for flow, the way a 12-year-old with ADHD would meet it. Note only what would make a reader
stop, get lost, get bored or get the wrong idea:

- a paragraph that is hard to follow, too long, or carries three ideas;
- a passage that reads as a list of dates or names with nothing holding them together;
- a hard word used without a plain explanation the first time in the chapter;
- a jump with no bridge (a new era, person or idea that arrives from nowhere);
- the same fact or story told twice close together, or a chapter repeating another's opening;
- a card, strip, closer or closing that does not match what the chapter actually does (a
  question the closing never answers, a "five minutes" span that is not there);
- a sentence that sounds performed rather than explained (a triad, a dramatic fragment, a
  rhetorical question, "not just X but Y", a closing twist);
- anything that reads as wrong, contradictory or confusing next to another chapter you read.

Do not report: style preferences, words you would choose differently, the length of the book,
plain words about hard subjects, or anything you cannot point to.

## Output

Write `control/review/<GROUP>.md` (create the folder if missing). One `## Chapter N: Title`
section per chapter. Under it, at most 25 findings, worst first, each one bullet:

`- [era label] "first six words of the passage" : what goes wrong for the reader : the fix you suggest`

Then one line per chapter: `Flow: good | uneven | hard` and one sentence why. Quote at most six
words of the book per finding; never paste paragraphs. Report to the director in under 150
words: the file path, findings per chapter, and the one problem you saw most.
