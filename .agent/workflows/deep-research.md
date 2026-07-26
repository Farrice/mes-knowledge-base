---
description: Deep Research
---

# /deep-research — Deep Research

Deploy the full research stack: **Gemini Deep Research (primary) or Perplexity sonar-deep-research (fallback)** as the foundation layer, 3 parallel specialist agents (Pattern Hunter, Psychology Miner, Contrarian Scout) to deepen each angle grounded in real data, synthesis with contradiction resolution, adversarial challenge round, and a McKinsey-grade Strategic Intelligence Report.

**Foundation backend (as of 2026-06-01 — Unified Research Engine)**: This workflow now invokes **`execution/research.py`** as the single foundation call. The engine runs **Gemini-first → Perplexity → Claude bedrock floor** internally, logs cost honestly (failed/empty calls cost $0 and never burn budget), and returns a **Research Receipt** showing exactly which engine served the foundation, what failed, what depth was achieved, and what it cost. The bedrock floor (WebSearch + WebFetch + Tavily) means this workflow **cannot break** — if both accelerators fail, the native floor catches it and the receipt says so. **Every report must lead with the Research Receipt** so the reader knows the grounding depth before trusting it.

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

### Step 0 — Budget Gate (handled by the engine)

**You no longer hand-gate budget here.** The unified engine (`execution/research.py`,
Step 2) does Gemini-first → Perplexity → free bedrock floor internally, each gated on
its own budget. Gemini is $0 under Ultra; Perplexity fires only if Gemini fails AND
budget ≥ $0.50; the floor is always free. A failed/empty accelerator costs **$0** and
is recorded as a failure — never as spend. The Research Receipt reports the actual path.

There is **no "both budgets exhausted → can't research" state** anymore: the bedrock
floor (WebSearch + WebFetch + Tavily) is always available at $0, so research always
returns a real, sourced result or an honest FAILED — it never silently produces nothing.

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

### Step 2 — Deep Research Foundation (Unified Engine)

**For `deep`/`max` depth, the PRIMARY is the native expert SWARM** — run the Workflow tool
with `.agent/workflows/deep-research-swarm.workflow.js` and `args: {query, depth}`. It
decomposes → casts world-class expert personas (Alen Sultanic / April Dunford / McRaney /
Harry Dry / …) → fans out 10-12 (deep) or up to ~36 (max) parallel subagents → gap-fill loop
→ adversarial verify → synthesizes collective insight, **$0 incremental**, with Gemini Deep
Research merging in parallel. It returns the honest Research Receipt + the cited brief.

For `quick`/`standard` (or a fast single call), use the dispatcher directly — Gemini-first →
Perplexity → bedrock floor, same receipt:

```bash
cd "/Users/farricecain/Google Antigravity" && python3 execution/research.py "[FOUNDATION QUERY]" --depth standard --task-context "deep-research"
```

- Use `--depth max` for maximum comprehensiveness (Gemini Deep Research Max when available).
- The printed **Research Receipt** tells you which engine served the foundation
  (`gemini_deep` / `perplexity` / `native`), the status (`REAL` / `DEGRADED` / `FAILED`),
  provenance %, and `$` cost. **Copy the receipt verbatim into the top of the final report.**
- If `status=DEGRADED` with `engine_used=native` and the warning says *"fan-out pending"*,
  the engine wrote `.tmp/research/<slug>/native-directive.md` — your Step 3 specialist agents
  ARE that fan-out. After Step 3, run the ingest call (below) to upgrade the result to `REAL`.
- For machine-readable output add `--json` (returns the typed `ResearchResult`).

**Ingest the specialist findings** (after Step 3) to fold the agent fan-out into the typed result:
```bash
python3 execution/research.py ingest --findings .tmp/research/<slug>/native-findings.jsonl --query "[FOUNDATION QUERY]" --depth deep
```
Each specialist writes one JSON object per validated finding (schema in the directive);
**every finding needs a real `source_url`** or it is dropped on ingest (provenance integrity).

<details><summary>ROLLBACK (deprecated direct-client path — kept one release for instant revert)</summary>

```bash
# Old direct path — superseded by research.py. Use ONLY if the engine is unavailable.
# python3 execution/deep_research_client.py "[QUERY]" --mode standard --task-context "deep-research"
# python3 execution/deep_research_engine.py --depth deep "[QUERY]"
```
</details>

**Sub-agents** (Step 3): Each parallel agent uses the free-tier research stack:
- `search_web` — 5-7 calls per agent (free, unlimited)
- `read_url_content` — 2-3 calls per agent for deep page reads (free, unlimited)
- `perplexity_ask` (basic sonar via MCP) — 1-2 calls per agent for synthesis (cheap, ~$0.01)
- Tavily MCP (`tavily_search`) — structured search alternative if configured

Full sub-agent research protocol: `.agent/workflows/deep-research-swarm.workflow.js` (multi-wave engine; `swarm-research.md` is a superseded stub — do not cite it). Depth floors: `execution/research_depth.py` (single source of truth, 2026-07-26).

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

**Budget logging is automatic and honest** — the engine logs real spend only for calls
that returned validated content; failed/empty calls cost $0 and go to a separate
`failures` array, never the budget counter. No manual usage-file editing (that was the
old AI-memory-dependent step — now deterministic). Save raw foundation output to
`.tmp/research/<slug>/` (the engine's working dir) or `.tmp/deep-research/foundation-[query-type].md`.

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

**Tool budget**: [X] `search_web` + [Y] `read_url_content`
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
| **Agent A: Pattern Hunter** | Real market patterns, growth signals, timing indicators | Industry reports, trend data, growth trajectories, market shifts, hiring patterns, funding signals, technology adoption curves | 7 `search_web` + 3 `read_url_content` |
| **Agent B: Psychology Miner** | Real human motivations, language, identity triggers, jobs-to-be-done | Reddit threads, YouTube comments, Amazon reviews, forum posts, Quora, social media discourse, product review sites | 7 `search_web` + 5 `read_url_content` |
| **Agent C: Contrarian Scout** | What everyone else misses — failures, counter-narratives, hidden risks, non-obvious opportunities | Failed products in the space, critical reviews, academic research, contrarian experts, historical analogues, regulatory risks | 7 `search_web` + 3 `read_url_content` |

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
- If unresolvable: run 1-2 targeted follow-up `search_web` queries to triangulate
- Document contradictions that remain — these are often the most valuable insights

**4c. Pattern Elevation**
- Surface non-obvious connections that only emerge when you see all 3 angles together
- The insight that "everyone in this market complains about X" (Agent B) + "the top competitor doesn't address X" (Agent A) + "three attempts to solve X have failed" (Agent C) = a specific opportunity with known risks

**4d. Predictive Modeling**
- Based on the patterns found, what can we predict with high confidence?
- What would need to change for these predictions to fail?

---

### Step 5 — Adversarial Challenge Round + Quality Gate

Before finalizing, pressure-test the synthesis:

1. **Confirmation Bias Check**: Did all agents anchor on the same narrative from the foundation? Are there findings that ONLY appear in one agent's work?
2. **Counter-Narrative Stress Test**: State the strongest argument AGAINST the emerging thesis. Is it addressed?
3. **Missing Enemy**: What threat, alternative, or disruption would invalidate these findings? Is it accounted for?
4. **Steelman the Opposition**: Present the best version of the counter-argument. Does the thesis survive?
5. **Source Quality Audit**: Flag any findings resting on a single source or uncorroborated claims. Mark confidence levels.
6. **Prediction Audit**: For each prediction, assign High/Medium/Low confidence and state what would need to be true for it to fail.

**Research Quality Gate** (mandatory before Step 6):
```bash
python3 execution/research_quality_gate.py validate .tmp/deep-research/foundation-compressed.md --strict
```
Must pass: source count ≥ 15, provenance ≥ 80%, no echo chamber, time-sensitive data from 2024+.

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
| Gemini Deep Research (Ultra quota) | $0 | 5-15 minutes |
| Perplexity (DEAD — never propose paid credits) | n/a | n/a |
| 3 Parallel Agents (`search_web` + `read_url_content`) | Free | 2-5 minutes |
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
