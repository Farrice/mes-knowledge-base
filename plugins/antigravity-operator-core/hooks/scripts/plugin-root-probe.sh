#!/bin/bash
# F-SYS fixture probe. Echoes the resolved plugin root so the fixture can
# prove ${CLAUDE_PLUGIN_ROOT} expands after a local install. If this prints
# an empty path, plugin path resolution is broken and the lift fails.
if [ -z "$CLAUDE_PLUGIN_ROOT" ]; then
  echo "PLUGIN ROOT PROBE: FAIL — CLAUDE_PLUGIN_ROOT unset"
else
  echo "PLUGIN ROOT PROBE: ok — $CLAUDE_PLUGIN_ROOT"
fi
