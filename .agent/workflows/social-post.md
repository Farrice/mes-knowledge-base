---
description: "/social-post — Image-bearing social post (single image or text+image) for a named brand: BRAND LOCK → our pens write the post → claim audit + classifier → Scrapes 00-social-content Scenario A for inference + the visual. Farrice's plain LinkedIn text posts stay on /ghostwrite. Never posts."
---
<!-- front door for the vendored Scrapes Skill Systems (2026-09-02). Machinery = .claude/skills/00-social-content; seams = ours. Design: _active/harness/scrapes-skill-systems/ORCHESTRATION-DESIGN.md -->

# /social-post — one post, one image, one brand

State the scale in one line: one post (platform, single image or text), one brand.

## Steps
1. **BRAND LOCK** — exactly `.agent/workflows/social-carousel.md` Step 0 (resolve → check with `--pool <platform>-single` → load canon + last 3 learnings). Ambiguity asks; never guesses. Plain text LinkedIn post for Farrice with no image → hand to `/ghostwrite` and stop.
2. **Research** — `social-carousel.md` Step 1 when the post carries a fact, number, or named entity; skip for pure opinion in the brand's own experience.
3. **Craft room** — `social-carousel.md` Step 2 with one difference: the deliverable is the post body + one image concept, no slide script. Hook pen → integrator → veto → `claim_audit --strict` → (optional `/tool-humanizer deep`) → `prose_classifier.py check`.
4. **Cost line** — single image: template $0 · AI $0.04–0.19 (GPT) or $0 (Gemini). `openai_budget_guard.py check --n=1` before any GPT call.
5. **Scrapes Scenario A** — invoke `00-social-content` with the finished post + "generate the image for this post"; pass `brand_context_path`, `template_pool`, `output_base` from BRAND.yaml; `--brand-context` on every render call; craft-map master on the image concept before `ssc-image-generator`. Content Studio approval is Farrice's.
6. **Compound** — `social-carousel.md` Step 5 (asset manifest line, learnings entry, `chain_runner.py finalize --workflow social-post`, handoff on `<brand>-social`).

## Never
Post or schedule. Run a client through Farrice's voice card. Let the Scrapes draft phase write the words. Edit inside `.claude/skills/*`.
