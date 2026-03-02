# Mark Kashef — Hidden Knowledge

Tacit expertise regarding agent performance that must be applied to orchestration.

- **The Trigger Phrase**: You MUST explicitly say `create an agent team` or `spawn an agent team`. Simply saying `spawn agents` frequently defaults to "sub-agents." Sub-agents process in parallel but lack inter-agent communication protocols. The distinction is critical.
- **The 3-to-5 Rule (Efficiency Horizon)**: A team size of 3-to-5 agents is the sweet spot. Attempting to spawn 8+ agents immediately plummets the return on investment through over-engineering, analysis paralysis, and horrific token burn.
- **The Omniscient Observer**: When agent teams execute, the core orchestration model takes on a 3rd-person perspective (`me` / the orchestrator). It observes the team passively. If you program an objective—such as `ensure each agent writes a unique angle`—the orchestrator will independently intervene if it detects overlap, forcefully re-assigning topics to agents. You must build your prompts trusting this overarching arbiter to work.
