---
description: Deploy an agent swarm to execute complex tasks with 10-50 experts working in orchestrated parallel
---

# /swarm Workflow

Orchestrate multiple expert agents to tackle complex objectives using the Swarm Commander skill.

// turbo-all

---

## Usage

```
/swarm [Your objective here]
/swarm --verbose [Your objective here]
```

### Flags

| Flag | Effect |
|------|--------|
| `--verbose` | Show each agent's FULL output inline before synthesis (learning mode) |
| (default) | Show only final synthesis with drill-down access to agent files |

## Steps

### 1. Read Swarm Commander Skill

Read the core methodology:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/SKILL.md
```

### 2. Read Genius Patterns

Internalize the 18 orchestration patterns:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/references/genius-patterns.md
```

### 3. Execute Phase 1: Swarm Planning

Read and apply:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/references/prompts/swarm-planning.md
```

Produce:
- `execution_plan.md` with dependency graph
- `work_orders/[agent_name].md` for each agent

### 4. Execute Phase 2: Agent Constellation

Read and apply:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/references/prompts/agent-constellation.md
```

Produce:
- `agent_constellation.md` with selection justification and tension map

**CHECKPOINT**: Present constellation to user for approval before execution.

### 4.5 Execute Phase 2.5: Perplexity Research Gate ⚠️ MANDATORY

> **This step is NON-NEGOTIABLE for any swarm with research/intelligence agents.**

Before ANY agent executes, ground the swarm in real data:

1. **Check budget**: Read `.agent/perplexity-usage.json` — verify remaining budget
2. **Identify research agents**: Any agent doing market intel, competitive analysis, social listening, or trend research
3. **Execute Perplexity queries** (max 10 per swarm, batched via Collapsing Rule):
   - Social listening: `mcp_perplexity-ask_perplexity_ask` for Reddit/forum pain points
   - Competitive intel: Named competitors, actual pricing, real positioning
   - Market validation: Real data with citations
   - Trend verification: Current-year sources
4. **Save research data** to `research_data/perplexity_findings.md`
5. **Log ALL queries** to `.agent/perplexity-usage.json`
6. **Feed research data INTO agent work orders** — agents must reference this file

**If budget is exhausted**: Fall back to `search_web` (NOT LLM-only). Notify user.
**If Perplexity unavailable**: Use `search_web` with same query structure. Notify user of degraded quality.

**Reference**: `directives/perplexity-usage-policy.md` and `directives/quality_assurance.md` (Mandate 5)

### 5. Execute Phase 3: Batch Execution

Read and apply:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/references/prompts/batch-execution.md
```

For each batch:
- Embody each expert's methodology
- Execute their work order
- **Reference `research_data/perplexity_findings.md`** for any factual claims
- Write output to `agent_outputs/[agent_name].md`
- **Tag each output** with research provenance: 🟢 GROUNDED / 🟡 SUPPLEMENTED / 🔴 PROJECTED

### 5.5. Execute Phase 3.5: Grounding Pass ⚠️ MANDATORY

> **This is the validation layer. No agent output reaches synthesis or the user without passing through this gate.**

After ALL agents have executed, run a Grounding Pass across every output file:

#### Purpose
Agent outputs contain expert frameworks and methodology — but they also contain factual claims (market sizes, growth rates, competitor names, pricing, behavioral patterns). The Grounding Pass validates every factual claim against the research data gathered in Phase 2.5.

#### Process (for EACH agent output file)

1. **Scan for factual claims** — Any number ($, %, market size), named entity (competitor, platform), trend assertion, or behavioral claim
2. **Cross-reference against `research_data/perplexity_findings.md`**:
   - **Claim matches data** → Tag 🟢 GROUNDED, add source citation inline
   - **Claim is directionally correct but imprecise** → Tag 🟡, correct with real data, note original claim
   - **Claim cannot be verified or is wrong** → Tag 🔴 PROJECTED or correct/remove entirely
3. **Inject missing intelligence** from research data that agents SHOULD have included:
   - Real competitor names and pricing where agents used generic references
   - Reddit verbatim quotes and sentiment data where agents used hypothetical pain points
   - Corrected market data (growth rates, TAM, segment sizes)
4. **Add Grounding Summary** at the top of each file:
   ```
   > **Grounding Pass**: ✅ Complete | [DATE]
   > **Claims Verified**: X/Y | **Corrections Made**: Z
   > **Research Source**: research_data/perplexity_findings.md
   ```

#### What Gets Corrected
- Inflated growth rates (e.g., "15-20% growth" → actual CAGR)
- Generic competitor references → real named competitors with pricing
- Hypothetical buyer quotes → actual Reddit/forum verbatims
- Unverified trend assertions → tagged with verification verdicts
- Missing data gaps → flagged clearly for the user

#### Quality Gate
**An agent output CANNOT proceed to synthesis unless:**
- [ ] Every factual claim is tagged (🟢/🟡/🔴)
- [ ] The Grounding Summary header is present
- [ ] No 🔴 PROJECTED claims remain without explicit user acknowledgment

#### Standalone Execution
This phase can also be run independently via `/grounding-pass` for any set of documents that need validation against research data.

### 6. Execute Phase 4: Swarm Synthesis

Read and apply:
```
/Users/farricecain/Google Antigravity/skills/swarm-commander/references/prompts/swarm-synthesis.md
```

Produce:
- `final_synthesis.md` with unified findings, provenance, and minority positions

### 7. Deliver to User

Present:
- Executive summary
- Key recommendations with confidence
- Minority report (if applicable)
- Links to detailed agent outputs for deep dives

---

## Example Invocations

```
/swarm Research my top 5 competitors in AI copywriting
/swarm Plan a product launch for my new course
/swarm Analyze 10 different positioning strategies for my brand
/swarm Write a comprehensive content strategy with multiple expert perspectives
```

## Swarm Sizes

- **Squad (3-5)**: Quick, focused tasks
- **Team (6-12)**: Standard complexity
- **Platoon (13-25)**: Deep research
- **Army (26-50)**: Enterprise initiatives

## Notes

- User approves constellation before execution begins
- All intermediate outputs saved to files for later review
- Minority positions always preserved
- Provenance tracked for every finding

## Cost & Quality Guardrails

- **Perplexity budget**: Max 10 queries per swarm (see `directives/perplexity-usage-policy.md`)
- **Loop protection**: If any agent makes 3+ consecutive queries with <10% new info, STOP that agent
- **Provenance tagging**: Every agent output must be tagged 🟢/🟡/🔴 (see `directives/quality_assurance.md`)
- **No Phantom Research**: Research agents MUST invoke external tools — LLM-only intelligence is NEVER acceptable
- **Budget check**: Read `.agent/perplexity-usage.json` BEFORE the swarm starts
