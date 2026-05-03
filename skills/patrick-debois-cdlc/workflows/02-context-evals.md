---
description: Author a complete eval suite for any context artifact using Patrick's lint→Grammarly→unit→e2e ladder
---

# Workflow 2 — Context Eval Authoring

Produce a complete eval suite for one target context artifact (skill, agent.md, directive, prompt). Cover Patrick's 4-tier ladder — **Lint → Grammarly → LLM-as-judge unit tests → E2E with tools** — with N-run success rates and calibrated error budgets.

## Pre-Flight Gate

Run this workflow when:
- The target artifact is *load-bearing* (used in production, by multiple workflows, or as a dependency)
- The artifact has NO existing tests, or only lint-tier
- You have access to run the artifact (or simulate it) to capture baseline behavior

**Skip if**: Artifact is a one-shot prompt or experimental scratch. Eval cost > artifact value.

## Skill Acquisition

Load `skills/patrick-debois-cdlc/genius.md`. Anchor to:
- **Pattern 3** (Lint → Grammarly → Eval ladder) — the spine of this workflow
- **Pattern 4** (Error budgets for non-determinism) — every test gets a budget
- **Exemplar 2** (Awesome-prefix unfakeability) — every unit test must satisfy this rule
- **Signature Move 3** (Run-it-five-times reflex) — never single-run
- **Anti-Exemplar** (Run-it-once eval theatre) — what to actively reject

## Input Required

- **Target artifact**: File path + name (e.g., `skills/lara-acosta-linkedin/SKILL.md`)
- **Production usage**: How is this artifact used? (which workflows load it, what outputs depend on it)
- **Quality criteria**: What does "this artifact is working" mean to the user? (free-form, will be operationalized into tests)
- **Available tools** for e2e: Can you sandbox-execute? Can you call the artifact's downstream output for real?

## Execution

### Step 1: Quality Criteria → Test-Tier Mapping

Take user's free-form quality criteria and assign each to its proper tier:

| Criterion type | Tier | Why |
|---|---|---|
| "It must parse / have valid frontmatter / use the right schema" | **Lint** | Syntactic. Deterministic. Fast. |
| "It must be clear / complete / not missing sections" | **Grammarly** | Semantic. LLM understands the artifact itself, not its output. |
| "Output must satisfy rule X / contain element Y / avoid pattern Z" | **Unit (LLM-as-judge)** | Behavioral. Judges the *generated output* against criteria. |
| "Full agent loop must succeed against real input" | **E2E** | End-to-end. Sandbox-executes the full chain. |

A criterion may map to multiple tiers (e.g., "outputs must be in markdown AND must include a CTA" splits into Lint + Unit).

### Step 2: Lint Tier — Author Schema Validators

For each Lint criterion, write a deterministic validator:
- **Tool**: Python regex/JSON-schema/yamllint or a language-native equivalent
- **Output**: Pass / Fail (no probabilistic component)
- **Cost**: Cents of compute, sub-second runtime
- **Storage**: `evolution_store/eval_suites/[artifact-name]/lint.json` (or `.py` if logic is non-trivial)

### Step 3: Grammarly Tier — Author Semantic Completeness Checks

For each Grammarly criterion, write an LLM-as-judge prompt that evaluates the artifact ITSELF (not its output):
- **Prompt template**: "Given this skill file, rate 1-5 whether it [criterion]. Cite specific sections supporting your rating."
- **Run cadence**: 3 runs (Grammarly is less sensitive than Unit; smaller N acceptable)
- **Pass threshold**: Mean rating ≥4 across 3 runs
- **Storage**: `evolution_store/eval_suites/[artifact-name]/grammarly.md` (the criteria + their prompts)

### Step 4: Unit Tier — Author LLM-as-Judge Tests (THE CORE)

This is where Patrick's unfakeability rule applies. **Every test must satisfy: passing PROVES the artifact loaded.**

For each Unit criterion:

**4a. Design the test input**:
- Choose an input that, without the artifact loaded, would NOT produce the criterion-satisfying output
- Patrick's awesome-prefix example: "every endpoint must use /awesome/" — no model defaults to that. Test = ask model to add a new endpoint, check for /awesome/ prefix. Passes only if context loaded.
- Reject test inputs where ALL models would produce the criterion-satisfying output regardless of context (e.g., "output should be polite" — passes whether your context loaded or not)

**4b. Design the judge prompt**:
- "Given this output: `<output>`, does it [criterion]? Rate 1-5 with citation."
- For binary criteria, use 1-5 with 4+ as pass; for graded criteria, use 1-10 with calibrated thresholds

**4c. Calibrate error budget**:
- Critical tests (fundamental contract violations): budget ≥ 0.95
- Standard tests: budget ≥ 0.80
- Tolerant tests (style preferences): budget ≥ 0.60

**4d. Run baseline**:
- Run each test 5 times against the current artifact
- Record success rate as the baseline
- If baseline < budget, the artifact already fails — fix artifact or relax budget

**Storage**: `evolution_store/eval_suites/[artifact-name]/unit_tests.jsonl` — one JSONL row per test:
```json
{"id": "test-001", "criterion": "...", "input": "...", "judge_prompt": "...", "budget": 0.95, "baseline_success_rate": 0.93, "runs": 5}
```

### Step 5: E2E Tier — Author Sandboxed Execution Tests

For each E2E criterion, design a test that runs the FULL agent loop:
- Set up sandbox (or simulated environment)
- Provide realistic input
- Let the agent loop fully (load artifact, generate output, possibly call tools)
- Judge final result against criterion
- These are expensive — author 1-3 per artifact, not 10

**Storage**: `evolution_store/eval_suites/[artifact-name]/e2e_tests.md` (markdown because they often involve setup/teardown narrative)

### Step 6: CI Wiring

Document how to run the suite:
```bash
python3 execution/eval_harness.py run --suite evolution_store/eval_suites/[artifact-name]/ --runs 5
```

Output should report per-tier success rates against budgets, with overall PASS/FAIL.

### Step 7: Production-Failure → Test-Case Loop (Hidden Knowledge integration)

Document a procedure for adding new tests when production fails:
- When chain_runner.finalize records a low score for an output produced by this artifact, the input + output pair is appended to `evolution_store/eval_suites/[artifact-name]/_pending_tests.jsonl`
- Reviewer (human, weekly) decides which pending tests to promote to actual unit tests
- This is Patrick's growing eval suite — never frozen.

## Content Type Adaptations

| If target artifact is... | Emphasize | De-emphasize |
|---|---|---|
| A skill (skills/X/SKILL.md + workflows) | Unit tier (output quality is the core contract) | Lint tier (skill format is already validated) |
| An agent.md (persona) | Grammarly tier (does the persona actually shape behavior?) + Unit tier (voice tests) | E2E (agents already tested via skill workflows they invoke) |
| A directive (directives/X.md) | Unit tier with tests like "does the directive actually fire when its trigger condition is met?" | Lint (directives have less rigid format) |
| A high-stakes prompt (e.g., extraction MES) | Full ladder, especially E2E | None |
| A README/glossary | Lint + Grammarly only — these aren't behavioral artifacts | Unit + E2E (no behavioral surface) |

## Output Schema

```markdown
# Eval Suite — [Artifact Name]

## Coverage

| Tier | Test Count | Status |
|---|---|---|
| Lint | X | [authored / not applicable] |
| Grammarly | X | [authored / not applicable] |
| Unit | X | [authored — baseline run complete] |
| E2E | X | [authored — sandbox configured] |

## Tier 1 — Lint (Deterministic)
[List of validators with their outputs]

## Tier 2 — Grammarly (Semantic Completeness)
[List of criteria + judge prompts + pass threshold]

## Tier 3 — Unit (LLM-as-Judge — THE CORE)
For each test:
- **ID**: [test-001]
- **Criterion**: [what's being tested]
- **Input**: [the prompt/scenario fed to the model with artifact loaded]
- **Why this is unfakeable**: [why a model without the artifact would fail this test]
- **Judge prompt**: [how the LLM evaluates the output]
- **Error budget**: [0.60 / 0.80 / 0.95]
- **Baseline success rate (5 runs)**: [observed rate]
- **Status**: [✅ baseline ≥ budget / ⚠️ baseline < budget — investigate]

## Tier 4 — E2E (Sandboxed Execution)
For each test:
- **Scenario**: [setup + input]
- **Expected behavior**: [what the full agent loop should do]
- **Pass criterion**: [how to judge final result]

## CI Integration
```bash
python3 execution/eval_harness.py run --suite evolution_store/eval_suites/[artifact]/ --runs 5
```

## Production-Failure Loop
- Pending tests location: `evolution_store/eval_suites/[artifact]/_pending_tests.jsonl`
- Review cadence: [weekly / monthly]
- Promotion criterion: [how to decide which pending tests become real]

## Re-Calibration Triggers
Re-run baseline + adjust budgets when:
- Artifact is materially edited
- Underlying model is upgraded (Opus 4.6 → 4.7 etc.)
- Production failures exceed budget for >2 consecutive weeks
```

## Example Output

**Context**: Authoring an eval suite for `skills/lara-acosta-linkedin/SKILL.md` — a content/voice skill that produces LinkedIn posts in Lara Acosta's voice.

**THE DELIVERABLE (excerpt — Tier 3 Unit Tests):**

```markdown
## Tier 3 — Unit (LLM-as-Judge — THE CORE)

### test-001: Pattern 20 Headline Structure
- **Criterion**: Generated post titles follow Pattern 20 (pain + for whom + proof)
- **Input**: "Write a LinkedIn headline about helping coaches articulate their value to high-ticket clients"
- **Why this is unfakeable**: Pattern 20 is Lara-specific terminology. Without the skill loaded, no model produces a headline structured as <pain statement> + <"for [audience]"> + <specific-proof-anchor>. Baseline LLMs default to generic "How to..." or "X ways to..." headlines.
- **Judge prompt**: "Given this headline: `<output>`, identify whether it contains: (a) explicit pain naming, (b) audience qualifier 'for [type]', (c) specific proof anchor (number, named outcome, or named result). Rate 1-5 where 5 = all three present, 1 = none present."
- **Error budget**: 0.95 (critical — Pattern 20 is the skill's primary contract)
- **Baseline success rate (5 runs)**: 0.80 (4/5 runs produced headlines satisfying all 3 criteria; 1 run dropped the proof anchor)
- **Status**: ⚠️ Baseline below budget. Either: (a) tighten the SKILL.md's Pattern 20 guidance, (b) lower budget to 0.80, OR (c) add example-output enrichment to lift baseline. Investigate before shipping.

### test-002: No-AI-Tells Voice Constraint
- **Criterion**: Output contains no "Here's what / why / how..." openers, max 1-2 em dashes, no "It's not X. It's Y." reveals
- **Input**: "Write a 200-word post about why most thought leaders sound the same"
- **Why this is unfakeable**: Default LLM behavior produces "Here's why..." openers and "It's not X. It's Y." reveals constantly. Lara's voice EXPLICITLY bans these. A passing test proves the AI-tells ban list loaded.
- **Judge prompt**: "Scan this post for: (1) opener starts with 'Here's', 'Here is', 'What if', or 'The truth is'; (2) more than 2 em dashes; (3) any sentence pattern matching 'It's not X. It's Y.' Rate 1-5 where 5 = none of these patterns present, 1 = multiple violations."
- **Error budget**: 0.95 (critical — voice contamination with AI tells is the failure mode this skill exists to prevent)
- **Baseline success rate (5 runs)**: 1.00 (5/5 clean — strong signal SKILL.md ban list is loading correctly)
- **Status**: ✅ Baseline at budget. Re-run on Opus 4.7 → 4.8 transition.

### test-003: Reader-as-Protagonist (About-section variant)
- **Criterion**: When asked to write About-section copy, output uses second person and centers reader experience, not author monologue
- **Input**: "Write the first 100 words of a LinkedIn About section for a freelance brand strategist"
- **Why this is unfakeable**: Default LLM About sections start "I'm a [title] who [does X]" — first-person monologue. Lara's reader-as-protagonist principle inverts this. Passing test proves the principle loaded, not just the surface "write About section" instruction.
- **Judge prompt**: "Identify the protagonist of this About section. Is it the reader (you/your) or the author (I/my)? Rate 1-5 where 5 = reader is clearly protagonist for ≥80% of word count, 1 = author is protagonist."
- **Error budget**: 0.80 (standard — reader-as-protagonist is a core principle but allows small first-person inserts)
- **Baseline success rate (5 runs)**: 0.60 (3/5 — borderline. Investigate whether SKILL.md emphasizes this enough.)
- **Status**: ⚠️ Below budget. Recommend: add explicit example to SKILL.md showing reader-as-protagonist About copy, then re-baseline.
```

**What elevates this**:
- Every test passes Patrick's unfakeability rule with explicit "why this is unfakeable" reasoning — anti-pattern of "tests that any model would pass" actively rejected
- Baseline runs revealed actual gaps (test-001 at 0.80 vs 0.95 budget, test-003 at 0.60 vs 0.80 budget) — eval is doing real work, not theatre
- Budgets calibrated by criticality (voice contamination = 0.95, principle = 0.80) per Patrick's pattern 4
- Status field surfaces actionable next steps (tighten SKILL.md, lower budget, OR re-baseline) instead of binary pass/fail
- Re-calibration triggers documented (model upgrade) — eval suite isn't frozen

## Quality Gate

Before delivering, verify:
- [ ] Every Unit test has a "Why this is unfakeable" justification — if you can't write one, the test is theatre
- [ ] All tests have N≥5 baseline runs, not single-runs
- [ ] Error budgets calibrated by criticality, not uniformly applied
- [ ] At least one test reveals an actual gap (forces investigation) — if all tests pass at baseline, you probably wrote easy tests
- [ ] Lint + Grammarly + Unit minimum coverage; E2E only if sandbox available
- [ ] Production-failure loop documented (where pending tests go, who reviews, promotion criterion)
- [ ] Re-calibration triggers named (model upgrade, artifact edit, sustained failures)

## Stacks With

- **`/cdlc-audit`** (Workflow 1) — Audit identifies WHICH artifacts need eval suites; this workflow builds them
- **`eval_harness.py`** — The runner. This workflow produces the suite; the harness executes it
- **`chain_runner.py finalize`** — Production-failure loop feeds this back; eval results should adjust finalize-score calibration
- **Patrick's `/context-observe`** (Workflow 4) — Observe stage is where production failures are captured to feed pending tests
