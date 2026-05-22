# Plugin Patches

Local patches applied to installed Claude Code plugins. Plugin caches at
`~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/` may be wiped or
overwritten by plugin updates — these patches must be re-applied when that
happens.

## Inventory

### `hookify-rule-engine-operators.patch`

**Target**: `~/.claude/plugins/cache/claude-plugins-official/hookify/<hash>/core/rule_engine.py`

**Purpose**: Adds the `contains_any` operator and fixes `not_contains` to
support regex-alternation patterns. Without this patch, 7 of 8 hookify Stop
rules silently no-op because they all use `contains_any` (an operator that
doesn't exist in the upstream rule engine) — discovered 2026-05-22.

**Audit story**: The 4 pre-existing rules (`freshness-tax-enforcement`,
`performance-log-reminder`, `quality-gate-enforcement`,
`intent-pipeline-check`) were created using a `contains_any` operator that
was never implemented in the engine. The unknown-operator default of `False`
caused every condition to fail silently. The hookify defense layer was
theatrical infrastructure for months. The 3 new Wave-1-5 rules
(`autopilot-ledger-reminder`, `routing-coverage-check`,
`anchor-named-discipline`) shipped with the same operator pattern and hit
the same bug.

**Fix**:
- `contains_any` → treats pattern as regex alternation (`re.search` with
  IGNORECASE). Plain text is valid regex, so backward-compatible.
- `not_contains` → upgraded from literal-substring negation to regex
  non-match. Patterns like `"VERIFIED|grounding-pass|deep-research-gemini"`
  now correctly check whether ANY of those substrings appear in the
  transcript (returning False if any match, True if none).

**Apply**:
```bash
HOOKIFY_DIR=$(ls -d ~/.claude/plugins/cache/claude-plugins-official/hookify/*/core)
cd "$HOOKIFY_DIR"
patch -p1 < /Users/farricecain/Google\ Antigravity/execution/patches/hookify-rule-engine-operators.patch
```

**Verify after applying**:
```bash
cd "$(ls -d ~/.claude/plugins/cache/claude-plugins-official/hookify/*/core)"
grep -q "contains_any" rule_engine.py && echo "✓ patch applied" || echo "✗ NOT applied"
```

**Upstream fix recommended**: file an issue with the hookify plugin
maintainers (Anthropic's claude-plugins-official) to add `contains_any` to
the supported operator set in `core/rule_engine.py _check_condition`.
