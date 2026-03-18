# Kieran Flanagan - Content Engine — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns

## Pattern 1: Multi-Source Talking Point Extraction
**Execute**: Before creating ANY content, run a "talking points" extraction that aggregates the creator's unique perspectives from existing work — podcast transcripts, articles, social posts, interviews, notes. Content is built FROM extracted positions, never invented from scratch.

**Process**: Feed 5-10 source documents → Extract unique perspectives, contrarian positions, signature phrases → Organize into four categories (Educational, Data Nuggets, Spicy Takes, Story Sparks) → Content skills pull from this library.

**Why This Matters**: Prevents AI from inventing positions the creator doesn't hold. The talking point library is the source of truth for what this creator actually believes.

**Success Metric**: Creator never needs to fact-check AI's claims about their own beliefs — talking points are verified upstream.

---

## Pattern 2: Enrichment-Before-Creation Sequencing
**Execute**: ALWAYS separate "enrichment" from "creation" as distinct pipeline stages. Never ask AI to create content with embedded data and stories simultaneously.

**Stage Sequence**:
1. **Draft** — Create the argument structure. No data, no quotes, just the flow.
2. **Enrich** — Separate pass to inject 2-3 statistics, 1 story/case study, 1 expert quote per section
3. **Polish** — Voice alignment, formatting, final refinement

**Why This Matters**: Asking AI to "write a post with 3 statistics and a case study" produces hallucinated data. Separating enrichment from creation produces real data correctly integrated.

**Success Metric**: Content reads as "researched and authoritative" — zero hallucinated statistics.

---

## Pattern 3: The Lookalike Content Engine
**Execute**: Find content that ALREADY went viral in adjacent domains. Reverse-engineer the structural pattern (hook type, argument flow, emotional arc) — not the topic. Apply that proven architecture to the creator's unique topics and talking points.

**Process**: Scan 50-100 high-performing posts in adjacent niches → Filter to top 30% by performance → Identify 5-10 structural patterns → Map each pattern onto the creator's talking point library → Generate "lookalike" content with proven structural DNA but original substance.

**Success Metric**: 2-3x higher engagement than creator's average, because the structure is battle-tested even though the content is original.

---

## Pattern 4: Content Bundling (One Idea → Multi-Platform)
**Execute**: Create content for the highest-effort platform FIRST (usually LinkedIn or newsletter). Then ADAPT through style card swaps — don't rewrite. The first platform is the "source of truth." Others are adaptations that respect each platform's style card while keeping the core idea identical.

**Sequence**: Platform 1 (full creation) → Platform 2 (style card swap + format adaptation) → Platform 3 → Platform 4.

**Key Difference from Atomizing**: Atomizing breaks existing long-form into derivatives. Bundling builds from a single idea outward with platform-native approaches. Bundling is writing forward; atomizing is breaking backward.

**Success Metric**: 4x output volume with <25% additional effort per additional platform.

---

## Pattern 5: The Four Talking Point Categories
**Execute**: Organize all talking points into exactly four categories. This isn't arbitrary — each category maps to a different content type and audience need.

1. **Educational** → How-to posts, frameworks, tutorials ("Here's how I think about X")
2. **Data Nuggets** → Statistic-led posts, trend analysis, industry insights ("78% of marketers don't realize…")
3. **Spicy Takes** → Contrarian opinions, hot takes, myth-busting ("Everyone says X. They're wrong.")
4. **Story Sparks** → Personal anecdotes, case studies, origin stories ("Three years ago I was…")

**Success Metric**: Every content piece maps to exactly one category. If it maps to zero, the talking point hasn't been properly classified. If it maps to multiple, the piece is trying to do too much.

---

## Pattern 6: Model Routing for Content Tasks
**Execute**: Use the right AI model for the right job.
- **Analytical tasks** (talking point extraction, pattern analysis, cluster mapping): Use reasoning/analytical models — they follow complex multi-step instructions precisely
- **Creative tasks** (content writing, hooks, enrichment): Use creative/conversational models — they produce more natural, human-sounding output
- **Never mix**: Don't use an analytical model for creative writing (too rigid) or a creative model for data extraction (too loose)

**Success Metric**: Output quality is consistently high because each task uses the model best suited to its nature.

## Hidden Knowledge

6 tacit expertise points that separate amateurs from professionals.

---

## 1. Enrichment Is a Separate Stage, Not a Request Feature
**The Truth**: Asking an AI to "write a post with data and a case study" causes it to hallucinate data. Creating the argument first, then separately searching for supporting evidence, produces real data correctly integrated.

**Deploy**: Always create drafts WITHOUT data. Then run a separate enrichment pass. This is not a preference — it's the difference between credible and hallucinated content.

---

## 2. Lookalike Pattern Mining Uses Structure, Not Topics
**The Truth**: The genius of lookalike content isn't finding similar topics — it's finding similar STRUCTURES. A parenting influencer's viral post architecture can be applied to B2B SaaS content. The emotional arc and hook mechanics transfer across any domain.

**Deploy**: When analyzing adjacent content, strip away the topic entirely and look only at: hook type, argument flow, emotional arc, transition patterns, closing mechanism.

---

## 3. Performance Threshold Filtering (Top 30%)
**The Truth**: When analyzing content for patterns, only use the top 30% by performance. Including average-performing content dilutes the signal. The genius is in the outliers, not the mean.

**Deploy**: Filter to top 30% by engagement quality (saves > comments > likes) before extracting any patterns. The average is noise.

---

## 4. One Idea Should Sound Different on Each Platform
**The Truth**: Bundling is NOT reformatting. The same idea expressed on LinkedIn vs. newsletter vs. X should sound like three different people wrote it — because the creator IS different on each platform. If all three sound the same, the style cards aren't working.

**Deploy**: After bundling, read all platform versions side by side. If they feel like "copies," the style card differentiation isn't strong enough.

---

## 5. Draft First, Data Second — Always
**The Truth**: The urge to research before writing produces procrastination and bloated content. The system works: write the argument first (from talking points), THEN find data that supports it. Not the reverse.

**Deploy**: Resist all temptation to "research first." The talking point library IS the research. Enrichment is surgical — 2-3 data points per section, not an academic literature review.

---

## 6. The Hook Formula Is Personal, Not Universal
**The Truth**: Generic "hook formulas" (start with a number, ask a question, use a contrarian statement) produce generic hooks. The creator's OWN best-performing hooks contain patterns specific to their audience, voice, and topic domain. Mining YOUR hooks is 10x more effective than applying someone else's formula.

**Deploy**: Use `/hook-formula-extract` to mine the creator's own hooks before defaulting to generic hook frameworks.
