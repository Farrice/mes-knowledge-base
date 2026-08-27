#!/usr/bin/env python3
"""
Persona Team — the bridge between the persona library and the agent-team runtime.

The load-bearing gap this closes (named in .claude/agents/_archived/swarm-orchestrator.md):
the 240-persona library and the subagent runtime were never wired together, so every
"deliberation" was conductor-mediated fan-out against a frozen snapshot — no persona
ever replied to a reply. This module materializes a council cast (council_cast.py)
into teammate-ready dispatch briefs: named agents that can DM each other via
SendMessage under the Mailroom protocol (directives/agent-mailroom.md).

Scar: frozen-snapshot deliberation (2026-08-27, Grok Bot blueprint session).
Consumer: council synthesis read by Farrice (hop 1).

Pure planning logic (no network, no dispatch). The conductor (main loop) does the
actual spawning via the Agent tool with `name:` — Workflow-engine agent() calls
cannot message each other, which is why live mode is a conductor runbook
(.agent/workflows/roundtable-live.md), not a .workflow.js.

CLI:
    python3 execution/persona_team.py "<task>" [--mode tight] [--commons <path>] [--seats N]
    python3 execution/persona_team.py close-session --session <path-to-session-digest> \
        --members "cardinal-mason,ocean-vuong" --question "<q>" --verdict "<one line>"
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))
from council_cast import MODE_SHAPE, build_council_plan  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
AGENTS = ROOT / "agents"
COMMONS_DIR = ROOT / "councils" / "commons"

# Cost discipline (Farrice 2026-08-27): personas load excerpts sized to the
# question, not whole files. Genius voice capped, memory capped.
GENIUS_CAP_CHARS = 6000
MEMORY_CAP_CHARS = 2000
DEFAULT_LIVE_SEATS = 4   # tight cast default; 6 max per cost discipline
MAX_LIVE_SEATS = 6


def slugify(name: str) -> str:
    """Persona display name → teammate-addressable name (Agent tool name rules)."""
    s = re.sub(r"\(you\)", "", name.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:64] or "seat"


def _read_capped(path: Path, cap: int) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore").strip()
    except Exception:
        return ""
    if len(text) <= cap:
        return text
    return text[:cap] + "\n\n[...excerpt capped for cost discipline — full file on disk]"


def _memory_path(slug: str) -> Optional[Path]:
    """Best-effort match of a persona slug to agents/<dir>/memory/context.md."""
    direct = AGENTS / slug / "memory" / "context.md"
    if direct.exists():
        return direct
    # fallback: match by last-name token against agent dirs
    last = slug.split("-")[-1]
    if len(last) > 2:
        try:
            for d in AGENTS.iterdir():
                if d.is_dir() and last in d.name:
                    p = d / "memory" / "context.md"
                    if p.exists():
                        return p
        except Exception:
            pass
    return None


def mailroom_block(self_name: str, peers: List[Dict], commons_path: str) -> str:
    peer_lines = "\n".join(
        f"  - `{p['slug']}` — {p['name']} [{p['domain_group']}]" for p in peers
    )
    return f"""## MAILROOM PROTOCOL (directives/agent-mailroom.md — binding for this meeting)
You are a seated member of a LIVE council meeting. Your peers are addressable teammates.

PEERS:
{peer_lines}

- **DM a peer** with SendMessage, `to: "<peer-slug>"`. Prefix every message subject with a tier:
  `[NORMAL]` — peer reads after finishing their current beat. Default tier.
  `[PRIORITY]` — peer reads at their next natural pause.
  `[URGENT]` — ONLY for a factual error or a finding that invalidates a peer's in-flight work.
- **Non-blocking:** after sending, keep working. Never idle waiting for a reply.
- **Meeting rounds:** when the conductor opens a round, either contribute (BUILD on a named peer,
  CHALLENGE with the real disagreement stated plainly — never smoothed — or CROSS-POLLINATE two
  ideas into something none of you said alone) or reply exactly `PASS`. Silence is a legal move;
  a PASS costs nothing and kills chatter. Do not restate agreement as contribution.
- **The Commons:** append evidence, findings, and disagreements to `{commons_path}` under your own
  `### {self_name}` heading. Read it before each contribution. Never edit another member's entries.
- **Precedence:** Farrice's conversation outranks everything; the conductor relays his input as [URGENT].
- **Dissent canon unchanged:** preserve real disagreement for the synthesis — blending is a failure.
- No Chain, no finalize, no Notion, no Next Moves — return only your contribution.
"""


def teammate_brief(member: Dict, task: str, peers: List[Dict], commons_path: str) -> str:
    """Full dispatch prompt for one seated persona as a live teammate."""
    slug = member["slug"]
    others = [p for p in peers if p["slug"] != slug]
    parts: List[str] = []
    wild = " You are the WILDCARD — bring your outsider lens precisely because it does not obviously fit." if member.get("wildcard") else ""
    parts.append(
        f"You are **{member['name']}** — {member['domain_group']}.{wild}\n"
        f"Your method: {member['core_method']}\nYour lens: {member['lens']}\n"
    )
    if member.get("genius_excerpt"):
        parts.append(f"## YOUR VOICE (genius file excerpt — embody it, don't summarize it)\n{member['genius_excerpt']}\n")
    if member.get("memory"):
        parts.append(
            "## YOUR PRIVATE NOTES (your accumulated memory — positions you've taken before)\n"
            f"{member['memory']}\n"
        )
    parts.append(f"## THE QUESTION BEFORE THE COUNCIL\n{task}\n")
    parts.append(mailroom_block(member["name"], others, commons_path))
    parts.append(
        "## FIRST MOVE\nGive your independent opening take BEFORE reading the Commons or messaging "
        "anyone (no anchoring). Return JSON {take, signature_angle, the_move} to the conductor, and "
        "append your `the_move` + any evidence to the Commons under your heading. Then await the "
        "conductor's meeting rounds and follow the Mailroom protocol."
    )
    return "\n".join(parts)


def build_team_plan(task: str, mode: str = "tight", seats: Optional[int] = None,
                    commons_path: Optional[str] = None) -> Dict:
    """Cast a council and emit teammate-ready briefs for live (agent-team) deliberation."""
    plan = build_council_plan(task, mode)
    n = min(seats or DEFAULT_LIVE_SEATS, MAX_LIVE_SEATS)

    # Live seats exclude the Farrice lens — he is a real human; the conductor holds
    # his taste gate and relays his input as [URGENT]. Frozen mode still seats his lens.
    candidates = [m for m in plan["roster"] if not m.get("is_user")][: max(n, 2)]

    today = date.today().isoformat()
    slug = re.sub(r"[^a-z0-9]+", "-", task.lower()).strip("-")[:48]
    commons = commons_path or str(COMMONS_DIR / f"{today}-{slug}.md")

    members: List[Dict] = []
    for m in candidates:
        mm = dict(m)
        mm["slug"] = slugify(m["name"])
        gp = m.get("genius_path")
        mm["genius_excerpt"] = _read_capped(ROOT / gp, GENIUS_CAP_CHARS) if gp else ""
        mem_path = _memory_path(mm["slug"])
        mm["memory"] = _read_capped(mem_path, MEMORY_CAP_CHARS) if mem_path else ""
        mm["memory_path"] = str(mem_path) if mem_path else None
        members.append(mm)

    peers = [{"slug": m["slug"], "name": m["name"], "domain_group": m["domain_group"]} for m in members]
    for m in members:
        m["brief"] = teammate_brief(m, task, peers, commons)

    return {
        "task": task,
        "mode": mode,
        "live_seats": len(members),
        "commons_path": commons,
        "wildcards": [m["name"] for m in members if m.get("wildcard")],
        "members": [
            {
                "slug": m["slug"],
                "name": m["name"],
                "domain_group": m["domain_group"],
                "wildcard": m.get("wildcard", False),
                "memory_path": m["memory_path"],
                "memory_loaded": bool(m["memory"]),
                "brief": m["brief"],
            }
            for m in members
        ],
    }


# ── Session close: wake the orphaned persona memory ──────────────────────────

SESSION_ENTRY = """
## Council session — {date}
- **Question:** {question}
- **My position:** {position}
- **Council verdict:** {verdict}
- **Session digest:** {session}
"""


def append_session_memory(member_slug: str, question: str, position: str,
                          verdict: str, session: str) -> Optional[str]:
    """Append one session entry to a persona's memory/context.md (create if absent)."""
    mem = _memory_path(member_slug)
    if mem is None:
        d = AGENTS / member_slug / "memory"
        if not (AGENTS / member_slug).exists():
            return None  # never invent agent dirs for unknown personas
        d.mkdir(parents=True, exist_ok=True)
        mem = d / "context.md"
        mem.write_text(f"# {member_slug} Memory\n", encoding="utf-8")
    entry = SESSION_ENTRY.format(
        date=date.today().isoformat(), question=question,
        position=position or "(not recorded)", verdict=verdict, session=session,
    )
    with mem.open("a", encoding="utf-8") as f:
        f.write(entry)
    return str(mem)


def close_session(members: List[str], question: str, verdict: str, session: str,
                  positions: Optional[Dict[str, str]] = None) -> Dict:
    positions = positions or {}
    written, skipped = [], []
    for slug in members:
        out = append_session_memory(slug, question, positions.get(slug, ""), verdict, session)
        (written if out else skipped).append(out or slug)
    return {"memory_written": written, "no_agent_dir": skipped}


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(prog="persona_team.py")
    sub = p.add_subparsers(dest="cmd")

    cast = sub.add_parser("cast", help="emit teammate briefs for a live council")
    cast.add_argument("task")
    cast.add_argument("--mode", default="tight", choices=list(MODE_SHAPE.keys()))
    cast.add_argument("--seats", type=int, default=None)
    cast.add_argument("--commons", default=None)

    close = sub.add_parser("close-session", help="append session entries to persona memories")
    close.add_argument("--members", required=True, help="comma-separated persona slugs")
    close.add_argument("--question", required=True)
    close.add_argument("--verdict", required=True)
    close.add_argument("--session", required=True, help="path to the session digest")
    close.add_argument("--positions", default=None, help="JSON dict slug→position")

    argv = sys.argv[1:]
    if argv and argv[0] not in {"cast", "close-session", "-h", "--help"}:
        argv = ["cast"] + argv  # bare "<task>" convenience
    a = p.parse_args(argv)

    if a.cmd == "close-session":
        pos = json.loads(a.positions) if a.positions else {}
        print(json.dumps(close_session(
            [m.strip() for m in a.members.split(",") if m.strip()],
            a.question, a.verdict, a.session, pos), indent=2))
    else:
        print(json.dumps(build_team_plan(a.task, a.mode, a.seats, a.commons), indent=2))
