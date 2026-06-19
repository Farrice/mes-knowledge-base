---
description: The offer doctor — turn a weak offer compelling, or flag a hollow one honestly
---

## Workflow: CE-Offer (`/ce-offer`)

**Expert**: Chase Hughes (Context Engineering) × Fladlien / Priestley / Sultanic
**Skill**: `skills/chase-hughes-context-engineering/`

Turn a weak offer into a compelling one — or flag a hollow one honestly. Diagnoses why an offer is weak across 6 axes (category, value clarity, mechanism, proof, promise, price/risk), then rebuilds it via the PCP category word + named mechanism + value stack + proof ladder. Makes a badly-BUILT offer good; will not make a buyer-HARMING offer sell.

### Steps

1. Read the skill files:
   - `skills/chase-hughes-context-engineering/SKILL.md`
   - `skills/chase-hughes-context-engineering/genius.md`
   - `skills/chase-hughes-context-engineering/references/pcp-and-upstream.md` (the category word)
   - `skills/chase-hughes-context-engineering/references/production-cross-pollination.md`

2. Load offer-craft experts: `jason-fladlien` (success by subtraction), `daniel-priestley` (premium positioning), `alen-sultanic` (offer economics).

3. **The honesty fork (BLOCKING):** if the offer genuinely does not serve the buyer on its merits (no real value, or it costs them more than it returns), say so plainly and stop. Do not paper over a hollow offer with better framing. This is the difference between an offer doctor and a con.

4. Read and execute the workflow:
   - `skills/chase-hughes-context-engineering/workflows/ce-offer.md`

5. **Ethics gate:**
   ```bash
   // turbo
   python3 execution/context_ethics_gate.py check --file <offer-path> --kind spec --workflow ce-offer --technique "offer rebuild: <category-flip>"
   # exit 2 = BLOCK; REVIEW = clear flags; PASS = ship
   ```

6. Quality gate: Is the rebuilt offer genuinely better on its merits for the buyer, or just better-disguised? Name the single change that does the most work.
