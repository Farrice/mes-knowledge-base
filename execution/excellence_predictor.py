#!/usr/bin/env python3
"""
Excellence Predictor — Pre-flight prediction + grade-inflation detection
(Excellence Lift Wave 3 / 2026-05-21).

Purpose: today the system discovers iteration requirements AT finalize
time — too late to budget effort. This module predicts, BEFORE execution
starts, what composite a task is likely to reach and how many iterations
it will need. The /autopilot dispatcher uses these predictions to
front-load high-leverage interventions (genius.md tier 2 loading,
adversarial-review, verification) instead of discovering them after.

Training signal: every trace in `evolution_store/v2_traces/*.json`. Each
trace records expert, workflow/component, and post-enforcement composite
scores. No ML — just bucketed medians with confidence proportional to
sample size.

Two public functions:
    predict(task_class, expert, skill, workflow, complexity_signals)
        → PredictionResult with predicted_composite, predicted_iterations,
          high_risk_dimensions, confidence, recommended_interventions.

    detect_grade_inflation(window=10, threshold=0.80)
        → Optional dict if last N traces show >threshold fraction of
          composites ≥8 — surfaces calibration drift.

Side effect: predict() writes a JSON to evolution_store/predictions/ so
the post-hoc actual-vs-predicted delta becomes its own training signal.

CLI:
    python3 execution/excellence_predictor.py predict --task-class Content \\
        --expert lara-acosta --skill lara-acosta-linkedin-ghostwriting \\
        --workflow high-dwell --signals '{"output_length_estimate": 1500}'

    python3 execution/excellence_predictor.py detect-inflation --window 10
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

TRACE_DIR = Path(__file__).parent.parent / "evolution_store" / "v2_traces"
PREDICTIONS_DIR = Path(__file__).parent.parent / "evolution_store" / "predictions"

# Thresholds (advisory; tune from data)
_HIGH_CONFIDENCE_SAMPLE = 10            # >= this many bucket samples → confidence 1.0
_MIN_CONFIDENCE_SAMPLE = 3              # < this → exploration mode (confidence <0.3)
_HIGH_RISK_DIM_FLOOR = 7.0              # any dim's median below this = high-risk
_ITERATION_1_PASS_COMPOSITE = 8.5       # ≥ this median → one-pass excellence likely
_ITERATION_2_COMPOSITE = 7.5            # in this range → 2 iterations likely
_INFLATION_DETECT_THRESHOLD = 0.80      # >this fraction of 8+ in window = drift


@dataclass
class PredictionResult:
    predicted_composite: float
    predicted_iterations_to_target: int
    high_risk_dimensions: List[str] = field(default_factory=list)
    confidence: float = 0.0
    recommended_interventions: List[str] = field(default_factory=list)
    reasoning: str = ""
    sample_size: int = 0
    bucket_used: str = ""               # which bucket key matched
    median_dims: Dict[str, float] = field(default_factory=dict)


def _load_traces() -> List[Dict[str, Any]]:
    """Load all v2 traces from disk. Tolerant of malformed JSON."""
    if not TRACE_DIR.exists():
        return []
    traces = []
    for path in TRACE_DIR.glob("trace_*.json"):
        try:
            traces.append(json.loads(path.read_text()))
        except Exception:
            continue
    return traces


def _trace_quality(t: Dict[str, Any]) -> Optional[Dict[str, float]]:
    """Extract quality scores from a trace; None if incomplete."""
    q = t.get("quality") or {}
    if not q or "composite" not in q:
        return None
    return {
        "composite": float(q.get("composite", 0)),
        "intent_alignment": float(q.get("intent_alignment", 0)),
        "expert_standard": float(q.get("expert_standard", 0)),
        "adversarial_resilience": float(q.get("adversarial_resilience", 0)),
    }


def _bucket_match(
    trace: Dict[str, Any],
    expert: str,
    skill: str,
    workflow: str,
) -> int:
    """Score how well a trace matches the (expert, skill, workflow) bucket.

    Returns specificity score: 3 = all three match, 2 = expert+one other,
    1 = single match, 0 = no match. Used to pick the tightest bucket with
    enough samples.
    """
    score = 0
    t_expert = (trace.get("expert") or "").lower()
    t_workflow = (trace.get("workflow") or "").lower()
    t_skill = (trace.get("component") or "").lower()  # skill is stored as component
    if expert and t_expert == expert.lower():
        score += 1
    if workflow and t_workflow == workflow.lower():
        score += 1
    if skill and t_skill == skill.lower():
        score += 1
    return score


def _select_bucket(
    traces: List[Dict[str, Any]],
    expert: str,
    skill: str,
    workflow: str,
) -> Tuple[List[Dict[str, Any]], str]:
    """Pick the tightest bucket with enough samples.

    Walk specificity from 3 → 0 and return the first level that has at
    least _MIN_CONFIDENCE_SAMPLE traces, OR the widest bucket if no level
    qualifies. Returns (bucket_traces, bucket_label).
    """
    by_score: Dict[int, List[Dict[str, Any]]] = {3: [], 2: [], 1: [], 0: []}
    for t in traces:
        s = _bucket_match(t, expert, skill, workflow)
        by_score[s].append(t)

    # Tightest-with-enough wins
    for level in (3, 2, 1):
        if len(by_score[level]) >= _MIN_CONFIDENCE_SAMPLE:
            label_parts = []
            if level >= 1 and expert:
                label_parts.append(f"expert={expert}")
            if level >= 2 and (skill or workflow):
                label_parts.append(f"skill/workflow match")
            return by_score[level], ", ".join(label_parts) or f"specificity={level}"

    # Fallback: any traces at all (low confidence, but better than nothing)
    all_traces = by_score[3] + by_score[2] + by_score[1] + by_score[0]
    return all_traces, "global (low specificity)"


def predict(
    task_class: str,
    expert: str,
    skill: str,
    workflow: str,
    complexity_signals: Optional[Dict[str, Any]] = None,
) -> PredictionResult:
    """Predict expected composite and iteration count for an upcoming task.

    Args:
        task_class: task_type (Content / Strategy / Research / etc.)
        expert: expert agent name (e.g., "lara-acosta")
        skill: skill directory name
        workflow: workflow name
        complexity_signals: free-form dict with optional keys:
            output_length_estimate (int), factual_surface (bool),
            multi_expert (bool), identity_resistant (bool)

    Returns:
        PredictionResult with prediction + recommended interventions.
    """
    complexity_signals = complexity_signals or {}
    traces = _load_traces()

    if not traces:
        return PredictionResult(
            predicted_composite=7.0,
            predicted_iterations_to_target=2,
            confidence=0.0,
            recommended_interventions=["no_training_data — exploration mode"],
            reasoning="No traces in evolution_store/v2_traces/. Exploration mode.",
            sample_size=0,
            bucket_used="empty",
        )

    bucket, bucket_label = _select_bucket(traces, expert, skill, workflow)
    qualities = [q for q in (_trace_quality(t) for t in bucket) if q is not None]

    if not qualities:
        return PredictionResult(
            predicted_composite=7.0,
            predicted_iterations_to_target=2,
            confidence=0.0,
            recommended_interventions=["no_quality_data — exploration mode"],
            reasoning=f"Bucket '{bucket_label}' has {len(bucket)} traces but none with quality scores.",
            sample_size=0,
            bucket_used=bucket_label,
        )

    median_composite = statistics.median(q["composite"] for q in qualities)
    median_dims = {
        "intent_alignment": statistics.median(q["intent_alignment"] for q in qualities),
        "expert_standard": statistics.median(q["expert_standard"] for q in qualities),
        "adversarial_resilience": statistics.median(q["adversarial_resilience"] for q in qualities),
    }

    confidence = min(1.0, len(qualities) / _HIGH_CONFIDENCE_SAMPLE)

    # High-risk dims: those whose historical median is below floor.
    high_risk = [name for name, val in median_dims.items() if val < _HIGH_RISK_DIM_FLOOR]

    # Iteration estimate from median composite.
    if median_composite >= _ITERATION_1_PASS_COMPOSITE:
        iterations = 1
    elif median_composite >= _ITERATION_2_COMPOSITE:
        iterations = 2
    else:
        iterations = 3

    # Adjust iterations up if complexity signals indicate harder work.
    if complexity_signals.get("multi_expert"):
        iterations = max(iterations, 2)
    if complexity_signals.get("factual_surface"):
        iterations = max(iterations, 2)
    if complexity_signals.get("identity_resistant"):
        iterations = max(iterations, 2)

    # Recommended interventions
    interventions: List[str] = []
    if iterations >= 2:
        interventions.append("front-load /adversarial-review after first draft")
    if iterations >= 3:
        interventions.append("require /writers-room before execution; escalate to genius.md tier 2")
    if "expert_standard" in high_risk:
        interventions.append(f"load skills/{skill}/genius.md at session start (tier 2)")
    if "adversarial_resilience" in high_risk:
        interventions.append("spawn adversarial sub-agent per sub_agent_protocol.md")
    if "intent_alignment" in high_risk:
        interventions.append("re-confirm intent via /validate-intent before drafting")
    if complexity_signals.get("factual_surface") or "factual_grounding" in high_risk:
        interventions.append("activate verification-agent-protocol upfront, not at Step 5.5")
    if confidence < 0.3:
        interventions.append("exploration mode — log prediction, do not gate on it")

    reasoning = (
        f"Bucket: {bucket_label}. N={len(qualities)} traces. "
        f"Median composite={median_composite:.2f}. "
        f"High-risk dims: {high_risk or 'none'}. "
        f"Complexity signals: {dict(complexity_signals)}"
    )

    result = PredictionResult(
        predicted_composite=round(median_composite, 2),
        predicted_iterations_to_target=iterations,
        high_risk_dimensions=high_risk,
        confidence=round(confidence, 2),
        recommended_interventions=interventions,
        reasoning=reasoning,
        sample_size=len(qualities),
        bucket_used=bucket_label,
        median_dims={k: round(v, 2) for k, v in median_dims.items()},
    )

    _write_prediction(task_class, expert, skill, workflow, result)
    return result


def _write_prediction(
    task_class: str,
    expert: str,
    skill: str,
    workflow: str,
    result: PredictionResult,
) -> None:
    """Persist the prediction so post-hoc delta can compound."""
    try:
        PREDICTIONS_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = PREDICTIONS_DIR / f"{ts}_{(skill or 'unknown')[:40]}.json"
        record = {
            "timestamp": datetime.now().isoformat(),
            "task_class": task_class,
            "expert": expert,
            "skill": skill,
            "workflow": workflow,
            "prediction": asdict(result),
        }
        path.write_text(json.dumps(record, indent=2))
    except Exception:
        pass  # Non-blocking — prediction storage is a nice-to-have


def detect_grade_inflation(
    window: int = 10,
    threshold: float = _INFLATION_DETECT_THRESHOLD,
) -> Optional[Dict[str, Any]]:
    """Detect calibration drift via window of recent finalize traces.

    If more than `threshold` fraction of the last `window` traces show
    composite ≥8, return a drift warning. Otherwise return None.

    Uses POST-enforcement composite (the actual logged value), so if
    Wave 1+2 caps are working, this should rarely fire post-Wave-2.
    """
    traces = _load_traces()
    if len(traces) < window:
        return None

    # Sort by timestamp descending; take most recent window.
    traces.sort(key=lambda t: t.get("timestamp", ""), reverse=True)
    recent = traces[:window]
    composites = [q["composite"] for q in (_trace_quality(t) for t in recent) if q]
    if not composites:
        return None

    above_8 = sum(1 for c in composites if c >= 8)
    pct_above_8 = above_8 / len(composites)

    if pct_above_8 < threshold:
        return None

    return {
        "drift_detected": True,
        "window": window,
        "samples_with_quality": len(composites),
        "above_8_count": above_8,
        "pct_above_8": round(pct_above_8, 3),
        "threshold": threshold,
        "median_composite": round(statistics.median(composites), 2),
        "recommendation": (
            "Calibration drift suspected — most recent traces cluster above 8. "
            "Spot-check the last 5 finalize calls against rubric_v1.md anchors. "
            "If scores are inflated, lower future scores or set anchor_named=False "
            "for any 8+ that can't cite a specific rubric anchor."
        ),
    }


# ─── CLI ────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Excellence Predictor")
    sub = parser.add_subparsers(dest="cmd")

    pred = sub.add_parser("predict", help="Predict composite + iterations for an upcoming task")
    pred.add_argument("--task-class", required=True)
    pred.add_argument("--expert", default="")
    pred.add_argument("--skill", default="")
    pred.add_argument("--workflow", default="")
    pred.add_argument("--signals", default="{}", help="JSON dict of complexity signals")
    pred.add_argument("--json", action="store_true")

    inf = sub.add_parser("detect-inflation", help="Check last N finalize traces for grade drift")
    inf.add_argument("--window", type=int, default=10)
    inf.add_argument("--threshold", type=float, default=_INFLATION_DETECT_THRESHOLD)

    args = parser.parse_args()

    if args.cmd == "predict":
        try:
            signals = json.loads(args.signals)
        except Exception:
            signals = {}
        result = predict(args.task_class, args.expert, args.skill, args.workflow, signals)
        if args.json:
            print(json.dumps(asdict(result), indent=2))
        else:
            print(f"\nPredicted composite:    {result.predicted_composite}")
            print(f"Predicted iterations:   {result.predicted_iterations_to_target}")
            print(f"Confidence:             {result.confidence}")
            print(f"Sample size:            {result.sample_size}")
            print(f"Bucket:                 {result.bucket_used}")
            print(f"High-risk dimensions:   {result.high_risk_dimensions or 'none'}")
            print(f"Median dims:            {result.median_dims}")
            print(f"\nReasoning: {result.reasoning}")
            if result.recommended_interventions:
                print(f"\nRecommended interventions:")
                for i in result.recommended_interventions:
                    print(f"  - {i}")
            print()
    elif args.cmd == "detect-inflation":
        drift = detect_grade_inflation(window=args.window, threshold=args.threshold)
        if drift:
            print(json.dumps(drift, indent=2))
        else:
            print(json.dumps({"drift_detected": False, "window": args.window}, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
