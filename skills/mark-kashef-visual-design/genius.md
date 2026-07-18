# Mark Kashef Visual Blueprint Methodology — Genius Context

> Load this file before executing any workflow. It contains the integrated genius patterns and hidden knowledge that inform every visual planning operation.

---

## How to Use This Skill (Model Calibration)

This is a sequencing instinct, not a checklist to announce. Kashef's whole method compresses into one reflex: **wireframe before code, always, no exceptions for "simple" outputs.** Absorb that reflex, then design originally — if a deliverable narrates "applying the Visual Contract Protocol" or "now invoking Taste Arbitrage" in labeled sequence, you have failed the assignment. The test: would Kashef recognize this as someone who instinctively stops before touching a design tool and asks "have I made every spatial assumption explicit yet?" — or as someone reciting wireframe terminology without ever actually drawing one? If it's the second, rebuild.

Specifically:
- Do NOT skip straight to a build prompt for a "quick" or "simple" visual ask. Kashef's own contrast case is the one-line lazy prompt — "Build me a SAS dashboard. I want a sidebar, some stat cards, a couple charts, and a data table" — which produced, in his own words, "a fairly ugly vibecoded icon looking sidebar." Simplicity is exactly when the wireframe gets skipped, and exactly when it matters most.
- Do NOT let a wireframe carry aesthetic instructions (colors, fonts, "make it modern"). That's a Taste Arbitrage violation — structure and beauty are two different cognitive tasks, and mixing them is the tell that the wireframe step was performed rather than used.
- His register is plain and demonstrative, not evangelist. He doesn't say "this technique will transform your workflow" — he says "before writing any code, create an ASCII wireframe of X," shows the artifact, then shows the output next to it. Polish is the tell-class warning: if a deliverable talks *about* the wireframe method instead of just producing a wireframe, rebuild.
- Never treat a technical diagram as done because it's structurally complete — if it "looks like gibberish" to the person who has to approve it, the Complexity Equalizer pattern hasn't fired yet.

## The Core Insight

Using ASCII art wireframes as a **visual contract** between human intent and AI execution. This eliminates the most expensive failure mode in AI-augmented design: **the assumption gap**. Humans provide taste and spatial judgment. AI handles execution beauty. The wireframe is the bridge. Kashef frames the whole method as replacing an entire design pipeline: "the same way we used to go on whiteboards and doodle and then send that doodle to our design team and then that design team would create a Figma" (source: extractions/mark-kashef-visual-design/transcript.txt) — the wireframe step is that whiteboard session, compressed to minutes and run inside the same tool that will build the thing.

---

## 8 Genius Patterns

### 1. Visual Contract Protocol
Force every visual project through a blueprint phase where BOTH human and AI agree on spatial layout before any production work begins. The wireframe IS the specification — not a suggestion, not an inspiration board. It's the contract. Kashef's own worked example: "before writing any code create a ask key wireframe of a SAS analytics dashboard. Put a sidebar stat cards two charts side by side and a data table below" (source: extractions/mark-kashef-visual-design/transcript.txt) — every element named before a single line of code exists.

### 2. Assumption Assassin
AI failure in visual work almost always stems from **unstated assumptions**, not capability gaps. Every element you don't specify in the wireframe is an element the AI will assume. Assumptions compound. Three unstated assumptions across ten elements = 30 divergence points. The wireframe makes the invisible visible.

### 3. Token Economist
All iteration happens at the wireframe layer (~50 tokens per change) instead of the code/design layer (~5,000 tokens per change). Slide decks are especially token-intensive — 5-6 iterations at the code layer can exhaust an entire context window. Wireframe-first reduces token spend by 60-80%.

### 4. Taste Arbitrage
Separate the **thinking** (layout, structure, relationships, hierarchy) from the **beauty** (colors, typography, spacing, polish). In the wireframe, specify WHAT goes WHERE and WHY. In the build prompt, tell AI to focus on making it beautiful. Never mix these two cognitive tasks. The dashboard wireframe prompt is the clean example of thinking-only input — "put a sidebar stat cards two charts side by side and a data table below" (source: extractions/mark-kashef-visual-design/transcript.txt) names zero colors, zero fonts, zero polish cues. Beauty gets deferred to a separate instruction entirely.

### 5. Progressive Refinement Engine
Use multi-turn conversation at the wireframe layer for surgical edits: "Two changes only. Make the line chart wider than the pie chart. Change active/green to inactive/gray. Redraw the full wireframe." Small, numbered, scoped changes. Each iteration takes <30 seconds.

### 6. Complexity Equalizer
Visual diagrams make technical concepts (database schemas, SQL relationships, API structures) accessible to non-technical stakeholders. If a diagram "looks like gibberish," request simplification: "make this diagram as if you're in seventh grade" (source: extractions/mark-kashef-visual-design/transcript.txt). The visualization forces comprehension — if you can't wireframe it, you don't understand it.

### 7. Multi-Vertical Blueprint
The SAME protocol works identically across radically different output types — dashboards, landing pages, slide decks, databases, email templates, PDFs, infographics. It's a universal cognitive protocol. The pattern: "Before writing any [output type], create an ASCII wireframe of [specifications]."

### 8. Orchestrator Identity Shift
The human becomes **creative director**, not prompt engineer. You sketch the blueprint. You approve the wireframe. You greenlight production. The AI is your production team. You focus on vision, taste, and approval gates. AI focuses on execution at the production layer. Kashef's own closing framing of the database-schema example: "once everything conceptually makes sense, you can then be the orchestrator, the conductor" (source: extractions/mark-kashef-visual-design/transcript.txt) — approval, not authorship, is the human's job past that point.

---

## 6 Hidden Knowledge Items

### The Lazy Prompt Firewall
Even LAZY prompts produce acceptable output when preceded by wireframes. The wireframe carries 80% of the specification load, so the build prompt can be simple. This is a firewall against prompting incompetence.

### The Figma Killer Insight
This eliminates the whiteboard → design team → Figma → development team pipeline. A 2-minute wireframe session replaces a $50K+/year design pipeline role.

### The Secret Slide Deck Revenue Play
Mark has used this for client slide decks for 6 months as a professional, revenue-generating technique, in his own words: "I've actually been using this for slide decks for clients for the past six months secretly" (source: extractions/mark-kashef-visual-design/transcript.txt). Slide decks are the highest-ROI use case because of token economics (slides are extremely token-expensive to iterate at the code layer).

### Visualization-as-Understanding
ASCII diagrams aren't just for planning — they're for **learning**. Use them to understand every new feature, concept, or system: "I use this day-to-day to better understand every single new feature and concept that comes out" (source: extractions/mark-kashef-visual-design/transcript.txt). The visualization forces comprehension at a level that text alone cannot achieve.

### The Vibe Coding Horror Stories Root Cause
Most AI development failures are human failures of specification, not AI failures of execution. "A lot of vibe coding horror stories just come from poor planning." The wireframe solves a PLANNING problem.

### Skills From Diagrams (Meta-Pattern)
ASCII wireframes can be used to DESIGN AI skills, agent architectures, and workflow topologies themselves. It's recursive — use the visual method to design the visual method. Kashef states this directly: "I even created a bunch of skills from them because this gives you the power to have full visualization and understanding of each and every part of an intricate system" (source: extractions/mark-kashef-visual-design/transcript.txt).

---

## The 6-Phase Execution Pattern

Every visual project follows this sequence:

1. **Conceptualize** — Define components, relationships, hierarchy. No tools yet.
2. **Wireframe** — "Before writing any [X], create an ASCII wireframe of [Y]."
3. **Iterate** — Small, numbered, scoped changes until wireframe = mental model.
4. **Annotate** — Add style/aesthetic notes to the locked wireframe.
5. **Execute** — "Build this using the wireframe as the exact specification."
6. **Validate** — Compare output to wireframe. 1:1 element mapping.

---

## Anti-Patterns (Sourced)

- **Never send a lazy one-line prompt straight to production for a "simple" visual ask** — Kashef's own contrast experiment: "Build me a SAS dashboard. I want a sidebar, some stat cards, a couple charts, and a data table" produced, in his own assessment, "a fairly ugly vibecoded icon looking sidebar" (source: extractions/mark-kashef-visual-design/transcript.txt, dashboard section, file on disk since 2026-03-07).
- **Never let vibecoded icon/emoji-style visuals ship without an explicit style override** — on the landing-page build he flags it live: "I can already see it's proposing some vibecoded icons" (source: extractions/mark-kashef-visual-design/transcript.txt, landing page section).
- **Never accept a technical diagram that "looks like gibberish" to the person who has to approve it** — the fix is a direct simplification request: "make this diagram as if you're in seventh grade" (source: extractions/mark-kashef-visual-design/transcript.txt, database/SQL section).
- **Never assume a generated database schema is correct without visualizing the relationships first** — "the average person who is non-technical just assumes that the database created is perfect and doesn't really get into the weeds as to how different things are stored" (source: extractions/mark-kashef-visual-design/transcript.txt, database section).
- **Never iterate a token-expensive output (slide decks especially) at the code/production layer** — the extraction report names the cost directly: slide decks are "very token intensive" and "5-6 iterations at the code layer can exhaust context windows entirely" (source: extractions/mark-kashef-visual-design/extraction-report.md, Genius Pattern 3 "The Token Economist").
- **Never mix aesthetic direction into the wireframe step** — the landing-page lazy-prompt comparison ("Make it modern and clean with a hero, features, pricing, and footer") produced a result Kashef himself critiques on structural-then-aesthetic grounds: "the coloring is not ideal," "this looks more of a therapeutic reading based website," "it just doesn't look clean" (source: extractions/mark-kashef-visual-design/transcript.txt, landing page lazy-prompt section) — proof that skipping the thinking/beauty split degrades both.

## Stacking Protocol

When used with other skills:
- **Before Banana Squad**: Wireframe the composition/layout before image generation
- **Before Kittl/Design**: Wireframe graphic layouts before production
- **Before `/design-first-build`**: Wireframe IS the design-first artifact
- **With Oren CEV**: Apply taste critique to wireframes before production
- **With any slide/deck work**: ALWAYS wireframe slides first (token economics mandate — same ~50 tokens/wireframe-change vs. ~5,000 tokens/code-layer-change ratio as Genius Pattern 3, "The Token Economist")
- **With Nana Banana image gen**: Translate wireframe specs into image generation prompts

---

## Hall of Fame Exemplars

### 1. Executive Dashboard Blueprint
```
## Executive Dashboard - Q3 Performance

```
+-------------------------------------------------------------+
| [HEADER]                                                    |
|  Title: Q3 Performance Overview                             |
|  Period Selector [Dropdown: Q1, Q2, Q3, Q4]                 |
+-------------------------------------------------------------+
| [KEY METRICS - GRID 2x2]                                    |
|  +--------------------+  +--------------------+             |
|  | REVENUE            |  | PROFIT MARGIN      |             |
|  | $1.5M (+12% YoY)   |  | 32% (+2% YoY)      |             |
|  +--------------------+  +--------------------+             |
|  +--------------------+  +--------------------+             |
|  | NEW CUSTOMERS      |  | AVG. DEAL SIZE     |             |
|  | 5,200 (+25% YoY)   |  | $2,800 (-5% YoY)   |             |
|  +--------------------+  +--------------------+             |
+-------------------------------------------------------------+
| [VISUALIZATIONS - 2 COLUMNS]                                |
|  +---------------------------+  +---------------------------+
|  | LINE CHART: Monthly Rev   |  | BAR CHART: Product Mix    |
|  | (X: Month, Y: Revenue)    |  | (X: Product, Y: % of Rev) |
|  | Legend: Product A, Prod B |  | Top 5 Products            |
|  +---------------------------+  +---------------------------+
+-------------------------------------------------------------+
| [DATA TABLE]                                                |
|  Top 10 Sales Regions (Sortable by Revenue, New Customers)  |
|  Columns: Region, Revenue, New Customers, Growth (%)        |
+-------------------------------------------------------------+
```
**What makes this excellent**: This wireframe acts as a precise visual contract, leaving zero ambiguity for the AI. Every element, from the header's components to specific chart types, axes, legends, and table columns, is explicitly defined. This embodies the "Visual Contract Protocol" and serves as an "Assumption Assassin," ensuring the AI builds exactly what's intended without costly post-production iteration. It perfectly separates the structural 'what' and 'where' from the aesthetic 'how it looks,' enabling "Taste Arbitrage" in subsequent steps.

### 2. Complex System Diagram for Non-Technical Audience
```
## Simplified API Workflow for [Product Name]

```
+-------------------------------------------------------------+
| [USER]                                                      |
|  Clicks "Submit Request"                                    |
+-------------------------------------------------------------+
      | (Sends Request)
      v
+-------------------------------------------------------------+
| [API GATEWAY]                                               |
|  - Validates Request                                        |
|  - Routes to Service                                        |
+-------------------------------------------------------------+
      | (Validated Request)
      v
+-------------------------------------------------------------+
| [SERVICE A: DATA PROCESSOR]                                 |
|  - Cleans & Formats Data                                    |
|  - Stores in Temporary DB                                   |
+-------------------------------------------------------------+
      | (Processed Data)
      v
+-------------------------------------------------------------+
| [SERVICE B: ANALYTICS ENGINE]                               |
|  - Runs Algorithms                                          |
|  - Generates Insights                                       |
+-------------------------------------------------------------+
      | (Insights)
      v
+-------------------------------------------------------------+
| [DATABASE: RESULTS STORAGE]                                 |
|  - Saves Final Output                                       |
+-------------------------------------------------------------+
      | (Confirmation)
      v
+-------------------------------------------------------------+
| [USER]                                                      |
|  Receives "Request Complete"                                |
+-------------------------------------------------------------+
```
**What makes this excellent**: This exemplar demonstrates the "Complexity Equalizer" pattern. It breaks down a technical API workflow into easily digestible, sequential blocks with clear labels and actions, making it comprehensible even to a non-technical stakeholder. The simplicity of the ASCII flow avoids overwhelming detail, ensuring immediate understanding and facilitating efficient communication about system architecture without deep technical dives.

### Anti-Exemplar: Vague Marketing Landing Page Request
"Design a sleek and modern landing page for our new AI-powered analytics platform. It needs to be super engaging and drive sign-ups. Make sure it has a clear call to action and looks professional."

**What makes this mediocre**: This is a textbook "vibe coding horror story" root cause. The prompt is laden with subjective adjectives ("sleek," "modern," "super engaging," "professional") but entirely lacks structural or content specification. It forces the AI to make dozens of assumptions about layout, element hierarchy, specific content blocks, and CTA placement. This violates the "Assumption Assassin" and "Visual Contract Protocol," leading to expensive, off-target iterations at the high-token production layer and a significant "assumption gap" between human intent and AI execution.

**Note on provenance**: this specific prompt string is an illustrative composition (constructed to demonstrate the pattern), not a line spoken in the source transcript — see `references/source-ledger.md`. The Anti-Patterns (Sourced) section above carries the transcript-verified equivalent: Kashef's own "Build me a SAS dashboard..." lazy-prompt experiment.

## Signature Moves

1.  **The Blueprint Mandate**: Always initiates any visual design task by requesting an ASCII wireframe, explicitly stating "Before writing any [output type], create an ASCII wireframe of [specifications]." This establishes the "Visual Contract Protocol" from the outset.
    → **Deploy when**: Any new visual output (dashboard, slide, landing page, diagram, email template) is requested.

2.  **Taste-Logic Arbitrage**: In separate prompts, first defines the structural layout and content hierarchy in a wireframe, and *only then* provides aesthetic or styling instructions for the final build. This ensures "Taste Arbitrage" by preventing mixing of cognitive tasks.
    → **Deploy when**: Transitioning from wireframe approval (structure and content) to final design execution (aesthetics and polish).

3.  **Surgical Refinement Loop**: Responds to initial wireframes with precise, numbered, and scoped modification requests (e.g., "Two changes only. 1. Make the line chart wider than the pie chart. 2. Change active/green to inactive/gray. Redraw the full wireframe.") to leverage the "Progressive Refinement Engine."
    → **Deploy when**: An initial wireframe needs specific, targeted adjustments before final approval.

4.  **The Orchestrator's Hand-off**: Concludes the wireframing phase by explicitly instructing the AI: "Build this using the wireframe as the exact specification. Focus on making it beautiful and modern within these aesthetic guidelines: [brief aesthetic notes]." This embodies the "Orchestrator Identity Shift" where the human is the creative director.
    → **Deploy when**: The final wireframe is approved and ready for production-level rendering.

## Expert-Specific Quality Rubric

| Criterion                         | Score 4 (Acceptable)                                 | Score 7 (Good)                                                     | Score 10 (Savant)                                                          |
| :-------------------------------- | :--------------------------------------------------- | :----------------------------------------------------------------- | :------------------------------------------------------------------------- |
| **1. Wireframe as Visual Contract** | Wireframe provides a general idea; some elements are vague or implied. | Wireframe defines most major elements and their relative placement. | Wireframe is an unambiguous 1:1 blueprint; every element's content, type, and location is explicitly defined. No room for interpretation. |
| **2. Assumption Elimination Score** | Wireframe still requires AI to infer several design choices (e.g., specific chart types, button labels). | Minor assumptions remain, mostly concerning aesthetic details, not core structure or content. | Zero implicit assumptions. Every structural, content, and functional element is explicitly stated or represented in the wireframe.          |
| **3. Iteration Granularity**      | Wireframe requires significant re-drawing for minor changes, or changes are described vaguely. | Wireframe allows for clear, moderate changes without full re-conceptualization. | Wireframe is designed for surgical, token-efficient edits (e.g., "move X left," "change Y to Z") with minimal redrawing, reflecting "Progressive Refinement." |
| **4. Cognitive Task Segregation** | Wireframe attempts to specify colors, fonts, or other aesthetic details, mixing layout with style. | Wireframe primarily focuses on layout but includes some light aesthetic notes that could be deferred. | Wireframe *only* defines structure, content placement, and hierarchy. All aesthetic concerns are explicitly deferred to a separate production-layer prompt, embodying "Taste Arbitrage." |
| **5. Complexity Compression Index** | Diagram is overly complex, requiring deep domain knowledge to interpret. | Diagram simplifies some concepts but might still be overwhelming for a layperson. | Diagram reduces complex systems or data into an immediately understandable visual structure, accessible to a "seventh grader," demonstrating "Complexity Equalizer." |
| **6. Output Fidelity to Wireframe** | Final output deviates significantly from the wireframe's layout or element inclusion. | Final output largely matches the wireframe, with minor discrepancies. | Final output is a pixel-perfect (or functionally equivalent) translation of the wireframe. Every element specified in the wireframe is present and correctly positioned in the output. |
| **7. Token Economy Adherence**     | Process involves multiple high-token iterations at the design/code layer before wireframe finalization. | Some iteration occurs at the design/code layer, but wireframe is the primary iteration point. | Iteration is almost exclusively confined to the low-token wireframe layer, achieving 60-80% token reduction before final production, as per "Token Economist." |
