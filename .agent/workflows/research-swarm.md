---
description: Fire 3 parallel research agents to scan a topic/market/space before building
---

# /research-swarm -- Pre-Build Intelligence Scan

Fire 3 parallel research agents -- Market Scanner, Audience Scanner, System Scanner -- to generate a unified intelligence brief before you commit to building anything. Returns market landscape, target audience profile, existing system assets, gaps, and recommended next steps.

## Usage

```
/research-swarm [topic, market, or project name]
/research-swarm "AI coaching tools for S&C coaches"
/research-swarm "EDM streetwear brand positioning"
```

## When to Use

- Before starting a new project, product, or market entry
- When you need a 360-degree view of a space before committing time or money
- Before writing a strategy brief -- this feeds the brief with real data
- When you suspect the codebase already has relevant assets but aren't sure what exists
- Before `/brief`, `/design-offer`, `/icp-build`, or any strategy workflow

## When NOT to Use

- You already know the market well and just need to execute (use `/ship` or `/content-sprint`)
- The task is purely creative and not data-dependent (use `/writers-room` or `/variant-sprint`)
- You need deep, multi-round research on a single angle (use `/deep-research` or `/research-sprint`)
- You need real-time competitive pricing or live data (use `/spy-market` or `/parallel-research --angles`)

---

## Steps

### 1. Accept Topic and Confirm Scope

Take the user's topic/market/project. Before launching, confirm the scan plan:

```
## Research Swarm Deployment

**Topic**: [topic]

| Agent | Role | Focus |
|-------|------|-------|
| Agent 1 | Market Scanner | Landscape, competitors, trends, pricing, market size |
| Agent 2 | Audience Scanner | ICP profile, pain points, language, consumer posture |
| Agent 3 | System Scanner | Existing skills, agents, extractions, knowledge in codebase |

Launch all 3 in parallel? Or adjust focus areas?
```

Wait for user approval (or proceed if intent is clear and Score >= 4).

### 2. Fire 3 Agents IN PARALLEL

Spawn 3 Agent tool calls **in a single message**. Each agent runs independently.

---

**Agent 1: Market Scanner**

```
You are a market intelligence researcher. Your job is to scan the landscape for: [topic]

**Your focus**:
- Market size and growth trajectory (find real numbers)
- Top 5-10 competitors or existing players -- names, positioning, pricing
- Key trends shaping this space in 2025-2026
- Pricing models and revenue benchmarks
- Gaps or underserved segments

**Instructions**:
1. Use Perplexity (`mcp_perplexity-ask_perplexity_search`) for 3-5 targeted market queries
   - Check `.agent/perplexity-usage.json` budget first; fall back to `search_web` if over budget
2. Use `search_web` for additional queries (5-7 calls)
3. Use `read_url_content` to read the top 3-5 most relevant results in full
4. For each finding, record: data point, source URL, and one actionable implication

**Output format**:
## Market Landscape: [topic]

### Market Size & Growth
- [Finding with source URL]

### Key Players
| Player | Positioning | Pricing | Notable |
|--------|------------|---------|---------|
| [name] | [positioning] | [price] | [note] |

### Trends (2025-2026)
- [Trend 1 with source]
- [Trend 2 with source]

### Gaps & Underserved Segments
- [Gap 1]
- [Gap 2]

### Confidence: [High/Medium/Low]

Write output to: .tmp/research-swarm/market-scanner.md
```

---

**Agent 2: Audience Scanner**

```
You are an audience intelligence researcher specializing in consumer posture analysis. Your job is to build a target audience profile for: [topic]

**Your focus**:
- Who is the ideal customer/user? Demographics, psychographics, identity
- What are their top 3-5 pain points (in THEIR language, not marketer language)?
- What is their current awareness level (unaware, problem-aware, solution-aware)?
- What objections or resistance patterns exist?
- Where do they hang out online? What communities, platforms, subreddits?
- What language do they use to describe their problem?

**Instructions**:
1. Read `skills/dai-media-consumer-posture/SKILL.md` for consumer posture framework
2. Use `search_web` (5-7 calls) to find audience discussions:
   - Reddit threads, forum posts, review sites, social media discussions
   - Search for "[topic] frustrations reddit", "[topic] reviews", "[topic] community"
3. Use `read_url_content` (3-5 calls) to read the most revealing audience discussions
4. Extract direct quotes -- the actual language real people use
5. Build the posture profile: what do they believe, fear, desire, resist?

**Output format**:
## Target Audience Profile: [topic]

### ICP Snapshot
- **Who**: [demographics + psychographics]
- **Current state**: [where they are now]
- **Desired state**: [where they want to be]
- **Awareness level**: [unaware / problem-aware / solution-aware]

### Pain Points (in their language)
1. "[Direct quote or paraphrase]" -- Source: [URL]
2. "[Direct quote or paraphrase]" -- Source: [URL]
3. "[Direct quote or paraphrase]" -- Source: [URL]

### Objections & Resistance Patterns
- [Objection 1]
- [Objection 2]

### Where They Congregate
| Platform | Specific Community | Activity Level |
|----------|-------------------|----------------|
| Reddit | r/[subreddit] | [active/moderate/low] |

### Language Map
- **Words they use**: [list]
- **Words that repel them**: [list]

### Confidence: [High/Medium/Low]

Write output to: .tmp/research-swarm/audience-scanner.md
```

---

**Agent 3: System Scanner**

```
You are an internal systems analyst for the Antigravity AI orchestration system. Your job is to find everything in the local codebase that's relevant to: [topic]

**Your focus**:
- Existing skills in `skills/` that relate to this topic
- Existing agents in `agents/` with relevant expertise
- Extractions in `extractions/` from relevant domain experts
- Knowledge base entries in `knowledge/` on this topic
- Strategy briefs in `strategy_briefs/` that touch this space
- Research outputs in `research_outputs/` on related topics
- Deliverables in `deliverables/` for similar projects
- Active projects in `projects/` that overlap

**Instructions**:
1. Search the codebase for files related to [topic]:
   - Glob for pattern matches in skills/, agents/, extractions/, knowledge/, strategy_briefs/, research_outputs/
   - Grep for topic keywords across all markdown files
2. For each relevant asset found, record:
   - File path
   - What it contains (1-line summary)
   - How it could be reused for this project
3. Check `DOMAIN_REGISTRY.md` for expert swim lanes that map to this topic
4. Check `agents/_framework/invocation-cards.md` for relevant expert cards

**Output format**:
## System Assets: [topic]

### Relevant Skills
| Skill | Path | Relevance |
|-------|------|-----------|
| [name] | `skills/[name]/` | [how it helps] |

### Relevant Agents
| Agent | Path | Expertise |
|-------|------|-----------|
| [name] | `agents/[name]/` | [relevant capability] |

### Existing Knowledge
| Asset | Path | Contents |
|-------|------|----------|
| [name] | [path] | [summary] |

### Expert Routing Recommendation
Based on DOMAIN_REGISTRY.md, the following experts map to this topic:
- [Expert 1] -- [reason]
- [Expert 2] -- [reason]

### Reuse Opportunities
- [Asset 1] can be directly applied to [specific use]
- [Asset 2] provides foundation for [specific use]

### Coverage Gaps
- [What's missing from the system that would need to be built]

Write output to: .tmp/research-swarm/system-scanner.md
```

### 3. Wait for All 3 Agents to Return

All three agents run independently and write their outputs to `.tmp/research-swarm/`. Wait for all to complete before proceeding.

### 4. Synthesize into Unified Intelligence Brief

Read all three outputs from `.tmp/research-swarm/` and produce a unified brief:

```markdown
# Intelligence Brief: [Topic]

**Date**: [date]
**Scan Type**: Research Swarm (3 parallel agents)

## Executive Summary
[3-5 sentences synthesizing the most important findings across all three scans.
What's the opportunity? What's the risk? What do we already have?]

## Market Landscape
[Top findings from Agent 1 -- market size, key players, trends, gaps]

## Target Audience
[Top findings from Agent 2 -- ICP, pain points, language, posture]

## Existing System Assets
[Top findings from Agent 3 -- what we already have, what can be reused]

## Gaps & Opportunities

### Opportunities (where market demand meets our capability)
1. [Opportunity + evidence from which agent(s)]
2. [Opportunity + evidence]

### Gaps (what we'd need to build or acquire)
1. [Gap + what would fill it]
2. [Gap + what would fill it]

## Recommended Next Steps

| # | Action | Rationale | Suggested Workflow |
|---|--------|-----------|-------------------|
| 1 | [action] | [why, based on which findings] | `/[workflow]` |
| 2 | [action] | [why] | `/[workflow]` |
| 3 | [action] | [why] | `/[workflow]` |

## Sources
[All URLs cited across all three scans]

## Claims Grounding
| Claim | Source | Status |
|-------|--------|--------|
| [claim] | [source] | GROUNDED / SUPPLEMENTED / PROJECTED |
```

### 5. Save and Deliver

Save the unified brief to `.tmp/research-swarm-[topic-slug].md`.

Present to user with suggested next moves:
- `/brief` -- Expand into a full McKinsey-grade strategy brief
- `/icp-build` -- Deep-dive on the audience profile
- `/parallel-swarm` -- Multi-expert analysis on specific opportunities
- `/design-offer` -- Design an offer based on the identified gaps
- Direct expert consultation via intent pipeline

---

## Limits

- **3 agents always** -- this is a breadth scan, not a depth drill
- Each external research agent gets 5-7 `search_web` + 3-5 `read_url_content` calls
- System Scanner uses only local file search (no API calls)
- Total scan time: 2-5 minutes depending on topic complexity
- For deeper research on any single angle, follow up with `/deep-research` or `/research-sprint`

## Cost

- Agent 1 + Agent 2: Perplexity budget (3-5 queries each, check `.agent/perplexity-usage.json`) + free search_web calls
- Agent 3: Zero cost (local file search only)
- Total: ~$0.10-0.30 depending on Perplexity usage

---

*Created: 2026-04-03*
*Related workflows: `/parallel-research`, `/brief`, `/spy-market`, `/research-sprint`*
