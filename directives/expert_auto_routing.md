# Expert Auto-Routing Protocol (MANDATORY)

> **Purpose**: Automatically invoke the right experts and skills for every request — without the user needing to remember slash commands or @mentions.
> **Effective**: 2026-02-05

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

1. Identify the 2-3 most relevant experts
2. Read their SKILL.md files (or AGENT.md for agents)
3. Read their `genius-patterns.md`
4. Apply their combined frameworks

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

## How to Read Expert Files

When auto-invoking an expert:

1. **Read SKILL.md** (or AGENT.md)
   - Path: `skills/[skill-name]/SKILL.md` or `agents/[agent-name]/AGENT.md`
   
2. **Read genius-patterns.md**
   - Path: `skills/[skill-name]/references/genius-patterns.md`
   
3. **Read relevant prompt** (if applicable)
   - Path: `skills/[skill-name]/references/prompts/[prompt-name].md`

4. **Apply their framework** to the user's request

5. **Cite the expert** in the output when relevant
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

*Effective: 2026-02-05*
*Classification: Mandatory Orchestration Protocol*
