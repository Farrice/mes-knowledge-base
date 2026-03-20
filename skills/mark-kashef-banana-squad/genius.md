# Mark Kashef — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns

**Expert**: Mark Kashef
**Domain**: AI-powered image generation via multi-agent orchestration
**Extraction Tier**: Standard
**Source**: YouTube transcript + companion files (spawn prompt, API guide, PaperBanana research paper, 10 workflow diagrams)

---

## Expert Profile

Mark Kashef is an AI systems architect specializing in multi-agent orchestration. This extraction captures his **Banana Squad** methodology — a Claude Code agent team that generates professional-grade images using the PaperBanana agentic framework and Gemini 3 Pro Image API.

---

## Genius Patterns (6)

### 1. Agent Team as Creative Pipeline
Instead of prompting one model, Mark decomposes image creation into a multi-agent pipeline where each agent owns one cognitive function. This mirrors how professional creative agencies work (researcher → art director → designer → quality reviewer).

### 2. Narrative Prompting Over Keyword Lists
Mark teaches that Gemini 3 Pro responds dramatically better to descriptive paragraph prompts ("A macro photograph of morning dew on a spider web, shot on a Canon EOS R5 with a 100mm macro lens...") than to comma-separated tag lists. The narrative format activates the model's scene understanding.

### 3. Reference Image DNA Extraction
The Research Agent doesn't just "look at" reference images — it extracts visual DNA across 5 dimensions: style, composition, color palette, lighting, and mood. This structured analysis becomes the constraint set for the Prompt Architect, ensuring generated images match the visual language of references.

### 4. Five Prompts, One Brief
The Prompt Architect always generates exactly 5 prompt variations per brief — each exploring a different creative direction while staying true to the extracted visual DNA. This prevents premature convergence and gives the Critic meaningful choices to evaluate.

### 5. Critic as Gatekeeper with KPIs
The Critic agent doesn't give subjective opinions — it scores each image on 5 quantified dimensions: composition, color harmony, detail quality, brand alignment, and emotional impact. Images must meet a minimum threshold to be presented to the user. This creates a quality floor.

### 6. Conversational Iteration Model
Mark's workflow uses multi-turn chat with the Gemini API rather than one-shot generation. The Generator agent can say "make the background darker" or "add more texture to the fabric" as follow-up turns, treating the API like a creative collaborator rather than a vending machine.

---

## Hidden Knowledge (4)

### 1. The 14-Image Reference Ceiling
Gemini 3 Pro supports up to 14 reference images in a single generation call. Mark recommends using 3-5 for best results — enough to establish visual DNA without confusing the model. Beyond 7-8, quality actually degrades.

### 2. Resolution Stacking
For highest quality output, Mark uses a two-pass approach: generate at standard resolution first, evaluate composition, then regenerate the winner at maximum resolution (~4K). This avoids wasting API calls on high-res images that don't compose well.

### 3. Brand Folder Architecture
The `reference-images/` directory is split into 5 specific sub-folders (style, composition, subject, brand, output-examples) rather than dumping everything in one place. This structure maps directly to how the Research Agent categorizes visual DNA and prevents cross-contamination of reference types.

### 4. Google Search Grounding for Real-World Objects
When generating images of real products, landmarks, or people, Mark enables Google Search grounding in the API call. This gives the model access to real-world visual data rather than relying solely on training data, dramatically improving accuracy for specific subjects.

---

## Crown Jewel Prompts (4)

1. `banana-squad-spawn` — Master spawn prompt to create the full agent team
2. `reference-reverse-engineer` — Analyze any image and extract its visual DNA for recreation
3. `visual-capitalist-infographic` — Generate data visualizations in Visual Capitalist style
4. `critique-loop-optimizer` — Configure the critic agent's scoring thresholds and iteration depth

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

2.  **Exemplar: "Heritage Brand Product Shot - Artisan Leather Wallet"**
    *   **Brief**: Create a macro product shot of a handcrafted leather wallet, emphasizing texture, stitching, and natural light, for a luxury artisan brand.
    *   **Process**:
        *   **Research Agent**: Utilized a curated `reference-images/brand/` folder with 3 existing brand product shots and `reference-images/subject/` with 2 macro leather texture photos. Extracted DNA: *Style: Minimalist, natural; Composition: Rule of thirds, shallow depth of field; Color Palette: Earth tones, warm browns; Lighting: Soft, diffused daylight; Mood: Sophisticated, authentic.* Google Search Grounding was enabled for "handcrafted leather texture."
        *   **Prompt Architect**: Developed 5 prompts, one specifically focusing on "fine grain leather texture under dappled sunlight" and another on "exquisite stitching detail with a subtle bokeh background."
        *   **Generator Agent**: Successfully achieved the desired shallow depth of field and texture via conversational iteration, correcting initial attempts that made the leather appear too smooth.
        *   **Critic Agent**: Scored high on *Detail Quality (9/10 - visible leather grain and thread definition)* and *Brand Alignment (10/10 - perfectly matched existing brand aesthetic)*, ensuring the output was indistinguishable from professional photography.
    *   **What makes this excellent**: Showcases the use of structured `reference-images/` folders, Google Search Grounding for material accuracy, and the Critic's ability to enforce strict brand and detail quality KPIs.

3.  **Anti-Exemplar: "Generic Sci-Fi Landscape"**
    *   **Brief**: "Sci-fi landscape, futuristic, space, mountains, alien plants, cool colors."
    *   **Process**: Single, keyword-based prompt fed directly to a generative model. No agent orchestration, no reference analysis, no iterative refinement.
    *   **Output**: An image with generic sci-fi tropes, inconsistent lighting, poorly defined alien flora, and a flat composition. The "cool colors" were present but lacked harmony or purpose. Details were muddy, and the overall impression was uninspired, resembling a default stock image rather than a curated piece.
    *   **Why it's mediocre**: Lacks any of Mark Kashef's core methodologies: no visual DNA extraction, no narrative prompting, no distinct creative directions, no quality gate. It’s a one-shot guess, not a designed outcome.

## Signature Moves

*   **Deconstruct & Pipeline First**: Before any image generation, Mark reflexively breaks the creative brief into a multi-agent pipeline (Researcher, Prompt Architect, Generator, Critic), assigning distinct cognitive functions to each. → **Deploy when**: The task involves complex visual concepts or requires professional-grade output.
*   **Visual DNA Blueprinting**: Always initiates image creation by having a Research Agent extract specific visual DNA (style, composition, color, lighting, mood) from 3-5 reference images, rather than relying on subjective interpretation. → **Deploy when**: Visual consistency with existing brand assets or a specific aesthetic is paramount.
*   **The Quintet Gambit**: The Prompt Architect invariably generates exactly five distinct narrative prompt variations for the Generator, ensuring a diverse exploration of the creative brief within the extracted visual DNA constraints. → **Deploy when**: Preventing premature convergence on a single creative direction and giving the Critic meaningful choices.
*   **Resolution Stacking for Polish**: Automatically uses a two-pass generation process: first generating at a standard resolution for compositional evaluation, then upscaling the approved image to maximum resolution (~4K) for final detail and fidelity. → **Deploy when**: Maximizing image quality while optimizing API call efficiency and avoiding wasted high-res generations.
*   **Critic's Quantified Gauntlet**: All generated images are subjected to a rigorous, objective quality assessment by the Critic agent, scoring against 5 quantified KPIs (composition, color harmony, detail, brand alignment, emotional impact) with a minimum threshold for acceptance. → **Deploy when**: Maintaining a high, consistent quality floor and preventing subjective biases from influencing final selection.

## Expert-Specific Quality Rubric

| Criterion                     | Score 4 (Acceptable)                                                                                                                              | Score 7 (Good)
