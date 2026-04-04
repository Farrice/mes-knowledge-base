---
description: Generate insight vectors from audience mental models — the upstream idea engine for all Luke Iha copy
---

# Insight Vectors

Run the full Insight Vector Generator pipeline from `skills/luke-iha-insight-vectors/`.

## Steps

1. Load `skills/luke-iha-insight-vectors/SKILL.md`
2. If deep/creative work, also load `skills/luke-iha-insight-vectors/genius.md`
3. Execute the core pipeline:
   - **Phase 1**: Run Mental Model Mapper (`workflows/mental-model-mapper.md`)
   - **Phase 2**: Run Insight Vector Generator (`workflows/insight-vector-generator.md`)
   - **Phase 3**: SIN-filter and shortlist vectors
4. For specific follow-up workflows, use:
   - `/insight-elaborate` — 8-fold elaboration
   - `/insight-audit` — audit existing copy for vector coverage
   - `/reverse-cause` — dedicated reverse causation engine
   - `/archetype-build` — build typing systems
   - `/insight-bridge` — convert vectors to mechanisms
   - `/insight-inject` — inject vectors into existing copy
   - `/insight-social` — generate social content from vectors
   - `/insight-brief` — creative strategy brief from vectors
   - `/belief-gap-sprint` — McRaney belief dissolution × insight vectors
   - `/insight-series` — multi-part content series from vectors
