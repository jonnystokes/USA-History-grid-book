"""Make story slugs globally unique across the book (the viewer requires it).

Rule: if a story slug appears in more than one chapter, every occurrence is
renamed to `<slug>-<chapter-slug>` (both the :start and :end markers).
Same person in several chapters = several distinct story slugs, one per lens.

    python tools/dedup_story_slugs.py        # report + fix outlines/*.md
"""
import pathlib
import re
from collections import defaultdict

BASE = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = BASE / "outlines"

CHAPTER_RE = re.compile(r'<!--\s*hb-chapter\s[^>]*?slug="([a-z0-9-]+)"')
STORY_RE = re.compile(r'(<!--\s*hb-story:(?:start|end)\s[^>]*?slug=")([a-z0-9-]+)(")')


def main():
    files = [p for p in OUTDIR.glob("*.md") if p.name not in ("_TEMPLATE.md", "BOOK-OUTLINE.md")]
    # pass 1: which chapters use each slug
    usage = defaultdict(set)
    chapter_of = {}
    for p in files:
        t = p.read_text(encoding="utf-8")
        m = CHAPTER_RE.search(t)
        if not m:
            print(f"  SKIP {p.name}: no hb-chapter")
            continue
        chapter_of[p] = m.group(1)
        for sm in STORY_RE.finditer(t):
            usage[sm.group(2)].add(m.group(1))

    dupes = {s for s, chs in usage.items() if len(chs) > 1}
    if not dupes:
        print("No duplicate story slugs across chapters. Nothing to do.")
        return

    print(f"{len(dupes)} slugs used in multiple chapters -> renaming per chapter:")
    for p in files:
        if p not in chapter_of:
            continue
        ch = chapter_of[p]
        t = p.read_text(encoding="utf-8")

        def fix(m):
            slug = m.group(2)
            if slug in dupes and not slug.endswith("-" + ch):
                return m.group(1) + slug + "-" + ch + m.group(3)
            return m.group(0)

        t2 = STORY_RE.sub(fix, t)
        if t2 != t:
            p.write_text(t2, encoding="utf-8", newline="")
            renamed = sorted({m.group(2) for m in STORY_RE.finditer(t) if m.group(2) in dupes})
            print(f"  {p.name}: {', '.join(renamed)} -> +-{ch}")


if __name__ == "__main__":
    main()
