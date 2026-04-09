# Nate B. Jones (Orchestration Intelligence) — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

The "Jagged Frontier" of AI capabilities is not inherent to the intelligence — it's an artifact of single-turn, unstructured interaction. Apply organizational structure (roles, handoffs, verification loops) and the frontier smooths. The convergent architecture independently built by Anthropic, Google DeepMind, OpenAI, and Cursor — Decompose, Parallelize, Verify, Iterate (DPVI) — is THE pattern for long-horizon agentic work. Harness design determines success more than model intelligence.

---

## Genius Patterns (Compressed)

### GP1: The Smoothing Thesis (Jagged to Smooth Frontier)
The "Jagged Frontier" is an artifact of unstructured interaction, not inherent AI limitation. When you ask a capable analyst to solve everything in one turn with no notes or retries, variance shows up as jaggedness. Apply organizational structure and the frontier smooths. When an agent fails, diagnose the harness before blaming the model — >80% of failures trace to missing structure.

### GP2: The DPVI Pattern (Decompose-Parallelize-Verify-Iterate)
Convergent architecture independently built by Anthropic, Google DeepMind, OpenAI, and Cursor. (1) Decompose work into subtasks small enough for single-context execution, (2) Parallelize across isolated workers with no cross-worker communication, (3) Verify outputs against acceptance criteria, (4) Iterate carrying accumulated artifacts, not conversation history. Independent convergence by 4 labs = proof of correctness.

### GP3: The Planner-Worker-Judge Hierarchy
Cursor's breakthrough after flat coordination failed: Planners explore problem space and create tasks (never execute), Workers pick up individual tasks and grind until done (zero coordination with other workers), Judges determine whether to continue, iterate, or accept. Judge's restart with fresh context circumvents context window limits entirely. Maps directly to PM plans, engineer executes, QA verifies.

### GP4: Harness Design as the Critical Variable
The harness — memory, task files, progress tracking, restart procedures, specification documents — determines success more than model intelligence. Audit checklist: persistent memory, clear specification, progress tracking, restart procedures, isolation. If <3 of 5 are present, fix the harness before evaluating model capability.

### GP5: Domain Verifiability Tiers
Tier 1 (Machine-checkable): code compiles, tests pass — fully delegable. Tier 2 (Expert-checkable): strategies, briefs, campaigns — 3-4 experienced practitioners reach near-consensus on quality — delegable with sniff-check. Tier 3 (Genuinely unverifiable): novel creative with no consensus criteria — retain for humans, usually <10%. Contrarian insight: "soft work" is far more verifiable than the industry assumes.

### GP6: The Sniff-Check Meta-Skill
As execution becomes cheap, evaluation appreciates in value. Declining: "I can do the work." Appreciating: "I can tell if the work is correct." For every domain, define what a correct sniff-check looks like with explicit criteria. People who develop fast, accurate sniff-checking are positioned for the agent era.

### GP7: Complexity Reduction > Complexity Addition
Cursor's most important improvements came from REMOVING coordination machinery. Simpler systems outperform complex ones when underlying agents are capable. Decision rule: when a multi-agent system underperforms, first try removing a layer. Add complexity only after proving simplification doesn't work.

### GP8: Organizational Intelligence Transfer
Human teams scaled cognition through sprint cycles, peer review loops, draft-revise-publish pipelines. These patterns generalize to agents with zero modification. Design rule: start every agent architecture from a proven human organizational pattern, map 1:1, then optimize.

### GP9: The Convergence Proof
When four independent organizations build the same structure without coordination, the underlying design is a near-certainty. Independent invention is stronger evidence than any benchmark. Look for convergence when choosing architectures — if multiple independent actors arrive at the same design, adopt it.

### GP10: The Team-of-One Multiplier
An individual with multi-agent orchestration capability is functionally a hundred-person team. The operator becomes a PM managing agent teams — defining roles, decomposing work, building verification criteria, iterating cycles. Solo leverage scales from 1x to 10-100x without hiring.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | The Invisible Learning Curve — harness fluency curve (our ability to structure agent work) is now more important than model intelligence for practical outcomes | Invest in harness design skills, not just model selection |
| HK2 | The Flat Structure Pathology — flat agent coordination produces risk-averse agents that optimize for small/safe changes; high activity, low progress | Never use flat coordination; always implement hierarchy |
| HK3 | The Judge Reset as Infinite Horizon Hack — judge's restart capability circumvents context window limits by beginning each iteration with clean memory plus accumulated artifacts | Use judge resets for indefinite-horizon work without cognitive degradation |
| HK4 | Prompting Survives the Agent Era — in mature systems, behavior is disproportionately determined by prompt design; this is systems engineering, not conversation | Treat prompt engineering as systems engineering that grows MORE critical with autonomy |
| HK5 | The "Soft Work" Verifiability Surprise — bring a product strategy to 3-4 experienced leaders with 15+ years and their assessments will be "remarkably consistent" | Expand the domain of agent-delegable work; expert consensus IS a verification standard |
| HK6 | The Single Surviving Capability — the question shifts from "Can AI do this?" to "Can this work be decomposed into verifiable subproblems?" and the answer is yes for far more work than people admit | Map all work through the verifiability lens before deciding what to delegate |
| HK7 | The Uncomfortable Migration — becoming a sniff-checker, tastemaker, and agent infrastructure builder is not optional; it's the survival response | Map your domain for delegation proactively |

---

## Research Enrichment (March 2026)

- **Cursor scale tests**: Browser from scratch (Rust, 1M+ lines, 1 week), Solid-to-React migration (3+ weeks), Java language server, Windows 7 emulator (1.2M lines), Excel clone (1.6M lines)
- **Math breakthrough**: Coding harness solved Problem 6 of Stanford/MIT/Berkeley spectral graph theory proof with STRONGER bounds than human solution. 4 days, zero hints.
- **Model insight**: GPT-5.2 consistently outperforms Claude Opus for long-horizon autonomous tasks (Opus tends to stop early and take shortcuts)
- **Anthropic**: Initializer + Coding agent pattern; without structure, specific failures: one-shot attempt, context exhaustion, leaving codebase worse
- **Harness best practices**: Git + worktrees for isolation, detailed specs/style guides, cycle-based resets with CI as safety net, human oversight boosts productivity 2-3x

---

## Signature Moves

1. **The Atomic Decomposer** — Ruthlessly breaks down any problem into smallest independently verifiable sub-components before any execution. Deploy when facing any task too large for single-turn execution.
2. **The Harness Auditor** — Scrutinizes environment for persistent memory, clear specs, progress tracking, restart procedures, and isolation BEFORE evaluating agent output. Deploy when any agent system underperforms.
3. **The Verifiability Mapper** — Classifies every task into Machine-checkable (Tier 1), Expert-checkable (Tier 2), or Genuinely Unverifiable (Tier 3) with explicit acceptance criteria. Deploy when delegating new task types to agents.
4. **The Complexity Stripper** — When multi-agent systems underperform, first instinct is to REMOVE a layer rather than add complexity. Deploy when systems exhibit unexpected behavior or suboptimal performance.
5. **The Sniff-Check Architect** — Articulates the "tells" and criteria an expert would use for rapid evaluation, turning tacit knowledge into actionable guidelines. Deploy when establishing quality gates for agent output.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Task Decomposition | Subtasks still too large, requiring multiple turns within single context | Generally manageable but occasionally need minor internal decomposition | Each subtask is atomic, requiring single focused execution with clearly defined inputs/outputs |
| Harness Completeness | Missing 2-3 critical components leading to frequent failures | Most components present but could be more robust | All 5 components (memory, spec, tracking, restart, isolation) explicitly defined and actively utilized |
| Verification Protocol | Relies on subjective judgment or vague "make it good" instructions | Criteria mostly clear with some edge cases requiring interpretation | Machine-checkable or expert-consensus-driven acceptance criteria enabling objective, rapid evaluation |
| Architecture Alignment | Flat coordination model leading to risk aversion or context exhaustion | Some hierarchical elements but lacking full DPVI or Planner-Worker-Judge separation | Fully implements Planner-Worker-Judge / DPVI with clear roles, isolated execution, iterative refinement |
| Complexity Efficiency | Over-engineered with unnecessary coordination layers | Generally efficient with a few redundant components | Ruthlessly simplified, maximum performance with minimal overhead |
