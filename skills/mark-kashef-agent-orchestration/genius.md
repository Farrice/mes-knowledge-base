# Mark Kashef Agent Orchestration — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns

The foundational mechanics behind world-class agent coordination, devoid of generic LLM-speak. 

### The Directed Assembly Line (Sequential Handoff)
- **What it is**: An intentional chronological splitting of tasks where Agent B is blocked by Agent A. 
- **The Execution**: Break a massive task (e.g., Pitch Deck creation) into distinct roles (Researcher -> Slide Writer -> Designer). Program the prompt to refuse advancement until the previous actor passes the payload.
- **Why it works**: Prevents context dilution. A single LLM acts as the "Researcher," focusing its entire context window on data extraction before a separate instance focuses purely on formatting.

### The Forced Consensus Protocol (Parallel Synthesis)
- **What it is**: Preventing homogeneous AI outputs by explicitly forcing agents to debate, cross-reference, and compare notes.
- **The Execution**: Spawning 3-5 parallel agents on mutually exclusive tasks, with a mandate to "share their top 3 findings with the group" before writing. A Synthesis Lead agent then normalizes and aggregates the final document.
- **Why it works**: Solves the AI "yes-man" problem by instigating structural friction. The overarching system (e.g. Claude Code) acts as the arbiter, reassigning angles if 2 agents pick the same data point.

### The Human Tollbooth
- **What it is**: Pre-programmed halts in logic that freeze token consumption until human authorization.
- **The Execution**: Insert an explicit requirement: `require plan approval from the user before proceeding to the final build stage`.
- **Why it works**: Protects against compounding errors in long-running processes. Correcting a bad outline takes seconds; correcting a fully populated codebase takes thousands of tokens.

### The Hybrid Grunt-to-Architect Pipeline
- **What it is**: A cost-saving methodology using both cheap and premium intelligence correctly.
- **The Execution**: Utilize a fast "sub-agent" to read, summarize, and compress a codebase/repo. Feed that condensed summary into the prompt of the "Agent Team". 
- **Why it works**: Avoids the "bloat" of asking 5 premium team agents to all individually read the exact same source material, which wastes context window capacity.

## Hidden Knowledge

Tacit expertise regarding agent performance that must be applied to orchestration.

- **The Trigger Phrase**: You MUST explicitly say `create an agent team` or `spawn an agent team`. Simply saying `spawn agents` frequently defaults to "sub-agents." Sub-agents process in parallel but lack inter-agent communication protocols. The distinction is critical.
- **The 3-to-5 Rule (Efficiency Horizon)**: A team size of 3-to-5 agents is the sweet spot. Attempting to spawn 8+ agents immediately plummets the return on investment through over-engineering, analysis paralysis, and horrific token burn.
- **The Omniscient Observer**: When agent teams execute, the core orchestration model takes on a 3rd-person perspective (`me` / the orchestrator). It observes the team passively. If you program an objective—such as `ensure each agent writes a unique angle`—the orchestrator will independently intervene if it detects overlap, forcefully re-assigning topics to agents. You must build your prompts trusting this overarching arbiter to work.

---

## Hall of Fame Exemplars

*   **Exemplar 1: The Enterprise Pitch Deck Architect**
    *   **Prompt Snippet**: "Create an agent team to develop a comprehensive investor pitch deck for a new SaaS product. `Researcher` will gather market data and competitor analysis. `Strategist` will define the unique value proposition and business model. `Copywriter` will draft compelling slide content. `Designer` will structure the deck flow and add visual cues. Each agent *must* pass its completed output to the next in sequence. `Designer` requires full approval from `Strategist`'s section before starting."
    *   **Outcome**: A 12-slide investor deck, fully researched, strategically sound, with persuasive copy and a clear visual outline, generated in one continuous, self-correcting workflow. The `Designer` agent explicitly halted, invoked the `ask_user_input` tool, and presented the `Strategist`'s output for review before proceeding.
    *   **What makes this excellent**: This showcases "The Directed Assembly Line" (sequential handoff) and "The Human Tollbooth" perfectly. Each agent's context is pure, preventing dilution. The forced approval prevents wasted tokens on a potentially misaligned design phase.

*   **Exemplar 2: The Go/No-Go AI Advisory Board**
    *   **Prompt Snippet**: "Create an agent team of 4 expert advisors: `Market Analyst`, `Financial Modeler`, `Technical Feasibility Expert`, and `Devil's Advocate`. Their objective is to advise on a 'Go/No-Go' decision for launching a new product feature. Each advisor *must* present their top 3 findings and recommendations to the group. The `Omniscient Observer` should ensure each advisor offers a unique perspective. After all findings are shared, the `Consensus Lead` agent will synthesize a final recommendation with supporting arguments and counterpoints."
    *   **Outcome**: A concise executive summary detailing the pros and cons of the feature launch, explicitly citing the distinct findings of each advisor. The `Omniscient Observer` intervened during the initial sharing phase, re-prompting the `Market Analyst` when its findings overlapped too heavily with the `Financial Modeler`'s, forcing a divergent analysis.
    *   **What makes this excellent**: This demonstrates "The Forced Consensus Protocol" (parallel synthesis) and the power of "The Omniscient Observer." By forcing distinct perspectives and structured debate, the output avoids the common AI "groupthink" and provides a truly multi-faceted analysis.

*   **Anti-Exemplar: The Monolithic Prompt Failure**
    *   **Prompt Snippet**: "Act as a market researcher, strategist, copywriter, and designer to create a pitch deck for a new SaaS product, including market analysis, business model, slide content, and visual layout suggestions."
    *   **Outcome**: A generic, superficial pitch deck. The market analysis was thin, the strategy lacked depth, the copy was bland, and the design suggestions were vague. The single LLM struggled to maintain context for all roles, leading to shallow output across the board and "hallucinating" data points because its context window was overloaded.
    *   **What makes this mediocre**: This directly violates the principle of "The Directed Assembly Line" and "Role Specialization." It attempts to force a single, undifferentiated intelligence to perform complex, multi-stage cognitive labor, leading to context dilution and poor quality across all dimensions.

## Signature Moves

*   **Explicit Team Instantiation**: Always starts a complex task by explicitly saying `create an agent team` or `spawn an agent team` to ensure inter-agent communication protocols are active, rather than defaulting to siloed sub-agents.
    → **Deploy when**: The task requires collaborative intelligence or phased execution, not just parallel processing of independent sub-tasks.
*   **Strategic Tollbooth Insertion**: Inserts `require plan approval from the user` at critical junctures (e.g., after outline generation, before final build) to prevent compounding errors and token waste on misaligned paths.
    → **Deploy when**: The workflow has high-cost downstream steps or involves irreversible generation (e.g., code, large documents, final images).
*   **Forced Perspective Divergence**: Programs parallel agents with a mandate to `share their top X findings with the group` or `wait for all insights to be submitted to ensure no overlap` to activate the "Omniscient Observer" and prevent homogeneous outputs.
    → **Deploy when**: The goal is to generate diverse perspectives, challenge assumptions, or synthesize a robust, multi-faceted recommendation.
*   **Context Compression with Grunts**: Deploys a fast, cheaper "sub-agent" to pre-process and summarize large datasets (e.g., entire codebases, long reports) before feeding the condensed summary to the main "Agent Team."
    → **Deploy when**: The task involves ingesting a massive amount of source material that would blow out multiple premium agent context windows and incur excessive token costs.
*   **The 3-to-5 Team Sizing Rule**: Consciously limits agent teams to 3 to 5 members, resisting the urge to add more, knowing that exceeding this range leads to diminishing returns, over-engineering, and excessive token burn.
    → **Deploy when**: Designing any multi-agent workflow to optimize for efficiency, clarity, and cost-effectiveness.

## Circuit Breaker Architecture (Failure Resilience Layer)

Multi-agent pipelines fail silently. One bad agent produces plausible-looking garbage that poisons every downstream agent. The Circuit Breaker Architecture prevents cascade failures by treating every agent handoff as a potential failure point.

### Quality Tripwires (Handoff Gates)
- **What they are**: Lightweight quality checks inserted between every agent handoff in a sequential chain, or before synthesis in a parallel chain.
- **Three checks per tripwire**: (1) Output meets minimum density threshold for the role — a Researcher who returns 2 sentences tripped. (2) Output references the input payload — detects hallucinated pivots where an agent ignores its input and generates from training data. (3) Transformation check — output must meaningfully differ from input, catching agents that just reformatted without adding value.
- **Deploy when**: Any sequential handoff or before a Synthesis Lead aggregates parallel outputs.

### Fallback Paths (Graceful Degradation)
- **What they are**: Pre-planned alternative routes when an agent trips a quality tripwire.
- **The Execution**: On first trip — re-prompt the same agent with a tighter constraint and explicit correction ("Your output lacked X, regenerate focusing on Y"). On second trip — spawn a replacement agent with a different angle prompt using the same upstream payload. On third trip — insert an emergency Human Tollbooth ("Agent [role] has failed twice; here is the best attempt — should we proceed, redirect, or abort?").
- **Why it works**: Prevents the two worst outcomes: (a) garbage flowing downstream unchecked, and (b) entire pipeline restart from scratch when only one agent failed.

### Blast Radius Containment (Checkpoint Caching)
- **What it is**: Caching each successful agent's output as a checkpoint, so failures downstream never require restarting the entire pipeline.
- **The Execution**: After each agent passes its quality tripwire, the orchestrator stores that output as a named checkpoint (e.g., `checkpoint_researcher`, `checkpoint_strategist`). If Agent 3 fails, recovery starts from `checkpoint_agent2`, not from the original input.
- **Why it works**: In a 5-agent pipeline, a failure at Agent 4 without checkpoints wastes all work from Agents 1-3. With checkpoints, you only re-run from the last good state.

### Degradation Signals (Pipeline Health Monitor)
- **What they are**: A running confidence score tracked by the Omniscient Observer across the entire pipeline.
- **The Execution**: Each quality tripwire reports PASS (no issues), WARN (marginal quality, passed but flagged), or FAIL (tripped). Two consecutive WARNs automatically insert a Human Tollbooth before the next agent engages. Any FAIL triggers the Fallback Path. The orchestrator surfaces the confidence trajectory to the user at the final Tollbooth: "Pipeline health: 4/5 PASS, 1 WARN at Strategist stage."
- **Why it works**: Makes invisible quality erosion visible. Without this, a pipeline can produce a 6/10 deliverable where every agent was individually 7/10 but small losses compounded.

## Quality Rubric

> Detailed scoring rubric: `references/quality-rubric.md` — load on-demand for grading.

---

### Patterns from claude.ai export — Mark Kashef conversations (2026-07-01)

*Source: transcript-grounded extraction conversations (Claude Code Masterclass "One-Person Company," AI Council subagents, model-card mastery, prompt-factory, solo AI consulting). Deduplicated against the full mark-kashef-* family — only net-new methodology below.*

#### Pattern: The Core Agent Rule (Agent Unification)
**Execute**: Stop designing agents as mutually exclusive corporate roles (UI designer, code reviewer, security auditor) — separate prompts with separate tools develop misaligned goals and contradict each other. Instead, take ONE task ("make the front end better"), split it into perspectives on that same task (color/hex lens, UX-structure lens, feature-expansion lens), generate each agent per-project (not from a generic role library), then fire one unified prompt: "invoke all of our agents to take X to the next level." Each agent keeps its own context window but shares the same incentive.
**Success Metric**: Agent outputs compose without contradiction — "soldiers under one unified army instead of fighting different wars." Bonus signal: agents surface unrequested-but-aligned improvements (e.g., keyboard shortcuts nobody asked for) because the shared objective, not the role card, is driving.

#### Pattern: Phase-Gated Development with External State Trackers
**Execute**: In plan mode, force the plan into logical phases with a cutoff where each phase can stand alone. Have Claude create a tracker markdown file with checkboxes per phase plus acceptance criteria, and commit a rule to project memory: "always stop after completing a phase and ask approval before the next." After each completed phase: run `/context` to check headroom, then `/clear` and re-anchor the fresh session by tagging ONLY the tracker file ("execute phase 2"). The tracker file — not the conversation — is the project's state.
**Success Metric**: No session ever crosses into compaction; every phase starts at ~85%+ free context. Correcting course costs one phase, never the whole build.

#### Pattern: Multi-Modal Token Routing
**Execute**: Route work across the three Claude surfaces by token value. Claude.ai chat = purely conceptual back-and-forth (subscription-cheap). Claude Code web = planning, brainstorming, PRDs, surface-level/aesthetic edits, and parallel micro-tasks that can run asynchronously from mobile (security scan + UI audit + PRD simultaneously). CLI = the "meatiest" build-and-iterate work only. Teleport web results back to the CLI (open-in-CLI button) when they're ready for real implementation; use branches/PRs so parallel web tasks never merge to production unreviewed.
**Success Metric**: Premium CLI tokens are spent only on high-value iteration; idle time (mobile, downtime) still advances the project through web micro-agents.

#### Pattern: Replicate-Anything Capability Transfer (Frontend Skill Extraction)
**Execute**: When claude.ai's front end has a capability Claude Code lacks (e.g., PPTX/DOCX/XLSX creation via its hidden skill files), run the task on the front end once, then ask it: "Recreate everything you had to do — every bash command, every mistake, every lesson learned — as a complete guide teaching another AI agent how to replicate what you did." Drag the guide + output artifacts + generated scripts into a fresh Claude Code repo, `/init` to upskill it, then one-shot future requests with a one-line prompt.
**Success Metric**: A capability that timed out and restarted-from-scratch on the front end becomes a repeatable one-shot command center in Claude Code — failures included in the guide are what make the transfer stick.

#### Pattern: Documentation Injection (Zero-Error API Onboarding)
**Execute**: For any new API/model/service, never let Claude work from training memory. Grab the official docs page as markdown (most doc sites have an "open as markdown" dropdown), paste into a repo file, `/init`, and prefix the build instruction with: "Use the following exactly as I'm telling you — this is the exact documentation. You're not aware of it because your training ended; this is a much newer API." Cheat-code variant: one-shot a working scaffold in the provider's playground (e.g., AI Studio auto-injects its own API docs), download as zip, drop into the repo, and tell Claude Code "recreate a better version of this."
**Success Metric**: First-attempt working integration — no deep-research detours, no deprecated-SDK code, no "hundreds of messages to reach the same point."

#### Pattern: The Codebase Inventory Map
**Execute**: For large codebases where `/init` would flood the context window, have Claude produce a separate inventory markdown: every folder/file, what functionality it correlates to, dependencies, in plain English ("assume I'm not a developer"). Then scope every future change: point plan mode at the inventory, tell it to ignore everything outside the relevant domain, and make pinpoint changes without ramming the codebase into context. CLAUDE.md carries the rules; the inventory carries the map.
**Success Metric**: Surgical edits in million-line codebases without full-repo context loads; a persistent artifact you carry into any session.

#### Pattern: Model-Card Dialect Migration
**Execute**: When a new model drops, skip tutorials and Discord — download the model/system cards for your current and target model and run the 5-part migration prompt: (1) the 3-5 differences that actually affect prompts (context handling, formatting preferences, capability gaps), (2) specific prompt fixes — words, structure, gotchas, (3) three before/after examples (basic task, complex multi-step, edge case), (4) a migration checklist, (5) "here's my actual prompt — convert it AND explain why you changed what you changed." Dialect anchors: Claude models keep rewarding XML; GPT reasoning models need markdown less than non-reasoning ones.
**Success Metric**: Under 10 minutes from model release to migrated, tested prompts. Caveat baked in: front-end behavior ≠ API behavior (hidden system prompts) — always retest in the deployment surface.

#### Pattern: Research → Mega-Guide → Prompt Factory
**Execute**: Three-stage compounding: (1) deep research on the latest prompting techniques for the target modalities (image, video, voice, text, agents); (2) "act as a prompt engineer and turn this research into a mega guide as if teaching another AI to master prompt engineering for these modalities" — one markdown file; (3) drop the guide into a Claude Code repo, `/init`, go into plan mode, and give a business-context mega prompt: generate a complete suite of production-ready prompts tailored to THIS business, organized in a folder structure per modality, prioritized with justifications. Claude decides which prompts the business needs — you never enumerate them.
**Success Metric**: A tailored, versioned prompt library (dozens of production prompts across modalities) from one business description — the "zero to 60%" asset that replaces generic sold prompt-packs.

#### Insight: Files Are Truth, Not Claims
Claude will tell you a plugin/MCP/setting is installed when it isn't — sometimes three to five times in a row. The verification standard is physical file state: `settings.local.json` for plugins and permissions, a hand-created `MCP.json` for servers. "When you see it hardcoded in the file, it's not lying to you."
**Deploy**: After ANY install/config claim, tag the settings file and confirm the entry exists before restarting the session. To install an MCP server, skip the ask-Claude dance entirely: create `MCP.json` yourself, paste researched documentation payload, save, new session — detected on the spot.

#### Insight: The 40-50% Quality Cliff (Hallucination Nation)
Claude visibly loses focus at ~40-50% context consumption, well before compaction — and compaction itself is non-deterministic about what it keeps ("where AI slop is born"). Most users blame the model for degradation they caused by treating Claude Code like a chatbot.
**Deploy**: Treat 50% used as the action threshold, not 90%. Prefer `/clear` + external-tracker re-anchor over `/compact`; only compact when a tracker file exists to backstop what the summary drops. Prune unused MCP servers and keep CLAUDE.md lean — a 15K-token CLAUDE.md "nukes your context every single time" and its instructions stop being followed.

#### Insight: `#` Is Session Memory vs. Command Center Memory
Corrections given mid-conversation ("no, you got this wrong") persist only in the session. Prefixing an instruction with `#` writes it into CLAUDE.md — permanent, every future session. Most users never learn the difference and re-teach the same rules forever.
**Deploy**: The moment a correction feels like a rule ("always stop after each phase," "never use periods, keep it informal"), `#` it into the command center. Judgment call each time: session-worthy or perpetuity-worthy.

#### Insight: Plan-Mode Insurance (The "Are You Sure" Rule)
A CLAUDE.md mandate — "if I'm not in plan mode and the instruction isn't trivially clear, push back with clarifying questions before executing; if I've articulated it fully, just execute" — acts as a last line of defense against frustrated, lazy, or destructive instructions ("nuke the whole app" → clarifying questions instead of deletion).
**Deploy**: Add it once per project. Pair with `/rewind` knowledge: rewind isn't just undo — it's for features built "99% right but 100% wrong structurally," where you redo the instruction WITH the newfound knowledge instead of patching a bad foundation.

#### Insight: Graceful Shutdown Is Part of the Skill
Agent teams left running after the deliverable quietly burn tokens — a forgotten squad idled overnight cost 10-20K tokens doing nothing. And the moment you send the same spawn prompt twice, it should stop being a prompt.
**Deploy**: Any recurring agent-team spawn gets promoted to a skill/slash command with the full lifecycle baked in: clarifying questions → spawn → dispatch on approval → present findings → graceful shutdown. Shutdown is a required step, not hygiene.

#### Insight: AI Is a Luxury, Not a Right (Operator Layer)
Businesses fail with AI because they use it as a solution looking for a problem. Kashef's consulting sequence: fix the business problem first (data integrity, unmaintained CRMs, undefined processes), THEN apply AI where a proper use case exists. The one-person-company advantage isn't building automations — knowledge is commoditizing; it's advising on sequencing: which automation takes precedence, where guardrails/fallbacks go, what stays human-in-the-loop.
**Deploy**: Before spinning up any agent pipeline for a business outcome, run the two-question gate: (a) does the underlying problem actually exist, (b) is AI the best-suited fix — and price your value on the sequencing judgment, not the build.
