# Supercomputer Mode — Natural-Language Detection

> **Status**: Mandatory routing binding (mirrored in `execution/routing_enforcer.py`).
> **Workflow**: `.agent/workflows/supercomputer.md`
> **Skill**: `skills/supercomputer/`
> **Companion modules**: `execution/cost_gate.py`, `execution/anchor_memory.py`, `execution/creative_router.py`

When the user's chat input matches a Supercomputer trigger phrase below, auto-fire `/supercomputer` INSTEAD of routing to a single-skill workflow. The Supercomputer is the right tool whenever a request spans multiple creative deliverables that should share brand state.

This directive defines:
1. **Trigger phrases** — patterns that auto-fire `/supercomputer`
2. **Project slug derivation** — how to name `projects/<slug>/`
3. **When to ASK vs INFER** — clarification policy
4. **Cost gate UX** — how to surface preview + approval cleanly
5. **Mid-mission pivots** — how to halt gracefully

---

## 1. Trigger Phrases

When user input matches any of the patterns below, fire `/supercomputer`.

### Brand-build patterns
- "Build me a brand for [X]"
- "Build a brand around [X]"
- "Brand identity for [X]"
- "Launch a brand called [X]" / "Start a brand called [X]"
- "Make a [X] brand from scratch"

### Campaign / launch patterns
- "Make me a campaign for [X]"
- "Run a campaign for [X]"
- "Launch [X] on [platform]"
- "Full marketing for [X]"
- "Marketing plan + assets for [X]"
- "Drop a campaign for [X]"

### Multi-deliverable creative patterns
- "Create a [UGC ad / video ad / brand identity / product sheet] for [X]"
- "Make me a [hero shot] AND [listing visuals] AND [ad concepts] for [X]"
- "Full content drop on [X]" (e.g., Substack + LinkedIn + Notes from one insight)
- "Build a complete asset pack for [X]"
- "I need brief + visuals + copy for [X]"

### Project state patterns (existing project, add to it)
- "Add [Y] to [existing-project-slug]"
- "Next phase for [existing-project-slug]"
- "Keep building on [existing-project-slug]"

> **Farrice — refine this list after 5-10 real missions.** The patterns above are best-guess defaults. Watch for false positives (single-deliverable asks that match a multi-deliverable pattern) and false negatives (multi-deliverable asks that miss). Update both this section AND `execution/routing_enforcer.py BINDINGS` together.

### When NOT to fire Supercomputer

- Single-deliverable explicit ask: "Write me one LinkedIn post about X" → `/ghostwrite` directly
- Diagnostic / review: "Look at this draft and critique it" → `/writers-room` or `/adversarial-review`
- System / file / git operations: never Supercomputer
- Conversational / informational: "What does Higgsfield's Supercomputer do?" → just answer
- Existing-project incremental work that's just ONE deliverable: load state, run one skill, don't trigger full 4-phase flow

If unsure: the chain's normal routing (CLAUDE.md Step 3) handles it. Supercomputer is for cross-deliverable cohesion, not for "be impressive."

---

## 2. Project Slug Derivation

Slugs become `projects/<slug>/` and live forever. Pick well.

### Rules

1. **Kebab-case lowercase.** No spaces, no underscores, no caps.
2. **Concrete > clever.** `foldable-resistance-band-rack` beats `iron-grip` (the descriptive slug is auditable; the clever one isn't).
3. **3–6 words max.** Long slugs become unwieldy in paths.
4. **No dates in slug.** Use `state.yaml created_at` field.
5. **Check existing projects first.** Always run `python3 execution/anchor_memory.py list` before initializing — the user may have an existing project you should extend.

### Derivation pipeline

Given input "Build me an Amazon brand for a foldable resistance band rack":

1. Extract the noun phrase that names the THING: "foldable resistance band rack"
2. Strip articles + filler: same
3. Kebab: `foldable-resistance-band-rack`
4. Check uniqueness in `projects/` — if collision, append `-2` or pick a more specific phrase

### Existing project mapping (verified)

Map these phrases to known existing slugs:

| User phrase | Existing project slug |
|---|---|
| "parallax", "my substack", "farrice brand", "the personal brand" | `farrice-brand` (lives in `_active/farrice-brand/` not `projects/`) |
| "jen's listings", "the realtor stuff", "real estate content" | `jen-santulan-listing-content` |
| "mybpm", "the streetwear brand" | `mybpm-streetwear-brand` |
| "andrea", "resonance", "the sober dance party" | `andrea-dj` |
| "javier", "human values collective" | `javier-human-values` |

> **Farrice — add to this map as you start new long-running projects.** This is the bridge between "casual reference" and "concrete project path."

---

## 3. ASK vs INFER

The Supercomputer should INFER aggressively and ASK only when inference cost > clarification cost.

### Always INFER (don't ask)

- Slug (derive from request, state it back: "Working in project `<slug>`")
- Service routing (run `creative_router.py`, state the choice + reason)
- Quality tier for first pass (always `medium` for images; user can request `high` for finals)
- Number of variants for an ad concept brief (default 5)
- Reasonable defaults for any setting documented in this directive or SKILL.md

### Always ASK (don't infer)

- Brand name if the request is "build me a brand" without naming the brand
- Platform if the request is platform-dependent (Amazon vs Shopify vs DTC site changes the deliverables)
- Audience if not implied by the product (a "resistance band" doesn't imply gym-rats vs travelers vs PT patients)
- Anything that affects more than $2 of spend (always confirm at plan time)
- Tone / positioning if 2+ valid reads exist (premium vs accessible vs niche-cult are very different deliverables)

### ASK pattern

When asking, batch the questions in ONE message using `AskUserQuestion` (not multiple rounds). Maximum 3 questions per round. Frame each as a multi-choice with a recommended first option.

---

## 4. Cost Gate UX

Higgsfield's killer mechanic ported clean.

### Plan-time preview (Phase 1 of supercomputer workflow)

Format (verbatim — user is trained to look for this):

```
═══════════════════════════════════════════════════
MISSION PLAN — <slug>
═══════════════════════════════════════════════════
[numbered steps with cost annotations]

Estimated total: $<paid_sum> paid + ~<N> Gemini calls (Ultra quota)

Anchors flow:
  step <N> (<type>) → required for steps <list>

Proceed? (y / adjust / cancel)
```

### Mid-mission gate (cost_gate.py exit 2)

When `cost_gate.py check` returns exit 2 (needs approval), surface a clean one-liner — don't dump the full check output:

```
⏸  Approve $1.50 for hero cinematic clip (higgsfield-cinema)? (y/n)
```

If user approved this exact step at plan time AND actual estimate is within 20% of planned, you may auto-proceed without re-asking (state which step the approval applies to). If estimate is >20% over plan or this is a new step not in the plan, always re-ask.

### Halt gate (cost_gate.py exit 1)

When `cost_gate.py check` returns exit 1 (denied), STOP immediately. Surface the denial reason verbatim from the check output. Ask user how to adjust:

```
❌ Step blocked: <reason from cost_gate output>

Options:
  • Lower quality (re-route)
  • Skip this step
  • Adjust mission scope
  • Reset daily cap (python3 execution/cost_gate.py reset-daily) if intentional
```

Never silently re-route. Never silently skip. Always surface the choice.

---

## 5. Mid-Mission Pivots

If the user changes direction mid-mission ("actually, scrap step 4 and instead do Y"):

1. **Acknowledge the pivot** — restate what's now scoped in and what's dropped.
2. **Update the plan** in writing — present a revised plan block.
3. **Re-cost** — show new total estimate.
4. **Confirm before continuing** — one "y" approval for the new plan.
5. **Anchor what's already done** — don't lose anchors from steps 1-3 just because step 4 changed.
6. **Log the pivot** in anchor memory:
   ```bash
   python3 execution/anchor_memory.py log <slug> \
       --phase "pivot" \
       --action "user redirected from <original> to <new>"
   ```

If the user wants to abort entirely: leave the project state intact (it has value for later), log the abort, exit cleanly. Don't delete `projects/<slug>/` unless explicitly asked.

---

## 6. Composition Etiquette (when Supercomputer calls into other workflows)

When the supercomputer composes `/build-bos`, `/parallax`, `/jcc-deploy`, etc:

1. **Pass `--project <slug>`** if the called workflow supports it (most don't yet — that's fine, just pass an env var `ANTIGRAVITY_PROJECT=<slug>` for downstream tools to pick up).
2. **Let the called workflow do its own quality gate** — don't double-finalize.
3. **Capture the called workflow's output paths** into anchor memory immediately after it returns.
4. **Don't deep-dive into the called workflow's internals** — trust it.

This is the "skill of composition" — the supercomputer's job is orchestration, handoff, and state. Each composed skill remains the owner of its own deliverable quality.

---

## See Also

- `skills/supercomputer/SKILL.md` — composition table + when-to-use
- `skills/supercomputer/genius.md` — design philosophy + open questions
- `.agent/workflows/supercomputer.md` — the executable 4-phase runbook
- `execution/routing_enforcer.py` — the expected-binding code (must mirror Section 1 above)
- CLAUDE.md "Mandatory Workflow Routing" table — the human-readable mirror of the bindings
