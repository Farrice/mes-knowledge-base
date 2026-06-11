# /reflect → /recommend: Cross-Domain Intelligence Synthesis

## Reflection Source Intelligence

**Searched domains**: Intent Engineering, Decision Frameworks, Handoff Chains, Resistance Patterns, Awareness Stages, Compound Pipelines, Revenue Proximity, Anti-Hoarding, Pre-Mortem Simulation

**Cross-domain patterns discovered**: 8 high-leverage fusions from 12+ expert systems

---

## 🔬 Pattern Fusions Discovered

### Fusion 1: Intent Signal Field → Predictive Routing
**Source**: Nate B. Jones genius.md, Pattern 9 — "Anticipatory Intent Capture"
**Current Gap**: `/recommend` waits for the full query, then matches. It doesn't read the *gradient* of the user's expression.

**Enhancement**: Before running the 4-layer engine, apply the **Intent Signal Field**:
- **Emphasis Signals**: What the user repeats or gets energetic about = real priorities
- **Omission Signals**: What they skip = internalized expertise (flag it: "You didn't mention X — do you already have that covered?")
- **Contradiction Signals**: Where stated goal conflicts with actual context (e.g., "I need a sales page" but they have no offer designed yet)

**Deploy**: Generate a "Here's what I think you actually need" prediction *before* asking clarifying questions. Inverts the current Discovery Mode from "what do you want?" to "I think you need X — correct what's wrong."

---

### Fusion 2: Awareness Stage Classification → Workflow Ordering
**Sources**: Joanna Wiebe genius.md (Schwartz awareness stages), Growth Ecosystems genius.md (5-stage progression)
**Current Gap**: `/recommend` doesn't classify *where the user is* in their journey. A "Most Aware" user gets the same flow as a "Problem Unaware" user.

**Enhancement**: Add an **Awareness Classifier** as Step 1.5:

| Stage | Signal | Routing Behavior |
|-------|--------|-----------------|
| **Unaware** | "I'm bored" / "something feels off" | → Dr. K or Discovery Mode first |
| **Problem Aware** | "My content isn't working" | → Diagnostic workflows first (audits, analytics) |
| **Solution Aware** | "I need a sales page" | → Direct expert routing (current behavior) |
| **Product Aware** | "Should I use StoryBrand or Insight Vectors?" | → Comparison + compound recommendations |
| **Most Aware** | "Run /proof-copy-engine on my draft" | → Instant execution, skip recommendation |

**Key insight**: Most Aware users should bypass the recommendation engine entirely and go straight to execution. The engine should recognize when it's not needed.

---

### Fusion 3: Consequence Pre-Mortem → Deployment Risk Scoring
**Source**: Nate B. Jones genius.md, Signature Moves — "Consequence Pre-Mortem"
**Current Gap**: `/recommend` always says "deploy this" without assessing what could go wrong.

**Enhancement**: Add a **Risk Layer** to the recommendation output:

```
## ⚠️ Pre-Mortem Check
- **What could go wrong**: [e.g., "Running /proof-copy-engine before your offer is designed will produce beautiful copy for the wrong product"]
- **Prerequisite check**: [e.g., "Do you have a validated offer? If not, run /design-digital-product-offer FIRST"]
- **Reversibility**: [Two-way door: can redo cheaply | One-way door: high-stakes, needs more intent validation]
```

This prevents the #1 failure mode: executing the right skill in the wrong sequence.

---

### Fusion 4: Stack Order Intelligence → Execution Chain Sequencing
**Sources**: Luke Iha genius.md (HK8: "Stack Order Matters"), Kallaway genius.md ("The Articulation Stack"), Maria Wendt SKILL.md ("Recommended Workflow Chains")
**Current Gap**: The current "Execution Chain" in Step 7 is manually assembled each time. No embedded intelligence about which expert must come *before* another.

**Enhancement**: Embed a **Prerequisite Graph** into the recommendation engine:

```
# PREREQUISITE CHAINS (order matters)
PREREQUISITES = {
    "proof-copy-engine": ["design-digital-product-offer OR design-offer"],
    "vicious-hook": ["storybrand OR one-liner"],  # Need core message before hooks
    "atomize": ["any long-form content piece"],  # Can't atomize nothing
    "content-bundle": ["any finished content piece"],
    "campaign": ["brief OR storybrand"],  # Need strategy before campaign
    "launch-day": ["content-series-plan"],
    "full-stack-ad": ["mechanism-discover"],  # Need mechanism before ad
    "proof-pipeline": ["proof-ladder-builder"],
    "haunt": ["any draft content"],  # Can't haunt nothing
}
```

When the router recommends a workflow that has prerequisites, it *automatically prepends* the prerequisite step. "You asked for `/full-stack-ad`. That needs a mechanism first. Here's your chain: `/mechanism-discover` → `/mechanism-validate` → `/full-stack-ad`."

---

### Fusion 5: Emotional Processing Gate → Pre-Tactical Triage
**Sources**: David McRaney genius.md ("Emotional Processing Precedes Cognitive Change"), Dr. K genius.md (Decision Framework), Steven Pressfield genius.md ("The Resistance")
**Current Gap**: The current triage catches explicit emotional words ("stuck", "overwhelmed") but misses *implicit* emotional states disguised as tactical questions.

**Enhancement**: Add an **Emotional Subtext Detector** that fires on patterns like:
- "I've tried everything" → Frustration + exhaustion, not a feature request
- "Nothing is working" → Identity crisis, not a strategy gap
- "Should I even bother?" → Resistance, not a decision question
- "I keep starting over" → Samskara pattern (Dr. K), not a skill gap
- "Everyone else seems to get it" → Imposter pattern, not a content problem

**Rule**: If emotional subtext is detected, the recommendation becomes a **two-phase protocol**:
1. **Phase 1**: Emotional processing expert (Dr. K / Pressfield / McRaney)
2. **Phase 2**: *Then* the tactical expert they actually asked about

> "I notice you said 'I've tried everything.' Before we deploy the sales page expert, let's clear the emotional resistance first. Running Dr. K → then David Deutsch."

---

### Fusion 6: Compound Pipeline Architecture → Mission Blueprinting
**Source**: Monk.AI genius.md (Pattern 6: "Compound Pipeline Architecture"), Creative Assembly SKILL.md
**Current Gap**: Compounds are surfaced as pairings, but there's no *pipeline blueprint* that shows how they sequence and hand off.

**Enhancement**: When compounds are detected, produce a **Mission Blueprint** using the Creative Assembly handoff protocol:

```
MISSION BLUEPRINT: [Goal]
━━━━━━━━━━━━━━━━━━━━━━━

Phase 1: INTEL          @april-dunford → Positioning foundation
  Handoff: Category + competitive alternatives + differentiated value
  
Phase 2: MESSAGING      @donald-miller → BrandScript + one-liner
  Handoff: StoryBrand 7-part framework + tagline + lead generator concept
  
Phase 3: PRODUCTION     @david-deutsch → Sales page copy
  Handoff: Complete sales page draft with proof architecture
  
Phase 4: VALIDATION     @proof-audit-360 → Quality gate
  Handoff: Scored audit with revision prescriptions

Estimated workflow count: 4 | Swarm candidate: YES
```

---

### Fusion 7: Revenue Proximity Scoring → Urgency-Weighted Routing
**Sources**: Grace Andrews genius.md (HK-9: "Revenue Sequencing Gate"), Lara Acosta genius.md (P23: "Revenue Bridge Architecture")
**Current Gap**: Revenue proximity is listed as tie-breaker #4 in matching priority, but it's never *calculated*.

**Enhancement**: Add a **Revenue Distance Score** to each recommendation:

| Revenue Distance | Signal | Example |
|-----------------|--------|---------|
| **0 — Direct** | "I need sales copy / an ad / a pitch" | → Prioritize @david-deutsch, @stefan-georgi |
| **1 — One step away** | "I need a content strategy" | → Strategy → leads → revenue |
| **2 — Two steps** | "I need positioning" | → Positioning → messaging → content → leads → revenue |
| **3 — Foundation** | "I need to figure out my niche" | → Niche → positioning → messaging → ... |

**Display in output**: `Revenue Distance: 1 step (content strategy → lead capture → conversion)`

This gives the user instant clarity on how close they are to income generation. When multiple experts tie, the closer-to-revenue option wins.

---

### Fusion 8: Anti-Hoarding Intelligence → Capability Recall
**Current Gap**: Anti-hoarding check is listed as Step 8, but runs *after* the recommendation. It should fire *first*.

**Enhancement**: Move anti-hoarding to **Step 0** and make it aggressive:

Before running the 4-layer engine, scan for exact matches:
1. Check if the user's query maps to a workflow they've *already used* (via memory_store)
2. Check if a genius.md has already been loaded for this exact expert pairing
3. Check if a prior session produced a deliverable for this exact task type

**Output format**: 
```
🔄 CAPABILITY RECALL
You already have this:
- @david-deutsch + /proof-copy-engine (used 3x, last: April 10)
- Deliverable: Sales page for coaching offer (conversation abc123)
→ Want me to re-run with updates, or are you looking for something different?
```

---

## Proposed Changes

### [MODIFY] [recommend.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/recommend.md)

Complete rewrite incorporating all 8 fusions:

1. **Step 0**: Anti-Hoarding Recall (moved from Step 8 to first)
2. **Step 1**: Intent Signal Field (predictive intent before clarification)
3. **Step 1.5**: Awareness Stage Classification
4. **Step 2**: Emotional Subtext Detection (enhanced triage)
5. **Steps 3-6**: Current 4-layer engine (expert → workflow → compound → context) — unchanged
6. **Step 7**: Enhanced recommendation with:
   - Prerequisite chain (automatic prepending)
   - Revenue distance scoring
   - Consequence pre-mortem
   - Mission blueprint (when compounds detected)
7. **Step 8**: Immediate execution offer — unchanged
8. **Step 9**: Most-Aware bypass (skip engine if user knows exactly what they want)

### [MODIFY] [expert_router.py](file:///Users/farricecain/Google%20Antigravity/execution/expert_router.py)

Add new Python infrastructure:
- `PREREQUISITES` dictionary mapping workflows to their required precursors
- `classify_awareness(query)` function returning awareness stage
- `detect_emotional_subtext(query)` function returning emotional signals
- `score_revenue_distance(expert_name)` function returning 0-3 numeric

---

## Verification Plan

### Automated Tests
Run 5 diagnostic queries against the enhanced workflow:
1. **Most Aware**: "Run `/proof-copy-engine` on my draft" → Should bypass engine, go straight to execution
2. **Emotional Subtext**: "Nothing I write seems to work anymore" → Should trigger Dr. K *before* content expert
3. **Missing Prerequisite**: "I need a sales page" → Should detect missing offer/positioning, prepend prerequisite chain
4. **Revenue-Proximate**: "How do I get more clients?" → Should rank closest-to-revenue experts higher
5. **Anti-Hoarding**: Previously used expert → Should surface the prior usage first

### Manual Verification
Farrice runs `/recommend` in a live session with a real intent and confirms the output quality.
