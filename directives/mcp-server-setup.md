# MCP Server Setup Guide

Quick-start guide for Google Workspace, Notion, and SQLite MCP servers for your Antigravity environment.

---

## Overview

| MCP Server | What It Does | Cost |
|------------|--------------|------|
| **Google Workspace** (`gws`) | Read/write Drive, Docs, Sheets, Gmail, Calendar, Chat, 50+ services | Free (OAuth) |
| **Notion** | Read/write Notion pages/databases | Free (API key) |
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

## 3. SQLite MCP

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
