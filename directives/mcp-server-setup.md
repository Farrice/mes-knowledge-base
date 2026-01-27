# MCP Server Setup Guide

Quick-start guide for installing Google Workspace, Notion, and SQLite MCP servers for your Antigravity environment.

---

## Overview

| MCP Server | What It Does | Cost |
|------------|--------------|------|
| **Google Workspace** | Read/write Docs, Sheets, Drive | Free (OAuth) |
| **Notion** | Read/write Notion pages/databases | Free (API key) |
| **SQLite** | Query local SQLite databases | Free |

---

## 1. Google Workspace MCP

### Step 1: Get Google OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use existing)
3. Enable these APIs:
   - Google Drive API
   - Google Docs API
   - Google Sheets API
4. Go to **Credentials** → **Create Credentials** → **OAuth Client ID**
5. Select **Desktop Application**
6. Download the JSON credentials

### Step 2: Install

```bash
# Set environment variables (replace with your values)
export GOOGLE_OAUTH_CLIENT_ID="your-client-id"
export GOOGLE_OAUTH_CLIENT_SECRET="your-client-secret"

# Install and run
uvx workspace-mcp
```

### Step 3: Add to MCP Config

Add to `~/.gemini/antigravity/mcp_config.json`:

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "uvx",
      "args": ["workspace-mcp"],
      "env": {
        "GOOGLE_OAUTH_CLIENT_ID": "YOUR_CLIENT_ID",
        "GOOGLE_OAUTH_CLIENT_SECRET": "YOUR_CLIENT_SECRET"
      }
    }
  }
}
```

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

## Complete Config Example

Here's what your full `~/.gemini/antigravity/mcp_config.json` should look like:

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "uvx",
      "args": ["workspace-mcp"],
      "env": {
        "GOOGLE_OAUTH_CLIENT_ID": "YOUR_GOOGLE_CLIENT_ID",
        "GOOGLE_OAUTH_CLIENT_SECRET": "YOUR_GOOGLE_CLIENT_SECRET"
      }
    },
    "notion": {
      "command": "npx",
      "args": ["@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_TOKEN": "YOUR_NOTION_API_KEY"
      }
    },
    "sqlite": {
      "command": "uvx",
      "args": ["mcp-server-sqlite", "--db-path", "/Users/farricecain/data/knowledge.db"]
    }
  }
}
```

---

## Prerequisites

Make sure you have these installed:

```bash
# Check if uv is installed
which uvx

# If not, install it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Check if npx is available (comes with Node.js)
which npx

# If not, install Node.js from https://nodejs.org/
```

---

## After Setup

Once configured, restart your AI environment. The MCP servers should be available and I'll be able to:

- **Google Workspace**: Read/write your Docs, Sheets, search Drive
- **Notion**: Create pages, update databases, search workspace
- **SQLite**: Query your local databases

---

## Need Help?

If you get stuck on any step, let me know and I can walk you through it.
