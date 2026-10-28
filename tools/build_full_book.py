#!/usr/bin/env python3
"""Build one reader-facing copy of the whole book (ROADMAP step 7).

Reads control/chapter-registry.md for chapter order, merges each chapter's
part files (manuscript/<slug>/part*.md) by era order, strips every hb- HTML
comment marker and every hb-note block, keeps the visible text (era titles,
span labels as headings, story names), and writes build/history-book.html.

Order of the book (each section listed in the contents):
  cover, contents, the grid (one page: 37 chapters by 10 eras, with page numbers)
  front matter   manuscript/_frontmatter/NN-*.md   (NN = two digits, in name order)
  introduction   manuscript/_introduction/how-we-know.md
  the 37 chapters
  back matter    manuscript/_backmatter/NN-*.md
Each front or back matter file is its own section titled by its "# " heading.
Missing or empty folders are fine. FRONT_BEFORE_INTRO flips the first two.

Chapter cards (ARCHITECTURE-GUIDE 4.1, 4.2): a zoom block labelled
"Chapter opening" that is the FIRST block of era 1 is lifted out and rendered
under the chapter heading, before the first era heading. A zoom block labelled
"Chapter closing" that is the LAST block of era 10 is rendered after the last
era. Either label anywhere else is left in place with a warning. The contents
line carries the opening card's "about N minutes"; the build computes the time
itself (words / WPM, rounded to 5, the measure_readability.py word rule) and
warns if the card disagrees.

Lines (T-706, measured 2026-10-27): the manuscript writes one paragraph per line (no body paragraph
is wrapped across lines anywhere) and the furniture one item per line with no blank line between
(ARCHITECTURE-GUIDE 4.1, 4.5, 5.7). So every line is its own paragraph: nothing is joined into a run-on
block, and no real paragraph is split. Consecutive "- " lines make one list, consecutive "> " lines one
record box.

Furniture, each kind with its own class and look (ARCHITECTURE-GUIDE 4, design review section 1):
  card      the "Chapter opening" block: the "Chapter N of 37" label, the spine a size larger, the
            three questions, "Five minutes?" and "Can skip:" (div.card.chapter-opening)
  closing   the "Chapter closing" block, styled as the card's partner (div.card.chapter-closing)
  strip     "Era N of 10 · ... · about N minutes", the first line of an era: a small-caps label with a
            ten-square ribbon, the era's square filled (p.strip)
  by        "By 1830:" lines inside a block, with a hairline above (p.byline)
  closer    an era-level zoom labelled "By 1850" or "By today": a tinted panel, its label on top
            (div.closer); a label is never a heading tag, so it adds no bookmark
  known     consecutive "Known:", "Not known:", "Disputed:" lines: one panel, labels in a column (div.kn)
  who       the story box "Who:" record, at body size and in ink (div.rec.who)
Links: the names quoted on "Five minutes?" and "Can skip:" lines link to their spans (span-<slug>-<n>);
every name that matches no span is a warning. "Chapter N" in the text links to that chapter (ch-<slug>).
The build prints a count of each kind per chapter, so a miss shows as a number.

Era colours: ten, one per era, from sepia (before 1500) to slate (2000 to today), all earth pigments,
used on the era heading's rule, the era strip and its ribbon, the story box bar and the closer of
that era (classes e1 to e10). Text never sits in an era colour. check_palette() checks each colour
against the page and the box tint (3:1 at least, for rules and bars) and that neighbours stay apart
in grey; no era footers and no named pages per era (they would force a page break at every era).

The grid page: each cell is the page where that chapter's era starts (era-<slug>-<n>), linked.
Back matter (manuscript/_backmatter, as tools/build_backmatter.py writes it): every line of the
glossary, timeline, people, places, movies and answers links to its target and shows its page. People
and movies go to their story box (matched on the story's name and its Movie line), glossary words,
timeline dates and places to the era (the hand-off's era label, else the first era that names it),
answers to the chapter closing (closing-<slug>). A line whose target cannot be found is linked to its
chapter, with a warning. tools/make_pdf.py fills every page number after layout, from the bookmarks
and the PDF's named destinations, in fixed-width slots, so filling them moves nothing.

Front-matter tokens: the front and back matter may write these, and every format (HTML, PDF and
Markdown) gets the build's own count in their place. Times are at WPM words a minute; one chapter's
time is rounded to 5 minutes as on the cards, a sum over many chapters to 15.
  {{words_per_minute}}                             200
  {{book_words}}                                   the 37 chapters' words, to the nearest 10,000 ("840,000")
  {{book_words_exact}}                             the same, exact ("838,412")
  {{book_hours}}                                   the 37 chapters' reading time, in whole hours ("70")
  {{story_count}}                                  story boxes in the chapters ("684")
  {{shortest_chapter}}, {{shortest_chapter_time}}  title and time of the shortest chapter
  {{longest_chapter}}, {{longest_chapter_time}}    title and time of the longest chapter
  {{most_chapters_from}}, {{most_chapters_to}}     the times most chapters fall between (the shortest
                                                   tenth and the longest tenth left out)
  {{era1_time}} ... {{era10_time}}                 one era read in every chapter ("2 hours 15 minutes")
  {{cards_time}}, {{closings_time}}                all the opening cards, all the chapter closings
  {{five_minutes_time}}                            all the spans the cards name under "Five minutes?"
  {{short_road_time}}                              the ten-minute history, the cards, the closings and
                                                   those spans
An unknown token is left as typed, with a warning.

Type (design review section 7): 12 pt Georgia, a column of about 72 characters, line height 1.6, left
aligned, no hyphenation, text-wrap: pretty, a white page in print. System fonts only (Georgia, Segoe
UI): after every PDF build tools/make_pdf.py runs pdffonts and stops if any other family was embedded
(FONT_FAMILIES, GLYPH_FALLBACK).

Pure standard library: no pandoc, no markdown package needed.
The manuscript's Markdown subset (VIEWER-CONTRACT.md) is small: headings,
paragraphs, **bold**, *italic*, blockquote records, bullet lists.

Usage:  python tools/build_full_book.py [--pdf]
  --pdf  also print build/history-book.pdf with headless Chrome (tools/make_pdf.py: page breaks,
         page numbers, bookmarks, the font check)
Prints the furniture counts and warnings for anything odd it finds (stray text outside blocks,
era heading/label mismatches, missing or duplicate eras, names and back-matter lines with no target).
"""
import html
import re
import sys
import time
import unicodedata
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MS = ROOT / "manuscript"
OUT = ROOT / "build"
REGISTRY = ROOT / "control" / "chapter-registry.md"
HANDOFF = ROOT / "control" / "backmatter"
INTRO = MS / "_introduction" / "how-we-know.md"
FRONT = MS / "_frontmatter"
BACK = MS / "_backmatter"
FRONT_BEFORE_INTRO = False  # dispatch T-660; ARCHITECTURE-GUIDE 6 has the introduction first
OPEN_LABEL, CLOSE_LABEL = "Chapter opening", "Chapter closing"
CARD_TIME = re.compile(r"\babout (\d+) minutes\b")
HTML2PDF = Path(r"C:\Users\jon\Projects\claude-workspace\tools\html2pdf.ps1")
BOOK_TITLE = "A History of the United States"
WPM = 200   # reading speed behind every time the book prints (ARCHITECTURE-GUIDE 4.1)

# Fonts the PDF may embed; tools/make_pdf.py checks with pdffonts after every PDF build. The CSS names
# system fonts only: Georgia for the text, Segoe UI for headings and labels. Georgia has no Hawaiian
# okina, so Chrome draws that one character in Times New Roman; nothing else may come from there.
FONT_FAMILIES = ("Georgia", "SegoeUI")
GLYPH_FALLBACK = {"TimesNewRomanPS": "\N{MODIFIER LETTER TURNED COMMA}"}   # font name prefix: characters

# The ten eras, earth pigments from sepia to slate (light page), and lighter twins for the screen's
# dark mode. Never used for text. check_palette() measures them.
ERA_COLOURS = ["#623f1b", "#744321", "#884428", "#954738", "#9e4e46",
               "#9b5d3e", "#966c3a", "#8d7a53", "#898372", "#778f9e"]
ERA_COLOURS_DARK = ["#a47f5e", "#b78465", "#cc886d", "#d98d7c", "#e1958b",
                    "#e0a386", "#dcb184", "#d2bf9b", "#cfc9b9", "#c0d4e3"]
BOX_TINT = "#f6f2ea"   # story boxes; --soft in the CSS
CANON_ERAS = ["before 1500", "1500s", "1600s", "1700 to 1750", "1750 to 1800", "1800 to 1850",
              "1850 to 1900", "1900 to 1950", "1950 to 2000", "2000 to today"]
GRID_HEAD = ["Before<br>1500", "The<br>1500s", "The<br>1600s", "1700 to<br>1750", "1750 to<br>1800",
             "1800 to<br>1850", "1850 to<br>1900", "1900 to<br>1950", "1950 to<br>2000", "2000 to<br>today"]
LQ, RQ = "\N{LEFT DOUBLE QUOTATION MARK}", "\N{RIGHT DOUBLE QUOTATION MARK}"

warnings = []
CHAPTERS = {}        # chapter number -> loaded chapter dict (prepare_book)
NUMBERS = {}         # token -> value (prepare_book)
FURN = {}            # chapter number -> Counter of furniture kinds (filled while rendering)
BACKLINKS = {}       # back-matter file kind -> Counter(linked, chapter_only)
CUR = {"c": None}    # the chapter being rendered (None in front and back matter)


def warn(msg):
    warnings.append(msg)


def count(kind, n=1):
    c = CUR["c"]
    if c is not None:
        FURN.setdefault(int(c["num"]), Counter())[kind] += n


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


# ---------- inline markdown and links ----------
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w\"'(])(https?://[^\s<)]+[^\s<).,;:])", r'<a href="\1">\1</a>', s)
    return s


RE_TAGS = re.compile(r"(<a\b[^>]*>.*?</a>|<[^>]+>)", re.S)
RE_CHREF = re.compile(r"\bChapter (\d{1,2})\b(?! of \d)")


def _chapter_link(m):
    c = CHAPTERS.get(int(m.group(1)))
    if c is None:
        warn(f"\"{m.group(0)}\" names no chapter in the registry")
        return m.group(0)
    count("xref")
    return f'<a class="xref" href="#ch-{c["slug"]}">{m.group(0)}</a>'


def link_chapters(h):
    """Link every "Chapter N" in rendered text to that chapter, outside tags and existing links."""
    parts = RE_TAGS.split(h)
    for i in range(0, len(parts), 2):
        if "Chapter" in parts[i]:
            parts[i] = RE_CHREF.sub(_chapter_link, parts[i])
    return "".join(parts)


def text(s):
    """Inline Markdown, then the chapter links: every paragraph and list item goes through this."""
    return link_chapters(inline(s))


def label_key(s):
    """A span label or quoted name, compared loosely: case, curly quotes, italics, end punctuation."""
    s = s.replace(LQ, '"').replace(RQ, '"').replace("\N{RIGHT SINGLE QUOTATION MARK}", "'")
    s = s.replace("\N{LEFT SINGLE QUOTATION MARK}", "'").replace("*", "").replace("_", " ")
    return " ".join(s.lower().split()).strip(" .?!:,;\"'")


def era_order(label):
    """1 to 10 for an era label in any of the book's spellings ("The 1500s", "2000 to Today"), else None."""
    s = " ".join(re.sub(r"\s*[-\N{EN DASH}]\s*", " to ", label.lower()).split())
    s = re.sub(r"^the\s+", "", s)
    return CANON_ERAS.index(s) + 1 if s in CANON_ERAS else None


# ---------- block markdown ----------
RE_HEAD = re.compile(r"^(#{1,6})\s+(.*)$")
RE_ITEM = re.compile(r"^[-*]\s+(.*)$")
RE_KN = re.compile(r"^\*\*(Known|Not known|Disputed):\*\*\s*(.*)$")
RE_BY = re.compile(r"^\*\*(By\b[^*]*?(?:\d{3,4}s?|today)):\*\*\s*(.*)$")
RE_STRIP = re.compile(r"^\*\*(Era (\d+) of (\d+) · .+?)\*\*\s*$")
RE_CARD = re.compile(r"^\*\*(Chapter \d+ of \d+ · .+?)\*\*\s*$")
RE_BOLD_LINE = re.compile(r"^\*\*([^*](?:.*?[^*])?)\*\*$")
KN_KIND = {"Known": "known", "Not known": "notknown", "Disputed": "disputed"}


class Plain:
    """How md_blocks renders one block's paragraphs and lists. This base: plain text, chapter links.
    The subclasses give the furniture its classes; c is the chapter being rendered (or None)."""

    def __init__(self, c=None):
        self.c = c
        self.next_list = ""     # class for the list that follows a list head

    def heading(self, level, raw):
        pass

    def para(self, s, list_follows):
        if RE_STRIP.match(s):
            warn(f'{self.c["slug"] if self.c else "matter"}: an era strip that is not the first line of '
                 f"its era: {s[:50]}")
            return strip_html(s, 0)
        return f"<p>{text(s)}</p>"

    def items(self, items):
        cls, self.next_list = self.next_list, ""
        tag = "ol" if cls == "qs" else "ul"
        attr = f' class="{cls}"' if cls else ""
        return f"<{tag}{attr}>" + "".join(self.item(i, cls) for i in items) + f"</{tag}>"

    def item(self, s, cls):
        if cls == "dates":
            d, sep, rest = s.partition(": ")
            if sep:
                return f'<li><span class="date">{inline(d)}:</span> {text(rest)}</li>'
        return f"<li>{text(s)}</li>"


class Body(Plain):
    """Era and span zooms and story boxes: "By [year]" lines."""

    def para(self, s, list_follows):
        m = RE_BY.match(s)
        if m:
            count("by")
            return f'<p class="byline"><span class="by">{inline(m.group(1))}:</span> {text(m.group(2))}</p>'
        return super().para(s, list_follows)


class Opening(Plain):
    """The chapter opening card."""

    def __init__(self, c):
        super().__init__(c)
        self.label = self.spine = False

    def para(self, s, list_follows):
        m = RE_CARD.match(s)
        if m and not self.label:
            self.label = True
            return f'<p class="card-label">{inline(m.group(1))}</p>'
        b = RE_BOLD_LINE.match(s)
        if b and list_follows:
            self.next_list = "qs" if "question" in s.lower() else ""
            return f'<p class="qhead">{inline(b.group(1))}</p>'
        if b and not self.spine:
            self.spine = True
            return f'<p class="card-spine">{text(b.group(1))}</p>'
        if s.startswith("**Five minutes?**"):
            count("five")
            return f'<p class="card-five">{span_links(s, self.c["five"])}</p>'
        if s.startswith("**Can skip:**"):
            count("skip")
            return f'<p class="card-skip">{span_links(s, self.c["skip"])}</p>'
        return super().para(s, list_follows)


class Closing(Plain):
    """The chapter closing, the card's partner. Its answers start with the card's three questions,
    word for word (ARCHITECTURE-GUIDE 4.1); the question is set in bold, and a mismatch is a warning."""

    def __init__(self, c):
        super().__init__(c)
        self.qn = 0

    def item(self, s, cls):
        if cls != "qs":
            return super().item(s, cls)
        qs, n = self.c.get("questions", []), self.qn
        self.qn += 1
        q = qs[n] if n < len(qs) and s.startswith(qs[n]) else None
        if q is None:
            warn(f'{self.c["slug"]}: closing answer {n + 1} does not start with the card\'s question {n + 1} '
                 f"word for word: {s[:60]!r}")
            q, sep, _ = s.partition("? ")
            q = q + "?" if sep else ""
        if not q:
            return f"<li>{text(s)}</li>"
        return f'<li><span class="q">{text(q)}</span> {text(s[len(q):].strip())}</li>'

    def para(self, s, list_follows):
        b = RE_BOLD_LINE.match(s)
        if b and list_follows:
            low = s.lower()
            self.next_list = "qs" if "question" in low else "dates" if "date" in low else ""
            return f'<p class="qhead">{inline(b.group(1))}</p>'
        for lab, cls in (("**What changed:**", "close-changed"), ("**Where to go:**", "close-where"),
                         ("**Next:**", "close-next")):
            if s.startswith(lab):
                if cls == "close-next":
                    count("next")
                return f'<p class="{cls}">{text(s)}</p>'
        return super().para(s, list_follows)


class Closer(Plain):
    """An era closer ("By 1850"): every line its own paragraph inside the panel."""

    def para(self, s, list_follows):
        if s.startswith("**If you remember one thing:**"):
            return f'<p class="closer-one">{text(s)}</p>'
        if s.startswith("**Next:**"):
            count("next")
            return f'<p class="closer-next">{text(s)}</p>'
        return super().para(s, list_follows)


class Back(Plain):
    """A back-matter file built by tools/build_backmatter.py: every list line links to its target."""

    def __init__(self, what):
        super().__init__(None)
        self.what, self.section = what, ""

    def heading(self, level, raw):
        self.section = raw.strip()

    def items(self, items):
        return '<ul class="bml">' + "".join(back_item(self.what, self.section, i) for i in items) + "</ul>"


def records(quote):
    recs = []
    for q in quote:
        if not q:
            continue
        m = re.match(r"\*\*(.+?):\*\*\s*(.*)", q)
        if m:
            recs.append([m.group(1), m.group(2)])
        elif recs:
            recs[-1][1] += " " + q
        else:
            recs.append(["", q])
    out = []
    for k, v in recs:
        if not k:
            out.append(f'<div class="rec">{text(v)}</div>')
            continue
        who = k.strip().lower() == "who"
        if who:
            count("who")
        out.append(f'<div class="rec{" who" if who else ""}"><span class="k">{inline(k)}:</span> {text(v)}</div>')
    return f'<div class="records">{"".join(out)}</div>'


def kn_panel(rows):
    out = []
    for s in rows:
        m = RE_KN.match(s)
        count(KN_KIND[m.group(1)])
        out.append(f'<div class="kn-row"><span class="kn-k">{m.group(1)}:</span>'
                   f'<span class="kn-v">{text(m.group(2))}</span></div>')
    return f'<div class="kn">{"".join(out)}</div>'


def md_blocks(lines, head_shift=0, ctx=None):
    """Render Markdown lines to HTML (the book's subset). Every non-blank line is its own paragraph
    (see the docstring); consecutive '- ' lines are one list, consecutive '>' lines one record box,
    consecutive Known / Not known / Disputed lines one panel. ctx (a Plain) gives furniture its classes."""
    ctx = ctx or Plain()
    toks = []
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            toks.append(("", ""))
            continue
        h = RE_HEAD.match(line)
        if h:
            toks.append(("h", h))
        elif line.startswith(">"):
            toks.append((">", line[1:].strip()))
        else:
            li = RE_ITEM.match(line)
            toks.append(("li", li.group(1)) if li else ("p", line.strip()))
    out, i = [], 0
    while i < len(toks):
        kind, val = toks[i]
        if kind == "h":
            lvl = min(6, len(val.group(1)) + head_shift)
            ctx.heading(lvl, val.group(2))
            out.append(f"<h{lvl}>{inline(val.group(2))}</h{lvl}>")
            i += 1
        elif kind in (">", "li"):
            j = i
            while j < len(toks) and toks[j][0] == kind:
                j += 1
            group = [v for _, v in toks[i:j]]
            out.append(records(group) if kind == ">" else ctx.items(group))
            i = j
        elif kind == "p" and RE_KN.match(val):
            j = i
            while j < len(toks) and toks[j][0] == "p" and RE_KN.match(toks[j][1]):
                j += 1
            out.append(kn_panel([v for _, v in toks[i:j]]))
            i = j
        elif kind == "p":
            out.append(ctx.para(val, i + 1 < len(toks) and toks[i + 1][0] == "li"))
            i += 1
        else:
            i += 1
    return "\n".join(out)


def strip_html(s, order):
    """The era strip: a ten-square ribbon (this era's square filled) and the strip's own words."""
    m = RE_STRIP.match(s)
    if order and int(m.group(2)) != order:
        warn(f'{CUR["c"]["slug"] if CUR["c"] else "matter"}: era {order} strip says "Era {m.group(2)}"')
    count("strip")
    squares = "".join(f'<i class="e{k}{" on" if k == order else ""}"></i>' for k in range(1, 11))
    cls = f" e{order}" if order else ""
    return (f'<p class="strip{cls}"><span class="ribbon" aria-hidden="true">{squares}</span>'
            f'<span class="strip-t">{inline(m.group(1))}</span></p>')


def span_links(s, resolved):
    """A "Five minutes?" or "Can skip:" line with each quoted name linked to its span."""
    h = text(s)
    for name, t in resolved:
        if not t:
            continue
        inner = inline(name)
        for q1, q2 in (('"', '"'), (LQ, RQ)):
            old = q1 + inner + q2
            if old in h:
                h = h.replace(old, f'{q1}<a class="spanlink" href="#{t["id"]}">{inner}</a>{q2}', 1)
                break
    return h


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
    return max(5, int(words / WPM / 5 + 0.5) * 5)


def load_chapter(c):
    """Parse one chapter and lift out its opening and closing cards.
    Adds to c: eras, opening, closing (block tuples or None), words, minutes, card_minutes, and the
    lookups of index_chapter()."""
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
    index_chapter(c)
    return c


def index_chapter(c):
    """Ids and lookups for one loaded chapter: era ids, span ids (written into the block's attrs as
    _id), the story list, each era's text and words, and the spans the opening card names."""
    slug = c["slug"]
    c.update(era_ids={}, era_label={}, era_txt={}, era_low={}, era_words={}, spans=[], stories=[])
    n = 0
    for e in c["eras"]:
        o = era_num(e)
        c["era_ids"][o] = f"era-{slug}-{o}"
        c["era_label"][o] = e["heading"] or e["label"]
        texts = []
        for kind, attrs, lines in e["blocks"]:
            texts.append(attrs.get("label", "") + "\n" + "\n".join(lines))
            if kind == "zoom" and attrs.get("level") == "span" and attrs.get("label"):
                n += 1
                attrs["_id"] = f"span-{slug}-{n}"
                c["spans"].append({"id": attrs["_id"], "label": attrs["label"], "era": o,
                                   "words": block_words(lines)})
            elif kind == "story":
                head = next((l.strip() for l in lines if l.strip()), "")
                title = re.sub(r"^#{1,6}\s+", "", head) if head.startswith("#") else attrs.get("name", "")
                movie = next((l for l in lines if re.match(r"^>\s*\*\*Movie:\*\*", l)), "")
                c["stories"].append({"id": f'story-{attrs.get("slug", "")}', "name": attrs.get("name", ""),
                                     "title": title, "era": o, "low": label_key("\n".join(lines)),
                                     "words": " " + " ".join(name_words(" ".join(lines))) + " ",
                                     "movie": re.sub(r"^>\s*\*\*Movie:\*\*", "", movie) or attrs.get("movie", "")})
        c["era_txt"][o] = "\n".join(texts)
        c["era_low"][o] = c["era_txt"][o].lower()
        c["era_words"][o] = sum(block_words(b[2]) for b in e["blocks"])
    c["closing_txt"] = "\n".join(c["closing"][2]) if c["closing"] else ""
    c["card_txt"] = "\n".join(c["opening"][2]) if c["opening"] else ""
    c["five"], c["skip"], c["questions"] = [], [], []
    in_qs = False
    for l in (c["opening"][2] if c["opening"] else []):
        s = l.strip()
        item = RE_ITEM.match(s)
        if in_qs and item:
            c["questions"].append(item.group(1).strip())
            continue
        in_qs = bool(RE_BOLD_LINE.match(s)) and "question" in s.lower()
        if s.startswith("**Five minutes?**"):
            c["five"] = resolve_names(c, s, "Five minutes?")
        elif s.startswith("**Can skip:**"):
            c["skip"] = resolve_names(c, s, "Can skip:")


RE_QUOTED = re.compile(f'"([^"]+)"|{LQ}([^{RQ}]+){RQ}')


def resolve_names(c, line, what):
    """[(name, span or story dict, or None)] for every quoted name on a card's line, with a warning
    for a name that matches no span (a loose or story match is linked, and still warned)."""
    out, eras_said = [], []
    for m in RE_QUOTED.finditer(line):
        name = m.group(1) or m.group(2)
        # the era written right after this name, if any ("... in 1800 to 1850")
        e = re.match(r"\s+in\s+(before 1500|the 1[56]00s|\d{4} to (?:\d{4}|today))", line[m.end():], re.I)
        eras_said.append(e.group(1) if e else None)
        key = label_key(name)
        hits = [s for s in c["spans"] if label_key(s["label"]) == key]
        if not hits:
            loose = [s for s in c["spans"] if key and (label_key(s["label"]).startswith(key)
                                                      or key.startswith(label_key(s["label"])))]
            stories = [s for s in c["stories"] if key in (label_key(s["name"]), label_key(s["title"]))]
            if len(loose) == 1:
                hits = loose
                warn(f'{c["slug"]}: "{what}" names "{name}", which matches no span exactly; '
                     f'linked to "{loose[0]["label"]}"')
            elif stories:
                hits = stories
                warn(f'{c["slug"]}: "{what}" names "{name}", a story box, not a span; linked to the story')
            else:
                warn(f'{c["slug"]}: "{what}" names "{name}", which matches no span in the chapter')
        elif len(hits) > 1:
            warn(f'{c["slug"]}: "{what}" names "{name}", which {len(hits)} spans share; linked to the first')
        out.append((name, hits[0] if hits else None))
    if what == "Five minutes?":
        for (name, hit), said_txt in zip(out, eras_said):
            if not (hit and "label" in hit and said_txt):
                continue
            if era_order(said_txt) != hit["era"]:
                warn(f'{c["slug"]}: "Five minutes?" says "{name}" is in {said_txt}, but it is in '
                     f'{c["era_label"].get(hit["era"], hit["era"])}')
    return out


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


# ---------- front-matter numbers ----------
RE_TOKEN = re.compile(r"\{\{\s*([a-z0-9_]+)\s*\}\}")


def time_words(minutes, step):
    """Minutes rounded to step, in words: "50 minutes", "1 hour", "2 hours 15 minutes"."""
    m = max(step, int(minutes / step + 0.5) * step)
    h, mm = divmod(m, 60)
    bits = ([f'{h} hour{"s" if h != 1 else ""}'] if h else []) + ([f"{mm} minutes"] if mm else [])
    return " ".join(bits)


def book_numbers(chapters, before):
    """The values of the front-matter tokens (see the docstring), from the build's own counts."""
    if not chapters:
        return {}
    words = sum(c["words"] for c in chapters)
    times = sorted((reading_minutes(c["words"]), c["title"]) for c in chapters)
    k = max(1, round(len(times) * 0.1))
    mid = times[k:-k] or times
    card = sum(block_words(c["opening"][2]) for c in chapters if c["opening"])
    close = sum(block_words(c["closing"][2]) for c in chapters if c["closing"])
    five = sum(t["words"] for c in chapters for _, t in c["five"][:1] if t and "words" in t)
    ten = next((m for m in before if "ten-minute" in m["id"]), None)
    ten_words = block_words(ten["lines"]) if ten else 0
    nums = {
        "words_per_minute": str(WPM),
        "book_words": f"{int(round(words, -4)):,}",
        "book_words_exact": f"{words:,}",
        "book_hours": str(round(words / WPM / 60)),
        "story_count": str(sum(len(c["stories"]) for c in chapters)),
        "shortest_chapter": times[0][1], "shortest_chapter_time": time_words(times[0][0], 5),
        "longest_chapter": times[-1][1], "longest_chapter_time": time_words(times[-1][0], 5),
        "most_chapters_from": time_words(mid[0][0], 5), "most_chapters_to": time_words(mid[-1][0], 5),
        "cards_time": time_words(card / WPM, 5), "closings_time": time_words(close / WPM, 5),
        "five_minutes_time": time_words(five / WPM, 15),
        "short_road_time": time_words((ten_words + card + close + five) / WPM, 15),
    }
    for o in range(1, 11):
        nums[f"era{o}_time"] = time_words(sum(c["era_words"].get(o, 0) for c in chapters) / WPM, 15)
    return nums


def fill_tokens(sections, nums):
    """Replace {{token}} in front, back and introduction lines with the build's own numbers."""
    for m in sections:
        def rep(t, sid=m["id"]):
            if t.group(1) in nums:
                return nums[t.group(1)]
            warn(f"{sid}: unknown token {t.group(0)} left as typed (the tokens are listed in "
                 f"tools/build_full_book.py)")
            return t.group(0)
        m["lines"] = [RE_TOKEN.sub(rep, l) for l in m["lines"]]
        m["title"], m["toc"] = RE_TOKEN.sub(rep, m["title"]), RE_TOKEN.sub(rep, m.get("toc", m["title"]))


def prepare_book():
    """Everything both builds need, in book order, with the front-matter tokens filled in:
    (chapters, parts, before, after)."""
    chapters, parts = read_registry()
    if len(chapters) != 37:
        warn(f"registry has {len(chapters)} chapters (expected 37)")
    CHAPTERS.clear()
    CHAPTERS.update({int(c["num"]): c for c in chapters})
    before, after = load_matters()
    for c in chapters:
        load_chapter(c)
    NUMBERS.clear()
    NUMBERS.update(book_numbers(chapters, before))
    fill_tokens(before + after, NUMBERS)
    return chapters, parts, before, after


# ---------- back matter ----------
RE_BM = re.compile(r"^\*\*(?P<name>.+?)\*\*:?\s*(?P<text>.*?)\s*"
                   r"\((?P<ref>Chapter (?P<num>\d+)(?:,\s*(?P<rest>[^()]*))?)\)\s*$")
BACK_KINDS = ("glossary", "timeline", "people", "places", "movies", "answers")
_HANDOFF = {}


def handoff_glossary(slug):
    """term (lower case) -> era label, from the chapter's hand-off file (control/backmatter/<slug>.md)."""
    if slug in _HANDOFF:
        return _HANDOFF[slug]
    out, sec = {}, None
    p = HANDOFF / f"{slug}.md"
    for line in (p.read_text(encoding="utf-8").splitlines() if p.exists() else []):
        h = re.match(r"^##\s+(.+?)\s*$", line)
        if h:
            sec = h.group(1).strip().lower()
            continue
        m = re.match(r"^\s*[-*]\s+(.*\S)\s*$", line)
        if sec != "glossary" or not m:
            continue
        item = m.group(1)
        for cm in re.finditer(": ", item):
            left = item[:cm.start()]
            if left.count('"') % 2 == 0 and all(left.count(a) == left.count(b) for a, b in ("()", "[]")):
                era = re.search(r"\(([^()]*)\)\s*$", item[cm.end():])
                if era:
                    out.setdefault(left.strip().lower(), era.group(1))
                break
    _HANDOFF[slug] = out
    return out


def find_era(c, key, case=False):
    """The first era of chapter c whose text names key (from the start of a word), or None.
    case=True compares capitals too, for proper names that are also plain words ("Glacier")."""
    if len(key) < 3:
        return None
    pat = re.compile(r"(?<!\w)" + re.escape(key if case else key.lower()))
    for o in sorted(c["era_low"]):
        if pat.search(c["era_txt"][o] if case else c["era_low"][o]):
            return o
    return None


def name_words(s):
    s = "".join(ch for ch in unicodedata.normalize("NFKD", s) if not unicodedata.combining(ch))
    s = re.sub(r'"[^"]*"|\([^)]*\)', " ", s.lower().replace(LQ, '"').replace(RQ, '"'))
    return [w for w in re.sub(r"[^a-z0-9 ]+", " ", s).split() if w not in ("jr", "sr", "ii", "iii", "iv")]


def find_story(c, name, era):
    """The story box of chapter c for a person: by its name (exact, then without initials, then a
    shared box whose name holds the whole name: "Lewis and William Clark"), then by its text for
    people a box tells together (a crew): the whole name, else every longer word of it, else the
    surname. The line's era decides between several."""
    def pick(hits):
        here = [h for h in hits if h["era"] == era]
        if len(here) == 1 or (len(hits) == 1 and not here):
            return (here or hits)[0]
        return None
    want = name_words(name)
    exact = [s for s in c["stories"] if want in (name_words(s["name"]), name_words(s["title"]))]
    if exact:
        return pick(exact) or exact[0]
    core = [w for w in want if len(w) > 1]
    trim = [s for s in c["stories"] if [w for w in name_words(s["name"]) if len(w) > 1] == core]
    if trim:
        return pick(trim) or trim[0]
    long_words = [w for w in want if len(w) > 2]
    tests = [lambda s: long_words and all(w in name_words(s["name"] + " " + s["title"]) for w in long_words),
             lambda s: f' {" ".join(want)} ' in s["words"],
             lambda s: long_words and all(f" {w} " in s["words"] for w in long_words),
             lambda s: long_words and f" {long_words[-1]} " in s["words"]]
    for test in tests:
        hits = [s for s in c["stories"] if test(s)]
        if hits and pick(hits):
            return pick(hits)
    return None


PLACE_JOIN = {"of", "de", "del", "la", "the", "and", "on", "at"}
PLACE_COMMON = {"National", "Museum", "Park", "State", "House", "Center", "Historic", "Historical", "Site",
                "Memorial", "Monument", "Library", "Hall", "Street", "Church", "School", "University", "Trail"}


def place_keys(name):
    """Search keys for a place line, most exact first: [(key, case-sensitive)]. The name without
    its notes in brackets; a capitalised name in brackets ("Fort Marion"); runs of capitalised words
    from every part ("Daisy Bates" from "Daisy Bates home"); last, single longer proper words."""
    name = name.replace('"', "").replace(LQ, "").replace(RQ, "")
    segs, depth, cur = [], 0, ""
    for ch in name:                       # split at the commas outside brackets
        depth += (ch == "(") - (ch == ")")
        if ch == "," and depth == 0:
            segs.append(cur)
            cur = ""
        else:
            cur += ch
    segs = [s.strip() for s in segs + [cur] if s.strip()]
    first = re.sub(r"\s*\([^)]*\)", "", segs[0]).strip() if segs else ""
    keys = [(first, False)]
    keys += [(p.strip(), True) for p in re.findall(r"\(([^)]*)\)", name) if p.strip()[:1].isupper()]
    runs = []
    for seg in segs:
        cur = []
        for w in re.findall(r"[A-Za-z][\w'.-]*", re.sub(r"\([^)]*\)", " ", seg)) + [""]:
            w = re.sub(r"'s$", "", w)
            if w[:1].isupper():
                cur.append(w)
            elif w in PLACE_JOIN and cur:
                cur.append(w)
            else:
                if cur:
                    runs.append(cur)
                cur = []
    subs = []
    for r in runs:
        for n in range(len(r), 1, -1):
            subs += [r[i:i + n] for i in range(len(r) - n + 1)
                     if r[i] not in PLACE_JOIN and r[i + n - 1] not in PLACE_JOIN]
    keys += [(" ".join(s), True) for s in sorted(subs, key=len, reverse=True)]
    singles = [w for w in (runs[0] if runs else []) if len(w) >= 5 and w not in PLACE_COMMON and w[:1].isupper()]
    keys += [(w, True) for w in sorted(singles, key=len, reverse=True)]
    seen, out = set(), []
    for k in keys:
        if k[0] and k not in seen:
            seen.add(k)
            out.append(k)
    return out


def back_target(what, section, m, c):
    """(target id, None) for one back-matter line, or (None, why not)."""
    name = m["name"]
    if what == "people":
        st = find_story(c, name, era_order(m["rest"] or ""))
        return (st["id"], None) if st else (None, "matches no story box name in the chapter")
    if what == "movies":
        key = label_key(re.sub(r"\s*\([^()]*\)\s*$", "", name))
        hits = ([s for s in c["stories"] if key and key in label_key(s["movie"])]
                or [s for s in c["stories"] if len(key) > 3 and key in s["low"]])
        if hits:
            return hits[0]["id"], None
        o = find_era(c, key)
        return (c["era_ids"][o], None) if o else (None, "is named in no story box and no era of the chapter")
    if what == "timeline":
        o = era_order(section)
        return (c["era_ids"][o], None) if o in c["era_ids"] else (None, f"the chapter has no era {section!r}")
    if what == "glossary":
        # a word split by meaning carries a label in brackets ("bond (in court)"): look up the word itself
        base = re.sub(r"\s*\([^()]*\)\s*$", "", name).strip() or name
        hg = handoff_glossary(c["slug"])
        o = era_order(hg.get(name.lower(), "") or hg.get(base.lower(), ""))
        yr = re.search(r"\((\d{4})\)\s*$", name)        # "Treaty of Paris (1898)": the era that has the year
        if yr:
            o = next((k for k in sorted(c["era_low"]) if base.lower() in c["era_low"][k]
                      and yr.group(1) in c["era_txt"][k]), None) or o
        if o not in c["era_ids"]:
            o = None
            for variant in (base, base.replace("-", ""), base.replace("-", " ")):    # "feeble-minded"
                o = find_era(c, variant)
                if o:
                    break
        if not o:
            # the chapter may use another form of the word ("ratified", "foundries"): try its stem
            first = base.split()[0]
            for n in range(len(first) - 1, max(4, len(first) - 3) - 1, -1):
                o = find_era(c, first[:n])
                if o:
                    break
        return (c["era_ids"][o], None) if o else (None, "the word is not in the chapter's eras")
    if what == "places":
        for key, case in place_keys(name):
            o = find_era(c, key, case)
            if o:
                return c["era_ids"][o], None
            for txt, tid in ((c["closing_txt"], f'closing-{c["slug"]}'), (c["card_txt"], f'card-{c["slug"]}')):
                if txt and len(key) >= 3 and re.search(r"(?<!\w)" + re.escape(key), txt, 0 if case else re.I):
                    return tid, None
        return None, "the place is not named in the chapter"
    return None, "unknown back-matter kind"


def bm_li(what, inner, tid):
    BACKLINKS.setdefault(what, Counter())["lines"] += 1
    return (f'<li class="bm"><span class="bm-t">{inner}</span>'
            f'<a class="bm-pg" href="#{tid}"><span class="pg" data-for="{tid}"></span></a></li>')


def back_item(what, section, s):
    """One back-matter line: its text, its reference linked to its target, and a page-number slot."""
    if what == "answers":
        m = re.match(r"Chapter (\d+)\b", section)
        c = CHAPTERS.get(int(m.group(1))) if m else None
        if c is None:
            warn(f"answers: a line under {section!r}, which names no chapter; not linked")
            return f"<li>{text(s)}</li>"
        if not c["closing"]:
            warn(f'answers: Chapter {int(c["num"])} has no "Chapter closing" block yet; linked to the chapter')
            BACKLINKS.setdefault(what, Counter())["chapter only"] += 1
        tid = f'closing-{c["slug"]}' if c["closing"] else f'ch-{c["slug"]}'
        return bm_li(what, text(s), tid)
    m = RE_BM.match(s)
    c = CHAPTERS.get(int(m["num"])) if m else None
    if c is None:
        warn(f"{what}: not in the form '**name**: text (Chapter N ...)' or no such chapter: {s[:70]!r}")
        return f"<li>{text(s)}</li>"
    tid, why = back_target(what, section, m, c)
    if tid is None:
        warn(f'{what}: "{m["name"]}" (Chapter {int(m["num"])}) {why}; linked to the chapter')
        BACKLINKS.setdefault(what, Counter())["chapter only"] += 1
        tid = f'ch-{c["slug"]}'
    head = f'<strong>{inline(m["name"])}</strong>' + (f': {text(m["text"])}' if m["text"] else "")
    if what == "glossary" and m["rest"]:
        ref = f'<a href="#{tid}">Chapter {int(m["num"])}</a>, {text(m["rest"])}'
    else:
        ref = f'<a href="#{tid}">{inline(m["ref"])}</a>'
    return bm_li(what, f"{head} ({ref})", tid)


def story_html(attrs, lines, ecls=""):
    name = attrs.get("name", "")
    body = list(lines)
    title = name
    # use the visible ### heading if present; drop it from the body
    for i, l in enumerate(body):
        if l.strip():
            h = re.match(r"^#{1,6}\s+(.*)$", l.strip())
            if h:
                title = h.group(1).strip()
                # a heading may add a nickname in quotes or brackets ('Barbara "Dusty" Roads'); that is
                # by design (the viewer decision of T-658), so only a different name is worth a warning
                nick = lambda s: re.sub(r"(?<!\w)'([^'\s][^']*)'(?!\w)", r'"\1"', s)    # 'Pap' as "Pap"
                if name and title != name and name_words(nick(title)) != name_words(nick(name)):
                    warn(f"story {attrs.get('slug')}: heading {title!r} != name {name!r}")
                body = body[i + 1:]
            break
    return (f'<section class="story{ecls}" data-b="{next_b()}" id="story-{html.escape(attrs.get("slug", ""))}">'
            f"<h4>{inline(title)}</h4>\n{md_blocks(body, 2, Body(CUR['c']))}</section>")


def zoom_html(attrs, lines, ecls=""):
    label = attrs.get("label", "")
    if attrs.get("level") == "span" and label:
        sid = f' id="{attrs["_id"]}"' if attrs.get("_id") else ""
        seam = ""
        k = next((x for x, l in enumerate(lines) if l.strip()), None)
        if k is not None and RE_BY.match(lines[k].strip()):
            # a "By [year]" line that opens a span states where things stand after the spans before
            # it, so it prints at the seam, above this span's heading
            seam = f'<div class="seam{ecls}">' + Body(CUR["c"]).para(lines[k].strip(), False) + "</div>\n"
            lines = lines[:k] + lines[k + 1:]
        return (seam + f'<div class="zoom{ecls}" data-b="{next_b()}"{sid}><h4 class="span">{inline(label)}</h4>\n'
                + md_blocks(lines, 2, Body(CUR["c"])) + "</div>")
    if attrs.get("level") == "era" and re.match(r"By\b", label):
        count("closer")
        return (f'<div class="zoom closer{ecls}"><p class="closer-label">{inline(label)}</p>\n'
                + md_blocks(lines, 2, Closer(CUR["c"])) + "</div>")
    return f'<div class="zoom{ecls}">' + md_blocks(lines, 2, Body(CUR["c"])) + "</div>"


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
    with its target b, kind (chapter, era, span, story, matter, other), text and element id
    (a story box's or span's id is its wrapper's)."""
    heads = []

    def plain(s):
        return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()

    def sub(m):
        if m.group(1):  # wrapper with its heading
            whole = m.group(0)
            kind = "story" if whole.startswith("<section") else "span"
            wid = re.search(r'\bid="([^"]*)"', whole[:whole.index(">")])
            heads.append({"b": int(m.group(1)), "kind": kind, "text": plain(m.group(4)),
                          "id": wid.group(1) if wid else None})
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
    """A front/back matter section: its # heading becomes an h2 carrying the anchor. Back-matter files
    made by build_backmatter.py (glossary, timeline, people, places, movies, answers) link every line."""
    what = next((k for k in BACK_KINDS if k in m["id"]), None) if m["id"].startswith("back-") else None
    ctx = Back(what) if what else Plain()
    return (f'<section class="{cls}">'
            + md_blocks(m["lines"], 1, ctx).replace("<h2>", f'<h2 id="{m["id"]}">', 1) + "</section>")


def grid_page(chapters, parts):
    """The grid: 37 chapters by 10 eras, each cell the page where that era of that chapter starts."""
    head = ('<thead><tr><th class="gc">Chapter</th>'
            + "".join(f'<th class="e{k}">{lab}</th>' for k, lab in enumerate(GRID_HEAD, 1)) + "</tr></thead>")
    rows, last = [], None
    for c in chapters:
        if c["part"] != last:
            last = c["part"]
            rows.append(f'<tr class="gp"><th colspan="11">Part {last}: {html.escape(parts.get(last, ""))}</th></tr>')
        cells = "".join(f'<td><a href="#{c["era_ids"][k]}"><span class="pg" data-for="{c["era_ids"][k]}"></span></a></td>'
                        if k in c["era_ids"] else "<td></td>" for k in range(1, 11))
        rows.append(f'<tr><th class="gch"><a href="#ch-{c["slug"]}"><span class="n">{int(c["num"])}</span>'
                    f'{html.escape(c["title"])}</a></th>{cells}</tr>')
    return ('<section class="gridpage"><h2 id="grid">The Grid</h2>'
            '<p class="gnote">Each row is a chapter and each column is an era. The number is the page where '
            "that era of the chapter begins. Read across a row to follow one subject through time, or down "
            "a column to see every subject in one era.</p>"
            f'<table class="grid"><colgroup><col class="gcol">{"<col>" * 10}</colgroup>{head}'
            f'<tbody>{"".join(rows)}</tbody></table></section>')


# ---------- era colours ----------
def _lum(hexc):
    def lin(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(int(hexc[i:i + 2], 16)) for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _contrast(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def _grey(hexc):
    y = _lum(hexc)
    return 116 * y ** (1 / 3) - 16 if y > 0.008856 else 903.3 * y


def check_palette():
    """The era colours draw rules, bars and ribbon squares, never text. Each needs 3:1 against the
    white page and the story-box tint (WCAG non-text contrast), and each pair of neighbours must stay
    apart when printed in grey (at least 2.5 L*). Returns a one-line summary; misses are warnings."""
    on_page = [_contrast(c, "#ffffff") for c in ERA_COLOURS]
    on_box = [_contrast(c, BOX_TINT) for c in ERA_COLOURS]
    greys = [_grey(c) for c in ERA_COLOURS]
    steps = [abs(b - a) for a, b in zip(greys, greys[1:])]
    for k, (p, b) in enumerate(zip(on_page, on_box), 1):
        if min(p, b) < 3:
            warn(f"era colour {k} ({ERA_COLOURS[k - 1]}): contrast {min(p, b):.2f}:1, below 3:1")
    for k, s in enumerate(steps, 1):
        if s < 2.5:
            warn(f"era colours {k} and {k + 1} print as nearly the same grey ({s:.1f} L* apart)")
    ink = _contrast("#1d1d1f", BOX_TINT)
    return (f"era colours: {min(on_page):.1f} to {max(on_page):.1f}:1 on the page, {min(on_box):.1f} to "
            f"{max(on_box):.1f}:1 on the box tint, grey steps {min(steps):.1f} to {max(steps):.1f} L*, "
            f"ink on the tint {ink:.1f}:1")


def era_css():
    light = " ".join(f"--e{k}:{c};" for k, c in enumerate(ERA_COLOURS, 1))
    dark = " ".join(f"--e{k}:{c};" for k, c in enumerate(ERA_COLOURS_DARK, 1))
    classes = "\n".join(f".e{k} {{ --era: var(--e{k}); }}" for k in range(1, 11))
    return (f":root {{ {light} }}\n@media (prefers-color-scheme: dark) {{ @media screen {{ :root {{ {dark} }} }} }}\n"
            + classes)


# ---------- assemble ----------
# Page geometry. tools/make_pdf.py reads PAGE_H, MARGIN_TOP and MARGIN_BOTTOM (points) to find the
# middle of the text area, so keep them in step with the @page rule below. The side margins give a
# column of about 72 characters at 12 pt.
PAGE_H, MARGIN_TOP, MARGIN_BOTTOM = 792.0, 0.85 * 72, 0.95 * 72

CSS = """
@page { size: letter; margin: 0.85in 1.35in 0.95in 1.35in;
  @bottom-center { content: counter(page); font: 9pt "Segoe UI", Calibri, Arial, sans-serif; color: #777; } }
@page cover { @bottom-center { content: none; } }
@page grid { margin: 0.6in 0.6in 0.7in 0.6in; }
:root { --ink:#1d1d1f; --dim:#5a5a5f; --accent:#1f4e79; --rule:#d6d6d6; --soft:#f6f2ea; --panel:#f3efe6;
  --card:#fbf9f4; --bg:#fffefb; }
@media (prefers-color-scheme: dark) { @media screen {
  :root { --ink:#e6e6e6; --dim:#a8a8ad; --accent:#8cb8e6; --rule:#3a3a3e; --soft:#24262b; --panel:#2b2d32;
    --card:#1f2024; --bg:#17181b; } } }
* { box-sizing: border-box; }
html { font-size: 12pt; }
body { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", serif; color: var(--ink);
  background: var(--bg); line-height: 1.6; text-align: left; margin: 0 auto; max-width: calc(35em + 32px);
  padding: 2em 16px 4em; }
@media print { body { max-width: none; padding: 0; background: #fff; } a { color: inherit; } }
p, li { text-wrap: pretty; hyphens: none; }
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
h3.era { font-size: 1.3em; border-bottom: 2px solid var(--era, var(--rule)); padding-bottom: .1em; margin-top: 2em; }
h4 { font-size: 1.05em; margin: 1.4em 0 .4em; }
p { margin: .55em 0; orphans: 3; widows: 3; }
li { orphans: 2; widows: 2; }
.story { background: var(--soft); border-left: 4px solid var(--era, var(--accent)); padding: .3em 1em .6em;
  margin: 1.2em 0; border-radius: 3px; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
.story h4 { margin-top: .6em; }
.records { font-size: .92em; color: var(--dim); margin: .4em 0 .8em; break-inside: avoid; }
.rec { margin: .15em 0; }
.rec .k { font-weight: bold; color: var(--ink); }
.records .rec.who { font-size: 1.087em; color: var(--ink); }
nav.toc { break-after: page; }
nav.toc ul { list-style: none; padding: 0; margin: 0; }
nav.toc li { display: flex; align-items: baseline; gap: .4em; margin: .2em 0; break-inside: avoid; }
nav.toc li a { flex: 0 1 auto; }
nav.toc li .lead { flex: 1 1 auto; border-bottom: 1px dotted var(--rule); min-width: 1em;
  transform: translateY(-.25em); }
nav.toc li .pg { flex: 0 0 2.6em; text-align: right; font-variant-numeric: tabular-nums; }
nav.toc li .n { display: inline-block; min-width: 1.7em; color: var(--dim); }
nav.toc li.tp { margin-top: .9em; font-weight: bold; color: var(--accent); break-after: avoid; }
nav.toc .time { color: var(--dim); font-size: .85em; white-space: nowrap; }
a { color: var(--accent); text-decoration: none; }
ul, ol { padding-left: 1.5em; }
section.introduction h2, section.matter h2 { break-before: page; }
.byline .by, .kn-k, .closer-label, .card-label, .qhead, p.strip { font-family: "Segoe UI", Calibri, Arial, sans-serif;
  font-weight: bold; text-transform: uppercase; letter-spacing: .07em; }
p.strip { display: flex; align-items: center; gap: .75em; margin: .35em 0 1em; font-size: .72em;
  line-height: 1.4; color: var(--dim); break-after: avoid; }
.ribbon { display: inline-flex; gap: .25em; flex: none; }
.ribbon i { display: block; width: .95em; height: .95em; border: 1.3px solid var(--era); border-radius: 1px; }
.ribbon i.on { background: var(--era); }
p.byline { border-top: 1px solid var(--era, var(--rule)); padding-top: .5em; margin-top: 1.2em; }
.byline .by { font-size: .78em; color: var(--dim); margin-right: .3em; }
.kn { background: var(--panel); border-radius: 3px; padding: .35em .9em; margin: .8em 0; break-inside: avoid; }
.story .kn { background: var(--bg); }
.kn-row { display: flex; gap: .7em; margin: .2em 0; }
.kn-k { flex: none; width: 7.6em; font-size: .74em; line-height: 2.15; color: var(--dim); }
.kn-v { flex: 1 1 auto; min-width: 0; }
.closer { background: var(--panel); border-top: 3px solid var(--era, var(--rule)); border-radius: 0 0 3px 3px;
  padding: .4em 1em .6em; margin: 1.5em 0 1.2em; break-inside: avoid; }
.closer-label { font-size: .74em; color: var(--dim); margin: .35em 0 .15em; }
.closer p { margin: .4em 0; }
.closer ul { margin: .35em 0; }
.closer-next { border-top: 1px solid var(--rule); padding-top: .45em; }
.card { background: var(--card); border: 1px solid var(--rule); border-top: 4px solid var(--accent);
  border-radius: 3px; padding: .5em 1.2em .8em; margin: 1em 0 1.6em; box-decoration-break: clone;
  -webkit-box-decoration-break: clone; }
.chapter-closing { margin-top: 2.2em; }
.card-label { font-size: .74em; color: var(--dim); margin: .5em 0 .7em; }
.card-spine { font-size: 1.16em; line-height: 1.45; font-weight: bold; margin: .4em 0 .8em; }
.qhead { font-size: .78em; color: var(--accent); margin: 1.1em 0 .25em; break-after: avoid; }
ol.qs { padding-left: 1.7em; margin: .3em 0 .7em; }
ol.qs li { margin: .3em 0; padding-left: .2em; }
ul.dates { list-style: none; padding-left: 0; margin: .3em 0 .7em; }
ul.dates li { margin: .2em 0; }
.date, ol.qs .q { font-weight: bold; }
.seam p.byline { margin-bottom: .2em; }
.card-five, .close-next { border-top: 1px solid var(--rule); padding-top: .55em; margin-top: 1em; }
ul.bml { list-style: none; padding-left: 0; }
li.bm { display: flex; align-items: last baseline; gap: .8em; margin: .25em 0; break-inside: avoid; }
.bm-t { flex: 1 1 auto; min-width: 0; padding-left: 1.2em; text-indent: -1.2em; }
.bm-pg { flex: 0 0 2.6em; text-align: right; font-variant-numeric: tabular-nums; color: inherit; }
section.gridpage { page: grid; }
section.gridpage h2 { margin-top: 0; }
.gnote { font-size: .86em; color: var(--dim); margin: .2em 0 .7em; }
table.grid { width: 100%; border-collapse: collapse; table-layout: fixed; font-family: "Segoe UI", Calibri, Arial, sans-serif;
  font-size: .68em; line-height: 1.2; font-variant-numeric: tabular-nums; }
table.grid col.gcol { width: 30%; }
table.grid thead th { font-weight: bold; color: var(--dim); text-align: center; vertical-align: bottom;
  padding: .3em .1em; border-top: 5px solid var(--era, var(--rule)); border-bottom: 1px solid var(--rule); }
table.grid thead th.gc { text-align: left; border-top: 0; }
table.grid td { text-align: center; padding: .1em 0; border-bottom: 1px solid var(--soft); }
table.grid th.gch { text-align: left; font-weight: normal; padding: .1em .3em .1em 0; white-space: nowrap;
  overflow: hidden; border-bottom: 1px solid var(--soft); }
table.grid th.gch .n { display: inline-block; width: 1.9em; color: var(--dim); }
table.grid tr.gp th { text-align: left; color: var(--accent); font-weight: bold; padding: .45em 0 .1em;
  border-bottom: 1px solid var(--rule); }
table.grid a { color: inherit; }
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
    chapters, parts, before, after = prepare_book()
    SEGMENTS.clear()
    FURN.clear()
    BACKLINKS.clear()

    def segment(name, fragment):
        frag, heads = tag_headings(fragment)
        SEGMENTS.append({"name": name, "html": frag, "heads": heads})

    CUR["c"] = None
    cover = ('<div class="cover">'
             f'<h1 class="book">{BOOK_TITLE}</h1>'
             f'<p class="sub">{len(chapters)} chapters, each told across the same ten eras</p></div>')
    # table of contents
    toc = ['<nav class="toc"><h2>Contents</h2><ul>', toc_line("grid", "The Grid")]
    toc += [toc_line(m["id"], inline(m["toc"])) for m in before]
    last_part = None
    for c in chapters:
        if c["part"] != last_part:
            last_part = c["part"]
            toc.append(f'<li class="tp">Part {last_part}: {html.escape(parts.get(last_part, ""))}</li>')
        time_ = f' <span class="time">about {c["card_minutes"]} min</span>' if c["card_minutes"] else ""
        toc.append(toc_line(f'ch-{c["slug"]}', html.escape(c["title"]), int(c["num"]), time_))
    toc += [toc_line(m["id"], inline(m["toc"])) for m in after]
    toc.append('</ul></nav>')
    # front matter and introduction: each file's # heading becomes h2, ## becomes h3
    segment("front", cover + "\n".join(toc) + "\n" + grid_page(chapters, parts) + "\n"
            + "\n".join(render_matter(m, "introduction" if m["id"] == "introduction" else "matter")
                        for m in before))

    last_part = None
    for c in chapters:
        CUR["c"] = c
        FURN.setdefault(int(c["num"]), Counter())
        slug, body = c["slug"], []
        if c["part"] != last_part:
            last_part = c["part"]
            body.append(f'<p class="partno">Part {last_part}</p>'
                        f'<h1 class="part">{html.escape(parts.get(last_part, ""))}</h1>')
        body.append(f'<div class="chap" style="page: ch{int(c["num"])}">')
        body.append(f'<h2 class="chapter" id="ch-{slug}">Chapter {int(c["num"])}: {html.escape(c["title"])}</h2>')
        if c["opening"]:
            count("card")
            body.append(f'<div class="zoom card chapter-opening" id="card-{slug}">'
                        + md_blocks(c["opening"][2], 2, Opening(c)) + "</div>")
        for e in c["eras"]:
            o = era_num(e)
            ecls = f" e{o}" if 1 <= o <= 10 else ""
            title = e["heading"] or e["label"]
            if e["heading"] and e["label"] and e["heading"] != e["label"]:
                warn(f'{slug} era {e["order"]}: heading {e["heading"]!r} != label {e["label"]!r}')
            body.append(f'<h3 class="era{ecls}" id="{c["era_ids"][o]}" data-b="{next_b()}">{inline(title)}</h3>')
            if not e["blocks"]:
                warn(f'{slug} era {e["order"]} ({e["label"]}): no zoom or story blocks')
            for bi, (kind, attrs, lines) in enumerate(e["blocks"]):
                if bi == 0:   # the era strip: the first line of the era's first block
                    k = next((x for x, l in enumerate(lines) if l.strip()), None)
                    if k is not None and RE_STRIP.match(lines[k].strip()):
                        body.append(strip_html(lines[k].strip(), o if ecls else 0))
                        lines = lines[:k] + lines[k + 1:]
                body.append(story_html(attrs, lines, ecls) if kind == "story" else zoom_html(attrs, lines, ecls))
        if c["closing"]:
            count("closing")
            body.append(f'<div class="zoom card chapter-closing" id="closing-{slug}">'
                        + md_blocks(c["closing"][2], 2, Closing(c)) + "</div>")
        body.append("</div>")
        segment(f'ch{int(c["num"]):02d}-{slug}', "\n".join(body))
    CUR["c"] = None
    # back matter: one segment per file, each starts on its own page
    for m in after:
        segment(f'back-{m["id"]}', render_matter(m, "matter"))

    out = write_page("".join(s["html"] + "\n" for s in SEGMENTS), chapters)
    return out


FURN_COLS = [("card", "card"), ("strip", "strips"), ("by", "By"), ("closer", "closers"),
             ("known", "Known"), ("notknown", "Not kn."), ("disputed", "Disp."), ("five", "5 min"),
             ("skip", "Skip"), ("next", "Next"), ("closing", "closing"), ("who", "Who"), ("xref", "Ch. links")]


def furniture_report(chapters):
    """Per-chapter counts of each furniture kind, as printable lines (a miss shows as a number)."""
    w = [max(5, len(h)) for _, h in FURN_COLS]
    lines = ["  ch  " + " ".join(h.rjust(n) for (_, h), n in zip(FURN_COLS, w))]
    total = Counter()
    for c in chapters:
        f = FURN.get(int(c["num"]), Counter())
        total.update(f)
        lines.append(f'  {int(c["num"]):2d}  ' + " ".join(str(f[k]).rjust(n) for (k, _), n in zip(FURN_COLS, w))
                     + f'  {c["slug"]}')
    lines.append("  all " + " ".join(str(total[k]).rjust(n) for (k, _), n in zip(FURN_COLS, w)))
    spans = sum(len(c["spans"]) for c in chapters)
    named = sum(1 for c in chapters for _, t in c["five"] + c["skip"])
    linked = sum(1 for c in chapters for _, t in c["five"] + c["skip"] if t)
    lines.append(f"  card names linked to spans: {linked} of {named} ({spans} spans in the book)")
    for what, n in BACKLINKS.items():
        lines.append(f'  back matter, {what}: {n["lines"]} lines linked, {n["chapter only"]} of them only to the chapter')
    return lines


def page_head(chapters, extra_css=""):
    return ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
            f"<title>{BOOK_TITLE}</title><style>{CSS}\n{era_css()}\n{chapter_page_css(chapters)}\n{extra_css}"
            "</style></head><body>\n")


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
    text_ = " ".join(g.parts)
    if "<!--" in path.read_text(encoding="utf-8") or "hb-" in text_:
        warn("built HTML still contains a comment or hb- text")
    return len(re.findall(r"\S+", text_))


if __name__ == "__main__":
    t_start = time.time()
    palette = check_palette()
    out = build()
    wc = word_count(out)
    print(f"HTML: {out} ({out.stat().st_size/1024:.0f} KB), words: {wc:,}")
    print(palette)
    print("furniture per chapter:")
    for line in furniture_report(list(CHAPTERS.values())):
        print(line)
    if "--pdf" in sys.argv:
        import make_pdf  # tools/make_pdf.py: page breaks, page numbers, font check, final PDF
        make_pdf.main(sys.modules[__name__])
    secs = time.time() - t_start
    print(f"build time: {int(secs // 60)} min {int(secs % 60)} s")
    print(f"warnings: {len(warnings)}")
    for w in warnings:
        print("  WARN", w)
