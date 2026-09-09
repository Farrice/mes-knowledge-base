# Launchd Scheduler Fix — 2026-08-27

## Problem
The scheduled Angle Map Listening job (`com.antigravity.angle-map-listening`) has been **failing silently since 2026-08-24** with:
```
Failed to authenticate: OAuth session expired and could not be refreshed
```

Root cause: The `claude` CLI uses OAuth stored in macOS Keychain. In headless launchd context (non-interactive), it cannot refresh an expired OAuth token. The token expired after 4 days, and every scheduled run at 05:30 UTC since 2026-08-24 exited with `rc=1`.

## Solution
Use `CLAUDE_CODE_SIMPLE=1` mode, which tells the claude CLI to authenticate via `ANTHROPIC_API_KEY` environment variable instead of OAuth/Keychain. This avoids the Keychain refresh issue in headless contexts.

## Changes Made

### 1. Updated `execution/angle_map_listening_run.sh`
- Added `.env` loader to source environment variables
- Set `CLAUDE_CODE_SIMPLE=1` before calling `claude -p`
- Added comments explaining the fix

**Commit:** `4661ee42b` (already pushed to local main; divergence with remote blocks push)

### 2. Updated `.env` (gitignored, local-only)
Added:
```bash
# ── Anthropic API Key (Claude Headless Auth) ────────────────────
# Used by claude CLI in CLAUDE_CODE_SIMPLE=1 mode for launchd scheduled jobs.
# Get key: https://console.anthropic.com/account/keys → Create Key
# REQUIRED for angle-map-listening scheduled runs to work.
ANTHROPIC_API_KEY=
```

## What You Need to Do

**MANUAL STEP — REQUIRED:**

1. Go to https://console.anthropic.com/account/keys (requires Anthropic account)
2. Create a new API key (copy the full key starting with `sk-ant-`)
3. Open `.env` in this repo and paste it:
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   ```
4. Save `.env` (it will not be committed, but launchd will read it)

## What Happens Next

Once you fill in the API key:
- The launchd job is already loaded and scheduled for daily runs at **05:30 UTC**
- The next run (tomorrow morning at 05:30) will use API-key auth and should succeed
- The job will continue daily on schedule

## Testing (Optional)

If you want to verify the fix works before waiting for 05:30 tomorrow, run:
```bash
cd "/Users/farricecain/Google Antigravity"
set -a; source .env; set +a
export CLAUDE_CODE_SIMPLE=1
bash execution/angle_map_listening_run.sh
```

Check the log at: `_active/knowledge/health-performance-ip-library/06-system/listening-run.log`

## Why This Works

- **OAuth problem:** Token stored in Keychain, expires after ~4 days, can't be refreshed in headless mode
- **API key solution:** Env var-based auth, no Keychain, no refresh needed, works in headless launchd
- **Trade-off:** API key must be stored in `.env` (which is `.gitignore`'d for safety), so it's not committed

## Related Files

- `execution/angle_map_listening_run.sh` — the scheduler runner (fixed)
- `.env` — environment variables (add API key here)
- `_active/knowledge/health-performance-ip-library/AUTOMATION_PROMPT.md` — the full automation spec
- `_active/knowledge/health-performance-ip-library/06-system/listening-run.log` — job output log

---

**Status:** Awaiting API key (step 1 above). Once filled, the scheduler is live.
