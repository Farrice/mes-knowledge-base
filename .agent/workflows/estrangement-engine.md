---
description: Transform mimetic writing into estranged prose using Ocean Vuong's behavioral displacement and Species Test — produce sentences the species has never had.
---

# Estrangement Engine

Deploy Ocean Vuong's core technique: transform familiar descriptions into genuinely novel perceptions.

## PHASE 1: LOAD EXPERT

Read these files IN ORDER:
1. `skills/ocean-vuong-perceptual-writing/genius.md` — operating principles + voice DNA
2. `skills/ocean-vuong-perceptual-writing/workflows/estrangement-engine.md` — full workflow

## PHASE 2: EXECUTE

Follow the workflow exactly as documented. The workflow contains:
- Pre-Flight Gate (is estrangement the right tool?)
- Anti-Pattern Guard (Vuong would-never checklist)
- 5-step estrangement process: Identify mimetic surfaces → behavioral displacement → perception audit → Species Test → thumbprint check

## PHASE 3: FINALIZE

Run chain finalize:
```bash
python3 execution/chain_runner.py finalize "Estrangement Engine output" \
    --expert ocean-vuong \
    --skill ocean-vuong-perceptual-writing \
    --workflow estrangement-engine \
    --type Creative \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[what worked, what didn't]"
```
