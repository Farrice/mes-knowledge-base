---
description: Gate-suppressed orchestration dispatcher. Composes the right mission package, runs end-to-end without mid-flight halts, surfaces only taste-level decisions. Skinny Wave-4 version — Research outcome class populated; Wave 5 fills the rest.
---

# `/autopilot` — Gate-Suppressed Orchestration

The dispatcher that takes fuzzy intent and runs the whole chain WITHOUT requiring you to review, copy-paste, or implement intermediate steps. Everything internal except three taste gates (G1/G2/G3).

This workflow is the wave-4 skinny version. It populates the Research outcome class end-to-end and stubs the other six. Use `/research-swarm`, `/writers-room`, `/supercomputer`, `/atomize`, etc. directly for the unsupported classes until Wave 5 ships.

## Quick Start

```
/autopilot "research the current state of agent orchestration frameworks"
/autopilot "competitive intel on personal-brand ghostwriting at the $5k+ tier"
/autopilot "deep research on Karpathy's autoresearch loop"
```

Implicit invocation: any user request matching `routing_enforcer.BINDINGS` `autopilot_orchestration` signal phrases routes here automatically.

## Args

| Flag | Required | Purpose |
|---|---|---|
| `<intent>` (positional) | yes | Free-text intent |
| `--project <slug>` | optional | Project slug for anchor memory write-back |
| `--manual` | optional | Restore conventional halt-and-confirm gates (override the gate-suppression contract) |
| `--no-predict` | optional | Skip the Wave-3 excellence predictor pre-flight (debug) |
| `--since <iso>` | optional | Ledger window start; defaults to one hour ago |

---

## Phase 0 — Intent + Package Resolution

**Goal**: take fuzzy intent in, emit a sealed mission package out. One gate (G1) only fires if the intent is unsalvageable.

1. Capture raw intent.
2. Generate session id:
   ```
   autopilot_session_id = "ap-{YYYYMMDDHHMMSS}-{slug-of-intent[:24]}"
   session_started_at = ISO timestamp now
   ```
3. Score intent with the DICE method internally (no user-facing message yet):
   - +1 Deliverable named
   - +1 Audience named
   - +1 Context/constraints
   - +1 End state described
   - +1 Specific language
4. **Gate G1 — Intent score ≤2**: if so, surface ONE round of sharpening per `CLAUDE.md` Step 2. Otherwise proceed silently.
5. Resolve mission package:
   ```bash
   python3 execution/intent_to_package.py resolve --intent "<intent>" --json
   ```
   Parse the JSON. The `outcome_class`, `primary_workflow`, `sub_workflows`, `skills_to_load`, `cost_tier`, `fanout_pattern` drive everything from here.
6. **Wave 4 skinny mode**: if `outcome_class == "freeform"`, the resolver fell through. Tell the user explicitly which workflow to invoke directly (the reasoning string carries the hint), then exit. Do NOT silently run /big-project under the autopilot banner — that's a Wave 5 capability.
7. Verify against routing bindings:
   ```bash
   python3 execution/routing_enforcer.py check --request "<intent>" --workflow <primary_workflow> --quiet
   ```
   If non-zero exit, surface the binding violation and let the user override.
8. Run Wave-3 pre-flight prediction (skip if `--no-predict`):
   ```bash
   python3 execution/excellence_predictor.py predict \
       --task-class <inferred-task-class> \
       --expert <package.experts[0] or ''> \
       --skill <package.skills_to_load[0] or ''> \
       --workflow <package.primary_workflow> \
       --signals '{"output_length_estimate": <est>, "factual_surface": <bool>}' \
       --json
   ```
   Parse the prediction. Apply its `recommended_interventions` to the upcoming run:
   - "front-load /adversarial-review" → schedule it after first draft inside Phase 2
   - "require /writers-room before execution" → run /writers-room as the first Phase-2 step
   - "load skills/<skill>/genius.md tier 2" → load it now, before Phase 2
   - "spawn adversarial sub-agent" → add to fan-out list
   - "activate verification-agent-protocol upfront" → set `verification_upfront = True` for Phase 4
   - "exploration mode" → log but don't gate
9. State the plan to the user, ONE line:
   ```
   Autopilot engaged. Outcome: <class>. Workflow: /<primary>. Predicted composite: <X.X> / iterations: <N>. Session: <id>.
   ```

---

## Phase 1 — Pre-flight (cost gate G2 only)

**Goal**: classify cost; surface a single aggregate gate if needed. Sub-threshold = silent auto-approve.

1. If `package.cost_tier in ("free", "cheap")` AND no individual paid step is anticipated: skip the cost gate entirely. Note in ledger as "G2 not tripped".
2. Else, for each anticipated paid step, run cost classification:
   ```bash
   python3 execution/creative_router.py route --kind <type> --intent "<intent>"
   ```
   Aggregate the predicted cost.
3. **Gate G2**: if aggregate > $5.00 OR any single call > $1.00, surface ONCE with the full plan:
   ```
   This mission will spend ~$X.XX across N paid steps:
     - <step 1>: ~$0.YY
     - <step 2>: ~$0.YY
   Proceed?  (y / cancel)
   ```
   Sub-threshold = silent.
4. Initialize anchor memory if `--project` was set and the slug doesn't yet have a state file:
   ```bash
   python3 execution/anchor_memory.py init <slug> --brand-name "<derived>" --audience "<derived>"
   ```
5. Load existing anchor context if the project does exist:
   ```bash
   python3 execution/anchor_memory.py load <slug>
   ```
   Inject the markdown into Phase 2 prompts.

---

## Phase 2 — Execute

**Goal**: run the package's primary workflow + any sub-workflows in the prescribed fan-out pattern. NO mid-execution gates.

### Wave-4 Research path (the only fully implemented one)

If `outcome_class == "research"`:

1. The package recommends `/research-swarm` parallel-research. Invoke it via existing infrastructure:
   ```bash
   # 3-5 research angles fan out via parallel_swarm.py
   python3 execution/parallel_swarm.py "<intent>" --grounded --research
   ```
   (Or invoke `/deep-research-gemini` if the request signals "deep" + the Gemini Ultra quota is healthy per `directives/google-api-usage-policy.md`.)
2. Each parallel worker:
   - Gets a sealed sub-prompt with the relevant Recall card injection (Tier 1.5 grounding fires automatically per `directives/recall-grounding-protocol.md`)
   - Produces a deliverable to `.tmp/autopilot/<session_id>/research-angle-<N>.md`
   - Returns a compact summary (300-500 tokens)
3. Main thread anchors all returned outputs:
   ```bash
   python3 execution/anchor_memory.py anchor <slug> \
       --type research_brief \
       --path <relative path> \
       --desc "<one-line description>" \
       --ref-for finalize \
       --phase "Phase 2 research"
   ```
4. Run synthesis pass: combine the 3-5 parallel outputs into a single research brief. Save to `research_outputs/<slug-or-topic>-<date>.md`.

### Other outcome classes (Wave 5)

For now, autopilot.md's Wave 4 stub mode applies — the intent_to_package resolver tells the user which workflow to run directly. Wave 5 will populate these phases here.

---

## Phase 3 — Taste Pass (G3 only)

**Goal**: run automated checks; surface ONLY taste-level prose decisions.

1. For each text deliverable produced in Phase 2:
   ```bash
   python3 execution/prose_classifier.py check <path>
   ```
2. **Gate G3**: if ANY deliverable returns `verdict == "FLAGGED"` AND the prediction said this task class typically scores `expert_standard ≥ 7`, surface the flagged file side-by-side with the rubric:
   ```
   Deliverable <path> flagged as AI-prose (ai_score X/10).
   Was this an intentional AI-register choice or unintentional drift?
     - "intentional" → ship as-is, note in finalize
     - "fix" → auto-invoke /writers-room before finalize
     - "show me" → display the offending signals + recommendation
   ```
3. Otherwise: silent pass.

---

## Phase 4 — Finalize

**Goal**: run `chain_runner.finalize` for each deliverable. Last call carries the ledger trigger.

1. For each deliverable:
   ```bash
   python3 execution/chain_runner.py finalize "<output-description>" \
       --expert <expert> \
       --skill <skill> \
       --workflow <workflow> \
       --type <task_type> \
       --intent <self-scored 1-10> \
       --expert-score <self-scored 1-10> \
       --adversarial <self-scored 1-10> \
       --factual <self-scored 1-10 OR omit for N/A> \
       --anchor-named   # only if you can name the rubric anchor for any 8+ score
       --notes "<what worked, what didn't>" \
       --project <slug if set> \
       --trace
   ```
   Note: Wave 1+2 caps fire automatically. Wave 3 grade-inflation detector fires automatically. If the system caps your composite, that's the bimodal taste signature working — accept the lower score.
2. If `verification_upfront` was set in Phase 0 (because the predictor flagged factual_surface): run `/verification-agent` BEFORE the finalize, not after.
3. The LAST finalize call should include any final session metadata.

---

## Phase 5 — Ledger (run ends)

**Goal**: emit the orchestration ledger, end the run. NO interrogative.

1. Generate ledger:
   ```bash
   python3 execution/orchestration_ledger.py \
       --session-id "<autopilot_session_id>" \
       --since "<session_started_at>" \
       --project "<slug if set>"
   ```
2. Print it inline. The ledger archives to `_active/_ledgers/autopilot-<session_id>.md` automatically.
3. **End the run.** Do NOT ask "what next?" or "want to refine?" — the ledger's "COPY-PASTE REFINEMENT PROMPTS" section already answers that. The user reads, chooses, and fires what they want, or doesn't.

---

## The Three Gates That Stay

| Gate | Fires when | Why it's genuine taste |
|---|---|---|
| **G1 — Intent ≤2** | DICE score after Phase 0 step 3 | Missing deliverable/audience/constraints — autopilot can't infer the package. One sharpening round, then proceed. |
| **G2 — Aggregate cost > $5 or single call > $1** | Phase 1 step 3 | The user's money. Surfaces ONCE with full plan, not per-step. |
| **G3 — Prose FLAGGED at Expert Standard ≥ 7** | Phase 3 step 2 | Prose classifier identifies AI-pattern slop; can't judge intentional vs unintentional AI-register. Only Farrice's taste can. |

Everything else suppressed:
- Supercomputer's Phase 1 "Proceed?" gate
- Parallax's topic-selection halt
- Per-step paid confirmations within G2 budget
- Big-project's session-boundary suggestion
- Any "want to continue?" mid-flight prompt

Use `--manual` to restore conventional gates if a specific mission warrants extra caution.

---

## What This Workflow Does NOT Do

- Does NOT support outcome classes 1, 2, 4, 5, 6 in Wave 4. The resolver tells you which workflow to invoke directly for now. Wave 5 fills these in.
- Does NOT modify any existing system workflow. /research-swarm, /parallax, etc. stay as-is. Autopilot calls them.
- Does NOT skip `chain_runner.finalize`. Quality scoring is non-negotiable — the gate suppression is about HALT behavior, not measurement behavior.
- Does NOT create new agents in `.claude/agents/` (those were removed 2026-05-02 per `feedback_no-claude-code-subagents.md`). Fan-out uses parallel Agent tool calls from the harness when phases allow.
