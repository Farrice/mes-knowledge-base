#!/usr/bin/env bash
# reset-notebooklm.sh — Full Chrome session reset for notebooklm-mcp
#
# Run this when queries return:
#   - "Could not find chat input element"
#   - Playwright TimeoutError
#   - Any "arrow_forward" non-response
#
# Preserves: auth cookies, login data (no re-auth needed in most cases)
# Clears:    session state, cache, service workers
#
# Usage:
#   bash execution/reset-notebooklm.sh           # soft reset (session only)
#   bash execution/reset-notebooklm.sh --full    # full reset (requires re-auth)

set -e

PROFILE_DIR="$(dirname "$0")/../mcp-servers/notebooklm/chrome_profile_notebooklm"

if [[ ! -d "$PROFILE_DIR" ]]; then
  echo "Chrome profile not found at: $PROFILE_DIR"
  echo "Nothing to reset."
  exit 0
fi

FULL_RESET=false
if [[ "$1" == "--full" ]]; then
  FULL_RESET=true
fi

if $FULL_RESET; then
  echo "→ Full reset: removing entire Chrome profile (re-auth required)"
  rm -rf "$PROFILE_DIR"
  echo "✓ Profile deleted. Run a query to trigger re-authentication."
else
  echo "→ Soft reset: clearing session state, cache, service workers"
  rm -rf "$PROFILE_DIR/Default/Session Storage"
  rm -rf "$PROFILE_DIR/Default/Cache"
  rm -rf "$PROFILE_DIR/Default/Code Cache"
  rm -rf "$PROFILE_DIR/Default/Service Worker"
  rm -rf "$PROFILE_DIR/Default/BrowsingTopicsState"
  echo "✓ Session state cleared. Auth cookies preserved — no re-auth needed."
fi

echo ""
echo "Next step: run a test query to verify"
echo "  python execution/notebooklm_client.py query 30579fcb \"What are Kallaway's core hook patterns?\""
