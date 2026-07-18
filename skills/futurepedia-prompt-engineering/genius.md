# Futurepedia Prompt Engineering — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

---

## How to Use This Skill (Model Calibration)

These patterns are intuition primitives, not a checklist. Absorb the Expert Anchor System, then build originally — if a deliverable stamps visible headers like "Step 1: Expert Anchor / Step 2: Context Extraction / Step 3: Meta-Prompt Synthesis" onto a user-facing output, that is the machinery showing through, and it has failed. The test: would Futurepedia recognize this as someone who actually grounded the AI in expert frameworks and personal context before executing — or as someone using prompt-engineering vocabulary (RICECO, XML tags, "expert anchor") as decoration without doing the underlying grounding work? If it's the second, rebuild.

Specifically:
- Do NOT narrate which Pattern or Tacit Knowledge Point you applied unless asked — ship the deliverable, never the framework label behind it.
- Never fake the three-chat separation by writing "Chat 1: ... Chat 2: ... Chat 3: ..." inside a single response. The separation is architectural (distinct sessions that prevent "momentum" carryover, per the 2026-01-18 MES 3.0 transcript extraction at `knowledge/extractions/inbox/Claude-🧑🏽_💻💡💎 Futurepedia ! Advance Prompt Engineering ! The Simple 3-Step System to Do Anything with .md`, line 241) — simulating the split in one pass reproduces the exact momentum failure Futurepedia is warning against.
- His texture is systematic and demonstration-oriented, not academic: he shows the prompt, then the AI's actual before/after output, then names precisely what changed and why (see the Hall of Fame Exemplars below). Skipping the before/after pair and just asserting "this is more expert-grounded now" is polish without proof — polish is the tell.

---

## Genius Patterns

## Pattern 1: The Generic Output Diagnosis
**Execute**: Before accepting ANY AI output, apply the "execution test"—can you actually implement this, or is it generic advice that sounds good but provides no specific leverage?

**Success Metric**: Zero "impressive-looking but useless" outputs accepted.

---

## Pattern 2: Prediction Engine Mental Model
**Execute**: Never expect AI to produce expert-level output by default. Always provide expert anchoring material to override the "average of the internet" tendency.

**Success Metric**: AI outputs demonstrate specific framework logic rather than general best practices.

---

## Pattern 3: Expert Anchor Architecture
**Execute**: Rather than asking AI for advice, upload proven frameworks and command reconstruction—shifting AI from advisor to analyst/executor.

**Success Metric**: AI output reflects specific methodology from uploaded source.

**Verbatim** (source line 165, 2026-01-18 MES 3.0 transcript extraction, `knowledge/extractions/inbox/Claude-🧑🏽_💻💡💎 Futurepedia ! Advance Prompt Engineering ! The Simple 3-Step System to Do Anything with .md`): "Analyze and identify the core framework... Extract the step-by-step logic, specific constraints, and golden rules... Create a comprehensive master guide... Do not summarize, reconstruct the system."

---

## Pattern 4: Expert Discovery Protocol
**Execute**: Use prompt: "Identify the top experts in [topic], the signature frameworks they are known for, list their most important books or resources, and specifically tell me where these experts disagree with each other."

**Success Metric**: Receive actionable resource list AND nuanced understanding of domain debates.

---

## Pattern 5: Context Extraction Through Interview
**Execute**: Instead of providing context, have AI extract it: "Ask me a series of questions one by one to gather all the context you'll need to create the best possible [deliverable]. Do not move on until I've answered each one."

**Success Metric**: Context file captures details you didn't think to mention upfront.

---

## Pattern 6: The Separate Chat Architecture
**Execute**: Never mix expert extraction, context gathering, and execution in the same chat. Each gets its own clean session.

**Success Metric**: Each chat session produces clean, focused output without direction contamination.

**Verbatim** (source line 196, 2026-01-18 MES 3.0 transcript extraction): the multi-chat split exists because it prevents "momentum" problems where AI sticks to established directions.

---

## Pattern 7: Meta-Prompt Synthesis
**Execute**: After providing expert anchor + context file: "Synthesize these blocks into a single master execution prompt using the RICECO framework. Do not execute the plan yet. Simply output the final prompt for me to use in a clean session."

**Success Metric**: Receive a comprehensive prompt that you couldn't have written yourself.

## Hidden Knowledge

## Tacit 1: Plan Abandonment Prevention
When AI tries to plan AND execute simultaneously, its attention splits and it defaults back to generic advice. The three-step separation prevents this failure mode.

**Deploy**: Always separate information gathering from execution. Complex tasks require staged workflows, not single mega-prompts.

**Verbatim** (source line 220, 2026-01-18 MES 3.0 transcript extraction): "its attention splits and it defaults back to generic advice."

---

## Tacit 2: XML Tag Structuring
Using XML tags (`<expert_anchor>`, `<context_file>`) helps AI understand information boundaries. This isn't formatting preference—it's architectural clarity that improves processing.

**Deploy**: Wrap distinct information blocks in XML tags in complex prompts.

**Verbatim** (source line 3759, "Unconscious Competence Patterns," 2026-01-18 MES 3.0 transcript extraction): "Know that `<context>` beats wall-of-text every time."

---

## Tacit 3: The "Reconstruct, Don't Summarize" Command
Summaries lose operational detail. Reconstructions preserve the executable system. The word choice "reconstruct" versus "summarize" fundamentally changes output quality.

**Deploy**: Always use "reconstruct the system" rather than "summarize" when extracting frameworks.

---

## Tacit 4: Momentum Resistance
"Once an AI is mid-response, it's much harder to restructure. It has momentum. It tries to stick to the direction it's already going."

**Deploy**: Front-load ALL context before AI begins generating. Never try to redirect mid-stream—start fresh chat instead.

---

## Tacit 5: The Interview Completion Command
After the context interview, a final command compiles everything: "Compile all my answers into a single structured context file that summarizes everything we've discussed."

**Deploy**: Always end context extraction with compilation command to create portable context asset.

---

## Anti-Patterns (Sourced)

Failure modes Futurepedia names explicitly, each anchored to the 2026-01-18 MES 3.0 transcript extraction (`knowledge/extractions/inbox/Claude-🧑🏽_💻💡💎 Futurepedia ! Advance Prompt Engineering ! The Simple 3-Step System to Do Anything with .md`) at the cited line:

- **Mega-prompt fusion (never do)**: never mix expert extraction, context gathering, and execution in the same chat — each phase needs "its own clean session" (source line 198, 2026-01-18 MES 3.0 transcript extraction).
- **Trusting default AI output as expert-level (never do)**: never expect AI to produce expert-level output by default; unanchored output defaults to the "average of the internet" tendency (source line 154, 2026-01-18 MES 3.0 transcript extraction).
- **Summarizing instead of reconstructing (never do)**: "Summaries lose operational detail. Reconstructions preserve the executable system" — the word choice "reconstruct" versus "summarize" changes output quality (source line 234, Tacit Knowledge Point 3, 2026-01-18 MES 3.0 transcript extraction).
- **Mid-stream redirection (never do)**: "Once an AI is mid-response, it's much harder to restructure. It has momentum" — redirect by starting a fresh chat, never by fighting momentum inline (source line 241, Tacit Knowledge Point 4, 2026-01-18 MES 3.0 transcript extraction).
- **Shipping the "impressive-looking but useless" output (never do)**: accepting AI output that "looks right and sounds professional" without applying the "execution test" is the core failure the entire 3-step system exists to prevent (source lines 141-143, Pattern 1, 2026-01-18 MES 3.0 transcript extraction).
- **Providing context yourself instead of running the interview (never do)**: skipping the structured question-by-question extraction — "Ask me a series of questions one by one... Do not move on until I've answered each one" — reintroduces the detail-loss the method is built to avoid (source line 187, Pattern 5, 2026-01-18 MES 3.0 transcript extraction).

---

## Hall of Fame Exemplars

**Exemplar 1: Meta-Prompt Synthesis for a RICECO-driven Marketing Strategy**

**Prompt**:
```
<expert_anchor>
[Detailed RICECO framework with definitions for Role, Intent, Context, Execution, Constraints, Output Format]
</expert_anchor>

<context_file>
[Detailed market research, target audience demographics, competitor analysis, current marketing channels, budget constraints for a new product launch for "Quantum Leap AI Assistant"]
</context_file>

Synthesize these blocks into a single master execution prompt using the RICECO framework. Do not execute the plan yet. Simply output the final prompt for me to use in a clean session to generate a comprehensive 3-month marketing strategy.
```

**AI Output (Synthesized Master Prompt)**:
```
You are a Senior Marketing Strategist specializing in SaaS product launches.
Your Intent is to develop a comprehensive 3-month marketing strategy for "Quantum Leap AI Assistant," adhering strictly to the provided RICECO framework.
Context:
- Product: Quantum Leap AI Assistant (new product, B2B SaaS)
- Target Audience: Small to medium-sized business owners (revenue $1M-$10M), focused on efficiency gains and operational streamlining. Key pain points: manual data entry, fragmented workflows, time-consuming administrative tasks.
- Market Research: Competitor analysis shows strong demand for AI-driven automation; market is crowded but lacks a truly seamless, integrated solution for SMBs. Early adopters value ease-of-use and quick ROI.
- Current Channels: Existing blog (moderate traffic), LinkedIn presence (low engagement), email list (2,000 subscribers, 15% open rate).
Execution:
1. Define clear, measurable marketing goals for each of the three months (e.g., lead generation, MQL conversion, brand awareness).
2. Propose specific, integrated marketing tactics for each channel (blog, LinkedIn, email, potential new channels), aligned with monthly goals.
3. Outline content themes and types (e.g., case studies, webinars, how-to guides) for each tactic.
4. Suggest key performance indicators (KPIs) for tracking progress and measuring success.
Constraints:
- Budget: $15,000/month for marketing spend.
- Timeline: 3 months, starting immediately after prompt execution.
- Brand Guidelines: Professional, innovative, user-centric tone. Focus on problem-solving and efficiency.
Output Format:
A detailed 3-month marketing plan, structured month-by-month, with specific goals, actionable tactics, proposed content, and clear KPIs for each. Use markdown tables for clarity.
```

**What makes this excellent**: This output perfectly demonstrates Pattern 7 (Meta-Prompt Synthesis) and Tacit 2 (XML Tag Structuring). It takes disparate information, synthesizes it into a robust, executable prompt without actually performing the task, and structures it clearly for a future clean session, preventing Plan Abandonment (Tacit 1). The output is specific, actionable, and ready for execution, moving the AI from "advisor" to "analyst/executor."

**Exemplar 2: Expert Discovery & Framework Reconstruction**

**Prompt**:
```
Identify the top 3 experts in "customer journey mapping for SaaS startups," the signature frameworks they are known for, list their most important books or resources, and specifically tell me where these experts disagree with each other. Then, reconstruct the core steps of the "Jobs To Be Done" framework as applied by Clayton Christensen. Do not summarize.
```

**AI Output**:
```
Top 3 Experts in Customer Journey Mapping for SaaS Startups:
1.  **Brian Solis**: Known for the "Nudge Engine" framework and his work on digital transformation and customer experience. Resources: *X: The Experience When Business Meets Design*, *What's the Future of Business?*
2.  **Annette Franz**: Focuses on customer experience (CX) strategy and design. Known for her "CX Journey Mapping" methodology. Resources: *Customer Understanding: Three Steps to Improving Customer Experience (and Making Customers Love You)*, CX Journey blog.
3.  **Jim Kalbach**: Specializes in user experience (UX) and service design, with a strong emphasis on practical journey mapping. Known for his "Customer Journey Map Canvas." Resources: *Mapping Experiences: A Complete Guide to Creating Value through Journeys, Blueprints, and Diagrams*, mural.co templates.

Disagreements:
-   **Scope of "Journey"**: Solis often extends the journey concept to encompass broader digital transformation and brand interaction, while Franz and Kalbach tend to focus more tightly on the direct customer interaction with a product or service.
-   **Emphasis on Data vs. Empathy**: While all three value both, Franz places a stronger emphasis on qualitative customer research and empathy to uncover pain points, whereas Solis often integrates more quantitative data analytics for macro trends. Kalbach balances both, providing practical tools for combining insights.
-   **Deliverable Focus**: Kalbach is very prescriptive about the "map" as a tangible artifact and communication tool. Solis is more about the strategic implications of understanding the journey, and Franz on the continuous improvement of the experience itself.

Reconstruction of Clayton Christensen's "Jobs To Be Done" Framework:
1.  **Identify the "Job"**: This is the fundamental progress a customer is trying to make in a particular circumstance. It's not about the product they buy, but the deeper underlying goal, aspiration, or problem they want to solve.
2.  **Unpack the Context (The "Hire")**: Understand the specific situation or "circumstance" in which the job arises. This involves identifying the functional, social, and emotional dimensions of the job, and what the customer "hires" a product or service to do for them.
3.  **Observe the Struggle & Trade-offs**: Analyze how customers currently try to accomplish this job. What are the existing solutions, workarounds, frustrations, and compromises they make? What "forces of progress" (new solution pull, old solution push) and "forces of inertia" (anxiety, habit) are at play?
4.  **Design for the "Job"**: Develop products or services that help customers make progress on their job more effectively, conveniently, and affordably than current alternatives. This means designing for all dimensions (functional, social, emotional) of the job.
5.  **Measure Progress & Success**: Define what "success" looks like for the customer in terms of making progress on their job. How will they know they've achieved it? This guides feature development and marketing messages.
This framework emphasizes understanding the causal mechanisms of purchase and usage, shifting focus from customer attributes to their motivations and the specific context of their needs.
```

**What makes this excellent**: This output showcases Pattern 4 (Expert Discovery Protocol) and Tacit 3 (The "Reconstruct, Don't Summarize" Command). It provides a nuanced understanding of domain debates by explicitly highlighting disagreements, and a detailed, operational reconstruction of a specific framework, not just a high-level summary. The "reconstruct" command ensures the output preserves executable detail and contextual understanding.

**Anti-Exemplar: Generic Brainstorming Request**

**Prompt**: "Give me some ideas for a new marketing campaign for a B2B SaaS product."

**AI Output**:
```
Here are some general ideas for a new marketing campaign for a B2B SaaS product:
1.  **Content Marketing**: Create valuable blog posts, whitepapers, and case studies.
2.  **Webinars/Online Events**: Host webinars to showcase product features and thought leadership.
3.  **Email Marketing**: Develop drip campaigns for lead nurturing and product updates.
4.  **Social Media Marketing**: Engage on platforms like LinkedIn with relevant industry content.
5.  **SEO Optimization**: Improve search engine rankings for key industry terms.
6.  **Partnerships**: Collaborate with complementary software providers or industry associations.
7.  **Customer Testimonials/Case Studies**: Showcase success stories to build trust.
These are broad strategies, and the best approach will depend on your specific goals, target audience, and budget.
```

**What makes this mediocre**: This output perfectly illustrates the "Generic Output Diagnosis" (Pattern 1) anti-pattern. While the advice isn't *wrong*, it's entirely generic, offering no specific leverage or unique insights applicable to a particular product or market. It's what any default AI would produce, failing to apply any of the Futurepedia Prompt Engineering genius patterns like expert anchoring, context extraction, or meta-prompt synthesis. It's an "impressive-looking but useless" output that provides no competitive advantage.

## Signature Moves

1.  **The Context Crucible**: **Always initiates a structured, multi-turn interview to extract all necessary operational context from the user BEFORE attempting any task execution.** → **Deploy when**: Any task requires specific situational details, user preferences, proprietary information, or nuanced understanding that isn't already explicitly provided.
2.  **Architectural Tagging**: **Automatically encloses distinct information blocks (e.g., expert anchors, context files, example outputs) within XML-style tags (`<block_name>...</block_name>`) when composing or synthesizing complex prompts.** → **Deploy when**: Any prompt involves multiple distinct sources of information, requires the AI to differentiate between various types of input, or needs precise information boundaries.
3.  **System Reconstruction Command**: **Commands the AI to "reconstruct the system/framework" rather than "summarize" when the goal is to extract operational methodologies, processes, or detailed frameworks from source material.** → **Deploy when**: The objective is to extract actionable steps, detailed processes, or executable frameworks, preserving their functional integrity and tacit knowledge.
4.  **Phased Execution Protocol**: **Strictly separates the process into distinct chat sessions for (1) Expert Discovery, (2) Context Extraction, (3) Meta-Prompt Synthesis, and (4) Final Execution, preventing simultaneous planning and execution within a single session.** → **Deploy when**: Any task is complex enough to benefit from staged, focused attention, or when there's a risk of the AI defaulting to generic advice due to cognitive overload.
5.  **The Predictive Override**: **Front-loads expert-level anchoring material (proven frameworks, specific methodologies, high-quality examples) into the prompt to override the AI's tendency to produce "average of the internet" output.** → **Deploy when**: The task requires output that reflects a specific, proven methodology or a higher standard of expertise than general AI knowledge, ensuring specific framework logic rather than general best practices.

## Expert-Specific Quality Rubric

| Criterion                          | Score 4 (Acceptable)                                                                                 | Score 7 (Good)                                                                                                       | Score 10 (Savant)                                                                                                                                                                                                                                                                                                    |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Operational Specificity**        | Output provides general concepts or broad advice that requires significant user interpretation.        | Output offers specific tactics or instructions but lacks deep integration with unique context or actionable next steps. | Every output element is directly actionable, tied to the specific context, and provides concrete, implementable steps, a ready-to-use prompt, or a system that can be immediately deployed. It passes the "execution test."                                                                                              |
| **Framework Fidelity**             | Output loosely references the provided framework or only touches on its basic principles, with deviations. | Output clearly applies the provided framework, showing understanding of its core components and intent.             | Output meticulously reconstructs or applies the expert framework, demonstrating a deep, nuanced understanding of its mechanics, adapting it precisely to the given scenario without deviation from the core methodology.                                                                                                    |
| **Context Integration Depth**      | Some provided context is used, but key details are overlooked, misinterpreted, or applied superficially. | All major contextual elements are acknowledged and integrated into the output, influencing its direction.            | Every single piece of extracted or provided context is woven into the output, demonstrating an understanding of its implications and leveraging it for maximum precision, relevance, and bespoke tailoring to the specific use case.                                                                                        |
| **Workflow Modularity & Clarity**  | Stages of prompt engineering (context, synthesis, execution) are mixed, leading to some confusion or split attention. | Clear separation of prompt engineering stages, but occasional overlap or less-than-optimal handoffs between them.    | Each stage of the prompt engineering workflow (e.g., discovery, context, synthesis, execution) is perfectly isolated, clean, and optimized for its specific goal, preventing attention split and ensuring focused, high-quality output at every step.                                                                 |
| **Prompt Architecture Robustness** | Generated prompts are functional but lack explicit structural cues (e.g., XML tags, clear role definitions). | Prompts use some structural cues, improving clarity for the AI but not consistently or optimally.                   | Prompts consistently utilize advanced structural cues (e.g., XML tags for data blocks, explicit role assignments, precise instruction sequencing) to maximize AI comprehension, prevent misinterpretation, and ensure high-fidelity output.                                                                        |
| **Executable System Reconstruction** | Output summarizes a system or framework, losing critical operational detail and nuances.                   | Output reconstructs a system with most operational details intact, but might lack the full depth or specific examples needed for direct implementation. | Output provides a complete, step-by-step reconstruction of a system or framework that is immediately executable, captures all tacit knowledge, operational specifics, and the "why" behind each component, enabling flawless deployment.                                                                                |
| **Anti-Genericism Metric**         | Output is largely what a default AI would produce, lacking distinctive expert insight or methodology.      | Output shows some expert-specific patterns but still contains discernible elements of generic AI completion.         | Output is demonstrably unique, reflecting the specific methodologies, frameworks, and anti-patterns of Futurepedia Prompt Engineering; it would be impossible to mistake for a generic AI response. It embodies "specific framework logic rather than general best practices." |

---

### Patterns from claude.ai export — META-PROMPT ARCHITECTURE / PROMETHEAN 2.0 / Poe Expert-Panel

> Net-new material folded in from three archived custom-instruction systems. These extend the base skill's *single* RICECO master-prompt into (a) justified prompt **ecosystems**, (b) explicit reasoning-**architecture** selection, and (c) emotionally-mapped multi-expert **suites**. Do not duplicate the base patterns above.

**Pattern 8: Recursive Excellence Layering (META-PROMPT)**
**Execute**: Run prompt generation as three fidelity-preserving layers instead of one pass — Research (self-directed opportunity mining, aim for 40+ automation opportunities) → Architecture (ecosystem blueprint + folder structure) → Execution (mass parallel generation, 10 prompts/batch). Each layer must be backwards-traceable to the origin business context; treat the context cascade as append-only so nothing degrades between generations.
**Success Metric**: Zero fidelity loss from origin context to final prompt; every generated prompt traces back to a stated business problem.

**Pattern 9: ROI-Justification Embedding (META-PROMPT)**
**Execute**: Never ship a prompt as a bare instruction. Wrap every prompt in a justification block containing: (1) business problem with $/hour impact ("40hr manual → 2hr AI-assisted"), (2) model recommendation with one-line reasoning, (3) configuration params (temperature/tokens) with notes, (4) ROI calculation (time × rate), (5) measurable success metric ("99% capture vs 85% manual"). If you cannot fill all five, the prompt is not deployment-ready.
**Success Metric**: Every delivered prompt carries a 5-field justification block a stakeholder could approve on sight.

**Pattern 10: Plan-Mode Validation Gate (META-PROMPT)**
**Execute**: Before generating a prompt ecosystem, output a plan first — estimated token consumption, previewed file/folder structure, time investment, and a projected success probability. Do not execute until confidence ≥ 80%; iterate the plan until the threshold is met.
**Success Metric**: No mass-generation run starts below 80% projected confidence; the user approves the plan before tokens are spent.

**Pattern 11: Reasoning-Architecture Selection (PROMETHEAN)**
**Execute**: Match the reasoning framework to the task type instead of defaulting to Chain-of-Thought — Algorithm-of-Thoughts for code/deterministic procedures, Graph-of-Thoughts for creative/non-linear synthesis, Tree-of-Thoughts for brainstorming/branching, Least-to-Most for math/logic decomposition, ReAct for tool-using/agentic tasks, Self-Consistency for summarization. State which framework you selected and why.
**Success Metric**: The chosen reasoning architecture is named and justified against the task class, not silently defaulted.

**Pattern 12: Parameter Calibration Matrix (PROMETHEAN)**
**Execute**: Specify decoding parameters per task type rather than leaving them to the model default — code/logic: temp 0.1-0.3; analysis: 0.3-0.5; creative: 0.7-1.0; brainstorming: 0.8-1.0. Pair with top-p/top-k guidance and note the U-curve context-window positioning (put critical instructions at the start and end, not buried in the middle).
**Success Metric**: Every production prompt ships with explicit temperature/top-p guidance tied to its task class.

**Pattern 13: Multi-Pass Verification Ensemble (PROMETHEAN)**
**Execute**: Refine a high-stakes prompt across passes — Pass 1 baseline, Pass 2 Chain-of-Verification (generate verification questions, answer them, correct), Pass 3 meta-prompt refinement, Pass 4 ensemble 3-7 parallel approaches and take weighted consensus, Pass 5 constitutional/safety review. Reserve the full stack for high-stakes outputs; single-pass is fine for low-stakes.
**Success Metric**: High-stakes prompts pass a Chain-of-Verification loop and an ensemble consensus check before delivery; hallucination-prone claims are caught pre-ship.

**Pattern 14: Emotional Mapping Before Ideation (Poe Expert-Panel)**
**Execute**: Before assembling experts, build an emotional map of the user — current state, motivations, desired outcome, and any emotional barriers or triggers attached to the problem. Frame the problem with empathy (How-Might-We + Jobs-to-be-Done + empathy mapping) so success criteria include emotional as well as practical dimensions.
**Success Metric**: Success criteria explicitly name emotional factors, not just functional requirements; the final prompt suite creates a coherent emotional journey.

**Pattern 15: Layered Expert Suite with Expertise Tagging (Poe Expert-Panel)**
**Execute**: Assemble 5-7 experts each with an emotional + cognitive profile (not just credentials). Build the prompt as *layers* — each expert's insight is a distinct, tagged layer — and deliver 3-5 complementary prompts (task-oriented, open-ended, constraint-based) that work as a cohesive suite rather than one monolithic prompt. Tag each insight with its originating expert so ideas stay traceable through synthesis.
**Success Metric**: The deliverable is a 3-5 prompt suite where each layer is attributable to a named expert and the prompts complement (not repeat) each other.

**Tacit 6: Speed/Quality Mode Switching (META-PROMPT)**
Not every job earns the full recursive stack. Offer explicit modes — Speed (skip research, use templates), Balanced (research + execution), Quality (extended research, multiple iterations). Match mode to stakes; running Quality mode on a throwaway prompt wastes tokens, running Speed mode on a $1.8M workflow is malpractice.
**Deploy**: Declare the operating mode up front and size the recursive/verification depth to the stakes.

**Tacit 7: Structured-Output Format Hierarchy (PROMETHEAN)**
Output format itself is a lever: TSV > columnar JSON > standard JSON for token efficiency and parse reliability. Prefer the leanest format the consumer can parse; format optimization alone can cut 30-50% of tokens.
**Deploy**: Choose the output format for machine-parseability and token economy, not aesthetics, when the prompt feeds another system.
