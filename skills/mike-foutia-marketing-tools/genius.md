# Mike Foutia — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## How to Use This Skill (Model Calibration)

These patterns are intuition primitives for scoping and building marketing automation, not a checklist to recite. Mike's genius is judgment about *where the line is* — what to automate aggressively and what to leave alone — not a fixed sequence of steps to announce.

- Do NOT narrate the machinery. Never write "Applying Layer 1, Layer 2, Layer 3" or "per the Automation Boundary Heuristic" inside a deliverable. Run the layers; don't label them.
- Do NOT default to building software. Mike's instinct when a client describes a pain point is "what's the smallest internal tool that kills this specific pain" — not "what SaaS product could this become." Scope creep away from that instinct is the tell you've lost the thread.
- His texture is practitioner-plain, not developer-jargon. He explains automation the way a marketer explains a media buy, not the way an engineer explains an architecture diagram. Keep deliverables readable by a non-technical ad-agency owner.
- The test: would Mike recognize this as a tool he'd actually ship to a client this week — or does it read like generic AI-automation vocabulary stapled onto a dashboard? If it's the second, rebuild: strip it back to the pain point, the layer that's missing, and the brand bible that should have been loaded first.
- Polish runs the wrong direction here: an over-engineered, fully-automated system (especially one that automates creative video) is the failure mode, not an underbuilt one. Mike's own line applies past the boundary — AI is "really good at getting you to the mean," which is safe, generic, and wrong for a brand that needs to stand out.

---

## Genius Patterns

## Content Assessment

```
Source: Interview transcript (~25 min) — Marketing Against The Grain podcast
Expert: Mike Foutia — Marketing tool builder, vibe-coded app developer for e-commerce brands and ad agencies
Transcribed by: Merlin AI
Domain: AI marketing automation + social media intelligence + creative brief generation
Depth Tier: Standard — single deep-dive interview with live demo and strategic framing
Genius Patterns: 6 identified
Hidden Knowledge: 5 tacit insights detected
Existing Overlap: Seena Rez (TikTok), Cardinal Mason (ad copy), PJ Accetturo (AI video)
```

## Executive Summary

- **Core Genius**: Building end-to-end AI workflows that convert social media trend research into deployable ad briefs in under 15 minutes — bridging the gap between organic virality and paid creative strategy.
- **What Makes Him Different**: Not an ad strategist or a developer — he's the rare intersection of both. Builds point-of-view-driven research tools that encode expert judgment into repeatable workflows, so teams get expert-grade analysis at button-click speed.
- **Deployable Skills**: Automated trend scraping → AI video analysis → brand-contextualized brief generation → creative volume pipeline.
- **Hidden Knowledge Captured**: The three-layer data escalation model, the automation boundary heuristic for knowing when NOT to automate, and the taste profile injection pattern.

---

## Genius Patterns

### 1. Three-Layer Research Escalation
- **What He Does Unconsciously**: Treats trend research as a data pyramid — Layer 1 is raw metrics (views, likes, comments), Layer 2 is semantic analysis of what's actually happening in the video (hooks, angles, pain points), Layer 3 is synthesized output (creative brief). He never jumps layers.
- **Executable Behavior**: Always collect raw data first (scrape → metrics), then run AI semantic analysis on the top performers, then synthesize into deliverable format. Never skip from raw data to brief.
- **Deployment Context**: Any research-to-action pipeline — competitive analysis, content calendars, product research.
- **Success Metric**: The brief contains specific proof (video URLs, exact hooks, actual data points) rather than generic category recommendations.
- **Source Benchmark**: Mike frames the whole pipeline around the "from nothing to brief in 15 minutes" benchmark (`extractions/mike-foutia-marketing-tools/extraction-report.md`, Genius Pattern 1, Success Metric).

### 2. Brand Bible Context Injection
- **What He Does Unconsciously**: Before generating any creative output, he loads a "brand bible" — tone of voice, target audience pain points, brand background, customer persona — as system context. The output is never generic AI slop because it's always filtered through brand-specific constraints.
- **Executable Behavior**: Create a structured brand context document (tone, audience, pain points, differentiators, winning ad patterns) and inject it as system context before any generation step. The template itself is AI-generated but human-refined.
- **Deployment Context**: Any AI content generation pipeline — ad briefs, social posts, email sequences, landing pages.
- **Success Metric**: A non-expert reading the output can immediately identify which brand it's for without being told.

### 3. Organic-to-Paid Bridge
- **What He Does Unconsciously**: Uses organic social media data (TikTok trending videos) as the strategic input for paid ad creative. The insight: organic virality is free market research. What's trending organically reveals what messaging, hooks, and angles resonate — then you fast-follow with paid ads using those proven patterns.
- **Executable Behavior**: Scrape trending organic content in your niche → identify winning hooks/angles/pain points → generate paid ad briefs that leverage those validated patterns → test at volume.
- **Deployment Context**: Facebook/Meta ad campaigns, TikTok ads, YouTube pre-roll, any performance marketing.
- **Success Metric**: Ad creative is based on proven organic patterns rather than guesswork; creative velocity increases because you're not starting from zero.
- **Source Benchmark**: The "Viral Hook Deconstruction Brief" exemplar cites the actual organic proof point behind this bridge: 5.2M views, 350K likes, 12K comments on the source TikTok (`references/exemplars.md`, Exemplar 1).

### 4. Automation Boundary Heuristic
- **What He Does Unconsciously**: Draws a sharp line between what should be automated (text-based research, writing, analysis, brief generation) and what should not (video creation, highly creative visual assets). His heuristic: if the AI output is "going to be a good reflection on your brand" at >95% reliability, automate it. If not, keep the human deeply in the loop.
- **Executable Behavior**: Before building any automation, ask: "Will the output be consistently brand-safe at scale?" Text research and writing → yes, automate. AI video and UGC → no, keep human-in-loop. Static ad images → maybe, with human revision step.
- **Deployment Context**: Any decision about where to invest in automation vs. where to invest in human creative time.
- **Success Metric**: Zero brand-damaging outputs escape the system. Automation investment generates positive ROI rather than expensive mediocrity.

### 5. Non-Coder Builder Pattern (Vibe Coding for Marketing)
- **What He Does Unconsciously**: Uses Claude Code and similar AI-assisted development tools to build fully functional internal marketing tools without traditional development skills. Started in N8N (low-code), then "graduated" to vibe-coded custom apps. This lets him build bespoke tools perfectly shaped to a client's specific workflow.
- **Executable Behavior**: Prototype in a low-code tool (N8N, Make), identify the limitations that matter, then vibe-code a custom version using Claude Code / Cursor that removes those limitations. Ship internal tools, not SaaS products.
- **Deployment Context**: Building internal marketing tools, client deliverables, workflow automation, custom dashboards.
- **Success Metric**: The tool does exactly what the team needs with zero unused features. Build time is hours, not weeks.

### 6. Creative Volume as Competitive Moat
- **What He Does Unconsciously**: Understands that Meta's algorithm rewards creative volume — specifically "net new concepts" — and builds his entire system around maximizing the velocity of brief-to-ad pipeline. The insight isn't just "make more ads" — it's that the speed of the research-to-creative pipeline is the actual competitive lever.
- **Executable Behavior**: Measure your creative pipeline by throughput (briefs per week, concepts tested per month). Build systems that compress the research → brief → ad cycle from days/weeks to minutes/hours. Stack automation at every non-creative bottleneck.
- **Deployment Context**: Any Meta/Facebook advertising operation, TikTok ads, performance marketing at scale.
- **Success Metric**: Creative testing velocity increases 5-10x; winning concepts are identified faster because more concepts are tested.

---

## Hidden Knowledge

### 1. The Comment Mining Goldmine
Mike specifically calls out comments as containing "a lot of gold" — especially for product-based content. The hidden insight: comments reveal objections, desired features, competitor weaknesses, and language patterns that your prospects actually use. Most marketers watch the video; the real intelligence is in the comment section. Gemini can mine hundreds of comments in seconds and cluster them by theme.

### 2. The Taste Profile as Strategic Guardrail
The host (Kip) references a "taste profile" concept — all the data about your customers matched with brand style and brand voice. Mike's tool operationalizes this: the brand bible isn't just "nice to have" context — it's the strategic guardrail that prevents AI from producing generic output. Without it, you get mean-reversion content. With it, you get brand-differentiated content.

### 3. Historical Ad Data as Context Layer
Mike mentions (and the host elaborates) that another context layer should include "what does a winning ad look like for our company based on our historical data." The hidden knowledge: the best brief-generation systems aren't just forward-looking (what's trending) — they're also backward-looking (what's already worked for us). Layering historical performance data on top of trend data on top of brand context produces dramatically better briefs.

### 4. The "Mean Reversion" Problem
Mike articulates a critical AI insight: "AI is really good at getting you to the mean." In marketing, success requires *deviating* from the mean. This means AI tools should be designed to handle the commodity work (research, first drafts, formatting) while explicitly preserving space for human creativity to push outputs away from average.

### 5. The Phase-Based Client Expansion Model
Mike's clients start by asking for trend research automation, then ask "what can you do for me next?" — extending to brief generation, then static ad creation, then potentially video. The hidden business model insight: build the first tool for the pain point they already know they have, then expand into adjacent automation as trust builds. Each phase funds the next.

---

## Anti-Patterns

> Grounded in `extractions/mike-foutia-marketing-tools/extraction-report.md` (Marketing Against The Grain podcast interview transcript, ~12,701 bytes, read in full) and cross-checked against this file's own Genius Patterns / Hidden Knowledge sections above. Full claim-by-claim audit: `references/source-ledger.md`.

- **Never skip from raw data straight to a brief.** Mike's system enforces three escalating layers — metrics → semantic analysis → synthesis — because "he never jumps layers" (extraction-report.md, Genius Pattern 1, Marketing Against The Grain podcast interview). Skipping the semantic layer produces briefs with generic category recommendations instead of the "from nothing to brief in 15 minutes" benchmark he holds himself to.
- **Don't build a SaaS product when the client needs an internal tool.** Mike explicitly ships "internal tools, not SaaS products" — bespoke builds shaped to one team's workflow, not general-purpose software (extraction-report.md, Genius Pattern 5 "Non-Coder Builder Pattern", podcast interview).
- **Don't automate creative video production at scale.** The automation boundary heuristic draws the line at text/research (automate aggressively) vs. visual creative production (keep human-in-the-loop) — extraction-report.md's Market Signals section is explicit that "AI video is NOT ready for full automation" (podcast interview, Market Signals section).
- **Don't start a non-coder build in N8N today.** Mike "explicitly says he would NOT learn [N8N] if starting today," after four months of reluctant use before switching to vibe coding (extraction-report.md, Hidden Knowledge "N8N is a Dead End for Non-Coders", podcast interview).
- **Never generate a brief without loading the brand bible first.** Skipping brand-context injection is the top failure mode: "without it, you get mean-reversion content" (this file, Hidden Knowledge #2 "The Taste Profile as Strategic Guardrail", podcast interview) — see the "Generic AI-Generated Brief" Anti-Exemplar in `references/exemplars.md` for exactly what this looks like shipped.
- **Don't trust a first AI draft at face value.** Mike's own diagnostic — "AI is really good at getting you to the mean" — means every generated brief needs a human pass explicitly aimed at pushing away from the generic (this file, Hidden Knowledge #4 "The Mean Reversion Problem", podcast interview).
- **The recognition test**: would Mike recognize this as a workflow he'd actually run, or does it read like generic AI-automation vocabulary stapled onto a dashboard? If the brief has no organic-content citation, no comment-mined objection, and no brand-bible fingerprint, he wouldn't recognize this as his (cross-checked against this file's Signature Moves section below and extraction-report.md's Executive Summary, podcast interview).

---

## Methodology

### The TikTok-to-Ad-Brief Pipeline

**Stage 1 — Trend Scraping**
- Define niche keyword(s)
- Set date range and result volume
- Use Apify API (or equivalent scraper) to pull TikTok videos matching criteria
- Display results with full metrics: views, likes, comments, shares

**Stage 2 — AI Video Analysis**
- Select high-performing videos from scrape results
- Pull transcript (if available)
- Send video to Gemini (multimodal) for semantic analysis
- Extract: visual hook, proof/demonstration, theme, funnel stage, messaging angle
- Mine comments for: questions, complaints, praise, language patterns

**Stage 3 — Brand Context Loading**
- Load pre-built brand bible: tone, audience, pain points, differentiators
- Optionally load historical ad performance data
- Optionally load competitor analysis

**Stage 4 — Brief Generation**
- Combine video analysis + brand context + brief template
- Generate creative brief: campaign name, objective, target audience description, pain points, key message, creative direction
- Human reviews and refines (expected 80% accuracy on first draft)

**Stage 5 — Creative Production** (future state)
- Brief feeds into ad creation tools (Nana Banana, Weevie, VO for video; static image generators for display)
- Multiple variations generated per concept for A/B testing
- Human quality check before deployment

---

## Applied Intelligence

### Capability Unlocks

- **Trend-to-Brief Automation**: Farrice can now build a complete pipeline from TikTok/Instagram trend scraping to client-ready creative briefs — a core service for e-commerce brands and ad agencies. This stacks directly with Seena Rez (TikTok hooks), Cardinal Mason (conversion copy), and Sabri Suby (ad strategy).
- **Client Tool Building**: The vibe-coded internal tool pattern — build custom marketing tools for clients as a service, not a SaaS product. Each tool is bespoke, high-value, and creates deep client lock-in.
- **Comment Intelligence Pipeline**: Mining social media comments at scale for consumer language, objections, and competitor intel. This stacks with the consumer-posture-research skill and Dai Media's consumer posture analysis.
- **Pricing Benchmark**: The productized version of this pipeline is scoped at $2-5K/mo to maintain a live trend-research feed for one client (`extractions/mike-foutia-marketing-tools/extraction-report.md`, Applied Intelligence § "Creative Volume Service").

### Market Signals

- **Creative volume is the new ad moat**: Meta's algorithm explicitly rewards more creative variants. Tools that compress the research-to-creative cycle are in high demand. E-commerce brands and agencies are the primary buyers.
- **Apify + Gemini multimodal = research automation layer**: The stack of Apify (scraping) + Gemini (video analysis) + brand context injection is a reusable pattern for any niche research automation.
- **AI video is NOT ready for full automation**: Mike explicitly states that automated AI video at scale produces "terrible" quality. The opportunity is in the research and brief phases, not the production phase — yet.

### System Enhancements

- **Brand Bible Template**: The brand bible / taste profile concept should become a standard Antigravity artifact — every client engagement starts by building one.
- **Scraping → Analysis → Synthesis Pattern**: This three-stage pattern (collect → analyze → synthesize) is generalizable beyond TikTok to any platform intelligence workflow.
- **Automation Boundary Framework**: Mike's heuristic for when to automate vs. keep humans in the loop could become a standard decision framework for all Antigravity tool-building projects.
- **Standardization Note**: Mike's own diagnostic — "AI is really good at getting you to the mean" — is the reason the Automation Boundary Framework needs to be a system-wide decision lens, not a one-off judgment call (this file, Hidden Knowledge #4).

---

## Implementation Pathway

- **24-Hour Quickstart**: Deploy the `tiktok-trend-scraper` prompt to scrape and analyze a niche. Build a brand bible for one client/project using the `brand-bible-builder` prompt.
- **7-Day Sprint**: Build a complete trend-to-brief pipeline for one niche using all prompts in sequence. Validate brief quality with a real creative team or ad account.
- **30-Day Integration**: Productize the pipeline as a recurring client service. Add historical ad data context layer. Expand to Instagram Reels and YouTube Shorts scraping.

---

## Hall of Fame Exemplars

> Full exemplar library: `references/exemplars.md` — load for deep pattern study. The GlowUp Serum brief alone is built from 500 scraped TikToks and 10,000+ mined comments — the canonical model for what "excellent" looks like under this skill.

## Signature Moves

*   **"Brand Bible First"**: Always initiates any creative brief or content generation workflow by loading a comprehensive, AI-refined "brand bible" (tone, audience, pain points, differentiators) as the foundational system context. → **Deploy when**: Starting any new AI content generation task or client project.
*   **"Layered Data Ascent"**: When conducting research, he meticulously progresses through raw metrics (Layer 1), then semantic analysis (Layer 2) of top performers, before synthesizing into a deliverable (Layer 3). Never skips directly from raw data to conclusions. → **Deploy when**: Any research-to-insight pipeline, competitive analysis, or trend spotting.
*   **"Organic Validation Loop"**: Systematically scrapes trending organic social content (e.g., TikTok) in a niche to identify proven hooks, angles, and messaging that resonate, then uses these validated patterns as the strategic input for paid ad briefs. → **Deploy when**: Developing creative strategy for performance marketing campaigns (Meta, TikTok Ads).
*   **"Automate Text, Not Visuals (Yet)"**: Applies the "automation boundary heuristic" by automating text-based research, analysis, and brief generation where reliability is >95%, but deliberately keeps humans in the loop for highly creative visual assets like video production. → **Deploy when**: Deciding where to invest automation efforts or scope AI tool capabilities.
*   **"Comment Mining Protocol"**: After identifying high-performing organic content, he triggers deep AI analysis of the comment section to extract explicit objections, desired features, competitor weaknesses, and verbatim customer language. → **Deploy when**: Refining messaging angles, identifying pain points, or gathering product feedback for ad copy.

## Quality Rubric

> Detailed scoring rubric: `references/quality-rubric.md` — load on-demand for grading. Scores span 4 (Acceptable) through 7 (Good) to 10 (Savant) across the three-tier criteria table.
