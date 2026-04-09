# Tao Prompts — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

AI video is an assembly line, not a magic box. Write prompts like architectural blueprints using the Cinematic Formula: [Visual Style] + [Camera Shot] + [Subject] + [Action] + [Environment] + [Camera Motion]. Never leave framing up to AI interpretation. Decouple action from dialogue — generate them separately and connect in the edit. Use Custom GPTs as syntax translators between narrative intent and tool-specific prompt formats.

---

## Genius Patterns (Compressed)

### GP1: The Cinematic Formula (Structured Control)
Assemble prompts strictly using: [Visual Style] + [Camera Shot] + [Subject] + [Action] + [Environment] + [Camera Motion]. Never leave framing or styling to AI interpretation. Write prompts like architectural blueprints, not novelist descriptions.

### GP2: Multi-Shot Sequential Prompting
Write a single unified prompt defining multiple distinct shots sequentially (Shot 1: Wide establishing. Shot 2: Close-up on fingers. Shot 3: Over-the-shoulder at screen). Constructs cohesive B-roll sequences maintaining stylistic and character continuity across cuts.

### GP3: The "Lazy Teacher" Prompt Translator
Feed the official prompt guideline PDF of the target tool (Cling AI, Runway, etc.) into a Custom GPT. Instruct it to act as strict syntax translator. Supply narrative intent, get tool-optimized prompt on first pass. Never hand-write tool-specific syntax.

### GP4: Modular Pipeline Orchestration
Treat AI video as an assembly line — never expect one model to do everything. Generate visuals (Runway/Cling), audio (11Labs), lip-sync (Creatify/SyncLabs) in separate specialized tools, then stitch together. Character movements don't warp when action and lip-sync are generated in parallel environments.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | The Decoupling Law — never prompt for intense physical action and dialogue lip-sync in same generation; create action as B-roll, close-ups for lip-sync, connect in edit | When planning character-driven sequences with action + dialogue |
| HK2 | The Storyboard Bridge — text is too fluid for multi-shot continuity; a visual storyboard grid (3x3 Midjourney grid) is mandatory between script and video generation | Before any multi-shot sequence requiring narrative arc and continuity |
| HK3 | Prompt Complexity does not equal Aesthetic Quality — more words/adjectives don't make better video; complexity is for control and specificity, not beauty; beginners clutter with redundant descriptors | When debugging incorrect framing or simplifying for subject continuity |

---

## Signature Moves

1. **The Syntax Translator Scan** — Before generating on any new platform, feed its official docs into a Custom GPT as a strict syntax translator. Never hand-write tool-specific syntax.
2. **The Shot Blueprint** — Every visual concept immediately deconstructed into [Visual Style] + [Camera Shot] + [Subject] + [Action] + [Environment] + [Camera Motion]. No free-form descriptions for core visuals.
3. **The Action/Dialogue Split** — Any scene with both significant physical action and spoken dialogue is flagged for two-stage generation: dynamic action shots + static close-ups for lip-sync, edited together.
4. **The Visual Pre-Flight** — For multi-shot sequences, generate a visual storyboard grid first (3x3 from Midjourney/LLM) to define continuity, character consistency, and shot progression before touching any video tool.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Shot Control Fidelity | Some camera shots/angles ignored or misinterpreted | Most followed with minor deviations | Every shot, angle, and motion executed with pixel-perfect precision |
| Multi-Shot Continuity | Noticeable shifts in character/lighting/environment | Consistency maintained but transitions abrupt | Perfect consistency across all shots; seamless editorial cohesion |
| Action-Dialogue Decoupling | Faces warp/stutter when speaking; poor decoupling | Mostly clean dialogue with subtle inconsistencies | Dynamic action + perfectly synced natural speech; no artifacts |
| Prompt Translation Accuracy | Translated prompts need significant manual adjustment | Work on first try but could be more efficient | Raw ideas flawlessly translated to tool-optimized syntax every time |
| Pipeline Orchestration | Tasks combined into single tools; suboptimal results | Mostly separated but clunky handoffs | Each task routed to optimal tool; smooth, artifact-free final output |
| Subject Focus & Clutter | Redundant descriptors confuse model or dilute focus | Generally concise but occasional unnecessary keywords | Maximally concise; complexity only for control, never embellishment |
