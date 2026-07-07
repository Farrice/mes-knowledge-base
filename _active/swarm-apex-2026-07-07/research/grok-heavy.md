# Grok 4 Heavy / DeepSearch — Mechanics Brief (2026-07-07, Sonnet deep-research)

## Thesis
Grok 4 Heavy's "multi-agent debate" is marketing gloss on a plain fan-out-then-single-leader-synthesis pattern. The parts worth stealing aren't the agent count — they're the single explicit fan-out knob and default cost/trace transparency. The part to avoid: a single synthesizing leader with no deterministic verification layer.

## Architecture Mechanics
- [VERIFIED — docs.x.ai/developers/model-capabilities/text/multi-agent] Two fan-out sizes: 4 agents (`reasoning.effort` low/medium) or 16 agents (high/xhigh); SDK exposes raw `agent_count`. Model: `grok-4.20-multi-agent`. xAI SDK / Responses API only — no custom client-side tools, no `max_tokens`.
- [VERIFIED] Reconciliation is leader-agent synthesis, not voting or adversarial debate: "A designated leader agent is responsible for synthesizing the discussion and presenting the final answer." Sub-agent traces encrypted; surfaced only with `use_encrypted_content=True`.
- [VERIFIED] Cost: all tokens from leader + sub-agents billed; docs warn multi-agent calls "may use significantly more tokens." No public latency figures.
- [VERIFIED — simonwillison.net July 2025] SuperGrok Heavy: $300/month, top tier.
- [UNCONFIRMED — likely fabricated] Named personas ("Harper/Benjamin/Lucas") and "65% hallucination reduction from debate" circulate on SEO content farms with zero primary corroboration. The real 65% figure (12.09%→4.22% FActScore) is from the Grok 4.1 model card, non-reasoning mode vs Grok 4 Fast — nothing to do with multi-agent debate. A real stat re-attributed to a sexier cause.

## DeepSearch / DeeperSearch
- [VERIFIED — xAI launch tweet] "a powerful agent that can rapidly synthesize key information, reason about conflicting facts & opinions."
- [LIKELY] Shape: sub-query decomposition, parallel web/X search, iterative read-summarize, "Thoughts" transparency toggle. Specifics ("10-step limit," "seven consistency layers") only from marketing-adjacent guides. No dedicated docs.x.ai page — less formally documented than the multi-agent API.
- [UNCONFIRMED] Source counts, citation-linking mechanics, whether verification is post-hoc or interleaved.

## Genuinely Best At
- [VERIFIED] HLE: 25.4% base / 38.6% with tools / 44.4% Heavy at July 2025 launch.
- [VERIFIED — interconnects.ai, Nathan Lambert] Search/retrieval genuinely strong — beats OpenAI Deep Research at mapping written content and organizing by topic; search queries "far more interpretable."

## Weaknesses
- [VERIFIED — Lambert] Vibe-test gap: tops benchmarks but crowdsourced leaderboards rank it "very middle of the pack"; failed a trivially simple everyday task; "benchmaxxed and overcooked."
- [LIKELY] Comparatively weak context window / long-document handling (170-page PDF failures reported).
- [VERIFIED — Willison] Objectivity risk: reasoning traces show it searching "what Musk thinks" on contested topics — baked into the search layer.

## Transferable Patterns
1. Single fan-out knob tied to declared complexity (4 vs 16) — encode as a deterministic function, not a judgment call per run.
2. Cost transparency by design — log/surface total sub-agent spend as a receipt line.
3. Do NOT copy unguarded leader-synthesis — one agent's bias passes through unchecked. Step 5.5 verification is a structural advantage Grok's public architecture lacks; keep it mandatory.
4. Role-typed sub-agents (fact-checker / quant / contrarian) over uniform parallel sampling — deliberately assigned, not marketing personas.

## Sources
Primary: docs.x.ai multi-agent page; simonwillison.net; xAI launch tweet; Grok 4.1 model card PDF. Analyst: interconnects.ai (Lambert). Secondary (low trust, flagged): ai-x.chat, verdent.ai, ai505.com, tryprofound.com, dageno.ai. Note: x.ai/news/grok-4 returned 403 — manual check needed if exact launch-post wording required.
