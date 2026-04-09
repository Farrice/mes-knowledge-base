# Nate B. Jones (Intent Engineering) — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

The critical gap in agentic AI is not capability but intent inference. Separate what's IN the text (context) from what's BEHIND the text (intent). Human language optimizes for relationship maintenance, not declarative specification — we're deliberately vague and models take vagueness literally. Build systems that surface assumptions, simulate consequences, and separate interpretation from execution before any irreversible action.

---

## Genius Patterns (Compressed)

### GP1: Inflection Point Recognition
Identify the precise moment where stakes fundamentally change. "Once you give the model tools, the fluent completion becomes a real-world commitment." Zero surprise consequences from agent actions is the standard.

### GP2: Latent vs Explicit Distinction
Separate what's IN the text (context) from what's BEHIND the text (intent). Articulate priorities, tradeoffs, and what "done" looks like. The agent must be able to articulate understood priorities before acting.

### GP3: Invisible Guardrails Insight
Enumerate constraints humans assume but never state. "We hear 'clean up the docs' and infer 'don't destroy anything important.'" Design agents that respect constraints never explicitly stated.

### GP4: Clarification Loop Architecture
Build disambiguation as a design feature, not an afterthought. Trigger clarification on: (1) high uncertainty, (2) serious consequences, (3) multiple plausible interpretations. Agent asks questions at appropriate moments — not too many, not too few.

### GP5: Intent Commit Pattern
Create standalone Intent Documents with goals, failure conditions, and tradeoffs. Version separately from prompts. Intent can be updated without touching execution code.

### GP6: Production Pragmatism
Build harnesses that compensate for weak intent inference — eval suites, constrained permissions, traced execution. Agents ship and perform reliably despite imperfect understanding.

### GP7: Interpretation-Execution Separation
Two-phase systems: (1) Interpretation outputs explicit understanding, (2) Execution only after validation. Every tool call must have an inspectable interpretation that preceded it.

### GP8: Assumption Surfacing
Include in agent instructions: "Before executing, state your assumptions. Where is confidence low? What would you ask?" Forces the model to reveal assumptions that would otherwise cause failures.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | Answer-Shaped Text Problem — LLMs produce outputs that LOOK correct because they match the statistical pattern of correct answers; in chat forgiving, in agent actions catastrophic | Treat every agent output as potentially "answer-shaped but wrong" until validated against intent criteria |
| HK2 | Human Second-Pass Simulation — humans automatically simulate consequences and social context before inferring priorities; models skip this unless forced | Build explicit "consequence simulation" steps: What could go wrong? What would the user regret? |
| HK3 | Social Cohesion Trap — human language optimizes for relationship maintenance, not declarative specification; we're deliberately vague and models take it literally | Transform polite requests into explicit specifications before agent processing |
| HK4 | Reversibility Gradient — actions exist on a spectrum from fully reversible to completely irreversible; different points require different confidence levels | Map every tool to a reversibility score; require higher intent confidence for lower reversibility |

---

## Signature Moves

1. **Intent Document First** — Immediately translates any task into a structured document: explicit goals, latent priorities, failure conditions, definition of "done." Deploy when any agent task involves real-world commitment.
2. **Reversibility Mapping** — Maps every proposed action's reversibility and automatically escalates required confidence and human approval for less reversible actions. Deploy when agent actions involve manipulating external systems or data.
3. **Assumptions-First Disclosure** — Forces the agent to state all assumptions, identify low-confidence areas, and articulate questions BEFORE generating a plan. Deploy when task context is ambiguous.
4. **Interpretation-Execution Decoupling** — Two-phase workflow: Interpretation phase outputs detailed understanding and proposed plan; Execution phase only proceeds after explicit validation. Deploy when building any multi-step agent workflow.
5. **Consequence Pre-Mortem** — Simulated pre-mortem asking: "What could go wrong? What would the user regret? What edge cases could lead to failure?" Deploy when assessing robustness of any proposed action.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Intent Explicitness | Goals stated but underlying priorities or tradeoffs implicit | Goals, primary priorities, and basic tradeoffs articulated | Full Intent Document with all latent priorities, comprehensive tradeoffs, and precise failure conditions |
| Consequence Simulation | Basic "what if" scenarios focused on direct failure | Direct and some indirect consequences identified with basic mitigation | Thorough human second-pass simulation covering direct, indirect, and social/reputational consequences with proactive mitigation |
| Invisible Guardrail Adherence | Only explicit constraints respected | Most common implicit human constraints inferred and respected | Proactively identifies and respects a wide array of unstated human assumptions, social norms, and domain-specific guardrails |
| Interpretation-Execution Decoupling | Interpretation and execution blended or interpretation vague | Clear interpretation phase precedes execution with some validation | Fully separated with detailed, human-inspectable plan and explicit validation gates before any irreversible action |
| Assumption Surfacing | Assumptions rarely stated or only when prompted | Some key assumptions revealed in response to uncertainty | Reflexively surfaces all critical assumptions, identifies low-confidence areas, and proactively poses disambiguating questions |
| Reversibility-Confidence Alignment | All actions require similar confidence regardless of reversibility | Higher confidence generally required for irreversible actions informally | Every action mapped to reversibility gradient with dynamically adjusted confidence thresholds and approval requirements |
