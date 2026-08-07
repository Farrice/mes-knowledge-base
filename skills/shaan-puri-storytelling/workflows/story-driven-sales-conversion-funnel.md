---
slug: "story-driven-sales-conversion-funnel"
name: "Story-Driven Sales Conversion Funnel"
description: "Build a story-led sales page and email sequence from a real offer and proof packet without fabricating claims, testimonials, urgency, or outcomes."
produces: "A complete sales page and automated email sequence"
expert: "Shaan Puri Storytelling Mastery"
load_context: "genius.md"
---

# Shaan Puri Storytelling Mastery — Story-Driven Sales Conversion Funnel

## Role
You are applying Shaan Puri's low-status opening, audience-specific transformation, before-state proof, and nested-story persuasion to a real offer. Story organizes supported proof; it never replaces proof or informed choice.

## Skill Acquisition

1. Require a `/shaan-story-deploy` decision of `FULL STORY` or `STORY FRAGMENT` before using this route.
2. Read `genius.md`, especially Decision Framework, Voice DNA, Patterns 1–7, transcript Pattern J, Anti-Patterns, and the Factual Integrity Invariant.
3. Load the offer's proof sources and claim constraints before drafting.
4. Execute `references/prompts-v2/story-driven-sales-conversion-funnel.md` for the exact deliverable shape.

When `/shaan-story-deploy` supplies an exact bounded exit condition such as one landing-page core, honor that requested subset instead of expanding the assignment into the default full funnel. Name the subset in the receipt, preserve every relevant proof and consent gate, and do not imply that omitted components were executed. The full-funnel contract remains the default when no narrower exit condition is supplied.

## Input Required
- **[PRODUCT/OFFER]**: What is being sold and the price point.
- **[JENNY]**: A vivid description of the ONE specific person this is for (their current physical/emotional context).
- **[THE OBSTACLE]**: The specific wall "Jenny" has hit trying to solve this before.
- **[THE 5-SECOND MOMENT]**: A supported pivot point, or `NONE` when the proof packet does not contain one.
- **[CORE FEELING]**: The single signature emotion this funnel must deliver (e.g., "Relief," "Power," "Belonging").
- **[PROOF PACKET]**: Authorized testimonials, case studies, demonstrations, data, credentials, and source paths.
- **[KEY OBJECTIONS]**: The buyer's real decision friction.
- **[CLAIM CONSTRAINTS]**: Factual, legal, policy, fit, tone, and urgency boundaries.

> **Pre-Flight Gate**: Run `genius.md` § Decision Framework. Separate verified proof, source-reported claims, hypotheses, and missing evidence. Insert `[PROOF NEEDED]` rather than completing unsupported claims.

Descriptions of an intake call, discovery process, buyer work, delivery sequence, or service mechanism are offer claims. Use them only when the proof packet supplies them. Do not infer what happens inside a call from the deliverables that follow it; omit the process or mark `[PROCESS SOURCE NEEDED]`.


## Workflow

### Phase 1: The Frame & The Feeling (Pre-Production)
1. **Identify the Merchant of Feelings**: Define the one signature feeling. If the product is a productivity app, the feeling isn't "efficiency"—it's "The Quiet Mind."
2. **The Low-Status Hook**: Use a supplied failure, admission, or relatable moment when available. Do not manufacture vulnerability.
3. **The Yin-Yang Contrast**: Map the "Before State" (Chaos/Pain) against the "After State" (Order/Peace). The distance between these two is your profit margin.

### Phase 2: The Sales Page Narrative (The Alchemist)
Construct the sales page as a buyer journey where the prospect remains the decision-maker and the offer's real mechanism, work, fit, and tradeoffs stay visible.
- **Hero Section**: A Frame > Hook headline that promises the [CORE FEELING].
- **The Audience Opening**: Use customer evidence to describe the decision context accurately. Label hypotheses and avoid invented private fear.
- **The Obstacle Landscape**: Explain why prior approaches fail only when supplied evidence supports the claim.
- **The Guide’s 5-Second Moment**: Use the creator's supported realization or omit it.
- **The Transformation Mechanism**: Connect features to supported use and fit. Narrative language is optional; specifications remain visible when they help the decision.
- **Proof via Mini-Narratives**: Reshape authorized testimonials or cases into concise before, moment, and after summaries without changing wording or result meaning. If proof is absent, mark the gap.
- **The Decision CTA**: State the next step, fit, price or terms, and relevant tradeoffs without implying that purchase is the only logical choice.

### Phase 3: The Nested Email Sequence (The Architect)
Create a 5-7 email sequence. Use the Dave Chappelle nested-story technique only when multiple supported stories exist; otherwise use proof, mechanism, tradeoffs, and direct explanation.
- **Email 1: The Connection**: Use a supported failure or relatable moment when available; otherwise establish direct relevance.
- **Email 2-4: The Pattern Reveal (Nested Stories)**:
    - Use up to 3 supported stories or proof fragments that point to the same [CORE PRINCIPLE]. If the proof packet cannot support them, use direct evidence or explanation.
    - Let the reader evaluate the pattern without hiding contrary evidence or forcing a conclusion.
- **Email 5: The Objection Dissolution**: Address the biggest "Yeah, but..." through relevant proof, mechanism, tradeoff, or a sourced story.
- **Email 6: The 5-Second Vision**: Describe the supported use experience or label it clearly as a hypothetical future scenario. Do not present imagined sensory detail as a result.
- **Email 7: The Decision**: Summarize fit, tradeoffs, evidence, and the next step. Use a two-path contrast only when both paths are accurate and non-coercive.

### Phase 4: The Quality Polish
1. **The "Jenny" Check**: Read the copy. Would the specific person described in the input feel like this was a private letter to them?
2. **The Status Scrub**: Remove unsupported ranking and credential claims. Use only supplied experience, proof, or a direct mechanism statement; never replace one unsupported claim with another.
3. **The Continuity Audit**: Give each email an honest reason to continue—usefulness, a real open question, or a supported story beat. A cliffhanger is optional and may not conceal material information.

4. **The Consent Audit**: Remove false urgency, false scarcity, guarantees, and emotional pressure that hides fit or tradeoffs.

## Content-Type Adaptations

| Offer context | Adaptation |
|---|---|
| New offer with little proof | Use mechanism, fit, demonstration, and `[PROOF NEEDED]`; do not manufacture case studies |
| Established offer | Map each material claim to authorized customer or performance evidence |
| High-ticket service | Make scope, buyer work, fit, tradeoffs, and decision process explicit |
| Evidence-sensitive category | Require domain and claim review; prefer fragment or direct evidence over transformation anecdote |
| Limited-time launch | State only real deadlines, inventory, and terms; no artificial countdown language |

## Output Contract
A single document containing, by default:
1. **Funnel Strategy Map**: The Core Feeling, the Frame, and the Yin-Yang contrast.
2. **The Sales Page**: Full copy from headline to CTA, using only the approved narrative dosage.
3. **The 5-7 Email Sequence**: Subject lines, content beats, evidence or story use, and CTAs.
4. **The Pattern Architecture**: A breakdown of nested stories only when the proof packet supports them; otherwise the direct evidence and objection structure.

For an exact router-supplied subset, return only the requested body asset plus the minimum strategy, proof/claim ledger, truth boundary, and deployment notes needed to validate that subset. State the omitted default components explicitly; do not call the result a complete funnel.

Execution prompt: `references/prompts-v2/story-driven-sales-conversion-funnel.md` — honor its Output Contract.

## Quality Gate
- **The Dosage Test**: Does the page and sequence honor the approved `FULL STORY` or `STORY FRAGMENT` decision?
- **The Pivot Test**: If a pivot appears, is it supplied and accurately represented?
- **The Opening Test**: Does the opening create relevance without manufactured vulnerability?
- **The Pattern Test**: If nested stories appear, are they supported and non-coercive?
- **The Feeling Test**: Is the core feeling an intended experience rather than a guaranteed audience response?
- **The Proof Test**: Does every result, quote, story, metric, mechanism, deadline, and scarcity claim trace to the Proof Packet?
- **The Process-Trace Test**: Does every intake, discovery, buyer-work, and delivery-process description trace to the Proof Packet rather than being inferred from the offer?
- **The Choice Test**: Are fit, tradeoffs, buyer work, and limitations clear enough for an informed decision?
- **The Scope Test**: Does a bounded router exit condition produce exactly that subset, while a full-funnel request still produces the complete default contract?


> **Anti-Pattern Check**: Review `genius.md` § Anti-Patterns, Voice DNA, and Factual Integrity Invariant before delivery.
