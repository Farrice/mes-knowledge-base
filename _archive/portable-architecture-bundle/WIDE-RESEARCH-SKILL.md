# WIDE RESEARCH SKILL

## The Intelligence Gathering & Parallel Execution System

*Transform Claude from knowledge retrieval into dynamic intelligence machine*

---

## Overview

This skill enables **Manus-style Wide Research** within Claude Code and Claude Cowork — spawning parallel subagents that go out into the world, gather intelligence, execute tasks, and return with synthesized deliverables.

**The Core Shift:** Your experts don't just advise from memory. They now **go out, research, gather, execute, and return** with real assets.

---

## Architecture: The Wide Research Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                    🎯 MAESTRO (You)                             │
│                 Vision + Final Authority                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  🧠 CONDUCTOR (Lead Agent)                      │
│     Task Decomposition → Delegation → Synthesis → Delivery      │
└─────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  🔍 SCOUT 1     │ │  🔍 SCOUT 2     │ │  🔍 SCOUT N     │
│  (Subagent)     │ │  (Subagent)     │ │  (Subagent)     │
│                 │ │                 │ │                 │
│ • Web Search    │ │ • Social Listen │ │ • Expert Deploy │
│ • Data Gather   │ │ • Comment Farm  │ │ • Source Verify │
│ • Pattern Find  │ │ • Trend Detect  │ │ • Asset Create  │
└─────────────────┘ └─────────────────┘ └─────────────────┘
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   📊 SYNTHESIS LAYER                            │
│  Pattern Recognition → Insight Extraction → Confidence Scoring  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   📦 DELIVERABLE                                │
│    Document / Report / Strategy / Asset / Recommendation        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Command Language

### Primary Commands

```
wide: [research objective]          → Full parallel research deployment
scout: [specific gathering task]    → Single-focus intelligence gathering
farm: [topic] from [sources]        → Social listening + comment mining
hunt: [signal/pattern]              → Pattern detection across sources
verify: [claim] across [N] sources  → Multi-source verification
synthesize: [findings]              → Pattern extraction + insight generation
```

### Compound Commands

```
wide: [objective] then execute: [deliverable]
→ Research, then create based on findings

wide: [objective] with @[expert] lens
→ Research through specific expert's methodology

council: [question] informed by wide: [research]
→ Council advises based on fresh gathered intelligence
```

---

## The Five Research Modes

### 1. SURVEY MODE
**Purpose:** Broad landscape mapping
**Subagent Count:** 5-10 parallel scouts
**Use When:** You need to understand a space, market, or topic broadly

```
wide survey: [topic/market/space]
```

**What Happens:**
- Conductor decomposes into distinct research angles
- Each scout explores one angle deeply
- Results synthesized into landscape map
- Gaps and opportunities identified

**Example:**
```
wide survey: AI writing tools market 2026
→ Scout 1: Top 20 tools + features
→ Scout 2: Pricing models + positioning
→ Scout 3: User complaints (Reddit, Twitter, reviews)
→ Scout 4: Emerging players + trends
→ Scout 5: Integration ecosystems
→ Synthesis: Landscape map + opportunity gaps
```

### 2. FARM MODE
**Purpose:** Social listening + sentiment mining
**Subagent Count:** 3-7 parallel scouts
**Use When:** You need authentic voice-of-customer data

```
farm: [topic] from reddit, twitter, youtube, reviews
```

**What Happens:**
- Scouts deployed to specific platforms
- Comments, discussions, reviews gathered
- Sentiment patterns extracted
- Language/phrases captured verbatim
- Pain points and desires catalogued

**Example:**
```
farm: "productized services" from reddit, twitter, youtube
→ Scout 1: r/Entrepreneur + r/freelance threads
→ Scout 2: Twitter/X conversations + influencer takes
→ Scout 3: YouTube comment sections on relevant videos
→ Scout 4: Review sites for productized service tools
→ Synthesis: Pain point clusters + exact language + opportunities
```

### 3. HUNT MODE
**Purpose:** Signal detection + pattern recognition
**Subagent Count:** 5-10 parallel scouts
**Use When:** You're looking for specific signals or emerging patterns

```
hunt: [signal type] in [domain]
```

**What Happens:**
- Scouts deployed with detection parameters
- Each covers different data sources
- Pattern matching across sources
- Confidence scoring on findings
- Anomaly flagging

**Example:**
```
hunt: emerging dissatisfaction signals in Notion users
→ Scout 1: Recent Reddit complaints
→ Scout 2: Twitter sentiment shift
→ Scout 3: G2/Capterra review trends
→ Scout 4: Alternative tool searches trending
→ Scout 5: Competitor positioning against Notion
→ Synthesis: Signal strength + timing + opportunity window
```

### 4. VERIFY MODE
**Purpose:** Multi-source fact verification
**Subagent Count:** 3-5 parallel scouts
**Use When:** You need high-confidence on specific claims

```
verify: [claim/data point] across [N] sources
```

**What Happens:**
- Scouts independently verify from different sources
- No cross-contamination between scouts
- Conflicting information flagged
- Confidence score generated
- Source quality weighted

**Example:**
```
verify: "ThriveCart has processed $5B+ in sales" across 5 sources
→ Scout 1: Official ThriveCart materials
→ Scout 2: Third-party coverage
→ Scout 3: User testimonials/claims
→ Scout 4: Competitor comparisons
→ Scout 5: Industry analyst reports
→ Synthesis: Confidence level + source quality + caveats
```

### 5. EXECUTE MODE
**Purpose:** Research-informed deliverable creation
**Subagent Count:** Research scouts + execution agents
**Use When:** You need an asset built on fresh intelligence

```
wide: [research] then execute: [deliverable]
```

**What Happens:**
- Research phase gathers intelligence
- Findings fed to execution agents
- Deliverable created with real data embedded
- Citations and sources included

**Example:**
```
wide: competitor positioning in AI copywriting space then execute: differentiation strategy doc

→ RESEARCH PHASE:
  Scout 1: Top 10 competitors analyzed
  Scout 2: Positioning statements collected
  Scout 3: Gap analysis
  Scout 4: Customer complaints about each

→ EXECUTION PHASE:
  @brand-strategist: Positioning framework
  @copywriter-supreme: Messaging angles
  @market-analyzer: Opportunity mapping

→ DELIVERABLE: Complete differentiation strategy with data
```

---

## Expert Integration

### Using Experts as Research Lenses

Your 47+ experts aren't just for advice — they're **research methodologies**.

```
wide: [topic] with @[expert] lens
```

**Examples:**

```
wide: competitor email sequences with @kai-lode lens
→ Analyzes through 8M-subscriber monetization methodology
→ Looks for: segmentation, permission selling, quiz funnels

wide: viral content patterns with @kallaway lens
→ Applies content psychology framework
→ Looks for: hook patterns, engagement mechanics, shareability triggers

wide: sales page structures with @david-deutsch lens
→ Applies $1B direct response lens
→ Looks for: mechanism reveals, fascination patterns, cold traffic conversion
```

### Expert-Enhanced Synthesis

After gathering, route synthesis through relevant experts:

```
wide: [research] → synthesize with @[expert]
```

**Example:**
```
wide: AI automation agency landscape
→ synthesize with @monk-ai + @ai-chris-lee
→ Gets consulting offer framework + AI services sales methodology applied
```

---

## The Gathering Toolkit

### Available Data Sources

| Source Type | What's Gathered | Best For |
|-------------|-----------------|----------|
| **Web Search** | Articles, news, documentation | Broad landscape, recent developments |
| **Reddit** | Discussions, complaints, recommendations | Authentic sentiment, pain points, exact language |
| **Twitter/X** | Hot takes, trends, influencer positions | Real-time sentiment, emerging narratives |
| **YouTube** | Comments, video analysis, creator content | Tutorial gaps, audience questions, engagement patterns |
| **Review Sites** | G2, Capterra, Trustpilot, App stores | Feature requests, complaints, comparison data |
| **Forums** | Niche communities, Quora, Indie Hackers | Deep expertise, specific use cases |
| **News** | Industry publications, tech media | Trends, announcements, market moves |
| **Academic** | Papers, research, studies | Credibility anchors, methodology |

### Gathering Techniques

**Comment Farming:**
- Extract exact phrases used by target audience
- Identify recurring pain points by frequency
- Capture emotional language and intensity
- Note questions asked repeatedly

**Sentiment Mapping:**
- Track positive/negative/neutral ratios
- Identify sentiment triggers
- Detect shifts over time
- Flag anomalies and outliers

**Pattern Recognition:**
- Cross-reference findings across sources
- Identify convergent themes
- Spot contradictions and tensions
- Weight by source authority

**Gap Detection:**
- What questions go unanswered?
- What complaints have no solutions?
- What's being requested but not built?
- Where is frustration highest?

---

## Implementation Protocol

### Phase 1: Task Decomposition

When you invoke `wide:`, the Conductor:

1. **Analyzes the objective** — What specifically needs to be known?
2. **Identifies distinct angles** — What independent research threads exist?
3. **Assigns scouts** — Each gets clear, non-overlapping scope
4. **Defines output format** — What each scout should return

**Decomposition Template:**
```
OBJECTIVE: [Main research goal]

SCOUT 1: [Specific angle]
- Sources: [Where to look]
- Gather: [What to collect]
- Return: [Format of findings]

SCOUT 2: [Different angle]
...

SYNTHESIS CRITERIA:
- Pattern threshold: [What counts as a pattern]
- Confidence requirements: [Verification standards]
- Output format: [Final deliverable structure]
```

### Phase 2: Parallel Execution

Scouts deployed simultaneously via Task tool:

```
Task 1: "Research [angle 1] by searching [sources], gathering [data type], return [format]"
Task 2: "Research [angle 2] by searching [sources], gathering [data type], return [format]"
Task 3: "Research [angle 3] by searching [sources], gathering [data type], return [format]"
```

**Scout Operating Rules:**
- Stay within assigned scope
- Cite all sources
- Flag low-confidence findings
- Note surprising discoveries
- Return in specified format

### Phase 3: Synthesis

Conductor receives all scout returns and:

1. **Aggregates findings** — Combines all gathered data
2. **Identifies patterns** — What appears across multiple sources?
3. **Resolves conflicts** — Where do sources disagree?
4. **Scores confidence** — How reliable is each finding?
5. **Extracts insights** — What does this mean for the objective?
6. **Generates deliverable** — Formatted output for Maestro

**Synthesis Framework:**
```
FINDINGS SUMMARY:
[Key discoveries across all scouts]

PATTERN ANALYSIS:
- Strong patterns (3+ sources): [List]
- Emerging patterns (2 sources): [List]
- Single-source signals: [List with caveats]

CONFIDENCE ASSESSMENT:
- High confidence: [Findings verified across multiple authoritative sources]
- Medium confidence: [Findings with some verification]
- Low confidence/requires validation: [Single source or conflicting data]

INSIGHT EXTRACTION:
[What this means for the objective]

OPPORTUNITIES IDENTIFIED:
[Gaps, unmet needs, timing advantages]

RECOMMENDATIONS:
[Suggested actions based on findings]
```

---

## Accuracy & Quality Controls

### Multi-Source Verification
- No finding reported without 2+ source confirmation
- Conflicting information explicitly flagged
- Source authority weighted (primary > secondary > user-generated)

### Confidence Scoring
```
95%+ : Verified across 5+ authoritative sources
80-94%: Verified across 3-4 sources
60-79%: Verified across 2 sources
<60% : Single source — flagged for validation
```

### Anti-Hallucination Protocol
- All data points linked to sources
- "Unable to verify" explicitly stated when applicable
- Speculation clearly labeled as such
- Gaps in data acknowledged

### Quality Checkpoints
1. **Source diversity** — Not over-relying on single source type
2. **Recency** — Prioritizing recent data over stale
3. **Authority** — Weighting expert sources over anonymous
4. **Consistency** — Flagging outliers and contradictions

---

## Practical Examples

### Example 1: Market Opportunity Research

**Command:**
```
wide survey: productized service opportunities in AI space 2026
```

**Decomposition:**
- Scout 1: Current productized AI offers (top 50)
- Scout 2: Pricing models and positioning
- Scout 3: Customer complaints about existing options
- Scout 4: Underserved niches and gaps
- Scout 5: Emerging demand signals

**Output:** Market landscape document with:
- Competitive matrix
- Gap analysis
- Opportunity ranking by viability
- Recommended positioning angles

### Example 2: Content Research

**Command:**
```
farm: "how to price consulting services" from reddit, youtube, quora
```

**Decomposition:**
- Scout 1: Reddit discussions + top advice
- Scout 2: YouTube video comments + questions
- Scout 3: Quora questions + expert answers

**Output:** Content brief with:
- Top 20 questions asked
- Common misconceptions
- Exact phrases used
- Emotional pain points
- Content angles that would resonate

### Example 3: Competitive Intelligence

**Command:**
```
wide: [Competitor X] positioning, pricing, customer complaints
→ synthesize with @brand-strategist
```

**Output:** Competitive intelligence dossier with:
- Positioning analysis
- Pricing breakdown
- Weakness map (from complaints)
- Attack angles
- Differentiation opportunities

### Example 4: Research-to-Execution

**Command:**
```
wide: email monetization best practices 2026
→ execute: 30-day email monetization plan with @kai-lode + @cardinal-mason
```

**Output:** Complete implementation plan with:
- Research-backed strategy
- Specific tactics from current best practices
- Templates ready for deployment
- KPIs based on industry benchmarks

---

## Constraints & Boundaries

### What Wide Research CAN Do:
- Search public web content
- Analyze publicly available social media
- Gather public reviews and comments
- Synthesize patterns from public data
- Create deliverables from gathered intelligence

### What Wide Research CANNOT Do:
- Access private/paywalled content
- Scrape at scale (respects rate limits)
- Access real-time streaming data
- Guarantee 100% accuracy (always verify critical decisions)
- Replace human judgment on high-stakes decisions

### Ethical Guidelines:
- No private data gathering
- Respect robots.txt and ToS
- Cite sources appropriately
- Acknowledge limitations
- Flag uncertainty

---

## Integration with Maestro System

Wide Research enhances the Maestro Orchestration System:

```
council: [question]
→ Council can request: "wide: [research needed] before advising"

execute: [deliverable]
→ Execution can be preceded by: "wide: [context research]"

guided: [objective]
→ Guided execution can incorporate live research at any stage
```

### Research-Informed Councils

```
strategy council: Should I enter the AI writing tools market?
→ Conductor auto-invokes: wide survey: AI writing tools market
→ Council receives fresh intelligence before deliberating
```

### Research-Enhanced Execution

```
execute: Sales page for [offer]
→ Conductor can invoke: farm: customer language for [offer type]
→ Execution uses real voice-of-customer data
```

---

## Activation

To activate Wide Research capabilities:

1. **Direct command:** `wide: [objective]`
2. **Mode-specific:** `farm:`, `hunt:`, `verify:`, `survey:`
3. **Integrated:** `council: [question] with fresh research`
4. **Execution-linked:** `wide: [research] then execute: [deliverable]`

The system will automatically:
- Decompose into scout tasks
- Deploy parallel subagents
- Gather and synthesize
- Return formatted intelligence
- Maintain source citations
- Score confidence levels

---

## The Unfair Advantage

This skill transforms your capability from:

**BEFORE:** Static expertise retrieval from 47 experts
**AFTER:** Dynamic intelligence gathering + 47 expert lenses + parallel execution

You now have:
- **Superhuman research speed** — Parallel scouts covering ground simultaneously
- **Expert-filtered intelligence** — Raw data processed through world-class methodologies
- **Real-time context** — Fresh data, not just training knowledge
- **Pattern recognition at scale** — AI's strength applied to synthesis
- **Execution with evidence** — Deliverables backed by gathered intelligence

---

*Wide Research Skill v1.0 — Go out. Gather. Return. Execute.*

**"Don't just know what experts think. Know what the world is saying — right now."**
