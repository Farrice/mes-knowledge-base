# MetaHarness → Self-Evolving Antigravity System

> **Source**: Matthew Berman video → [MetaHarness paper](https://arxiv.org/html/2603.28052v1) (Yoonho Lee et al., Stanford/MIT/Crafted) + [Karpathy autoresearch](https://github.com/karpathy/autoresearch)

## The Concept (What We're Building)

MetaHarness proves that **the harness around an LLM matters as much as the model itself** (6x performance gap on identical benchmarks), and that harness engineering can be **fully automated** by a coding agent proposer that:

1. **Proposes** new harness variants (code changes to prompts, retrieval, memory, orchestration)
2. **Evaluates** them against a search set
3. **Logs** code, scores, and execution traces to a file system
4. **Iterates** — inspecting prior artifacts via grep/cat to diagnose failures and propose fixes

Key result: MetaHarness-discovered harnesses **surpass all hand-engineered baselines** on TerminalBench-2, text classification, and IMO math — using 10x fewer evaluations and far fewer tokens.

**For Antigravity**: We already have the primitives (self-annealing, harness audits, quality gates). What we're missing is **the outer loop** — the automated propose → evaluate → log → iterate cycle that makes the system **permanently self-improving**, not just self-recovering.

---

## Swarm Assessment: What MetaHarness Means for Antigravity

| MetaHarness Concept | Antigravity Equivalent (exists) | Gap / What to Build |
|---|---|---|
| Proposer (coding agent) | Nick Saraev self-annealing | Self-annealing only *recovers*. Proposer actively *improves*. Build evolution loop. |
| Execution traces (stored) | Quality gate finalize logs | Logs exist but aren't structured for re-inspection. Need JSON trace format. |
| Pareto frontier tracking | None | Build accuracy × token cost frontier tracking for workflows. |
| File-system artifact store | `.agent/session-state.md` | Session state is ephemeral. Need persistent evolution store. |
| Harness = single-file program | Workflow `.md` files | Workflows are the harness. They can be versioned and evolved. |
| Search set (hard examples) | Quality gate failures | Mine past failures as the search set for evolution. |
| Skill text (steers proposer) | `SKILL.md` + Chain directives | Already strong. Can be refined per MetaHarness tips. |

---

## Proposed Changes

### Component 1: Self-Evolving Systems Skill

#### [NEW] [SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/self-evolving-systems/SKILL.md)
Full MES 3.0 skill extraction covering:
- MetaHarness methodology (proposer → evaluate → log → iterate)
- Karpathy autoresearch pattern (overnight experiment loops)
- AlphaEvolve principles (search with selective access to diagnostic history)
- The Bitter Lesson applied to harness engineering

#### [NEW] [genius.md](file:///Users/farricecain/Google%20Antigravity/skills/self-evolving-systems/genius.md)
Genius patterns and hidden knowledge:
- **The Harness Matters More** — 6x performance gap from harness alone
- **Let the Model Choose** — adaptive retrieval > monolithic prompt packing
- **Code-Space Regularity** — coding models propose coherent algorithms, not brittle heuristics
- **Trace-Based Diagnosis** — raw traces > scalar rewards for improvement signal
- **Emergent Strategy** — proposer naturally starts from strong priors without being told to
- **Inspectable Overfitting** — code-space overfitting is visible (brittle if-chains), weight-space isn't

### Component 2: ~8 Workflow Commands

#### [NEW] [self-evolve.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/self-evolve.md)
**The master command.** Runs a MetaHarness-style evolution loop on any Antigravity component:
1. Select target (workflow, skill prompt, directive)
2. Define evaluation criteria and search set
3. Create baseline version
4. Run N iterations of propose → evaluate → log
5. Report Pareto frontier and best-performing variant

#### [NEW] [harness-evolve.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/harness-evolve.md)
Evolve a specific agentic harness (workflow file) through automated iteration. More focused than `/self-evolve` — targets a single workflow's prompts, flow, and gates.

#### [NEW] [auto-experiment.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/auto-experiment.md)
Karpathy-style experiment runner: define a hypothesis, let the system run iterations overnight, commit only improvements. Uses git-branch isolation per experiment.

#### [NEW] [evolution-audit.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/evolution-audit.md)
Inspect the evolution history for any component — view Pareto frontier, detect regressions, identify confounded edits, trace causal chains through iteration history.

#### [NEW] [skill-anneal.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/skill-anneal.md)
Apply self-annealing specifically to a skill's prompts and workflows — run against past quality gate failures to find and fix weak spots.

#### [NEW] [proposer-sprint.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/proposer-sprint.md)
Time-boxed, fixed-iteration improvement sprint. User defines: target, iterations (5-20), evaluation metric. System proposes variants, evaluates, and reports winner.

#### [NEW] [evolution-status.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/evolution-status.md)
Dashboard command: list all active/completed evolution loops, their iteration counts, current best scores, and improvement trajectories.

#### [NEW] [bitter-lesson-check.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/bitter-lesson-check.md)
Audit any hand-coded heuristic, prompt engineering trick, or manual pattern for evolution replacement potential. Scores: how much of this is hand-coded vs. learnable?

### Component 3: Extraction Report

#### [NEW] [extraction_report.md](file:///Users/farricecain/Google%20Antigravity/extractions/matthew-berman/extraction_report.md)
Full extraction document containing:
- Source summary (Berman video + MetaHarness paper + autoresearch)
- Key frameworks extracted
- Genius patterns and hidden knowledge
- Mapping to Antigravity integration points
- Research references (arXiv, GitHub repos)

### Component 4: Directive Updates

#### [MODIFY] [deep_self_annealing.md](file:///Users/farricecain/Google%20Antigravity/directives/deep_self_annealing.md)
Add a **Tier 4: Self-Evolution** layer above the current 3 tiers:
- Tier 1 (Auto-Fix) → Tier 2 (Diagnose) → Tier 3 (Escalate) → **Tier 4 (Evolve)**
- Tier 4 fires when the same *class* of error recurs 3+ times — triggers a `/proposer-sprint` on the failing component

---

## What NOT to Build (Scope Boundaries)

- **Not building actual MetaHarness infrastructure** (Python eval loops, CLI tools) — that's premature. We're extracting the *methodology* and creating *workflow commands* that a human + Antigravity can execute.
- **Not modifying the Chain** — the Chain is already the harness. These workflows improve the harness *around* the Chain.
- **Not automating overnight runs** — requires compute infrastructure we don't have. The workflows are designed for human-supervised iteration sprints.

---

## Verification Plan

### Manual Verification
1. **Slash command registration**: After creating all workflow files, run `/workflows` and confirm all 8 new commands appear in the list
2. **Skill file structure**: Verify `skills/self-evolving-systems/` contains `SKILL.md` and `genius.md` matching MES 3.0 format
3. **Dry-run `/self-evolve`**: Invoke the workflow on a simple target (e.g., the `/hook-forge` workflow) and verify it produces a coherent evolution plan without errors
4. **Cross-reference check**: Confirm `deep_self_annealing.md` Tier 4 references the new workflows correctly

> [!NOTE]
> Since this is a methodology extraction (not code), verification is structural — do the files exist, are they well-formed, do they cross-reference correctly, and does the workflow produce coherent output when invoked?
