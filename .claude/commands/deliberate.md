---
description: "Multi-model deliberation — run the same prompt through Claude AND Gemini, surface explicit contradictions instead of blending. Distinct from /council (single-model multi-persona). For high-stakes decisions."
---

Read and execute the workflow at `.agent/workflows/deliberate.md` — Multi-model deliberation. Run the same prompt through Claude (this orchestrator inline) AND Gemini (via execution/deliberate.py), then synthesize with explicit contradiction-preservation. Beats Perplexity's "model council" by surfacing disagreement instead of blending it. Use for high-stakes decisions.
