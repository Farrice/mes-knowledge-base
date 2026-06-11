---
description: Thin bridge for Kimi-style research and general-purpose swarm packet compilation
---

# /kimi-swarm

`/kimi-swarm` compiles Kimi-style context packs, research swarms, and general council work into Codex-native packets. It is a bridge, not a competing router.

Owners:

- `/virtuoso` composes the route.
- `/deep-research-os` owns research mode.
- `/convene` owns general-purpose collective-genius mode.
- the main Codex thread owns integration.

## Usage

Research:

```bash
python3 execution/kimi_swarm.py plan "[research question]" --mode research --depth standard --allow-subagents --json
```

General/council:

```bash
python3 execution/kimi_swarm.py plan "[strategy or creative task]" --mode general --convene-mode wide --json
```

Context pack:

```bash
python3 execution/kimi_swarm.py plan --from-pack path/to/kimi-pack.md --mode auto --json
```

## Boundary

This command prepares worker packets, source rules, phase receipts, and verification commands. It does not spawn real Codex subagents unless Farrice explicitly authorizes real delegated agent work in the current run.

## Verification

```bash
python3 execution/verify_kimi_swarm.py
python3 execution/verify_convene.py
python3 execution/verify_deep_research_os.py
python3 execution/verify_virtuoso_orchestration.py
python3 execution/verify_subagent_readiness.py
```
