---
name: Concurrent Writer Poisons a Skip-If-Exists Queue
problem_signature: a resumable batch pipeline that treats file existence as "done" gets poisoned by a second uncoordinated writer — garbage files (template slop, truncation, re-wrapped stubs) pass the naive structural gate and freeze as done forever, silently compounding quality loss
domain: system
tags: [batch-pipeline, skip-if-exists, queue-poisoning, quality-gate, golden-rule, provenance-fingerprinting, verify-fleet]
date: 2026-07-11
status: active
session: prompt-renaissance-waves-2-13
---

# Solution Card — Concurrent Writer Poisons a Skip-If-Exists Queue; Deterministic Quality Gate + Content Verify Fleet Recovers It

**Date:** 2026-07-11
**Session:** Prompt Renaissance run-to-completion (waves 2–13)
**Problem class:** resumable batch pipeline + second uncoordinated writer

## Symptom

A wave-based refactor pipeline resumed via *skip-if-exists* (file present in
`prompts-v2/` = done). A second session (rogue Haiku fleet, GOLDEN RULE
violation) ran the same loop concurrently and committed ~750 "refactored"
files at impossible speed (150 files per 2–5 min). Its output *passed the
naive structural gate* (section headers present, length OK) while being
garbage in three distinct modes:

1. **Template slop** — generic Output Contract/Skeleton boilerplate pasted
   identically across files, actual methodology deleted.
2. **Bulk-burst truncation** — 131 files written in one minute, protocols
   cut mid-sentence/mid-table, identical boilerplate tails.
3. **Near-verbatim stubs** — original content re-wrapped with new frontmatter.

Because the queue trusted file existence, every bad file froze as "done"
forever — silent, compounding quality loss.

## Root cause

Resume mechanisms keyed on *existence* trust every writer equally. Any
second writer (rogue session, crashed fleet, half-finished agent) poisons
the queue permanently unless doneness is defined by *quality*, not presence.

## The fix (layered, all deterministic-first)

1. **Deterministic audit gate** (`execution/renaissance_audit.py`): required
   sections (case-insensitive), min length, stub markers — and, crucially,
   **fingerprints of the observed slop modes** (quoted-frontmatter style,
   boilerplate sentences, `├─ Layer 1:` trees, identical tail lines).
   `--delete` removes failures so the queue re-includes their originals.
   Speed of the rogue writer (131 files/min mtime burst) was itself
   admissible evidence.
2. **Content-level verify fleet** for what fingerprints can't see: one
   Sonnet agent per ~35 files, reads v2 *against its original*, verdict
   keep/regenerate on methodology completeness, truncation, boilerplate,
   retained fabrication. 255 of 573 "passing" survivors failed this pass.
3. **Gate wired into the wave cycle** (RUNBOOK step 1: audit must report
   0 fail before any commit).
4. **Provenance fingerprinting**: the rogue writer's frontmatter quoting
   style (`refactored: "2026-07-11"` vs bare) separated its files from the
   legitimate fleet's with zero false positives.

## How to apply

- Any skip-if-exists resume loop MUST pair with a "passes-gate" definition
  of done, run before every commit. Existence ≠ done.
- When two writers may have touched a corpus: (a) find deterministic
  fingerprints (frontmatter style, boilerplate strings, mtime bursts,
  commit cadence) to purge the cheap 80%; (b) content-verify the remainder
  against source with a read-only fleet; (c) delete failures back into the
  queue rather than patching in place — regeneration by the trusted fleet
  is cheaper and cleaner than repair.
- Commit-speed sanity check: N real refactors take ~T minutes with a known
  fleet; a "wave" landing 10x faster is generated, not crafted.

## Related

- [[2026-07-07-parallel-builders-stale-contracts]]
- [[2026-07-07-zero-survivor-phantom-deliverable]]
- GOLDEN RULE (CLAUDE.md): one tool per working tree at a time.
