"""List the project files whose writer is on record, by model: Fable, Opus, both, and Sonnet (readers).

Usage:  python tools/who_wrote_what.py [--out control/WHO-WROTE-WHAT.md]

Scope: every commit from the start of the session that ran the readability edit (5f428f9, 6:42 PM on
2026-10-26) to HEAD. The director committed each agent's work separately under its task id, so a
commit's task id names the agent, and the agent's model is on record:
  - T-650..T-658 (GAPS-FINAL): opus, per the WORKLOG header of that burst;
  - T-660 and every task from T-670 on: opus; T-661..T-664: fable (each agent's own transcript);
  - R01..R25 review files: sonnet.
Files the director (the main session) wrote are attributed by commit time: the session ran on
claude-fable-5-1 until 11:18 PM on 2026-10-26 and on claude-opus-5-5 from 3:11 AM on 2026-10-27
(its transcript). Generated outputs (book/, build/) are not "written" and are left out, and so is any
file that no longer exists. Work from before this session is not listed: many of those tasks have no
model on record.
"""
import re
import subprocess
import sys
from collections import OrderedDict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START = "5f428f9"
SWITCH = datetime.fromisoformat("2026-10-27T03:11:00-07:00")      # director: fable before, opus after
FABLE_TASKS = {"T-661", "T-662", "T-663", "T-664"}
TOOL_TASKS = {"T-660", "T-705", "T-706"}                            # tasks whose job was tools/
DIRECTOR_PATHS = ("tools/", "control/briefs/", "control/WORKLOG.md", "control/AUDIT-QUEUE.md", "BUGS.md",
                  "control/TODO.md", "control/DECISIONS.md", "CLAUDE.md", "control/RESUME.md",
                  "control/project-notes.md", "control/REPORT-", "control/ARCHITECTURE-GUIDE.md",
                  "control/writing-style-guide.md", "control/general-writing-style-guide.md", "README.md")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                          check=True).stdout


def model_of_task(task):
    return "Fable" if task in FABLE_TASKS else "Opus"


def writer(path, task, when):
    """(model, who) for one file changed in one commit."""
    m = re.match(r"control/review/(R\d\d)\.md$", path)
    if m:
        return "Sonnet", f"reader {m.group(1)}"
    m = re.match(r"control/checkpoints/(T-\d+)", path)
    if m:
        return model_of_task(m.group(1)), f"agent {m.group(1)}"
    director = path.startswith(DIRECTOR_PATHS) and not (task in TOOL_TASKS and path.startswith("tools/"))
    if task and not director:
        return model_of_task(task), f"agent {task}"
    return ("Fable" if when < SWITCH else "Opus"), "director"


def main(argv):
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else ROOT / "control" / "WHO-WROTE-WHAT.md"
    log = git("log", "--reverse", "--format=%H%x09%aI%x09%s", f"{START}^..HEAD").strip().splitlines()
    files = OrderedDict()                      # path -> list of (model, who)
    chapters = OrderedDict()                   # manuscript folder -> writers in order of first change
    for line in log:
        h, when, subj = line.split("\t", 2)
        when = datetime.fromisoformat(when)
        m = re.match(r"(T-\d+)", subj)
        task = m.group(1) if m else None
        for p in git("show", "--name-only", "--format=", h).split("\n"):
            p = p.strip()
            if not p or p.startswith(("book/", "build/")):
                continue
            w = writer(p, task, when)
            seq = files.setdefault(p, [])
            if not seq or seq[-1] != w:
                seq.append(w)
            if p.startswith("manuscript/") and p.count("/") == 2:
                ch = chapters.setdefault(p.split("/")[1], [])
                if w not in ch:
                    ch.append(w)
    files = OrderedDict((p, s) for p, s in files.items() if (ROOT / p).exists())
    older = set(git("ls-tree", "-r", "--name-only", f"{START}^").split("\n"))

    def full(p):
        return str(ROOT / p).replace("/", "\\")

    def age(p):
        return "older file, changed" if p in older else "new file"

    groups = {"Fable": [], "Opus": [], "Both": [], "Sonnet": []}
    for p, seq in files.items():
        models = {m for m, _ in seq}
        if models == {"Sonnet"}:
            groups["Sonnet"].append((p, seq))
        elif "Fable" in models and "Opus" in models:
            groups["Both"].append((p, seq))
        elif "Fable" in models:
            groups["Fable"].append((p, seq))
        else:
            groups["Opus"].append((p, seq))

    def who(seq):
        return ", then ".join(f"{m} {w}" for m, w in seq)

    lines = ["# Who wrote what: Opus and Fable", "",
             f"Generated {datetime.now().strftime('%B %d, %Y, %I:%M %p').replace(' 0', ' ')} by "
             "`python tools/who_wrote_what.py` from the git history.", "",
             "**What is listed.** Every project file changed from the start of the session that ran the "
             "readability edit (6:42 PM, October 26, 2026) to now, where the writer is on record. Each "
             "agent's work was committed under its task number, and each agent's model is confirmed by "
             "its own transcript (or, for T-650 to T-658, by the work log). Files the main session wrote "
             "are dated by commit: it ran on Fable until 11:18 PM on October 26 and on Opus from 3:11 AM "
             "on October 27.", "",
             "**New file or older file.** \"New file\" means the file was created in this window, so "
             "the writer named wrote all of it. \"Older file, changed\" means it already existed (for "
             "the chapters, from the first draft) and the writers named changed it here. The readability "
             "edit rewrote nearly every paragraph of every chapter, so a chapter's text today is mostly "
             "the readability writer's.", "",
             "**What is not listed.** Work from before that session. Its commit messages name the model "
             "on 198 commits as Opus and 111 as Sonnet, and on none as Fable, but 610 task commits name "
             "no model and the research, outlines and first manuscript came in with the first import "
             "(September 24, 2026) with no record, so those files cannot be assigned one by one. No "
             "earlier agent is on record as Fable (the work log names Fable only for the pilot wave), so "
             "every chapter text a Fable agent wrote is in this list. Which model ran the main session in "
             "earlier sessions is not on record here. Generated files (`book\\`, `build\\`) are made by "
             "scripts, not written.", "",
             "Paths are under `C:\\Users\\jon\\Projects\\History-Book-Project-claude\\`. "
             "\"Director\" is the main session.", "",
             "## The book at a glance", "",
             "Each folder under `manuscript\\`, with the writers who changed it in this window, in order. "
             "T-650 to T-658 were small fact fixes, T-661 to T-703 the readability edit (the big rewrite), "
             "T-710 to T-728 the one fix pass after the reader review.", "",
             "| Folder | Writers, in order |", "|---|---|"]
    for ch, ws in sorted(chapters.items()):
        if (ROOT / "manuscript" / ch).exists():
            lines.append(f"| `manuscript\\{ch}\\` | {', then '.join(f'{m} {w}' for m, w in ws)} |")
    lines.append("")
    titles = {"Fable": "Written by Fable only", "Opus": "Written by Opus only",
              "Both": "Written by Fable, then edited by Opus (or the other way round)",
              "Sonnet": "Written by Sonnet (the reader reviews)"}
    for g in ("Fable", "Both", "Opus", "Sonnet"):
        items = groups[g]
        lines += [f"## {titles[g]} ({len(items)} files)", ""]
        by_dir = OrderedDict()
        for p, seq in sorted(items):
            by_dir.setdefault(str(Path(p).parent).replace("/", "\\"), []).append((p, seq))
        for d, rows in by_dir.items():
            lines.append("**The project folder itself**" if d == "." else f"**{d}\\**")
            lines.append("")
            for p, seq in rows:
                lines.append(f"- `{full(p)}`: {who(seq)} ({age(p)})")
            lines.append("")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{out}: Fable {len(groups['Fable'])}, both {len(groups['Both'])}, Opus {len(groups['Opus'])}, "
          f"Sonnet {len(groups['Sonnet'])} files")


if __name__ == "__main__":
    main(sys.argv[1:])
