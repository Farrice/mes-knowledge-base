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
