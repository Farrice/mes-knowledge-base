# 🔬 Intent Refiner Directive (MANDATORY)

> **Purpose**: Automatically catch raw, unformed user intent and sharpen it into razor-sharp objectives that yield world-class results. This is the guardrail between vague thoughts and wasted tokens.
> **Effective**: 2026-02-10

---

## Why This Exists

The user (Farrice) naturally works in raw intent mode — half-formed ideas, unstructured thoughts, instinctive direction. This is a STRENGTH (speed, creativity, intuition) but it produces poor AI outputs when fed directly into execution. This directive bridges the gap automatically.

**The math**: A 2-minute refinement step produces 10x better output than a 30-second raw prompt. The system pays that cost so Farrice doesn't have to.

---

## When to Trigger (Detection Rules)

### ALWAYS Trigger When:
- User's request lacks a **specific audience** (who is this for?)
- User's request lacks a **concrete deliverable** (what exactly do they want?)
- User's request uses vague language: "something about...", "I'm thinking...", "help me with...", "I want to do..."
- User's request could be interpreted 3+ different ways
- User explicitly says their thought isn't fully formed

### NEVER Trigger When:
- Request is a clear, specific instruction with all parameters
- User says "just do it", "go ahead", "execute", or similar
- It's a follow-up refinement to an already-sharp objective
- It's a simple factual question
- It's a bug fix, correction, or file edit with clear scope

---

## The DICE Protocol (4-Question Sharpener)

When raw intent is detected, run these four questions. **Do NOT ask all 4 if some are already clear from context.** Only ask what's missing.

### D — Deliverable
> "What's the concrete thing you want in your hands when this is done?"

Patterns to listen for:
- Copy (hooks, emails, sales pages, posts)
- Strategy (plan, playbook, roadmap)
- Research (analysis, competitive intel, market sizing)
- System (workflow, automation, tool)
- Content (video scripts, LinkedIn posts, campaigns)

### I — Intended Audience
> "Who specifically will consume, read, or be affected by this?"

Push for specificity:
- ❌ "Business owners" → ✅ "Solo consultants making $150K-$300K who are skeptical of AI"
- ❌ "My audience" → ✅ "LinkedIn followers who are coaches considering AI tools"

### C — Context
> "What's the situation? Any constraints, deadlines, or things I should know?"

Surface invisible guardrails:
- Budget constraints
- Tone/brand requirements
- Prior work this builds on
- What's already been tried

### E — End State
> "What does 'nailed it' look like? What would make you say 'this is exactly what I needed'?"

This is the most important question. It reveals:
- Quality bar (quick draft vs. polished deliverable)
- Success criteria (engagement? conversions? clarity?)
- Hidden expectations the user hasn't articulated

---

## Intent Sharpness Score

After gathering DICE inputs (or assessing the original request), score the intent:

| Score | Label | Action |
|-------|-------|--------|
| **1** | Raw thought | MUST refine. Ask all missing DICE questions. |
| **2** | Directional | MUST refine. Ask 2-3 targeted DICE questions. |
| **3** | Formed | OFFER to refine. Present sharpened version + ask "Is this what you mean?" |
| **4** | Sharp | Proceed. Briefly confirm interpretation, then execute. |
| **5** | Razor | Execute immediately. No refinement needed. |

### Scoring Criteria Checklist
Award 1 point for each:
- [ ] Has a specific deliverable type
- [ ] Has a defined audience
- [ ] Has context or constraints stated
- [ ] Has a clear success criteria / end state
- [ ] Uses specific language (numbers, names, concrete nouns) vs. abstract language

---

## Agent Recommendation Engine

Once intent is sharpened (Score 3+), recommend the optimal agent team:

### Step 1: Domain Match
Use the domain detection table from `directives/expert_auto_routing.md` to identify primary domain.

### Step 2: Combo Selection
Present a recommendation in this format:

```
## 🎯 Recommended Agent Team

**Your sharpened objective**: [1-paragraph razor-sharp version of their intent]

**Agent team (3 experts)**:
| Agent | Role in This Task |
|-------|-------------------|
| **[Agent 1]** | [What they'll contribute] |
| **[Agent 2]** | [What they'll contribute] |
| **[Agent 3]** | [What they'll contribute] |

**Estimated cost**: ~$0.001 (3 agents × Gemini 3 Flash)
**Estimated time**: ~90 seconds

Ready to fire? Or want to adjust the team?
```

### Step 3: High-Leverage Combos Reference

| Goal | Best Combo | Why |
|------|-----------|-----|
| Killer sales copy | cardinal-mason + harry-dry + alen-sultanic | System + concrete + psychology |
| Viral content | seena-rez + shaan-puri + kallaway | Hooks + story + retention |
| LinkedIn authority | lara-acosta + nicolas-cole + dan-koe | Platform + sentences + philosophy |
| Product launch | samuel-thompson + daniel-priestley + jeremy-miner | Economics + demand + close |
| Brand positioning | erica-mallet + tom-noske + alex-copper | Belief + magnetism + visual |
| Strategic analysis | jim-oshaughnessy + rory-sutherland + manus-ai | Cross-domain + behavioral + research |
| Storytelling | shaan-puri + lucas-alpay + jonathan-franzen | Emotion + structure + depth |
| AI consulting sales | lindsay + monk-ai + sean-kochel | Outreach + offer + strategy |

---

## Output Format

After refinement, present this to the user:

```
## 🔬 Intent Refined

**What you said**: "[original raw input]"

**What I heard (Score: X/5)**:
[Brief interpretation]

**Sharpened objective**:
"[Razor-sharp, one-paragraph objective ready for execution]"

**Recommended approach**: [Swarm / Single expert / Direct execution]
**Agent team**: [If swarm recommended]

➡️ **Fire with this objective?** Or want to adjust?
```

---

## Integration Points

- **Works WITH** `directives/expert_auto_routing.md` — uses its domain detection
- **Works WITH** `directives/pre_flight_validation.md` — replaces it for swarm-bound tasks
- **Works WITH** `/validate-intent` workflow — the workflow triggers this directive
- **Powered BY** Nate B Jones Intent Engineering — disambiguation and guardrails methodology

---

## Anti-Patterns (What NOT to Do)

1. **Don't over-ask** — If 2 DICE questions are already answered by context, only ask the remaining 2
2. **Don't block flow** — If the user is in rapid-fire mode and intent is Score 3+, just confirm and go
3. **Don't be annoying** — One round of questions max. If user says "just go", go.
4. **Don't skip for swarms** — The swarm amplifies both quality AND mistakes. Always refine for swarms.

---

*Effective: 2026-02-10*
*Classification: Mandatory Orchestration Protocol*
*Methodology: Nate B Jones Intent Engineering + DICE Framework*
