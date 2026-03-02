# Mark Kashef — Claude Claw Hidden Knowledge

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
