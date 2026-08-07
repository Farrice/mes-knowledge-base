# Task 06 — Python build with verification (code lane)

Build `.tmp/bakeoff/link_audit.py` (stdlib only, Python 3.9+):

1. Walks a directory of markdown files (CLI arg, default `knowledge/`), extracts all relative links/refs of the form `[text](path)` and `` `path/to/file.md` ``.
2. Reports: total refs, unique targets, broken targets (file doesn't exist relative to repo root), and the top 10 most-referenced files.
3. `--json` flag for machine output; human table otherwise.
4. Include 5+ unit tests in `.tmp/bakeoff/test_link_audit.py` (tempdir fixtures, no network) and RUN them; show the passing output.
5. Then run the tool for real against `directives/` and include the actual output.

Scoring cares about: tests actually executed (not just written), honest broken-link findings, clean handling of edge cases (anchors `#`, external `http`, images).
