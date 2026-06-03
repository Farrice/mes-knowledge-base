---
description: Spin up an AI council
---

# /council

Instantly create and run an AI council for any decision requiring multiple perspectives.

> **Now a preset of the Collective Genius Council (2026-06-02).** The reliable, default path is
> the Workflow engine — invoke the **Workflow tool** with `scriptPath:
> .agent/workflows/collective-genius-council.workflow.js` and `args: { "task": "<the decision>",
> "mode": "tight" }`. It convenes a diverse cross-domain council + your lens, runs genuine 2-round
> deliberation (genius-loaded, contradictions preserved as forks), synthesizes, and emits a "How
> the Masters Thought" learning digest. The manual runbook below is the fallback when the Workflow
> tool isn't available.

## Usage

```
/council [your decision or question]
```

## Examples

```
/council Should I raise my prices from $500 to $1,500?
/council Which of these three product ideas should I build first?
/council Is it time to hire my first employee?
```

## Steps

### 1. Capture the Decision

If no decision provided, ask:
- What decision are you facing?
- What are the stakes if you get it wrong?
- What options are you considering?

### 2. Generate Council Configuration

Read and apply: `skills/mark-kashef-ai-councils/references/prompts/council-commander.md`

Generate:
- 3-4 perspective agents with behavioral mandates
- Natural tensions between agents
- Specific questions each agent must answer

### 2.5. 🔒 MANDATORY: Research Grounding Pass (Anti-Echo-Chamber Gate)

> ⚠️ **This step is NON-NEGOTIABLE.** Without it, the council becomes a confirmation bias engine — agents will repackage the user's own beliefs in expert costumes.

**Before ANY agent speaks, run 3-5 grounding queries** using the tiered tool strategy from `directives/research-protocol.md`:

**Tool priority**:
- **Priority 1**: `mcp_perplexity-ask_perplexity_ask` (Sonar via MCP) — check `.agent/perplexity-usage.json` budget first
- **Priority 2**: `search_web` (free, unlimited) — the workhorse for most queries
- **Priority 3**: `read_url_content` (free, unlimited) — for reading top results in full

**Query targets**:
1. **Identify the user's existing belief** — What does the user ALREADY think the answer is?
2. **Research the OPPOSITE position** — Find data that supports the option the user is leaning AGAINST
3. **Verify factual claims** — Any numbers, market sizes, conversion rates, or competitive claims cited by the user or existing KIs
4. **Find real competitors/examples** — Named entities doing what's being discussed, with actual pricing and outcomes
5. **Search for disconfirming evidence** — Specifically look for reasons the user's preferred option might be wrong

**Hard Rules**:
- Every council agent MUST cite at least one piece of external research in their initial position
- Any factual claim without a source gets tagged 🔴 PROJECTED
- If research contradicts the user's assumption, the council MUST present this conflict prominently — not bury it
- The council output MUST include a "Claims Grounding Table" showing which claims are 🟢 GROUNDED, 🟡 SUPPLEMENTED, or 🔴 PROJECTED

**Why**: Agents deliberating from existing context = echo chamber. Agents deliberating from external research = actual counsel. The difference is the research step.

### 3. Run Deliberation

**Round 1: Initial Positions** (grounded in research)
Each agent states their position and reasoning from their mandate, citing research from Step 2.5.

**Round 2: Steelman**
Each agent articulates the strongest version of opposing arguments.

**Round 3: Crux Isolation**
- Where exactly do agents disagree?
- What evidence would change minds?
- Are disagreements resolvable?
- **Which claims are 🔴 PROJECTED vs 🟢 GROUNDED?** Flag honestly.

### 4. Synthesize and Deliver

Output:
- Areas of genuine agreement
- Primary recommendation with confidence level
- Minority report (dissenting view and when it would be right)
- Decision checkpoints (when to revisit)
- **Claims Grounding Table** (mandatory)

## Output Format

```markdown
# COUNCIL DECISION: [Topic]

## The Council
[Brief description of agents assembled]

## Claims Grounding Table
| Claim | Source | Status |
|-------|--------|--------|
| [Claim 1] | [Perplexity/search citation] | 🟢/🟡/🔴 |

## Deliberation Summary

### Points of Agreement
- [Point 1]
- [Point 2]

### Key Disagreement
[The core tension]

## Recommendation

**Action**: [What to do]
**Confidence**: [High/Medium/Low]
**Reasoning**: [Why]

## Minority Report
**Dissenting view**: [Position]
**They would be right if**: [Conditions]

## Decision Checkpoints
Revisit this decision if:
- [ ] [Condition 1]
- [ ] [Condition 2]
```

## Quick Modes

- `/council [decision]` - Full deliberation (default)
- `/council rapid [decision]` - Quick synthesis, skip steelman (Step 2.5 still runs)
- `/council devil [decision]` - Just two opposing views (Step 2.5 still runs)

## Notes

- Best for high-stakes decisions where being wrong is costly
- Overkill for simple yes/no questions with obvious answers
- The value is in surfacing perspectives you'd otherwise miss
- **🔴 ECHO CHAMBER WARNING**: If the council output agrees with the user on every point, something is wrong. True multi-perspective deliberation should produce AT LEAST one uncomfortable insight the user didn't already have. If all agents agree with the user, re-run Step 2.5 with stronger disconfirming queries.
