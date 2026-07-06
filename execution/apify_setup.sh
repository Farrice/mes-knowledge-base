#!/usr/bin/env bash
#
# apify_setup.sh — register the Apify MCP server for Claude Code, then verify.
#
# One command to make the curated Apify actors available as native
# mcp__apify__* tool calls. Idempotent: removes any existing 'apify' server
# first, then re-adds with the full curated actor list.
#
# The actor list is NOT hardcoded here — it is emitted by
# `apify_client.py mcp-tools`, whose ACTORS dict is the single source of truth.
# Add an actor there and re-run this script; the MCP registration follows.
#
# Usage:  bash execution/apify_setup.sh
# Policy: directives/apify-usage-policy.md
set -euo pipefail

cd "$(dirname "$0")/.."

# Load .env so APIFY_TOKEN is available (never printed).
if [ -f .env ]; then
  set -a; . ./.env; set +a
fi

if [ -z "${APIFY_TOKEN:-}" ]; then
  echo "ERROR: APIFY_TOKEN not set. Add it to .env:" >&2
  echo "  APIFY_TOKEN=apify_api_xxxxxxxxxxxxxxxxxxxx" >&2
  echo "  (get it at https://console.apify.com/account/integrations)" >&2
  exit 1
fi

if ! command -v claude >/dev/null 2>&1; then
  echo "ERROR: 'claude' CLI not found on PATH — cannot register the MCP server." >&2
  echo "The Python wrapper still works: python3 execution/apify_client.py <cmd>" >&2
  exit 1
fi

TOOLS="$(python3 execution/apify_client.py mcp-tools)"
echo "Registering Apify MCP server with actors:"
echo "  ${TOOLS//,/, }"

# Idempotent re-register.
claude mcp remove apify -s project >/dev/null 2>&1 || true
claude mcp add apify -s project --env APIFY_TOKEN="$APIFY_TOKEN" -- \
  npx -y @apify/actors-mcp-server --tools "$TOOLS"

echo ""
echo "✅ Apify MCP registered (project scope). Restart the session to load the tools."
echo ""
python3 execution/apify_client.py verify
