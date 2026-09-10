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


# ── Critique swarm: read-only seats against a named bar (directives/swarm-usage-policy.md) ──
# Verification never gets its own seat, with one Mailroom-shaped exception: a critique swarm
# may seat at most 4 read-only seats, each returning the single biggest gap against a named
# bar artifact (never adjectives), with dissent logged verbatim. Bench = the skill library:
# a seat is cast with ONE skill's SKILL.md (agents/_framework/seats/<slug>.md overrides it).

SEATS_DIR_DEFAULT = AGENTS / "_framework" / "seats"
SKILLS_ROOT_DEFAULT = ROOT / "skills"
CRITIQUE_BYTE_CAP = 6144
CRITIQUE_LENS_CAP = 1024
MAX_CRITIQUE_LENSES = 4

CRITIQUE_READ_ONLY = (
    "This assignment is read-only: return text and evidence to the conductor; do not edit "
    "files, spawn agents, finalize, publish or spend."
)

GAP_CONTRACT = (
    'Return ONLY this JSON: {"biggest_gap": <one sentence>, '
    '"evidence_lines": ["artifact:L<n> <quote>", "bar:L<n> <quote>"], '
    '"proposed_fix": <at most 3 lines>, "dissent": <what you disagree with in the brief or '
    'the bar, or "none because ...">}. A gap you cannot tie to a quoted artifact line AND a '
    'quoted bar line is not a gap; return biggest_gap: null. Adjectives are not evidence.'
)


def _critique_messaging(platform: str) -> str:
    """Reuses expert_production.py's codex/claude messaging-shape split."""
    if platform == "codex":
        return ("Use collaboration.send_message(target=<canonical peer task name>, "
                 "message=<full contribution>). Only the conductor dispatches. Native messages "
                 "do not guarantee an idle peer restarts; the conductor uses followup_task when needed.")
    return "Use native SendMessage to named teammates; the conductor owns Agent dispatch."


def _slice_bar_lines(text: str, spec: Optional[str]) -> str:
    """`--bar-lines a-b`: 1-indexed inclusive slice. No/invalid spec = whole file."""
    if not spec:
        return text
    m = re.match(r"^\s*(\d+)\s*-\s*(\d+)\s*$", spec)
    if not m:
        return text
    start, end = int(m.group(1)), int(m.group(2))
    lines = text.splitlines(keepends=True)
    start = max(1, start)
    end = min(len(lines), end)
    if start > end:
        return ""
    return "".join(lines[start - 1:end])


def _critique_lens_text(slug: str, seat_prompts_dir: Path, skills_root: Path) -> str:
    """Seat prompt file wins; else the skill library (SKILL.md + genius.md excerpt)."""
    seat_file = seat_prompts_dir / f"{slug}.md"
    if seat_file.exists():
        return _read_capped(seat_file, CRITIQUE_LENS_CAP)
    skill_md = skills_root / slug / "SKILL.md"
    text = _read_capped(skill_md, CRITIQUE_LENS_CAP) if skill_md.exists() else ""
    genius_md = skills_root / slug / "genius.md"
    if genius_md.exists():
        genius_text = _read_capped(genius_md, CRITIQUE_LENS_CAP)
        if genius_text:
            text = f"{text}\n\n{genius_text}".strip() if text else genius_text
    return text


def build_critique_plan(artifact: str, bar: str, lenses: List[str], run_id: str, platform: str,
                        out_dir: str, bar_lines: Optional[str] = None,
                        seat_prompts_dir: Optional[str] = None,
                        skills_root: Optional[str] = None) -> Dict:
    """Compile read-only critique seat briefs against a named bar. No dispatch, no writes
    outside `out_dir`. Each seat brief opens with `[swarm:<run-id>] <lens>` on line 1 so the
    meter's reconcile can match it, and carries the full artifact + bar slice + lens + the
    GAP_CONTRACT output shape. Oversize briefs and lenses beyond the 4-seat cap write nothing."""
    artifact_path = Path(artifact).resolve()
    bar_path = Path(bar).resolve()
    out = Path(out_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    seats_dir = Path(seat_prompts_dir).resolve() if seat_prompts_dir else SEATS_DIR_DEFAULT
    skroot = Path(skills_root).resolve() if skills_root else SKILLS_ROOT_DEFAULT

    artifact_text = artifact_path.read_text(encoding="utf-8", errors="ignore")
    bar_text = _slice_bar_lines(bar_path.read_text(encoding="utf-8", errors="ignore"), bar_lines)
    messaging = _critique_messaging(platform)

    seats: List[Dict] = []
    for i, lens in enumerate(lenses):
        if i >= MAX_CRITIQUE_LENSES:
            seats.append({"lens": lens, "brief_path": None, "bytes": 0, "status": "SEAT_CAP"})
            continue
        lens_text = _critique_lens_text(lens, seats_dir, skroot)
        header = f"[swarm:{run_id}] {lens}"
        brief = "\n\n".join([
            header,
            "## ARTIFACT\n" + artifact_text,
            "## BAR\n" + bar_text,
            "## LENS\n" + lens_text,
            messaging,
            CRITIQUE_READ_ONLY,
            GAP_CONTRACT,
        ])
        nbytes = len(brief.encode("utf-8"))
        if nbytes > CRITIQUE_BYTE_CAP:
            seats.append({"lens": lens, "brief_path": None, "bytes": nbytes, "status": "INPUT_GAP"})
            continue
        brief_path = out / f"{lens}-brief.md"
        brief_path.write_text(brief, encoding="utf-8")
        seats.append({"lens": lens, "brief_path": str(brief_path), "bytes": nbytes, "status": "READY"})

    plan = {"run_id": run_id, "artifact": str(artifact_path), "bar": str(bar_path),
            "seats": seats, "platform": platform}
    (out / "critique-plan.json").write_text(json.dumps(plan, indent=2), encoding="utf-8")
    return plan


def critique_digest(seat_outputs: List[Dict]) -> Dict:
    """Fold GAP_CONTRACT seat outputs (each with a `lens` key) into a Composition Ledger
    digest. Crux = the gap named by >=2 seats verbatim, else the first non-null gap."""
    gaps: List[Dict] = []
    dissent_log: List[Dict] = []
    null_seats: List[str] = []
    gap_to_lenses: Dict[str, List[str]] = {}
    gap_order: List[str] = []

    for so in seat_outputs:
        lens = so.get("lens")
        gap = so.get("biggest_gap")
        if gap is None or (isinstance(gap, str) and not gap.strip()):
            null_seats.append(lens)
        else:
            gaps.append({
                "lens": lens,
                "biggest_gap": gap,
                "evidence_lines": so.get("evidence_lines", []),
                "proposed_fix": so.get("proposed_fix"),
            })
            if gap not in gap_to_lenses:
                gap_to_lenses[gap] = []
                gap_order.append(gap)
            gap_to_lenses[gap].append(lens)
        dissent = so.get("dissent")
        if isinstance(dissent, str) and dissent.strip() and not dissent.strip().lower().startswith("none"):
            dissent_log.append({"lens": lens, "dissent": dissent})

    crux = None
    for gap_text in gap_order:
        if len(gap_to_lenses[gap_text]) >= 2:
            crux = gap_text
            break
    if crux is None and gaps:
        crux = gaps[0]["biggest_gap"]

    return {"crux": crux, "gaps": gaps, "dissent_log": dissent_log,
            "null_seats": null_seats, "cost": None}


def render_ledger(digest: Dict) -> str:
    """Composition Ledger markdown: lens · gap · disposition (blank for the pen) · evidence."""
    lines = ["| lens | gap | disposition | evidence |", "|---|---|---|---|"]
    for g in digest.get("gaps", []):
        evidence = "; ".join(g.get("evidence_lines") or [])
        lines.append(f"| {g.get('lens', '')} | {g.get('biggest_gap', '')} | | {evidence} |")
    return "\n".join(lines)


def _load_seat_outputs(outputs_dir: Path) -> List[Dict]:
    """Read `<lens>.json` seat-output files from a directory; lens defaults to the filename."""
    seat_outputs: List[Dict] = []
    for f in sorted(outputs_dir.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        data = dict(data)
        data.setdefault("lens", f.stem)
        seat_outputs.append(data)
    return seat_outputs


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(prog="persona_team.py")
    sub = p.add_subparsers(dest="cmd")

    cast = sub.add_parser("cast", help="emit teammate briefs for a live council")
    cast.add_argument("task")
    cast.add_argument("--mode", default="tight", choices=list(MODE_SHAPE.keys()))
    cast.add_argument("--seats", type=int, default=None)
    cast.add_argument("--commons", default=None)

    production = sub.add_parser("production", help="compile opt-in production briefs; no dispatch")
    production.add_argument("--packet", required=True, help="production assignment JSON")
    production.add_argument("--platform", choices=["codex", "claude"], default="codex")

    evaluate = sub.add_parser("evaluate", help="read pilot evidence; never self-judge quality")
    evaluate.add_argument("--record", required=True)

    close = sub.add_parser("close-session", help="append session entries to persona memories")
    close.add_argument("--members", required=True, help="comma-separated persona slugs")
    close.add_argument("--question", required=True)
    close.add_argument("--verdict", required=True)
    close.add_argument("--session", required=True, help="path to the session digest")
    close.add_argument("--positions", default=None, help="JSON dict slug→position")

    critique = sub.add_parser("critique", help="compile read-only critique seat briefs against a named bar")
    critique.add_argument("--artifact", required=True)
    critique.add_argument("--bar", required=True)
    critique.add_argument("--bar-lines", default=None, help="1-indexed inclusive slice, e.g. 4-18")
    critique.add_argument("--lenses", required=True, help="comma-separated skill/seat slugs, max 4")
    critique.add_argument("--run", required=True, help="run-id, e.g. from swarm_meter.py open")
    critique.add_argument("--platform", choices=["codex", "claude"], required=True)
    critique.add_argument("--out", required=True)
    critique.add_argument("--seat-prompts-dir", default=None,
                          help="default agents/_framework/seats")
    critique.add_argument("--skills-root", default=None, help="default skills/ (test override)")

    digest = sub.add_parser("digest", help="fold critique seat outputs into a Composition Ledger digest")
    digest.add_argument("--outputs", required=True, help="dir of <lens>.json seat-output files")

    argv = sys.argv[1:]
    if argv and argv[0] not in {"cast", "production", "evaluate", "close-session",
                                 "critique", "digest", "-h", "--help"}:
        argv = ["cast"] + argv  # bare "<task>" convenience
    a = p.parse_args(argv)

    if a.cmd == "production":
        from expert_production import build_production_plan
        packet_path = Path(a.packet).resolve()
        result = build_production_plan(json.loads(packet_path.read_text()), packet_path.parent, a.platform)
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["status"] == "READY_FOR_DISPATCH" else 1)
    elif a.cmd == "evaluate":
        from expert_production import adoption_verdict
        print(json.dumps(adoption_verdict(json.loads(Path(a.record).read_text())), indent=2))
    elif a.cmd == "close-session":
        pos = json.loads(a.positions) if a.positions else {}
        print(json.dumps(close_session(
            [m.strip() for m in a.members.split(",") if m.strip()],
            a.question, a.verdict, a.session, pos), indent=2))
    elif a.cmd == "critique":
        lenses = [s.strip() for s in a.lenses.split(",") if s.strip()]
        plan = build_critique_plan(
            artifact=a.artifact, bar=a.bar, lenses=lenses, run_id=a.run,
            platform=a.platform, out_dir=a.out, bar_lines=a.bar_lines,
            seat_prompts_dir=a.seat_prompts_dir, skills_root=a.skills_root,
        )
        print(json.dumps(plan, indent=2))
        ready = sum(1 for s in plan["seats"] if s["status"] == "READY")
        sys.exit(0 if ready >= 1 else 1)
    elif a.cmd == "digest":
        seat_outputs = _load_seat_outputs(Path(a.outputs).resolve())
        print(json.dumps(critique_digest(seat_outputs), indent=2))
    else:
        print(json.dumps(build_team_plan(a.task, a.mode, a.seats, a.commons), indent=2))
