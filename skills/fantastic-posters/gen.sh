#!/usr/bin/env bash
# Wrapper for node generate.js that sources FAL_KEY (and optional KIE_KEY)
# from the project root .env (single source of truth).
#
# This skill's gitignore covers .env, so we never duplicate the key into the
# skill directory. The wrapper sources the parent .env and execs node.
#
# Usage:
#   ./gen.sh "<brief>"
#   ./gen.sh "<brief>" --quality=low --n=1 --yes
#   ./gen.sh --batch=path/to/listings.json --quality=high
#   ./gen.sh --list
#
# Always pre-flight via the budget guard before calling this:
#   python3 ../../execution/fal_budget_guard.py check --quality=<...> --n=<...>

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
ENV_FILE="$PROJECT_ROOT/.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "ERROR: project root .env not found at $ENV_FILE" >&2
  exit 1
fi

FAL_KEY="$(grep -E '^FAL_KEY=' "$ENV_FILE" | head -1 | cut -d= -f2-)"
if [[ -z "$FAL_KEY" ]]; then
  echo "ERROR: FAL_KEY is empty in $ENV_FILE" >&2
  exit 1
fi
export FAL_KEY

# KIE_KEY is optional — `|| true` keeps pipefail from killing the wrapper when absent
KIE_KEY="$(grep -E '^KIE_KEY=' "$ENV_FILE" | head -1 | cut -d= -f2- || true)"
if [[ -n "$KIE_KEY" ]]; then
  export KIE_KEY
fi

cd "$SCRIPT_DIR"
exec node generate.js "$@"
