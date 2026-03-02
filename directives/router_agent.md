# Router Agent Directive

> **Purpose**: Lightweight intent-to-expert dispatcher. Fast-path routing algorithm using invocation cards before full agent loading.
> **Reads**: `agents/_framework/invocation-cards.md` (Tier 0), then `AGENT_INDEX.md` for deep matching
> **Loading Protocol**: `directives/agent-loading-protocol.md`

---

## Routing Algorithm

On every user request:

### Step 1: Classify Intent (Fast)

Parse the request into one or more domain categories:

```
DOMAINS: [research | content | strategy | copywriting | brand | product | sales | video | ai | seo | design | writing | communication]
COMPLEXITY: [simple | moderate | complex | swarm-worthy]
```

### Step 2: Card Check FIRST (Tier 0 — ALWAYS)

1. Read `agents/_framework/invocation-cards.md` (~50 tokens per expert)
2. Match request domain to expert cards (DOMAIN + CORE METHOD fields)
3. Use PAIRS WITH field to identify complementary experts
4. Return top 1-3 agents ranked by relevance

**Only escalate to `AGENT_INDEX.md`** if:
- No card matches the domain (missing card → read AGENT_INDEX.md, then add a card after)
- Need deep keyword matching beyond what cards provide

### Step 3: Apply Escalation Ladder

Based on complexity, determine the engagement level:

| Level | Label | When | Loading Tier | Action |
|-------|-------|------|-------------|--------|
| 1 | Solo | Clear domain, single expert | **Tier 1** (SKILL.md + prompt) | Auto-route silently, deliver |
| 2 | Support | Main expert + complement | **Tier 1-2** | Load agent + supporting skill |
| 3 | Mini-council | Multiple perspectives needed | **Tier 2** or **Tier 3** (sub-agents) | Present recommendation, wait for approval |
| 4 | Council/Swarm | High-stakes, multi-domain | **Tier 3** (sub-agents) | Use `/roundtable` or `/swarm` |
| 5 | Human | Ambiguous intent | **Tier 0 only** | Ask user to clarify |

### Step 4: Execute or Recommend

**For Levels 1-2** (most requests):
- Auto-route silently. Load skill files per the tiered chain, apply framework, deliver.
- Invocation card is sufficient context for routing — no need to read AGENT.md for simple tasks.

**For Levels 3-4**:
- Present the Expert Recommendation Block (defined in `expert_auto_routing.md`)
- Use invocation card data to build the recommendation (don't load full files until approved)
- Wait for user confirmation, THEN load at Tier 2-3

**For Level 5**:
- Ask 1-2 targeted clarifying questions
- Do NOT proceed until user clarifies

---

## Complexity Signals

| Signal | Complexity |
|--------|------------|
| Single action verb ("write", "analyze", "fix") | Simple |
| "should I..." / "compare" / "what's the best approach" | Moderate |
| "build a strategy for..." / "create a full plan" | Complex |
| "research + build + launch" / multi-step pipeline | Swarm-worthy |

---

## Integration

- **Replaces**: Manual scanning of domain detection tables
- **Works with**: `expert_auto_routing.md` (ensemble patterns, recommendation block format)
- **Works with**: `agents/_framework/invocation-cards.md` (Tier 0 card check — primary routing source)
- **Works with**: `AGENT_INDEX.md` (fallback for deep keyword matching)
- **Works with**: `directives/agent-loading-protocol.md` (tiered loading chain)
- **Works with**: `quality_gate.md` (runs after agent output)

---

*Created: 2026-02-17 | Updated: 2026-02-27 (Context Engine integration)*
