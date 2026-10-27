#!/usr/bin/env python3
"""Assemble the back matter from the writers' hand-off files (ARCHITECTURE-GUIDE 6).

Reads control/backmatter/<slug>.md (one per chapter, six ## sections written by the readability
writers: Glossary, People, Dates, Places, Movies, Questions) in chapter order and writes:

  manuscript/_backmatter/02-glossary.md   every explained word, A to Z, chapter of first use
  manuscript/_backmatter/03-timeline.md   the dates, oldest first, grouped by the ten eras
  manuscript/_backmatter/04-people.md     every story subject, by last name, chapter and era
  manuscript/_backmatter/05-places.md     places to see, by state
  manuscript/_backmatter/06-movies.md     the movie list with accuracy notes
  manuscript/_backmatter/07-answers.md    the three questions of every chapter, answered

This is the mechanical first draft. An editor pass then merges duplicate glossary words, trims
the timeline to about 150 dates and checks every line against its chapter.

Usage:  python tools/build_backmatter.py [--draft-dir DIR]
  --draft-dir  write the six files to DIR instead of manuscript/_backmatter (for a look first)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_full_book as B  # noqa: E402

HAND = ROOT / "control" / "backmatter"
SECTIONS = ("Glossary", "People", "Dates", "Places", "Movies", "Questions")
ERAS = [(-10**9, 1499, "Before 1500"), (1500, 1599, "The 1500s"), (1600, 1699, "The 1600s"),
        (1700, 1749, "1700 to 1750"), (1750, 1799, "1750 to 1800"), (1800, 1849, "1800 to 1850"),
        (1850, 1899, "1850 to 1900"), (1900, 1949, "1900 to 1950"), (1950, 1999, "1950 to 2000"),
        (2000, 10**9, "2000 to today")]
MONTHS = {m: i for i, m in enumerate(
    "january february march april may june july august september october november december".split(), 1)}
warnings = []


def read_hand(slug):
    p = HAND / f"{slug}.md"
    if not p.exists():
        return None
    out, cur = {k: [] for k in SECTIONS}, None
    for line in p.read_text(encoding="utf-8").splitlines():
        h = re.match(r"^##\s+(.+?)\s*$", line)
        if h:
            cur = h.group(1).strip().title()
            if cur not in out:
                warnings.append(f"{slug}: unknown section {cur!r}")
                cur = None
            continue
        m = re.match(r"^\s*[-*]\s+(.*\S)\s*$", line)
        if m and cur:
            out[cur].append(m.group(1))
        elif line.strip() and cur and out[cur]:
            out[cur][-1] += " " + line.strip()      # a wrapped bullet
    return out


def split_item(s):
    """'key: rest', split on the first colon followed by a space (a time like 9:30 has none)."""
    k, _, rest = s.partition(": ")
    return k.strip(), rest.strip()


def trailing_paren(s):
    m = re.match(r"^(.*?)\s*\(([^()]*)\)\s*$", s)
    return (m.group(1).strip(), m.group(2).strip()) if m else (s.strip(), "")


def year_key(d):
    """Sort key (year, month, day) for a date as the chapters write it."""
    low = d.lower()
    m = re.search(r"([\d,]+)\s*years ago", low)
    if m:
        return (2026 - int(m.group(1).replace(",", "")), 0, 0)
    m = re.search(r"(\d{1,5})\s*(bce|bc)\b", low)
    if m:
        return (-int(m.group(1)), 0, 0)
    m = re.search(r"\b(\d{3,4})s?\b", low)
    if not m:
        return None
    y = int(m.group(1))
    mon = next((v for k, v in MONTHS.items() if k in low), 0)
    day = re.search(rf"\b{list(MONTHS)[mon - 1]}\s+(\d{{1,2}})\b", low) if mon else None
    return (y, mon, int(day.group(1)) if day else 0)


def chap_ref(c):
    return f'Chapter {int(c["num"])}'


def main():
    draft = Path(sys.argv[sys.argv.index("--draft-dir") + 1]) if "--draft-dir" in sys.argv else \
        ROOT / "manuscript" / "_backmatter"
    draft.mkdir(parents=True, exist_ok=True)
    chapters, _ = B.read_registry()
    gloss, people, dates, places, movies, answers = {}, [], [], {}, [], []
    missing = []
    for c in chapters:
        h = read_hand(c["slug"])
        if h is None:
            missing.append(c["slug"])
            continue
        ref = chap_ref(c)
        for it in h["Glossary"]:
            term, rest = split_item(it)
            expl, _era = trailing_paren(rest)
            g = gloss.setdefault(term.lower(), {"term": term, "expl": expl, "chs": []})
            if ref not in g["chs"]:
                g["chs"].append(ref)
        for it in h["People"]:
            name, rest = split_item(it)
            role, era = trailing_paren(rest)
            people.append((name, role, ref, era, c["title"]))
        for i, it in enumerate(h["Dates"]):
            d, ev = split_item(it)
            k = year_key(d)
            if k is None:
                warnings.append(f'{c["slug"]}: cannot read the date in {it!r}')
                continue
            dates.append((k, d, ev, ref, i < 5))
        for it in h["Places"]:
            place, what = split_item(it)
            parts = [p.strip() for p in place.split(",")]
            state = parts[-1] if len(parts) >= 3 else "Other places"
            places.setdefault(state, []).append((", ".join(parts[:-1]) if len(parts) >= 3 else place, what, ref))
        for it in h["Movies"]:
            title, note = split_item(it)
            movies.append((title, note, ref))
        qs = []
        for it in h["Questions"]:
            m = re.match(r"^Q:\s*(.*?)\s+A:\s*(.*)$", it)
            if m:
                qs.append(m.groups())
            else:
                warnings.append(f'{c["slug"]}: question line without "Q: ... A:" {it[:60]!r}')
        answers.append((c, qs))

    files = {}
    # glossary
    lines = ["# Glossary", "",
             "Every hard word the chapters explain, from A to Z, with the chapter where it first appears.", ""]
    letter = None
    for key in sorted(gloss, key=lambda k: re.sub(r"[^a-z0-9 ]", "", k)):
        g = gloss[key]
        first = re.sub(r"[^A-Za-z]", "", g["term"])[:1].upper() or "#"
        if first != letter:
            letter = first
            lines += ["", f"## {letter}", ""]
        more = f', also {", ".join(g["chs"][1:])}' if len(g["chs"]) > 1 else ""
        lines.append(f'- **{g["term"]}**: {g["expl"]} ({g["chs"][0]}{more})')
    files["02-glossary.md"] = lines
    # timeline: the five closing dates of every chapter, then the rest, oldest first
    lines = ["# Timeline", "",
             "The dates the chapters lean on, oldest first. Each line names the chapter that tells the story.", ""]
    seen, era = set(), None
    for k, d, ev, ref, key5 in sorted(dates, key=lambda x: (x[0], not x[4])):
        sig = (k, ev.lower()[:40])
        if sig in seen:
            continue
        seen.add(sig)
        name = next(n for lo, hi, n in ERAS if lo <= k[0] <= hi)
        if name != era:
            era = name
            lines += ["", f"## {era}", ""]
        lines.append(f"- **{d}**: {ev} ({ref})")
    files["03-timeline.md"] = lines
    # people, by last name
    def surname(n):
        n = re.sub(r"\(.*?\)|\".*?\"", "", n).strip()
        bits = [b for b in n.split() if b.lower() not in ("jr.", "sr.", "ii", "iii", "jr", "sr")]
        return (bits[-1] if bits else n).lower()
    lines = ["# People", "",
             "Everyone who has a story box in this book, by last name, with the chapter and era to find them.", ""]
    letter = None
    for name, role, ref, era, _t in sorted(people, key=lambda p: (surname(p[0]), p[0])):
        first = surname(name)[:1].upper()
        if first != letter:
            letter = first
            lines += ["", f"## {letter}", ""]
        where = f"{ref}, {era}" if era else ref
        lines.append(f"- **{name}**: {role} ({where})")
    files["04-people.md"] = lines
    # places
    lines = ["# Places to See", "",
             "Museums, sites and archives the chapters name, where you can see the real thing. Grouped by state.", ""]
    for state in sorted(places, key=lambda s: (s == "Other places", s)):
        lines += ["", f"## {state}", ""]
        for place, what, ref in sorted(places[state]):
            lines.append(f"- **{place}**: {what} ({ref})")
    files["05-places.md"] = lines
    # movies
    lines = ["# Movies", "",
             "Every movie the story boxes mention, with what the box says about how true it is.", ""]
    for title, note, ref in sorted(movies, key=lambda m: re.sub(r"^(the|a|an)\s+", "", m[0].lower())):
        lines.append(f"- **{title}**: {note} ({ref})")
    files["06-movies.md"] = lines
    # answers
    lines = ["# Answers to the Chapter Questions", "",
             "Each chapter opens with three questions. Here they are with their answers, chapter by chapter.", ""]
    for c, qs in answers:
        lines += ["", f'## Chapter {int(c["num"])}: {c["title"]}', ""]
        for q, a in qs:
            lines.append(f"- **{q}** {a}")
    files["07-answers.md"] = lines

    for name, ls in files.items():
        (draft / name).write_text("\n".join(ls).replace("\n\n\n", "\n\n") + "\n", encoding="utf-8")
    print(f"wrote {len(files)} files to {draft}: glossary {len(gloss)}, dates {len(seen)}, "
          f"people {len(people)}, places {sum(len(v) for v in places.values())}, movies {len(movies)}, "
          f"questions {sum(len(q) for _, q in answers)}")
    if missing:
        print(f"MISSING hand-offs ({len(missing)}): {', '.join(missing)}")
    for w in warnings:
        print("  WARN", w)


if __name__ == "__main__":
    main()
