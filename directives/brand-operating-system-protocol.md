# Brand Operating System (BOS) Protocol

Governance for `skills/brand-operating-system/`, `.agent/workflows/build-bos.md`, and `templates/brand-operating-system-v1/`.

The BOS skill exists to produce 6-layer brand systems at the Resonance quality bar — every time, for any brand. This directive locks the discipline that prevents drift between the template, the skill, the workflow, and the live reference implementation (Resonance for Andrea).

---

## The 4 Components and What They Do

| Component | What it is | Source of truth for |
|---|---|---|
| `skills/brand-operating-system/` | The skill (SKILL.md + genius.md + 7 workflow files) | The build sequence, agent/skill invocation order, quality gates |
| `.agent/workflows/build-bos.md` | The slash command entry point | Argument parsing, phase orchestration, top-level routing |
| `templates/brand-operating-system-v1/` | The 47-file template scaffold | The structural skeleton + identity tokens |
| `projects/andrea-dj/brand-operating-system/` | The live reference implementation (Resonance v1) | The proof it works end-to-end at the bar we want |

These four components must stay in lockstep. Drift between any two breaks the system.

---

## Amendment Discipline

### When the template amends

Triggered by: a worked-example improvement, a new universal token, a structural pattern that proved itself in a build.

**Required actions:**
1. Update `templates/brand-operating-system-v1/<file>` directly.
2. Update `templates/brand-operating-system-v1/TOKENS.md` if the change adds/renames a token.
3. **Back-apply to Resonance** — `projects/andrea-dj/brand-operating-system/<file>` gets the same change. Otherwise template + reference diverge.
4. If the change affects the structural skeleton (new section, reordered sections, new file), bump skill version (v1 → v2) and document in `skills/brand-operating-system/CHANGELOG.md`.
5. If back-application to Resonance is intentionally skipped (e.g., Resonance has a unique constraint), note the divergence in `projects/andrea-dj/brand-operating-system/05-ops/01-change-log.md` AND in this directive's "Known Divergences" section below.

### When Resonance amends (founder-driven)

Triggered by: Andrea names an amendment per Constitution principle ("amend, don't rewrite").

**Required actions:**
1. Update `projects/andrea-dj/brand-operating-system/<file>` per `05-ops/00-update-protocol.md`.
2. Re-render to Drive (`md_to_gdoc.py` overwrites or updates the corresponding native Google Doc).
3. **Evaluate template back-application**: is this a Resonance-specific tweak or a universal pattern? If universal, back-apply to `templates/brand-operating-system-v1/<file>`. If Resonance-specific, log under "Known Divergences."
4. Log in `projects/andrea-dj/brand-operating-system/05-ops/01-change-log.md`.

### When the skill amends

Triggered by: a new agent/skill becomes available and improves a phase, a quality gate gets sharpened, a phase order changes.

**Required actions:**
1. Update the relevant `skills/brand-operating-system/workflows/0N-*.md` file.
2. Update `skills/brand-operating-system/SKILL.md` if the input/output contract changes.
3. Update `.agent/workflows/build-bos.md` if the slash command's args or top-level orchestration changes.
4. Update `execution/routing_enforcer.py` BINDINGS if a new mandatory binding appears.
5. **Run a regression build** — invoke `/build-bos` against a stub anchor doc, confirm 43 files generate cleanly, confirm Phase G quality gates pass.

---

## Versioning

**Major version (v1 → v2)**: Structural skeleton change. New layer, new section in the master creative brief template, new ops protocol, removed file. Forces re-scaffold for any new BOS.

**Minor version (v1.0 → v1.1)**: Identity token addition, content-block guidance refinement, agent invocation swap (e.g., upgrading from `master-copywriter` to a newer agent for the same job). Existing BOSes remain compatible.

**Patch version (v1.1.0 → v1.1.1)**: Typo fixes, link corrections, doc clarifications.

Track in:
- Skill changelog: `skills/brand-operating-system/CHANGELOG.md`
- Live BOS changelogs: each `projects/<client>/brand-operating-system/05-ops/01-change-log.md`

---

## Known Divergences (Template ↔ Resonance)

This section logs any intentional differences between `templates/brand-operating-system-v1/` and `projects/andrea-dj/brand-operating-system/`. Empty at v1 ship.

| Date | File | Divergence | Reason |
|---|---|---|---|
| _(none at v1.0 ship)_ | | | |

If this section grows past 5 entries, the template needs a v2 to absorb the differences — divergence is a smell.

---

## Ship Bar (Non-Negotiable Quality Gates)

A BOS ships when:

1. **All 43 docs exist.** No partial deliveries. If a phase failed, halt the build, fix, resume. Don't ship at 35/43.
2. **Phase G1 adversarial review composite ≥7/10.** Each axis ≥6. CRITICAL fixes resolved inline; HIGH/MEDIUM may ship as v1.1 backlog.
3. **Phase G2 prose-doctor 0 banned-move violations.** ≤2 em-dash violations across the entire BOS. Anything more = re-run prose-doctor with edits.
4. **Phase G4 chain finalize composite ≥7.** Each of 4 dimensions ≥6 (Intent / Expert Standard / Adversarial / Factual Grounding).
5. **If `--drive-parent` supplied: 43/43 native Google Docs in pageless format.** Zero raw .docx remaining. (Per `feedback_google-docs-pageless.md`.)
6. **Cold-start test passes.** Pasting `04-ai-handoff/00-ai-brain-master.md` into a fresh Claude session and asking for an asset returns on-brand output without re-prompting.

If any gate fails, halt. The cost of holding ship is hours; the cost of shipping a degraded BOS is the founder/client losing trust in the system.

---

## Anti-Patterns (Routing Enforcer Halts)

These are mirrored in `execution/routing_enforcer.py BINDINGS`:

1. Building a BOS via `agents/brand-system-builder/` direct invocation → halt. Use `/build-bos`.
2. Skipping Phase A (synthesis pass) because "we know the brand" → halt. Phase A surfaces compounding conflicts.
3. Skipping Phase G (adversarial + prose) because "the docs look good" → halt. Resonance had a CRITICAL file-numbering bug that survived 6 human reviews and only G1 caught it.
4. Manually rendering to .docx + dragging to Drive instead of `md_to_gdoc.py --mirror-folders` → halt per pageless rule.
5. Authoring custom 4-layer or 8-layer variants at runtime → halt. If a brand needs a different shape, bump skill version and update the template.

---

## Working with `_working/` Artifacts

`_working/` holds A1 reconciliation, A3 discovery, G1 adversarial review, G2 prose scan. These are scaffolding artifacts.

**Rules:**
- DO NOT deliver to clients. The directory is excluded from `md_to_gdoc.py --mirror-folders` by default.
- DO NOT version-control client-specific `_working/` artifacts beyond the project repo. They contain raw decision logs.
- DO read `_working/A1-reconciliation.md` before starting v1.1 amendments — it shows what conflicts were resolved and why.
- DO use `_working/G1-adversarial-review.md` as input to v1.1 G1' (each adversarial review compounds on the prior).

---

## Reference: When to Use This Skill

```
/build-bos --name "<Brand>" --source <doc> --output <path>          # canonical-doc mode
/build-bos --name "<Brand>" --discovery --output <path>             # interview mode
/build-bos --name "<Brand>" --source <doc> --output <path> \
           --drive-parent <id>                                       # + auto-Drive
```

Use this skill when the scope includes ALL of: foundation (spine/voice/ICP) AND production (briefs/marketing) AND AI handoff AND ops. For single-layer scopes, use the component skill (`design-md`, `voice-document`, `icp-deep-dive`, etc.) directly.

---

## Source of Truth Hierarchy (When in Doubt)

1. **Resonance live reference** — wins on what works in practice
2. **`directives/brand-operating-system-protocol.md`** (this file) — wins on governance
3. **`skills/brand-operating-system/SKILL.md`** — wins on skill contract
4. **`templates/brand-operating-system-v1/`** — wins on structural skeleton
5. **`.agent/workflows/build-bos.md`** — wins on orchestration
6. **`execution/bos_scaffold.py` + `execution/md_to_gdoc.py --mirror-folders`** — win on mechanics

If two sources conflict, walk up this hierarchy. If conflict persists at level 1 (Resonance), surface to user — do not silently resolve.
