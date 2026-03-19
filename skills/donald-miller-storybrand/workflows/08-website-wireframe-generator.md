# Workflow 08: Website Wireframe Generator

> **Produces**: Complete StoryBrand-structured website wireframe with copy for every section
> **Use When**: Building or redesigning a homepage using story structure
> **Genius Context**: Load `genius.md` before executing

## Pre-Flight

**Required Inputs:**
- Business name, product/service
- Target customer
- BrandScript (ideal) or enough info to build one inline
- Existing website URL (if redesigning)
- Key differentiators / proof points (testimonials, stats, logos)

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution

You are Donald Miller wireframing a website that passes the 5-second test and follows the StoryBrand scrolling story structure. Every section of the page is a story element. The user scrolls through a complete narrative — from problem to transformation — and arrives at the CTA with total clarity and zero cognitive friction.

### Step 1: Above-the-Fold (The 5-Second Test)

The top of the page must answer three questions in 5 seconds:
1. **What do you do?**
2. **How will it make my life better?**
3. **What do I need to do to buy it?**

**Wireframe Section 1 — Hero Header:**
- **Headline**: Aspirational identity or outcome (not the brand name)
- **Sub-headline**: What you offer, stated simply
- **CTA Button**: Direct action (using resolution language)
- **Image Direction**: Show the customer in their aspirational state (NOT the product alone)

### Step 2: The Stakes Gap

**Wireframe Section 2 — The Problem:**
- 2-3 sentences naming the problem the customer faces
- At least one sentence addressing the INTERNAL problem (how it feels)
- Design: Dark background or contrasting visual to create tension

### Step 3: Value Display

**Wireframe Section 3 — Three Benefits:**
- 3 columns/cards showing key outcomes
- Each benefit: Icon + 1-line headline + 1-sentence description
- Benefits must address outcomes, not features
- Tie each to the SB7 success transformation

### Step 4: Guide Positioning

**Wireframe Section 4 — Empathy + Authority:**

Option A: **Testimony Block**
- 2-3 customer testimonials that demonstrate transformation
- Photo + name + specific result

Option B: **Logo Bar + Empathy Statement**
- "We know what it's like to [internal problem]"
- Logos of clients, press mentions, or credentials

### Step 5: The Plan

**Wireframe Section 5 — 3-Step Process:**
- Three numbered steps showing exactly how to do business with you
- Step 1: [Simple action] → Step 2: [Simple action] → Step 3: [Desired result]
- Design: Clean, numbered, visual. No complexity.

### Step 6: Explanatory Paragraph

**Wireframe Section 6 — The Deep Dive:**
- For visitors who need more detail
- 1-2 paragraphs explaining the mechanism
- Still follows story structure (problem → solution → result)
- Transitional CTA at the bottom: "Download our free [lead gen asset]"

### Step 7: Negative Stakes

**Wireframe Section 7 — What's At Risk:**
- 2-3 consequences of NOT acting
- Emotionally specific, not abstract
- Design: Contrasting section that creates tension

### Step 8: Success Vision

**Wireframe Section 8 — The Transformation:**
- Customer success stories or aspirational images
- Show the AFTER — what life/business looks like post-engagement
- Specific outcomes, not generic happiness
- Design: Bright, expansive, aspirational

### Step 9: Final CTA

**Wireframe Section 9 — The Close:**
- Headline: Mini restatement of value prop
- Direct CTA: Resolution formula button
- Transitional CTA: Lead generator for the not-yet-ready
- Trust elements: Guarantee, privacy, security badges

### Step 10: Copy Generation

For each section, write:
- **Headline** (exact copy)
- **Body text** (exact copy, 2-4 sentences max per section)
- **CTA text** (button or link text)
- **Image direction** (what the visual should convey)
- **Design notes** (layout, spacing, emphasis)

## Output Schema

```yaml
deliverable: "StoryBrand Website Wireframe"
components:
  five_second_test:
    description: "3 questions answered above the fold"
    questions: [what_we_do, how_it_helps, what_to_do]
  wireframe_sections:
    description: "9-section top-to-bottom page structure"
    sections:
      - hero_header: "Headline, sub-headline, CTA button, image direction"
      - problem: "2-3 sentences naming customer pain + internal problem"
      - three_benefits: "3 outcome cards with icon + headline + description"
      - guide_positioning: "Empathy statement + authority proof + testimonials"
      - plan: "3-step numbered process"
      - explainer: "Deeper mechanism paragraph + transitional CTA"
      - stakes: "3 consequences of not acting"
      - success: "3 transformation outcomes"
      - final_cta: "Headline + direct CTA + transitional CTA + trust elements"
    per_section: [headline, body_text, cta_text, image_direction, design_notes]
```

## Quality Gate

- [ ] Passes 5-second test (three questions answered above the fold)
- [ ] Customer is the hero (header shows aspirational state, not brand ego)
- [ ] Product/service positioned as solution AFTER problem established
- [ ] Plan has exactly 3 steps (simple, clear, numbered)
- [ ] Both direct and transitional CTAs present
- [ ] Negative stakes create genuine urgency
- [ ] Success section paints specific, emotionally resonant transformation
- [ ] Zero jargon — every visitor understands instantly


> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
