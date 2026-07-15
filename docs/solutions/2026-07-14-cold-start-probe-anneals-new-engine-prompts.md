---
name: Cold-Start Probe Anneals New Engine Prompts
problem_signature: a freshly forged engine prompt (one other agents will execute) passes the deterministic structure audit while carrying hidden ambiguities only a cold reader hits — dangling references, undefined jargon, contradictory placement instructions the author can't see because they had full context
domain: system
tags: [forge-os, prompt-forging, cold-start, poc-gate, usability-test, annealing]
date: 2026-07-14
status: active
session: forge-os-wave-1-poc
---

# Cold-Start Probe Run Anneals a Brand-New Engine Prompt Same-Session

**Date**: 2026-07-14 · **Domain**: system / prompt forging · **Origin**: Forge OS Wave 1 PoC

## Problem

A freshly forged engine prompt (a v2 prompt other agents will execute) can pass the deterministic
audit (sections present, ≥20 lines, structure-pure) while still carrying hidden ambiguities that
only bite a cold reader: dangling references to stages defined elsewhere, undefined jargon
("wiring trio" — actually four steps), contradictory placement instructions, schema keys mentioned
in prose but absent from the frontmatter spec. The author can't see these — they had the full
context the cold user won't.

## Solution

Run the engine's mandatory in-session PoC (Forge Radar gate) as a **double-duty probe**: dispatch
one fresh-context agent to (a) execute the engine on a real input end-to-end, AND (b) return, as
part of its receipt, "every place the engine prompt was ambiguous or hard to follow — this is a
usability test of the engine itself; be honest, list every friction point." Then fix the engine
same-session and re-run the deterministic gates.

First run on `skills/forge-os/references/prompts-v2/prompt-forge.md`: the probe both produced a
valid artifact (audit-passing, corpus-grounded, correctly rejected two wrong-fit owning skills on
their own scope lines) and surfaced 7 real defects (undefined wiring steps, dangling F1 reference,
frontmatter semantics only in the upstream spec, fidelity-key contradiction, ambiguous fixture
placement, no rule for prompts with no owning workflow, no mechanism for the no-owning-skill
case). All 7 fixed before the engine shipped.

## Why it works

The cold-start agent is the artifact's REAL user (fresh context, no author knowledge), so its
friction report is ground truth, not review theater. Bundling proof + usability into one run costs
nothing extra — the agent was already required by the PoC gate.

## How to apply

Any time a new prompt/workflow/skill that OTHER agents will execute is built: the PoC dispatch
prompt must include the "report every friction point in the instructions themselves" clause, and
the friction list gets fixed before registration, then gates re-run. Wired into Forge OS spine as
part of F5 PROVE.
