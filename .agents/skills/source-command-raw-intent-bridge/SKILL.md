---
name: "source-command-raw-intent-bridge"
description: "Run /raw-intent-bridge when the user gives raw intent, messy entrepreneurial context, rough notes, asks for a prompt-engineering bridge, says they do not know how to ask Codex, wants a Codex-ready run packet, or needs predicted need, objective, quality bar, route, gates, first safe action, and proof before normal execution."
---

# source-command-raw-intent-bridge

Use this skill when the user invokes `/raw-intent-bridge`,
`source-command-raw-intent-bridge`, asks for the Raw Intent Virtuoso Bridge, or
needs messy operator intent compiled into a deterministic Codex run packet.

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
  actions, or real Codex subagents without explicit authorization

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
