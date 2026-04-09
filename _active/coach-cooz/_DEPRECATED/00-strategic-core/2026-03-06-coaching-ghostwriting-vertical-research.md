# Research Design: Coaching Ghostwriting Vertical Deep Dive

**Date:** March 6, 2026
**Objective:** Determine whether ghostwriting for coaches is the right vertical, identify perfect market fit, and build a Consumer Posture Profile for immediate client acquisition.
**Method:** 7-agent parallel swarm with Perplexity grounding
**Builds on:** `strategy_briefs/2026-03-04-ai-ghostwriting-landscape.md` (macro market validation)

---

## Gap Analysis

The existing landscape brief answers **"Is ghostwriting viable?"** (yes — $4.2B market, bifurcating, premium opportunity). This research answers the **launch questions**:

1. Which coaching sub-segment is the ideal target? (life, business, health, executive, career)
2. What is the Consumer Posture of the ideal coaching client? (identity-level, not demographic)
3. Why do coaches say no even when they know they need help?
4. Who's already serving this niche and where are the gaps?
5. How do you position as the only choice with zero proof?
6. How do you engineer demand and land the first 5 clients?

---

## Agent Assignments (7 Agents, Parallel Execution)

### 1. Dai Media — Consumer Posture Profile
- Find ONE specific coaching archetype (not a demographic segment)
- Build full 3D Consumer Posture: Occupation, Activity, Thought Process
- Apply the Kristen Stewart Test ("would a real person recognize themselves?")
- Map buying triggers, identity threats, and psychological barriers
- **Output:** Complete Consumer Posture Profile document

### 2. Samuel Thompson — Market Economics & Sub-Segment Analysis
- Break coaching into sub-verticals: life, business, health, executive, career, relationship
- Spending power per segment, content needs, LinkedIn activity levels
- TAM/SAM/SOM for ghostwriting in each sub-segment
- Unit economics: pricing sweet spot, client lifetime, churn patterns
- **Output:** Sub-segment comparison matrix with recommended target

### 3. April Dunford — Positioning Analysis
- Apply "Obviously Awesome" framework to coaching ghostwriting
- Competitive alternatives map (DIY, AI tools, agencies, VAs, do nothing)
- Unique value proposition that only Farrice can deliver
- Category design: what category should this service CREATE?
- **Output:** Positioning canvas with competitive context

### 4. Jeremy Miner — Sales Psychology & Objection Mapping
- Map the buying journey for a coach considering ghostwriting
- Identify real objections vs. stated objections (NEPQ methodology)
- Design questions that surface the real pain
- Closing framework for the sales conversation
- **Output:** Objection map + sales conversation blueprint

### 5. Lara Acosta — LinkedIn Coaching Ecosystem
- Who's already ghostwriting for coaches on LinkedIn?
- Content patterns that work for coaching content specifically
- Gaps in the market — what's underserved?
- LinkedIn-specific opportunities for coaching ghostwriting
- **Output:** Competitive landscape + content opportunity map

### 6. Rory Sutherland — Behavioral Economics of Coach Buying
- Why coaches resist buying content services (reactance, loss aversion, identity threat)
- Psychological reframes that make the purchase feel safe
- Pricing psychology: how to frame $3-5K/month as obvious value
- Trust-building mechanics for zero-proof situations
- **Output:** Behavioral strategy for coach conversion

### 7. Daniel Priestley — Demand Engineering
- "Oversubscribed" methodology applied to ghostwriting launch
- How to create demand with 0 testimonials and 0 portfolio
- Waitlist strategy, diagnostic-first approach
- First 5 clients playbook
- **Output:** Launch sequence with demand engineering tactics

---

## Synthesis Deliverables

1. **Unified Synthesis Report** — Agreements, conflicts, and resolution across all 7 agents
2. **Consumer Posture Profile** — The ONE coach archetype, fully mapped at identity level
3. **Sub-Segment Recommendation** — Which coaching vertical wins the head-to-head
4. **Go-to-Market Blueprint** — Positioning + sales + demand engineering combined
5. **Competitive Gap Analysis** — Where to attack the market

---

## Execution Command

```bash
python execution/parallel_swarm.py --research \
  --agents "dai-media,samuel-thompson,april-dunford,jeremy-miner,lara-acosta,rory-sutherland,daniel-priestley" \
  "Deep research: Coaching ghostwriting vertical analysis. For each agent's domain, analyze:
   1. Which coaching sub-segment (life, business, health, executive, career) is the best target for premium LinkedIn ghostwriting services?
   2. What is the psychology, identity, and buying behavior of coaches who would pay $3,000-5,000/month for ghostwriting?
   3. What competitive alternatives exist and where are the gaps?
   4. How should a solo operator with AI-augmented voice-first methodology position, price, and launch this service with zero existing proof?
   Context: The operator has 18 years psychology/coaching experience, 95 expert AI agents, a voice-first content pipeline, and is building AI-integrated ghostwriting systems. Target platform is LinkedIn."
```

---

## Post-Swarm Actions

1. Review `swarm_outputs/latest/synthesis.md`
2. Extract Consumer Posture Profile → `strategy_briefs/2026-03-06-coaching-consumer-posture-profile.md`
3. Extract Go-to-Market Blueprint → `strategy_briefs/2026-03-06-coaching-ghostwriting-gtm.md`
4. Update existing landscape brief with coaching-specific findings
