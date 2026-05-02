---
name: Persona Audit
command: /mcclain-persona-audit
expert: Corey McClain
category: Practitioner
description: Audit existing agents for persona layer quality — diagnose generic vs. distinct outputs
inputs: Existing agent outputs (3-5 samples), agent configuration files
outputs: Scored audit with specific upgrade prescriptions
---

# Persona Audit

Diagnose whether an existing agent is producing at the default floor or at a persona-elevated level. This audit identifies the specific gaps in the persona layer (or its absence) and prescribes targeted upgrades. Based on Corey's observation that AI "always gives you a response that's just good enough — it's never going to try to give you the best answer."

## Workflow

### Step 1 — Output Sample Collection

Gather 3-5 recent outputs from the agent across different task types:
- A standard/routine task
- A creative/judgment task
- A task requiring audience awareness
- (Optional) A task where the output was disappointing

### Step 2 — Vanilla Comparison

For at least one output, generate a vanilla version:
1. Take the same task
2. Run it with no persona, no custom instructions — just the raw model
3. Compare side by side

**Key question**: Can you tell which output came from your agent and which came from vanilla? If not, the persona layer is absent or ineffective.

### Step 3 — Seven-Point Audit

Score the agent's outputs (1-10 each):

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **Distinction** — Could you identify this agent's output in a blind test? | | |
| **Voice Consistency** — Do outputs sound like the same person across tasks? | | |
| **Worldview Presence** — Do outputs reflect specific beliefs and values? | | |
| **Taste Level** — Is the output selling or stating? (Prada Principle) | | |
| **Human Texture** — Does the output feel human or template-generated? | | |
| **Audience Alignment** — Does the output resonate with the intended audience? | | |
| **Anti-Default** — Is the output clearly above the model's default floor? | | |

**Composite Score**: Sum / 70. Below 40% = no effective persona. 40-60% = thin persona. 60-80% = functional persona. 80%+ = strong persona.

### Step 4 — Gap Diagnosis

Based on scores, identify which persona components need work:

| Low Score | Missing Component | Fix |
|-----------|------------------|-----|
| Distinction < 5 | No persona installed or persona is too generic | `/mcclain-persona-forge` — build from scratch |
| Voice < 5 | No voice specification | `/mcclain-voice-texture` — design voice layer |
| Worldview < 5 | No worldview beliefs | `/mcclain-worldview-container` — construct belief system |
| Taste < 5 | Worldview lacks sophistication | Deepen worldview with quality standards and aesthetic convictions |
| Human Texture < 5 | No messy details in backstory | `/mcclain-backstory-engine` — add formation narrative and daily life |
| Audience Alignment < 5 | Worldview not reverse-engineered from audience | Redesign worldview using audience posture data |
| Anti-Default < 5 | Persona is too thin to shift model behavior | Expand all persona components — more depth across the board |

### Step 5 — Upgrade Prescription

Write the specific upgrade plan:
1. What's the biggest gap? (Fix this first — it has the highest leverage)
2. What's the specific action? (Link to the relevant workflow)
3. What's the expected quality improvement?
4. How will you validate the improvement? (A/B test protocol)

### Step 6 — Post-Upgrade Validation

After implementing upgrades:
1. Run the same 3-5 tasks that generated the original samples
2. Re-score using the same 7-point audit
3. Compare composite scores — improvement should be visible
4. If improvement is < 10 percentage points, the upgrade was too surface-level — go deeper

---

## Quality Gate

- [ ] 3-5 output samples were evaluated
- [ ] At least 1 vanilla comparison was run
- [ ] All 7 criteria were scored with evidence
- [ ] Gap diagnosis maps low scores to specific missing components
- [ ] Upgrade prescription includes specific workflows and validation plan
