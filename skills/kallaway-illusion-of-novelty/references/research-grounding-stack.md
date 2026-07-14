---
description: The live-research & signal stack that replaces "writing from internal context" — our replicable equivalent of Kallaway's Sandcastles.ai. Maps the real tools we already have to the three jobs Sandcastles does (trend discovery, fact/proof harvest, what's-working/winner analysis), with the protocol for Phase 0.5 (Research & Ground) and Phase 8 (Calibrate) of /novelty-engine.
---

# Research-Grounding Stack — Our Sandcastles Equivalent

> Kallaway's edge is not the framework alone — it is that **Sandcastles.ai feeds the framework live signal**: what's trending, what's real, what's actually winning. An engine running on internal context only is half the system. This file is the other half: the real tools we already have, mapped to what Sandcastles does, so `/novelty-engine` grounds every build in external reality.

## What Sandcastles does → what we use instead

| Sandcastles job | What it produces for Kallaway | Our equivalent (already available) |
|---|---|---|
| **1. Trend / topic discovery** | What's new and moving right now → New Reveal + honest Urgency | `/hunt-trends` · `mcp__perplexity-ask__perplexity_search` (recency filter) · `WebSearch` · `tavily-search` (time-range) · `mcp__recall__search` (prior zeitgeist cards) |
| **2. Fact / proof harvest** | Real studies, stats, numbers, named sources → Bullseye Proof, grounded claims | `execution/research.py` (Gemini-first, **Honest Receipt** per result) · `mcp__perplexity-ask__perplexity_research` · `tavily-research` / `tavily-extract` (primary-source pull) · `WebFetch` · `mcp__recall__search` |
| **3. What's-working / winner analysis** | The hooks/angles/formats actually performing in the niche → angle selection + the pattern loop | **Apify** social scraping (`directives/apify-usage-policy.md`, $29/mo) · `mcp__playwright__*` (manual high-performer pulls) · `perplexity_search` ("top performing LinkedIn posts about X") · then `/novelty-pattern` on the pulled set |

## The protocol — Phase 0.5 (Research & Ground)

Run BEFORE building. Produce a one-page **grounded brief**:

1. **Trend scan** → 3–6 genuinely-recent shifts in the topic (dated). Each is a candidate New Reveal and a possible honest Urgency window. Prefer the freshest real shift over an invented "new angle."
2. **Fact/proof harvest** → the real studies/stats/sources that can carry proof, each labeled **VERIFIED / LIKELY / UNCONFIRMED** with its source URL. Nothing unlabeled enters the draft. This is where the honesty spine is enforced at the source, not after the fact.
3. **What's-working scan** → 5–15 currently-performing posts/hooks/formats in the niche (with engagement signal where scrapeable). Extract the *pattern* (what the winners share), not just examples.

Output: `trend → verified-facts → competitor-pattern`, handed to Phase 1 (angle) and Phase 2 (build). A New Reveal anchored to a real recent shift, proof drawn from a real labeled source, and an angle informed by what's actually winning is the difference between this engine and an AI guessing from its own priors.

## The protocol — Phase 8 (Calibrate, close the loop)

Feed `/novelty-pattern` REAL data:
- **Own data:** the account's winners-vs-losers (transcripts + metrics) via Apify export or platform export.
- **Outside-in data:** the Phase 0.5 competitor-winner set, when own history is thin.
Extract the niche-specific words/structures/proof-rungs that win, fold them back into the build. Each run compounds — exactly the Sandcastles flywheel.

## Cost / budget posture (respect the gates)
- **Free / cheap, default-on:** `WebSearch`, `WebFetch`, `mcp__recall__search`, Perplexity MCP search/ask (within the $30/mo Perplexity budget), `/hunt-trends`.
- **Budget-gated, use with intent:** `execution/research.py` (Gemini Deep Research, $10 ceiling — PRIMARY for deep facts per `feedback_research-priority-gemini-primary.md`), `perplexity_research` (slower/deeper), **Apify** ($29/mo, social scraping — the closest thing to Sandcastles' data pull).
- Prefer MCP/web tools over Bash-wrapped paid calls so the cost gate stays clean; surface any real paid spend at autopilot's G2.

## What to BUILD next (to get all the way to a Sandcastles-grade asset)
The pieces above cover trend + fact + manual winner-pull today. To make it a true standing asset (the user's goal), the gap is a **deterministic social-data pipeline**:
- A small `execution/` script (e.g., `social_signal.py`) that, given a niche/handle set, pulls recent posts + metrics via Apify, normalizes to `{transcript, hook, format, saves/likes/comments, date}`, and writes a CSV the `/novelty-pattern` loop reads directly — our `Bulk Analyze`.
- Optional: a scheduled (launchd) weekly pull so the winner/loser corpus compounds without manual runs (pair with a deterministic backstop per `feedback_ai-memory-dependent-observability.md` — never AI-invocation-dependent).
- This is the one net-new tool worth building; everything else is composition of what we already have.

> Bottom line: we do not need Sandcastles. We need to *point the tools we already have* at the three Sandcastles jobs, in this order, every real run. The engine now does.
