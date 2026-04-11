# QA Anti-Patterns

> Internalize during Step 5 (PRODUCE). Check during production — not post-production.

## 1. Template Slop
Generate from templates without grounding. Fix: Agentic Research (live search_web/Perplexity).

## 2. Entity Blindness
Treating all inputs the same. **ALWAYS classify entity type** (Product|Service|Demographic|Program|Location|Concept) before generating.

## 3. Speed Without Validation
Moving fast without sanity-checking. Fix: Cross-check key claims, ask "Would an expert find this embarrassing?", cite sources.

## 4. Phantom Research ⚠️
Marking research tasks complete without invoking external tools. Output looks like research but is pure LLM. Fix: Mandate 5 (Perplexity-First).

## 5. Structurally Sound But Flat
Correct structure, zero tension/emotion/recognition. Fix: Tension Test + Recognition Test + writers' room for content ≥500 chars.

## 6. AI-Shaped Prose
Right methodology, wrong words. Banned vocab: delve, tapestry, landscape, leverage, robust, realm, multifaceted. Fix: `directives/ai-slop-detector.md`.

## 7. Echo Chamber Deliberation ⚠️
Multi-agent unanimous validation using no external data. Fix: Disconfirming queries + Uncomfortable Insight Rule + Fabrication Scan.
