# Launch Folder Manifest

*Navigation aid for understanding what's current, what's reference depth, and what's archived. Updated 2026-05-28 via /autopilot project hygiene mission.*

---

## How to read this manifest

Files and folders here fall into one of four tiers:

- 🟢 **ACTIVE** — Currently load-bearing. Andrea reads, Farrice ships from, or downstream prompts/workflows depend on.
- 🔵 **REFERENCE** — Detailed backup retained per density-over-completeness architecture. NOT outdated; serves the compressed Andrea-facing version. Don't archive.
- 🟡 **CANDIDATE** — Awaiting decision (variant pick, taste call). Becomes ACTIVE or ARCHIVED depending on outcome.
- ⚫ **ARCHIVED** — Preserved for provenance only. Do not use in production.

---

## 🟢 ACTIVE (the launch deliverables)

| Path | What it is | Last updated |
|---|---|---|
| `README.md` | Entry-point orchestrator. Hand Andrea the 3-doc reading list here. | 2026-05-28 |
| `04-gap-action-sprint.md` | 1-page weekly action sprint + 24-hour pre-event doctrine | 2026-05-28 |
| `05-andrea-decisions.md` | ≤2-page decision sheet for Andrea sign-off (3 decisions + status pulse) | 2026-05-28 |
| `design.md` | RESONANCE visual identity anchor. **Upload to any AI image generator as system reference.** | 2026-05-28 |
| `waitlist-landing-page.html` | Production landing page (940 lines) | 2026-05-28 |
| `01-announcement-package/README.md` | Phase 1/2/3 weekly content calendar — 17 entries across 3 phases, voice-audited | 2026-05-28 |
| `02-outreach-playbook/README.md` | Compressed Andrea-facing playbook (venue + JR outreach) | 2026-05-28 |
| `06-genspark-deployment/README.md` | 6-file Genspark prompt playbook orchestrator | 2026-05-28 |
| `06-genspark-deployment/00-capabilities-map.md` | Verified Genspark model catalog + routing matrix | 2026-05-28 |
| `06-genspark-deployment/01-image-to-video-prompts.md` | I2V prompts for Veo 3.1 / Kling 2.1 / Runway Gen-4.5 | 2026-05-28 |
| `06-genspark-deployment/02-social-media-prompt-pack.md` | Phase 1 IG carousel + Story + Substack Note prompts | 2026-05-28 |
| `06-genspark-deployment/03-announcement-content-pack.md` | Phase 2 Day 0 announcement deployment | 2026-05-28 |
| `06-genspark-deployment/04-waitlist-landing-pack.md` | Landing page hero video + og:image + email heroes | 2026-05-28 |
| `06-genspark-deployment/05-model-overrides.md` | Override prompts for Genspark Super Agent misrouting | 2026-05-28 |

---

## 🟡 CANDIDATE (awaiting decision)

| Path | What it is | Decision gate |
|---|---|---|
| `03-visual-variants/variant-b-hero-shots-v3/` | 7 PNG Soul-generated hero shots for Variant B (Latin-American Modernism) | Andrea picks B vs C |
| `03-visual-variants/variant-c-hero-shots-v3/` | 8 PNG Soul-generated hero shots for Variant C (Restrained Marble + Sage + Gold) | Andrea picks B vs C |
| `03-visual-variants/variant-a-hero-shots/`<br>`-v2/`<br>`-v3/` | Empty drop-zones for user-supplied reference images (Variant A direction now manual-reference-based, not AI-generated) | User drops in references |
| `03-visual-variants/variant-a-DESIGN.md` | DESIGN.md spec for Variant A (Editorial Broadsheet) | Stays as spec even if Variant A is not picked |
| `03-visual-variants/variant-b-DESIGN.md` | DESIGN.md spec for Variant B | Becomes canonical if Variant B wins |
| `03-visual-variants/variant-c-DESIGN.md` | DESIGN.md spec for Variant C | Becomes canonical if Variant C wins |
| `03-visual-variants/README.md` | Variant comparison + selection criteria | Updates after variant pick |
| `03-visual-variants/prompt-set-for-manual-deployment.md` + `.pdf` | Historical source for v3 hero generation (still operable for B/C if new shots needed) | Stays as reference until variant locked |

---

## 🔵 REFERENCE (detailed backup, NOT outdated)

These exist per the density-over-completeness architecture: Andrea-facing docs stay ≤2 pages compressed, internal versions retain full pedagogy.

| Path | What it is | Backed-up version of |
|---|---|---|
| `_README-v1-detailed.md` | Original verbose master index | Current `README.md` |
| `_04-gap-action-sprint-v1-detailed.md` | Full audit-must-haves analysis + 8 gaps detail | `04-gap-action-sprint.md` |
| `01-announcement-package/_v1-detailed.md` | Pre-compression version | `01-announcement-package/README.md` |
| `02-outreach-playbook/_v1-detailed.md` | 1,291-line full scaffolding (8-question filter, B.6 awkward conversations, C.5 negotiation talking points) | `02-outreach-playbook/README.md` |

**Rule**: Do not archive these. They serve the compressed README in case future editors need full context.

---

## ⚫ ARCHIVED (preserved for provenance only)

### Visual generation archive — `03-visual-variants/_archive/`

| Path | Contains | Why archived |
|---|---|---|
| `variant-a-rejected-2026-05-28/v1-fal-rated-0/` | 4 PNG | Wrong tool (Fal), 0/10 rating, MODE masthead leak |
| `variant-a-rejected-2026-05-28/v2-higgsfield-nanobanana-rated-2/` | 2 PNG | Two-body composition struggle, 2/10 |
| `variant-a-rejected-2026-05-28/v3-higgsfield-soul-rated-rejected/` | 8 PNG | Variant A direction rejected by Farrice (not the tool's fault — Soul produced workable output) |
| `variant-b-rejected-2026-05-28/v1-fal-rated-0/` | 4 PNG | Wrong tool, rejected |
| `variant-b-rejected-2026-05-28/v2-higgsfield-nanobanana-rated-2/` | 2 PNG | Composition struggle, rejected |
| `variant-c-rejected-2026-05-28/v1-fal-rated-0/` | 4 PNG | Wrong tool, rejected |
| `variant-c-rejected-2026-05-28/v2-higgsfield-nanobanana-rated-2/` | 2 PNG | Composition struggle, rejected |
| `stale-fal-scripts-2026-05-28/` | 3 files (`_generate-heroes.sh`, `_generate-heroes-continue.sh`, `_generation-log.txt`) | Fal pipeline retired; Soul + Genspark are current routes |

### Launch folder archive — `launch/_archive/`

| Path | Contains | Why archived |
|---|---|---|
| `2026-05-25-supercomputer-handoff/SESSION-HANDOFF.md` | Original /supercomputer + /autopilot mission handoff doc (May 25) | Work has moved past — replaced by current README + MANIFEST |

### Project root archive — `_archive/2026-05-28-cleanup/old-project-docs/`

| Path | Contains | Why archived |
|---|---|---|
| `PROJECT-SCHEMA.md` | April 2026 project setup schema | Superseded — project has evolved past initial schema |
| `README.md` | April 2026 project root README | Project moved to launch/-centric navigation |
| `v1.1-session-1-handoff.md` | May 11 session handoff | Historical |

---

## What was removed (not archived — just deleted)

- All `.DS_Store` files across the project (macOS junk, never useful)
- Empty `variant-b-hero-shots/`, `variant-b-hero-shots-v2/`, `variant-c-hero-shots/`, `variant-c-hero-shots-v2/` directories (folders only — files inside were archived, then empty folders removed since v3 is the active candidate for B and C)

---

## What was NOT touched (intentionally kept in place)

- `brand-operating-system/` — 47 files across 7 subfolders. Source of truth, all current. No cleanup needed.
- `RISKS.md` (project root) — current live risk tracker
- `CLAUDE.md` (project root) — project inheritance contract
- `state.yaml` (project root) — anchor registry

---

## Re-archiving rule

If new artifacts become outdated in future sessions:
1. Move to `launch/_archive/YYYY-MM-DD-<reason>/` or `03-visual-variants/_archive/YYYY-MM-DD-<reason>/`
2. Update this MANIFEST with the new entry
3. Update `state.yaml` anchor status to `ARCHIVED` with archive path
4. Update referencing docs (`README.md`, downstream packs) to reflect the change

Do not delete artifacts that contain creative work or have an output_ref in state.yaml. Always archive with provenance.

---

*See `launch/README.md` for the canonical Andrea-facing entry point. See `06-genspark-deployment/README.md` for the Genspark production playbook.*
