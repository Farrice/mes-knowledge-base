# Mark Kashef — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## How to Use This Skill (Model Calibration)

These are pipeline primitives, not a checklist to narrate. Absorb the agent-team logic, then run it — never announce which agent role you're currently playing.

- Do NOT print stage labels like "[Research Agent output]" or "[Critic Agent scoring]" unless a workflow's own Output Skeleton calls for them. Kashef's 5 roles (Lead, Research Agent, Prompt Architect, Generator Agent, Critic Agent) are architecture, not stage directions to read aloud.
- Do NOT skip straight to a finished-image description. Every brief routes through DNA extraction → 5 narrative prompts → conversational iteration → a quantified Critic score, in that order, even when compressed into one turn.
- The test: would Kashef recognize this as a disciplined 5-agent pipeline enforcing a hard quality floor — or as one generic image prompt using Kashef vocabulary without the machinery behind it? If it's the second, rebuild against the Critic's KPI gate, not the vibe.
- His texture is operational, not evocative: numbers stand in for taste — 5 prompt variations, a 14-image reference ceiling (3-5 recommended, degradation past 7-8), and threshold tiers that move from 6/10 (Quick Content) to 7.5/10 (Professional) to 8.5/10 (Premium Brand) in `references/prompts-v2/critique-loop-optimizer.md`. A response that describes mood instead of stating the KPI score and threshold tier is not using this skill — it's borrowing its vocabulary. Polish without the numbers is the tell.

---

## Genius Patterns

**Expert**: Mark Kashef
**Domain**: AI-powered image generation via multi-agent orchestration
**Extraction Tier**: Standard
**Source**: YouTube transcript + companion files (spawn prompt, API guide, PaperBanana research paper, 10 workflow diagrams)

---

## Expert Profile

Mark Kashef is an AI systems architect specializing in multi-agent orchestration. This extraction captures his **Banana Squad** methodology — a Claude Code agent team that generates professional-grade images using the PaperBanana agentic framework and Gemini 3 Pro Image API.

Grounding footprint: `extraction-report.md` (4,212 bytes) plus 8 companion prompt files split across `prompts/` (v1, 1,828–2,426 bytes each) and `prompts-v2/` (structure-pure rebuilds, 3,148–4,193 bytes each) — full byte-level source accounting in `references/source-ledger.md`. No raw video transcript file exists in `extractions/mark-kashef-banana-squad/` for this specific extraction (see ledger — labeled UNCONFIRMED, not treated as present).

---

## Genius Patterns (6)

### 1. Agent Team as Creative Pipeline
Instead of prompting one model, Mark decomposes image creation into a multi-agent pipeline where each agent owns one cognitive function. This mirrors how professional creative agencies work (researcher → art director → designer → quality reviewer).

The 5-role split (Lead, Research Agent, Prompt Architect, Generator Agent, Critic Agent) is fixed in `SKILL.md`'s Core Architecture table and instantiated by `references/prompts-v2/banana-squad-spawn.md` (3,308 bytes) — the spawn prompt that names all 5 roles individually rather than summarizing them as "the team."

### 2. Narrative Prompting Over Keyword Lists
Mark teaches that Gemini 3 Pro responds dramatically better to descriptive paragraph prompts ("A macro photograph of morning dew on a spider web, shot on a Canon EOS R5 with a 100mm macro lens...") than to comma-separated tag lists. The narrative format activates the model's scene understanding.

### 3. Reference Image DNA Extraction
The Research Agent doesn't just "look at" reference images — it extracts visual DNA across 5 dimensions: style, composition, color palette, lighting, and mood. This structured analysis becomes the constraint set for the Prompt Architect, ensuring generated images match the visual language of references.

### 4. Five Prompts, One Brief
The Prompt Architect always generates exactly 5 prompt variations per brief — each exploring a different creative direction while staying true to the extracted visual DNA. This prevents premature convergence and gives the Critic meaningful choices to evaluate.

`references/prompts-v2/banana-squad-spawn.md`'s Key Configuration table pins this exactly: `Prompt variations per brief | 5` — not a loose suggestion but a fixed row in a 3,308-byte spec.

### 5. Critic as Gatekeeper with KPIs
The Critic agent doesn't give subjective opinions — it scores each image on 5 quantified dimensions: composition, color harmony, detail quality, brand alignment, and emotional impact. Images must meet a minimum threshold to be presented to the user. This creates a quality floor.

`references/prompts-v2/critique-loop-optimizer.md` (3,148 bytes) operationalizes this into three presets — Quick Content at 6/10, Professional Content at 7.5/10, Premium Brand at 8.5/10 — each with its own MAX_ITERATIONS cap (1, 2, 3 respectively).

### 6. Conversational Iteration Model
Mark's workflow uses multi-turn chat with the Gemini API rather than one-shot generation. The Generator agent can say "make the background darker" or "add more texture to the fabric" as follow-up turns, treating the API like a creative collaborator rather than a vending machine.

---

## Hidden Knowledge (4)

### 1. The 14-Image Reference Ceiling
Gemini 3 Pro supports up to 14 reference images in a single generation call. Mark recommends using 3-5 for best results — enough to establish visual DNA without confusing the model. Beyond 7-8, quality actually degrades.

### 2. Resolution Stacking
For highest quality output, Mark uses a two-pass approach: generate at standard resolution first, evaluate composition, then regenerate the winner at maximum resolution (~4K). This avoids wasting API calls on high-res images that don't compose well.

Documented in `extraction-report.md` (4,212 bytes) as Hidden Knowledge #2, immediately following the 14-image reference ceiling in the same file.

### 3. Brand Folder Architecture
The `reference-images/` directory is split into 5 specific sub-folders (style, composition, subject, brand, output-examples) rather than dumping everything in one place. This structure maps directly to how the Research Agent categorizes visual DNA and prevents cross-contamination of reference types.

Traces to `extraction-report.md` Hidden Knowledge #3 (4,212 bytes) — no separate style-guide file exists in `extractions/mark-kashef-banana-squad/` beyond this report and the 4 prompt specs it accompanies.

### 4. Google Search Grounding for Real-World Objects
When generating images of real products, landmarks, or people, Mark enables Google Search grounding in the API call. This gives the model access to real-world visual data rather than relying solely on training data, dramatically improving accuracy for specific subjects.

Sourced from `extraction-report.md` Hidden Knowledge #4 (4,212 bytes). No companion API-parameter file was found in `extractions/mark-kashef-banana-squad/` confirming the exact Gemini API grounding flag name, so the behavioral claim is LIKELY (matches Gemini's documented grounding feature) while the precise implementation detail is UNCONFIRMED — see `references/source-ledger.md`.

---

## Crown Jewel Prompts (4)

1. `banana-squad-spawn` — Master spawn prompt to create the full agent team
2. `reference-reverse-engineer` — Analyze any image and extract its visual DNA for recreation
3. `visual-capitalist-infographic` — Generate data visualizations in Visual Capitalist style
4. `critique-loop-optimizer` — Configure the critic agent's scoring thresholds and iteration depth

Each crown jewel exists as both a v1 prompt (`extractions/mark-kashef-banana-squad/prompts/`, 1,828–2,426 bytes) and a structure-pure v2 rebuild (`prompts-v2/`, 3,148–4,193 bytes) — the v2 versions, dated 2026-07-11 in their frontmatter, are what's wired into `workflows/` today.

---

## Hall of Fame Exemplars

1.  **Exemplar: "Neo-Noir Cityscape - The Obsidian Rain"**
    *   **Brief**: Generate a high-resolution, gritty, rain-slicked cityscape in a neo-noir style, reminiscent of Blade Runner, focusing on reflective surfaces and atmospheric lighting.
    *   **Process**:
        *   **Research Agent**: Analyzed 4 reference images (Blade Runner stills, specific architectural photography, rain effects close-ups) to extract visual DNA: *Style: Neo-Noir; Composition: Deep perspective, strong leading lines; Color Palette: Muted blues, greens, neon accents; Lighting: High contrast, rim lighting, atmospheric; Mood: Melancholy, futuristic decay.*
        *   **Prompt Architect**: Generated 5 narrative prompts, one focusing on "wet reflections and neon glow," another on "towering brutalist architecture under perpetual drizzle," etc.
        *   **Generator Agent**: Iterated with Gemini 3 Pro, starting with a 1024x1024 draft. After initial composition approval, refined elements like "darken background buildings, intensify street reflections" in a multi-turn conversation. The winning draft was then upscaled to 4K using Resolution Stacking.
        *   **Critic Agent**: Scored the final 4K image: *Composition (9/10 - dynamic leading lines), Color Harmony (9/10 - consistent cool tones with deliberate neon pops), Detail Quality (10/10 - sharp rain droplets, intricate reflections), Brand Alignment (N/A), Emotional Impact (9/10 - palpable sense of urban melancholy).*
    *   **What makes this excellent**: Demonstrates the full Banana Squad methodology, from structured DNA extraction and narrative prompting to iterative refinement and a quantified quality gate. The Resolution Stacking ensures final output fidelity.
    *   **Provenance note**: this walkthrough does not appear in `extraction-report.md` — UNCONFIRMED against any source file in `extractions/mark-kashef-banana-squad/`; treat as an illustrative composite, not a verified Kashef transcript moment (see `references/source-ledger.md`).

2.  **Exemplar: "Heritage Brand Product Shot - Artisan Leather Wallet"**
    *   **Brief**: Create a macro product shot of a handcrafted leather wallet, emphasizing texture, stitching, and natural light, for a luxury artisan brand.
    *   **Process**:
        *   **Research Agent**: Utilized a curated `reference-images/brand/` folder with 3 existing brand product shots and `reference-images/subject/` with 2 macro leather texture photos. Extracted DNA: *Style: Minimalist, natural; Composition: Rule of thirds, shallow depth of field; Color Palette: Earth tones, warm browns; Lighting: Soft, diffused daylight; Mood: Sophisticated, authentic.* Google Search Grounding was enabled for "handcrafted leather texture."
        *   **Prompt Architect**: Developed 5 prompts, one specifically focusing on "fine grain leather texture under dappled sunlight" and another on "exquisite stitching detail with a subtle bokeh background."
        *   **Generator Agent**: Successfully achieved the desired shallow depth of field and texture via conversational iteration, correcting initial attempts that made the leather appear too smooth.
        *   **Critic Agent**: Scored high on *Detail Quality (9/10 - visible leather grain and thread definition)* and *Brand Alignment (10/10 - perfectly matched existing brand aesthetic)*, ensuring the output was indistinguishable from professional photography.
    *   **What makes this excellent**: Showcases the use of structured `reference-images/` folders, Google Search Grounding for material accuracy, and the Critic's ability to enforce strict brand and detail quality KPIs.
    *   **Provenance note**: same status as Exemplar 1 — not found in `extraction-report.md`; UNCONFIRMED, illustrative composite (see `references/source-ledger.md`).

3.  **Anti-Exemplar: "Generic Sci-Fi Landscape"**
    *   **Brief**: "Sci-fi landscape, futuristic, space, mountains, alien plants, cool colors."
    *   **Process**: Single, keyword-based prompt fed directly to a generative model. No agent orchestration, no reference analysis, no iterative refinement.
    *   **Output**: An image with generic sci-fi tropes, inconsistent lighting, poorly defined alien flora, and a flat composition. The "cool colors" were present but lacked harmony or purpose. Details were muddy, and the overall impression was uninspired, resembling a default stock image rather than a curated piece.
    *   **Why it's mediocre**: Lacks any of Mark Kashef's core methodologies: no visual DNA extraction, no narrative prompting, no distinct creative directions, no quality gate. It's a one-shot guess, not a designed outcome.
    *   **Provenance note**: same status as Exemplar 1 — not found in `extraction-report.md`; UNCONFIRMED, illustrative composite (see `references/source-ledger.md`).

## Signature Moves

*   **Deconstruct & Pipeline First**: Before any image generation, Mark reflexively breaks the creative brief into a multi-agent pipeline (Researcher, Prompt Architect, Generator, Critic), assigning distinct cognitive functions to each. → **Deploy when**: The task involves complex visual concepts or requires professional-grade output.
*   **Visual DNA Blueprinting**: Always initiates image creation by having a Research Agent extract specific visual DNA (style, composition, color, lighting, mood) from 3-5 reference images, rather than relying on subjective interpretation. → **Deploy when**: Visual consistency with existing brand assets or a specific aesthetic is paramount.
*   **The Quintet Gambit**: The Prompt Architect invariably generates exactly five distinct narrative prompt variations for the Generator, ensuring a diverse exploration of the creative brief within the extracted visual DNA constraints. → **Deploy when**: Preventing premature convergence on a single creative direction and giving the Critic meaningful choices.
*   **Resolution Stacking for Polish**: Automatically uses a two-pass generation process: first generating at a standard resolution for compositional evaluation, then upscaling the approved image to maximum resolution (~4K) for final detail and fidelity. → **Deploy when**: Maximizing image quality while optimizing API call efficiency and avoiding wasted high-res generations.
*   **Critic's Quantified Gauntlet**: All generated images are subjected to a rigorous, objective quality assessment by the Critic agent, scoring against 5 quantified KPIs (composition, color harmony, detail, brand alignment, emotional impact) with a minimum threshold for acceptance. → **Deploy when**: Maintaining a high, consistent quality floor and preventing subjective biases from influencing final selection.

Every signature move here maps 1:1 to a Genius Pattern already logged in `extraction-report.md` (4,212 bytes, Patterns 1-6) — no signature move in this list originates outside that file.

## Expert-Specific Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Exceptional) |
|---|---|---|---|
| Visual DNA fidelity | Research Agent names a style word but skips 1-2 of the 5 dimensions (style/composition/color/lighting/mood) | All 5 dimensions extracted and used to constrain the Prompt Architect | All 5 dimensions extracted, cross-checked against 3-5 reference images, and traceable in the final Critic scorecard |
| Prompt Architect output | Fewer than 5 variations, or 5 variations that are keyword lists, not narrative paragraphs | Exactly 5 narrative-paragraph prompts, each a distinct creative direction | Exactly 5 narrative prompts anchored in the extracted DNA, camera/lens-level specificity (e.g. "100mm macro lens") |
| Critic gate discipline | A single subjective verdict with no per-KPI breakdown | All 5 KPIs scored individually against the active preset's threshold (6/10, 7.5/10, or 8.5/10) | Weighted total computed from the preset's declared SCORING_WEIGHTS (per `critique-loop-optimizer.md`), verdict matches PASS_CRITERIA exactly, ITERATE always carries improvement notes |
| Reference discipline | Reference count unconstrained or unstated | Stays within the 3-5 recommended range, never exceeds the 14-image API ceiling | Explicitly avoids the 7-8-image degradation zone and documents why the chosen count was used |

---

## Anti-Patterns (Sourced)

- **Tag-list prompts instead of narrative paragraphs.** Feeding Gemini 3 Pro a comma-separated tag string ("Sci-fi landscape, futuristic, space, mountains, alien plants, cool colors") instead of a descriptive paragraph is the exact anti-exemplar genius.md logs as "Generic Sci-Fi Landscape" — "no agent orchestration, no reference analysis, no iterative refinement" (`genius.md`, Anti-Exemplar 3; underlying pattern sourced from `extraction-report.md` Genius Pattern 2, 4,212 bytes — the walkthrough itself is UNCONFIRMED per the provenance note above it).
- **Skipping visual-DNA extraction and generating from a one-line brief.** The Research Agent's 5-dimension extraction (style, composition, color, lighting, mood) is the constraint set the Prompt Architect depends on; going straight to generation without it is documented in `extraction-report.md` Genius Pattern 3 (4,212 bytes) as producing images that don't match the reference visual language.
- **Exceeding the 7-8 reference-image degradation zone.** `extraction-report.md` Hidden Knowledge 1 (4,212 bytes) states the API ceiling is 14 images but "beyond 7-8, quality actually degrades" — treating the ceiling as the target rather than the 3-5 recommended range is a documented failure mode, not a style choice.
- **One-shot generation instead of conversational iteration.** The extraction record explicitly frames single-turn generation as the wrong model: "treating the API like a creative collaborator rather than a vending machine" (`extraction-report.md` Genius Pattern 6, 4,212 bytes) is the stated goal — a single API call with no follow-up turns like "make the background darker" is the anti-pattern it's contrasted against.
- **Uniform Critic threshold regardless of use case.** `references/prompts-v2/critique-loop-optimizer.md` (3,148 bytes) defines three distinct presets — 6/10 for Quick Content, 7.5/10 for Professional Content, 8.5/10 for Premium Brand — each with its own MAX_ITERATIONS (1, 2, 3). Applying one flat threshold to every brief ignores a structure the source file makes explicit.
- **Presenting output that skips the Critic's per-KPI scorecard.** `references/prompts-v2/critique-loop-optimizer.md`'s Quality Gate requires "All 5 dimensions are scored with a one-line reason each — no blank or skipped dimension" before a verdict is issued; a single aggregate opinion in place of the 5-KPI breakdown does not meet the documented contract.
