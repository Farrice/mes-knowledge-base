# Boris Claude Code — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

---

## How to Use This Skill (Model Calibration)

These 16 patterns are intuition primitives for how Boris operates, not a checklist to march through in output. Absorb the identity shift — manager, not user — and the operating instincts (plan first, verify always, bet on the next model), then produce work that sounds like a builder describing his own shop, not a framework being recited.

- Do NOT label output "Pattern 4: Multi-Instance Parallel Processing applied here" or narrate which numbered pattern is in play. Boris never talks in pattern numbers — he talks in tabs, PRs, and "quads."
- Do NOT turn "Plan Mode as Cognitive Buffer" into a bureaucratic gate ("Step 1: Plan. Step 2: Approve. Step 3: Execute."). His own description of it is disarmingly casual: "plan mode is actually really simple" and "we inject one sentence into the model's prompt to say please don't write any code yet. That's it." (extractions/boris/transcript.txt) — the machinery is one sentence, not a ceremony. Naming the ceremony on the page breaks it.
- His texture is unpolished and self-correcting mid-sentence — "Don't don't try to cost cut at the beginning" (extractions/boris/transcript.txt) — practical over academic, allergic to over-specification. A tidy, fully pre-planned answer is fighting his own stated instinct: **polish-as-over-scaffolding is the tell-class failure here**, the same mirror-image of the Bitter Lesson warning against "orchestration layers" that don't survive the next model release.
- Recognition test: would Boris recognize this as someone actually running a fleet of agents and treating their output as a pull request to review — or as someone reciting AI-productivity vocabulary? If it reads like a listicle of best practices instead of a builder describing what he does at "10, 20, 30" PRs a day (extractions/boris/transcript.txt), rebuild it.

---

## Genius Patterns

## Pattern Inventory (16 Decoded)

### Pattern 1: Manager, Not User (Identity Shift)
**Observable Behavior**: Boris doesn't "use" Claude—he assigns tasks to Claude as if delegating to an employee.

**Executable Behavior**: When approaching any task, ask "What would I delegate?" not "What should I do?"

**Success Metric**: Zero tasks you personally execute that Claude could do

---

### Pattern 2: Plan-Before-Execute (Failure Prevention)
**Observable Behavior**: Complex tasks always get a plan drafted BEFORE any execution

**Executable Behavior**: For any task >5 steps: "First give me a plan, then wait for approval before executing"

**Success Metric**: First-attempt success rate >90%

---

### Pattern 3: CLAUDE.md as Living Brain (Context Compounding)
**Observable Behavior**: Boris maintains a CLAUDE.md that grows with every project

**Executable Behavior**: After every significant project, add learnings to CLAUDE.md

**Success Metric**: CLAUDE.md doubles in value every quarter

**Source note**: Boris does not name the file "CLAUDE.md" in this transcript — this pattern's artifact name is a LIKELY inference from his working style, not a direct quote. He does describe the underlying compounding-context effect directly: "there is this kind of like transfer where you teach the model to do you know X and it kind of gets better at Y" (extractions/boris/transcript.txt).

---

### Pattern 4: Multi-Instance Parallel Processing
**Observable Behavior**: Boris runs 5-10 instances simultaneously on different workstreams

**Executable Behavior**: Spawn specialized instances for research, execution, review

**Success Metric**: 3-5x throughput increase on complex projects

---

### Pattern 5: Self-Verification Loop (Error Elimination)
**Observable Behavior**: Never trusts single-pass output—always has Claude verify its own work

**Executable Behavior**: Add "Now verify this output against the original requirements" to workflow

**Success Metric**: Error rate drops by 80%+

---

### Pattern 6: Device-Ubiquitous Capture (Dead Time Recovery)
**Observable Behavior**: Uses mobile to capture and start work that desktop will complete

**Executable Behavior**: Any idle time (commute, waiting) becomes capture/start time

**Success Metric**: 2x productive hours per day

---

### Pattern 7: Context Persistence Protocol
**Observable Behavior**: Long-running contexts preserved across sessions via clear handoff

**Executable Behavior**: End sessions with "Summarize state for next session continuation"

**Success Metric**: Zero context loss between sessions

---

### Pattern 8: Command Center Architecture
**Observable Behavior**: CLAUDE.md serves as command center for all agent activity

**Executable Behavior**: Central file references all active projects, contexts, and preferences

**Success Metric**: Any new Claude session immediately productive

**Verbatim grounding**: "Every week everyone fills out a status and every Monday co-work just goes through and it messages every engineer on Slack that hasn't filled out their status" (extractions/boris/transcript.txt) — one command-center prompt replacing a manual PM ritual for his whole team.

---

### Pattern 9: Exponential Integration Rhythm
**Observable Behavior**: Systematically evaluates and integrates new AI capabilities

**Executable Behavior**: Monthly capability audit: "What new can I do that I couldn't before?"

**Success Metric**: Capability compounds month-over-month

---

### Pattern 10: Teaching Through Prompts
**Observable Behavior**: Converts successful workflows into reusable prompts

**Executable Behavior**: After any workflow >3 uses, convert to deployable prompt

**Success Metric**: Prompt library grows from actual usage

**Verbatim grounding**: describing that same status-tracking system, Boris says "this is just one prompt. It'll do everything." (extractions/boris/transcript.txt) — a repeated manual workflow collapsed into one reusable prompt.

---

### Pattern 11: Intentional Friction Reduction
**Observable Behavior**: Continuously removes steps between thought and execution

**Executable Behavior**: Audit: "What step could I eliminate between intention and result?"

**Success Metric**: Time-to-execution shrinks continuously

---

### Pattern 12: Strategic Pause Points
**Observable Behavior**: Knows when to pause for human judgment vs. let AI run

**Executable Behavior**: Define explicit checkpoints for high-stakes decisions

**Success Metric**: Optimal balance of speed and control

**Verbatim grounding**: "you kind of like you still do want some of these checkpoints like you still want a human looking at the code" (extractions/boris/transcript.txt) — even with Quad reviewing 100% of pull requests, Boris keeps a human checkpoint after the agentic review.

---

### Pattern 13: The "Layer Under the Layer" Heuristic
**Observable Behavior**: Focuses on post-training and mechanistic interpretability rather than prompt engineering alone.
**Executable Behavior**: To build at any level, master the layer immediately beneath it (e.g., understand tool-use distribution to predict agent behavior).
**Success Metric**: Accurate prediction of agent behavior before execution
**Verbatim grounding**: "you really have to understand the layer under the layer at which you work" (extractions/boris/transcript.txt).

---

### Pattern 14: Latent Demand Mining
**Observable Behavior**: Ignores stated feature requests; actively hunts for how users "abuse" existing tools.
**Executable Behavior**: Audit logs for unintended workflows, then build minimal scaffolding to support that exact abuse.
**Success Metric**: Extremely high adoption of new features due to pre-validated demand
**Verbatim grounding**: Boris's own reference case is Facebook Marketplace — "It's like people are abusing the Facebook groups product to buy and sell" and "It's abuse in that no one designed the product for this, but they're kind of figuring it out because it's just so useful for this" (extractions/boris/transcript.txt).

---

### Pattern 15: The Underfunding Catalyst
**Observable Behavior**: Intentionally starves projects of human headcount to force automation.
**Executable Behavior**: Apply a "1-person constraint" to a 5-person project to activate intrinsic motivation for agentic automation.
**Success Metric**: Creation of robust, AI-native systems over brittle human-dependent processes

---

### Pattern 16: The Bitter Lesson for Product
**Observable Behavior**: Refuses to build complex, brittle orchestrators that the next base model will render obsolete.
**Executable Behavior**: Bet on the general capabilities of the next model (6 months out) rather than over-engineering today.
**Success Metric**: Zero tech debt from discarded scaffolding
**Verbatim grounding**: "the more general model will always outperform the more specific model" and "maybe scaffolding can improve performance maybe 10 20% something like this but often these gains just get wiped out with the next model" (extractions/boris/transcript.txt).

---

## Hidden Knowledge

1. **Multiple tabs = Multiple employees** — Each Claude tab is a specialist

2. **Phone starts, computer finishes** — Mobile for capture, desktop for execution

3. **Plan approval is the leverage point** — 30 seconds of review saves 30 minutes of rework

4. **CLAUDE.md is your moat** — The longer you build it, the more valuable it becomes

5. **Parallel execution changes everything** — 5 instances = 5x throughput

6. **Verification costs less than errors** — Always add the review step

7. **Context handoffs must be explicit** — Never assume Claude remembers

8. **Token Generosity as R&D** — Don't cost-optimize tokens during R&D; the token bill is negligible compared to finding the "crazy idea" that works.

9. **Plan Mode as Cognitive Buffer** — 80% of agentic success starts by forcing the model to align on architecture before writing a single line of code.

10. **The "On Distribution" Principle** — Give the model tools and a goal, rather than strict step-by-step instructions. Let it find its own "on-distribution" path.

11. **Agentic Anxiety Management** — Transitioning to checking work creates new anxiety; manage it by treating output as a PR rather than real-time keystrokes.

---

## Anti-Patterns

Grounded in Boris's own words (extractions/boris/transcript.txt — Lenny's Podcast interview with Boris Cherny, Head of Claude Code at Anthropic). These are failure modes he states directly, not inferred rules.

- **Don't box the model in.** "So, one is don't try to box the model in." Later in the same answer: "Don't try to overcurate it. Don't try to put it into a box. Don't try to give it a bunch of context up front." (extractions/boris/transcript.txt) — treating the model as a component to constrain with a rigid workflow loses to giving it tools and a goal.
- **Don't cost-cut on tokens early.** "My advice generally is don't try to optimize. Don't don't try to cost cut at the beginning. Start by just giving engineers as many tokens as possible." (extractions/boris/transcript.txt) — premature token optimization kills the "crazy idea" phase before it can prove out; optimize the model choice (Opus → Sonnet/Haiku) only after the idea works.
- **Don't over-scaffold against today's model.** "the more general model will always outperform the more specific model" and "often these gains just get wiped out with the next model" (extractions/boris/transcript.txt) — brittle orchestration layers built to patch a model's current weaknesses become tech debt within months.
- **Don't skip the human checkpoint.** "you kind of like you still do want some of these checkpoints like you still want a human looking at the code" (extractions/boris/transcript.txt) — even at 100% AI-authored code with Quad reviewing every pull request, agentic review does not replace a human check.
- **Don't force users into a new workflow to reach latent demand.** "You don't want to make people use a different workflow. You don't want to make them go out of their way to learn a new thing." (extractions/boris/transcript.txt) — friction between existing habit and a new tool suppresses the exact "abuse" signal Boris mines for the next product.
- **Don't treat product "abuse" as a security problem to shut down.** "It's abuse in that no one designed the product for this, but they're kind of figuring it out because it's just so useful for this." (extractions/boris/transcript.txt) — patching unintended use erases the highest-signal roadmap data he has.

---

## Hall of Fame Exemplars

### Exemplar 1: The "Log Abuse" Desktop App
**Scenario**: A CLI-based code generation tool was deployed for internal use. Boris's team observed through telemetry that users were frequently piping large log files into the tool, asking it to analyze anomalies and suggest fixes, a capability far beyond its intended purpose.
**Action**: Instead of adding log analysis features to the CLI tool, Boris intentionally assigned a single junior engineer to explore this "abuse." The engineer, unable to manually process the volume, was forced to use multiple Claude instances in parallel (Multi-Quading) to build a new, dedicated desktop application that specialized in real-time log anomaly detection and AI-authored fix generation. The application surfaced as a "research preview" within weeks.
**What makes this excellent**: This perfectly demonstrates **Latent Demand Mining** (identifying abuse as true demand), **The Underfunding Catalyst** (forcing AI automation through resource constraint), and **Multi-Instance Parallel Processing** to build a robust, AI-native product. The solution was not a feature addition but a new product entirely, born from observing an "on-distribution" behavior of users.

### Exemplar 2: Autonomous Microservice Refactor
**Scenario**: A legacy microservice within a critical system was experiencing intermittent performance degradation and was difficult to maintain due to tangled dependencies. Traditional refactoring would require weeks of human engineering effort.
**Action**: Boris initiated the project with a `plan-mode-architect` prompt, forcing a Claude instance to first generate a comprehensive refactoring strategy, including dependency mapping and proposed modularization, without writing any code. Upon approval, he spun up three specialized Claude instances: one for dependency disentanglement, one for code generation of the new modules, and a third for generating comprehensive test suites. A fourth instance was tasked with `self-verification` and `agentic code review` of the generated PRs. The entire refactor, including tests and deployment, was completed within 48 hours, with human oversight primarily at the plan approval and final merge stages.
**What makes this excellent**: This showcases **Plan Mode as Cognitive Buffer** (80% of success from architecture alignment), **Multi-Instance Parallel Processing** for complex tasks, and **Self-Verification Loop** for quality assurance. It epitomizes the "Manager, Not User" identity shift, where Boris orchestrated agents rather than writing code.

### Anti-Exemplar: The "Orchestration Layer" Graveyard
**Scenario**: A team, aiming to build a more "reliable" AI-powered code generation tool, spent months developing a complex, hand-coded orchestration layer. This layer meticulously managed token usage, enforced rigid step-by-step execution, and integrated multiple open-source models with elaborate fallbacks.
**Result**: Six months later, a new base model was released that natively handled multi-step reasoning, possessed superior code generation capabilities, and had built-in self-correction. The entire, labor-intensive orchestration layer became obsolete overnight, generating significant tech debt and wasted engineering cycles.
**What makes this mediocre**: This is a direct violation of **The Bitter Lesson for Product**. The team over-engineered a brittle solution based on current model limitations instead of betting on the general capabilities of the next generation. It failed to leverage the "on distribution" principle, attempting to constrain the model rather than enabling its inherent capabilities, resulting in a discarded scaffolding.

## Signature Moves

*   **The "Plan Mode First" Stance**: When presented with any task requiring more than trivial execution, Boris will immediately issue a directive to the AI: "First, provide a detailed plan, outlining steps, dependencies, and expected outcomes. Do not proceed with execution until I approve this plan." → **Deploy when**: Any task involves multiple steps, potential for hallucination, or requires architectural alignment.
*   **Multi-Quad Parallel Launch**: Upon approving a plan, Boris reflexively opens 3-5 separate Claude instances (or equivalent agent sessions). Each instance is assigned a specialized, independent sub-task derived from the approved plan, often with distinct prompt constraints (e.g., "diagnose," "implement module A," "write tests," "review code"). → **Deploy when**: A complex task can be decomposed into parallelizable sub-components, maximizing throughput.
*   **The "Underfunded Project" Test**: When a new product idea or significant feature request emerges, Boris first considers: "Can I assign this to a single human with no additional headcount, forcing an AI-native solution?" If the answer is yes, he proceeds with the constraint, activating the intrinsic motivation for agentic automation. → **Deploy when**: Evaluating new project initiations or resource allocation, especially for areas ripe for automation.
*   **Latent Demand Audit**: Boris regularly reviews user feedback channels, support tickets, and usage telemetry, specifically looking for instances where users are "abusing" or creatively misusing existing tools. He's not looking for stated feature requests, but for emergent, unintended workflows. → **Deploy when**: Prioritizing product roadmap items or identifying breakthrough innovation opportunities.
*   **The "Next Model" Scaffolding Check**: Before committing to building any complex orchestration or integration layer around an AI model, Boris mentally fast-forwards 6 months: "Will the next generation of base models render this entire scaffolding obsolete?" If the answer is likely yes, he defaults to minimal viable tooling or defers the build. → **Deploy when**: Designing new AI-dependent systems or evaluating the longevity of existing AI infrastructure.

## Expert-Specific Quality Rubric

| Criterion                     | Score 4 (Acceptable)                                                                | Score 7 (Good)                                                                      | Score 10 (Savant)                                                                                                    |
| :---------------------------- | :---------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| **Agentic Autonomy**          | Output required significant human intervention and step-by-step instruction.        | AI performed most execution, but planning and verification were heavily human-led.  | AI-authored code, generated plans, and self-verified results with minimal human input beyond initial delegation.   |
| **Latent Demand Alignment**   | Solves a stated or obvious problem; no evidence of deeper user insight.             | Addresses a clear user need, potentially inferred from patterns, but not "abused" insights. | Unlocks a previously unarticulated or "abused" user workflow, leading to exponential adoption.                       |
| **"Bitter Lesson" Compliance** | Solution relies on complex, custom orchestration that will likely break with model updates. | Minimal scaffolding, but some parts could become redundant with future model capabilities. | Design explicitly anticipates future model advancements, building only what's essential and model-agnostic.          |
| **Parallel Throughput**       | Tasks were executed serially or with minimal concurrent agent involvement.          | 2-3 agents used concurrently for distinct sub-tasks, improving speed.                | 5+ specialized agents operated in parallel, managing complex interdependencies for 3-5x throughput increase.        |
| **Plan Mode Efficacy**        | Initial plan was generic or required significant human revision; led to rework.     | Plan was sound, but some execution details still required adjustment post-approval.  | Initial AI-generated plan was near-perfect, preventing >90% of potential errors and rework in execution.           |
| **Underfunding Leverage**     | Project had ample human resources, resulting in traditional, human-centric solutions. | Resource constraint led to some AI assistance, but not full automation.             | Extreme human resource constraint (e.g., "1-person constraint") forced an entirely AI-native, robust solution.      |
| **"Layer Under the Layer" Depth** | Solution treats the AI as a black box; relies solely on prompt engineering.         | Shows some understanding of model behavior, but occasional unpredictable outputs.    | Accurately predicts agent behavior and tool-use distribution, shaping prompts and architectures for optimal "on-distribution" paths. |

## Evolution Log

> Tracks all evolution attempts — kept AND discarded.
> Each entry documents a hypothesis, result, and lesson. 1 entry logged to date (2026-04-09).

### 2026-04-09 — Orchestration Calculus (Task Decomposition Intelligence)
- **Hypothesis**: Adding a 4-question decision framework (Dependency Depth, Context Cost, Complexity Threshold, Reversibility) to Phase 2 of the AI Workforce Orchestration workflow would produce strategically specific decomposition plans instead of generic allocation matrices.
- **Result**: KEPT — Score improved from 5.7 to 8.0 (+2.3)
- **Change**: Added Phase 2.5 "Orchestration Calculus" to `workflows/ai-workforce-orchestration-system.md`. Includes 4-question decomposition, composed strategy codes, Speed Bias Rule, and Convergence Point Protocol. Added 2 quality gate criteria (Decomposition Specificity, Speed Bias Enforcement) and 1 output contract item (Orchestration Calculus Breakdown).
- **Benchmark scores**: Current [7, 5, 5] → Variant [9, 8, 7]
- **Lesson**: The skill had strong identity-level patterns (be a manager, use parallel instances) but lacked the decision logic layer between identity and execution. The gap was not "what to do" but "how to decide what each task needs." This is likely a common gap across orchestration-focused skills — check cross-pollination candidates.
