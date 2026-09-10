# Swarm Usage Policy (critique + research seats, both harnesses)

> **Cap**: **$10.00 per swarm run, hard stop with a receipt** (Farrice, 2026-09-09). Warn at $7. Daily block $20 (same as `cost_gate.py`). Max 4 seats, max 3 rounds, max 6,144 bytes per seat brief.
> **Tracker**: `.agent/swarm-usage.json` + one receipt per run in `.agent/swarm-runs/<run-id>.json` | **Meter**: `execution/swarm_meter.py` | **Claude gate**: `execution/hooks/swarm_meter_hook.py` (PreToolUse on `Agent|Task`, fires only while a run is open) | **Codex gate**: the runbook calls `swarm_meter.py price` before every `spawn_agent` and files a Delegation Receipt (`CODEX.md` § subagents).
> **Runbook**: `.agent/workflows/swarm-critique.md` | **Brief compiler**: `execution/persona_team.py critique` | **Seat prompts**: `agents/_framework/seats/{critique-seat,research-seat}.md`

## Why this exists

Farrice, 2026-09-09: the Kimi-style ask. "When I give it a task, it spawns appropriate agents that have the depth and expertise to go conquer that domain… they come back and contribute." The Sept 8 pilot tried this and failed for three measurable reasons, none of them capability: the judge had no anchor and lowered its own bar; every seat got the same 100 KB brief; the gates measured coverage and hashes while cost read UNMEASURED. This policy fixes those three and nothing else.

## The amendment (doctrine, binding — replaces the absolute in `orchestration-doctrine.md` and `blind-bar-protocol.md`)

Verification never gets its own seat, **with one Mailroom-shaped exception (Farrice, 2026-09-09):** a critique swarm may seat at most 4 read-only seats for at most 3 rounds, each returning the single biggest gap against a **named bar artifact** (never adjectives), with dissent logged verbatim and cost printed. The swarm never writes the artifact: **one pen writes, the pen revises once, and Farrice is the only judge** (no model judge seat). A run opens against a $10 budget with a hard stop that reports. An unbudgeted, unbarred, or unreceipted critique seat is a Seating Charter violation. The May 2026 scar (twelve critic subagents killed for agreeable padding) is answered by the bar rule those critics never had: a seat that cannot cite the bar line and the artifact line it is comparing returns nothing.

Solo work keeps the in-context Blind Bar (2 rounds, ~5–15k tokens, zero subagents). The swarm is invoked deliberately, never auto-routed.

## Casting (MoE in practice: the right few, never all)

- **Bench = the skill library.** A seat is cast with ONE skill's `SKILL.md` + `genius.md` (+ one named workflow at most). Depth comes from the extraction, not from the prompt. Never a generic persona, never the common library.
- **Router = the skill router's scores** for the task (`execution/skill_router_hook.py`, `routing_enforcer.py` BINDINGS): top-k, k ≤ 4, filtered by the Pattern Table in `orchestration-doctrine.md`. The cast is printed as a receipt before any spawn: `CAST: <skill> (research|critique) · …`.
- **Two seat types.** Research seats return `{findings, evidence_paths, unknowns}`; critique seats return `{biggest_gap, evidence_lines: [artifact:Ln, bar:Ln], proposed_fix ≤3 lines, dissent}`. No writer seats. No judge seat.
- **Budget dial.** "Lightweight" = 2 research seats. "Full" = 4 mixed. Both stop at $10.

## Hard rules

1. `swarm_meter.py open` before the first seat; `price` before every seat; `close` after the judge. A seat spawned without a priced reservation is a violation, on either harness.
2. Seat briefs ≤ 6,144 bytes: the artifact, the bar slice, the lens (≤1 KB), the output contract. Over → `INPUT_GAP`, no seat.
3. Seats are read-only. On Claude the fleet write guard and main write guard enforce it; on Codex `main_write_guard.py` fires inside subagents and the brief says so.
4. The pen integrates through the Composition Ledger (`.agent/workflows/expert-composition-governor.md`): every gap accepted, skipped, or rejected with evidence. Coverage is not quality.
5. The judge is Farrice, blind, in the `/jam` grammar (`A` / `B` / `A but <dial>` / `mix` / `neither`). One revise round. `neither` twice = retain solo, keep the meter.
6. Receipt line, appended to the Blind Bar receipt: `Swarm: <run-id> seats=<n> rounds=<r> cost=$<x> (est|actual) dissent=<n>`. `actual` whenever a transcript exists (Claude subagent files, Codex child rollouts); UNMEASURED is a violation, not a value.
7. Thread-limit failure (Codex): fall back to sequential seats, record `seats_parallel:false`, never loop-retry; two unseatable seats → close `PARTIAL`, the pen ships v1 with the gap named.

## Pricing (per MTok, from the Executor Registry; actuals overwrite estimates)

| Seat | In | Out | Note |
|---|---|---|---|
| sonnet (Sonnet 5) | $3 | $15 | default seat body |
| opus (Opus 5) | $5 | $25 | judge-panel finals only, never a critique seat by default |
| haiku (Haiku 4.5) | $1 | $5 | mechanical shuttling only |
| gpt-6-astra (Codex seats) | $5 | $25 | **UNCONFIRMED** — Codex subagents bill against the ChatGPT plan, not per token; the meter still prices them so the dial means the same thing on both harnesses |

Estimate = (brief bytes ÷ 4 + 3,000 harness overhead) × in-price + expected output (default 1,200 tokens) × out-price. Cache-read tokens at 10% of in-price, cache-write at 125%.

## What "worth it" means (3-run review, same rule as the Mailroom)

Nothing about swarm mode becomes a default until three receipts show Farrice preferred the post-critique take at a printed cost he calls worth it. Adoption is per work class (Jen-comparable content first), never global.
