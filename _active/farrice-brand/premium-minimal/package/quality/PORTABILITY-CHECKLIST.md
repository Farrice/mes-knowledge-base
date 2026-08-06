# Portability Checklist

Run this checklist before issuing a new package ZIP.

- [ ] All document references are relative to the package root.
- [ ] Every SVG-linked image exists beside or beneath the SVG.
- [ ] No original workspace path appears in any packaged file.
- [ ] No runtime-specific build script or dependency cache is included.
- [ ] No font binary is included.
- [ ] Helvetica Neue requirement and fallback limitation are disclosed.
- [ ] The original portrait is absent from the shareable core ZIP.
- [ ] Rejected, stale, or unconfirmed branches are absent.
- [ ] Carousel PPTX is labeled as an assembled flat-page container.
- [ ] Editable carousel page SVGs are present.
- [ ] Field-guide PDF and PPTX are present.
- [ ] JSON parses.
- [ ] SVG XML parses.
- [ ] PDF page counts pass.
- [ ] Raster dimensions pass.
- [ ] Local links and dependencies resolve after extraction.
- [ ] MANIFEST.json covers the payload.
- [ ] CHECKSUMS.sha256 verifies.
- [ ] ZIP integrity passes.
- [ ] The extracted package passes the same checks as the source folder.

