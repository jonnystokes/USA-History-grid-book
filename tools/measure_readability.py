"""Readability measurements, a first indicator only (DECISIONS #53: reading decides).

Usage:  python tools/measure_readability.py [slug ...]        (default: all 37 + the introduction)
Prints one row per chapter and a book total. Counts only prose inside blocks (hb-note blocks and
marker lines are skipped). Nothing here is a gate.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAN = ROOT / "manuscript"

MARK = re.compile(r"^\s*<!--\s*/?hb-")
NOTE_START = re.compile(r"^\s*<!--\s*hb-note")
NOTE_END = re.compile(r"^\s*<!--\s*/hb-note")
TIME_START = re.compile(r'<!--\s*hb-time:start[^>]*id="([^"]+)"')
STORY_START = re.compile(r"<!--\s*hb-story:start")
STORY_END = re.compile(r"<!--\s*hb-story:end")
DATE_FIRST = re.compile(r"^(In|On|By|From|During|Between|After|Before)\s+(the\s+)?(\d{3,4}|[A-Z][a-z]+\s+\d{1,2},?\s+\d{4}|\d{1,2}\s+[A-Z][a-z]+\s+\d{4})")
DEF = re.compile(r"\b(means|is called|are called|is a word for|, which means|, a word)\b")
ATTR = re.compile(r"\b(says|said|states|stated|reports|reported|writes|wrote|according to)\b")
ALSO = re.compile(r"\balso\b")
YOU = re.compile(r"\byou\b|\byour\b", re.I)
SENT = re.compile(r"[.!?](\s|$)")


def paragraphs(text):
    paras, cur, in_note = [], [], False
    for line in text.splitlines():
        if NOTE_START.match(line):
            in_note = True
            continue
        if NOTE_END.match(line):
            in_note = False
            continue
        if in_note or MARK.match(line) or line.startswith("#") or line.startswith(">"):
            if cur:
                paras.append(" ".join(cur)); cur = []
            continue
        if not line.strip():
            if cur:
                paras.append(" ".join(cur)); cur = []
            continue
        cur.append(line.strip())
    if cur:
        paras.append(" ".join(cur))
    return paras


def era_sizes(text):
    sizes, cur, in_note, cur_id = {}, 0, False, None
    for line in text.splitlines():
        m = TIME_START.search(line)
        if m:
            cur_id = m.group(1); sizes[cur_id] = 0; continue
        if NOTE_START.match(line): in_note = True; continue
        if NOTE_END.match(line): in_note = False; continue
        if in_note or MARK.match(line) or cur_id is None:
            continue
        sizes[cur_id] += len(line.split())
    return sizes


def story_sizes(text):
    sizes, cur, in_story = [], 0, False
    for line in text.splitlines():
        if STORY_START.search(line): in_story, cur = True, 0; continue
        if STORY_END.search(line): in_story = False; sizes.append(cur); continue
        if in_story and not MARK.match(line):
            cur += len(line.split())
    return sizes


def measure(files):
    text = "\n\n".join(p.read_text(encoding="utf-8", errors="replace") for p in files)
    paras = paragraphs(text)
    words = sum(len(p.split()) for p in paras)
    n = max(len(paras), 1)
    k = max(words, 1) / 1000
    eras = era_sizes(text)
    stories = story_sizes(text)
    return {
        "words": words,
        "paras": len(paras),
        "avg_para": words / n,
        "over90": sum(1 for p in paras if len(p.split()) > 90),
        "date_first%": 100 * sum(1 for p in paras if DATE_FIRST.match(p)) / n,
        "def/1k": len(DEF.findall(text)) / k,
        "attr/1k": len(ATTR.findall(text)) / k,
        "also/1k": len(ALSO.findall(text)) / k,
        "you": len(YOU.findall(text)),
        "longest_era": max(eras.values()) if eras else 0,
        "eras>4000": sum(1 for v in eras.values() if v > 4000),
        "stories": len(stories),
        "story_med": sorted(stories)[len(stories) // 2] if stories else 0,
        "stories>400": sum(1 for s in stories if s > 400),
    }


def main(argv):
    slugs = argv or sorted(d.name for d in MAN.iterdir() if d.is_dir())
    cols = ["words", "paras", "avg_para", "over90", "date_first%", "def/1k", "attr/1k", "also/1k", "you",
            "longest_era", "eras>4000", "stories", "story_med", "stories>400"]
    print(f"{'chapter':24}" + "".join(f"{c:>12}" for c in cols))
    tot = {c: 0 for c in cols}
    for slug in slugs:
        files = sorted((MAN / slug).glob("*.md"))
        if not files:
            continue
        m = measure(files)
        print(f"{slug:24}" + "".join(f"{m[c]:12.1f}" if isinstance(m[c], float) else f"{m[c]:12d}" for c in cols))
        for c in cols:
            if c in ("longest_era",):
                tot[c] = max(tot[c], m[c])
            else:
                tot[c] += m[c]
    print(f"{'TOTAL/MAX':24}" + "".join(f"{tot[c]:12.1f}" if isinstance(tot[c], float) else f"{tot[c]:12d}" for c in cols))
    print("(avg_para, date_first%, def/1k, attr/1k, also/1k totals are sums across chapters: divide by chapter count)")


if __name__ == "__main__":
    main(sys.argv[1:])
