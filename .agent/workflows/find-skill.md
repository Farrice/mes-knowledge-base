# /find-skill — Find the right skill via local keyword search

> **Why this exists**: Claude Code's skill auto-fire uses keyword matching against a character-budgeted listing (default ~1% of context). With 257 skills, most descriptions get truncated to ~30 chars at session start — so auto-fire is unreliable for anything beyond the first few skills loaded. This workflow bypasses auto-fire entirely.
>
> Investigation that surfaced the mechanism: 2026-05-23 test of `nate-b-jones-context-engineering` — utterance "My agent forgets everything between conversations" did NOT fire the skill in a fresh Claude Code session despite the description containing the trigger phrase. Root cause: listing truncation + keyword-match-not-semantic.

## When to Use

- You know there's a skill for what you want, but can't remember the slash command
- You typed a natural question and Claude went into plan-mode-and-clarify instead of firing the matching skill
- You're exploring what skills exist for a domain ("anything for newsletter growth?")
- You want a sibling check before invoking — see what *else* might apply

## How to Run

```bash
python3 execution/find_skill.py "<what you want to do, in natural language>"
```

### Examples that exercise different match surfaces

```bash
# Sibling discrimination (the case auto-fire failed on)
python3 execution/find_skill.py "my agent forgets everything between conversations"

# Creative invocation
python3 execution/find_skill.py "make a vintage poster for a wellness retreat"

# Strategy / positioning
python3 execution/find_skill.py "we're stuck in a crowded market and pricing power is eroding"

# Domain exploration
python3 execution/find_skill.py "anything for newsletter growth"
```

### Flags

- `--top N` — show top N matches (default 5)
- `--rebuild-index` — force rebuild of the cached skill index
- `--json` — machine-readable output (for piping or scripts)

## Output Format

```
Top 3 matches for: 'my agent forgets everything between conversations'

1. nate-b-jones-context-engineering   score 18.4
   → /nate-b-jones-context-engineering
   Architects memory and context systems for agentic systems using Nate B. Jones's TurboQuant-informed methodology…

2. memory-architect   score 9.2
   → /memory-architect
   Design persistent memory with decay, episodic/semantic/procedural tiers…

3. self-evolving-systems   score 7.8
   → /self-evolving-systems
   Runs MetaHarness propose-evaluate-log-iterate loops to permanently improve agentic systems…

Invoke by typing the slash command above.
```

## How Matching Works

BM25 keyword scoring across each skill's:
- **Name** (×3 weight — names are intentional, repeating boosts signal)
- **Description** (the YAML frontmatter field)
- **"When to Use" section** (high-signal trigger surface)

Query-side **synonym expansion** via `SYNONYMS` map in `find_skill.py` — maps Farrice's idiom ("forgets", "stuck", "viral", "poster", "picks") to canonical search terms. This is the high-leverage tuning surface — when matching whiffs, add the user's phrasing to SYNONYMS pointing at the words that actually appear in the matching skill's description.

## Index

Cached at `.agent/skill-index.json`, keyed by per-file mtime. Auto-rebuilds when any `SKILL.md` changes. The cache survives across sessions.

## When This Workflow Fails

- **No results** → query too vague or no matching skill exists. Try different words, or use this as evidence that a skill needs to be built.
- **Right skill not in top 5** → its description probably doesn't contain the keywords you typed. Two fixes: (a) add your phrasing to `SYNONYMS`, (b) rewrite the skill's description to front-load typed phrases.
- **Top score < 5** → matches are weak. Add domain words to the query (e.g., "agent forgets" → "AI agent memory persistence").

## Related Infrastructure

- **Skill index**: `.agent/skill-index.json` — JSON cache of all parsed SKILL.md frontmatter + when-to-use sections
- **Synonym map**: `execution/find_skill.py:SYNONYMS` — user-curated idiom → canonical
- **Audit doc that drove this**: `_active/_archive/2026-08-07-sweep/system-integration/2026-05-22-description-rewrite-followup.md`
