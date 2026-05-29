# Workflow Gate Convention

> **Trigger**: Any new or revised system-tier workflow (multi-phase orchestration). Loaded by Skill Architecture — Atoms vs Systems (CLAUDE.md).
> **Distinct from**: `directives/quality_gate.md` (post-execution 4-dim scoring). This doc is about MID-execution halt/proceed gates between phases.
> **Source**: 2026-05-12 integration brief, Phase C Move 4 (`_active/system-integration/2026-05-12-agentic-os-elevation-brief.md`).

---

## The Convention

A **workflow gate** is a phase boundary where the workflow stops, surfaces a structured halt/proceed question to the user, and refuses to proceed without explicit approval. Gates exist to prevent end-to-end execution on bad inputs — the Parallax Edition 02 failure mode (7 fabrications shipped because there was no gate between research and drafting).

### What Counts as a Gate

A gate is **NOT** just a phase boundary or a status update. It must have:

1. **A specific halt question** — not "should I continue?" but "did Phase 2's claims pass verification? If yes, list which 3 claims you most want to verify before drafting."
2. **A two-path output** — explicit conditions for PROCEED vs HALT, named upfront before the user answers
3. **A halt rationale** — why halting here is cheaper than rolling back later (e.g., "drafting on unverified claims costs 2 hours of rewrite if anything is wrong")
4. **A skip flag** — explicit override syntax (`--no-ground`, `--skip-gate-X`, etc.) for cases where the gate is genuinely not load-bearing

Anti-pattern: rubber-stamp gates ("Looks good, proceed?") with no structured halt path. These train Claude and the user to auto-click yes, defeating the gate.

### When a Workflow MUST Have a Gate

| Condition | Gate required |
|-----------|--------------|
| Production-from-scratch (research → draft → publish) | Before drafting phase (Parallax 2.5 is the model) |
| Multi-expert ensemble producing client deliverable | Before synthesis layer fires |
| Code change touching deterministic backstops (chain_runner, hooks, routing_enforcer) | Before commit |
| Public-facing output (Substack, LinkedIn, press) | Before publish action |
| Client work where voice/positioning is contested | Before locked-in copy decisions |
| Extraction from source flagged as marginal by gate-first rule | After source acquisition, before forge phases |

### When a Gate Is Optional

- Refinement-on-existing workflows (writers-room when input draft already exists — implicit gate is "this is the draft, refine it")
- Single-deliverable atom workflows (no phases to gate between)
- Parallel-by-design workflows (parallel-content, parallel-extract — synthesis layer is the gate)
- Internal tooling outputs (system audits, performance reports — user reads, no downstream action)

---

## Gate Structure Template

Every gate phase in a workflow file should follow this structure:

```markdown
### Phase N.M — [Gate Name]

**Halt question:** [Structured question that surfaces what could go wrong]

**Halt conditions (PROCEED requires all):**
- [ ] [Specific test 1]
- [ ] [Specific test 2]
- [ ] [Specific test 3]

**If any halt condition fails:** [What to do — re-research, re-verify, re-prompt, escalate to user]

**Skip syntax:** `--skip-[gate-name]` — only valid when [specific condition that makes this gate non-load-bearing]

**Why this gate exists:** [One sentence — the failure mode this prevents, citing the incident or risk if known]
```

---

## Worked Example: Parallax Phase 2.5 (The Gold Standard)

```markdown
### Phase 2.5 — Ground + Zeitgeist Check (NON-OPTIONAL for Editions 02+)

**Halt question:** Does this raw take rest on factual claims that, if wrong, would mean the entire edition's premise collapses?

**Halt conditions (PROCEED requires all):**
- [ ] Claim extraction complete (every factual claim in raw take inventoried)
- [ ] Budget-tiered verification done (Recall first; Perplexity for unverifiable in Recall)
- [ ] Zeitgeist scan complete (is the claimed cultural moment current and accurate?)
- [ ] Halt/proceed verdict explicit — VERIFIED / LIKELY / UNCONFIRMED labels per claim

**If any halt condition fails:** Pause drafting. Re-research the failing claim. If unverifiable, mark UNCONFIRMED and either (a) cut the claim, (b) rewrite to caveat, (c) escalate to user.

**Skip syntax:** `--no-ground` — only valid when edition has zero external factual surface (pure memoir, no public figures, no events, no brands, no stats).

**Why this gate exists:** Parallax Edition 02 shipped with 7 fabrications (Madeon as unknown DJ, wrong day, invented distance, song-age math). All slipped past mechanical audits because there was no claim-by-claim verification between raw take and draft. Drafting on unverified claims costs 2 hours of rewrite minimum if anything is wrong.
```

Full implementation: `.agent/workflows/parallax.md` Phase 2.5.

---

## Auditing Existing Workflows

When updating or creating a system-tier workflow, run this check:

```bash
# Quick audit
grep -ci "halt\|proceed\|gate\|checkpoint\|approval" .agent/workflows/<name>.md
```

Audit results (2026-05-12 baseline):

| Workflow | Gate-keyword mentions | Status |
|----------|----------------------|--------|
| `parallax` | 17 | ✅ Well-gated (Phase 2.5 is the gold standard) |
| `extract-forge` | 6 | ✅ Has 3 checkpoints |
| `big-project` | 5 | ✅ Structured around gates |
| `parallel-content` | 2 | 🟡 Light coverage |
| `proof-pipeline` | 1 | 🟡 Light coverage |
| `campaign` | 1 | 🟡 Light coverage |
| `jcc-deploy` | 1 | 🟡 Light coverage |
| `writers-room` | 0 | 🔴 No explicit gates — worked-example fix shipped 2026-05-12 |
| `content-bundle` | 0 | 🔴 No explicit gates |
| `brief` | 0 | 🔴 No explicit gates |

Heuristic: a system-tier workflow with `< 3 gate-keyword mentions` likely lacks explicit gates. Read it, check, add per template above.

---

## Anti-Patterns

- ❌ **Gate inflation**: 5+ gates in a single workflow. Cap at 2-3 high-stakes phase boundaries; otherwise gates feel bureaucratic and get skipped.
- ❌ **Rubber-stamp gates**: "Looks good, proceed?" with no structured halt path. Worse than no gate — trains habit of clicking through.
- ❌ **Gate-then-ignore**: Workflow surfaces a gate question, user approves, workflow doesn't actually halt the chain on a no-answer. Make the halt structural, not advisory.
- ❌ **Conflating with quality_gate**: Workflow gates are mid-execution halt/proceed. Quality gate is post-execution 4-dim scoring. Don't merge the docs.

---

## Cross-References

- Gold-standard implementation: `.agent/workflows/parallax.md` Phase 2.5
- Worked example (added 2026-05-12): `.agent/workflows/writers-room.md` diagnosis gate
- Quality scoring (different concept): `directives/quality_gate.md`
- Source brief: `_active/system-integration/2026-05-12-agentic-os-elevation-brief.md` Move 4

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Created** | 2026-05-12 |
| **Last Activated** | Not yet activated (new directive) |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-06-12 |
