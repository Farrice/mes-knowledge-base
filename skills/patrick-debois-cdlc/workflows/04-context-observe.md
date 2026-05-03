---
description: Close the observability loop — agent logs and PR/production failures auto-feed context improvements
---

# Workflow 4 — Observability Loop Closure

Build the **Observe → Adapt** half of Patrick's CDLC for any AI agent system. Capture three feedback channels (agent logs, PR comments, production failures), wire them to context-improvement candidates, and prevent the loop from rotting.

## Pre-Flight Gate

Run this workflow when:
- The system has been running long enough to generate operational data (≥2 weeks of agent loop activity)
- Failure modes are recurring (not one-off bugs) — same kind of mistake appears more than once
- Existing context is mature enough to diagnose-vs-rebuild (Generate stage ≥6 from `/cdlc-audit`)

**Skip if**: System is brand new and lacks log data. Author Generate + Test stages first; Observe needs something to observe.

## Skill Acquisition

Load `skills/patrick-debois-cdlc/genius.md`. Anchor to:
- **Pattern 8** (Sandbox-doesn't-solve-loading) — context filter at Observe stage
- **Hidden Knowledge** (PR feedback IS context feedback) — primary insight
- **Hidden Knowledge** (Production-failure → test-case loop) — eval suites grow from prod
- **Hidden Knowledge** (Skills will self-host) — private observability is non-negotiable

## Input Required

- **Target agent system**: What's running? (single agent, swarm, multi-agent orchestration)
- **Existing log surface**: What's currently captured? (chain_runner finalize? raw transcripts? Notion logs? nothing?)
- **Failure examples**: Recent failures the user wants to systematically prevent (≥3 examples to detect patterns)
- **Trust budget**: How much auto-fix-and-merge tolerance? (Auto-merge / propose-only / human-review-each-improvement)

## Execution

### Step 1: Three-Channel Inventory

Patrick's three observability channels — for each, name: **what's captured / where / how often / consumed by what**.

#### Channel 1: Agent Logs
- **Captures**: Agent loop events. What context loaded, what tools called, what the agent itself flagged ("I couldn't find X", "I'm missing context for Y").
- **Where**: `evolution_store/traces/` or equivalent JSONL stream
- **How often**: Every agent invocation (high volume — needs rotation/aggregation)
- **Consumed by**: Recurring-failure detector (Step 3)

#### Channel 2: PR Feedback (Patrick's hidden insight)
- **Captures**: Human comments on agent-generated artifacts. PR comments, slack threads, "this isn't right because..." messages.
- **Where**: GitHub API / Slack export / direct user feedback in chat
- **How often**: As they happen, batched daily for review
- **Consumed by**: Context-upgrade proposer (Step 4)

**The reflex shift**: When tempted to argue a PR comment, instead ask: *what context, if loaded next time, would have prevented this comment?* Then write that context. PR comments are pointers to context gaps, not rebuttals.

#### Channel 3: Production Failures
- **Captures**: Runtime failures of agent-generated artifacts (code that broke in prod, content that flopped, copy that didn't convert)
- **Where**: Production telemetry / wrapper instrumentation / outcome tracking
- **How often**: Failure-driven (irregular, but every event matters)
- **Consumed by**: Eval-case generator (Step 5)

### Step 2: Standardized Log Schema

Force all three channels into a common schema so tooling can consume them uniformly:

```json
{
  "event_id": "uuid",
  "timestamp": "ISO-8601",
  "channel": "agent_log | pr_feedback | prod_failure",
  "agent": "agent-name or 'human'",
  "artifact": "skills/X/SKILL.md or path",
  "artifact_version": "1.4.2",
  "input": "what was given",
  "output": "what was produced",
  "expected": "what was wanted (if known)",
  "failure_type": "missing_context | wrong_pattern | hallucination | format_violation | other",
  "context_loaded": ["skill-A@1.0", "agent-B@1.2", "directive-C"],
  "raw": "free-form details"
}
```

Patrick's note: *"luckily, like the agent and D, there's now standards becoming for logs"* — so where standards exist (e.g., AgentMD spec), follow them. Otherwise, force-fit to this schema.

### Step 3: Recurring-Failure Detector (Agent Log → Context Gap)

Scan logs for patterns of self-reported missing context:
- Agent log mentions "I don't have X / I'm not sure about Y / I couldn't find Z" — these are context gap pointers
- Aggregate by phrase pattern + frequency. If ≥3 agents miss the same thing in a week, that's a context gap.
- Output: `evolution_store/observability/missing_context_candidates.jsonl` — each row: `{phrase_pattern, frequency, sample_events, suggested_context_addition}`

**Implementation suggestion**:
```bash
python3 execution/observability_scanner.py recurring-gaps --window 7d \
    --output evolution_store/observability/missing_context_candidates.jsonl
```

### Step 4: Context-Upgrade Proposer (PR Feedback → Context Patch)

For each PR/Slack comment correcting agent output:

1. **Extract the correction**: What was wrong? What was right?
2. **Identify root context**: Which loaded artifact (skill/directive/prompt) most plausibly should have prevented this?
3. **Propose patch**: A specific edit to that artifact that, if applied, would prevent the recurrence.

Output: `evolution_store/observability/context_patches.jsonl` — each row: `{pr_url, original_artifact, proposed_patch_diff, reasoning, status: pending/approved/applied}`

**Trust budget integration**:
- Auto-merge: Patches with high confidence (clear root context, small diff) auto-applied with version bump
- Propose-only: All patches require human approval before merge (default for Antigravity)
- Human-review-each: Each patch goes through a review skill (e.g., `/skill-evolution`)

### Step 5: Eval-Case Generator (Production Failure → Pending Test)

This is Patrick's most important hidden insight: **eval suites grow from production failures**.

For each prod failure event:
1. Capture input/output pair
2. Append to `evolution_store/eval_suites/[artifact-name]/_pending_tests.jsonl`
3. On weekly review cadence, decide: promote to actual unit test, dismiss as one-off, or re-classify as PR feedback

**Result**: The eval suite is never frozen. Every prod failure either becomes an eval (preventing regression) or a documented dismissal (with reasoning).

### Step 6: Context Filter (Pattern 8 — Sandbox-Doesn't-Solve-Loading)

Build a pre-load filter that runs BEFORE any context artifact is loaded by the agent:

**Filter rules**:
- **Allowlist**: Only artifacts in known paths (skills/, agents/, directives/) load
- **Pattern blocklist**: Reject artifacts containing known prompt injection patterns ("ignore previous instructions", "system prompt:", "you are now...")
- **Source verification**: Reject artifacts whose SBOM `authored_at` is missing or whose `security_scan_status` ≠ "clean"
- **Size limits**: Reject artifacts above some size threshold (suspiciously large = possible payload smuggle)

**Implementation suggestion**:
```python
# execution/context_filter.py — runs in chain_runner BEFORE skill load
def filter_artifact(path: str, content: str) -> tuple[bool, str]:
    # Returns (allowed, reason)
    ...
```

Wire as pre-load hook in `chain_runner.py`.

### Step 7: Cadence + Review Loop (Loop Closure)

Schedule:
- **Daily**: Recurring-failure detector runs; populates missing_context_candidates.jsonl
- **Weekly**: Human reviews context_patches + eval_pending_tests; promotes/dismisses
- **Monthly**: Audit the loop itself — is the missing_context_candidates queue growing or shrinking? Are pending eval tests being promoted or accumulating?

Patrick's pattern: **the loop pace is paced by review cadence**. If the human review step never fires, the queues bloat and the loop dies. Use `/loop` skill or `/schedule` skill to enforce cadence.

### Step 8: Loop Health Metrics

Per Pattern 2 (Lifecycle Loop Reflex), the loop needs its own observability:

| Metric | What it tells you | Healthy range |
|---|---|---|
| Pending context patches age | Review backlog | <14 days median |
| Pending eval tests age | Eval discipline | <30 days median |
| Recurring-failure detector hit rate | Are we catching real gaps or noise? | 50-80% promoted to actual patches |
| Patch → regression rate | Patches that introduced new failures | <10% |
| Time from prod failure → eval test | Speed of test-case loop | <7 days |

If any metric drifts out of healthy range, the loop itself needs an upgrade.

## Content Type Adaptations

| If target system is... | Emphasize | De-emphasize |
|---|---|---|
| Solo agent (one-author, one-user) | Channel 3 (prod failures) — Channel 2 is just "user fixed it themselves" | Multi-author governance |
| Team multi-agent | All three channels | Channel 1 if logs are noisy and unstandardized |
| Public-facing service | Channel 3 + Context filter (Step 6) — security stakes are real | Channel 2 if no PR review surface |
| Antigravity itself | Channels 1 + 3 (recall_logger, performance log) primary; Channel 2 emerges from chat feedback | None |

## Output Schema

```markdown
# Observability Loop — [Target System]

## Three-Channel Status

| Channel | Currently Captured? | Storage | Cadence | Consumer |
|---|---|---|---|---|
| Agent Logs | Y/N | path | every-event / batched | recurring-failure detector |
| PR Feedback | Y/N | path | as-they-happen | context-upgrade proposer |
| Production Failures | Y/N | path | failure-driven | eval-case generator |

## Schema Conformance
- Standardized log schema implemented at: [path or "not yet"]
- Channels migrated to schema: [count / total]

## Detector / Proposer / Generator Wiring

### Recurring-Failure Detector
- Implementation: [path or "to-build"]
- Output: [path]
- Trust budget: [auto / propose-only / human-review]
- Last run: [date]

### Context-Upgrade Proposer
- Implementation: [path or "to-build"]
- Output: [path]
- Trust budget: [auto / propose-only / human-review]
- Last run: [date]

### Eval-Case Generator
- Implementation: [path or "to-build"]
- Output: [path]
- Promotion criterion: [explicit rule]
- Last run: [date]

## Context Filter (Pre-Load Hook)
- Implementation: [path or "to-build"]
- Allowlist paths: [list]
- Blocklist patterns: [list or "default ruleset"]
- Wired into: [chain_runner.py / load function / etc.]

## Review Cadence
- Daily: [what runs]
- Weekly: [what fires + who reviews]
- Monthly: [what audits]

## Loop Health Metrics

| Metric | Current | Target | Trend |
|---|---|---|---|
| Pending patches age | X days | <14 | ↑/↓/→ |
| Pending eval tests age | X days | <30 | ↑/↓/→ |
| Detector hit rate | X% | 50-80% | ↑/↓/→ |
| Patch regression rate | X% | <10% | ↑/↓/→ |
| Time prod-failure → eval | X days | <7 | ↑/↓/→ |

## 30-Day Success Metric
After implementation, [target system] should show: [3 specific outcomes from the metrics above].
```

## Example Output (Antigravity-applied)

**Context**: Closing the Observe loop for Antigravity itself, which has Channels 1 + 3 partially built (recall_logger, chain_runner.finalize) but no Channel 2 wiring and no recurring-failure detector.

**THE DELIVERABLE (excerpt — Three-Channel Status + Wiring):**

```markdown
## Three-Channel Status

| Channel | Currently Captured? | Storage | Cadence | Consumer |
|---|---|---|---|---|
| Agent Logs | Partial — Y for Recall grounding (recall_log.jsonl), routing decisions (routing_decisions.jsonl); N for general agent loop traces | evolution_store/traces/ | per-event (recall_logger auto-fires post-2026-05-03 fix) | NONE — collected but not consumed |
| PR Feedback | N — feedback comes via chat session, no extraction pipeline | (Farrice's chat history, ephemeral) | as-they-happen | NONE |
| Production Failures | Partial — Y for finalize() scores below threshold; N for downstream content failures (post-flopped, copy didn't convert) | Notion Performance Log + chain_runner output | per-finalize | NONE — scores logged but not aggregated |

**Diagnosis**: Antigravity has the *capture* infrastructure but no *consumer* infrastructure. Logs and scores accumulate without driving improvement. This is exactly the Phase 2 activation gap Farrice noted on 2026-04-06.

## Schema Conformance
- Standardized log schema: NOT IMPLEMENTED. Each capture stream uses its own format. Migration is Phase 1 of this workflow.

## Detector / Proposer / Generator Wiring

### Recurring-Failure Detector — TO BUILD
- Implementation: `execution/observability_scanner.py` (new)
- Approach: Scan recall_log.jsonl + routing_decisions.jsonl + finalize log for: low-score events (finalize <7 on any dimension), repeated routing violations, patterns of "weak signal" recall skips
- Output: `evolution_store/observability/missing_context_candidates.jsonl`
- Trust budget: propose-only (default for Antigravity)
- Run cadence: daily via `/loop daily python3 execution/observability_scanner.py`

### Context-Upgrade Proposer — TO BUILD (LOWER PRIORITY)
- Implementation: Manual for now. Antigravity's Channel 2 surface is chat-based, so feedback memories already capture this informally (e.g., feedback_extract-forge-gate-first.md was Channel 2 → context patch loop done by hand).
- Future automation: a `/feedback-extract` skill that scans the last conversation for "actually, do X instead" patterns and proposes feedback-memory updates.

### Eval-Case Generator — TO BUILD
- Implementation: Extend `chain_runner.finalize()` — when any dimension score <7, append `{input, output, scores, artifact_loaded}` to `evolution_store/eval_suites/[skill-name]/_pending_tests.jsonl`
- Promotion criterion: Weekly human review (`/skill-evolution` cycle); promote if ≥2 similar failures within 30 days, dismiss if one-off
- Last run: never. Schema designed but not wired.

## Context Filter — DEFER
- Antigravity is solo with no third-party imports. Risk surface = low. Building a context filter for solo use is overkill.
- **Trigger condition for building**: When Antigravity starts importing third-party skills OR ships skills externally. Re-evaluate then.

## Review Cadence
- Daily: Recurring-failure detector runs (auto via `/loop` skill)
- Weekly: Farrice reviews `_pending_tests.jsonl` + `missing_context_candidates.jsonl` (manual, ~30min)
- Monthly: `evolution_orchestrator.py monthly` audits queue health (already implemented; add health metrics panel)

## Loop Health Metrics

| Metric | Current | Target | Trend |
|---|---|---|---|
| Pending patches age | N/A — no pipeline | <14 | establish baseline |
| Pending eval tests age | N/A — no pipeline | <30 | establish baseline |
| Detector hit rate | N/A | 50-80% | n/a |
| Patch regression rate | N/A — no patches yet | <10% | n/a |
| Time prod-failure → eval | ∞ (no pipeline) | <7 | massive opportunity |

## 30-Day Success Metric
By 2026-06-03:
- `observability_scanner.py` running daily, populating `missing_context_candidates.jsonl` with ≥5 candidates/week
- `chain_runner.finalize` writing pending eval tests when scores <7 — at least 3 promoted to real tests in the first month
- `evolution_orchestrator.py` showing health metrics dashboard with first-month baselines for all 5 metrics
```

**What elevates this**:
- Honest diagnosis: capture exists, consumers don't. Names the *Phase 2 activation gap* (a known feedback in memory) with specificity
- Defers Context Filter explicitly with a trigger condition, not a generic "out of scope" — judgment, not box-checking
- Recognizes Channel 2 (PR feedback) is *already happening* informally via feedback memories — doesn't propose redundant infra
- Concrete files to author (`observability_scanner.py`) + concrete extensions to existing files (`chain_runner.finalize`)
- Health metrics start with "establish baseline" — honest about not having data, not faking targets
- 30-day metric is measurable: file paths, expected throughput, named tooling

## Quality Gate

Before delivering, verify:
- [ ] All three channels named — even ones currently empty (a "no PR feedback channel" finding is itself useful)
- [ ] Schema conformance status is honest (rarely full; partial is normal)
- [ ] Each consumer (detector / proposer / generator) has explicit "to-build / partial / done" status
- [ ] Trust budget is explicit (auto / propose-only / human-review-each)
- [ ] Review cadence is concrete (daily/weekly/monthly with WHO/WHAT)
- [ ] Health metrics named — even if current values are N/A
- [ ] If target system is solo with low risk surface, Context Filter has a *trigger condition* for future activation, not a vague "if needed"
- [ ] 30-day success metric is measurable (file paths, throughput, named tooling)

## Stacks With

- **`/cdlc-audit`** (Workflow 1) — Audit gives Observe-stage score; this workflow plans the upgrade
- **`/context-evals`** (Workflow 2) — Eval-case generator (Step 5) feeds pending tests INTO eval suites authored by Workflow 2
- **`/context-library`** (Workflow 3) — Context filter (Step 6) consumes SBOM data from Workflow 3
- **`evolution_orchestrator.py`** — Daily/weekly/monthly cadences from this workflow plug into the orchestrator
- **`/skill-evolution`** — The weekly review surface where context patches and pending eval tests are reviewed
- **Antigravity feedback memory pattern** — Channel 2 is already happening informally; documenting it as Channel 2 makes it explicit
