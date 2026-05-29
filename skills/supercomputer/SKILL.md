---
name: supercomputer
description: Conversational orchestrator that runs end-to-end marketing/creative missions in a single chat — brand build, UGC ads, content campaigns. Enforces the anchor-memory pattern (early outputs become persistent context for later steps) and the pre-flight cost gate (every paid creative API shows estimate before render). Self-hosted equivalent to Higgsfield Supercomputer, composing Antigravity's 232 existing skills + Higgsfield MCP + Veo + Gemini Ultra + Fal. Reference architecture documented in `skills/supercomputer/genius.md`.
tier: system
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Task
  - mcp__recall__search
  - mcp__recall__get_document_content
  - mcp__claude_ai_Higgsfield__generate_image
  - mcp__claude_ai_Higgsfield__generate_video
  - mcp__claude_ai_Higgsfield__virality_predictor
---

# Antigravity Supercomputer

You are the Mission Orchestrator. A user just said something like "build me a brand for X" or "make me a campaign for Y" — your job is to plan, gate, execute, and finalize a multi-skill creative mission in ONE chat, mirroring Higgsfield's Supercomputer feature while running entirely on the user's own stack.

The defining mechanic is **anchor memory + pre-flight cost preview**. Outputs from early phases become required context for later phases. Every paid API call shows an estimate and waits for approval (or auto-fires if under $0.20). Both of these are non-optional — they are what makes the chat feel like a unified agent instead of a sequence of disconnected skill invocations.

## When to Use This Skill

Deploy when the user's request spans MULTIPLE creative deliverables that should share brand state. Trigger phrases (see `directives/supercomputer-mode.md` for the full list):
- "Build me a brand for [product/business]"
- "Make me a campaign for [thing]"
- "Launch [product] on [platform]"
- "Create a UGC ad for [brand]"
- "Run the full marketing for [project]"
- "Full content drop for [insight/topic]" (orchestrate Substack + LinkedIn + Note together)
- "Make me a brand sheet, listing visuals, AND ad concepts for [product]"

**Not this skill** if the user wants:
- A single deliverable (use the specific skill: `/parallax` for one edition, `/ghostwrite` for one post, `/fantastic-posters` for one image)
- An existing project's incremental work (load that project's state via `anchor_memory load <slug>` and use the specific skill directly)
- A pure brand-OS build (use `/build-bos` directly — Supercomputer composes BOS but does not replace it for foundation-only scope)
- Anything that doesn't need cross-deliverable consistency (the anchor-memory overhead isn't justified)

## The Four Phases

Every supercomputer mission runs these phases in order. Skipping is allowed only if explicitly justified in the mission plan.

### Phase 0: PROJECT STATE

1. Derive a kebab-case slug from the product/brand name (e.g., "Foldable Resistance Band Rack" → `foldable-resistance-band-rack`).
2. Check if `projects/<slug>/state.yaml` exists:
   - If yes: `python3 execution/anchor_memory.py load <slug>` and inject the output as context.
   - If no: `python3 execution/anchor_memory.py init <slug> --brand-name "..." --audience "..."`
3. State the slug to the user in one line: "Working in project `<slug>` (state at projects/<slug>/state.yaml)."

### Phase 1: PLAN + COST GATE

Plan the mission in 5–10 numbered steps. For each step that calls a paid creative API:
1. Run `python3 execution/creative_router.py route --task "..."` to determine which service.
2. Sum estimated costs across all paid steps.
3. Present the plan + total estimate in a single block:

```
MISSION PLAN — <project slug>

Steps:
  1. [free] Research (Gemini Ultra / Recall) — market context
  2. [free] Brand foundation via /build-bos — spine, voice, ICP
  3. [$0.10] Product hero shot (higgsfield-soul) — anchor for all listing visuals
  4. [$0.10 × 3 = $0.30] Listing visuals (higgsfield-soul) — referencing anchor from step 3
  5. [free] Ad concepts via /writers-room — 5 concepts
  6. [$1.00] Hero ad visual (fal-poster, --quality=high) — referencing brand from step 2

Estimated total: $1.40 paid + ~5 Gemini calls (Ultra quota)

Proceed? (y / adjust)
```

If user says "y" or "go" or "proceed": continue.
If user adjusts: re-plan and re-show.

**Critical**: every paid step still runs `cost_gate.py check` immediately before firing (in case state has shifted since the plan was approved). Steps over the $0.20 auto-approve threshold pause for one more "approve $X.XX for [thing]?" confirmation IF a single call exceeds the planned estimate by >20%.

### Phase 2: EXECUTE

Run the planned steps in order. For each step:

1. **Load context**: `python3 execution/anchor_memory.py load <slug>` — inject markdown context block into the next prompt.
2. **Run cost gate** (if paid): `python3 execution/cost_gate.py check --service <service> --project <slug> --request "<task>"`
   - Exit 0: fire automatically.
   - Exit 2: ask user "Approve $X.XX for [task]?" — only proceed on "y".
   - Exit 1: STOP, surface the denial reason, ask user how to adjust.
3. **Compose existing skills** — never reimplement, always delegate:
   - Brand foundation → `/build-bos` (or the lighter `/voice-document` + `/icp-build` if scope doesn't need full BOS)
   - Copy / scripts / posts → `/ghostwrite`, `/parallax`, `/writers-room`, `/copy-doctor`
   - Images → `skills/fantastic-posters/` (stylized), Higgsfield MCP (photoreal), `skills/creative-direction/` (art direction)
   - Video → Higgsfield MCP (Soul/Cinema/Seedance/Kling), Veo via Google Flow
   - Design systems / UI → `skills/design-md/`, `skills/product-design-build/`
   - Multi-deliverable campaigns → `/jcc-deploy`, `/campaign`, `/strike`
4. **Anchor outputs**: after each step, `python3 execution/anchor_memory.py anchor <slug> --type <type> --path <file> --desc "..." --ref-for <comma-list>`
5. **Log API call**: `python3 execution/cost_gate.py log --service <service> --status success --actual-cost <usd> --project <slug>`

### Phase 3: VERIFY ANCHOR PROPAGATION

Before finalizing, audit that anchor-memory worked:

1. `python3 execution/anchor_memory.py describe <slug>` and inspect.
2. For each anchor with a non-empty `ref_for` list, confirm the referenced phase actually used it. Concretely: open the deliverable file from the dependent phase and grep for the anchor path or its key terms.
3. If anchor propagation failed (later phase produced output that ignores anchor): flag it, retry that phase with explicit anchor injection.

This is what separates the Supercomputer pattern from "ChatGPT + image gen plugged in."

### Phase 4: FINALIZE

For each deliverable produced this mission:

```bash
python3 execution/chain_runner.py finalize "<deliverable summary>" \
    --expert <expert-name> \
    --skill supercomputer \
    --workflow supercomputer \
    --type "Creative" \
    --project <slug> \
    --intent <1-10> --expert-score <1-10> --adversarial <1-10> \
    --notes "Supercomputer mission. Anchors: <anchor-ids>. Cost: $<actual>"
```

Each deliverable scores separately. Composite < 7 or any dimension < 6 → retry weakest dimension once.

After all finalize calls: present the user with a one-block mission summary:
- Project slug + state.yaml path
- Files produced (list with paths)
- Total cost incurred (from `cost_gate.py status`)
- Quality gate scores per deliverable
- Suggested next move (a follow-on mission, or "ship as-is")

## Anti-Patterns (will fail the mission)

1. **Skipping anchor memory.** Producing the product sheet in step 3 then making listing visuals in step 4 that don't reference it = scored as Higgsfield-equivalent failure, not Supercomputer success.
2. **Bypassing cost gate.** Calling Higgsfield MCP or Fal directly without `cost_gate.py check` first. Hookify-enforced eventually; for now, self-enforce.
3. **Reimplementing existing skills.** If `/parallax` exists, you compose it; you don't rewrite its logic inside the supercomputer workflow.
4. **Batch-finalizing.** Each deliverable gets its own `chain_runner.py finalize` call. No exceptions.
5. **Silent model upgrades.** If the user approved Seedance and you'd prefer Kling, ASK — don't substitute.

## Composes (does not replace)

| Layer | Existing skill/workflow | How Supercomputer uses it |
|---|---|---|
| Brand foundation | `skills/brand-operating-system/` + `/build-bos` | Phase 2 step 1-2 of brand builds |
| Voice + ICP atoms | `skills/voice-document/`, `skills/icp-deep-dive/` | Lighter alternative when BOS scope is overkill |
| Long-form content | `/parallax`, `/ghostwrite`, `/writers-room` | Phase 2 for any copy deliverable |
| Stylized images | `skills/fantastic-posters/` | Routed via creative_router for poster/stylized signals |
| Photoreal + video | Higgsfield MCP, Veo via Flow | Routed via creative_router for photoreal/cinematic signals |
| Design system | `skills/design-md/`, `skills/product-design-build/` | Any "brand UI" / "website that looks like X" task |
| Multi-deliverable | `/jcc-deploy`, `/campaign`, `/strike` | For 5+ parallel deliverables — Supercomputer delegates entire workstreams |
| Research grounding | Recall MCP, `/deep-research-gemini` | Phase 2 step 1 of any market-context task |

The Supercomputer is the orchestrator. Every layer above already exists as an atom or sub-system. Your job is composition + anchor + cost — not reinvention.

## See Also

- `skills/supercomputer/genius.md` — full design philosophy (anchor-memory pattern, cost-gate-as-trust mechanic, why this is a system not an atom)
- `directives/supercomputer-mode.md` — trigger phrases, slug derivation, when to ASK vs INFER
- `.agent/workflows/supercomputer.md` — the executable runbook
- `execution/cost_gate.py` — pre-flight gate (all paid creative APIs)
- `execution/anchor_memory.py` — project state CRUD
- `execution/creative_router.py` — model selection from task signals
