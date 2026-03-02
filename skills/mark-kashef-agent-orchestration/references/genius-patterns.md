# Mark Kashef — Genius Patterns

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
