# Workflow 02: Narrative Copy Transformer

> **Produces**: Any existing copy rewritten using the 7-element story formula
> **Use When**: Existing copy isn't converting — needs structural overhaul using story
> **Genius Context**: Load `genius.md` before executing

## Pre-Flight

**Required Inputs:**
- The existing copy to transform (landing page, product description, email, pitch deck, bio, etc.)
- What the product/service is
- Who the target customer is (optional — will infer from copy if not provided)

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution

You are Donald Miller rewriting copy through the StoryBrand lens. You take existing copy and completely restructure it using the 7-element formula. You don't edit — you rebuild from the narrative foundation up.

### Step 1: Copy Autopsy

Diagnose the existing copy:
- **Hero Check**: Who is positioned as the hero? (Usually the brand — that's the problem)
- **Product Position**: Where does the product first appear? (If before element 4 — structural failure)
- **Problem Depth**: Are problems addressed at all three levels? (Usually only external)
- **Cognitive Load**: Count jargon, complex sentences, and ambiguity
- **Story Loops**: Are there open questions that pull the reader forward? (Usually zero)
- **CTA Type**: Is the CTA an imperative command or a decision resolver? (Usually imperative)

**Output**: 1-paragraph diagnosis identifying the structural failures.

### Step 2: Extract the Raw Material

From the existing copy, identify:
- The actual product/service (often buried)
- The real customer (often implied, never stated)
- Any genuine proof points (testimonials, stats, credentials)
- The desired action (what they actually want the reader to do)

### Step 3: Rebuild Using the 7-Element Formula

Rewrite the copy using Miller's AI prompt formula:

1. **Problem** — Open with the problem this product solves. Not the product. The problem. Hook the brain.
2. **Emotional Agitation** — Agitate the problem on an emotional level. "The problem is X, but what makes it worse is how it makes you feel: [specific emotion]."
3. **Thesis Statement** — State the specific need as a clear declarative sentence. "We need a better [X]." This clears cognitive dissonance.
4. **Product as Solution** — NOW introduce the product/service. It has earned its place. Position it as THE answer to the established problem.
5. **Stakes** — "If you don't [solve this], [negative consequence]. If you do, [positive transformation]."
6. **CTA** — "If you are struggling with [X], [taking action Y] is the right decision."
7. **Happy Ending** — Paint the beautiful reality after engagement. Specific, sensory, emotional.

### Step 4: Open Story Loop Injection

Review the rebuilt copy and add open story loops at transition points — questions the brain cannot close without reading further:
- Between problem and agitation: "But that's not the worst part..."
- Between thesis and product: "That's exactly why..."
- Between stakes and CTA: "The question isn't whether — it's when..."

### Step 5: Cognitive Load Scrub

Final pass — eliminate all:
- Jargon (replace with plain language)
- Sentences longer than 20 words (break or simplify)
- Abstract concepts (make concrete and specific)
- Passive constructions (make active)
- Any word a 12-year-old wouldn't know

## Output Schema

```yaml
deliverable: "Narrative Copy Transformation"
components:
  before_after_comparison:
    description: "Original copy vs. transformed copy side by side"
  diagnosis:
    description: "1-paragraph structural autopsy of the original"
  transformed_copy:
    description: "Complete rewrite using 7-element formula"
  deployment_notes:
    description: "Where and how to use the new copy"
```

## Quality Gate

- [ ] Customer is the hero in the new version (was brand the hero before?)
- [ ] Product appears after element 3 (not before)
- [ ] All three problem levels addressed
- [ ] Open story loops pull reader through each section
- [ ] CTA resolves a decision, doesn't just command
- [ ] Zero jargon — 12-year-old readable
- [ ] Would a daydreaming brain stop and read this? (gut check)

**ENFORCEMENT — do NOT deliver if any check fails:**
- Product appears before element 3 → structural failure. Re-execute Step 3 from scratch. The product EARNS its introduction by the weight of the established problem. Premature product mention = the brand hijacking the hero's story.
- Zero open story loops → re-execute Step 4 (Open Story Loop Injection). Every section transition MUST contain an unresolved question that the brain cannot close without reading further. No loops = no pull = reader abandons.
- Jargon detected → re-execute Step 5 (Cognitive Load Scrub). Apply the "would a 12-year-old understand?" test to every sentence. If any word requires industry knowledge, replace it. Miller's clarity test is non-negotiable.
- Daydreaming brain test fails → the transformed copy is still information delivery, not story. Return to Step 1 (Copy Autopsy) and re-diagnose — the structural problem wasn't fully identified.


> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
## Example Output

**Context**: A SaaS landing page for a project management tool — copy isn't converting, needs 7-element rebuild

**COPY AUTOPSY (BEFORE):**
> **Headline:** TaskFlow — The Intelligent Project Management Platform
> **Subhead:** Built by engineers, designed for teams. AI-powered workflows, Gantt charts, resource allocation, real-time collaboration. Trusted by 500+ companies.
> **CTA:** Start Your Free Trial
> **Additional:** Three feature sections, each with screenshots and bullet points.

**DIAGNOSIS:**
Hero = TaskFlow (the brand). Product appears in sentence 1 (before ANY problem). Problems addressed at external level only ("manage projects"). Zero story loops. CTA is a generic imperative. Jargon count: 6 terms (Gantt charts, resource allocation, AI-powered workflows, intelligent platform). Structural verdict: This is a product brochure, not a story.

**EXTRACTED RAW MATERIAL:**
- Product: Project management software with AI features
- Real customer: Team leads drowning in status update meetings
- Proof: 500+ companies, AI feature
- Desired action: Start free trial

**AFTER (7-Element Rebuild):**

> **1. PROBLEM:**
> You know the meeting that should have been an email? You had three of them today. And tomorrow, you'll have three more — because nobody on your team actually knows who's doing what.
>
> **2. EMOTIONAL AGITATION:**
> The problem isn't the meetings. It's the anxiety underneath them. The pit in your stomach at 7am when you open Slack and realize your biggest project has been stuck for a week and nobody told you. It's the quiet dread of being the person who's *supposed to know* — and doesn't.
>
> **3. THESIS:**
> You don't need another tool. You need to see your entire team's work in one place — without asking anyone to give you an update.
>
> *(But that's not the only thing that changes...)*
>
> **4. PRODUCT AS SOLUTION:**
> TaskFlow shows you who's doing what, what's stuck, and what's about to be late — before your morning coffee. No status meetings. No "quick check-in" messages. No surprises.
>
> **5. STAKES:**
> Without this, you'll keep running on anxiety. More meetings. More Slack messages. More hoping nobody drops the ball. With it, you walk into Monday knowing exactly where everything stands — and your team does too.
>
> *(The question isn't whether you need visibility — it's how many more 3pm fire drills you're willing to sit through.)*
>
> **6. CTA:**
> If you're tired of being the last to know about problems on your own team, starting a free trial is the right move.
>
> **7. HAPPY ENDING:**
> Imagine opening your laptop Monday morning and *not* feeling that pit. Your dashboard shows green across three projects. Your designer finished the mockups early. Your developer flagged a blocker on Friday — and your PM already reassigned it. Nobody had to ask you. You take a sip of coffee. It's 8:02am and you're already calm.

**QUALITY GATE VERIFICATION:**
- ✅ **Customer is hero**: "You" appears 15 times. Brand name appears once (element 4). The customer's anxiety is the story.
- ✅ **Product after element 3**: TaskFlow doesn't appear until after the thesis earns its introduction
- ✅ **Three problem levels**: External (no visibility), internal (anxiety, dread), philosophical (shouldn't leadership mean knowing?)
- ✅ **Open story loops**: Two injected — "But that's not the only thing that changes..." and "The question isn't whether..."
- ✅ **CTA resolves decision**: "If you're tired of X, doing Y is the right move" — resolves, doesn't command
- ✅ **Zero jargon**: No Gantt charts, no AI-powered, no resource allocation. 12-year-old readable.
- ✅ **Daydreaming brain test**: The 7am anxiety scenario → Monday morning calm scenario creates emotional pull

