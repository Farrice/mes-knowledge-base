#!/usr/bin/env python3
"""
Chain Runner — Deterministic enforcement engine for Antigravity's Chain.

Replaces Steps 6-7 of The Chain (Quality Gate + Performance Log) with a
single finalize() call that cannot be forgotten or partially executed.

What finalize() does (in order):
    1. Validates all 3 quality sub-scores are present
    2. Calculates composite quality score
    3. Determines pass/fail against the quality gate thresholds
    4. Checks for regression against skill's rolling baseline
    5. Logs to Notion Performance Database
    6. Activates protocol tracking on quality_gate.md and feedback-ratchet.md
    7. Writes session state checkpoint

Usage:
    from execution.chain_runner import finalize

    result = finalize(
        output_description="LinkedIn carousel on AI-first positioning",
        expert="lara-acosta",
        skill="lara-acosta-linkedin-ghostwriting",
        workflow="high-dwell",
        task_type="Content",
        intent_alignment=8,
        expert_standard=7,
        adversarial_resilience=8,
    )
    # result contains: composite_score, passed, regression_check, notion_url, etc.

CLI:
    python execution/chain_runner.py finalize "LinkedIn carousel" \\
        --expert lara-acosta \\
        --skill lara-acosta-linkedin-ghostwriting \\
        --workflow high-dwell \\
        --type Content \\
        --intent 8 --expert-score 7 --adversarial 8

IMPORTANT: This script is additive — it calls existing execution/ scripts
(log_performance.py, protocol_tracker.py, checkpoint_manager.py) but does
not modify any directives, skills, or system architecture. It only enforces
what already exists.
"""

import os
import sys
import json
import argparse
from datetime import date, datetime
from pathlib import Path
from typing import Optional, Dict, Any

# Ensure execution/ is on the path for sibling imports
sys.path.insert(0, str(Path(__file__).parent))

from log_performance import log_output, check_regression, get_baseline
from protocol_tracker import activate_protocol
from checkpoint_manager import save_session_state

# Evolution trace directory
TRACE_DIR = Path(__file__).parent.parent / "evolution_store" / "traces"


# Quality Gate thresholds (from directives/quality_gate.md)
COMPOSITE_PASS_THRESHOLD = 7
SINGLE_DIMENSION_MIN = 6

# Protocols to activate on finalize
QUALITY_GATE_PATH = "directives/quality_gate.md"
FEEDBACK_RATCHET_PATH = "directives/feedback-ratchet.md"
SESSION_STATE_PATH = "directives/session-state-protocol.md"


def finalize(
    output_description: str,
    expert: str = "",
    skill: str = "",
    workflow: str = "",
    task_type: str = "System",
    intent_alignment: Optional[float] = None,
    expert_standard: Optional[float] = None,
    adversarial_resilience: Optional[float] = None,
    notes: str = "",
    user_rating: Optional[float] = None,
    experiment_tag: str = "",
    skip_notion: bool = False,
    write_trace: bool = False,
) -> Dict[str, Any]:
    """
    Enforce the complete Chain Steps 6-7 in a single deterministic call.

    Args:
        output_description: What was produced (for the performance log).
        expert: The expert agent used (e.g., "lara-acosta").
        skill: The skill directory name (e.g., "lara-acosta-linkedin-ghostwriting").
        workflow: The workflow file name (e.g., "high-dwell").
        task_type: Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis
        intent_alignment: Quality Gate score 1-10 for intent alignment.
        expert_standard: Quality Gate score 1-10 for expert standard.
        adversarial_resilience: Quality Gate score 1-10 for adversarial resilience.
        notes: Freeform notes about what worked/didn't.
        user_rating: Optional user-provided rating (1-10).
        experiment_tag: Optional experiment tag for A/B testing.
        skip_notion: If True, skip Notion logging (for testing).

    Returns:
        Dict with:
            - composite_score: Average of 3 sub-scores
            - passed: Whether the quality gate passed
            - failed_dimensions: List of dimensions that scored < 6
            - regression_check: Result from check_regression()
            - notion_result: Result from log_output() (or None if skipped)
            - protocols_activated: List of activated protocol files
            - session_state_written: Whether session state was saved
            - status: "Keep" if passed, "Needs Improvement" if not
    """
    result = {
        "output": output_description,
        "expert": expert,
        "skill": skill,
        "timestamp": datetime.now().isoformat(),
    }

    # ── Step 1: Validate scores ──────────────────────────────────
    missing = []
    if intent_alignment is None:
        missing.append("intent_alignment")
    if expert_standard is None:
        missing.append("expert_standard")
    if adversarial_resilience is None:
        missing.append("adversarial_resilience")

    if missing:
        result["success"] = False
        result["error"] = f"Missing required quality scores: {', '.join(missing)}. The quality gate requires all 3 sub-scores."
        return result

    # ── Step 2: Calculate composite ──────────────────────────────
    composite = round((intent_alignment + expert_standard + adversarial_resilience) / 3, 1)
    result["composite_score"] = composite
    result["intent_alignment"] = intent_alignment
    result["expert_standard"] = expert_standard
    result["adversarial_resilience"] = adversarial_resilience

    # ── Step 3: Quality Gate pass/fail ───────────────────────────
    failed_dimensions = []
    if intent_alignment < SINGLE_DIMENSION_MIN:
        failed_dimensions.append(f"intent_alignment ({intent_alignment})")
    if expert_standard < SINGLE_DIMENSION_MIN:
        failed_dimensions.append(f"expert_standard ({expert_standard})")
    if adversarial_resilience < SINGLE_DIMENSION_MIN:
        failed_dimensions.append(f"adversarial_resilience ({adversarial_resilience})")

    passed = composite >= COMPOSITE_PASS_THRESHOLD and len(failed_dimensions) == 0
    status = "Keep" if passed else "Needs Improvement"

    result["passed"] = passed
    result["failed_dimensions"] = failed_dimensions
    result["status"] = status

    if not passed:
        if failed_dimensions:
            result["gate_message"] = f"⚠️  QUALITY GATE FAIL — Composite: {composite}, Failed dimensions: {', '.join(failed_dimensions)}. Retry weakest section."
        else:
            result["gate_message"] = f"⚠️  QUALITY GATE MARGINAL — Composite: {composite} (below {COMPOSITE_PASS_THRESHOLD}). Consider improving weakest dimension."
    else:
        result["gate_message"] = f"✅  QUALITY GATE PASS — Composite: {composite}"

    # ── Step 4: Regression check ─────────────────────────────────
    if skill:
        try:
            regression = check_regression(skill=skill, latest_score=composite)
            result["regression_check"] = regression
        except Exception as e:
            result["regression_check"] = {"error": str(e), "message": f"Regression check failed: {e}"}
    else:
        result["regression_check"] = {"message": "No skill specified — skipping regression check."}

    # ── Step 5: Log to Notion Performance DB ─────────────────────
    if not skip_notion:
        try:
            notion_result = log_output(
                output=output_description,
                agent=expert,
                skill=skill,
                workflow=workflow,
                task_type=task_type,
                quality_score=composite,
                user_rating=user_rating,
                intent_alignment=intent_alignment,
                expert_standard=expert_standard,
                adversarial_resilience=adversarial_resilience,
                status=status,
                notes=notes,
                experiment_tag=experiment_tag,
            )
            result["notion_result"] = {"success": True, "url": notion_result.get("url", "logged")}
        except Exception as e:
            result["notion_result"] = {"success": False, "error": str(e)}
    else:
        result["notion_result"] = {"success": True, "skipped": True}

    # ── Step 6: Activate protocol tracking ───────────────────────
    protocols_activated = []
    for protocol_path in [QUALITY_GATE_PATH, FEEDBACK_RATCHET_PATH]:
        try:
            activation = activate_protocol(protocol_path, note=f"chain_runner finalize for {skill or expert or task_type}")
            if activation.get("success"):
                protocols_activated.append(protocol_path)
        except Exception as e:
            # Non-fatal: protocol tracking is observability, not critical path
            pass

    result["protocols_activated"] = protocols_activated

    # ── Step 7: Write session state checkpoint ───────────────────
    try:
        save_session_state(
            active_task=f"Produced {task_type}: {output_description}",
            experts_deployed=[{"name": expert, "contribution": f"Produced {task_type} output"}] if expert else None,
            key_findings=[
                f"Quality: {composite}/10 ({status})",
                result.get("regression_check", {}).get("message", "No regression data"),
            ],
            current_phase="Post-production (finalized)",
            next_steps=["Review output quality", "Check Notion Performance Log for trends"],
        )
        result["session_state_written"] = True

        # Also activate the session state protocol
        try:
            activate_protocol(SESSION_STATE_PATH, note="chain_runner session checkpoint")
            protocols_activated.append(SESSION_STATE_PATH)
        except Exception:
            pass
    except Exception as e:
        result["session_state_written"] = False

    result["success"] = True

    # ── Step 8 (optional): Write evolution trace ─────────────────
    if write_trace:
        try:
            TRACE_DIR.mkdir(parents=True, exist_ok=True)
            trace = {
                "timestamp": result["timestamp"],
                "output": output_description,
                "expert": expert,
                "skill": skill,
                "workflow": workflow,
                "task_type": task_type,
                "intent_alignment": intent_alignment,
                "expert_standard": expert_standard,
                "adversarial_resilience": adversarial_resilience,
                "composite_score": composite,
                "status": status,
                "passed": passed,
                "failed_dimensions": failed_dimensions,
                "regression": result.get("regression_check", {}),
                "notes": notes,
                "experiment_tag": experiment_tag,
            }
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            trace_file = TRACE_DIR / f"trace_{ts}_{skill or expert or 'unknown'}.json"
            with open(trace_file, "w") as f:
                json.dump(trace, f, indent=2)
            result["trace_file"] = str(trace_file)
        except Exception as e:
            result["trace_file"] = f"ERROR: {e}"

    return result


def print_result(result: Dict) -> None:
    """Pretty-print the finalize result."""
    if not result.get("success"):
        print(f"\n  ❌ FINALIZE FAILED: {result.get('error', 'Unknown error')}")
        return

    print("\n" + "=" * 60)
    print("  CHAIN FINALIZE — Steps 6-7 Complete")
    print("=" * 60)
    print(f"  Output:     {result['output']}")
    print(f"  Expert:     {result.get('expert', 'n/a')}")
    print(f"  Skill:      {result.get('skill', 'n/a')}")
    print(f"  Composite:  {result['composite_score']}/10")
    print(f"  Status:     {result['status']}")
    print(f"  {result['gate_message']}")
    print("-" * 60)

    # Sub-scores
    print(f"  Intent Alignment:       {result['intent_alignment']}/10")
    print(f"  Expert Standard:        {result['expert_standard']}/10")
    print(f"  Adversarial Resilience: {result['adversarial_resilience']}/10")

    # Regression
    reg = result.get("regression_check", {})
    if "message" in reg:
        print(f"\n  Regression: {reg['message']}")

    # Notion
    notion = result.get("notion_result", {})
    if notion.get("success"):
        if notion.get("skipped"):
            print(f"\n  Notion:     Skipped (test mode)")
        else:
            print(f"\n  Notion:     ✅ Logged → {notion.get('url', 'done')}")
    else:
        print(f"\n  Notion:     ❌ {notion.get('error', 'failed')}")

    # Protocols
    protocols = result.get("protocols_activated", [])
    print(f"\n  Protocols activated: {len(protocols)}")
    for p in protocols:
        print(f"    • {p}")

    # Session state
    if result.get("session_state_written"):
        print(f"  Session state: ✅ Written")
    else:
        print(f"  Session state: ⚠️  Not written")

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Chain Runner CLI — Enforce The Chain Steps 6-7")
    sub = parser.add_subparsers(dest="command")

    # finalize
    fin = sub.add_parser("finalize", help="Run Steps 6-7 (Quality Gate + Log)")
    fin.add_argument("output", help="Output description")
    fin.add_argument("--expert", default="", help="Expert agent name")
    fin.add_argument("--skill", default="", help="Skill directory name")
    fin.add_argument("--workflow", default="", help="Workflow name")
    fin.add_argument("--type", default="System", help="Task type")
    fin.add_argument("--intent", type=float, required=True, help="Intent alignment score (1-10)")
    fin.add_argument("--expert-score", type=float, required=True, help="Expert standard score (1-10)")
    fin.add_argument("--adversarial", type=float, required=True, help="Adversarial resilience score (1-10)")
    fin.add_argument("--notes", default="", help="Freeform notes")
    fin.add_argument("--rating", type=float, help="User rating (1-10)")
    fin.add_argument("--tag", default="", help="Experiment tag")
    fin.add_argument("--skip-notion", action="store_true", help="Skip Notion logging (test mode)")
    fin.add_argument("--trace", action="store_true", help="Write JSON trace to evolution_store/traces/")

    args = parser.parse_args()

    if args.command == "finalize":
        result = finalize(
            output_description=args.output,
            expert=args.expert,
            skill=args.skill,
            workflow=args.workflow,
            task_type=args.type,
            intent_alignment=args.intent,
            expert_standard=args.expert_score,
            adversarial_resilience=args.adversarial,
            notes=args.notes,
            user_rating=args.rating,
            experiment_tag=args.tag,
            skip_notion=args.skip_notion,
            write_trace=args.trace,
        )
        print_result(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
