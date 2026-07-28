#!/usr/bin/env python3
"""execution_receipt.py — did the machinery actually run, or was it only claimed?

WHY (Farrice, 2026-07-27): "I just need to know that certain skills, certain
workflows, and things were fully deployed versus being fooled into thinking
that 'oh yeah, we ran it' but we didn't, or we skimmed it."

Measured that day across 400 sessions / 9.5 days: 43 sessions wrote to a
deliverable path; 29 of them read fewer than 2 skill files; 13 read ZERO.
`content_creation_gate` sets the floor at 2. Nothing had ever checked it.

The root cause was never missing proof — it was proof with no reader:
  - verify_fleet: 73 verifiers, 12 failing, written to .agent/health/fleet.log
  - citation_integrity: 2 broken pointers, written to .agent/citation-integrity.log
  - the session ledger: knew every skill load, rendered to nobody
Three honest signals, three dead channels. This module is the reader.

CONTRACT
  - REPORTS ONLY. Never blocks, never accrues debt, never writes to the ledger.
    (Compass doctrine 2026-07-27: only the cost gate and the factual veto block.)
  - Reads CACHED health artifacts. Never runs verify_fleet or citation_integrity
    itself — a Stop hook has a 10s budget and those take minutes.
  - Stale evidence is reported AS stale, never silently as green. A check that
    last ran a week ago tells you about last week.
  - Fail-safe: render() never raises. A broken receipt must not trap a session.

USAGE
    python3 execution/execution_receipt.py                 # latest session
    python3 execution/execution_receipt.py <session_id>
    python3 execution/execution_receipt.py --all           # every live ledger
    python3 execution/execution_receipt.py --json
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SESSIONS_DIR = REPO_ROOT / ".agent" / "sessions"
HEALTH_DIR = REPO_ROOT / ".agent" / "health"
FLEET_JSON = HEALTH_DIR / "verify-fleet.json"
CITATION_LOG = REPO_ROOT / ".agent" / "citation-integrity.log"
SKILLS_DIR = REPO_ROOT / "skills"

# directives/content_creation_gate.md — content work loads >= 2 skill files.
CONTENT_SKILL_FLOOR = 2

# Evidence older than this is reported as stale rather than as a verdict.
FLEET_STALE_DAYS = 8      # fleet runs Sundays; >8d means a run was missed
CITATION_STALE_DAYS = 2   # citation-integrity runs daily

# Repo-relative roots whose writes count as durable work.
#
# BUG FOUND IN FIRST REAL RUN (2026-07-27), and the correction to it, because
# both matter:
#   The list was too SHORT. It shipped without guides/, docs/, skills/ or
#   execution/ — so real sessions writing there scored zero deliverables and
#   UNDER FLOOR never fired. A false GREEN from the anti-false-green check.
#   My first stated root cause for that was "absolute-path substring
#   matching," and that was WRONG: `guides/` is a substring of the absolute
#   path too, so substring matching would have worked. Proven by reverting
#   the change and watching the regression test still pass. The path-form fix
#   below is real but SEPARATE robustness — it stops `~/Downloads/projects/x`
#   (outside the repo) from scoring as a deliverable.
DELIVERABLE_ROOTS = ("deliverables/", "_active/", "products/", "projects/",
                     "clients/", "strategy_briefs/", "research_outputs/",
                     "guides/", "knowledge/", "docs/", "skills/", "execution/",
                     "directives/", "agents/", "extractions/")
EPHEMERAL = ("/scratchpad/", "/private/tmp/", "/tmp/", "/.tmp/")


# ──────────────────────────────────────────────────────────────────
# evidence loaders — each returns (status, detail) and never raises
# ──────────────────────────────────────────────────────────────────
def _age_days(p: Path) -> float | None:
    try:
        return (datetime.now() - datetime.fromtimestamp(p.stat().st_mtime)).total_seconds() / 86400
    except OSError:
        return None


def fleet_status() -> tuple[str, str]:
    """Verifier fleet: the 73-check Sunday train. RED here means the harness
    is failing its own tests, whatever this session did."""
    age = _age_days(FLEET_JSON)
    if age is None:
        return "UNKNOWN", "never run — `python3 execution/verify_fleet.py run`"
    try:
        d = json.loads(FLEET_JSON.read_text())
    except (OSError, ValueError) as e:
        return "UNKNOWN", f"unreadable ({type(e).__name__})"
    counts = d.get("counts") or {}
    failing = d.get("failing") or []
    total = d.get("total", sum(counts.values()) if counts else 0)
    stale = f" [STALE {age:.0f}d]" if age > FLEET_STALE_DAYS else ""
    when = str(d.get("ts", ""))[:10]
    if failing:
        head = ", ".join(str(f) for f in failing[:3])
        more = f" +{len(failing) - 3} more" if len(failing) > 3 else ""
        return "RED", (f"{len(failing)} of {total} failing (ran {when}){stale} — "
                       f"{head}{more}")
    return "GREEN", f"{counts.get('PASS', 0)}/{total} pass (ran {when}){stale}"


def citation_status() -> tuple[str, str]:
    """Broken doc/memory pointers. A live doc citing a missing file is a
    LOSS SIGNAL — it usually means work exists only in an orphaned branch."""
    age = _age_days(CITATION_LOG)
    if age is None:
        return "UNKNOWN", "no cached run — `python3 execution/citation_integrity.py`"
    try:
        txt = CITATION_LOG.read_text(errors="replace")
    except OSError:
        return "UNKNOWN", "log unreadable"
    stale = f" [STALE {age:.0f}d]" if age > CITATION_STALE_DAYS else ""
    tail = txt.strip().splitlines()[-40:]
    for line in reversed(tail):
        s = line.strip()
        if "missing pointer" in s:
            n = s.split()[0]
            if n.isdigit() and int(n) > 0:
                return "RED", f"{n} broken pointer(s){stale} — `python3 execution/citation_integrity.py`"
            return "GREEN", f"no broken pointers{stale}"
    return "UNKNOWN", f"no verdict line in log{stale}"


# ──────────────────────────────────────────────────────────────────
# ledger reading
# ──────────────────────────────────────────────────────────────────
def latest_ledger_path() -> Path | None:
    try:
        files = sorted(SESSIONS_DIR.glob("ledger-*.json"),
                       key=lambda p: p.stat().st_mtime, reverse=True)
        return files[0] if files else None
    except OSError:
        return None


def load_ledger(session_id: str | None) -> tuple[dict | None, Path | None]:
    if session_id:
        import re
        safe = re.sub(r"[^A-Za-z0-9_-]", "_", session_id)[:64]
        p = SESSIONS_DIR / f"ledger-{safe}.json"
    else:
        p = latest_ledger_path()
    if not p or not p.exists():
        return None, p
    try:
        return json.loads(p.read_text()), p
    except (OSError, ValueError):
        return None, p


def _is_expert(name: str) -> bool:
    return (SKILLS_DIR / name / "genius.md").exists()


def _rel(p: str) -> str:
    """Repo-relative form of an absolute ledger path (unchanged if outside)."""
    try:
        return str(Path(p).resolve().relative_to(REPO_ROOT))
    except (ValueError, OSError):
        return p


def _deliverables(ledger: dict) -> list[str]:
    out = []
    for p in (ledger.get("produced_paths") or []):
        if any(e in p for e in EPHEMERAL):
            continue
        r = _rel(p)
        if any(r.startswith(root) for root in DELIVERABLE_ROOTS):
            out.append(r)
    return out


def _has_manifest(ledger: dict) -> bool:
    """True only for sessions recorded AFTER the manifest shipped.

    Ledgers written before 2026-07-27 have no manifest. Judging them on
    absent data would print TIER 1 ONLY and NO GROUNDING for work that may
    well have loaded genius.md — a false RED, which erodes trust in the
    receipt exactly as fast as a false green does. Legacy sessions get their
    facts reported and their manifest-derived flags withheld.
    """
    m = ledger.get("manifest")
    return isinstance(m, dict) and "reads_total" in m


# ──────────────────────────────────────────────────────────────────
# the receipt
# ──────────────────────────────────────────────────────────────────
def build(ledger: dict) -> dict:
    """Structured receipt. Pure function of the ledger + cached health files."""
    m = ledger.get("manifest") or {}
    debts = ledger.get("debts") or []

    full = list(m.get("skills_full") or [])
    genius = list(m.get("genius_read") or [])
    grepped = [d["name"] for d in debts if d.get("type") == "skill_grepped"]
    loaded = [d["name"] for d in debts if d.get("type") == "skill_loaded"]
    # Union: a skill can reach the ledger via the Skill tool without a Read.
    all_full = sorted(set(full) | set(loaded))
    experts = [s for s in all_full if _is_expert(s)]

    deliv = _deliverables(ledger)
    gates = list(m.get("gates_run") or [])
    live = _has_manifest(ledger)

    flags: list[str] = []

    if deliv and len(all_full) < CONTENT_SKILL_FLOOR:
        flags.append(
            f"UNDER FLOOR — content_creation_gate wants >= {CONTENT_SKILL_FLOOR} skill "
            f"files; {len(all_full)} loaded while writing {len(deliv)} deliverable(s)")
    if grepped:
        flags.append(
            f"PARTIAL LOAD — {', '.join(sorted(set(grepped)))} reached only via "
            f"grep/sed/head, never a full read (Tier 1 not met)")
    # Depth and grounding are manifest-derived: on a legacy ledger their
    # absence is missing data, not a finding. Withheld rather than guessed.
    tier1_only = [s for s in experts if s not in genius] if live else []
    if tier1_only:
        flags.append(
            f"TIER 1 ONLY — {', '.join(tier1_only[:6])}"
            f"{f' +{len(tier1_only) - 6} more' if len(tier1_only) > 6 else ''} "
            f"loaded SKILL.md without genius.md (no Tier 2 depth)")
    if live and deliv and not m.get("recall_calls") and "tier_1_5b_memory_facade" not in gates:
        flags.append(
            "NO GROUNDING — neither Recall (Tier 1.5a) nor memory_facade (Tier 1.5b) "
            "ran before producing")
    if deliv and not ledger.get("finalized_at"):
        flags.append("NO FINALIZE — Chain Step 6 never ran on produced work")
    if ledger.get("finalize_failures"):
        flags.append(f"FINALIZE FAILED x{ledger['finalize_failures']} — scores were never logged")

    f_st, f_det = fleet_status()
    c_st, c_det = citation_status()
    if f_st == "RED":
        flags.append(f"HARNESS RED — verify fleet: {f_det}")
    if c_st == "RED":
        flags.append(f"BROKEN POINTERS — citation integrity: {c_det}")

    return {
        "session_id": ledger.get("session_id"),
        "manifest_live": live,
        "skills_full": all_full,
        "skills_expert": experts,
        "genius_read": sorted(genius),
        "skills_partial": sorted(set(grepped)),
        "workflows_read": sorted(m.get("workflows_read") or []),
        "directives_read": sorted(m.get("directives_read") or []),
        "skill_tool_calls": sorted(m.get("skill_tool_calls") or []),
        "gates_run": sorted(gates),
        "recall_calls": int(m.get("recall_calls") or 0),
        "reads_total": int(m.get("reads_total") or 0),
        "subagent_spawns": int(ledger.get("subagent_spawns") or 0),
        "deliverables": deliv,
        "produced_paths": ledger.get("produced_paths") or [],
        "finalized_at": ledger.get("finalized_at"),
        "fleet": {"status": f_st, "detail": f_det},
        "citations": {"status": c_st, "detail": c_det},
        "flags": flags,
    }


def _fmt_list(vals: list[str], empty: str = "none") -> str:
    return ", ".join(vals) if vals else empty


def render(ledger: dict) -> str:
    """Human-readable receipt. Never raises — a render bug must not trap a session."""
    try:
        r = build(ledger)
    except Exception as e:  # noqa: BLE001 — fail-safe by contract
        return f"EXECUTION RECEIPT — unavailable ({type(e).__name__}: {e})"

    sid = str(r["session_id"] or "unknown")[:8]
    L = [f"EXECUTION RECEIPT — session {sid} (deterministic, from the tool log — not a claim)"]

    if not r["manifest_live"]:
        L.append("  [legacy session — recorded before the manifest shipped; "
                 "depth and grounding unknown, not assumed]")

    if r["deliverables"]:
        L.append(f"  Produced   : {_fmt_list(r['deliverables'][-3:])}")
    elif r["produced_paths"]:
        L.append(f"  Produced   : {_fmt_list([_rel(p) for p in r['produced_paths'][-2:]])}"
                 " (internal/ephemeral)")
    else:
        L.append("  Produced   : nothing durable")

    depth = []
    for s in r["skills_full"]:
        tier = ("T2" if s in r["genius_read"] else "T1") if r["manifest_live"] else "?"
        depth.append(f"{s}[{tier}]")
    L.append(f"  Skills     : {_fmt_list(depth[:8])}"
             + (f" +{len(depth) - 8} more" if len(depth) > 8 else "")
             + (f"   PARTIAL: {_fmt_list(r['skills_partial'])}" if r["skills_partial"] else ""))
    if r["workflows_read"]:
        L.append(f"  Workflows  : {_fmt_list(r['workflows_read'][:6])}")
    if r["skill_tool_calls"]:
        L.append(f"  Skill calls: {_fmt_list(r['skill_tool_calls'][:6])}")
    if r["manifest_live"]:
        L.append(f"  Grounding  : recall x{r['recall_calls']}"
                 f" | gates: {_fmt_list(r['gates_run'])}")
        L.append(f"  Reads {r['reads_total']:<4} | subagents {r['subagent_spawns']}"
                 f" | finalize {'yes' if r['finalized_at'] else 'NO'}")
    else:
        L.append(f"  Subagents {r['subagent_spawns']}"
                 f" | finalize {'yes' if r['finalized_at'] else 'NO'}")
    L.append(f"  Harness    : fleet {r['fleet']['status']} — {r['fleet']['detail']}")
    L.append(f"               citations {r['citations']['status']} — {r['citations']['detail']}")

    if r["flags"]:
        L.append(f"  {len(r['flags'])} FLAG(S) — reported, nothing blocked:")
        L.extend(f"    - {f}" for f in r["flags"])
    else:
        L.append("  CLEAN — every declared step left a trace in the tool log.")
    return "\n".join(L)


def main() -> int:
    args = [a for a in sys.argv[1:]]
    as_json = "--json" in args
    args = [a for a in args if not a.startswith("--")]

    if "--all" in sys.argv:
        try:
            paths = sorted(SESSIONS_DIR.glob("ledger-*.json"),
                           key=lambda p: p.stat().st_mtime, reverse=True)
        except OSError:
            paths = []
        cutoff = datetime.now() - timedelta(days=7)
        shown = 0
        for p in paths:
            try:
                if datetime.fromtimestamp(p.stat().st_mtime) < cutoff:
                    continue
                led = json.loads(p.read_text())
            except (OSError, ValueError):
                continue
            if not led.get("produced"):
                continue
            print(render(led)); print()
            shown += 1
        if not shown:
            print("No producing sessions in the last 7 days.")
        return 0

    ledger, path = load_ledger(args[0] if args else None)
    if ledger is None:
        print(f"No ledger found{f' at {path}' if path else ''}.", file=sys.stderr)
        return 2
    if as_json:
        print(json.dumps(build(ledger), indent=2))
    else:
        print(render(ledger))
    return 0


if __name__ == "__main__":
    sys.exit(main())
