# Autopilot Mode — Natural-Language Detection

> **Status**: Mandatory routing binding (mirrored in `execution/routing_enforcer.py` as `autopilot_orchestration`).
> **Workflow**: `.agent/workflows/autopilot.md`
> **Companion modules**: `execution/intent_to_package.py` (outcome → package resolver), `execution/excellence_predictor.py` (pre-flight prediction), `execution/orchestration_ledger.py` (post-run trace emitter), `execution/chain_runner.py` (Wave 1+2+3 calibration enforcement).
> **Plan reference**: `/Users/farricecain/.claude/plans/based-on-all-of-sprightly-whale.md`

When the user's chat input matches an Autopilot trigger phrase below, auto-fire `/autopilot` INSTEAD of routing to a specific workflow. Autopilot is the gate-suppression dispatcher — it composes the right mission package, runs end-to-end without mid-flight halts, and surfaces only taste-level decisions.

This directive defines:
1. **Trigger phrases** — patterns that auto-fire `/autopilot`
2. **The 7 outcome classes** — full taxonomy + signal lexicons
3. **The 3 taste gates** — what stays user-facing and why
4. **Halt suppressions** — what gets internalized per outcome class
5. **Override path** — when to invoke `--manual`

---

## 1. Trigger Phrases

When user input matches any of these patterns, fire `/autopilot`:

### Direct invocation
- "autopilot [intent]"
- "run /autopilot on [intent]"
- "/autopilot [intent]"

### Gate-suppression intent
- "run end-to-end on [X]"
- "ship it end to end"
- "no gates" / "no halts" / "no review steps"
- "just execute [X]" / "stop asking just do [X]"
- "run the full thing"
- "true autopilot"
- "I trust you to run this all the way through"

### Implicit gate-suppression frustration
When user expresses frustration with workflow halt-and-narrate patterns ("why do you keep stopping?", "stop asking me", "just complete the task"), surface `/autopilot` as the offered solution: "It sounds like you want gate-suppressed orchestration — /autopilot is built for that. Want me to run [their intent] via /autopilot?"

---

## 2. The 7 Outcome Classes

Autopilot's Phase 0 calls `intent_to_package.resolve()` which matches the intent against signal lexicons in specificity-descending order. First match wins.

### Class 6 — Refinement / Diagnosis (highest specificity, checked first)
**Signal phrases**: "polish this", "writers room on", "refine this", "diagnose this", "review and fix", "fix this draft", "improve this draft", "tighten this", "rewrite this", "what's wrong with this"

**Primary workflow**: `/writers-room`
**Fan-out**: parallel (5 of 9 expert lenses, diagnosis-only — see Read-Only Constraint below)
**Gates**: G3 (taste call on final prose)

### Class 3 — Research / Intelligence
**Signal phrases**: "research the", "research on", "deep research", "competitive intel", "what's the landscape", "investigate", "study the", "comparative analysis", "literature review", "intelligence brief", "deep dive on", "scan the field", "what are the best"

**Primary workflow**: `/research-swarm`
**Fan-out**: parallel (3-5 angles via parallel_swarm.py)
**Gates**: G2 (if Perplexity cost aggregates above threshold)

### Class 4 — Creative Atomization
**Signal phrases**: "atomize", "remix this into", "platform-adapt", "make derivatives from", "spin this into", "adapt for instagram/linkedin/substack", "multi-format", "across platforms"

**Primary workflow**: `/atomize`
**Fan-out**: sequential by default (write-heavy; Wave 5 v1 constraint) — parallel only with explicit scope isolation
**Gates**: G3

### Class 5 — System / Maintenance
**Signal phrases**: "audit the system", "system audit", "system pulse", "evolve skill", "knowledge compiler", "sync instructions", "maintenance pass", "system hygiene", "compile knowledge", "rebuild index", "system status", "evolution status"

**Primary workflow**: `/system-audit`
**Fan-out**: sequential (deterministic Python ordering)
**Gates**: none (no taste judgment in deterministic operations)

### Class 2 — Multi-Deliverable Mission
**Signal phrases**: "build me a brand for", "build a brand for", "make me a campaign for", "full content drop on", "full marketing for", "launch [product/platform]", "hero shot and listing visuals", "campaign for", "complete brand system", "ugc ad for"

**Primary workflow**: `/supercomputer` (Phase 1 aggregate gate replaced by G2; per-step gates auto-fire under threshold)
**Fan-out**: sequential by default (dependency graph) — parallel only within independent anchor leaves
**Gates**: G2 (paid cost likely > $5 aggregate)

### Class 1 — Single Deliverable Production (multi-subroute)
The resolver checks SPECIFIC sub-class signals first, then falls to generic.

**Subroutes (most-specific first)**:
- **Parallax**: "parallax edition", "parallax substack", "next substack", "parallax prompt pack" → `/parallax` (sequential, Phase 2.5 grounding gate stays load-bearing)
- **LinkedIn from scratch**: "linkedin post from scratch", "draft a linkedin post", "draft one linkedin", "new linkedin post" → `/ghostwrite` + Lara Acosta skill
- **Brand OS**: "brand operating system", "brand os", "build a bos", "full brand system for", "resonance-style package" → `/build-bos`
- **DESIGN.md**: "design.md", "make it look like", "synthesize design", "brand library entry" → `/design-md-synthesize`
- **SEO**: "seo strategy", "seo audit", "search gap analysis", "keyword research" → `/spy-market` + Nathan Gotch
- **VSL**: "vsl", "video sales letter", "build a vsl", "write a vsl" → `/nuclear-vsl` + Luke Iha
- **Generic**: "write me one", "draft a", "draft one", "make one", "create one", "give me a", "produce a" → `/solo` (JCC solo mission, runtime expert selection)

**Fan-out**: sequential (one deliverable, no parallel benefit)
**Gates**: G3 typically

### Class 7 — Freeform / Unclassified
**Trigger**: no signals from classes 1-6 match.

**Primary workflow**: `/big-project` (scaffold + sharpening)
**Fan-out**: sequential
**Gates**: G1 (intent likely needs sharpening)

---

## 3. The 3 Taste Gates That Stay

Only these halt mid-execution. Everything else suppressed.

| Gate | Trigger | Why It's Genuine Taste |
|---|---|---|
| **G1 — Intent Score ≤2** | Phase 0 DICE check finds <3 dimensions (deliverable / audience / constraints / end state / specific language) | System literally cannot infer a mission package from "do the thing." Surface ONE round of sharpening, then proceed. |
| **G2 — Aggregate Paid Cost > $5 OR Single Call > $1** | Phase 1 cost classification | User's money. Surfaces ONCE with full plan, not per-step. Sub-threshold = silent auto. |
| **G3 — Prose FLAGGED at Expert Standard ≥7** | Phase 3 taste-pass check after Phase 2 produces deliverables | Prose classifier identifies AI-pattern slop but cannot judge intentional vs unintentional AI-register. Only the user can. |

---

## 4. Halt Suppressions by Outcome Class

For each outcome class, autopilot suppresses these halts that would otherwise fire from the wrapped workflow:

| Class | Halts suppressed |
|---|---|
| Research | none beyond default (no halts in /research-swarm worth surfacing) |
| Refinement | writers-room phase-boundary halts (the 3 craft layers run internally) |
| Atomization | per-derivative review halts |
| Maintenance | none (deterministic Python doesn't halt) |
| Multi-Deliverable | supercomputer Phase 1 "Proceed?" aggregate gate (replaced by G2); supercomputer per-step paid confirmations within G2-approved budget |
| Single-Deliverable / Parallax | parallax topic-selection halt (`--topic` inferred from intent or anchor memory); parallax raw-take halt (sourced from session context); parallax post-audit approval gate (replaced by G3) — **Phase 2.5 grounding gate STAYS load-bearing** |
| Single-Deliverable / generic | per-step review halts |
| Freeform | none (G1 catches the real gate) |

---

## 5. Override Path

When a specific mission warrants conventional halt-and-confirm gates (high-stakes, novel scope, or first-run validation), use `--manual`:

```
/autopilot "research the agent orchestration landscape" --manual
```

`--manual` restores:
- Per-step paid confirmations (even under G2 threshold)
- Phase-boundary review gates inside wrapped workflows
- Pre-finalize "show me before logging" pause

Use sparingly. Default autopilot behavior (3 gates only) is the intended posture.

---

## 6. Read-Only Fan-Out Constraint (Wave 5 v1)

Critical constraint encoded in `.agent/workflows/autopilot.md` Phase 2 per Cognition's "Don't Build Multi-Agents" thesis: parallel fan-out is restricted to read-heavy phases in Wave 5 v1. Refinement lenses must DIAGNOSE (read-only) — the synthesizer/rewriter is a single sequential pass after fan-in. Atomization and multi-deliverable default sequential until scope-isolation patterns prove out. See Phase 2 of autopilot.md for the full posture matrix.

---

## 7. When NOT to Auto-Fire Autopilot

- User invokes a specific workflow directly (`/parallax`, `/writers-room`, `/build-bos`) — respect explicit routing.
- User asks a question / wants conversation (no deliverable target).
- User is clearly mid-conversation refining something autopilot just produced (subsequent refinement is a separate /autopilot call or direct workflow invocation, not the same dispatcher fanning out again).
- Plan mode is active — autopilot's gate suppression conflicts with plan-then-approve mode by design.

---

## 8. Diagnostics

If `/autopilot` produces unexpected routing:

```bash
# Inspect resolver output for a given intent
python3 execution/intent_to_package.py resolve --intent "<your text>"

# List all signal lexicons
python3 execution/intent_to_package.py classes

# Verify routing binding fires correctly
python3 execution/routing_enforcer.py check --request "<your text>" --workflow autopilot

# Pull recent autopilot ledgers
ls -lt _active/_ledgers/autopilot-*.md | head -5

# Predictor sanity check for a task class
python3 execution/excellence_predictor.py predict --task-class Research --expert researcher
```

---

## 9. Cross-References

- Workflow: [`.agent/workflows/autopilot.md`](../.agent/workflows/autopilot.md)
- Composer: [`execution/intent_to_package.py`](../execution/intent_to_package.py)
- Predictor: [`execution/excellence_predictor.py`](../execution/excellence_predictor.py)
- Ledger: [`execution/orchestration_ledger.py`](../execution/orchestration_ledger.py)
- Gate enforcement: [`execution/chain_runner.py`](../execution/chain_runner.py) Wave 1+2+3
- Routing source-of-truth: [`execution/routing_enforcer.py`](../execution/routing_enforcer.py) BINDINGS `autopilot_orchestration`
- Predictor protocol: [`directives/excellence-prediction-protocol.md`](excellence-prediction-protocol.md)
- Sub-agent fan-out protocol: [`directives/sub_agent_protocol.md`](sub_agent_protocol.md)
- The original ask + design plan: `/Users/farricecain/.claude/plans/based-on-all-of-sprightly-whale.md`
