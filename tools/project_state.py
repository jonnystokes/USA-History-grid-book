#!/usr/bin/env python3
"""project_state.py — derive the TRUE state of the book from the files.

The tracker lies; the files do not. STATUS.md was four weeks stale and wrong in
both directions before this script existed. Nothing here is remembered, claimed
or inherited: every number is measured on the spot.

Usage:
    python tools/project_state.py                 # full table
    python tools/project_state.py <slug>          # one chapter, verbose
    python tools/project_state.py --check <slug> --stage research
    python tools/project_state.py --json          # machine-readable
    python tools/project_state.py --punct <file>  # em dashes / semicolons left (style v2)

--check exits 0 only if the chapter genuinely meets the definition of done for
that stage. That exit code is the ONLY acceptable proof a task is complete.
"""

import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTLINES = os.path.join(ROOT, "outlines")
RESEARCH = os.path.join(ROOT, "research")
MANUSCRIPT = os.path.join(ROOT, "manuscript")
WORKSPACE = os.path.join(ROOT, "workspace")

ERAS = ["before-1500", "1500s", "1600s", "1700-1750", "1750-1800",
        "1800-1850", "1850-1900", "1900-1950", "1950-2000", "2000-today"]

RE_MARK = re.compile(r'^\s*<!--\s*(/?)(hb-[a-z]+)(:start|:end)?\s*(.*?)\s*-->\s*$')
RE_ATTR = re.compile(r'([\w-]+)\s*=\s*"([^"]*)"')
RE_VERIFY = re.compile(r'\[VERIFY', re.I)


def attrs(tail):
    return dict(RE_ATTR.findall(tail))


def prose_words(text):
    """Word count of renderable content only: no markers, no headings."""
    n = 0
    for line in text.split("\n"):
        s = line.strip()
        if not s or RE_MARK.match(s) or s.startswith("#") or s.startswith("<!--"):
            continue
        n += len(s.split())
    return n


RE_ENTITY = re.compile(r'&#?\w+;')


def punctuation(text):
    """Em dashes (U+2014) and semicolons (U+003B) in reader-facing text.

    Added 2026-09-26 with writing style guide v2, which forbids both and requires every
    draft to return zero matches for each. Counts every line a reader can see: prose,
    headings and story blockquotes. Skips marker lines, hb-note blocks (editor notes)
    and HTML entities such as &amp;.
    """
    dash = semi = 0
    in_note = False
    for line in text.split("\n"):
        m = RE_MARK.match(line)
        if m:
            slash, name, se, tail = m.groups()
            if name == "hb-note":
                in_note = not slash
            continue
        if in_note or line.strip().startswith("<!--"):
            continue
        clean = RE_ENTITY.sub("", line)
        dash += clean.count("\u2014")
        semi += clean.count(";")
    return dash, semi


def scan_file(path):
    """Parse one grid file. Returns a dict of measured facts."""
    with open(path, encoding="utf-8") as f:
        text = f.read()

    info = {
        "mode": None, "eras": {}, "stories": [], "notes": 0,
        "verify_tags": len(RE_VERIFY.findall(text)),
        "words": prose_words(text),
        "open_blocks": [],
    }
    era = None
    for no, line in enumerate(text.split("\n"), 1):
        m = RE_MARK.match(line)
        if not m:
            continue
        slash, name, se, tail = m.groups()
        A = attrs(tail)
        opening = se == ":start" or (not se and not slash and name in ("hb-note", "hb-zoom"))

        if name == "hb-chapter":
            info["mode"] = A.get("mode")
            info["slug"] = A.get("slug")
            info["id"] = A.get("id")
        elif name == "hb-time":
            if opening:
                era = A.get("id")
                info["eras"][era] = {
                    "state": A.get("state", "full"),
                    "progress": A.get("progress", ""),
                    "stories": 0, "words": 0, "line": no,
                }
            else:
                era = None
        elif name == "hb-story" and opening:
            st = {"slug": A.get("slug", ""), "name": A.get("name", ""),
                  "status": A.get("status", ""), "kind": A.get("kind", ""),
                  "movie": A.get("movie", ""), "era": era, "line": no}
            info["stories"].append(st)
            if era and era in info["eras"]:
                info["eras"][era]["stories"] += 1
        elif name == "hb-note" and opening:
            info["notes"] += 1

    # per-era renderable words
    cur = None
    for line in text.split("\n"):
        m = RE_MARK.match(line)
        if m:
            slash, name, se, tail = m.groups()
            if name == "hb-time":
                A = attrs(tail)
                cur = A.get("id") if se == ":start" else None
            continue
        s = line.strip()
        if cur and s and not s.startswith("#") and not s.startswith("<!--"):
            if cur in info["eras"]:
                info["eras"][cur]["words"] += len(s.split())
    return info


def validator(path, part=False):
    """Run the real viewer parser. Returns (errors:int|None, note:str).

    part=True passes --part, which suppresses the ten-era completeness check. Use it
    for ONE file of a multi-file chapter; the ten-era check is then done across the
    whole set by the caller, not per file.
    """
    js = os.path.join(ROOT, "tools", "validate_grid.js")
    if not os.path.exists(js):
        return None, "validate_grid.js missing"
    cmd = ["node", js, path] + (["--part"] if part else [])
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except FileNotFoundError:
        return None, "node not installed"
    except subprocess.TimeoutExpired:
        return None, "validator timed out"
    m = re.search(r"(\d+)\s+errors?", r.stdout)
    # validate_grid.js exits with its error count since 2026-09-06 (T-002), but the
    # printed count is still what we read - it survives a change to the exit convention.
    return (int(m.group(1)) if m else None), r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""


def chapter_state(slug):
    out = os.path.join(OUTLINES, slug + ".md")
    if not os.path.exists(out):
        return None
    info = scan_file(out)
    bank = os.path.join(RESEARCH, "research-%s.md" % slug)
    bank_words = 0
    if os.path.exists(bank):
        with open(bank, encoding="utf-8") as f:
            bank_words = len(f.read().split())

    ms_dir = os.path.join(MANUSCRIPT, slug)
    ms_files = []
    if os.path.isdir(ms_dir):
        ms_files = sorted(x for x in os.listdir(ms_dir) if x.endswith(".md"))
    ms_words = 0
    for x in ms_files:
        with open(os.path.join(ms_dir, x), encoding="utf-8") as f:
            ms_words += prose_words(f.read())

    # PROSE-STAGE FACTS COME FROM THE MANUSCRIPT, NOT THE OUTLINE.
    # Fixed 2026-09-07. Before this, derive_stage() and the prose bar read progress=
    # flags out of outlines/<slug>.md, where they correctly say "researched" and never
    # say "written" - so the prose bar could not pass for any chapter, ever, no matter
    # how finished. city-building had 10/10 written eras, 14 verified stories, 13,768
    # words and a clean validator, and still measured FAIL / stage=WRITING.
    ms_eras, ms_status, ms_verify = {}, [], 0
    ms_dash = ms_semi = 0
    for x in ms_files:
        with open(os.path.join(ms_dir, x), encoding="utf-8") as f:
            a, b = punctuation(f.read())
        ms_dash += a
        ms_semi += b
        mi = scan_file(os.path.join(ms_dir, x))
        ms_eras.update(mi["eras"])          # merged across parts: one chapter, ten eras
        ms_status += [s["status"] for s in mi["stories"]]
        ms_verify += mi["verify_tags"]

    st = [s["status"] for s in info["stories"]]
    d = {
        "slug": slug,
        "id": info.get("id"),
        "mode": info.get("mode"),
        "eras_present": len(info["eras"]),
        "eras_missing": [e for e in ERAS if e not in info["eras"]],
        "progress_researched": sum(1 for e in info["eras"].values() if e["progress"] == "researched"),
        "progress_written": sum(1 for e in info["eras"].values() if e["progress"] == "written"),
        "empty_eras": sum(1 for e in info["eras"].values() if e["state"] == "empty"),
        "eras_no_story": sorted(k for k, v in info["eras"].items()
                                if v["stories"] == 0 and v["state"] != "empty"),
        "stories": len(info["stories"]),
        "verified": st.count("verified"),
        "candidate": st.count("candidate"),
        "target": st.count("target"),
        "other_status": sorted({s for s in st if s not in ("verified", "candidate", "target")}),
        "outline_words": info["words"],
        "verify_tags": info["verify_tags"],
        "bank_words": bank_words,
        "bank_exists": os.path.exists(bank),
        "manuscript_files": ms_files,
        "manuscript_words": ms_words,
        "ms_eras_present": len(ms_eras),
        "ms_eras_missing": [e for e in ERAS if e not in ms_eras],
        "ms_progress_written": sum(1 for e in ms_eras.values() if e["progress"] == "written"),
        "ms_stories": len(ms_status),
        "ms_verified": ms_status.count("verified"),
        "ms_verify_tags": ms_verify,
        "ms_emdash": ms_dash,
        "ms_semicolon": ms_semi,
        "dup_slugs": sorted({s["slug"] for s in info["stories"]
                             if [x["slug"] for x in info["stories"]].count(s["slug"]) > 1 and s["slug"]}),
        "empty_story_slugs": sum(1 for s in info["stories"] if not s["slug"]),
        # a story tagged verified while its own text still carries [VERIFY] is the
        # art-music failure mode; flagged here because no validator can see it.
        "suspect_verified": [],
    }

    # detect the art-music failure: verified stories in a file that still has VERIFY tags
    if d["verify_tags"] and d["verified"]:
        with open(out, encoding="utf-8") as f:
            lines = f.read().split("\n")
        for s in info["stories"]:
            if s["status"] != "verified":
                continue
            body = []
            for ln in lines[s["line"]:]:
                if RE_MARK.match(ln):
                    break
                body.append(ln)
            if RE_VERIFY.search("\n".join(body)):
                d["suspect_verified"].append(s["slug"] or s["name"])

    d["stage"] = derive_stage(d)
    return d


def derive_stage(d):
    if d["manuscript_words"] > 500 and d["ms_progress_written"] == 10:
        return "WRITTEN"
    if d["manuscript_files"]:
        return "WRITING"
    researched = d["progress_researched"] + d["progress_written"]
    if researched == 10 and d["bank_exists"]:
        # NOTE (2026-09-06): "every non-empty era has a story" was REMOVED from the bar.
        # It contradicted Jon's naming ruling: hb-story blocks are named people only, and
        # some eras have no individually documented person (before-1500 above all).
        # native-nations' before-1500 cell is rich - Cahokia, Chaco, the Calusa, the Great
        # Law of Peace - and correctly carries no story. eras_no_story is now reported as
        # information, never as a failure.
        clean = (d["target"] == 0 and d["candidate"] == 0
                 and not d["suspect_verified"]
                 and d["bank_words"] >= d["outline_words"])
        return "RESEARCHED" if clean else "RESEARCHED*"
    if researched >= 5 or (d["bank_exists"] and d["bank_words"] > 3000):
        return "PARTIAL"
    return "SEED"


DONE = {
    # stage -> (predicate, human description of the bar)
    "research": (
        lambda d: (d["stage"] in ("RESEARCHED", "WRITING", "WRITTEN")
                   and d["eras_present"] == 10 and d["target"] == 0
                   and d["candidate"] == 0 and not d["suspect_verified"]
                   and d["bank_exists"] and d["bank_words"] >= d["outline_words"]
                   and d["verify_tags"] == 0),
        "10/10 eras researched | 0 target | 0 candidate | no suspect verified | "
        "bank >= outline words | 0 [VERIFY] tags"),
    "patch": (
        lambda d: (d["target"] == 0 and d["candidate"] == 0
                   and not d["suspect_verified"] and d["bank_exists"]
                   and d["bank_words"] >= d["outline_words"]),
        "0 target | 0 candidate | no suspect verified | bank >= outline words"),
    # Every term below is measured from manuscript/<slug>/*.md. See the note in
    # chapter_state() for why reading the outline here was wrong.
    "prose": (
        lambda d: (d["stage"] == "WRITTEN"
                   and d["ms_eras_present"] == 10
                   and d["ms_stories"] > 0
                   and d["ms_verified"] == d["ms_stories"]
                   and d["ms_verify_tags"] == 0
                   and d["ms_emdash"] == 0 and d["ms_semicolon"] == 0
                   and d["manuscript_words"] >= 3000),
        "manuscript 10/10 eras progress=written | every manuscript story verified | "
        "0 [VERIFY] tags in the manuscript | 0 em dashes and 0 semicolons (style guide v2) | "
        ">= 3000 words"),
}


def all_slugs():
    return sorted(f[:-3] for f in os.listdir(OUTLINES)
                  if f.endswith(".md") and not f.startswith("_")
                  and f != "BOOK-OUTLINE.md")


def main():
    args = sys.argv[1:]
    if "--punct" in args:
        # Per-file em dash / semicolon finder for writers (style guide v2). Lists every
        # reader-facing line that still holds one, with its line number.
        path = args[args.index("--punct") + 1]
        with open(path, encoding="utf-8") as f:
            text = f.read()
        dash, semi = punctuation(text)
        print("%s: emdash=%d semicolon=%d" % (path, dash, semi))
        in_note = False
        for no, line in enumerate(text.split("\n"), 1):
            m = RE_MARK.match(line)
            if m:
                if m.group(2) == "hb-note":
                    in_note = not m.group(1)
                continue
            if in_note or line.strip().startswith("<!--"):
                continue
            clean = RE_ENTITY.sub("", line)
            if "\u2014" in clean or ";" in clean:
                print("  %5d: %s" % (no, line.strip()[:110]))
        return 0 if dash == semi == 0 else 1
    if "--check" in args:
        i = args.index("--check")
        slug = args[i + 1]
        stage = args[args.index("--stage") + 1] if "--stage" in args else "research"
        d = chapter_state(slug)
        if d is None:
            print("FAIL  no outline for %s" % slug)
            return 2
        pred, bar = DONE[stage]
        ok = pred(d)

        # Validate the files the stage is actually about. For prose that is every
        # manuscript part (with --part when there is more than one, since a single part
        # legitimately holds fewer than ten eras); otherwise it is the outline.
        per = []
        if stage == "prose":
            ms_dir = os.path.join(MANUSCRIPT, slug)
            multi = len(d["manuscript_files"]) > 1
            per = [(x, validator(os.path.join(ms_dir, x), part=multi)[0])
                   for x in d["manuscript_files"]]
            if not per or any(e is None for _, e in per):
                errs = None
            else:
                errs = sum(e for _, e in per)
        else:
            errs, _ = validator(os.path.join(OUTLINES, slug + ".md"))
        ok = ok and (errs == 0)
        print("%s  %s / %s" % ("PASS" if ok else "FAIL", slug, stage))
        print("  bar: %s | validator 0 errors" % bar)
        if stage == "prose":
            print("  measured: stage=%s ms_eras=%d/10 written=%d/10 ms_stories=%d "
                  "(verified %d) ms_verify_tags=%d emdash=%d semicolon=%d manuscript=%dw "
                  "files=%d validator_errors=%s"
                  % (d["stage"], d["ms_eras_present"], d["ms_progress_written"],
                     d["ms_stories"], d["ms_verified"], d["ms_verify_tags"],
                     d["ms_emdash"], d["ms_semicolon"],
                     d["manuscript_words"], len(d["manuscript_files"]), errs))
            if d["ms_eras_missing"]:
                print("  manuscript missing eras: %s" % ", ".join(d["ms_eras_missing"]))
            for x, e in per:
                print("    %-34s %s errors" % (x, e))
        else:
            print("  measured: stage=%s eras=%d/10 stories=%d (v%d c%d t%d) "
                  "verify_tags=%d bank=%dw outline=%dw manuscript=%dw validator_errors=%s"
                  % (d["stage"], d["eras_present"], d["stories"], d["verified"],
                     d["candidate"], d["target"], d["verify_tags"], d["bank_words"],
                     d["outline_words"], d["manuscript_words"], errs))
        if d["suspect_verified"]:
            print("  SUSPECT verified-but-unsourced: %s" % ", ".join(d["suspect_verified"]))
        # eras_no_story is measured from the OUTLINE, so it is meaningless in prose mode -
        # printing it there implies a fact about the manuscript that was never measured.
        if d["eras_no_story"] and stage != "prose":
            print("  eras with no story: %s" % ", ".join(d["eras_no_story"]))
        return 0 if ok else 1

    slugs = all_slugs()
    if args and not args[0].startswith("-"):
        slugs = [args[0]]

    data = [chapter_state(s) for s in slugs]
    data = [d for d in data if d]

    if "--json" in args:
        print(json.dumps(data, indent=1))
        return 0

    if len(slugs) == 1:
        d = data[0]
        for k in sorted(d):
            print("%-22s %s" % (k, d[k]))
        return 0

    print("%-22s %-12s %5s %5s %4s %4s %6s %7s %7s" %
          ("slug", "stage", "eras", "stor", "cand", "targ", "VERIFY", "outline", "bank"))
    print("-" * 84)
    for d in sorted(data, key=lambda x: x["id"] or "99"):
        flag = "!" if d["suspect_verified"] else " "
        print("%-22s %-12s %5s %5d %4d %4d %6d %7d %7d%s" %
              (d["slug"], d["stage"], "%d/10" % d["eras_present"], d["stories"],
               d["candidate"], d["target"], d["verify_tags"],
               d["outline_words"], d["bank_words"], flag))
    n = len(data)
    tally = {}
    for d in data:
        tally[d["stage"]] = tally.get(d["stage"], 0) + 1
    print("-" * 84)
    print("%d chapters | %s" % (n, " | ".join("%s %d" % kv for kv in sorted(tally.items()))))
    print("stories %d (verified %d, candidate %d, target %d) | outline %dw | banks %dw | manuscript %dw"
          % (sum(d["stories"] for d in data), sum(d["verified"] for d in data),
             sum(d["candidate"] for d in data), sum(d["target"] for d in data),
             sum(d["outline_words"] for d in data), sum(d["bank_words"] for d in data),
             sum(d["manuscript_words"] for d in data)))
    susp = [d["slug"] for d in data if d["suspect_verified"]]
    if susp:
        print("! verified-but-unsourced stories in: %s" % ", ".join(susp))
    return 0


if __name__ == "__main__":
    sys.exit(main())
