---
description: Conversational orchestrator — runs end-to-end marketing/creative missions in one chat. Anchor memory + pre-flight cost gate. Self-hosted equivalent to Higgsfield Supercomputer.
---

# `/supercomputer` — Antigravity Mission Orchestrator

The executable runbook for the Supercomputer skill. Read `skills/supercomputer/SKILL.md` for the full philosophy and skill composition table. This workflow is the step-by-step runner.

## Quick Start

```
/supercomputer "Build me a brand for [product]"
/supercomputer "Make a UGC ad for [existing-project-slug]"
/supercomputer "Full content drop on [thought-bank theme]" --project farrice-brand
```

Or invoke implicitly via natural language — `directives/supercomputer-mode.md` auto-fires this workflow when the user's request matches one of the 15+ trigger phrases.

## Args

| Flag | Required | Purpose |
|---|---|---|
| `<request>` (positional) | yes | Free-text mission description |
| `--project <slug>` | optional | Existing project slug. If omitted, derived from request. |
| `--auto-approve-under <usd>` | optional | Override `cost_gate.py` $0.20 default for this mission. |
| `--no-cost-gate` | DANGER | Skip cost preview entirely. Only use when running against quota-only services (Gemini text, Veo within quota). |

---

## Phase 0 — Project State

**Goal**: every output produced by this mission lands in `projects/<slug>/` and is tracked in anchor memory.

1. Derive slug from request:
   - "Build me a brand for foldable resistance band rack" → `foldable-resistance-band-rack`
   - "UGC ad for mybpm streetwear" → `mybpm-streetwear` (or use existing `mybpm-streetwear-brand` if `anchor_memory list` shows it)
   - "Full content drop on suppression wound" → `farrice-brand` (user's existing project) + `--theme suppression-wound` as decision

2. Initialize or load:
   ```bash
   # If projects/<slug>/state.yaml exists:
   python3 execution/anchor_memory.py load <slug>
   # Else:
   python3 execution/anchor_memory.py init <slug> --brand-name "..." --audience "..."
   ```

3. Inject the `load` output as context for Phase 1.

4. State to user: `"Working in project \`<slug>\`. State at projects/<slug>/state.yaml."`

---

## Phase 1 — Plan + Cost Gate

**Goal**: produce a numbered mission plan with cost estimates, get one explicit approval, then run.

### Build the plan

1. Decompose the request into 5–10 numbered steps. Each step is one deliverable.
2. For each step, classify:
   - **Text-only** (free under Gemini Ultra quota): mark as `[free]`
   - **Image / video / paid**: run `python3 execution/creative_router.py route --task "<step description>" --json` to identify service + reason
3. For each paid step, look up estimate from `cost_gate.py` service catalog (just read the SERVICES dict in `execution/cost_gate.py`).
4. Sum estimated costs.

### Present the plan

Use this exact format (the user is trained to look for it):

```
═══════════════════════════════════════════════════
MISSION PLAN — <slug>
═══════════════════════════════════════════════════

Steps:
  1. [free] <description> — via <skill/workflow>
  2. [free] <description> — via <skill/workflow>
  3. [$X.XX] <description> — via <service>, anchored to step <N>
  4. [$X.XX × N = $Y.YY] <description> — via <service>, anchored to step <N>
  ...

Estimated total: $<paid_sum> paid + ~<N> Gemini calls (Ultra quota)

Anchors flow:
  step 2 (brand brief) → required for steps 3, 4, 6
  step 3 (hero visual) → required for steps 4, 5

Proceed? (y / adjust / cancel)
```

### Wait for approval

- "y" / "go" / "proceed" / "yes" / "ship it" → continue to Phase 2
- Anything else → treat as adjustment request, re-plan, re-show
- "cancel" → halt, leave state as-is

---

## Phase 2 — Execute

For each step in the approved plan, in order:

### 2A. Load anchor context

```bash
python3 execution/anchor_memory.py load <slug>
```

Inject the markdown output into the next prompt.

### 2B. Pre-flight cost gate (paid steps only)

```bash
python3 execution/cost_gate.py check --service <service> --project <slug> --request "<task>"
```

Handle the exit code:
- **0** (auto-approved): fire immediately
- **2** (needs approval): ask user `"Approve $X.XX for [task]?"` — only proceed on explicit "y"
- **1** (denied): STOP. Surface the denial reason. Ask user how to adjust (lower quality? skip step? change service?)

### 2C. Execute the step

Compose the right existing skill — never reimplement. Reference table:

| Step type | Skill / workflow | Notes |
|---|---|---|
| Market research | `mcp__recall__search` first, then `/deep-research-gemini` if gaps | Recall is free + grounded |
| Brand foundation (full) | `/build-bos` | 6-layer, 43 docs — heavy |
| Brand foundation (light) | `/voice-document` + `/icp-build` | When BOS overkill |
| Substack edition | `/parallax` | Phase 2.5 ground-check enforced |
| LinkedIn post | `/ghostwrite` (with Lara Acosta skill) | |
| Notes / micro-content | Notes Trailer Playbook | See `_active/farrice-brand/content/parallax-packages/NOTES_TRAILER_PLAYBOOK.md` |
| Writers-room refinement | `/writers-room` | For draft polishing, not from-scratch |
| Stylized image | `skills/fantastic-posters/` via `./gen.sh` | 38 styles |
| Photoreal image | Higgsfield MCP `generate_image` (Soul/Nano) | Via creative_router |
| Single-shot cinematic | Higgsfield MCP `generate_video` (Cinema/Seedance) | 5-10s only |
| Multi-shot video | Higgsfield MCP `generate_video` (Kling) | Multi-cut, audio-consistent |
| Premium cinema | Veo via Google Flow | Uses Ultra quota, $0 marginal |
| Design system | `skills/design-md/` workflows | `/design-md-synthesize`, `/brand-library` |
| Product UI build | `skills/product-design-build/` | `/product-build`, `/component-build` |
| Multi-deliverable campaign | `/jcc-deploy`, `/campaign`, `/strike`, `/solo` | When 5+ parallel deliverables |
| Virality check | Higgsfield MCP `virality_predictor` | Cheap, useful for hook testing |

### 2D. Anchor the output

```bash
python3 execution/anchor_memory.py anchor <slug> \
    --type <product_sheet|brand_brief|hero_visual|copy|video|ad_concept|...> \
    --path <relative/path/to/file> \
    --desc "<one-line description>" \
    --ref-for <comma,separated,future,phase,names> \
    --phase "Phase 2 step <N>"
```

The `--ref-for` field is the contract: any later step listed there MUST reference this anchor in its prompt.

### 2E. Log the API call (paid steps)

```bash
python3 execution/cost_gate.py log \
    --service <service> --status success \
    --actual-cost <usd> \
    --request "<task>" \
    --output-path <file> \
    --project <slug>
```

If the call failed: `--status failed`. The cost gate handles the consecutive-failure circuit.

---

## Phase 3 — Verify Anchor Propagation

Before finalizing, audit that anchor memory actually shaped downstream outputs.

```bash
python3 execution/anchor_memory.py describe <slug>
```

For each anchor with `ref_for: [<phase>...]`:

1. Open the deliverable file from each phase in `ref_for`
2. Grep for the anchor's path or distinctive key terms
3. If absent: anchor propagation failed. Retry that phase with explicit injection: load the anchor path into the prompt verbatim, regenerate.

This is the difference between Supercomputer success and "ChatGPT + image gen plugged in." Don't skip.

---

## Phase 4 — Finalize

For each deliverable produced:

```bash
python3 execution/chain_runner.py finalize "<one-line deliverable summary>" \
    --expert <expert-name-or-multi> \
    --skill supercomputer \
    --workflow supercomputer \
    --type "Creative" \
    --project <slug> \
    --intent <1-10> --expert-score <1-10> --adversarial <1-10> \
    --notes "Supercomputer mission. Anchors: <list of anchor-ids>. Cost: \$<actual>"
```

Score each deliverable on the 4-dimension rubric (see CLAUDE.md Step 6). Composite < 7 or any dimension < 6 → retry weakest section once, then re-finalize.

For Factual Grounding (dimension 4): if the deliverable is pure creative with no real-world claims, mark **N/A** in notes.

---

## Closing the Mission

After all finalize calls succeed, present one block to the user:

```
═══════════════════════════════════════════════════
MISSION COMPLETE — <slug>
═══════════════════════════════════════════════════

Files produced (<N>):
  • projects/<slug>/research/market-research.md
  • projects/<slug>/brand-operating-system/00-foundation/01-brand-bible.md
  • projects/<slug>/deliverables/product-sheet-hero.png
  • projects/<slug>/deliverables/listing-visuals/01-front.png
  • projects/<slug>/deliverables/listing-visuals/02-lifestyle.png
  • projects/<slug>/deliverables/ad-concepts.md

Cost incurred:
  Paid: $<actual> (estimate was $<planned>)
  Quota: <N> Gemini calls

Quality gate (4-dim composite):
  market-research:   <score>
  brand-bible:       <score>
  product-sheet:     <score>
  listing-visuals:   <score>
  ad-concepts:       <score>

State updated at projects/<slug>/state.yaml
<N> new anchors registered

Suggested next move:
  • <one specific follow-on, e.g., "/supercomputer 'launch-day plan for <slug>'">
  • Or ship as-is
```

---

## Anti-Patterns (mission FAIL)

1. Skipping Phase 0 (no state.yaml = no anchor memory = not a Supercomputer mission)
2. Skipping Phase 1's cost preview (every paid call burns trust)
3. Skipping Phase 2D anchor calls (downstream phases lose context)
4. Skipping Phase 3 verification (uncaught anchor failures = "looks Higgsfield-grade" but isn't)
5. Batch-finalizing all deliverables in one chain_runner call
6. Reimplementing skills inside the workflow instead of composing them
7. Silently substituting models (Seedance → Kling without asking)

## See Also

- `skills/supercomputer/SKILL.md` — composition table + when-to-use
- `skills/supercomputer/genius.md` — design philosophy
- `directives/supercomputer-mode.md` — natural-language detection
- `execution/cost_gate.py` — pre-flight cost gate
- `execution/anchor_memory.py` — project state
- `execution/creative_router.py` — model selection
