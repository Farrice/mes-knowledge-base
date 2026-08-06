# B-Roll Ladder — a beat needs a visual you don't have

Free-first, ORDERED, mandatory (Farrice 2026-08-06). Descend only when the rung above
genuinely can't serve the beat — and record which rung served each beat in the cutlist notes.

## Rung 1 — Own footage & screen recordings ($0, most authentic)
- `broll/screen/`, `footage/`, prior projects. Search the asset manifest FIRST:
  `python3 execution/broll_source.py search --query "<subject>"` greps owned/indexed clips before any API.
- Screen recordings of the AI system, dashboards, terminals = native B-roll for the teaching lane. QuickTime/Cmd-Shift-5 is enough.

## Rung 2 — Free stock ($0, VOX-authentic archival feel)
- `python3 execution/broll_source.py search --query "..." --provider all --orientation landscape --min-duration 5`
- `python3 execution/broll_source.py fetch --id pexels:12345 --project <slug> --tags "..."`
- License + source_url land in the manifest automatically. Pexels/Pixabay both allow monetized use; attribution not required (Pexels appreciated).

## Rung 3 — Motion graphics as code ($0, the purest VOX grammar)
- Data, concepts, diagrams, quotes, UI mockups → a graphic beats found footage.
- HyperFrames (overlay/standalone graphic beats) or Remotion (charts, maps, full comps — see `rules/charts.md`, `rules/maps.md`). Design stack loaded, always.

## Rung 4 — Generated ($, cost-gated, LAST)
- Only when the beat needs footage that cannot exist (concept shots, stylized worlds, product-in-scene).
- Route: `/generate` → craft-map grammar (seedance → cinema-worldbuilder M1-M5; kling → multishot grammar) → quote cost WITH the crafted prompt → fal wrapper under `fal_budget_guard`.
- seedance-720p ceiling (1080p HARD-BLOCKED; 720p is invisible at B-roll scale). People/photoreal → fal people lane. **NO Higgsfield.**
- Output → `broll/generated/` with prompt+cost provenance in the manifest.

## Selection craft (any rung)
- The Decoupling Law (tao-prompts): action B-roll cuts away from the speaker — never generate lip-sync plates.
- A B-roll clip earns its slot by ADDING information or emotion, not by relieving visual boredom; 2-6s per insert, cut on motion.
- Match grade/energy to the main track — a mismatched stock clip reads cheaper than a graphic.
