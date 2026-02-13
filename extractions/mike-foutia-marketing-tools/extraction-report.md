# Mike Foutia — Mastery Extraction

## Content Assessment

```
Source: YouTube interview (~25 min) — Marketing Against The Grain (HubSpot) + host Kip/Kieran
Expert: Mike Foutia — Marketing tool builder, e-commerce AI automation specialist
Domain: Vibe-coded marketing tools, TikTok trend scraping → AI analysis → creative brief generation
Depth Tier: Standard — Full interview, single workflow deep-dive with strategic context
Genius Patterns: 6 identified
Hidden Knowledge: 5 tacit insights detected
Existing Overlap: Partial overlap with andrew-wilkinson (vibe coding mindset), nick-saraev (agentic workflows), seena-rez (TikTok content). Mike's unique angle: non-coder building production marketing tools for ad teams, with a specific 3-layer data pipeline architecture.
```

## Executive Summary

- **Core Genius**: Building end-to-end marketing automation pipelines by chaining scraper APIs → multimodal AI analysis → templated brief generation — all without traditional coding skills, using vibe coding in Claude Code.
- **What Makes Him Different**: Mike is not an engineer who learned marketing — he's a marketing practitioner who learned to build. His tools are shaped by actual client pain (e-commerce brands and Facebook ad agencies), not developer curiosity. He knows exactly which parts of the ad workflow to automate (research + briefs) and which to leave manual (video creation), because he's seen what fails at scale.
- **Deployable Skills**: TikTok trend research pipeline, AI video analysis system, automated creative brief generation, brand bible integration, client project architecture
- **Hidden Knowledge Captured**: The 3-layer escalation pattern (data → analysis → asset), the automation boundary heuristic (text = automate, creative video = don't), the "brand bible as context injection" pattern, research-to-brief as the highest-ROI automation target

## Genius Patterns

### 1. The 3-Layer Research Escalation
- **What They Do Unconsciously**: Mike structures every tool as three escalating layers — raw data collection → AI-powered analysis → synthesized deliverable. Never stops at just scraping data.
- **Executable Behavior**: When building any marketing research tool, enforce a 3-stage pipeline: (1) pull structured data via API scrapers, (2) run multimodal AI analysis on the content, (3) generate a human-ready deliverable (brief, report, strategy doc). Each layer adds intelligence.
- **Deployment Context**: Any time you're building a research → action tool. Works for competitor analysis, content research, ad creative research, market trend monitoring.
- **Success Metric**: The "from nothing to brief in 15 minutes" benchmark — can someone go from zero knowledge to an actionable strategy document in a single session?

### 2. Brand Bible as Context Injection
- **What They Do Unconsciously**: Pre-loads ALL brand context (voice, audience, pain points, customer data) into the AI before generating any output. The brief quality isn't from better prompting — it's from richer context.
- **Executable Behavior**: Before any generative marketing workflow, build a structured brand context document: tone of voice, target audience profiles, known pain points, competitor positioning, historical campaign performance. Inject this as system-level context for every generation step.
- **Deployment Context**: Creative brief generation, ad copy writing, content strategy, campaign planning — any workflow where outputs need brand alignment.
- **Success Metric**: Generated outputs require only 20% human editing (the "80% there" standard Mike and Kieran both cite).

### 3. Organic-to-Paid Bridge
- **What They Do Unconsciously**: Uses organic TikTok performance as a leading indicator for paid ad creative. Doesn't guess at what hooks/angles work — lets viral organic content prove it first.
- **Executable Behavior**: Scrape top-performing organic content for your niche → extract the hooks, angles, proof elements, and themes → use those validated elements as the foundation for paid ad creative. Organic virality = pre-validated messaging.
- **Deployment Context**: Facebook/Meta ad creative strategy, TikTok Shop ads, any paid social where creative volume is the competitive moat.
- **Success Metric**: Ad creative concepts are traceable back to organic content that already demonstrated audience resonance (views, engagement rate).

### 4. The Automation Boundary Heuristic
- **What They Do Unconsciously**: Draws a sharp line between what to automate and what not to. Text-based operations (research, analysis, writing, briefs) = automate aggressively. Creative visual production (AI video, UGC) = keep human-in-the-loop.
- **Executable Behavior**: Before automating any marketing workflow, apply the test: "Is this text/research or creative production?" Text and research → automate end-to-end. Creative production → assist but don't fully automate. AI video at scale = expensive bad output. Research at scale = massive time savings.
- **Deployment Context**: Scoping any AI automation project for marketing teams. Critical for setting realistic expectations with clients.
- **Success Metric**: The "brand safety" test — would automated output embarrass the brand if published without human review?

### 5. Non-Coder Builder Pattern
- **What They Do Unconsciously**: Builds production-grade internal tools without traditional coding skills by pairing a vibe-coding IDE (Claude Code) with a second AI instance for debugging/learning. Two-screen workflow: build in one, learn in the other.
- **Executable Behavior**: Open Claude Code (or Codex) in one screen. Open a regular Claude/ChatGPT chat in the other. Build in the IDE, copy errors to the chat for explanation and fixes. Learn by building, not by studying.
- **Deployment Context**: Any marketer or non-technical operator who wants to build internal tools. Specifically: skip N8N/Make/Zapier and go straight to vibe coding for faster iteration and better outputs.
- **Success Metric**: Can a non-coder ship a functional internal tool within a day of focused work?

### 6. Creative Volume as Competitive Moat
- **What They Do Unconsciously**: Frames the entire tool around Meta's algorithmic demand for "net new concepts" — the platform rewards creative volume, so the tool is designed to produce volume of research → volume of briefs → volume of ads.
- **Executable Behavior**: Build workflows that maximize the number of distinct creative concepts you can generate and test per week. The goal isn't one perfect ad — it's 20 good-enough ads that the algorithm can optimize from.
- **Deployment Context**: Facebook/Meta ad accounts, TikTok Shop campaigns, any paid social where the platform's algorithm benefits from more creative inputs.
- **Success Metric**: Number of net new ad concepts tested per week increases 3-5x compared to manual process.

## Hidden Knowledge

### The "Record Yourself" Discovery Pattern
Mike reveals Gemini can consume videos up to 1 hour long. The tactical insight most people miss: record yourself doing the manual task you hate, feed the recording to Gemini, and ask it to identify what can be automated. Use AI to find what to build with AI.

### N8N is a Dead End for Non-Coders
Despite N8N being the industry standard for AI automation, Mike explicitly says he would NOT learn it if starting today. His journey: avoided N8N for 4 months → learned it reluctantly → now advocates skipping it entirely for vibe coding. The "node-based workflow" paradigm is being superseded by natural language coding.

### Client Pain as Build Specification
Mike didn't start with technology — he started with a client's specific frustration (manual TikTok scrolling for ad angles). The build specification IS the client's complaint. This inverts the typical builder approach of "what can I build?" to "what are people paying to avoid doing?"

### The Apify Stack for Social Scraping
Mike uses Apify as the scraper layer, Gemini as the analysis layer. This is a specific, production-tested stack — not theoretical. Apify handles the messy extraction (rate limits, anti-bot measures, data normalization), freeing Mike to focus on the intelligence layer.

### Comment Section = Gold Mine
Mike emphasizes analyzing video comments, not just the videos themselves. Questions commenters ask about competitor products, complaints, desires — this is zero-cost market research that most marketers ignore. The tool specifically extracts and analyzes comment sentiment and themes.

## Methodology

### The TikTok-to-Brief Pipeline

**Stage 1 — Trend Discovery**
1. Define search keyword aligned with brand/niche
2. Set date range and result count parameters
3. Execute Apify scraper against TikTok search
4. Display results with engagement metrics (views, likes, comments, shares)
5. Sort/filter by performance signals

**Stage 2 — AI Video Analysis**
1. Select high-performing videos for deep analysis
2. Pull video transcript where available
3. Send video to Gemini for multimodal analysis
4. Extract structured elements: visual hook, proof mechanism, theme/angle, funnel stage
5. Analyze comment section: questions, complaints, desires, sentiment

**Stage 3 — Brief Generation**
1. Load brand bible context (tone, audience, pain points, positioning)
2. Select analyzed video(s) as creative inspiration source
3. Generate creative brief using brand template + research data
4. Output: campaign name, objective, target audience, pain points, key message, creative direction
5. Human review + 20% refinement → ship to creative team

### The Automation Decision Framework
```
Is the task text-based? (research, writing, analysis)
  → YES → Automate aggressively. This is where AI saves most time.
  → NO → Is it creative visual production? (video, complex imagery)
    → YES → Human-in-the-loop only. AI assists, doesn't drive.
    → NO → Evaluate case-by-case.
```

## Applied Intelligence

### Capability Unlocks

- **TikTok Trend Intelligence Pipeline**: Farrice can now build a production-grade tool that scrapes TikTok by keyword, analyzes trending videos with Gemini, and generates creative briefs — all in under 15 minutes per cycle. This is directly deployable for e-commerce clients or as a productized service.

- **Client Pain → Tool Architecture**: Mike's approach of using client complaints as build specifications is directly applicable to Farrice's AI consulting practice. Every client call that surfaces a manual pain point is a potential tool build. The pattern: "What do you hate doing?" → Record it or describe it → Build a tool that does 80% of it.

- **Creative Volume Service**: The "research → brief → volume" pipeline could be packaged as a productized offering for e-commerce brands and ad agencies. Charge $2-5K/mo to maintain a live trend research pipeline that feeds their creative team with pre-validated concepts and briefs.

### Market Signals

- **E-commerce ad agencies** are the primary market for this type of tool — they need creative volume but can't hire enough researchers
- **The "net new concepts" demand** from Meta's algorithm is creating constant pressure for more creative brainstorming → any tool that accelerates ideation has a captive market
- **N8N fatigue** is real — Mike explicitly calls out the shift from node-based automation to vibe coding as the future, signaling opportunity in helping teams transition
- **AI video is NOT ready** for full automation — anyone selling automated AI UGC/video at scale is selling vapor. This is an important consultative insight for Farrice's positioning.

### System Enhancements

- **Apify integration pattern** could become a standard execution script in Antigravity for any social scraping workflow (not just TikTok — Instagram, YouTube, Reddit)
- **Brand bible as context document** mirrors the "taste profile" concept — could standardize this as a skill across all brief-generation workflows in the system
- **The "Record Yourself" diagnostic** could be offered as a free consultation tool: "Record yourself doing any task for up to an hour, and I'll tell you what can be automated"

## Implementation Pathway

- **24-Hour Quickstart**: Deploy the `tiktok-trend-scraper` prompt to manually run trend research for any niche keyword. Test with a known brand.
- **7-Day Sprint**: Build out brand bible template + creative brief generator. Combine with trend research for a full pipeline test on one client/brand.
- **30-Day Integration**: Package as a productized service offering. Create client onboarding flow (brand bible intake → keyword configuration → weekly trend reports + briefs).
