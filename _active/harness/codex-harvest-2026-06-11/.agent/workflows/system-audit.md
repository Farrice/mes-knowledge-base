---
description: Control-plane audit for Autopilot, routing, bridges, activation, telemetry, and firing behavior
---

# /system-audit - Control Plane Audit

Use this when the system feels broken, cluttered, slow, duplicated, or "built but not firing." This is the practical audit route for the Codex Antigravity control plane, not a generic duplicate-file scan.

The audit standard is: a system only counts as working if it has a trigger, route, activation path, telemetry or proof surface, and a verifier.

For agentic engineering behavior, the system also counts as working only if it
keeps operator-owned intent, uses precise source truth instead of context bloat,
splits work into reviewable chunks, gates risky dependencies, and stops review
loops on measurable proof.

## Operator Core Alignment

This workflow is the canonical source of truth for System-audit behavior.
Global and local System-audit wrappers must stay thin compatibility wrappers
that point back here, not competing behavior contracts.

Preserve these invariants:

- `/system-audit` is the control-plane audit and repair route for broken, drifted, cluttered, or not-firing harness behavior.
- `/system-audit` also owns operating-alignment repair when the user asks for unified global/workspace Codex behavior, maximum firepower, orchestration layers, expert/subagent coordination, automation cleanup, or output consistency. Use `semantic_libraries/antigravity/primitives/operating-alignment-contract.md`.
- `/system-audit` owns Operator Cockpit V2 repair when the user describes engineering debt, bottlenecks, user failure modes, safeguards not working, Codex/Claude intent mismatch, retrieval overload, or a need to rebuild the harness without shrinking the intelligence arsenal.
- Run read-only proof first: routing, bridge, activation, telemetry, cohesion, and verifier checks.
- Distinguish structural health from firing behavior; files existing is not proof.
- Repairs must be severity-ranked, verifier-backed, and workspace-local by default.
- Global `~/.codex` edits require explicit approval; external writes, publishing, connector writes, destructive cleanup, broad archive/delete, and Mission mutation require explicit approval and proof.
- Mission remains untouched unless `verify_mission_activation_contract.py` fails and Farrice explicitly approves Mission repair.
- Route normal status reads to `/health-check`, routing analytics to `/routing-intelligence`, and raw intent or broad broken-harness triage to `/autopilot`.
- Real Codex subagents require explicit authorization.

## Scope

- Authority: `CODEX.md`, workspace `AGENTS.md`, global `~/.codex/AGENTS.md` when read-only comparison is needed, project Autopilot workflow, and Operator Autopilot agent.
- Control plane: `/autopilot`, `/system-audit`, `/repeatability-spine`, `/orchestrate`, `/mission`, `/routing-intelligence`, `/health-check`, `/self-evolve`, `/skill-anneal`, `/knowledge-librarian`, and `/source-to-skill-system`.
- Bridges: `.agent/workflows/`, `.claude/commands/`, hot `.agents/skills/source-command-*`, and cold `.agents/cold-skills/source-command-wrappers/`.
- Runtime signals: router parity, governor lane, protocol activation, performance log, routing intelligence, session state, and regression guards.
- Cohesion spine: intent memory, shared system-cohesion state, activation queue, weekly cohesion platter, and mission handoffs.
- Agentic engineering loop: `semantic_libraries/antigravity/primitives/agentic-engineering-loop-contract.md`, exact source paths, context plan, work chunks, review stop, dependency safety, use-now artifact, and hardening proof.
- Operating alignment: `semantic_libraries/antigravity/primitives/operating-alignment-contract.md`, `semantic_libraries/antigravity/primitives/magic-preservation-regression-set.md`, meta-intent routing, Orchestration Receipt, and global-write approval gate.
- Operator Cockpit V2: `execution/operator_cockpit.py`, Intent Confidence Packet, local friction capture, retrieval/project home, dated backlog map, and global mirror checkpoint.
- Out of scope by default: deleting the migrated command library, changing `~/.codex`, publishing, connector writes, or destructive cleanup.

## Step 1: Baseline Proof

Run the existing proof set first so the audit distinguishes structural health from firing behavior:

```bash
python3 execution/verify_codex_authority.py
python3 execution/verify_agentic_engineering_loop_contract.py
python3 execution/verify_skill_system_contract.py
python3 execution/verify_autopilot_runtime_preflight.py
python3 execution/verify_autopilot_routing.py
python3 execution/verify_operator_lesson.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```

Then run the activation and telemetry checks:

```bash
python3 execution/system_health.py --quick
python3 execution/protocol_tracker.py audit
python3 execution/routing_intelligence.py scoreboard
python3 execution/log_performance.py baseline
```

## Step 2: Golden Routing Matrix

Run the control-plane guard:

```bash
python3 execution/verify_system_control_plane.py
```

If it fails, treat the failure as higher priority than generic command-count or duplicate-skill findings. The guard must catch:

- broken-system phrases routing to specialist workflows
- repeatability phrases routing to literal keyword workflows instead of `/repeatability-spine`
- `system audit` ranking a content audit above `/system-audit`
- command menu and workflow router disagreement
- governor failures to detect `system-failure`
- missing bridge coverage for control-plane commands
- missing Autopilot behavior-contract text

## Step 3: Authority Map

Compare the current instruction layers and report conflicts:

| Surface | What To Check |
|---------|---------------|
| `CODEX.md` | Active authority order, hot/cold policy, verification standard |
| `AGENTS.md` | Workspace rule that points to `CODEX.md` and preserves compatibility boundary |
| `~/.codex/AGENTS.md` | Global defaults only; read-only unless user approved global edits |
| `.agent/workflows/autopilot.md` | Intent Lock, Clarity Score, Autopilot Trace, first action, verification, closeout |
| `agents/operator-autopilot/AGENT.md` | Same behavior contract as the workflow, without overclaiming native Plan Mode |

Flag any instruction that makes the user choose from a menu when Autopilot should choose a route, or any instruction that claims native Plan Mode is active when it is only being emulated.

## Step 4: Bridge Map

For each control-plane command, verify that the executable workflow and Codex skill exist. Source command compatibility is useful but not the active authority.

Required commands:

- `autopilot`
- `system-audit`
- `orchestrate`
- `repeatability-spine`
- `mission`
- `routing-intelligence`
- `health-check`
- `self-evolve`
- `skill-anneal`
- `knowledge-librarian`
- `source-to-skill-system`

Report each as:

```markdown
| Command | Workflow | Codex skill | Source command | Status | Notes |
```

## Step 5: Activation Map

Classify each major system:

| Status | Meaning |
|--------|---------|
| Active | Triggered recently and has proof data |
| Dormant | Exists but has not fired or has zero data |
| Blocked | Waiting on upstream data, approval, dependency, or threshold |
| Stale | Fired before but not within the expected window |
| Unmeasured | Built but no telemetry/verifier proves it fires |

Use the health report, protocol tracker, routing intelligence, and performance baseline as the evidence. Do not call a system "working" just because the files exist.

## Step 5.5: Cohesion Spine Check

Verify that the system is acting like one coordinated unit, not isolated tools:

```bash
python3 execution/verify_intent_memory_contract.py
python3 execution/verify_system_cohesion_spine.py
python3 execution/verify_automation_cohesion_standard.py
python3 execution/activation_governor.py plan --dry-run
python3 execution/system_cohesion_platter.py verify
```

The spine is healthy when:

- `/autopilot` and `/mission` preserve the active intent before meaningful work.
- `.agent/system-cohesion-state.json` records the active route, support gates, activation queue, verifier status, weekly platter path, and next move.
- activation recommendations are queued with approval boundaries instead of fake protocol, expert, or performance activity.
- `weekly-system-pulse` includes the System Cohesion Platter as the recurring readout.

## Step 6: Issue Ledger

Produce a severity-ranked ledger:

```markdown
| Severity | Symptom | Cause | Affected Surface | Fix | Verifier | Boundary |
|----------|---------|-------|------------------|-----|----------|----------|
```

Severity rules:

- P0: Autopilot/front-door failure, unsafe routing, or approval-boundary break.
- P1: router parity, bridge coverage, authority conflict, or broken-system phrases misrouting.
- P2: dormant telemetry, stale protocols, missing closeout proof, weak activation data.
- P3: cleanup, documentation, naming, or low-risk hygiene.

Boundary must be one of: workspace-only, global approval required, external approval required, or destructive approval required.

## Step 7: Repair And Prove

Apply workspace-local fixes first. After any fix, rerun:

```bash
python3 execution/verify_system_control_plane.py
python3 execution/verify_agentic_engineering_loop_contract.py
python3 execution/verify_autopilot_runtime_preflight.py
python3 execution/verify_autopilot_routing.py
python3 execution/verify_operator_lesson.py
python3 execution/codex_harness_check.py
```

If system, router, workflow, skill, or bridge files changed, also rerun the relevant checks from `CODEX.md`.

When the repair touches intent memory, cohesion state, activation, or weekly pulse, also rerun:

```bash
python3 execution/verify_intent_memory_contract.py
python3 execution/verify_system_cohesion_spine.py
python3 execution/verify_automation_cohesion_standard.py
python3 execution/activation_governor.py verify
python3 execution/system_cohesion_platter.py verify
python3 execution/recurring_ops.py weekly-system-pulse --dry-run
```

## Output

End with:

- what was broken
- what was repaired
- what now passes
- what remains dormant or blocked
- whether any global `~/.codex` mirror work is recommended
- the next fresh-session smoke test prompt

## Verification

After changing this workflow, run:

```bash
python3 execution/sync_operator_core_system_audit.py --check
python3 execution/verify_operator_core_system_audit.py
python3 execution/validate_skill.py source-command-system-audit
python3 execution/operator_core_status.py --plain
python3 execution/verify_operator_core_status.py
python3 execution/verify_system_control_plane.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```
