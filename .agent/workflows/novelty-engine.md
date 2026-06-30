---
description: Conductor alias for the Kallaway novelty workflow family
---

# /novelty-engine - Novelty Workflow Conductor

Use this as the end-to-end conductor for turning a topic into a novelty-backed
content asset, campaign angle, hook bank, audit, or retention-ready asset.

## Execution

1. Load `skills/kallaway-illusion-of-novelty/SKILL.md`.
2. Load `skills/kallaway-illusion-of-novelty/genius.md`.
3. Choose the existing workflow by job:
   - full asset: `.agent/workflows/novelty-forge.md`
   - angle mining: `.agent/workflows/novelty-angles.md`
   - hook bank: `.agent/workflows/novelty-hook.md`
   - diagnostic: `.agent/workflows/novelty-audit.md`
   - retention handoff: `.agent/workflows/novelty-to-addictive.md`
   - campaign scaleout: `.agent/workflows/novelty-campaign.md`
   - calibration: `.agent/workflows/novelty-pattern.md`
4. Read the selected workflow and execute that path.

## Default

If the user simply asks for the novelty engine, default to
`.agent/workflows/novelty-forge.md` first, then recommend the next workflow only
when the output naturally needs retention, campaign, or calibration work.

## Boundary

This is a conductor over existing workflows. It must not become a competing
router, super-skill, or `.claude` command generator.
