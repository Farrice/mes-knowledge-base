# Mark Kashef Visual Blueprint Methodology — Genius Context

> Load this file before executing any workflow. It contains the integrated genius patterns and hidden knowledge that inform every visual planning operation.

---

## The Core Insight

Using ASCII art wireframes as a **visual contract** between human intent and AI execution. This eliminates the most expensive failure mode in AI-augmented design: **the assumption gap**. Humans provide taste and spatial judgment. AI handles execution beauty. The wireframe is the bridge.

---

## 8 Genius Patterns

### 1. Visual Contract Protocol
Force every visual project through a blueprint phase where BOTH human and AI agree on spatial layout before any production work begins. The wireframe IS the specification — not a suggestion, not an inspiration board. It's the contract.

### 2. Assumption Assassin
AI failure in visual work almost always stems from **unstated assumptions**, not capability gaps. Every element you don't specify in the wireframe is an element the AI will assume. Assumptions compound. Three unstated assumptions across ten elements = 30 divergence points. The wireframe makes the invisible visible.

### 3. Token Economist
All iteration happens at the wireframe layer (~50 tokens per change) instead of the code/design layer (~5,000 tokens per change). Slide decks are especially token-intensive — 5-6 code-layer iterations can exhaust an entire context window. Wireframe-first reduces token spend by 60-80%.

### 4. Taste Arbitrage
Separate the **thinking** (layout, structure, relationships, hierarchy) from the **beauty** (colors, typography, spacing, polish). In the wireframe, specify WHAT goes WHERE and WHY. In the build prompt, tell AI to focus on making it beautiful. Never mix these two cognitive tasks.

### 5. Progressive Refinement Engine
Use multi-turn conversation at the wireframe layer for surgical edits: "Two changes only. Make the line chart wider than the pie chart. Change active/green to inactive/gray. Redraw the full wireframe." Small, numbered, scoped changes. Each iteration takes <30 seconds.

### 6. Complexity Equalizer
Visual diagrams make technical concepts (database schemas, SQL relationships, API structures) accessible to non-technical stakeholders. If a diagram "looks like gibberish," request simplification: "Make this diagram as if you're in seventh grade." The visualization forces comprehension — if you can't wireframe it, you don't understand it.

### 7. Multi-Vertical Blueprint
The SAME protocol works identically across radically different output types — dashboards, landing pages, slide decks, databases, email templates, PDFs, infographics. It's a universal cognitive protocol. The pattern: "Before writing any [output type], create an ASCII wireframe of [specifications]."

### 8. Orchestrator Identity Shift
The human becomes **creative director**, not prompt engineer. You sketch the blueprint. You approve the wireframe. You greenlight production. The AI is your production team. You focus on vision, taste, and approval gates. AI focuses on execution at the production layer.

---

## 6 Hidden Knowledge Items

### The Lazy Prompt Firewall
Even LAZY prompts produce acceptable output when preceded by wireframes. The wireframe carries 80% of the specification load, so the build prompt can be simple. This is a firewall against prompting incompetence.

### The Figma Killer Insight
This eliminates the whiteboard → design team → Figma → development team pipeline. A 2-minute wireframe session replaces a $50K+/year design pipeline role.

### The Secret Slide Deck Revenue Play
Mark has used this for client slide decks for 6 months as a professional, revenue-generating technique. Slide decks are the highest-ROI use case because of token economics (slides are extremely token-expensive to iterate at the code layer).

### Visualization-as-Understanding
ASCII diagrams aren't just for planning — they're for **learning**. Use them to understand every new feature, concept, or system. The visualization forces comprehension at a level that text alone cannot achieve.

### The Vibe Coding Horror Stories Root Cause
Most AI development failures are human failures of specification, not AI failures of execution. "A lot of vibe coding horror stories just come from poor planning." The wireframe solves a PLANNING problem.

### Skills From Diagrams (Meta-Pattern)
ASCII wireframes can be used to DESIGN AI skills, agent architectures, and workflow topologies themselves. It's recursive — use the visual method to design the visual method.

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

## Stacking Protocol

When used with other skills:
- **Before Banana Squad**: Wireframe the composition/layout before image generation
- **Before Kittl/Design**: Wireframe graphic layouts before production
- **Before `/design-first-build`**: Wireframe IS the design-first artifact
- **With Oren CEV**: Apply taste critique to wireframes before production
- **With any slide/deck work**: ALWAYS wireframe slides first (token economics mandate)
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
