---
description: Full end-to-end visual blueprint pipeline — concept → wireframe → annotation → build → validate
---

# /visual-blueprint — Full Blueprint-to-Build Pipeline

Run the complete Visual Blueprint Pipeline from raw concept to production-ready visual asset. This is the comprehensive workflow that chains wireframing, style annotation, build handoff, and validation into a single end-to-end flow.

## Usage

```
/visual-blueprint [describe the full project — what it is, who it's for, style direction]
```

Examples:
- `/visual-blueprint modern dark SaaS dashboard for an AI analytics tool — sidebar nav, KPI cards, revenue chart, user activity table`
- `/visual-blueprint landing page for Farrice's ghostwriting service — hero with value prop, social proof, service tiers, testimonials, CTA`
- `/visual-blueprint 10-slide pitch deck for AI Brain Builder service — problem/solution narrative, pricing, case study`
- `/visual-blueprint email sequence template — welcome email with brand header, 3 value blocks, and soft CTA`

## Steps

### 1. Load Skill
// turbo
Read `skills/mark-kashef-visual-design/genius.md` for genius context.

### 2. Determine Asset Type
Route to the appropriate workflow:
- **Slide deck** → Read and execute `skills/mark-kashef-visual-design/workflows/03-slide-deck-architect.md`
- **Technical diagram** → Read and execute `skills/mark-kashef-visual-design/workflows/04-design-system-visualizer.md`
- **All other visual assets** → Read and execute `skills/mark-kashef-visual-design/workflows/02-visual-blueprint-to-build.md`

### 3. Execute the Full Pipeline
Follow the workflow through all phases:
1. **Wireframe** — Generate and iterate until locked
2. **Annotate** — Add style, color, typography, and interaction specs
3. **Build** — Translate to production prompt and execute
4. **Validate** — Compare output to wireframe specification

### 4. Taste Gate (Optional)
If the user wants quality validation before production, read and execute `skills/mark-kashef-visual-design/workflows/05-visual-taste-gate.md` between wireframe and build phases.

### 5. Deliver
Present the completed asset with:
- The locked wireframe (specification)
- The built output
- Validation checklist showing wireframe-to-output mapping

## Notes
- For **slide decks specifically**, this command automatically invokes the Slide Deck Architect workflow which handles narrative architecture + per-slide wireframing
- For **technical diagrams**, this routes to the Design System Visualizer with complexity simplification
- The **taste gate** is optional but recommended for high-stakes deliverables (client work, revenue-generating assets)
