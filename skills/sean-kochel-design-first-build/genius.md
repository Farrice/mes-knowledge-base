# Sean Kochel: Design-First Web Building — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## How to Use This Skill (Model Calibration)

These are intuition primitives, not a checklist. Internalize the phase discipline, then build originally — the machinery should be invisible in what ships, even though it is rigid in how you got there. The test: would Sean Kochel recognize this as his research → design → build trinity — three categorical phases, three different tools, one discrete reviewable deliverable per phase — or as generic "AI website builder" vocabulary wearing his terminology? If it's the second, rebuild.

Specifically:
- Do NOT label the final deliverable "Phase 1: Research," "Phase 2: Design," "Phase 3: Build" as a visible scaffold the client sees. The phases are how you WORK, not a section header in the output. Kochel never narrates his own system while running it in the video — he just runs it, then shows the result.
- Do NOT skip straight to a build prompt because research "feels like busywork." He names this directly as the majority failure mode — "99% of people skip this step" — and the urge to skip is itself the strongest signal you need it most.
- Do NOT hand a design tool the full draft copy on the first pass. His texture is *sequenced*, not *simultaneous*: scaffold first, copy second, always in that order, even when simultaneous feels faster — feeding it all the copy upfront is what produces "a pretty mid-level design."
- His delivery register is unpolished workshop demo, not academic whitepaper — numbered systems narrated like a screen recording ("boom," "moment of truth"), not framework slides. Keep instructional language plain and demonstrative: show the before/after, don't theorize about why it works.
- Polish-is-the-tell for this expert inverts the usual warning: the failure mode isn't over-polish, it's under-sequencing — a landing page that LOOKS finished but skipped the competing-hypotheses step reads as authoritative and is actually unaudited guesswork wearing a good coat of paint. Design quality without research underneath is exactly the "Just Build It Brochure Site" anti-pattern below, not a win.

## Genius Patterns

## 1. The Under-Specified Plan Diagnosis

**What They Do**: Identifies that every failed vibe-coded project traces to the same root cause — unanswered questions in the brief that the LLM must improvise at generation time. "Any unanswered question in your plan has to be decided upon by the language model at game time."

**Executable Behavior**: Before any build prompt, audit your brief for gaps. Every undefined element (audience, tone, structure, competitor landscape, positioning angle) = a coin flip the LLM makes for you. Fill every gap with research, not imagination. Zero tolerance for "I'll figure it out later."

**Deploy When**: Starting ANY AI-assisted build — landing pages, web apps, mobile apps, marketing assets. This is the universal pre-flight check.

**Success Metric**: You can answer every question about audience, positioning, structure, visual direction, and section content BEFORE the first build prompt fires. Zero blanks.

---

## 2. The Research → Design → Build Trinity

**What They Do**: Never collapse the pipeline. Three categorical steps, three different tools, three different outputs. Research produces intelligence. Design produces visuals. Build produces code. They do not blend. In his own words: "there's three pieces to this system. research, design, and finally build" (video transcript, extractions/sean-kochel/transcript.txt).

**Executable Behavior**: Enforce hard phase gates. Research phase uses deep research tools (ChatGPT Deep Research, Gemini, Claude). Design phase uses visual tools (Google Stitch, Figma). Build phase uses code tools (Antigravity, Cursor, VS Code). Each phase produces a deliverable that gets reviewed before the next begins.

**Deploy When**: Building any customer-facing visual asset where quality matters. This is especially critical for client work and revenue-generating pages.

**Success Metric**: Phase 1 deliverable = competitive research doc. Phase 2 deliverable = approved visual mockup. Phase 3 deliverable = working code. Each reviewed independently.

---

## 3. Direct vs. Indirect Competitor Mapping

**What They Do**: Expand the competitive frame beyond obvious competitors. Direct competitors sell the same solution. Indirect competitors solve the same problem differently. His own example, verbatim: "An indirect competitor might be jabbing yourself with a pharmaceutical to lose weight" (video transcript) — same problem as a personal trainer, wildly different approach.

**Executable Behavior**: For any project, map at least 2 direct competitors (same product category) AND 2 indirect competitors (different approach to same underlying problem). Extract from each: headline language, USP, brand identity, and page structure. The indirect competitors often reveal the most powerful positioning insights because they show what else your audience is considering.

**Deploy When**: Starting competitive research for any positioning, landing page, or product strategy work.

**Success Metric**: Your competitor map includes both categories, and the indirect competitors have surfaced at least one positioning insight you wouldn't have found from direct competitors alone.

---

## 4. The Competing Hypotheses Technique

**What They Do**: Refuse to lock into a single positioning angle. Generate 3 distinct approaches — e.g., efficiency-focused, quality-focused, personalization-focused — and consciously evaluate each before committing. In the video's own example, one hypothesis lands on the "efficiency and scaleoriented approach" (video transcript, verbatim) while the others cover quality/nuance and personalization. This prevents the default failure mode of going with the first idea that sounds decent.

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

## Hidden Knowledge

## 1. The 99% Skip

**Tacit Insight**: 99% of people skip competitive research entirely. They jump straight to "build me a beautiful landing page." This is the #1 reason AI-built websites fail — not bad code, not ugly design, but speaking to nobody in particular because the creator never researched who they're speaking to. "You cannot hit a target that you have not defined."

**Why Others Miss This**: Competitive research feels like busywork when AI tools make building feel instant. Why spend 30 minutes researching when you can have a page in 30 seconds? The answer: the 30-second page converts at near-zero because every decision was made by an LLM guessing.

**Deploy When**: Any time you feel the urge to skip research and jump to building. The urge to skip is the strongest signal that you NEED it most.

---

## 2. Landing Pages Are Solved Architecture

**Tacit Insight**: Landing page structure is essentially a solved problem. They virtually always follow: hero (headline + subheadline + CTA) → social proof → features/benefits → how it works → pricing → FAQ. The competitive advantage isn't structural innovation — it's how precisely each section is filled with language that matches a specific person's pain.

**Why Others Miss This**: People think they need novel page structures. They don't. Novel structure confuses visitors. The value is in the copy within the familiar structure — specifically, copy derived from competitive research about what makes YOUR solution different for YOUR specific person.

**Deploy When**: Designing any landing page. Don't reinvent the wheel on structure; invest your creative energy in copy and visual design within the proven structure.

---

## 3. Stitch's Design Quality Inversely Correlates with Copy Completeness

**Tacit Insight**: When you feed Google Stitch (or similar AI design tools) all your copy upfront, the designs come out "pretty mid." When you let it design the aesthetic scaffolding first (layout, color, typography, visual rhythm) with placeholder text, and THEN swap in real copy, the designs are significantly better. The tool optimizes layout differently when it's not burdened with accommodating specific text lengths.

**Why Others Miss This**: It feels logical to give the tool everything at once. More context = better output, right? In THIS case, no. The design optimization and the copy optimization compete with each other when done simultaneously. Separating them produces better results in both dimensions.

**Deploy When**: Using any AI design tool for page generation. Always run two passes: aesthetic first, copy second.

---

## 4. Style Keywords as Compressed Design Systems

**Tacit Insight**: A single design keyword — "claymorphism," "glassmorphism," "brutalist," "neobrutalist" — functions as an entire compressed design system. It encodes typography choices, color theory, spacing patterns, shadow behavior, border radius, texture, and visual rhythm in a SINGLE WORD. Adding or changing this keyword completely transforms the output from the same underlying content.

**Why Others Miss This**: People describe their desired aesthetic in paragraphs when a single keyword does more work. These keywords tap into the training data's understanding of established design movements, producing more coherent visual systems than trying to describe each element individually.

**Deploy When**: Generating design variations in AI design tools. Test 2-3 style keywords on the same scaffolding to rapidly explore radically different aesthetics.

---

## 5. Image-as-Style-Transfer

**Tacit Insight**: Pasting a single reference image (a video thumbnail, a brand asset, a screenshot you like) communicates more about desired aesthetic than paragraphs of written description. The design tool extracts color palette, vibe, texture, composition, and "design DNA" from the image — producing outputs with visual coherence that text prompts struggle to achieve. Kochel's own demo did exactly this with a newsletter thumbnail: "it kind of took that essence and turned it into an entirely new thing" (video transcript, verbatim).

**Why Others Miss This**: People think in terms of text descriptions ("dark mode, purple accent, clean layout"). But an image carries thousands of implicit design decisions — the exact shade of dark, the weight of the typography, the density of elements, the amount of whitespace. One image transmits all of this instantly.

**Deploy When**: You have a reference that captures the "vibe" you want — a screenshot, thumbnail, brand asset, or even a photo. Paste it as style input instead of (or in addition to) text descriptions.

---

## Anti-Patterns

Every item below is a failure mode Sean Kochel names directly against his own patterns above, anchored to the source video (see `references/source-ledger.md` for full provenance):

- Prompting straight to "build me a beautiful landing page" with zero competitive research — the majority failure mode he calls out by name: "you cannot hit a target that you have not defined" (video transcript, extractions/sean-kochel/transcript.txt).
- Leaving the brief under-specified and letting the model guess — "Any unanswered question in your plan has to be decided upon by the language model at game time" (video transcript) — this is the single philosophical takeaway he leads the video with.
- Handing an AI design tool the full draft copy before the visual scaffolding is locked — doing so "tends to give you a pretty mid-level design" (video transcript), the opposite of the two-pass sequencing he teaches.
- Downloading a screenshot and hoping the build tool pixel-clones it, or exporting raw HTML and hand-extracting the design system — the two workarounds he explicitly rejects in favor of the MCP bridge: "Both of those approaches kind of sucked to be honest" (video transcript).
- Mapping only direct competitors and skipping indirect ones — his own corrective example is the personal trainer who never checks what "jabbing yourself with a pharmaceutical to lose weight" competitors are offering instead (video transcript, verbatim quote).
- Locking into the first positioning idea that sounds decent instead of generating competing hypotheses — the default failure mode the competing-hypotheses technique exists to prevent, demonstrated in the video's own efficiency-vs-quality-vs-personalization split (video transcript).

## Hall of Fame Exemplars

> Provenance note: the two named case studies and the anti-exemplar below are illustrative composites built to demonstrate the patterns in combination — they do not appear in the source video or extraction report and are not documented Kochel client engagements. Treat them as worked examples of the mechanics, not as verified case history (labeled UNCONFIRMED in `references/source-ledger.md`). The patterns they illustrate are themselves grounded in the transcript.

**1. "The SaaS Onboarding Flow That Just *Clicked*"**
*   **Description**: A complex B2B SaaS onboarding flow for a new project management tool. Instead of immediately building, the team spent a full week on competitive research, mapping 3 direct and 2 indirect competitors (e.g., email-based task managers, even physical Kanban boards). This led to three distinct positioning hypotheses: "Hyper-Efficient Task Automation," "Collaborative Project Storytelling," and "Focus-Driven Workflow Simplification." After selecting "Focus-Driven Workflow Simplification," a visual mockup was created in Google Stitch using placeholder text, focusing purely on clean layout, intuitive navigation, and a calming color palette. Only after design approval was the precise, research-backed copy integrated, ensuring the visual authority reinforced the precise messaging. The final code was generated via an MCP bridge, perfectly replicating the Stitch design.
*   **What makes this excellent**: Exemplifies the full "Research → Design → Build Trinity," "Under-Specified Plan Diagnosis" by filling all gaps, "Direct vs. Indirect Competitor Mapping" for unique insights, "Competing Hypotheses Technique" for deliberate positioning, "Design Quality as Subconscious Authority" for trust, "Structure-Before-Copy Sequencing" for optimal design output, and "The MCP Bridge Pattern" for lossless translation.

**2. "The 'Claymorphism' Conversion Beast"**
*   **Description**: A landing page for a new AI-powered copywriting tool. The initial brief was vague. Sean's team enforced the "Under-Specified Plan Diagnosis," detailing target audience pain points, unique selling propositions against both direct competitors (other AI writers) and indirect (human copywriters, content agencies). During the design phase, instead of generic descriptors, the team tested the style keyword "claymorphism" in Google Stitch with placeholder content. This single keyword generated a distinct, tactile, and visually authoritative aesthetic. Once the aesthetic was locked, the researched, pain-point-focused copy was integrated. The page achieved 3x higher conversion rates than a previous, generic design.
*   **What makes this excellent**: Demonstrates the power of "The Under-Specified Plan Diagnosis" in pre-empting LLM improvisation, "Style Keywords as Compressed Design Systems" for rapid and coherent aesthetic exploration, "Design Quality as Subconscious Authority" driving conversion, and "Structure-Before-Copy Sequencing" for superior visual output.

**Anti-Exemplar: "The 'Just Build It' Brochure Site"**
*   **Description**: A startup founder, eager to launch, prompted an AI builder: "Build me a modern, clean website for my new productivity app." No competitive research was done, no specific audience defined, no unique positioning considered. The AI generated a visually acceptable but generic site with boilerplate copy. The founder then tried to force-fit their actual product messaging into the pre-existing structure, resulting in awkward phrasing and a diluted value proposition. The site garnered minimal interest, with visitors quickly bouncing because it didn't speak to their specific problem or offer a compelling reason to stay.
*   **What makes this mediocre**: A direct violation of "The 99% Skip" (no research), "Under-Specified Plan Diagnosis" (unanswered questions), and "Research → Design → Build Trinity" (collapsed phases). The resulting site lacks authority and specific appeal, confirming that "you cannot hit a target that you have not defined."

## Signature Moves

*   **The Pre-Flight Brief Audit**: Before *any* build prompt fires, rigorously review the project brief for *every* unanswered question regarding audience, tone, structure, competitors, and positioning. If a single blank exists, halt and research. → **Deploy when**: Initiating any AI-assisted web build or design task.
*   **The Tri-Phase Lock-Down**: Enforce strict, sequential phase gates for Research, Design, and Build. Each phase uses distinct tools, produces a specific deliverable (e.g., research doc, approved mockup, working code), and requires independent review before proceeding to the next. → **Deploy when**: Managing any end-to-end web project, especially for clients or revenue-generating assets.
*   **The Indirect Competitor Hunt**: Systematically identify at least two indirect competitors (solving the same problem differently) in addition to direct ones. Analyze their headlines, USP, brand identity, and page structure for novel positioning insights. → **Deploy when**: Beginning competitive research for any new product, page, or campaign.
*   **The Aesthetic Scaffolding Pass**: When using AI design tools, always generate the visual layout, typography, color palette, and rhythmic flow using placeholder text first. Lock the aesthetic, then perform a second pass to integrate the actual, specific copy. → **Deploy when**: Utilizing AI design tools (e.g., Google Stitch, v0) for initial page mockups.
*   **The Style Keyword Blitz**: Rapidly explore diverse aesthetic directions by applying single, powerful design keywords (e.g., "claymorphism," "brutalist," "glassmorphism") or a single reference image to the same foundational content. Observe how these compressed design systems instantly transform the visual output. → **Deploy when**: Seeking to establish a distinct visual identity or explore aesthetic variations quickly.

## Quality Rubric

> Detailed scoring rubric: `references/quality-rubric.md` — load on-demand for grading. The rubric scores each criterion on a 4/7/10 scale (Acceptable/Good/Savant); a Savant-tier landing page brief shows zero unanswered questions, not partial credit.
