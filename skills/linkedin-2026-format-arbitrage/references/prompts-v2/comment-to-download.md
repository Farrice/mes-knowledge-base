---
name: "The Comment-to-Download Flywheel"
source_prompt: "skills/linkedin-2026-format-arbitrage/references/prompts/comment-to-download.md"
skill: linkedin-2026-format-arbitrage
standard: structure-pure-v2
refactored: 2026-07-11
---

# The Comment-to-Download Flywheel

**Context:** This format engineers algorithmic velocity by combining a high-value native post with a strategic Call-to-Action (CTA) that demands a comment for asset delivery. It captures leads and strengthens algorithmic connections.

## Your Objective
Build a post designed to introduce a high-value framework, ending with a "soft" CTA that converts readers into commenters through the promise of a deeper asset (e.g., a PDF, blueprint, or guide).

## Input Parameters
* **The "Tease" Framework:** [A valuable but incomplete piece of your methodology]
* **The Asset:** [The actual PDF/guide you will DM them]
* **Target Audience:** [Who this is for]

## The Flywheel Architecture

### 1. The Value Tease (The Native Post)
* **Goal:** Deliver enough value natively that the post stands on its own, even if they don't comment.
* **Mechanism:** The 1-3-1 structure.
* **Structure:**
    * **Hook:** A bold claim about the framework you are introducing.
    * **Context:** Why this matters *now* (urgency).
    * **The Tease:** Outline the 3 high-level concepts of the framework, but do not provide the detailed execution steps.

### 2. The Soft CTA (The Conversion Mechanism)
* **Goal:** Drive the comment without sounding desperate.
* **Mechanism:** "I turned this into a [Asset Type] so it's easier to use."
* **The Language:** "Want the complete blueprint? Drop '[KEYWORD]' in the comments and I'll send you the PDF."

### 3. The DM Delivery (The 2nd Degree Connection)
This is crucial for the 2026 algorithm. You must structure the DM response.
* **Goal:** Force a reply to your DM to cement the algorithmic tie.
* **DM Script requirement:** Deliver the link, then ask a qualifying question. (e.g., "Here's the blueprint: [Link]. Quick question: What's the biggest bottleneck in your coaching business right now?")

## Output Contract

**Voice layer (binding — Farrice 2026-07-13):** if this deliverable ships under Farrice's own name, load `_active/farrice-brand/voice/VOICE-CARD.md` + dial mode (default BLEND, per `skills/voice-os/SKILL.md`) as a layer BEFORE drafting — binding `farrice_voice_alignment`.

Deliver exactly three components, in this order:
1. **The Post Text** — ready to paste into the LinkedIn feed. Follows the 1-3-1 structure (1 hook, 3 tease concepts, 1 soft CTA). No links or external CTAs in the post body.
2. **The Asset Title** — one compelling name for the PDF/guide being offered, framed as a deliverable outcome, not a generic label ("guide," "resource").
3. **The DM Script** — the exact text sent when replying to a qualifying comment: delivery line + one qualifying question. No more than 2-3 sentences.

## Output Skeleton
```
POST TEXT
---------
[HOOK — one bold claim about the framework, no throat-clearing]

[CONTEXT — one line on why this matters now / urgency]

[TEASE — 3 high-level concepts named, not explained in full]
  1. [Concept name]
  2. [Concept name]
  3. [Concept name]

[SOFT CTA — "Drop '[KEYWORD]' below and I'll send you the [asset type]"]

ASSET TITLE
-----------
[One outcome-framed title for the PDF/guide]

DM SCRIPT
---------
[Delivery line with link placeholder] + [one qualifying question tied to the target audience's likely bottleneck]
```

## Quality Gate
- [ ] Post stands alone as valuable even if no one comments (the tease is not clickbait-empty)
- [ ] The 3 tease concepts are named but not fully explained — no accidental full-value giveaway
- [ ] Post body contains zero links and zero direct CTAs other than the comment-keyword ask
- [ ] DM script ends in a genuine qualifying question, not a generic "thanks!"
- [ ] Asset title names an outcome, not a format ("The [X] Blueprint," not "My PDF Guide")
