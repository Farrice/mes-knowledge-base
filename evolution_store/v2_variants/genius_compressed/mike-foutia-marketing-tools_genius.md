# Mike Foutia — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

Foutia sits at the rare intersection of marketing strategist and tool builder, constructing end-to-end AI workflows that convert social media trend research into deployable ad briefs in under 15 minutes. His core insight: organic virality is free market research — what's trending organically reveals proven messaging, hooks, and angles that can be fast-followed with paid ads. He encodes expert judgment into repeatable workflows so teams get expert-grade analysis at button-click speed.

---

## Genius Patterns (Compressed)

### GP1: Three-Layer Research Escalation
Treat trend research as a data pyramid. Layer 1: raw metrics (views, likes, comments). Layer 2: AI semantic analysis of what's actually happening (hooks, angles, pain points). Layer 3: synthesized deliverable (creative brief). Never jump layers — always collect, then analyze, then synthesize.

### GP2: Brand Bible Context Injection
Before any creative output, load a brand bible (tone, audience, pain points, differentiators, winning ad patterns) as system context. Output is never generic because it's filtered through brand-specific constraints. A non-expert reading should immediately identify which brand it's for.

### GP3: Organic-to-Paid Bridge
Use organic social data (TikTok trending) as strategic input for paid ad creative. Scrape trending content → identify winning hooks/angles/pain points → generate paid briefs leveraging proven patterns → test at volume. Creative based on proven organic patterns, not guesswork.

### GP4: Automation Boundary Heuristic
Sharp line: automate text-based research, writing, analysis, brief generation (>95% brand-safe). Keep humans in loop for video creation and highly creative visual assets. Ask: "Will output be consistently brand-safe at scale?" If not, human stays in loop.

### GP5: Non-Coder Builder Pattern (Vibe Coding for Marketing)
Prototype in low-code (N8N, Make), identify limitations, then vibe-code custom version with Claude Code/Cursor. Ship internal tools, not SaaS products. Build time in hours, not weeks. Tools do exactly what team needs with zero unused features.

### GP6: Creative Volume as Competitive Moat
Meta's algorithm rewards creative volume — specifically "net new concepts." Build systems maximizing research-to-creative pipeline velocity. The speed of the pipeline is the actual competitive lever, not just "make more ads."

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | Comment Mining Goldmine — comments reveal objections, desired features, competitor weaknesses, and prospect language patterns; the real intelligence is below the video | Product research, messaging refinement, objection handling |
| HK2 | Taste Profile as Strategic Guardrail — brand bible isn't "nice to have," it's what prevents AI from producing mean-reversion content | Any AI content generation pipeline |
| HK3 | Historical Ad Data as Context Layer — best briefs layer backward-looking data (what worked for us) on top of forward-looking (what's trending) on top of brand context | Creative brief generation |
| HK4 | The "Mean Reversion" Problem — AI gets you to the mean; marketing success requires deviating from it; design AI for commodity work while preserving space for human creativity | Scoping any AI marketing automation |
| HK5 | Phase-Based Client Expansion — build first tool for known pain point, expand into adjacent automation as trust builds; each phase funds the next | Client engagement and upsell strategy |

---

## TikTok-to-Ad-Brief Pipeline

1. **Trend Scraping** — Define niche keywords, date range, volume; use Apify to pull TikTok videos with full metrics
2. **AI Video Analysis** — Select high-performers, pull transcripts, send to Gemini multimodal; extract: visual hook, proof/demo, theme, funnel stage, angle; mine comments for patterns
3. **Brand Context Loading** — Load brand bible + optional historical ad data + competitor analysis
4. **Brief Generation** — Combine analysis + context + template; generate brief (campaign name, objective, audience, pain points, key message, creative direction); human reviews (80% first-draft accuracy)
5. **Creative Production** — Brief feeds into ad creation tools; multiple variations per concept for A/B testing; human QC before deployment

---

## Signature Moves

1. **"Brand Bible First"** — Always loads comprehensive brand bible as foundational context before any creative generation.
2. **"Layered Data Ascent"** — Meticulously progresses through raw metrics → semantic analysis → deliverable synthesis; never skips layers.
3. **"Organic Validation Loop"** — Scrapes trending organic content to identify proven hooks/angles, then uses as strategic input for paid ad briefs.
4. **"Automate Text, Not Visuals (Yet)"** — Automates text-based research and briefs; deliberately keeps humans in loop for creative visual assets.
5. **"Comment Mining Protocol"** — Triggers deep AI analysis of comment sections to extract objections, features, competitor weaknesses, and verbatim language.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Research Layer Discipline | Jumps from raw data to brief without analysis layer | Most layers followed but some shortcuts | Strict Layer 1 → 2 → 3 progression with no layer skipping; brief contains specific proof (URLs, exact hooks, data) |
| Brand Context Integration | Generic output without brand filtering | Brand context present but output still somewhat interchangeable | Output immediately identifiable as belonging to specific brand without being told |
| Organic-to-Paid Bridge | Paid creative based on guesswork or generic strategy | Some organic signals informing paid strategy | Paid briefs directly leverage proven organic hooks, angles, and validated messaging patterns |
| Automation Boundary Awareness | Fully automated pipeline including creative visual assets | Mostly automated with ad-hoc human checkpoints | Sharp line between automated text/research and human-in-loop creative; zero brand-damaging escapes |
| Pipeline Velocity | Days/weeks from research to brief | Same-day research to brief with some manual steps | Minutes from trend scrape to client-ready brief; 5-10x creative testing velocity increase |
