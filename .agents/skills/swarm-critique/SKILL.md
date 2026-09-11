---
name: "swarm-critique"
description: "The metered critique + research swarm (Codex and Claude). Use when Farrice asks for a swarm, a council of experts on a draft, adversarial critique against a named bar, or parallel research with receipts. One pen writes; ≤4 read-only seats cast from the skill library; $10 hard stop; Farrice is the only judge. Never auto-route."
---

# swarm-critique (Codex entry)

Read and execute the workflow at `.agent/workflows/swarm-critique.md`. Policy and caps: `directives/swarm-usage-policy.md`.

Codex specifics: you (Astra) are the conductor AND the pen. Before every `spawn_agent`, run `python3 execution/swarm_meter.py price --seat gpt-6-astra --brief <brief> --label "<lens>" --run <id>`; a nonzero exit is a stop. Seats are read-only; file a Delegation Receipt per seat. After `wait_agent`, run `swarm_meter.py reconcile --run <id> --harness codex --parent <your thread id>`. Thread limit reached → sequential seats, `seats_parallel:false`, never loop-retry.
