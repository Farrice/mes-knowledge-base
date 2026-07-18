# Feedback Ratchet Protocol

> **Trigger**: After any significant expert-driven deliverable.
> **Purpose**: Close the feedback loop so skills compound, not merely accumulate.

---

## Core Principle

Every output is an experiment. Improvements ratchet upward. Regressions trigger review. The system can only get better or stay the same — never silently degrade.

---

## When to Log

Log after: workflow completion, strategy brief, content piece, research output, client deliverable, system improvement, creative asset.
**Do NOT log**: Trivial questions, follow-ups, file ops, debugging, routing decisions.

---

## How to Log

### Automated (Preferred)

```python
from execution.log_performance import log_output

log_output(
    output="[description]", agent="[agent]", skill="[skill]",
    workflow="[workflow]", task_type="[Content|Strategy|Extraction|Research|Client Work|System|Creative|Analysis]",
    quality_score=[1-10], intent_alignment=[1-10],
    expert_standard=[1-10], adversarial_resilience=[1-10],
    status="[Keep|Discard|Needs Improvement|Baseline]",
    notes="[what worked/didn't]",
)
```

### CLI

```bash
python execution/log_performance.py log "Brief description" --agent X --skill X --type X --quality 8 --status Keep --notes "Notes"
```

Manual: When user gives feedback, update User Rating on the most recent entry.

---

## Scoring: 9-10 Exceptional (publishable) | 7-8 Strong (minor polish) | 5-6 Adequate | 3-4 Weak (generic) | 1-2 Failed

Sub-scores (Intent Alignment, Expert Standard, Adversarial Resilience, + Factual Grounding when applicable) map to Quality Gate's 4-point check.

**Repo-wide finalize convention (E4/E5 sweep, 2026-07-02)**: scores are NEVER templated into workflow files — 45 workflows carried hardcoded `--intent 8/9` blocks, which made every run score identically and starved the ratchet of signal. All now read `[evidence-based]`. Derive each score from evidence at finalize time; any dimension ≥8 requires `--anchor-named` plus naming the matching `rubric_v1.md` anchor in notes (the 7.25 cap for unanchored ≥8s is deliberate and stays — `execution/taste_signature.py` Rule 2). Full discipline: `directives/embodiment-standard.md` § Scoring Discipline.

---

## Ratchet Mechanism

**Regression** (score >1.0 below rolling 10-output avg): Flag "Needs Improvement", note degraded dimension, review recent skill changes. 3+ pattern → trigger `/skill-evolution`.

**Improvement** (score >1.0 above avg): Note cause, check transferability, update Evolution Log.

**Evolution Reminder**: After 5+ expert outputs in a session → surface `/skill-evolution` prompt. Reminder, not gate.

---

## Status: Keep (met baseline) | Discard (abandon approach) | Needs Improvement (fixable) | Baseline (first output, establishes starting point)

## Baselines

```bash
python execution/log_performance.py baseline --skill [name]
python execution/log_performance.py baseline --agent [name]
python execution/log_performance.py check --skill [name] --score 5
```

---

## Quality Gate Integration

Quality Gate runs DURING output (silent check on all applicable dimensions — 4 when factual claims present, 3 for pure creative/strategic). Feedback Ratchet runs AFTER delivery (captures signal permanently). Gate = referee. Ratchet = scoreboard. When Factual Grounding fires, include in notes: confidence label counts (VERIFIED/LIKELY/UNCONFIRMED) and verification verdict (PASS/FAIL/PARTIAL).

## Notion DB: `31f49875a89781dbb599dee5e7961b5c` | Script: `execution/log_performance.py`

---

## Step-Level Telemetry (Kimi K2.6-Inspired)

Optional telemetry fields capture *process* signals alongside *quality* signals. Pair step counts with quality scores to identify cost/quality inflection points (where adding more steps stops improving output) and validate critical-path scheduling.

**Available fields** (all optional; pass via `chain_runner.py finalize` CLI or `finalize()` kwargs):

| Field | CLI flag | What it measures |
|---|---|---|
| `tool_calls` | `--tool-calls N` | Count of tool invocations in the session |
| `file_reads` | `--file-reads N` | Count of Read tool calls (subset of tool_calls; high file-reads without matching quality gain = context bloat signal) |
| `sub_agents_spawned` | `--sub-agents N` | Count of Agent tool invocations (sub-agent spawns) |
| `session_duration_seconds` | `--duration S` | Wall-clock session duration |
| `critical_path_depth` | `--critical-path K` | For JCC Campaign/Full Deploy: longest sequential workstream chain (from mission-decomposer) |

**Example:**
```bash
python3 execution/chain_runner.py finalize "Parallax edition 03" \
    --expert lara-acosta --skill lara-acosta-linkedin --workflow ghostwrite \
    --type Content --intent 8 --expert-score 8 --adversarial 7 \
    --tool-calls 23 --file-reads 9 --sub-agents 3 --duration 1420 \
    --notes "strong hook, weak close | Factual Grounding: N/A"
```

**Persistence**: Telemetry appears in three places:
1. `result["telemetry"]` dict returned by `finalize()`
2. Appended to `notes` field in Notion Performance Log (no schema change required)
3. `context.telemetry` in evolution_store v2 traces (queryable by evolution engine)

**Interpretation rules**:
- **Rising tool_calls without quality gain** → investigate context bloat or ineffective workflow
- **Rising sub_agents_spawned without quality gain** → sub-agent delegation isn't compounding; consider Solo at higher Tier
- **Falling critical_path_depth on Campaign/Full Deploy missions over time** → decomposition is maturing (good)
- **Critical_path / workstream_count ≥ 0.7** → parallelism is ineffective; scale down

**Use this data** when running `/skill-evolution` to identify which skills are becoming step-efficient vs. step-bloated.

---

## Ground Truth Calibration

Run ground truth comparison when: skill evolution produces new variant, Expert Standard plateaus at 7-8, monthly for top 5 revenue skills, 10+ consecutive "Keep" entries.

```bash
python execution/ground_truth.py gap-report
python execution/ground_truth.py compare <domain> <path-to-ai-output>
python execution/ground_truth.py reveal <comparison-filename>
```

Revenue tracking: `python execution/revenue_tracker.py log "deliverable" --revenue <$> --outcome "what happened"`

Prose classifier integrated into `chain_runner.py finalize()` — auto-warns on banned AI vocab, uniform rhythm, inflated Expert Standard. Manual: `python execution/prose_classifier.py check <file>`

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-07-18 (chain_runner finalize for fleet-conductor-doctrine) |
| **Activation Count** | 661 |

**Phase 2**: PRIMED, not cycling (corrected 2026-07-02 audit — the 2026-03-30 run was a one-off, not a loop). Candidates via `skill_evolution_candidates.py scan`; run `/skill-evolution <candidate>` after the E3 bake-off calibrates the eval set.
**Phase 3**: PAUSED — concrete unlock in `.agent/evolution-paused.json`: eval set ≥15 human-calibrated entries + one Phase 2 cycle on a calibrated candidate. (The 2026-03-30 cross-pollination was a one-off predating the rubric pause.)
**Phase 4**: 🔒 LOCKED. Requires 3+ recurring gaps in `.agent/gap-log.md` — gap entries now auto-append via `skill_router_hook.py` (2026-07-02), so this can actually unlock.

*Created: 2026-03-10 | Compressed: 2026-04-13*
