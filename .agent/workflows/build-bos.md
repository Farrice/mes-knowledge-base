---
description: Build a complete 6-layer Brand Operating System (BOS) for any brand — client, personal, or new venture. 43 markdown docs across foundation, visual, briefs, marketing, AI handoff, and ops layers, optionally auto-uploaded to Drive as native Google Docs in pageless format. Reference implementation: Resonance for Andrea (shipped 2026-05-04).
---

# `/build-bos` — Universal Brand Operating System Builder

Produces an AI-handoff-first Brand Operating System at the same quality bar as the Resonance reference. 7 phases (A-G), 43 docs, optional Drive auto-upload. The pattern that worked for Andrea, codified for any future brand.

## Quick Start

```
/build-bos --name "<Brand>" --source <path-to-canonical-doc> --output <project-path>
/build-bos --name "<Brand>" --source <path> --output <path> --drive-parent <folder-id>   # + Drive
/build-bos --name "<Brand>" --discovery --output <path>                                  # No source docs → run founder interview first
```

## Args

| Flag | Required | Purpose |
|---|---|---|
| `--name <Brand>` | yes | Brand display name. Becomes `{{BRAND_NAME}}` in scaffold. |
| `--source <path>` | one of `--source` or `--discovery` | Path to ≥1 canonical input doc (manifesto, anchor, brand brief). |
| `--discovery` | one of `--source` or `--discovery` | No prior docs — run structured founder interview to manufacture canonical inputs first. |
| `--output <path>` | yes | Target project directory. Default: `projects/<slug>/brand-operating-system/`. |
| `--drive-parent <id>` | optional | If supplied, auto-uploads to Drive as native Google Docs at end of Phase G. Get folder ID via `gws drive files list`. |
| `--tokens-file <path>` | optional | JSON file with identity tokens. If absent, prompt interactively. See `templates/brand-operating-system-v1/TOKENS.md`. |
| `--no-finalize` | optional | Skip chain finalize at end (use during in-progress runs). |
| `--force` | optional | Overwrite output dir if non-empty. |

---

## What This Produces

A 6-layer directory tree at `<output>`:

```
<output>/
├── 00-foundation/        Spine: brand bible, ICP, voice, positioning, non-negotiables, master index (6 docs)
├── 01-visual/            Surface: DESIGN.md, photography, components, brand library, aesthetics (5 docs)
├── 02-briefs/            Production: master template + 9 per-asset briefs (10 docs)
├── 03-marketing/         Distribution: pillars, hooks, channels, curation, crisis, why-gate, funnel, offer (8 docs)
├── 04-ai-handoff/        Friction-killer: AI Brain Master, Claude Pro setup, prompts, image, Canva (5 docs)
├── 05-ops/               Self-correction: update protocol, change log, handoff, drift, metrics, exits, run-of-show (7 docs)
├── _working/             Intermediate scaffolding (A1, A3, G1, G2 — not for client delivery)
└── _source/              Archived canonical inputs
```

If `--drive-parent` supplied: a dated subfolder in Drive with all 43 docs as native Google Docs in pageless format.

---

## Pre-flight

Before running, verify:

1. **Routing check** (deterministic, halts if wrong workflow chosen):
   ```bash
   python3 execution/routing_enforcer.py check --request "$USER_REQUEST" --workflow build-bos --quiet
   ```

2. **Skill exists**: `skills/brand-operating-system/SKILL.md` and 7 workflow files under `skills/brand-operating-system/workflows/`

3. **Template exists**: `templates/brand-operating-system-v1/` with TOKENS.md

4. **For Drive upload**: `gws auth login -s drive,docs` is fresh

---

## Phase 0 — Scaffold

```bash
python3 execution/bos_scaffold.py \
    --template templates/brand-operating-system-v1/ \
    --output <output>/ \
    --tokens-file <tokens-file> \
    [--force]
```

Substitutes identity tokens (`{{BRAND_NAME}}`, `{{FOUNDER_NAME}}`, `{{CITY}}`, `{{SPINE_LINE}}`, etc.). Output: 47 files copied (43 BOS + 2 source placeholders + 4 working). Brand-specific content sections (the 12 non-negotiables, voice patterns, ICP profiles) are preserved from Resonance for Phase A-B to overwrite with new-brand content.

---

## Phase A — Discovery

Read [skills/brand-operating-system/workflows/01-discover.md](../../skills/brand-operating-system/workflows/01-discover.md) for full protocol.

Steps:
- A0 — Archive canonical inputs to `_source/` (or run discovery interview)
- A1 — `agents/synthesis-engine/` reconciliation pass → `_working/A1-reconciliation.md`
- A2 — `agents/icp-deep-canvasser/` + `skills/icp-deep-dive/` → `00-foundation/02-icp-master.md` (early)
- A3 — `/ai-brain-discovery` 8-dimension diagnostic → `_working/A3-discovery.md`

Quality gate Phase A → B: see workflow file.

---

## Phase B — Foundation

Read [skills/brand-operating-system/workflows/02-foundation.md](../../skills/brand-operating-system/workflows/02-foundation.md).

Steps:
- B1 — `agents/brand-system-builder/` → brand bible
- B2 — Direct port from canonical → non-negotiables
- B3 — `/voice-document` → voice document
- B4 — Finalize ICP master from A2 draft
- B5 — `agents/master-copywriter/` → positioning one-pager (⚠️ main thread saves output)
- B6 — `agents/master-copywriter/` → master index

Quality gate Phase B → C: see workflow file.

---

## Phase C — Visual

Read [skills/brand-operating-system/workflows/03-visual.md](../../skills/brand-operating-system/workflows/03-visual.md).

Steps:
- C1 — `/design-md-synthesize` → DESIGN.md (lints clean)
- C2 — `/brand-library` → brand library entry
- C3 — `/junyuh-brandbook` → aesthetics + components + photography rules

Quality gate Phase C → D: see workflow file.

---

## Phase D — Creative Briefs

Read [skills/brand-operating-system/workflows/04-briefs.md](../../skills/brand-operating-system/workflows/04-briefs.md).

Steps:
- D1 — Master template (already substituted in scaffold)
- D2-D10 — **9 parallel `agents/master-copywriter/` invocations** for IG×3, email, flyer, ticket, venue, press, DJ — main thread saves all outputs

Quality gate Phase D → E: see workflow file.

---

## Phase E — Marketing & Content

Read [skills/brand-operating-system/workflows/05-marketing.md](../../skills/brand-operating-system/workflows/05-marketing.md).

Steps:
- E1 — `/content-cluster` → content pillars
- E2 — `/hook-bank` + `/hook-forge` → hook library
- E3 — `agents/master-copywriter/` × 6 → channels, curation, crisis, why-gate, funnel, offer card
- E4 — Direct port from canonical → drift signals, success metrics, exit interview protocol

Quality gate Phase E → F: see workflow file.

---

## Phase F — AI Handoff

Read [skills/brand-operating-system/workflows/06-ai-handoff.md](../../skills/brand-operating-system/workflows/06-ai-handoff.md).

Steps:
- F1 — `/ai-brain-context` → AI Brain Master (≤4K tokens)
- F2 — `/ai-brain-deploy` → blueprint informs F3-F5
- F3 — `/4c-architect` → Claude Pro project setup
- F4 — `agents/master-copywriter/` → prompt library (15-25 prompts)
- F5 — `/creative-prompt` → image prompt formulas + Canva spec

Quality gate Phase F → G: see workflow file. **Cold-start test required** — paste only AI Brain Master into fresh Claude session, confirm on-brand output.

---

## Phase G — Wrap

Read [skills/brand-operating-system/workflows/07-wrap.md](../../skills/brand-operating-system/workflows/07-wrap.md).

Steps:
- G1 — `agents/adversarial-reviewer/` → 5-axis stress test (composite ≥7 to ship)
- G2 — `agents/prose-doctor/` → voice + structural-tell scan (0 banned-move violations)
- G3 — Drive upload (only if `--drive-parent` supplied):
  ```bash
  python3 execution/md_to_gdoc.py <output>/ \
      --drive-parent <folder-id> \
      --mirror-folders \
      --create-folder "$(date +%Y-%m-%d) — Brand Operating System v1"
  ```
- G4 — Chain finalize (composite ≥7 required):
  ```bash
  python3 execution/chain_runner.py finalize "<Brand> Brand Operating System v1" \
      --expert "brand-system-builder" \
      --skill "brand-operating-system" \
      --workflow "build-bos" \
      --type "Client Work" \
      --intent 9 --expert-score 9 --adversarial 8 \
      --notes "<Brand> BOS v1 — 6 layers, 43 docs | Factual Grounding: 9 | Verification: PASS"
  ```

Quality gate Phase G → done: see workflow file.

---

## Resumability

Each phase writes its outputs to disk before advancing. If a run halts mid-build (quality-gate failure, founder review needed, system interruption), restart by:

```bash
/build-bos --name "<Brand>" --resume --output <existing-path>
```

The orchestrator detects which phase outputs already exist and resumes from the next pending phase. Idempotent: re-running a completed phase does not duplicate outputs (it overwrites).

---

## Anti-Patterns (Routing Enforcer Halts These)

1. **Substituting `agents/brand-system-builder/` direct invocation** for the orchestrated 7-phase build. The agent is a Phase B component, not a replacement.
2. **Skipping Phase A** because "we already know the brand." The synthesis pass surfaces conflicts that would compound through the build.
3. **Skipping Phase G** because "the docs look good." Adversarial review catches structural-soundness bugs that human eyes miss (Resonance had a CRITICAL file-numbering bug caught in G1).
4. **Manually rendering to .docx + uploading to Drive** instead of using `md_to_gdoc.py`. Standing rule: native Google Docs + pageless, every Drive upload.
5. **Authoring a custom 4-layer or 8-layer variant** for "this brand is different." If a brand needs more or fewer layers, the architecture itself is changing — bump to v2 of the skill, don't fork at runtime.

---

## Reference Implementation

**Resonance for Andrea** (shipped 2026-05-04):
- Source: `projects/andrea-dj/brand-operating-system/`
- Drive: [Andrea DJ Package / 2026-05-04 — Brand Operating System v1](https://drive.google.com/drive/folders/18KsPdrORo-YNo_Yr4ejALWuw1fgeqvVE)
- Quality: Composite 8.3/10, adversarial 7.6/10, all 43 native Google Docs in pageless format

The Resonance build is the live reference. When `/build-bos` amends, the Resonance instance gets back-applied per `directives/brand-operating-system-protocol.md`.

---

## Verification

```bash
# 1. Scaffold + token round-trip
python3 execution/bos_scaffold.py --template templates/brand-operating-system-v1/ \
    --output /tmp/test-bos-rt/ --tokens-file scratch/resonance-tokens.json --force
diff -r projects/andrea-dj/brand-operating-system/ /tmp/test-bos-rt/  # only _source/ should differ

# 2. Routing check
python3 execution/routing_enforcer.py check --request "build a BOS" --workflow build-bos --quiet  # exit 0
python3 execution/routing_enforcer.py check --request "build a BOS" --workflow brand-system-builder --quiet  # exit non-zero

# 3. End-to-end (with stub source doc)
echo "# Test Brand Anchor\n\nWe make X for Y." > /tmp/test-anchor.md
/build-bos --name "TestBrand" --source /tmp/test-anchor.md --output /tmp/test-bos-e2e/ --no-finalize
ls /tmp/test-bos-e2e/  # should show 6 layer folders + _working + _source
```
