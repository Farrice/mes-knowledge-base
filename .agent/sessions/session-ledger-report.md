# Session-Ledger Report (finalize-debt observe mode)
Generated 2026-08-28T07:20:29 · source: .agent/sessions/observe-log.jsonl

- **1318 would-block events** collapse to **173 debted sessions** (noise factor 7.6x — multi-Stop firings per session; enforcement today would block ~7.6x per honest session).
- Sessions ending with zero measured subagent spawns: 119.
- Top open-debt types (last event per session): skill_loaded (927), skill_grepped (69), qualifying_workflow (3)

## Debted sessions per ISO week

| week | sessions |
|---|---|
| 2026-W24 | 2 |
| 2026-W26 | 4 |
| 2026-W27 | 20 |
| 2026-W28 | 21 |
| 2026-W29 | 33 |
| 2026-W30 | 17 |
| 2026-W31 | 15 |
| 2026-W32 | 34 |
| 2026-W33 | 7 |
| 2026-W34 | 10 |
| 2026-W35 | 10 |

## Decision guidance (deterministic, not advice)

- Flip `LEDGER_ENFORCE=1` only when the weekly debted-session count is a number you would
  accept being hard-blocked that many times per week — the noise factor above is the
  false-positive multiplier to fix (dedupe Stop firings) BEFORE enforcement.
