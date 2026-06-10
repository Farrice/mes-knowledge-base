---
description: Weekly outer-loop closure — evolution, revenue outcomes, calibration, core drift (~20 min)
tier: system
---

# /weekly-closeout — The Outer-Loop Ritual

Closes the loops that otherwise go stale: evolution cycles, revenue outcome tracking, calibration drift, and Production Core drift. Designed so the deterministic staleness hook (`session_ledger_hook.py prompt`) PROMPTS this — Farrice never has to remember it.

**Cadence**: weekly (Friday, or Monday before `/weekly-pulse`). ~20 minutes. Surfaces only judgment calls; everything mechanical runs automatically.

## Steps

### 1. Evolution catch-up (~1 min, automatic)

```bash
// turbo
python3 execution/evolution_orchestrator.py auto
python3 execution/evolution_orchestrator.py status
```

Report what ran (daily/weekly/monthly) in one line. (The launchd agent `com.antigravity.evolution-auto` also runs this daily at 07:00 — this step is the catch-up + visibility pass.)

### 2. Revenue outcome drain (~10 min, 5 questions max)

```bash
// turbo
python3 execution/revenue_tracker.py pipeline
```

Present the **5 OLDEST** pending deliverables, one at a time, each with exactly one question:

> "**[deliverable]** (delivered [date], composite [score]) — revenue, dead, or still pending?"

- **Revenue N** → `python3 execution/revenue_tracker.py log "<deliverable>" --revenue N --outcome "<what happened>"`
- **Dead** → log with `--revenue 0 --outcome "dead: <reason>"` — draining the queue honestly beats a fantasy pipeline
- **Still pending** → skip, it resurfaces next week

Never present more than 5. The queue drains at ~5/week; that's the design.

### 3. Calibration drift (~2 min, show only if firing)

```bash
// turbo
python3 execution/eval_harness.py calibrate --days 7
```

If the inflation guardrail fires (scores clustering 8+), show the flag and the worst offender. Otherwise: one line, "calibration clean."

### 4. Evolution queue (~3 min, one decision)

```bash
// turbo
python3 execution/evolution_orchestrator.py queue
```

Present the TOP queued item only. Accept → execute it. Reject → log why. Empty queue → skip silently.

### 5. Monthly only (first closeout of each month, ~5 min)

```bash
// turbo
python3 execution/skill_auditor.py audit
python3 execution/forge_gate.py status
```

- **CORE DRIFT**: read the section in the new audit report. Any core entry trace-less 2 consecutive months → propose demotion from `PRODUCTION_CORE.md` + `.agent/production-core.json`. Any long-tail skill with 3+ traces → propose promotion.
- **REVIEW-tier pass**: present up to 5 REVIEW-tier skills for archive judgment (`skill_auditor.py archive --tier REVIEW --names <approved> --annotate --apply`).
- **Forge gate**: report the last extraction's production-use count (X/3).

### 6. Close

One-paragraph summary: what closed, what drained, what drifted. Then:

```bash
python3 execution/chain_runner.py finalize "Weekly closeout <date>" \
    --expert system --skill system --workflow weekly-closeout \
    --type System --intent 9 --expert-score 8 --adversarial 8 \
    --notes "outcomes drained: N | calibration: clean/flagged | queue: accepted/rejected | Factual Grounding: N/A | Verification: N/A"
```

## Anti-patterns

- Batching 20 revenue questions into one session (drains trust, not the queue) — 5 max.
- Skipping the "dead" option — pendings that will never pay are noise, kill them.
- Running this without presenting judgment calls to Farrice — the whole point is the human closes the loop.
