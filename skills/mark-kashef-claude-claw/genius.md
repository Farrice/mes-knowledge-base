# Mark Kashef: Claude Claw — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## How to Use This Skill (Model Calibration)

These patterns are architectural instincts, not a build checklist. Absorb them, then design originally — if the output stamps "Pattern 1: Derivative Detector, Pattern 2: Bridge-Not-Brain..." in labeled sequence, you have failed. The test: would Kashef recognize this as someone who instinctively eliminates a redundant layer before writing a line of code — or as someone reciting bridge-architecture terms without ever asking "can I just bridge to what already works"? If it's the second, rebuild.

Specifically:
- Do NOT enumerate which genius patterns you applied unless asked. Show the elimination; never narrate it.
- Do NOT label deliverables "here's the Bridge-Not-Brain move" or "here's the Cost-Zero Infrastructure Bias check." Execute the instinct; never announce it.
- Kashef's entire craft is a subtraction reflex. The answer to "how do I extend this system to a new platform" is almost never "build" — it's "bridge." A deliverable that proposes new intelligence, a new database, or a parallel skill set has already failed his standard before a single line is written.
- His register is engineer-plain, not evangelist. He states constraints (computer must stay on, $0/month, <200 lines of bridge code) as design decisions, not caveats to apologize for. Hedge language, disclaimers, and "best of both worlds" framing are the tell — his artifacts read like an engineer's build log, not a pitch deck. Polish is the tell-class warning: if it sounds like marketing copy for the architecture instead of the architecture itself, rebuild.

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

**Success Metric**: Remote interface has identical capability to the desktop terminal experience — the pipeline this runs through is Stage 6 of Kashef's 8-stage bridge (Messaging → Auth → Auth Gate → Media Handler → Memory Injection → Agent SDK Bridge → Response Processing → Delivery), clocking end-to-end latency of "<5 seconds for text, 30-40 seconds for video interpretation" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Methodology section).

## 4. Cost-Zero Infrastructure Bias
**What They Do**: Gravitates toward local-first, zero-cost infrastructure. SQLite over Supabase. Local files over cloud. No third-party dependencies unless strictly necessary.

**Executable Behavior**: For every infrastructure component, ask: "Can this run locally with zero cost?" Default answer should be yes for personal tools.

**Deploy When**: Building any single-user personal tool or assistant.

**Success Metric**: $0/month infrastructure cost beyond the existing Claude subscription.

## 5. The Wizard Builder Pattern
**What They Do**: Encodes complex multi-step configuration as an interactive wizard (mega prompt) that interviews the user and self-builds, rather than writing documentation or setup guides.

**Executable Behavior**: For complex setups, create a single markdown prompt that: (1) explains the system, (2) uses `ask_user` to interview for preferences, (3) builds the customized version automatically.

**Deploy When**: Any complex system that needs to be replicable or customizable for different users.

**Success Metric**: A non-technical user deploys a fully customized system by answering multiple-choice questions — the same pacing Kashef's own Implementation Pathway uses to stage the build: a "24-Hour Quickstart" (bridge + first subprocess round-trip), a "7-Day Sprint" (memory + media handler), and a "30-Day Integration" (cron scheduling, voice, second messaging platform) (source: extractions/mark-kashef-claude-claw/extraction-report.md, Implementation Pathway).

## 6. Memory Decay Architecture
**What They Do**: Designs memory with intentional decay — recent messages weighted higher, older context deprioritized. Deduplication before injection. Not infinite recall, but *relevant* recall.

**Executable Behavior**: 3-layer memory: (1) Session-scoped context window, (2) SQLite with semantic + episodic stores and time-based decay, (3) Pre-message context injection with aggressive dedup.

**Deploy When**: Any conversational system where context quality matters more than context quantity.

**Success Metric**: Assistant feels like it remembers what matters without drowning in irrelevant history — the report frames the dedup step as deduplicating "anything that seems to be noise" before each message, keeping things "fluid and buttery" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Hidden Knowledge 3).

## 7. The 4-Minute-Mile Reframe
**What They Do**: Credits predecessors for proving something is possible ("OpenClaw was the 4-minute mile") while clearly identifying their structural flaws. Doesn't dismiss — transcends.

**Executable Behavior**: When evaluating existing solutions, separate their *proof-of-concept value* from their *architectural quality*. Take the insight, discard the implementation if a simpler path exists.

**Deploy When**: Evaluating any open-source tool or framework for adoption.

**Success Metric**: You adopt the core principle while achieving dramatically simpler implementation.

## 8. Platform-Agnostic Bridge Design
**What They Do**: Designs each layer of the bridge independently swappable — messaging platform, media handler, memory system, and AI runtime are all decoupled.

**Executable Behavior**: Architect in layers: (1) messaging interface, (2) media handler, (3) memory, (4) AI runtime bridge. Each must be independently replaceable.

**Deploy When**: Any system where you want to avoid lock-in on messaging platform or AI provider — the report states the swap-target explicitly: "Telegram could be swapped for WhatsApp; Claude Code could be swapped for Codex or Gemini CLI" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Genius Pattern 8).

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
**Tacit Insight**: A mega prompt can serve as documentation AND build instructions AND interactive wizard simultaneously. Instead of creating three separate artifacts (docs, code, setup guide), compress them into a single executable document that Claude Code can read, understand, and execute. The report states this directly: the prompt IS "the architecture documentation AND the build instructions AND the interactive wizard, all compressed into one artifact" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Hidden Knowledge 5).

**Why Others Miss This**: They separate concerns by habit. Documentation goes in README. Code goes in src/. Setup goes in INSTALL.md. Kashef realized that for AI-built systems, the prompt IS all three.

**Deploy When**: Creating any complex system that needs to be replicable. The prompt should be able to produce its own implementation.

## 6. Session ID Is the Simplest Persistence Primitive
**Tacit Insight**: Instead of complex state management patterns, use a single session ID to group related messages. Combined with SQLite, this provides conversation persistence with near-zero architectural complexity. No need for Redis, no need for cloud databases, no need for state machines.

**Why Others Miss This**: They reach for heavyweight solutions first — complex state management libraries, cloud databases, message queues. A session ID column in SQLite solves 90% of persistence needs for single-user systems.

**Deploy When**: Any conversational system that needs to persist context across messages. Start with the simplest thing that works.

---

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Hall of Fame Exemplars

> These two scenarios are illustrative constructions built to demonstrate how the Genius Patterns compose together in a deliverable — they are not verbatim episodes reported by Kashef in the source material and are labeled UNCONFIRMED (constructed) in `references/source-ledger.md`. Use them to calibrate shape and rigor, not as reported case studies.

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
**Execution**: They build a separate cloud-hosted Telegram bot using a conventional API-first approach. This bot has its own set of skills and configurations, distinct from their local Claude Code setup. It uses a cloud database (e.g., Supabase) for state management — the exact tool Kashef's own infrastructure bias rejects: the report states his default plainly as "SQLite over Supabase" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Genius Pattern 4), against a target of "$0/month infrastructure cost beyond existing Claude subscription." When a new task management skill is added to their local Claude Code, they have to manually recreate and deploy it for the Telegram bot.
**What makes this mediocre**:
*   **Derivative Detector Failure**: Recreates functionality already present in the local Claude Code system.
*   **Dual-Entry Tax**: Incurs significant maintenance overhead by having two separate systems to update.
*   **Subprocess < API Call**: Relies only on model intelligence via API, missing the full harness of local tools and files.
*   **Costly Infrastructure**: Incurs ongoing cloud hosting and database costs unnecessarily.
*   **Memory Decay Architecture**: Likely uses simple, undeduplicated memory, leading to irrelevant context.

## Anti-Patterns (Sourced)

- **Never fork-and-customize an existing open-source bot before asking whether you can bridge to what already works** — Kashef's own build history is the caught failure: he "tried OpenClaw, forked it, customized it, then stopped and asked 'am I building a derivative of a derivative of a derivative?'" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Genius Pattern 1 "The Derivative Detector," file on disk since 2026-03-02).
- **Never maintain two separate skill sets that need to stay in sync** — labeled the "dual-entry tax" in the extraction report: "the ongoing cost of keeping them in sync," a cost that "is invisible until it compounds into abandonment" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Hidden Knowledge 1).
- **Never wire the bridge directly to a raw model API call when the full harness is available** — per the report's framing, "an API call gives you intelligence; a subprocess gives you capability" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Hidden Knowledge 2 "Subprocess > API Call").
- **Never default to a cloud database (Supabase, Postgres-as-a-service) for a single-user personal tool** — the report states the bias directly: "SQLite over Supabase. Local file system over cloud storage" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Genius Pattern 4 "Cost-Zero Infrastructure Bias").
- **Never inject raw, undeduplicated conversation history into the prompt** — the report describes deduplicating "anything that seems to be noise" before each message to keep things "fluid and buttery" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Hidden Knowledge 3).
- **Never split a replicable system into three separate artifacts (README + code + setup guide)** — the report frames Kashef's approach as compressing them into "the architecture documentation AND the build instructions AND the interactive wizard, all compressed into one artifact" (source: extractions/mark-kashef-claude-claw/extraction-report.md, Hidden Knowledge 5).
- **Never say "spawn agents" when the deliverable needs agents that can actually talk to each other** — VERIFIED against the raw video transcript of a companion Kashef source: "The most important magic words you always need to say is create an agent team or spawn an agent team. If you just say spawn agents, it could get confused between sub aents, which are very different in the way they work versus agent teams" [sic — "sub aents" is verbatim in the source transcript] (source: extractions/mark-kashef/transcript.txt — a different Kashef video/skill than Claude Claw itself, cited here as cross-domain corroboration, not part of the Claude Claw source material).

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
