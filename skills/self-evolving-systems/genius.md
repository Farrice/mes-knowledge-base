# Self-Evolving Systems (MetaHarness) — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## How to Use This Skill (Model Calibration)

These patterns are intuition primitives, not a checklist. Absorb GP-1 through GP-8, then diagnose originally. If the output mechanically stamps "Applying GP-4: Search Set Construction" before doing the actual work, you have failed — that's vocabulary, not method.

Specifically:
- Do NOT enumerate which genius patterns or hidden-knowledge items you applied unless asked. Run the diagnosis; never narrate the framework on the page.
- Do NOT open with "Let's evolve the harness" or close with a checklist recap of GP numbers. The proposer's job is to find the failure mode and propose a change — not to perform methodology.
- This composite's texture is engineering pragmatism, not persuasion: no hype, no "significant improvement" — name the actual number ("6x performance gap," "700 experiments in 48 hours," "11% speedup"). A confident-sounding claim with no number attached is the tell that the diagnosis was invented, not run.
- The recognition test: would someone fluent in Karpathy's autoresearch loop and the MetaHarness propose-evaluate-log-iterate cycle recognize this as a harness actually being diagnosed and evolved — or as evolution vocabulary borrowed to dress up a manual edit? If it's the second, rebuild from GP-1: is this actually a harness problem, or did you skip straight to a fix without checking whether the failure is model-level or harness-level?
- Trace-first, always. If you can't point to the specific prompt, retrieval query, or state mutation that caused the failure, you haven't diagnosed it — you've guessed and dressed the guess in evolution terminology (GP-7, Trace > Score).

---

## Core Operating System

The genius of MetaHarness is that harness engineering produces a 6x performance gap on the same model weights — the harness IS the intelligence layer, not decoration. The system deliberately avoids hand-coded search heuristics (Bitter Lesson), gives the proposer agent full trace access to ALL prior iterations including failures, and represents evolved artifacts as executable code to exploit coding models' natural regularization bias. Invest in evolution infrastructure now; it pays compound interest as models improve.

---

## Genius Patterns

### GP-1: The 6x Lever
**What it is**: Harness engineering produces a 6x performance gap on the same model weights, the same benchmark, the same task. The harness is not decoration — it IS the intelligence layer.

**How to apply**: When a workflow produces mediocre output, the instinct is to blame the model. Resist it. The workflow's prompt construction, retrieval logic, and state management are at least as responsible. Evolve those first.

**Anti-pattern**: Upgrading from Gemini 2.5 Flash to Gemini 2.5 Pro to fix a quality problem that exists in the harness.

---

### GP-2: The Proposer Must Be an Agent, Not a Prompt
**What it is**: MetaHarness uses a coding agent (with file system access, dev tools, navigation) as its proposer — not a raw LLM with a fixed prompt. The proposer decides what to inspect, what to change, and how much to change.

**How to apply**: When running evolution loops, the proposer must have:
- Access to prior harness code (all versions, not just the best)
- Access to execution traces (actual prompts sent, actual outputs received)
- Ability to navigate and search the artifact store via grep/cat/diff
- Freedom to make local edits OR full rewrites

**Anti-pattern**: Summarizing evolution history into a fixed prompt and asking the model "what should change?" — this loses the diagnostic signal.

**Grounding**: Karpathy's own proposer ran unattended for "700 experiments in 48 hours. 20 genuine improvements discovered" (`research_outputs/research-karpathy-wiki-architecture.md`, 2026-03-17 Fortune interview) — a volume no human-paced review loop reaches.

---

### GP-3: Let It See the Failures
**What it is**: MetaHarness imposes no parent-selection rule. The proposer can inspect ANY prior harness — including low-performing ones. This prevents local maxima by letting the proposer learn from failures, not just successes.

**How to apply**: When logging evolution history, keep ALL iterations — not just improvements. A harness that scored poorly might have one brilliant insight buried in a bad execution. The proposer can find it.

**Anti-pattern**: Only showing the proposer the top-3 performing variants.

**Grounding**: Antigravity's own `directives/skill-evolution-protocol.md` (Effective 2026-03-10) enforces the same discipline in Safety Rail 4 — "even failures are data" — and Step 7 logs every DISCARDED attempt precisely so the same hypothesis doesn't get retried.

---

### GP-4: Search Set = Your Hardest Cases
**What it is**: The search set should be constructed from examples the baseline gets WRONG, or a diverse subset of difficult instances. Evolution has nothing to optimize if the baseline already saturates.

**How to apply**: Mine quality gate failures, low-scoring Chain outputs, expert-standard scores < 7 as the search set. These are the cases where the current harness breaks down. Evolution targets them specifically.

**Anti-pattern**: Evaluating evolution against easy examples where everything already scores 9+.

**Grounding**: The Excellence Prediction Protocol's 2026-04-24 audit is the canonical internal example — it found "94-99% of finalize scores were 8+ while real iteration counts were 2-3 passes" (`directives/excellence-prediction-protocol.md`), proof the scoring, not the underlying work, was the soft target that evolution should have been aimed at.

---

### GP-5: The Skill Text Dominates
**What it is**: Iterating on the skill text (the instructions given to the proposer) had a larger effect on search quality than changing iteration count or population size. Run 3-5 short evolution runs specifically to debug the skill before a full run.

**How to apply**: Before running a 20-iteration evolution loop, run 3 quick 3-iteration loops focused on refining the skill/workflow description. The quality of the instructions to the proposer determines the ceiling of what evolution can discover.

**Anti-pattern**: Running 50 iterations with a mediocre skill description and expecting evolution to compensate.

**Grounding**: `directives/skill-evolution-protocol.md` caps benchmark tasks at a "10 minutes per benchmark task" time-box, explicitly "inspired by Karpathy's 5-minute training runs" — the same discipline applied to skill-text debugging cycles, not just full evolution runs.

---

### GP-6: Code-Space Regularity Bias
**What it is**: When harnesses are represented as programs (not templates or configs), coding models naturally propose coherent algorithms rather than brittle heuristics. Code space has an inherent regularization bias.

**How to apply**: Represent evolved artifacts as executable code or structured workflows, not arbitrary text. The proposer's coding training naturally regularizes the search toward generalizable solutions.

**Anti-pattern**: Evolving free-form prompt text where the proposer can generate arbitrary, unstructured content.

**Grounding**: Karpathy's own arena enforces this literally: the agent may modify exactly one file (`train.py`), against one measurable metric, inside a fixed 5-minute window (`research_outputs/research-karpathy-wiki-architecture.md`, 2026-03-17) — the "constrained arena" that makes the search space regular enough to trust.

---

### GP-7: Trace > Score (The Diagnostic Richness Principle)
**What it is**: Compressed feedback (scalar scores, summaries) removes the information needed to trace downstream failures to earlier harness decisions. Raw execution traces let the proposer form and test causal hypotheses.

**How to apply**: Log EVERYTHING: the actual prompt sent to the model, the actual response received, the state updates made, the retrieval queries issued, the files accessed. Store in JSON. Make queryable.

**Anti-pattern**: Logging only the final quality score (e.g., "7/10") without the trace that produced it.

**Grounding**: One of Karpathy's 20 kept improvements was a missing scalar multiplier in QK-Norm attention — invisible in the score, visible only in the trace — worth an "11% speedup (2.02 → 1.80 hours)" once found (`research_outputs/research-karpathy-wiki-architecture.md`, 2026-03-17 Fortune interview).

---

### GP-8: The Bitter Lesson Is Real
**What it is**: Rich Sutton's observation that hand-engineered heuristics always lose to learned solutions at scale. Applied to harnesses: hand-tuned prompts, manually designed workflows, and human-curated retrieval logic will be outperformed by evolved versions.

**How to apply**: Every manually-tuned component in Antigravity is a candidate for evolution. The question isn't whether to evolve it — it's when. Start with the highest-value, most-manually-tuned workflows.

**Anti-pattern**: Believing your hand-crafted workflow is already optimal because you spent a lot of time on it.

**Grounding**: The pattern generalized fast in practice — Karpathy's autoresearch repo hit "42,000 GitHub stars in one week" and was independently ported to cold-email reply rates, page-render speed, and retrieval accuracy within days (`research_outputs/research-karpathy-wiki-architecture.md`, March-April 2026).

---

## Hidden Knowledge

### HK-1: The Proposer Gets Better at Proposing
**What it is**: By leaving diagnosis and edit decisions to the proposer, MetaHarness improves automatically as coding agents become more capable. Each frontier model upgrade makes all evolution loops more effective without changing anything.

**Implication**: Invest in evolution infrastructure now. It pays compound interest as models improve.

**Grounding**: `directives/skill-evolution-protocol.md` logged an Activation Count of 42 and 76 Phase 1 entries by 2026-04-09 — infrastructure that kept paying down as the underlying proposer improved, without a rewrite.

---

### HK-2: Warm-Starting from Offline Experience
**What it is**: If relevant offline experience exists (rollouts from other models, solved problem corpora, relevant papers), converting it into the same directory structure can warm-start exploration and ground new ideas.

**Implication**: Quality gate logs, past Chain finalize outputs, and session state files can all be converted into evolution warm-start material.

**Grounding**: The Excellence Prediction Protocol already does this in production — it trains its bucketed-median predictor on the existing `evolution_store/v2_traces/` corpus ("159 files at time of writing" — `directives/excellence-prediction-protocol.md`), no separate model-training step required.

---

### HK-3: Lightweight Validation Saves 90% of Wasted Eval Cost
**What it is**: A simple test (import, instantiate, call on 2-3 examples) catches most malformed or nonfunctional candidates in seconds. Run this before expensive full evaluation.

**Implication**: Every evolution loop should have a fast pre-check gate. Don't spend evaluation tokens on broken candidates.

**Grounding**: Antigravity's analog is the finalize-time grade-inflation detector, which flags when more than 80% of the last 10 traces score 8+ — a cheap statistical check that runs before anyone spends a full quality-gate pass re-litigating the result (`directives/excellence-prediction-protocol.md`, `detect_grade_inflation()`).

---

### HK-4: The CLI Saves Proposer Tokens
**What it is**: A small CLI that lists the Pareto frontier, shows top-k harnesses, and diffs code between runs can save the proposer significant tokens on navigation.

**Implication**: Build evolution tooling that gives the proposer shortcuts. `list-frontier`, `show-best 5`, `diff harness_003 harness_007`. This is closely aligned with how coding agents are trained.

**Grounding**: `execution/skill_benchmark.py benchmark <skill-name>` is Antigravity's version of this shortcut — it returns weakest workflow and dimension in a single call instead of forcing the proposer to re-derive it from raw logs (`directives/skill-evolution-protocol.md`, Step 1).

---

### HK-5: Co-Evolution Is the Next Frontier
**What it is**: The paper's "natural next step" — co-evolve the harness AND the model weights simultaneously. The strategy shapes what the model learns, and vice versa.

**Implication**: Today we evolve harnesses around frozen models. Tomorrow we fine-tune small models with evolved harnesses, creating a double optimization loop. Watch this space.

**Grounding**: Not yet implemented anywhere in Antigravity — flagged UNCONFIRMED as a live capability in `references/source-ledger.md`. The closest existing analog is the "3 consecutive DISCARD results" stopping rule in `directives/skill-evolution-protocol.md`, which still assumes frozen skill weights throughout.

---

## Decision Framework

Before running any evolution workflow, answer:

1. **What is the target?** — Specific workflow, prompt, retrieval logic, or orchestration pattern
2. **What is the evaluation metric?** — Quality gate score, accuracy, token cost, user satisfaction
3. **What is the search set?** — Past failures, hard examples, edge cases
4. **How many iterations?** — 5 for quick sprints, 10-20 for full evolution
5. **What is the baseline?** — Current version, documented performance
6. **What can the proposer change?** — Constraints on scope (everything? prompts only? flow only?)
7. **What is forbidden?** — Safety rails, non-negotiable behaviors, brand voice

---

## Anti-Patterns

1. **Score Worship** — Optimizing for a single number instead of understanding WHY it's that number; internal precedent for this failure mode is the 2026-04-24 finalize audit that found "94-99% of finalize scores were 8+ while real iteration counts were 2-3 passes" (`directives/excellence-prediction-protocol.md`)
2. **Trace Amnesia** — Not logging execution traces, only final scores; Karpathy's autoresearch avoids this by design — "the ratchet name comes from git: each success adds a commit, each failure reverts" (`research_outputs/research-karpathy-wiki-architecture.md`, 2026-03-17 Fortune interview)
3. **Success Bias** — Only showing the proposer winning variants, hiding failures; Antigravity's own evolution protocol names the fix directly as Safety Rail 4 — "even failures are data" (`directives/skill-evolution-protocol.md`, Effective 2026-03-10)
4. **Premature Optimization** — Running evolution on a system that hasn't been manually tuned at all yet; matches the Plateau trigger threshold of "10+ outputs with < 0.5 variance" that must be met before evolution fires at all (`directives/skill-evolution-protocol.md`, 2026-03-10)
5. **Iteration Inflation** — Running 100 iterations when 20 would suffice (diminishing returns); the internal stopping rule is explicit — "3 consecutive DISCARD results on the same skill" ends the cycle (`directives/skill-evolution-protocol.md`, Stopping Criteria, updated 2026-04-06)
6. **Skill Neglect** — Under-investing in the skill/instruction quality for the proposer; the Excellence Prediction Protocol responds to exactly this gap by forcing a reload — "Load `skills/<skill>/genius.md` at session start (tier 2 instead of tier 1)" whenever expert_standard is flagged high-risk (`directives/excellence-prediction-protocol.md`, Wave 3, 2026-05-21)
7. **Monolithic Prompts** — Packing everything into one prompt instead of giving adaptive access; the variant-generation rule requires proposers to "modify only the targeted aspect (process steps, inline patterns, quality gate criteria)" per cycle, never the whole workflow at once (`directives/skill-evolution-protocol.md`, Step 4, 2026-03-10)

---

## Voice DNA

This skill speaks in **engineering pragmatism**:
- No hype. Results speak. "Discovered harnesses surpass hand-engineered baselines."
- Specificity over abstraction. "6x performance gap" not "significant improvement."
- Let the data lead. "Run 3-5 short cycles to debug the skill" — concrete, actionable.
- Humility about hand-engineering. "This simplicity is deliberate" — trust the system.

---

## Verbatim Grounding

Direct quotes from the primary sources this skill's composite voice actually draws on, included so the language can be checked against real originals rather than paraphrase drift. See `references/source-ledger.md` for the full claim-by-claim provenance table.

> "You're not touching any of the Python files. Instead, you are programming the program.md Markdown files that provide context to the AI agents."

— Karpathy, autoresearch GitHub README, quoted in `research_outputs/research-karpathy-wiki-architecture.md` (2026-03, primary source: github.com/karpathy/autoresearch)

> "The ratchet name comes from git: each success adds a commit, each failure reverts. The codebase can only move forward."

— synthesis of Karpathy's autoresearch loop in `research_outputs/research-karpathy-wiki-architecture.md`, 2026-03-17 (Fortune interview quotes)

---

## Expert-Specific Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
| :--- | :--- | :--- | :--- |
| **6x Lever Application** | Identifies that harness matters, but defaults to model upgrades when quality is low. | Diagnoses whether a quality issue is model-level or harness-level, and targets the right one. | Produces a 2x+ improvement by evolving prompts, retrieval, or state management without changing model weights. |
| **Proposer Agent Quality** | Proposer is a static prompt with summarized history; loses diagnostic signal. | Proposer has trace access and can navigate prior versions, but search strategy is manual. | Proposer autonomously inspects traces, diffs prior versions, and generates targeted hypotheses with measurable predictions. |
| **Evaluation Rigor** | Uses a single score or subjective assessment; no holdout validation. | Fixed benchmark tasks with consistent rubric; detects obvious regressions. | Multi-dimensional scoring with holdout sets, statistical significance checks, and regression detection across all quality dimensions. |
| **Trace Architecture** | Logs final scores only; no execution traces or intermediate state. | Logs prompts sent and outputs received; traces are searchable but not systematically analyzed. | Full trace pipeline: prompts, outputs, timing, token counts, and per-step quality signals — all indexed and diff-able across iterations. |
| **Evolution Discipline** | Runs evolution without clear stopping criteria; iterates until budget exhausted. | Defined iteration budget with keep/discard protocol, but may over-iterate on diminishing returns. | Precise stopping criteria (convergence detection, plateau detection), binary keep/discard after each cycle, and deliberate scope constraints on what the proposer can change. |
| **Anti-Pattern Avoidance** | Falls into 2+ anti-patterns (score worship, trace amnesia, success bias) without recognizing them. | Avoids major anti-patterns but occasionally runs premature optimization or iteration inflation. | Actively monitors for all 7 anti-patterns, self-corrects when detected, and documents the correction in evolution logs. |

---

## Expert-Specific Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
| :--- | :--- | :--- | :--- |
| **Harness-First Diagnosis** | Blames model capability for poor output without examining the workflow, prompts, or retrieval logic. | Investigates the harness before considering model upgrades, but doesn't systematically isolate the failure point. | Applies the 6x Lever principle — exhaustively diagnoses prompt construction, state management, and retrieval logic before any model-level intervention. |
| **Trace Diagnostic Richness** | Logs only final scores or pass/fail without capturing the execution trace that produced the result. | Logs prompts and outputs but misses intermediate state (retrieval queries, file access, state updates). | Captures complete execution traces in queryable format — every prompt sent, response received, state mutation, and retrieval query — enabling causal hypothesis formation. |
| **Search Set Construction** | Evaluates evolution against easy examples where the baseline already performs well. | Uses a mix of easy and hard cases, but doesn't specifically mine quality gate failures or low-scoring outputs. | Constructs the search set exclusively from the system's hardest cases — quality gate failures, expert-standard scores below 7, and edge cases where the current harness breaks down. |
| **Proposer Agency** | Summarizes evolution history into a fixed prompt and asks "what should change?" — losing diagnostic signal. | Gives the proposer access to prior versions and scores, but limits navigation and inspection capabilities. | Proposer operates as a full coding agent with file system access, grep/diff tools, access to ALL prior harnesses (including failures), and freedom to make local edits or full rewrites. |
| **Skill Text Investment** | Runs long evolution loops with mediocre skill descriptions, expecting iteration count to compensate. | Invests some effort in skill text quality but doesn't run dedicated short cycles to debug the instructions before the main evolution run. | Runs 3-5 short diagnostic cycles specifically to refine the skill/instruction text BEFORE the main evolution loop — recognizing that skill text quality determines the ceiling. |
| **Code-Space Representation** | Evolves free-form prompt text where the proposer can generate arbitrary, unstructured content. | Uses some structured format but doesn't fully leverage executable code representation for regularization. | Represents all evolved artifacts as executable code or structured workflows, exploiting coding models' natural regularization bias toward generalizable solutions. |
| **Bitter Lesson Alignment** | Treats hand-engineered workflows as sacred and resists evolution on the grounds of time invested. | Acknowledges evolution potential but only applies it to low-value or peripheral components. | Every manually-tuned component is a candidate for evolution — the question is "when," not "whether." Hand-crafted effort is respected as a warm-start, not a ceiling. |
