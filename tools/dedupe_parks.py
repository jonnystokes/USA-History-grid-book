"""Remove the second copy of any '## Parked from ...' section that appears twice in a bank
(caused by re-filing T-251..T-255 on 2026-09-29). Keeps the first copy, drops later identical ones."""
import glob, re, os
ROOT = r"C:\Users\jon\Projects\History-Book-Project-claude"
total = 0
for path in sorted(glob.glob(os.path.join(ROOT, "research", "research-*.md"))):
    text = open(path, encoding="utf-8").read()
    # split into blocks at every level-2 heading, keeping the heading with its block
    parts = re.split(r"(?m)^(?=## )", text)
    seen, out, dropped = set(), [], 0
    for p in parts:
        if p.startswith("## Parked from"):
            key = p.strip()
            if key in seen:
                dropped += 1
                continue
            seen.add(key)
        out.append(p)
    if dropped:
        open(path, "w", encoding="utf-8").write("".join(out))
        total += dropped
        print(f"{os.path.basename(path)}: removed {dropped} duplicate parked section(s)")
print("total removed:", total)
