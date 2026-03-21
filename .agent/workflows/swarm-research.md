---
description: Deploy orchestrated parallel research swarm — Manus/Kimi-style wide research using free-tier tools, with optional Perplexity premium layer. Decomposes questions → fires parallel sub-agents → synthesizes across all findings → research quality gate.
---

# Swarm Research Workflow

This workflow gives you systematic, multi-angle deep research WITHOUT requiring premium API calls. It uses `search_web` + `read_url_content` (both free and unlimited) as the workhorse, with Perplexity `sonar-deep-research` available as a premium layer when budget allows.

**How it works**: Like Manus.ai or Kimi 2.5, this decomposes one question into 4-6 sub-questions, researches each angle in parallel, then synthesizes everything into a grounded intelligence document.

---

## Step 1: Decompose the Research Question

First, decompose the user's question into parallel research tracks.

Run the decomposition engine:
```bash
python3 execution/deep_research_engine.py --decompose-only "USER_QUERY"
```

This produces 4-6 sub-questions, each with 3 pre-built search queries and an angle (market_data, psychology, competitive, contrarian). The output is a markdown document ready for agent handoff.

**If the auto-decomposition doesn't fit**, manually write 4-6 sub-questions following this formula:

1. **Data Foundation**: "What are the core facts, numbers, and current state of {topic}?"
2. **Psychology/Audience**: "What do real people say about {topic} on Reddit, forums, reviews?"
3. **Competitive Landscape**: "Who else is doing {topic} and what strategies are working?"
4. **Contrarian/Risk**: "What are the criticisms, failures, and risks related to {topic}?"
5. **Case Studies**: "What are 3-5 specific real examples of {topic} with named companies/people?"
6. **Expert Perspective**: "What do domain experts or practitioners recommend about {topic}?"

---

## Step 2: Execute Parallel Research Tracks (Free Tier)

For each sub-question, execute this research sequence using the agent's built-in tools. This is the core free-tier research layer — no API costs.

### Per Sub-Question Research Protocol

For each of the 4-6 sub-questions:

**Phase A — Wide Search (3-5 calls per sub-question)**

Use `search_web` with each of the pre-built search queries from the decomposition. For each search:
- Extract all cited URLs from the results
- Note the key claims and data points WITH their source URLs
- Flag anything that sounds like LLM summary vs. actual cited data

**Phase B — Deep Read (2-3 calls per sub-question)**

Pick the 2-3 most promising URLs from Phase A and use `read_url_content` on each:
- Get the full page content
- Extract specific numbers, quotes, examples, and data points
- Note the publication date (for recency scoring)
- Record the author/organization (for authority scoring)

**Phase C — Findings Assembly**

For each sub-question, produce a structured findings block:

```markdown
### Sub-Question: [the question]
**Angle**: [market_data / psychology / competitive / contrarian]
**Sources searched**: [count]
**Pages read in full**: [count]

#### Key Findings
- 🟢 [High-confidence finding with specific data] — Source: [URL]
- 🟡 [Medium-confidence finding] — Source: [URL]
- 🔴 [Low-confidence or single-source finding] — Source: [URL]

#### Verbatim Quotes
> "[Exact quote from source]" — [Author/Source, Date]

#### Data Points
| Metric | Value | Source | Date |
|--------|-------|--------|------|
| [metric] | [value] | [source URL] | [date] |
```

---

## Step 3: Synthesis (Cross-Track Integration)

After all sub-questions are researched, synthesize across all tracks:

1. **Cross-reference findings**: Do findings from different angles corroborate each other?
2. **Flag contradictions**: Where do sources disagree? Note both sides with URLs.
3. **Identify gaps**: What questions remain unanswered? What angles weren't covered?
4. **Rank by confidence**: High (3+ corroborating sources), Medium (1-2 sources), Low (unverified)
5. **Write the synthesis**: A coherent narrative that answers the original question, with every data point linked to its source.

Template:

```markdown
# Research Intelligence: [Original Question]

## Executive Summary
[3-5 sentence summary of the key findings — every claim sourced]

## Key Findings by Theme
### [Theme 1: e.g., Market Opportunity]
[Findings from relevant sub-questions, cross-referenced]

### [Theme 2: e.g., Audience Psychology]
[Customer voice data, pain points, language patterns]

### [Theme 3: e.g., Competitive Reality]
[What competitors do, what's working, what gaps exist]

### [Theme 4: e.g., Risks & Contrarian View]
[What could go wrong, what critics say, blind spots]

## Contradictions & Open Questions
- [Where sources disagree]
- [What we still don't know]

## Source Appendix
[All unique URLs organized by domain]
```

---

## Step 4: Premium Layer (Optional — Budget Permitting)

If the Perplexity budget allows ($30/month pool), enhance the synthesis with premium research:

```bash
# Check remaining budget first
python3 -c "from execution.perplexity_client import PerplexityClient; c=PerplexityClient(); print(f'Remaining: ${c.budget_remaining():.2f}')"
```

If budget >= $1.00, fire 1-2 `sonar-deep-research` calls on the highest-value sub-questions:
```bash
python3 execution/deep_research_engine.py --depth deep "THE MOST IMPORTANT SUB-QUESTION"
```

**Budget guardrails**:
- Quick/Standard research: Always use free tier (`search_web` + `read_url_content`)
- Deep research: Only when user explicitly requests deep, OR the topic is high-stakes strategy
- Never fire more than 3 `sonar-deep-research` calls in a single session

---

## Step 5: Quality Gate

Run the research quality gate on the final output:

```bash
python3 execution/research_quality_gate.py validate .tmp/research/final-report.md --strict
```

Must pass:
- ✅ Minimum source count met for depth level
- ✅ 80%+ of data claims have source URLs
- ✅ No echo chamber (contrarian perspectives present)
- ✅ Time-sensitive data is from 2024+
- ✅ No more than 3 naked claims (unsourced superlatives/absolutes)

If the gate fails, address the specific issues it identifies before delivering the research.

---

## When to Use Each Depth

| Scenario | Depth | Tools Used | Cost | Time |
|----------|-------|-----------|------|------|
| Sanity check on a claim | Quick | 3-5 `search_web` | Free | 30s |
| Content research for a post | Standard | 10-15 `search_web` + 3-5 `read_url_content` | Free | 2-3 min |
| Strategy brief or council prep | Standard+ | Full workflow above | Free | 5-10 min |
| Deep strategic intelligence | Deep | Full workflow + Perplexity premium | ~$0.50-0.75 | 8-15 min |
| ICP/audience deep dive | Deep | Full workflow + Reddit/forum deep reads | ~$0.25 | 10-15 min |

---

## Integration with Other Workflows

This workflow is the **research foundation** for:

- **`/deep-research`**: Directly calls this workflow with Deep depth
- **`/council`**: Research phase before expert deliberation
- **`/roundtable`**: Research phase before multi-expert discussion
- **`/generate-brief`**: Foundation research for strategy briefs
- **`/icp-research`**: VOC mining phase
- **`/parallel-swarm`**: Each swarm agent uses this for their research track
- **`/mini-brief`**: Research validation step
- **`/competitor-intel`**: Competitive research angle
- **`/betting-edge`**: Player/stat research

**Rule**: Any workflow that produces facts, data, or claims as part of its output MUST run at least Quick depth research through this system. No exceptions.
