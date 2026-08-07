---
name: ai-visibility-receipts-without-paid-tooling
problem_signature: "An offer module promises deterministic 'how AI engines describe your brand' receipts via Ahrefs Brand Radar, but the account is on a free plan — both brand-radar and site-explorer ai-responses endpoints return 'Insufficient plan', and a naive fallback (single live ChatGPT screenshot) collapses under prospect scrutiny because AI answers are non-deterministic"
domain: offer-delivery
tags: [aeo, geo, ai-search, proof-objects, ahrefs, zero-budget, proof-to-market]
date: 2026-07-18
status: active
session: "daa0cd59-783f-4b90-9746-40af72be63a3"
---

## Problem

The Proof-to-Market Sprint's AI-Search Shadow module was spec'd on Ahrefs Brand Radar pulls as its receipt mechanism. Empirical test (2026-07-18): `management-brand-radar-reports` AND `site-explorer-ai-responses-count` both return `MCP error: Insufficient plan` on Farrice's free Ahrefs plan. The adversarial reviewer independently flagged the deeper failure mode: even with a screenshot, a prospect re-runs the same ChatGPT query, gets a different answer, and the "proof" reads as a parlor trick. Small brands compound it — engines often return *nothing* about them, making a comparison table look hollow.

## Solution

Live-query receipts with three honesty rules baked into the spec (now in `_active/linkedin/02-offer/PROOF-TO-MARKET-OS.md`, AI-Search Shadow section):
1. **Pattern, not roll** — run each buying question 2-3 times per engine (ChatGPT, Perplexity, Google AI Overviews) and report the recurring names/descriptions, stated as a pattern with engine + date + exact prompt shown. Survives the prospect's own re-run.
2. **Invisible IS the finding** — scripted reframe for small brands: "the machine doesn't describe you wrongly; it doesn't describe you at all — every category question is answered with someone else's name." Turns the empty-result failure mode into the sharpest version of the pitch.
3. **Always resolve to positioning** — the module ends in a message implication, never an SEO to-do list, keeping it a diagnostic inside the strategy sprint rather than a standalone audit the council found no budget line for.

Cost: $0 (vs. Ahrefs paid tier). Upgrade path noted: a paid plan later adds Brand Radar as a deterministic layer on top, never a replacement for the live pattern read.

## Reuse Test

Any time an offer or content asset needs "what does AI say about X" evidence on zero tooling budget: pattern-of-3 live queries + dated screenshots + the invisible-is-the-finding script. Also the general shape: when a paid data source is plan-gated, test the gate empirically FIRST (one API call), then design the honesty rules that make the free path survive adversarial scrutiny — don't ship the module spec on an unverified dependency.
