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

### 1.5. System Health Review (~3 min — absorbed /system-pulse + /maintenance, 2026-07-15)

```bash
// turbo
python3 execution/health_metrics.py flags --latest
python3 execution/protocol_tracker.py audit
python3 execution/log_performance.py baseline
```

- **Vitals + flags**: the daily collector (`launchd com.antigravity.health-metrics`, 06:15) already surfaced today's flags in the Morning Brief — here, review the **Sunday deep snapshot** (`.agent/health/<date>-deep.json`): dead-skill candidates, fully-stale `_active/` dirs, orphan verify scripts. Trend check when suspicious: `python3 execution/health_metrics.py trend --metric context_injection.total_bytes --days 60`.
- **Pending removals**: walk `.agent/health/pending-review.md` `status: pending` blocks with Farrice — approve/reject each (approved → execute the archive/prune, flip status; rejected → flip status, note why). **Nothing executes without his yes.**
- **Protocol + baseline**: flag zombie critical protocols (quality_gate, feedback-ratchet, session-state, intent-pipeline) and any skill regression >1.0 below rolling average (`python3 execution/gap_analysis.py recommendations` + `python3 execution/pattern_propagation.py scan` for evolution/cross-pollination candidates — feeds Step 4's queue decision).
- **Verifier fleet**: run `python3 execution/self_heal.py report` FIRST — it classifies every failing verifier as AUTO / EVIDENCE / JUDGMENT and groups them by root cause, so "12 failing" reads as the 2–3 decisions it actually is. Anything AUTO/EVIDENCE was already repaired at session close; **hand-triage only the JUDGMENT rows** (each carries a diagnosis and an exact command). Then `python3 execution/verify_fleet.py status` for the raw board. Failing verifiers are broken CONTRACTS, not noise: real drift → fix the system; stale expectation → fix or propose-archive via pending-review. Check `evolution_store/failure-registry.md` for anything marked CHRONIC — a fix that keeps failing is a standing decision, and retrying it is wasted work.
- **Loop self-check**: `python3 execution/health_metrics.py verify` — a dead health loop hides every other problem.
- **Wiring deep pass** (Model-Dialect Adaptation Layer, 2026-07-28): `python3 execution/wiring_audit.py drain --batch 400` then `status` — the weekly deeper sweep over the firing-path index (the daily 06:00 audit maintains ~150/day). ORPHAN assets are a wire-it-or-archive-it decision with Farrice; the audit itself never deletes or blocks. New orphans since last week = something shipped unwired — check `docs/solutions/2026-07-21-wired-but-never-loaded-prompts.md` before hand-wiring.

- **Org drift** (Global Org Sweep, 2026-07-28): `python3 execution/projects_index.py check` — contradictions only, never a list of unstamped projects. Four kinds: a project stamped `active` but cold >45d, stamped `done` but touched <14d, a project with **no entry point** (`missing_index`), and a **dual-taxonomy** collision (two sibling dirs on one canonical prefix, e.g. `03-content` + `03-launch`). Fix for the first three is a `status:` stamp in that project's own `INDEX.md`; the fourth is a filing decision. Also listed: files the session-close sweep **deferred** for judgment — file them with `project_filer.py plan --project "<abs dir>"`. The daily 06:00 job already regenerated `PROJECTS.md`; nothing here blocks.

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
- **Extraction telemetry** (informational only — extractions are never gated): report the last extraction's production-use count from `forge_gate.py status`.

### 5.5. Taste Ratchet (~3 min — Farrice-approved 2026-07-13)

Review new entries in `.agent/jam/taste-ledger.jsonl` since last closeout. For any **dial that has repeated across 2+ jams** (e.g. "natural spoken phrasing over formal," "density-per-beat"), promote it into the Quality Gates of the affected domain's v2 prompts (`skills/<skill>/references/prompts-v2/`) as ONE checkable criterion — then re-run `python3 execution/renaissance_audit.py` + `python3 execution/prompt_library.py build` + `python3 execution/wire_prompt_pointers.py --write`. One-off verdicts stay in the ledger; only repeated taste becomes law. Skip silently if no new entries.

**EMBODIMENT PURITY GUARD (Farrice 2026-07-13, binding):** taste dials promote ONLY into prompts for Farrice-owned deliverables (his brand, his clients' work he directs, system output). NEVER into an extracted expert's embodiment — Role & Activation framing, the expert's methodology, voice texture, or signature moves stay THE EXPERT'S. The intent of every extraction is replicate-then-surpass the expert's own flavor; Farrice's taste applies as a separate overlay (`/voice-over`), never baked into the expert. When in doubt, the dial stays in the ledger.

### 6. Close

One-paragraph summary: what closed, what drained, what drifted. Then:

```bash
python3 execution/chain_runner.py finalize "Weekly closeout <date>" \
    --expert system --skill system --workflow weekly-closeout \
    --type System --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "outcomes drained: N | calibration: clean/flagged | queue: accepted/rejected | Factual Grounding: N/A | Verification: N/A"
```

## Anti-patterns

- Batching 20 revenue questions into one session (drains trust, not the queue) — 5 max.
- Skipping the "dead" option — pendings that will never pay are noise, kill them.
- Running this without presenting judgment calls to Farrice — the whole point is the human closes the loop.
