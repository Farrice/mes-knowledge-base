# Mark Kashef (Banana Squad) — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

Kashef decomposes image creation into a multi-agent pipeline mirroring professional creative agencies (researcher → art director → designer → quality reviewer). The core insight: AI image generation is not a single-prompt problem but a structured creative process where each cognitive function — visual DNA extraction, narrative prompting, iterative generation, and quantified critique — must be isolated in dedicated agents.

---

## Genius Patterns (Compressed)

### GP1: Agent Team as Creative Pipeline
Instead of prompting one model, decompose image creation into a multi-agent pipeline: Research Agent → Prompt Architect → Generator → Critic. Each agent owns one cognitive function, preventing context dilution and enabling professional-grade output.

### GP2: Narrative Prompting Over Keyword Lists
Gemini 3 Pro responds dramatically better to descriptive paragraph prompts ("A macro photograph of morning dew on a spider web, shot on a Canon EOS R5 with a 100mm macro lens...") than comma-separated tags. Narrative format activates scene understanding.

### GP3: Reference Image DNA Extraction
The Research Agent extracts visual DNA across 5 dimensions: style, composition, color palette, lighting, and mood. This structured analysis becomes the constraint set for the Prompt Architect, ensuring generated images match the visual language of references.

### GP4: Five Prompts, One Brief
The Prompt Architect always generates exactly 5 prompt variations per brief — each exploring a different creative direction while staying true to extracted visual DNA. Prevents premature convergence and gives the Critic meaningful choices.

### GP5: Critic as Gatekeeper with KPIs
The Critic scores each image on 5 quantified dimensions: composition, color harmony, detail quality, brand alignment, and emotional impact. Images must meet minimum threshold to be presented. Creates a quality floor, not subjective opinions.

### GP6: Conversational Iteration Model
Multi-turn chat with Gemini API rather than one-shot generation. The Generator can say "make the background darker" or "add more texture" as follow-up turns, treating the API as a creative collaborator, not a vending machine.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | 14-Image Reference Ceiling — Gemini supports up to 14 refs per call; use 3-5 for best results; beyond 7-8 quality degrades | Reference image selection |
| HK2 | Resolution Stacking — generate at standard resolution first, evaluate composition, then regenerate winner at ~4K; avoids wasting API calls on bad compositions | Maximizing output quality |
| HK3 | Brand Folder Architecture — split reference-images/ into 5 sub-folders (style, composition, subject, brand, output-examples) mapping to Research Agent categories | Organizing reference materials |
| HK4 | Google Search Grounding — enable for real products/landmarks/people; gives model real-world visual data instead of training data alone | Generating images of real-world subjects |

---

## Signature Moves

1. **Deconstruct & Pipeline First** — Before any generation, breaks creative brief into multi-agent pipeline with distinct cognitive functions per agent.
2. **Visual DNA Blueprinting** — Research Agent extracts visual DNA (style, composition, color, lighting, mood) from 3-5 references before any prompting begins.
3. **The Quintet Gambit** — Prompt Architect invariably generates exactly 5 distinct narrative prompt variations per brief.
4. **Resolution Stacking for Polish** — Two-pass approach: standard resolution for compositional evaluation, then 4K upscale of the approved winner.
5. **Critic's Quantified Gauntlet** — All images scored against 5 quantified KPIs with minimum threshold for acceptance.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Pipeline Decomposition | Single prompt, no agent separation | Some role separation but incomplete pipeline | Full 4-agent pipeline (Research → Prompt Architect → Generator → Critic) with distinct cognitive functions |
| Visual DNA Extraction | General style description without structured analysis | Some dimensions analyzed but incomplete coverage | All 5 dimensions (style, composition, color, lighting, mood) extracted from 3-5 references |
| Prompt Narrative Quality | Keyword/tag lists | Partial narrative with some descriptive elements | Full descriptive paragraphs activating scene understanding with camera/lens/lighting specifics |
| Creative Divergence | Single prompt direction | 2-3 variations with limited differentiation | Exactly 5 distinct creative directions, each exploring different aspects while honoring visual DNA |
| Quality Gate Rigor | Subjective "looks good" assessment | Some quantified criteria but inconsistent application | 5 KPIs scored numerically with minimum threshold enforced before presentation |
