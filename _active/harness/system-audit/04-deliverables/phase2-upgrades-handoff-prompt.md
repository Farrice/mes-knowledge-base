# Phase 2 Karpathy Audit — Fresh Session Handoff Prompt

> **Purpose**: Complete the remaining two upgrades (3 + 5) from the Phase 2 Karpathy Audit in a fresh conversation. This document is the complete briefing — no prior conversation context needed.
>
> **Date created**: 2026-04-20
> **Upgrades 1, 2, 6 already complete** — verified and committed in prior session
> **This session's work**: Upgrades 3 (Regression Suite) + 5 (Cross-Skill Cascade Detection)
> **Estimated time**: 10-14 hours total (Upgrade 3: 6-8 hrs, Upgrade 5: 4-6 hrs)

---

## Context (Read This First)

You are Claude, continuing work on Antigravity's Phase 2 (Skill Evolution) system upgrade. An audit against Nate B Jones's 18 Karpathy Loop patterns identified 5 upgrades. Three are done. You are finishing two.

**The prior session completed**:

1. **Upgrade 1 — Trace Infrastructure Depth** ✅
   - Expanded `execution/evolution_tracer.py` from v2 (score-only) to v3 (reasoning trajectory)
   - New fields: `hypothesis`, `variant_diff`, `reasoning_chain`, `failure_signals`, `benchmark_tasks`, `held_out_score`, `held_out_delta`, `gaming_flag`, `factual`
   - New CLI commands: `diagnose` (read reasoning chain for a trace), `gaming-check` (scan recent traces for gaming signals)
   - Backwards compatible: v2 traces remain valid
   - Failure detection upgraded to flag on: composite<7, any dim<6, factual<6, gaming flag, blocker-severity signals

2. **Upgrade 2 — Held-Out Benchmark Rotation** ✅
   - Restructured `execution/skill_benchmark.py` `BENCHMARK_TASKS` dict from flat lists to `{seen, held_out}` split
   - Authored 21 new held-out tasks (3 per domain × 7 domains)
   - Added `select_held_out_task(domain, cycle_number)` rotation function
   - Added `compute_gaming_delta(seen_scores, held_out_score)` → returns `{delta, flag, seen_avg}`
   - Gaming flag fires when delta > 1.5
   - `.agent/workflows/skill-evolution.md` Step 7 updated with held-out check + gaming auto-DISCARD logic

3. **Upgrade 6 — Model Empathy Constraint Documentation** ✅
   - Added constraint #11 to `directives/evolution-direction.md`: same-model meta/task pairing (Claude↔Claude) required
   - Added constraint #12: v3 trace logging with reasoning fields required for every cycle

**Your task**: Implement Upgrades 3 and 5. Both are defined below with full specifications.

---

## Upgrade 3 — Regression Suite (CRITICAL)

### Why This Matters

Phase 2 currently shows a **100% KEEP rate across 100+ evolution cycles**. This is suspicious. Either the system is genuinely perfect (unlikely) or silent degradation is going undetected. Without a regression suite, a KEPT variant that degrades a foundational task will go unnoticed until the next time that task type surfaces in a real deliverable.

Per Nate B Jones GP-12 (Silent Degradation failure mode): "Quality erosion that persists undetected because monitoring wasn't designed for autonomous edits."

### What to Build

A **golden-set regression suite** — canonical tasks the system should NEVER regress on, run periodically during evolution to catch silent degradation.

### Specification

**New file**: `execution/regression_suite.py`

**Data structure**:

```python
# Golden set: 5-10 tasks per domain, each with expected score range
# Tasks chosen to be canonical examples of domain competence
# Expected range: (minimum_acceptable, expected_target) — system should score within this
GOLDEN_SET = {
    'copywriting': [
        {
            'task': 'Write a direct-response sales letter opener (first 200 words) for a $97 info product on email deliverability, cold traffic.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Classic DR fundamentals — should score strong on hook, pattern interrupt, problem agitation.',
        },
        # ... 5-10 total per domain
    ],
    'content': [...],
    # ... all 7 domains
}
```

**Required functions**:

```python
def run_regression_audit(domains: list = None, sample_per_domain: int = 3) -> dict:
    """
    Run golden-set tasks against current skills in the specified domains.
    Returns:
    {
        'timestamp': iso,
        'audit_type': 'regression',
        'results': [
            {
                'domain': str,
                'task': str,
                'expected_min': float,
                'current_score': float,
                'delta': float,  # current - expected_min
                'status': 'PASS' | 'WARNING' | 'REGRESSION',
            },
            ...
        ],
        'summary': {
            'total_run': int,
            'passed': int,
            'warnings': int,  # within 0.5 below expected_min
            'regressions': int,  # more than 0.5 below expected_min
        },
        'blocking': bool,  # True if any regression found
    }
    """

def log_regression_result(result: dict) -> None:
    """Log audit result to evolution_store/regression_audits/ (timestamped JSON)."""

def compare_to_baseline(domain: str, task: str) -> dict:
    """Given a domain+task, read last N regression results, return trend."""
```

**CLI commands**:
```bash
python execution/regression_suite.py audit                    # Run full audit
python execution/regression_suite.py audit --domain copywriting  # Single domain
python execution/regression_suite.py history --limit 10       # Recent audit results
python execution/regression_suite.py trend --domain content   # Trend analysis
```

**Storage**:
- `evolution_store/regression_audits/audit_YYYYMMDD_HHMMSS.json` — each audit result
- `evolution_store/regression_audits/baseline.json` — rolling baseline (updated on PASS)

**Integration points**:
1. `.agent/workflows/skill-evolution.md` Step 10 (after KEEP) — run regression suite every 5 KEPT cycles
2. If regression suite returns `blocking: True` → alert user, pause further evolution until resolved
3. Log regression results as v3 traces via `evolution_tracer.py` (use new `operation: "regression_audit"` value)

### Golden Set Authoring Requirements (Hardest Part — Do This Carefully)

Author **5-10 tasks per domain**. For each task:
- **Must be canonical** — represents core competence, not edge case
- **Must have a justified expected_range** — tight enough to catch regression, loose enough to not trigger on normal variance
- **Must be different from** existing `BENCHMARK_TASKS` (don't reuse — regression != evolution benchmark)
- **Should cover the range** — if a domain has 4 sub-capabilities, include tasks for each

**Domains to cover** (same 7 as BENCHMARK_TASKS):
- copywriting, content, strategy, sales, research, brand, default

**Total tasks to author**: 35-70 (conservative: 5 per domain × 7 = 35; thorough: 10 per domain × 7 = 70)

**Authoring methodology**:
1. For each domain, list 5-10 core capabilities (e.g., copywriting: cold email opener, landing page headline, sales letter, email sequence, objection handler, VSL opener, lead magnet copy)
2. For each capability, write ONE canonical task
3. For each task, estimate expected_range by mentally running it through the current best workflow — your expected score IS the upper bound; floor = your expected score - 1.0
4. Document authored_date and notes (why this task is canonical)

### Testing Upgrade 3

```bash
# 1. Verify all domains have golden sets
python3 execution/regression_suite.py audit --dry-run
# Expected: shows count per domain, all ≥5

# 2. Run full audit
python3 execution/regression_suite.py audit
# Expected: produces timestamped JSON, shows PASS/WARN/REGRESSION breakdown

# 3. Deliberately introduce a regression (test case)
# - Temporarily weaken a workflow
# - Rerun audit
# - Verify REGRESSION flag fires
# - Restore the workflow

# 4. Verify integration with skill-evolution.md
# - Run a mock evolution cycle (KEEP a trivial variant)
# - Verify regression audit runs automatically if cycle_count % 5 == 0
```

---

## Upgrade 5 — Cross-Skill Cascade Detection (HIGH)

### Why This Matters

When a KEPT variant changes a skill workflow, it can inadvertently affect related skills through:
- Shared genius.md references (rare but possible)
- Shared reference files (e.g., both skills reference `emergent-behaviors-catalog.md`)
- Cross-pollination (pattern in skill A propagates to skill B)
- Shared expert (the expert agent's thinking shifts, affecting all their skills)

Per Nate B Jones GP-12 (Compounding Errors): "Bad optimization in one system can cascade into a bunch of interconnected business processes."

Phase 2 currently has **no cross-skill regression check** after KEEP.

### What to Build

A **downstream impact monitor** that, after a KEPT variant, samples related skills and verifies they haven't regressed.

### Specification

**Modify (or create)**: Most likely expand `execution/pattern_propagation.py` (check if exists). If not, create `execution/cascade_detector.py`.

**Required functions**:

```python
def find_downstream_skills(skill_kept: str, max_results: int = 5) -> list:
    """
    Identify skills that could be affected by a change to `skill_kept`.
    Relationships checked:
    1. Same expert (all other skills by same expert agent)
    2. Shared reference files (skills that load the same references)
    3. Cross-pollination history (from knowledge/patterns/)
    4. Explicit stacking declarations in SKILL.md
    Returns list of skill_slugs ranked by likelihood of impact.
    """

def check_cascade_impact(skill_kept: str, sample_size: int = 3) -> dict:
    """
    After KEEPing a variant in skill_kept:
    1. Find downstream skills
    2. Sample up to `sample_size` of them
    3. Run benchmark on each (using skill_benchmark)
    4. Compare to their baseline (last N Performance Log entries)
    5. Flag any that regressed >0.5 below baseline
    Returns:
    {
        'skill_kept': str,
        'downstream_checked': [skill_slug, ...],
        'regressions': [{
            'skill': str,
            'current_score': float,
            'baseline_score': float,
            'delta': float,
        }, ...],
        'flag': bool,  # True if any regression
    }
    """

def log_cascade_audit(result: dict) -> None:
    """Log cascade audit to evolution_store/cascade_audits/ (timestamped)."""
```

**CLI commands**:
```bash
python execution/cascade_detector.py check <skill-name>          # Check after a KEEP
python execution/cascade_detector.py related <skill-name>        # Show downstream graph
python execution/cascade_detector.py history --limit 20          # Recent cascade audits
```

**Storage**:
- `evolution_store/cascade_audits/audit_YYYYMMDD_HHMMSS.json`
- `evolution_store/cascade_graph.json` — cached relationship graph (regenerate on demand)

**Integration points**:
1. `.agent/workflows/skill-evolution.md` Step 11 (Cross-Pollination Check) — upgrade to include cascade audit
2. If cascade audit flags regression → alert user, recommend investigation (non-blocking)
3. Log cascade results as v3 traces

### Discovery Methodology for `find_downstream_skills()`

**Relationship types to detect** (in priority order):

1. **Same expert** (highest confidence)
   - Parse skill directory name (e.g., `nate-b-jones-auto-improvement-loops`)
   - Find all other skills with same expert prefix
   - These ALL have genius.md interdependence

2. **Shared reference files** (high confidence)
   - Scan each skill's workflows for `references/` file loads
   - Build reverse index: reference → [skills that load it]
   - Any skill that loads a reference the kept skill also loads

3. **Cross-pollination history** (medium confidence)
   - Read `knowledge/patterns/` for evolved patterns
   - Any skill marked as receiving a pattern transfer from the kept skill

4. **Explicit stacking** (high confidence when present)
   - Parse SKILL.md "Stacking Guide" table
   - Direct stacking partners listed there

**Algorithm**:
```python
def find_downstream_skills(skill_kept):
    related = {}  # {skill_slug: confidence_score}
    
    # Priority 1: same expert
    expert = extract_expert(skill_kept)  # e.g., "nate-b-jones"
    for s in all_skills:
        if s != skill_kept and extract_expert(s) == expert:
            related[s] = related.get(s, 0) + 3.0
    
    # Priority 2: shared references
    kept_refs = parse_references(skill_kept)
    for s in all_skills:
        if s == skill_kept: continue
        s_refs = parse_references(s)
        overlap = set(kept_refs) & set(s_refs)
        if overlap:
            related[s] = related.get(s, 0) + 2.0 * len(overlap)
    
    # Priority 3: pattern transfer (scan knowledge/patterns/)
    transfers = read_pattern_transfers()
    for t in transfers:
        if t['source'] == skill_kept and t['target'] != skill_kept:
            related[t['target']] = related.get(t['target'], 0) + 1.5
    
    # Priority 4: explicit stacking
    stacking = parse_stacking_guide(skill_kept)
    for s in stacking:
        related[s] = related.get(s, 0) + 2.5
    
    # Sort by confidence, return top N
    return sorted(related.items(), key=lambda x: -x[1])[:max_results]
```

### Testing Upgrade 5

```bash
# 1. Verify discovery works
python3 execution/cascade_detector.py related nate-b-jones-orchestration-intelligence
# Expected: returns at least other 5 Nate skills (same expert)

# 2. Run cascade check
python3 execution/cascade_detector.py check nate-b-jones-orchestration-intelligence
# Expected: samples 3 downstream skills, returns JSON result

# 3. Integration test
# - KEEP a variant in a test skill
# - Verify cascade check runs in skill-evolution.md Step 11
# - Verify audit logged to evolution_store/cascade_audits/
```

---

## Critical Constraints (DO NOT VIOLATE)

These are the same constraints from `directives/evolution-direction.md`:

1. **Never modify genius.md content** of existing skills
2. **Single file per cycle** — evolution can only modify ONE workflow file per experiment
3. **Keep the human in the loop** — present audits, wait for approval before auto-pausing evolution
4. **Same-model meta/task pairing** — Claude↔Claude only
5. **v3 trace logging required** — every regression audit and cascade audit must log via `evolution_tracer.py`
6. **No breaking changes** to existing Phase 2 loop — regression + cascade are ADDITIVE layers, never blockers on first implementation

---

## File Inventory (What You'll Touch)

**Create**:
- `execution/regression_suite.py` (new, ~300-500 lines)
- `execution/cascade_detector.py` (new, ~200-300 lines) — OR expand `pattern_propagation.py`
- `evolution_store/regression_audits/` (new directory)
- `evolution_store/cascade_audits/` (new directory)
- `evolution_store/cascade_graph.json` (generated on first run)

**Modify**:
- `.agent/workflows/skill-evolution.md` Step 10 (add regression call) + Step 11 (add cascade call)
- `directives/evolution-direction.md` — add Upgrade 3 + 5 completion notes to System Status table

**Read (reference only, do not modify)**:
- `execution/skill_benchmark.py` — for `benchmark_skill()` signature and scoring integration
- `execution/evolution_tracer.py` — for v3 trace logging signature
- `_active/harness/system-audit/04-deliverables/phase2-karpathy-audit-2026-04-20.md` — full original audit
- `skills/nate-b-jones-auto-improvement-loops/genius.md` — canonical patterns
- `skills/nate-b-jones-auto-improvement-loops/references/emergent-behaviors-catalog.md` — for Pattern 8 (held-out) and Pattern 9 (rubric randomization) principles

---

## Suggested Execution Order

**Session structure** (if doing both in one session):

### Hours 1-4: Upgrade 3 Code + Infrastructure
1. Create `execution/regression_suite.py` skeleton with all 4 functions
2. Stub `GOLDEN_SET` with 2 tasks per domain to validate structure
3. Implement `run_regression_audit()` and `log_regression_result()`
4. CLI hooks + test with stubbed data
5. Verify integration with `evolution_tracer.py`

### Hours 5-7: Upgrade 3 Golden Set Authoring
6. Expand `GOLDEN_SET` from 2 → 5-10 tasks per domain
7. Carefully author expected_range for each
8. Document authored_date and notes
9. Run first full audit, verify baseline captures correctly

### Hours 8-10: Upgrade 5 Code
10. Create `execution/cascade_detector.py`
11. Implement `find_downstream_skills()` with all 4 relationship types
12. Implement `check_cascade_impact()` with sampling
13. CLI hooks + test with a known-relationship skill (e.g., any Nate skill)

### Hours 11-13: Integration + Testing
14. Update `.agent/workflows/skill-evolution.md` Steps 10 + 11
15. Update `directives/evolution-direction.md` System Status table
16. Run end-to-end test: mock evolution cycle → regression fires → cascade fires → all audits logged

### Hour 14: Commit + Finalize
17. Verify git status shows all expected changes
18. Commit: "feat(phase2): Upgrades 3+5 — regression suite + cascade detection (Karpathy audit)"
19. Run `python3 execution/chain_runner.py finalize` to log completion
20. Optional: re-run `/nate-auto-phase2` for post-upgrade delta audit

---

## Quality Gates

Before considering either upgrade complete:

**Upgrade 3 (Regression Suite)**:
- [ ] `execution/regression_suite.py` exists with all 4 required functions
- [ ] CLI commands work (audit, history, trend, --dry-run)
- [ ] GOLDEN_SET has 5+ tasks per domain (7 domains minimum)
- [ ] Each task has expected_range tuple
- [ ] Deliberately-introduced regression is caught by audit
- [ ] Results logged to `evolution_store/regression_audits/`
- [ ] Integration with `skill-evolution.md` Step 10 verified

**Upgrade 5 (Cascade Detection)**:
- [ ] `execution/cascade_detector.py` exists with all 3 required functions
- [ ] CLI commands work (check, related, history)
- [ ] `find_downstream_skills()` correctly identifies same-expert siblings
- [ ] `find_downstream_skills()` correctly identifies shared-reference relationships
- [ ] `check_cascade_impact()` samples and scores downstream skills
- [ ] Results logged to `evolution_store/cascade_audits/`
- [ ] Integration with `skill-evolution.md` Step 11 verified

---

## Sanity Checks Before Starting

Run these commands to confirm the prior upgrades are in place:

```bash
# 1. Verify v3 trace schema is live
python3 execution/evolution_tracer.py log --help | grep hypothesis
# Should show --hypothesis arg

# 2. Verify held-out benchmark structure exists
cd execution && python3 -c "from skill_benchmark import BENCHMARK_TASKS, select_held_out_task, compute_gaming_delta; print(list(BENCHMARK_TASKS['copywriting'].keys()))"
# Should output: ['seen', 'held_out']

# 3. Verify model empathy constraint is documented
grep -c "Same-model meta/task pairing" directives/evolution-direction.md
# Should output: 1

# 4. Verify skill-evolution.md Step 7 references held-out check
grep -c "select_held_out_task" .agent/workflows/skill-evolution.md
# Should output: 1
```

If any of these fail, STOP and check what's missing before proceeding with Upgrades 3 + 5.

---

## Upon Completion

1. **Re-audit with `/nate-auto-phase2`** — should show CRITICAL gaps resolved:
   - GP-12 Silent Degradation: was 3/10 → should be 8+/10
   - GP-12 Compounding Errors: was 4/10 → should be 8+/10
   - Average pattern score should move from 6.5/10 → 8.0+/10

2. **Update `_active/harness/system-audit/04-deliverables/phase2-karpathy-audit-2026-04-20.md`** — add a "Status as of [new date]" section at top showing which upgrades were completed.

3. **Document any NEW emergent behaviors** observed during the audit runs themselves. Add to `skills/nate-b-jones-auto-improvement-loops/references/emergent-behaviors-catalog.md`.

4. **Schedule Upgrade 7 (Revenue Tracker auto-link, MEDIUM priority)** for a future session if desired — it's 2 hrs but produces the business-value correlation data that validates the entire audit.

---

## Reference Documents

When executing, have these open:
- **The audit itself**: `_active/harness/system-audit/04-deliverables/phase2-karpathy-audit-2026-04-20.md` — full spec for all 7 upgrades
- **Nate's genius**: `skills/nate-b-jones-auto-improvement-loops/genius.md` — 18 patterns, 9 signature moves
- **Emergent behaviors catalog**: `skills/nate-b-jones-auto-improvement-loops/references/emergent-behaviors-catalog.md`
- **Current evolution direction**: `directives/evolution-direction.md` (has Karpathy Triplet header + new constraints 11-12)
- **Skill benchmark**: `execution/skill_benchmark.py` — reference for BENCHMARK_TASKS structure
- **Evolution tracer**: `execution/evolution_tracer.py` — v3 schema reference

---

## Prompt to Kick Off the Fresh Session

Copy-paste this into a fresh Claude Code conversation in the Antigravity workspace:

```
Continue the Phase 2 Karpathy Audit upgrade work. Read _active/harness/system-audit/04-deliverables/phase2-upgrades-handoff-prompt.md for full context — it's a complete briefing from the prior session.

Summary: Upgrades 1, 2, and 6 are done (trace v3, held-out rotation, model empathy doc). Now implement Upgrades 3 (Regression Suite) and 5 (Cross-Skill Cascade Detection).

Start with the sanity checks at the bottom of the handoff document to verify prior upgrades are live. Then execute Upgrade 3 fully, then Upgrade 5 fully. Estimated 10-14 hours of focused work.

When complete, re-run /nate-auto-phase2 for a delta audit showing which gaps closed. Commit after each major upgrade (not one giant commit).
```

That's it. The fresh session will have everything needed.
