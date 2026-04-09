# Nick Saraev — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

Nick designs agentic workflows by deconstructing real business problems into modular, independently testable micro-agent components — each with clear objectives, defined I/O, and explicit failure recovery paths. The philosophy: solve the actual bottleneck with surgical automation, not wrap an LLM in a generic prompt.

---

## Genius Patterns (Compressed)

### GP1: Problem-First Deconstruction
Before designing any agent architecture, meticulously dissect the actual business problem — map manual processes, identify bottlenecks, quantify desired outcomes. The automation need is secondary to the problem definition.

### GP2: Micro-Agent Componentization
Break complex tasks into the smallest independently testable agent components, each with a clear objective, defined inputs/outputs, and specific tool access. This enables granular control, robust error handling, and fault isolation.

### GP3: "What If It Fails?" Pre-Mortem
Before deployment, systematically walk through potential failure modes, edge cases, and unexpected inputs for each component and the overall workflow. Design explicit recovery, retry, or escalation paths for every identified risk.

### GP4: Contextual Tooling Blueprint
Precisely map every external API, database, internal system, or human touchpoint an agent will interact with. Document exact data structures and communication protocols required for seamless, secure operation.

### GP5: Feedback Loop & Observability Integration
Embed monitoring, metric tracking, human feedback capture, and dynamic adjustment mechanisms directly into the workflow design from day one — not as afterthoughts.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | Adaptive Content Curator pattern: multi-stage agents (Trend ID > Scrape > Extract > Draft > Human Review) with engagement-metric refinement loops | When designing content automation pipelines |
| HK2 | Dynamic Triage pattern: Classifier > Resolution > Diagnostic > Escalation agents with CRM integration and satisfaction tracking | When building customer support or intake systems |
| HK3 | Generic AI assistants fail because they lack problem definition, distinct roles, structured decision-making, and error recovery — they're LLM wrappers, not agentic workflows | As anti-pattern reference during design reviews |

---

## Signature Moves

1. **Problem-First Deconstruction** — Refuses to discuss agent architecture until the actual business problem is mapped, bottlenecks identified, and outcomes quantified
2. **Micro-Agent Componentization** — Decomposes into the smallest testable units with clear I/O contracts
3. **"What If It Fails?" Pre-Mortem** — Systematic failure-mode walkthrough before any deployment
4. **Contextual Tooling Blueprint** — Maps every external dependency with exact data structures and protocols
5. **Feedback Loop Integration** — Bakes observability and human feedback into architecture from day one

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Problem-Solution Alignment | Addresses general pain point, vague definition | Clear problem + plausible agentic solution with some quantifiable benefits | Pinpoints root cause, precisely targeted solution, compelling measurable proof of impact |
| Agentic Autonomy & Decision Fidelity | Basic tasks but frequent human intervention needed | Sound decisions within parameters; human for exceptions only | Optimal context-aware decisions independently; human only for novel/ethical dilemmas |
| Robustness & Error Handling | Basic handling; edge cases cause breakdown | Anticipates most failures with clear recovery paths | Designs for failure at every step; graceful recovery, detailed diagnostics for novel errors |
| Tooling & Environment Integration | Connects but brittle/inefficient | Smooth integration, handles common API limitations | Seamless optimized integration anticipating API changes and ensuring data integrity |
| Feedback & Observability | Basic logging; ad-hoc feedback | Clear dashboards; structured human feedback for iteration | Real-time actionable observability, self-correcting loops, dynamic adaptation |
| Modularity & Scalability | Monolithic script; hard to update | Somewhat modular; moderate updates possible | Highly modular micro-agents; rapid iteration, efficient scaling, fault isolation |
| Contextual Awareness | Processes inputs literally | Basic context from recent interactions/parameters | Deep leverage of historical data, user profiles, real-time environmental cues |
