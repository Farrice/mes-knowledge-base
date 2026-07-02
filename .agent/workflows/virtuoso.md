---
description: Deploy-at-will Virtuoso orchestration trace for route, owner, gates, composition, raw-intent packets, delegation boundaries, plugin surface, and proof
---

# /virtuoso - Orchestration Composer

Use `/virtuoso` when a goal needs the full harness composed into one visible
trace: route, owner, stack, bounded composition, tool/plugin surface, verifier
plan, and first safe action.

Virtuoso is a composer over the current routers. It is not a competing
super-router and does not spawn real Codex subagents.

## Raw Intent Bridge

When the user says they do not know how to ask Codex, gives messy context, asks
for a prompt-engineering bridge, or needs the full Codex capability surface for
entrepreneurial work, compile a raw intent packet before normal execution:

```bash
python3 execution/raw_intent_run_packet.py "[raw intent]" --plain
```

Use `--mode revenue`, `--mode creative`, or `--mode system` when the lane is
obvious. Otherwise use `--mode auto`.

The packet must show predicted need, center, quality bar, chosen route, support
gates, composition slots, context plan, execution decision, first safe action,
verification plan, operator run prompt, and plugin packaging verdict.

## Usage

```bash
python3 execution/virtuoso_orchestration.py "[goal]"
python3 execution/virtuoso_orchestration.py "[goal]" --json
python3 execution/virtuoso_orchestration.py "[goal]" --trace-only
python3 execution/virtuoso_orchestration.py "[goal]" --workflow
python3 execution/virtuoso_orchestration.py "[goal]" --mode revenue
python3 execution/virtuoso_orchestration.py "[goal]" --mode creative
python3 execution/virtuoso_orchestration.py "[goal]" --delegate-intent
```

`--delegate-intent` prepares subagent packets only. Real Codex subagents require
explicit authorization and a Delegation Receipt.

## Output Standard

Every Virtuoso trace should include:

- Co-Creative Launchpad
- Raw Intent Bridge status
- route and owner
- support gates
- composition slots
- plugin/tool surface
- delegation boundary
- routing evidence
- execution receipt
- verifier plan
- first safe action or exact judgment gate

## Boundaries

- No external writes, publishing, paid tools, destructive cleanup, connector
  writes, global mirrors, Mission mutation, or real subagents without explicit
  approval.
- Plugin packaging stays deferred until local cold-start proof passes.
- Support gates are considered, not executed, unless the trace explicitly says
  they ran.
