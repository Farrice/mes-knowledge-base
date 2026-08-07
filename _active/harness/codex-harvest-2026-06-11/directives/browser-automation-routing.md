# Browser Automation Routing

**Fires when**: Any task involves retrieving, observing, or interacting with live web content. Decides which tool — Playwright vs WebFetch vs Perplexity vs Gemini Deep Research vs Apify/Tavily — is correct for the situation.

**Why this exists**: Playwright MCP shipped in `.mcp.json` on 2026-04-25 but the agent stack still defaults to WebFetch + Perplexity even when JS-rendered pages, login walls, or visual evidence make those tools inadequate. Repo-wide audit (2026-04-30): ~178 WebFetch references, ~58 Perplexity, ~15 Playwright. The capability exists; the invocation patterns didn't. This directive fixes the routing layer.

**Sister directive**: [`browser-automation-safety.md`](browser-automation-safety.md) governs *how* to run browser actions safely (Tier 1 reads / Tier 2 confirmations / credentials / audit log). This directive governs *when* to reach for browser automation in the first place. Use both together — never one without the other.

---

## Core Principle

The web tools are **complements, not substitutes**.

| Tool | What it's for |
|---|---|
| **Playwright** (`mcp__playwright__browser_*`) | Interactive or visual web work — JS-rendered pages, login-gated content, screenshots, multi-step navigation, form interaction |
| **WebFetch** | Static text retrieval — public articles, blog posts, plain HTML pages |
| **Perplexity ask / search** | Single-claim fact checks with citations, narrow synthesis questions |
| **Gemini Deep Research** | Foundation research, strategic intelligence across many sources (per [`research-protocol.md`](research-protocol.md)) |
| **Tavily** | Free structured search supplementation |
| **Apify** | Scaled scraping where Playwright would be too slow or expensive |

The wrong choice has a real cost: WebFetch on a JS-heavy SPA returns the empty shell HTML and produces a hallucinated summary. Perplexity on a question that needs primary-source verbatim quotes returns secondhand paraphrase. Playwright on a static blog post is overkill. Match the tool to the surface.

---

## Decision Matrix

| Situation | Primary Tool | Fallback |
|---|---|---|
| Static HTML article / blog / SEO page | WebFetch | Perplexity ask |
| Modern marketing site (Webflow / Framer / Next.js) — hero copy, pricing, public content | **WebFetch first** (most modern marketing sites SSR their hero/pricing for SEO) | Playwright if WebFetch returns near-empty content |
| Truly client-rendered SPA (dashboard, app interior, no SSR) | Playwright `navigate` + `evaluate` | Apify if scaled |
| Infinite scroll / lazy-loaded feeds (X, Instagram, TikTok) | Playwright `navigate` + scroll + `evaluate` | n/a |
| Login-gated content (LinkedIn, Substack analytics, Notion shared workspace, MLS) | Playwright + persistent profile | Manual login resume per safety protocol |
| Visual evidence required (screenshots for briefs, design refs, competitor sales pages) | Playwright `take_screenshot` + `snapshot` | WebFetch + describe (degraded) |
| Multi-step navigation (drill into 3 pages, extract data) | Playwright | n/a |
| Form submission / state change (post, send, submit, buy) | Playwright (gated by Tier 2 confirmation per safety protocol) | n/a |
| Single-claim fact check | `search_web` / Perplexity ask | WebFetch |
| Foundation research (strategy briefs, ICP, deep dives) | Gemini Deep Research first (per `research-protocol.md`) | Perplexity sonar-deep-research |
| Cross-source synthesis (10+ sources) | Gemini Deep Research / `swarm-research` | n/a |
| Scaled scraping (100+ URLs, structured data extraction) | Apify | Tavily / Playwright batch |

---

## Triggers — When Playwright SHOULD Fire

Positive signals that browser automation is the right tool:

1. **User language**: "see," "screenshot," "verify on the actual site," "scrape," "monitor," "navigate," "take a look at," "check what they say on their pricing page"
2. **Surface signals**: Target site is a truly client-rendered app (no SSR — common for dashboards, app interiors, Notion shared workspaces, some e-commerce checkout flows). **Calibration note (2026-04-30 functional test)**: most modern marketing sites built on Webflow / Framer / Next.js DO server-render their hero and pricing pages for SEO, so WebFetch usually retrieves them fine. Don't assume "JS framework = needs Playwright" — try WebFetch first, escalate when content is genuinely missing or visibly degraded.
3. **Auth signals**: LinkedIn profile content, Substack analytics dashboards, Notion shared workspaces, MLS/realtor portals, paywalled research sites. WebFetch will return a login wall HTML page; Playwright with a persistent profile returns the actual content.
4. **Evidence requirements**: Brief or deliverable demands verbatim quotes, screenshots, or visual proof. "Trust me, this is what they say" fails the proof bar; "here is the screenshot with the URL" passes.
5. **Multi-step task**: The task requires drilling 2+ pages deep (homepage → pricing → checkout flow) or interacting with UI state (open dropdown, click tab, scroll-load).

If 2+ of these signals are present, Playwright is the correct primary tool.

---

## Triggers — When Playwright Should NOT Fire

Negative signals — reach for a lighter tool instead:

1. **Pure static text suffices** — a blog post, an SEO article, a public PDF — WebFetch is faster and cheaper.
2. **Quick fact check** (single claim, single source) — `search_web` or Perplexity ask. Don't spin up a browser for one fact.
3. **Budget-sensitive scale work** (50+ similar URLs to scrape) — Apify is purpose-built; Playwright will be slow.
4. **No interactive surface needed** — if the task is "summarize this article," not "navigate this dashboard," WebFetch wins.
5. **Pure synthesis** — if the deliverable is "what does the literature say about X," that's Gemini Deep Research, not Playwright.

---

## Cost & Blast-Radius Reminder

Playwright actions split into two safety tiers per [`browser-automation-safety.md`](browser-automation-safety.md):

- **Tier 1 (read-only)** — `navigate`, `screenshot`, `snapshot`, read-only `evaluate`, scrolling, hovering. Free to execute. No confirmation. This directive's "should fire" signals all map to Tier 1 actions.
- **Tier 2 (state-changing)** — posting, messaging, submitting, purchasing, account changes. Require explicit confirmation per the safety protocol. This directive does not redefine that flow — defer to safety protocol entirely.

Cost-wise, Playwright via the MCP server runs locally, so per-call cost is effectively zero (browser CPU + bandwidth only). The real cost is *latency* — a Playwright navigate + screenshot can take 3-8 seconds vs WebFetch's <1 second for static pages. Match the tool to the situation, not the budget.

---

## Integration With Existing Protocols

This directive sits alongside, not above or below, three existing routing layers:

1. **[`research-protocol.md`](research-protocol.md)** — owns "depth + synthesis" routing (Quick / Standard / Deep, Gemini-first priority, Perplexity-as-fallback). Cross-reference for any task that's primarily *research* (multi-source synthesis with citations) rather than *interaction* (navigate, screenshot, verify on site).
2. **[`browser-automation-safety.md`](browser-automation-safety.md)** — owns Tier 1 / Tier 2 confirmation flow once Playwright is chosen. Always link; never duplicate.
3. **[`recall-grounding-protocol.md`](recall-grounding-protocol.md)** — owns the Tier 1.5 silent grounding pre-load. Recall fires *before* tool selection; this directive fires *during* tool selection.

When a task is ambiguous (e.g., "research what competitors charge"), apply both research-protocol (Gemini Deep Research for synthesis) and this directive (Playwright if pricing is on JS-rendered pages or behind auth). They compose: Gemini synthesizes the landscape, Playwright pulls the verbatim primary-source pricing for proof.

---

## Subagent Tool Access

Subagents inherit Playwright access via their `tools:` frontmatter. As of 2026-04-30, the following production subagents in `.claude/agents/` have Playwright wired:

- `competitive-intel` — primary-source competitor research, screenshot evidence
- `deep-research` — login-gated and JS-rendered source access
- `fact-verifier` — primary-source verification of public-figure claims
- `icp-deep-canvasser` — live forum / Reddit / Quora navigation
- `expert-extractor` — live channel metadata and podcast platform extraction
- `synthesis-engine` — revisit live sources during cross-source synthesis
- `swarm-orchestrator` — needs full tool surface to delegate appropriately

Subagents NOT given Playwright (no clear value-add): `prose-doctor`, `content-finalizer`, `master-copywriter`, `brand-system-builder`, `adversarial-reviewer`. These can be retrofitted later if a use case appears.

---

## Future Capability — Computer Use API

Anthropic's Computer Use API offers full OS-level control (mouse, keyboard, arbitrary applications) beyond the browser. **Not currently integrated** into this system. Surface as a deferred option for the day a workflow needs to control desktop applications (native Notion, design tools like Figma desktop, accounting software, native AI tools) rather than the browser.

When to revisit:
- A workflow requires interacting with a native macOS app that has no useful web equivalent.
- A skill consistently fails because the necessary surface is desktop-only (e.g., advanced Figma operations, native Notion offline mode, certain creative tools).
- Cost-benefit shifts (Computer Use adds a new security surface, separate API budget, and per-call cost — not free).

Until then: Playwright covers ~95% of the live-web work agents need; reach for it first.

---

## Quick Reference Card

| If the task is... | Use... |
|---|---|
| "Read this article" (URL is a public blog post) | WebFetch |
| "What's their pricing?" (URL is a SaaS pricing page) | Playwright `navigate` + `evaluate` (likely JS-rendered) |
| "Screenshot their hero section for the brief" | Playwright `take_screenshot` |
| "Verify this LinkedIn profile fact" | Playwright + persistent profile (login-gated) |
| "What does the research say about X?" | Gemini Deep Research |
| "Quick fact check on this stat" | Perplexity ask / `search_web` |
| "Scrape 100 product pages" | Apify |
| "Post this to LinkedIn" | Playwright (Tier 2 — confirmation required per safety protocol) |
| "Navigate this dashboard and extract metrics" | Playwright multi-step |
| "Synthesize competitor positioning from public content" | Gemini Deep Research + Playwright for verbatim quotes |
