"""Build the whole book as ONE Markdown file: build/history-book.md.

Usage:  python tools/build_full_book_md.py

Same order and content as tools/build_full_book.py (front matter, the introduction, the chapters in
registry order with three part files per chapter in era order, back matter), using its parser and its
chapter loader: the "Chapter opening" card sits under the chapter heading and the "Chapter closing" card
after the last era (see that file's docstring for the rules). Viewer markers and editor notes are dropped; era titles,
span labels and story names become headings. A linked table of contents comes first, with explicit
anchors so the links work in any Markdown viewer, and every chapter ends with a link back to it.

Every line of a block is its own paragraph, as in the HTML (T-706): a blank line goes between two lines
of text, between a list and the line after it, and between a record box and the line after it. So a
Markdown viewer never joins furniture lines (an era closer's lines, a Known / Not known pair, the card's
"Five minutes?" and "Can skip:") into one paragraph, and never pulls a "Next:" line into the last bullet.
A "By [year]" line that opens a span is printed above the span's heading, as in the HTML. The
front-matter tokens ({{book_words}} and the others listed in build_full_book.py) are filled in.
tools/review_extract.py cuts this file at its "# Part N:" and "## Chapter N:" lines: keep both forms.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_full_book as B  # noqa: E402  (reuses the registry reader and the grid parser)


def shift(lines, n):
    """Push every Markdown heading in a block down n levels (max ######)."""
    out = []
    for l in lines:
        m = re.match(r"^(\s*)(#{1,6})(\s+.*)$", l)
        out.append(m.group(1) + "#" * min(6, len(m.group(2)) + n) + m.group(3) if m else l.rstrip())
    return out


def tidy(lines):
    """Trim blank lines at both ends and collapse runs of blank lines."""
    out = []
    for l in lines:
        if not l.strip() and (not out or not out[-1].strip()):
            continue
        out.append(l)
    while out and not out[-1].strip():
        out.pop()
    return out


def line_kind(l):
    if re.match(r"^(?:[-*]|\d+\.)\s+", l):
        return "li"
    if l.startswith(">"):
        return ">"
    return "p"


def separate(lines):
    """Every line its own paragraph: a blank line between two lines that are not both list items
    or both record lines."""
    out = []
    for l in lines:
        if out and l.strip() and out[-1].strip():
            a, b = line_kind(out[-1]), line_kind(l)
            if not (a == b and a in ("li", ">")):
                out.append("")
        out.append(l)
    return out


def body(lines, n):
    return separate(tidy(shift(lines, n)))


def matter(lines):
    """A front or back matter section. A "## Chapter N:" heading there (the answers file's sections)
    goes one level down, so that only the chapters themselves carry the form review_extract.py cuts at."""
    return [re.sub(r"^## (Chapter \d+:)", r"### \1", l) for l in body(lines, 0)]


def story(attrs, lines):
    name, rest = attrs.get("name", ""), list(lines)
    for i, l in enumerate(rest):
        if l.strip():
            h = re.match(r"^#{1,6}\s+(.*)$", l.strip())
            if h:
                name = h.group(1).strip()
                rest = rest[i + 1:]
            break
    slug = attrs.get("slug", "")
    return [f'<a id="story-{slug}"></a>', "", f"#### {name}", ""] + body(rest, 2) + [""]


def zoom(attrs, lines):
    out, lines = [], list(lines)
    if attrs.get("level") == "span" and attrs.get("label"):
        k = next((x for x, l in enumerate(lines) if l.strip()), None)
        if k is not None and B.RE_BY.match(lines[k].strip()):
            out += [lines[k].strip(), ""]       # a "By [year]" line belongs above the span (see above)
            lines = lines[:k] + lines[k + 1:]
        out += [f"#### {attrs['label']}", ""]
    return out + body(lines, 2) + [""]


def build():
    chapters, parts, before, after = B.prepare_book()
    md = [f"# {B.BOOK_TITLE}", "",
          f"*{len(chapters)} chapters, each told across the same ten eras*", "",
          '<a id="contents"></a>', "", "## Contents", ""]
    for m in before:
        md += [f"**[{m['toc']}](#{m['id']})**", ""]
    last = None
    for c in chapters:
        if c["part"] != last:
            last = c["part"]
            md += ["", f"**Part {last}: {parts.get(last, '')}**", ""]
        time = f" · about {c['card_minutes']} minutes" if c["card_minutes"] else ""
        md.append(f"{int(c['num'])}. [{c['title']}](#ch-{c['slug']}){time}")
    if after:
        md.append("")
    for m in after:
        md += [f"**[{m['toc']}](#{m['id']})**", ""]
    md += ["", "---", ""]
    for m in before:
        md += [f'<a id="{m["id"]}"></a>', ""] + matter(m["lines"]) + ["", "[Back to contents](#contents)", "", "---", ""]

    last = None
    for c in chapters:
        if c["part"] != last:
            last = c["part"]
            md += [f'<a id="part-{last}"></a>', "", f"# Part {last}: {parts.get(last, '')}", ""]
        md += [f'<a id="ch-{c["slug"]}"></a>', "", f"## Chapter {int(c['num'])}: {c['title']}", ""]
        if c["opening"]:
            md += zoom(c["opening"][1], c["opening"][2])
        for e in c["eras"]:
            md += [f"### {e['heading'] or e['label']}", ""]
            for kind, attrs, lines in e["blocks"]:
                md += story(attrs, lines) if kind == "story" else zoom(attrs, lines)
        if c["closing"]:
            md += zoom(c["closing"][1], c["closing"][2])
        md += ["[Back to contents](#contents)", "", "---", ""]
    for m in after:
        md += [f'<a id="{m["id"]}"></a>', ""] + matter(m["lines"]) + ["", "[Back to contents](#contents)", "", "---", ""]

    B.OUT.mkdir(exist_ok=True)
    out = B.OUT / "history-book.md"
    text = "\n".join(md) + "\n"
    # each record line (> **Who:** ...) is its own paragraph inside the quote box
    text = re.sub(r"(?m)^(>.*)\n(?=> \*\*)", r"\1\n>\n", text)
    out.write_text(text, encoding="utf-8")
    return out


if __name__ == "__main__":
    out = build()
    text = out.read_text(encoding="utf-8")
    words = len(re.sub(r"<[^>]+>|\]\(#[^)]*\)|[#*>\[\]|-]", " ", text).split())
    print(f"Markdown: {out} ({out.stat().st_size/1024:.0f} KB), about {words:,} words, "
          f"comments left: {text.count('<!--')}")
    print(f"warnings: {len(B.warnings)}")
    for w in B.warnings:
        print("  WARN", w)
