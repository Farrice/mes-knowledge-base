# Phase A — Discovery

**Duration**: ~half-day. Required before any foundation work.

## Required inputs

One of:
- `--source <path>` — pre-existing canonical doc(s). Andrea's case: Internal Anchor + Manifesto v2.
- `--discovery` — no prior docs; run founder interview to manufacture canonical inputs first.

Plus brand identity tokens (BRAND_NAME, FOUNDER_NAME, etc.) for scaffold.

## Steps

### A0 — Archive canonical inputs

If `--source <path>`:
```bash
# Copy each source doc into _source/
cp <path>/*.md <output>/_source/
```

If `--discovery`:
1. Run a structured founder interview — 8 dimensions:
   - The point (one sentence)
   - The person (out-loud-asking signal)
   - Non-negotiables (what cannot bend)
   - Success at first cycle (specific, measurable)
   - Success at 5 years (vision)
   - Kill conditions (when to walk)
   - Drift signals (early warnings of failure)
   - Founding story (why this, why now, why you)
2. Synthesize answers into a "Founder Anchor v0" document. Save to `_source/founder-anchor-v0.md`.
3. **Halt** for founder review before proceeding. Do not silently consume.

### A1 — Reconciliation pass

Invoke `agents/synthesis-engine/`:

> Reconcile the canonical inputs against any prior brand framing (e.g., earlier strategy briefs, prior research). Where they conflict, founder docs win. Where they agree, prior docs supply depth.

Output: `_working/A1-reconciliation.md` — conflict table, spine resolution, canonical phrasings to lock.

### A2 — ICP master

Invoke `agents/icp-deep-canvasser/` + `skills/icp-deep-dive/`:

> Produce the ICP Master from canonical inputs. Three layers:
> 1. Umbrella description (the broad audience signal)
> 2. Profile #1 LOCKED (filled from canonical)
> 3. Profile #2 + #3 PROPOSED (drafted; flagged for founder adjudication)
>
> Each profile gets: demographic, psychographic, language map (avoid/use words), Bridge Message (the single sentence that lets reader cross from current state to next), audience-state mapping (pre-contemplation / contemplation / preparation / action).

Output: early draft of `00-foundation/02-icp-master.md`.

### A3 — AI Brain discovery diagnostic

Run `/ai-brain-discovery` (skill: `skills/ai-brain-discovery/`):

> 8-dimension diagnostic on the brand. Surfaces gaps the human eye misses — voice patterns not yet named, ICP states not yet mapped, mechanic vs metaphor confusion, etc.

Output: `_working/A3-discovery.md` — gap list with severity flags.

## Output Schema

**Inputs**: 
- Canonical docs (from `--source <path>` OR `--discovery` founder interview) 
- Brand identity tokens (BRAND_NAME, FOUNDER_NAME, etc.)

**Outputs**:
- `_source/*.md` — Archived canonical input(s)
- `_working/A1-reconciliation.md` — Conflict resolution table, spine resolution, canonical phrasings to lock
- `_working/A3-discovery.md` — 8-dimension diagnostic (voice gaps, ICP gaps, mechanic vs metaphor confusion, etc.) with severity flags
- `00-foundation/02-icp-master.md` — Early draft ICP Master (umbrella description + ≥1 LOCKED profile + ≥2 PROPOSED profiles)

**Each profile includes**: Demographic, psychographic, language map (avoid/use words), Bridge Message (1 sentence), audience-state mapping (pre-contemplation / contemplation / preparation / action).

**Purpose**: Establish canonical inputs, resolve upstream conflicts, surface gaps, and lock the ICP umbrella + primary profile before Foundation phase.

**Quality Gate Checkpoint**: 
- [ ] `_source/` has ≥1 canonical doc
- [ ] `_working/A1-reconciliation.md` exists and resolves all conflicts (no UNRESOLVED flags)
- [ ] `00-foundation/02-icp-master.md` early draft has umbrella + ≥1 LOCKED profile
- [ ] `_working/A3-discovery.md` exists with gap list (gaps OK; missing diagnostic NOT OK)
- [ ] Founder has reviewed PROPOSED ICP profiles (or accepted PROPOSED status to proceed in parallel)

If any unchecked, halt and resolve. Do not advance to Phase B with unresolved conflicts — they compound.

---

## Quality gate (Phase A → B)

Before advancing to Phase B:
- [ ] `_source/` has ≥1 canonical doc
- [ ] `_working/A1-reconciliation.md` exists and resolves all conflicts (no UNRESOLVED flags)
- [ ] `00-foundation/02-icp-master.md` early draft has umbrella + ≥1 LOCKED profile
- [ ] `_working/A3-discovery.md` exists with gap list (gaps OK; missing diagnostic NOT OK)
- [ ] Founder has reviewed PROPOSED ICP profiles (or accepted PROPOSED status to proceed in parallel)

If any unchecked, halt and resolve. Do not advance to Phase B with unresolved conflicts — they compound.
