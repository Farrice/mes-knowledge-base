---
description: Audit any content against Ocean Vuong's 7-dimension anti-homogenization protocol — detect AI sameness, mimetic defaults, and automatized perception. Prescribe estrangement rewrites.
---

# Anti-Homogenization Audit

Ocean Vuong's content differentiation diagnostic. Catches what the slop detector misses — not just AI vocabulary, but AI *perception*.

## PHASE 1: LOAD EXPERT

Read these files IN ORDER:
1. `skills/ocean-vuong-perceptual-writing/genius.md` — operating principles + voice DNA
2. `skills/ocean-vuong-perceptual-writing/workflows/anti-homogenization-audit.md` — full workflow

## PHASE 2: EXECUTE

Follow the workflow exactly as documented. The workflow contains:
- Pre-Flight Gate
- Anti-Pattern Guard
- 7-dimension audit: Perception, Syntax, Correspondence, Stakes, Reader Space, Cultural Register, Thumbprint
- Homogenization Score (1-10 per dimension)
- Prioritized rewrite prescriptions

## PHASE 3: FINALIZE

Run chain finalize:
```bash
python3 execution/chain_runner.py finalize "Anti-Homogenization Audit" \
    --expert ocean-vuong \
    --skill ocean-vuong-perceptual-writing \
    --workflow anti-homogenization-audit \
    --type Creative \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[what worked, what didn't]"
```

**Execution prompts**: before producing the deliverable, check `skills/ocean-vuong-perceptual-writing/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
