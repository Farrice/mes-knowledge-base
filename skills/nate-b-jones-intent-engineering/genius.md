# Nate B Jones Intent Engineering — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## How to Use This Skill (Model Calibration)

These patterns are intuition primitives, not a checklist. Absorb them, then reason from them — don't stamp "Pattern 3, Pattern 8" onto a deliverable in order. The test: would Nate recognize this as the actual intent gap he diagnoses on his channel — the moment a fluent-sounding output quietly becomes a real-world commitment — or does it just borrow his vocabulary ("intent," "reversibility," "guardrails") without doing the diagnostic work underneath? If it's the second, rebuild.

Specifically:
- Do NOT narrate the machinery ("Now applying the Reversibility Gradient..."). Surface the Intent Document, the reversibility score, the assumption list — as the artifact itself, never as a labeled step.
- Nate's texture is analyst-practical, not academic: he traces a failure back to a single sentence a human would have caught, then generalizes it into a reusable rule. Mirror that — one concrete failure, then the rule it implies — never a rule stated in the abstract with no failure behind it.
- Polish is the tell-class warning here specifically: an Intent Document that reads as comprehensive but never names what could go wrong, or a Six-Line Spec with generic Non-Goals ("don't do anything harmful"), is answer-shaped output pretending to be intent-engineered output — the exact failure mode this skill exists to catch. Every Non-Goal, guardrail, or failure condition must be specific enough to be violated in an observable way.
- When a source anchor is genuinely unconfirmed (see `references/source-ledger.md`), say so in the deliverable rather than smoothing over the gap — that honesty is itself Pattern 8 (Assumption Surfacing) applied to your own output.

## Genius Patterns

## Pattern 1: Inflection Point Recognition
**Execute**: Identify the precise moment where stakes fundamentally change. "Once you give the model tools, the fluent completion becomes a real-world commitment."

**Success Metric**: Zero surprise consequences from agent actions.

---

## Pattern 2: Latent vs Explicit Distinction
**Execute**: Separate what's IN the text (context) from what's BEHIND the text (intent). Articulate priorities, tradeoffs, what done looks like. Nate's own worked instance of this distinction: a TurboQuant "save memory" request is explicit about compression but latent about *zero information loss* — the "lossless" qualifier is the whole thesis (GP-2, `extractions/nate-b-jones/turbokvant-context-engineering-extraction.md`). Treat every request the same way: find the qualifier the requester assumed was obvious.

**Success Metric**: Agent can articulate understood priorities before acting.

---

## Pattern 3: Invisible Guardrails Insight
**Execute**: Enumerate constraints humans assume but never state. "We hear 'clean up the docs' and infer 'don't destroy anything important.'"

**Success Metric**: Agent respects constraints that were never explicitly stated.

---

## Pattern 4: Clarification Loop Architecture
**Execute**: Build disambiguation as a design feature. Trigger: (1) high uncertainty, (2) serious consequences, (3) multiple plausible interpretations.

**Success Metric**: Agent asks questions at appropriate moments—not too many, not too few.

---

## Pattern 5: Intent Commit Pattern
**Execute**: Create standalone Intent Documents with goals, failure conditions, tradeoffs. Version separately from prompts. Nate's system-level analog of this pattern: the Karpathy Loop's `program.md`, a living document the meta-agent reads and revises independently of the task agent's execution code (`extractions/nate-b-jones/karpathy-loop-mes-extraction.md`) — proof that a versioned intent artifact survives outside the thing it governs, at production scale, not just in a single prompt.

**Success Metric**: Intent can be updated without touching execution code.

---

## Pattern 6: Production Pragmatism
**Execute**: Build harnesses that compensate for weak intent inference—eval suites, constrained permissions, traced execution. Nate's clearest real-world instance: Cursor's Planner-Worker-Judge harness, which four labs converged on independently (GP-3, `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md`) — a harness compensating for imperfect intent inference at organizational scale, not a single clever prompt.

**Success Metric**: Agents ship and perform reliably despite imperfect understanding.

---

## Pattern 7: Interpretation-Execution Separation
**Execute**: Two-phase systems: (1) Interpretation outputs explicit understanding, (2) Execution only after validation.

**Success Metric**: Every tool call has inspectable interpretation that preceded it.

---

## Pattern 8: Assumption Surfacing
**Execute**: Include in agent instructions: "Before executing, state your assumptions. Where is confidence low? What would you ask?"

**Success Metric**: Model reveals assumptions that would otherwise cause failures.

## Pattern 9: Intent Signal Field (Anticipatory Intent Capture)
**Execute**: Before the user finishes articulating intent, read the GRADIENT of their expression across three signal types:
- **Emphasis Signals**: What they repeat, slow down on, or get energetic about — these are their real priorities, even if unlabeled.
- **Omission Signals**: What they skip or treat as obvious — often their deepest expertise, so internalized they forget it's valuable. Flag the gap: "You didn't mention X — is that because it's obvious to you, or because you don't address it?"
- **Contradiction Signals**: Where stated positioning conflicts with actual examples (e.g., "I help beginners" but every case study is advanced). These reveal true intent vs. marketed intent.

After signal analysis, generate a "Here's what I think you actually need" prediction BEFORE asking clarification questions. This inverts Pattern 4 — instead of "what did you mean?", present "I think you meant X, Y, Z — correct what's wrong." Faster, builds trust, surfaces assumptions the user didn't know they had. Each interaction updates the predictive model: track confirmed vs. corrected predictions to build increasingly accurate intent capture across sessions.

**Success Metric**: System anticipates user needs before full articulation; prediction accuracy improves with each interaction cycle.

---

## Hidden Knowledge

## Tacit 1: Answer-Shaped Text Problem
LLMs produce outputs that LOOK correct because they match the statistical pattern of correct answers. In chat, forgiving. In agent actions, catastrophic. The mirror-image real case: Karpathy's meta-agent found a genuine bug in his attention implementation ("a bug that Karpathy had missed") *because* it ran 700 experiments instead of stopping at the first answer-shaped-looking result (`extractions/nate-b-jones/karpathy-loop-mes-extraction.md`) — the inverse of the failure mode, achieved only by refusing to treat fluent-looking as validated.

**Deploy**: Treat every agent output as potentially "answer-shaped but wrong" until validated against intent criteria.

---

## Tacit 2: Human Second-Pass Simulation
Humans automatically simulate consequences and social context before inferring priorities. Models skip this unless forced. See Exemplar 1 below (the GDPR data-retention scenario) for a worked instance of forcing this simulation explicitly.

**Deploy**: Build explicit "consequence simulation" steps: What could go wrong? What would the user regret?

---

## Tacit 3: Social Cohesion Trap
Human language optimizes for relationship maintenance, not declarative specification. We're deliberately vague. Models take vagueness literally. See Exemplar 2 below (the "optimal meeting time" scenario) for a worked instance of a vague, polite request concealing three distinct possible priorities.

**Deploy**: Transform polite requests into explicit specifications before agent processing.

---

## Tacit 4: Reversibility Gradient
Actions exist on spectrum from fully reversible to completely irreversible. Different points require different confidence levels. Operationalized in this skill as a 1–5 Reversibility Score (1 = fully reversible, 5 = permanent/external impact) — see the Reversibility Matrix in `workflows/operational-safety-and-communication-design.md` § Output Contract for the applied table format.

**Deploy**: Map every tool to reversibility score. Require higher intent confidence for lower reversibility.

---

## Hall of Fame Exemplars

### Exemplar 1: The "Delete Old Data" Safegaurd
**Scenario**: A user asks an agent, "Please delete all customer data older than 5 years to comply with GDPR."
**Nate B Jones Intent Engineering Application**:
The agent, following Intent Engineering principles, first generates an "Intent Document" (Pattern 5). This document doesn't just list the command; it explicitly surfaces potential hidden constraints and consequences:
1.  **Goal**: GDPR compliance.
2.  **Explicit Instruction**: Delete customer data > 5 years old.
3.  **Latent Priorities/Tradeoffs**:
    *   *Priority 1*: Avoid deleting *any* legally required archival data (e.g., financial transaction records, audit logs that might reference customer data).
    *   *Priority 2*: Ensure data integrity across related systems (e.g., if a customer record is deleted, are associated support tickets orphaned or handled appropriately?).
    *   *Tradeoff*: Speed of deletion vs. absolute data safety.
4.  **Failure Conditions**: Accidental deletion of critical data, data corruption, non-compliance with *other* regulations.
5.  **Proposed Action Plan**:
    *   Phase 1 (Interpretation): Identify all data stores potentially containing customer data. For each, generate a list of records matching "customer data > 5 years old". Cross-reference with known archival requirements.
    *   Phase 2 (Validation): Present the generated list and a detailed impact analysis to the user for explicit approval.
    *   Phase 3 (Execution): Only upon approval, proceed with deletion, with a rollback plan where possible (Tacit 4).
**What makes this excellent**: It demonstrates Pattern 2 (Latent vs Explicit Distinction), Pattern 3 (Invisible Guardrails), Pattern 5 (Intent Commit Pattern), Pattern 7 (Interpretation-Execution Separation), Tacit 2 (Human Second-Pass Simulation), and Tacit 4 (Reversibility Gradient) by transforming a simple instruction into a robust, consequence-aware plan, preventing catastrophic data loss.

### Exemplar 2: The "Optimized Meeting Schedule" Clarification
**Scenario**: A busy executive tells their scheduling agent, "Find the optimal time for my team's weekly sync next week."
**Nate B Jones Intent Engineering Application**:
Recognizing the vagueness and high stakes, the agent doesn't just pick the first available slot. It triggers a clarification loop (Pattern 4) by asking:
1.  "When you say 'optimal,' what are the key priorities? (Pattern 2)
    *   Is it minimizing conflicts for *everyone*?
    *   Is it ensuring *your* availability above all else?
    *   Is it avoiding specific days or times due to existing deep work blocks or external commitments? (Pattern 3 - Invisible Guardrails: recognizing 'optimal' implies more than just calendar availability)
2.  "What are the failure conditions for this meeting? (e.g., if key person X isn't there, it's a wasted meeting; if it runs over 60 mins, it's too long)." (Pattern 2 - Articulate what "done" looks like)
3.  "Are there any specific team members whose attendance is absolutely critical, even if it means rescheduling others?"
The agent then presents a few options, each annotated with the tradeoffs based on the executive's clarified intent (e.g., "Option A: 90% attendance, but you'll have to shift a low-priority task. Option B: 100% attendance, but it's an hour later than ideal for half the team.").
**What makes this excellent**: It showcases Pattern 2 (Latent vs Explicit Distinction) and Pattern 4 (Clarification Loop Architecture) by proactively seeking the *true* intent behind a vague request, preventing a statistically "correct" but practically "wrong" outcome (Tacit 1 - Answer-Shaped Text Problem).

### Anti-Exemplar: The "Clean Up My Inbox" Disaster
**Scenario**: A user instructs an email agent, "Archive all emails older than 6 months and delete anything from marketing lists."
**Mediocre Outcome**: The agent proceeds to archive *all* emails older than 6 months, including critical legal documents, financial receipts, and project communications that were explicitly kept for record-keeping. It also deletes marketing emails, but in doing so, unsubscribes the user from essential industry newsletters that they manually filter and read. The user's inbox is "clean" but vital information is lost, and preferred subscriptions are gone, leading to significant frustration and manual recovery efforts.
**Why it's an anti-exemplar**: The agent failed to apply Pattern 3 (Invisible Guardrails) by not inferring that "old emails" don't include critical records, and "marketing lists" don't include preferred newsletters. It also failed to implement Pattern 4 (Clarification Loop Architecture) or Pattern 8 (Assumption Surfacing) to ask about these implicit constraints, demonstrating a lack of Tacit 2 (Human Second-Pass Simulation) and a literal interpretation of vague instructions (Tacit 3).

## Anti-Patterns

Sourced, list-form failure modes — what Intent Engineering explicitly forbids. Each item carries the date it was recorded in this system and the file it can be traced to; items without a locatable primary transcript are labeled UNCONFIRMED rather than given a false anchor (full claim-by-claim accounting in `references/source-ledger.md`).

- **The "Clean Up My Inbox" Disaster** (recorded 2026-01-27, `genius.md` Anti-Exemplar, UNCONFIRMED primary source): agent archives *all* emails >6 months including legal/financial records, and unsubscribes the user from newsletters they manually curated — literal interpretation of "old" and "marketing," zero Invisible Guardrail check (Pattern 3), zero Clarification Loop (Pattern 4).
- **Literal invisible-guardrail failure** (recorded 2026-01-27, `genius.md` Pattern 3, UNCONFIRMED primary source) — quote: *"We hear 'clean up the docs' and infer 'don't destroy anything important.'"* An agent that skips this inference destroys files a human would never have touched.
- **Answer-shaped execution** (recorded 2026-01-27, `genius.md` Tacit 1, UNCONFIRMED primary source): treating a fluent, plausible-looking agent output as validated without checking it against intent criteria — "answer-shaped but wrong," forgivable in chat, catastrophic once tools fire.
- **Bias-to-ship silent compounding** (dated 2026-07-01 in-file citation, "Inside ChatGPT-5's Brain: System Prompt Secrets for First Movers," Aug 2025 — LIKELY, raw export file not located; see source-ledger) — quote: wrong assumptions embedded in a prompt to a bias-to-ship model "compound into nicely-looking disasters instead of helpful clarifications," because the model gets at most one clarifying question before executing.
- **Score-only logging with no traces** (VERIFIED — `extractions/nate-b-jones/karpathy-loop-mes-extraction.md` § Anti-Patterns, item 4, dated 2026-04-20): "no traces = no interpretability = random mutations." Directly violates Pattern 7 (Interpretation-Execution Separation) — an agent whose reasoning was never captured can't be audited for intent-alignment after the fact.
- **No human inspection gate on promotion** (VERIFIED — `extractions/nate-b-jones/karpathy-loop-mes-extraction.md` § Anti-Patterns, item 6, dated 2026-04-20): shipping a change without a mandatory human checkpoint before it goes live. Directly violates Tacit 4 (Reversibility Gradient) — promotion to production is a low-reversibility action that requires the highest confidence threshold, not the lowest.

## Signature Moves

*   **Intent Document First**: Immediately translates any task into a structured "Intent Document" outlining explicit goals, latent priorities, failure conditions, and a clear definition of "done," before any action is considered. → **Deploy when**: Any agent task involves real-world commitment or non-trivial consequences.
*   **Reversibility Mapping**: Before proposing any action, maps the action's reversibility (from fully reversible to irreversible) and automatically escalates required confidence and human approval for less reversible actions. → **Deploy when**: An agent's proposed action involves manipulating external systems or data.
*   **Assumptions-First Disclosure**: Forces the agent to explicitly state all assumptions it's making, identify areas of low confidence, and articulate potential questions *before* generating a plan or executing. → **Deploy when**: Task context is ambiguous, or the agent is about to make a significant decision.
*   **Interpretation-Execution Decoupling**: Designs any agent workflow as a two-phase system: first, an "Interpretation" phase that outputs a detailed understanding and proposed plan, followed by a distinct "Execution" phase that only proceeds after explicit validation (often human). → **Deploy when**: Building any multi-step agent workflow or tool-using agent.
*   **Consequence Pre-Mortem**: Before committing to a course of action, conducts a simulated "pre-mortem" asking: "What could go wrong? What would the user regret? What are the edge cases that could lead to failure?" → **Deploy when**: Assessing the robustness of an agent's proposed action or plan.

## Expert-Specific Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
| :-------- | :------------------- | :------------- | :---------------- |
| **Intent Explicitness** | Goals are stated, but underlying priorities or tradeoffs are implicit. | Goals, primary priorities, and some basic tradeoffs are articulated. | The full "Intent Document" is generated, clearly articulating goals, *all* latent priorities, comprehensive tradeoffs, and precise failure conditions. |
| **Consequence Simulation Depth** | Basic "what if" scenarios are considered, mostly focused on direct failure. | Potential direct and some indirect negative consequences are identified, with basic mitigation. | A thorough "human second-pass simulation" is evident, identifying direct, indirect, and social/reputational consequences, with proactive mitigation strategies. |
| **Invisible Guardrail Adherence** | Only explicit constraints are respected; implicit human assumptions are often missed. | Most common implicit human constraints (e.g., "don't destroy important things") are inferred and respected. | The agent proactively identifies and respects a wide array of unstated human assumptions, social norms, and domain-specific "invisible guardrails." |
| **Interpretation-Execution Decoupling** | Interpretation and execution are blended, or the interpretation is vague. | A clear interpretation phase precedes execution, but validation points may be generic. | Interpretation is fully separated from execution, producing a detailed, human-inspectable plan with explicit validation gates before *any* irreversible action. |
| **Assumption Surfacing** | Assumptions are rarely stated, or only when explicitly prompted. | Some key assumptions are revealed, often in response to uncertainty. | The agent reflexively surfaces all critical assumptions, identifies areas of low confidence, and proactively poses disambiguating questions as a design feature. |
| **Reversibility-Confidence Alignment** | All actions require a similar level of confidence, regardless of reversibility. | Higher confidence is generally required for irreversible actions, but the mapping is informal. | Every tool call or action is mapped to its reversibility gradient, and the required confidence level and human approval threshold are dynamically adjusted accordingly. |
| **Clarification Loop Effectiveness** | Clarification loops are triggered rarely or ask generic questions. | Clarification loops are triggered appropriately, but questions might not fully uncover latent intent. | Clarification loops are highly targeted, asking precise questions that rapidly disambiguate latent intent, priorities, and unstated constraints. |

---

### Patterns from claude.ai export — Nate B. Jones conversations (2026-07-01)

*Source: "Inside ChatGPT-5's Brain: System Prompt Secrets for First Movers" (Aug 2025). These patterns cover the USER side of the intent gap — how to delegate to bias-to-ship agentic models that will NOT run the clarification loop for you.*

## Pattern 10: The Bias-to-Ship Inversion
Agentic models are configured to proceed, not ask — GPT-5's system prompt allows at most one clarifying question before execution mode. This inverts the clarification responsibility: with conversational models, the back-and-forth caught wrong assumptions; with bias-to-ship models, wrong assumptions embedded in the prompt "compound into nicely-looking disasters instead of helpful clarifications."
**Execute**: Before delegating to any agentic model, assume zero clarification rounds. Audit your prompt for embedded assumptions the model will silently execute. Anything you would normally settle in turn 2-3 must be stated in turn 1.
**Success Metric**: Tasks that previously took five back-and-forths complete in one, without answer-shaped-but-wrong deliverables.

## Pattern 11: Spec-First Delegation (Conversations → Specifications)
The unit of interaction shifts from conversation to specification. "You have to be higher grade in your intent. You have to write specs, not just conversations." Iterative refinement still works on conversational models; agentic models reward nailing the first shot with clear deliverables, assumptions, and constraints — and an imperfect spec still beats a loose prompt.
**Execute**: Rewrite your highest-volume AI workflow as a spec: front-load assumptions, set tool policies, define acceptance criteria. Build a personal prompt library of reusable specs — agentic models reward it.
**Success Metric**: First-pass output is decision-ready without a refinement round; spec reuse rate climbs across the workflow.

## Pattern 12: The Six-Line Delegation Spec
Nate's master template for agentic delegation, one labeled line each:
1. **Task** — define it as clearly as you can
2. **Deliverable** — format, length, audience (even if the audience is just you)
3. **Assumptions** — bind the model to your context/scope/timeline assumptions at the top
4. **Non-Goals** — what must NOT be done (the speculative-execution killer)
5. **Tools** — explicitly allowed and explicitly forbidden
6. **Acceptance** — the success criteria that define "done"
**Execute**: Use all six lines for any delegation with a Reversibility Score > 2 (see Tacit 4). The Non-Goals line is the direct fix for speculative execution (comprehensive output when you wanted a quick check); the Tools line is the direct fix for tool-usage surprises (unrequested web searches, unwanted code execution — "don't build this in code, just think strategically").
**Success Metric**: Zero overcompletion events; zero unrequested tool invocations on delegations that matter.

## Tacit 5: System-Prompt Archaeology
**Insight**: A leaked system prompt is the clearest behavioral map of a model you will ever get — clearer than any public statement from the vendor. It tells you the model's default posture (ship vs. ask), its non-negotiable prompt elements, its buried failure modes (e.g., GPT-5's system prompt explicitly kills commentary after image generation — so generate, then analyze, in separate turns), and the vendor's product roadmap ("they've articulated and built an agent that ships first and asks questions later").
**Deploy**: When a new frontier model launches, read its system prompt (they reliably leak within days) before writing your prompting guidance for it. Derive per-model prompting posture from the prompt itself, not from habits carried over from the previous model. Treat every clause that constrains the model as a clause you may need to compensate for in your own specs.
