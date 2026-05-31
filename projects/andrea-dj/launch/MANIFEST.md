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
- `download.html` (root-level empty file, 0 bytes)

---

## Project-Wide Folder Map (added 2026-05-28 — full project clarity)

The launch/ folder is the production surface, but the project has 5 other root folders. Here's what each is and its tier:

### `brand-operating-system/` 🟢 ACTIVE — source of truth

47 files across 7 subfolders. The canonical brand operating system. All current. **Untouched in cleanup.**

| Subfolder | What it owns |
|---|---|
| `00-foundation/` | Master index, brand bible, ICP master, voice document, positioning, 12 Non-Negotiables |
| `01-visual/` | DESIGN.md, aesthetic refs, brand library, component tokens, photography rules |
| `02-briefs/` | 10 creative brief templates (IG feed/reel/story, flyer, email, press, venue pitch, etc.) |
| `03-marketing/` | Funnel, curation mechanics, awareness ladder, etc. |
| `04-ai-handoff/` | AI brain master, image-prompt formulas, paste-in blocks for AI sessions |
| `05-ops/` | Run-of-show, change log, update protocol, drift signals |
| `_working/` | A1-reconciliation + ongoing reconciliation work |

### `source/` 🟢 ACTIVE — canonical voice source (Andrea's actual writing)

3 files. **Critical — referenced extensively from BOS. Never archive.**

| File | What it is | Referenced by |
|---|---|---|
| `andrea-internal-anchor.md` (Apr 29 2026) | Andrea's private decision doc — the room's operating system | brand-bible, icp-master, brand-library |
| `andrea-manifesto-v2.md` (May 4 2026) | Andrea's public-facing manifesto — polished voice register | brand-bible, ig-feed-post, brand-library |
| `andrea-story-2026-05-11.md` (May 11 2026) | Andrea's founder-origin narrative — interior + conversational register | brand-bible §5 (canonical) |

### `research/` 🔵 REFERENCE — foundational research (don't archive)

6 files from April 9, 2026. Where the project started. **Actively cited from BOS.**

| File | What it is | Status |
|---|---|---|
| `00-START-HERE.md` | Original project orientation | Historical onramp |
| `01-market-research.md` | Initial Chicago singles-event market scan | Foundational |
| `02-brand-naming.md` | How "Resonance" was chosen | Historical record |
| `03-event-blueprint.md` | 8-phase in-room experience arc | **Cited by BOS funnel + run-of-show** (note: written in evening voice, needs daytime port — flagged in BOS) |
| `04-instagram-strategy.md` | Original IG strategy | Pre-launch package, partially superseded |
| `05-venue-and-pricing.md` | Venue type research + pricing ranges | **Cited by BOS venue-pitch** (note: evening voice, rates port; framing needs rewrite) |

### `deliverables/` 🔵 REFERENCE — Monday Package lineage source (don't archive)

1 active subfolder. **Critical lineage. BOS was built from this. Cannot archive.**

| Path | What it is | Why kept |
|---|---|---|
| `deliverables/2026-04-11-monday-package/` | First major delivery (Apr 11, 2026) — Pulse brand identity, archetype work, working method, 8-week timeline | BOS cites this in ≥12 places: Maya/Simone/Darius archetypes (icp-master), Scripts 1-4 (curation-mechanics), working method (update-protocol), change-log historical record |

### `pre-launch/` 🟢 ACTIVE (4 docs) — operational reference for current launch

After cleanup: only the 4 actively-referenced docs remain.

| File | Referenced by | Status |
|---|---|---|
| `02-male-acquisition-strategy.md` | `brand-operating-system/00-foundation/02-icp-master.md` (Path B avatar split) | 🟢 Active |
| `05-photoshoot-brief.md` | `launch/_04-gap-action-sprint-v1-detailed.md` (Andrea's pre-launch portrait) | 🟢 Active — needed for portrait booking this week |
| `07-anti-omission-audit.md` | `launch/04-gap-action-sprint.md` (the 42-item audit) | 🟢 Active — Andrea reads weekly |
| `08-andrea-event-role-doctrine.md` | `launch/_04-gap-action-sprint-v1-detailed.md` (item #11 day-of role) | 🟢 Active — event-day doctrine |

### `notes/` ⚪ EMPTY — placeholder with `.gitkeep`

Trivial. Kept as-is for git tracking. Use if you want ad-hoc project notes outside the launch/ structure.

---

## Newly archived in this cleanup (2026-05-28 round 2)

### `_archive/2026-05-28-cleanup/stale-bos-v1-docx-exports/`
- `2026-05-04-brand-operating-system-v1/` (full subtree of `.docx` files)
- **Why archived**: These are the May 4 client-delivery Word exports of the BOS. The live BOS at `brand-operating-system/` is in Markdown and has evolved since May 4. The `.docx` exports are stale. **Restore + regenerate from current BOS** if Andrea ever needs Word format again.

### `_archive/2026-05-28-cleanup/pre-launch-superseded-by-launch-package/`
10 orphan files + `_enrichment/` subdir — all superseded by the current launch package (`01-announcement-package/`, `02-outreach-playbook/`, `04-gap-action-sprint.md`, `06-genspark-deployment/`):

| Archived file | Superseded by |
|---|---|
| `00-command-center.md` | `04-gap-action-sprint.md` + `05-andrea-decisions.md` |
| `01-venue-target-list-framework.md` | `02-outreach-playbook/_v1-detailed.md` Section C |
| `01a-venue-warm-pitch.md` | `02-outreach-playbook/_v1-detailed.md` Section B.3 |
| `01b-venue-cold-pitch-email.md` | `02-outreach-playbook/_v1-detailed.md` Section C.3 |
| `01c-venue-followup-and-decision-tree.md` | `02-outreach-playbook/_v1-detailed.md` Section C.4 |
| `03-this-week-action-plan.md` | `04-gap-action-sprint.md` (now-current "this week") |
| `04-ig-profile-and-first-week-content.md` | `01-announcement-package/README.md` Phase 1 |
| `06-tools-stack-setup.md` | `06-genspark-deployment/README.md` + `05-andrea-decisions.md` Decision 3 |
| `06a-canva-pro-action-steps.md` | `06-genspark-deployment/02-social-media-prompt-pack.md` |
| `06b-claude-pro-action-steps.md` | `06-genspark-deployment/05-model-overrides.md` |
| `_enrichment/data-brief.md` + `recognition-map.md` + `universal-anchors.md` | Absorbed into BOS / launch package; no live cross-refs |

---

## What was NOT touched (intentionally kept in place)

- `brand-operating-system/` — 47 files. Source of truth, all current.
- `source/` — 3 files. Canonical voice. Cited across BOS.
- `research/` — 6 files. Foundational. Cited in BOS funnel + venue-pitch.
- `deliverables/2026-04-11-monday-package/` — Active lineage. BOS built FROM this.
- `pre-launch/` 4 active docs — actively cross-referenced.
- `notes/` — empty placeholder with `.gitkeep`.
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
