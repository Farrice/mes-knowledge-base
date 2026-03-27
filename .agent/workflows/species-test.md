---
description: Run Ocean Vuong's Species Test on any content — "Has the species had this sentence yet?" Audit for genuine novelty, flag mimetic defaults, score perceptual originality.
---

# Species Test Protocol

Ocean Vuong's ultimate quality bar: could any other writer's AI produce this? If yes, delete it.

## PHASE 1: LOAD EXPERT

Read these files IN ORDER:
1. `skills/ocean-vuong-perceptual-writing/genius.md` — operating principles + voice DNA
2. `skills/ocean-vuong-perceptual-writing/workflows/species-test-protocol.md` — full workflow

## PHASE 2: EXECUTE

Follow the workflow exactly as documented. The workflow contains:
- Pre-Flight Gate
- Anti-Pattern Guard
- Sentence-by-sentence novelty audit
- Mimetic vs. poietic classification
- Rewrite prescriptions for failed sentences

## PHASE 3: FINALIZE

Run chain finalize:
```bash
python3 execution/chain_runner.py finalize "Species Test audit" \
    --expert ocean-vuong \
    --skill ocean-vuong-perceptual-writing \
    --workflow species-test-protocol \
    --type Creative \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[what worked, what didn't]"
```
