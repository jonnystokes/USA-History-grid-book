"""Give each reader-review group its own copy of the chapters it reads: build/review/<GROUP>.md.

Usage:  python tools/review_extract.py R01 R02 ...      (rebuilds build/history-book.md first)
        python tools/review_extract.py --all
        python tools/review_extract.py --list
        add --no-build to cut from the existing build/history-book.md

Why: the reader agents read one Markdown file with offset and limit. If the whole-book file were
rebuilt while one of them was reading it, every line number after a changed chapter would move
under the reader. A per-group copy never changes while its reader works.

Groups follow the book order (control/briefs/READER-REVIEW-DISPATCH.md): pairs of neighbouring
chapters up to about 50,000 words, big chapters alone. "front" is everything before Part 1 (title,
contents, introduction, front matter); "back" is everything after the last chapter.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "build" / "history-book.md"
OUT = ROOT / "build" / "review"

GROUPS = {
    "R01": ["front", 1], "R02": [2, 3], "R03": [4, 5], "R04": [6, 7], "R05": [8, 9],
    "R06": [10, 11], "R07": [12, 13], "R08": [14, 15], "R09": [16, 17], "R10": [18, 19],
    "R11": [20], "R12": [21], "R13": [22, 23], "R14": [24], "R15": [25], "R16": [26, 27],
    "R17": [28], "R18": [29], "R19": [30], "R20": [31], "R21": [32], "R22": [33],
    "R23": [34, 35], "R24": [36, 37], "R25": ["back"],
}


def sections(lines):
    """Map 'front', 'back' and each chapter number to its (start, end) line range."""
    chap = [(i, int(m.group(1))) for i, l in enumerate(lines)
            if (m := re.match(r"^## Chapter (\d+): ", l))]
    part1 = next(i for i, l in enumerate(lines) if l.startswith("# Part 1:"))
    last = chap[-1][0]
    back = next(i for i in range(last + 1, len(lines))
                if lines[i].startswith("# ") and not lines[i].startswith("# Part "))
    out = {"front": (0, part1), "back": (back, len(lines))}
    for k, (i, n) in enumerate(chap):
        end = chap[k + 1][0] if k + 1 < len(chap) else back
        # a chapter ends where the next one (or the next part heading) starts
        for j in range(i + 1, end):
            if lines[j].startswith("# Part "):
                end = j
                break
        out[n] = (i, end)
    return out


def main(argv):
    if "--list" in argv:
        for g, items in GROUPS.items():
            print(g, items)
        return
    names = list(GROUPS) if "--all" in argv else [a for a in argv if a in GROUPS]
    bad = [a for a in argv if not a.startswith("--") and a not in GROUPS]
    if bad or not names:
        sys.exit(f"unknown or missing group: {bad or 'none given'} (see --list)")
    if "--no-build" not in argv:
        subprocess.run([sys.executable, str(ROOT / "tools" / "build_full_book_md.py")], check=True,
                       capture_output=True)
    lines = BOOK.read_text(encoding="utf-8").split("\n")
    sec = sections(lines)
    OUT.mkdir(parents=True, exist_ok=True)
    for g in names:
        body = []
        for item in GROUPS[g]:
            a, b = sec[item]
            body += lines[a:b] + [""]
        path = OUT / f"{g}.md"
        path.write_text("\n".join(body), encoding="utf-8")
        words = sum(len(l.split()) for l in body)
        print(f"{g}: {path.relative_to(ROOT)}  {len(body)} lines, {words:,} words  {GROUPS[g]}")


if __name__ == "__main__":
    main(sys.argv[1:])
