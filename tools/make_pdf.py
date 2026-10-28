#!/usr/bin/env python3
"""Print the book to PDF with automatic, layout-checked page breaks.

Called by `python tools/build_full_book.py --pdf` after the HTML is built.

The rule (Jon, 2026-10-27): a heading may not start in the bottom half of a page. When one does,
a page break goes in front of it (in front of the story box or span block it opens, so a box is
never cut from its title), and everything after it moves down. The check runs from the front of
the book to the back: each pass prints the layout, finds the FIRST heading in each section that
breaks the rule, adds one break there, and prints again, until no heading breaks it. Nothing is
placed by hand. Positions come from the real layout: Chrome writes every heading into the PDF's
bookmarks with its page and its height on the page.

Sections (SEGMENTS in build_full_book.py) each start on a fresh page, so their layouts do not
affect one another and are checked side by side. The whole book is then printed once, checked
again (a heading out of place there is fixed with the same loop on the whole book), and every page
number slot is filled in: the contents, the grid page and the back matter
(<span class="pg" data-for="ID">). A heading's page comes from the bookmarks; any other linked
target (a chapter closing, a card) from the PDF's named destinations, which Chrome writes for every
id that a link points at. The slots have a fixed width, so filling them moves nothing; the final
print is checked for that (same pages, no offenders, every number still right). Last, pdffonts
checks the fonts (build_full_book.FONT_FAMILIES, GLYPH_FALLBACK): a substituted font stops the build
before the PDF is copied into place.

Outputs: build/history-book.pdf (with bookmarks), build/page-breaks.json (the breaks it chose and
the per-section pass counts), and a summary on stdout.
"""
import json
import re
import shutil
import subprocess
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from pypdf import PdfReader

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
WORKERS = 10
MAX_PASSES = 400
SLOT = re.compile(r'<span class="pg" data-for="([^"]+)"></span>')


def chrome_pdf(html_path, pdf_path, udd, timeout=1800):
    if pdf_path.exists():
        pdf_path.unlink()
    r = subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-first-run", "--disable-extensions",
                        "--no-pdf-header-footer", "--generate-pdf-document-outline",
                        f"--user-data-dir={udd}", f"--print-to-pdf={pdf_path}", html_path.as_uri()],
                       capture_output=True, timeout=timeout)
    if not pdf_path.exists():
        raise RuntimeError(f"Chrome made no PDF for {html_path.name}: {r.stderr[-400:]!r}")


def outline(pdf_path):
    """Bookmarks in document order: (title, page 1-based, top in points from the page bottom)."""
    r = PdfReader(str(pdf_path))
    out = []

    def walk(items):
        for x in items:
            if isinstance(x, list):
                walk(x)
            else:
                out.append((str(x.title), r.get_destination_page_number(x) + 1, float(x.get("/Top") or 0)))
    walk(r.outline)
    return out, len(r.pages)


def named_pages(pdf_path):
    """{id: page} for every named destination (Chrome writes one for each id a link points at)."""
    r = PdfReader(str(pdf_path))
    return {str(k).lstrip("/"): r.get_destination_page_number(v) + 1 for k, v in r.named_destinations.items()}


def norm(s):
    # Chrome drops the space where a long heading wraps, so compare without any spaces
    return "".join(s.split())


class Layout:
    def __init__(self, B):
        self.B = B
        self.mid = (B.PAGE_H - B.MARGIN_TOP + B.MARGIN_BOTTOM) / 2   # middle of the text area
        self.work = B.OUT / ".pdfwork"
        if self.work.exists():
            shutil.rmtree(self.work, ignore_errors=True)
        self.work.mkdir(parents=True)

    def css(self, breaks):
        if not breaks:
            return ""
        sel = ",".join(f'[data-b="{b}"]' for b in sorted(breaks))
        return f"{sel} {{ break-before: page !important; }}"

    def render(self, name, body, breaks, chapters):
        html_path = self.work / f"{name}.html"
        pdf_path = self.work / f"{name}.pdf"
        html_path.write_text(self.B.page_head(chapters, self.css(breaks)) + body + "</body></html>\n",
                             encoding="utf-8")
        chrome_pdf(html_path, pdf_path, self.work / f"udd-{name}")
        return pdf_path

    def check(self, pdf_path, heads, breaks, name):
        """Match bookmarks to headings; return (first offender's b or None, pages, offenders count)."""
        marks, pages = outline(pdf_path)
        if len(marks) != len(heads):
            raise RuntimeError(f"{name}: {len(marks)} bookmarks for {len(heads)} headings")
        bad = []
        for (title, page, top), h in zip(marks, heads):
            # Chrome repeats some of a heading's text in its bookmark (a heading at a page top, or one
            # whose lines fall on two pages), so only the start of the text is compared
            if not norm(title).startswith(norm(h["text"])[:24]):
                raise RuntimeError(f"{name}: bookmark {title!r} does not match heading {h['text']!r}")
            h["page"], h["top"] = page, top
            if top < self.mid and h["b"] not in breaks and h["kind"] not in ("chapter", "part"):
                bad.append(h)
        return (bad[0]["b"] if bad else None), pages, len(bad)

    def settle(self, name, body, heads, chapters, breaks=None, log=None):
        """Front-to-back loop for one section: break before the first offender, print again."""
        breaks = set(breaks or ())
        first_bad = None
        for n in range(1, MAX_PASSES + 1):
            pdf = self.render(name, body, breaks, chapters)
            b, pages, nbad = self.check(pdf, heads, breaks, name)
            if n == 1:
                first_bad = nbad
            if b is None:
                if log is not None:
                    log[name] = {"passes": n, "breaks_added": len(breaks), "offenders_first_pass": first_bad,
                                 "pages": pages}
                return breaks, pages
            breaks.add(b)
        raise RuntimeError(f"{name}: still breaking the rule after {MAX_PASSES} passes")


def page_map(heads, pdf_path, B=None):
    """{id: page}: headings from their bookmarks (the pages check() stored), every other linked id from
    the PDF's named destinations. Where both know an id they must agree; a difference is a warning."""
    pages = {h["id"]: h["page"] for h in heads if h.get("id") and h.get("page")}
    for hid, pg in named_pages(pdf_path).items():
        if hid not in pages:
            pages[hid] = pg
        elif pages[hid] != pg and B is not None:
            B.warn(f"page of #{hid}: bookmark says {pages[hid]}, link destination says {pg}")
    return pages


def fill_page_numbers(body, pages):
    """Put each target's page number into every slot that points at its id (contents, grid, back
    matter). Returns (body, ids that have a slot but no page)."""
    missing = set()

    def sub(m):
        pg = pages.get(m.group(1))
        if pg is None:
            missing.add(m.group(1))
            return m.group(0)
        return f'<span class="pg" data-for="{m.group(1)}">{pg}</span>'
    return SLOT.sub(sub, body), missing


def fallback_chars(pdf_path, prefixes):
    """{font name: (characters it draws, pages it is on)} for the fonts whose name starts with one of
    prefixes, read from each font's ToUnicode map."""
    r = PdfReader(str(pdf_path))
    out, done = {}, set()
    for pno, page in enumerate(r.pages, 1):
        fonts = (page.get("/Resources") or {}).get("/Font") or {}
        for _, ref in fonts.items():
            f = ref.get_object()
            base = str(f.get("/BaseFont", "")).lstrip("/").split("+", 1)[-1]
            if not any(base.startswith(p) for p in prefixes):
                continue
            chars, pages = out.setdefault(base, (set(), set()))
            pages.add(pno)
            key = getattr(ref, "idnum", None)
            tu = f.get("/ToUnicode")
            if tu is None or key in done:
                continue
            done.add(key)
            data = tu.get_object().get_data().decode("latin-1")
            for block in re.findall(r"beginbfchar(.*?)endbfchar", data, re.S):
                for _src, dst in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
                    chars.add(bytes.fromhex(dst).decode("utf-16-be", "replace"))
            for block in re.findall(r"beginbfrange(.*?)endbfrange", data, re.S):
                for lo, hi, dst in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
                    chars.update(chr(int(dst, 16) + k) for k in range(int(hi, 16) - int(lo, 16) + 1))
    return out


def check_fonts(pdf_path, B):
    """pdffonts on the finished PDF. Every embedded font must belong to FONT_FAMILIES, all of which must
    be there; a GLYPH_FALLBACK font may draw only its listed characters. Anything else stops the build
    with a plain message (a substituted font must fail, never slip through). Returns a summary line."""
    exe = shutil.which("pdffonts")
    if not exe:
        raise SystemExit("FONT CHECK FAILED: pdffonts was not found, so the fonts cannot be checked. "
                         "Install poppler (winget install oschwartz10612.Poppler) and build again.")
    r = subprocess.run([exe, str(pdf_path)], capture_output=True, text=True, timeout=900)
    if r.returncode != 0:
        raise SystemExit(f"FONT CHECK FAILED: pdffonts could not read the PDF: {r.stderr[-300:]}")
    found, fallback, other = {}, {}, []
    for line in r.stdout.splitlines()[2:]:
        if not line.strip():
            continue
        base = line.split()[0].split("+", 1)[-1]
        fam = base.split("-")[0]
        prefix = next((p for p in B.GLYPH_FALLBACK if base.startswith(p)), None)
        if fam in B.FONT_FAMILIES:
            found.setdefault(fam, set()).add(base)
        elif prefix:
            fallback.setdefault(prefix, set()).add(base)
        else:
            other.append(base)
    missing = [f for f in B.FONT_FAMILIES if f not in found]
    if other or missing:
        raise SystemExit(
            "FONT CHECK FAILED: the PDF does not use only the book's fonts. "
            + (f"Embedded but not expected: {', '.join(sorted(set(other)))}. " if other else "")
            + (f"Expected but missing: {', '.join(missing)} (is the font installed?). " if missing else "")
            + f"Expected: {', '.join(B.FONT_FAMILIES)}. The PDF was not copied into place.")
    notes = []
    if fallback:
        for base, (chars, pages) in fallback_chars(pdf_path, list(fallback)).items():
            prefix = next(p for p in B.GLYPH_FALLBACK if base.startswith(p))
            extra = sorted(ch for ch in chars if ch not in B.GLYPH_FALLBACK[prefix])
            if extra:
                listed = ", ".join(f"U+{ord(ch):04X} {unicodedata.name(ch, '?')}" for ch in extra[:12])
                raise SystemExit(
                    f"FONT CHECK FAILED: {base} draws characters the book's fonts should draw: {listed} "
                    f"(pages {sorted(pages)[:10]}). The book's fonts lack them, or a font is missing. "
                    "The PDF was not copied into place.")
            allowed = " ".join(f"U+{ord(ch):04X}" for ch in sorted(chars))
            notes.append(f"{base} for {allowed} only, on {len(pages)} pages")
    fams = ", ".join(f"{f} ({len(s)} styles)" for f, s in sorted(found.items()))
    return f"fonts: OK, {fams}" + (f"; glyph fallback {'; '.join(notes)}" if notes else "")


def main(B):
    t0 = time.time()
    chapters, _ = B.read_registry()
    L = Layout(B)
    segs = B.SEGMENTS
    log, breaks = {}, set()
    print(f"page breaks: settling {len(segs)} sections, {WORKERS} at a time ...", flush=True)
    with ThreadPoolExecutor(WORKERS) as ex:
        futs = {ex.submit(L.settle, s["name"], s["html"], s["heads"], chapters, None, log): s for s in segs}
        for f, s in futs.items():
            got, _ = f.result()
            breaks |= got
    print(f"  sections done in {time.time() - t0:.0f} s, {len(breaks)} breaks added", flush=True)

    # whole book: same breaks, checked again on the real thing
    body = "".join(s["html"] + "\n" for s in segs)
    heads = [h for s in segs for h in s["heads"]]
    breaks, pages = L.settle("whole-book", body, heads, chapters, breaks, log)
    print(f"  whole book checked: {pages} pages, passes {log['whole-book']['passes']}", flush=True)

    # page numbers (contents, grid, back matter); the slots have a fixed width, so filling them moves nothing
    targets = page_map(heads, L.work / "whole-book.pdf", B)
    body, missing = fill_page_numbers(body, targets)
    empty = len(SLOT.findall(body))
    filled = re.findall(r'<span class="pg" data-for="([^"]+)">(\d+)</span>', body)
    for hid in sorted(missing):
        B.warn(f"page number: nothing in the PDF for #{hid}; its slot stays empty")
    final = L.render("final", body, breaks, chapters)
    b, pages2, nbad = L.check(final, heads, breaks, "final")
    if nbad or pages2 != pages:
        raise RuntimeError(f"final print moved: {nbad} offenders, {pages2} pages (expected {pages})")
    after = page_map(heads, final)
    moved = [(hid, pg, after.get(hid)) for hid, pg in set(filled) if after.get(hid) != int(pg)]
    if moved:
        raise RuntimeError(f"final print moved {len(moved)} page numbers, for example {sorted(moved)[:5]}")
    fonts = check_fonts(final, B)
    pdf = B.OUT / "history-book.pdf"
    shutil.copyfile(final, pdf)
    B.write_page(body, chapters, L.css(breaks), name="history-book-print.html")

    kinds = {}
    by_b = {h["b"]: h for h in heads}
    for b in breaks:
        k = by_b[b]["kind"] if b in by_b else "?"
        kinds[k] = kinds.get(k, 0) + 1
    (B.OUT / "page-breaks.json").write_text(json.dumps(
        {"pages": pages, "breaks": sorted(breaks), "breaks_by_kind": kinds, "sections": log,
         "rule": "no heading starts below the middle of the text area"}, indent=1), encoding="utf-8")
    print(f"page numbers: {len(filled)} filled ({len(set(h for h, _ in filled))} targets), "
          f"{empty} empty; every one checked in the final print")
    print(fonts)
    print(f"PDF: {pdf} ({pdf.stat().st_size / 1e6:.1f} MB, {pages} pages), "
          f"{len(breaks)} automatic breaks {kinds}, {time.time() - t0:.0f} s")
    shutil.rmtree(L.work, ignore_errors=True)
