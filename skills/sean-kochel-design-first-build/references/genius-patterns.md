# Sean Kochel — Design-First Web Building — Genius Patterns

## 1. The Under-Specified Plan Diagnosis

**What They Do**: Identifies that every failed vibe-coded project traces to the same root cause — unanswered questions in the brief that the LLM must improvise at generation time. "Any unanswered question in your plan has to be decided upon by the language model at game time."

**Executable Behavior**: Before any build prompt, audit your brief for gaps. Every undefined element (audience, tone, structure, competitor landscape, positioning angle) = a coin flip the LLM makes for you. Fill every gap with research, not imagination. Zero tolerance for "I'll figure it out later."

**Deploy When**: Starting ANY AI-assisted build — landing pages, web apps, mobile apps, marketing assets. This is the universal pre-flight check.

**Success Metric**: You can answer every question about audience, positioning, structure, visual direction, and section content BEFORE the first build prompt fires. Zero blanks.

---

## 2. The Research → Design → Build Trinity

**What They Do**: Never collapse the pipeline. Three categorical steps, three different tools, three different outputs. Research produces intelligence. Design produces visuals. Build produces code. They do not blend.

**Executable Behavior**: Enforce hard phase gates. Research phase uses deep research tools (ChatGPT Deep Research, Gemini, Claude). Design phase uses visual tools (Google Stitch, Figma). Build phase uses code tools (Antigravity, Cursor, VS Code). Each phase produces a deliverable that gets reviewed before the next begins.

**Deploy When**: Building any customer-facing visual asset where quality matters. This is especially critical for client work and revenue-generating pages.

**Success Metric**: Phase 1 deliverable = competitive research doc. Phase 2 deliverable = approved visual mockup. Phase 3 deliverable = working code. Each reviewed independently.

---

## 3. Direct vs. Indirect Competitor Mapping

**What They Do**: Expand the competitive frame beyond obvious competitors. Direct competitors sell the same solution. Indirect competitors solve the same problem differently. The personal trainer's indirect competitor is Ozempic — same problem, wildly different approach.

**Executable Behavior**: For any project, map at least 2 direct competitors (same product category) AND 2 indirect competitors (different approach to same underlying problem). Extract from each: headline language, USP, brand identity, and page structure. The indirect competitors often reveal the most powerful positioning insights because they show what else your audience is considering.

**Deploy When**: Starting competitive research for any positioning, landing page, or product strategy work.

**Success Metric**: Your competitor map includes both categories, and the indirect competitors have surfaced at least one positioning insight you wouldn't have found from direct competitors alone.

---

## 4. The Competing Hypotheses Technique

**What They Do**: Refuse to lock into a single positioning angle. Generate 3 distinct approaches — e.g., efficiency-focused, quality-focused, personalization-focused — and consciously evaluate each before committing. This prevents the default failure mode of going with the first idea that sounds decent.

**Executable Behavior**: After competitive research, generate exactly 3 competing hypotheses for positioning. Each must be genuinely distinct (not variations of the same theme). Each gets mapped to a concrete headline, subheadline, and CTA. Evaluate against the target audience, then select. Document why the others were rejected.

**Deploy When**: Any time you need a positioning angle, headline, or core message for a page, product, or campaign.

**Success Metric**: 3 distinct angles generated, consciously evaluated, and one selected with reasoning. The chosen angle is demonstrably better than the default first-instinct option would have been.

---

## 5. Design Quality as Subconscious Authority

**What They Do**: Treat visual quality not as aesthetic preference but as a conversion mechanism. "Quality design is a subconscious authority signal. People are attracted to authority figures like moths to a flame." Perceived authority is a "needle mover you can possibly imagine."

**Executable Behavior**: Invest in visual polish proportional to business impact. A landing page that looks beautiful converts better — not because beauty sells, but because beauty signals authority, and authority builds trust. When choosing between "ship faster" and "ship prettier," recognize that the visual quality IS the product for first impressions.

**Deploy When**: Any customer-facing deliverable where trust or authority influences conversion.

**Success Metric**: A first-time visitor forms an impression of authority and professionalism BEFORE reading any copy.

---

## 6. The Structure-Before-Copy Sequencing

**What They Do**: Design the visual scaffolding WITHOUT real copy first, then layer copy in as a second pass. This counterintuitive sequencing produces better designs than doing both simultaneously. When you give a design tool all the copy upfront, "it tends to give you a pretty mid-level design."

**Executable Behavior**: In design tools, start with layout, typography, color palette, and visual rhythm using placeholder text. Get the aesthetic locked. THEN swap in the researched copy as a second generation. The design tool optimizes layout differently when it isn't trying to accommodate specific text.

**Deploy When**: Using any AI design tool (Google Stitch, v0, Figma AI) to generate page designs.

**Success Metric**: The visual direction is approved before real copy is introduced. The copy integration pass preserves the design quality while adding specificity.

---

## 7. The MCP Bridge Pattern

**What They Do**: Use MCP servers as the lossless bridge between design tools and development environments. Instead of downloading screenshots and hoping the LLM can clone them, or exporting raw HTML and trying to extract design tokens — connect the tools directly. "Both of those approaches kind of sucked."

**Executable Behavior**: Set up MCP server for the design tool (Google Stitch → Stitch MCP) in your IDE. Install the companion skill library so the LLM understands the design system natively. Issue a single build command referencing the design project. The skills extract the design system and build every component to spec.

**Deploy When**: You have an approved design in a tool that offers MCP integration and need to translate it to working code.

**Success Metric**: The built output matches the approved design — same colors, typography, spacing, and component patterns — without manual CSS translation.
