---
description: The daily zeitgeist engine — live social signals (Apify/Monid, pulse-budgeted) rendered as a research brief on the Asset Command board every morning; run on demand for any lane or topic
---

# /zeitgeist — Daily Zeitgeist Engine

The ambient "ear to the ground": scheduled daily at 06:20 (launchd `com.antigravity.zeitgeist-daily`), a rotation of listening lanes is scraped cheap-tier (`--pulse-mode`, $5/mo sub-ledger, graceful skip), synthesized into a research brief (evidence rows + ranked decisions + deploy blocks), rendered via `execution/render_brief.py --gdoc`, and landed on the board's 📋 shelf + as a Google Doc. Lanes: `.agent/zeitgeist-lanes.json` (config, edit freely).

## Status / rotation / spend

// turbo
```bash
python3 execution/zeitgeist_engine.py status
```

## Run now (on demand)

```bash
python3 execution/zeitgeist_engine.py run                 # whatever is due today
python3 execution/zeitgeist_engine.py run --lane ai-consulting-linkedin
python3 execution/zeitgeist_engine.py run --force          # all lanes
```

Then synthesize: follow `.agent/zeitgeist-synthesis-prompt.md` for each printed pack (in-session, same rules — no Chain, artifacts only). One-off topic not in a lane? Run the pulls directly (`apify_client.py twitter "<topic>" --limit 30 --pulse-mode` etc.), then produce the brief JSON per `execution/render_brief.py`'s schema and render with `--gdoc`.

## Consumption contract (the ambient layer)

Content workflows read the freshest brief for their lane BEFORE producing (free — the morning run already paid): check `deliverables/research-briefs/zeitgeist-<lane>-*/`, freshness ≤48h. Full protocol: `directives/live-data-grounding-protocol.md`. Library view: `/briefs` · board: `/assets-board`.

## Cost rails
- Rotation ≈ $0.13–0.16/day → ~$4–5/mo, inside the $5 pulse sub-budget (of Apify's included $29 credits — no new cash).
- Per-run hard cap $5 (approval token above), monthly ceilings unchanged. Every brief prints its run cost in the source ledger.
