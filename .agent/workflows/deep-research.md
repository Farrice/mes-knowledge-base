---
description: "Deep Research — Perplexity Deep Research foundation + 3 grounded parallel specialist agents + adversarial challenge + McKinsey-grade strategic intelligence report"
---

# /deep-research — Deep Research

Deploy the full research stack: Perplexity Deep Research as the foundation layer, 3 parallel specialist agents (Pattern Hunter, Psychology Miner, Contrarian Scout) to deepen each angle grounded in real data, synthesis with contradiction resolution, adversarial challenge round, and a McKinsey-grade Strategic Intelligence Report.

**The standard**: Research that finds the real psychological movers, jobs-to-be-done, and hidden patterns — not surface-level market data. The research itself is the unfair advantage. Every decision downstream (product, pricing, positioning, copy) should have a high likelihood of success because the foundation is grounded in truth.

## Usage

```
/deep-research [topic or question]
/deep-research --intent "market entry" "AI consulting for solopreneurs"
/deep-research --angles "pricing psychology, competitor moats, audience language" "Premium coaching offers"
```

## When to Use (Depth Classifier)

**Routes HERE (`/deep-research`):**
- Strategy, positioning, market entry
- Competitive intelligence, avatar research
- Foundation for downstream work (copy, offers, pricing, products)
- Going from zero to expert in a domain
- Product launch research, PMF validation
- Psychology mining, jobs-to-be-done, buying triggers
- Any research where the output becomes the BASIS for decisions

**Routes to `/research-topic` instead:**
- Quick fact lookup, single-question research
- Time-bounded lookups ("what happened yesterday")
- Budget under $3 remaining (notify user of degradation)

---

## Steps

### Step 0 — Budget Gate

Read `.agent/perplexity-usage.json`. Estimate ~$0.75-1.50 for this run (2-3 `sonar-deep-research` queries at $0.25 each).

- **If budget > $3**: Proceed with full deep research.
- **If budget $1-3**: Run with 1 deep research query instead of 2-3. Notify user.
- **If budget < $1**: Degrade to `/research-sprint` (free, WebSearch-only). Notify user: "Perplexity budget low — running research sprint instead of deep research."

### Step 1 — Scope & Deploy Plan

Parse the research question and identify the **research intent**: What decisions will this research inform? What does "knowing enough" look like?

Define 3 specialist angles using this default decomposition (override with `--angles` if user provides custom angles):

| Research Intent | Angle A (Pattern Hunter) | Angle B (Psychology Miner) | Angle C (Contrarian Scout) |
|---|---|---|---|
| **Market Entry / Product Launch** | Market Landscape & Timing — size, growth signals, timing windows, key players | Avatar Psychology & Jobs-to-be-Done — real motivations, language, identity, buying triggers | Competitive Moats & Gaps — what's working, what's failing, where the openings are |
| **Competitive Intelligence** | Business Model Reverse-Engineering — revenue architecture, unit economics, growth engines | Customer Psychology & Switching Triggers — why people buy, stay, or leave | Vulnerability Mapping — weaknesses, blindspots, attack vectors |
| **Avatar / Audience Research** | Behavioral Patterns & Market Signals — what the audience does, where they spend, what they consume | Psychographic Deep Mining — comments, reviews, forums, verbatim language, identity patterns | Contrarian Archetypes & Edge Cases — who doesn't fit the mold, why people resist, hidden segments |
| **Domain Mastery (zero to expert)** | Foundational Knowledge & Key Frameworks — core concepts, best sources, expert consensus | Current State of the Art & Key Players — who's leading, what's working, latest developments | Contrarian Views & Hidden Patterns — what the mainstream gets wrong, emerging counter-narratives |
| **Pricing / Offer Design** | Willingness-to-Pay & Value Perception — what people actually pay, anchor pricing, perceived value | Psychological Pricing Triggers — loss aversion, identity-based buying, urgency patterns | Competitive Pricing Architecture & Failures — what's failed, race-to-bottom risks, premium positioning gaps |

Present the deployment plan:

```markdown
## Deep Research Deployment

**Question**: [research question]
**Research Intent**: [detected intent]
**Estimated Perplexity cost**: ~$[0.75-1.50]

### Foundation Layer (Phase 2)
| Query | Focus | Model |
|-------|-------|-------|
| Core | [main question + sub-dimensions] | sonar-deep-research |
| Psychology | [real human drivers, JTBD, verbatim language] | sonar-deep-research |
| Counter-narrative | [criticisms, failures, contrarian views] | sonar-deep-research |

### Parallel Specialist Agents (Phase 3)
| Agent | Role | Angle | Key Questions |
|-------|------|-------|---------------|
| A | Pattern Hunter | [angle] | 1. [q1] 2. [q2] 3. [q3] |
| B | Psychology Miner | [angle] | 1. [q1] 2. [q2] 3. [q3] |
| C | Contrarian Scout | [angle] | 1. [q1] 2. [q2] 3. [q3] |

Launch? Or adjust angles/questions?
```

Wait for user approval.

---

### Step 2 — Perplexity Deep Research Foundation

Execute 2-3 `sonar-deep-research` queries ($0.25 each) using the Perplexity MCP tools.

**Tool Selection** (in priority order):
1. **MCP Tool** (preferred): Use `mcp__perplexity-ask__perplexity_research` for deep research queries. This uses the `sonar-deep-research` model natively.
2. **Python Client** (fallback): If MCP tool unavailable, run via `execution/perplexity_client.py`:
   ```bash
   cd "/Users/farricecain/Google Antigravity" && python3 -c "
   from execution.perplexity_client import PerplexityClient, load_env
   load_env()
   client = PerplexityClient()
   result = client.search('[QUERY]', model='sonar-deep-research')
   print(result.text)
   print('---CITATIONS---')
   for c in result.citations: print(c)
   "
   ```

**Sub-agents**: When spawning parallel agents in Step 3, each agent should use the MCP Perplexity tools directly for supplementary queries if available, or WebSearch as the primary tool.

**Query 1 — Core Research** (MANDATORY):
Collapse the main question with key sub-dimensions using the Collapsing Rule. Example:
```
"Comprehensive analysis of [topic]: market size and growth trajectory, key players and their positioning,
dominant business models, growth channels, and emerging trends. Include specific data points with citations."
```

**Query 2 — Psychology & Human Truth** (MANDATORY):
```
"What are the real psychological drivers, jobs-to-be-done, frustrations, and aspirations of people in [domain]?
What do they say in their own words on Reddit, YouTube comments, forums, and product reviews?
What identity patterns and emotional triggers drive their purchasing decisions? Include verbatim quotes."
```

**Query 3 — Counter-Narrative** (if budget allows):
```
"What are the biggest criticisms, failures, and contrarian perspectives on [topic]?
What have skeptics said? What products/approaches have failed in this space and why?
What does the strongest argument AGAINST this opportunity look like? Include specific examples."
```

After each query:
- **If using MCP tool**: Log the query manually to `.agent/perplexity-usage.json` (the MCP server doesn't auto-log to our budget file). Add an entry with timestamp, type "deep-research", model "sonar-deep-research", description, task_context, and estimated_cost 0.25.
- **If using Python client**: Budget logging happens automatically via `perplexity_client.py`.
- Save raw results to `.tmp/deep-research/foundation-[query-type].md`

**Foundation Compression** — Extract for agent injection:
- Top 25 data points with source URLs
- Key psychological patterns and verbatim language (exact quotes)
- Identified contradictions and open questions
- 3 sub-questions per parallel agent angle (informed by what the foundation revealed)

Save compressed foundation to `.tmp/deep-research/foundation-compressed.md`

> **Why this matters**: Existing workflows use basic `sonar` or `sonar-pro`. The `sonar-deep-research` model does multi-step internal research — it plans queries, executes them, synthesizes across sources, and returns deeply sourced data. This is the equivalent of a senior analyst spending hours, not a quick Google search.

---

### Step 3 — 3 Grounded Parallel Specialist Agents

Spawn 3 Agent tool sub-agents **in a single message** (true parallel execution).

Each agent receives:
1. The compressed foundation from Step 2
2. Their specific angle assignment with 3 key questions
3. The instruction below

#### Agent Prompt Template

```
You are a deep research specialist. Your role: [ROLE NAME].

**Research question**: [question]
**Your assigned angle**: [angle description]
**Key questions to answer**:
1. [question 1 — informed by foundation gaps]
2. [question 2 — informed by foundation gaps]
3. [question 3 — informed by foundation gaps]

## Foundation Data (already gathered — DO NOT repeat this)
[Compressed foundation: top 25 data points, key patterns, source URLs]

## Your Mission
The foundation above is your STARTING POINT, not your ceiling. Your job is to go DEEPER on your angle — find primary sources, case studies, real human language, expert opinions, and patterns the foundation MISSED.

**Surface-level findings are worthless.** Find what others can't find. Dig into:
- Primary sources (not summaries of summaries)
- Real human language (comments, reviews, forum posts)
- Case studies and specific examples (not generalizations)
- Data that contradicts or nuances the foundation
- Expert opinions and contrarian perspectives

**Tool budget**: [X] WebSearch + [Y] WebFetch
**Output**: Write findings to .tmp/deep-research/angle-[N]-[slug].md

## Output Format

# [Angle Name] — Deep Research Findings

## Key Discoveries (that go BEYOND the foundation)
- [Finding 1] — Source: [URL] — Why this matters: [implication]
- [Finding 2] — Source: [URL] — Why this matters: [implication]
[...]

## Verbatim Language & Real Human Voices
[Exact quotes from real people — Reddit, YouTube, reviews, forums]

## Patterns & Signals
[Non-obvious patterns you detected across sources]

## Contradictions with Foundation
[Where your findings differ from or nuance the foundation data]

## Data Quality
- Sources found: [count]
- Primary vs secondary: [ratio]
- Recency: [most recent source date]
- Confidence: [High/Medium/Low] with reasoning
```

#### Agent Specializations

| Agent | Role | What They Mine | Tool Budget |
|---|---|---|---|
| **Agent A: Pattern Hunter** | Real market patterns, growth signals, timing indicators | Industry reports, trend data, growth trajectories, market shifts, hiring patterns, funding signals, technology adoption curves | 7 WebSearch + 3 WebFetch |
| **Agent B: Psychology Miner** | Real human motivations, language, identity triggers, jobs-to-be-done | Reddit threads, YouTube comments, Amazon reviews, forum posts, Quora, social media discourse, product review sites | 7 WebSearch + 5 WebFetch |
| **Agent C: Contrarian Scout** | What everyone else misses — failures, counter-narratives, hidden risks, non-obvious opportunities | Failed products in the space, critical reviews, academic research, contrarian experts, historical analogues, regulatory risks | 7 WebSearch + 3 WebFetch |

**Agent B (Psychology Miner) is the key differentiator.** This agent specifically:
- Farms real human comments and language from communities
- Identifies avatar archetypes and identity patterns (like "that girl energy")
- Extracts verbatim phrases that reveal real pain, desire, and identity
- Maps jobs-to-be-done from behavioral patterns, not demographics
- Finds the emotional triggers that drive purchasing decisions
- Looks for the language people use to DESCRIBE THEMSELVES and their problems

Each agent writes to `.tmp/deep-research/angle-[N]-[slug].md`

---

### Step 4 — Synthesis + Contradiction Resolution

After all 3 agents return, read their outputs plus the foundation. Synthesize:

**4a. Cross-Pollination**
- Which findings from Agent A (patterns) explain what Agent B (psychology) found?
- Which psychology insights reveal WHY the market patterns exist?
- Which contrarian findings (Agent C) challenge or nuance the other agents' conclusions?

**4b. Contradiction Resolution**
- Where do agents disagree? Which has stronger evidence?
- If unresolvable: run 1-2 targeted follow-up WebSearch queries to triangulate
- Document contradictions that remain — these are often the most valuable insights

**4c. Pattern Elevation**
- Surface non-obvious connections that only emerge when you see all 3 angles together
- The insight that "everyone in this market complains about X" (Agent B) + "the top competitor doesn't address X" (Agent A) + "three attempts to solve X have failed" (Agent C) = a specific opportunity with known risks

**4d. Predictive Modeling**
- Based on the patterns found, what can we predict with high confidence?
- What would need to change for these predictions to fail?

---

### Step 5 — Adversarial Challenge Round

Before finalizing, pressure-test the synthesis:

1. **Confirmation Bias Check**: Did all agents anchor on the same narrative from the foundation? Are there findings that ONLY appear in one agent's work?
2. **Counter-Narrative Stress Test**: State the strongest argument AGAINST the emerging thesis. Is it addressed?
3. **Missing Enemy**: What threat, alternative, or disruption would invalidate these findings? Is it accounted for?
4. **Steelman the Opposition**: Present the best version of the counter-argument. Does the thesis survive?
5. **Source Quality Audit**: Flag any findings resting on a single source or uncorroborated claims. Mark confidence levels.
6. **Prediction Audit**: For each prediction, assign High/Medium/Low confidence and state what would need to be true for it to fail.

---

### Step 6 — Deliverable: Strategic Intelligence Report

Produce the final report using this structure:

```markdown
# Strategic Intelligence Report: [Topic]

**Date**: [date]
**Research Intent**: [intent classification]
**Perplexity Queries**: [count] | **Parallel Agents**: 3 | **Total Sources**: [count]

---

## 1. Executive Summary (BLUF)
[5-7 sentences that directly answer: "What should I do and why?" This is the board-level takeaway.]

## 2. The Real Landscape
[Market state, key players, growth signals, timing indicators. Every claim cited.]

### Key Data Points
| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| [metric] | [value] | [source URL] | [H/M/L] |

## 3. The Human Truth
[Psychology mining results. This section reads like a psychological portrait, not a demographic report.]

### Avatar Archetypes
[Identity patterns discovered — who these people ARE, not just what they buy]

### Verbatim Language
[Exact quotes that reveal real pain, desire, and identity — sourced]

### Jobs-to-be-Done
[What people are ACTUALLY trying to accomplish — mapped from behavior, not surveys]

### Emotional Triggers
[What drives purchasing decisions at the feeling level]

## 4. The Hidden Patterns
[Cross-cutting insights that only emerge from multi-angle analysis. Non-obvious connections. The "truth underneath."]

### Pattern Map
| Pattern | Evidence (Agent A) | Evidence (Agent B) | Evidence (Agent C) | Confidence |
|---------|-------------------|-------------------|-------------------|------------|

## 5. The Counter-Narrative
[What could go wrong. What skeptics say. Risks and failure modes. Steelmanned opposition.]

### Known Failures in This Space
[Specific examples of what has failed and why]

### Strongest Argument Against
[The best case for NOT pursuing this direction]

## 6. Strategic Recommendations
| # | Recommendation | Evidence Basis | Confidence | Expected Impact |
|---|---------------|----------------|------------|-----------------|
| 1 | [action] | [which findings] | [H/M/L] | [description] |

## 7. Prediction Map
| Prediction | Confidence | Based On | Would Fail If |
|-----------|------------|----------|---------------|

## 8. Source Appendix
### Angle A: Pattern Hunter
[URLs with quality rating]

### Angle B: Psychology Miner
[URLs with quality rating]

### Angle C: Contrarian Scout
[URLs with quality rating]

### Perplexity Foundation
[URLs from deep research queries]
```

Save to: `research_outputs/[date]-[topic-slug]-deep-research.md`

---

## Output Files

```
.tmp/deep-research/
  foundation-core.md
  foundation-psychology.md
  foundation-counter-narrative.md
  foundation-compressed.md
  angle-A-pattern-hunter.md
  angle-B-psychology-miner.md
  angle-C-contrarian-scout.md

research_outputs/
  [date]-[topic-slug]-deep-research.md
```

---

## Error Handling

- **1 agent fails**: Synthesize from 2 agents + foundation. Note the gap in the report.
- **Perplexity query fails**: Fall back to `sonar-pro` for that query. If all Perplexity fails, degrade to `/research-sprint`.
- **Budget exhausted mid-run**: Complete with whatever foundation data was gathered. Note in report: "Partial deep research — [N] of 3 Perplexity queries completed."
- **All agents return low-confidence results**: Flag in the report. Recommend follow-up research with specific questions to investigate.

---

## Estimated Cost & Time

| Component | Cost | Time |
|-----------|------|------|
| Perplexity Deep Research (2-3 queries) | $0.50-0.75 | 30-90 seconds |
| 3 Parallel Agents (WebSearch + WebFetch) | Free | 2-5 minutes |
| Synthesis + Adversarial | Free | 1-2 minutes |
| **Total** | **$0.50-0.75** | **4-8 minutes** |

At $30/month budget = **40-60 deep research runs per month**.

---

## Next Steps After Deep Research

- `/brief` — Convert findings into a full McKinsey-grade strategy brief
- `/design-offer` — Design an offer based on The Human Truth findings
- `/icp-build` — Build detailed ICP from psychology mining results
- `/content-sprint` — Create content grounded in the real language and triggers found
- `/roundtable` — Debate the strategic recommendations with expert agents
