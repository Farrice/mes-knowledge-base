# Mark Kashef: Claude Claw — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns

## 1. The Derivative Detector
**What They Do**: Immediately recognizes when layered abstractions add maintenance cost without proportional capability gain. Tried OpenClaw → forked it → customized it → stopped when he realized he'd built "a derivative of a derivative of a derivative."

**Executable Behavior**: Before building anything new, audit: "Am I recreating something that already exists in a working system? Can I bridge to it instead of rebuilding it?"

**Deploy When**: Any system design where you're about to build a second version of existing functionality — especially when extending an AI system to a new interface.

**Success Metric**: Zero dual-entry. Changes in one place propagate everywhere automatically.

## 2. The Bridge-Not-Brain Pattern
**What They Do**: Defaults to creating thin interface layers that connect to existing powerful systems rather than building new intelligent systems from scratch.

**Executable Behavior**: When you need a new access point (mobile, messaging, voice), build the thinnest possible bridge to existing infrastructure. Target: <200 lines of bridge code that inherits 100% of underlying capabilities.

**Deploy When**: Extending any existing AI system to new platforms. The instinct to "build a bot" is wrong — the instinct to "bridge to what works" is right.

**Success Metric**: The bridge adds minimal code and inherits all underlying capabilities without modification.

## 3. Subprocess-as-Architecture
**What They Do**: Uses process spawning as the primary architectural primitive. A subprocess gives you the full Claude Code harness (tools, skills, MCP servers, file system). An API call gives you only model intelligence.

**Executable Behavior**: Use Agent SDK subprocess spawning instead of direct API calls. `claude subprocess` ≠ `anthropic.messages.create()`. The former gives you an entire operating environment; the latter gives you a chat completion.

**Deploy When**: Any time you need Claude Code's full capability remotely, not just model intelligence.

**Success Metric**: Remote interface has identical capability to the desktop terminal experience.

## 4. Cost-Zero Infrastructure Bias
**What They Do**: Gravitates toward local-first, zero-cost infrastructure. SQLite over Supabase. Local files over cloud. No third-party dependencies unless strictly necessary.

**Executable Behavior**: For every infrastructure component, ask: "Can this run locally with zero cost?" Default answer should be yes for personal tools.

**Deploy When**: Building any single-user personal tool or assistant.

**Success Metric**: $0/month infrastructure cost beyond the existing Claude subscription.

## 5. The Wizard Builder Pattern
**What They Do**: Encodes complex multi-step configuration as an interactive wizard (mega prompt) that interviews the user and self-builds, rather than writing documentation or setup guides.

**Executable Behavior**: For complex setups, create a single markdown prompt that: (1) explains the system, (2) uses `ask_user` to interview for preferences, (3) builds the customized version automatically.

**Deploy When**: Any complex system that needs to be replicable or customizable for different users.

**Success Metric**: A non-technical user deploys a fully customized system by answering multiple-choice questions.

## 6. Memory Decay Architecture
**What They Do**: Designs memory with intentional decay — recent messages weighted higher, older context deprioritized. Deduplication before injection. Not infinite recall, but *relevant* recall.

**Executable Behavior**: 3-layer memory: (1) Session-scoped context window, (2) SQLite with semantic + episodic stores and time-based decay, (3) Pre-message context injection with aggressive dedup.

**Deploy When**: Any conversational system where context quality matters more than context quantity.

**Success Metric**: Assistant feels like it remembers what matters without drowning in irrelevant history.

## 7. The 4-Minute-Mile Reframe
**What They Do**: Credits predecessors for proving something is possible ("OpenClaw was the 4-minute mile") while clearly identifying their structural flaws. Doesn't dismiss — transcends.

**Executable Behavior**: When evaluating existing solutions, separate their *proof-of-concept value* from their *architectural quality*. Take the insight, discard the implementation if a simpler path exists.

**Deploy When**: Evaluating any open-source tool or framework for adoption.

**Success Metric**: You adopt the core principle while achieving dramatically simpler implementation.

## 8. Platform-Agnostic Bridge Design
**What They Do**: Designs each layer of the bridge independently swappable — messaging platform, media handler, memory system, and AI runtime are all decoupled.

**Executable Behavior**: Architect in layers: (1) messaging interface, (2) media handler, (3) memory, (4) AI runtime bridge. Each must be independently replaceable.

**Deploy When**: Any system where you want to avoid lock-in on messaging platform or AI provider.

**Success Metric**: Swapping Telegram for WhatsApp or Claude for Codex requires changes in one layer only.

## Hidden Knowledge

## 1. The Dual-Entry Tax
**Tacit Insight**: Every time you maintain two separate systems that share capabilities (desktop skills + mobile bot skills), you pay an invisible "dual-entry tax" — the ongoing cost of keeping them in sync. This cost compounds until you abandon one system.

**Why Others Miss This**: They see the initial setup cost of building a second system but not the maintenance compounding. Kashef experienced the full cycle: build → customize → maintain → realize it's unsustainable.

**Deploy When**: Evaluating any architecture that requires parallel capability sets. If you're about to copy-paste a skill or config from System A to System B, you've found the tax.

## 2. Subprocess > API Call
**Tacit Insight**: Spawning a Claude Code subprocess gives you the full *harness* (tools, skills, file system, MCP servers, CLAUDE.md). An API call gives you only model intelligence. The gap between "smart responses" and "capable execution" is the harness.

**Why Others Miss This**: API-first thinking dominates. Developers default to `anthropic.messages.create()` because that's how cloud services work. The subprocess pattern feels unconventional but is architecturally superior for personal tools because it inherits everything.

**Deploy When**: Building any personal AI tool where you need full Claude Code capability, not just conversational intelligence.

## 3. Memory Dedup > Memory Size
**Tacit Insight**: Before injecting conversation context, deduplicating noise matters more than having a larger context window. Clean 10K tokens of relevant context outperforms noisy 100K tokens.

**Why Others Miss This**: The industry obsesses over context window size. Kashef focuses on context window *signal-to-noise ratio*. His system deduplicates "anything that seems to be noise" before each message.

**Deploy When**: Designing any memory injection system. Always ask "is this context helping or diluting?"

## 4. The Computer-Must-Be-On Constraint Is a Feature
**Tacit Insight**: Requiring your computer to be on isn't a limitation — it's the simplest security model. Your AI has access to your files, skills, and tools ONLY when your machine runs. Power off = instant kill switch. No cloud service to audit, no API keys floating in the ether.

**Why Others Miss This**: They frame "computer must be on" as a downside vs. cloud deployment. Kashef frames it as zero-config security that requires zero maintenance.

**Deploy When**: Evaluating security for personal AI assistants. The question isn't "how do I keep this secure in the cloud" but "do I even need the cloud?"

## 5. The Self-Building System Prompt
**Tacit Insight**: A mega prompt can serve as documentation AND build instructions AND interactive wizard simultaneously. Instead of creating three separate artifacts (docs, code, setup guide), compress them into a single executable document that Claude Code can read, understand, and execute.

**Why Others Miss This**: They separate concerns by habit. Documentation goes in README. Code goes in src/. Setup goes in INSTALL.md. Kashef realized that for AI-built systems, the prompt IS all three.

**Deploy When**: Creating any complex system that needs to be replicable. The prompt should be able to produce its own implementation.

## 6. Session ID Is the Simplest Persistence Primitive
**Tacit Insight**: Instead of complex state management patterns, use a single session ID to group related messages. Combined with SQLite, this provides conversation persistence with near-zero architectural complexity. No need for Redis, no need for cloud databases, no need for state machines.

**Why Others Miss This**: They reach for heavyweight solutions first — complex state management libraries, cloud databases, message queues. A session ID column in SQLite solves 90% of persistence needs for single-user systems.

**Deploy When**: Any conversational system that needs to persist context across messages. Start with the simplest thing that works.

---

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Hall of Fame Exemplars

### 1. The "Custom Claude Code CLI" Self-Builder
**Scenario**: A user wants a custom CLI tool that integrates deeply with their local file system, runs complex Python scripts, and leverages specific Claude Code skills, but needs it to be easily deployable and configurable for different projects.
**Execution**: Mark architects a single, comprehensive markdown prompt. This prompt first explains the purpose of the CLI, then uses `ask_user` in a wizard-like fashion to gather project-specific details (e.g., target directories, preferred coding styles, specific tool integrations). Based on these inputs, an "Agent Team" (3-5 agents) is spawned: a "Configurator Agent" that writes the initial setup files, a "Skill Architect Agent" that integrates relevant Claude Code skills, and a "Test & Validate Agent" that runs initial checks. This team leverages `claude subprocess` calls to execute file system operations and install dependencies locally.
**What makes this excellent**:
*   **Wizard Builder Pattern**: The entire complex setup is contained within a self-executing prompt, making it accessible to non-technical users.
*   **Subprocess-as-Architecture**: Full Claude Code capabilities (file system, skills) are leveraged for the build, not just model intelligence.
*   **Cost-Zero Infrastructure Bias**: The resulting CLI is local-first, requires no external cloud infrastructure, and is free to run beyond Claude usage.
*   **Agent Team Cohesion**: The agent team works in concert, with specific roles, to produce a complete, functional system.

### 2. The "Cross-Platform AI Assistant Bridge"
**Scenario**: A user has a powerful Claude Code-based personal assistant running on their desktop, managing tasks, documents, and code. They want to extend its capabilities to Telegram and Discord without rebuilding any logic or duplicating skills.
**Execution**: Mark designs a thin "Bridge" architecture. This involves creating separate, lightweight Python scripts (<200 lines each) for Telegram and Discord. These scripts are strictly responsible for parsing incoming messages, formatting them for the core Claude Code system, and sending back responses. Crucially, they use `claude subprocess` to invoke the *exact same* Claude Code instance and its skills that the desktop app uses. Any changes or new skills added on the desktop are immediately available through Telegram and Discord. Memory is managed centrally using a shared SQLite database with session IDs.
**What makes this excellent**:
*   **Bridge-Not-Brain Pattern**: No new "bot intelligence" is built; existing capabilities are simply exposed.
*   **Platform-Agnostic Bridge Design**: Each messaging platform is an independently swappable layer.
*   **Subprocess > API Call**: The full Claude Code harness is utilized, ensuring identical capability across all interfaces.
*   **Cost-Zero Infrastructure Bias**: Local SQLite for memory, local subprocess calls, minimal external dependencies.
*   **Hidden Knowledge: Dual-Entry Tax Avoidance**: Zero duplication of skills or configuration across platforms.

### Anti-Exemplar: The "Monolithic Cloud Bot"
**Scenario**: A developer wants a Telegram bot that can manage their tasks and interact with their code.
**Execution**: They build a separate cloud-hosted Telegram bot using a conventional API-first approach. This bot has its own set of skills and configurations, distinct from their local Claude Code setup. It uses a cloud database (e.g., Supabase) for state management. When a new task management skill is added to their local Claude Code, they have to manually recreate and deploy it for the Telegram bot.
**What makes this mediocre**:
*   **Derivative Detector Failure**: Recreates functionality already present in the local Claude Code system.
*   **Dual-Entry Tax**: Incurs significant maintenance overhead by having two separate systems to update.
*   **Subprocess < API Call**: Relies only on model intelligence via API, missing the full harness of local tools and files.
*   **Costly Infrastructure**: Incurs ongoing cloud hosting and database costs unnecessarily.
*   **Memory Decay Architecture**: Likely uses simple, undeduplicated memory, leading to irrelevant context.

## Signature Moves

*   **The Bridge-First Reflex**: When presented with a need for a new interface or platform, immediately asks, "What existing system can this *bridge* to, rather than rebuilding from scratch?" → **Deploy when**: Extending an existing AI system to a new frontend (e.g., mobile, web, messaging).
*   **The Harness Call**: When any remote or extended capability is needed, defaults to spawning a full `claude subprocess` instead of making a direct `anthropic.messages.create()` API call. → **Deploy when**: Any time the full power of Claude Code (tools, file system, MCP servers, CLAUDE.md) is required remotely.
*   **The Team Invocation**: To ensure agents collaborate and communicate, explicitly prompts the LLM to "create an agent team" with defined roles, rather than simply instructing it to "spawn agents" or "use multiple agents." → **Deploy when**: Orchestrating complex tasks requiring specialized, intercommunicating AI personas.
*   **The Context Compressor**: Before injecting conversation history or external documents into the prompt, reflexively applies aggressive deduplication and filters out anything that appears to be noise or redundant. → **Deploy when**: Managing context for any conversational or document-processing AI system to maintain high signal-to-noise ratio.
*   **The Wizard Prompt Architect**: For any system or workflow that requires custom configuration or setup, immediately conceptualizes it as a single, interactive markdown prompt that guides the user and self-builds the system. → **Deploy when**: Designing replicable, customizable, or complex AI systems for varied users.

## Expert-Specific Quality Rubric

| Criterion                      | Score 4 (Acceptable)                                          | Score 7 (Good)                                                               | Score 10 (Savant)                                                                     |
| :----------------------------- | :------------------------------------------------------------ | :--------------------------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| **Architectural Parsimony**      | Introduces new, redundant components or complex dependencies.  | Uses existing components but might have some duplicated functionality.       | Thin interface layer (<200 lines), inherits 100% of underlying capability.            |
| **Capability Inheritance**       | New interface offers significantly reduced functionality compared to the core system. | Exposes most core functions but requires some replication of logic.            | New interface provides *identical* capability to the core system via subprocess.      |
| **Agent Team Cohesion & Output** | Agents work in parallel but outputs are repetitive, lack synthesis, or show token waste. | Agents communicate, but distribution of tasks or token efficiency could be improved. | Optimal 3-5 agents with distinct roles, explicit communication, forced consensus, diverse, and token-efficient output. |
| **Context Signal-to-Noise**      | Dumps raw conversation history, leading to irrelevant or redundant recall. | Filters context by recency or basic keywords, but some noise persists.        | Aggressive deduplication, semantic + episodic stores, time-based decay, highly relevant context. |
| **Deployment Simplicity**        | Requires manual setup, external documentation, or complex CLI commands. | Provides a setup script, but still needs user intervention or technical knowledge. | A single, interactive wizard prompt guides non-technical users to self-deploy a customized system. |
| **Infrastructure Cost Bias**     | Integrates cloud services or heavyweight databases for single-user needs. | Uses minimal third-party tools, but could achieve lower cost.                 | Local-first (SQLite, local files), zero external dependencies, $0/month infrastructure cost. |
| **Security Model Simplicity**    | Relies on cloud-based authentication or external API key management. | Uses local storage but requires manual key management or access control.       | "Computer-must-be-on" model: local execution, power off = instant kill switch, zero config security. |
