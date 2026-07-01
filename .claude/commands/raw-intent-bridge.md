---
description: Compile messy entrepreneurial intent into a Codex-ready Raw Intent Virtuoso Bridge run packet before routing or execution
---

# /raw-intent-bridge

Read and execute the workflow at `.agent/workflows/raw-intent-bridge.md`.

This command runs the local packet compiler:

```bash
python3 execution/raw_intent_run_packet.py "[raw intent]" --plain
```

Use `--mode revenue`, `--mode creative`, or `--mode system` only when the lane
is obvious.

Plugin packaging stays deferred to `antigravity-operator-core` until local
cold-start proof passes; do not create a new plugin from this command.
