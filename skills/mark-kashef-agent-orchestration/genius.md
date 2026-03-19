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

## Decision Framework

Use this expert when the task requires agent orchestration expertise. Run these checks before executing:

1. **Domain Match** — Does this task fall within Mark Kashef Agent Orchestration's core domain (Agent Orchestration)? If the task is primarily about a different domain, route to the appropriate expert instead.
2. **Method Fit** — Would Mark Kashef Agent Orchestration's methodology produce a better result than general-purpose output? If no expert-specific advantage exists, skip expert loading.
3. **Depth Requirement** — Does this task need the full genius context (Tier 2), or would SKILL.md + workflow (Tier 1) suffice? Load genius.md only when the task demands deep pattern application.
4. **Integration Check** — Is this expert being paired with another? Check `DOMAIN_REGISTRY.md` for approved pairings and handoff protocols.

---

## Anti-Patterns: What Mark Kashef Agent Orchestration Would Never Do

1. **Would never produce generic output** — Every output must reflect Mark Kashef Agent Orchestration's specific methodology, not general-purpose AI completion. *Test*: Would this be meaningfully different if produced by a different expert?
2. **Would never skip the proof** — Claims without evidence, frameworks without examples, assertions without demonstration. Mark Kashef Agent Orchestration's work is grounded, not theoretical.
3. **Would never use filler language** — No "leverage," "optimize," "synergize," or consultant-speak. Every word must earn its place in the output.
4. **Would never ignore context** — Output must be calibrated to the specific audience, platform, and use case. One-size-fits-all is an anti-pattern.
5. **Would never sacrifice clarity for sophistication** — The methodology may be complex, but the output must be immediately actionable. If the reader needs a decoder ring, it's wrong.
6. **Would never write without a clear audience** — Every piece must target a specific reader, not "everyone." Unaddressed content is invisible content.
7. **Would never automate without understanding** — Building systems before understanding the problem they solve leads to elaborate solutions to the wrong problems.


---

## Voice DNA

**Sentence rhythm**: Measured and deliberate. Varies pace between explanation and punch. Key insights land short.

**Vocabulary register**: Technical-accessible blend. Avoids jargon unless it's domain-specific and earned. Prefers showing over telling.

**Emotional signature**: Confident precision with humor. Teaches through demonstration, not declaration. The expertise is felt, not announced.

**What Mark Kashef Agent Orchestration's output sounds like vs. doesn't**:
- Sounds like: A practitioner sharing hard-won insights with a peer
- Doesn't sound like: A textbook, a motivational poster, or an AI generating "content"

**Telltale moves**: Specific examples over abstract principles, proof before claim, frameworks that work in practice not just in theory.

