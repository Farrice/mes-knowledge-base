---
description: Audit and upgrade a skill collection's distribution maturity from copy-paste to versioned package registry
---

# Workflow 3 — Context Library Curation

Move a skill/agent/directive collection along Patrick's distribution maturity arc — **Copy-paste → Repo → Versioned Library → Registry → Marketplace** — with version pins, dependency declarations, security scans, and SBOMs. Predict each tier's failure modes before they hit.

## Pre-Flight Gate

Run this workflow when:
- Collection has 10+ artifacts
- Artifacts are shared (across projects, teammates, or organizations) — even self-sharing across multiple agent loops counts
- The user is hitting friction: "which version of this skill am I on?", "did this skill work last week?", "this skill broke after I edited a different one"

**Skip if**: Solo system <10 artifacts with no cross-skill stacking. Library overhead > collection value.

## Skill Acquisition

Load `skills/patrick-debois-cdlc/genius.md`. Anchor to:
- **Pattern 6** (Library → Registry → Marketplace arc) — the distribution maturity ladder
- **Pattern 7** (Honest skill-quality verdict — 99.9% is crap) — baseline classification rule
- **Hidden Knowledge** ("Skills will self-host") — predicts the private-registry trajectory
- **Pattern 8** (Sandbox-doesn't-solve-loading) — security scanning is required, not optional
- **Signature Move 5** ("Crap until proven otherwise") — applies to imported third-party skills

## Input Required

- **Target collection**: Path to skill/agent collection (e.g., `skills/`, `agents/`, third-party imported skills)
- **Current distribution tier** (from `/cdlc-audit` if run): copy-paste / repo / versioned-library / registry / marketplace
- **Cross-skill dependencies**: Which skills reference / load / stack with other skills (best-effort inventory)
- **Quality evidence available**: Are eval suites present (output of `/context-evals`)? Or zero eval coverage?
- **Distribution constraints**: Solo / team / org / public

## Execution

### Step 1: Tier Classification (Patrick's Maturity Arc)

For the collection, name the CURRENT distribution tier and the NEXT TARGET tier.

| Tier | Signature | Tooling Requirement |
|---|---|---|
| **0 — Slack/DM** | Copy-paste between conversations or chat windows | None. Lossy. |
| **1 — Repo** | Checked into git, accessible to anyone with repo access | git, README index |
| **2 — Versioned Library** | Each artifact has semver, breaking changes bumped | version field, CHANGELOG, version log |
| **3 — Registry** | Centralized index with discoverability + dependency resolution + security scanning | discoverability index, dependency resolver, security scanner, SBOM |
| **4 — Marketplace** | Public/semi-public registry with multiple authors + governance + ratings | governance, rating/review system, author identity |

**Rule**: Don't skip tiers. Tier 1 → Tier 3 fails because Tier 2 forcing functions (versioning discipline) aren't internalized.

### Step 2: Inventory + Honest Classification

For each artifact in the collection, classify quality (Patrick's "crap until proven otherwise" rule):

| Classification | Criterion |
|---|---|
| **A** | Has eval suite (`/context-evals` output) AND eval baseline meets all budgets |
| **B** | Has eval suite, baseline below budget on ≤30% of tests |
| **C** | No eval suite OR eval coverage <50% of artifact's contracts |
| **REVIEW** | Default for anything not yet classified |

**Anti-pattern reject**: If your distribution skews to A-tier without eval evidence, you're inflating. The 2026-04-24 Antigravity audit found 94-99% of finalize scores were 8+ — same inflation pattern. Default-A is theatre.

### Step 3: Version Scheme + Migration

For Tier 2 target, add semver to artifact frontmatter:

```yaml
---
name: skill-name
version: 1.4.2  # major.minor.patch
description: ...
---
```

**Bump rules** (Patrick-flavored, not strictly SemVer):
- **Major (X.0.0)**: Breaking workflow signature change (input format, output schema, removed workflows). Consumers MUST update.
- **Minor (X.Y.0)**: New workflow added, new optional input, expanded methodology. Backward compatible.
- **Patch (X.Y.Z)**: Content refinement, prompt rewording, example additions, no contract change.

**Migration path**:
1. Add `version: 1.0.0` to all existing artifacts (treat current state as v1.0.0).
2. Create `evolution_store/skill_versions.jsonl` log — each entry: `{date, artifact, from_version, to_version, diff_summary, breaking}`
3. Going forward, every artifact edit gets a version bump + jsonl log entry. Pre-commit hook can enforce.

### Step 4: Dependency Declarations

For each artifact that references another, add:

```yaml
---
name: skill-name
version: 2.1.0
depends_on:
  - lara-acosta-linkedin@>=1.5
  - mes-3.0-extract@^2.0
---
```

**Conflict prediction (Patrick's "dependency hell")**:
- Two artifacts depending on incompatible versions of a third = unresolvable load.
- Solution: dependency resolver (simple version: prefer most recent compatible; complex: graph solve).
- For Tier 2, manual resolution is acceptable. For Tier 3, build resolver.

### Step 5: Security Scanning (Tier 3 requirement)

Before any artifact loads, scan for:
- **Credential exposure**: API keys, tokens, passwords accidentally pasted into prompts
- **Prompt injection patterns**: Known jailbreak strings, payload-execution patterns
- **Untrusted external references**: URLs to non-allowlisted domains, file paths outside the workspace
- **Authorship metadata**: SBOM-style — who built this, with what model, when, with what eval status

Patrick's insight: **sandboxes don't solve loading** (Pattern 8). The scanner runs PRE-LOAD. Auto-loaded skills (in Antigravity, the routed skill) bypass any post-load defense.

**Implementation suggestion** (for Antigravity scale):
```bash
python3 execution/skill_security_scan.py --collection skills/ --report evolution_store/security_scans/$(date +%Y-%m-%d).json
```
Author this script as part of Tier 3 upgrade.

### Step 6: AI SBOM (Software Bill of Materials, AI-flavored)

For each artifact, capture:

```yaml
sbom:
  authored_by: "Farrice via /extract-forge"
  authored_with: "claude-opus-4-7[1m]"
  authored_at: "2026-05-03"
  source_attribution: "Patrick Debois — AI Engineering Summit keynote"
  source_url: "https://www.youtube.com/watch?v=bSG9wUYaHWU"
  eval_suite: "evolution_store/eval_suites/patrick-debois-cdlc/"
  eval_baseline_date: "2026-05-03"
  security_scan_date: "2026-05-03"
  security_scan_status: "clean"
```

**Why this matters**: When something goes wrong, you need to trace which model authored which prompt with what evidence. SBOM IS that trace.

### Step 7: Discoverability Upgrade

Tier 3 requires that artifacts be findable beyond grep:

- **Tagged index**: Domain tags (content / brand / strategy / extraction / etc.) per artifact
- **Stacking graph**: Which artifacts pair well — explicit edges in a graph
- **Search affordance**: A query interface beyond `grep -r`. (For Antigravity, `recommend` + `find-context` skills already provide this.)
- **Quality surface**: Eval baseline + version + classification visible at the index level, not buried in artifact files

### Step 8: Migration Plan + Effort Estimate

Produce concrete migration steps from current tier to target tier:

| Step | Effort | Output |
|---|---|---|
| 1. Inventory + classification | (hours/days) | Spreadsheet/JSONL of all artifacts with A/B/C/REVIEW |
| 2. Add version: 1.0.0 frontmatter to all | (hours) | All artifacts versioned at v1.0.0 baseline |
| 3. Author skill_versions.jsonl + git pre-commit hook | (hours) | Version bumps logged automatically |
| 4. Add depends_on declarations to top-N artifacts (those referenced by others) | (hours/days) | Cross-skill graph explicit |
| 5. Author skill_security_scan.py | (days) | Scanner running on every commit |
| 6. Add SBOM frontmatter to all artifacts | (days) | SBOM coverage = 100% |
| 7. Author tagged index + stacking graph | (days) | Tier 3 discoverability |

## Content Type Adaptations

| If collection is... | Emphasize | De-emphasize |
|---|---|---|
| Solo personal library | Versioning + SBOM (forgettability is the enemy) | Security scanning (you are the only author) |
| Team library | Versioning + dependency declarations + classification | Marketplace governance |
| Org platform | Full Tier 3: versioning + deps + scanner + SBOM + discoverability | Tier 4 unless you're actually open-sourcing |
| Imported third-party skills | Aggressive scanning + classification (default REVIEW) + sandboxing | Versioning if upstream doesn't version (just freeze the snapshot) |

## Output Schema

```markdown
# Context Library Curation — [Collection Name]

## Current State
- **Tier**: [0-4 with evidence]
- **Artifact count**: X total / Y eval'd / Z classified
- **Cross-references**: [count of skill→skill stacking calls]
- **Security**: [scanned / never scanned / manual review only]

## Target State
- **Target tier**: [next tier up — never skip]
- **Why this tier**: [forcing function this tier provides — versioning discipline / dependency resolution / security gate]

## Inventory + Classification

| Artifact | Current Tier | Classification | Has Eval | Has SBOM | Notes |
|---|---|---|---|---|---|
| skill-A | repo | REVIEW | N | N | (1-line) |
| skill-B | repo | C | N | N | (1-line) |
| skill-C | versioned (1.2.0) | A | Y | Y | (1-line) |
[full list]

**Distribution sanity check**: [does the A/B/C/REVIEW distribution skew to A without eval evidence? If yes, name the inflation.]

## Migration Plan

### Phase 1 — Versioning (Tier N → Tier N+0.5)
- [ ] [specific step with effort estimate]
- [ ] [specific step]
- [ ] [specific step]

### Phase 2 — Dependencies (Tier N+0.5 → Tier N+0.75)
- [ ] [specific step]
- [ ] [specific step]

### Phase 3 — Security + SBOM + Discoverability (Tier N+0.75 → Tier N+1)
- [ ] [specific step]
- [ ] [specific step]

## Predicted Failure Modes (Patrick's Foresight)

| Failure Mode | Will Hit At Tier | Mitigation |
|---|---|---|
| Version drift across consumers | Tier 2 | Pre-commit hook enforces version bump |
| Dependency hell (incompatible deps) | Tier 2-3 | Dependency resolver before resolver becomes unresolvable |
| Untrusted skill auto-load | Tier 3 | Pre-load security scanner + context filter |
| SBOM rot (stale eval baselines) | Tier 3 | Re-baseline triggered by model upgrade or 90-day staleness |
| Marketplace quality dilution (99.9% crap) | Tier 4 | Default REVIEW classification + eval-evidence gate before A-tier |

## 90-Day Success Metric
After migration to target tier, [specific measurable outcome — e.g., "all version bumps logged with diff summary; cross-skill dependency graph navigable; security scan runs in <10s on full collection"].
```

## Example Output (Antigravity-applied excerpt)

**Context**: Curating Antigravity's `skills/` collection (210 skills), currently Tier 1 (repo), target Tier 2 (versioned library).

**THE DELIVERABLE (excerpt — Inventory + Migration Plan):**

```markdown
## Current State
- **Tier**: 1 (repo) with partial Tier 2 readiness — SKILL.md frontmatter has `version: "2.0"` but it's a FORMAT version (completion-engine), not a semantic version per skill
- **Artifact count**: 210 skills / 16 with ground-truth benchmarks / 0 with full eval suites
- **Cross-references**: ~80 cross-skill stacking calls (rough grep count)
- **Security**: Never scanned. Manual review by Farrice when extracting from third-party sources. Imported third-party skills: 0 (all skills authored in-system).

## Target State
- **Target tier**: 2 (versioned library)
- **Why this tier**: Forcing function = version-bump discipline. Currently, when Farrice edits a skill, dependent skills don't know they're consuming a different version. This causes silent regressions (a skill calling another skill's pattern that was renamed).

## Inventory + Classification (top-20 by usage)

| Artifact | Current Tier | Classification | Has Eval | Has SBOM | Notes |
|---|---|---|---|---|---|
| lara-acosta-linkedin | repo | B | Partial (16 benchmarks across all skills) | N | High usage; needs full eval suite |
| mes-3.0-extract (directive) | repo | REVIEW | N | N | Foundational — load-bearing for all extractions |
| writers-room | repo | B | Partial | N | Recently calibrated post-2/10 LinkedIn fail |
| /extract-forge | repo | REVIEW | N | N | Just shipped 2026-05-03 with gate-first feedback |
| ... | ... | ... | ... | ... | ... |

**Distribution sanity check**: 0 skills classified A. 90%+ classified REVIEW. **This is the honest baseline** — Patrick's "crap until proven otherwise" applied to the system itself. The 2026-04-24 audit predicted exactly this.

## Migration Plan

### Phase 1 — Versioning
- [ ] Add `skill_version: 1.0.0` to all 210 SKILL.md files (treat current state as v1.0.0). 1 sprint.
- [ ] Author `evolution_store/skill_versions.jsonl` + write entry per skill: `{date: 2026-05-03, artifact: <name>, version: 1.0.0, baseline: true}`. 1 day.
- [ ] Add git pre-commit hook: any change to skills/X/* requires bumping skill_version in that skill's SKILL.md AND appending a row to skill_versions.jsonl. 1-2 days.
- [ ] Add `python3 execution/skill_versions.py status` reporter — shows skills modified without version bump in last commit. 1 day.

### Phase 2 — Dependencies
- [ ] Audit cross-skill stacking — grep for "stacks with" / "load skills/" / "see skills/" / etc. Build initial dependency graph (~80 edges). 2-3 days.
- [ ] Add `depends_on: [skill-name@>=X.Y]` frontmatter to top-50 skills (those most depended-on). 2 days.
- [ ] Add dependency resolver to `chain_runner.py` — when loading skill A that depends on B@>=1.5, refuse load if B is at 1.4. 2 days.

### Phase 3 — Security + SBOM + Discoverability
- [ ] Defer to a future sprint. Antigravity is solo with no third-party imports — security scanner is overkill until Antigravity ships skills externally.
- [ ] Add minimal SBOM frontmatter to skills (authored_with model, authored_at date, source_attribution if extracted from external). 2 days for top-20 skills.
- [ ] Discoverability is already strong via `/recommend`, `/find-context`, AGENT_INDEX, SKILL_INDEX. No upgrade needed at this tier.

## Predicted Failure Modes

| Failure Mode | Will Hit At Tier | Mitigation |
|---|---|---|
| Version bump skipped on edit | Tier 2 (during Phase 1) | Pre-commit hook (Phase 1 step) |
| Dependency declared on a version that doesn't exist | Tier 2 | Resolver checks declared deps against skill_versions.jsonl |
| SBOM rot (skills extracted in 2026-02 still claim Opus 4.6 authorship after re-edit) | Tier 2.5 | SBOM auto-update on re-edit (defer to Phase 3) |
| Cross-skill loop (A depends on B depends on A) | Tier 2 | Resolver detects cycles (cheap to add) |

## 90-Day Success Metric
By 2026-08-03: All 210 skills carry `skill_version` semver; `skill_versions.jsonl` has ≥1 entry per skill; pre-commit hook fires on every skill-touching commit; top-50 skills have `depends_on` declarations; cross-skill dependency graph is navigable via `python3 execution/skill_dependencies.py graph`.
```

**What elevates this**:
- Forces the Tier-1 → Tier-2 step instead of leaping to Tier-3 (Patrick's "don't skip tiers" rule)
- Honest classification: 0 A-tier skills, 90%+ REVIEW. Refuses inflation.
- Migration plan is concrete steps with effort + tooling, not "implement versioning"
- Predicted failure modes named upfront (Patrick's foresight pattern) — mitigations baked into the plan
- Phase 3 explicitly *deferred* with justification ("Antigravity is solo with no third-party imports") — demonstrates judgment, not box-checking
- Surfaces an existing tension: SKILL.md `version: "2.0"` is a FORMAT version, not a SemVer per skill. Renaming to `skill_version` avoids collision.

## Quality Gate

Before delivering, verify:
- [ ] Current tier and target tier named (no skipping)
- [ ] Inventory has honest classification distribution (A-tier requires eval evidence — if 90% A-tier without evals, you inflated)
- [ ] Migration plan is steps with effort estimates, not abstractions
- [ ] Predicted failure modes match Patrick's known patterns (dep hell, version drift, SBOM rot, marketplace dilution)
- [ ] Mitigations are concrete tools/hooks, not "be careful"
- [ ] If target system is solo, Tier-4 work is explicitly deferred (don't author marketplace governance for solo)
- [ ] If target system has imported third-party artifacts, security scanning is in scope (not deferrable)

## Stacks With

- **`/cdlc-audit`** (Workflow 1) — Audit tells you the Distribute-stage score; this workflow plans the upgrade
- **`/context-evals`** (Workflow 2) — Eval suites feed the A/B/C classification rule
- **`skill_auditor.py`** — A/B/C/REVIEW classification can plug directly into this script's tier logic
- **Antigravity `evolution_orchestrator.py`** — Phase 4 gap analysis can include skill_versions.jsonl drift detection
