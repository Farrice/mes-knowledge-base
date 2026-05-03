# Patrick Debois — Context Development Life Cycle (CDLC) Genius Context

**Source**: AI Engineering Summit keynote, "Context is the new code" (~25 min, 4,276 words)
**Expert pedigree**: Founder of DevOps (coined the term, organized first DevOpsDays Ghent 2009). Currently founder/CTO at Tessl. The single person uniquely positioned to extend the DevOps mental model into AI-augmented engineering.

---

## Core Genius

Patrick treats **AI context as code with a full development lifecycle**. The same way he asked in 2009 *"what if ops looked more like dev?"* (birthing DevOps), he now asks *"what if context is the code?"* — and answers it with the **CDLC** (Context Development Life Cycle): **Generate → Test → Distribute → Observe → Adapt**.

Everyone else talks prompt engineering as a craft. Patrick treats it as **systems engineering with testing, packaging, registries, security, and observability** — and predicts the maturity arc the entire field will travel from 2025-2028 because he already lived it 2009-2015 with DevOps.

---

## The CDLC — 5 Stages

```
            ┌─────────────────────────────────┐
            │                                 │
        ▼   │                                 │   ▲
    GENERATE → TEST → DISTRIBUTE → OBSERVE → ADAPT
        ▲                                     │   ▼
            │                                 │
            └─────────────────────────────────┘
```

### Generate
Context creation: prompts, agent.md/CLAUDE.md, skills, fetched library docs, MCP-pulled context (GitLab/GitHub/Slack), spec-driven prompts → planning mode → step-by-step prompts. Voice-coding > typing because it produces more elaborate (= better) context.

### Test
Maturity ladder: **Lint** (syntactic — does it parse? does it match the spec format?) → **Grammarly** (semantic — does the LLM understand what's written?) → **LLM-as-judge unit tests** (criterion-based — does generated output meet rules?) → **E2E with tools** (sandboxed execution — does the full agent loop succeed?). Each tier catches what the previous can't.

### Distribute
Maturity ladder: **Copy-paste** (Slack tier) → **Checked-into-repo** (library tier) → **Versioned package in registry** (npm/pip equivalent) → **Marketplace** (platform tier). Each tier requires different tooling: copy → discoverability index → version manager + dependency resolver → security scanner + SBOM.

### Observe
Agent log feedback ("agent said it was missing X" → recurring → become context). PR review feedback IS context feedback. Production runtime failures → automatic test case generation. Sandbox monitoring (sandbox catches what agent *does*, NOT what agent *reads* — context filter is required, separate, WAF-style).

### Adapt
Improvements push back into Generate. Loop closes. The unit of progress is a completed loop, not a shipped artifact.

---

## 8 Genius Patterns

### 1. The Parallel-First Move
Before proposing anything new, find the established discipline it parallels. *"What if ops looked more like dev?"* → DevOps. *"What if context is the code?"* → CDLC. Never invents from scratch — ports.

**Executable**: For new domain → name the established analog → carry vocabulary, lifecycle, tooling categories, maturity arc across.

### 2. The Lifecycle Loop Reflex
Every system gets wrapped in an infinity loop with named phases. The loop is the unit of thinking, not the artifact.

**Executable**: For any new system, force it into a 4-5 stage continuous loop. Name each phase. Each phase gets tooling and a maturity ladder.

### 3. Lint → Grammarly → Eval Ladder
Tests have tiers. Lint (syntactic) → Grammarly-style (semantic completeness) → LLM-as-judge (criterion-based) → end-to-end with tools (full agent loop).

**Executable**: When evaluating any context artifact, name the test tier. Most teams stop at lint. Mature teams cover all four. The bigger the blast radius, the higher the test tier required.

### 4. Error Budgets for Non-Deterministic Tests
LLM evals are non-deterministic; binary pass/fail is wrong. Port SRE error budgets directly: run N times (≥5), measure success rate, set per-test budgets calibrated by criticality.

**Executable**: Critical tests get tight budgets (≥95%), tolerant tests get loose budgets (≥60%). Failures within budget don't block; failures exceeding budget do.

### 5. Consistency-as-Eval
Run downstream generation N times in parallel; if outputs vary, the input source was poor; if outputs converge, the source is well-formed. **Variance is a quality signal for the upstream source, not just for the test.**

**Executable**: To grade any prompt/brief/definition, generate downstream output 3-5× in parallel. Measure semantic convergence. High variance = upstream rewrite needed; low variance = downstream can proceed.

### 6. Library → Registry → Marketplace Maturity Arc
Port the entire package management evolution onto context. Local files → versioned libraries → registries → marketplaces. **Predict each stage's problems before they hit** (e.g., "with context we're going to have dependency hell").

**Executable**: For any context artifact you want to share, name the distribution tier and its tooling requirement.

### 7. The Honest Skill-Quality Verdict
*"99.9% of the skills [in registries] is crap... hardly any of them, if you run kind of any set of evals on there, is actually up to a quality standard."*

**Executable**: When auditing a skill collection, baseline classification is REVIEW-or-worse. Require eval evidence to elevate. Default-A distributions are inflation theatre.

### 8. The Sandbox-Doesn't-Solve-Loading Insight
*"Your code agent by default without any restrictions loads your agent.md, you load your skill.md. So if you download this, immediately it's loaded. So you can't filter that with sandboxes. You need to have another way."*

**Executable**: Treat context loading as a separate security boundary from execution. Sandboxes catch what the agent *does*; context filters catch what the agent *reads*. Both required. Context filter = WAF for prompts.

---

## 5 Hidden Knowledge Insights

### The Voice-Coding Insight
*"That's why I like to voice code. For some reason, I'm way more elaborate voice coding than typing."*

**Implication**: Prompt quality correlates with linguistic elaboration, not effort. The medium of capture shapes artifact quality. Dictation > typing for skill/directive authoring.

### PR Feedback IS Context Feedback
*"Any feedback you get on a PR that's not complete, that's feedback on your context because that PR was created with certain pieces of context. If you say this is not correct, you can kind of keep arguing on the PR, or you can just say, 'Let's improve the context.'"*

**Implication**: Default reflex is to argue the PR. Masterful reflex is to upgrade upstream context so the next PR auto-corrects. Every PR comment is a pointer to a context gap.

### The Time Conservation Law
*"You thought you were going to save time by writing actually your context instead of all your code, but if you take this rigorously, you're going to spend time on writing the right evals."*

**Implication**: Time isn't saved — it's transferred from code-writing to eval-writing. The mature practitioner spends MORE total time on evals than on prompts. If you're spending less, you're cutting corners.

### Production-Failure → Test-Case Loop
*"This is a tool that actually instruments your code, pushes it out... When it fails, it says, 'These pieces of code were changed and were failing... Can we create a test case for this?'"*

**Implication**: The eval suite is not authored once and frozen — it grows from production failures. Every prod incident = mandatory eval addition. Static eval suites rot.

### Skills Will Self-Host
*"There's also a tendency that a lot of the skills and pieces, people actually want to put that in their own registry."*

**Implication**: He's predicting organizations will fork public skills into private registries with their evals + security scans + versioning. Public marketplaces become inspiration; private registries become production. Antigravity is already this.

---

## Hall of Fame Exemplars

### Exemplar 1: The DevOps → CDLC Parallel
*"In 2009... it was kind of me saying like what if ops looked more like dev? And then we got like, hey, collaboration, kind of our deployment, all that stuff. So... last year I started thinking, what if context is the code?"*

**What makes this excellent**: He invokes the parallel BEFORE proposing the new framework. Standard "thought leader" move would dramatically *unveil* CDLC; Patrick *grounds* it in established analog first. The audience now has scaffolding for everything that follows.

### Exemplar 2: The Awesome-Prefix Eval (Unfakeability)
*"Imagine you put in your agent.md... every API endpoint must use the prefix awesome... add me a new endpoint to save a user. And you expect actually your coding agent to just say the code that's being generated has /awesome/user... we can test this by asking then an LLM does it actually start with /awesome?... imagine you would ask the same question without your context above. No LLM is ever going to prefix your URL with awesome."*

**What makes this excellent**: The convention is so absurd ("awesome") that it's *unfakeable* — no model would default to it, so passing the test PROVES context loaded. Anti-pattern: testing for things models do anyway (greeting users politely) — passes whether your context worked or not. **The test must be impossible to pass without the context.**

### Anti-Exemplar: Run-It-Once Eval
**What mediocre looks like**: Most teams add LLM-as-judge, run it once, ship. When it fails in CI, they retry until it passes ("flaky test, retry") or disable the test ("LLM evals are unreliable").

**Why it fails**: Violates the error-budget principle. Non-deterministic evals require N-runs + budget thresholds. Single-run evals are theatre. Disabling them is worse — abandons the test rather than calibrating it.

---

## 5 Signature Moves

| # | Move | Trigger |
|---|------|---------|
| 1 | **Force the Parallel First** — Before proposing any new framework, name the established discipline it parallels. Carry vocabulary, lifecycle, tooling categories. | Introducing infrastructure for an emerging domain. |
| 2 | **Demand the Test Tier** — When someone shows you a prompt or skill, immediately ask: "What's your eval tier — lint, Grammarly, unit, or e2e?" If they don't have one, that's the actual finding. | Auditing any context artifact. |
| 3 | **Run-It-Five-Times Reflex** — Never accept the result of a single LLM-eval run. Always run N (≥5), report success rate against an explicit error budget. | Any LLM-as-judge evaluation. |
| 4 | **Convert PR Argument to Context Upgrade** — When tempted to argue a PR comment, instead ask: "what context, if loaded next time, would have prevented this PR comment?" Then write that context. | PR review friction with AI-generated code. |
| 5 | **Default to "Crap Until Proven Otherwise"** — When evaluating skills/prompts/contexts you didn't author, baseline assumption is failure. Require eval evidence to elevate. | Auditing third-party or your own legacy context library. |

---

## Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
|-----------|---------------------|----------------|-------------------|
| **Test tier coverage** | Lint only (syntax check) | Lint + LLM-as-judge unit tests | Full ladder: lint + Grammarly + unit + e2e with sandboxed tools |
| **Determinism handling** | Single-run pass/fail | N-runs reported with success rate | Per-test error budgets calibrated by criticality |
| **Test design unfakeability** | Tests things models do anyway | Tests company-specific conventions | Tests so domain-specific that passing PROVES context loaded |
| **Distribution maturity** | Copy-paste over Slack | Checked into repo | Versioned package in registry with deps, security scan, SBOM |
| **Observability loop** | Manual reading of agent logs | Standardized log format consumed by tooling | Production failures auto-generate test cases |
| **Context filter** | None (sandbox only) | Pattern-based filter at load time | WAF-style filter with prompt-injection rules |
| **Error budget discipline** | "Flaky test, retry" | Tracked but not enforced | Budgets enforced, failures > budget block deploy |

---

## Anti-Patterns to Reject

- **Single-run eval theatre**: Treating LLM-as-judge results as deterministic. Always N-run with budgets.
- **Lint-only confidence**: A skill that passes lint but has no semantic or behavioral tests is uncalibrated.
- **Default-A skill classification**: If 90%+ of skills classify as A-tier, you're inflating, not auditing.
- **Sandbox-as-only-defense**: Sandboxes don't filter what's loaded. Context filter is a separate, required boundary.
- **Static eval suites**: Eval suites that don't grow from production failures rot as the system evolves.
- **Generate-only thinking**: Spending all attention on prompt authoring while Test/Distribute/Observe stages are unstaffed.
- **Argue-the-PR reflex**: Every PR comment that could be solved by better context but instead becomes a turf war with the agent.

---

## Domain Boundaries

**Patrick's CDLC frame applies to**: AI-augmented engineering systems, skill/agent/directive collections, prompt libraries, multi-agent orchestrations, any system where artifacts are authored, deployed, and improved over time.

**It does NOT apply to**: One-shot prompts, throwaway scripts, single-author personal toolkits where no distribution or observability surface exists.

**Direct relevance to Antigravity**: The system operates at registry-tier complexity (210 skills, 117 agents, 58 directives) but at copy-paste-tier hygiene. The 2026-04-24 system audit identified this gap empirically. CDLC provides the lifecycle vocabulary to organize what's already being built (`eval_harness.py`, `routing_enforcer.py`, `skill_auditor.py`, `evolution_orchestrator.py`).
