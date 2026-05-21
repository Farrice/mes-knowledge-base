#!/usr/bin/env python3
"""
Taste Signature — Bimodal calibration filter (Excellence Lift Wave 2 / 2026-05-21).

This module encodes Farrice's bimodal taste signature as a programmatic
filter that runs on top of the calibrated rubric. It is the second-tier
quality enforcement layer:

    raw scores (AI self-assessment)
        ↓
    _enforce_caps()  ← Wave 1: AI prose, copy calibration, factual veto
        ↓
    taste_signature.apply()  ← Wave 2: bimodal verdict, 8-must-be-earned
        ↓
    final composite + verdict

Why bimodal: Farrice's calibration signature (memory/user_taste-calibration-
signature.md) is clear PASS or clear FAIL with a narrow marginal band. The
system's pre-Wave-2 distribution was 94-99% above 8 — opposite shape.
Without this filter, the rubric's "8 must be earned" rule stays advisory
and grade inflation persists.

The five rules (encoded from memory/user_taste-calibration-signature.md and
directives/quality_gate.md):

    Rule 1 — Failure penalty (harsher on the failure side):
        Any dimension ≤6 incurs -1.0 on that dimension. Cost of false PASS
        ≫ cost of false FAIL; when in doubt, fail harder.

    Rule 2 — 8-must-be-earned:
        Any dimension ≥8 without anchor_named=True is capped at 7.5.
        Claude must name the rubric anchor to claim the 8.

    Rule 3 — Anti-cluster:
        All 3+ dimensions ≥8 simultaneously AND anchor not named AND
        prose_verdict != CLEAN → suspicious cluster. Cap composite at
        7.5, verdict=MARGINAL. Forces a regrade.

    Rule 4 — Bimodal verdict mapping:
        all dims ≥7 AND composite ≥7.5            → PASS
        composite in [7.0, 7.5)                    → MARGINAL (≈ FAIL)
        any dim ≤6 OR composite <7                 → FAIL

    Rule 5 — Factual veto override:
        Preserved even if upstream _enforce_caps didn't catch it
        (defense in depth). If factual_grounding is set and <6,
        force verdict=FAIL regardless of composite.

Usage:
    from execution.taste_signature import apply

    adjusted = apply(
        scores={"intent_alignment": 9, "expert_standard": 8, "adversarial_resilience": 8},
        anchor_named=False,
        prose_verdict="CLEAN",
        factual_grounding=None,
    )
    print(adjusted.composite)        # 7.5 (Rule 2 fired)
    print(adjusted.taste_verdict)    # "MARGINAL"
    print(adjusted.adjustments)      # audit trail
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any


@dataclass
class AdjustedScores:
    intent_alignment: float
    expert_standard: float
    adversarial_resilience: float
    factual_grounding: Optional[float]
    composite: float
    raw_composite: float
    taste_verdict: str            # "PASS" | "MARGINAL" | "FAIL"
    adjustments: List[Dict[str, Any]] = field(default_factory=list)


# ── Tunable thresholds (matched to rubric_v1.md bimodal profile) ──
_FAILURE_PENALTY_THRESHOLD = 6.0        # dims at or below this get -1.0
_FAILURE_PENALTY_AMOUNT = 1.0           # how much to subtract
_EARNED_8_THRESHOLD = 8.0               # ≥ this requires named anchor
_EARNED_8_CAP = 7.5                     # what it gets capped to
_ANTI_CLUSTER_DIM_THRESHOLD = 8.0       # all dims at/above triggers cluster check
_PASS_COMPOSITE_FLOOR = 7.5             # bimodal PASS threshold
_PASS_DIMENSION_FLOOR = 7.0             # every dim must clear this for PASS
_FAIL_DIMENSION_CEILING = 6.0           # any dim at/below this = FAIL
_FAIL_COMPOSITE_CEILING = 7.0           # composite below this = FAIL
_FACTUAL_VETO_FLOOR = 6.0               # factual_grounding below = FAIL


def apply(
    scores: Dict[str, float],
    anchor_named: bool = False,
    prose_verdict: str = "CLEAN",
    factual_grounding: Optional[float] = None,
) -> AdjustedScores:
    """Apply Farrice's bimodal taste filter on top of raw/capped scores.

    Args:
        scores: dict with at least the three required dimensions
            (intent_alignment, expert_standard, adversarial_resilience).
        anchor_named: True iff Claude named the rubric anchor for any
            score ≥8. If False and any dim ≥8, Rule 2 caps it at 7.5.
        prose_verdict: "CLEAN" | "WARNING" | "FLAGGED" | other. Used by
            Rule 3 anti-cluster check.
        factual_grounding: optional 4th dimension (1-10) or None for N/A.

    Returns:
        AdjustedScores with the post-filter dims, recomputed composite,
        bimodal taste verdict, and audit trail of every rule that fired.
    """
    intent = float(scores["intent_alignment"])
    expert = float(scores["expert_standard"])
    adv = float(scores["adversarial_resilience"])

    raw_composite = round((intent + expert + adv) / 3, 2)
    adjustments: List[Dict[str, Any]] = []

    # ── Rule 1: Failure penalty (harsher on failure side) ──
    # Apply -1.0 to any dimension at or below 6. Bimodal taste pushes
    # marginal failures further into the FAIL zone so they don't ship.
    for name, val in (
        ("intent_alignment", intent),
        ("expert_standard", expert),
        ("adversarial_resilience", adv),
    ):
        if val <= _FAILURE_PENALTY_THRESHOLD:
            new_val = max(1.0, val - _FAILURE_PENALTY_AMOUNT)
            adjustments.append({
                "rule": "failure_penalty",
                "dimension": name,
                "from": val,
                "to": new_val,
                "reason": (
                    f"dim ≤{_FAILURE_PENALTY_THRESHOLD} → -{_FAILURE_PENALTY_AMOUNT} "
                    "(harsh-on-failure bimodal signature)"
                ),
            })
            if name == "intent_alignment":
                intent = new_val
            elif name == "expert_standard":
                expert = new_val
            elif name == "adversarial_resilience":
                adv = new_val

    # ── Rule 2: 8-must-be-earned ──
    # Any dim ≥8 without anchor_named is capped at 7.5. Forces Claude to
    # cite the rubric anchor for any "excellent" claim.
    if not anchor_named:
        for name, val in (
            ("intent_alignment", intent),
            ("expert_standard", expert),
            ("adversarial_resilience", adv),
        ):
            if val >= _EARNED_8_THRESHOLD:
                adjustments.append({
                    "rule": "earned_8_cap",
                    "dimension": name,
                    "from": val,
                    "to": _EARNED_8_CAP,
                    "reason": (
                        f"dim ≥{_EARNED_8_THRESHOLD} without anchor_named=True → "
                        f"cap at {_EARNED_8_CAP} (8-must-be-earned rule)"
                    ),
                })
                if name == "intent_alignment":
                    intent = _EARNED_8_CAP
                elif name == "expert_standard":
                    expert = _EARNED_8_CAP
                elif name == "adversarial_resilience":
                    adv = _EARNED_8_CAP

    # Recompute composite after Rules 1+2
    composite = round((intent + expert + adv) / 3, 2)

    # ── Rule 3: Anti-cluster ──
    # If all dims ≥8 AND anchor not named AND prose not CLEAN, this is a
    # suspicious cluster. Cap composite at 7.5 and force MARGINAL verdict.
    # (Rule 2 will usually have already capped these, but check the pre-Rule-2
    # values for "what AI claimed" detection.)
    raw_intent = float(scores["intent_alignment"])
    raw_expert = float(scores["expert_standard"])
    raw_adv = float(scores["adversarial_resilience"])
    all_high = (
        raw_intent >= _ANTI_CLUSTER_DIM_THRESHOLD
        and raw_expert >= _ANTI_CLUSTER_DIM_THRESHOLD
        and raw_adv >= _ANTI_CLUSTER_DIM_THRESHOLD
    )
    cluster_suspicious = (
        all_high
        and not anchor_named
        and prose_verdict != "CLEAN"
    )
    if cluster_suspicious and composite > _EARNED_8_CAP:
        adjustments.append({
            "rule": "anti_cluster",
            "dimension": "composite",
            "from": composite,
            "to": _EARNED_8_CAP,
            "reason": (
                f"all dims ≥{_ANTI_CLUSTER_DIM_THRESHOLD} + anchor not named + "
                f"prose_verdict={prose_verdict} → suspicious cluster, cap composite"
            ),
        })
        composite = _EARNED_8_CAP

    # ── Rule 5: Factual veto override (check before verdict mapping) ──
    factual_veto_fires = (
        factual_grounding is not None
        and factual_grounding < _FACTUAL_VETO_FLOOR
    )

    # ── Rule 4: Bimodal verdict mapping ──
    if factual_veto_fires:
        verdict = "FAIL"
        adjustments.append({
            "rule": "factual_veto_override",
            "dimension": "verdict",
            "from": "computed",
            "to": "FAIL",
            "reason": (
                f"factual_grounding={factual_grounding} < {_FACTUAL_VETO_FLOOR} → "
                "FAIL regardless of composite (defense in depth)"
            ),
        })
    else:
        any_dim_low = (
            intent <= _FAIL_DIMENSION_CEILING
            or expert <= _FAIL_DIMENSION_CEILING
            or adv <= _FAIL_DIMENSION_CEILING
        )
        if any_dim_low or composite < _FAIL_COMPOSITE_CEILING:
            verdict = "FAIL"
        elif composite >= _PASS_COMPOSITE_FLOOR and all(
            d >= _PASS_DIMENSION_FLOOR for d in (intent, expert, adv)
        ):
            verdict = "PASS"
        else:
            verdict = "MARGINAL"

        # Anti-cluster forces MARGINAL even if PASS criteria met
        if cluster_suspicious and verdict == "PASS":
            verdict = "MARGINAL"
            adjustments.append({
                "rule": "anti_cluster_verdict_demote",
                "dimension": "verdict",
                "from": "PASS",
                "to": "MARGINAL",
                "reason": "anti-cluster check forces MARGINAL verdict",
            })

    return AdjustedScores(
        intent_alignment=intent,
        expert_standard=expert,
        adversarial_resilience=adv,
        factual_grounding=factual_grounding,
        composite=composite,
        raw_composite=raw_composite,
        taste_verdict=verdict,
        adjustments=adjustments,
    )


# ── CLI (manual inspection / debugging) ─────────────────────────
def main():
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Taste Signature — bimodal taste filter")
    parser.add_argument("--intent", type=float, required=True)
    parser.add_argument("--expert", type=float, required=True)
    parser.add_argument("--adversarial", type=float, required=True)
    parser.add_argument("--factual", type=float, default=None)
    parser.add_argument("--anchor-named", action="store_true")
    parser.add_argument("--prose-verdict", default="CLEAN")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = apply(
        scores={
            "intent_alignment": args.intent,
            "expert_standard": args.expert,
            "adversarial_resilience": args.adversarial,
        },
        anchor_named=args.anchor_named,
        prose_verdict=args.prose_verdict,
        factual_grounding=args.factual,
    )

    if args.json:
        print(json.dumps({
            "intent_alignment": result.intent_alignment,
            "expert_standard": result.expert_standard,
            "adversarial_resilience": result.adversarial_resilience,
            "factual_grounding": result.factual_grounding,
            "composite": result.composite,
            "raw_composite": result.raw_composite,
            "taste_verdict": result.taste_verdict,
            "adjustments": result.adjustments,
        }, indent=2))
    else:
        print(f"\nRaw composite:      {result.raw_composite}")
        print(f"Adjusted composite: {result.composite}")
        print(f"Dims (i/e/a):       {result.intent_alignment} / {result.expert_standard} / {result.adversarial_resilience}")
        print(f"Taste verdict:      {result.taste_verdict}")
        if result.adjustments:
            print(f"\nAdjustments ({len(result.adjustments)}):")
            for a in result.adjustments:
                print(f"  [{a['rule']}] {a['dimension']}: {a['from']} -> {a['to']}")
                print(f"     {a['reason']}")
        else:
            print("\nNo adjustments fired.")


if __name__ == "__main__":
    main()
