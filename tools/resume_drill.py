#!/usr/bin/env python3
"""resume_drill.py — run the moment an interruption is reported.

ONE COMMAND. Run it before deciding anything, and never re-dispatch work before it
has answered. It exists because the same mistake was made three times in this
project: an agent reported as "failed" had already written its files, and twice the
research of a genuinely dead agent was thrown away and paid for again.

    python tools/resume_drill.py

What it does, in order:

  1. ASKS BOTH QUESTIONS: is it on disk, AND did it finish? A file existing is not
     proof of a finished write — an agent killed mid-Write leaves a short file that
     looks like success. "Agent failed" is a claim about an agent, never about the
     repository; "file exists" is a claim about a file, never about the work.
  2. LISTS every sub-agent transcript, flagging which died mid-task — then for each
     dead one compares the bytes it SENT in every write against the bytes now on
     disk, so a truncated write cannot pass as finished work.
  3. Reports which RESUME ROUTES exist on this build, and tells you the one command
     to run for each.
  4. Prints a ready-to-paste CONTINUATION BRIEF for any dead agent, so a fresh agent
     starts from that agent's research instead of from zero.

Findings behind it are in control/AGENT-MECHANICS.md. Re-verify on a new version.
"""

import glob
import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAUDE = os.path.expanduser("~/.claude")
DEAD_MARKERS = ("usage limit", "session limit", "rate_limit", "429")


def sh(cmd):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                           cwd=ROOT, timeout=120)
        return (r.stdout or r.stderr).strip()
    except Exception as e:
        return "(failed: %s)" % e


def transcripts():
    out = []
    for d in glob.glob(os.path.join(CLAUDE, "projects", "*", "*", "subagents")):
        for p in glob.glob(os.path.join(d, "agent-*.jsonl")):
            meta = {}
            mp = p.replace(".jsonl", ".meta.json")
            if os.path.exists(mp):
                try:
                    meta = json.load(open(mp, encoding="utf-8"))
                except Exception:
                    pass
            last, tools = "", 0
            try:
                for line in open(p, encoding="utf-8", errors="replace"):
                    try:
                        rec = json.loads(line)
                    except Exception:
                        continue
                    if rec.get("type") == "assistant":
                        for c in (rec.get("message") or {}).get("content", []) or []:
                            if isinstance(c, dict):
                                if c.get("type") == "text" and c.get("text", "").strip():
                                    last = c["text"].strip()
                                elif c.get("type") == "tool_use":
                                    tools += 1
            except Exception:
                pass
            died = any(m in last.lower() for m in DEAD_MARKERS)
            out.append({
                "id": os.path.basename(p)[6:-6], "path": p, "mtime": os.path.getmtime(p),
                "size": os.path.getsize(p), "task": meta.get("description", "?"),
                "tools": tools, "died": died,
                "last": last.replace("\n", " ")[:70],
            })
    out.sort(key=lambda x: -x["mtime"])
    return out


def main():
    print("=" * 78)
    print("RESUME DRILL — measure before you decide anything")
    print("=" * 78)

    print("\n[1] IS IT ON DISK — AND DID IT FINISH?")
    print("-" * 78)
    state = sh("python tools/project_state.py")
    print("\n".join(state.splitlines()[-3:]) if state else "(project_state.py unavailable)")

    print("\n  A file existing is NOT proof the work is done. An agent killed mid-write")
    print("  leaves a short file that looks like success. Section [2b] checks both.")
    print("\n  Files changed in the last hour:")
    cutoff, found = time.time() - 3600, False
    for base in ("outlines", "research", "manuscript", "workspace", "control"):
        for dp, _, fs in os.walk(os.path.join(ROOT, base)):
            for f in fs:
                fp = os.path.join(dp, f)
                try:
                    if os.path.getmtime(fp) > cutoff:
                        print("    %s  (%d bytes)" % (os.path.relpath(fp, ROOT), os.path.getsize(fp)))
                        found = True
                except Exception:
                    pass
    if not found:
        print("    (nothing — the interrupted agent wrote nothing, so salvage is the whole story)")

    print("\n[2] SUB-AGENT TRANSCRIPTS (newest first)")
    print("-" * 78)
    ts = transcripts()
    dead = [t for t in ts if t["died"]]
    for t in ts[:12]:
        flag = "DIED " if t["died"] else "ok   "
        print("  %s %s  %8d B  %3d tools  %-30s %s"
              % (flag, t["id"], t["size"], t["tools"], t["task"][:30], t["last"][:34]))
    if not ts:
        print("  (no transcripts found — check the session path in AGENT-MECHANICS.md §1)")

    if dead:
        print("\n[2b] DID THE DEAD AGENTS FINISH? (measured, per agent)")
        print("-" * 78)
        for t in dead[:4]:
            print("\n  --- %s (%s) ---" % (t["id"], t["task"][:40]))
            for ln in sh("python tools/salvage_agent.py %s --wrote" % t["id"]).splitlines():
                if ln.strip():
                    print("    " + ln)
            print("    READ THIS BEFORE DECIDING — it is your judgement, not the script's:")
            print("      python tools/salvage_agent.py %s --tail" % t["id"])
            print("    A write as the last act means its NEXT step never happened.")

    print("\n[3] RESUME ROUTES ON THIS BUILD")
    print("-" * 78)
    print("""  MEASURED COSTS ON THIS BUILD (2.1.260) — decide with these, not by feel:
    re-running a dead research agent cold ... ~1,000,000 tok (128 tool calls)
    feeding it the FULL salvage digest ...... ~90,000 tok
    feeding it the --brief payload .......... ~12,000 tok   <-- use this
    a fork spawn (inherits everything) ...... ~621,000 tok, and it did NO work
    a cold general-purpose spawn ............ ~50,000 tok floor

  a) Workflow resumeFromRunId .............. THE ONLY TRUE RESUME. Use if the work
     ran as a Workflow. Completed agent() calls replay from cache and cost nothing.
       Workflow({scriptPath: "<path from the launch result>", resumeFromRunId: "wf_..."})
     DO NOT edit or reorder earlier agent() calls first — the cache matches by
     POSITION, so "tidying the script to skip what already landed" is exactly what
     destroys it. Same-session only; compaction can silently break it.

  b) Salvage -> fresh agent ................. ALWAYS AVAILABLE. Two shapes, and
     WHICH ONE IS A JUDGEMENT CALL — read the tail first, do not let a script pick.

       --brief   (~12k tok)  when YOU can already see what is missing and can give
                             the fresh agent a precise instruction. Conclusions and
                             source list only.
       full      (~90k tok)  when the state is AMBIGUOUS — it died mid-something and
                             you cannot tell how far it got. Send everything: its
                             research, its reasoning, its raw material, and let the
                             fresh agent work out where it was and finish from there.
                             python tools/salvage_agent.py <agentId> -o handover.md

     Paying 90k to avoid guessing wrong is cheap against ~1M to redo it, and far
     cheaper than a confident wrong guess that corrupts a chapter.

  c) fork ................................... AVAILABLE BUT USUALLY WRONG HERE.
     Enable with env.CLAUDE_CODE_FORK_SUBAGENT=1 in ~/.claude/settings.json (takes
     effect mid-session). It genuinely inherits the whole conversation — but it cost
     621k tokens to say one sentence, ~12x a cold spawn, because it carries the
     entire parent context. Cost scales with conversation length. Worth it ONLY for
     a task that truly needs the whole session and would otherwise re-read a lot.
     Revert the flag afterwards; it may make ALL spawns forks.

  d) SendMessage to the agent ............... NOT AVAILABLE on this build.
     Re-verify on a new version — ToolSearch "select:SendMessage" — because this is
     the single fact the whole strategy rests on. Even if it returns, a KILLED agent
     may still be unaddressable: the roster drops killed agents.""")

    if dead:
        d = dead[0]
        print("\n[4] CONTINUATION BRIEF for the most recent dead agent")
        print("-" * 78)
        print("  Agent %s — task was: %s" % (d["id"], d["task"]))
        print("  It made %d tool calls before dying. Recover them first:\n" % d["tools"])
        print("    python tools/salvage_agent.py %s --brief -o _reference/salvaged/brief-%s.md"
              % (d["id"], d["id"]))
        print("    # --brief, not the full digest: ~12k tokens instead of ~90k.")
        print("\n  Then dispatch a fresh agent whose prompt OPENS with this:\n")
        print("    A previous agent was given this exact task and was killed by a usage")
        print("    limit before it could report. Its research survived and is in")
        print("    `_reference/salvaged/brief-%s.md` — %d tool calls." % (d["id"], d["tools"]))
        print("    READ THAT FILE FIRST. Do not repeat its searches. Your job is to")
        print("    finish the task from where it got to, not to start over.")
        print("    WRITE YOUR OUTPUT FILE EARLY and keep appending — the previous agent")
        print("    died with nothing on disk because it saved all its writing for last.")
    else:
        print("\n[4] No agent in this session died mid-task.")
        print("-" * 78)
        print("  If something was still interrupted, check [1]: the work may have landed.")

    print("\n" + "=" * 78)
    print("RULE: salvage first, re-dispatch second. Never re-run a research agent from")
    print("zero without reading what the dead one already found.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
