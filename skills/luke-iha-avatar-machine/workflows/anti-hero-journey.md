---
description: Reverse-engineer the emotional backstory arc (Garden of Eden, Slow Descent, Fall of Man/PIG Story, Dark Night) calibrated to the market's consciousness level
tier: 2
stacks_with: luke-iha-vsl-leads, wright-thompson, eric-roth
---

# Anti-Hero's Journey Architect

Builds the emotional backstory that makes a sales narrative *move* people — by substituting the product/mechanism for the classic Hero's-Journey epiphany (the "Energetic Changeling"), calibrated to where the market sits on the consciousness ladder.

## Pre-Flight Gate
- Need the Core Wound (run `/core-wound`) and ideally Pain Matrix — the arc is *reverse-engineered from the avatar.*
- Pick the consciousness level first: **Victim / Hybrid / Accountability** (genius.md Pattern 7). It changes who carries responsibility (product vs. inner transformation) and the tone.
- This stage gathers narrative *resources* (for images, sales letters, testimonials, analogies) — not necessarily finished copy.

## PHASE 0 — GROUND (light — sensory texture only; heartbeat-protected)
Per `references/research-spine.md`. This is a PROSE stage. It is reverse-engineered from the already-grounded Core Wound + Pain Matrix — do NOT re-derive structure from research. Pull only *verbatim sensory texture* so the Garden/Dark-Night scenes use the market's real phrases, not AI-clinical language:
- If the dossier exists, mine `voc-pack.md` for vivid, concrete, first-person phrasing (the "what she'd tell a friend over wine" register).
- Standalone: skip new research unless the Core Wound is missing (then run `/core-wound` first).
> Guardrail: research feeds *texture*, never *structure*. Over-structuring this stage produces clinical prose (genius.md auto-fails "summarized beats instead of written scenes"). Write scenes.

## Skill Acquisition
Load `references/framework-library.md` § G (the full structure + PIG guidelines). Load genius.md Pattern 7, Exemplar 3 (Dark Night).

## Execution
1. **Set consciousness level** → note responsibility split + market/price implications.
2. **Garden of Eden** — vivid ideal state = the *reverse* of the Core Wound. Nostalgic, sensory, relatable, hints at coming loss.
3. **Slow Descent & False Idols** — gradual worsening + the failed solutions ("False Idols") from the Pain Matrix; emotional + interpersonal consequences; end on a cliffhanger.
4. **Fall of Man (PIG Story)** — the humiliating public collapse. Apply the 4 guidelines: add Stakes (public/important) · add Delusion (top of the world → rug pulled) · reflect the Core Wound directly · make people *real*, not cartoon villains.
5. **Dark Night of the Soul** — explicit confrontation with the Core Wound; isolation, mounting desperation, open-ended ache that demands a solution.
6. *(Optional)* **Part 2 beats** — A New Hope → Guru → Epiphany/Insight/Mechanism → Initial→Final Results → A World Redeemed (for the post-mechanism half of a sales letter).

## Content Type Adaptations
| Asset | Use |
|---|---|
| VSL / long sales letter | Full Pt 1 up front, Pt 2 after the mechanism |
| Short ad / email | Compress to Garden→Fall→Dark Night in 4–6 lines |
| Testimonial structure | Map a real customer story onto the beats |
| Image / thumbnail concept | Mine the PIG Story moment for the visual |

## Output Requirements
- Consciousness level + responsibility note.
- All four Part-1 beats as written passages (not bullet summaries).
- PIG Story explicitly hitting the 4 guidelines.

## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-avatar-machine --workflow anti-hero-journey \
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
Beats must be *written prose*, reverse-engineered from the actual Core Wound (not generic). PIG Story must have real stakes + real (non-cartoon) antagonists. Auto-fail: arc that doesn't reflect the market's specific wound; summarized beats instead of written scenes; consciousness level ignored.
