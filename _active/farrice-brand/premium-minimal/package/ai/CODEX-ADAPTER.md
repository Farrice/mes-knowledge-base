# Codex Adapter

## Recommended operating sequence

1. Read the root package documents and machine-readable tokens.
2. Inspect the nearest template and its export before editing.
3. Confirm the current approval state and exact copy source.
4. Make local, reversible edits only.
5. Preserve relative paths inside the package.
6. Export at native dimensions.
7. Visually inspect the output at full scale and approximately 25–30% scale.
8. Run the package QA checklist.
9. Return a change receipt and leave the asset in `review` unless Farrice explicitly promotes it.

## File handling

- Prefer SVG for editable static assets.
- Prefer PPTX for editable multi-page presentation systems when the source is truly editable.
- Treat the carousel PPTX as a container; its editable page sources are the SVG files.
- Use flattened, font-embedded PDF for review and delivery.
- Use sRGB PNG-24 for LinkedIn image uploads.
- Preserve the original portrait file without image editing.

## Verification expectations

At minimum verify:

- JSON parsing;
- SVG XML validity;
- raster dimensions;
- PDF page count;
- font embedding or substitution disclosure;
- local linked-file resolution;
- visible fictional-demo labels;
- protected-copy integrity; and
- ZIP integrity when repackaging.

Do not hardcode the original project path in new portable assets. Use paths relative to this package root.

## External boundary

Local generation and verification do not authorize profile edits, publication, uploads, DMs, outreach, or deployment.

