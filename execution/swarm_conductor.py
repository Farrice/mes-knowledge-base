#!/usr/bin/env python3
"""
swarm_conductor.py — deterministic mission scaffolding for the /swarm conductor
(Swarm Apex Session 1: `_active/swarm-apex-2026-07-07/PLAN.md`).

Does the boring, deterministic parts of "plan → gate → launch → receipt" so the
orchestrator (Fable/Sonnet main loop) only has to do the judgment parts:
  * the effort→fan-out function (the Grok knob, done deterministically)
  * casting a REAL, file-verified expert roster for the `heavy` pattern (reuses
    council_cast.py — never re-invents casting logic)
  * writing the Mission Plan file (`.tmp/swarm/<slug>/mission.md`) that doubles
    as the Manus-style `todo.md` recitation surface
  * writing the post-run receipt (reuses run_receipt.py's machinery) with
    per-run economics lines (agents spawned, tokens spent)

This script does NOT execute the swarm itself — that's the native Workflow
tool's job (`.agent/workflows/swarm-heavy.workflow.js` and
`.agent/workflows/swarm-research.workflow.js`, which consume this contract
directly). `plan` prints the exact invocation the orchestrator should fire.

CLI:
    python3 execution/swarm_conductor.py plan --brief "<outcome wanted>" \\
        --pattern heavy|research --effort low|medium|high --slug <kebab-slug> \\
        [--domains "d1,d2"] [--deliverable <path>]

    python3 execution/swarm_conductor.py receipt --slug <slug> \\
        --status pass|partial|fail --agents N --tokens N \\
        [--deliverable <path>] [--notes "..."] [--dry-run]

    python3 execution/swarm_conductor.py status
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
EXEC_DIR = ROOT / "execution"
SKILLS = ROOT / "skills"
SWARM_DIR = ROOT / ".tmp" / "swarm"
PRODUCTION_CORE = ROOT / "PRODUCTION_CORE.md"
PATH_DECISION_DOC = "_active/path-decision-2026-07-01/README.md"

sys.path.insert(0, str(EXEC_DIR))

# ── Fan-out: the effort→count function (the Grok knob, done right) ──────────
HEAVY_FAN_OUT = {"low": 4, "medium": 8, "high": 12}
RESEARCH_FAN_OUT = {"low": 6, "medium": 6, "high": 10}
RESEARCH_DEPTH_LABEL = {"low": "standard", "medium": "standard", "high": "deep"}

# Plan-time roster casting always casts at max breadth (council_cast "deploy"
# mode, 16 candidates) so there's headroom to file-verify + trim down to any
# fan_out up to the 12-worker cap. The runtime script (swarm-heavy.workflow.js)
# consumes the roster decided HERE — no re-casting at execution time.

LENS_BANK = [
    "mechanism-first", "risk-first", "buyer-psychology", "distribution",
    "economics", "contrarian", "evidence-audit", "simplicity",
]

# Two-word phrases where a bare token ("offer", "brand") would fire on nearly
# every routine copy brief — guard stays conservative, but not hair-trigger.
STRATEGY_KEYWORDS = (
    "strategy", "positioning", "reposition", "pivot", "pricing", "new offer",
    "offer shelf", "business model", "brand strategy", "market entry",
    "go-to-market", "monetiz",
)

CONSTRAINTS_BASE = [
    "Grounding tags mandatory on every factual claim. In prose/files: 🟢 GROUNDED / "
    "🟡 SUPPLEMENTED / 🔴 PROJECTED. In any schema `tag` field: the plain word only — "
    "GROUNDED | SUPPLEMENTED | PROJECTED (no emoji; the emoji form fails schema "
    "validation) (swarm-commander Grounding Pass discipline; directives/quality_assurance.md).",
    "Density > completeness — every worker report capped at ≤500 tokens "
    "(feedback_density-over-completeness).",
    "No paid API calls without cost-gate approval (execution/cost_gate.py; "
    "hook-enforced PreToolUse block).",
    "12-worker cap on any single fan-out; never pin Opus — sub-agents inherit/run "
    "Sonnet, degrade a tier on unavailability rather than stalling.",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s or "mission"


def fan_out_for(pattern: str, effort: str) -> int:
    table = HEAVY_FAN_OUT if pattern == "heavy" else RESEARCH_FAN_OUT
    return table[effort]


def print_fan_out_mapping(pattern: str, effort: str, fan_out: int) -> None:
    if pattern == "heavy":
        mapping = ", ".join(f"{k}={v}" for k, v in HEAVY_FAN_OUT.items())
        print(f"Fan-out mapping (heavy): {mapping} -> effort={effort} selected {fan_out}")
    else:
        mapping = ", ".join(f"{k}={v} ({RESEARCH_DEPTH_LABEL[k]})" for k, v in RESEARCH_FAN_OUT.items())
        print(
            f"Fan-out mapping (research): {mapping} -> effort={effort} selected "
            f"{fan_out} subtopics ({RESEARCH_DEPTH_LABEL[effort]})"
        )


# ── Roster casting (heavy pattern only) — reuses council_cast.py ────────────
def _skill_dirs() -> Dict[str, Path]:
    if not SKILLS.exists():
        return {}
    return {d.name: d for d in SKILLS.iterdir() if d.is_dir() and (d / "SKILL.md").exists()}


def _skill_path_for_card(name: str, entry_prompt: str, skill_dirs: Dict[str, Path]) -> Optional[str]:
    """Resolve a council_cast card to a verified skills/<dir>/SKILL.md path."""
    m = re.match(r"skills/([^/]+)/", entry_prompt or "")
    if m and m.group(1) in skill_dirs:
        return f"skills/{m.group(1)}/SKILL.md"
    last = name.lower().split()[-1].strip("().") if name else ""
    if last and len(last) > 2:
        for d in skill_dirs:
            if last in d:
                return f"skills/{d}/SKILL.md"
    return None


def _genius_path_for(skill_path: Optional[str]) -> Optional[str]:
    if not skill_path:
        return None
    rel_dir = Path(skill_path).parent
    if (ROOT / rel_dir / "genius.md").exists():
        return str(rel_dir / "genius.md")
    return None


def _production_core_fallback(
    hint_text: str, needed: int, exclude_names: set, skill_dirs: Dict[str, Path]
) -> List[Dict[str, Any]]:
    """Graceful degrade: pick real skills off PRODUCTION_CORE.md matching the
    domain hint when council_cast can't fill the roster on its own."""
    if needed <= 0 or not PRODUCTION_CORE.exists():
        return []
    text = PRODUCTION_CORE.read_text(encoding="utf-8", errors="ignore")
    tokens = re.findall(r"`/?([a-zA-Z][a-zA-Z0-9-]{2,60})`", text)
    kws = set(re.findall(r"[a-zA-Z][a-zA-Z-]{2,}", hint_text.lower()))
    seen_dirs: set = set()
    candidates: List[str] = []
    for raw in tokens:
        tok = raw.strip("-").lower()
        if tok in skill_dirs and tok not in seen_dirs:
            candidates.append(tok)
            seen_dirs.add(tok)
            continue
        if len(tok) > 3:
            for d in skill_dirs:
                if tok in d and d not in seen_dirs:
                    candidates.append(d)
                    seen_dirs.add(d)
                    break

    def score(d: str) -> int:
        return sum(1 for k in kws if k in d)

    candidates.sort(key=score, reverse=True)
    out: List[Dict[str, Any]] = []
    for d in candidates:
        if len(out) >= needed:
            break
        display_name = d.replace("-", " ").title()
        if display_name in exclude_names:
            continue
        genius = SKILLS / d / "genius.md"
        out.append({
            "name": display_name,
            "skill": f"skills/{d}/SKILL.md",
            "genius": f"skills/{d}/genius.md" if genius.exists() else None,
            "fallback": True,
        })
    return out


def build_heavy_roster(brief: str, domains: str, fan_out: int) -> Tuple[List[Dict[str, Any]], List[str]]:
    """Cast `fan_out` file-verified experts for the heavy pattern via council_cast.py.

    Returns (roster, notes). Never raises — any casting failure degrades to the
    PRODUCTION_CORE.md fallback and is REPORTED in notes, never silent.
    """
    notes: List[str] = []
    skill_dirs = _skill_dirs()
    task_text = brief + (f" Domain hint: {domains}" if domains else "")
    roster: List[Dict[str, Any]] = []
    seen: set = set()

    try:
        import council_cast  # local import: keeps this script runnable even if absent
        plan = council_cast.build_council_plan(task_text, mode="deploy")
        cards = council_cast.parse_cards()
        entry_by_name = {c["name"]: c.get("entry_prompt", "") for c in cards}
        for member in plan.get("roster", []):
            if len(roster) >= fan_out:
                break
            if member.get("is_user"):
                continue
            name = member["name"]
            if name in seen:
                continue
            skill_path = _skill_path_for_card(name, entry_by_name.get(name, ""), skill_dirs)
            if not skill_path:
                continue  # unresolved file — skip, never crash
            roster.append({
                "name": name,
                "skill": skill_path,
                "genius": _genius_path_for(skill_path),
                "lens": LENS_BANK[len(roster) % len(LENS_BANK)],
            })
            seen.add(name)
        if len(roster) < fan_out:
            notes.append(
                f"council_cast produced only {len(roster)}/{fan_out} file-verified experts "
                "— topping up from PRODUCTION_CORE.md"
            )
    except Exception as exc:  # noqa: BLE001 — any casting failure degrades, never crashes
        notes.append(
            f"council_cast unavailable ({type(exc).__name__}: {exc}) — degrading entirely "
            "to PRODUCTION_CORE.md roster"
        )

    if len(roster) < fan_out:
        fallback = _production_core_fallback(domains or brief, fan_out - len(roster), seen, skill_dirs)
        for f in fallback:
            f["lens"] = LENS_BANK[len(roster) % len(LENS_BANK)]
            roster.append(f)
            seen.add(f["name"])
        if fallback:
            notes.append(f"added {len(fallback)} fallback expert(s) from PRODUCTION_CORE.md")

    if len(roster) < fan_out:
        notes.append(
            f"WARNING: roster short by {fan_out - len(roster)} — proceeding with "
            f"{len(roster)}/{fan_out} (never crash on missing files)"
        )

    return roster, notes


# ── Mission file: frontmatter is single-line JSON-per-key (valid YAML flow
# scalars) — stdlib-only, robust to colons/quotes/unicode in the brief, and
# trivially round-trippable with json.loads. ────────────────────────────────
def _fm_line(key: str, value: Any) -> str:
    return f"{key}: {json.dumps(value, ensure_ascii=False)}"


def render_mission_md(
    meta: Dict[str, Any], brief: str, roster: Optional[List[Dict[str, Any]]],
    constraints: List[str], plan_steps: List[str],
) -> str:
    lines = ["---"]
    for key in ("slug", "pattern", "effort", "fan_out", "created", "status", "deliverable", "question"):
        lines.append(_fm_line(key, meta.get(key)))
    if meta.get("pattern") == "heavy":
        lines.append(_fm_line("roster", roster or []))
    lines.append("---")
    body = ["", "## Objective", "", brief.strip(), "", "## Plan", ""]
    body += [f"- [ ] {step}" for step in plan_steps]
    body += ["", "## Constraints", ""]
    body += [f"- {c}" for c in constraints]
    body.append("")
    return "\n".join(lines) + "\n" + "\n".join(body)


def _parse_mission_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    fields: Dict[str, Any] = {}
    for line in block.splitlines():
        m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2)
        try:
            fields[k] = json.loads(v)
        except json.JSONDecodeError:
            fields[k] = v.strip().strip('"')
    return fields, body


def _update_frontmatter_field(text: str, key: str, value: Any) -> str:
    """Replace (or insert) one scalar frontmatter field, leaving the body untouched."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    block = text[3:end]
    rest = text[end:]
    new_line = _fm_line(key, value)
    pattern = re.compile(rf"^{re.escape(key)}:.*$", re.MULTILINE)
    if pattern.search(block):
        block = pattern.sub(new_line, block, count=1)
    else:
        block = block.rstrip("\n") + "\n" + new_line
    return "---" + block + rest


# ── plan ──────────────────────────────────────────────────────────────────
def cmd_plan(args: argparse.Namespace) -> int:
    if not args.brief.strip():
        print("ERROR: --brief cannot be empty", file=sys.stderr)
        return 1

    pattern = args.pattern
    effort = args.effort
    fan_out = fan_out_for(pattern, effort)
    slug = slugify(args.slug)
    if slug != args.slug:
        print(f"WARNING: slug normalized '{args.slug}' -> '{slug}'", file=sys.stderr)

    mission_dir = SWARM_DIR / slug
    mission_dir.mkdir(parents=True, exist_ok=True)
    mission_path = mission_dir / "mission.md"

    notes: List[str] = []
    roster: Optional[List[Dict[str, Any]]] = None
    if pattern == "heavy":
        roster, roster_notes = build_heavy_roster(args.brief, args.domains or "", fan_out)
        notes += roster_notes

    constraints = list(CONSTRAINTS_BASE)
    strategy_shaped = any(k in args.brief.lower() for k in STRATEGY_KEYWORDS)
    if strategy_shaped:
        constraints.append(
            "PATH DECISION guard: this brief reads as strategy-shaped — surface "
            f"{PATH_DECISION_DOC} (Incumbency Rule: no repositioning/new offers until "
            "$5K/mo COLLECTED) in the deliverable before recommending any pivot."
        )

    if pattern == "heavy":
        plan_steps = [
            "Cast expert roster (fixed at plan time — see frontmatter `roster`)",
            f"Launch {fan_out} independent expert trajectories on the same problem, each "
            "through its assigned lens, schema-constrained submit",
            "Reflective aggregation — synthesize WITHOUT blending away dissent; preserve forks",
            "Step 5.5 verification pass on the merged answer (claim inventory + labels)",
            "Package deliverable + honest receipt (`swarm_conductor.py receipt`)",
        ]
    else:
        depth_label = RESEARCH_DEPTH_LABEL[effort]
        plan_steps = [
            f"Decompose the question into {fan_out} subtopics (depth={depth_label})",
            "Parallel search workers — one per subtopic, word-ceilinged, source-locked",
            "Iterative deepen on promising clusters (gap-fill wave)",
            "Claim inventory: every finding labeled VERIFIED / LIKELY / UNCONFIRMED",
            "Honest receipt + visible task-trace section in the deliverable "
            "(`swarm_conductor.py receipt`)",
        ]

    meta: Dict[str, Any] = {
        "slug": slug,
        "pattern": pattern,
        "effort": effort,
        "fan_out": fan_out,
        "created": now_iso(),
        "status": "planned",
        "deliverable": args.deliverable or None,
        "question": args.brief,
    }
    mission_md = render_mission_md(meta, args.brief, roster, constraints, plan_steps)
    mission_path.write_text(mission_md, encoding="utf-8")

    rel_mission = mission_path.relative_to(ROOT)
    print(f"Mission file: {rel_mission}")
    print_fan_out_mapping(pattern, effort, fan_out)

    if notes:
        print("\nDegradation notes:")
        for n in notes:
            print(f"  - {n}")

    if pattern == "heavy":
        print(f"\nRoster ({len(roster or [])}/{fan_out}):")
        print(f"{'#':<3} {'Name':<24} {'Lens':<18} Skill")
        for i, m in enumerate(roster or [], 1):
            print(f"{i:<3} {m['name']:<24} {m['lens']:<18} {m['skill']}")

    print(f"\nPLAN GATE — reply 'go' to launch unattended, or edit {rel_mission} first.")

    if pattern == "heavy":
        wf_args = {
            "slug": slug,
            "brief": args.brief,
            "fanOut": fan_out,
            "roster": roster,
            "missionPath": str(rel_mission),
            "outDir": str(mission_dir.relative_to(ROOT)),
        }
        script_path = ".agent/workflows/swarm-heavy.workflow.js"
    else:
        wf_args = {
            "slug": slug,
            "question": args.brief,
            "depth": RESEARCH_DEPTH_LABEL[effort],
            "missionPath": str(rel_mission),
            "outDir": str(mission_dir.relative_to(ROOT)),
        }
        script_path = ".agent/workflows/swarm-research.workflow.js"

    print("\nWorkflow invocation:")
    print(f"  scriptPath: {script_path}")
    print(f"  args: {json.dumps(wf_args, indent=2, ensure_ascii=False)}")

    return 0


# ── receipt ───────────────────────────────────────────────────────────────
def cmd_receipt(args: argparse.Namespace) -> int:
    slug = slugify(args.slug)
    mission_path = SWARM_DIR / slug / "mission.md"
    if not mission_path.exists():
        print(f"ERROR: no mission file at {mission_path.relative_to(ROOT)} — run `plan` first", file=sys.stderr)
        return 1

    text = mission_path.read_text(encoding="utf-8")
    meta, _ = _parse_mission_frontmatter(text)
    pattern = meta.get("pattern", "unknown")
    brief = meta.get("question", "")
    fan_out = meta.get("fan_out", "?")
    roster = meta.get("roster") or []

    try:
        import run_receipt
    except Exception as exc:
        print(f"ERROR: run_receipt.py unavailable ({type(exc).__name__}: {exc})", file=sys.stderr)
        return 1

    expert_lenses = (
        "; ".join(f"{m.get('name')} [{m.get('lens')}]" for m in roster)
        if roster else "n/a (research pattern)"
    )
    receipt = run_receipt.build_receipt(
        query=brief,
        route=f"swarm/{pattern}",
        status=f"{args.status.upper()} — {args.agents} agent(s), {args.tokens} token(s) spent",
        owner="swarm",
        support_gates=f"12-worker cap; plan-gate compass-not-cage; fan_out={fan_out}",
        expert_lenses=expert_lenses,
        subagent_boundary=f"fan_out={fan_out}",
        subagents_requested=str(fan_out),
        meta_intent=f"swarm/{pattern} mission '{slug}'",
        composition_owner="swarm_conductor.py",
        changed=args.deliverable or "",
        passed=args.notes if args.status == "pass" else "",
        failed=args.notes if args.status == "fail" else "",
        judgment=args.notes if args.status == "partial" else "",
        next_action="Review deliverable; re-run `plan` for any flagged fork/gap.",
    )

    if args.dry_run:
        print(json.dumps({"dry_run": True, "would_write": False, "receipt_preview": receipt},
                          indent=2, ensure_ascii=False))
        print("(mission frontmatter NOT modified — dry run)")
        return 0

    paths = run_receipt.write_receipt(receipt)

    economics = (
        f"\n## Economics\n\n- **Agents spawned**: {args.agents}\n"
        f"- **Tokens spent**: {args.tokens}\n- **Fan-out planned**: {fan_out}\n"
    )
    with (ROOT / paths["markdown"]).open("a", encoding="utf-8") as fh:
        fh.write(economics)
    with run_receipt.LATEST_MD.open("a", encoding="utf-8") as fh:
        fh.write(economics)

    new_status = "failed" if args.status == "fail" else "done"
    updated = _update_frontmatter_field(text, "status", new_status)
    if args.deliverable:
        updated = _update_frontmatter_field(updated, "deliverable", args.deliverable)
    mission_path.write_text(updated, encoding="utf-8")

    print(json.dumps({**paths, "mission_status": new_status}, indent=2, ensure_ascii=False))
    return 0


# ── status ────────────────────────────────────────────────────────────────
def cmd_status(args: argparse.Namespace) -> int:
    if not SWARM_DIR.exists():
        print("(no swarm missions yet — .tmp/swarm/ does not exist)")
        return 0
    rows = []
    for mp in sorted(SWARM_DIR.glob("*/mission.md")):
        text = mp.read_text(encoding="utf-8", errors="ignore")
        meta, _ = _parse_mission_frontmatter(text)
        rows.append((
            meta.get("slug", mp.parent.name),
            meta.get("pattern", "?"),
            meta.get("status", "?"),
            meta.get("created", "?"),
        ))
    if not rows:
        print("(no missions found in .tmp/swarm/)")
        return 0
    for slug, pattern, status, created in rows:
        print(f"{slug:<32} pattern={pattern:<10} status={status:<10} created={created}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="swarm_conductor.py",
        description="Deterministic mission scaffolding for the /swarm conductor (Swarm Apex Session 1).",
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("plan", help="Build the Mission Plan file + print the plan gate.")
    pp.add_argument("--brief", required=True, help="The outcome wanted, verbatim.")
    pp.add_argument("--pattern", required=True, choices=["heavy", "research"])
    pp.add_argument("--effort", required=True, choices=["low", "medium", "high"])
    pp.add_argument("--slug", required=True, help="kebab-slug identifying this mission.")
    pp.add_argument("--domains", default="", help="Comma-separated domain hint for roster casting.")
    pp.add_argument("--deliverable", default="", help="Expected deliverable path.")
    pp.set_defaults(fn=cmd_plan)

    rp = sub.add_parser("receipt", help="Write the post-run receipt + flip mission status.")
    rp.add_argument("--slug", required=True)
    rp.add_argument("--status", required=True, choices=["pass", "partial", "fail"])
    rp.add_argument("--agents", type=int, required=True, help="Measured sub-agents spawned.")
    rp.add_argument("--tokens", type=int, required=True, help="Measured tokens spent.")
    rp.add_argument("--deliverable", default="")
    rp.add_argument("--notes", default="")
    rp.add_argument("--dry-run", action="store_true",
                     help="Build the receipt via run_receipt machinery but do not write it.")
    rp.set_defaults(fn=cmd_receipt)

    sp = sub.add_parser("status", help="List all missions under .tmp/swarm/.")
    sp.set_defaults(fn=cmd_status)

    args = ap.parse_args()
    try:
        return args.fn(args)
    except Exception as exc:  # noqa: BLE001 — CLI-level fail-safe, always report clearly
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
