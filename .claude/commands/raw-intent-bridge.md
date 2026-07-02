---
description: Compile messy entrepreneurial intent into a Codex-ready Raw Intent Virtuoso Bridge run packet before routing or execution
---

# /raw-intent-bridge

Read and execute the workflow at `.agent/workflows/raw-intent-bridge.md`.

## Invocation Contract

Accepted forms are equivalent:

```text
/raw-intent-bridge [payload]
raw-intent-bridge: [payload]
source-command-raw-intent-bridge: [payload]
```

Treat everything after the prefix as the payload. Strip the prefix before
packet generation and never echo the bridge command into the first safe action.

Default behavior is Packet + Run: compile the packet, then follow the first
safe local action when it is reversible and inside the workspace boundaries.

This command runs the local packet compiler:

```bash
python3 execution/raw_intent_run_packet.py "[raw intent]" --plain
```

Use `--mode revenue`, `--mode creative`, or `--mode system` only when the lane
is obvious.

Plugin packaging stays deferred to `antigravity-operator-core` until local
cold-start proof passes; do not create a new plugin from this command.
