---
description: Contextual skill recommendation
---

# /recommend — System Intelligence Advisor

Analyze what Farrice is working on — or thinking about — and **recommend** the best approach, experts, workflows, and execution paths from the entire Antigravity system. His universal "what should I do?" command.

> **CRITICAL**: This is an **advisor**, not an executor. Present a strategic recommendation and **wait for Farrice to choose**. Do NOT load experts, run workflows, or generate content until he explicitly says to proceed.

Works for task requests, raw context dumps, planning questions, and system navigation.

## Usage

```
/recommend [what you're working on or trying to accomplish]
/recommend --discovery  (interactive narrowing)
```

---

## Steps

### 0. Bypass Check

**Only bypass** if the query contains a literal `/command` or `@expert` reference (e.g., "Run /proof-copy-engine", "Load @david-deutsch"). Natural language like "I want to write better copy" is NOT a bypass — it needs the full recommendation. If in doubt, don't bypass.

If bypassed, confirm: "You're calling for `/[workflow]`. Want me to go ahead, or see alternatives first?"

---

### 1. Anti-Hoarding Recall

Check if Farrice already has deployed assets for this:

// turbo
```bash
python3 execution/memory_store.py search "[user's query]" 2>/dev/null || echo "No memory hits"
```

If a match exists, surface it: "You already have @[expert] + /[workflow] — want to re-run it, or looking for something different?" If re-running, skip remaining steps.

---

### 2. Intelligence Diagnostic

// turbo
```bash
python3 execution/expert_router.py diagnose "[user's query]"
```

This produces **awareness stage**, **emotional subtext**, and **revenue proximity** simultaneously. Apply these rules:

**Awareness routing:**
- **Unaware** → Jump to Step 3 (Discovery Mode)
- **Problem Aware** → Prioritize diagnostic/audit workflows
- **Solution Aware** → Standard routing (Step 4)
- **Product Aware** → Comparison mode — show side-by-side capabilities
- **Most Aware** → Should have been caught in Step 0

**Emotional subtext detected?** Present a two-phase protocol:
```
⚠️ EMOTIONAL GATE: I notice [patterns]. Recommended sequence:
Phase 1: @[pre_expert] → /[pre_workflow] (process first)
Phase 2: THEN your tactical request → [recommendation]
Want Phase 1 first, or override to tactical?
```
Never suppress the gate. User can override, but always flag it.

---

### 3. Discovery Mode

**Trigger**: `--discovery` flag, vague query (Awareness = unaware), or zero router matches.

Use the **Intent Signal Field** to predict rather than interrogate:
```
🔍 DISCOVERY MODE
Prediction: [predicted deliverable] — Why: [signal evidence]
Is this close? One correction round to sharpen.
```

If truly blank, offer quick 3-question diagnostic: (1) What to produce? (2) Where in process? (3) Emotional temperature? Then re-run Steps 4-6 with sharpened query.

---

### 4. Four-Layer Search

Run all four in parallel:

// turbo
```bash
python3 execution/expert_router.py route "[user's query]" -n 5
```

// turbo
```bash
python3 execution/workflow_router.py search "[user's query]"
```

// turbo
```bash
python3 execution/expert_router.py compounds "[user's query]"
```

// turbo
```bash
python3 execution/context_retriever.py search "[user's query]"
```

Capture: top 3-5 experts, top 3-5 workflows, any compound pairings, and relevant knowledge chunks.

---

### 5. Prerequisite & Revenue Check

For the top recommendations:

// turbo
```bash
python3 execution/expert_router.py prereqs "[top workflow]"
```

// turbo
```bash
python3 execution/expert_router.py revenue "[top expert]"
```

If prerequisites exist, prepend them to the execution chain. Never recommend a workflow without its precursors.

---

### 6. Produce Recommendation

Synthesize all layers into a single brief:

```
🎯 RECOMMENDATION

## What You're Doing
[Restate the real intent]

## Awareness: [Stage] | Revenue Distance: [0-3]

## Primary Expert
@[expert] → [specific skill/prompt] — Why: [rationale]
Produces: [expected deliverable]

## Workflows
1. /[primary] — [what it does] ⭐
2. /[enhancer] — [what it adds]
3. /[quality-gate] — [what it catches]

## Execution Chain
[If prereqs: list prerequisite → primary → enhance → validate]
[If no prereqs: start → enhance → validate → deploy]

## Pre-Mortem
- Risk: [what could go wrong]
- Reversibility: [two-way door / one-way door]

## Deep Knowledge
📚 [Relevant chunk from genius file or methodology]

## Support Experts
@[expert-2] → [value-add] | @[expert-3] → [value-add]
```

**When compounds detected**, add a Mission Blueprint:
```
⚡ MISSION BLUEPRINT: [Goal]
Phase 1: @[expert-1] → [deliverable] → handoff to Phase 2
Phase 2: @[expert-2] → [deliverable] → handoff to Phase 3
Phase N: @[quality-gate] → validation
Swarm candidate: [YES/NO]
```

---

### 7. Present & Wait

End with a clear menu. **Never execute without explicit direction.**

```
What would you like to do?
  A. Execute the primary recommendation
  B. See alternative approaches
  C. Adjust the scope or intent
  D. Just needed the map — I'll take it from here
  [S. Deploy as swarm | M. Run as multi-step mission]
```

---

## Matching Priority

1. **Revenue proximity** — closer to revenue wins
2. **Prerequisite completeness** — already-met beats new-work-required
3. **Specificity** — exact-fit beats general
4. **Practitioner mode** — produces deliverable beats advises on it
5. **Compound potential** — multiplier pairings create more value
6. **Recency** — recently evolved skills may have deeper coverage

## Error Handling

| Scenario | Action |
|---|---|
| Zero matches | Offer Discovery Mode |
| Expert but no workflow | Load SKILL.md, recommend manually |
| Tangential matches | One clarifying question, re-route |
| "That's not what I meant" | Switch to Discovery Mode |
| Emotional override | Flag, continue, note override |
| Missing prereq + user insists | Execute with pre-mortem warning |
| Memory store unavailable | Skip recall, proceed with routing |
