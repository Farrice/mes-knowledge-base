# Mark Kashef (Claude Claw) — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

Kashef builds personal AI tools by creating the thinnest possible bridge to existing powerful systems rather than rebuilding intelligence from scratch. His architecture is defined by three biases: subprocess over API call (inherits the full harness, not just model intelligence), local-first zero-cost infrastructure, and aggressive elimination of dual-entry maintenance tax. The computer-must-be-on constraint is a feature, not a limitation — it's zero-config security.

---

## Genius Patterns (Compressed)

### GP1: The Derivative Detector
Before building anything new, audit: "Am I recreating something that already exists?" Kashef tried OpenClaw → forked → customized → stopped when he realized he'd built "a derivative of a derivative of a derivative." Bridge to existing systems instead of rebuilding. Zero dual-entry.

### GP2: The Bridge-Not-Brain Pattern
Build the thinnest possible interface layer connecting to existing infrastructure. Target: <200 lines of bridge code inheriting 100% of underlying capabilities. The instinct to "build a bot" is wrong; "bridge to what works" is right.

### GP3: Subprocess-as-Architecture
`claude subprocess` ≠ `anthropic.messages.create()`. Subprocess gives the full Claude Code harness (tools, skills, MCP servers, file system). API call gives only model intelligence. Always choose subprocess when full capability is needed remotely.

### GP4: Cost-Zero Infrastructure Bias
For every infrastructure component, ask: "Can this run locally with zero cost?" SQLite over Supabase. Local files over cloud. No third-party dependencies unless strictly necessary. Target: $0/month beyond Claude subscription.

### GP5: The Wizard Builder Pattern
Encode complex multi-step configuration as an interactive wizard (mega prompt) that interviews the user and self-builds. The prompt IS documentation + code + setup guide simultaneously. A non-technical user deploys a customized system by answering multiple-choice questions.

### GP6: Memory Decay Architecture
3-layer memory: (1) session-scoped context window, (2) SQLite with semantic + episodic stores and time-based decay, (3) pre-message context injection with aggressive dedup. Clean 10K tokens outperforms noisy 100K. Focus on signal-to-noise ratio, not window size.

### GP7: The 4-Minute-Mile Reframe
Separate existing solutions' proof-of-concept value from their architectural quality. Take the insight, discard the implementation if a simpler path exists. "OpenClaw was the 4-minute mile" — credit predecessors while transcending their structure.

### GP8: Platform-Agnostic Bridge Design
Architect in layers: (1) messaging interface, (2) media handler, (3) memory, (4) AI runtime bridge. Each independently replaceable. Swapping Telegram for WhatsApp or Claude for Codex requires changes in one layer only.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | Dual-Entry Tax — maintaining two systems sharing capabilities compounds in sync cost until you abandon one; if you're copy-pasting skills between systems, you've found the tax | Evaluating any parallel-capability architecture |
| HK2 | Subprocess > API Call — the gap between "smart responses" and "capable execution" is the harness (tools, skills, file system, CLAUDE.md) | Building any personal AI tool needing full Claude Code capability |
| HK3 | Memory Dedup > Memory Size — deduplicating noise before injection matters more than larger context windows | Designing memory injection systems |
| HK4 | Computer-must-be-on is a feature — local execution means power off = instant kill switch, zero cloud auditing, no floating API keys | Evaluating security for personal AI assistants |
| HK5 | Self-building system prompt — mega prompt serves as docs + code + setup simultaneously; for AI-built systems, the prompt IS all three | Creating replicable complex systems |
| HK6 | Session ID is the simplest persistence primitive — combined with SQLite, provides conversation persistence with near-zero complexity | Any conversational system needing context persistence |

---

## Signature Moves

1. **The Bridge-First Reflex** — When needing a new interface, immediately asks "What existing system can this bridge to?" rather than rebuilding from scratch.
2. **The Harness Call** — Defaults to spawning full `claude subprocess` instead of `anthropic.messages.create()` for remote capabilities.
3. **The Team Invocation** — Explicitly prompts "create an agent team" with defined roles to ensure collaboration, not siloed sub-agents.
4. **The Context Compressor** — Applies aggressive deduplication and noise filtering before injecting any conversation history or documents.
5. **The Wizard Prompt Architect** — Conceptualizes any complex system as a single interactive markdown prompt that guides users and self-builds.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Architectural Parsimony | New redundant components or complex dependencies | Existing components used but some duplication | Thin interface layer (<200 lines), inherits 100% of underlying capability |
| Capability Inheritance | New interface offers reduced functionality | Most core functions exposed but some logic replicated | Identical capability to core system via subprocess |
| Context Signal-to-Noise | Raw history dumped; irrelevant recall | Filtered by recency/keywords but some noise | Aggressive dedup, semantic + episodic stores, time-based decay, highly relevant context |
| Deployment Simplicity | Manual setup, external docs, complex CLI | Setup script needing user intervention | Single interactive wizard prompt; non-technical users self-deploy |
| Infrastructure Cost | Cloud services or heavyweight DBs for single-user | Minimal third-party tools | Local-first (SQLite, local files), $0/month infrastructure |
| Security Simplicity | Cloud-based auth or external API key management | Local storage with manual key management | Computer-must-be-on model: local execution, power off = kill switch, zero config |
