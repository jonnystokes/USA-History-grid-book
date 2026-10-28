"""Cut the glossary into letter-range files so several editors can work on it at once, and join them back.

Usage:  python tools/backmatter_chunks.py split [N]   (default 6) -> control/backmatter-work/glossary-K.md
        python tools/backmatter_chunks.py join        -> manuscript/_backmatter/02-glossary.md

split: reads manuscript/_backmatter/02-glossary.md (written by tools/build_backmatter.py), keeps its
title and introduction aside, and cuts the letter sections into N files of about equal entry counts,
always at a letter boundary, so every spelling of one word stays in one file. Each file starts with a
one-line note naming the letters it holds.
join: puts the title, the introduction and the edited files back together in order and removes the
work folder's glossary files.
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(os.environ.get("HB_ROOT") or Path(__file__).resolve().parent.parent)   # HB_ROOT: test copy
GLOSS = ROOT / "manuscript" / "_backmatter" / "02-glossary.md"
WORK = ROOT / "control" / "backmatter-work"
HEAD = WORK / "glossary-head.md"


def split(n):
    text = GLOSS.read_text(encoding="utf-8")
    parts = re.split(r"(?m)^(?=## )", text)
    head, sections = parts[0], parts[1:]
    counts = [len(re.findall(r"(?m)^- ", s)) for s in sections]
    total, target = sum(counts), sum(counts) / n
    WORK.mkdir(parents=True, exist_ok=True)
    HEAD.write_text(head, encoding="utf-8")
    # linear partition: cut the letter sections into n runs so that the largest run is as small as possible
    m = len(sections)
    n = min(n, m)
    pre = [0]
    for c in counts:
        pre.append(pre[-1] + c)
    INF = float("inf")
    best = [[INF] * (m + 1) for _ in range(n + 1)]
    cut = [[0] * (m + 1) for _ in range(n + 1)]
    best[0][0] = 0
    for k in range(1, n + 1):
        for j in range(1, m + 1):
            for i in range(k - 1, j):
                v = max(best[k - 1][i], pre[j] - pre[i])
                if v < best[k][j]:
                    best[k][j], cut[k][j] = v, i
    bounds, j = [], m
    for k in range(n, 0, -1):
        i = cut[k][j]
        bounds.append((i, j))
        j = i
    chunks = [sections[i:j] for i, j in reversed(bounds)]
    for k, ch in enumerate(chunks, 1):
        letters = [re.match(r"## (.+)", s).group(1).strip() for s in ch]
        entries = sum(len(re.findall(r"(?m)^- ", s)) for s in ch)
        note = f"<!-- glossary part {k} of {len(chunks)}: letters {letters[0]} to {letters[-1]}, {entries} entries -->\n\n"
        (WORK / f"glossary-{k}.md").write_text(note + "".join(ch), encoding="utf-8")
        print(f"glossary-{k}.md: {letters[0]}..{letters[-1]}, {entries} entries")
    print(f"total {total} entries in {len(chunks)} files")


def join():
    files = sorted(WORK.glob("glossary-[0-9]*.md"), key=lambda p: int(re.search(r"(\d+)", p.stem).group(1)))
    body = []
    for f in files:
        t = f.read_text(encoding="utf-8")
        t = re.sub(r"\A<!-- glossary part .*?-->\s*", "", t, flags=re.S)
        body.append(t.rstrip() + "\n\n")
    text = "".join(body)
    # entries that start with a numeral ("10 a.m. policy", "3D printer") go in one section at the top
    nums = re.findall(r"(?m)^- \*\*\d.*\n?", text)
    text = re.sub(r"(?m)^- \*\*\d.*\n?", "", text)
    text = re.sub(r"(?m)^## [^\n]*\n\s*(?=## |\Z)", "", text)          # drop letter headings left empty
    numbers = ("## 0 to 9\n\n" + "".join(sorted(n.rstrip("\n") + "\n" for n in nums)) + "\n") if nums else ""
    GLOSS.write_text(HEAD.read_text(encoding="utf-8").rstrip() + "\n\n" + numbers + text.rstrip() + "\n",
                     encoding="utf-8")
    n = len(re.findall(r"(?m)^- ", GLOSS.read_text(encoding="utf-8")))
    for f in files + [HEAD]:
        f.unlink()
    print(f"{GLOSS.relative_to(ROOT)}: {n} entries from {len(files)} files")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "split":
        split(int(sys.argv[2]) if len(sys.argv) > 2 else 6)
    elif len(sys.argv) > 1 and sys.argv[1] == "join":
        join()
    else:
        sys.exit(__doc__)
