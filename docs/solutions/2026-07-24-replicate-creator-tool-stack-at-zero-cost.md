---
name: replicate-creator-tool-stack-at-zero-cost
problem_signature: "A YouTube creator demos a high-value agent stack built on paid third-party APIs; how to replicate and surpass it without new subscriptions"
domain: system
tags: [extraction, apify, notion, playwright, tavily, ad-spy, scraping, zero-cost, riley-brown]
date: 2026-07-24
status: active
session: "riley-brown extract-forge 2026-07-24"
---

## Problem

Riley Brown's "Codex Is Basically Running My Company Now" demos 9 marketing agent workflows on a paid stack: ScrapeCreators API (credits), Foreplay ($175/mo Workflow plan for Spyder), Paper.design, Firecrawl, Buffer, plus a Chorus-app agent. Farrice wanted the capabilities replicated and surpassed in the Antigravity harness with zero new spend — and the full picture of what the creator left out.

## Root Cause (of the apparent cost)

Creator tool stacks are conventions, not requirements. Each paid tool maps to a *capability* (social scraping, ad intelligence, site scraping, creative variation, staging), and the harness already owned an equivalent for every one — some literally the same vendor via a cheaper door (ScrapeCreators publishes its actors on Apify, already inside the $29/mo budget with 10 sc-* actors wired in apify_client.py).

## Approach That Worked

1. **Inventory before buying.** Map each demoed tool → capability → owned equivalent BEFORE pricing anything: ScrapeCreators→Apify sc-* actors; Foreplay→Meta Ad Library via read-only Playwright (his own "longest-running ad = winning ad" heuristic uses a field the free Ad Library exposes: "Started running on"); Firecrawl→Tavily+Playwright; Paper.design→Dara/Fantastic Studio/Canva/Higgsfield; Buffer→Typefully free tier (Buffer's public API is closed anyway); Gmail/Drive/Cal.com→connected MCP + free-tier APIs.
2. **Watch the frames, not just the transcript.** The visual layer held everything the audio glossed: skills are real multi-file Python pipelines, the creator→skill mechanism is Codex's `New workflow`/`Memory→AGENTS.md` commands, ~7 API keys sit behind "just ask" demos.
3. **PoC gate per capability.** Each build proved itself live before shipping: 2 scraped posts with transcripts in the Social Intelligence Notion DB ($0.01), 5 real AG1 ads ranked by runtime (176-day winners) at $0.
4. **Integration-owned Notion DB** (classic model, created via REST under the shared hub page) per the notion-ai-database-gotcha card — writable on day one.
5. **Parallel-tool draft ≠ ground truth.** A Codex session had pre-built the skill from half the source; the fix was correct-against-acquired-ground-truth (MES + visual notes + full transcript), not rebuild — ~15 fabrication classes removed while keeping the sound structure.

## Dead Ends

- Foreplay API at $175/mo — unnecessary; runtime ranking replicates the core signal free.
- Raw HTTP to Meta Ad Library — 403 bot-blocked; a real Playwright browser context is the only viable free route.
- Search-result "sibling videos" as corpus — two were other channels entirely; corpus enrichment must verify the uploader, not trust title matching.

## Verification

Blind pass EVAL-055 PASS (model-judged, Farrice pass pending) · skill_auditor 6/6 · renaissance_audit 0-fail · finalize composite 8.33 · both PoCs independently re-queried from Notion. Total incremental spend: $0.01.

## Reusable Rule

Before any "we need tool X" purchase triggered by creator content: (1) name the capability, (2) grep the harness for an owned equivalent (apify_client.py ACTORS, MCP connectors, Tavily, Playwright), (3) check whether the paid tool's core signal is derivable from public data, (4) PoC the free route with a per-run ceiling before considering the subscription.
