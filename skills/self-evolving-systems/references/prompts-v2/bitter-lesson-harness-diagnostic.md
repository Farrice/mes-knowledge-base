---
name: "Self-Evolving Systems — Bitter Lesson Harness Diagnostic"
source_prompt: born-v2
skill: self-evolving-systems
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are applying **Rich Sutton's Bitter Lesson** to an Antigravity harness component, using the MetaHarness composite frame (Yoonho Lee / Andrej Karpathy / Rich Sutton, sourced from "MetaHarness — End-to-End Optimization of Model Harnesses," arXiv:2603.28052v1, Stanford/MIT/Crafted). The Bitter Lesson: hand-engineered heuristics always lose to learned/evolved solutions eventually. Every manually-tuned component is a candidate for evolution — the real question is *when*, not *whether*.

This deliverable runs BEFORE an evolution cycle, not instead of one. Its job is to answer two questions with evidence: is a given quality problem harness-level or model-level, and which of the hand-coded pieces inside this component are legitimate evolution candidates versus genuine safety rails that must stay hand-coded. Skipping this diagnostic and jumping straight to "upgrade the model" or "evolve everything" is exactly the anti-pattern it exists to prevent.

## Input Required

- **[SYSTEM/COMPONENT UNDER REVIEW]** — the specific workflow, prompt, retrieval routine, or orchestration pattern being diagnosed
- **[OBSERVED QUALITY ISSUE]** — the concrete symptom: e.g., quality gate scores plateauing at 6-7, a recurring error class, a specific failure pattern
- **[CURRENT HAND-CODED HEURISTICS]** — an inventory of the manually-tuned rules, prompts, thresholds, or logic branches currently inside the component
- **[PROPOSED FIX]** — whatever remedy is already on the table, if any (e.g., "upgrade to a more expensive model," "add another manual rule") — state "NONE PROPOSED YET" if this diagnostic is running proactively

## Execution Protocol

### Step 1 — The 6x Lever test

Before accepting [PROPOSED FIX] (especially if it's a model upgrade), exhaustively examine the harness: prompt construction, retrieval logic, state management, orchestration sequencing. The founding evidence for this test is that harness engineering alone produces a 6x performance gap on the same model weights and the same task — the harness is an intelligence layer, not decoration. Document what was actually examined, not just that the check was "considered."

Score this step against the source rubric's three anchors:
- **4 (Acceptable)**: blames model capability without examining the workflow, prompts, or retrieval logic.
- **7 (Good)**: investigates the harness before considering a model upgrade, but doesn't systematically isolate the actual failure point.
- **10 (Savant)**: exhaustively diagnoses prompt construction, state management, and retrieval logic before any model-level intervention, and can point to the specific mechanism that produces [OBSERVED QUALITY ISSUE].

State which anchor the diagnosis actually reached, and why.

### Step 2 — Heuristic-by-heuristic Bitter Lesson candidacy

For each item in [CURRENT HAND-CODED HEURISTICS], classify it as one of:
- **Safety rail (never evolve)** — a non-negotiable behavior, brand-voice constraint, or genuine safety boundary that must stay hand-coded regardless of score potential.
- **Evolution candidate** — a manually-tuned rule/prompt/threshold that exists because someone hand-tuned it, not because it must be fixed; a legitimate target for a future MetaHarness cycle.

Score the overall candidacy work against the source rubric's three anchors:
- **4**: treats hand-engineered workflows as sacred, resists evolution on the grounds of time already invested.
- **7**: acknowledges evolution potential but only applies it to low-value or peripheral heuristics.
- **10**: treats every manually-tuned component as a candidate — the hand-crafted effort is respected as a warm start for evolution, not treated as a ceiling.

### Step 3 — Anti-pattern scan against the observed issue

Check [OBSERVED QUALITY ISSUE] against these seven failure modes and state which, if any, are actually in play (do not check all seven mechanically — reason about which apply to this specific symptom):
1. Score Worship — optimizing a number without understanding why it moved
2. Trace Amnesia — no execution trace was ever logged, only final scores
3. Success Bias — only winning variants were ever reviewed
4. Premature Optimization — evolution was attempted before any manual tuning happened at all
5. Iteration Inflation — many iterations were run past the point of diminishing returns
6. Skill Neglect — the proposer's instruction quality was never invested in
7. Monolithic Prompts — everything was packed into one prompt instead of adaptive access

### Step 4 — Compounding-investment note

If the verdict favors harness evolution, note explicitly: because the proposer is itself powered by a model, every frontier-model upgrade makes future evolution cycles on this component more effective automatically, at no extra harness-design cost. This is a reason to invest in evolution infrastructure now rather than defer it — it is not a reason to skip the diagnosis and evolve blindly.

### Step 5 — Verdict and routing

Render one of: **HARNESS-LEVEL** (evolve first — the harness has not been genuinely optimized), **MODEL-LEVEL** (the harness is already close to its ceiling; a model upgrade is justified), or **MIXED** (both apply — specify which parts). Tie the verdict directly to the evidence gathered in Steps 1-3, not to intuition.

If the verdict is HARNESS-LEVEL, recommend which MetaHarness deliverable should run next:
- A single **MetaHarness Evolution Cycle** if this is the first pass or no evolution history exists yet.
- A **Trajectory Ratchet** cycle if evolution history already exists for this component (2+ prior cycles) and the concern is whether progress is genuinely compounding.
- Note if the recurring-error pattern in [OBSERVED QUALITY ISSUE] suggests a self-annealing pass (fixing recurring mistakes) should run before or alongside a full evolution cycle.

## Output Contract

A **Bitter Lesson / Harness Diagnostic Report**: the 6x Lever verdict with its rubric anchor and evidence, a full heuristic-by-heuristic candidacy table (every item from [CURRENT HAND-CODED HEURISTICS] classified, none skipped), the anti-pattern scan results, the compounding-investment note if the verdict favors evolution, and a final routing recommendation naming a specific next deliverable.

## Output Skeleton

```
## Bitter Lesson / Harness Diagnostic — [SYSTEM/COMPONENT UNDER REVIEW]

### 6x Lever Test
- What was examined: [prompt construction / retrieval logic / state management / orchestration — specifics]
- Rubric anchor reached: [4 / 7 / 10]
- Reasoning: [tied to specifics of OBSERVED QUALITY ISSUE]

### Heuristic Candidacy Table
| Heuristic | Classification (Safety Rail / Evolution Candidate) | Reasoning |
|---|---|---|
[one row per item in CURRENT HAND-CODED HEURISTICS, none omitted]

- Candidacy rubric anchor reached: [4 / 7 / 10]

### Anti-Pattern Scan
- Score Worship: [in play / not — why]
- Trace Amnesia: [in play / not — why]
- Success Bias: [in play / not — why]
- Premature Optimization: [in play / not — why]
- Iteration Inflation: [in play / not — why]
- Skill Neglect: [in play / not — why]
- Monolithic Prompts: [in play / not — why]

### Compounding-Investment Note
[only if verdict favors evolution — one paragraph]

### Verdict: [HARNESS-LEVEL / MODEL-LEVEL / MIXED]
- Evidence: [tied to Steps 1-3]

### Routing Recommendation
- Next deliverable: [MetaHarness Evolution Cycle / Trajectory Ratchet / self-annealing pass first]
- First frontier to target: [specific, measurable]
```

## Quality Gate

- Does the 6x Lever test cite specific things examined (prompt construction, retrieval logic, state management), not a generic "the harness was reviewed"?
- Is every item from [CURRENT HAND-CODED HEURISTICS] classified in the candidacy table — none silently dropped?
- Is at least one anti-pattern explicitly ruled IN or OUT with reasoning, rather than the whole section defaulting to "none apply"?
- Does the final verdict cite evidence from Steps 1-3 rather than asserting a conclusion first?
- If [PROPOSED FIX] was a model upgrade, does the report explicitly state whether the harness was found to already be near-optimal (justifying the upgrade) or not (contradicting it)?
- Does the routing recommendation name one specific next deliverable rather than a vague "continue evolving"?

## Creative Latitude

The classification calls in Step 2 are inherently judgment, not formula — the same heuristic could be a safety rail in one system and an evolution candidate in another depending on what it actually protects (brand voice, factual grounding, legal/compliance boundaries are typically safety rails; hand-tuned scoring thresholds or prompt phrasing are typically candidates). State the reasoning for each classification rather than defaulting to a pattern-match on the heuristic's name. Similarly, the Step 5 verdict when evidence is genuinely mixed should say so plainly rather than forcing a clean HARNESS-LEVEL/MODEL-LEVEL split the evidence doesn't support.

## Deploy When

- Before upgrading to a more expensive model to fix a quality problem — confirm the ceiling is genuinely model-level first.
- A workflow's quality gate scores have plateaued and the instinct is "we need a smarter model," not "we need a better harness."
- Deciding which parts of a hand-tuned system are safe to hand off to an evolution loop and which must stay manually controlled.
- Before a large evolution investment (a full Proposer Sprint or multi-cycle Trajectory Ratchet), to confirm the target and scope are correctly identified first.
