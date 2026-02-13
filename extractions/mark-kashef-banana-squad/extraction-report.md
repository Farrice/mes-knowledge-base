# MES 3.0 Extraction Report — Mark Kashef: Banana Squad Image Agent Team

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
