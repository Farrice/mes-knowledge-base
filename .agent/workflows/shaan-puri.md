---
description: "Shaan Puri expert front door with decision-first story deployment and conditional methodology loading."
---

# /shaan-puri — Shaan Puri Expert Front Door

1. Start with `.agent/workflows/shaan-story-deploy.md`.
2. Do not load the Shaan persona or genius context until the router selects a Shaan production route.
3. When selected, load `agents/shaan-puri/AGENT.md`, `skills/shaan-puri-storytelling/SKILL.md`, and only the context named by the chosen workflow.
4. If the router selects an external or no-story owner, use that owner and keep Shaan bounded to the selected frame, specificity, pacing, or no contribution.
5. Preserve the router's truth constraints through delivery.
