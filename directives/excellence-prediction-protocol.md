# Excellence Prediction Protocol

**Status:** Active (Wave 3 / 2026-05-21)
**Owner module:** [`execution/excellence_predictor.py`](../execution/excellence_predictor.py)
**Auto-fires from:** [`execution/chain_runner.py finalize()`](../execution/chain_runner.py) (grade-inflation detector) and [`.agent/workflows/autopilot.md`](../.agent/workflows/autopilot.md) Phase 0 (pre-flight prediction).

## Purpose

The system used to discover iteration requirements at finalize time — too late to budget effort. This protocol moves the iteration decision UPSTREAM: before execution, predict the expected composite, name the high-risk dimensions, front-load interventions that historically lift those dimensions. Result: 9/10 first-pass instead of iterate-to-7.

The 2026-04-24 audit found 94-99% of finalize scores were 8+ while real iteration counts were 2-3 passes. The system was scoring excellent while requiring extra passes. Wave 1 (runtime caps) + Wave 2 (bimodal taste filter) collapse that inflated distribution. Wave 3 closes the loop by predicting iteration count before the work starts.

## Two operations

### 1. `predict()` — pre-flight prediction (fires from /autopilot)

Called by `.agent/workflows/autopilot.md` Phase 0 after intent_to_package resolves the mission package. Receives:

- `task_class` — task_type from the chain (Content / Strategy / Research / Creative / etc.)
- `expert` — expert agent name
- `skill` — skill directory name
- `workflow` — workflow name
- `complexity_signals` — dict with optional `output_length_estimate`, `factual_surface`, `multi_expert`, `identity_resistant`

Returns `PredictionResult` containing:

- `predicted_composite` (float)
- `predicted_iterations_to_target` (int: 1, 2, or 3+)
- `high_risk_dimensions` (list of dims whose historical median is <7)
- `confidence` (0.0-1.0; based on bucket sample size)
- `recommended_interventions` (specific actions to take BEFORE execution)
- `reasoning`, `sample_size`, `bucket_used`, `median_dims`

### 2. `detect_grade_inflation()` — rolling-window drift detector (fires from finalize)

Called automatically inside `chain_runner.finalize()` after the quality gate computes. Examines the last 10 traces in `evolution_store/v2_traces/`. If >80% of them have composite ≥8, attaches `result["calibration_drift_warning"]` with the distribution stats.

Wave 1+2 caps usually keep this detector silent. If it fires, it's a signal that either:
- The caps stopped working (verify with synthetic test)
- Scores are still inflated despite caps (anchor_named flag being set without evidence — audit the last 5 finalizes)
- The user's taste signature has genuinely shifted (rare; would warrant a rubric review)

## Routing decisions /autopilot makes from `PredictionResult`

| Condition | Action |
|---|---|
| `predicted_iterations == 1` AND `predicted_composite ≥ 8.5` | Proceed straight to execution. Expect one-pass excellence. |
| `predicted_iterations == 2` | Auto-front-load `/adversarial-review` after first draft. Build it into the workflow before the user sees output. |
| `predicted_iterations >= 3` | Require `/writers-room` before any production. Escalate to genius.md tier 2 loading. Spend the cycles upfront. |
| `high_risk_dimensions` includes `expert_standard` | Load `skills/<skill>/genius.md` at session start (tier 2 instead of tier 1). |
| `high_risk_dimensions` includes `adversarial_resilience` | Spawn an adversarial sub-agent per `directives/sub_agent_protocol.md`. |
| `high_risk_dimensions` includes `intent_alignment` | Run `/validate-intent` before drafting. |
| `complexity_signals.factual_surface` is True OR `factual_grounding` historically low | Activate `directives/verification-agent-protocol.md` upfront, not at Step 5.5. |
| `confidence < 0.3` (fewer than 3 matching traces) | Exploration mode — log the prediction but don't gate on it. Build the bucket. |

## Why predictions can be trusted

The training signal is the existing `evolution_store/v2_traces/` corpus (159 files at time of writing, growing per finalize call). No model training — just bucketed medians with confidence proportional to sample size. The algorithm walks bucket specificity from 3 (exact expert+skill+workflow match) down to 0 (global), picks the tightest bucket with ≥3 samples.

If a skill has never been used: prediction returns `confidence=0.0`, exploration mode flag, default composite 7.0 / 2 iterations. The next finalize compounds the bucket.

## Side effect: predictions persist for delta tracking

Every `predict()` call writes a JSON to `evolution_store/predictions/<timestamp>_<skill>.json`. After the work finalizes, a future tool can compute `actual_composite - predicted_composite` for each pair. If the mean absolute error (MAE) of predictions consistently exceeds 1.0 point, the predictor needs retuning (likely: tighten bucket selection or weight recent traces more heavily).

This is the calibration training signal — the predictor improves as the trace corpus grows. Karpathy-style: every measurement compounds.

## When to invoke this protocol manually

You don't need to. `chain_runner.finalize` calls `detect_grade_inflation` on every run. `.agent/workflows/autopilot.md` Phase 0 calls `predict` on every run. The protocol is invisible infrastructure — it fires automatically.

Manual invocation is useful only for inspection:

```bash
# What does the predictor think about a hypothetical task?
python3 execution/excellence_predictor.py predict \
    --task-class Content \
    --expert lara-acosta \
    --skill lara-acosta-linkedin-ghostwriting \
    --workflow high-dwell \
    --signals '{"output_length_estimate": 1500, "factual_surface": false}'

# Has grade inflation crept back in?
python3 execution/excellence_predictor.py detect-inflation --window 10
```

## Cross-references

- `evolution_store/ground_truth/rubric_v1.md` — the calibrated rubric (advisory until 15+ eval entries) + Bimodal Taste Profile (active Wave 2 enforcement)
- `directives/quality_gate.md` — the four hard rules (Wave 1+2 enforce them at runtime)
- `directives/feedback-ratchet.md` — the broader autoresearch loop this prediction layer plugs into
- `directives/sub_agent_protocol.md` — how to spawn the adversarial sub-agent that the predictor recommends
- `directives/verification-agent-protocol.md` — what to run when `factual_surface` is True
- `memory/feedback_auto-evolution-cant-substitute-for-ground-truth.md` — the discipline this protocol respects: don't auto-modify the rubric itself

## Known limitations

1. **Cold start**: skills with <3 traces produce `confidence < 0.3`. Exploration mode logs the prediction but doesn't drive routing decisions. Buckets fill as work compounds.
2. **No content awareness**: predictions are based on (expert, skill, workflow, task_type) only. Two different drafts from the same workflow get the same prediction. Future iteration: incorporate `complexity_signals.output_length_estimate` and `factual_surface` more heavily.
3. **Schema drift**: relies on the v2 trace shape (`quality.composite`, `expert`, `workflow`, `component`). If trace schema changes, update `_trace_quality()` in `excellence_predictor.py`.
4. **Anchor-named honesty**: the predictor sees post-Wave-2 enforced scores. If Claude routinely sets `anchor_named=True` without naming the anchor in finalize notes, the predictor will be trained on inflated data. Safeguard: the grade-inflation detector remains as a backstop — if it ever fires post-Wave-2, the anchor honesty pattern has likely broken.
