---
description: Systematic competitive intelligence system
---

> **Browser tools**: WebFetch handles most public marketing pages (Webflow / Framer / Next.js typically SSR their hero + pricing). Reach for Playwright (`mcp__playwright__browser_*`) when you need screenshot evidence for the brief, login-gated competitor content (LinkedIn profile facts, Substack analytics, paywalled research), multi-step navigation (drilling into pricing or checkout flows), or when WebFetch returns visibly degraded content. See `directives/browser-automation-routing.md`.

# Competitor Intelligence System

Build systematic competitive research for content strategy.

## Workflow

1. Load `skills/alex-content-science/genius.md`
2. Load `skills/alex-content-science/workflows/07-competitor-intel-system.md`
3. **Research phase** using tiered tool strategy from `directives/research-protocol.md`:
   - **Priority 1**: `mcp_perplexity-ask_perplexity_ask` — for competitive landscape queries
   - **Priority 2**: `search_web` — for individual competitor discovery and SERP analysis
   - **Priority 3**: `read_url_content` — read each competitor's about page, pricing page, and top content in full
4. Execute with user's niche, platform(s), known competitors, and goals
5. Deliver:
   - 3-tier competitor database (Direct, Adjacent, Aspirational Cross-Niche)
   - High-performance topic scan with ratio analysis
   - Opportunity mapping (High Demand + Low Competition)
   - Trend detection (rising, migrating, dying)
   - Strategic action plan with 30-day content calendar
6. Quality gate: 20+ accounts mapped, 3+ opportunity gaps, 30-day calendar with specific concepts

**Execution prompts**: before producing the deliverable, check `skills/alex-content-science/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
