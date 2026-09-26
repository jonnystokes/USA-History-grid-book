#!/usr/bin/env python3
"""bank_coverage.py: how many of a file's numbers can be found in its research bank?

    python tools/bank_coverage.py <slug>              # outline vs bank
    python tools/bank_coverage.py <slug> --prose      # manuscript vs bank
    python tools/bank_coverage.py --all               # every chapter's outline, one line each
    python tools/bank_coverage.py <slug> --list       # also print the missing numbers in context

Added 2026-09-26 after the city-building v2 revision found about 78 prose claims that
its research bank does not contain. The earlier writer took them from the outline's inline
notes. This is a CHEAP PROBE, NOT A GATE. It checks only numbers (years, counts, amounts,
percentages), because a number is the one kind of claim a machine can look up literally. A
number missing from the bank is a lead to read, not proof of an unsourced claim. A number
present in the bank does not prove the sentence around it is sourced. It is a REPORT only
and gates nothing.

FIRST RESULT (2026-09-26), which limits what this tool can do: city-building's outline numbers
are 97% in the bank and its prose numbers are 99%. Yet the revision agents found about 78 prose
claims the bank lacks. Those claims were qualitative ("Otis stood on the platform", "the
sewers had no pumps"), and number matching cannot see them. So this probe detects a thin
bank (the seed chapters score 16-40%). It does NOT detect the city-building failure. Only a
reader comparing sentences to the bank can do that.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from project_state import RE_MARK, all_slugs  # noqa: E402

RE_NUM = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)(?![\w])")
SMALL = 12  # numbers 0..12 are too common to mean anything


def reader_lines(text):
    """Lines a reader would see: skips markers, hb-note blocks, comments and headings."""
    in_note = False
    for no, line in enumerate(text.split("\n"), 1):
        m = RE_MARK.match(line)
        if m:
            if m.group(2) == "hb-note":
                in_note = not m.group(1)
            continue
        s = line.strip()
        if in_note or not s or s.startswith("<!--") or s.startswith("#"):
            continue
        yield no, s


def numbers(s):
    out = []
    for tok in RE_NUM.findall(s):
        v = tok.replace(",", "")
        try:
            if float(v) <= SMALL:
                continue
        except ValueError:
            continue
        out.append(v)
    return out


def bank_numbers(slug):
    p = os.path.join(ROOT, "research", "research-%s.md" % slug)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return {t.replace(",", "") for t in RE_NUM.findall(f.read())}


def coverage(slug, prose=False):
    bank = bank_numbers(slug)
    if bank is None:
        return None
    if prose:
        d = os.path.join(ROOT, "manuscript", slug)
        files = [os.path.join(d, x) for x in sorted(os.listdir(d)) if x.endswith(".md")] if os.path.isdir(d) else []
    else:
        files = [os.path.join(ROOT, "outlines", slug + ".md")]
    total, missing = 0, []
    for fp in files:
        with open(fp, encoding="utf-8") as f:
            text = f.read()
        for no, s in reader_lines(text):
            for n in numbers(s):
                total += 1
                if n not in bank:
                    missing.append((os.path.relpath(fp, ROOT), no, n, s))
    return total, missing


def main():
    args = sys.argv[1:]
    prose = "--prose" in args
    if "--all" in args or not args:
        print("%-24s %6s %7s %6s" % ("slug", "nums", "missing", "found%"))
        for slug in all_slugs():
            r = coverage(slug, prose)
            if r is None:
                print("%-24s   (no bank)" % slug)
                continue
            total, missing = r
            pct = 100.0 * (total - len(missing)) / total if total else 100.0
            print("%-24s %6d %7d %5.0f%%" % (slug, total, len(missing), pct))
        return 0
    slug = args[0]
    r = coverage(slug, prose)
    if r is None:
        print("no bank for %s" % slug)
        return 2
    total, missing = r
    pct = 100.0 * (total - len(missing)) / total if total else 100.0
    print("%s (%s): %d numbers, %d not found in the bank, %.0f%% found"
          % (slug, "manuscript" if prose else "outline", total, len(missing), pct))
    if "--list" in args:
        for fp, no, n, s in missing:
            i = s.find(n[:4])
            print("  %s:%d  %s   ...%s..." % (fp, no, n, s[max(0, i - 50):i + 50]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
