#!/usr/bin/env python3
"""Build one reader-facing copy of the whole book (ROADMAP step 7).

Reads control/chapter-registry.md for chapter order, merges each chapter's
part files (manuscript/<slug>/part*.md) by era order, puts the introduction first
(manuscript/_introduction/how-we-know.md), strips every hb- HTML comment marker
and every hb-note block, keeps the visible text (era titles, span labels as
headings, story names), and writes build/history-book.html.

Pure standard library: no pandoc, no markdown package needed.
The manuscript's Markdown subset (VIEWER-CONTRACT.md) is small: headings,
paragraphs, **bold**, *italic*, blockquote records, bullet lists.

Usage:  python tools/build_full_book.py [--pdf]
  --pdf  also print build/history-book.pdf with headless Chrome via
         C:/Users/jon/Projects/claude-workspace/tools/html2pdf.ps1
Prints warnings for anything odd it finds (stray text outside blocks,
era heading/label mismatches, missing or duplicate eras).
"""
import html
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MS = ROOT / "manuscript"
OUT = ROOT / "build"
REGISTRY = ROOT / "control" / "chapter-registry.md"
INTRO = MS / "_introduction" / "how-we-know.md"
HTML2PDF = Path(r"C:\Users\jon\Projects\claude-workspace\tools\html2pdf.ps1")
BOOK_TITLE = "A History of the United States"

warnings = []


def warn(msg):
    warnings.append(msg)


# ---------- registry ----------
def read_registry():
    text = REGISTRY.read_text(encoding="utf-8")
    chapters = []
    for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*`([a-z-]+)`\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|", text, re.M):
        chapters.append({"num": m.group(1), "slug": m.group(2), "title": m.group(3), "part": int(m.group(4))})
    parts = {}
    pm = re.search(r"^## Parts\s*\n(.+)$", text, re.M)
    if pm:
        for m in re.finditer(r"(\d+)\.\s*([^(·]+?)\s*\(", pm.group(1)):
            parts[int(m.group(1))] = m.group(2).strip()
    return chapters, parts


# ---------- inline + block markdown ----------
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w\"'(])(https?://[^\s<)]+[^\s<).,;:])", r'<a href="\1">\1</a>', s)
    return s


def md_blocks(lines, head_shift=0):
    """Render a list of Markdown lines to HTML (subset used by the book)."""
    out, para, items, quote = [], [], [], []

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()
        if items:
            out.append("<ul>" + "".join("<li>" + inline(i) + "</li>" for i in items) + "</ul>")
            items.clear()
        if quote:
            recs = []
            for q in quote:
                m = re.match(r"\*\*(.+?):\*\*\s*(.*)", q)
                if m:
                    recs.append([m.group(1), m.group(2)])
                elif recs:
                    recs[-1][1] += " " + q
                else:
                    recs.append(["", q])
            body = "".join(
                f'<div class="rec"><span class="k">{inline(k)}:</span> {inline(v)}</div>' if k
                else f'<div class="rec">{inline(v)}</div>' for k, v in recs)
            out.append(f'<div class="records">{body}</div>')
            quote.clear()

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        h = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h:
            flush()
            lvl = min(6, len(h.group(1)) + head_shift)
            out.append(f"<h{lvl}>{inline(h.group(2))}</h{lvl}>")
            continue
        if line.startswith(">"):
            if para or items:
                f_q = list(quote)
                quote.clear()
                flush()
                quote.extend(f_q)
            quote.append(line[1:].strip())
            continue
        li = re.match(r"^[-*]\s+(.*)$", line)
        if li:
            if para or quote:
                flush()
            items.append(li.group(1))
            continue
        if items or quote:
            flush()
        para.append(line.strip())
    flush()
    return "\n".join(out)


# ---------- grid parsing ----------
ATTR = re.compile(r'(\w+)="([^"]*)"')
MARK = re.compile(r"^\s*<!--\s*(/?hb-[a-z]+(?::(?:start|end))?)\b(.*?)-->\s*$")


def parse_chapter(slug):
    files = sorted((MS / slug).glob("part*.md"))
    if len(files) != 3:
        warn(f"{slug}: {len(files)} part files (expected 3)")
    eras = []  # dicts: order, label, blocks[(kind, attrs, lines)]
    for f in files:
        lines = f.read_text(encoding="utf-8").splitlines()
        era = None
        block = None  # (kind, attrs, lines)
        in_note = False
        for n, line in enumerate(lines, 1):
            m = MARK.match(line)
            if m:
                tag, attrs = m.group(1), dict(ATTR.findall(m.group(2)))
                if tag == "hb-note":
                    in_note = True
                elif tag == "/hb-note":
                    in_note = False
                elif tag == "hb-time:start":
                    era = {"order": attrs.get("order", "99"), "label": attrs.get("label", ""),
                           "id": attrs.get("id", ""), "heading": None, "blocks": [], "src": f"{f.name}:{n}"}
                    eras.append(era)
                elif tag == "hb-time:end":
                    era = None
                elif tag in ("hb-zoom", "hb-story:start"):
                    if block:
                        warn(f"{slug}/{f.name}:{n}: block opened inside an open block")
                    block = ("story" if tag == "hb-story:start" else "zoom", attrs, [])
                    if era is None:
                        warn(f"{slug}/{f.name}:{n}: {tag} outside any hb-time era")
                elif tag in ("/hb-zoom", "hb-story:end"):
                    if block and era is not None:
                        era["blocks"].append(block)
                    block = None
                elif tag == "hb-chapter":
                    if attrs.get("slug") != slug:
                        warn(f"{slug}/{f.name}:{n}: hb-chapter slug={attrs.get('slug')!r}")
                continue
            if in_note:
                continue
            if "<!--" in line:
                warn(f"{slug}/{f.name}:{n}: other HTML comment dropped: {line.strip()[:60]}")
                continue
            if block is not None:
                block[2].append(line)
                continue
            s = line.strip()
            if not s:
                continue
            if re.match(r"^#\s", s):
                continue  # chapter heading, emitted from the registry
            if era is not None and re.match(r"^##\s", s) and era["heading"] is None:
                era["heading"] = s[3:].strip()
                continue
            warn(f"{slug}/{f.name}:{n}: stray text outside blocks: {s[:70]}")
    eras.sort(key=lambda e: e["order"])
    orders = [e["order"] for e in eras]
    if len(set(orders)) != len(orders):
        warn(f"{slug}: duplicate era orders {orders}")
    if len(eras) != 10:
        warn(f"{slug}: {len(eras)} eras (expected 10)")
    return eras


def render_story(attrs, lines):
    name = attrs.get("name", "")
    body = list(lines)
    title = name
    # use the visible ### heading if present; drop it from the body
    for i, l in enumerate(body):
        if l.strip():
            h = re.match(r"^#{1,6}\s+(.*)$", l.strip())
            if h:
                title = h.group(1).strip()
                if name and title != name:
                    warn(f"story {attrs.get('slug')}: heading {title!r} != name {name!r}")
                body = body[i + 1:]
            break
    return (f'<section class="story" id="story-{html.escape(attrs.get("slug", ""))}">'
            f"<h4>{inline(title)}</h4>\n{md_blocks(body, head_shift=2)}</section>")


def render_zoom(attrs, lines):
    out = []
    if attrs.get("level") == "span" and attrs.get("label"):
        out.append(f'<h4 class="span">{inline(attrs["label"])}</h4>')
    out.append(md_blocks(lines, head_shift=2))
    return '<div class="zoom">' + "\n".join(out) + "</div>"


# ---------- assemble ----------
CSS = """
@page { size: letter; margin: 0.85in 0.9in 0.95in 0.9in; }
:root { --ink:#1d1d1f; --dim:#5a5a5f; --accent:#1f4e79; --rule:#d6d6d6; --soft:#f4f6f9; --bg:#fffefb; }
@media (prefers-color-scheme: dark) { @media screen {
  :root { --ink:#e6e6e6; --dim:#a8a8ad; --accent:#8cb8e6; --rule:#3a3a3e; --soft:#24262b; --bg:#17181b; } } }
* { box-sizing: border-box; }
html { font-size: 12pt; }
body { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", serif; color: var(--ink);
  background: var(--bg); line-height: 1.6; margin: 0 auto; max-width: 42em; padding: 2em 16px 4em; }
@media print { body { max-width: none; padding: 0; background: #fff; } html { font-size: 11.5pt; } }
h1, h2, h3, h4 { font-family: "Segoe UI", Calibri, Arial, sans-serif; color: var(--accent);
  line-height: 1.25; break-after: avoid; }
h1.book { font-size: 2.4em; text-align: center; margin: 3em 0 0.3em; }
p.sub { text-align: center; color: var(--dim); }
h1.part { font-size: 1.9em; text-align: center; margin: 4em 0 0.5em; break-before: page; }
p.partno { text-align: center; color: var(--dim); text-transform: uppercase; letter-spacing: .12em;
  margin-top: 6em; break-before: page; }
p.partno + h1.part { margin-top: .3em; break-before: avoid; }
h2.chapter { font-size: 1.75em; border-bottom: 2px solid var(--accent); padding-bottom: .2em;
  margin-top: 2.5em; break-before: page; }
h3.era { font-size: 1.3em; border-bottom: 1px solid var(--rule); padding-bottom: .1em; margin-top: 2em; }
h4 { font-size: 1.05em; margin: 1.4em 0 .4em; }
p { margin: .55em 0; orphans: 3; widows: 3; }
.story { background: var(--soft); border-left: 4px solid var(--accent); padding: .3em 1em .6em;
  margin: 1.2em 0; border-radius: 3px; }
.story h4 { margin-top: .6em; }
.records { font-size: .92em; color: var(--dim); margin: .4em 0 .8em; }
.rec { margin: .15em 0; }
.rec .k { font-weight: bold; color: var(--ink); }
nav.toc { break-after: page; }
nav.toc ol { padding-left: 1.4em; }
nav.toc li { margin: .15em 0; }
nav.toc .tp { font-weight: bold; margin-top: .8em; list-style: none; margin-left: -1.4em; color: var(--accent); }
a { color: var(--accent); text-decoration: none; }
ul { padding-left: 1.5em; }
section.introduction h2 { break-before: page; }
"""


def build():
    chapters, parts = read_registry()
    if len(chapters) != 37:
        warn(f"registry has {len(chapters)} chapters (expected 37)")
    body = [f'<h1 class="book">{BOOK_TITLE}</h1>',
            f'<p class="sub">{len(chapters)} chapters, each told across the same ten eras</p>']
    # table of contents
    toc = ['<nav class="toc"><h2>Contents</h2><ol>', '<li class="tp"><a href="#introduction">Introduction: How We Know What Happened</a></li>']
    last_part = None
    for c in chapters:
        if c["part"] != last_part:
            last_part = c["part"]
            toc.append(f'<li class="tp">Part {last_part}: {html.escape(parts.get(last_part, ""))}</li>')
        toc.append(f'<li value="{int(c["num"])}"><a href="#ch-{c["slug"]}">{html.escape(c["title"])}</a></li>')
    toc.append('</ol></nav>')
    body.append("\n".join(toc))
    # introduction: its own # heading becomes h2, ## becomes h3
    iw = [l for l in INTRO.read_text(encoding="utf-8").splitlines() if "<!--" not in l]
    body.append('<section class="introduction">'
                + md_blocks(iw, head_shift=1).replace("<h2>", '<h2 id="introduction">', 1) + '</section>')

    last_part = None
    for c in chapters:
        if c["part"] != last_part:
            last_part = c["part"]
            body.append(f'<p class="partno">Part {last_part}</p>'
                        f'<h1 class="part">{html.escape(parts.get(last_part, ""))}</h1>')
        body.append(f'<h2 class="chapter" id="ch-{c["slug"]}">Chapter {int(c["num"])}: {html.escape(c["title"])}</h2>')
        for e in parse_chapter(c["slug"]):
            title = e["heading"] or e["label"]
            if e["heading"] and e["label"] and e["heading"] != e["label"]:
                warn(f'{c["slug"]} era {e["order"]}: heading {e["heading"]!r} != label {e["label"]!r}')
            body.append(f'<h3 class="era">{inline(title)}</h3>')
            if not e["blocks"]:
                warn(f'{c["slug"]} era {e["order"]} ({e["label"]}): no zoom or story blocks')
            for kind, attrs, lines in e["blocks"]:
                body.append(render_story(attrs, lines) if kind == "story" else render_zoom(attrs, lines))

    page = ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
            f"<title>{BOOK_TITLE}</title><style>{CSS}</style></head><body>\n"
            + "\n".join(body) + "\n</body></html>\n")
    OUT.mkdir(exist_ok=True)
    out = OUT / "history-book.html"
    out.write_text(page, encoding="utf-8")
    return out


class TextGrab(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, a):
        if tag in ("style", "script", "title"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("style", "script", "title"):
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip:
            self.parts.append(d)


def word_count(path):
    g = TextGrab()
    g.feed(path.read_text(encoding="utf-8"))
    text = " ".join(g.parts)
    if "<!--" in path.read_text(encoding="utf-8") or "hb-" in text:
        warn("built HTML still contains a comment or hb- text")
    return len(re.findall(r"\S+", text))


if __name__ == "__main__":
    out = build()
    wc = word_count(out)
    print(f"HTML: {out} ({out.stat().st_size/1024:.0f} KB), words: {wc:,}")
    if "--pdf" in sys.argv:
        pdf = OUT / "history-book.pdf"
        r = subprocess.run(["pwsh", "-NoProfile", "-File", str(HTML2PDF), "-Html", str(out), "-Pdf", str(pdf)],
                           capture_output=True, text=True)
        print((r.stdout + r.stderr).strip())
    print(f"warnings: {len(warnings)}")
    for w in warnings:
        print("  WARN", w)
