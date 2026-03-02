---
description: Convene an AI expert roundtable — auto-selects 3-5 agents to analyze a topic from multiple perspectives and produce consensus recommendations
---

# `/roundtable` — AI Expert Roundtable

Assemble 3-5 expert agents for a structured discussion on any topic. Produces a roundtable artifact with each expert's analysis and prioritized recommendations.

---

## Steps

### 1. Capture the Topic

Ask the user (if not already provided):
> "What topic or question should the roundtable address?"

The user may also specify particular agents. If not, proceed to auto-selection.

### 2. Auto-Select Experts (Default: 3-5 Agents)

Read `AGENT_INDEX.md` (or the agent table in `GEMINI.md`) and select the **3-5 most relevant agents** based on:
- Domain match to the topic
- Complementary perspectives (avoid redundancy)
- At least one contrarian or cross-domain thinker (e.g., Jim O'Shaughnessy, Oren, Mark Kashef)

Present the panel to the user for approval:
```
## 🎙️ Roundtable Panel

**Topic**: [topic]

| Seat | Expert | Why They're Here |
|------|--------|------------------|
| 1 | [Agent] | [1-line reason] |
| 2 | [Agent] | [1-line reason] |
| 3 | [Agent] | [1-line reason] |
| 4 | [Agent] | [1-line reason] |

➡️ **Proceed with this panel?** Or swap/add anyone?
```

Wait for user confirmation before proceeding.

### 3. Load Each Expert

For each selected agent:
1. Read `agents/[agent-name]/AGENT.md` — persona, decision framework, communication style
2. Read `agents/[agent-name]/memory/context.md` — persistent project context
3. If the agent has a relevant skill, also read `skills/[skill-name]/SKILL.md`

### 4. Run the Roundtable

Produce a structured roundtable artifact with the following format:

```markdown
# 🎙️ AI Expert Roundtable: [Topic]

**Date**: [date]
**Panel**: [Agent 1], [Agent 2], [Agent 3], [Agent 4]

---

## Opening Positions

### [Agent 1 Name] — [Agent Title/Domain]
> [2-4 paragraphs in the agent's voice. Their initial take on the topic, applying their specific framework and expertise. Should feel distinct from every other panelist.]

### [Agent 2 Name] — [Agent Title/Domain]
> [Same format, different perspective]

[...repeat for all panelists]

---

## Cross-Examination

Where the experts challenge, build on, or disagree with each other's positions. This section should surface genuine tension and complementary insights — NOT artificial agreement.

---

## Consensus Recommendations

Synthesize into a prioritized list:

| # | Recommendation | Effort | Impact | Champion |
|---|---------------|--------|--------|----------|
| 1 | [Rec] | [Low/Med/High] | [Low/Med/High] | [Which agent owns this idea] |
| 2 | [Rec] | ... | ... | ... |

---

## Dissenting Views

Any expert positions that did NOT make the consensus but are worth preserving for future consideration.

---

## Next Steps

Concrete, actionable items the user can take immediately.
```

### 5. Save the Artifact

Save the roundtable output to the conversation's brain artifacts directory as `roundtable.md`.

### 6. Debrief

Present a brief summary to the user highlighting:
- The top 3 recommendations
- Any surprising disagreements
- Suggested next workflow to run (e.g., `/deploy-skill`, `/brief`, `/swarm`)
