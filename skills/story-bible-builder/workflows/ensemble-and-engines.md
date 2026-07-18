---
name: "Ensemble Dynamics and Structural Engines"
slug: "ensemble-and-engines"
produces: "Bible sections 9–10: relationships/ensemble dynamics and structural engines"
skill: "story-bible-builder"
load_context: "genius.md"
---

# Story Bible Builder — Ensemble Dynamics and Structural Engines

## Role
You are running Build-Flow Steps 4–5 of Story Bible Builder, after all characters are individually locked (the Character Deep-Dive workflow). This workflow captures how the locked characters interact as a group and what recurring chapter shapes the story runs on. Both sections are short but, per the skill, "disproportionately valuable" (`SKILL.md`, line 127).

## Input Required
1. The full set of already-locked character sections from the Character Deep-Dive workflow — this workflow never runs before at least two characters are locked.
2. User answers to the room-dynamics question and the chapter-shape question below.

## Workflow

### Step 1 — Ensemble dynamics (section 9)
Ask: "When these characters are in a room together, what's the shape of the room? Who leads what? Who fills silence? Who watches? Which pairings are calm, which are charged?" (`SKILL.md`, line 124). Capture as short declarative sentences naming specific characters and specific pairings — never a generic relationship-map summary. Model shape: "Maren and Wren are the quietest room in the house — neither fills space, both notice everything. Owen and Iris cannot be in the same kitchen without one of them leaving." (`SKILL.md`, line 126).

### Step 2 — Structural engines (section 10)
Ask: "What are the recurring chapter shapes your story runs on? Not specific episodes — the shapes. A heist? A rescue? A performance? A confrontation? A flashback?" (`SKILL.md`, line 132). List each engine as a one-line shape description, and note explicitly that engines stack — "a heist can end in a confrontation, a performance can be interrupted by a rescue" (`SKILL.md`, line 134). This becomes future Claude's menu of story shapes for new-scene requests.

### Step 3 — Show back and lock
Present both sections together since they're short; iterate on either independently if the user wants changes.

## Output Schema

Two bible sections, in order:
1. **Relationships and ensemble dynamics** — a short block of declarative sentences, each naming specific characters, covering both the group-shape question (who leads/fills silence/watches) and named-pairing dynamics.
2. **Structural engines** — a numbered or bulleted list, each entry a one-line chapter *shape* (never a specific plot event), with an explicit note that engines can combine.

## Quality Gate

1. **Every ensemble sentence names specific locked characters** by name — no unnamed "the siblings" generalization once names exist.
2. **Pairing dynamics are named, not just group dynamics** — at least one specific two-character pairing is captured (`SKILL.md`, line 126 model).
3. **Structural engines are shapes, not plot** — each entry should be reusable across multiple hypothetical future scenes, not a description of one specific event that already happened.
4. **Stacking is noted explicitly** — the output states or implies that engines can combine, not just a flat list.
5. **No character introduced here for the first time** — this workflow only references characters already locked by the Character Deep-Dive workflow.
