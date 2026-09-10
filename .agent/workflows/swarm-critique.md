---
description: "/swarm-critique — the metered critique + research swarm (both harnesses). One pen writes; ≤4 read-only seats cast from the skill library find gaps against a NAMED bar or bring research with receipts; Farrice judges blind; $10 hard stop with a receipt. Policy: directives/swarm-usage-policy.md."
---

# /swarm-critique — router → one pen → parallel seats → blind judge → receipt

Why (Farrice 2026-09-09): "when I give it a task, it spawns appropriate agents that have the depth and expertise to go conquer that domain… they come back and contribute." The Sept 8 pilot failed on an unanchored judge, 100 KB identical briefs, coverage-only gates and unmeasured cost. This runbook fixes those four and nothing else. Invoked deliberately, never auto-routed. Solo work keeps the in-context Blind Bar.

Usage:
```
/swarm-critique <artifact-path> --bar <bar-path> [--lenses a,b,c,d] [--dial lightweight|full]
```

Every step prints its receipt line. A missing receipt means the next step does not start.

## 0 · ROUTE
Pattern Table (`directives/orchestration-doctrine.md` § Pattern Table): default is solo. Swarm only when Farrice invoked this runbook, or the task spans ≥2 domains, or names research + critique. Receipt: `ROUTE: swarm (<reason>) · dial=<lightweight|full>`.

## 1 · PEN v1
One pen writes v1 to a file (Claude: Opus seat per the hop-1 law, or the conductor when Farrice granted hop 0; Codex: Astra, the conductor is the pen). Receipt: `PEN: v1 → <path>`.

## 2 · BAR
Name the bar as a PATH (approved specimen, golden reference, register exemplar). Adjectives are not a bar. No path → stop with `Bar: none` and run the in-context Blind Bar instead. Receipt: `BAR: <path> [lines a–b]`.

## 3 · METER open
```
python3 execution/swarm_meter.py open --budget 10 --run <id> --harness claude|codex
```
Receipt: `METER: open <id> budget=$10`.

## 4 · CAST + SEATS
Cast from the skill router's scores for the task (top-k, k ≤ 4; `python3 execution/skill_router_hook.py` scoring or `routing_enforcer.py`), two seat types only (critique, research). Print `CAST: <skill> (critique) · <skill> (research) · …` BEFORE any spawn.
Compile briefs (≤6 KB each; artifact + bar + lens + contract; never the common library):
```
python3 execution/persona_team.py critique --artifact <v1> --bar <bar> --lenses <slugs> --run <id> --platform claude|codex --out .tmp/swarm/<id>/
```
Price every seat before it spawns; a nonzero exit is a stop, not a suggestion:
```
python3 execution/swarm_meter.py price --seat sonnet --brief .tmp/swarm/<id>/<lens>-brief.md --label "<lens>" --run <id>
```
- **Claude:** Agent tool, `subagent_type: general-purpose`, `model: sonnet`, `description: "[swarm:<id>] <lens>"` (the meter reconciles by this prefix), prompt = the brief. Seats run in parallel, read-only (fleet write guard + main write guard). The PreToolUse hook `swarm_meter_hook.py` blocks any dispatch the meter refuses.
- **Codex:** `spawn_agent(fork_context=false, message=<brief>)` per seat after `price`; `wait_agent`; round-2 questions via `send_message`; an idle seat via `followup_task`. Delegation Receipt per seat (`CODEX.md` § subagents). **Thread-limit failure:** fall back to sequential seats, record `seats_parallel:false`, never loop-retry; two unseatable seats → `close --partial`, the pen ships v1 with the gap named.
Receipt: `SEATS: <n> spawned · parallel=<true|false> · est=$<x>`.

## 5 · DIGEST + reconcile
Collect each seat's JSON to `.tmp/swarm/<id>/<lens>.json`, then:
```
python3 execution/persona_team.py digest --outputs .tmp/swarm/<id>/
python3 execution/swarm_meter.py reconcile --run <id> --harness claude|codex [--parent <codex thread id>]
```
The digest is `{crux, gaps, dissent_log (verbatim), null_seats, cost}`. Dissent is preserved, never blended. Receipt: `DIGEST: crux=<one line> · gaps=<n> · dissent=<n> · cost=$<x> (actual|est)`.

## 6 · PEN revises once
The pen integrates through the Composition Ledger (`.agent/workflows/expert-composition-governor.md`): every gap accepted / skipped / rejected with evidence, written to `.tmp/swarm/<id>/LEDGER.md`. One revision, v2 to a file. Coverage is not quality. Receipt: `PEN: v2 → <path> · ledger accepted=<n> skipped=<n> rejected=<n>`.

## 7 · JUDGE = Farrice, blind
Blind the pair (`operator/blind-key.json` pattern: `{"A": "<v1|v2>", "B": "<v2|v1>"}`), show both, ask for the `/jam` grammar: `A` / `B` / `A but <dial>` / `mix` / `neither — <one word>`. One question, no argument. `neither` → one REVISE round from the source; a second `neither` → RETAIN solo, keep the meter. Receipt: `JUDGE: <verdict> · winner=<v1|v2>`.

## 8 · RECEIPT
```
python3 execution/swarm_meter.py close --run <id> --dissent <n>
```
Append the printed `Swarm: …` line to the Blind Bar receipt of the deliverable; one line to `evolution_store/verdict_advisory.jsonl` (`skill: "swarm-critique"`); his verdict into the domain's calibration log. Receipt: `Swarm: <id> seats=<n> rounds=<r> cost=$<x> (actual|est) dissent=<n>`.

## Refuses
- A seat that writes. A judge seat. A fifth seat. A fourth round. A brief over 6 KB. A run without `open`. A seat without `price`. UNMEASURED when a transcript exists.
- Auto-routing: this runbook runs only when named or when the Pattern Table row is printed as the reason.

## Adoption rule
Three receipts where Farrice preferred v2 at a cost he calls worth it, for one work class (Jen-comparable content first). Until then the swarm is an experiment with a meter, not a default.
