# MCP Setup Guide: Perplexity Sonar + Tavily Research Tools

## Overview

The Antigravity research layer uses two MCP servers for research:

1. **Perplexity Sonar MCP** — Premium AI search with `sonar-deep-research` support
2. **Tavily Search MCP** — Free high-quality structured search for LLMs

Together they give us unlimited free research (Tavily) + premium deep research on demand (Perplexity).

---

## 1. Perplexity Sonar MCP Server

### What it replaces

The current `perplexity-ask` MCP only exposes a basic `perplexity_ask` function using the default Sonar model. The replacement exposes all Sonar models including `sonar-deep-research`.

### Recommended: pplx-api/perplexity-mcp

**Repository**: https://github.com/pplx-api/perplexity-mcp

**Installation**:
```bash
# Clone the repo
git clone https://github.com/pplx-api/perplexity-mcp.git
cd perplexity-mcp

# Install dependencies
npm install

# Build
npm run build
```

**MCP Configuration** (add to your IDE's MCP settings):
```json
{
  "mcpServers": {
    "perplexity-sonar": {
      "command": "node",
      "args": ["/path/to/perplexity-mcp/dist/index.js"],
      "env": {
        "PERPLEXITY_API_KEY": "YOUR_PERPLEXITY_API_KEY"
      }
    }
  }
}
```

**Alternative: perplexity-deep-research MCP**

If the above repo doesn't support `sonar-deep-research`, use this purpose-built alternative:

**Repository**: https://github.com/jsonallen/perplexity-deep-research-mcp

This specifically exposes a `deep_research` tool that uses `sonar-deep-research`.

---

## 2. Tavily Search MCP Server

### Why Tavily

Tavily is built specifically for LLM search. It returns structured, LLM-ready content with:
- Summary fields
- Source citations
- Content highlights
- Trimmed snippets — no post-processing needed

**Free tier**: 1,000 searches/month (plenty for our usage)
**Paid**: $50/month unlimited (worth it if we heavy-use research)

### Getting a Tavily API Key

1. Go to https://tavily.com
2. Sign up for a free account
3. Go to API Keys section
4. Copy your API key

### Recommended: tavily-ai/tavily-mcp

**Repository**: https://github.com/tavily-ai/tavily-mcp (official)

**Installation**:
```bash
# Via npx (simplest)
npx -y tavily-mcp@latest
```

**MCP Configuration**:
```json
{
  "mcpServers": {
    "tavily-search": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@latest"],
      "env": {
        "TAVILY_API_KEY": "YOUR_TAVILY_API_KEY"
      }
    }
  }
}
```

### Alternative: pinkpixel-dev/deep-research-mcp

This uses Tavily's Search + Crawl APIs for multi-step research:

**Repository**: https://github.com/pinkpixel-dev/deep-research-mcp

```bash
git clone https://github.com/pinkpixel-dev/deep-research-mcp.git
cd deep-research-mcp
npm install
npm run build
```

---

## 3. Final MCP Configuration

After setting up both servers, your combined MCP configuration should look like:

```json
{
  "mcpServers": {
    "perplexity-sonar": {
      "command": "node",
      "args": ["/path/to/perplexity-mcp/dist/index.js"],
      "env": {
        "PERPLEXITY_API_KEY": "YOUR_PERPLEXITY_API_KEY"
      }
    },
    "tavily-search": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@latest"],
      "env": {
        "TAVILY_API_KEY": "YOUR_TAVILY_API_KEY"
      }
    }
  }
}
```

### Store API Keys in .env

Add these to the project `.env` file:
```
PERPLEXITY_API_KEY=pplx-xxxxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxxxx
```

---

## 4. Verification After Setup

After configuring both MCP servers, verify they work:

1. **Test Perplexity Sonar**: Ask the agent to run `perplexity_sonar_search` (or whatever the tool name is) on a simple query
2. **Test Tavily**: Ask the agent to run `tavily_search` on a simple query
3. **Test Deep Research**: Run `/swarm-research` on a test topic and verify it produces grounded results with source URLs

---

## 5. Tool Priority After Setup

With both MCP servers active, the research tool priority becomes:

| Priority | Tool | Cost | Use Case |
|----------|------|------|----------|
| 1 | `search_web` | Free | Quick searches (built-in) |
| 2 | `read_url_content` | Free | Full page reads (built-in) |
| 3 | Tavily MCP | Free* | Structured LLM-ready search |
| 4 | Perplexity Sonar MCP | ~$0.01 | AI-synthesized search |
| 5 | Perplexity Deep Research | ~$0.25 | Strategic intelligence |

*Free for 1,000 calls/month

The research engine (`deep_research_engine.py`) will automatically route to the appropriate tool based on depth level and budget.
