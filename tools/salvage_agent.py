#!/usr/bin/env python3
"""salvage_agent.py — recover the work of a sub-agent that died before reporting.

WHY THIS EXISTS
    A sub-agent killed by a usage limit is gone as a process and cannot be
    resumed: this build has no SendMessage tool (verified 2026-09-07 by direct
    name-select — six of seven requested tools returned, SendMessage did not),
    and the Agent tool has no `name` or `maxTurns` parameter.

    BUT ITS TRANSCRIPT SURVIVES ON DISK, in full, including every web page it
    fetched. Two `america-world` research agents were written off as a "total
    loss"; their transcripts held 103 and 99 web fetches across 623 and 740
    distinct URLs — congress.gov, history.state.gov, loc.gov, archives.gov.
    Hours of primary-source research, recoverable as text.

    The agent is not resumable. Its research is. That is what this tool does.

USAGE
    python tools/salvage_agent.py --list
        Show every sub-agent transcript for this session, newest first, with
        size, its task description, and whether it produced a final report.

    python tools/salvage_agent.py <agentId> [-o out.md]
        Write a digest: the task it was given, its reasoning, every source it
        fetched, and the substance of what it found. Hand that file to a fresh
        agent as prior work. That is a manual resume.

    python tools/salvage_agent.py <agentId> --tail [N]
        WHAT WAS IT DOING WHEN IT STOPPED. The last N events (default 8) — each
        thought, tool call and result — truncated to 300 CHARACTERS each, with the
        remaining size shown and an --event I to expand any one in full. Ends with a
        verdict describing the SHAPE of the ending - never a ruling that the task is
        done. Only a closing report suggests the agent thought it had finished; a
        write as the last act means its next step never happened. YOU judge.
        Character truncation, never lines: one line can hold a whole base64 image.

    python tools/salvage_agent.py <agentId> --wrote
        DID ITS WRITES LAND WHOLE? Compares the bytes the agent SENT in each
        Write/Edit against the bytes now on disk. A file existing is NOT proof of a
        finished write — an agent killed mid-Write leaves a short file that looks
        like success. Flags SHORT! and MISSING!.

    python tools/salvage_agent.py <agentId> --brief
        THE CHEAP RESUME PAYLOAD: what it concluded + every source it reached,
        WITHOUT the raw fetched pages. This is what you hand a fresh agent.

    python tools/salvage_agent.py <agentId> --urls
        Just the source list — cheapest possible recovery.

TRANSCRIPTS EXPIRE. cleanupPeriodDays defaults to 30. Salvage promptly.
"""

import argparse
import glob
import json
import os
import re
import sys

# Windows consoles default to cp1252, which CANNOT encode the arrows, em dashes and
# accented names that appear constantly in fetched research. Before this, --tail died
# mid-listing with UnicodeEncodeError on a single "→" and printed nothing further --
# a recovery tool failing exactly when recovery was needed. 2026-09-08.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
import sys

# Session transcripts live beside the main conversation, one file per agent.
CLAUDE_HOME = os.path.expanduser("~/.claude")


def session_dirs():
    return sorted(glob.glob(os.path.join(CLAUDE_HOME, "projects", "*", "*", "subagents")))


def find_transcript(agent_id):
    for d in session_dirs():
        p = os.path.join(d, "agent-%s.jsonl" % agent_id)
        if os.path.exists(p):
            return p
    hits = []
    for d in session_dirs():
        hits += glob.glob(os.path.join(d, "agent-*%s*.jsonl" % agent_id))
    return hits[0] if hits else None


def read_records(path):
    out = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                out.append(json.loads(line))
            except Exception:
                continue
    return out


def text_of(content):
    """Flatten a message content field to plain text."""
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts = []
    for c in content:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "text":
            parts.append(c.get("text", ""))
        elif c.get("type") == "tool_result":
            inner = c.get("content")
            parts.append(text_of(inner) if not isinstance(inner, str) else inner)
    return "\n".join(p for p in parts if p)


def meta_for(path):
    m = path.replace(".jsonl", ".meta.json")
    if os.path.exists(m):
        try:
            return json.load(open(m, encoding="utf-8"))
        except Exception:
            pass
    return {}


def summarize(path):
    recs = read_records(path)
    meta = meta_for(path)
    assistant_text, tool_results, urls, tools_used = [], [], [], {}

    for d in recs:
        msg = d.get("message", {}) or {}
        if d.get("type") == "assistant":
            for c in msg.get("content", []) or []:
                if not isinstance(c, dict):
                    continue
                if c.get("type") == "text" and c.get("text", "").strip():
                    assistant_text.append(c["text"].strip())
                elif c.get("type") == "tool_use":
                    n = c.get("name", "?")
                    tools_used[n] = tools_used.get(n, 0) + 1
                    inp = json.dumps(c.get("input", {}))
                    urls.extend(re.findall(r'https?://[^\s"\\<>)]+', inp))
        elif d.get("type") == "user":
            t = text_of(msg.get("content"))
            if t and len(t) > 200:
                tool_results.append(t)
                urls.extend(re.findall(r'https?://[^\s"\\<>)]+', t))

    seen, uniq = set(), []
    for u in urls:
        u = u.rstrip('.,);"\'')
        if u not in seen:
            seen.add(u)
            uniq.append(u)

    return {
        "meta": meta, "records": len(recs), "assistant_text": assistant_text,
        "tool_results": tool_results, "urls": uniq, "tools_used": tools_used,
    }


def timeline(path):
    """Every event in order: what the agent thought, called, and got back.

    Truncation is by CHARACTER, never by line — a single line can hold a whole
    base64 image, and literal backslash-n sequences can make a whole file look
    like one line. Characters are the only safe unit here.
    """
    events = []
    for d in read_records(path):
        msg = d.get("message", {}) or {}
        if d.get("type") == "assistant":
            for c in msg.get("content", []) or []:
                if not isinstance(c, dict):
                    continue
                if c.get("type") == "text" and c.get("text", "").strip():
                    events.append(("THOUGHT", "", c["text"].strip()))
                elif c.get("type") == "tool_use":
                    inp = c.get("input", {}) or {}
                    # the most telling field first: what it was writing or fetching
                    key = ""
                    for k in ("file_path", "path", "url", "command", "pattern", "prompt"):
                        if inp.get(k):
                            key = str(inp[k])
                            break
                    body = json.dumps(inp)
                    events.append(("CALL " + c.get("name", "?"), key, body))
        elif d.get("type") == "user":
            t = text_of(msg.get("content"))
            if t.strip():
                events.append(("RESULT", "", t.strip()))
    return events


def finished_verdict(events):
    """EVIDENCE about where it stopped — not a ruling on whether the task is done.

    That ruling is a judgement call and belongs to the human or the director agent
    reading the tail, never to this function. All this does is name the shape of the
    ending so the reader knows what they are looking at.

    Note (theory, UNCONFIRMED): the runtime appears to let an in-flight tool call
    complete rather than severing it mid-write — every kill observed so far shows a
    completed write followed by the error, never a half-written file. Do not rely on
    it. Always confirm with --wrote.
    """
    if not events:
        return "EMPTY", "no events at all"

    # walk back past the kill notice to find what it was actually doing
    kinds = [e[0] for e in events]
    last_kind, last_text = events[-1][0], events[-1][2]
    killed = any(m in last_text.lower() for m in
                 ("usage limit", "session limit", "rate_limit", "429"))

    real = None
    for k in reversed(kinds[:-1] if killed else kinds):
        real = k
        break

    if killed:
        if real and real.startswith("CALL"):
            return "KILLED MID-ACTION", (
                "its last real act was %s. Check --wrote, then READ THE TAIL: an agent "
                "killed straight after a write had not yet done whatever came next." % real)
        if real == "RESULT":
            return "KILLED AFTER A RESULT", (
                "a tool returned and it was killed before acting on that result. "
                "Whatever it meant to do next did not happen.")
        return "KILLED", "killed after writing text; read the tail to see how far it got"

    if last_kind == "THOUGHT":
        return "ENDED WITH A REPORT", (
            "it wrote a closing message of %d chars — the only real sign an agent "
            "believed it was finished. Read it and judge." % len(last_text))
    if last_kind.startswith("CALL"):
        return "ENDED ISSUING A CALL", "no result recorded for %s" % last_kind
    if last_kind == "RESULT":
        return "ENDED ON A RESULT", "no closing message — it did not report"
    return "UNKNOWN", last_kind


def cmd_tail(agent_id, n, chars):
    path = find_transcript(agent_id)
    if not path:
        print("No transcript for %s" % agent_id, file=sys.stderr)
        return 2
    ev = timeline(path)
    verdict, why = finished_verdict(ev)
    meta = meta_for(path)

    print("Agent %s — %s" % (agent_id, meta.get("description", "?")))
    print("%d events. VERDICT: %s (%s)\n" % (len(ev), verdict, why))
    print("Last %d events, newest LAST. Each truncated to %d chars.\n" % (min(n, len(ev)), chars))

    start = max(0, len(ev) - n)
    for i, (kind, key, body) in enumerate(ev[start:], start):
        body = body.replace("\n", " ")
        shown = body[:chars]
        more = len(body) - len(shown)
        head = "[%d] %s" % (i, kind)
        if key:
            head += "  -> %s" % key[:110]
        print(head)
        print("    %s" % shown)
        if more > 0:
            print("    ... +%d more chars. Full text: --event %d" % (more, i))
        print()

    if not verdict.startswith("ENDED WITH A REPORT"):
        print("-" * 70)
        print("NO CLOSING REPORT. This agent did not tell anyone it was finished, so")
        print("YOU decide whether its work stands. The events above are the evidence:")
        print("  - did it finish the thing it was in the middle of?")
        print("  - was a write its last act? then its NEXT step never happened.")
        print("  - is there a natural next step it clearly had not reached?")
        print("Confirm the writes landed whole:  --wrote")
        print("If in doubt, hand the WHOLE thing to a fresh agent and let it judge:")
        print("  python tools/salvage_agent.py %s -o handover.md" % agent_id)
        print("  (full digest - research and reasoning included, not --brief)")
    return 0


def cmd_event(agent_id, idx):
    path = find_transcript(agent_id)
    if not path:
        print("No transcript for %s" % agent_id, file=sys.stderr)
        return 2
    ev = timeline(path)
    if idx < 0 or idx >= len(ev):
        print("Event %d out of range (0..%d)" % (idx, len(ev) - 1), file=sys.stderr)
        return 2
    kind, key, body = ev[idx]
    print("Event %d of %d — %s%s\n%s chars\n" % (idx, len(ev) - 1, kind,
                                                 ("  -> " + key) if key else "", len(body)))
    print(body)
    return 0


def cmd_wrote(agent_id):
    """Did its writes actually land, and land WHOLE?

    Compares the content the agent SENT in each write against the bytes now on
    disk. A file that exists is not proof of a finished write — an agent killed
    mid-Write leaves a short file that looks like success. This catches that.
    """
    path = find_transcript(agent_id)
    if not path:
        print("No transcript for %s" % agent_id, file=sys.stderr)
        return 2

    intents = []   # (tool, file, intended_chars, confirmed_by_result)
    pending = None
    for d in read_records(path):
        msg = d.get("message", {}) or {}
        if d.get("type") == "assistant":
            for c in msg.get("content", []) or []:
                if not isinstance(c, dict) or c.get("type") != "tool_use":
                    continue
                name = c.get("name", "")
                if name not in ("Write", "Edit", "NotebookEdit"):
                    continue
                inp = c.get("input", {}) or {}
                body = inp.get("content") or inp.get("new_string") or ""
                pending = [name, inp.get("file_path", "?"), len(body), False]
                intents.append(pending)
        elif d.get("type") == "user" and pending is not None:
            t = text_of(msg.get("content")).lower()
            if "successfully" in t or "has been updated" in t or "created" in t:
                pending[3] = True
            pending = None

    # An agent can write through Bash just as easily as through Write/Edit -- heredocs,
    # sed -i, tee, or an inline python script. This tool used to be blind to all of it and
    # printed "issued no Write/Edit calls", which reads as "nothing was written". On
    # 2026-09-09 that was FALSE for agent aa41f8911f1cd4ade: it had appended ~1,100 words to
    # a research bank and ~660 to an outline entirely through Bash heredocs. Acting on that
    # line unexamined would have thrown the work away.
    bash_writes = []
    for d in read_records(path):
        if d.get("type") != "assistant":
            continue
        for c in (d.get("message", {}) or {}).get("content", []) or []:
            if not isinstance(c, dict) or c.get("type") != "tool_use" or c.get("name") != "Bash":
                continue
            cmd = (c.get("input", {}) or {}).get("command", "")
            if re.search(r">>|(?<![0-9<>])>(?![>&])|\bsed\s+-i\b|\btee\b|<<\s*'?[A-Z]", cmd):
                bash_writes.append(cmd)

    if bash_writes:
        print("\n*** %d Bash call(s) COULD HAVE WRITTEN TO DISK ***" % len(bash_writes))
        print("This tool only tracks Write/Edit/NotebookEdit. Bash heredocs, sed -i, tee and")
        print("inline python are invisible to the table above. Check the real files yourself:")
        print("    python tools/project_state.py <slug>        (measure, do not assume)")
        for cmd in bash_writes[:6]:
            print("    $ %s" % " ".join(cmd.split())[:130])
        if len(bash_writes) > 6:
            print("    ... and %d more" % (len(bash_writes) - 6))
        print()

    if not intents:
        if bash_writes:
            print("No Write/Edit calls -- but see the Bash calls above. DO NOT read this as")
            print("'nothing was written'. Measure the files.")
        else:
            print("Agent %s issued no Write/Edit calls, and no Bash call that looks like a"
                  % agent_id)
            print("write. It probably died before producing anything -- but measure anyway.")
        return 0

    print("Agent %s — %d write(s) attempted\n" % (agent_id, len(intents)))
    print("%-6s %-9s %10s %10s  %s" % ("tool", "confirmed", "sent", "on disk", "file"))
    print("-" * 100)
    suspect = 0
    for tool, fp, sent, ok in intents:
        if os.path.exists(fp):
            actual = os.path.getsize(fp)
            # A Write should land within a few percent of what was sent (encoding,
            # line endings). Much smaller means it was cut off.
            if tool == "Write" and sent and actual < sent * 0.9:
                verdict, suspect = "SHORT!", suspect + 1
            else:
                verdict = "ok"
        else:
            actual, verdict, suspect = 0, "MISSING!", suspect + 1
        print("%-6s %-9s %10d %10d  %s  %s"
              % (tool, "yes" if ok else "NO", sent, actual, os.path.basename(fp), verdict))

    print()
    if suspect:
        print("%d write(s) look INCOMPLETE — the file on disk is shorter than what the" % suspect)
        print("agent sent. Treat those files as poison: discard and rewrite.")
    else:
        print("Every write landed at the size it was sent. That is ALL this proves.")
    print()
    print("IT DOES NOT MEAN THE TASK IS FINISHED. A write is rarely an agent's last")
    print("act — normally it writes, then reports, or writes again, or validates. An")
    print("agent whose final recorded action is a write was almost certainly cut off")
    print("BEFORE its next step, whatever that was.")
    print()
    print("Only a final written report shows the agent believed it was done. Read the")
    print("last few events and judge for yourself:")
    print("    python tools/salvage_agent.py %s --tail" % agent_id)
    return 0


def cmd_list():
    rows = []
    for d in session_dirs():
        for p in glob.glob(os.path.join(d, "agent-*.jsonl")):
            meta = meta_for(p)
            size = os.path.getsize(p)
            recs = read_records(p)
            final = ""
            for d2 in reversed(recs):
                if d2.get("type") == "assistant":
                    t = text_of((d2.get("message") or {}).get("content"))
                    if t.strip():
                        final = t.strip().replace("\n", " ")[:60]
                        break
            rows.append((os.path.getmtime(p), size,
                         os.path.basename(p)[6:-6], meta.get("description", "?"), final))
    rows.sort(reverse=True)
    print("%-19s %9s  %-34s %s" % ("agentId", "bytes", "task", "last words"))
    print("-" * 108)
    for _, size, aid, desc, final in rows:
        print("%-19s %9d  %-34s %s" % (aid, size, desc[:34], final))
    print("\n%d transcripts. Transcripts expire (cleanupPeriodDays, default 30)." % len(rows))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent_id", nargs="?")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--urls", action="store_true")
    ap.add_argument("--brief", action="store_true",
                    help="cheap resume payload: conclusions + sources, NO raw page dumps")
    ap.add_argument("--tail", nargs="?", const=8, type=int, metavar="N",
                    help="last N events (default 8): what it thought, called and got back")
    ap.add_argument("--chars", type=int, default=300,
                    help="truncate each event to this many CHARACTERS (default 300)")
    ap.add_argument("--wrote", action="store_true",
                    help="did its writes land WHOLE? sent bytes vs bytes on disk")
    ap.add_argument("--event", type=int, metavar="I",
                    help="dump event I in full (index from --tail)")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()

    if a.list or not a.agent_id:
        cmd_list()
        return 0

    if a.wrote:
        return cmd_wrote(a.agent_id)
    if a.event is not None:
        return cmd_event(a.agent_id, a.event)
    if a.tail is not None:
        return cmd_tail(a.agent_id, a.tail, a.chars)

    path = find_transcript(a.agent_id)
    if not path:
        print("No transcript for %s" % a.agent_id, file=sys.stderr)
        return 2
    s = summarize(path)

    if a.urls:
        for u in s["urls"]:
            print(u)
        return 0

    if a.brief:
        # The CHEAP resume payload: what the agent concluded and where it looked.
        # Deliberately omits the raw fetched pages — a fresh agent re-fetches the
        # two or three sources it actually needs instead of being fed all of them.
        out = a.out or ("salvage-brief-%s.md" % a.agent_id)
        ncalls = sum(s["tools_used"].values())
        with open(out, "w", encoding="utf-8") as f:
            f.write("# Prior work recovered from sub-agent `%s`\n\n" % a.agent_id)
            f.write("**Task it was given:** %s\n\n" % s["meta"].get("description", "?"))
            f.write("This agent was killed before it could report. It made **%d tool calls** "
                    "and reached **%d distinct sources**. Its conclusions and its source list "
                    "are below.\n\n**Do not repeat its searches.** Re-fetch only the specific "
                    "sources you actually need to finish the job.\n\n" % (ncalls, len(s["urls"])))
            f.write("## What it had worked out\n\n")
            if s["assistant_text"]:
                for t in s["assistant_text"]:
                    f.write(t + "\n\n")
            else:
                f.write("_It was killed before writing any conclusions. The source list below "
                        "is the recoverable part — it shows exactly which ground was already "
                        "covered._\n\n")
            f.write("## Sources it already reached\n\n")
            for u in s["urls"]:
                f.write("- %s\n" % u)
        print("Wrote %s (%d bytes) - BRIEF payload, no raw page dumps." % (out, os.path.getsize(out)))
        return 0

    out = a.out or ("salvage-%s.md" % a.agent_id)
    with open(out, "w", encoding="utf-8") as f:
        f.write("# Salvaged work from sub-agent `%s`\n\n" % a.agent_id)
        f.write("Recovered from its transcript after the agent itself was lost. "
                "This is prior work, not a fresh start.\n\n")
        f.write("- **Task given:** %s\n" % s["meta"].get("description", "?"))
        f.write("- **Agent type:** %s\n" % s["meta"].get("agentType", "?"))
        f.write("- **Transcript records:** %d\n" % s["records"])
        f.write("- **Tool calls:** %s\n" % ", ".join(
            "%s x%d" % (k, v) for k, v in sorted(s["tools_used"].items(), key=lambda x: -x[1])))
        f.write("- **Distinct sources reached:** %d\n\n" % len(s["urls"]))

        f.write("## What it worked out (its own words, in order)\n\n")
        for t in s["assistant_text"]:
            f.write(t + "\n\n")

        f.write("## Sources it reached\n\n")
        for u in s["urls"]:
            f.write("- %s\n" % u)

        f.write("\n## Raw material it gathered\n\n")
        f.write("_Fetched pages and command output, in order. Long results are truncated._\n\n")
        for i, t in enumerate(s["tool_results"], 1):
            f.write("### Result %d\n\n```\n%s\n```\n\n" % (i, t[:4000]))

    print("Wrote %s (%d bytes)" % (out, os.path.getsize(out)))
    print("Task was: %s" % s["meta"].get("description", "?"))
    print("%d sources, %d reasoning blocks, %d gathered results."
          % (len(s["urls"]), len(s["assistant_text"]), len(s["tool_results"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
