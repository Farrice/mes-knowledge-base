# Mark Kashef — Mastery Extraction

## Content Assessment

Source: YouTube Video (approx. 20 mins) — "7 Agent Team Use Cases"
Expert: Mark Kashef — AI Workflows & Agent Orchestration
Domain: Agentic Workflows, AI Engineering, Multi-agent Systems
Depth Tier: Standard — Highly practical, focused on 7 discrete use cases for agent teams.
Genius Patterns: 4 identified
Hidden Knowledge: 3 tacit insights detected
Existing Overlap: Mark Kashef AI Councils (COUNCIL.md / roundtable)

## Executive Summary
- **Core Genius**: Structuring complex cognitive labor into discrete, intercommunicating agent roles to produce high-value, comprehensive deliverables (pitch decks, RFPs, marketing campaigns, codebase rewrites) in a single shot.
- **What Makes Them Different**: He treats LLMs not as single processors, but as full corporate departments, explicitly programming communication protocols, dependencies, and human-in-the-loop approvals.
- **Deployable Skills**: Architecting parallel and sequential agent teams, writing deterministic orchestration prompts, building AI advisory boards.
- **Hidden Knowledge Captured**: The precise terminology to trigger team behavior, the 3-5 agent threshold for token efficiency, and hybridizing sub-agents with team agents for cost-effective execution.

## Genius Patterns

### The Directed Assembly Line (Sequential Handoff)
- **What They Do Unconsciously**: Break a massive task (e.g., Pitch Deck creation) into distinct chronological phases with strict prerequisites.
- **Executable Behavior**: Assigning singular roles (Researcher -> Slide Writer -> Designer) where Agent B cannot start until Agent A finishes and passes the payload.
- **Deployment Context**: When a task has distinct phases of research, drafting, and formatting that would dilute a single prompt's context window.
- **Success Metric**: The final agent produces the requested file without hallucinating missing research data.

### The Forced Consensus Protocol (Parallel with Synthesis)
- **What They Do Unconsciously**: Prevent homogeneous AI outputs by forcing specialized agents to debate or cross-reference before writing.
- **Executable Behavior**: Prompting parallel agents to "share their top 3 findings with the group" or "wait for all insights to be submitted to ensure no overlap" before allowing a Synthesis Lead to finalize the deliverable.
- **Deployment Context**: Multi-platform content repurposing, complex business decisions (Go/No-Go), or competitive intelligence analysis.
- **Success Metric**: A final executive brief that includes diverse perspectives, flagged overlaps, and a synthesized recommendation.

### The Human Tollbooth
- **What They Do Unconsciously**: Pause expensive computation before irreversible format generation.
- **Executable Behavior**: Explicitly prompting the team to "require plan approval from the user" before proceeding to the final build stage (e.g., generating a PPTX or a codebase).
- **Deployment Context**: Long-running generation tasks where fixing a mistake at the end takes more effort than approving an outline in the middle.
- **Success Metric**: The agent halts execution, invokes the "ask user input" tool, and waits for explicit approval.

### The Hybrid Grunt-to-Architect Pipeline
- **What They Do Unconsciously**: Use the cheapest intelligence for data gathering and the most expensive intelligence for synthesis.
- **Executable Behavior**: Deploying a fast "sub-agent" to read a codebase/repo, document its architecture, and feed that summary into the larger "Agent Team" prompt to use as the foundation for the new build.
- **Deployment Context**: Large-scale codebase analysis and rebuilding (e.g., customizing OpenHands or Claude Code).
- **Success Metric**: The agent team executes the build using the exact context provided by the sub-agent without needing to re-read the entire repo.

## Hidden Knowledge
- **The Phrase That Pays**: You MUST say "create an agent team" or "spawn an agent team." Saying "spawn agents" will result in sub-agents that work in parallel but cannot communicate with each other. Team agents speak; sub-agents are siloed.
- **The Sweet Spot**: The optimal team size is 3 to 5 agents. Exceeding this leads to over-engineering, analysis paralysis, and massive token burn (diminishing returns).
- **The Omniscient Observer**: When agent teams run, the core LLM acts as a 3rd-person observer. It can survey the outputs of the sub-agents, recognize when multiple agents pick the same angle, and unilaterally reassign angles to ensure diversity.

## Methodology
The Kashef Orchestration Protocol:
1. **Define the Objective**: What is the final deliverable?
2. **Determine the Architecture**: Is this a Sequential Assembly Line (Phase A -> Phase B) or a Parallel Synthesis (Agents A, B, C work together -> Synthesis Lead).
3. **Role Specification**: Define the exact personas involved. Do not leave the agent choice up to the LLM. Specify roles like `competitor analyst`, `financial modeler`, `devil's advocate`.
4. **Enforce Communication**: Insert explicit instructions for agents to pause and share insights before drafting.
5. **Establish the Output**: Tell the Synthesis Lead exactly how to format the final document or file.

## Applied Intelligence

### Capability Unlocks
- **[Capability 1]**: Spawning multi-agent AI advisory boards for complex business decisions (Go/No-Go models).
- **[Capability 2]**: Automating RFPs (Request for Proposal) by dedicating agents to separate sections and having a final agent compile and review for omissions.
- **[Capability 3]**: Full-campaign marketing deployment (orchestrating emails, social posts, ad variants, and landing pages from a single brief).

### System Enhancements
- These insights directly enhance the Antigravity `parallel-swarm` and `swarm` workflows, particularly the forced communication protocol and the 3-5 agent sweet spot to prevent token waste.

## Implementation Pathway
- **24-Hour Quickstart**: Test a 3-agent Sequential Assembly Line for a simple research task.
- **7-Day Sprint**: Build a full AI Advisory Board prompt for a looming business decision.
- **30-Day Integration**: Create a custom CLI/assistant by chaining sub-agent research with team-agent architecture building.
