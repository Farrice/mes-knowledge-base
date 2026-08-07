# /verticalize — Vertical Bootstrap Workflow (Phase C / 2026-05-25)

> **System-tier conductor**. Takes "I'm entering [domain X]" and produces, in one orchestrated pass, the full calibration package needed to do world-class work in that vertical: ICP profile, voice document, ground-truth seed, expert routing bindings, per-project CLAUDE.md contract, and a first deliverable.

> **Why it exists**: Today setting up a new vertical (real estate for Jen, Resonance for Andrea, My.BPM streetwear, etc.) takes 1-2 weeks bespoke per vertical. This workflow composes existing atoms into one session — target time 1-2 hours.

> **NON-NEGOTIABLE**: Phase 2.5 user-validation gate. Without it, the new vertical's ground-truth calibrates to auto-seed and grade inflation enters from day one (per `feedback_auto-evolution-cant-substitute-for-ground-truth.md`).

---

## Quick Start

```bash
/verticalize "<vertical name or short description>"
```

Or via autopilot's universal resolver:
```bash
/autopilot "I'm entering AI-for-construction consulting"
```

## Args

| Arg | Required | Description |
|-----|----------|-------------|
| `<name>` | yes | The vertical's short name. Slugify auto: "Real Estate SFV" → `real-estate-sfv`. |
| `--reference-creator` | optional, repeatable | URL of a reference creator's content (1-3 max). Used in Phase 3 ground-truth seeding. |
| `--icp-sketch` | optional | Path to a rough ICP sketch document if you have one. Skips Phase 1 first half. |
| `--voice-samples` | optional, repeatable | Paths to existing voice samples if you have them. Speeds up Phase 2. |
| `--no-deliverable` | optional flag | Skip Phase 6 (first deliverable). Use when you want infrastructure-only setup. |

---

## Phase 0 — Signal Capture & Slug Validation

**Goal**: Lock the vertical's slug, validate it isn't already registered, capture inputs.

1. Generate slug from name (lowercase, hyphens; reject reserved names).
2. Check existing registries:
   ```bash
   python3 execution/ground_truth.py domains | grep -i "<slug>"
   ```
   If slug already exists → halt and ask whether to extend existing vertical or pick a new slug.
3. Capture: target audience snapshot (1 paragraph), known pain points (3-5), what success looks like for a customer (1 paragraph).
4. Write Phase 0 capture to `projects/<slug>/_working/phase-0-capture.md`.

---

## Phase 1 — ICP Construction

**Goal**: Generate a McRaney-grade ICP profile at identity-resistance level, not demographic level.

1. **Primary**: invoke `/icp-deep-dive` with the Phase 0 capture as input.
2. **Alternative for low-data verticals**: `/mcraney-deep-canvass` (deep canvassing methodology — generates ICP from minimal starting signal).
3. Output: `projects/<slug>/00-foundation/02-icp-master.md`.
4. The ICP must include: identity-level resistance, articulation gap, audience state mapping, language map (use/avoid), bridge message.
5. **Anchor**: register ICP doc via `anchor_memory.py anchor <slug> --type icp --ref-for finalize`.

Stop conditions:
- If ICP draft scores < 7 on Expert Standard via the eval_harness anchor lookup → re-run Phase 1 with sharper Phase 0 capture before proceeding.

---

## Phase 2 — Voice Document

**Goal**: Capture the voice the vertical's owner will use (or BE — for solopreneur verticals where the user IS the brand).

1. Invoke `/voice-document` with:
   - Phase 0 capture
   - Any `--voice-samples` provided
   - ICP from Phase 1 (voice is partly a function of audience)
2. Output: `projects/<slug>/00-foundation/03-voice-document.md`
3. The voice doc must include: voice test (one-sentence question that resolves yes/no), tone calibration anchors, banned patterns specific to this vertical, 3-5 worked examples of voice-true output.
4. **Anchor**: register via `anchor_memory.py anchor <slug> --type voice --ref-for finalize`.

---

## Phase 2.5 — GATE: User Validation (NON-SKIPPABLE)

**Goal**: Halt for user to confirm ICP and voice doc before any downstream calibration writes happen. This gate is load-bearing.

Surface to the user:

```
═══════════════════════════════════════════════════════════════
PHASE 2.5 GATE — Validate ICP + Voice before continuing
═══════════════════════════════════════════════════════════════

ICP Master:    projects/<slug>/00-foundation/02-icp-master.md
Voice Doc:     projects/<slug>/00-foundation/03-voice-document.md

Read both. Then answer:

1. Does the ICP recognize this audience at the identity/resistance level?
   (Not "is the demographic right" — is the WINCE captured?)

2. Does the voice doc produce a "yes" on the voice test for sample lines
   the owner would actually say?

3. Are there cultural / lived-experience claims that need validation by
   someone with that experience BEFORE we generate ground-truth?
   (Per `feedback_naming-cultural-connotation-failure.md`)

Reply with:
   /verticalize continue           → proceed to Phase 3
   /verticalize revise icp         → re-run Phase 1
   /verticalize revise voice       → re-run Phase 2
   /verticalize halt               → stop here, no Phase 3+ writes
═══════════════════════════════════════════════════════════════
```

**Do not auto-advance.** Wait for explicit user signal.

**Skip syntax**: `/verticalize --skip-2.5` is RESERVED for the case where the user is verticalizing a domain they're already deeply expert in and confirms ICP/voice from memory. Per the [workflow gate convention](../../directives/workflow-gate-convention.md), the skip flag must be passed explicitly — not inferred.

---

## Phase 3 — Ground-Truth Seed

**Goal**: Generate 5 expert-grade output samples that anchor calibration for the new domain.

1. Register the domain in ground_truth's registry:
   ```bash
   python3 execution/ground_truth.py init-domain <slug> \
       --description "<from Phase 0 capture>" \
       --expert "<owner or reference creator>" \
       --output-type "<one of the domain's deliverable types>" \
       --output-type "<another>"
   ```
2. For each `--reference-creator` provided in args (1-3): invoke `/extract` to pull their high-signal output samples. Save raw samples to `extractions/<slug>/`.
3. From extractions + voice doc, generate 5 PASS-marked seed samples:
   ```bash
   python3 execution/ground_truth.py add <slug> <sample-file> \
       --expert <name> \
       --type <output-type> \
       --notes "Seed sample; PASS per Farrice taste"
   ```
4. **Critical**: User must approve each sample as PASS before it's added. The 5-sample seed IS the calibration anchor for this domain forever.

Stop condition:
- If fewer than 5 samples reach user-approved PASS, halt. Don't ship a vertical with under-calibrated ground-truth.

---

## Phase 4 — Routing Bindings

**Goal**: Propose entries for `execution/routing_enforcer.py BINDINGS` so the new vertical's signal phrases route correctly.

1. Read existing BINDINGS structure:
   ```bash
   grep -A 5 "^BINDINGS" execution/routing_enforcer.py | head -20
   ```
2. Propose 1-3 new BINDING entries:
   - Signal phrases that should route to this vertical's primary workflow
   - The mandatory workflow (likely a new skill or existing skill within this vertical)
   - Anti-patterns (when NOT to use)
3. Surface the diff to the user for approval. Do NOT auto-edit `routing_enforcer.py` — this is a system-config file.
4. If approved: user copies the suggested entries into the file. Re-run `python3 execution/routing_enforcer.py list` to verify.

---

## Phase 5 — Per-Project CLAUDE.md (Inheritance Contract)

**Goal**: Generate the inheritance contract per the template established by `_active/clients/andrea-dj/CLAUDE.md`, `_active/clients/jen-listings/CLAUDE.md`, and `_active/farrice-brand/CLAUDE.md`.

Required sections (per the 2026-05-12 inheritance contract):

1. **Inheritance declaration** — pointer to root CLAUDE.md
2. **Brand Identity (One Paragraph)** — NOT a duplicate of the brand bible, a one-paragraph anchor
3. **Voice Test** — the one-sentence question that resolves yes/no
4. **When to Load Full Context** — task → context file table
5. **Override List** — where this vertical diverges from root behavior
6. **Anti-Patterns Specific to This Vertical**

Output: `projects/<slug>/CLAUDE.md`.

Also: append a line to the root CLAUDE.md "Per-Client / Per-Project CLAUDE.md Inheritance" table.

---

## Phase 6 — First Deliverable (Optional, default ON)

**Goal**: Produce one real deliverable in the new vertical's voice to test the stack end-to-end.

1. Pick one output type from the domain's `output_types`.
2. Invoke the appropriate single-deliverable workflow. Pass the freshly-generated voice doc + ICP as anchored context.
3. Run `chain_runner.finalize` on the output. The Expert Standard score should be 8+ — if not, the calibration package needs revision.
4. Save to `projects/<slug>/deliverables/first/<output-type>-<date>.md`.

Skip with `--no-deliverable` if user wants infrastructure-only setup.

---

## Phase 7 — Register & Ledger

**Goal**: Final registration + ledger emit.

1. Verify all artifacts exist:
   - `projects/<slug>/00-foundation/02-icp-master.md`
   - `projects/<slug>/00-foundation/03-voice-document.md`
   - `projects/<slug>/CLAUDE.md`
   - `knowledge/expert-benchmarks/<slug>/samples.json` with ≥5 samples
   - 1-3 routing BINDING entries proposed (user-applied state)
   - (if Phase 6 ran) at least one deliverable file
2. Anchor everything via `anchor_memory.py anchor` so future autopilot sessions in this vertical pick up the calibration package automatically.
3. Emit ledger:
   ```bash
   python3 execution/orchestration_ledger.py emit \
       --session-id "verticalize-<slug>-$(date +%Y%m%d)" \
       --project "<slug>" \
       --since "<verticalize_start_time>"
   ```
4. Print the ledger. The "SUGGESTED NEXT MOVES" section will surface the first deliverable + a recommendation to add more samples over time.

---

## The Three Gates

| Gate | Fires when | Why |
|---|---|---|
| **G2** — Paid cost | If Phase 1 ICP research or Phase 3 extraction crosses budget thresholds | Real estate / construction / niche verticals may need Perplexity research |
| **Phase 2.5** — User validation | Always | Load-bearing. Auto-validation = guaranteed grade inflation in the new vertical |
| **G3** — Phase 6 first-deliverable taste check | If the first deliverable goes flagged | Surface for user taste call before declaring the stack "calibrated" |

Everything else is auto-advanced. No "are you sure" mid-flight.

---

## What This Workflow Does NOT Do

- Does NOT replace `/build-bos` for an EXISTING vertical that needs a brand operating system layer. `/build-bos` assumes the vertical is calibrated already; `/verticalize` BUILDS that calibration.
- Does NOT modify `execution/routing_enforcer.py BINDINGS` automatically. Phase 4 PROPOSES — the user applies. This is a system-config file; manual gating is intentional.
- Does NOT skip the 5-sample minimum at Phase 3. Under-seeded ground-truth means the new vertical's quality gate calibrates to noise.
- Does NOT support "verticalize at scale" (5+ verticals in parallel) in v1. Each vertical bootstrap is sequential because Phase 2.5 user-validation is per-vertical.

---

## v1 Scope (2026-05-25)

This is the workflow contract. The full skill implementation (`skills/verticalize/`) lands alongside this file but the workflow's first end-to-end test on a real vertical happens in a follow-on session — testing against a fake "AI-for-construction consulting" target first per the plan's verification section.

Related files:
- Resolver: `execution/intent_to_package.py:_resolve_vertical_bootstrap` (class 10)
- Domain registry: `execution/ground_truth.py:init_domain` + `_REGISTERED_DOMAINS_FILE`
- Inheritance template: 3 existing per-project CLAUDE.md files
- Plan: `/Users/farricecain/.claude/plans/i-think-the-biggest-virtual-emerson.md` Phase C
