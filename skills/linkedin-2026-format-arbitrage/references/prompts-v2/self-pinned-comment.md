---
name: "The Self-Pinned Comment Strategy"
source_prompt: "skills/linkedin-2026-format-arbitrage/references/prompts/self-pinned-comment.md"
skill: linkedin-2026-format-arbitrage
standard: structure-pure-v2
refactored: 2026-07-11
---

# The Self-Pinned Comment Strategy

**Context:** The algorithm prioritizes clean, readable posts but demands conversation depth. The Self-Pinned Comment solves this by keeping the main post pure of CTAs and links, while immediately seeding the comment section with high-value discussion.

## Your Objective
For *any* generated post, you must create a strategic first comment that the creator will pin. This comment establishes the tone for the entire thread.

## The 3 Archetypes of the Pinned Comment

When generating this comment, choose ONE of the following archetypes based on the post type:

### Archetype 1: The "Behind the Scenes" (Best for Carousels/Educational)
* **Purpose:** Adds proof-of-work. Shows you actually *do* this, not just preach it.
* **Pattern:** "Behind the scenes: I just built a [System] for a [Client Type] with [X] years of experience. It took [Time]. Now they [Outcome]. Want to see how it works? Drop a question below."

### Archetype 2: The Soft Funnel (Best for Contextual Selfies/Stories)
* **Purpose:** Drives leads without cluttering a vulnerable/authentic post.
* **Pattern:** "P.S. If you're tired of [Problem] and want to build a [Solution], I have a free breakdown on how I did it. Drop 'BUILD' below and I'll send you the link."

### Archetype 3: The Contrarian Challenge (Best for Trapdoor Text Posts)
* **Purpose:** Sparks debate and drives 2nd-degree multi-threaded conversations.
* **Pattern:** "The hardest part about this? Accepting that [Contrarian Truth]. What's the biggest roadblock you've hit trying to implement this?"

## Formatting Rules
* Must be posted at T-Zero (immediately after publishing).
* Must end with a specific question or clear instruction to drive replies.
* Do not use generic questions like "What do you think?" Use highly specific questions: "Where does your system break down first?"

## Output Contract
Deliver exactly two components:
1. **Archetype Selection** — one line naming which of the 3 archetypes was chosen and why, tied to the source post type (carousel/educational, selfie/story, or trapdoor text post).
2. **Pinned Comment Text** — the exact comment text, filled to the chosen archetype's pattern, ending in a specific question or clear instruction (never a generic "thoughts?").

## Output Skeleton
```
ARCHETYPE SELECTION
--------------------
Chosen: [Behind the Scenes | Soft Funnel | Contrarian Challenge]
Why: [one line tying the post type to the archetype]

PINNED COMMENT TEXT
--------------------
[Comment text filled to the chosen archetype's pattern]
[Closes with a specific question or instruction — no generic engagement bait]
```

## Quality Gate
- [ ] Archetype choice matches the source post type (carousel→Behind the Scenes, selfie/story→Soft Funnel, trapdoor text→Contrarian Challenge)
- [ ] Comment contains zero generic questions ("What do you think?", "Thoughts?", "Agree?")
- [ ] Closing question is specific enough that a reply requires real engagement, not a one-word reaction
- [ ] Comment reads as postable at T-Zero — no placeholder brackets left unfilled
