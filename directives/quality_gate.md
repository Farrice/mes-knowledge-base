# Self-Annealing Quality Gate

> **Trigger**: Silently after any output using expert skill/agent persona. Fires for ALL expert output (content, strategy, research, copy, analysis, creative). Does NOT fire for pure system operations. "Trivial" and "follow-up" are NOT skip conditions.
> **Feeds into**: `directives/feedback-ratchet.md`

---

## The 4-Point Gate (Score 1-10 each)

### 1. Intent Alignment
Does output match what user asked for? Check scope drift, format expectations.
- 9-10: Precisely addresses request | 7-8: Core addressed, minor drift | 5-6: Partial | <5: Wrong deliverable
- **Fail (<6):** "Good work, but not what they asked for."

### 2. Expert Standard
Would the skill's expert be proud? Embodies thinking style (not just terminology)? Passes named quality test?
- 9-10: Indistinguishable from expert | 7-8: Captures depth | 5-6: Framework without insight | <5: Generic + terminology
- **Copy Calibration:** Read as ICP on phone with 2 seconds. Know (a) about you, (b) what person does, (c) what's in it for you? Score ≤6 if problem named without concrete result.
- **AI Prose Cap:** AI-shaped prose cannot score >6 regardless of methodology. Predictable rhythm, Tier 1 vocab, formulaic structures = fail.
- **Fail (<6):** "A junior could produce this with a template."

### 3. Adversarial Resilience
Would this survive domain scrutiny? Unsupported assertions? Embarrassing claims?
- 9-10: Bulletproof | 7-8: Minor nitpicks | 5-6: Needs backing | <5: Expert dismisses immediately
- **Cultural Check:** "Would a 10+ year resident find this tone-deaf?" If user has lived experience → ask. If not → flag gap.
- **Fail (<6):** "A domain expert would pick this apart in 30 seconds."

### 4. Factual Grounding
Are real-world claims in this output verified against primary sources? Policies, names, dates, prices, specs, APIs — anything that can be checked, was it checked?
- 9-10: Every factual claim cross-referenced against primary sources. Unverifiable items explicitly flagged | 7-8: Core claims verified, minor details flagged as unverified | 5-6: Some claims unverified, none flagged — user would discover errors on their own | <5: Claims presented as fact without verification. False confidence throughout
- **Confidence Labeling:** Every factual claim in the deliverable must carry implicit or explicit grounding. If a claim cannot be verified, it MUST be flagged — not presented with the same confidence as verified facts. Presenting uncertain info as certain = automatic score ≤4.
- **Source Diversity:** Single-source claims score lower than multi-source claims. A fact confirmed across 3+ independent sources is grounded. A fact from one ambiguous paragraph is a guess wearing a suit.
- **Verification Timing:** Verify BEFORE writing, not after being pushed. If the verification pass happens only because the user pushed back, the system failed regardless of the final accuracy.
- **Fail (<6):** "The user had to fact-check their own deliverable."

**When Dimension 4 Fires:**
- Any deliverable referencing real-world facts: policies, regulations, prices, dates, names, technical specs, API behavior, legal terms, event schedules, weather data, product features
- Does NOT fire for: pure creative/strategic output where claims are opinions or frameworks, not verifiable facts
- When in doubt: it fires. Better to verify something that didn't need it than to skip something that did

### Quick Diagnostics (from Reflection Pass synthesis)

**Attention Equation** (if content/copy): `Attention = Signal ÷ Noise × Pull`
- **Signal**: Does it have a single truth? (Single Truth Convergence) — if not, it's covering too much
- **Noise**: Are there unconstrained additions? (Constraint as Creative Input) — if yes, delete until focused
- **Pull**: Does it have narrative gravity? (Dwell Time = Narrative Gravity) — if not, import screenwriting mechanics
- "Structurally sound but flat" = low noise (good) + low signal (no single truth) + zero pull (no gravity). Diagnose which is missing.

**Persuasion Stack Check** (if persuasive output): Does it have all 4 layers?
1. [ ] Single truth (one sentence)
2. [ ] Mechanism (why it's true)
3. [ ] Matched proof (right tier for claim weight + attention budget)
4. [ ] Identity awareness (if audience is identity-resistant, layer 4 tools loaded)
- Any layer at 0 = fail regardless of composite score.

### Composite Score
Average of all applicable sub-scores (3 dimensions for creative/strategic, 4 dimensions when Factual Grounding fires). **≥7: Pass** | **5-6: Retry weakest** | **<5: Fail**
Evolution mode: ≥7 KEEP, <7 DISCARD (binary, no marginal zone).
**Factual Grounding veto:** If Dimension 4 fires and scores <6, the deliverable CANNOT pass regardless of composite. A factually wrong document that's well-written and on-strategy is worse than a rough draft that's accurate — because the user trusts the polish.

---

## On Failure (composite <7 OR any dimension <6)
1. Diagnose (1 sentence) → 2. Fix failing section only → 3. Re-check → 4. Max 1 retry. Still fails → deliver with confidence note.
**Factual Grounding failure (Dim 4 <6):** Do NOT retry the writing. Go back to research. The problem is upstream — the claims weren't verified. Re-research, re-verify, THEN rewrite.

## Performance Logging
After delivery, log via `execution/log_performance.py`: output, agent, skill, workflow, task_type, quality_score, sub-scores, status, notes.

---

## Rubric Variants (Upgrade 4 — Pattern 9 Anti-Rubric-Gaming)

Rotate these phrasings across benchmark scoring runs to detect variants that optimize for specific rubric wording rather than underlying quality. Pick one phrasing per dimension per task via `phrasing_idx = (cycle_number + task_idx) % 3`.

### Intent Alignment
- **Phrasing A**: Does the output match what the user actually asked for?
- **Phrasing B**: If the user read this output blind, would they say "yes, that's what I wanted"?
- **Phrasing C**: Does the deliverable resolve the specific question/task, or does it answer an adjacent one?

### Expert Standard
- **Phrasing A**: Would the real expert recognize this as quality work?
- **Phrasing B**: If posted under the expert's name, would it damage or enhance their reputation?
- **Phrasing C**: Does this output demonstrate the expert's actual thinking, or is it generic with expert-branded terminology?

### Adversarial Resilience
- **Phrasing A**: Would this output survive critical scrutiny from a hostile reader?
- **Phrasing B**: What's the strongest counterargument to this, and does the output pre-empt it?
- **Phrasing C**: If a skeptical peer reviewer picked this apart for 30 minutes, what would they find?

### Factual Grounding (when applicable)
- **Phrasing A**: Are real-world claims verified against primary sources?
- **Phrasing B**: If every factual claim had to be cited, could it be?
- **Phrasing C**: Which claims would survive a fact-check from a domain expert, and which would not?

**Gaming detection**: Score variance on the same variant across phrasings > 1.5 on the same dimension = rubric gaming flag.

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-04-25 (chain_runner finalize for verify) |
| **Activation Count** | 143 |
| **30-Day Review Date** | 2026-04-11 |

*Created: 2026-02-17 | Compressed: 2026-04-13*
