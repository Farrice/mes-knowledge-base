# MCP Server Setup Guide

Quick-start guide for Google Workspace, Notion, and SQLite MCP servers for your Antigravity environment.

---

## Overview

| MCP Server | What It Does | Cost |
|------------|--------------|------|
| **Google Workspace** (`gws`) | Read/write Drive, Docs, Sheets, Gmail, Calendar, Chat, 50+ services | Free (OAuth) |
| **Notion** | Read/write Notion pages/databases | Free (API key) |
| **Perplexity** (`perplexity-ask`) | Deep research, web search, reasoning via Sonar models | $30/mo budget |
| **Apify** (`apify`) | Scraping, social listening, structured data (Reddit, IG, TikTok, YouTube, Amazon, Maps, web) | $29/mo Starter plan |
| **SQLite** | Query local SQLite databases | Free |

---

## 1. Google Workspace MCP (via `gws` CLI)

**GitHub:** https://github.com/googleworkspace/cli
**npm:** `@googleworkspace/cli`

The official Google Workspace CLI includes a built-in MCP server that exposes Google APIs as structured tools for AI agents.

### Step 1: Install

```bash
npm install -g @googleworkspace/cli
gws --version
```

Requires Node.js 18+. Pre-built Rust binaries — no Rust toolchain needed.

### Step 2: Authenticate

**If you have `gcloud` CLI:**
```bash
gws auth setup    # Creates GCP project + OAuth credentials automatically
gws auth login    # Opens browser for OAuth consent
```

**Manual setup (no `gcloud`):**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create/select a project and enable Workspace APIs (Drive, Docs, Sheets, Calendar, Gmail)
3. Go to **Credentials** → **Create Credentials** → **OAuth Client ID** → **Desktop Application**
4. Download client JSON to `~/.config/gws/client_secret.json`
5. Run `gws auth login -s drive,gmail,calendar,sheets,docs`

Credentials are encrypted at rest via OS keyring (macOS Keychain, AES-256-GCM).

### Step 3: Verify

```bash
gws auth status
gws drive files list --params '{"pageSize": 3}'
```

### Step 4: Register MCP Server for Claude Code

```bash
claude mcp add google-workspace -s project -- gws mcp -s drive,gmail,calendar,sheets,docs
```

This creates `.mcp.json` in the project root:

```json
{
  "mcpServers": {
    "google-workspace": {
      "type": "stdio",
      "command": "gws",
      "args": ["mcp", "-s", "drive,gmail,calendar,sheets,docs"]
    }
  }
}
```

**Service flag (`-s`):** Controls which APIs are exposed. Options include `drive`, `gmail`, `calendar`, `sheets`, `docs`, `chat`, `admin`, or `all`.

### Security Features

- `--sanitize` — Integrates with Google Cloud Model Armor (prompt injection detection)
- `--dry-run` — Preview commands without execution
- `-s` flag — Scope-limit which services the MCP server exposes

### Current Setup (as of 2026-03-09)

- **GCP Project:** Jarvis V2 (`jarvis-v2-488418`)
- **OAuth Client:** "Javris" (Desktop type)
- **Account:** farrice.cain@gmail.com
- **Scopes:** drive, spreadsheets, gmail.modify, calendar, documents, userinfo.email, openid
- **Credentials:** `~/.config/gws/credentials.enc` (encrypted)

---

## 2. Notion MCP

### Step 1: Get Notion API Key

1. Go to [Notion Integrations](https://www.notion.so/profile/integrations)
2. Create a new internal integration
3. Copy the API key (starts with `ntn_` or `secret_`)
4. Share your pages/databases with this integration

### Step 2: Add to MCP Config

Add to your mcp_config.json:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_TOKEN": "YOUR_NOTION_API_KEY"
      }
    }
  }
}
```

**Alternative (Notion's hosted server):**

You can also use Notion's hosted MCP at `https://mcp.notion.com/mcp` - connect via Notion Settings → Connections → Notion MCP.

---

## 3. Perplexity MCP (`perplexity-ask`)

### Installation

```bash
claude mcp add perplexity-ask --env PERPLEXITY_API_KEY="$PERPLEXITY_API_KEY" -- npx -y @perplexity-ai/mcp-server
```

API key is in root `.env` as `PERPLEXITY_API_KEY`.

### Available Tools

| Tool | Model | Use For | Est. Cost |
|------|-------|---------|-----------|
| `perplexity_search` | sonar | Direct web search, quick lookups | ~$0.02 |
| `perplexity_ask` | sonar-pro | Conversational AI with web search | ~$0.05 |
| `perplexity_research` | sonar-deep-research | Deep research (multi-step) — **PRIMARY for `/deep-research`** | ~$0.25 |
| `perplexity_reason` | sonar-reasoning-pro | Advanced reasoning and analysis | ~$0.08 |

### Budget Tracking

The MCP server does NOT auto-log to our budget file. After each MCP query, manually log to `.agent/perplexity-usage.json`. Budget: **$30/month**. Full policy: `directives/perplexity-usage-policy.md`.

### Fallback

If MCP tools unavailable, use `execution/perplexity_client.py` (Python client with built-in budget tracking).

---

## 4. Apify MCP (`apify`)

Apify provides web scraping and social listening for sites generic web search can't reach (Reddit, Instagram, TikTok, YouTube, Amazon, Google Maps, JS-rendered pages).

### Step 1: Get API Token

1. Go to [Apify Console](https://console.apify.com/account/integrations)
2. Copy your personal API token (starts with `apify_api_`)

### Step 2: Add to .env

```
APIFY_TOKEN=apify_api_xxxxxxxxxxxxxxxxxxxx
```

### Step 3: Register MCP Server (one command)

```bash
bash execution/apify_setup.sh
```

This reads `APIFY_TOKEN` from `.env`, registers the MCP server with the curated actor list (pulled from `apify_client.py mcp-tools` — the single source of truth), then runs a config check. Idempotent — safe to re-run. Restart the session afterward to load the `mcp__apify__*` tools.

**Auto-registration:** a SessionStart hook (`execution/hooks/apify_mcp_bootstrap.py`, wired in `.claude/settings.json`) runs this automatically whenever the token is present and `apify` isn't already in `.mcp.json` — so fresh containers self-heal. Registration takes effect on the next session (Claude Code reads `.mcp.json` at start).

Manual equivalent (if you prefer not to use the script):

```bash
set -a; source .env; set +a
claude mcp add apify -s project --env APIFY_TOKEN="$APIFY_TOKEN" -- \
  npx -y @apify/actors-mcp-server --tools "$(python3 execution/apify_client.py mcp-tools)"
```

**Only the 12 curated actors are loaded.** No expensive enterprise actors — even if Claude tries to call something else, the MCP server doesn't have it.

### The 12 Curated Actors

| Actor | Purpose | Cost class |
|---|---|---|
| `apify/rag-web-browser` | JS-rendered page fetch | Cheap |
| `trudax/reddit-scraper-lite` | Reddit posts/comments | Cheap |
| `apify/instagram-scraper` | IG profiles, posts | Cheap |
| `clockworks/free-tiktok-scraper` | TikTok hashtags | Medium |
| `apidojo/youtube-scraper` | YouTube + transcripts | Medium |
| `junglee/amazon-scraper` | Amazon products/reviews | Cheap-Medium |
| `compass/crawler-google-places` | Google Maps places | Medium |
| `harvestapi/linkedin-post-search` | LinkedIn post search (no cookies) | Medium |
| `harvestapi/linkedin-profile-scraper` | LinkedIn profiles / companies | Medium |
| `apidojo/tweet-scraper` | X/Twitter search + timelines | Cheap |
| `curious_coder/threads-scraper` | Threads profile posts | Cheap |
| `apify/facebook-posts-scraper` | Facebook public page posts | Cheap |

The 5 social actors were added 2026-07 and are pending first-run verification — see "Verification Status" in `directives/apify-usage-policy.md`. Their `mcp__apify__*` tools work immediately (MCP auto-loads schemas); validate the CLI convenience commands with `python3 execution/apify_client.py verify --live`.

### Python Wrapper (for Gemini + workflows)

Gemini Antigravity does NOT support MCP. For Gemini and any non-MCP workflow, use the Python wrapper:

```bash
python execution/apify_client.py budget-status
python execution/apify_client.py reddit "first time home buyer" --limit 50 --comments
python execution/apify_client.py instagram realestatewithjing --limit 20
python execution/apify_client.py youtube "pilates day in life" --limit 5 --transcript
python execution/apify_client.py linkedin "AI ghostwriting" --limit 30
python execution/apify_client.py twitter --query "personal branding" --limit 50
# (full CLI: reddit, instagram, tiktok, youtube, amazon, maps, web, linkedin,
#  linkedin-profile, twitter, threads, facebook, run, verify, mcp-tools,
#  budget-status, budget-reset)
```

The wrapper:
- Reads `APIFY_TOKEN` from `.env` automatically
- Enforces a hard 90% cap against the $29/mo Starter plan
- Returns `{"fallback": true}` instead of raising on cap exhaustion (workflows degrade, never break)
- Logs every call to `.agent/apify-usage.json`
- Auto-resets on calendar month change

### Fallback Contract (CRITICAL)

If an Apify call returns `{"fallback": true}`, **the workflow must reroute** to:
1. Perplexity (`perplexity_client.py`)
2. Tavily search
3. Generic `read_url_content`

This is what makes Apify safe at the budget edge. Full policy: `directives/apify-usage-policy.md`.

### Python Dependencies

The wrapper uses `requests` and `python-dotenv`, both already installed for other execution scripts. No new pip installs needed.

### Security Note

`.mcp.json` contains the literal `APIFY_TOKEN` value because `claude mcp add --env` stores it inline. **`.mcp.json` is gitignored** to prevent token leakage. Each developer registers their own MCP server locally.

---

## 5. SQLite MCP

### Step 1: Add to MCP Config

No external credentials needed - just point to your database file:

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "uvx",
      "args": ["mcp-server-sqlite", "--db-path", "/path/to/your/database.db"]
    }
  }
}
```

Replace `/path/to/your/database.db` with your actual SQLite database path.

---

## Prerequisites

```bash
# Node.js 18+ (required for gws)
node --version

# uv (required for SQLite MCP)
which uvx || curl -LsSf https://astral.sh/uv/install.sh | sh

# npx (required for Notion MCP, comes with Node.js)
which npx
```

---

## After Setup

Once configured, restart your Claude Code session. The MCP servers will be available:

- **Google Workspace**: Read/write Drive, Docs, Sheets; manage Calendar events; send/read Gmail
- **Notion**: Create pages, update databases, search workspace
- **SQLite**: Query your local databases

---

## Need Help?

If you get stuck on any step, let me know and I can walk you through it.

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-11 |

**Update Rule**: When this protocol fires (MCP server configured or referenced), update the date and increment count.
