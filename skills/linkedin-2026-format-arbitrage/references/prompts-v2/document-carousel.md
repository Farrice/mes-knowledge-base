---
name: "The Document Carousel (Apex Predator)"
source_prompt: "skills/linkedin-2026-format-arbitrage/references/prompts/document-carousel.md"
skill: linkedin-2026-format-arbitrage
standard: structure-pure-v2
refactored: 2026-07-11
---

# The Document Carousel (Apex Predator)

**Context:** The document carousel is a top-performing LinkedIn format, driven by a "commitment escalation loop" — each swipe is a micro-commitment, and the algorithm rewards completion. Every slide must hold attention or the carousel dies to abandonment.

## Your Objective
Generate the text and structural blueprint for an 8-10 slide document carousel that adapts the user's specific expertise into a comprehensive, finite framework.

## Input Parameters
* **Target Audience:** [Who this is for]
* **Core Topic/Framework:** [What is being taught]
* **Niche Bend:** [E.g., "Adapting a fitness transformation framework to AI consulting"]
* **Solopreneur Sovereignty Angle:** [How this leverages time/expertise]

## The Carousel Architecture

Your output must follow this exact slide-by-slide structure, optimizing for dwell time and the sunk-cost swipe.

### Slide 1: The Cover (The Hook)
* **Goal:** Negative urgency or a specific, quantifiable promise.
* **Mechanism:** Loss aversion or an irresistible curiosity gap. Focus heavily on what it *costs* them not to know this.
* **Text Structure:** Short, punchy headline + 1-sentence subtitle.

### Slide 2: The Retention Bridge
* **Goal:** Lock them into the swipe.
* **Mechanism:** Ego challenge or commitment escalation.
* **Text Structure:** E.g., "Most people stop here. If you want [Outcome], swipe." or "The mistake costing you [X] happens in step 2."

### Slides 3-8: The Core Payload (1 Idea Per Slide)
* **Goal:** Deliver the framework logically.
* **Mechanism:** Cognitive ease and "chunking."
* **Formatting Rules:**
    * ONE complete idea per slide. Do not split concepts across slides.
    * Use numbered lists if applicable (creates cognitive scaffolding).
    * Bold key terms.
    * Mandate extreme white space.

### Slide 9: The Transformation Summary
* **Goal:** Aspirational projection.
* **Mechanism:** The Contrast Principle.
* **Text Structure:** A clear Before vs. After juxtaposition. E.g., "Before: 10 hours repeating yourself. After: 10 hours reclaimed."

### Slide 10: The Exit & Save Trigger
* **Goal:** Secure the algorithmic "Save" action.
* **Mechanism:** Action priming + future self-projection.
* **Text Structure:** Explicitly ask for the save. E.g., "Save this for your next strategy session." Include the primary CTA for the creator's offer (e.g., "DM me 'BRAIN' for the blueprint").

## Output Contract

**Voice layer (binding — Farrice 2026-07-13):** if this deliverable ships under Farrice's own name, load `_active/farrice-brand/voice/VOICE-CARD.md` + dial mode (default BLEND, per `skills/voice-os/SKILL.md`) as a layer BEFORE drafting — binding `farrice_voice_alignment`.

Deliver exactly three components:
1. **The Hook Evaluation** — a short explanation (2-4 sentences) of why Slide 1 will stop a scroll, tied to loss aversion or curiosity-gap mechanics.
2. **The Slide Deck** — text for all 8-10 slides, each labeled by its architecture role (Cover, Retention Bridge, Payload 1-6, Transformation Summary, Exit), with visual notes per slide.
3. **The Pinned Comment** — one self-pinned comment adding behind-the-scenes value or sparking conversation.

## Output Skeleton
```
HOOK EVALUATION
---------------
[2-4 sentences: why this cover stops the scroll — name the mechanism used]

SLIDE DECK
----------
Slide 1 (Cover): [headline] / [1-sentence subtitle]
  Visual note: [description]

Slide 2 (Retention Bridge): [ego-challenge or commitment-escalation line]
  Visual note: [description]

Slide 3 (Payload — Idea 1): [one complete idea, chunked]
  Visual note: [description]

Slide 4 (Payload — Idea 2): [one complete idea, chunked]
  Visual note: [description]

[... continue through Slide 8, one idea per slide ...]

Slide 9 (Transformation Summary): Before: [state] / After: [state]
  Visual note: [description]

Slide 10 (Exit & Save Trigger): [save ask] + [primary CTA]
  Visual note: [description]

PINNED COMMENT
--------------
[Behind-the-scenes value or conversation-starter, ready to post]
```

## Quality Gate
- [ ] Total slide count is 8-10, matching the architecture
- [ ] Every payload slide (3-8) carries exactly one complete idea — none split across two slides
- [ ] Slide 2 explicitly names the cost of stopping or the ego challenge, not a generic "keep swiping"
- [ ] Slide 9 contains a genuine before/after contrast, not a summary paragraph
- [ ] Slide 10 asks for the save explicitly and separately from the CTA
- [ ] Hook Evaluation names the specific mechanism (loss aversion vs. curiosity gap), not both vaguely
