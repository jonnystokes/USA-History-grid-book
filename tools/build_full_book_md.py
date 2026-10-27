"""Build the whole book as ONE Markdown file: build/history-book.md.

Usage:  python tools/build_full_book_md.py

Same order and content as tools/build_full_book.py (front matter, the introduction, the chapters in
registry order with three part files per chapter in era order, back matter), using its parser and its
chapter loader: the "Chapter opening" card sits under the chapter heading and the "Chapter closing" card
after the last era (see that file's docstring for the rules). Viewer markers and editor notes are dropped; era titles,
span labels and story names become headings. A linked table of contents comes first, with explicit
anchors so the links work in any Markdown viewer, and every chapter ends with a link back to it.
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


def story(attrs, lines):
    name, body = attrs.get("name", ""), list(lines)
    for i, l in enumerate(body):
        if l.strip():
            h = re.match(r"^#{1,6}\s+(.*)$", l.strip())
            if h:
                name = h.group(1).strip()
                body = body[i + 1:]
            break
    slug = attrs.get("slug", "")
    return [f'<a id="story-{slug}"></a>', "", f"#### {name}", ""] + tidy(shift(body, 2)) + [""]


def zoom(attrs, lines):
    out = []
    if attrs.get("level") == "span" and attrs.get("label"):
        out += [f"#### {attrs['label']}", ""]
    return out + tidy(shift(lines, 2)) + [""]


def build():
    chapters, parts = B.read_registry()
    before, after = B.load_matters()
    for c in chapters:
        B.load_chapter(c)
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
        md += [f'<a id="{m["id"]}"></a>', ""] + tidy(shift(m["lines"], 0)) + ["", "[Back to contents](#contents)", "", "---", ""]

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
        md += [f'<a id="{m["id"]}"></a>', ""] + tidy(shift(m["lines"], 0)) + ["", "[Back to contents](#contents)", "", "---", ""]

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
