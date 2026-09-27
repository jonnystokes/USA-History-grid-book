#!/usr/bin/env python3
"""Print only the eras a sub-agent needs from a chapter's outline and research bank.

    python tools/slice_bank.py <slug> --eras 6-7              # outline slice + bank slice
    python tools/slice_bank.py <slug> --eras 1-5 -o out.md    # write to a file instead
    python tools/slice_bank.py <slug> --eras 8-10 --summary   # sections, eras, word counts only
    python tools/slice_bank.py <slug> --eras 9 --bank-only    # (or --outline-only)
    python tools/slice_bank.py <slug> --eras 6-7 --no-untagged

Why (2026-09-26): writers were told to "grep the bank for your eras". That costs reading
and misses material: many banks keep "Parked from <chapter>" sections at the end, with
their own era sub-headings, which a grep for "## 06" never finds. This tool reads every
heading style the banks actually use and keeps each section whose era overlaps the request.

NOTHING IS SILENTLY DROPPED. A section the tool cannot place in an era (a "Disputes" log,
a parked note with no era, a "Sources used" list) is printed under UNTAGGED, unless you
pass --no-untagged. The summary line at the top says how many words were left out.

Outline: the hb-chapter line and hb-note before the first era always print, then each
hb-time block whose order= is requested.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Era bounds, [start, end). Era 1 is everything before 1500, era 10 is 2000 on.
BOUNDS = {1: (-10**6, 1500), 2: (1500, 1600), 3: (1600, 1700), 4: (1700, 1750),
          5: (1750, 1800), 6: (1800, 1850), 7: (1850, 1900), 8: (1900, 1950),
          9: (1950, 2000), 10: (2000, 10**6)}

DASH = r"\s*(?:to|through|-|–|—)\s*"

# Era titles, the strong signal. Checked against the heading text.
TITLE_PATTERNS = [
    (re.compile(r"\bbefore\s+(?:the\s+)?1500", re.I), {1}),
    (re.compile(r"\b1490s\b.*\b1500s\b", re.I), {2}),
    (re.compile(r"\b1700" + DASH + r"1750\b", re.I), {4}),
    (re.compile(r"\b1750" + DASH + r"1800\b", re.I), {5}),
    (re.compile(r"\b1800" + DASH + r"1850\b", re.I), {6}),
    (re.compile(r"\b1850" + DASH + r"1900\b", re.I), {7}),
    (re.compile(r"\b1900" + DASH + r"1950\b", re.I), {8}),
    (re.compile(r"\b1950" + DASH + r"2000\b", re.I), {9}),
    (re.compile(r"\b2000" + DASH + r"(?:today|now|present|20\d\d)\b", re.I), {10}),
]
# "The 1600s", "1800s", "1500s-1700s". A century heading covers every era inside it.
CENTURY = {15: {2}, 16: {3}, 17: {4, 5}, 18: {6, 7}, 19: {8, 9}, 20: {10}}
CENTURY_SPAN = re.compile(r"\b(1[5-9]|20)00s" + DASH + r"(?:the\s+)?(1[5-9]|20)00s\b", re.I)
CENTURY_ONE = re.compile(r"\b(1[5-9]|20)00s\b", re.I)
ERA_WORD = re.compile(r"\bera\s*0?(\d{1,2})\b(?!\s*[-–]\s*\d)", re.I)          # "Era 08", "(era 3)"
ERA_RANGE = re.compile(r"\beras?\s*0?(\d{1,2})" + DASH.replace("through", "through|and")
                       + r"0?(\d{1,2})\b", re.I)                                 # "Eras 1-5", "eras 7 and 8"
LEAD_NUM = re.compile(r"^\s*0?(\d{1,2})\s*[.·]?\s+\S")                          # "## 06 · 1800", "### 8. 1900"
YEAR_RANGE = re.compile(r"\b(1[4-9]\d\d|20\d\d)\s*[-–]\s*(1[4-9]\d\d|20\d\d)\b")


def eras_for_range(a, b):
    return {e for e, (lo, hi) in BOUNDS.items() if a < hi and b >= lo}


def strong_eras(text):
    """Eras stated by an era title or an explicit 'Era N'. None if no strong signal."""
    m = ERA_RANGE.search(text)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        if 1 <= a <= b <= 10:
            return set(range(a, b + 1))
    m = ERA_WORD.search(text)
    if m and 1 <= int(m.group(1)) <= 10:
        return {int(m.group(1))}
    for pat, eras in TITLE_PATTERNS:
        if pat.search(text):
            return set(eras)
    m = CENTURY_SPAN.search(text)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        return set().union(*(CENTURY[c] for c in range(a, b + 1) if c in CENTURY))
    m = CENTURY_ONE.search(text)
    if m:
        return set(CENTURY[int(m.group(1))])
    return None


def weak_eras(text):
    """A bare year range ("1900-1940") or a leading era number. Used only when the parent
    heading has no era, because inside an era a range is usually a lifespan."""
    m = YEAR_RANGE.search(text)
    if m:
        return eras_for_range(int(m.group(1)), int(m.group(2)))
    m = LEAD_NUM.match(text)
    if m and 1 <= int(m.group(1)) <= 10:
        return {int(m.group(1))}
    return None


def parse_eras_arg(s):
    out = set()
    for part in s.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            out.update(range(int(a), int(b) + 1))
        elif part:
            out.add(int(part))
    bad = [e for e in out if not 1 <= e <= 10]
    if bad or not out:
        sys.exit(f"--eras must name eras 1 to 10, e.g. 6-7 or 1,3,5 (got {s!r})")
    return out


def bank_sections(lines):
    """Split a bank into sections at every heading. Each gets the eras it belongs to."""
    heading = re.compile(r"^(#{1,6})\s+(.*)$")
    stack = []            # (level, eras or None)
    sections = []         # dicts: title, level, eras, lines
    cur = {"title": "(text before the first heading)", "level": 0, "eras": None, "lines": []}
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        m = None if in_fence else heading.match(line)
        if m:
            sections.append(cur)
            level, text = len(m.group(1)), m.group(2)
            while stack and stack[-1][0] >= level:
                stack.pop()
            parent = next((e for _, e in reversed(stack) if e is not None), None)
            eras = strong_eras(text)
            if parent is not None:
                # Inside a dated section a heading may only NARROW the eras ("## 1. Before
                # 1500" under "# PART A, Eras 1-5"). If it names eras outside its parent
                # ("### What the 1700s left behind" under 1800-1850), keep both, so a
                # section never drops out of the era it is filed under.
                if eras is None:
                    eras = parent
                elif not eras <= parent:
                    eras = eras | parent
            elif eras is None:
                eras = weak_eras(text)
            stack.append((level, eras))
            cur = {"title": text.strip(), "level": level, "eras": eras, "lines": [line]}
        else:
            cur["lines"].append(line)
    sections.append(cur)
    return [s for s in sections if "".join(s["lines"]).strip()]


def outline_blocks(lines):
    """(order or None, lines). None = the chapter header and notes before the first era."""
    start = re.compile(r'<!--\s*hb-time:start\b[^>]*\border="0?(\d{1,2})"')
    end = re.compile(r"<!--\s*hb-time:end\b")
    blocks, cur, order = [], [], None
    for line in lines:
        m = start.search(line)
        if m:
            if cur:
                blocks.append((order, cur))
            cur, order = [line], int(m.group(1))
            continue
        cur.append(line)
        if end.search(line):
            blocks.append((order, cur))
            cur, order = [], "between"
    if cur:
        blocks.append((order, cur))
    return blocks


def words(lines):
    return sum(len(l.split()) for l in lines)


def label(eras):
    return "untagged" if eras is None else "eras " + ",".join(str(e) for e in sorted(eras))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--eras", required=True, help="e.g. 6-7, 8-10, or 1,3,5")
    ap.add_argument("--bank-only", action="store_true")
    ap.add_argument("--outline-only", action="store_true")
    ap.add_argument("--no-untagged", action="store_true", help="leave out sections with no era")
    ap.add_argument("--summary", action="store_true", help="list sections and word counts only")
    ap.add_argument("-o", "--out", help="write here instead of printing")
    a = ap.parse_args()
    want = parse_eras_arg(a.eras)
    tag = f"eras {a.eras}"

    out = []
    notes = []

    if not a.bank_only:
        path = os.path.join(ROOT, "outlines", f"{a.slug}.md")
        if not os.path.exists(path):
            sys.exit(f"no outline at {path}")
        with open(path, encoding="utf-8") as f:
            olines = f.read().splitlines(keepends=True)
        blocks = outline_blocks(olines)
        kept = [(o, b) for o, b in blocks if o is None or o == "between" or o in want]
        # Drop blank separators between eras that were not kept.
        kept = [(o, b) for o, b in kept if o not in ("between",) or "".join(b).strip()]
        kw, tw = sum(words(b) for _, b in kept), words(olines)
        notes.append(f"OUTLINE outlines/{a.slug}.md, {tag}: {kw} of {tw} words")
        if a.summary:
            for o, b in blocks:
                mark = "KEEP" if (o is None or o == "between" or o in want) else "    "
                name = "header + notes" if o is None else ("(between eras)" if o == "between" else f"era {o:02d}")
                out.append(f"  {mark} outline {name:<16} {words(b):>6}w\n")
        else:
            out.append(f"\n<!-- ===== SLICE: outlines/{a.slug}.md, {tag} ===== -->\n")
            for _, b in kept:
                out.extend(b)

    if not a.outline_only:
        path = os.path.join(ROOT, "research", f"research-{a.slug}.md")
        if not os.path.exists(path):
            sys.exit(f"no bank at {path}")
        with open(path, encoding="utf-8") as f:
            blines = f.read().splitlines(keepends=True)
        secs = bank_sections(blines)
        match = [s for s in secs if s["eras"] is not None and s["eras"] & want]
        untagged = [s for s in secs if s["eras"] is None]
        other = [s for s in secs if s["eras"] is not None and not s["eras"] & want]
        mw, uw, ow = (sum(words(s["lines"]) for s in g) for g in (match, untagged, other))
        notes.append(f"BANK research/research-{a.slug}.md, {tag}: {mw} words matched, "
                     f"{uw} untagged ({'left out' if a.no_untagged else 'included'}), "
                     f"{ow} in other eras left out, of {words(blines)}")
        if a.summary:
            for s in secs:
                keep = s in match or (s in untagged and not a.no_untagged)
                out.append(f"  {'KEEP' if keep else '    '} {label(s['eras']):<16} {words(s['lines']):>6}w  "
                           f"{'#' * s['level']} {s['title'][:90]}\n")
        else:
            out.append(f"\n<!-- ===== SLICE: research/research-{a.slug}.md, {tag} ===== -->\n")
            for s in secs:
                if s in match:
                    out.extend(s["lines"])
            if untagged and not a.no_untagged:
                out.append(f"\n<!-- ===== UNTAGGED sections of the bank (no era could be read from the "
                           f"heading). Check them for material on your eras. ===== -->\n")
                for s in untagged:
                    out.extend(s["lines"])

    head = "".join(f"<!-- {n} -->\n" for n in notes)
    text = head + "".join(out)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(head, end="")
        print(f"wrote {a.out}")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
