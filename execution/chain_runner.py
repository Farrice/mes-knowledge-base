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
import re
import sys
import json
import argparse
from datetime import date, datetime
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple

# Ensure execution/ is on the path for sibling imports
sys.path.insert(0, str(Path(__file__).parent))

from log_performance import log_output, check_regression, get_baseline
from protocol_tracker import activate_protocol
from checkpoint_manager import save_session_state
from prose_classifier import should_cap_expert_standard
from taste_signature import apply as apply_taste_signature
from excellence_predictor import detect_grade_inflation
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


# Grounding-relevance set per directives/recall-grounding-protocol.md trigger conditions.
# Used by Step 11.7 (Fix 5b / 2026-05-03) to auto-log grounding events so observability
# survives the AI forgetting manual recall_logger CLI invocation.
_GROUNDING_RELEVANT_DOMAINS = {
    'content', 'copywriting', 'brand', 'voice', 'storytelling',
    'positioning', 'strategy', 'sales', 'persuasion', 'creative',
    'screenwriting', 'research',
}
_GROUNDING_RELEVANT_TASK_TYPES = {
    'Content', 'Strategy', 'Creative', 'Client Work', 'Copy',
}


def _auto_log_grounding(skill: str, expert: str, task_type: str, notes: str) -> Dict[str, Any]:
    """Auto-log a Recall grounding decision so observability is deterministic.

    Why this exists: the original recall_logger design required Claude to manually
    invoke `python3 execution/recall_logger.py log ...` after every grounding
    decision. The May 2026 audit found that approach went silent within 24 hours
    of shipping (12.8% fire rate over 14 days; only 1 of 10 expected domains).
    This backstop ensures every chain finalize produces a baseline log entry.

    Inference rules:
    - If task_type or skill domain is grounding-relevant AND notes contain an
      explicit fire signal → status=fired (source: explicit).
    - If grounding-relevant but no explicit signal → status=skipped, reason=not_observed
      (the gap between expected and observed is now visible).
    - If not grounding-relevant → status=skipped, reason=non_grounding_domain.

    This does NOT replace explicit logging by the AI when Recall MCP is actually
    called — that signal (cards returned, signal level) is still richer. It just
    guarantees a floor of observability when the AI forgets.
    """
    try:
        from recall_logger import log_decision
    except ImportError:
        try:
            from execution.recall_logger import log_decision
        except ImportError:
            return {"logged": False, "reason": "import_failed"}

    domain = _classify_domain_from_skill(skill) if skill else (task_type or "system").lower()
    is_relevant = (
        task_type in _GROUNDING_RELEVANT_TASK_TYPES
        or domain in _GROUNDING_RELEVANT_DOMAINS
    )

    notes_lower = (notes or '').lower()
    explicit_fire = (
        'recall grounding:' in notes_lower
        or 'recall fired' in notes_lower
        or 'cards returned' in notes_lower
        or 'grounded with' in notes_lower
    )

    if not is_relevant:
        log_decision(
            status="skipped",
            domain=domain,
            expert=expert,
            reason="non_grounding_domain",
            note="auto-logged from chain_runner finalize",
        )
        return {"status": "skipped", "reason": "non_grounding_domain", "source": "auto_inferred"}

    if explicit_fire:
        log_decision(
            status="fired",
            domain=domain,
            expert=expert,
            note="auto-logged from chain_runner finalize; explicit signal in notes",
        )
        return {"status": "fired", "source": "explicit_in_notes"}

    log_decision(
        status="skipped",
        domain=domain,
        expert=expert,
        reason="not_observed",
        note="auto-logged from chain_runner finalize; grounding-relevant domain but no explicit fire signal in notes",
    )
    return {"status": "skipped", "reason": "not_observed", "source": "auto_inferred"}


# Sub-agent qualifying workflows — system-tier multi-expert/multi-phase orchestrations
# where running without sub-agent context isolation is likely a miss per
# directives/sub_agent_protocol.md auto-spawn triggers. Source: 2026-05-12 integration
# brief Move 2 (Phase D activation). Update this set alongside the brief's
# routing_enforcer bindings — code is source of truth.
_SUB_AGENT_QUALIFYING_WORKFLOWS = {
    'parallax', 'extract-forge', 'writers-room', 'campaign', 'jcc-deploy',
    'swarm', 'parallel-swarm', 'swarm-research', 'research-swarm',
    'big-project', 'content-bundle', 'proof-pipeline', 'build-bos',
    'roundtable', 'council', 'parallel-extract', 'parallel-content',
    'jcc-strike', 'jcc-campaign', 'jcc-solo', 'jcc-refine', 'jcc-upgrade', 'jcc-aar',
    'brief', 'generate-brief', 'mini-brief', 'deep-research',
}


def _auto_log_sub_agent_miss(
    workflow: str,
    skill: str,
    expert: str,
    task_type: str,
    sub_agents_spawned: Optional[int],
) -> Dict[str, Any]:
    """Detect when a qualifying multi-expert workflow ran without sub-agent spawn.

    Why this exists: directives/sub_agent_protocol.md had 0 recorded activations since
    creation (2026-02-17 → 2026-04-24 audit). The protocol relies on the AI remembering
    to spawn sub-agents at qualifying triggers — exactly the AI-memory-dependent
    observability anti-pattern banned by feedback_ai-memory-dependent-observability.md
    (2026-05-03). This function makes the miss visible WITHOUT changing runtime
    behavior. After 30 days of misses data, the 2026-05-12 integration brief Move 2
    proposes escalating to gate-blocking when qualifying tasks ran without sub-agents.

    Detection: workflow name in _SUB_AGENT_QUALIFYING_WORKFLOWS AND sub_agents_spawned
    is None or 0 → MISS logged. False positives are tolerable here — this is
    observation only, never blocks finalize, never fails the quality gate.

    Source: _active/system-integration/2026-05-12-agentic-os-elevation-brief.md Move 2.
    """
    workflow_normalized = (workflow or "").lower().strip()
    qualifies = workflow_normalized in _SUB_AGENT_QUALIFYING_WORKFLOWS
    spawned_count = sub_agents_spawned if sub_agents_spawned is not None else 0
    is_miss = qualifies and spawned_count == 0

    record = {
        "timestamp": datetime.now().isoformat(),
        "workflow": workflow,
        "skill": skill,
        "expert": expert,
        "task_type": task_type,
        "qualifies": qualifies,
        "sub_agents_spawned": spawned_count,
        "miss": is_miss,
    }

    if is_miss:
        log_path = Path(__file__).parent.parent / "evolution_store" / "sub_agent_misses.jsonl"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(log_path, "a") as f:
                f.write(json.dumps(record) + "\n")
            record["logged"] = True
        except Exception as e:
            record["logged"] = False
            record["log_error"] = str(e)

    return record


# ─────────────────────────────────────────────────────────
# Excellence Lift — runtime cap enforcement (Wave 1 / 2026-05-21)
# ─────────────────────────────────────────────────────────
# Background: directives/quality_gate.md specifies three caps (AI Prose ≤6,
# Copy Calibration ≤6, Factual Veto <6) but pre-Wave-1 the gate only logged
# advisory warnings — the 2026-04-24 audit found 94-99% of finalize scores
# were 8+ as a result. _enforce_caps() converts those advisory rules into
# deterministic score mutations so they cannot be ignored.
#
# Result-key contract (what _enforce_caps returns is folded into finalize's
# result dict — see Wave 1 wiring):
#   intent_alignment        — possibly capped at 6.0 (Copy Calibration)
#   expert_standard         — possibly capped at 6.0 (AI Prose)
#   adversarial_resilience  — unchanged by caps (no documented hard rule)
#   factual_grounding       — passthrough; veto fires separately
#   caps_applied[]          — audit trail (rule, from, to, reason)
#   blocked                 — True iff Factual Veto fires
#   block_reason            — human-readable veto reason
#   prose_verdict           — CLEAN | WARNING | FLAGGED | NOT_RUN
#   prose_details           — full classify_prose dict if run

# Heuristic patterns for the Copy Calibration cap. Concrete-result language
# the user values: numbers + outcome verbs OR explicit second-person promises
# paired with a specific deliverable. Abstract benefit language ("visibility",
# "growth", "transformation") without a named result fails the check.
_COPY_CONCRETE_NUMBER_PATTERN = re.compile(
    r"\b\d{1,4}(?:[.,]\d+)?\s*(?:%|x|×|hours?|days?|weeks?|months?|years?|"
    r"customers?|clients?|leads?|posts?|followers?|subscribers?|sales?|"
    r"dollars?|usd|deals?|booked|opens?|replies|words?|pieces?|episodes?|listings?)\b",
    re.IGNORECASE,
)
_COPY_RESULT_VERBS = re.compile(
    r"\b(?:get(?:s)?|book(?:s|ed)?|land(?:s|ed)?|close(?:s|d)?|win(?:s)?|"
    r"convert(?:s|ed)?|generate(?:s|d)?|earn(?:s|ed)?|build(?:s|t)?|ship(?:s|ped)?|"
    r"finish(?:es|ed)?|publish(?:es|ed)?|sign(?:s|ed)?)\b",
    re.IGNORECASE,
)
_COPY_VAGUE_BENEFITS = re.compile(
    r"\b(?:visibility|growth|transformation|alignment|clarity|"
    r"empowerment|elevation|optimization|breakthrough|impact)\b",
    re.IGNORECASE,
)
_COPY_TASK_TYPES = {"Content", "Copy", "Creative"}


def _check_concrete_result(text: str) -> Tuple[bool, str]:
    """Heuristic: does the text name a concrete result (Copy Calibration rule)?

    Returns (passes, reason). passes=True if at least one concrete-result
    signal is found in the last 30% of the text (where the result-promise
    typically lives), OR a result-verb appears alongside a number anywhere.

    Tolerates false-positives (favors letting copy through) — the cap is
    meant to catch egregiously abstract benefit-only copy, not edge cases.
    """
    if not text or len(text) < 100:
        return True, "text_too_short_to_judge"

    tail_start = max(0, int(len(text) * 0.7))
    tail = text[tail_start:]

    has_number_in_tail = bool(_COPY_CONCRETE_NUMBER_PATTERN.search(tail))
    has_result_verb_in_tail = bool(_COPY_RESULT_VERBS.search(tail))
    has_number_anywhere = bool(_COPY_CONCRETE_NUMBER_PATTERN.search(text))
    has_result_verb_anywhere = bool(_COPY_RESULT_VERBS.search(text))
    vague_count = len(_COPY_VAGUE_BENEFITS.findall(text))

    # Strong signal: number + result-verb in tail → concrete result named.
    if has_number_in_tail and has_result_verb_in_tail:
        return True, "concrete_result_in_close"
    # Decent signal: number + result-verb anywhere.
    if has_number_anywhere and has_result_verb_anywhere:
        return True, "concrete_result_in_body"
    # Negative signal: heavy vague-benefit language and no concretes.
    if vague_count >= 3 and not has_number_anywhere and not has_result_verb_anywhere:
        return False, f"vague_benefits_only ({vague_count} abstract words, 0 concrete results)"
    # Weak signal: at least one concrete element somewhere.
    if has_number_anywhere or has_result_verb_anywhere:
        return True, "minimum_concrete_present"
    # Last resort: no concretes, no heavy vagueness → judgment call, default pass.
    return True, "no_strong_signal_either_way"


def _enforce_caps(
    raw_scores: Dict[str, float],
    output_text: str,
    task_type: str,
    factual_grounding: Optional[float],
) -> Dict[str, Any]:
    """Apply runtime caps mandated by directives/quality_gate.md.

    Three rules, in order:
        1. AI Prose Cap — if prose_classifier returns FLAGGED, cap
           expert_standard at 6.0.
        2. Copy Calibration — for Content/Copy/Creative tasks with >100
           chars, cap intent_alignment at 6.0 if no concrete result is named.
        3. Factual Veto — if factual_grounding < 6, BLOCK delivery
           (composite still computed; status=BLOCKED, passed=False).

    Each cap that fires writes to caps_applied[] audit trail so
    print_result() can show the user WHY the composite dropped.
    """
    enforced = dict(raw_scores)
    caps_applied: List[Dict[str, Any]] = []
    blocked = False
    block_reason = ""
    prose_verdict = "NOT_RUN"
    prose_details: Dict[str, Any] = {}

    # ── Cap 1: AI Prose ──────────────────────────────────────
    if output_text and len(output_text) > 100:
        try:
            cap_required, details = should_cap_expert_standard(output_text)
            prose_details = details
            prose_verdict = details.get("verdict", "NOT_RUN")
            current_expert = enforced.get("expert_standard")
            if cap_required and current_expert is not None and current_expert > 6:
                caps_applied.append({
                    "rule": "ai_prose_cap",
                    "dimension": "expert_standard",
                    "from": current_expert,
                    "to": 6.0,
                    "reason": (
                        f"prose_classifier FLAGGED "
                        f"(ai_score {details.get('ai_score', '?')}/10, "
                        f"{details.get('signal_count', '?')} signals)"
                    ),
                })
                enforced["expert_standard"] = 6.0
        except Exception as e:
            prose_verdict = "ERROR"
            prose_details = {"error": str(e)}

    # ── Cap 2: Copy Calibration ──────────────────────────────
    if task_type in _COPY_TASK_TYPES and output_text and len(output_text) > 100:
        passes, reason = _check_concrete_result(output_text)
        current_intent = enforced.get("intent_alignment")
        if not passes and current_intent is not None and current_intent > 6:
            caps_applied.append({
                "rule": "copy_calibration_cap",
                "dimension": "intent_alignment",
                "from": current_intent,
                "to": 6.0,
                "reason": f"copy names no concrete result ({reason})",
            })
            enforced["intent_alignment"] = 6.0

    # ── Cap 3: Factual Veto ──────────────────────────────────
    if factual_grounding is not None and factual_grounding < 6:
        blocked = True
        block_reason = (
            f"Factual Grounding scored {factual_grounding} (< 6 hard floor). "
            f"Delivery BLOCKED per quality_gate.md — verify claims before re-finalizing."
        )
        caps_applied.append({
            "rule": "factual_veto",
            "dimension": "factual_grounding",
            "from": factual_grounding,
            "to": factual_grounding,  # score unchanged; status changes
            "reason": block_reason,
        })

    return {
        "intent_alignment": enforced.get("intent_alignment"),
        "expert_standard": enforced.get("expert_standard"),
        "adversarial_resilience": enforced.get("adversarial_resilience"),
        "factual_grounding": factual_grounding,
        "caps_applied": caps_applied,
        "blocked": blocked,
        "block_reason": block_reason,
        "prose_verdict": prose_verdict,
        "prose_details": prose_details,
    }


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
    # Supercomputer anchor-memory integration (added 2026-05-20)
    project: str = "",
    anchor_type: str = "",
    anchor_path: str = "",
    anchor_ref_for: str = "",
    # Excellence Lift Wave 1 (added 2026-05-21)
    factual_grounding: Optional[float] = None,
    # Excellence Lift Wave 2 (added 2026-05-21)
    anchor_named: bool = False,
    # Autopilot Wave 5 stabilization (added 2026-05-23): original user intent
    # used for the post-hoc routing check at line ~918. When None, the call
    # falls back to checking output_description (legacy behavior). Autopilot's
    # Phase 4 template MUST pass the original user request here to prevent the
    # autopilot_orchestration binding from firing on every sub-workflow.
    source_request: Optional[str] = None,
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

    # ── Step 2: Calculate raw composite (pre-enforcement) ────────
    raw_composite = round((intent_alignment + expert_standard + adversarial_resilience) / 3, 1)
    result["raw_composite_score"] = raw_composite
    result["raw_intent_alignment"] = intent_alignment
    result["raw_expert_standard"] = expert_standard
    result["raw_adversarial_resilience"] = adversarial_resilience

    # ── Step 2.5: Apply runtime caps (Excellence Lift Wave 1) ────
    # _enforce_caps converts the three quality_gate.md hard rules from
    # advisory text into deterministic score mutations. See _enforce_caps
    # docstring above for rule details.
    enforced = _enforce_caps(
        raw_scores={
            "intent_alignment": intent_alignment,
            "expert_standard": expert_standard,
            "adversarial_resilience": adversarial_resilience,
        },
        output_text=output_description,
        task_type=task_type,
        factual_grounding=factual_grounding,
    )

    # ── Step 2.7: Apply bimodal taste signature (Wave 2) ──────────
    # taste_signature.apply runs ON TOP of the Wave 1 caps. It encodes
    # Farrice's bimodal taste signature (rubric_v1.md Bimodal Taste section)
    # — harsh on failures, 8-must-be-earned, anti-cluster detection.
    adjusted = apply_taste_signature(
        scores={
            "intent_alignment": enforced["intent_alignment"],
            "expert_standard": enforced["expert_standard"],
            "adversarial_resilience": enforced["adversarial_resilience"],
        },
        anchor_named=anchor_named,
        prose_verdict=enforced["prose_verdict"],
        factual_grounding=factual_grounding,
    )

    intent_alignment = adjusted.intent_alignment
    expert_standard = adjusted.expert_standard
    adversarial_resilience = adjusted.adversarial_resilience
    composite = adjusted.composite

    result["composite_score"] = composite
    result["intent_alignment"] = intent_alignment
    result["expert_standard"] = expert_standard
    result["adversarial_resilience"] = adversarial_resilience
    result["factual_grounding"] = factual_grounding
    result["taste_verdict"] = adjusted.taste_verdict
    result["anchor_named"] = anchor_named
    # Audit trail: Wave 1 caps + Wave 2 taste adjustments combined
    result["caps_applied"] = enforced["caps_applied"] + adjusted.adjustments
    result["prose_check"] = {
        "verdict": enforced["prose_verdict"],
        "ai_score": enforced["prose_details"].get("ai_score"),
        "signal_count": enforced["prose_details"].get("signal_count"),
    }

    # ── Step 3: Quality Gate pass/fail ───────────────────────────
    # Factual veto (from _enforce_caps) overrides composite arithmetic.
    failed_dimensions = []
    if intent_alignment < SINGLE_DIMENSION_MIN:
        failed_dimensions.append(f"intent_alignment ({intent_alignment})")
    if expert_standard < SINGLE_DIMENSION_MIN:
        failed_dimensions.append(f"expert_standard ({expert_standard})")
    if adversarial_resilience < SINGLE_DIMENSION_MIN:
        failed_dimensions.append(f"adversarial_resilience ({adversarial_resilience})")

    # Wave 2: bimodal taste verdict is the source of truth for pass/fail.
    # Wave 1 factual veto (blocked) overrides everything.
    if enforced["blocked"]:
        passed = False
        status = "BLOCKED — Factual Veto"
        result["block_reason"] = enforced["block_reason"]
    elif adjusted.taste_verdict == "PASS":
        passed = True
        status = "Keep"
    elif adjusted.taste_verdict == "MARGINAL":
        passed = False
        status = "Needs Improvement"
    else:  # FAIL
        passed = False
        status = "Needs Improvement"

    result["passed"] = passed
    result["failed_dimensions"] = failed_dimensions
    result["status"] = status

    if enforced["blocked"]:
        result["gate_message"] = f"🚫  QUALITY GATE BLOCKED — {enforced['block_reason']}"
    elif adjusted.taste_verdict == "FAIL":
        if failed_dimensions:
            result["gate_message"] = f"⚠️  QUALITY GATE FAIL — Composite: {composite}, Failed dimensions: {', '.join(failed_dimensions)}. Retry weakest section."
        else:
            result["gate_message"] = f"⚠️  QUALITY GATE FAIL — Composite: {composite} (bimodal verdict FAIL). Retry weakest dimension."
    elif adjusted.taste_verdict == "MARGINAL":
        result["gate_message"] = f"⚠️  QUALITY GATE MARGINAL — Composite: {composite} (bimodal narrow band 7.0-7.5). Bimodal taste treats marginal as fail — retry or accept with eyes open."
    else:  # PASS
        cap_note = f" (raw {raw_composite}, capped {composite})" if result["caps_applied"] else ""
        result["gate_message"] = f"✅  QUALITY GATE PASS — Composite: {composite}{cap_note}"

    # ── Inflation guardrail (Wave 3 / 2026-05-21) ────────────────
    # Original guardrail (single-call all-9s check) now augmented with
    # rolling-window drift detection via excellence_predictor. The detector
    # operates on the LOGGED trace distribution — if it fires, prior runs
    # collectively show grade inflation, not just this one.
    if intent_alignment >= 9 and expert_standard >= 9 and adversarial_resilience >= 9:
        result["inflation_warning"] = (
            "All 3 dimensions scored ≥9 after Wave 1+2 enforcement. Verify each matches "
            "the Anchor 9 worked example in evolution_store/ground_truth/rubric_v1.md. "
            "If you can't name the anchor, lower the score and set anchor_named=False. "
            "Reference: python3 execution/eval_harness.py anchor --dimension <dim> --score 9"
        )
    try:
        drift = detect_grade_inflation(window=10)
        if drift:
            result["calibration_drift_warning"] = drift
    except Exception:
        pass  # detector failures are non-fatal

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

    # ── Step 8.5: Mirror staleness check ─────────────────────────
    # Sprint 3 (2026-05-25): notion_mirror is now BLOCKING.
    # Non-blocking sources (sovereign_db) stay WARN.
    # Auto-fire is the deterministic backstop per the 2026-05-03
    # AI-Memory-Dependent Observability feedback rule.
    # Recall mirror intentionally deferred — see directives/recall-mirror-deferred.md
    try:
        try:
            from memory_ops import check_mirror_freshness
        except ImportError:
            from execution.memory_ops import check_mirror_freshness
        freshness_report = check_mirror_freshness()

        # BLOCKING: notion_mirror stale > 72h (or empty)
        if freshness_report.get("blocking_halt"):
            stale_blocking = freshness_report.get("stale_blocking_sources", [])
            details = [
                f"{name}: {freshness_report['sources'][name].get('status')}"
                f" ({freshness_report['sources'][name].get('age_hours')}h)"
                for name in stale_blocking
            ]
            halt_msg = (
                f"BLOCKING memory mirror stale: {', '.join(details)}. "
                f"Run `python3 execution/mirror_notion.py` to refresh, "
                f"or check the nightly launchd job."
            )
            result["memory_halt"] = halt_msg
            result["status"] = "halted"
            print(f"\n{'🔴 ' * 20}")
            print(f"🔴 {halt_msg}")
            print(f"{'🔴 ' * 20}\n")
            return result

        # WARN: any source past 36h (non-blocking, advisory)
        if freshness_report.get("warn"):
            stale_sources = [
                f"{name} ({info['age_hours']}h)"
                for name, info in freshness_report.get("sources", {}).items()
                if info.get("status") in ("warn", "halt")
            ]
            warn_msg = (
                f"Memory mirror staleness: {', '.join(stale_sources)} "
                f"(WARN threshold 36h; HALT threshold 72h for blocking sources)"
            )
            result["memory_warning"] = warn_msg
            print(f"\n{'⚠️ ' * 20}")
            print(f"⚠️  {warn_msg}")
            print(f"{'⚠️ ' * 20}\n")
    except Exception as e:
        result["memory_warning_error"] = str(e)

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
            # Prefer the original user request when supplied (autopilot threads
            # it via --source-request to prevent the autopilot_orchestration
            # binding from firing on every sub-workflow). Fall back to
            # output_description for legacy callers.
            check_input = source_request or output_description
            validation = _check_routing(check_input, workflow)
            _log_routing_decision(
                request=check_input,
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

    # ── Step 11.7: Recall grounding auto-log (Fix 5b / 2026-05-03) ──
    # The original Fix 5 (recall_logger.py) required manual CLI invocation by
    # the AI after every grounding decision. The May 2026 audit found that
    # approach went silent within 24 hours of shipping. This backstop ensures
    # every chain finalize produces a baseline grounding log entry — automatic,
    # inference-based, never depends on AI memory. Non-fatal: any error is
    # swallowed so grounding observability never breaks the quality gate.
    try:
        grounding_log = _auto_log_grounding(skill, expert, task_type, notes)
        result["grounding_log"] = grounding_log
    except Exception as e:
        result["grounding_log_error"] = str(e)

    # ── Step 11.8: Sub-agent miss detection (Phase D / 2026-05-12) ──
    # Auto-log when a qualifying multi-expert workflow ran without sub-agent spawn.
    # See _auto_log_sub_agent_miss docstring for full rationale. Observation only —
    # never blocks finalize. After 30 days of misses data, the 2026-05-12 brief
    # proposes escalating to gate-blocking when qualifying tasks ran without sub-agents.
    try:
        sub_agent_log = _auto_log_sub_agent_miss(
            workflow=workflow,
            skill=skill,
            expert=expert,
            task_type=task_type,
            sub_agents_spawned=sub_agents_spawned,
        )
        result["sub_agent_log"] = sub_agent_log
    except Exception as e:
        result["sub_agent_log_error"] = str(e)

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

    # ── Supercomputer anchor-memory write (added 2026-05-20) ─────────
    # When a project slug is supplied, log this finalize to the project's
    # state.yaml history and (optionally) register the deliverable as a
    # context anchor for downstream supercomputer phases.
    if project:
        try:
            import subprocess
            root = Path(__file__).resolve().parent.parent
            anchor_script = root / "execution" / "anchor_memory.py"
            project_state = root / "projects" / project / "state.yaml"
            anchor_results: Dict[str, Any] = {"project": project}

            if not project_state.exists():
                anchor_results["skipped"] = True
                anchor_results["reason"] = (
                    f"projects/{project}/state.yaml does not exist. "
                    f"Run `python3 execution/anchor_memory.py init {project}` first."
                )
            else:
                # Always append a history entry for this finalize
                log_cmd = [
                    "python3", str(anchor_script), "log", project,
                    "--phase", f"finalize:{skill or workflow or 'unknown'}",
                    "--action", (
                        f"composite={composite}, status={result.get('status', '?')}, "
                        f"output='{output_description[:120]}'"
                    ),
                ]
                subprocess.run(log_cmd, capture_output=True, check=False)

                # Register as anchor if all three anchor fields supplied
                if anchor_type and anchor_path:
                    anchor_cmd = [
                        "python3", str(anchor_script), "anchor", project,
                        "--type", anchor_type,
                        "--path", anchor_path,
                        "--desc", output_description[:200],
                        "--phase", f"finalize:{skill or workflow or 'unknown'}",
                    ]
                    if anchor_ref_for:
                        anchor_cmd.extend(["--ref-for", anchor_ref_for])
                    ar = subprocess.run(anchor_cmd, capture_output=True, text=True, check=False)
                    anchor_results["anchor_registered"] = (ar.returncode == 0)
                    anchor_results["anchor_output"] = ar.stdout.strip()
                    if ar.returncode != 0:
                        anchor_results["anchor_error"] = ar.stderr.strip()
                else:
                    anchor_results["anchor_registered"] = False
                    anchor_results["reason"] = (
                        "No --anchor-type / --anchor-path supplied; history logged but no anchor."
                    )

            result["anchor_memory"] = anchor_results
        except Exception as e:
            result["anchor_memory"] = {"skipped": True, "error": str(e)}

    # ── Phase B (2026-05-25) — Ledger feedback backstop ──────────
    # If this workflow invocation matches a recently-emitted ledger
    # suggestion (within 24h), auto-fire record_outcome(action='invoked').
    # Closes the AI-Memory-Dependent-Observability failure class — the
    # ledger feedback loop no longer depends on Claude remembering to log.
    if workflow:
        try:
            from execution.orchestration_ledger import (
                find_pending_match, record_outcome,
            )
            match = find_pending_match(workflow, max_age_hours=24)
            if match:
                record_outcome(
                    suggestion_id=match["suggestion_id"],
                    action="invoked",
                    workflow=workflow,
                    session_id=match.get("session_id"),
                    notes=f"auto-matched via chain_runner.finalize ({skill or 'no-skill'})",
                )
                result["ledger_feedback"] = {
                    "matched_suggestion_id": match["suggestion_id"],
                    "auto_recorded": True,
                }
            else:
                result["ledger_feedback"] = {"matched_suggestion_id": None}
        except Exception as e:
            # NEVER block finalize on ledger-feedback issues
            result["ledger_feedback"] = {"skipped": True, "error": str(e)}

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

    # Sub-agent miss (Phase D / 2026-05-12) — surfaces only on actual miss
    sa = result.get("sub_agent_log") or {}
    if sa.get("miss"):
        print(
            f"\n  ⚠️  SUB-AGENT MISS: workflow={sa.get('workflow')} qualifies but ran with "
            f"sub_agents_spawned={sa.get('sub_agents_spawned')}. Logged to "
            f"evolution_store/sub_agent_misses.jsonl. After 30d of misses, the 2026-05-12 brief "
            f"proposes escalating to gate-blocking. Pass --sub-agents N when invoking finalize."
        )

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
    # Supercomputer anchor-memory integration (added 2026-05-20)
    fin.add_argument("--project", default="", help="Project slug for anchor-memory write-back (projects/<slug>/state.yaml)")
    fin.add_argument("--anchor-type", default="", help="Anchor type (product_sheet|brand_brief|hero_visual|copy|video|ad_concept|...). Requires --project + --anchor-path to register.")
    fin.add_argument("--anchor-path", default="", help="Path to the deliverable file to register as an anchor. Requires --project + --anchor-type.")
    fin.add_argument("--anchor-ref-for", default="", help="Comma-separated list of later phase names that must reference this anchor.")
    # Excellence Lift Wave 1 (added 2026-05-21)
    fin.add_argument("--factual", type=float, default=None, help="Factual grounding score 1-10. Omit for N/A (pure creative/opinion). Score <6 BLOCKS delivery per quality_gate.md factual veto.")
    # Excellence Lift Wave 2 (added 2026-05-21)
    fin.add_argument("--anchor-named", action="store_true", help="Set when scores ≥8 have a named rubric anchor (rubric_v1.md). Without this flag, any dim ≥8 is capped at 7.5 by the bimodal taste filter.")
    # Autopilot Wave 5 stabilization (added 2026-05-23)
    fin.add_argument("--source-request", default=None, help="Original user request verbatim. Used for the post-hoc routing check instead of the output description. Autopilot's Phase 4 template MUST pass this to prevent false positives on the autopilot_orchestration binding.")

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
            project=args.project,
            anchor_type=args.anchor_type,
            anchor_path=args.anchor_path,
            anchor_ref_for=args.anchor_ref_for,
            factual_grounding=args.factual,
            anchor_named=args.anchor_named,
            source_request=args.source_request,
        )
        print_result(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
