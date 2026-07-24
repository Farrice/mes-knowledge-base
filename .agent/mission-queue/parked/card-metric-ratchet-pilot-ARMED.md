# Mission Card — Metric-Ratchet Overnight Pilot (ARMED, awaiting trigger)
Tier: T2
Produced: 2026-07-24 (loop-engineering brief candidate 12 — Farrice all-12 GO)

## Trigger (do NOT run before one of these is true)
- verify-fleet shows ≥5 genuinely failing contracts (not stale-bless drift), OR
- another deterministic, mechanically-checkable metric shows sustained headroom
  (prose-classifier flag rate, health-metrics regression) named by Farrice.

At build time (2026-07-24) the fleet went green (69/0/4) during candidate 8's
triage — ratcheting a green metric is loop-sprawl (standing refusal #3). This
card banks the design so the capability exists the night it's needed.

## Terms (non-negotiable, from the locked verdict)
- Scope: agent may edit ONLY the artifacts the target metric checks, per-card list.
- Ratchet semantics: commit-on-measured-improvement, auto-revert on regression.
- Hard iteration ceiling: 25 passes, one night, one metric.
- `session_lock.py` held for the entire run; runs only when no harness is active.
- Contract/checker files are READ-ONLY to the agent (anti-metric-gaming guard —
  Shopify's "deleting files" failure mode).
- Morning gate: Farrice (or conductor session) reviews the full diff before the
  branch of work is accepted; `git status` clean before any human session resumes.
- Token cost: one overnight subscription session; zero paid APIs (cost-gate untouched).

## Canon
autoresearch pattern (Karpathy → Lütke → Shopify pi-autoresearch) — the only
independently-replicated loop in the 2026-07-24 canon survey. Local precedent:
alex-suzuki ratchet cycle, commit dcc8f69d7.
