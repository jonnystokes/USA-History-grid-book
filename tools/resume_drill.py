#!/usr/bin/env python3
"""resume_drill.py: run it the moment an interruption is reported.

    python tools/resume_drill.py                    # this session's agents
    python tools/resume_drill.py --session <id>     # an earlier session's agents

THE RULE (Jon, 2026-10-26: C:/Users/jon/.claude/CLAUDE.md, "Sub-agents: parallel is fine,
resume is the rule"):
  - A sub-agent stopped by the usage limit, an app restart or a crash is RESUMED, never
    replaced: SendMessage to its name or id with the plain message "continue". Say nothing
    about why. It did not notice the stop, and the resume gives it back its whole memory.
  - If SendMessage fails with "No transcript found", the session id has changed. COPY (never
    move) the agent's files (agent-<id>.jsonl, agent-<id>.meta.json, and agent-<id>.prefix.json
    when there is one) from the old session's subagents folder into the current session's,
    then send "continue" again.
  - If a resume is impossible (it fails again, or the transcript ends mid-tool-call and the
    resume fails), STOP and tell Jon.
  - Never start a recovery, salvage or replacement agent. Only Jon can direct a fresh agent
    to take over, at the time, in so many words.

What it prints:
  1. The measured state (project_state.py) and the project files changed in the last hour.
  2. This project's sub-agents in the session, newest first, each with how its transcript
     ends: STOPPED (an API error such as the usage limit ended it), MID-STEP (it ends on a
     tool call, a tool result or a message with no reply: still running, or cut off), or
     REPLIED (its last turn is a reply). Only agents whose working folder is this project
     count: every project launched from C:/Users/jon/Projects shares one project key.
  3. The rule, and for each agent that did not end on a reply, the SendMessage line, with
     the copy commands for when SendMessage says "No transcript found".

The session is CLAUDE_CODE_SESSION_ID (set in the director's own shells) unless --session
names another. After a session-id change the agents to resume are in the old session: the
drill names the newest earlier sessions that hold this project's agents, and the WORKLOG wave
entry records the session id its agents were launched in. Only the last records of each
transcript are read.
"""

import argparse
import glob
import json
import os
import subprocess
import sys
import time

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECTS = os.path.join(os.path.expanduser("~/.claude"), "projects")
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def when(ts):
    """A time for Jon to read: 12-hour with AM/PM."""
    t = time.localtime(ts)
    return "%s %d %d:%02d %s" % (MONTHS[t.tm_mon - 1], t.tm_mday, t.tm_hour % 12 or 12,
                                 t.tm_min, "AM" if t.tm_hour < 12 else "PM")


def ago(ts):
    m = int((time.time() - ts) // 60)
    return "%d min ago" % m if m < 120 else ("%d hours ago" % (m // 60) if m < 2880 else
                                              "%d days ago" % (m // 1440))


def fw(p):
    """A path for the Bash tool: forward slashes."""
    return p.replace("\\", "/")


def sh(cmd):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", cwd=ROOT, timeout=300, env=env)
        return (r.stdout or r.stderr).strip()
    except Exception as e:
        return "(failed: %s)" % e


def norm(p):
    return os.path.normcase(os.path.normpath(p))


def in_project(cwd):
    if not cwd:
        return False
    c, r = norm(cwd), norm(ROOT)
    return c == r or c.startswith(r + os.sep)


def first_cwd(path):
    """The folder the agent worked in, from the first records of its transcript."""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for _ in range(5):
                line = f.readline()
                if not line:
                    break
                try:
                    rec = json.loads(line)
                except Exception:
                    continue
                if isinstance(rec, dict) and rec.get("cwd"):
                    return rec["cwd"]
    except OSError:
        pass
    return None


def project_agents():
    """Every copy of every sub-agent transcript of this project on the PC. The resume
    recipe's file copy leaves the same agent in two session folders."""
    out = []
    for p in glob.glob(os.path.join(PROJECTS, "*", "*", "subagents", "agent-*.jsonl")):
        if not in_project(first_cwd(p)):
            continue
        meta = {}
        try:
            with open(p[:-len(".jsonl")] + ".meta.json", encoding="utf-8") as f:
                meta = json.load(f)
        except Exception:
            pass
        sub = os.path.dirname(p)
        try:
            mtime, size = os.path.getmtime(p), os.path.getsize(p)
        except OSError:
            continue
        out.append({"id": os.path.basename(p)[len("agent-"):-len(".jsonl")], "path": p,
                    "subagents": sub, "session": os.path.basename(os.path.dirname(sub)),
                    "mtime": mtime, "size": size,
                    "name": meta.get("name") or "", "task": meta.get("description") or "?"})
    return out


def last_event(path):
    """The last user or assistant record, read backwards from the end of the file."""
    try:
        with open(path, "rb") as f:
            pos, buf, step = os.path.getsize(path), b"", 1 << 18
            while pos > 0:
                n = min(step, pos)
                pos -= n
                f.seek(pos)
                buf = f.read(n) + buf
                lines = buf.split(b"\n")
                if pos > 0:
                    lines = lines[1:]          # the first piece may be part of a line
                for raw in reversed(lines):
                    raw = raw.strip()
                    if not raw:
                        continue
                    try:
                        rec = json.loads(raw.decode("utf-8", "replace"))
                    except Exception:
                        continue
                    if isinstance(rec, dict) and rec.get("type") in ("user", "assistant"):
                        return rec
                step *= 2
    except OSError:
        pass
    return None


def ending(rec):
    """(state, detail): how a transcript ends."""
    if rec is None:
        return "EMPTY", "no messages in the transcript"
    msg = rec.get("message") or {}
    content = msg.get("content")
    blocks = [c for c in content if isinstance(c, dict)] if isinstance(content, list) else []
    kinds = [c.get("type") for c in blocks]
    if rec.get("type") == "assistant":
        text = " ".join((c.get("text") or "") for c in blocks if c.get("type") == "text").strip()
        # A usage limit or other API error is a message the app writes, not the model.
        if rec.get("isApiErrorMessage") or rec.get("apiError") or msg.get("model") == "<synthetic>":
            return "STOPPED", text or str(rec.get("apiError") or rec.get("error") or "an API error")
        if "tool_use" in kinds:
            return "MID-STEP", "ends on a tool call with no result"
        if text:
            return "REPLIED", text
        return "MID-STEP", "ends inside a turn, with no reply"
    if "tool_result" in kinds:
        return "MID-STEP", "ends on a tool result with no reply"
    return "MID-STEP", "ends on a message to it with no reply"


def subagents_dir(session):
    """The subagents folder of a session, found by its transcript or folder name."""
    for d in glob.glob(os.path.join(PROJECTS, "*", session)) + \
            [p[:-len(".jsonl")] for p in glob.glob(os.path.join(PROJECTS, "*", session + ".jsonl"))]:
        return os.path.join(d, "subagents")
    return None


def other_sessions(copies, skip):
    """Sessions other than `skip` that hold this project's agents, newest first."""
    by = {}
    for t in copies:
        if t["session"] == skip:
            continue
        n, newest = by.get(t["session"], (0, 0))
        by[t["session"]] = (n + 1, max(newest, t["mtime"]))
    return sorted(by.items(), key=lambda kv: -kv[1][1])


def print_sessions(copies, skip):
    rows = other_sessions(copies, skip)[:3]
    if not rows:
        return
    print("\n  Other sessions that hold this project's agents (newest first):")
    for sid, (n, newest) in rows:
        print("    %s  %3d agent(s), the newest written %s" % (sid, n, when(newest)))
    print("  After a session-id change, the agents to resume are in the old session:")
    print("    python tools/resume_drill.py --session <old session id>")
    print("  (the WORKLOG wave entry records the session id its agents were launched in)")


def main():
    ap = argparse.ArgumentParser(description="Run the moment an interruption is reported.")
    ap.add_argument("--session", help="the session whose agents to check "
                                      "(default: CLAUDE_CODE_SESSION_ID, the current one)")
    a = ap.parse_args()
    current = os.environ.get("CLAUDE_CODE_SESSION_ID") or None
    target = a.session or current

    print("=" * 78)
    print("RESUME DRILL: measure, then resume. Never replace an agent.")
    print("=" * 78)

    print("\n[1] THE MEASURED STATE")
    print("-" * 78)
    state = sh("python tools/project_state.py")
    print("\n".join(state.splitlines()[-3:]) if state else "(project_state.py unavailable)")
    print("\n  Project files changed in the last hour, newest first:")
    cutoff, changed = time.time() - 3600, []
    for base in ("outlines", "research", "manuscript", "workspace", "control"):
        for dp, _, fs in os.walk(os.path.join(ROOT, base)):
            for f in fs:
                fp = os.path.join(dp, f)
                try:
                    ts = os.path.getmtime(fp)
                    if ts > cutoff:
                        changed.append((ts, fp, os.path.getsize(fp)))
                except OSError:
                    pass
    changed.sort(reverse=True)
    for ts, fp, size in changed[:20]:
        print("    %s  (%d bytes)" % (fw(os.path.relpath(fp, ROOT)), size))
    if len(changed) > 20:
        print("    ... and %d more" % (len(changed) - 20))
    if not changed:
        print("    (none)")

    copies = project_agents()
    print("\n[2] THIS PROJECT'S SUB-AGENTS IN SESSION %s" % (target or "(unknown)"))
    print("-" * 78)
    if not target:
        print("  CLAUDE_CODE_SESSION_ID is not set, so the session is unknown. Run this from the")
        print("  director's own shell, or name the session: --session <id>.")
        print_sessions(copies, None)
        return 2

    newest = {}
    for t in copies:
        if t["id"] not in newest or t["mtime"] > newest[t["id"]]["mtime"]:
            newest[t["id"]] = t
    agents = sorted((newest[i] for i in {t["id"] for t in copies if t["session"] == target}),
                    key=lambda t: -t["mtime"])
    for t in agents:
        t["state"], t["detail"] = ending(last_event(t["path"]))
    act = [t for t in agents if t["state"] != "REPLIED"]
    replied = [t for t in agents if t["state"] == "REPLIED"]

    def row(t):
        print("  %-8s %-8s %-17s %-15s %-28s %s" % (
            t["state"], (t["name"] or "-")[:8], t["id"], when(t["mtime"]), t["task"][:28],
            " ".join(t["detail"].split())[:48]))

    if not agents:
        print("  None of this project's agents ran in this session.")
    for t in act:
        row(t)
    for t in replied[:8]:
        row(t)
    if len(replied) > 8:
        print("  ... and %d more that REPLIED" % (len(replied) - 8))
    print("\n  %d agent(s): %d STOPPED, %d MID-STEP, %d REPLIED."
          % (len(agents), sum(t["state"] == "STOPPED" for t in agents),
             sum(t["state"] in ("MID-STEP", "EMPTY") for t in agents), len(replied)))
    print_sessions(copies, target)

    print("\n[3] THE RULE: RESUME, NEVER REPLACE (Jon, 2026-10-26)")
    print("-" * 78)
    print("""  - A stopped sub-agent is resumed: SendMessage to its name or id, the plain message
    "continue". Nothing about why: it did not notice the stop.
  - "No transcript found" means the session id changed: COPY (never move) its files
    agent-<id>.* from the old session's subagents folder into the current session's,
    then send "continue" again.
  - If a resume is impossible (it fails again, or the transcript ends mid-tool-call and
    the resume fails), STOP and tell Jon.
  - Never start a recovery, salvage or replacement agent. Only Jon can direct a fresh
    agent to take over, at the time, in so many words.
  - Resume every stopped agent whose task is still open in control/WORKLOG.md. One whose
    task the WORKLOG shows done, or given to another agent on Jon's word, needs nothing.
  Source: C:/Users/jon/.claude/CLAUDE.md, "Sub-agents: parallel is fine, resume is the rule".""")

    if act:
        cur_sub = subagents_dir(current) if current else None
        print("\n  For each agent that did not end on a reply:")
        for t in act:
            moved = t["session"] != current
            copied = bool(cur_sub) and os.path.exists(os.path.join(cur_sub, os.path.basename(t["path"])))
            mins = int((time.time() - t["mtime"]) // 60)
            print("\n  %s %s: %s, last written %s (%s)" % (
                t["name"] or "(no name)", t["id"], t["state"], when(t["mtime"]), ago(t["mtime"])))
            if t["state"] != "STOPPED" and not moved and mins < 60:
                # Written lately, in the current session: most likely still working.
                print("    It %s: most likely still running. Leave it alone." % t["detail"])
                print('    Only if you know it was cut off: SendMessage to "%s" (or %s): continue.'
                      % (t["name"] or t["id"], t["id"]))
                print("    If that fails, stop and tell Jon.")
                continue
            if t["state"] != "STOPPED":
                why = "its session ended under it" if moved else "nothing written since %s" % when(t["mtime"])
                print("    It %s (%s): probably cut off. Try the resume; if it fails," % (t["detail"], why))
                print("    stop and tell Jon.")
            if moved:
                print('    SendMessage to %s: continue' % t["id"])
            else:
                print('    SendMessage to "%s" (or %s): continue' % (t["name"] or t["id"], t["id"]))
            if moved and copied:
                print("    (its files are already copied into the current session)")
            elif moved:
                dest = fw(cur_sub) if cur_sub else "<the current session's subagents folder>"
                print('    If it says "No transcript found", copy its files, then send "continue" again:')
                print('      mkdir -p "%s"' % dest)
                print('      cp -n "%s/agent-%s."* "%s/"' % (fw(t["subagents"]), t["id"], dest))
        print("\n  To see what an agent was doing (reading only): python tools/salvage_agent.py <id> --tail")
    else:
        print("\n  Every agent in this session ended on a reply: nothing to resume. Check [1]:")
        print("  run each task's VERIFY command from its WORKLOG entry.")

    print("\n" + "=" * 78)
    print("RULE: resume with SendMessage \"continue\" (copy the agent's files first after a")
    print("session-id change). If a resume is impossible, stop and tell Jon. Never start a")
    print("replacement agent.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
