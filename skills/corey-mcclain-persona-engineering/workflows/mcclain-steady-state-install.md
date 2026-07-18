---
name: Steady-State Install
command: /mcclain-steady-state-install
expert: Corey McClain
category: Practitioner
description: Persistent workspace persona deployment — the compound-over-time method
inputs: Tested persona (from transistory install or persona forge), workspace/project environment
outputs: Installed persona file with router integration, compounding over time
---

# Steady-State Install

Deploy a persona as a persistent workspace installation that compounds over time. This is the long-game — the persona gets better with every conversation as memory accumulates, refinements are made, and the document evolves. This is how Corey's agents maintain quality consistency across sessions.

## Workflow

### Step 1 — Persona Document Finalization

Take the tested persona (from transistory install or full forge) and polish it:

1. **Expand thin sections**: Any area that felt improvised in the transistory version gets fleshed out
2. **Strengthen voice**: Add specific vocabulary preferences, forbidden phrases, and cadence instructions
3. **Deepen worldview**: Convert vague values into specific convictions with reasoning
4. **Add formation detail**: The backstory should read like a biography, not a sketch
5. **Verify messy details**: Ensure 5-10 task-irrelevant details are woven throughout

**Format**: Save as `persona.md` — plain markdown, narrative prose, 500-2000 words.

### Step 2 — Router Integration

Connect the persona to the agent's instruction chain:

**Option A — Persona First**: Router prompt loads persona.md before logic and library. The persona sets the atmospheric context for everything that follows.

**Option B — Persona Last**: Router prompt loads logic and library first, persona last. The persona acts as a final filter on everything produced.

**Corey's guidance**: "That's your choice." Test both. Some agents perform better with persona-first, others with persona-last. The difference is subtle but measurable.

**Router prompt reference example**:
```
When a conversation starts:
1. Read persona.md — this is your identity. You don't reference it in output. It defines how you think.
2. Read logic.md — this governs your workflow and rules.
3. Read library/ — these are your tools, templates, and references.
4. Check memory/ — recall relevant prior work.
```

### Step 3 — Initial Deployment Validation

Run 3 tasks across different categories the agent handles:
1. A standard task (the most common thing this agent does)
2. An edge case (something unusual or complex)
3. A creative task (something requiring judgment and taste)

For each, verify:
- Output is distinctive (not vanilla-floor)
- Persona influence is invisible (no persona details leak into output)
- Quality is consistent across task types

### Step 4 — Compound Schedule

Set up the refinement cycle:

- **After 10 conversations**: Review outputs. Identify patterns in what works and what doesn't. Refine persona document.
- **After 30 conversations**: The persona should feel "settled." Voice should be consistent. Worldview should produce predictable-quality outputs.
- **Monthly**: Review the persona against your evolving quality standards. The persona may need worldview updates as your understanding of the domain deepens.
- **Quarterly**: Full persona review. Is this still the right identity for this agent? Has the agent's purpose shifted? Does the persona need a major rewrite?

### Step 5 — Memory-Persona Interaction

Configure how memory and persona interact:
- Memory stores what happened. Persona defines who experienced it.
- When the agent recalls a memory, it should recall it *through* the persona's worldview — not as neutral facts.
- Memory helps the persona compound: the agent remembers how its persona-filtered judgment worked in past situations.

---

## Output Schema

Two artifacts:

1. **`persona.md`** — the finalized 500-2000 word narrative persona (Step 1), saved to the agent's workspace.
2. **Router integration block** — the loading-sequence instructions (Step 2's example format: Read persona.md → logic.md → library/ → memory/), written into the agent's router prompt, with the persona-first-vs-last decision documented.

Plus the Compound Schedule (Step 4: 10 / 30 conversation checkpoints, monthly, quarterly) recorded so the review cadence is trackable.

## Quality Gate

- [ ] Persona document is 500-2000 words of narrative prose
- [ ] Router prompt references persona.md with clear loading instructions
- [ ] 3 validation tasks show consistent quality elevation
- [ ] Compound schedule is documented (10/30/monthly/quarterly)
- [ ] Persona influence is invisible in output (no persona details leak)
