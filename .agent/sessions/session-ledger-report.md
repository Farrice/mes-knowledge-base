# Session-Ledger Report (finalize-debt observe mode)
Generated 2026-08-11T06:15:08 · source: .agent/sessions/observe-log.jsonl

- **1210 would-block events** collapse to **150 debted sessions** (noise factor 8.1x — multi-Stop firings per session; enforcement today would block ~8.1x per honest session).
- Sessions ending with zero measured subagent spawns: 98.
- Top open-debt types (last event per session): skill_loaded (922), skill_grepped (48), qualifying_workflow (3)

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
| 2026-W32 | 35 |
| 2026-W33 | 3 |

## Decision guidance (deterministic, not advice)

- Flip `LEDGER_ENFORCE=1` only when the weekly debted-session count is a number you would
  accept being hard-blocked that many times per week — the noise factor above is the
  false-positive multiplier to fix (dedupe Stop firings) BEFORE enforcement.
