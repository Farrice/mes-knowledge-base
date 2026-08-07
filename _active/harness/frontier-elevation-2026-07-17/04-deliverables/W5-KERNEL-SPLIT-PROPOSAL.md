# W5 First Slice — Kernel vs Personal Split (PROPOSAL, awaiting Farrice's nod)

**2026-07-18, Fable conductor.** The productize-as-IP foundation: what ships to any
client/machine unchanged (KERNEL), what is only-Farrice (PERSONAL), what a client gets
as an overlay. Rule of thumb applied throughout: **kernel = mechanisms that earned their
place through caught failures; personal = anything carrying voice, taste, clients, or
identity.** When a file mixes both, the mechanism goes kernel and the examples stay
personal.

## KERNEL (portable — ships to every install)
- **The Chain** (CLAUDE.md's 6-step spine, stripped of Farrice-specific routes) +
  `directives/constitution-core/` grown into the real shared spine
- Execution spine: `chain_runner.py`, `skill_auditor.py`, `fleet_merge.py`,
  `mission_validator.py`, `mission_runner.py`, `session_lock.py`, `routing_enforcer.py`,
  `prose_classifier.py`, `knowledge_compiler.py`, `memory_facade.py` (store paths
  parameterized), `handoff_store.py`, eval harness
- Doctrine directives (mechanism, not taste): merge-discipline, fleet-conductor-doctrine,
  worker-envelope-standard, orchestration-doctrine, quality_gate, verification-agent-
  protocol, ai-slop-ban-bank (the CHECKS; the 64 entries are arguably personal-taste —
  propose: structure kernel, bank contents overlay-editable), afk-mission-runner
- The rubric STRUCTURE (rubric_v1.md anchors-as-format) and hook wiring contract
- MES 3.0 extraction machinery + skill/workflow/genius.md conventions (the format, zero
  extracted experts)

## PERSONAL (never ships — `personal/` layer)
- All 371 `skills/` extractions and `agents/` (they encode Farrice's curation),
  FARRICE-MASTER-CONTEXT.md, voice/ (VOICE-CARD, PLATFORM-NARRATIVE-CARD), thought-bank
- `evolution_store/ground_truth/eval_set_v1.jsonl` — **the calibrated judge IS
  Farrice's taste**; a client install starts with an EMPTY eval set and earns its own
  (the seeder + REVIEW-PROTOCOL ship kernel-side as the mechanism)
- All client folders (`projects/`, `_active/*-brand`, jen/andrea/josh overlays), offers,
  strategy_briefs, memory stores (sovereign.db, episodic), Notion/Recall wiring + keys,
  budget trackers, missions/handoffs/telemetry under `.agent/`
- MEMORY.md + ~/.claude memory (by definition)

## CLIENT OVERLAY TEMPLATE (`distro/client-overlay-template/`)
Empty-but-shaped: CLIENT-CONTEXT.md (their FARRICE-MASTER equivalent) · voice/VOICE-CARD
template · one starter CLAUDE.md that declares inheritance from kernel · empty eval set +
seed protocol · offers/ scaffold · anti-patterns bank starter. Install story: kernel +
overlay compose into a working build (accept test: scratch overlay boots on Codex).

## The three judgment calls I want your nod on
1. **Eval set is personal** (client judges start empty) — even though it makes the kernel
   demo less impressive out of the box. Alternative: ship 5 anonymized structural
   exemplars. My call: personal, no exceptions — your taste is the moat.
2. **Slop-ban bank**: check-mechanism kernel, 64-entry bank starts as a COPY clients may
   edit (taste diverges by brand). 
3. **Skills ship empty**: the kernel includes the extraction ENGINE, zero experts —
   clients watch their own sources (feedback memory: watch-to-embody; transcript-only
   extractions grade 5/10 anyway).

Nod = "approved" (or flip any of the 3) → next session scaffolds `distro/` +
constitution-core growth + platform_compiler v2 pilot on AGENTS.md per PLAN.md.

## AMENDMENT (Farrice, 2026-07-18) — the 90%-done handoff via Intake Interview
Judgment call #3 refined, not flipped: clients never receive Farrice's extracted experts,
but the overlay must not FEEL empty. The client overlay template gains a **Foundry Intake
flow** — a structured interview (built on the existing /go + geoff-woods thought-partner +
avatar-machine Phase-0 machinery, one question at a time) that grills the new owner for
the missing 10%: who they are, their voice, their clients, their domain, their watch-list
of source experts. The system then builds their personal layer FROM the answers — kernel
+ interview = a system that arrives 90% done and finishes itself specifically for them.
This is the install story W5 scaffolds next session.
