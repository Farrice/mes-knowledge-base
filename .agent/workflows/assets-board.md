---
description: Rescan all asset zones + rebuild and open the Asset Command Center (visual gallery of every generated/collected media asset)
---

# /assets-board — Asset Command Center

// turbo
```bash
python3 execution/asset_index.py && python3 execution/asset_gallery.py && open .agent/assets/assets-board.html
```

The board is a local file:// page (masonry grid, filter chips, search, lightbox, copy-path, Styles tab). It is NOT published as an Artifact — file:// images can't resolve from claude.ai. To share a visual cut instead:

```bash
python3 execution/asset_gallery.py --embed --recent 40
```

then publish `.agent/assets/assets-highlights.html` via the Artifact tool.
- Same conversation as a prior publish: same file path keeps the URL.
- Different conversation: pass the existing artifact URL as `url` (find via Artifact list) — never mint a duplicate board.
- Favicon stays 🖼️ (stable tab identity).

Data sources (all deterministic): `.agent/assets/manifest.jsonl` (owned by `execution/asset_index.py`; engine-appended lines from `execution/generate_media.py` and sweeps reconcile by path+mtime, latest-line-wins) · zones: `skills/fantastic-posters/out/` · `deliverables/{generations,images,designs,carousel-images,video-enhancement}/` · `_active/*/{05-assets,visuals}/` · styles registry `skills/generate/styles/<slug>/`.

If an asset is missing from the board, it wasn't indexed — fix the zone list in `asset_index.py` or the engine's manifest append, not the board. The in-page state is static: after generating or adding files, re-run this workflow (the `/generate` engine calls `asset_gallery.py --quick` itself at end of run).
