---
name: "source-command-raw-intent-bridge"
description: "Run /raw-intent-bridge when the user gives raw intent, messy entrepreneurial context, rough notes, asks for a prompt-engineering bridge, says they do not know how to ask Codex, wants a Codex-ready run packet, or needs predicted need, objective, quality bar, route, gates, first safe action, and proof before normal execution."
---

# source-command-raw-intent-bridge

Put this skill before any raw context when the user invokes
`/raw-intent-bridge`, `raw-intent-bridge:`,
`source-command-raw-intent-bridge:`, asks for the Raw Intent Virtuoso Bridge, or
needs messy operator intent compiled into a deterministic Codex run packet.

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

Default behavior is Packet + Run: compile the packet, then follow the first
safe local action when it is reversible, current-workspace local, and inside the
boundaries. Stop for approval before global writes, external writes,
publishing, outreach, paid/quota-heavy tools, destructive cleanup, connector
writes, plugin marketplace edits, non-current-workspace harness edits, or real
Codex subagents.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/raw-intent-bridge.md` as the
canonical behavior source. It must preserve:

- raw intent is compiled before normal routing
- the durable compiler is `execution/raw_intent_run_packet.py`
- `/autopilot` and `/virtuoso` remain support surfaces, not competing owners
- `/source-to-skill-system` owns bridge-build and companion-layer evolution
- prompt-engineer/world-class/virtuoso wording does not capture unrelated
  creative-writing routes
- plugin packaging is deferred to `antigravity-operator-core` after cold-start
  proof
- no global mirrors, plugin marketplace edits, external writes, destructive
  actions, or real Codex subagents without explicit authorization; a thin
  global trigger wrapper is allowed only when Farrice explicitly asks for
  global deployment

## Command Template

Read and execute `.agent/workflows/raw-intent-bridge.md`. Compile the packet:

```bash
python3 execution/raw_intent_run_packet.py "<raw intent>" --plain
```

Use one of these modes when useful:

```bash
python3 execution/raw_intent_run_packet.py "<raw intent>" --mode revenue --plain
python3 execution/raw_intent_run_packet.py "<raw intent>" --mode creative --plain
python3 execution/raw_intent_run_packet.py "<raw intent>" --mode system --plain
```

Then follow the packet's chosen route, support gates, first safe action, and
verification plan.
