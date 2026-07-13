---
name: "The Trapdoor Text Post"
source_prompt: "skills/linkedin-2026-format-arbitrage/references/prompts/trapdoor-text-post.md"
skill: linkedin-2026-format-arbitrage
standard: structure-pure-v2
refactored: 2026-07-11
---

# The Trapdoor Text Post

**Context:** Leveraging the Jasmin Alic "Three-Line Rule" and "1-3-1 Method," this prompt engineers extreme readability and capitalizes on the Zeigarnik effect. The primary goal is to force the mobile "...see more" click and drive conversation depth.

## Your Objective
Write a text-only LinkedIn post that masters the curiosity gap in the first three lines and delivers a compelling, readable narrative.

## Input Parameters
* **Core Insight/Story:** [The main point or un-intuitive truth]
* **Target Audience Pain Point:** [What is bleeding right now]
* **Sovereignty Angle:** [The "Anti-Guru" or leverage position]

## The Trapdoor Architecture (HLCP Framework)

Your output MUST rigidly adhere to these structural constraints:

### Part 1: The Trapdoor (The First 3 Lines)
* **Goal:** Engineer the "...see more" click. This is do or die.
* **Line 1 (Hook):** A single sentence. A pattern interrupt, a jarring statistic, or a contrarian claim.
* **Line 2 (Lead):** Deepens the curiosity. Does *not* resolve the hook.
* **Line 3 (The Cliffhanger):** The final visible line before LinkedIn truncates. It must leave an unresolved narrative loop (The Zeigarnik effect).

### Part 2: The Payload (1-3-1 Method)
* **Rule of Three:** Deliver the body of the post in 3 distinct beats or steps. (Never 2, never 4). This creates cognitive completeness.
* **Formatting:** Single-line paragraphs. Extreme readability. Use the `↳` symbol to create visual hierarchy for lists or sub-points.

### Part 3: The Anti-Niche Open (If Applicable)
* If the post is highly technical, begin with a *universally relatable problem* (e.g., time loss, frustration) before pivoting into the specific niche solution.

### Part 4: The Prompt (The Close)
* **Goal:** Drive comments for algorithmic velocity.
* **Mechanism:** The question must be *easy* to answer (yes/no, or a simple A/B choice) but invite elaboration.

## Output Contract

**Voice layer (binding — Farrice 2026-07-13):** if this deliverable ships under Farrice's own name, load `_active/farrice-brand/voice/VOICE-CARD.md` + dial mode (default BLEND, per `skills/voice-os/SKILL.md`) as a layer BEFORE drafting — binding `farrice_voice_alignment`.

Deliver exactly two components:
1. **The Post Text** — exactly as it should be pasted into LinkedIn, following the HLCP structure: 3-line trapdoor, 3-beat payload, closing prompt.
2. **The Trapdoor Analysis** — a 2-sentence explanation of why the first 3 lines force the "see more" click, naming the specific mechanism used (pattern interrupt, jarring statistic, or contrarian claim).

## Output Skeleton
```
POST TEXT
---------
[LINE 1 — HOOK: single sentence, pattern interrupt / jarring statistic / contrarian claim]
[LINE 2 — LEAD: deepens curiosity, does not resolve the hook]
[LINE 3 — CLIFFHANGER: last visible line before truncation, unresolved loop]

[Optional: ANTI-NICHE OPEN — universally relatable problem, only if topic is technical]

↳ [BEAT 1 of 3]
↳ [BEAT 2 of 3]
↳ [BEAT 3 of 3]

[CLOSING PROMPT — easy-to-answer question that still invites elaboration]

TRAPDOOR ANALYSIS
-----------------
[2 sentences: which mechanism the first 3 lines use and why it forces the click]
```

## Quality Gate
- [ ] Line 3 ends on a genuinely unresolved loop — reading only lines 1-3 leaves a real open question
- [ ] Payload has exactly 3 beats, never 2 or 4
- [ ] Every paragraph in the payload is a single line (no multi-sentence blocks)
- [ ] Closing prompt is answerable in one word/choice but still invites a real reply
- [ ] Trapdoor Analysis names one specific mechanism, not a vague "it's engaging"
