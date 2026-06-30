---
description: Google-local Codex front door for intent lock, route choice, safe execution, proof, and closeout
---

# /autopilot - Codex Intent-To-Outcome Front Door

Autopilot is the Google Antigravity front door for raw intent. It turns a messy
request into one owner route, bounded support gates, the first safe local action,
verification, and a run receipt. It is not a competing router and not the older
gate-suppressed mission dispatcher.

For substantial operator/system work, start with the local preflight:

```bash
python3 execution/codex_operator_preflight.py "<raw intent>" --plain
```

Follow the `local_next_action` when it is safe, local, and verifier-backed.
Pause only for external writes, destructive cleanup, paid/quota-heavy tools,
global `~/.codex` edits, Codex Antigravity mutation, publishing/outreach,
connector writes, or real Codex subagents.

## Usage

```bash
/autopilot [raw context]
/autopilot --plan [raw context]
/autopilot --menu [raw context]
```

Default behavior is execute-safe-local-work. `--plan` stops at a
decision-complete plan. `--menu` is for cases where Farrice explicitly wants
ranked options.

## Routing Owner Rules

- Broken, drifted, noisy, not-firing, route/hook/default/wiring, Codex/Claude
  parity, or execution-bias complaints route to `/system-audit`.
- Prior-session, golden-run, caliber drift, or "lost the good part" complaints
  route to `/repeatability-spine`.
- More than three plausible experts/routes route through
  `/expert-composition-governor` as a support gate, not an expert soup default.
- Council, deliberate cross-domain judgment, and collective-genius requests route
  to `/convene`.
- Steering and next-prompt coaching route to `/steering-compass`; persistent
  closeout behavior is global and should not hijack system repair.
- `source-command-jcc-refine` is an intent-refinement support path only. It can
  sharpen ambiguity, but it does not own system repair, route wiring, hooks, or
  Claude-parity complaints.

## Execution Sequence

1. Capture the raw intent.
2. Build the preflight packet with `execution/codex_operator_preflight.py`.
3. Confirm the chosen owner with the workflow router and routing enforcer. Use
   `routing_enforcer.py check --no-log` for probes and verifier checks.
4. If the owner is `/system-audit`, run proof-first local diagnosis before
   patching: route probes, hook probes, bridge checks, registry/index health,
   and the relevant verifier.
5. Patch only the Google-local owner surface needed to change behavior.
6. Rerun the targeted verifier set.
7. Write or update a run receipt for meaningful system work.
8. Close with proof, remaining risks, and concrete next prompts.

## Safety Boundaries

- Do not edit `.claude/` for Codex parity repairs.
- Do not edit `~/.codex` without explicit approval.
- Do not mutate `/Users/farricecain/Codex Antigravity` from this workspace.
- Do not spawn real Codex subagents without explicit run-specific authorization.
- Real Codex subagents, when authorized, are read-only diagnostics by default:
  no further subagents, and the main thread owns all edits, synthesis, and
  integration.
- For research fan-out, add to fan-out list only if Farrice has explicitly authorized it for this run; otherwise run the research angles sequentially in the main thread.
- Any authorization packet must name worker count, read-only scope, deny list, halt condition, and no further subagents.
- Treat "without breaking my workspace" as a safety constraint: keep the first
  action local, reversible, and verifier-backed.

## Proof Standard

Autopilot work counts as repaired only when the route, hook, verifier, and
visible behavior agree. For routing/wiring repair, the minimum proof set is:

```bash
python3 execution/verify_codex_claude_parity.py
python3 execution/verify_google_operator_core.py
python3 execution/verify_system.py --errors-only
python3 execution/run_receipt.py --verify
```

Use narrower checks first while patching, but finish with the full proof set
when the work changes control-plane behavior.
