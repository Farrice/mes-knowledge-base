# Studio Preview Wrapper — build brief (LIVING; written 2026-09-03 for a fresh executor session)

**Task.** Build OUR review surface for the Scrapes carousel pool and runs: a local page that shows each template or slide at its TRUE 4:5 size inside LinkedIn and Instagram frame mockups, a plain comment box per item that writes to the same `comments.json` the Scrapes Studio reads, and Approve / Retire buttons that write `status` into the pool's `manifest.json`. Farrice's words: "It's not even cropped right to the actual size... doesn't show me a true preview of what it would look like on Instagram and LinkedIn... It would be easier if a box popped up and I can type into that box and then submit it."

**Build method.** One Python file, `execution/studio_preview.py`, stdlib + Pillow only, serving on localhost. Two modes: `--pool <dir>` (templates) and `--run <dir>` (rendered slides). No framework, no npm, no AI, $0. Never edit anything under `.claude/skills/` (hash-gated vendor code). Read the vendor code to match its file shapes; do not import it.

**Bar.** Farrice opens the page, sees his eight editorial templates at real 1080×1350 proportions inside a LinkedIn document-post frame and an Instagram carousel frame, types a comment into a visible box, hits Submit, and the comment is in `<template>/comments.json` in the shape the Scrapes Studio already writes. He taps Approve and `manifest.json` reads `approved` with `approved_by`/`approved_on`. `python3 execution/scrapes_brand.py check farrice --pool linkedin-carousel` still says READY. Nothing else counts as done.

## What exists (read these first, in order)
1. `.claude/skills/00-social-content/scripts/content-studio/content_studio.py` — the vendor Studio. Read how `--mode template` lists templates, how it renders previews, and the exact JSON shape it writes to `<template>/comments.json` (there is at least one real file to copy from: `brand_context/templates/linkedin-carousel/*/comments.json` if present; otherwise grep the vendor code for `comments.json`). Match that shape byte-for-byte in spirit: same keys, same timestamp format.
2. `brand_context/templates/linkedin-carousel/manifest.json` — `templates[]` with `id`, `file`, `role`, `status` (`ready|approved|retired|draft`), `needs`, `optional`, `style`; approvals carry `approved_by`, `approved_on`; retirements carry `retired_reason`. `styles.json` lists template ids per style; a retired id must be removed from every style list.
3. `brand_context/templates/linkedin-carousel/_preview/*.png` — existing template previews (1080×1350 @2x = 2160×2700). Re-render one only if missing, with:
   `uv run --quiet --with playwright python .claude/skills/viz-image-gen/scripts/render_template.py --template-pool linkedin-carousel --template-id <id> --brand-context brand_context --use-sample-text --no-ai-bg --data <json FILE> --output <png>` (`--data` must be a file path; inline JSON crashes it).
4. `projects/00-social-content/2026-09-03/blind-bar-01-take-a-ag1/` — a finished run: `slide-0N.png`, `slide-0N.data.json`, `manifest.json`, `pipeline-log.md`. `--run` mode reads this layout.
5. `execution/scrapes_brand.py` (`check` counts `ready|approved` as the usable pool) and `tests/test_scrapes_routing.py` (test style to copy).
6. `brand_context/visual-identity/tokens.json` — page chrome uses the brand: canvas #F3F3F0, ink #101010, graphite #555553, line #D8D8D3, Helvetica Neue. No other colors.

## Page spec (keep it small)
- Header: pool or run name, brand lock line from `scrapes_brand.py resolve --from-prompt "<brand>"`, count approved / ready / retired.
- One row per template or slide: left, the PNG at exact 4:5 inside two frames side by side, "LinkedIn" (document post: white card, 1200-wide feed column scaled, name row above, reaction row below) and "Instagram" (portrait carousel: phone-width, dot indicator, caption area). Frames are CSS only; the PNG is never resized off-ratio; a toggle shows the raw PNG at 100%.
- Right: a `<textarea>` labeled "Comment", a Submit button, and the existing comments listed under it with timestamps. Submit POSTs to the local server, which appends to `<template>/comments.json` (pool mode) or `<run>/comments.json` (run mode) and re-renders the list. No modal, no pill.
- Below the textarea in pool mode: Approve and Retire buttons. Approve writes `status: approved`, `approved_by: "Farrice"`, `approved_on: YYYY-MM-DD`. Retire asks for one line of reason in the same textarea and writes `status: retired`, `retired_reason`, and removes the id from every list in `styles.json`. Both write atomically (write temp, rename).
- Footer: the render command that produced the PNG, and the file path, in monospace. Nothing else.
- CLI: `python3 execution/studio_preview.py --pool brand_context/templates/linkedin-carousel [--port N] [--no-open]` and `--run <dir>`. Print the URL. Auto-pick a free port when none given. `--no-open` prints only.

## Tests (sabotage both directions before calling anything verified)
`tests/test_studio_preview.py`, pytest, tmp pool fixture with two fake templates and PNGs:
- GET `/` lists both; each PNG served with correct content-type.
- POST comment appends one record with the vendor keys; a second POST appends, never overwrites.
- POST approve flips status and stamps the two fields; `scrapes_brand.check`-style count goes up by one.
- POST retire flips status, stores reason, removes id from `styles.json` lists.
- Sabotage: break the atomic write (write to the real path first) and confirm the test catches a half-written manifest; then restore.
Run: `uv run --quiet --with pytest --with pillow python -m pytest tests/test_studio_preview.py -q -p no:cacheprovider`.

## Constraints
- Lane discipline: work in a worktree lane (SessionStart auto-lane), `worktree_lane.py merge --lane <branch> --push` when green. Main is integration-only.
- Never edit inside `.claude/skills/*`. Never post or send anything. $0 build: no API calls.
- The Bash guard in lanes rejects compound commands it cannot verify and paths containing the word "source"; split commands, avoid that word in paths.
- State the running cost in the final message ($0 expected). One `chain_runner.py finalize` at the end, type System.
- Report honestly: if a vendor shape could not be matched, say which key and why. Do not invent a comments format.

## Hand-back
Final message to Farrice: the URL to open, the two commands (pool mode, run mode), test output pasted, and one line on anything left out. Then update `_active/harness/scrapes-skill-systems/USER-GUIDE.md` §"Leaving notes in a Studio" to point at this page instead of the vendor Studio, and add one dated line under `## 00-social-content` in `context/learnings.md`.
