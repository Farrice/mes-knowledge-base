# Antigravity Quality Rubric v1

**Created**: 2026-04-24 (Fix 1 from system audit)
**Purpose**: Calibrate the 4-dimension quality scoring used by `chain_runner.py finalize()` so scores are defensible, not vibes-based. Anchors prevent grade inflation ("everything is a 9/10") and grade compression (everything is a 6 or 7).

**How to use**:
1. Score each dimension 1-10 against the anchors below.
2. If a dimension scores 5 or below, name *which anchor* it matches and *why*.
3. Composite = arithmetic mean of the 3 mandatory dimensions (Intent / Expert Standard / Adversarial). Factual Grounding is the 4th dimension with veto power: <6 blocks delivery regardless of composite.
4. **The bar**: A "world-class deliverable to a paying client" should score 8.5+ composite with all dimensions ≥8. A "ships to internal use" deliverable should score 7+ with no dimension <6.

**Calibration principle**: Score by comparing to the WORKED EXAMPLE at the anchor, not by feel. If you can't name the anchor, you can't name the score.

---

## Dimension 1: Intent Alignment

**The question**: Does the output deliver what the user actually asked for — not what was easy to produce, not what the system has skills for, not what would have been a good idea — what they ASKED for?

### Anchor 9 — Exemplary
**Example**: User asks for "5 LinkedIn headlines for a coaching offer targeting overwhelmed founders." Output is 5 LinkedIn headlines. Each headline (a) names the audience clearly, (b) names a specific pain or outcome, (c) fits the LinkedIn ~60-char truncation, (d) follows the user's stated voice constraints. The user can pick one and post it as-is.
**Test**: Could the user complete their workflow with this output and zero clarification?

### Anchor 6 — Passable but flawed
**Example**: User asks for "5 LinkedIn headlines." Output gives 5 headlines BUT also includes 3 unsolicited "bonus" headline frameworks, a paragraph explaining why headlines matter, and 2 of the 5 headlines exceed 60 chars. Direction is right; ratio of signal to noise is wrong.
**Test**: Did the output ALSO do things the user didn't ask for, OR fail to constrain to the request?

### Anchor 3 — Clear fail
**Example**: User asks for "next Parallax Substack edition" (a specific production workflow). System runs `writers-room` (a diagnostic refinement workflow) on a draft they didn't have. Output is a critique of an imaginary draft, not a written edition. **This is the 2026-04-21 incident.** The system delivered something coherent — but not what was asked for.
**Test**: Did the output answer a different question than the user asked?

---

## Dimension 2: Expert Standard

**The question**: Would the actual expert whose framework was loaded recognize this as quality work in their tradition? Not "does it use the expert's terminology" — does it embody their THINKING?

### Anchor 9 — Exemplary
**Example**: A LinkedIn post produced via the Lara Acosta skill where the headline follows Pattern 20 (pain + for whom + proof) NATURALLY rather than as a label, the hook engineering follows her actual SLAY pattern, the post structure leverages mobile-first formatting, and dwell-time engineering is visible across the entire piece. Lara would recognize this as her work, not as someone imitating her vocabulary.
**Test**: If the real expert read this output cold, would they say "yes, that's how I think" or "that's someone using my words"?

### Anchor 6 — Passable but flawed
**Example**: A LinkedIn post that uses Lara Acosta's terminology (mentions "SLAY format," "Pattern 20") but the headline doesn't actually FOLLOW Pattern 20 (it's just a clever line), the structure is generic LinkedIn-good rather than specifically Acosta-good, and dwell-time mechanics appear in the first 2 lines but vanish for the rest of the post. Reads as "competent LinkedIn writing with Lara Acosta vocabulary applied."
**Test**: Could this output have been produced WITHOUT loading the expert's skill files?

### Anchor 3 — Clear fail
**Example**: The 2026-03-11 LinkedIn session documented in MEMORY.md. Expert files were "loaded" but the output was generic "social media expert advice" with Lara Acosta's name attached. Expert Standard score: 3-4. **This is the failure mode the audit flagged across the system: scaffolding outpaces evals.** A score of 3 means "the loaded expert added nothing the LLM couldn't have produced from training data alone."
**Test**: Would the real expert be embarrassed to be associated with this?

---

## Dimension 3: Adversarial Resilience

**The question**: If a sharp critic — competitor, skeptical client, the expert themselves — read this output looking for weaknesses, would it survive? Or would the first 30 seconds of scrutiny reveal that it's brittle?

### Anchor 9 — Exemplary
**Example**: A strategic brief that an external strategist could read and find: (a) every claim has a specific supporting reference or stated assumption, (b) the recommended action explicitly addresses the 3 most likely objections, (c) where the brief lacks data, it says so explicitly rather than papering over with generic phrasing, (d) trade-offs are surfaced rather than hidden. A skeptic would say "I disagree with the conclusion but I cannot fault the reasoning."
**Test**: Could a sharp critic find a specific, fixable weakness in 60 seconds of reading?

### Anchor 6 — Passable but flawed
**Example**: A strategy doc that's structurally sound and uses the right frameworks, but on close reading: 2 claims are presented as fact when they're really assertions, 1 recommendation glosses over a known constraint, the success metrics are described as "increase engagement" rather than specific numbers. A skeptic would say "the bones are right but I have follow-up questions you should have answered already."
**Test**: Are there obvious questions a smart reader would ask that the output didn't preempt?

### Anchor 3 — Clear fail
**Example**: A "polished-looking" deliverable where the structure is right and the language sounds professional, but: factual claims are vague ("studies show," "the data suggests" without citation), generic assertions stand in for specific insight ("audiences want authentic content"), the recommendation is too universal to act on ("focus on storytelling"). A skeptic would dismiss this as "consultant-speak with no substance." This is the "structurally sound but flat" failure mode flagged in MEMORY.md.
**Test**: Could you find a specific, falsifiable claim in this output? If no, it's at most a 4.

---

## Dimension 4: Factual Grounding (VETO POWER)

**The question**: Are all real-world claims (real people, events, dates, statistics, technical facts, market claims, source attributions) actually true and verifiable? Are uncertainties flagged?

**This dimension has VETO power**: A score below 6 blocks delivery regardless of composite. A polished document with wrong facts is worse than a rough draft with right facts — because polish creates trust.

### Anchor 9 — Exemplary
**Example**: A profile piece that mentions a real person where: (a) every name, title, and affiliation is verified against current sources, (b) every quote is from a real verifiable transcript or publication with a citation pattern that's auditable, (c) any claim that couldn't be verified is explicitly marked UNCONFIRMED or replaced with a hedged formulation, (d) statistics include source and as-of date.
**Test**: Could every factual claim be confirmed by Googling for 10 minutes? Are uncertainties named?

### Anchor 6 — Passable
**Example**: A piece where most factual claims check out, but 1-2 are presented confidently when they should be hedged. The work is shippable but a fact-checker would flag a few items for revision before publication.
**Test**: Are there 1-3 claims that need a hedge but don't have one?

### Anchor 3 — Clear fail / VETO TRIGGERED
**Example**: Parallax Edition 02 (2026-04-21). 7 fabrications shipped: Madeon was described as "an unknown DJ" (he is a Grammy-nominated headliner with 1B+ streams), wrong day cited, distance invented, song-age math wrong, etc. The piece read polished — that was the problem. The polish made the wrong facts look authoritative. **A score of 3 here triggers DELIVERY BLOCK regardless of how good the writing is.**
**Test**: Are there specific, verifiable claims in this output that are wrong, OR claims that are presented as fact when they should be flagged as uncertain?

### N/A — When this dimension doesn't apply
Pure creative writing with no factual surface (a fictional scene, pure voice exercise, an opinion-only essay with no claims about people/events/data) — mark N/A and skip the veto. The N/A bar is HIGH: if the piece mentions any real person, brand, statistic, or historical event, factual grounding applies.

---

## How to Score in chain_runner finalize()

When running `python3 execution/chain_runner.py finalize`:

```bash
python3 execution/chain_runner.py finalize "<output description>" \
    --expert <expert> --skill <skill> --workflow <workflow> --type Content \
    --intent <1-10>           # Use Anchor 9 / 6 / 3 above
    --expert-score <1-10>     # Use Anchor 9 / 6 / 3 above
    --adversarial <1-10>      # Use Anchor 9 / 6 / 3 above
    --notes "Factual Grounding: <1-10 or N/A> | Verification: PASS|FAIL|PARTIAL|N/A | <other notes>"
```

**Pre-scoring checklist** (run mentally before assigning scores):
1. Did I name the anchor for each dimension? If I can't, I'm scoring on vibes.
2. If I scored 8+ on Expert Standard, did I check that the output couldn't have been produced WITHOUT the expert files loaded?
3. If I scored 8+ on Adversarial Resilience, did I imagine a specific critic and what they'd attack?
4. If I scored ≥6 on Factual Grounding (not N/A), did I actually verify the top 3 factual claims in the last 5 minutes?

**Post-scoring sanity check**:
- Composite ≥8.5 means "world-class deliverable to a paying client." Use only when true.
- Composite 7.0-8.4 means "ships to internal use, refine before paid use."
- Composite <7 triggers retry of the weakest dimension.
- Factual Grounding <6 (not N/A) blocks delivery.

---

## Calibration Status

This rubric ships with seeded anchors but is **NOT yet calibrated against ground truth**. Calibration requires:
1. The accompanying `eval_set_v1.jsonl` (30 tasks with expected pass/fail) to be filled out by the user as the calibration human
2. A blind-comparison pass: run the rubric against 5 historical outputs WITHOUT knowing their original scores; compare results
3. If divergence > 1.5 points on any dimension, refine the anchors

**Until calibration is complete, treat scores as advisory.** The rubric becomes load-bearing once at least 15 of the 30 eval tasks have human-validated scores and the blind-comparison pass shows <1.0 point average divergence.

See: [`eval_set_v1.jsonl`](eval_set_v1.jsonl) | [`execution/eval_harness.py`](../../execution/eval_harness.py)

---

## Bimodal Taste Calibration Profile (Farrice) — Wave 2 / 2026-05-21

This section encodes Farrice's calibration signature as documented in
`memory/user_taste-calibration-signature.md`. It overlays the rubric above
with a programmatic filter implemented in [`execution/taste_signature.py`](../../execution/taste_signature.py).
The filter runs ON TOP of the rubric, not in place of it — the rubric still
defines what each score MEANS, the filter defines how those scores
COMBINE into a pass/fail verdict.

### Distribution shape

Farrice's quality judgment is **bimodal**:
- **Clear PASS**: composite ≥7.5 AND every dimension ≥7
- **Clear FAIL**: composite <7.0 OR any dimension ≤6
- **Marginal band (7.0-7.5)**: narrow, treated as FAIL by default ("when in doubt, fail")

This is the inverse of the system's pre-Wave-2 distribution, which had 94-99%
of finalize scores clustered above 8 (per the 2026-04-24 audit). The bimodal
filter is how the system mirrors actual human taste instead of drifting
toward grade inflation.

### The 5 rules (implemented in `taste_signature.apply()`)

**Rule 1 — Failure penalty**: Any dimension at or below 6 is reduced by
-1.0 on that dimension. The cost of a false PASS (shipping work that isn't
ready) is much higher than the cost of a false FAIL (one extra iteration).
When in doubt, fail harder.

**Rule 2 — 8 must be earned**: Any dimension ≥8 without `anchor_named=True`
is capped at 7.5. To claim an 8 or above on any dimension, Claude must
name the rubric anchor it matches and explain why. Without that evidence,
the score reflects an aspiration, not a measurement.

**Rule 3 — Anti-cluster**: If all three dimensions score ≥8 AND
`anchor_named=False` AND prose_classifier verdict is not CLEAN, the
combination is suspicious — composite is capped at 7.5 and the verdict
is forced to MARGINAL. (When Wave 1's AI Prose cap already broke the
cluster by dropping one dimension, Rule 3 doesn't fire — Wave 1 handled it.)

**Rule 4 — Bimodal verdict mapping**:
- **PASS**: composite ≥7.5 AND all dims ≥7
- **MARGINAL**: composite in [7.0, 7.5) — bimodal taste rejects this band
- **FAIL**: composite <7 OR any dim ≤6

**Rule 5 — Factual veto override**: If `factual_grounding` is set and <6,
verdict is forced to FAIL regardless of composite. This is defense in
depth — Wave 1's `_enforce_caps` already blocks delivery on factual veto,
Rule 5 ensures the taste filter agrees if Wave 1 ever loses the signal.

### Why this works against grade inflation

The 2026-04-24 audit found 94-99% of recent traces scored 8+. Wave 2's
Rule 2 makes that statistically impossible without explicit anchor naming:
every claimed 8 must point to a worked example in the rubric. Claude can
still SELF-SCORE highly, but the system caps the result.

The `anchor_named` flag is the bridge between Claude's introspective
quality estimate and the rubric's anchored measurement. If Claude sets
the flag, Claude is asserting "I can name the anchor for this 8." That
assertion is auditable — every finalize trace stores `anchor_named` in
the result dict.

### Why `rubric_load_bearing: false` still holds

Wave 2 enforces the bimodal taste signature WITHOUT modifying the rubric
itself. The rubric stays in its current calibration state (15+ eval entries
required for promotion to load-bearing). The taste filter is independent —
it provides PASS/FAIL judgment using the rubric's anchored scores as
input, not by rewriting the anchors.

This separation matters per `memory/feedback_auto-evolution-cant-substitute-for-ground-truth.md`:
auto-modification of subjective evaluation criteria drifts toward inflation
without human calibration. The filter does not modify the rubric, so it
does not violate the pause.

### Configuration

Tunable thresholds in `execution/taste_signature.py`:
- `_FAILURE_PENALTY_THRESHOLD = 6.0`
- `_FAILURE_PENALTY_AMOUNT = 1.0`
- `_EARNED_8_THRESHOLD = 8.0`
- `_EARNED_8_CAP = 7.5`
- `_PASS_COMPOSITE_FLOOR = 7.5`
- `_PASS_DIMENSION_FLOOR = 7.0`
- `_FAIL_DIMENSION_CEILING = 6.0`
- `_FAIL_COMPOSITE_CEILING = 7.0`
- `_FACTUAL_VETO_FLOOR = 6.0`

These should not be tuned without empirical evidence that the current
values produce a distribution mismatched to Farrice's actual PASS/FAIL
judgments on real deliverables.
