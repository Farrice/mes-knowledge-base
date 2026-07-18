# Provenance — michael-bernoff-identity-engineering repair (Wave 3 Lane 4 Batch 11)

Anchor → source file + location, for adversarial-verifier spot-checks.

| Anchor | Genius.md location | Source file | Line | Verified how |
|---|---|---|---|---|
| AN-1 (mirroring/rapport) | Anti-Patterns, bullet 1 | `knowledge/extractions/inbox/Claude-💡💰💎 Michael Bernoff ! This Mental Shift Will Finally Break You Out of Average.md` | 256 | `grep -n "Never mirror obviously"` — exact match |
| AN-2 (sorry/forgive me) | Anti-Patterns, bullet 2 | same file | 303 | `grep -n "is submissive"` — exact match |
| AN-3 (Good job) | Anti-Patterns, bullet 3 | same file | 179, 7648 | `grep -n "Never say .Good job"` and `grep -n "Good job. says"` — both exact matches |
| AN-4 (A-type deference) | Anti-Patterns, bullet 4 | same file | 1126 | `grep -n "This is exactly wrong"` — exact match |
| AN-5 (analytical=objection) | Anti-Patterns, bullet 5 | same file | 2365 | `grep -n "hear .objection"` — exact match |
| AN-6 (hollow Inner Hero) | Anti-Patterns, bullet 6 | same file | 1669 | `grep -n "Too weak and it's just flattery"` — exact match |
| Recognition-test phrasing | Model Calibration section + Anti-Patterns intro | N/A — original content per batch instruction | N/A | Written fresh, not sourced from a Bernoff quote; modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7-16 |

## Source file sizes (verified 2026-07-18, `wc -c`)

```
432060  knowledge/extractions/inbox/Claude-💡💰💎 Michael Bernoff ! This Mental Shift Will Finally Break You Out of Average.md
471091  knowledge/extractions/inbox/Claude-💡💰💎 Michael Bernoff ! This Mental Shift Will Finally Break You Out of Average pt.2.md
```

Both files are substantial, non-empty, non-0-byte Claude.ai chat exports (name fragments searched without punctuation via `find . -iname "*bernoff*"`; no tar/archive was involved for this skill's sources, so no `tarfile` per-member scan was needed — both candidate files are plain `.md` on disk).

## What was checked and ruled out

- `extractions/` (top-level dir) has no `bernoff` match — checked via `ls extractions/ | grep -i bernoff`, zero results.
- No raw/timestamped YouTube transcript for Bernoff exists anywhere in the repo (checked via repo-wide `find . -iname "*bernoff*"`) — only the two extraction-session exports above, plus downstream derivative artifacts (`agents/michael-bernoff/`, `research_outputs/ai_authority_architect_agents/michael_bernoff.md`, various `swarm_outputs/`) that are themselves generated FROM these two files, not independent sources.
- This absence was confirmed by directory search and file-size checks, not assumed — per the batch rule that a claim of "no source exists" is itself a provenance claim requiring verification.
