# Calibration Replay Results — Wave 1-2 Validation

**Date**: 2026-05-22
**Author**: Calibration replay session
**Source code under test**: `execution/chain_runner.py::_enforce_caps` + `execution/taste_signature.py::apply` (commit 82685da6, Wave 1-2)
**Trace window**: 20 most recent files in `evolution_store/v2_traces/` by mtime (2026-05-12 → 2026-05-22 09:19)
**Replay harness**: `.tmp/replay_calibration.py` (not committed)

> **Note on timing**: An earlier draft of this doc ran before four parallel-task finalize() calls (`research-swarm`, `lara-acosta-linkedin-ghostwriting`, `system-audit`, `atomize`) wrote new traces. This re-run includes those four — they replaced the four oldest traces in the prior window (`extract-forge 040155`, `oren-brand-archetypes`, and two older entries). Numbers shifted modestly; the structural findings did not.

---

## TL;DR Verdict

**Partial pass.** Two of three success criteria met, one failed in a way that reveals a real architectural artifact, not a tuning miss.

| Criterion | Target | Observed | Result |
|---|---|---|---|
| Mean composite drops 0.5-1.5 | -0.5 to -1.5 | **-0.50** | PASS (right at the floor) |
| ≥30% (6+) trip a cap | 30%+ | **75% (15/20)** | PASS (overshoots) |
| Bimodal distribution: clear PASS/FAIL clusters, thin 7.0-7.5 band | thin 7.0-7.5 | **70% (14/20) IN 7.0-7.5 band** | **FAIL** — opposite of bimodal |

The system aggressively caps high scores (good) and aggressively penalizes failures (good), but the two harshness mechanisms collide at exactly 7.50, producing a **MARGINAL plateau** where the bimodal mid-band was supposed to be thin.

---

## Comparison Table (20 traces, sorted by mtime desc)

| # | File | Task | Raw composite | New composite | Δ | Verdict | Caps fired | Rules |
|---|------|------|--------------:|--------------:|--:|---------|----------:|-------|
| 1 | trace_20260522_091955_research-swarm | Research | 7.17 | 7.17 | 0.00 | MARGINAL | 0 | — |
| 2 | trace_20260522_091711_lara-acosta-linkedin-ghostwriting | Content | 5.83 | 5.17 | **−0.66** | FAIL | 2 | failure_penalty ×2 |
| 3 | trace_20260522_091637_system-audit | System | 7.17 | 7.17 | 0.00 | MARGINAL | 0 | — |
| 4 | trace_20260522_091557_atomize | Content | 5.00 | 4.33 | **−0.67** | FAIL | 2 | failure_penalty ×2 |
| 5 | trace_20260522_091419_writers-room | Content | 5.83 | 5.17 | **−0.66** | FAIL | 2 | failure_penalty ×2 |
| 6 | trace_20260522_081942_vince-nijhof-dtc-operator-system | Strategy | 7.50 | 7.50 | 0.00 | **PASS** | 0 | — |
| 7 | trace_20260522_081253_linkedin-post-production | Content | 7.50 | 7.50 | 0.00 | **PASS** | 0 | — |
| 8 | trace_20260521_120512_research-landscape | Research | 7.67 | 7.33 | −0.34 | MARGINAL | 2 | earned_8_cap ×2 |
| 9 | trace_20260521_115858_test | Content | 8.00 | 7.50 | −0.50 | MARGINAL | 4 | earned_8_cap ×3 + anti_cluster_verdict_demote |
| 10 | trace_20260521_115539_test | Strategy | 8.00 | 7.50 | −0.50 | MARGINAL | 4 | earned_8_cap ×3 + anti_cluster_verdict_demote |
| 11 | trace_20260521_115538_test | Content | 7.33 | 7.33 | 0.00 | MARGINAL | 0 | — |
| 12 | trace_20260521_115536_test | Content | 6.67 | 6.33 | −0.34 | FAIL | 1 | failure_penalty |
| 13 | trace_20260521_115503_test | Content | 6.67 | 6.33 | −0.34 | FAIL | 1 | failure_penalty |
| 14 | trace_20260521_115124_test | Strategy | 8.00 | 7.50 | −0.50 | MARGINAL | 4 | earned_8_cap ×3 + anti_cluster_verdict_demote |
| 15 | trace_20260521_115056_test-skill | Content | 8.00 | 6.67 | **−1.33** | FAIL | 3 | failure_penalty + earned_8_cap ×2 |
| 16 | trace_20260521_093655_jen-santulan-listing-content | Client Work | 8.33 | 7.50 | −0.83 | MARGINAL | 4 | earned_8_cap ×3 + anti_cluster_verdict_demote |
| 17 | trace_20260520_213904_supercomputer | Creative | 7.67 | 7.33 | −0.34 | MARGINAL | 2 | earned_8_cap ×2 |
| 18 | trace_20260520_201348_brand-operating-system | Client Work | 9.00 | 7.50 | **−1.50** | MARGINAL | 4 | earned_8_cap ×3 + anti_cluster_verdict_demote |
| 19 | trace_20260520_190821_deep-research | Research | 8.67 | 7.50 | **−1.17** | MARGINAL | 4 | earned_8_cap ×3 + anti_cluster_verdict_demote |
| 20 | trace_20260512_043309_extract-forge | System | 7.67 | 7.33 | −0.34 | MARGINAL | 2 | earned_8_cap ×2 |

**Aggregates**
- Mean raw composite: **7.38**
- Mean new composite: **6.88** (Δ = **−0.50**)
- Caps fired on **15/20 (75%)** traces
- Verdict mix: **2 PASS / 12 MARGINAL / 6 FAIL**
- Largest single drop: **−1.50** (brand-operating-system, 9.00 → 7.50)
- 6 FAILs cluster in 4.33–6.67 (clean failure cluster, including the two newest organic FAILs at 4.33 and 5.17)
- 12 MARGINALs cluster in 7.0–7.5; **8 of those land at exactly 7.50**

---

## Distribution Buckets

| Bucket | Raw | New |
|---|---:|---:|
| < 6.0 | 3 | 3 |
| 6.0 – 6.4 | 0 | 2 |
| 6.5 – 6.9 | 2 | 1 |
| 7.0 – 7.4 | 3 | 6 |
| **7.5 exact** | 2 | **8** |
| 7.6 – 7.9 | 3 | 0 |
| 8.0+ | 7 | 0 |

The 8.0+ population (7 traces) and the 7.6–7.9 population (3 traces) **all** collapsed into 7.5 or 7.0–7.4. None survived in the "earned excellent" zone — because no historical trace had `anchor_named=True`.

---

## What the Four New Parallel-Task Traces Contributed

The 4 traces that landed during the parallel batch (09:15–09:19 on 2026-05-22) added an organic spread to the picture:

| Trace | Raw | Verdict after caps | Note |
|---|--:|---|---|
| `research-swarm` | 7.17 | MARGINAL (no caps) | Natural moderate self-score; no caps needed |
| `system-audit` | 7.17 | MARGINAL (no caps) | Natural moderate self-score; no caps needed |
| `lara-acosta-linkedin-ghostwriting` | 5.83 | FAIL (failure_penalty ×2) | Real content failure; harsh-on-failure rule did its job |
| `atomize` | 5.00 | FAIL (failure_penalty ×2) | Lowest composite in the full 20; clean FAIL classification |

Net effect on aggregates vs the pre-parallel-run draft: mean Δ slipped from −0.55 → −0.50 (the new FAILs have a smaller per-trace drop than the high-score MARGINALs they displaced, because `failure_penalty` is bounded by `max(1.0, val − 1.0)`); cap-trip rate slipped 85% → 75% (two of the new traces had zero caps fire on natural-moderate scores); FAIL count went 5 → 6. **The structural finding is unchanged**: high-score traces still pile at 7.50/MARGINAL.

---

## Per-Criterion Analysis

### Criterion 1: Mean drop 0.5–1.5 → PASS (at the floor)

Observed −0.50 sits exactly at the bottom of the target band. Two contributors keep the drop modest:

- **Five traces had no cap fire** (`research-swarm`, `system-audit`, `vince-nijhof`, `linkedin-post-production`, `test 115538`) because their raw dims were already at 7.5 or below 8 without tripping `failure_penalty`. They contribute Δ = 0.
- **Six traces had only `failure_penalty` fire** (already-failing items got harsher) and their drops are −0.34 to −0.67 each — small in absolute terms because the penalty is bounded by `max(1.0, val − 1.0)`.

The mean would have been more negative (closer to −1.0) if either (a) more of the 20 were in the 8.0+ zone (only 7 of 20 were), or (b) `ai_prose_cap` and `copy_calibration_cap` had fired at least once.

**They did not. Neither cap fired on any of the 20 traces.** See "Caps That Did Not Fire" below.

### Criterion 2: ≥30% trip a cap → PASS (massive overshoot)

75% (15/20) tripped at least one cap. Of those:

- `earned_8_cap` fired **24 times** across 10 traces (the workhorse rule).
- `anti_cluster_verdict_demote` fired **6 times** (one per trace whose all-3-dims were originally ≥8).
- `failure_penalty` fired **9 times** across 8 traces (some traces tripped it twice).
- `ai_prose_cap` (Wave 1 Cap 1): **0 times.**
- `copy_calibration_cap` (Wave 1 Cap 2): **0 times.**
- `factual_veto` (Wave 1 Cap 3): **0 times** (per spec we used factual=7 when absent).

The Wave-2 taste-signature rules are doing all the work. The Wave-1 caps mostly didn't fire.

### Criterion 3: Bimodal distribution → FAIL

Wave 2's success criterion was *"distribution becomes bimodal (clear PASS/FAIL clusters with thin 7.0-7.5 band)."* The observed distribution is the **opposite shape**:

- Clear FAIL cluster: 6 traces in 4.33 – 6.67. ✓ (this part worked)
- Clear PASS cluster: 2 traces, both at exactly 7.50. ✗
- Thin marginal band: 12 traces in 7.0 – 7.5, with **8 at exactly 7.50**. ✗

The mode of the entire new distribution is **7.50 exact**. That is the worst possible outcome for a bimodal-taste design — the "decision band" of MARGINAL is now the majority population.

Mechanism: `earned_8_cap` rewrites every ≥8 dim to **the same constant 7.5**. When all 3 raw dims were ≥8 (10 of 20 traces), the new composite is mathematically forced to be exactly 7.50, which then trips `anti_cluster_verdict_demote` (raw dims all ≥8 + anchor not named + `prose_verdict != "CLEAN"`) and downgrades from PASS to MARGINAL. The result is an 8-deep stack at 7.50/MARGINAL.

---

## Diagnostic — Why Two Caps Never Fired

> Diagnose, don't fix. Findings recorded for the next session.

### Finding 1: `ai_prose_cap` cannot fire on v2-trace replay (storage artifact)

`chain_runner._enforce_caps` requires `len(output_text) > 100` to call `should_cap_expert_standard`. All 20 traces passed that gate (15 are at the maximum 200, 5 are 42–94). But the prose classifier has an **internal** floor:

```python
# prose_classifier.should_cap_expert_standard, run manually on a 186-char output:
(False, {'reason': 'text_too_short', 'word_count': 36})
```

The classifier returns `verdict=NOT_RUN` (or its equivalent) for any text under ~37 words. The v2 trace writer at `chain_runner.py:755` truncates stored output to `output_description[:200]` — that's roughly 30–40 words for typical English prose. **Every replayed trace falls below the classifier's confidence floor.**

So this finding is not "the threshold is too lenient." It's a **storage truncation artifact** specific to replay: the classifier could not see enough of the original output to make a call. In live finalize() runs (where the full output is in memory), this cap will fire normally — we just can't validate it from historical traces.

Side-effect: because `prose_verdict` was `NOT_RUN` for all 20, the anti-cluster rule's `prose_verdict != "CLEAN"` check passed for every all-dims-≥8 trace. That contributed to the 6-fire count of `anti_cluster_verdict_demote`. If those outputs' prose had been judged CLEAN in a real finalize() call, several MARGINAL verdicts would have been PASS (composite 7.50, clean prose, all dims ≥ 7.0 → meets `_PASS_COMPOSITE_FLOOR=7.5`).

**Implication**: This replay systematically *over*-estimates how many real finalize calls land in MARGINAL. Live calls will pass the prose check more often → fewer anti-cluster demotions → cleaner bimodal shape than what we observed.

### Finding 2: `copy_calibration_cap` did not fire on Content-tagged traces

Eight traces had `task_type ∈ {Content, Creative, Client Work}` (all in `_COPY_TASK_TYPES`). None tripped `copy_calibration_cap`. Spot-checking the outputs:

- `trace_20260521_115858_test`: *"Send 3 cold emails per day. Track which ones get replies. After 30 days, you'll see 2-3 patterns in what works. Most agents I work with book 1-2 listing calls per week using this loop."* — names a concrete number (3, 30, 2-3, 1-2) and a result-verb (`book`). `_check_concrete_result` correctly passed this.
- `trace_20260522_091419_writers-room`: 200 chars of writers-room output, dims 5/6/7 (failure case). Likely also contains numbers from the rubric or skill metadata.

The detector is probably operating correctly — most expert outputs **do** name a number, even in their truncated 200-char prefix. The cap is intended to catch abstract benefit-claims ("visibility", "growth", "authority") that fail the concrete-result test, and those don't appear in the truncated trace prefixes either.

Same storage-truncation caveat as Finding 1: this replay can't fully validate Cap 2.

### Finding 3: The 7.50 MARGINAL plateau is structural, not a bug

The plateau is the deliberate emergent consequence of three rules composing:

1. `earned_8_cap` (Wave 2 Rule 2): every dim ≥8 → 7.5 *constant*.
2. Composite arithmetic: (7.5 + 7.5 + 7.5) / 3 = 7.50 *exactly*.
3. `anti_cluster_verdict_demote` (Wave 2 Rule 3): if raw dims were all ≥8 and anchor not named, PASS → MARGINAL.

Until Claude starts naming rubric anchors when scoring high (`anchor_named=True`), every "originally excellent" output is destined for the 7.50 MARGINAL pile. The bimodal shape only emerges in a future regime where (a) Claude regularly names anchors, lifting excellent work to composite ≥8, OR (b) the `earned_8_cap` value is differentiated (e.g., cap-to-7.5 for one cap fire, cap-to-7.0 for two, cap-to-6.5 for three) so cluster-cap traces drop into the FAIL zone instead of pooling at 7.5.

**This is the architectural finding worth carrying forward.** The Wave-1/2 design is internally consistent and behaviorally aggressive, but it does not produce a bimodal distribution from historical un-anchored traces. The pre-condition for bimodality is anchor-naming discipline going forward.

### Finding 4: The "94-99% scored 8+" baseline in CLAUDE.md is not what these 20 show

CLAUDE.md cites a 2026-04-24 calibration finding that 94-99% of recent finalize scores were 8+. The 20 most recent traces show a raw mean of **7.38** with only 7 of 20 (35%) at composite 8+. Possible explanations:

- The 94-99% figure is per-dimension, not per-composite. The 20 traces have raw composites averaging 7.38, but individual dimensions cluster higher.
- The autopilot test session on 2026-05-21 wrote 7 traces with deliberately moderate self-grades (7.0-8.0) to test the pipeline — these pull the mean down.
- The parallel-batch finalize calls on 2026-05-22 09:19 included two organic FAILs (composite 5.00 and 5.83) and two natural-MODERATE traces (composite 7.17 each) — recent finalize discipline may already be tightening.
- The 04-24 measurement window is older than the most recent 20 traces; some grade-deflation may already have started in the 04-25 → 05-22 window.

Worth a separate eval_harness run with a longer window (e.g., 90 days) to compare.

---

## What This Replay Cannot Tell You

- Whether `ai_prose_cap` works on real-length outputs (truncation artifact).
- Whether `copy_calibration_cap` works on real-length outputs (same).
- Whether prose verdicts would be CLEAN often enough to suppress `anti_cluster_verdict_demote` (also blocked by truncation).
- Whether `factual_veto` works (we used factual=7 when absent per spec; no trace had a real factual_grounding < 6).
- Whether the bimodal shape would emerge with `anchor_named=True` discipline going forward.

A live shadow-mode finalize() over the next 20 real runs (with full output text and anchor-naming discipline) is the only way to validate those.

---

## Recommended Next Step (not in scope for this session)

Run a **shadow-mode validation**: for the next 20 live finalize() calls, capture the raw output in full *before* the 200-char truncation, then replay `_enforce_caps` on the full text to see whether `ai_prose_cap` and `copy_calibration_cap` actually fire and how that shifts the MARGINAL count. That removes the storage-truncation confound this replay could not work around.

If the shadow run still shows a 7.50 MARGINAL plateau with anchor-naming engaged, the architectural fix candidates are:

1. **Tiered `earned_8_cap` values** (cap to 7.5 / 7.0 / 6.5 depending on cluster severity), so the post-cap composite spreads instead of pooling at one number.
2. **Reverse the anti-cluster sequence**: demote *before* the earned_8_cap rewrite so the composite drops more decisively into FAIL territory.
3. **Make `anchor_named` checkable at finalize-time** via grep over the user's notes for explicit anchor references — reduces dependence on Claude self-declaring it.

None of these are recommended yet — wait for shadow validation first.
