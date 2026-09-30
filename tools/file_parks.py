"""File the TO PARK items of the parallel run T-251..T-255 into the target chapters' banks.
Each item is copied verbatim under one '## Parked from `<source>` (2026-09-27, T-nnn)' section per
(source, target). Items naming several targets go to each. Coordination-only notes are skipped."""
import os, re, glob, collections
ROOT = r"C:\Users\jon\Projects\History-Book-Project-claude"
SLUGS = [os.path.basename(p)[9:-3] for p in glob.glob(os.path.join(ROOT, "research", "research-*.md"))]
SKIP = ("`marketplace` (T-253): this chapter now tells",)

out = collections.defaultdict(list)   # (task, source, target) -> items
report = []
import sys
CPS = [os.path.join(ROOT, p) for p in sys.argv[1:]] or sorted(glob.glob(os.path.join(ROOT, "control", "checkpoints", "T-25[1-5]-*.md")))
for cp in CPS:
    task, source = re.match(r"(T-\d+)-(.+)\.md", os.path.basename(cp)).groups()
    text = open(cp, encoding="utf-8").read()
    if re.search(r"^## TO PARK \(FILED", text, re.M):
        report.append(f"{task}: already filed, skipped"); continue
    open(cp, "w", encoding="utf-8").write(re.sub(r"^## TO PARK[^\n]*", "## TO PARK (FILED by the director, 2026-09-27)", text, count=1, flags=re.M))
    m = re.search(r"^## TO PARK[^\n]*\n(.*?)(?=^## )", text, re.S | re.M)
    body = m.group(1) if m else ""
    preamble = [l for l in body.splitlines() if l.strip() and not l.startswith("- ")]
    items = re.findall(r"^- (.*?)(?=^- |\Z)", body, re.S | re.M)
    for it in items:
        it = it.strip()
        if any(it.startswith(s) for s in SKIP):
            report.append(f"{task}: skipped coordination note")
            continue
        head = it.split(":", 1)[0]
        targets = [s for s in SLUGS if re.search(r"(?<![a-z-])" + re.escape(s) + r"(?![a-z-])", head)]
        if not targets:
            report.append(f"{task}: NO TARGET FOUND -> {it[:80]}")
            continue
        for t in targets:
            out[(task, source, t)].append(it)
        note = (" | " + " ".join(preamble)) if preamble else ""
        report.append(f"{task}: -> {', '.join(targets)}")
    out.setdefault(("_pre", source, task), preamble)

for (task, source, target), items in sorted(out.items()):
    if task == "_pre":
        continue
    pre = out.get(("_pre", source, task), [])
    path = os.path.join(ROOT, "research", f"research-{target}.md")
    block = [f"\n## Parked from `{source}` (2026-09-27, {task})\n",
             f"Filed by the director after the parallel run. Full sourced text is in "
             f"`research/research-{source}.md` under the {task} PATCH named in each item.\n"]
    block += [p + "\n" for p in pre]
    block += ["- " + it.replace("\n", "\n  ").rstrip() + "\n" for it in items]
    with open(path, "a", encoding="utf-8") as f:
        f.write("".join(block))
print("\n".join(report))
print("files touched:", sorted({t for (k, s, t) in out if k != "_pre"}))
