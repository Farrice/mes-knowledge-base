# Workspace Reorganization + Research-Grounded Strategic Clarity Rebuild

## The Problem (Two Issues)

### Issue 1: Research Quality
The 5 strategic clarity documents were built primarily from **recycled internal KI artifacts**, not fresh external research. Only 2 supplementary Perplexity queries were run. The documents read like session summaries because that's what they are — a remix of existing knowledge, not a market-validated strategic analysis.

### Issue 2: Organizational Clutter
18+ sessions of work have created overlapping, unstructured file sprawl that causes context bleeding:

| Problem | Details |
|---------|---------|
| **Duplicate zones** | `_active/content/` overlaps with `deliverables/`, `_active/offers/` overlaps with `deliverables/revenue-sprint/`, `_active/research/` overlaps with `research_outputs/` |
| **Orphan files** | 3 `.skill` files at workspace root (`lara-acosta-linkedin-growth.skill`, `sean-mabry-voice-mastery.skill`, `tyler-denk-audience-monetization.skill`) |
| **Zombie directory** | `00_FOCUS_MODE/` contains 19 stub files (7-21 bytes each) — placeholder configs that serve no purpose |
| **Sprawl in `_active/linkedin-launch/`** | 31 items (13 subdirs + 18 files) with no index — this is where most of the "bleeding" is |
| **Unnamed swarm outputs** | `swarm_outputs/` has 36 timestamp-named dirs with no description or index |
| **No clear "current work" zone** | `strategic-clarity/` at root, `_active/`, and `00_FOCUS_MODE/` all compete to be "where current work lives" |

---

## Proposed Changes

### Phase 1: Workspace Reorganization

> [!IMPORTANT]
> All moves are non-destructive — files are relocated, never deleted.

#### Step 1: Establish Clean Structure

The workspace should have **one** clear place for each type of content:

```
/Google Antigravity/
├── _active/                    ← CURRENT work (max 3-5 active projects)
│   ├── linkedin-launch/        ← Keep (active project, consolidate)
│   ├── farrice-brand/          ← Merge brand + content + offers into one
│   └── strategic-clarity/      ← Move from root (after Phase 2 rebuild)
│
├── _archive/                   ← COMPLETED work (date-stamped)
│   └── [existing + archived items]
│
├── deliverables/               ← CLIENT work (keep as-is, clean internal)
├── research_outputs/           ← RESEARCH artifacts (keep, add index)
├── strategy_briefs/            ← STRATEGY docs (keep, add index)
├── swarm_outputs/              ← SWARM results (add index.md)
│
├── projects/                   ← BUILDS (websites, tools)
├── skills/                     ← SKILLS (system)
├── agents/                     ← AGENTS (system)
├── execution/                  ← SCRIPTS (system)
├── directives/                 ← PROTOCOLS (system)
└── [system config files]       ← CLAUDE.md, FARRICE.md, etc.
```

#### Step 2: Specific Moves

##### [MOVE] Orphan `.skill` files → `_archive/orphan-skills/`
- `lara-acosta-linkedin-growth.skill`
- `sean-mabry-voice-mastery.skill`
- `tyler-denk-audience-monetization.skill`

##### [MOVE] `00_FOCUS_MODE/` → `_archive/00_FOCUS_MODE-deprecated/`
This directory contains 19 stub/placeholder files. It's a dead experiment.

##### [CONSOLIDATE] `_active/brand/` + `_active/content/` + `_active/offers/` → `_active/farrice-brand/`
These 3 directories are all "Farrice's business" — brand identity, content strategy, and offer architecture. They should be sub-folders of one project, not siblings.

```
_active/farrice-brand/
├── identity/           ← from _active/brand/
├── content/            ← from _active/content/
├── offers/             ← from _active/offers/
├── research/           ← from _active/research/
└── icp-intelligence/   ← from _active/icp-intelligence-service/
```

##### [MOVE] `strategic-clarity/` → `_archive/2026-07-28-org-sweep/strategic-clarity/`
After Phase 2 rebuild, this becomes an active project, not a root-level artifact.

##### [CREATE] Index files for directories that lack them
- `swarm_outputs/INDEX.md` — catalog of what each timestamp dir contains
- `_active/linkedin-launch/INDEX.md` — map of the 31 items

##### [MOVE] `_active/demos/` → `_active/linkedin-launch/demos/`
Demos are part of the LinkedIn launch workflow.

##### [MOVE] `_active/platforms/` → `_active/linkedin-launch/platforms/`
Platform configs are part of the launch workflow.

---

### Phase 2: Research-Grounded Strategic Clarity Rebuild

> [!CAUTION]
> The existing 5 documents will be archived, not overwritten. New versions will be built from scratch with real research as the foundation.

#### Research Protocol

Each document gets rebuilt using this protocol:

1. **Perplexity Deep Research** — 3-5 specific queries per document targeting *external market validation*, not internal knowledge
2. **Parallel Research Swarm** — Deploy 3 research agents simultaneously for cross-validation
3. **Grounding Pass** — Every claim must cite either a Perplexity source or a specific data point

#### Specific Research Queries Planned

**For Identity & Expertise Map (Doc 01):**
- "What does the market for AI-augmented ghostwriting services look like in 2026? Who are the key players, what are they charging, and what gaps exist?"
- "What premium service categories command the highest rates in the coaching/consulting content space?"
- "How are coaches and consultants currently buying content services? What does their purchasing decision look like?"

**For Market Opportunity Matrix (Doc 02):**
- "What are the most painful content and visibility challenges for executive coaches and wellness consultants in 2026?"
- "What AI tools and services are coaches/consultants currently paying for? What's working and what's failing?"

**For Offer Architecture (Doc 03):**
- "What are successful solopreneurs charging for productized writing, ghostwriting, and AI-consulting services in 2026? Real pricing examples."
- "What service delivery models are working for one-person agencies in the coaching niche?"

**For Revenue Sprint (Doc 04):**
- "What are the fastest-proven methods for a solo consultant to generate $2K-$5K in the first 2 weeks of launching a service?"
- "Upwork, Fiverr, and LinkedIn — where are coaches currently hiring ghostwriters and content strategists?"

**For Decision Framework (Doc 05):**
- Synthesized from the other 4 documents' research — no additional queries needed

---

## Verification Plan

### Automated Checks
- Run `find` to confirm no orphan `.skill` files remain at root
- Run `ls -la` on new directory structure to verify all moves completed
- Count files before and after to confirm nothing was lost

### Manual Verification
1. **Research grounding**: Each rebuilt document will include a "Sources" section at the bottom citing specific Perplexity research findings
2. **Freshness check**: You (Farrice) read the rebuilt docs and confirm they contain *new* insights you haven't seen in our previous sessions
3. **Organization check**: Navigate the workspace and confirm you can find things intuitively

---

## User Review Required

> [!IMPORTANT]
> Before I move any files, I need your approval on the reorganization structure. The moves are non-destructive (archive, not delete), but the new structure changes where you'll find things.

Two questions:
1. **Does the proposed `_active/farrice-brand/` consolidation make sense?** Or do you want brand, content, and offers to remain separate?
2. **Are there any directories I should NOT touch?** (e.g., if you have muscle memory for certain file locations)
