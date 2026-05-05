# Daily Zeitgeist Brief — Setup Guide

The brief generation + Gmail delivery is now built. Two scheduling paths:

## Path A — In-Session Schedule (already active, today only)

CronCreate job `d29455c8` is queued in this Claude Code session at
**7:03am LA daily**. It fires only while a Claude Code REPL is open.
Auto-expires after 7 days.

This is the **safety net**, not the primary delivery method. Use it
to test the engine while you set up Path B.

## Path B — Autonomous launchd (recommended — true 24/7)

This path runs the brief without any Claude Code session open. macOS
launchd wakes up at 7:03am, runs `claude --print` in non-interactive
mode, executes the workflow, and sends the Gmail.

### One-time setup steps

**Step 1 — Re-auth gws Gmail with send scope**

The current `gws` token has `gmail.modify` but not `gmail.compose` /
`gmail.send`. Re-auth once:

```bash
gws auth login -s drive,gmail,calendar,sheets,docs
```

Follow the OAuth browser flow. After this completes, `gws gmail +send`
will work without the 403 scope error.

Verify with:

```bash
gws gmail +send --to farrice.cain@gmail.com \
  --subject "Test" --body "Auth check" --draft
```

If you see a draft ID returned, you're good.

**Step 2 — Install the launchd plist**

```bash
cp _active/farrice-brand/setup/com.farrice.zeitgeist-brief.plist \
   ~/Library/LaunchAgents/

launchctl load ~/Library/LaunchAgents/com.farrice.zeitgeist-brief.plist
```

**Step 3 — Test the runner manually**

```bash
bash _active/farrice-brand/setup/run-zeitgeist-brief.sh
```

Should produce:
- `.tmp/zeitgeist/[YYYY-MM-DD]-research-dossier.md`
- `.tmp/zeitgeist/[YYYY-MM-DD]-brief.md`
- A Gmail draft (or sent email if you remove `--draft`)
- `knowledge/zeitgeist-archive/[YYYY-MM-DD].md`
- An entry in `.agent/zeitgeist-runs.jsonl`

**Step 4 — Verify launchd loaded**

```bash
launchctl list | grep parallax
```

Should show `com.farrice.zeitgeist-brief` with a recent timestamp.

### Removing the schedule

```bash
launchctl unload ~/Library/LaunchAgents/com.farrice.zeitgeist-brief.plist
```

### Running on demand

```bash
launchctl start com.farrice.zeitgeist-brief
```

### Logs

Stdout → `.tmp/zeitgeist/launchd-stdout.log`
Stderr → `.tmp/zeitgeist/launchd-stderr.log`

If the brief stops landing, check stderr first.

## Path C — Manual backup

If both schedulers fail or you want to run on demand inside Claude
Code, just type:

```
/daily-zeitgeist-brief
```

The workflow runs the same logic interactively.

## Cost and observability

Per-run cost estimate (Claude Code tokens + Perplexity + Apify):
- Anthropic API: ~$2-4 (Tier 1.5 grounding + research subagent)
- Perplexity: 5-8 queries (~$0.30 from $30/mo budget)
- Apify Reddit: ~$0.40 (when enabled — currently rate-limited fallback)
- Total: ~$2.70 - $4.70 per brief

Tracked in `.agent/zeitgeist-runs.jsonl`. Weekly Sunday lookback in
the workflow surfaces "you flagged X 3 weeks ago, it just hit
LinkedIn mainstream" wins.

## Troubleshooting

**Brief didn't land in inbox**
1. Check `.tmp/zeitgeist/launchd-stderr.log`
2. If "scope error" → re-run `gws auth login` (Step 1 above)
3. If "API key" → check `.env` for ANTHROPIC_API_KEY, GROQ_API_KEY,
   PERPLEXITY_API_KEY
4. If "no dossier produced" → run `/daily-zeitgeist-brief` interactively
   to see where it broke

**Brief lands but content is thin**
- Reddit/Apify may have rate-limited. Workflow logs to
  `.agent/zeitgeist-runs.jsonl` with `gaps` field. Manual 30-min
  Reddit pass tonight fills the seam.

**Personal prompt drew on suppression vein on a heavy day**
- Sensitivity gate didn't fire correctly. Edit
  `.agent/workflows/daily-zeitgeist-brief.md` Phase 5 to tighten
  the gate logic.
