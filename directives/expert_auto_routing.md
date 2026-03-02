# Expert Auto-Routing Protocol (MANDATORY)

> **Purpose**: Automatically invoke the right experts and skills for every request — without the user needing to remember slash commands or @mentions.
> **Effective**: 2026-02-05 | **Updated**: 2026-02-27 (Context Engine integration)
> **Router**: See `directives/router_agent.md` for fast-path dispatch and escalation ladder
> **Agent Registry**: See `AGENT_INDEX.md` for keyword-based agent matching
> **Loading Protocol**: See `directives/agent-loading-protocol.md` for the tiered loading chain

---

## The Problem This Solves

The user has invested heavily in building world-class expert skills and agents. But the value is lost when:
- They forget to invoke the right expert
- They're in "flow state" and don't want to context-switch to remember commands
- The conversation moves naturally between domains

**Solution**: I must automatically detect domains and invoke relevant expertise on EVERY request.

---

## Domain Detection Checklist (Run on EVERY Request)

Before responding to ANY user request, I must run this mental checklist:

### Step 1: What TYPE of request is this?

| Request Type | Signals | Action |
| :--- | :--- | :--- |
| **Research/Intelligence** | "analyze", "research", "find out", "what's the market" | Auto-invoke Manus.AI + relevant domain expert |
| **Content Creation** | "write", "create", "draft", "content" | Auto-invoke appropriate content expert(s) |
| **Strategy/Decision** | "should I", "what's the best", "how do I approach" | Auto-invoke Jim O'Shaughnessy + domain experts |
| **Copywriting** | "sales page", "email", "headline", "convert" | Auto-invoke Cardinal Mason + Harry Dry |
| **Personal Brand** | "LinkedIn", "positioning", "brand", "authority" | Auto-invoke Lara Acosta + Tom Noske |
| **Ghostwriting** | "ghostwrite", "write as", "voice capture", "coach content", "proof run", "demo rewrite" | Auto-invoke Ghostwriting Voice Engine (`/ghostwrite`) |
| **Product/Offer** | "product", "offer", "pricing", "launch" | Auto-invoke Samuel Thompson + Monk.AI |
| **Sales/Persuasion** | "objection", "close", "persuade", "sell" | Auto-invoke Jeremy Miner + Alen Sultanic |
| **Storytelling** | "story", "narrative", "hook", "engage" | Auto-invoke Shaan Puri + Lucas Alpay |
| **Video/TikTok** | "video", "TikTok", "viral", "hook" | Auto-invoke Seena Rez + Kallaway |
| **AI/Automation** | "automate", "workflow", "agent", "AI" | Auto-invoke Nick Saraev + Boris |
| **SEO/Search** | "rank", "SEO", "keywords", "traffic" | Auto-invoke Nathan Gotch + Adam Enfroy |
| **Design/Visual** | "design", "visual", "aesthetic", "creative" | Auto-invoke Oren + Kittl |
| **Launch/Innovation** | "launch", "validate", "early adopter", "monitor" | Auto-invoke Seena Rez + Samuel Thompson |

### Step 2: Is this multi-domain?

If the request spans multiple domains (e.g., "research the market and then write copy"), invoke an **Expert Ensemble**:

1. **Tier 0 (Card Check):** Read `agents/_framework/invocation-cards.md` to identify the 2-3 most relevant experts (~50 tokens each)
2. **Tier 1-2 (Load as needed):** Read SKILL.md + prompt (Tier 1) or + genius-patterns (Tier 2) per task complexity
3. **Tier 3 (Sub-Agent):** For 3+ experts or 10+ files already loaded, spawn sub-agents with fresh context

See `directives/agent-loading-protocol.md` for full tiered chain and decision matrix.

### Step 3: Is this a strategic/high-stakes decision?

If YES, also invoke:
- **Jim O'Shaughnessy** for cross-domain synthesis
- **Manus.AI** for competitive intelligence depth
- **Mark Kashef** council methodology if conflicting perspectives needed

---

## Expert Ensemble Patterns

### For Innovation/Launch
1. Seena Rez (early adopter signal)
2. Samuel Thompson (shadow markets)
3. Oren (identity aesthetics)

### For Market Research + Content
1. Manus.AI (research depth)
2. Kallaway (content psychology)
3. Nathan Gotch (SEO/retrieval)

### For Product Launch
1. Samuel Thompson (shadow markets, economics)
2. Monk.AI (offer architecture)
3. Cardinal Mason (conversion copy)

### For Personal Brand Building
1. Lara Acosta (LinkedIn mastery)
2. Tom Noske (magnetic personal brand)
3. Dan Koe (multipassionate positioning)

### For Strategic Decisions
1. Jim O'Shaughnessy (philosopher-financier)
2. Manus.AI (competitive intelligence)
3. Domain-specific expert(s)

### For High-Converting Copy
1. Harry Dry (Three Rules Test)
2. Cardinal Mason (conversion systems)
3. Alen Sultanic (buyer psychology)

### For Coach Ghostwriting
1. Ghostwriting Voice Engine (`/ghostwrite` — full pipeline)
2. Lara Acosta (voice extraction + LinkedIn mastery)
3. Nicolas Cole (sentence refinement + voice preservation)

### For Viral Content
1. Seena Rez (TikTok commerce)
2. Kallaway (dopamine ladder)
3. Shaan Puri (storytelling)

---

## McKinsey-Grade Execution Standard

All intelligence/research outputs must follow this format:

### Minimum 8 Sections for Strategic Briefs
1. **Executive Summary** — Verdict + 5 key insights with data
2. **Market Sizing** — TAM/SAM/SOM with numbers and sources
3. **Buyer/Customer Profile** — Psychographics, pain points, verbatims
4. **Competitive Intelligence** — SERP/market landscape + exploitable gaps
5. **Options/Paths** — Decision tree or program matrix
6. **Economic Model** — ROI projections, break-even analysis
7. **Risk Matrix** — Probability/Impact/Mitigation
8. **Execution Playbook** — Day-by-day or week-by-week actions

### Every Insight Must Have
- **A data point** (number, statistic, quote)
- **A source** (URL or publication)
- **An action** (what to DO about it)

### No "Glob of Words" Allowed
If an output reads like a report without clear actions, it has FAILED. Every paragraph must either:
- State a fact with a source, OR
- Give a specific instruction

---

## How to Load Expert Files (Tiered Chain — ENFORCED)

**Always start at Tier 0. Escalate only when the task demands it.**

| Tier | What to Read | Token Cost | When |
|------|-------------|-----------|------|
| **0 — Card Check** | `agents/_framework/invocation-cards.md` | ~80 | Routing, recommendations, ensemble selection |
| **1 — Standard** | SKILL.md + specific prompt | ~1,350 | Single expert, clear task |
| **2 — Deep** | SKILL.md + genius-patterns + prompt | ~2,550 | Creative/complex work |
| **3 — Sub-Agent** | Spawn sub-agent (reads in fresh context) | ~300 main | Multi-expert, 10+ files loaded |

**Full protocol:** `directives/agent-loading-protocol.md`
**Skill file paths:** `directives/skill-paths-reference.md`

After loading and applying, **cite the expert** in the output:
- "Applying Cardinal Mason's conversion architecture..."
- "Using Manus.AI's McKinsey-grade research protocol..."

---

## When to Auto-Route vs. Ask

### Auto-Route (Don't Ask)
- Domain is clear from the request
- Task type is unambiguous
- Time-sensitivity is high

### Ask First (Present Options)
- User's intent is ambiguous
- Multiple conflicting approaches possible
- Stakes are very high and direction matters

---

## Expert Recommendation Block (Show Before Executing)

For complex or multi-step requests, I will present a recommendation block before executing:

### Format

```
## 🎯 Expert Ensemble Recommendation

**Domain Detected**: [Research/Content/Strategy/etc.]

**Recommended Experts**:
| Expert | Why They're Right for This |
| :--- | :--- |
| **[Expert 1]** | [1-line reason] |
| **[Expert 2]** | [1-line reason] |
| **[Expert 3]** (optional) | [1-line reason] |

**Alternative Experts** (if you prefer a different angle):
- [Expert A] — [angle they'd bring]
- [Expert B] — [angle they'd bring]

**Execution Approach**: [Brief description of how I'll tackle this]

➡️ **Proceed with these experts?** Or would you like to add/swap anyone?
```

### When to Show This Block

**Always Show For**:
- Research/intelligence tasks
- Strategy/decision tasks
- Multi-step builds (products, campaigns, systems)
- Any request where 3+ experts could apply

**Skip For** (Just Execute):
- Simple questions with clear single-expert domain
- Follow-up requests in an established flow
- Corrections or refinements to prior work
- User explicitly says "just do it" or similar

### Example

```
## 🎯 Expert Ensemble Recommendation

**Domain Detected**: Market Research + Content Strategy

**Recommended Experts**:
| Expert | Why They're Right for This |
| :--- | :--- |
| **Manus.AI** | Deep competitive intelligence, McKinsey-grade research |
| **Kallaway** | Content psychology, dopamine ladder for engagement |
| **Nathan Gotch** | SEO/retrieval layer optimization for discoverability |

**Alternative Experts** (if you prefer a different angle):
- Samuel Thompson — If you want product economics focus
- Harry Dry — If copy quality is the priority

**Execution Approach**: Run 6-query research protocol → Synthesize into 8-section dossier → Include week-by-week playbook

➡️ **Proceed with these experts?**
```

---

## Integration with Other Directives

This directive works WITH:
- `directives/quality_assurance.md` — Agentic Research mandate
- `directives/pre_flight_validation.md` — Variation presentation
- The Expert-First Work Protocol in GEMINI.md

---

## Failure Mode

If I receive a request and:
- Do NOT run domain detection
- Do NOT invoke relevant experts
- Produce generic output without expert frameworks

...then I have FAILED this directive.

---

## Usage Tracking

> **Purpose**: Detect dead infrastructure. If this directive hasn't fired in 30 days, it should be reviewed for relevance or archived.

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-03-19 |

**Update Rule**: When this protocol fires (domain detection + expert invocation), update the "Last Activated" date and increment the count. If the 30-day review date passes with 0 activations, flag for archival review.

---

*Effective: 2026-02-05*
*Classification: Mandatory Orchestration Protocol*
