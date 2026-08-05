---
description: Research-brief library — list, open, and render house-style HTML research briefs (Codex Antigravity design system); briefs also live on the Asset Command Center's 📋 shelf
---

# /briefs — Research-Brief Library

The storage system: every brief lives at `deliverables/research-briefs/<slug>/` as a self-contained `<slug>-brief.html` plus its `<slug>-brief.json` source (provenance — the JSON is what gets re-rendered after edits). The Asset Command Center (`/assets-board`) indexes the same directory as the **📋 Research Briefs** shelf; clicking a brief card opens the brief.

## List the library

// turbo
```bash
ls -t deliverables/research-briefs/*/*-brief.html 2>/dev/null | while read f; do echo "$(date -r "$f" '+%Y-%m-%d')  $f"; done
```

## Open a brief (or the whole board)

```bash
open deliverables/research-briefs/<slug>/<slug>-brief.html   # one brief
python3 execution/asset_index.py && python3 execution/asset_gallery.py && open .agent/assets/assets-board.html   # board view
```

## Produce a NEW brief

1. Do the research (Chain applies — route/load/ground as usual; scraping via `apify_client.py` or Monid per `directives/monid-usage-policy.md`).
2. Write the brief as structured JSON per the schema in `execution/render_brief.py`'s docstring — trust header (window/lens/sources/compiled), evidence rows each carrying `source_url` + `confidence` (VERIFIED/LIKELY/UNCONFIRMED — never render an unverified claim without its chip), ranked `decision` section, `deploy` copy-paste blocks, `caveats` reliability ranking, source `ledger`.
3. Render + index:

```bash
python3 execution/render_brief.py <path/to/brief.json> --open
python3 execution/asset_index.py && python3 execution/asset_gallery.py
```

Template: `templates/research-brief/template.html` (Codex Antigravity tokens — edit tokens there, never inline in briefs). Reference anatomy: `extractions/eddy-ballesteros/reference-corpus/brief-anatomy.md`. Pilot exemplar: `deliverables/research-briefs/monid-research-stack/`.

## Re-render after editing a brief's JSON

```bash
python3 execution/render_brief.py deliverables/research-briefs/<slug>/<slug>-brief.json
```
