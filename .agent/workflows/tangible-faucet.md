---
description: Identify and validate the repeatable tangible asset
---

# Tangible Faucet

Design the never-ending tangible asset for a newsletter.

## Steps

1. Load expert context:
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/02-tangible-faucet.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: validated tangible asset, audience: self, context: newsletter concept design, end state: named asset with faucet test passed).

3. Route (Chain Step 3): Nicolas Cole → `nicolas-cole-newsletter-flywheel` skill, `tangible-faucet` workflow.

4. Gather input from user:
   - Newsletter topic area or rough concept
   - Their area of expertise
   - What they personally consume obsessively (Self-Consumption Audit)

5. Execute the workflow — run 7-type taxonomy, triple faucet test, infinite repeatability check.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Tangible asset identification — [asset type]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow tangible-faucet \
    --type Strategy \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Asset ID with faucet test validation"
```

**Execution prompts**: before producing the deliverable, check `skills/nicolas-cole-newsletter-flywheel/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
