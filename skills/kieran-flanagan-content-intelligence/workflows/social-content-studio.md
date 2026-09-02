---
name: "Social Content Studio"
produces: "Grounded surplus inventory, selected social-content week, review artifacts, format briefs, evidence ledger, and approval manifest"
source: "extractions/video-context/hoVC2W0p0Zg"
owner: "kieran-flanagan-content-intelligence"
execution_prompt: "skills/kieran-flanagan-content-intelligence/references/prompts-v2/social-content-studio.md"
---

# Social Content Studio

## Input Contract

Required: seed idea or queue ID, platform, and either a context root or inline identity, audience, and offer context.

Optional: horizon, formats, cadence, performance evidence, visual contract, source-language corpus, and firewall definition.

Default horizon is one week. A month request expands inventory only; it never authorizes publication or requires using every item.

## Execution

### 1. Prepare Brain

Resolve and cite identity and public/private boundaries, audience profile, voice or source-language corpus, offer and business job, visual grammar, performance/pattern evidence, refusal file, and human/AI firewall.

Label each item `VERIFIED`, `PROVISIONAL`, `INFERRED`, or `MISSING`. If identity, audience, or offer is missing, return a Missing Context Packet and stop before ideation.

### 2. Focus

Lock **Person**, **Tension**, **Path**, business job, and proof boundary. Do not proceed when the spine requires an invented fact, client result, private detail, or unverified legal/medical conclusion.

### 3. Style

Bind the voice register, platform behavior, visual grammar, evidence treatment, and at least three enforceable anti-style constraints. For Farrice, the canonical Voice Card and LinkedIn system outrank generic source style.

### 4. Plan

Generate 10–15 materially different executions. Vary argument, proof object, narrative frame, format, and audience entry—not merely hooks. Prune duplicates and weak-proof candidates. Select 3–5 for the requested horizon and record a decision reason for every selection.

Kallaway is a bounded quality check here: prefer buyer-quality authority over empty reach and preserve honest proof labels.

### 5. Create

Kieran owns the outline and handoff. Review copy is produced only through the supplied voice system or source-language corpus and remains `HUMAN_REVIEW_PENDING`.

- Text post: review draft plus source/claim notes.
- Carousel: slide architecture plus bounded handoff to `ai-carousel-content-engine`.
- Video: concept, spoken-script draft, shot/visual brief, and bounded handoff to `video-studio`.

Never invoke a paid adapter automatically. Never reactivate `higgsfield-content-factory`.

### 6. Package

Emit the Context Lock, Content Spine, surplus inventory, selected weekly plan, review artifacts and format briefs, evidence/claim ledger, and approval manifest with unresolved inputs and one next safe action.

All artifacts stay local. Publishing, scheduling, profile editing, outreach, and connector writes require separate approval.

## Quality Gate

- [ ] All required context is present and source-cited.
- [ ] `Person → Tension → Path` is specific and shared across the week.
- [ ] At least three refusal constraints are executable.
- [ ] Inventory contains 10–15 distinct candidates; 3–5 are selected with reasons.
- [ ] Unsupported facts are `NEEDS_SOURCE`; stale performance data is `PROVISIONAL`.
- [ ] Every draft and brief is `HUMAN_REVIEW_PENDING`.
- [ ] No external action, paid tool, or retired Higgsfield route is invoked.
- [ ] Package exposes proof ceilings: local behavior is not audience or revenue proof.

## Failure Return

When a gate fails, return only the missing or failed field, exact source or decision needed, nearest safe continuation, and artifacts that remain valid.
