---
description: Compile messy entrepreneurial intent into a Codex-ready run packet with predicted need, objective, quality bar, route, support gates, first safe action, proof plan, and plugin-packaging boundary
---

# /raw-intent-bridge - Raw Intent Virtuoso Bridge

Put `/raw-intent-bridge` before any rough context when Farrice needs Codex to
translate natural operator language into a deterministic run packet before
normal execution. Use it for messy notes, "I do not know how to ask Codex"
language, prompt-engineer/virtuoso requests, or any entrepreneurial objective
where the route, proof, and first safe action should be made explicit.

This is a command surface for the local companion layer, not a separate plugin
and not a competing router.

## Invocation Contract

Accepted forms are equivalent:

```text
/raw-intent-bridge [payload]
raw-intent-bridge: [payload]
source-command-raw-intent-bridge: [payload]
```

The payload is everything after the prefix. Strip the prefix before packet
generation, route selection, first safe action generation, and handoff. Never
echo `/raw-intent-bridge`, `raw-intent-bridge:`, or
`source-command-raw-intent-bridge:` back into the first safe action.

## Packet + Run Default

Default behavior is Packet + Run:

1. Compile the Codex-ready packet from the stripped payload.
2. Follow the packet's first safe local action when it is reversible,
   current-workspace local, and inside the stated boundaries.
3. Stop for approval when the packet points to global writes, external writes,
   publishing, outreach, paid/quota-heavy tools, destructive cleanup, connector
   writes, plugin marketplace edits, non-current-workspace harness edits, or
   real Codex subagents.

## Execution

Run the packet compiler first:

```bash
python3 execution/raw_intent_run_packet.py "[raw intent]" --plain
```

Use a mode when the lane is obvious:

```bash
python3 execution/raw_intent_run_packet.py "[raw intent]" --mode revenue --plain
python3 execution/raw_intent_run_packet.py "[raw intent]" --mode creative --plain
python3 execution/raw_intent_run_packet.py "[raw intent]" --mode system --plain
```

Default to `--mode auto` when unsure.

## Packet Contract

The command must produce:

- raw intent
- predicted need
- center
- success standard
- constraints
- missing inputs
- questions that change execution
- chosen route
- support gates
- composition slots
- context plan
- execution decision
- first safe action
- verification plan
- operator run prompt
- plugin packaging verdict

## Routing Rules

- Revenue/money/client/offer goals route toward revenue or offer workflows.
- Creative/campaign/content/taste goals keep creative quality gates visible.
- Bridge-build, skill-system, workflow-bridge, run-packet, or companion-layer
  goals route to `/source-to-skill-system`.
- Prompt-engineer, world-class, and virtuoso language is raw-intent context,
  not a reason to route into unrelated creative-writing workflows.
- Plugin packaging stays deferred for `antigravity-operator-core` until local
  cold-start proof passes.

## Boundaries

- No global `~/.codex` writes during normal packet runs. A thin global skill
  wrapper is allowed only when Farrice explicitly asks for global deployment.
- No plugin marketplace edits.
- No external writes, publishing, outreach, or connector writes.
- No destructive cleanup.
- No real Codex subagents without explicit authorization.

## Verification

After changing this command or the packet compiler, run:

```bash
python3 execution/verify_raw_intent_bridge_command.py
python3 execution/verify_raw_intent_run_packet.py
python3 execution/verify_autopilot_runtime_preflight.py
python3 execution/verify_virtuoso_orchestration.py
python3 execution/verify_google_operator_core.py
```
