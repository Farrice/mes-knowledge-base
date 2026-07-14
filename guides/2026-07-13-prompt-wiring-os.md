---
date: 2026-07-13
session: prompt-wiring-os
tier: operator-guide
status: enriched
---

# Prompt Wiring OS — What We Built 2026-07-13 and How to Use It

> The session that closed the gap between having ~1,860 refactored crown-jewel prompts and actually *using* them. Every skill now carries verified born-v2 execution prompts, every SKILL.md points at them, a hook surfaces them the moment a skill loads, and every future extraction ships them by gate. Spec: `directives/prompt-forging-spec.md` · proof of why it matters: `_active/prompt-wiring-os-2026-07-13/proof/JUDGMENT.md` · final commit `64fe0e151`.

## ⚡ If you only read 10 lines

- Find a prompt: `python3 execution/prompt_library.py search "<deliverable>" --top 10` — ~7,000 prompts across 360 skills/extractions, keyword-ranked, $0, instant.
- Doctrine line: improvisation is where degradation lives — a matched v2 prompt's Output Contract is a FLOOR (shape, completeness, honesty), never a ceiling on creativity.
- After ANY prompt change the order is fixed: `prompt_library.py build` FIRST → `wire_prompt_pointers.py --write` → `renaissance_audit.py` at 0 fail → commit. Reversed order wires stale data.
- Hard rule: **0 audit fails before any commit that touched prompts** (currently 3,523 audited, 0 fail). Existence is not done-ness.
- Never re-run the backfill: 1,650 born-v2 prompts across 237 skills are DONE; `python3 execution/forge_queue.py --status` returns 0. Renaissance (~1,860 v2s) is also done.
- Never hand-edit SKILL.md pointer blocks — regenerated wholesale by `wire_prompt_pointers.py --write`; hand edits get overwritten.
- The menu hook injects each loaded skill's prompt menu automatically; a shapeless deliverable from a skill you know carries prompts is a miss — call it.
- Fidelity rule: prompts forge only from the skill's own extracted material, never training memory; thin source = fewer, deeper prompts, not padded ones.
- Every extraction now ships its execution layer by gate (Step 5.5 `/extract`, Phase 5.5 `/extract-forge`) — an extraction PR without prompts-v2 is incomplete.
- The one open human task: 40 fidelity-low flags await review (28 nathan-gotch-ai-seo, 3 alex-copper, 5 oscar-hoglund, 2 thrivecart, 1 kittl, 1 samuel-thompson).

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `python3 execution/prompt_library.py search "proof ladder" --top 10` | Ranked matches with path, skill, kind, opening gist | You know the deliverable but not which expert owns it |
| `python3 execution/prompt_library.py build` | Rebuilt `.agent/prompt-index.json` | FIRST step after any prompt change; fresh forges are invisible until rebuild |
| `python3 execution/prompt_library.py stats` | Index coverage numbers | Checking library health |
| `python3 execution/prompt_library.py orphans` | Prompts nothing points at | Hunting wiring gaps |
| `wire_prompt_pointers.py --write` | Regenerated SKILL.md pointer blocks | SECOND — always after the index rebuild |
| `python3 execution/renaissance_audit.py` | Structural audit report over every v2 file | Before any prompt-touching commit (must read 0 fail) |
| `python3 execution/renaissance_audit.py --delete` | Deletes failures so the queue re-includes their originals | Cleaning hollow files after a failed audit |
| `python3 execution/forge_queue.py --status` | Backfill queue count (should be 0) | Verifying the backfill stays closed |

---

## The mental model (read this once, everything else follows)

Three ideas run through everything wired:

1. **Improvisation is where degradation lives.** A skill gives the model the expert's *thinking*; without an execution prompt, the model improvises the *output shape* every run — and that improvisation is the source of the run-to-run quality wobble you felt. The A/B proved it: same skill, wired take was the clear win.
2. **High floor, unlimited ceiling** (your binding design principle, in the spec). The Output Contract and Skeleton are a FLOOR — shape, completeness, and honesty become deterministic, so no run comes back malformed, padded, or fabricated. They never cap the ceiling: no prompt constrains word choice, angle, or creative leaps beyond what the expert's own methodology demands. A v2 that reads like a fill-in-the-blanks form has *failed* the spec even if it passes the audit.
3. **Prompts nothing loads don't exist.** Before this session, 13 of 357 SKILL.mds referenced their prompts — thousands of battle-tested assets, orphaned. The wiring layer (index → pointer blocks → load-time hook) makes discovery deterministic, not memory-dependent.

---

## 1. Born-v2 structure-pure prompts — the asset itself

### What it is

One prompt per **distinct deliverable** a skill produces (typically 4-10 per skill), at `skills/<skill>/references/prompts-v2/<slug>.md`, frontmatter `forged: born-v2`. "Born v2" means it never had a fabrication era — nothing to strip later. Required anatomy, audit-enforced:

| Section | What it does for you |
|---|---|
| **Role & Activation** | The expert's real frame — only credentials corroborated by their corpus, no invented stats |
| **Input Required** | `[BRACKET]` architecture — you see exactly what to hand it |
| **Execution Protocol** | The skill's ACTUAL methodology at full depth, lifted from SKILL.md/genius.md/workflows — never thinned, never invented |
| **Output Contract** | Exact deliverable components, format, length bounds |
| **Output Skeleton** | Code-fenced SHAPE specimen — placeholders only, never sample copy posing as output |
| **Quality Gate** | 3-6 checkable yes/no criteria the expert would check |
| **Creative Latitude** | Names exactly where to push past the skeleton — load-bearing, not decoration |
| **Deploy When** | Trigger scenarios |

### When to reach for it

Any time a deliverable you're asking for matches a listed prompt: the contract guarantees the shape, the protocol carries the expert's real method, and the latitude section keeps the ceiling open.

### When NOT to

Genuinely novel deliverable shapes with no matching prompt — run the skill's workflow normally. Don't force-fit a prompt whose Deploy When doesn't match; a wrong contract is worse than an honest improvisation.

### Honest edge

The **fidelity rule**: prompts are forged only from the skill's own extracted material — never from training memory about the expert (that's how generic 5/10 skills happen). Thin source means fewer, deeper prompts, not padded ones. So some skills legitimately carry 3 prompts, not 10.

---

## 2. The prompt library — finding a prompt for a deliverable

### What it is

A deterministic keyword index (`.agent/prompt-index.json`) over every prompt population in the system — currently ~7,000 prompts across 360 skills/extractions. No LLM, $0, instant.

### How to invoke — copy-paste examples

```
python3 execution/prompt_library.py search "proof ladder" --top 10
python3 execution/prompt_library.py stats
python3 execution/prompt_library.py build
python3 execution/prompt_library.py orphans
```

### Worked example

`search "proof ladder" --top 3` returns 225 matches, ranked — top hit *Luke Iha — Proof Ladder Strategy* at `skills/luke-iha-proof-ladder/references/prompts-v2/proof-ladder-strategy.md`, with skill, kind (`prompt-v2`), and an opening gist so you can judge fit before reading. That's the day-to-day move when you know the deliverable but not which expert owns it: search, read the winner, honor its contract.

### When NOT to

Don't use search as a routing substitute — the Chain still routes to experts first. The library is for *within* a routed session ("which of this system's prompts builds X?") or for cross-skill discovery.

### Honest edge

Keyword ranking, not semantic — try two phrasings before concluding nothing exists. And `build` only reads what's on disk: a freshly forged prompt is invisible until you rebuild.

---

## 3. SKILL.md pointer blocks + the load-time menu hook

### What it is

Two layers that make discovery automatic. **Pointer blocks**: every SKILL.md with v2 prompts carries a generated `<!-- BEGIN:execution-prompts -->` section listing each prompt (title + path) — see `skills/sean-dollwet-kdp-publishing/SKILL.md` for the shape: "7 deterministic practitioner prompts… When a deliverable matches one, Read it and honor its contract instead of improvising the output shape." **Menu hook**: `execution/hooks/prompt_menu_hook.py` (PostToolUse on SKILL.md reads) injects the same menu the moment any session loads a skill — up to 8 lines, near-zero tokens, prompt bodies read on demand.

### When to reach for it

You don't. Both fire automatically. Your part is downstream: when a session says it's honoring a prompt's contract, that's the system working; when an expert deliverable arrives shapeless from a skill you know carries prompts, that's a miss — call it.

### When NOT to

Never hand-edit the pointer block (the marker says so) — it's regenerated wholesale by `wire_prompt_pointers.py --write`, and hand edits get overwritten.

### Honest edge

The hook also flags prompt-less skills at load time (the lazy-backfill signal), so gaps stay visible instead of silent. A flag on an archived or deliberately thin skill is information, not a to-do.

---

## 4. The forging gate — every extraction ships its execution layer

### What it is

Born-v2 forging is now a **non-optional phase** of extraction: Step 5.5 in `/extract`, Phase 5.5 in `/extract-forge`, plus the gate appended to five more skill-producing workflows. The standing rule from the spec: *a skill without prompts is half-finished work* — the model gets the expert's thinking but has to improvise the output shape forever after.

### When to reach for it

Automatically, whenever you extract. Nothing to invoke — but when reviewing a fresh extraction, the prompts-v2 directory is now part of what "done" means. An extraction PR without one is incomplete.

### Honest edge

Voice-adjacent skills forge with a contract-level VOICE-CARD.md + dial-mode line from birth (binding `farrice_voice_alignment`), and jam verdicts repeated across 2+ jams get promoted into Quality Gates at `/weekly-closeout` Step 5.5 — one-off verdicts never patch prompts directly. The taste ratchet compounds slowly by design.

---

## 5. `renaissance_audit.py` — the 0-fail gate

### What it is

The deterministic quality gate over every v2 file (currently 3,523 audited, 0 fail). Checks: the three required sections present, ≥20 lines, no stub markers (including the template-slop fingerprints from the 2026-07-11 rogue-Haiku incident), correct `structure-pure-v2` frontmatter.

### How to invoke

```
python3 execution/renaissance_audit.py            # report failures
python3 execution/renaissance_audit.py --delete   # delete failures so the queue re-includes their originals
```

### The rule

**0 fail before any commit that touched prompts.** Existence is not done-ness — the audit exists precisely because a concurrent session once poisoned the skip-if-exists queue with files that existed but were hollow (solution card: `docs/solutions/2026-07-11-concurrent-writer-queue-poisoning-quality-gate.md`).

### Honest edge

It audits structure, not fidelity — a prompt can pass while being thinner than its source deserves. Fidelity is the forger's honesty plus your review, which is what the 40 flags below are.

---

## 6. Maintenance rules (the part that keeps this from rotting)

- **Never re-run the backfill.** It's DONE: 1,650 born-v2 prompts across 237 skills, 100% content-verified, 2.3% caught and repaired. `python3 execution/forge_queue.py --status` returns 0. Same for the Renaissance itself (~1,860 v2s, complete 2026-07-11).
- **Index-then-pointers order, always.** After ANY prompt change: `prompt_library.py build` FIRST, then `wire_prompt_pointers.py --write`, then `renaissance_audit.py` at 0 fail before commit. Pointers are generated *from* the index — reversed order wires stale data.
- **40 fidelity-low flags await your review** (paths in the wave commit bodies): 28 in nathan-gotch-ai-seo (whole skill thin — source re-watch candidate), 3 alex-copper, 5 oscar-hoglund, 2 thrivecart, 1 kittl, 1 samuel-thompson. Reviewing these is the one open human task from the project.
- **Verifier lesson**, banked in the spec: legitimate forging/verifying sources include `workflows/*.md` and same-expert `.agent/workflows/<prefix>-*.md` files outside the skill folder — missing that scope was the #1 cause of false fidelity flags.

---

## How it all chains — one deliverable, end to end

```
you ask for an expert deliverable
   ▼
Chain routes → skill loads (Tier 1/2)
   ▼
prompt_menu_hook injects the v2 menu automatically
   ▼
deliverable matches a listed prompt? ──yes──► Read it · honor Output Contract
   │                                          · push inside Creative Latitude
   no
   ▼
run the workflow normally (and note the gap —
new extractions can't have this gap; the gate forges at birth)
   ▼
Chain Step 6 finalize as usual
```

*Created 2026-07-13 (Prompt Wiring OS session). Extend this guide as the layer evolves — don't let it sediment.*
