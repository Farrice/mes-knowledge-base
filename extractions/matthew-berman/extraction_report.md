# Extraction Report: Self-Evolving AI Systems

> **Source**: Matthew Berman — "All Software Will Be Self-Evolving Software Very Soon" (2026)
> **Paper**: MetaHarness: End-to-End Optimization of Model Harnesses (arXiv:2603.28052v1)
> **Authors**: Yoonho Lee et al. (Stanford, MIT, Crafted/KRAFTON AI)
> **Supporting**: Andrej Karpathy — autoresearch (github.com/karpathy/autoresearch)
> **Extracted**: 2026-03-31

---

## Core Thesis

The performance of LLM systems depends not only on model weights but equally on their **harness** — the code that determines what information to store, retrieve, and present to the model. Changing the harness around a fixed LLM can produce a **6x performance gap** on the same benchmark. MetaHarness automates harness engineering via an outer loop that uses a coding agent to propose, evaluate, and iterate on harness code.

---

## Framework 1: MetaHarness — The Self-Evolving Outer Loop

### Architecture
```
┌─────────────────────────────────────────────┐
│             META-HARNESS (Outer Loop)        │
│                                              │
│  ┌──────────┐   ┌──────────┐   ┌─────────┐ │
│  │ PROPOSER  │──▶│ EVALUATE │──▶│  LOG    │ │
│  │ (Coding   │   │ (Search  │   │ (Code + │ │
│  │  Agent)   │◀──│  Set)    │   │ Traces) │ │
│  └──────────┘   └──────────┘   └─────────┘ │
│       │                             │        │
│       └─────── ITERATE ◀───────────┘        │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │         FILE SYSTEM STORE            │   │
│  │  /harness_001/ code.py, scores.json  │   │
│  │  /harness_002/ code.py, traces.json  │   │
│  │  /harness_N/   ...                   │   │
│  └──────────────────────────────────────┘   │
│                                              │
├──────────────────────────────────────────────┤
│             TASK HARNESS (Inner)             │
│  Prompts → Model → Response → State Update  │
└──────────────────────────────────────────────┘
```

### The Proposer
- A **coding agent** (Claude Code + Opus 4.6 in the paper), not a raw LLM
- Has file system access — navigates prior artifacts via `grep`, `cat`, standard dev tools
- Decides autonomously: which prior harnesses to inspect, which failure modes to address, local edit vs. full rewrite
- Never sees test-set results — only search-set feedback and execution traces
- Typical run: ~60 harnesses evaluated over ~20 iterations

### Storage Model
Each evaluated harness gets a directory containing:
- Source code (single-file Python program)
- Scores (JSON)
- Execution traces (prompts, tool calls, model outputs, state updates)

The proposer queries this growing file system rather than ingesting it as a single prompt. This is critical — the accumulated experience often exceeds 10M tokens, far beyond any context window.

### Evaluation
- Joint optimization over **accuracy** and **context cost** (tokens used)
- Pareto frontier tracking — no single best, but a curve of trade-offs
- No parent-selection rule — proposer can inspect any prior harness, including low-performing ones (avoids local maxima)
- Search set kept deliberately small (50-100 examples) for fast iteration

---

## Framework 2: Karpathy's autoresearch

### Architecture
- 630-line Python tool
- AI agent modifies training code → runs 5-minute training runs → commits only if metrics improve
- Git branch isolation per experiment
- Results: 11% speedup discovered over 700 experiments, 20 optimizations found
- Shopify CEO ran it overnight: 19% performance improvement after 37 experiments

### Key Difference from MetaHarness
autoresearch evolves **model training code**. MetaHarness evolves **the harness around the model**. Both use the same pattern: propose → evaluate → log → iterate.

---

## Genius Patterns Extracted

### 1. The Harness Matters More
> Changing the harness around a fixed LLM produces a 6x performance gap. The model is the engine; the harness is the car.

**Application**: Stop upgrading models when performance is bad. Evolve the harness first.

### 2. Let the Model Choose (Adaptive Retrieval)
> Useful context should be accessed adaptively rather than monolithically packed into a single prompt. Let the model decide what it needs.

**Application**: Don't pre-pack prompts. Give the agent access to artifacts and let it select what's relevant.

### 3. Code-Space Regularity
> Coding models propose coherent algorithms rather than brittle, hard-coded solutions. Code space has a natural regularization bias.

**Application**: When evolving workflows, represent them as executable programs — the proposer will naturally avoid overfitting.

### 4. Trace-Based Diagnosis > Scalar Rewards
> The proposer isn't limited to scalar rewards or fixed summaries; it can inspect raw code, execution traces, and prior failures, then use that information to form and test hypotheses.

**Application**: Log everything. JSON traces > summary scores. The richness of diagnostic data determines evolution quality.

### 5. Emergent Strategy
> The proposer often starts from a strong prior harness, but this is an emergent strategy rather than a hard-coded rule.

**Application**: Don't constrain the evolution search. Give it access to all prior attempts and let it choose its starting point.

### 6. Inspectable Overfitting
> Overfitting in code space is inspectable: brittle if-chains or hard-coded class mappings are visible. Weight-space overfitting is not.

**Application**: When an evolved workflow seems too specialized, you can literally read the code and see the problem.

### 7. The Skill Text Is Your Strongest Lever
> Iterating on the skill text had a larger effect on search quality than changing iteration count or population size.

**Application**: The equivalent of SKILL.md is the most important artifact. Invest heavily in its quality. Run 3-5 short evolution cycles specifically to debug the skill before committing to a full run.

### 8. The Bitter Lesson Applied to Harnesses
> Hand-engineered heuristics never beat end-to-end learned systems. AI figuring out what to do always beats humans telling it what to do.

**Application**: Any manually-tuned prompt, workflow, or decision tree in Antigravity is a candidate for evolution replacement. The question isn't *if* — it's *when*.

---

## Key Results (Paper)

| Benchmark | MetaHarness | Best Baseline | Improvement |
|---|---|---|---|
| Text Classification (avg) | 48.0 | 40.9 (ACE) | +7.1 points |
| Text Classification (median vs best) | 50.0 median | 45.6 best | Median > their best |
| Math Reasoning (IMO) | +4.7pt avg | — | Across 5 held-out models |
| TerminalBench-2 (Opus 4.6) | 76.4 | 74.3 (Forge Code) | +2.1 points |
| TerminalBench-2 (Haiku 4.5) | 37.6 | 35.5 (Goose) | +2.1 points |
| Token Usage (text class.) | 11.4 | 28.5-50.8 | 2.5-4.5x cheaper |
| OOD Generalization (9 datasets) | 73.1 | 70.2 (ACE) | +2.9 points |

---

## Practical Implementation Tips (from Paper Appendix D)

1. **Write a good skill** — constrain outputs and safety, not diagnosis procedure. Run 3-5 short cycles to debug the skill first.
2. **Start with a hard search set** — baseline should NOT saturate the eval. Filter for examples it gets wrong.
3. **Log everything queryably** — JSON, hierarchical directories, consistent naming. Machine-readable formats.
4. **Build a small CLI** — list Pareto frontier, show top-k, diff between harness versions. Saves proposer tokens.
5. **Lightweight validation first** — import, instantiate, call on tiny examples before expensive benchmarks.
6. **Automate evaluation outside the proposer** — proposer diagnoses and proposes; a separate system evaluates.

---

## References

- Paper: https://arxiv.org/html/2603.28052v1
- autoresearch: https://github.com/karpathy/autoresearch
- AlphaEvolve: Google DeepMind (matrix multiplication breakthrough)
- TerminalBench-2: Terminal-based LLM evaluation benchmark
- The Bitter Lesson: Rich Sutton (2019) — applied to harness engineering
