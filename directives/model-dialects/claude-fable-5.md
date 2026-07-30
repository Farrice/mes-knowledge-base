# Model Dialect — claude-fable-5 (SEEDED 2026-07-28 — not yet probe-scored)

> **Status: SEEDED, not PROBED.** The opus-5 card came from an 8-probe battery; this card is
> seeded from live-session observation (2026-07-28 unhobble session, Fable in the main seat)
> plus vendor canon. Run the P1–P9 battery when probe budget is available — Fable turns are
> ~50% of monthly budget, so the battery itself is a deliberate spend decision, not a default.

## Identity & Params
Model ID `claude-fable-5`. Mythos-class tier above Opus; same underlying model as Claude
Mythos 5 (Fable = generally-available seat with dual-use safety measures). For pricing,
context, effort ladder and API params: **`claude-api` skill is the single source of truth —
never restate numbers here** (repetition→simplicity, six-shifts card). System role:
**apex conductor** (`orchestration-doctrine.md` Conductor Ladder: strongest available model
conducts; Fable conducts when seated, Opus 5 steady-state, Sonnet 5 grunt).

## Observed Behavior (live-session evidence, 2026-07-28)
- **Scope containment: STRONG (contrast with Opus 5's P9 FAIL).** Held plan-mode boundaries
  across two planning cycles; subagent dispatches carried the negative brief and none executed
  Chain/Notion side effects; stopped at genuine user forks instead of steamrolling them.
- **Honest-negative reporting: STRONG.** Reported the Gemini FAILED receipt verbatim instead of
  papering over it; shipped a null result ("Anthropic never said graph engineering") as the
  headline finding; quarantined unverifiable stats rather than laundering them.
- **Delegation: calibrated.** Fanned out 3–4 subagents only for genuinely parallel research
  tracks; zero verification subagents; folded results without re-deriving them.
- **Verbosity: family trait present on deliverable turns.** Delivery messages run long
  unprompted (same P2/P6 tendency as Opus 5, less narration-of-verification). State length
  bounds explicitly on deliverables; conversational asks get conversational scale.
- **Judgment under ambiguity: high.** Distinguished a fabricated-attribution hype wave from a
  real primary-sourced story on the same topic in the same day without being told the
  difference existed.

## Prompting Adjustments
- **DO** seat Fable for: conducting multi-agent missions, hype-vs-real judgment calls,
  taste-bearing strategy, canonical-file surgery, anything where a wrong call cascades.
- **DO** state length on deliverables — same rule as every Claude 5 family member.
- **DO** hand it bare v2 Output Contracts; no scaffolding, no restate-the-rules tax.
- **DON'T** spend Fable turns on mechanical work (file moves, formatting, wiring) — that is
  Opus-5/Sonnet-5 work per the seating charter. Fable ≈ 50% of monthly budget.
- **DON'T** add verify/double-check instructions — self-verification is native tier-wide.
- Subagent briefs: same negative brief as Opus 5 (subagents inherit CLAUDE.md regardless of
  the conductor's tier).

## Re-probe Triggers
P1–P9 battery run from an independent seat · provider version bump past `claude-fable-5` ·
fixture replay flags drift on Fable-conducted work · the seating charter changes Fable's role.

## Machine-Readable Dialect (consumed by `steering_loop_hook.py` — the bound injector)

<!-- BEGIN:machine-dialect -->
```json
{
  "model_match": ["claude-fable-5", "fable-5", "fable"],
  "inject": {
    "deliverable": [
      "State the length/scale you will hold in ONE line, then hold it; scope = exactly the ask, sized to the loaded expert's exemplars."
    ],
    "conversational": [
      "Direct answer first, conversational scale, no unrequested expansion."
    ],
    "delegation": [
      "Fable conducts — delegate mechanical/parallel tracks to cheaper seats; dispatch briefs carry verbatim: \"{negative_brief}\" (subagents inherit CLAUDE.md side effects)."
    ]
  },
  "negative_brief": "no Chain, no finalize, no Notion, no Next Moves, return only the artifact",
  "probe_evidence": "SEEDED from live-session observation 2026-07-28; P1-P9 battery pending — treat inject lines as provisional"
}
```
<!-- END:machine-dialect -->
