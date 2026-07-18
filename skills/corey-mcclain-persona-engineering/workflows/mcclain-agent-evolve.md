# Agent Evolve — Post-Deployment Compounding Engine

> The agent that stops evolving starts dying. This workflow keeps deployed agents sharp through structured feedback loops, persona deepening, and skill expansion — without breaking what already works.

---

## Pre-Flight Gate

- [ ] Agent is **deployed and operational** (passed stress test)
- [ ] Minimum **3 real outputs** exist to evaluate
- [ ] Original source material accessible for re-mining
- [ ] Agent directory path confirmed: `agents/[name]/`

---

## Phase 1 — Performance Audit

Evaluate the agent's live outputs against its original intent.

### 1.1 Output Collection
Gather the agent's 3-5 most recent outputs. For each, capture:
- **Task given** — what was requested
- **Output quality** — 1-10 against the expert's actual standard
- **Persona bleed** — did the voice hold or drift toward generic?
- **Blind spots** — what did the agent miss that the real expert wouldn't?

### 1.2 Drift Diagnosis
Score each dimension:

| Dimension | Score (1-10) | Drift Direction |
|---|---|---|
| Voice fidelity | | Toward generic / toward caricature |
| Framework application | | Too rigid / too loose |
| Worldview consistency | | Breaking character / over-filtering |
| Skill depth | | Surface-level / hallucinating expertise |
| Persona density | | Thinning out / bloating |

**Composite < 7 = evolution required.** Composite ≥ 8 = maintenance mode only.

---

## Phase 2 — Source Re-Mining

Go back to the original source material with fresh eyes. Now that the agent has been running, you know what's missing.

### 2.1 Gap-Targeted Extraction
For each blind spot identified in Phase 1:
1. **Re-read source** looking specifically for that gap
2. **Extract the missing pattern** — the framework, heuristic, or decision tree the expert uses that the agent doesn't
3. **Document as a new Library entry** with the format:
   ```
   ## [Pattern Name]
   - **When to apply:** [trigger condition]
   - **How it works:** [mechanism]
   - **Source evidence:** [quote or timestamp]
   - **Why it was missed initially:** [extraction blind spot]
   ```

### 2.2 Persona Deepening
Mine for second-layer details that only surface after you've lived with the persona:
- **Contradiction patterns** — where does the expert contradict themselves, and why?
- **Emotional triggers** — what topics make them light up vs. shut down?
- **Evolution markers** — how has their thinking changed over time?
- **Relationship to their audience** — mentor, peer, provocateur, coach?

Add these to the persona narrative document as new sections, not replacements.

---

## Phase 3 — Surgical Updates

> Rule: **Never rewrite the agent. Patch it.**

### 3.1 Logic Layer Updates
If framework application scored < 7:
- Add missing decision trees to `AGENT.md` Logic section
- Tighten existing framework descriptions with better trigger conditions
- Add "anti-patterns" — things this expert would never do

### 3.2 Library Layer Updates
If skill depth scored < 7:
- Add new methodology entries from Phase 2 gap extraction
- Enrich existing entries with second-order details
- Add cross-references between related frameworks

### 3.3 Memory Layer Updates
If worldview consistency scored < 7:
- Add new memory anchors from contradiction patterns
- Update the "formation narrative" with evolution markers
- Strengthen the worldview filter with new boundary conditions

### 3.4 Persona Layer Updates
If voice fidelity scored < 7:
- Add new vocabulary entries (words they use, words they'd never use)
- Tighten cadence patterns with more examples
- Add emotional texture notes from Phase 2.2
- **Never compress the persona narrative** — only expand it

---

## Phase 4 — Regression Check

Before committing updates, verify nothing broke.

### 4.1 A/B Comparison
Take 2 of the original test prompts from the stress test:
1. Run them against the **pre-evolution** agent (saved version)
2. Run them against the **post-evolution** agent (updated version)
3. Compare side-by-side for:
   - Voice consistency (should improve or hold)
   - Framework depth (should improve)
   - Persona density (should not thin)
   - Blind spot coverage (should improve)

### 4.2 Identity Stability Test
Ask the evolved agent a question that tests its core worldview:
- It should give the same *type* of answer as before, with more depth
- If the answer fundamentally changed, the evolution broke something — roll back that specific patch

---

## Phase 5 — Evolution Log

Document what changed and why. This creates the compounding record.

### Evolution Entry Format:
```markdown
## Evolution [N] — [Date]

### Trigger
[What performance gap or new source material triggered this evolution]

### Changes Made
- Logic: [what was added/modified]
- Library: [what was added/modified]  
- Memory: [what was added/modified]
- Persona: [what was added/modified]

### Before/After Scores
| Dimension | Before | After |
|---|---|---|
| Voice fidelity | X | Y |
| Framework application | X | Y |
| Worldview consistency | X | Y |
| Skill depth | X | Y |
| Persona density | X | Y |

### Regression Status
- [ ] A/B comparison passed
- [ ] Identity stability confirmed
- [ ] No persona thinning detected

### Next Evolution Triggers
[What to watch for that would trigger the next evolution cycle]
```

Save as `agents/[name]/memory/evolution-log.md` — append, never overwrite.

---

## Phase 6 — Compounding Schedule

Set the cadence based on agent usage:

| Usage Level | Evolution Cadence | Trigger |
|---|---|---|
| Daily use | Every 2 weeks | After 20+ outputs |
| Weekly use | Monthly | After 10+ outputs |
| Occasional | Quarterly | After 5+ outputs |
| New source material added | Immediate | Any new source |

### Auto-Triggers (bypass schedule):
- Voice fidelity drops below 6 on any output
- Agent produces a response the real expert would actively reject
- New source material surfaces (video, article, interview)
- Agent is asked to cover a topic not in its current Library

---

## Output Schema

Two artifacts, both append-only:

1. **Evolution Log Entry** — appended to `agents/[name]/memory/evolution-log.md` using the `## Evolution [N] — [Date]` template from Phase 5: Trigger, Changes Made (per LLMP layer), Before/After Scores table, Regression Status checklist, Next Evolution Triggers. Never overwrite prior entries.
2. **Gap/Regression Notes** — `agents/[name]/memory/evolution-[N]-gaps.md` (Phase 2 gap-targeted extraction) and `agents/[name]/memory/evolution-[N]-regression.md` (Phase 4 A/B comparison results), one pair per evolution cycle.

Full artifact map: see the `## Output Artifacts` table below.

## Quality Gate

Evolution is complete when:
- [ ] All drift scores improved or held (no regressions)
- [ ] A/B comparison shows improvement without identity loss
- [ ] Evolution log entry committed
- [ ] Next evolution triggers defined
- [ ] Agent file changes committed to version control

**Composite improvement ≥ 1 point = successful evolution.**
**Any dimension regression = investigate before shipping.**

---

## Output Artifacts

| Artifact | Location |
|---|---|
| Updated AGENT.md | `agents/[name]/AGENT.md` |
| Evolution log entry | `agents/[name]/memory/evolution-log.md` |
| Gap extraction notes | `agents/[name]/memory/evolution-[N]-gaps.md` |
| A/B comparison results | `agents/[name]/memory/evolution-[N]-regression.md` |
