# Rachel Woods: AI Operations Mastery — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns

## 1. The Decomposition Instinct

**What They Do**: Takes any complex business function and breaks it into discrete tasks, then classifies each by automation readiness — without hesitation or analysis paralysis.

**Executable Behavior**:
1. Name the function (e.g., "client onboarding")
2. List every step chronologically
3. For each step, ask: "Does this require judgment, or just execution?"
4. For judgment steps, ask: "Can I give AI criteria to make this judgment?"
5. If yes → Good Enough Task. If no → Expert Task. If no judgment → Objective Task.
6. Start automating from Objective Tasks upward.

**Deploy When**: Any time someone says "we can't automate that" or "it's too complex for AI." The decomposition reveals that the complex function is actually a chain of simple tasks, many of which are automatable.

**Success Metric**: Every task in the function has a clear input, output, and automation tier assignment. No task is left as "too complex" without being decomposed further.

---

## 2. The Specification Habit

**What They Do**: Never builds a prompt in isolation — always builds a full specification document that accounts for the surrounding system.

**Executable Behavior**:
1. Before writing any prompt, answer:
   - Where does this prompt live in the workflow? (What comes before? After?)
   - What does "good enough" output look like? (Define the quality bar)
   - What happens when it fails? (Error handling and fallback)
   - Who reviews the output, when, and how? (Human checkpoint)
2. Write the MASTER spec first (Mission, Audience, Style, Tone, Examples, Response format)
3. Only then write the actual prompt
4. Include the spec alongside the prompt as documentation

**Deploy When**: Building any AI workflow that will be used more than once, or by anyone other than the original builder.

**Success Metric**: A new team member can pick up the spec and run the prompt without asking questions. The prompt produces consistent results across different users.

---

## 3. The Operator Positioning

**What They Do**: Creates and fills a professional category — "AI Operator" — that sits between strategist and executor, capturing the highest-leverage position in AI transformation.

**Executable Behavior**:
1. Identify the gap: Who is translating business strategy into AI workflows? (Usually nobody.)
2. Position the operator as: more strategic than an implementer, more practical than a consultant, more scalable than an executive.
3. Define the operator's deliverables: process maps, task hierarchies, CRAFT blueprints, MASTER specs.
4. Make the role measurable: time recaptured, processes automated, quality improvements, cost reductions.

**Deploy When**: Positioning yourself or someone else as the person who "owns AI" in an organization. Also deploy when a company has AI tools but no coherent strategy for using them.

**Success Metric**: The organization has a named person responsible for AI operations, with clear KPIs and a first-90-days roadmap.

---

## 4. The Quality Bar as Design Principle

**What They Do**: Starts every AI implementation decision with "how good does it need to be?" instead of "how good can it be?" This prevents both over-engineering and under-engineering.

**Executable Behavior**:
1. For each task in a process, define the quality bar on a scale:
   - 80% accuracy → Full automation with spot checks
   - 90% accuracy → AI draft + human polish
   - 95% accuracy → Human-led with AI research support
   - 99%+ accuracy → Human only, AI cannot participate
2. Assign automation level based on quality bar, not AI capability.
3. Revisit quality bars quarterly as AI improves.

**Deploy When**: Designing any AI workflow. Especially important when stakeholders have either unrealistic expectations ("AI should be perfect") or unnecessary fears ("AI isn't reliable enough").

**Success Metric**: Every AI task in the workflow has an explicit, documented quality bar that the team has agreed to. No debates about "is AI good enough?" — the bar is already defined.

---

## 5. The Compound System

**What They Do**: Connects individual AI tasks into chains that produce emergent capabilities — output of one task feeds into the next, creating systems that are greater than the sum of their parts.

**Executable Behavior**:
1. Map the progression: Single prompt → Prompt chain → Workflow → System → Learning system → AI Edge.
2. For each AI task, ask: "Can the output of this task feed into another task?"
3. For each chain, ask: "Can the results be stored and used to improve future runs?"
4. For each system, ask: "What data is being generated that creates a competitive moat?"
5. Build feedback loops: route outputs back to earlier stages to improve quality over time.

**Deploy When**: Moving beyond individual AI tasks to building systems. When a company has 3+ AI tasks running independently, look for connection opportunities.

**Success Metric**: AI tasks are interconnected, with outputs feeding downstream tasks. The system generates proprietary data and improves over time without manual intervention.

## Hidden Knowledge

## 1. The 30% Ceiling Is Structural, Not Technical

**Tacit Insight**: Companies that bolt AI onto existing processes hit a hard ceiling at ~30% productivity improvement. This isn't because AI can't do more — it's because the processes themselves were designed for humans, and optimizing a human process with AI only captures incremental gains. Systemic transformation (100%+ improvement) requires redesigning processes with AI as a native capability.

**Why Others Miss This**: Most AI consultants celebrate the 30% gain and move on. They attribute the ceiling to "AI limitations" instead of recognizing it as a process design problem. The real bottleneck is human workflow architecture, not model capability.

**Deploy When**: A company reports being "satisfied" with their AI implementation but you can see they've only scratched the surface. Use this to reframe the conversation from "AI is working" to "you're leaving 70% of the value on the table."

---

## 2. Operators Are the Missing Layer

**Tacit Insight**: Most AI transformation failures aren't about tools or strategy — they're about the gap between the two. Companies hire visionaries (executives who see the opportunity) and implementers (people who can build prompts and automations). But without an operator — someone who maps business processes to AI capabilities and architects the system — the visionary's ideas never translate into the implementer's work.

**Why Others Miss This**: The AI industry markets tools (for implementers) and strategy (for visionaries). Nobody is marketing the connective tissue. Rachel identifies this as the highest-leverage hire a company can make.

**Deploy When**: A company has both AI tools and executive buy-in but isn't seeing results. The diagnosis is almost always a missing operator.

---

## 3. AI Edge Requires Three Ingredients

**Tacit Insight**: True AI competitive advantage (the "AI Edge") only exists at the intersection of three things: proprietary knowledge that competitors don't have, proprietary data that competitors can't access, and a scale problem that would be impossibly expensive to solve manually. Remove any one of these three and you have a commodity implementation that competitors can replicate.

**Why Others Miss This**: Companies focus on "using AI better" without asking whether their AI use case creates a moat. Using ChatGPT for customer support is not an AI Edge — anyone can do it. Using your 10,000 past customer interactions to train an AI that predicts churn before it happens IS an AI Edge, because competitors would need your data to replicate it.

**Deploy When**: Companies ask "what should we use AI for?" This flips the question to "where do you have unique knowledge + unique data + a scale problem?"

---

## 4. Process Before Prompts Is Non-Negotiable

**Tacit Insight**: The most common and most expensive mistake in AI adoption is starting with the AI. "Let's try GPT for this" is the wrong first step. The correct first step is always: "Let me map the current process, document every decision point, define the quality bar at each step, and THEN determine where AI fits." This sequence change alone eliminates 80% of failed AI implementations.

**Why Others Miss This**: Prompt engineering culture encourages experimentation with tools. It's fun to play with AI. Process mapping is boring. But boring process mapping produces reliable systems, while exciting prompt experiments produce demos that never scale.

**Deploy When**: Any time someone wants to "just try AI" on something. Slow them down long enough to document the process first. The implementation will be 10x more effective.

---

## 5. The Unlimited Time Frame Unlocks Different Questions

**Tacit Insight**: Framing AI as "time-saving" leads to incremental thinking — "save 2 hours on this task." Framing AI as "unlimited time" leads to transformational thinking — "what would we do if we could personally respond to every lead, audit every customer interaction, test 1,000 content variations?" These are fundamentally different questions that produce fundamentally different implementations.

**Why Others Miss This**: "Save time" is the obvious sell. It's tangible and measurable. But it anchors thinking to existing processes. "Unlimited time" is harder to sell but opens doors to implementations that wouldn't be conceived under the time-saving frame.

**Deploy When**: Reframing a company's AI strategy from reactive ("help us do current work faster") to proactive ("help us do work we've never been able to attempt"). Especially powerful in sales conversations where the prospect is underwhelmed by AI's promise.

---

## 6. Task Hierarchy Decomposition Is the Core Skill

**Tacit Insight**: The single most valuable skill in AI operations isn't prompting — it's the ability to look at what someone calls an "Expert Task" and find the Objective or Good Enough sub-tasks hidden inside it. Every complex task contains simpler tasks that can be automated, but finding them requires a specific analytical skill that Rachel calls "decomposition." This skill is transferable across every industry and every AI tool.

**Why Others Miss This**: The AI industry focuses on prompt engineering as the core skill. But a perfectly crafted prompt pointed at the wrong task is worthless. The leverage is in task selection, not task execution.

**Deploy When**: Training anyone in AI operations. This is the foundational skill that makes everything else work.

