---
description: "Universal domain research — maps any topic into a tiered landscape with depth mining, audience resonance mapping, and strategic throughline. The creative bridge between 'I need to understand this domain' and 'I know exactly what to create.'"
---

# /research-landscape — Universal Domain Research

Takes a raw domain or topic and produces a **tiered research landscape**: 15-20 ranked topics in 3 tiers, each with timely context, depth-mined truth, audience resonance rating, and unique angle mapping. Includes industry data points, competitive whitespace analysis, strategic throughline, and 30+ cited sources.

**This is the FIRST STEP before creating anything.** It maps the terrain so everything downstream — content, marketing, strategy, expertise development — starts from understanding, not guessing.

## Usage

```
/research-landscape [domain/topic]
/research-landscape [domain] --ethos "[your relationship to this domain]"
/research-landscape [domain] --audience "[who you're creating for]"
/research-landscape [domain] --use-case [content|marketing|expertise|strategy]
```

**Examples:**
- `/research-landscape "AI automation agencies" --audience "solopreneurs" --use-case content`
- `/research-landscape "functional fitness for 40+" --ethos "15 years as a trainer" --use-case marketing`
- `/research-landscape "executive coaching market 2026" --use-case strategy`
- `/research-landscape "psychedelic-assisted therapy" --use-case expertise`

**Defaults:** `--use-case content`, audience and ethos inferred from `FARRICE.md` if not provided.

---

## Phase 0: Context Intake

Collect 4 inputs. Ask for anything missing; infer what you can from context.

| Input | Required? | Source |
|-------|-----------|--------|
| **Domain** | YES | User provides |
| **Audience** | YES (can infer) | User provides OR infer from domain context |
| **Ethos** | NO (enriches output) | User's relationship to domain — background, experience, credentials |
| **Use Case** | NO (default: content) | `content` / `marketing` / `expertise` / `strategy` |

**Rules:**
- If ethos not provided but `FARRICE.md` exists and is relevant to the domain, pull background from it
- If no ethos at all, "Your Unique Angle" sections will use domain-general framing ("A practitioner with deep [X] experience could...")
- Score intent sharpness 1-5 per `directives/intent-pipeline.md`. If ≤ 3, ask 1-2 clarifying questions.

**Output:**
```markdown
## Context Validated
- **Domain**: [domain]
- **Audience**: [who]
- **Ethos**: [user's relationship, or "not provided"]
- **Use Case**: [content/marketing/expertise/strategy]
- **Sharpness**: [score]/5
```

---

## Phase 1: Demand Scan (Perplexity-First)

**Reuses**: Perplexity-First Gate from `/research-topic`, budget tracking via `.agent/perplexity-usage.json`

### Steps

1. **Check Perplexity budget**: Read `.agent/perplexity-usage.json`
2. **Execute 3-5 targeted queries** (Perplexity if budget available, `search_web` / `WebSearch` fallback):

| Query Type | Purpose | Template |
|------------|---------|----------|
| **Trend Scan** | What's rising RIGHT NOW? | `"[domain] trends 2026 rising emerging"` |
| **Pain Mining** | What are people struggling with? | `"[domain] [audience] frustration challenges pain points 2026 reddit"` |
| **Industry Shifts** | What changed recently? Regulation, tech, market? | `"[domain] industry changes disruption 2026"` |
| **Competitive Content** | What's being said? What's saturated? | `"[domain] thought leadership content 2026"` |
| **Data Points** | Hard numbers — market size, growth, adoption | `"[domain] market size statistics data 2026"` |

3. **Log queries** to `.agent/perplexity-usage.json`
4. **Apply RARA rubric** (from `/research-topic`) to each source:
   - **R**elevance: >70% on-topic
   - **A**ccuracy: 2+ sources agree
   - **R**ecency: <1 year for fast-moving topics
   - **A**uthority: Official docs, industry leaders, .gov/.edu preferred

**Stopping criteria** (reuse from `/research-topic`):
- Saturation: 3+ sources repeating the same information
- Core query types all answered
- Budget limit reached

**Output**: Raw research data saved to `.tmp/research-landscape/raw-research.md`

---

## Phase 2: Topic Extraction

From raw research, extract **15-20 candidate topics**.

### Extraction Criteria

Each topic must pass ALL of these:

1. **Timely** — connected to something happening NOW (market shift, platform change, cultural moment, regulation, technology)
2. **Deep** — has a truth underneath the surface conversation (not just a trend, but a REASON behind it)
3. **Audience-relevant** — directly affects the defined audience's work, identity, or decisions
4. **Ownable** — if ethos provided, the user has a credible angle (if not, the topic must be ownable by a practitioner in this domain)

### Anti-Patterns (reject topics that are)

- Generic advice ("How to be better at X") — no tension, no depth
- Pure news reporting without a depth layer — informational, not insightful
- Topics with no audience tension — nobody's struggling with this
- Already-resolved topics — the conversation has moved past this

**Output**: Candidate topic list with 1-line descriptions + which extraction criteria they're strongest on.

---

## Phase 3: Depth Mining (The 10x Differentiator)

> This phase is what separates a `/research-landscape` from a Google search. The "truth underneath" is the user's COMPETITIVE ADVANTAGE — it's what lets them create content that feels like genuine understanding, not surface research.

For each candidate topic, mine TWO layers:

### Layer 1 — "Why Now"

What makes this topic urgent/timely? This is the surface layer — what any good researcher would find.

- Cite specific data, trends, or shifts
- Name the trigger event or market change
- Quantify where possible (market size, adoption rates, survey data)

### Layer 2 — "The Truth Underneath"

What's REALLY going on? The conceptual/psychological/philosophical truth that most people discussing this topic miss.

**Depth Mining Protocol — ask these 4 questions for each topic:**

1. **Symptom → Disease**: "If this topic is the SYMPTOM, what's the DISEASE? What's the root cause nobody's naming?"
2. **Expert Lens**: "What would a psychologist / philosopher / systems thinker / economist say about why this is happening? What's the structural or cognitive pattern?"
3. **Hidden Incentive**: "What's the defense mechanism, cognitive bias, or structural incentive creating this pattern? Why does the status quo persist?"
4. **Unspoken Truth**: "What would the audience never say out loud but secretly feel about this? What's the private version of the public conversation?"

**Quality test**: If the "truth underneath" reads like something you could find in the first page of Google results, it's not deep enough. Go deeper. The truth should make the reader feel genuinely UNDERSTOOD — like someone finally named what they've been experiencing.

---

## Phase 4: Audience Resonance & Unique Angle Mapping

### Resonance Rating

Rate each topic:

| Rating | Definition |
|--------|-----------|
| **HIGH** | Audience is actively struggling with this AND talking about it publicly |
| **MEDIUM-HIGH** | Audience feels this pain but hasn't fully articulated it yet — recognition content |
| **MEDIUM** | Relevant to audience but not top-of-mind; niche or emerging |

### Unique Angle Mapping

**If ethos was provided:**
- How does the user's specific background/expertise connect to this topic?
- What can they say about this that nobody else credibly can?
- What lived experience, professional hours, or domain knowledge gives them authority?
- Rate: YES (strong connection) / MODERATE / NO

**If no ethos:**
- Frame as: "A practitioner with deep [domain] experience could uniquely address this by..."
- Focus on what TYPE of expertise would make this topic ownable

---

## Phase 5: Synthesis & Tiering

### Tier Assignment

Rank topics using 5 weighted criteria:

| Criterion | Weight | Measure |
|-----------|--------|---------|
| Audience resonance | 30% | HIGH / MEDIUM-HIGH / MEDIUM |
| Depth of truth underneath | 25% | Does the depth layer create a genuine, non-obvious insight? |
| Timeliness | 20% | Connected to current events/shifts with specific data? |
| Unique angle strength | 15% | Can the user (or a domain expert) OWN this topic? |
| Competitive whitespace | 10% | Is this angle open or saturated? |

**Tier assignment:**
- **Tier 1 — High Resonance** (top 5-7): Strong on ALL criteria. These are the topics to create first.
- **Tier 2 — Strong Resonance** (next 5-6): Strong on MOST criteria. Solid second-wave topics.
- **Tier 3 — Targeted Resonance** (remaining): Niche but valuable for specific audience segments or contexts.

### Strategic Throughline

Identify the meta-narrative connecting Tier 1 topics. This is ONE SENTENCE that captures the overarching insight the landscape reveals.

**Example** (from coaching landscape): *"Your coaching expertise IS your content strategy. The same psychology you use in sessions is the psychology you need to understand to show up online."*

The throughline should:
- Unify the strongest topics under a single thesis
- Feel like a revelation, not a summary
- Be immediately usable as a positioning statement

### Red Team Pass

Before finalizing, run an adversarial check (reuse from `/research-topic`):

- **Confirmation bias**: Did we only search for data that supports a premise? Run at least one counter-narrative query.
- **Missing enemy**: What is the most significant threat, alternative, or criticism of the landscape's thesis? Include it.
- **Recency trap**: Are any "2026 trends" actually recycled 2024 narratives with new dates?

---

## Phase 6: Output Assembly

### Document Structure

```markdown
# [Domain] Research Landscape
**Research Date:** [date]
**Target Audience:** [audience description]
**Use Case:** [content/marketing/expertise/strategy]

---

## TIER 1 — HIGH RESONANCE (Topics 1-N)

---

### 1. [Punchy Topic Title — 5-12 words]

**Why it matters NOW:**
[2-3 sentences. Specific data, trends, or shifts. Cite sources.]

**The truth underneath:**
[2-4 sentences. The conceptual/psychological/philosophical depth layer. This is the insight most people miss.]

**Estimated audience resonance:** [HIGH / MEDIUM-HIGH / MEDIUM]

**Your unique angle:** [YES/MODERATE/NO — 1-2 sentences connecting user's ethos to this topic, or domain-general framing]

---

[Repeat for each Tier 1 topic]

## TIER 2 — STRONG RESONANCE (Topics N-M)

[Same structure per topic]

## TIER 3 — TARGETED RESONANCE (Topics M-P)

[Same structure per topic]

---

## RESEARCH CONTEXT: [Domain] Key Data Points

### [Category 1 — e.g., Market Dynamics]
- [Data point] — [source]
- [Data point] — [source]

### [Category 2 — e.g., Platform/Technology Shifts]
- [Data point] — [source]

### [Category 3 — e.g., Audience Behavior]
- [Data point] — [source]

---

## STRATEGIC RECOMMENDATION

**The throughline:** *[One sentence meta-narrative]*

**Strongest topic clusters:**
1. [Cluster name] (topics X, Y, Z) — [why this cluster matters]
2. [Cluster name] (topics A, B) — [why this cluster matters]

**Recommended next steps:**
- For content: [which topics to create first, in what order]
- For marketing: [which angles have the most commercial potential]
- For expertise: [where to deepen knowledge for maximum leverage]
- For strategy: [what the landscape reveals about positioning/opportunity]

---

## Sources

- [Source title](URL)
- [Source title](URL)
[...]
```

### Save Location

- If inside an active project: `_active/[project-slug]/research/[date]-[domain-slug]-landscape.md`
- If standalone: `strategy_briefs/[date]-[domain-slug]-landscape.md`

---

## Chain Compatibility

```
/research-landscape [domain]          ← YOU ARE HERE
        ↓
/voice-first-content prompts          — create prompt sets from Tier 1 topics
/mini-brief [topic]                   — forge any topic into a 7-element production brief
/research-topic [topic] --depth deep  — deep dive on any single topic
/research-sprint [question]           — business intelligence on strategy questions
/hunt-trends [niche]                  — shadow market detection within a topic
```

**`/research-landscape` is the FIRST STEP.** It maps the terrain. Everything else operates on specific topics FROM the landscape.

---

## Execution Notes

### Parallelism

For large domains, Phase 1 queries can run in parallel (multiple `WebSearch` calls). Phase 3 depth mining is sequential — each topic's depth layer benefits from patterns identified in previous topics.

### Token Efficiency

- Phase 1 raw research goes to `.tmp/` (not delivered to user)
- Phase 2 candidate list is internal working state
- Only Phase 6 assembled document is the deliverable
- If context is heavy, consider sub-agents for Phase 1 research (Research Scout, Social Listener roles from `/research-topic`)

### Quality Safeguards

- **No fabricated data**: Every statistic must have a cited source. If a data point can't be verified, mark it as "unverified" or omit it.
- **No recycled trends**: Check dates on sources. "2026 trends" articles published in 2024 are suspect.
- **Depth test**: If "the truth underneath" for any topic reads like a summary rather than an insight, revise it using the 4-question Depth Mining Protocol until it passes.
- **Universality check**: The workflow must work equally well for "executive coaching," "drone photography," "SaaS pricing," or "ancient philosophy." If any phase assumes a specific domain, it's not universal enough.
