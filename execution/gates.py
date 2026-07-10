#!/usr/bin/env python3
"""
Autopilot taste gates — deterministic evaluation of G1/G2/G3.

Wave 2 (Verifier Layer) of the Harness Apex Plan: the three gate conditions
in `.agent/workflows/autopilot.md` were multi-clause prose that mid-tier
models collapse or skip. This script turns them into an exit code.

Gates:
  G1 — Intent:      DICE score <= 2 -> fires (sharpen via ONE DICE question round)
  G2 — Cost:        est-cost > $5 OR any --services entry returns
                    needs-approval/denied from cost_gate.py check -> fires
  G3 — Prose/taste: --deliverable given AND --expert-score >= 7 AND
                    prose_classifier verdict FLAGGED -> fires

Degraded-graceful contract: a gate whose inputs were not provided is reported
as "not evaluated (missing --x)" — it is never silently passed.

Exit codes:
  0 = no gate fires (not-evaluated gates are reported, they do not fire)
  2 = at least one gate fires (informational, not an error)
  1 = usage / internal error only

Usage:
  python3 execution/gates.py check --dice 4
  python3 execution/gates.py check --dice 4 --est-cost 12
  python3 execution/gates.py check --dice 4 --services higgsfield-cinema,fal-kling
  python3 execution/gates.py check --dice 5 --deliverable draft.md --expert-score 8
  python3 execution/gates.py check --dice 3 --json
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COST_GATE = ROOT / "execution" / "cost_gate.py"

# Autopilot G2 threshold: paid spend above this needs a one-time approval.
EST_COST_THRESHOLD_USD = 5.00
# Autopilot G3 threshold: taste call only when Expert Standard is trending high.
EXPERT_SCORE_THRESHOLD = 7

FIRES = "fires"
PASS = "pass"
NOT_EVALUATED = "not_evaluated"


def _gate(status: str, reason: str, remediation: str = "") -> dict:
    return {"status": status, "reason": reason, "remediation": remediation}


# ───────────────────────────────────────────────────────────────────
# G1 — Intent
# ───────────────────────────────────────────────────────────────────
def check_g1(dice: int) -> dict:
    if dice <= 2:
        return _gate(
            FIRES,
            f"DICE intent score {dice} <= 2 — intent too vague to execute safely",
            "Sharpen via ONE DICE question round on the missing dimensions only "
            "(Deliverable/Audience/Context/End state/Specific language), then re-run: "
            "python3 execution/gates.py check --dice <new-score>",
        )
    return _gate(PASS, f"DICE intent score {dice} >= 3 — write assumptions and proceed, no halt")


# ───────────────────────────────────────────────────────────────────
# G2 — Cost
# ───────────────────────────────────────────────────────────────────
def _check_service(service: str) -> dict:
    """Run cost_gate.py check for one service. Returns a per-service verdict.

    cost_gate.py check exit codes: 0=approved, 2=needs approval, 1=denied/unknown.
    """
    try:
        proc = subprocess.run(
            [sys.executable, str(COST_GATE), "check", "--service", service],
            capture_output=True, text=True, cwd=str(ROOT), timeout=60,
        )
    except Exception as e:  # cost_gate missing/broken must not silently pass
        return {"service": service, "decision": "error", "detail": str(e)}
    code = proc.returncode
    decision = {0: "approved", 2: "needs_approval", 1: "denied"}.get(code, f"exit={code}")
    detail = (proc.stderr.strip() or proc.stdout.strip()).splitlines()
    return {"service": service, "decision": decision, "detail": detail[1] if len(detail) > 1 else (detail[0] if detail else "")}


def check_g2(est_cost: float | None, services: list[str]) -> dict:
    if est_cost is None and not services:
        return _gate(NOT_EVALUATED, "not evaluated (missing --est-cost and --services)")

    reasons: list[str] = []
    remedies: list[str] = []
    service_results: list[dict] = []

    if est_cost is not None and est_cost > EST_COST_THRESHOLD_USD:
        reasons.append(f"estimated paid spend ${est_cost:.2f} > ${EST_COST_THRESHOLD_USD:.2f} threshold")
        remedies.append(
            "Ask Farrice once for this run; before each paid call run "
            "python3 execution/cost_gate.py check --service <id> and, after an explicit yes, "
            "python3 execution/cost_gate.py approve --service <id>"
        )

    for svc in services:
        res = _check_service(svc)
        service_results.append(res)
        if res["decision"] == "needs_approval":
            reasons.append(f"service '{svc}' needs approval per cost_gate")
            remedies.append(
                f"Ask Farrice once; ONLY after explicit yes run: "
                f"python3 execution/cost_gate.py approve --service {svc}  (15-min token), then retry"
            )
        elif res["decision"] == "denied":
            reasons.append(f"service '{svc}' DENIED by cost_gate ({res['detail']})")
            remedies.append(
                f"HARD BLOCK — surface to Farrice, do not retry. Inspect: "
                f"python3 execution/cost_gate.py status  (service: {svc})"
            )
        elif res["decision"] == "error":
            reasons.append(f"service '{svc}' cost_gate check errored: {res['detail']}")
            remedies.append("Fix cost_gate invocation, then re-run gates.py check")

    if reasons:
        gate = _gate(FIRES, "; ".join(reasons), " | ".join(remedies))
    else:
        evaluated = []
        if est_cost is not None:
            evaluated.append(f"est-cost ${est_cost:.2f} <= ${EST_COST_THRESHOLD_USD:.2f}")
        if services:
            evaluated.append(f"{len(services)} service(s) approved by cost_gate")
        gate = _gate(PASS, "; ".join(evaluated))
    if service_results:
        gate["services"] = service_results
    return gate


# ───────────────────────────────────────────────────────────────────
# G3 — Prose/taste
# ───────────────────────────────────────────────────────────────────
def check_g3(deliverable: str | None, expert_score: int | None) -> dict:
    missing = []
    if deliverable is None:
        missing.append("--deliverable")
    if expert_score is None:
        missing.append("--expert-score")
    if missing:
        return _gate(NOT_EVALUATED, f"not evaluated (missing {' and '.join(missing)})")

    if expert_score < EXPERT_SCORE_THRESHOLD:
        return _gate(
            PASS,
            f"expert-score {expert_score} < {EXPERT_SCORE_THRESHOLD} — "
            "G3 taste-call threshold not met, prose check not required",
        )

    path = Path(deliverable)
    if not path.exists():
        return _gate(
            FIRES,
            f"deliverable path not found: {deliverable} — cannot verify prose, failing loud",
            "Fix the path, then re-run: python3 execution/gates.py check --dice <n> "
            f"--deliverable <path> --expert-score {expert_score}",
        )

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from prose_classifier import classify_prose
        result = classify_prose(path.read_text())
    except Exception as e:
        return _gate(
            FIRES,
            f"prose_classifier failed on {deliverable}: {e} — cannot verify prose, failing loud",
            "Repair prose_classifier or the file encoding, then re-run gates.py check",
        )

    verdict = result["verdict"]
    if verdict == "FLAGGED":
        return _gate(
            FIRES,
            f"prose FLAGGED (AI score {result['ai_score']}/10, {result['signal_count']} signals) "
            f"with expert-score {expert_score} >= {EXPERT_SCORE_THRESHOLD}",
            "Surface exactly ONE taste call to Farrice — bimodal PASS/FAIL, -1/dimension on a FAIL, "
            "never re-litigate the whole draft. Detail: "
            f"python3 execution/prose_classifier.py check {deliverable}",
        )
    return _gate(
        PASS,
        f"prose {verdict} (AI score {result['ai_score']}/10) — no taste call required",
    )


# ───────────────────────────────────────────────────────────────────
# CLI
# ───────────────────────────────────────────────────────────────────
def cmd_check(args) -> int:
    services = [s.strip() for s in (args.services or "").split(",") if s.strip()]
    gates = {
        "G1_intent": check_g1(args.dice),
        "G2_cost": check_g2(args.est_cost, services),
        "G3_prose": check_g3(args.deliverable, args.expert_score),
    }
    fired = [name for name, g in gates.items() if g["status"] == FIRES]
    exit_code = 2 if fired else 0

    if args.json:
        print(json.dumps({"gates": gates, "fired": fired, "exit_code": exit_code}, indent=2))
        return exit_code

    icons = {FIRES: "🔴 FIRES", PASS: "✅ PASS", NOT_EVALUATED: "⚪ NOT EVALUATED"}
    print("=" * 64)
    print("AUTOPILOT TASTE GATES (G1 intent / G2 cost / G3 prose)")
    print("=" * 64)
    for name, g in gates.items():
        print(f"{name:<10s} {icons[g['status']]:<18s} {g['reason']}")
        if g["status"] == FIRES and g.get("remediation"):
            print(f"{'':10s} ↳ remediation: {g['remediation']}")
    print("-" * 64)
    if fired:
        print(f"VERDICT: {len(fired)} gate(s) fire → {', '.join(fired)}  (exit 2 — informational halt)")
    else:
        print("VERDICT: no gate fires — run end-to-end, close with Friction Ledger + Run Receipt (exit 0)")
    return exit_code


def main() -> int:
    p = argparse.ArgumentParser(description="Deterministic evaluation of autopilot's G1/G2/G3 taste gates")
    sub = p.add_subparsers(dest="cmd", required=True)

    pc = sub.add_parser("check", help="Evaluate the three taste gates against provided inputs")
    pc.add_argument("--dice", type=int, required=True, choices=range(1, 6), metavar="1-5",
                    help="DICE intent score per CLAUDE.md Step 1")
    pc.add_argument("--est-cost", type=float, default=None,
                    help="Estimated total paid spend for this run, in dollars")
    pc.add_argument("--services", default="",
                    help="CSV of paid service ids to pre-check via cost_gate.py (see cost_gate.py status)")
    pc.add_argument("--deliverable", default=None,
                    help="Path to the content artifact for the G3 prose check")
    pc.add_argument("--expert-score", type=int, default=None,
                    help="Expert Standard dimension score (1-10) trending for this deliverable")
    pc.add_argument("--json", action="store_true", help="Emit machine-readable JSON")

    args = p.parse_args()
    return {"check": cmd_check}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
