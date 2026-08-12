---
name: Notion Second Brain local-first reliability repair
problem_signature: Notion repeatedly errors during Codex finalization while the intended Simon Library is absent from local retrieval and session closeouts never reach Session Memory
domain: system
tags: [notion, second-brain, memory, local-first, dns, regression, mirror]
date: 2026-08-11
status: active
---

# Notion Second Brain Local-First Reliability Repair

## Problem

Codex runs repeatedly reported `api.notion.com` name-resolution errors, including
finalizations invoked with `--skip-notion`. At the same time, the documented
Second Brain claimed Session Memory was active and queryable.

## Root causes

1. `log_performance.get_baseline()` queried Notion during every regression check.
   `--skip-notion` skipped the write but not that read.
2. Codex's sandbox cannot resolve `api.notion.com`; the macOS nightly launchd job
   can and was succeeding.
3. `memory_facade.py` did not query `notion_mirror`, so 1,113 locally mirrored
   Notion pages existed but were not part of the declared unified recall path.
4. `mirror_notion.py` targeted the older operational databases, not the five
   integration-owned Simon Intellectual Library databases.
5. Session Memory closeout delivery was documented as optional Phase 4 and never
   wired. The live database held only three setup rows.

## Repair

- Regression baselines now read `.agent/performance-log.jsonl`, the declared
  local source of truth.
- Notion is a first-class `memory_facade` source backed by the local mirror.
- The nightly registry includes Knowledge Entries, Experts, Sources, Skills &
  Playbooks, and Session Memory, while preserving the older operational set.
- Notion requests have a bounded timeout and structured network errors.
- Authority docs now distinguish the live library from the unwired automatic
  session-closeout path.

## Verification

- Live integration token and all five Simon database schemas passed read-only API checks.
- Expanded ten-database mirror dry-run: ten successes, zero errors.
- Live counts: 84 Knowledge Entries, 12 Experts, 12 Sources, 13 Skills, 3 Session Memory rows.
- `verify_notion_second_brain_reliability.py`: 7 pass, 0 fail.
- Network-free `memory_facade --sources notion` returned real mirrored Notion records.

## Remaining policy gate

Automatic Session Memory delivery cannot be enabled safely until Farrice chooses
the privacy mode: all distilled closeouts, explicit approval per closeout, or
automatic only for closeouts marked safe. Do not infer that decision from the
technical repair.
