# Self-Annealing Quality Gate

> **Trigger**: Silently after any output using expert skill/agent persona. Fires for ALL expert output (content, strategy, research, copy, analysis, creative). Does NOT fire for pure system operations. "Trivial" and "follow-up" are NOT skip conditions.
> **Feeds into**: `directives/feedback-ratchet.md`

---

## The 3-Point Gate (Score 1-10 each)

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
Average of 3 sub-scores. **≥7: Pass** | **5-6: Retry weakest** | **<5: Fail**
Evolution mode: ≥7 KEEP, <7 DISCARD (binary, no marginal zone).

---

## On Failure (composite <7 OR any dimension <6)
1. Diagnose (1 sentence) → 2. Fix failing section only → 3. Re-check → 4. Max 1 retry. Still fails → deliver with confidence note.

## Performance Logging
After delivery, log via `execution/log_performance.py`: output, agent, skill, workflow, task_type, quality_score, sub-scores, status, notes.

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-04-13 (chain_runner finalize for stefan-georgi-dopamine-copy) |
| **Activation Count** | 125 |
| **30-Day Review Date** | 2026-04-11 |

*Created: 2026-02-17 | Compressed: 2026-04-13*
