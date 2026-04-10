# Self-Evolving Systems (MetaHarness) — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

The genius of MetaHarness is that harness engineering produces a 6x performance gap on the same model weights — the harness IS the intelligence layer, not decoration. The system deliberately avoids hand-coded search heuristics (Bitter Lesson), gives the proposer agent full trace access to ALL prior iterations including failures, and represents evolved artifacts as executable code to exploit coding models' natural regularization bias. Invest in evolution infrastructure now; it pays compound interest as models improve.

---

## Genius Patterns (Compressed)

### GP1: The 6x Lever
Harness engineering produces 6x performance gap on same model weights. When output is mediocre, resist blaming the model — the workflow's prompt construction, retrieval logic, and state management are at least as responsible. Evolve those first.

### GP2: The Proposer Must Be an Agent, Not a Prompt
The proposer needs file system access, dev tools, navigation — not a raw LLM with a fixed prompt. It must access prior harness code (all versions), execution traces, and have freedom to make local edits OR full rewrites. Summarizing history into a fixed prompt loses diagnostic signal.

### GP3: Let It See the Failures
Keep ALL iterations including low-performing ones. A poor-scoring harness might have one brilliant insight buried in bad execution. No parent-selection rule — the proposer can inspect any prior harness, preventing local maxima.

### GP4: Search Set = Your Hardest Cases
Construct the search set from examples the baseline gets WRONG or a diverse subset of difficult instances. Mine quality gate failures and expert-standard scores < 7. Evolution has nothing to optimize if the baseline already saturates.

### GP5: The Skill Text Dominates
Iterating on the skill text (instructions to the proposer) had larger effect than changing iteration count or population size. Run 3-5 short evolution runs to debug the skill BEFORE a full run. Skill quality determines the ceiling.

### GP6: Code-Space Regularity Bias
Represent evolved artifacts as executable code or structured workflows, not arbitrary text. Coding models naturally propose coherent algorithms rather than brittle heuristics. Code space has inherent regularization bias toward generalizable solutions.

### GP7: Trace > Score (Diagnostic Richness)
Compressed feedback (scalar scores, summaries) removes information needed to trace failures to earlier decisions. Log EVERYTHING: actual prompts sent, responses received, state updates, retrieval queries, files accessed. Store in JSON, make queryable.

### GP8: The Bitter Lesson Is Real
Hand-engineered heuristics always lose to learned solutions at scale. Every manually-tuned component is a candidate for evolution. The question isn't whether — it's when. Hand-crafted effort is a warm-start, not a ceiling.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | Proposer Gets Better at Proposing: As coding agents improve with each frontier model, all evolution loops become more effective without changing anything. | Invest in evolution infrastructure now — compound interest as models improve. |
| HK2 | Warm-Starting from Offline Experience: Relevant rollouts, solved corpora, and papers can be converted into same directory structure to warm-start exploration. Quality gate logs and Chain outputs are evolution warm-start material. | When starting new evolution loops with existing performance history. |
| HK3 | Lightweight Validation Saves 90% of Wasted Eval Cost: Simple test (import, instantiate, call on 2-3 examples) catches most malformed candidates in seconds. | Every evolution loop needs a fast pre-check gate before expensive evaluation. |
| HK4 | CLI Saves Proposer Tokens: Small CLI (list-frontier, show-best 5, diff harness_003 harness_007) saves significant navigation tokens. Aligned with how coding agents are trained. | Build evolution tooling with proposer shortcuts. |
| HK5 | Co-Evolution Is the Next Frontier: Co-evolve harness AND model weights simultaneously. Strategy shapes what model learns, vice versa. Today: frozen models. Tomorrow: double optimization loop. | Watch this space — future capability. |

---

## Decision Framework

Before any evolution run: (1) What is the target? (2) What is the evaluation metric? (3) What is the search set? (4) How many iterations? (5) What is the baseline? (6) What can the proposer change? (7) What is forbidden?

## Anti-Patterns

1. **Score Worship** — Optimizing single number without understanding WHY
2. **Trace Amnesia** — Not logging execution traces, only final scores
3. **Success Bias** — Only showing proposer winning variants
4. **Premature Optimization** — Evolving before manual tuning
5. **Iteration Inflation** — 100 iterations when 20 suffice
6. **Skill Neglect** — Under-investing in instruction quality for proposer
7. **Monolithic Prompts** — Packing everything into one prompt vs. adaptive access

---

## Signature Moves

1. **6x Lever Diagnosis** — When quality is low, exhaustively diagnoses harness (prompts, retrieval, state) before any model-level intervention.
2. **Trace-First Debugging** — Examines full execution traces (prompts sent, outputs received, state mutations) to form causal hypotheses before proposing changes.
3. **Hardest-Cases Search Set** — Constructs evaluation sets exclusively from quality gate failures and low-scoring outputs.
4. **Skill Text Sprint** — Runs 3-5 short diagnostic cycles to refine skill/instruction text BEFORE main evolution loop.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| 6x Lever Application | Defaults to model upgrades for quality problems | Diagnoses whether issue is model-level or harness-level | Produces 2x+ improvement by evolving prompts/retrieval/state without changing model |
| Proposer Agent Quality | Static prompt with summarized history | Trace access and prior version navigation, manual search | Autonomous inspection of traces, diffs, targeted hypotheses with measurable predictions |
| Evaluation Rigor | Single score, no holdout validation | Fixed benchmark with consistent rubric, detects regressions | Multi-dimensional scoring, holdout sets, statistical significance, regression detection |
| Trace Architecture | Logs final scores only | Logs prompts and outputs, searchable | Full pipeline: prompts, outputs, timing, token counts, per-step signals — indexed and diff-able |
| Evolution Discipline | No stopping criteria, iterates until budget exhausted | Defined budget with keep/discard protocol | Convergence detection, plateau detection, binary keep/discard, deliberate scope constraints |
| Anti-Pattern Avoidance | Falls into 2+ anti-patterns unrecognized | Avoids major anti-patterns, occasional premature optimization | Actively monitors all 7 anti-patterns, self-corrects, documents corrections |
| Bitter Lesson Alignment | Treats hand-engineered workflows as sacred | Acknowledges evolution but only for peripheral components | Every manually-tuned component is a candidate — hand-crafted effort is warm-start, not ceiling |
