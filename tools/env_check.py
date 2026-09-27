#!/usr/bin/env python3
"""Which environment is this project running in, and which workflow applies?

    python tools/env_check.py          # prints a short report, exits 0
    python tools/env_check.py --name   # prints just CLOUD or LOCAL

CLOUD = Claude Code on the web (Anthropic's servers, an ephemeral Linux container,
        repo cloned from GitHub). The cloud workflow is ARCHIVED (2026-09-26) in
        control/archive/cloud/. Read its README.md and ask Jon before working.
LOCAL = Jon's Windows PC (C:/Users/jon/Projects/...). Follow control/RESUME.md.

Detection, strongest signal first:
  1. CLAUDE_CODE_REMOTE=true            (set by the cloud harness)
  2. CLAUDE_CODE_CONTAINER_ID present   (set by the cloud harness)
  3. os.name == "nt"                    (Windows -> LOCAL)
Anything else is reported as LOCAL with a warning, because the local docs are the
older, fuller set and are the safer default on an unknown machine.
"""
import os
import sys


def detect():
    if os.environ.get("CLAUDE_CODE_REMOTE", "").lower() == "true":
        return "CLOUD", "CLAUDE_CODE_REMOTE=true"
    if os.environ.get("CLAUDE_CODE_CONTAINER_ID"):
        return "CLOUD", "CLAUDE_CODE_CONTAINER_ID is set"
    if os.name == "nt":
        return "LOCAL", "Windows (os.name == 'nt')"
    return "LOCAL", "no cloud signal found (unknown machine; defaulting to LOCAL docs)"


def main():
    name, why = detect()
    if "--name" in sys.argv:
        print(name)
        return 0
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"ENVIRONMENT: {name}   ({why})")
    print(f"project root: {root}")
    if name == "CLOUD":
        print("CLOUD WORKFLOW IS ARCHIVED: read control/archive/cloud/README.md and ask Jon before any work.")
    else:
        print("FOLLOW: control/RESUME.md  (then control/TODO.md, then the WORKLOG tail)")
    # Both environments: style guide Version 2 lives in the repo (Jon, 2026-09-26).
    guide = os.path.join(root, "control", "general-writing-style-guide.md")
    print(f"general style guide (v2): control/general-writing-style-guide.md "
          f"{'(present)' if os.path.exists(guide) else '(MISSING - no prose may be written or judged)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
