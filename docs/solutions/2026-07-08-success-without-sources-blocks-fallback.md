---
name: Success-Without-Sources Blocks the Healthy Fallback
problem_signature: a paid/primary research leg reports SUCCESS while producing zero sourced output — the dispatcher tests "returned without raising" instead of "cleared the provenance floor," so the healthy $0 fallback never fires and placeholder or citation-empty output ships wearing a success receipt
domain: research
tags: [research-dispatcher, fallback-chain, phantom-success, provenance-floor, citation-drift, placeholder-artifacts]
date: 2026-07-08
status: active
---

# Success-Without-Sources Blocks the Healthy Fallback

**Date:** 2026-07-08 · **Domain:** research infrastructure / dispatcher design · **Severity:** high (silent quality collapse + wasted spend)

## The Problem Shape

A primary/accelerator leg reports SUCCESS while producing **zero sourced output**. The dispatcher treats delivery as binary (success vs failure/exception), so the healthy $0 fallback never fires. Unsourced or placeholder output ships wearing a success receipt.

Appeared TWICE on 2026-07-08, independently:

1. **world_pulse_research.py** — Perplexity key dead (401) → `_manual_research_protocol` wrote "[RESEARCH NEEDED]" placeholder files and **exited 0**. `cos_prep.ensure_world_pulse` saw rc=0 and never ran the working Tavily fallback (`world_brief.py`). Bonus damage: the placeholder file's existence blocked same-day regeneration.
2. **research.py dispatcher** — Gemini Deep Research returned rich text with `citations=[]` (API schema drift, see below) → `validate_engine_text` passed, attempt logged SUCCESS "0 sources", 132 claims quarantined, status DEGRADED — but the native floor was `NOT_ATTEMPTED ("accelerator delivered")`. $0.50 spent for unusable output while a $0 leg that produces 19 sources sat idle.

Related prior card: `2026-07-07-zero-survivor-phantom-deliverable.md` (same family: phantom success at the orchestration layer).

## Root Causes

- **Delivery ≠ usability.** "Returned text without raising" is not success for research. Success = clears the provenance floor (min sources / min domains for the depth).
- **Placeholder artifacts are worse than no artifact.** A scaffold file with fake items satisfies existence checks, blocks retries, and silently ends the fallback chain.
- **API schema drift (specific instance):** Google's Interactions API (Gemini Deep Research) stopped populating the `citations` array and now embeds sources as **inline markdown links wrapped in `vertexaisearch.cloud.google.com/grounding-api-redirect/...` URLs**. A 56k-char max run carried 65 in-text URLs and an empty citations field.

## The Fix Pattern

1. **Floor-check before declaring delivery** (`research.py` step 3): after an accelerator "success," compare `source_count`/`unique_domains` against `DEPTH_MIN_SOURCES`/`DEPTH_MIN_DOMAINS`. Below floor → run the native floor anyway; better result wins; receipt names the rescue. Log accelerator spend even when the floor result is used.
2. **Never write placeholders; fail loudly** (`world_pulse_research.py`): zero sourced items → **no file written, exit 1** → caller's fallback chain actually fires. Deleted `_manual_research_protocol` entirely.
3. **Harvest + resolve drifted citations** (`deep_research_client._parse_final` + `_resolve_grounding_redirects`): if `citations==[]` but text has URLs, harvest inline (dedup, order-preserving), then follow grounding-redirect wrappers to real domains (capped at 40, fail-safe keeps wrapper). Verified: 65 wrappers → 32 real domains, replayed offline from the saved response without re-spending.
4. **401 = latch, not retry** (`deep_research_engine._search_and_extract`): first auth failure disables the dead client for the whole run (was 12×401 per topic) and drops to the Tavily leg.

## Verification Discipline That Caught It

Live proof runs with receipts, not code review: run each leg for real, read the RESEARCH RECEIPT (sources / domains / provenance% / cost / attempts). The receipt line `native → NOT_ATTEMPTED (accelerator delivered)` next to `0 sources` IS the bug, visible in one glance.

## Reuse Trigger

Any dispatcher/orchestrator with a paid-or-primary leg and a free-or-fallback leg: ask "what does the fallback condition actually test — that the primary *returned*, or that it *delivered something usable*?" If the former, this bug exists there.
