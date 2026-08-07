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


def _auto_log_context_ethics(workflow: str, skill: str, notes: str) -> Dict[str, Any]:
    """Deterministic backstop for the Context Engineering Defense/Ethics Gate.

    The gate inside /ce-design and /ce-build is a persona-run judgment (name the
    technique, surface test, destabilization check). Per the banned-pattern rule
    ("AI-Memory-Dependent Observability is BANNED; always pair with a
    deterministic backstop"), that judgment must be paired with a deterministic
    log so the gate cannot silently no-op. When a context-engineering workflow
    finalizes, this guarantees a verdict entry — inferred from notes when the
    persona recorded one, else logged as NOT_OBSERVED so the gap is visible.
    Non-fatal: any error is swallowed so this never breaks the quality gate.
    """
    try:
        from context_ethics_gate import log_verdict, CONTEXT_ENGINEERING_WORKFLOWS
    except ImportError:
        try:
            from execution.context_ethics_gate import log_verdict, CONTEXT_ENGINEERING_WORKFLOWS
        except ImportError:
            return {"logged": False, "reason": "import_failed"}

    wf = (workflow or "").strip().lstrip("/")
    skill_l = (skill or "").lower()
    is_ce = wf in CONTEXT_ENGINEERING_WORKFLOWS or "context-engineering" in skill_l
    if not is_ce:
        return {"status": "skipped", "reason": "non_context_engineering"}

    notes_lower = (notes or "").lower()
    verdict = None
    for v in ("block", "review", "pass"):
        if (f"ethics gate: {v}" in notes_lower
                or f"defense/ethics verdict: {v}" in notes_lower
                or f"ethics: {v}" in notes_lower):
            verdict = v.upper()
            break

    if verdict:
        log_verdict(
            verdict,
            workflow=wf,
            note="auto-logged from chain_runner finalize; explicit verdict in notes",
            source="finalize_explicit",
        )
        return {"status": "logged", "verdict": verdict, "source": "explicit_in_notes"}

    log_verdict(
        "NOT_OBSERVED",
        workflow=wf,
        note="auto-logged from chain_runner finalize; context-engineering workflow finalized with no explicit ethics-gate verdict in notes",
        source="finalize_backstop",
    )
    return {"status": "logged", "verdict": "NOT_OBSERVED", "source": "auto_inferred"}


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
    'avatar-machine', 'avatar-manifold', 'manifold-to-copy',
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

    Source: _active/_archive/2026-08-07-sweep/system-integration/2026-05-12-agentic-os-elevation-brief.md Move 2.
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
# Types where factual grounding matters — the grounding_guard backstop runs here.
_GROUNDING_TASK_TYPES = {"Research", "Strategy", "Analysis", "Content", "Client Work"}

# ── Claim Risk Scan (added 2026-07-06) ───────────────────────────
# Path A = claim-safe content for funded health/supplement brands (binding
# decision 2026-07-01). A missed disease-claim is a real liability, so this
# cannot be a workflow the model has to remember to run — it has to be a
# deterministic trigger inside finalize. Task types where a health-flavored
# deliverable is plausible without any other signal.
_CLAIM_RISK_TASK_TYPES = {"Content", "Client Work", "Creative"}
# Health-domain keyword net — fires the scan even on a non-content-shaped
# task_type (e.g. "Strategy") when the description/skill/notes name a health
# brand. Deliberately broad; false positives just mean an extra scan runs
# (compass, not cage — the scan never blocks, so over-triggering is cheap).
_HEALTH_DOMAIN_TERMS = [
    "supplement", "wellness", "weight loss", "weight-loss", "fitness brand",
    "health brand", "nutrition", "gut health", "sleep aid", "energy drink",
    "hormone", "hormones", "immune", "detox", "probiotic", "vitamin",
    "keto", "cbd", "skincare claim", "metabolism", "gut ",
]


def _claim_risk_domain_match(*texts: str) -> str:
    """Return the first health-domain keyword found across the given texts
    (lowercased substring match), or '' if none. Used to fire claim_risk_scan
    on non-Content task types (e.g. a Strategy brief for a supplement brand)."""
    haystack = " ".join(t for t in texts if t).lower()
    for term in _HEALTH_DOMAIN_TERMS:
        if term in haystack:
            return term.strip()
    return ""


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

    # ── Cap 1.5: Structural Tells (added 2026-06-01) ─────────
    # The deterministic backstop for the banned MOVES (em-dashes, "It's not X.
    # It's Y." reveals, triple anaphora, "here's the part nobody…", cheap-question
    # closes) that prose_classifier's vocab scan misses. Origin: a teardown batch
    # shipped with all of these and finalized at a hollow 8.33 because nothing
    # mechanically scanned for structure. A FAIL caps expert_standard at 5.0 —
    # harder than the prose cap, since these are explicit voice-rule violations.
    if task_type in _COPY_TASK_TYPES and output_text and len(output_text) > 100:
        try:
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            import content_finish_gate as _cfg_mod
            _cfg = _cfg_mod.evaluate(output_text)
            if _cfg.get("verdict") == "FAIL":
                cur = enforced.get("expert_standard")
                if cur is not None and cur > 5:
                    caps_applied.append({
                        "rule": "structural_tells_cap",
                        "dimension": "expert_standard",
                        "from": cur, "to": 5.0,
                        "reason": "content_finish_gate FAIL: " + "; ".join(_cfg.get("fails", [])[:3]),
                    })
                    enforced["expert_standard"] = 5.0
        except Exception:
            pass

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

    # ── Cap 4: Grounding Integrity (added 2026-06-02) ────────
    # The SYSTEMIC backstop for the research-integrity bug class. Catches
    # ungrounded factual output — unsourced stats, [MODELED]-as-fact, a hardcoded
    # "GROUNDED" label with no URLs — at finalize, REGARDLESS of which workflow
    # produced it. So the false-PASS era cannot recur even from a workflow that
    # bypasses research.py. A FLAG caps expert_standard at 6.0 and tells the user
    # to re-ground via the unified engine. (Heuristic → cap+warn, not auto-block,
    # to avoid false positives; the cap still keeps ungrounded work out of the
    # high-quality band.) Deterministic backstop per feedback_ai-memory-dependent.
    grounding_verdict = "NOT_RUN"
    grounding_signals: List[str] = []
    if task_type in _GROUNDING_TASK_TYPES and output_text and len(output_text) > 200:
        try:
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            import grounding_guard as _gg
            _gr = _gg.scan(output_text, task_type)
            grounding_verdict = _gr.get("verdict", "NOT_RUN")
            grounding_signals = _gr.get("signals", [])
            if grounding_verdict == "FLAG":
                cur = enforced.get("expert_standard")
                # Always record on FLAG so the user SEES the grounding problem even
                # if another cap (e.g. prose) already lowered expert_standard.
                caps_applied.append({
                    "rule": "grounding_integrity_cap",
                    "dimension": "expert_standard",
                    "from": cur,
                    "to": (6.0 if (cur is not None and cur > 6) else cur),
                    "reason": ("grounding_guard FLAG: " + "; ".join(grounding_signals[:2])
                               + " — re-ground via `python3 execution/research.py`"),
                })
                if cur is not None and cur > 6:
                    enforced["expert_standard"] = 6.0
        except Exception:
            pass

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
        "grounding_verdict": grounding_verdict,
        "grounding_signals": grounding_signals,
    }


# ─────────────────────────────────────────────────────────────
# Wave 2 finalize-input latches (Harness Apex 2026-07-09)
# Factored as pure-ish functions so they are unit-testable without
# running a full finalize (finalize has no dry-run mode).
# ─────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────
# COMPASS MODE (Farrice, 2026-07-27) — "Nothing should ever be a cage."
# ──────────────────────────────────────────────────────────────────
# Quality latches (anchor-named, blind-pass, learning-debt, memory-mirror
# staleness) used to REFUSE finalize outright. Every one of them was a
# process check dressed as a correctness check, and every one of them
# interrupted flow work mid-ship. They now WARN and let the work through.
#
# The single exception is the Factual Veto (factual_grounding < 6). That one
# stays hard, because it only fires when the author has ALREADY scored the
# facts as unreliable — refusing to publish knowingly-wrong claims is not a
# cage, it's the whole point of the rubric.
#
# Toggle: COMPASS_MODE=0 in the environment restores the old refusals for a
# single run. There is no scheduled path back to blocking.
COMPASS_MODE = os.environ.get("COMPASS_MODE", "1") != "0"


def _compass(result: Dict[str, Any], message: str) -> bool:
    """Record a latch fire. Returns True if the caller should still refuse.

    In compass mode the message is appended to result['compass_warnings'] and
    the caller continues. Outside compass mode the caller refuses as before.
    """
    if COMPASS_MODE:
        result.setdefault("compass_warnings", []).append(message)
        return False
    return True


def check_anchor_named(
    scores: Dict[str, Optional[float]],
    anchor_named: Any,
) -> Optional[str]:
    """Anchor-named validation: any submitted dimension ≥8 requires a
    NON-EMPTY anchor phrase (--anchor-named "<anchor phrase>").

    Returns an error string (refusal) or None (ok). The phrase itself is
    extracted by the caller via anchor_phrase().
    """
    phrase = anchor_phrase(anchor_named)
    high = [f"{k}={v}" for k, v in scores.items() if v is not None and float(v) >= 8]
    if high and not phrase:
        return (
            "ANCHOR REQUIRED — " + ", ".join(high) + " scored ≥8 without "
            "--anchor-named \"<anchor phrase>\": rubric_v1.md says a ≥8 must name "
            "its matching anchor (can't name it → lower the score)."
        )
    return None


def anchor_phrase(anchor_named: Any) -> str:
    """The named anchor as a string. Legacy bool True yields '' — the CLI
    now passes the phrase itself; bare --anchor-named no longer satisfies
    the ≥8 requirement."""
    return anchor_named.strip() if isinstance(anchor_named, str) else ""


def check_blind_pass_latch(
    task_type: str,
    skill: str,
    expert: str,
    skip_blind_pass: bool,
    output_description: str = "",
    workflow: str = "",
) -> "Tuple[Dict[str, Any], Optional[str]]":
    """Extraction latch: finalize --type Extraction requires a recorded
    blind-pass verdict (execution/blind_pass.py) for the skill, or an
    explicit --skip-blind-pass override (logged, compass-not-cage —
    extractions stay cost-ungated per standing decision 2026-06-09).

    Returns (blind_pass_check dict for the result, error string or None).
    """
    if task_type != "Extraction":
        return {"status": "N/A"}, None

    slug = (skill or expert or "").strip()
    if not slug:
        return {"status": "MISSING"}, (
            "BLIND-PASS LATCH — finalize --type Extraction needs --skill (or --expert) "
            "so the recorded blind-pass verdict can be looked up. Pass the skill dir name."
        )

    verdicts: List[Dict[str, Any]] = []
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import blind_pass as _bp
        verdicts = _bp.recorded_verdicts(slug)
    except Exception as _exc:  # noqa: BLE001 — latch must not crash finalize
        return {"status": "ERROR", "detail": str(_exc)}, None

    if verdicts:
        latest = verdicts[-1]
        return {
            "status": "OK",
            "eval_id": latest.get("id"),
            "verdict": (latest.get("blind_pass") or {}).get("verdict")
                        or latest.get("expected_verdict"),
            "entries": len(verdicts),
        }, None

    if skip_blind_pass:
        # Wave-2 flip #2 (dormant until .agent/enforce-trials/blind_pass.json
        # activates): while the trial enforces, a bare --skip-blind-pass refuses —
        # the skip must carry a stated reason (--override-reason), which is logged
        # and surfaced in the COS morning receipt. Rubber-stamp skips were fired
        # on essentially every recent extraction (audit finding #3).
        _trial = None
        try:
            sys.path.insert(0, str(Path(__file__).resolve().parent / "hooks"))
            from enforce_trial import active_trial as _at
            _trial = _at("blind_pass")
        except Exception:
            _trial = None
        _reason = (os.environ.get("BLIND_PASS_OVERRIDE_REASON") or "").strip()
        if _trial and not _reason:
            return {"status": "MISSING"}, (
                f"BLIND-PASS ENFORCEMENT (trial to {_trial.get('ends')}): --skip-blind-pass "
                "now requires a stated reason. Re-run with env "
                "BLIND_PASS_OVERRIDE_REASON=\"<why the blind pass is genuinely not possible>\" "
                "(logged + surfaced in the COS receipt), or run the 3-step ritual below. "
                "Revert: set active:false in .agent/enforce-trials/blind_pass.json."
            )
        # Same override-logging pattern as the learning latch
        # (evolution_store/learning_latch_overrides.jsonl).
        try:
            _ov_path = Path(__file__).resolve().parent.parent / "evolution_store" / "blind_pass_overrides.jsonl"
            _ov_path.parent.mkdir(parents=True, exist_ok=True)
            with open(_ov_path, "a") as _of:
                _of.write(json.dumps({
                    "ts": datetime.now().isoformat(),
                    "event": "blind_pass_latch_override",
                    "output": output_description[:120],
                    "skill": skill, "expert": expert, "workflow": workflow,
                    "override_reason": _reason or None,
                    "trial_enforced": bool(_trial),
                }) + "\n")
        except Exception:
            pass
        return {"status": "OVERRIDDEN", "detail": "no recorded verdict; --skip-blind-pass logged"}, None

    return {"status": "MISSING"}, (
        f"BLIND-PASS MISSING — finalize --type Extraction requires a recorded blind-pass "
        f"verdict for '{slug}' and none exists in evolution_store/ground_truth/eval_set_v1.jsonl.\n"
        "Run the ritual (the judgment stays human/model; the record is automatic):\n"
        f"  1. python3 execution/blind_pass.py prepare --expert {slug}\n"
        "  2. Generate 1-2 outputs with the skill's Tier-1 workflow; judge side-by-side vs the\n"
        "     reference corpus per directives/embodiment-standard.md Blind-Pass Protocol.\n"
        f"  3. python3 execution/blind_pass.py record --expert {slug} --verdict PASS|FAIL --notes \"...\"\n"
        "Then re-run finalize. Override (logged to evolution_store/blind_pass_overrides.jsonl): "
        "--skip-blind-pass."
    )


def check_verdict_advisory(verdict: str, precedent: str, composite) -> Dict[str, Any]:
    """Grading R1 (GRADING-LOOP-REDESIGN.md) — ADVISORY precedent validation.

    SHIP should cite the nearest calibrated precedent by EVAL-ID; this validates
    the citation deterministically (exists, calibrated_by_human, expected_composite
    within ±1.0 of this finalize's composite when both are present). R1 never
    blocks — results are logged to evolution_store/verdict_advisory.jsonl so the
    R2 blocking decision is made on a week of real data, per the rollout table.
    """
    if verdict == "SHIP" and not precedent:
        return {"status": "MISSING_PRECEDENT",
                "detail": "SHIP without --precedent EVAL-ID (R2 will refuse this)"}
    if not precedent:
        return {"status": "OK", "detail": ""}
    try:
        eval_path = Path(__file__).resolve().parent.parent / "evolution_store" / "ground_truth" / "eval_set_v1.jsonl"
        rows = {}
        with open(eval_path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                    rows[str(r.get("id", "")).upper()] = r
                except ValueError:
                    continue
    except OSError as exc:
        return {"status": "ERROR", "detail": f"eval set unreadable: {exc}"}
    row = rows.get(precedent.upper())
    if not row:
        return {"status": "UNKNOWN_PRECEDENT", "detail": f"{precedent} not in eval_set_v1.jsonl"}
    if not row.get("calibrated_by_human"):
        return {"status": "UNCALIBRATED_PRECEDENT",
                "detail": f"{precedent} exists but is not calibrated_by_human"}
    exp = row.get("expected_composite")
    if exp is not None and composite is not None and abs(float(exp) - float(composite)) > 1.0:
        return {"status": "TOLERANCE_FAIL",
                "detail": f"{precedent} expected_composite={exp} vs this composite={composite} (>±1.0)"}
    return {"status": "VALID", "detail": f"{precedent} calibrated, within tolerance"}


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
    # Excellence Lift Wave 2 (added 2026-05-21). Harness Apex Wave 2
    # (2026-07-09): now a STRING — the anchor phrase itself (rubric_v1.md
    # anchor name). Any submitted dim ≥8 without a non-empty phrase refuses
    # (check_anchor_named). Legacy bool True no longer satisfies ≥8.
    anchor_named: Any = False,
    # Autopilot Wave 5 stabilization (added 2026-05-23): original user intent
    # used for the post-hoc routing check at line ~918. When None, the call
    # falls back to checking output_description (legacy behavior). Autopilot's
    # Phase 4 template MUST pass the original user request here to prevent the
    # autopilot_orchestration binding from firing on every sub-workflow.
    source_request: Optional[str] = None,
    # Content scanning (added 2026-06-01): the path to the ACTUAL deliverable so
    # the prose + structural-tells caps scan the real artifact, not the short
    # output_description summary. Without this the caps scanned summaries and slop
    # (em-dashes, reveals, cheap closes) shipped with a clean score. If given and
    # readable, its contents become the text the caps scan.
    content_path: str = "",
    # Outcome-loop closure (added 2026-06-12): what success looks like for this
    # deliverable and when to check whether it happened. Flows into the pending
    # revenue-outcome stub so `revenue_tracker due` + the session-ledger
    # staleness line surface it deterministically. check_in_days=None uses the
    # tracker default (14d).
    expected_outcome: str = "",
    check_in_days: Optional[int] = None,
    # Research depth gate (added 2026-07-26, shallow-research fix): path to a
    # depth-gate receipt JSON produced by `research_quality_gate.py validate
    # --receipt`. Research-type finalizes without a PASSING receipt get Factual
    # Grounding capped at 6 (see Step 2.4).
    depth_receipt: str = "",
    # Learning-debt latch (Solution Recorder, added 2026-07-07): finalize
    # refuses to proceed if the newest session ledger has open learning_debt
    # (a hard-won fix never captured as a Solution Card), unless the caller
    # clears it (learning_path -> validated card) or explicitly overrides
    # (skip_learning -> logged to evolution_store/learning_latch_overrides.jsonl).
    learning_path: str = "",
    skip_learning: bool = False,
    # Extraction blind-pass latch (Harness Apex Wave 2, 2026-07-09): finalize
    # --type Extraction refuses without a recorded blind_pass.py verdict for
    # the skill unless this override is set (logged to
    # evolution_store/blind_pass_overrides.jsonl — same pattern as skip_learning).
    skip_blind_pass: bool = False,
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

    # ── Step 1.05: Anchor-named validation (Harness Apex Wave 2, 2026-07-09) ─
    # Any submitted dimension ≥8 must arrive with --anchor-named "<anchor phrase>"
    # (a non-empty string naming the rubric_v1.md anchor). Refusal here replaces
    # the old silent path where unanchored 8s slid through to taste_signature
    # Rule 2 and got flattened to 7.25 without explanation (2026-07-07 incident).
    _anchor_err = check_anchor_named(
        {
            "intent_alignment": intent_alignment,
            "expert_standard": expert_standard,
            "adversarial_resilience": adversarial_resilience,
            "factual_grounding": factual_grounding,
        },
        anchor_named,
    )
    if _anchor_err and _compass(result, _anchor_err):
        result["success"] = False
        result["error"] = _anchor_err
        return result
    _anchor_phrase = anchor_phrase(anchor_named)
    if _anchor_phrase:
        result["anchor_phrase"] = _anchor_phrase
        if f"anchor: {_anchor_phrase.lower()}" not in (notes or "").lower():
            notes = (notes + " | " if notes else "") + f"Anchor: {_anchor_phrase}"
    # Downstream (taste_signature) consumes a bool.
    anchor_named = bool(_anchor_phrase) or anchor_named is True

    # ── Step 1.07: Extraction blind-pass latch (Harness Apex Wave 2) ─
    # Quality latch, not a spend gate — extractions stay cost-ungated per
    # Farrice's standing decision 2026-06-09. See check_blind_pass_latch().
    _bp_check, _bp_err = check_blind_pass_latch(
        task_type=task_type, skill=skill, expert=expert,
        skip_blind_pass=skip_blind_pass,
        output_description=output_description, workflow=workflow,
    )
    result["blind_pass_check"] = _bp_check
    if _bp_err and _compass(result, _bp_err):
        result["success"] = False
        result["error"] = _bp_err
        return result

    # ── Step 1.1: Learning-debt latch (Solution Recorder, added 2026-07-07) ─
    # session_ledger_hook.py books learning_debt on the newest session ledger
    # when a Bash fail->success streak (>=3) never got captured as a Solution
    # Card. Finalize is the Chain's hard stop — it refuses here rather than
    # let the capture evaporate. Only FRESH debt (ts within the last 4h,
    # solution_recorder.LEARNING_DEBT_FRESH_HOURS) can block — the active
    # session's ledger is almost always the newest (its posttool hook touches
    # it every call) and the GOLDEN RULE forbids concurrent drivers, so
    # freshness is the proportionate guard against a stale ledger false-block.
    # Surgical: this is the only new gate; scoring/taste logic is untouched.
    _ledger_glob_dir = Path(__file__).resolve().parent.parent / ".agent" / "sessions"
    _ledger_path = None
    _ledger_data: Dict[str, Any] = {}
    try:
        _candidates = sorted(_ledger_glob_dir.glob("ledger-*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
        if _candidates:
            _ledger_path = _candidates[0]
            _ledger_data = json.loads(_ledger_path.read_text(encoding="utf-8"))
    except Exception:
        _ledger_path, _ledger_data = None, {}

    # ── Expert-load truth, half 2 (2026-07-27) ─────────────────────────
    # Compare what the session ACTUALLY loaded (full reads) against what it
    # only grepped, and against the roster a multi-expert room claims to run.
    # Root incident: /writers-room reported a 13-expert treatment while the
    # ledger showed one skill_loaded — the genius files were grepped, not
    # read, and nothing surfaced the gap. Nudge only (compass doctrine).
    try:
        _lt_loaded = sorted({d["name"] for d in (_ledger_data.get("debts") or [])
                             if d.get("type") == "skill_loaded"})
        _lt_grepped = sorted({d["name"] for d in (_ledger_data.get("debts") or [])
                              if d.get("type") == "skill_grepped"})
        result["load_truth"] = {"loaded": _lt_loaded, "grepped": _lt_grepped}
        # SYSTEM-WIDE roster derivation (Farrice 2026-07-27: "make sure this
        # doesn't happen system-wide"): the roster is read from the workflow
        # file itself — every genius.md it names — so ANY multi-expert room,
        # current or future, gets the truth check with zero registration.
        # Floor: a room that names N experts must fully load at least
        # ceil(N * 0.6) of them (cards count; grep does not).
        _room_min = None
        _wf_slug = (workflow or "").strip().lstrip("/")
        if _wf_slug:
            _wf_path = Path(__file__).resolve().parent.parent / ".agent" / "workflows" / f"{_wf_slug}.md"
            if _wf_path.exists():
                _named = set(re.findall(r"skills/([a-z0-9\-]+)/(?:genius|lens-card)\.md",
                                        _wf_path.read_text(encoding="utf-8", errors="replace")))
                if len(_named) >= 3:
                    _room_min = max(3, -(-len(_named) * 6 // 10))  # ceil(N*0.6)
        if _room_min and len(_lt_loaded) < _room_min:
            result.setdefault("compass_warnings", []).append(
                f"EXPERT-LOAD TRUTH — workflow '{workflow}' declares a room of "
                f"{_room_min}+ experts but this session fully loaded "
                f"{len(_lt_loaded)} ({', '.join(_lt_loaded) or 'none'}) and only "
                f"grepped {len(_lt_grepped)}. A named-but-unloaded expert is a "
                f"laundered half-pass — load lens-card.md per expert, read "
                f"genius.md on every lens that fires."
            )
    except Exception:
        pass

    _all_debt = _ledger_data.get("learning_debt") or []
    try:
        from solution_recorder import split_debt_freshness as _split_debt
        _learning_debt, _stale_debt = _split_debt(_all_debt)
    except ImportError:
        # Inline fallback mirroring solution_recorder.split_debt_freshness:
        # unparseable ts counts as stale (can't prove freshness -> can't block).
        from datetime import timedelta as _timedelta
        _cutoff = datetime.now() - _timedelta(hours=4)
        _learning_debt, _stale_debt = [], []
        for _d in _all_debt:
            try:
                _ok = datetime.fromisoformat(str(_d.get("ts", ""))) >= _cutoff
            except Exception:
                _ok = False
            (_learning_debt if _ok else _stale_debt).append(_d)

    if _learning_debt:
        if learning_path:
            # The card must be a REAL, valid Solution Card under docs/solutions/
            # — any other file refuses (Fix 3, 2026-07-07). Validation is
            # solution_recorder.validate_card (single source of truth); the
            # inline fallback covers ImportError only.
            _lp = Path(learning_path).resolve()
            _solutions_dir = Path(__file__).resolve().parent.parent / "docs" / "solutions"
            _violations: List[str] = []
            if _solutions_dir.resolve() not in _lp.parents:
                _violations.append(f"file must live under docs/solutions/ (got {_lp})")
            elif not _lp.exists():
                _violations.append(f"file not found: {_lp}")
            else:
                try:
                    from solution_recorder import validate_card as _validate_card
                    _violations = _validate_card(_lp)
                except ImportError:
                    # Fallback: frontmatter keys + 7-H2 presence check inline.
                    try:
                        _text = _lp.read_text(encoding="utf-8")
                        _fm_m = re.match(r"^---\n(.*?)\n---\n?(.*)$", _text, re.DOTALL)
                        if not _fm_m:
                            _violations.append("frontmatter block not found")
                        else:
                            _fm_text, _body = _fm_m.group(1), _fm_m.group(2)
                            for _key in ("name", "problem_signature", "domain", "tags", "date", "status"):
                                if not re.search(rf"^{_key}:\s*\S", _fm_text, re.MULTILINE):
                                    _violations.append(f"missing required frontmatter key: {_key}")
                            for _h2 in ("## Problem", "## Root Cause", "## Approach That Worked",
                                        "## Dead Ends", "## Verification", "## Weaker-Model Trap",
                                        "## Pointers"):
                                if _h2 not in _body:
                                    _violations.append(f"missing section: {_h2}")
                    except OSError as _exc:
                        _violations.append(f"file unreadable: {_exc}")
            if _violations:
                result["success"] = False
                result["error"] = (
                    f"LEARNING CARD INVALID — {learning_path} does not pass Solution Card "
                    "validation:\n  - " + "\n  - ".join(_violations) +
                    "\nSave a valid card first: python3 execution/solution_recorder.py save --file <path>."
                )
                return result
            if _ledger_path is not None:
                try:
                    _ledger_data["learning_debt"] = []
                    _ledger_path.write_text(json.dumps(_ledger_data, indent=1), encoding="utf-8")
                except Exception:
                    pass
        elif skip_learning:
            try:
                _overrides_path = Path(__file__).resolve().parent.parent / "evolution_store" / "learning_latch_overrides.jsonl"
                _overrides_path.parent.mkdir(parents=True, exist_ok=True)
                with open(_overrides_path, "a") as _of:
                    _of.write(json.dumps({
                        "ts": datetime.now().isoformat(),
                        "event": "learning_latch_override",
                        "output": output_description[:120],
                        "skill": skill, "workflow": workflow,
                        "learning_debt": _learning_debt,
                    }) + "\n")
            except Exception:
                pass
        else:
            _evidence_lines = "\n".join(
                f"  - {d.get('ts', '?')} · streak {d.get('streak', '?')} · {d.get('evidence', '')}"
                for d in _learning_debt
            )
            _ld_err = (
                "LEARNING DEBT OPEN — a hard problem was cracked this session "
                f"({len(_learning_debt)} fresh fail→success streak(s), ledger: "
                f"{_ledger_path.name if _ledger_path else '<unknown>'}) with no Solution Card saved.\n"
                f"{_evidence_lines}\n"
                "Run: python3 execution/solution_recorder.py draft --slug <s> --problem \"<one line>\", "
                "fill it in, then python3 execution/solution_recorder.py save --file <path>. Rerun "
                "finalize with --learning <path-to-card>.\n"
                "If this debt belongs to another window/session, clear with --skip-learning "
                "(logged) — see docs/solutions/index.md first."
            )
            if _compass(result, _ld_err):
                result["success"] = False
                result["error"] = _ld_err
                return result

    # ── Step 1.5: Verification accountability (added 2026-06-12) ─
    # Chain Step 5.5 fired before delivery — this makes skipping it VISIBLE.
    # Fact-bearing task types must arrive with either a --factual score or an
    # explicit "Verification: <PASS/FAIL/PARTIAL/N/A>" declaration in --notes
    # (a deliberate N/A is honest; silence is not). Misses are logged to
    # evolution_store/verification_misses.jsonl (deterministic telemetry, same
    # pattern as sub_agent_misses). Observe-mode by default; VERIFY_ENFORCE=1
    # turns a miss into a hard finalize failure. Follows the LEDGER_ENFORCE
    # observe-then-enforce rollout pattern (2026-06-09).
    _FACT_BEARING_TYPES = {"Content", "Research", "Strategy", "Client Work", "Analysis"}
    verification_declared = "verification:" in (notes or "").lower()
    if task_type in _FACT_BEARING_TYPES and factual_grounding is None and not verification_declared:
        miss = {
            "timestamp": datetime.now().isoformat(),
            "output": output_description[:120],
            "task_type": task_type,
            "skill": skill,
            "workflow": workflow,
            "enforced": os.environ.get("VERIFY_ENFORCE", "0") == "1",
        }
        try:
            _misses_path = Path(__file__).resolve().parent.parent / "evolution_store" / "verification_misses.jsonl"
            _misses_path.parent.mkdir(parents=True, exist_ok=True)
            with open(_misses_path, "a") as _mf:
                _mf.write(json.dumps(miss) + "\n")
        except Exception:
            pass
        result["verification_check"] = {
            "status": "MISSING",
            "detail": (
                f"task_type '{task_type}' is fact-bearing but no --factual score was given "
                "and --notes carries no 'Verification:' declaration. Run Chain Step 5.5 "
                "(deterministic assist: python3 execution/claim_audit.py check <deliverable>), then "
                "either pass --factual <1-10> or add '| Verification: PASS/FAIL/PARTIAL/N/A' to --notes."
            ),
        }
        if os.environ.get("VERIFY_ENFORCE", "0") == "1":
            result["success"] = False
            result["error"] = "VERIFICATION MISSING — " + result["verification_check"]["detail"]
            return result
    else:
        result["verification_check"] = {"status": "OK" if (factual_grounding is not None or verification_declared) else "N/A"}

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
    # Scan the ACTUAL deliverable when a content_path is supplied; else fall back
    # to the description (legacy behavior). This is what lets the caps see the
    # real post, not a flattering summary of it.
    _scan_text = output_description
    if content_path:
        try:
            _cp = Path(content_path)
            if _cp.exists():
                _scan_text = _cp.read_text()
        except Exception:
            pass

    # ── Step 2.4: Research depth gate (2026-07-26 shallow-research fix) ──
    # A Research-type deliverable without a PASSING depth-gate receipt
    # (execution/research_quality_gate.py validate --receipt) caps Factual
    # Grounding at 6.0. URL-having is not coverage: this is what stops a
    # reconnaissance sweep from being laundered into "trusted insight" by a
    # high self-scored grounding number. Shallow work may exist; shallow work
    # scored as decision-grade may not.
    depth_gate_status = "N/A"
    if task_type == "Research":
        _receipt_ok = False
        if depth_receipt:
            try:
                _rd = json.loads(Path(depth_receipt).read_text())
                _receipt_ok = bool(_rd.get("overall_pass"))
                depth_gate_status = "PASS" if _receipt_ok else "FAIL"
            except Exception:
                depth_gate_status = "UNREADABLE"
        else:
            depth_gate_status = "MISSING"
        if not _receipt_ok and factual_grounding is not None and factual_grounding > 6.0:
            factual_grounding = 6.0
            notes = (notes + " | DEPTH GATE: no passing depth receipt — Factual Grounding "
                             "capped at 6 (RECON-GRADE, not decision-grade). Run "
                             "research_quality_gate.py validate --receipt and pass "
                             "--depth-receipt to lift the cap.").strip(" |")

    enforced = _enforce_caps(
        raw_scores={
            "intent_alignment": intent_alignment,
            "expert_standard": expert_standard,
            "adversarial_resilience": adversarial_resilience,
        },
        output_text=_scan_text,
        task_type=task_type,
        factual_grounding=factual_grounding,
    )

    # ── Step 2.7: Apply bimodal taste signature (Wave 2) ──────────
    # taste_signature.apply runs ON TOP of the Wave 1 caps. It encodes
    # Farrice's bimodal taste signature (rubric_v1.md Bimodal Taste section)
    # — harsh on failures, 8-must-be-earned, anti-cluster detection.
    #
    # THE "FLATTENING" IS INTENDED BEHAVIOR (diagnosed 2026-07-09, Harness
    # Apex Wave 2). Incident 2026-07-07: --intent 9 --expert-score 9
    # --adversarial 8 without --anchor-named produced uniform
    # 7.25/7.25/7.25 (composite 7.25). Code path: taste_signature.apply()
    # Rule 2 ("8-must-be-earned") sets EACH dim ≥8 to the fixed value
    # _EARNED_8_CAP = 7.25 when no anchor is named — a per-dimension cap to
    # a constant, so three dims ≥8 all land on the same number and relative
    # structure (9/9/8) is deliberately discarded: an unanchored 9 carries
    # no more evidence than an unanchored 8. WHY 7.25 and not a composite
    # cap: 7.25 sits below the 7.5 PASS floor so unanchored ≥8s can never
    # PASS (fixes the 2026-05-22 plateau where cap==floor piled 70% of
    # traces at exactly 7.50); documented in taste_signature.py Rule 2
    # docstring and confirmed CORRECT-and-stays by E3
    # (directives/embodiment-standard.md § Scoring Discipline). NOT the
    # prose_classifier cap (that caps expert_standard only, at 6.0) and NOT
    # regression logic (read-only baseline compare). Since Step 1.05, the
    # unanchored-≥8 path refuses loudly at input instead of flattening
    # silently — Rule 2 remains as defense in depth for programmatic
    # callers. Raw scores stay visible in raw_* keys; the cap writes an
    # earned_8_cap audit row per dimension into caps_applied.
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
    result["depth_gate"] = depth_gate_status
    result["taste_verdict"] = adjusted.taste_verdict
    result["anchor_named"] = anchor_named
    # Audit trail: Wave 1 caps + Wave 2 taste adjustments combined
    result["caps_applied"] = enforced["caps_applied"] + adjusted.adjustments
    result["prose_check"] = {
        "verdict": enforced["prose_verdict"],
        "ai_score": enforced["prose_details"].get("ai_score"),
        "signal_count": enforced["prose_details"].get("signal_count"),
    }
    result["grounding_check"] = {
        "verdict": enforced.get("grounding_verdict", "NOT_RUN"),
        "signals": enforced.get("grounding_signals", []),
    }

    # ── Step 2.6: Claim Risk Scan (added 2026-07-06) ─────────────
    # Deterministic first pass for Path A (claim-safe content for funded
    # health brands) — see _CLAIM_RISK_TASK_TYPES / _HEALTH_DOMAIN_TERMS above.
    # Compass-not-cage: FLAGS loudly on DISEASE_CLAIM, never blocks or caps a
    # score. Fires only when a real content_path is given (the scan needs the
    # actual artifact, same as the prose/grounding caps above) AND either the
    # task_type is content-shaped or a health-domain keyword appears in the
    # description/skill/notes. Everything else pays zero cost: no content_path
    # means no scan and no print at all.
    _domain_hit = _claim_risk_domain_match(output_description, skill, notes)
    if content_path:
        if task_type in _CLAIM_RISK_TASK_TYPES or _domain_hit:
            try:
                sys.path.insert(0, str(Path(__file__).resolve().parent))
                import claim_risk_scan as _crs
                claim_risk_result = _crs.scan(_scan_text)
                result["claim_risk_check"] = {
                    "verdict": claim_risk_result["verdict"],
                    "counts": claim_risk_result["counts"],
                    "domain_signal": _domain_hit or f"task_type={task_type}",
                }
                if claim_risk_result["verdict"] == "DISEASE_CLAIM":
                    notes = (notes + " | " if notes else "") + "claim_risk: FLAGGED"
                    disease_hits = claim_risk_result["hits"]["DISEASE_CLAIM"]
                    print("\n" + "🚨" * 30)
                    print("🚨 CLAIM RISK — DISEASE-CLAIM LANGUAGE DETECTED (claim_risk_scan.py)")
                    print("🚨" * 30)
                    for h in disease_hits[:8]:
                        print(f"  • {h['pattern']}  —  \"{h['context']}\"")
                        print(f"      compliant swap → {h['swap']}")
                    if len(disease_hits) > 8:
                        print(f"  ...and {len(disease_hits) - 8} more.")
                    print(f"  Full detail: python3 execution/claim_risk_scan.py scan {content_path}")
                    print("  This FLAGS — it does not block. Path A ships claim-safe content; route")
                    print("  this asset through /pre-launch-compliance-gate before it goes live.")
                    print("🚨" * 30 + "\n")
                elif claim_risk_result["verdict"] in ("RISKY", "WATCH"):
                    r_count = claim_risk_result["counts"].get("RISKY", 0)
                    w_count = claim_risk_result["counts"].get("WATCH", 0)
                    print(
                        f"  claim_risk_scan: {claim_risk_result['verdict']} — {r_count} RISKY / "
                        f"{w_count} WATCH hit(s). Detail: python3 execution/claim_risk_scan.py scan {content_path}"
                    )
            except Exception as e:
                result["claim_risk_check"] = {"verdict": "ERROR", "error": str(e)}
        else:
            result["claim_risk_check"] = {"verdict": "SKIPPED"}
            print(f"  claim_risk_scan: skipped (task_type={task_type!r}, no health-domain signal)")
    else:
        result["claim_risk_check"] = {"verdict": "NOT_APPLICABLE"}

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

    # ── Step 6.5: Auto-log routing decision ──────────────────────
    # Routing intelligence sat DORMANT (0 entries ever, 2026-07-02 audit)
    # because logging depended on manual CLI / /rate calls. Finalize is the
    # deterministic seam where expert/skill/workflow/intent are all known.
    try:
        from routing_intelligence import log_routing_decision
        routing_id = log_routing_decision(
            request_summary=output_description,
            intent_score=int(intent_alignment) if intent_alignment is not None else 0,
            domain_detected=task_type or "unspecified",
            experts_deployed=[e for e in [expert] if e],
            tier_loaded=0,
            mode="finalize-auto",
            workflow_used=workflow or "",
            ensemble=bool(sub_agents_spawned and sub_agents_spawned >= 2),
        )
        result["routing_logged"] = routing_id
    except Exception:
        result["routing_logged"] = None

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
            if _compass(result, halt_msg):
                result["memory_halt"] = halt_msg
                result["status"] = "halted"
                print(f"\n{'🔴 ' * 20}")
                print(f"🔴 {halt_msg}")
                print(f"{'🔴 ' * 20}\n")
                return result
            print(f"\n  ⚠  {halt_msg}\n     (compass mode: warned, not halted)")

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

            # Map bimodal taste verdict -> Verdict select option (MARGINAL
            # reads as PARTIAL — neither a clean pass nor a clean fail).
            _verdict_map = {"PASS": "PASS", "MARGINAL": "PARTIAL", "FAIL": "FAIL"}
            vault_verdict = _verdict_map.get(getattr(adjusted, "taste_verdict", ""), "")

            vault_result = notion.create_knowledge_vault_entry(
                name=output_description,
                summary=output_description,
                source=f"chain_runner finalize ({workflow or 'direct'})",
                expert=expert or '',
                domain=domain,
                entry_type=entry_type,
                key_patterns=notes[:200] if notes else '',
                genius_score=min(5, max(2, int(composite / 2))),
                antigravity_skill=skill or '',
                tags=tags,
                workflow=workflow or '',
                task_type=task_type,
                intent_score=intent_alignment,
                expert_score=expert_standard,
                adversarial_score=adversarial_resilience,
                factual_score=factual_grounding,
                composite_score=composite,
                verdict=vault_verdict,
                sub_agents=sub_agents_spawned,
                notes=notes or '',
                session_date=datetime.now().date().isoformat(),
            )
            result["knowledge_vault_sync"] = {"success": True, "url": vault_result}
            if getattr(notion, "_last_degraded", None):
                result["knowledge_vault_sync"]["degraded_properties"] = notion._last_degraded
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

    # ── Step 11.9: Context-engineering ethics-gate backstop (2026-05-30) ──
    # Deterministic floor for the Defense/Ethics Gate inside /ce-design,
    # /ce-build, /ce-honesty etc. so it cannot silently no-op (the banned
    # AI-memory-dependent-observability pattern). Logs a verdict for every
    # context-engineering finalize — explicit when the persona recorded one,
    # NOT_OBSERVED otherwise so the gap is visible. Non-fatal.
    try:
        ce_ethics_log = _auto_log_context_ethics(workflow, skill, notes)
        result["context_ethics_log"] = ce_ethics_log
    except Exception as e:
        result["context_ethics_log_error"] = str(e)

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
                expected_outcome=expected_outcome,
                check_in_days=check_in_days,
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


def _pin_session_from_finalize(output_description, *, workflow="", project="",
                               content_path="", thread="", status="active",
                               task_type="") -> None:
    """Auto-pin a finalized session to the handoff store so /resume surfaces it by
    name (title = output_description). Idempotent per (date, thread): slug=thread
    means re-finalizing the same work-stream UPDATES the one menu row rather than
    piling up. Best-effort: prints `CHAIN PINNED` on success (the session-ledger
    Stop hook watches for that marker to keep its no-pin backstop quiet) and never
    raises into finalize. Part of the session-pin formula (2026-06-23)."""
    try:
        import re as _re, sys as _sys, tempfile as _tf, subprocess as _sp
        from pathlib import Path as _Path

        def _slug(s):
            return _re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")

        th = _slug(thread) or _slug(project) or _slug(workflow) or _slug(output_description)[:48]
        if not th:
            print("  (session pin skipped: no thread slug)")
            return
        title = (output_description or th).strip().replace("\n", " ")
        ptr = (content_path or "").strip()
        body = (
            f"# {title}\n\n"
            + (f"**Pointer:** `{ptr}`\n\n" if ptr else "")
            + f"**Next session focus**: Resume the `{th}` work-stream — see the deliverable above.\n\n"
            + f"_Auto-pinned by chain_runner.finalize ({workflow or task_type or 'finalize'})._\n"
        )
        tmp = _Path(_tf.gettempdir()) / f"handoff-pin-{th}.md"
        tmp.write_text(body, encoding="utf-8")
        store = _Path(__file__).resolve().parent / "handoff_store.py"
        r = _sp.run(
            [_sys.executable, str(store), "save", str(tmp),
             "--thread", th, "--slug", th, "--status", status,
             "--hint", title, "--pin", "--overwrite"],
            capture_output=True, text=True, timeout=20,
        )
        if r.returncode == 0:
            print(f"  CHAIN PINNED thread={th}  → resume with: /resume {th}")
        else:
            print(f"  (session pin skipped: {(r.stderr or r.stdout).strip()[:140]})")
    except Exception as e:
        print(f"  (session pin skipped: {e})")


def _print_auto_preview(content_path: str, task_type: str) -> None:
    """--auto: surface the SAME deterministic checks _enforce_caps() runs
    internally (prose_classifier.should_cap_expert_standard + grounding_guard)
    up front, before the caller commits to --intent/--expert-score/--adversarial.

    Read-only preview. Changes no scoring/veto logic — finalize() below still
    runs the real _enforce_caps() pass and applies the caps itself; this just
    removes the guesswork of not knowing in advance whether one will fire.
    """
    print("\n" + "=" * 60)
    print("🔎 AUTO-COMPUTED (--auto preview)")
    print("=" * 60)

    if not content_path or not os.path.isfile(content_path):
        print("  ⚠️  No readable --content-file given — nothing to scan.")
        print("      Pass --content-file <path> to preview prose/grounding caps.")
        print("=" * 60 + "\n")
        return

    try:
        with open(content_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"  ⚠️  Could not read {content_path}: {e}")
        print("=" * 60 + "\n")
        return

    # Same Cap 1 check finalize()/_enforce_caps() runs internally.
    if len(text) > 100:
        try:
            cap_required, details = should_cap_expert_standard(text)
            verdict = details.get("verdict", "?")
            ai_score = details.get("ai_score", "?")
            signal_count = details.get("signal_count", "?")
            print(f"  prose_classifier   : verdict={verdict}  ai_score={ai_score}/10  signals={signal_count}")
            if cap_required:
                print("                        -> would cap expert_standard at 6.0")
        except Exception as e:
            print(f"  prose_classifier   : ERROR ({e})")
    else:
        print("  prose_classifier   : NOT_RUN (content <=100 chars)")

    # Same Cap 4 check finalize()/_enforce_caps() runs internally, for the
    # task types the real gate applies it to.
    if task_type in _GROUNDING_TASK_TYPES and len(text) > 200:
        try:
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            import grounding_guard as _gg
            gr = _gg.scan(text, task_type)
            g_verdict = gr.get("verdict", "?")
            g_signals = gr.get("signals", [])
            print(f"  grounding_guard    : verdict={g_verdict}  signals={'; '.join(g_signals[:2]) or 'none'}")
            if g_verdict == "FLAG":
                print("                        -> would cap expert_standard at 6.0 (unless already lower)")
        except Exception as e:
            print(f"  grounding_guard    : ERROR ({e})")
    else:
        print(f"  grounding_guard    : NOT_RUN (task_type={task_type!r} not gated, or content <=200 chars)")

    print("=" * 60)
    print("  These are previews of the SAME caps finalize() applies below.")
    print("  Judgment scores (--intent/--expert-score/--adversarial) are still")
    print("  required from you — --auto only removes the guesswork on the")
    print("  deterministic dimensions.")
    print("=" * 60 + "\n")


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

    # Compass-mode nudges: latches that used to refuse now report and let the
    # work through. Visible so they still do their job, never blocking.
    for _w in result.get("compass_warnings", []):
        print(f"\n  🧭 NUDGE (did not block): {_w.splitlines()[0]}")
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

    # Grounding check (the systemic research-integrity backstop)
    grounding = result.get("grounding_check")
    if grounding and grounding.get("verdict") == "FLAG":
        print(f"\n  Grounding:  🔴 FLAG — ungrounded factual output (re-ground via `python3 execution/research.py`):")
        for s in grounding.get("signals", [])[:3]:
            print(f"                • {s}")
    elif grounding and grounding.get("verdict") == "WARN":
        print(f"\n  Grounding:  🟡 WARN — thin sourcing: {'; '.join(grounding.get('signals', [])[:2])}")

    # Claim risk check (Path A deterministic compliance flag — never blocks)
    crc = result.get("claim_risk_check")
    if crc and crc.get("verdict") == "DISEASE_CLAIM":
        print(f"\n  Claim Risk: 🚨 DISEASE_CLAIM — {crc['counts'].get('DISEASE_CLAIM', 0)} hit(s). See warning block above.")
    elif crc and crc.get("verdict") in ("RISKY", "WATCH"):
        print(f"\n  Claim Risk: ⚡ {crc['verdict']} — {crc['counts']}")

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

    # Verification accountability (Step 5.5 made visible — 2026-06-12)
    vc = result.get("verification_check", {})
    if vc.get("status") == "MISSING":
        print(f"\n  ⚠️  VERIFICATION MISSING (observe mode — logged to evolution_store/verification_misses.jsonl)")
        print(f"     {vc.get('detail', '')[:220]}")
    elif vc.get("receipt"):
        print(f"\n  🧾 Verification receipt: {vc['receipt'][:200]}")

    # Revenue tracking reminder (for client/content deliverables)
    task_type = result.get("task_type", "")
    if task_type in ("Client Work", "Content", "Creative", "Strategy"):
        print(f"\n  💰 Revenue tracking: Log outcome when results come in →")
        print(f"     python execution/revenue_tracker.py log \"{result['output'][:50]}...\" --revenue <$> --outcome \"<result>\"")
        reg = result.get("revenue_autolink", {})
        entry = reg.get("entry", {}) if isinstance(reg, dict) else {}
        if entry.get("check_in_date"):
            exp = f" | expected: {entry['expected_outcome']}" if entry.get("expected_outcome") else ""
            print(f"     Outcome check-in scheduled: {entry['check_in_date']}{exp}")

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
    fin.add_argument("--receipt", default="", help=(
        "Verification receipt: one line naming what was verified, on which surface, "
        "by what instrument (with VERIFIED/LIKELY/UNCONFIRMED counts). Appended into "
        "--notes as a 'Verification:' declaration so Step 1.5 accountability is satisfied. "
        "Produced by the isolated verification subagent per directives/task-lifecycle-content.md."))
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
    fin.add_argument("--depth-receipt", default="", help="Path to depth-gate receipt JSON from `research_quality_gate.py validate --receipt`. Research-type finalizes without a PASSING receipt cap Factual Grounding at 6 (RECON-GRADE).")
    # Excellence Lift Wave 2 (added 2026-05-21)
    fin.add_argument("--anchor-named", nargs="?", const="", default="", metavar="PHRASE",
                     help="The rubric_v1.md anchor phrase your ≥8 score matches (e.g. \"Anchor 9 — expert would sign it unchanged\"). REQUIRED (non-empty) whenever any dimension score is ≥8 — finalize refuses otherwise. Bare --anchor-named (no phrase) no longer counts. Unanchored ≥8s used to slip through and get flattened to 7.25 by the bimodal taste filter (taste_signature.py Rule 2); now they refuse at input.")
    # Autopilot Wave 5 stabilization (added 2026-05-23)
    fin.add_argument("--source-request", default=None, help="Original user request verbatim. Used for the post-hoc routing check instead of the output description. Autopilot's Phase 4 template MUST pass this to prevent false positives on the autopilot_orchestration binding.")
    fin.add_argument("--verdict", default="", choices=["", "SHIP", "MARGINAL", "FAIL"],
                     help="Grading R1 (ADVISORY, GRADING-LOOP-REDESIGN.md): verdict-first grading. Logged + precedent-checked, never blocks in R1.")
    fin.add_argument("--precedent", default="", metavar="EVAL-ID",
                     help="Grading R1 (ADVISORY): nearest calibrated precedent in eval_set_v1.jsonl backing a SHIP verdict (e.g. EVAL-031). Validated: must exist, be calibrated_by_human, and sit within ±1.0 composite tolerance.")
    fin.add_argument("--content-file", default="", dest="content_file", help="Path to the ACTUAL deliverable. The prose + structural-tells caps scan THIS (not the summary), so slop with banned moves cannot finalize clean. Pass the artifact for every Content/Copy/Creative finalize.")
    # Finalize-friction cut (added 2026-07-06): --auto pre-computes the
    # deterministic dimensions (prose_classifier + grounding_guard — the same
    # modules _enforce_caps() runs internally) from --content-file and prints
    # them as a clearly-labeled preview BEFORE finalize runs. Does not change
    # required args or veto/cap logic — --intent/--expert-score/--adversarial
    # are still required from the caller either way; --auto only removes the
    # guesswork of not knowing in advance whether a cap will fire.
    fin.add_argument("--auto", action="store_true", help="Preview mode: print the already-computed prose_classifier/grounding_guard verdicts for --content-file before finalize applies the same caps. No-op without --content-file. Judgment scores (--intent/--expert-score/--adversarial) are still required.")
    # Outcome-loop closure (added 2026-06-12)
    fin.add_argument("--expected-outcome", default="", dest="expected_outcome", help="What success looks like for this deliverable (e.g. 'client signs', 'post >2k impressions'). Stored on the pending revenue stub so the check-in is concrete, not vibes.")
    fin.add_argument("--check-in", type=int, default=None, dest="check_in", help="Days until the outcome check-in for this deliverable (default 14). Surfaced by `revenue_tracker.py due` and the session staleness line when it arrives.")
    # Session-title pinning (added 2026-06-23): auto-pin the finalized session to the
    # handoff store so /resume surfaces it by name. Default ON for deliverable types;
    # the Stop-hook backstop catches anything that skips this path.
    fin.add_argument("--pin-session", dest="pin_session", action="store_true", default=None,
                     help="Pin this finalized session to the handoff store (/resume by name). Default ON for Content/Creative/Strategy.")
    fin.add_argument("--no-pin-session", dest="pin_session", action="store_false",
                     help="Skip the session pin for this finalize.")
    fin.add_argument("--pin-thread", default="", help="Thread slug for the session pin (default: --project, else --workflow). Pass explicitly to avoid splitting the /resume menu.")
    fin.add_argument("--pin-status", default="active", help="Handoff status for the pin: active|blocked|ready|mid-build|done. Default active.")
    fin.set_defaults(pin_session=None)
    # Learning-debt latch (Solution Recorder, added 2026-07-07)
    fin.add_argument("--learning", default="", dest="learning_path", help="Path to a saved Solution Card that clears open learning_debt on the newest session ledger.")
    fin.add_argument("--skip-learning", action="store_true", help="Proceed despite open learning_debt. Logged to evolution_store/learning_latch_overrides.jsonl for audit — use sparingly.")

    # Harness Apex Wave 2 (2026-07-09): extraction blind-pass latch override.
    fin.add_argument("--skip-blind-pass", action="store_true",
                     help="Finalize --type Extraction without a recorded blind_pass.py verdict. Logged to evolution_store/blind_pass_overrides.jsonl for audit (compass-not-cage). Prefer running the ritual: blind_pass.py prepare → side-by-side judgment → blind_pass.py record.")

    args = parser.parse_args()

    if args.command == "finalize":
        _content_path = getattr(args, "content_file", "") or args.anchor_path or ""
        if args.auto:
            _print_auto_preview(_content_path, args.type)
        # --receipt (2026-07-21 ladder-audit build): fold the verification receipt
        # into --notes so Step 1.5's existing 'verification:' sniff stays the single
        # source of truth. Purely additive; finalize() signature untouched.
        if args.receipt:
            if "verification:" in (args.notes or "").lower():
                args.notes = f"{args.notes} | Receipt: {args.receipt}"
            else:
                args.notes = (f"{args.notes} | " if args.notes else "") + \
                    f"Verification: PASS | Receipt: {args.receipt}"
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
            content_path=_content_path,
            expected_outcome=args.expected_outcome,
            check_in_days=args.check_in,
            depth_receipt=args.depth_receipt,
            learning_path=args.learning_path,
            skip_learning=args.skip_learning,
            skip_blind_pass=args.skip_blind_pass,
        )
        if args.receipt:
            try:
                result.setdefault("verification_check", {})["receipt"] = args.receipt
            except Exception:
                pass
        # ── Grading R1 (ADVISORY — GRADING-LOOP-REDESIGN.md, never blocks) ──
        if args.verdict or args.precedent:
            adv = check_verdict_advisory(args.verdict, args.precedent, result.get("composite"))
            result["verdict_advisory"] = adv
            try:
                _vlog = Path(__file__).resolve().parent.parent / "evolution_store" / "verdict_advisory.jsonl"
                with open(_vlog, "a") as _vf:
                    _vf.write(json.dumps({
                        "ts": datetime.now().isoformat(), "output": args.output[:120],
                        "skill": args.skill, "verdict": args.verdict,
                        "precedent": args.precedent, **adv,
                    }) + "\n")
            except Exception:
                pass
            print(f"\n  Verdict (R1 advisory): {args.verdict or '—'} | precedent {args.precedent or '—'} → {adv.get('status')}"
                  + (f" — {adv['detail']}" if adv.get("detail") else ""))
        print_result(result)
        # Wave 2 latches must be shell-visible: refusal = non-zero exit.
        if not result.get("success"):
            sys.exit(1)
        _do_pin = args.pin_session
        if _do_pin is None:
            _do_pin = args.type in ("Content", "Creative", "Strategy")
        if _do_pin and result.get("success"):
            _pin_session_from_finalize(
                args.output, workflow=args.workflow, project=args.project,
                content_path=_content_path,
                thread=args.pin_thread, status=args.pin_status, task_type=args.type,
            )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
