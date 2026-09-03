---
description: "/social-repurpose — One finished piece → platform-native posts for a named brand: BRAND LOCK → Scrapes mkt-content-repurposing does the platform mechanics → our ICP-verbatim + voice check per platform → classifier. TEST FIRST vs /atomize (blind bar #3). Never posts."
---
<!-- front door for the vendored Scrapes Skill Systems (2026-09-02). Machinery = .claude/skills/mkt-content-repurposing; seams = ours. Design: _active/harness/scrapes-skill-systems/ORCHESTRATION-DESIGN.md -->

# /social-repurpose — one source, many platforms, one brand

State the scale in one line: source piece → N platforms (name them), one brand.

## Steps
1. **BRAND LOCK** — `.agent/workflows/social-carousel.md` Step 0 (resolve → load canon + last 3 entries under `## mkt-content-repurposing` in `context/learnings.md`). The source piece must belong to the locked brand; a Parallax edition is Farrice's, a listing caption is Jen's. Mismatch → stop and ask.
2. **Source facts** — list every claim in the source with its existing tag; anything untagged gets `claim_audit.py check --strict` before it travels to another platform.
3. **Scrapes mechanics** — invoke `mkt-content-repurposing` with the source text, the target platforms, and `brand_context_path` from BRAND.yaml (it reads `voice-profile.md` and `icp.md` there — never the root one for a client). Output lands under BRAND.yaml `output_base`/mkt-content-repurposing/.
4. **Our check per platform** (one integrator pass, not six seats):
   - ICP verbatim survived (memory: ICP verbatim > pageantry) — the buyer's researched words appear EXACTLY, not paraphrased.
   - Voice: Farrice → VOICE-CARD dial + `execution/voice_evaluator.py check <file>`; client → the brand's `voice.canon` and `pens.veto` read.
   - `python3 execution/prose_classifier.py check <file>` per platform file — FLAGGED never ships.
5. **Blind bar #3 (until decided)** — when the source is a Parallax edition, also run `/atomize` on the same input and hand Farrice both, unlabeled. Log his tap in `context/learnings.md`.
6. **Compound** — learnings entry, `chain_runner.py finalize --skill vendor:mkt-content-repurposing --workflow social-repurpose`, handoff on `<brand>-social`.

## Never
Post or schedule. Literal copy across platforms. Drop a verbatim buyer line for a smoother paraphrase. Edit inside `.claude/skills/*`.
