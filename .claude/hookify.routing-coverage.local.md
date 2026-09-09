---
name: routing-coverage-check
enabled: false
event: stop
action: warn
conditions:
  - field: transcript
    operator: contains_any
    pattern: "/parallax|/writers-room|/supercomputer|/build-bos|/autopilot|/jcc-deploy|/campaign|/research-swarm"
  - field: transcript
    operator: not_contains
    pattern: "routing_enforcer\\.py check|routing_enforcer check|routing_decisions\\.jsonl|binding_matched"
---

**Routing Enforcer Skipped**: A mandatory-binding workflow was invoked (/parallax, /writers-room, /supercomputer, /build-bos, /autopilot, /jcc-deploy, /campaign, /research-swarm) but no pre-flight check against `execution/routing_enforcer.py` was logged.

The 2026-04-21 incident (Parallax Edition 02 → 7 fabrications) traced to silent binding violation. The enforcer is the deterministic backstop. Run it pre-flight:

```bash
python3 execution/routing_enforcer.py check \
    --request "<user request>" \
    --workflow <chosen-workflow> \
    --quiet --source <caller-id>
```

Non-zero exit means the chosen workflow violates a mandatory binding — pivot to the mandatory workflow OR invoke the documented override flag (e.g., `--no-ground` for Parallax memoir editions).

`chain_runner.py finalize()` runs a post-hoc check when `--workflow` is supplied, so violations DO surface eventually — but pre-flight is cheaper and faster. Full bindings: `execution/routing_enforcer.py BINDINGS` + CLAUDE.md "Mandatory Workflow Routing" table.
