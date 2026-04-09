# Evolution Direction

> **Analog**: Karpathy's `program.md` — the natural language instruction set that guides the self-improvement loop.
> **Purpose**: Single source of truth for what to evolve, why, and when to stop.
> **Updated**: After every evolution cycle. Read before every `/skill-evolution` run.
> **Created**: 2026-04-06

---

## Current Evolution Priorities

### Priority 1: Activate Phase 2 (First Evolution Cycle)

**Target**: Pick the lowest-performing skill from Performance Log (76+ entries available).

**Why**: Phase 2 infrastructure has been built since 2026-03-10 but has never been activated. The threshold (20 entries) was met months ago. Running the first cycle proves the loop works end-to-end.

**Approach**:
1. Run `python execution/skill_benchmark.py benchmark <skill-name>` on 3-5 candidate skills
2. Select the one with the clearest improvement target (lowest dimension score)
3. Write hypothesis, generate variant, test, keep/discard
4. Log result + git commit if KEPT

**Success criteria**: One full evolution cycle completed, result logged, variant either KEPT or DISCARDED with a documented lesson.

### Priority 2: Ground Truth Calibration

**Target**: Validate that our quality scores actually reflect expert-level quality.

**Why**: Without calibrating against real expert output, we could be "evolving" toward AI-pleasing patterns that don't match real expertise. The ground truth system exists but hasn't been used systematically.

**Approach**:
1. Run `python execution/ground_truth.py gap-report` to see current coverage
2. Add 2-3 expert samples to the most-used domains (if missing)
3. Run blind comparisons on skills that just went through evolution
4. If scores diverge >2 points from expert baseline, recalibrate

### Priority 3: Cross-Pollination Activation

**Target**: After first KEPT variant, check if improvement transfers to related skills.

**Why**: Phase 3 has 0 activations. One successful transfer would prove the pattern family mapping works.

**Blocked by**: Priority 1 (needs at least one KEPT evolution result).

---

## Constraints (Do Not Cross)

1. **Never modify genius.md content** — expert frameworks are the bedrock. Only workflow files and Evolution Log sections change.
2. **Never test more than one hypothesis per cycle** — isolated variables prevent false positives.
3. **Keep the human in the loop** — present comparisons, wait for approval before replacing workflows.
4. **Time-box all benchmark runs** — 10 minutes max per task. If it's not producing in 10 minutes, the approach is wrong.
5. **Binary decisions during evolution** — composite >= 7 = KEEP, < 7 = DISCARD. No "marginal" retries.
6. **Git-commit every KEPT variant** — auditable evolution history, always.

---

## Stopping Criteria

**Pause evolution and reassess when**:
- 3 consecutive DISCARD results on the same skill (hypothesis space may be exhausted for now)
- A KEPT variant causes downstream regression in a different skill
- Quality scores diverge >2 points from Ground Truth blind comparison results
- Revenue Tracker shows KEPT variants producing lower business outcomes than originals

---

## Evolution History

> Updated after every cycle. Shows the full trail of what was tried and what happened.

| Date | Skill | Hypothesis | Result | Score Delta | Notes |
|------|-------|-----------|--------|-------------|-------|
| 2026-04-09 | lara-acosta-linkedin-mastery | Add Phase 4b Proof Layer Audit + adversarial quality gate checks | KEPT | 7.8 → 8.3 (+0.5) | First evolution cycle. Targets adversarial resilience. |
| 2026-04-09 | kallaway-word-mastery | Add Emotional Stakes Architecture to Grip & Tension Engine | KEPT | 8.3 (tie, qualitative win) | 5 stakes mechanics (Personal Mirror, Cost Made Concrete, Belief Collision, Near-Miss Story, Identity Bridge). Reader becomes protagonist. |
| 2026-04-09 | nicolas-cole-sentence-craft | Add Sentence Demand Architecture to Terminal Power & Rhythm Engineering | KEPT | 8.3 (tie, 43% vs 32% compression) | 5 demand mechanics (Incomplete Transfer, Expectation Violation, Specificity Spike, Reversal Bridge, Compression Cliffhanger) + Energy Crescendo Mapping. |

---

## Research Directions (What to Explore Next)

These are ideas for future evolution cycles, not current commitments:

- **Hook quality across content skills**: Many content skills score well on structure but plateau on hook power. Test whether borrowing Kallaway's curiosity gap patterns improves hook scores.
- **Voice authenticity**: Prose classifier catches AI tells, but can we actively inject more human variance? Test whether adding "voice disruption" steps (vary sentence length, add specific details) improves Expert Standard.
- **Cross-domain proof patterns**: Luke Iha's proof mechanisms might strengthen brand strategy skills. Test whether weaving proof architecture into positioning workflows improves Adversarial Resilience.

---

## System Status

| Component | Status | Last Activated | Entries |
|-----------|--------|---------------|---------|
| Feedback Ratchet (Phase 1) | ACTIVE | 2026-04-05 | 76 |
| Skill Evolution (Phase 2) | **ACTIVE** | 2026-04-09 | 3 |
| Cross-Pollination (Phase 3) | WAITING | Never | 0 |
| Ground Truth | READY | Manual only | — |
| Intelligence Gap Detector | READY | On-demand | — |
| Revenue Tracker | READY | Manual only | — |

---

*This document is the evolution compass. Update it after every cycle. Read it before every evolution run.*
