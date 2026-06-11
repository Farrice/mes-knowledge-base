---
description: Read-only harness status, activation health, routing probes, and feedback-loop readiness
---

# /health-check - Harness Status And Activation Health

> **Purpose**: Show what is working, stale, or broken in the Antigravity harness without mutating state by default.

## Operator Core Alignment

This workflow is the canonical source of truth for Health-check behavior. Global
and local Health-check wrappers must stay thin compatibility wrappers that point
back here, not competing behavior contracts.

Preserve these invariants:

- `/health-check` is read-only by default.
- For meaningful work starts, use Operator Cockpit V2 before slower or broader checks: `python3 execution/operator_cockpit.py --intent "<raw request>" --plain`. It renders the confidence packet, status, local friction capture, retrieval home, and global mirror checkpoint.
- Start with `python3 execution/savant_control_room.py --plain` when the user wants the best next move, and `python3 execution/harness_status.py --plain` for the compact trust/status surface.
- Use `python3 execution/operator_core_fast_proof.py --plain` as the daily fast proof layer before slower full control-plane verification.
- Then run `python3 execution/system_health.py --quick` for activation and feedback-loop detail.
- Include `python3 execution/operator_core_status.py --plain` as the compact Operator Core alignment closeout.
- Do not write reports, sync Notion, optimize routes, mutate Mission, or perform cleanup unless explicitly requested.
- Mission remains read-only unless `python3 execution/verify_mission_activation_contract.py` fails.
- Route system-failure or drift-audit language to `/autopilot` or `/system-audit`; use `/health-check` for explicit status and health questions.
- Real Codex subagents require explicit authorization.

## Usage

```bash
/health-check
health-check
source-command-health-check
run harness status
```

## Steps

### 1. Show Harness Status
// turbo
Run the current control room first when a broader next-move answer is useful:

```bash
python3 execution/operator_cockpit.py --intent "[raw request]" --plain
python3 execution/savant_control_room.py --plain
```

Then run the compact trust surface:

```bash
python3 execution/harness_status.py --plain
```

Present the result plainly:

- **Working**: current proof and probes are passing.
- **Stale**: a refresh, mission activation, or scheduled pulse is due, but no breakage is proven.
- **Broken**: a verifier, routing probe, or state contract failed.
- **Next move**: the highest-leverage next action from the status surface.

### 2. Show Activation Detail
// turbo
Run the local-first activation detail view:

```bash
python3 execution/system_health.py --quick
```

Use this for Performance Log readiness, Skill Evolution candidate status,
Notion sync diagnostics, hook guards, routing intelligence counts, and cascade
dependencies. Treat network or Notion unavailability as an environment/sync
detail, not as proof that the local harness is broken.

### 3. Show Fast Proof And Operator Core Alignment
// turbo
Run the fast proof layer, then the compact Operator Core trust panel:

```bash
python3 execution/operator_core_fast_proof.py --plain
python3 execution/operator_core_status.py --plain
```

The fast proof layer checks no-broken harness state, routing probes, live
surface strictness, run receipt schema, friction ledger readability, and local
`/ai-employee-os` proof without changing files. The dashboard checks Autopilot,
Orchestrate, End-session, Health-check, and repaired Operator Core surfaces
without changing files. Include the summary status, aligned count, and next
hardening candidate in the `/health-check` closeout so Farrice does not need to
remember a second command.

### 4. Recommend One Safe Next Move
Give one compact recommendation:

- If `harness_status.py` reports **Broken**, recommend `/system-audit` with the failing verifier or probe.
- If status is **Stale** only, recommend the smallest refresh step and say what can safely wait.
- If activation detail shows Notion sync pending or unavailable, recommend a dry-run sync check only; do not perform a live sync by default.
- If Operator Core alignment fails, recommend the matching sync helper and verifier.
- If feedback evidence is ready for improvement, route supervised changes through `/skill-anneal` or `/self-evolve`; do not invent a separate evolution route.

### 5. Boundaries

- Do not run `python3 execution/system_health.py` without `--quick` by default; the full mode writes a local report file.
- Do not run live Notion sync, route optimization, cleanup, deletion, publishing, or global mirrors from `/health-check`.
- Do not edit Mission files or Mission workflow text from `/health-check` unless the Mission verifier fails and the user explicitly approves repair.
- Do not spawn real Codex subagents unless the user explicitly authorizes delegation, parallel agents, or subagents.

## Verification

After changing this workflow, run:

```bash
python3 execution/sync_operator_core_health_check.py --check
python3 execution/verify_operator_core_health_check.py
python3 execution/validate_skill.py source-command-health-check
python3 execution/savant_control_room.py --plain
python3 execution/operator_core_fast_proof.py --plain
python3 execution/harness_status.py --plain
python3 execution/harness_status.py --json
python3 execution/system_health.py --quick
python3 execution/operator_core_status.py --plain
python3 execution/verify_operator_core_status.py
python3 execution/verify_operator_core_fast_proof.py
python3 execution/verify_savant_control_room.py
python3 execution/verify_system_control_plane.py
python3 execution/verify_mission_activation_contract.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```
