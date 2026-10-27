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
again (a heading out of place there is fixed with the same loop on the whole book), the contents
page numbers are filled in from the bookmarks, and the final PDF is printed.

Outputs: build/history-book.pdf (with bookmarks), build/page-breaks.json (the breaks it chose and
the per-section pass counts), and a summary on stdout.
"""
import json
import shutil
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from pypdf import PdfReader

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
WORKERS = 10
MAX_PASSES = 400


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


def fill_page_numbers(body, heads):
    """Put each heading's page number into the contents lines that point at its id."""
    pages = {h["id"]: h["page"] for h in heads if h.get("id") and h.get("page")}
    for hid, pg in pages.items():
        body = body.replace(f'<span class="pg" data-for="{hid}"></span>',
                            f'<span class="pg" data-for="{hid}">{pg}</span>')
    return body


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

    # contents page numbers; the slots have a fixed width, so filling them moves nothing
    body = fill_page_numbers(body, heads)
    final = L.render("final", body, breaks, chapters)
    b, pages2, nbad = L.check(final, heads, breaks, "final")
    if nbad or pages2 != pages:
        raise RuntimeError(f"final print moved: {nbad} offenders, {pages2} pages (expected {pages})")
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
    print(f"PDF: {pdf} ({pdf.stat().st_size / 1e6:.1f} MB, {pages} pages), "
          f"{len(breaks)} automatic breaks {kinds}, {time.time() - t0:.0f} s")
    shutil.rmtree(L.work, ignore_errors=True)
