---
title: Swarm engines silently inherited the conductor model
date: 2026-09-14
tags: [orchestration, seating, workflow-tool, swarm, token-budget]
job: swarm-audit-and-manager-layer
---

# Swarm engines silently inherited the conductor model

## Symptom
"Do we actually have swarm engineering, or does it just burn tokens?" Under a Fable conductor,
every council and research swarm felt expensive and the Fable share of the weekly pool drained
faster than the work justified.

## Cause
The Workflow tool's `agent()` call inherits the main-loop model when `model` is omitted (confirmed
in the `workflow-authoring` reference). Four engines were written before the seating law existed:
`collective-genius-council.workflow.js` had 0 of 6 calls seated, `deep-research-swarm.workflow.js`
0 of 5, `swarm-heavy` 2 unseated, `swarm-research` 3 unseated; `parallel-extract.md` and
`parallel-content.md` never named a model. Every worker-grade agent ran on Fable. Separately, the
swarm meter (`swarm_meter.py` + PreToolUse hook) was wired into `/swarm-critique` only and had
never fired (`.agent/swarm-usage.json` did not exist).

## Fix
- Seat every call: workers `model: 'sonnet'`, integrator/judge/decompose `model: 'opus'`; a header
  comment in each engine states the rule. `node --check` on all four.
- Meter open/close lines on the `/swarm` and `/convene` fronts.
- Two dead references fixed (`council.md` → mark-kashef workflow path; `swarm-critique.md` blind-key path).
- Playbook Play 7 records what exists, where it runs (Claude only; Codex = worker seats), and the
  token anti-patterns from the primary sources.

## How to recognise it next time
Fable usage drops during a council or research swarm; `grep -c "model:"` in a `.workflow.js` is
lower than `grep -c "agent("`. Any new engine: seat at authoring time, never rely on inheritance.

## Probe result (same day)
Workflow-internal `agent()` calls do NOT pass through the PreToolUse meter hook: the probe run
(`probe-opus48-vs-5-steerability`, 33 agents, 5,245,091 subagent tokens, 26 min, 0 errors) closed
the meter at seats=0 cost=$0. The meter records only what you `charge` by hand from the conductor
receipt; the spend dial for engines is `--effort` and the engine's runaway caps. Verify was 20 of 33
agents and produced 2 refutations, one of which corrected a wrong GDPval number a Sonnet research
seat had reported earlier the same day — the critique pass earns its cost.
