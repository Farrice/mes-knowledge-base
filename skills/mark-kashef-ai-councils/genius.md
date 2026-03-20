# Mark Kashef AI Councils — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns

## Pattern 1: Subagent Council Architecture
**Execute**: Use Claude Code subagents as perspective agents with opposing mandates. Each agent has distinct behavioral requirements.

**Success Metric**: Getting genuinely divergent viewpoints on any decision.

---

## Pattern 2: Behavioral Mandates Over Personality
**Execute**: Define what agent MUST DO, not personality traits. "Must assume failure has occurred" vs "be pessimistic."

**Success Metric**: Agents produce distinctive outputs regardless of context.

---

## Pattern 3: Shared Reasoning File
**Execute**: Create file-based memory capturing HOW agents think, not just conclusions. Document reasoning evolution.

**Success Metric**: Reasoning persists across sessions and informs future decisions.

---

## Pattern 4: Anti-Sycophancy Architecture
**Execute**: Make disagreement structurally guaranteed. Optimist agent CANNOT agree with pessimist's concerns—mandates conflict.

**Success Metric**: Zero unanimous agreement on complex decisions.

---

## Pattern 5: Context Window Preservation
**Execute**: Use subagents for distinct reasoning threads. Prevents context degradation in long conversations.

**Success Metric**: Quality maintained across extended sessions.

---

## Pattern 6: Single-Phrase Invocation
**Execute**: Design invocation protocol where one phrase summons correct council. "Strategy decision" → Business Council.

**Success Metric**: Zero friction to activate appropriate expertise.

---

## Pattern 7: Steelman Requirements
**Execute**: Before disagreeing, agent must articulate strongest version of opposing position. No strawmanning allowed.

**Success Metric**: Debates produce actual crux isolation, not surface disagreement.

---

## Pattern 8: Domain-Specific Council Configuration
**Execute**: Different decisions need different expert combinations. Hiring Council ≠ Marketing Council.

**Success Metric**: Council composition matches decision domain.

## Hidden Knowledge

## Tacit 1: Sycophancy is Architectural
You cannot prompt your way out of AI sycophancy. "Be honest with me" doesn't work. Opposition must be structurally required through conflicting mandates.

**Deploy**: Build systems where agents CAN'T agree even if they wanted to.

---

## Tacit 2: Mandates Create Consistent Behavior
Personality descriptions produce inconsistent agents. Behavioral mandates ("must always X before Y") produce reliable, distinctive outputs.

**Deploy**: Replace personality words with behavioral requirements.

---

## Tacit 3: Shared Memory Enables Learning
Without shared reasoning files, each council session starts fresh. With them, wisdom accumulates across decisions.

**Deploy**: Always capture reasoning, not just conclusions.

---

## Tacit 4: Subagents Preserve Context Quality
Claude Code subagents run in separate contexts. Main conversation stays focused while subagents do heavy reasoning.

**Deploy**: Offload intensive reasoning to subagents to prevent degradation.

---

## Tacit 5: Opposition Reveals Blind Spots
The value isn't in the "right" perspective—it's in the tension between perspectives that surfaces assumptions you didn't know you had.

**Deploy**: Design councils for maximum productive tension.

---

## Tacit 6: Invocation Friction Kills Usage
If summoning a council requires complex setup, you won't use it. Single-phrase activation eliminates friction.

**Deploy**: Make council activation effortless.

---

## Tacit 7: Calibration Through Tracking
Which agent was right? Track predictions over time to calibrate agent reliability and fine-tune mandates.

**Deploy**: Build prediction tracking into council operations.

---

## Tacit 8: Unanimous Agreement is a Red Flag
If all agents agree, either the decision is trivial or your council design has failed.

**Deploy**: Treat consensus as signal to probe deeper.

---

## Hall of Fame Exemplars

### Exemplar 1: The "Go/No-Go" Strategic Decision Council
**Scenario**: A client needs to decide whether to launch a new product feature with significant investment.
**Council Configuration**: A 4-agent council is invoked:
1.  **Market Analyst**: Mandated to identify maximum market opportunity and growth potential.
2.  **Risk Assessor**: Mandated to identify all potential failure points, competitive threats, and resource drain.
3.  **Financial Modeler**: Mandated to project best-case and worst-case ROI, burn rate, and break-even points.
4.  **Devil's Advocate**: Mandated to steelman the arguments of all other agents and then present a counter-argument to each.
**Output**: A comprehensive "Go/No-Go" brief. The Market Analyst presents an optimistic outlook, the Risk Assessor highlights critical vulnerabilities, and the Financial Modeler provides a range of financial outcomes. Critically, the Devil's Advocate dissects each argument, forcing the other agents to refine their positions and surface hidden assumptions. The final recommendation is a nuanced "Go, with these 3 critical mitigations and a phased rollout plan," rather than a simple yes/no.
**What makes this excellent**: Demonstrates Pattern 4 (Anti-Sycophancy Architecture) and Pattern 7 (Steelman Requirements) by generating genuine, structured disagreement that leads to a more robust, de-risked decision. Tacit 5 (Opposition Reveals Blind Spots) is perfectly illustrated.

### Exemplar 2: The "Full-Stack Marketing Campaign" Assembly Line
**Scenario**: A startup needs a complete marketing campaign (email sequence, social posts, ad copy, landing page outline) for a new SaaS product.
**Council Configuration**: A sequential 3-agent team, with a human tollbooth:
1.  **Market Researcher**: Mandated to identify target audience pain points, competitor messaging, and key selling propositions. Output: Research brief.
2.  **Content Strategist**: Mandated to take the research brief and outline the core messaging themes, call-to-actions, and content pillars for each channel. Output: Campaign outline.
3.  **Copywriter & Designer**: Mandated to generate specific email copy, social posts, ad variants, and a landing page wireframe based on the outline. Output: Full campaign assets.
**Human Tollbooth**: After the Content Strategist completes the campaign outline, the system pauses and requests user approval before proceeding to the Copywriter & Designer, preventing costly re-generation.
**Output**: A fully developed, integrated marketing campaign with consistent messaging across all channels, generated from a single prompt, with a mid-process human review.
**What makes this excellent**: Exemplifies the "Directed Assembly Line" pattern from the extraction report, showing clear sequential handoffs and dependencies. Pattern 3 (Shared Reasoning File) ensures the Copywriter has full context. The "Human Tollbooth" pattern prevents wasted tokens and effort, aligning with Tacit 4 (Subagents Preserve Context Quality).

### Anti-Exemplar: The "Agreeable Brainstorm"
**Scenario**: A user asks a general-purpose AI to "brainstorm ideas for a new product with 3 different perspectives: an innovator, a marketer, and a finance expert."
**Output**: The AI generates three distinct paragraphs, each from the requested perspective. All three perspectives largely agree on the product's viability and offer complementary, rather than conflicting, ideas. There's no structured debate, no challenge to assumptions, and no synthesis of divergent views. The "finance expert" might suggest budgeting, the "marketer" might suggest branding, and the "innovator" might suggest features—all in harmony.
**What makes this mediocre**: This fails to leverage Tacit 1 (Sycophancy is Architectural) and Pattern 4 (Anti-Sycophancy Architecture). The agents are described by personality traits ("innovator") rather than behavioral mandates ("must identify market saturation points and potential for disruption"), leading to generic, non-confrontational output. The lack of structured interaction or a synthesis phase means no deeper insights are generated beyond what a single, well-prompted LLM could achieve.

## Signature Moves

*   **Mandate-First Configuration**: Always starts by defining explicit, behavioral mandates for each agent ("must identify failure modes," "must assume success") rather than vague personality traits. → **Deploy when**: Architecting any new agent council or defining a new agent role.
*   **Conflict Architect**: Designs council structures where agent mandates inherently conflict or require steelmanning of opposing views, guaranteeing productive disagreement. → **Deploy when**: Tackling complex decisions where consensus is a red flag (Tacit 8) or when seeking to expose hidden assumptions.
*   **Reasoning Trace Linker**: Establishes a shared reasoning file for councils, ensuring that the evolution of thought, intermediate findings, and disagreements are all documented and persist. → **Deploy when**: Any multi-session council, or when post-mortem analysis of decision-making is critical.
*   **Precision Invocation**: Ensures that the activation of any specialized council is via a single, unambiguous phrase, eliminating cognitive load and friction for the user. → **Deploy when**: Integrating councils into a broader workflow or making them accessible to non-technical users.
*   **Hybrid Grunt-to-Architect Pipeline**: Automatically deploys cheaper, focused sub-agents for initial data gathering (e.g., summarizing a codebase) before feeding that distilled context to more expensive, reasoning-heavy agent teams. → **Deploy when**: Processing large volumes of raw data or complex documentation as a prerequisite for a higher-level task.

## Expert-Specific Quality Rubric

| Criterion                     | Score 4 (Acceptable)                                                                 | Score 7 (Good)                                                                      | Score 10 (Savant)                                                                                                                                              |
| :---------------------------- | :----------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Disagreement Fidelity**     | Agents present distinct but often complementary views; mild disagreement.              | Agents present genuinely divergent views, with some structural conflict.             | Agents' mandates are architected for inherent conflict, forcing steelmanning and surfacing deep-seated assumptions; zero sycophancy.                           |
| **Agent Mandate Specificity** | Agent roles are defined with personality traits (e.g., "be creative").                 | Agent roles include some behavioral instructions, but still allow for broad interpretation. | Agent roles are defined exclusively by explicit, measurable behavioral mandates (e.g., "must identify three novel risks," "must refute the strongest point"). |
| **Reasoning Traceability**    | Final conclusions are presented; intermediate reasoning is implicit or lost.           | Some intermediate reasoning is captured, but not consistently linked across agents. | A comprehensive, shared reasoning file captures the full evolution of thought, disagreements, and data points for every agent.                                  |
| **Crux Identification**       | Disagreements are superficial; agents don't fully engage with opposing arguments.      | Agents acknowledge opposing arguments but may not fully articulate their strongest form. | Every disagreement is preceded by a steelmanned articulation of the opposing position, leading to clear identification of the core crux.                      |
| **Council-Task Alignment**    | A general-purpose council is used for a specialized task.                             | A relevant council is chosen, but its specific configuration might be generic.      | The council's composition (number and type of agents) is precisely tailored to the domain and specific decision at hand (Pattern 8).                          |
| **Context Purity**            | Main agent context window is cluttered with sub-agent deliberations.                 | Sub-agent deliberations are somewhat separated, but still impact main context.      | Intensive reasoning is offloaded to Claude Code subagents, maintaining a pristine and focused context for the main conversation.                               |
| **Consensus Challenge**       | Unanimous agreement is accepted as a sign of success.                               | Unanimous agreement is noted but not always probed.                                 | Unanimous agreement is treated as a critical red flag, triggering a deeper structural review or re-prompt to ensure genuine tension (Tacit 8).                 |
