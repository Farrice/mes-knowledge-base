---
date: 2026-07-21
session: go-v3 build
name: wired-but-never-loaded-prompts
problem_class: harness / wiring / load-path hole
domain: harness
status: proven
problem_signature: "every wiring audit passes green yet the operator says the prompts or contracts are not linked — the asset is linked on disk but never arrives in context, because the way it actually gets invoked (a bare slash command) skips the file the injection hangs off"
tags: [prompts, wiring, wrappers, load-path, audit, routing]
---
# Wired-but-never-loaded — an asset linked on disk is not an asset loaded at fire time

**Date**: 2026-07-21 · **Session**: /go-v3 build · **Domain**: system / prompt wiring / routing

## Problem

The Prompt Wiring OS linked 3,600+ v2 prompts into SKILL.md files (audit green, 0 fail) — but the load path had a hole: the prompt menu injects on **SKILL.md reads**, and slash-command wrappers execute `skills/<x>/workflows/<y>.md` directly without reading SKILL.md. Measured: **1,301 of 1,373 wrappers** pointing at prompt-carrying skills contained zero contract-load language. Result: Output Contracts existed everywhere and loaded almost nowhere — the operator felt "prompts aren't linked" while every wiring audit passed. Same class as /go v2: engines existed (`codex_operator_preflight`, `raw_intent_run_packet`) and go.md explicitly declined to call them, re-implementing compilation as prose.

## Solution

1. **Sweep deterministically**: scan every wrapper for a `prompts-v2`/`Output Contract`/`execution prompt` mention; count the gap before fixing (the number IS the diagnosis).
2. **Fix additively + idempotently**: append one standard footer line per gap wrapper directing the session to the skill's `prompts-v2/` dir and its Output Contract. Re-runnable; skip-if-present.
3. **For engines** (the /go case): reverse any "read for reference, don't ship its output" rule — the workflow calls the engine and ships its output as the reasoning surface; prose re-implementation is the defect.

## Re-solve guard

When wiring any asset class to another (prompts→skills, engines→workflows, cards→runners), test the **fire path, not the link path**: invoke the way the operator actually invokes (bare command, not SKILL.md read) and check the asset arrives in context. An audit that only checks disk-side linkage will stay green through total load failure. The drift guard (`verify_born_intent_drift.py`) + this sweep pattern are the standing checks.
