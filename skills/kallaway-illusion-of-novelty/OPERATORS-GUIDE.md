# Kallaway Illusion of Novelty — Operator's Guide

The system-level view: how the engine composes, what the benchmark proved about its calibration, how quality is enforced, and how to maintain or extend the deployment without breaking it. Companion: `USER-GUIDE.md` (how to use it). Built from the original extraction plus the 2026-07-13 benchmark, flagship, and enrichment sessions.

## 1. The deployment map (three layers)

**Layer A: the front door.** `/novelty-engine` (`.agent/workflows/novelty-engine.md`, mirrored in `.claude/commands/`) conducts the family: load SKILL.md + genius.md, run live-research grounding (Phase 0.5: current-source reveals, dated urgency windows, verifiable proof; the flagship's all-VERIFIED source table is the standard), route by job to the owning workflow, deliver expert-pure. Contract: conductor over existing workflows, never a competing router or super-skill. Grounding procedure: `references/research-grounding-stack.md`; composition spec: `references/orchestration-blueprint.md`.

**Layer B: three canonical modes.** The operator-facing shapes the 13 workflows collapse into:

| Mode | Command | Job | Calibration status |
|---|---|---|---|
| Gut Check | `/novelty-audit` | Score a draft: 3 questions × 5 components + fix list | Honest, restrained, lane-blind (§2) |
| Co-Writer | `/novelty-forge` | Topic → finished asset + component map | Benchmark's convergence test reproduced the human-chosen frame cold |
| Pattern Analyst | `/novelty-pattern` | Winners/losers → niche execution rules | Correctly refuses at N=1; needs real performance data |

**Layer C: à la carte.** 13 workflows in three tiers (4 foundation, 5 practitioner, 4 stacking/system) per SKILL.md, each with a structure-pure v2 prompt in `references/prompts-v2/` carrying its Output Contract, Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor the contract instead of improvising shape.

## 2. The benchmark verdict (the one thing every operator must know)

2026-07-13: 13 workflows × 2 specimens (original vs. Diandra-upgraded post) = 26 runs against Farrice's ranking as ground truth. Report: `_active/linkedin-launch/99-archive/kallaway-novelty-benchmark/00-REPORT.md`. Findings:

- **The scorecard is honest inside its lane.** No workflow forced a component it didn't believe in; six returned clean "ship it"; `/novelty-meta` and `/novelty-pattern` correctly declined to run rather than manufacture output. The over-engineering trap the test was built to catch did not spring.
- **It is lane-blind to body coherence.** Both specimens scored 10/10 Integrity PASS while Farrice ranked them apart. The deciding axis (loop closure, narrative tissue, rhythm) lives between components, not inside any of them. Solution card: `docs/solutions/2026-07-13-novelty-scorecard-lane-blind-to-coherence.md`.
- **The binding routing rule:** original-vs-rewrite and any ceiling-tie quality call routes to `/novelty-to-addictive` (loop integrity) or a prose/writers-room lens. Never break the tie by rerunning the scorecard; a sixth ad hoc component just moves the blind spot.
- **The instrument to watch:** `/novelty-hook`'s raw density score misreads long-form (scored a 10/10 whisper line a 5). It self-corrects in prose; an operator trusting the number over the narrative degrades the post.

## 3. The quality system (how honesty is enforced, not hoped)

- **The 9-criterion rubric** (`genius.md`) with hard vetoes: fabricated fact or proof = auto-fail; fake urgency = auto ≤4; one mascot reveal = auto ≤5; salesy register = cap 6; single-job hook = cap 5. Score ≥8 must name its anchor.
- **The honesty spine, three axes:** never fake the reveal, never fake urgency, never fake proof. The illusion is of *novelty*, never of *facts*. This held across all 26 benchmark runs; every workflow that touched the composite anecdote refused to fabricate a sharper one.
- **Phase 0.5 grounding** feeds the spine: reveals and urgency windows come from live research with VERIFIED/LIKELY/UNCONFIRMED labels, and the flagship's source table shows the required shape, including its DO-NOT-USE row for a cut claim.
- **The standing gates run after, never instead:** `prose_classifier.py check` (slop bank), voice rules per surface, `fact-verifier` on real-world claims, coherence lens per §2.

## 4. Deployment targets (where this earns money now)

- **linkedin-launch / the $5K sprint** (primary). The flagship post is the template: saturated wellness topic, novelty ceiling, dated real urgency, all-VERIFIED claims. Voice layering per §5 before anything ships in Farrice's name.
- **Client work, wellness/performance brands**: Path B angle-mining on categories the client thinks are exhausted; `/novelty-campaign` atomizes the winning angle. Ships expert-pure plus client constraints.
- **Jen's listings**: the reveal + outcome formula as listing hooks (new aspect of the property tied to what the buyer actually wants); respects the Jen hook style card (short, high-energy, objection-in-≤8-words).

## 5. The voice contract (never invert)

The engine's delivery phase is expert-pure Kallaway; that is deliberate. For anything in Farrice's own voice, `_active/farrice-brand/voice/VOICE-CARD.md` plus the voice-os dial (`skills/voice-os/SKILL.md`, default BLEND) layers ON TOP of the finished asset. Architecture and component decisions stay Kallaway's; sentence-level voice is the layer's. Do not blend the voice into the engine's phases, and do not ship engine output raw under Farrice's name.

## 6. Stack order and handoffs

Front end only: this skill manufactures the LOOK, then hands off. `/novelty-to-addictive` automates the retention handoff (kallaway-addictive-storytelling owns the STAY). ICP/avatar skills supply Step 2's held belief and Step 4's viewer-mimic; proof skills deepen Step 4; word-mastery owns the tone execution of Step 5; `/platform-adapt` and `/atomize` scale `/novelty-campaign`. Full matrix in SKILL.md's Stacking Guide and genius.md's Cross-Kallaway Stacking Map. Handoffs are options, never pipeline steps.

## 7. Source ground truth

- **Primary:** Kallaway, "The Illusion of Novelty" (YouTube `LvuoNlYRs7g`, ~20 min, 6,310-word transcript at `extractions/kallaway/transcript.txt`). Verbatim anchors in `genius.md` and `references/source-quotes.md`; never paraphrase as exact quotes.
- **Session-proven exemplars:** the flagship (`_active/linkedin-launch/04-deliverables/content-os/novelty-engine-flagship/FLAGSHIP.md`) and the benchmark's three surviving fixes (close the loop, re-aim the stat, real anecdote over composite) are ground truth for what a passing run looks like in Farrice's domains.
- **Calibration evidence:** the benchmark report + solution card in §2. These are load-bearing; a future session that trusts a scorecard tie is repeating a solved failure.

## 8. Extend-never-rebuild rules

- **Add a workflow (#14+):** write `skills/kallaway-illusion-of-novelty/workflows/novelty-<name>.md` to the house bar → wrapper in `.agent/workflows/` → mirror in `.claude/commands/` → row in SKILL.md tier table + bump `workflows:` count → add the routing branch to `/novelty-engine`'s job list → `python3 execution/sync_registries.py`.
- **Add a v2 prompt:** regenerate via `execution/wire_prompt_pointers.py`; never hand-edit the generated SKILL.md block.
- **Add calibration evidence:** new benchmark or felt-verdict divergence gets a solution card in `docs/solutions/` and a pointer here; do not patch the scorecard to match one verdict.
- **Never:** fabricate to climb the Trust Ladder, bolt urgency onto an evergreen piece, let `/novelty-engine` grow generation logic of its own, or gate extractions (standing decision).

## 9. Failure modes → fixes

| Symptom | Cause | Fix |
|---|---|---|
| Two rival versions both score 10/10 | Lane-blindness (§2) | Route to `/novelty-to-addictive` or a prose lens; never rerun the card |
| Hook lands, body flat | Front end ran without the retention handoff | `/novelty-to-addictive`; check for opened-then-dropped loops first |
| Piece reads salesy despite good substance | Town-crier register | `/novelty-protect` gossip-whisperer rewrite; cut exclamation-point moves |
| Intrigue collapses mid-piece | Mascot reveal (hedge, false modesty, "this is just X") | `/novelty-protect` audit; commit to the storyline |
| Contrast confuses instead of gripping | Not the avatar's actual held belief, or not a true opposite | Reload the avatar payload; re-run `/novelty-contrast` against the named belief |
| Urgency feels bolted-on | No honest window exists | Skip it; four real components beat five with one fake |
| Long-form hook scored low by `/novelty-hook` | Density lens misapplied to essay register | Read the prose diagnosis, not the number (benchmark-documented misread) |
| Claims can't be sourced | Phase 0.5 skipped | Re-run grounding per `references/research-grounding-stack.md`; label everything or cut it |

## 10. Session receipts (evidence, not claims)

- **2026-07-13, benchmark:** 13 workflows × 2 specimens, 26 runs; verdict honest-but-lane-blind; routing rule set; solution card written. Report archived at `_active/linkedin-launch/99-archive/kallaway-novelty-benchmark/`.
- **2026-07-13, flagship:** `/novelty-engine` run on AI answer-engine discovery for wellness brands; 10/10 Gut-Check, coherence pass TRUE, seven VERIFIED claims, one deliberately-open closing rehook. The standing template for sprint posts.
- **Standing:** the composite-founder rule from the flagship (generic peer, never a named real person without permission) applies to every bullseye-proof composite this skill produces.
