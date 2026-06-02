---
description: Generate market hooks via the Maze Metaphor (What/Who/How x dimension combos) and Bootleg Hook Theory, mapped to pain dimensions
tier: 2
stacks_with: luke-iha-vicious-hooks, luke-iha-copy-blocks, diandra-headline-engineer
---

# Maze Hooks & Market Pick-Up Lines

Generates attention hooks ("market pick-up lines") using the Maze Metaphor — every market is a maze; a hook is a snapshot of one element. Each hook is tied back to the pain dimensions it activates.

## Pre-Flight Gate
- Best with a completed Pain Matrix (so hooks map to real dimensions) and Epiphany Threshold set (so hooks land in the Goldilocks Zone).
- Hooks must not clash with Identity (genius.md Pattern 3) — check against `/resonance-hierarchy` lead-conflict flags.

## PHASE 0 — GROUND (auto-fires; skip with `--no-ground`)
Per `references/research-spine.md`. Hooks must map to angles that ACTUALLY circulate and win in this market — FB Ad Library is the primary source.
- If the dossier exists, read the Live Hooks section of `voc-pack.md`.
- Standalone & not `--no-ground` — route market grounding through the ONE chokepoint first (reuse = **$0**; its VOC pack already carries a hook bank), then harvest live hooks via the FREE model-side path:
```bash
// turbo
python3 execution/avatar_manifold_runner.py ground --slug <slug> --market "<market>" --tier deep 2>/dev/null \
  || echo "DEGRADE → mcp__recall__search; map hooks to [MODELED] angles"
```
- Model-side (primary, FREE): `mcp__playwright__browser_navigate` → `facebook.com/ads/library` → `browser_snapshot` to harvest live winning ad angles ($0). Map each generated hook to a real circulating angle + the pain dimension it activates. (Only if the cached `voc-pack.md` hook bank is thin AND you need TikTok/YouTube scale, fire ONE `apify_client.py` pull — but the cached dossier + free FB Ad Library usually suffice.)

## Skill Acquisition
Load `references/framework-library.md` § F (Maze types, dimensions, 32 combos, Bootleg theory, curiosity generators). Optionally `source-prompts/maze-hook-theory-prompt.md`. Load genius.md Pattern 9.

## Execution
1. **Choose hook types** — What (problem/situation) · Who (entities/authorities) · How (process). Cover all three.
2. **Apply dimensions** — Time · Specificity · Scale · Conflict · Insight · Center/Edge · Accepted/Not-Accepted · Status · Narrative · Number · Perspective. Vary combos (the 32 significant pairings).
3. **Generate 10–15 hooks.** For each, annotate: hook type + the pain dimension(s) it activates + the curiosity generator used.
4. **Bootleg pass** — also produce a Problem + {What/Who/How} set ("The Truth About X" / "What [authority] gets wrong about X" / "3 [things] that…").
5. **Goldilocks filter** — kill any hook below the Epiphany Threshold or above the BS Limit.
6. **Curiosity audit** — prefer authority-vs-authority conflict, "popular theory is wrong," live > past, extreme edge > center, genuine insight.

## Content Type Adaptations
| Platform | Lean |
|---|---|
| FB/IG paid | What + Conflict + Number; emoji-friendly (see meta-prompt templates) |
| YouTube | Who + High Status + Narrative |
| Email subject | Specificity + Hidden Factor |
| Short-form video | Edge + Not-Accepted + live |

## Output Requirements
- 10–15 annotated hooks (type · pain dims · curiosity generator).
- A Bootleg set. All inside the Goldilocks Zone.

## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-avatar-machine --workflow market-pickup-lines \
  --type Analysis --intent N --expert-score N --adversarial N --factual N \
  --notes "Factual Grounding: N | Verification: PASS|N/A | Cache: WARM|COLD"
```
If the output contains stats / prices / dates / named entities, FIRST build a proof-claims ledger and run the deterministic G5 gate (see `/copy-engine` Phase 5):
```bash
// turbo
python3 execution/verify_proof_ledger.py --draft <draft-file> --ledger .tmp/copy-engine/<slug>/proof-claims.md || echo "label/cut claims before delivery"
```
Grep finalize output for `QUALITY GATE BLOCKED` and do NOT deliver on a match (finalize exits 0 even when it blocks).

## Quality Gate
Hooks tie to real pain dimensions and stay in the Goldilocks Zone; types are varied (not all "How"). Auto-fail: hooks clashing with Identity; generic hooks with no dimension mapping; everything one hook type.
