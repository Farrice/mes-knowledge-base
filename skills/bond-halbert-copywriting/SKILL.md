---
name: "Bond Halbert - Ultimate Copywriting Mastery"
description: 'Executes Bond Halbert''s 47-year direct-response copywriting system — market research, velocity-optimized copy creation, and complete campaign architecture from the son and protege of Gary Halbert (founder of the modern DR copy lineage). Use when building full direct-response campaigns (sales letter + email sequence + ad), running deep market research before writing copy, optimizing existing copy for measurable velocity gains (CTR, conversion, AOV), or applying old-school DR fundamentals that modern copywriters skip. Trigger proactively whenever the user says "direct response", "sales letter", "DR copy", "Gary Halbert", "market research for copy", or wants to know "what would actually work in the mail". For online-native dopamine-copy mechanics use stefan-georgi-dopamine-copy; for high-stakes financial promos use chris-cimorelli-copywriting.'
version: "2.0"
format: "completion-engine"
workflows: 4
---

# Bond Halbert - Ultimate Copywriting Mastery

The complete direct response copywriting arsenal from Bond Halbert, son and protégé of Gary Halbert. 26 Crown Jewel prompts covering market language extraction through velocity-optimized conversion systems.

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| market | [Market Resonance & Language Blueprint](workflows/market-resonance-language-blueprint.md) | A comprehensive Market Language & Psychology Dossier | You are entering a new market or need to deeply understand the prospect's internal dialogue before writing. |
| velocity | [Velocity-Optimized Sales Copy Asset](workflows/velocity-optimized-sales-copy-asset.md) | A high-converting sales letter, VSL script, or landing page | You need to draft and refine direct response copy that converts skimmers, skeptics, and analytical readers alike. |
| rapid | [Rapid Market Entry & Offer System](workflows/rapid-market-entry-offer-system.md) | A complete Cold-to-Sold Campaign Architecture | You are launching a new product or funnel and need to compress the buying journey from stranger to customer. |
| omnipresent | [Omnipresent Authority & Content Engine](workflows/omnipresent-authority-content-engine.md) | A multi-channel content distribution and market takeover plan | You want to scale your message across platforms, build long-term authority, and dominate a market category. |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Legacy Prompts**: [references/_legacy-prompts/](references/_legacy-prompts/) — archived atomic prompts

> **Note on "market research":** The `market` workflow's research is Halbert-style — living in the market, reading the prospect's internal dialogue — not live web/data retrieval. This skill does NOT fetch market data. If you need grounded market claims (real VOC, stats, competitor proof), run `/copy-engine` ground or `python3 execution/research.py "<query>" --depth quick|standard|deep|max` first, then feed the findings in. Do not present this skill's output as "market-researched" on its own.
