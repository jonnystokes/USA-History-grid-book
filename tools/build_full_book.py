#!/usr/bin/env python3
"""Build one reader-facing copy of the whole book (ROADMAP step 7).

Reads control/chapter-registry.md for chapter order, merges each chapter's
part files (manuscript/<slug>/part*.md) by era order, strips every hb- HTML
comment marker and every hb-note block, keeps the visible text (era titles,
span labels as headings, story names), and writes build/history-book.html.

Order of the book (each section listed in the contents):
  front matter   manuscript/_frontmatter/NN-*.md   (NN = two digits, in name order)
  introduction   manuscript/_introduction/how-we-know.md
  the 37 chapters
  back matter    manuscript/_backmatter/NN-*.md
Each front or back matter file is its own section titled by its "# " heading.
Missing or empty folders are fine. FRONT_BEFORE_INTRO flips the first two.

Chapter furniture (ARCHITECTURE-GUIDE 4.1, 4.2): a zoom block labelled
"Chapter opening" that is the FIRST block of era 1 is lifted out and rendered
under the chapter heading, before the first era heading. A zoom block labelled
"Chapter closing" that is the LAST block of era 10 is rendered after the last
era. Either label anywhere else is left in place with a warning. The contents
line carries the opening card's "about N minutes"; the build computes the time
itself (words / 200, rounded to 5, the measure_readability.py word rule) and
warns if the card disagrees.

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
FRONT = MS / "_frontmatter"
BACK = MS / "_backmatter"
FRONT_BEFORE_INTRO = False  # dispatch T-660; ARCHITECTURE-GUIDE 6 has the introduction first
OPEN_LABEL, CLOSE_LABEL = "Chapter opening", "Chapter closing"
CARD_TIME = re.compile(r"\babout (\d+) minutes\b")
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


def era_num(e):
    try:
        return int(e["order"])
    except ValueError:
        return 0


def block_words(lines):
    """Words a reader reads, by measure_readability.py's rule: no headings, no > records."""
    return sum(len(l.split()) for l in lines if not l.startswith(("#", ">")))


def reading_minutes(words):
    return max(5, int(words / 200 / 5 + 0.5) * 5)


def load_chapter(c):
    """Parse one chapter and lift out its opening and closing cards.
    Adds to c: eras, opening, closing (block tuples or None), words, minutes, card_minutes."""
    slug = c["slug"]
    eras = parse_chapter(slug)
    opening = closing = None
    if eras and era_num(eras[0]) == 1 and eras[0]["blocks"]:
        kind, attrs, _ = eras[0]["blocks"][0]
        if kind == "zoom" and attrs.get("label") == OPEN_LABEL:
            opening = eras[0]["blocks"].pop(0)
    if eras and era_num(eras[-1]) == 10 and eras[-1]["blocks"]:
        kind, attrs, _ = eras[-1]["blocks"][-1]
        if kind == "zoom" and attrs.get("label") == CLOSE_LABEL:
            closing = eras[-1]["blocks"].pop()
    for e in eras:
        for kind, attrs, _ in e["blocks"]:
            if attrs.get("label") in (OPEN_LABEL, CLOSE_LABEL):
                warn(f'{slug} era {e["order"]}: "{attrs["label"]}" block is not the '
                     f'{"first block of era 1" if attrs["label"] == OPEN_LABEL else "last block of era 10"}'
                     f"; left in place")
    words = sum(block_words(b[2]) for e in eras for b in e["blocks"])
    words += sum(block_words(b[2]) for b in (opening, closing) if b)
    card = CARD_TIME.search(" ".join(opening[2])) if opening else None
    c.update(eras=eras, opening=opening, closing=closing, words=words,
             minutes=reading_minutes(words), card_minutes=int(card.group(1)) if card else None)
    if opening and not card:
        warn(f"{slug}: chapter opening has no \"about N minutes\"")
    if card and c["card_minutes"] != c["minutes"]:
        warn(f'{slug}: opening says about {c["card_minutes"]} minutes, '
             f'{words:,} words gives about {c["minutes"]}')
    return c


def matter_files(folder):
    """The NN-*.md files of a front or back matter folder, in name order ([] if missing)."""
    if not folder.is_dir():
        return []
    files = []
    for p in sorted(folder.iterdir()):
        if re.match(r"^\d\d-.+\.md$", p.name):
            files.append(p)
        elif p.suffix == ".md":
            warn(f"{folder.name}/{p.name}: ignored (name must be NN-name.md)")
    return files


def load_matter(path, sid):
    """One front/back matter or introduction file: {id, title, lines}. Title = its first '# ' heading."""
    lines = [l for l in path.read_text(encoding="utf-8").splitlines() if "<!--" not in l]
    title = next((m.group(1).strip() for m in (re.match(r"^#\s+(.*\S)", l) for l in lines) if m), None)
    if title is None:
        title = re.sub(r"^\d\d-", "", path.stem).replace("-", " ").capitalize()
        warn(f"{path.parent.name}/{path.name}: no '# ' heading; titled {title!r}")
        lines = [f"# {title}", ""] + lines
    return {"id": sid, "title": title, "lines": lines}


def load_matters():
    """(before, after): the sections before the chapters (front matter and introduction, in book
    order) and after them (back matter). Each is {id, title, toc, lines}."""
    front = [load_matter(p, f"front-{p.stem}") for p in matter_files(FRONT)]
    back = [load_matter(p, f"back-{p.stem}") for p in matter_files(BACK)]
    for m in front + back:
        m["toc"] = m["title"]
    intro = load_matter(INTRO, "introduction")
    intro["toc"] = f'Introduction: {intro["title"]}'
    return (front + [intro] if FRONT_BEFORE_INTRO else [intro] + front), back


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
    return (f'<section class="story" data-b="{next_b()}" id="story-{html.escape(attrs.get("slug", ""))}">'
            f"<h4>{inline(title)}</h4>\n{md_blocks(body, head_shift=2)}</section>")


def render_zoom(attrs, lines, cls="zoom"):
    out = []
    b = ""
    if attrs.get("level") == "span" and attrs.get("label"):
        out.append(f'<h4 class="span">{inline(attrs["label"])}</h4>')
        b = f' data-b="{next_b()}"'
    out.append(md_blocks(lines, head_shift=2))
    return f'<div class="{cls}"{b}>' + "\n".join(out) + "</div>"


# ---------- page-break targets ----------
# Every heading gets a break target: the story box or span block it opens, or the heading itself.
# tools/make_pdf.py forces a page break before a target whose heading lands in the bottom half
# of a page. data-b numbers are unique across the whole book.
_b = [0]


def next_b():
    _b[0] += 1
    return _b[0]


WRAP_HEAD = re.compile(r'<(?:section|div)\b[^>]*\bdata-b="(\d+)"[^>]*>\s*<h([1-6])\b([^>]*)>(.*?)</h\2>'
                       r'|<h([1-6])\b([^>]*)>(.*?)</h\5>', re.S)


def tag_headings(fragment):
    """Give every heading not already covered by a wrapper target its own data-b.
    Returns (new_fragment, heads): heads lists, in document order, one dict per heading
    with its target b, kind (chapter, era, span, story, matter, other), text and element id."""
    heads = []

    def plain(s):
        return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()

    def sub(m):
        if m.group(1):  # wrapper with its heading
            whole = m.group(0)
            kind = "story" if whole.startswith("<section") else "span"
            heads.append({"b": int(m.group(1)), "kind": kind, "text": plain(m.group(4)), "id": None})
            return whole
        lvl, attrs, inner = m.group(5), m.group(6), m.group(7)
        bm = re.search(r'data-b="(\d+)"', attrs)
        if bm:
            b = int(bm.group(1))
        else:
            b = next_b()
            attrs += f' data-b="{b}"'
        cls = re.search(r'class="([^"]*)"', attrs)
        cls = cls.group(1) if cls else ""
        kind = ("chapter" if "chapter" in cls else "era" if "era" in cls else
                "part" if "part" in cls or "book" in cls else "other")
        idm = re.search(r'id="([^"]*)"', attrs)
        heads.append({"b": b, "kind": kind, "text": plain(inner), "id": idm.group(1) if idm else None})
        return f"<h{lvl}{attrs}>{inner}</h{lvl}>"

    return WRAP_HEAD.sub(sub, fragment), heads


def render_matter(m, cls):
    """A front/back matter section: its # heading becomes an h2 carrying the anchor."""
    return (f'<section class="{cls}">'
            + md_blocks(m["lines"], head_shift=1).replace("<h2>", f'<h2 id="{m["id"]}">', 1) + "</section>")


# ---------- assemble ----------
# Page geometry. tools/make_pdf.py reads PAGE_H, MARGIN_TOP and MARGIN_BOTTOM (points) to find the
# middle of the text area, so keep them in step with the @page rule below.
PAGE_H, MARGIN_TOP, MARGIN_BOTTOM = 792.0, 0.85 * 72, 0.95 * 72

CSS = """
@page { size: letter; margin: 0.85in 0.9in 0.95in 0.9in;
  @bottom-center { content: counter(page); font: 9pt "Segoe UI", Calibri, Arial, sans-serif; color: #777; } }
@page cover { @bottom-center { content: none; } }
:root { --ink:#1d1d1f; --dim:#5a5a5f; --accent:#1f4e79; --rule:#d6d6d6; --soft:#f4f6f9; --bg:#fffefb; }
@media (prefers-color-scheme: dark) { @media screen {
  :root { --ink:#e6e6e6; --dim:#a8a8ad; --accent:#8cb8e6; --rule:#3a3a3e; --soft:#24262b; --bg:#17181b; } } }
* { box-sizing: border-box; }
html { font-size: 12pt; }
body { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", serif; color: var(--ink);
  background: var(--bg); line-height: 1.6; margin: 0 auto; max-width: 42em; padding: 2em 16px 4em; }
@media print { body { max-width: none; padding: 0; background: #fff; } html { font-size: 11.5pt; }
  a { color: inherit; } }
h1, h2, h3, h4, h5, h6 { font-family: "Segoe UI", Calibri, Arial, sans-serif; color: var(--accent);
  line-height: 1.25; break-after: avoid; break-inside: avoid; }
.cover { page: cover; text-align: center; }
h1.book { font-size: 2.6em; margin: 5.5em 0 0.4em; }
p.sub { text-align: center; color: var(--dim); font-size: 1.1em; }
p.ages { text-align: center; color: var(--dim); margin-top: 1.5em; }
h1.part { font-size: 1.9em; text-align: center; margin: 4em 0 0.5em; break-before: page; }
p.partno { text-align: center; color: var(--dim); text-transform: uppercase; letter-spacing: .12em;
  margin-top: 6em; break-before: page; }
p.partno + h1.part { margin-top: .3em; break-before: avoid; }
h2.chapter { font-size: 1.75em; border-bottom: 2px solid var(--accent); padding-bottom: .2em;
  margin-top: 2.5em; break-before: page; }
h3.era { font-size: 1.3em; border-bottom: 1px solid var(--rule); padding-bottom: .1em; margin-top: 2em; }
h4 { font-size: 1.05em; margin: 1.4em 0 .4em; }
p { margin: .55em 0; orphans: 3; widows: 3; }
li { orphans: 2; widows: 2; }
.story { background: var(--soft); border-left: 4px solid var(--accent); padding: .3em 1em .6em;
  margin: 1.2em 0; border-radius: 3px; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
.story h4 { margin-top: .6em; }
.records { font-size: .92em; color: var(--dim); margin: .4em 0 .8em; break-inside: avoid; }
.rec { margin: .15em 0; }
.rec .k { font-weight: bold; color: var(--ink); }
nav.toc { break-after: page; }
nav.toc ul { list-style: none; padding: 0; margin: 0; }
nav.toc li { display: flex; align-items: baseline; gap: .4em; margin: .2em 0; break-inside: avoid; }
nav.toc li a { flex: 0 1 auto; }
nav.toc li .lead { flex: 1 1 auto; border-bottom: 1px dotted var(--rule); min-width: 1em;
  transform: translateY(-.25em); }
nav.toc li .pg { flex: 0 0 2.6em; text-align: right; font-variant-numeric: tabular-nums; }
nav.toc li .n { display: inline-block; min-width: 1.7em; color: var(--dim); }
nav.toc li.tp { margin-top: .9em; font-weight: bold; color: var(--accent); break-after: avoid; }
a { color: var(--accent); text-decoration: none; }
ul { padding-left: 1.5em; }
section.introduction h2, section.matter h2 { break-before: page; }
.chapter-opening, .chapter-closing { background: var(--soft); padding: .3em 1em .6em; margin: 1.2em 0;
  border-radius: 3px; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
.chapter-closing { border-top: 2px solid var(--accent); margin-top: 2em; }
nav.toc .time { color: var(--dim); font-size: .85em; white-space: nowrap; }
"""


def chapter_page_css(chapters):
    """One named page per chapter: its footer carries the chapter's number and title."""
    rules = []
    for c in chapters:
        label = f'Chapter {int(c["num"])} \\00B7  {c["title"]}'.replace('"', '\\"')
        rules.append(f'@page ch{int(c["num"])} {{ @bottom-center {{ content: "{label}   \\00B7   " counter(page); }} }}')
    return "\n".join(rules)


SEGMENTS = []   # filled by build(): [{"name", "html", "heads"}]; each one starts on a fresh page


def toc_line(href, label, num="", time=""):
    n = f'<span class="n">{num}</span>' if num else ""
    return (f'<li><a href="#{href}">{n}{label}</a>{time}<span class="lead"></span>'
            f'<span class="pg" data-for="{href}"></span></li>')


def build():
    chapters, parts = read_registry()
    if len(chapters) != 37:
        warn(f"registry has {len(chapters)} chapters (expected 37)")
    before, after = load_matters()
    for c in chapters:
        load_chapter(c)
    SEGMENTS.clear()

    def segment(name, fragment):
        frag, heads = tag_headings(fragment)
        SEGMENTS.append({"name": name, "html": frag, "heads": heads})

    cover = ('<div class="cover">'
             f'<h1 class="book">{BOOK_TITLE}</h1>'
             f'<p class="sub">{len(chapters)} chapters, each told across the same ten eras</p></div>')
    # table of contents
    toc = ['<nav class="toc"><h2>Contents</h2><ul>']
    toc += [toc_line(m["id"], inline(m["toc"])) for m in before]
    last_part = None
    for c in chapters:
        if c["part"] != last_part:
            last_part = c["part"]
            toc.append(f'<li class="tp">Part {last_part}: {html.escape(parts.get(last_part, ""))}</li>')
        time = f' <span class="time">about {c["card_minutes"]} min</span>' if c["card_minutes"] else ""
        toc.append(toc_line(f'ch-{c["slug"]}', html.escape(c["title"]), int(c["num"]), time))
    toc += [toc_line(m["id"], inline(m["toc"])) for m in after]
    toc.append('</ul></nav>')
    # front matter and introduction: each file's # heading becomes h2, ## becomes h3
    segment("front", cover + "\n".join(toc) + "\n"
            + "\n".join(render_matter(m, "introduction" if m["id"] == "introduction" else "matter")
                        for m in before))

    last_part = None
    for c in chapters:
        body = []
        if c["part"] != last_part:
            last_part = c["part"]
            body.append(f'<p class="partno">Part {last_part}</p>'
                        f'<h1 class="part">{html.escape(parts.get(last_part, ""))}</h1>')
        body.append(f'<div class="chap" style="page: ch{int(c["num"])}">')
        body.append(f'<h2 class="chapter" id="ch-{c["slug"]}">Chapter {int(c["num"])}: {html.escape(c["title"])}</h2>')
        if c["opening"]:
            body.append(render_zoom(c["opening"][1], c["opening"][2], "zoom chapter-opening"))
        for e in c["eras"]:
            title = e["heading"] or e["label"]
            if e["heading"] and e["label"] and e["heading"] != e["label"]:
                warn(f'{c["slug"]} era {e["order"]}: heading {e["heading"]!r} != label {e["label"]!r}')
            body.append(f'<h3 class="era" data-b="{next_b()}">{inline(title)}</h3>')
            if not e["blocks"]:
                warn(f'{c["slug"]} era {e["order"]} ({e["label"]}): no zoom or story blocks')
            for kind, attrs, lines in e["blocks"]:
                body.append(render_story(attrs, lines) if kind == "story" else render_zoom(attrs, lines))
        if c["closing"]:
            body.append(render_zoom(c["closing"][1], c["closing"][2], "zoom chapter-closing"))
        body.append("</div>")
        segment(f'ch{int(c["num"]):02d}-{c["slug"]}', "\n".join(body))
    # back matter: one segment per file, each starts on its own page
    for m in after:
        segment(f'back-{m["id"]}', render_matter(m, "matter"))

    out = write_page("".join(s["html"] + "\n" for s in SEGMENTS), chapters)
    return out


def page_head(chapters, extra_css=""):
    return ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
            f"<title>{BOOK_TITLE}</title><style>{CSS}\n{chapter_page_css(chapters)}\n{extra_css}</style></head><body>\n")


def write_page(body_html, chapters, extra_css="", name="history-book.html"):
    OUT.mkdir(exist_ok=True)
    out = OUT / name
    out.write_text(page_head(chapters, extra_css) + body_html + "</body></html>\n", encoding="utf-8")
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
        import make_pdf  # tools/make_pdf.py: page breaks, contents page numbers, final PDF
        make_pdf.main(sys.modules[__name__])
    print(f"warnings: {len(warnings)}")
    for w in warnings:
        print("  WARN", w)
