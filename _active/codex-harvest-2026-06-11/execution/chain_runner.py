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
from prose_classifier import classify_prose, quick_check
from revenue_tracker import get_pipeline as get_revenue_pipeline

# Routing enforcer (Fix 2 / 2026-04-24) — post-finalize observability for
# workflow choices so we can detect drift from CLAUDE.md mandatory bindings.
try:
    from routing_enforcer import check_routing as _check_routing
    from routing_enforcer import log_decision as _log_routing_decision
    _HAS_ROUTING_ENFORCER = True
except ImportError:
    _HAS_ROUTING_ENFORCER = False

# Evolution trace directory (v2)
TRACE_DIR = Path(__file__).parent.parent / "evolution_store" / "v2_traces"

# Import v2 evolution tracer for auto-logging
try:
    from evolution_tracer import log_trace as evo_log_trace
    _HAS_EVO_TRACER = True
except ImportError:
    _HAS_EVO_TRACER = False

# Import sovereign memory store for auto-hooks
try:
    from memory_store import store_memory_silent
    _HAS_MEMORY_STORE = True
except ImportError:
    _HAS_MEMORY_STORE = False


# Quality Gate thresholds (from directives/quality_gate.md)
COMPOSITE_PASS_THRESHOLD = 7
SINGLE_DIMENSION_MIN = 6

# Protocols to activate on finalize
QUALITY_GATE_PATH = "directives/quality_gate.md"
FEEDBACK_RATCHET_PATH = "directives/feedback-ratchet.md"
SESSION_STATE_PATH = "directives/session-state-protocol.md"


def _classify_domain_from_skill(skill_name: str) -> str:
    """Infer knowledge domain from a skill directory name."""
    skill_lower = skill_name.lower()
    domain_hints = {
        'linkedin': 'content', 'content': 'content', 'social': 'content',
        'copy': 'copywriting', 'vsl': 'copywriting', 'email': 'copywriting',
        'seo': 'seo', 'gotch': 'seo',
        'brand': 'brand', 'naming': 'brand', 'storybrand': 'brand',
        'screen': 'screenwriting', 'dialogue': 'screenwriting', 'connelly': 'screenwriting',
        'strategy': 'strategy', 'positioning': 'strategy', 'audit': 'strategy',
        'research': 'research', 'consumer': 'research', 'icp': 'research',
        'sales': 'sales', 'objection': 'sales', 'persuasion': 'sales',
    }
    for hint, domain in domain_hints.items():
        if hint in skill_lower:
            return domain
    return 'general'


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
    # Step-level telemetry (Kimi K2.6-inspired; see directives/feedback-ratchet.md)
    tool_calls: Optional[int] = None,
    file_reads: Optional[int] = None,
    sub_agents_spawned: Optional[int] = None,
    session_duration_seconds: Optional[float] = None,
    critical_path_depth: Optional[int] = None,
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
        "task_type": task_type,
        "timestamp": datetime.now().isoformat(),
    }

    # ── Telemetry (optional; Kimi K2.6-inspired step counting) ───
    telemetry = {
        k: v for k, v in {
            "tool_calls": tool_calls,
            "file_reads": file_reads,
            "sub_agents_spawned": sub_agents_spawned,
            "session_duration_seconds": session_duration_seconds,
            "critical_path_depth": critical_path_depth,
        }.items() if v is not None
    }
    if telemetry:
        result["telemetry"] = telemetry

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

    # ── Step 2.5: Prose classifier check (advisory) ───────────────
    prose_result = None
    if output_description and len(output_description) > 100:
        try:
            prose_result = classify_prose(output_description)
            result["prose_check"] = {
                "verdict": prose_result["verdict"],
                "ai_score": prose_result["ai_score"],
                "signal_count": prose_result["signal_count"],
            }
            if prose_result["verdict"] == "FLAGGED" and expert_standard and expert_standard > 6:
                result["prose_warning"] = (
                    f"Prose classifier FLAGGED (AI score {prose_result['ai_score']}/10). "
                    f"Expert Standard may be inflated at {expert_standard}. "
                    f"Consider cap at 6 per quality_gate.md."
                )
        except Exception:
            pass  # Prose check is advisory, never blocks

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

    # ── Inflation guardrail (Fix 1 / 2026-04-24) ──────────────────
    # Calibration found 94-99% of recent traces scored 8+ across all dimensions.
    # If all 3 dims are ≥9, surface a reminder to spot-check against rubric anchors.
    # Inflation in scoring corrupts every downstream evolution decision.
    if intent_alignment >= 9 and expert_standard >= 9 and adversarial_resilience >= 9:
        result["inflation_warning"] = (
            "All 3 dimensions scored ≥9. Verify each matches the Anchor 9 worked example in "
            "evolution_store/ground_truth/rubric_v1.md. If you can't name the anchor, lower the score. "
            "Reference: python3 execution/eval_harness.py anchor --dimension <dim> --score 9"
        )

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
    # Telemetry is appended to notes so it persists in Notion without
    # requiring a schema change to the Performance Log database.
    notion_notes = notes
    if telemetry:
        telemetry_str = " | ".join(f"{k}={v}" for k, v in telemetry.items())
        notion_notes = f"{notes} | telemetry: {telemetry_str}" if notes else f"telemetry: {telemetry_str}"

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
                notes=notion_notes,
                experiment_tag=experiment_tag,
            )
            sync_status = notion_result.get("sync_status", "remote-synced")
            result["notion_result"] = {
                "success": sync_status == "remote-synced",
                "sync_status": sync_status,
                "url": notion_result.get("url", "logged"),
                "local_id": notion_result.get("local_id", ""),
                "local_path": notion_result.get("local_path", ""),
            }
            if notion_result.get("notion_error"):
                result["notion_result"]["error"] = notion_result["notion_error"]
        except Exception as e:
            result["notion_result"] = {"success": False, "error": str(e)}
    else:
        result["notion_result"] = {"success": True, "sync_status": "skipped", "skipped": True}

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

    # ── Step 8: Write v2 evolution trace (ALWAYS, not optional) ──
    try:
        if _HAS_EVO_TRACER:
            # V2 tracer: auto-populates search set on failures
            evo_log_trace(
                component=skill or expert or task_type,
                operation="chain_finalize",
                expert=expert,
                workflow=workflow,
                quality_score=composite,
                intent=intent_alignment,
                expert_score=expert_standard,
                adversarial=adversarial_resilience,
                notes=notes,
                context={
                    "output": output_description[:200],
                    "task_type": task_type,
                    "experiment_tag": experiment_tag,
                    "regression": result.get("regression_check", {}),
                    "telemetry": telemetry or None,
                },
            )
            result["v2_trace"] = True
        else:
            # Fallback: legacy trace writing
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
                "telemetry": telemetry or None,
            }
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            trace_file = TRACE_DIR / f"trace_{ts}_{skill or expert or 'unknown'}.json"
            with open(trace_file, "w") as f:
                json.dump(trace, f, indent=2)
            result["trace_file"] = str(trace_file)
    except Exception as e:
        result["v2_trace"] = False
        result["trace_error"] = str(e)

    # ── Step 9: Auto-store sovereign memory ──────────────────────
    if _HAS_MEMORY_STORE:
        try:
            mem_meta = {
                "source": "chain_runner",
                "expert": expert,
                "skill": skill,
                "workflow": workflow,
                "task_type": task_type,
                "composite": composite,
                "status": status,
                "experiment_tag": experiment_tag,
            }

            # Always store an episodic/milestone memory for the output
            mid = store_memory_silent(
                tier="episodic",
                category="milestone",
                content=f"[{status}] {task_type}: {output_description[:200]} (composite: {composite}/10, expert: {expert or 'n/a'}, skill: {skill or 'n/a'})",
                metadata=mem_meta,
            )
            result["memory_id"] = mid

            # On FAIL: also store an error memory capturing failure dimensions
            if not passed:
                fail_content = f"QUALITY GATE FAIL: {output_description[:150]}. Failed dimensions: {', '.join(failed_dimensions)}. Composite: {composite}/10."
                if notes:
                    fail_content += f" Notes: {notes[:100]}"
                store_memory_silent(
                    tier="episodic",
                    category="error",
                    content=fail_content,
                    metadata={**mem_meta, "failed_dimensions": failed_dimensions},
                )
                result["memory_error_stored"] = True

            # On regression: store a semantic/error_pattern memory
            reg = result.get("regression_check", {})
            if reg.get("regression_detected"):
                reg_content = f"REGRESSION: {skill or expert} dropped from baseline {reg.get('baseline', '?')} to {composite}/10. {reg.get('message', '')}"
                store_memory_silent(
                    tier="semantic",
                    category="pattern",
                    content=reg_content,
                    metadata={**mem_meta, "regression": reg},
                )
                result["memory_regression_stored"] = True

        except Exception as e:
            result["memory_store_error"] = str(e)

    # ── Step 10: Wiki cascade (Karpathy compounding loop) ───────
    # High-quality outputs trigger wiki updates so future sessions
    # start with enriched knowledge. Log all finalize events;
    # only regenerate briefing/index for quality >= 8.
    try:
        try:
            from knowledge_compiler import log_activity, update_index, generate_briefing as gen_briefing
        except ImportError:
            from execution.knowledge_compiler import log_activity, update_index, generate_briefing as gen_briefing
        domain = _classify_domain_from_skill(skill) if skill else task_type.lower()
        log_activity(
            action='finalize',
            title=output_description[:100],
            domain=domain,
            expert=expert or '',
            notes=f"composite:{composite} status:{status}",
        )
        if composite >= 8:
            gen_briefing()
        result["wiki_cascade"] = True
    except Exception as e:
        result["wiki_cascade"] = False
        result["wiki_cascade_error"] = str(e)

    # ── Step 11: Knowledge Vault sync (Notion activation) ───────
    # High-quality outputs (>= 7) auto-create a Knowledge Vault entry
    # in Notion so the knowledge base is discoverable from Notion search/AI.
    # Files stay local — Notion entries are pointers + metadata.
    if composite >= 7 and not skip_notion:
        try:
            try:
                from notion_api import NotionAPI
            except ImportError:
                from execution.notion_api import NotionAPI
            notion = NotionAPI()
            domain = _classify_domain_from_skill(skill) if skill else task_type.lower()

            # Map task_type to Knowledge Vault entry type
            type_map = {
                'Extraction': 'MES 3.0 Extraction',
                'Research': 'Research Brief',
                'Strategy': 'Framework',
                'Content': 'Pattern Library',
                'Client Work': 'Case Study',
            }
            entry_type = type_map.get(task_type, 'Research Brief')

            # Determine tags based on quality
            tags = ['Actionable']
            if composite >= 9:
                tags.append('Crown Jewel')

            vault_result = notion.create_knowledge_vault_entry(
                name=output_description[:100],
                source=f"chain_runner finalize ({workflow or 'direct'})",
                expert=expert or '',
                domain=domain,
                entry_type=entry_type,
                key_patterns=notes[:200] if notes else '',
                genius_score=min(5, max(2, int(composite / 2))),
                antigravity_skill=skill or '',
                tags=tags,
            )
            result["knowledge_vault_sync"] = {"success": True, "url": vault_result}
        except Exception as e:
            result["knowledge_vault_sync"] = {"success": False, "error": str(e)}

    # ── Step 11.5: Post-finalize routing trace (Fix 2 / 2026-04-24) ──
    # Records every workflow that actually completed a chain so we can
    # later detect drift between intended routing (routing_decisions.jsonl
    # source=cli) and actual usage (source=post_finalize). Non-fatal.
    if _HAS_ROUTING_ENFORCER and workflow:
        try:
            validation = _check_routing(output_description, workflow)
            _log_routing_decision(
                request=output_description,
                chosen_workflow=workflow,
                validation=validation,
                source="post_finalize",
            )
            if not validation["valid"]:
                # Surface as a warning in the result — don't block, just flag
                result["routing_violation"] = {
                    "binding": validation["binding_matched"],
                    "matched_signal": validation["matched_signal"],
                    "mandatory": validation["mandatory_workflow"],
                    "chosen": workflow,
                    "reason": validation["violation_reason"],
                }
        except Exception:
            pass

    # ── Step 12: Revenue Tracker auto-link (Upgrade 7) ──────────
    # Passed deliverables in revenue-relevant task_types get a pending
    # outcome stub registered so `revenue_tracker pipeline` surfaces
    # them without manual follow-up. User later updates with actual
    # revenue via `python execution/revenue_tracker.py log ...`.
    # Non-fatal: any error is swallowed so revenue tracking never
    # breaks the quality gate.
    if passed:
        try:
            try:
                from revenue_tracker import auto_register_outcome
            except ImportError:
                from execution.revenue_tracker import auto_register_outcome
            notion_page_id = ""
            if isinstance(result.get("notion_result"), dict):
                notion_page_id = result["notion_result"].get("page_id", "")
            reg = auto_register_outcome(
                deliverable=output_description[:200],
                expert=expert,
                skill=skill,
                workflow=workflow,
                task_type=task_type,
                composite=composite,
                notion_page_id=notion_page_id,
                experiment_tag=experiment_tag,
            )
            result["revenue_autolink"] = reg
        except Exception as e:
            result["revenue_autolink"] = {"skipped": True, "error": str(e)}

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
    elif notion.get("sync_status") == "sync-failed":
        print(f"\n  Notion:     Local only → {notion.get('url', 'local log')}")
        print(f"              Sync failed: {notion.get('error', 'network or API unavailable')}")
    else:
        print(f"\n  Notion:     ❌ {notion.get('error', 'failed')}")

    # Protocols
    protocols = result.get("protocols_activated", [])
    print(f"\n  Protocols activated: {len(protocols)}")
    for p in protocols:
        print(f"    • {p}")

    # Prose check
    prose = result.get("prose_check")
    if prose:
        verdict = prose.get("verdict", "N/A")
        ai_score = prose.get("ai_score", 0)
        if verdict == "FLAGGED":
            print(f"\n  Prose:      ⚠️  FLAGGED (AI score {ai_score}/10) — Expert Standard may be inflated")
        elif verdict == "WARNING":
            print(f"\n  Prose:      ⚡ WARNING (AI score {ai_score}/10) — review before delivery")

    # Prose warning (if Expert Standard seems inflated)
    if result.get("prose_warning"):
        print(f"  ⚠️  {result['prose_warning']}")

    # Session state
    if result.get("session_state_written"):
        print(f"  Session state: ✅ Written")
    else:
        print(f"  Session state: ⚠️  Not written")

    # Inflation warning (rubric calibration from Fix 1)
    iw = result.get("inflation_warning")
    if iw:
        print(f"\n  ⚠️  INFLATION GUARDRAIL: {iw[:300]}")

    # Routing violation (post-hoc detection from routing_enforcer)
    rv = result.get("routing_violation")
    if rv:
        print(f"\n  ⚠️  ROUTING VIOLATION DETECTED")
        print(f"     Signal:    {rv['matched_signal']!r} → binding {rv['binding']}")
        print(f"     Mandatory: {rv['mandatory']}")
        print(f"     Chosen:    {rv['chosen']}")
        print(f"     {rv['reason'][:200]}{'...' if len(rv['reason']) > 200 else ''}")

    # Revenue tracking reminder (for client/content deliverables)
    task_type = result.get("task_type", "")
    if task_type in ("Client Work", "Content", "Creative", "Strategy"):
        print(f"\n  💰 Revenue tracking: Log outcome when results come in →")
        print(f"     python execution/revenue_tracker.py log \"{result['output'][:50]}...\" --revenue <$> --outcome \"<result>\"")

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
    fin.add_argument("--tool-calls", type=int, default=None, help="Telemetry: number of tool calls this session")
    fin.add_argument("--file-reads", type=int, default=None, help="Telemetry: number of file reads this session")
    fin.add_argument("--sub-agents", type=int, default=None, help="Telemetry: number of sub-agents spawned this session")
    fin.add_argument("--duration", type=float, default=None, help="Telemetry: session duration in seconds")
    fin.add_argument("--critical-path", type=int, default=None, help="Telemetry: critical-path depth (from mission-decomposer)")

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
            tool_calls=args.tool_calls,
            file_reads=args.file_reads,
            sub_agents_spawned=args.sub_agents,
            session_duration_seconds=args.duration,
            critical_path_depth=args.critical_path,
        )
        print_result(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
