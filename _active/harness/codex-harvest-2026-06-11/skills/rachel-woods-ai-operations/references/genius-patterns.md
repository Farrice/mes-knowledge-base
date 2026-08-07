# Rachel Woods — Genius Patterns

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

---

## 6. Own the Playbook, Rent the Tech

**What They Do**: Separates the durable operating method from the AI tool that runs it. Rachel treats the playbook as the asset and the tool as interchangeable infrastructure.

**Executable Behavior**:
1. Pick a repeated process that causes re-explaining, skipped planning, or generic AI output.
2. Capture the owner's method: intake questions, step order, preferences, decision rules, examples, and gotchas.
3. Convert the method into a step-by-step playbook that AI must run one step at a time.
4. Store the playbook where it can be reused: Custom GPT instructions, Claude project instructions, Copilot, an automation tool, or an SOP.
5. Add a final reflection step: "What did this run teach us that should be added back into the playbook?"

**Deploy When**: The user keeps starting from scratch in chat, correcting the same AI mistakes, or waiting for agents and tool integrations before documenting the process.

**Success Metric**: The user can say "run my playbook" and receive an output that follows their method without re-teaching the AI each time. Misses become permanent playbook updates.

---

## 7. The First Half Is Articulation

**What They Do**: Treats AI-ifying the work as the second half of the job. The first half is articulating the process clearly enough that it can be taught.

**Executable Behavior**:
1. Name the process and the outcome.
2. Break the work into research, analysis, judgment, execution, review, and handoff.
3. Define what good means at each step.
4. Capture examples, anti-examples, assumptions, and gotchas.
5. Only then choose the tool, prompt, automation, or agent.

**Deploy When**: A user wants reliable, repeatable AI output but has not mapped the human process.

**Success Metric**: The playbook can be handed to a new person or AI system and the process still runs correctly.
