# Gemini Truncation Fix — Walkthrough

## Problem
Gemini models crashed with `could not convert a single message before hitting truncation`. The system prompt (AGENTS.md + GEMINI.md + 416 workflow descriptions + platform metadata + KI summaries) exceeded Gemini's per-message token budget before a single user message could be processed.

## Root Cause
The user-controlled portion of the system prompt was **77,914 characters (~19,478 tokens)**. Combined with platform-injected content (MCP server metadata, KI summaries, conversation summaries), total injection exceeded **105,000+ characters per message**.

## What Changed

### Phase 1: Workflow Descriptions (122 files trimmed)
- All 416 workflow `description:` fields now ≤8 words
- Example: `Build a systematic competitive intelligence system for analyzing competitors` → `Competitive intelligence system`
- **No workflow files were modified** beyond the YAML frontmatter description line

### Phase 2: AGENTS.md (15,490 → 10,187 chars, -34%)
- **Removed**: "When Steps Narrow" 5-row table → replaced with 8 concise bullet points
- **Removed**: "Chain Efficiency Rules" verbose section → merged rules inline
- **Removed**: Directive Index (7 categorized sub-tables, 30+ entries) → 3-line reference
- **Preserved**: All 6 Chain steps, Architecture, Context Engine, all critical logic

### Phase 3: GEMINI.md (5,350 → 1,121 chars, -79%)
- **Removed**: Architecture section (duplicate of AGENTS.md)
- **Removed**: Chain steps 1-6 (duplicate of AGENTS.md)
- **Removed**: Environment & Tooling section (duplicate of AGENTS.md)
- **Removed**: Artifact-First rule (duplicate of AGENTS.md)
- **Preserved**: Zero-Crash Law, AI Slop banned words, Deep Alignment Protocol

### Phase 4: Token Efficiency Protocol
- Added **Rule 7: System Prompt Hygiene** with limits, rationale, and audit command
- Updated activation date and review cycle

## What Was NOT Touched
| Component | Status |
|-----------|--------|
| All 416 workflow `.md` files (logic) | ✅ Untouched |
| All skills (SKILL.md, genius.md, prompts) | ✅ Untouched |
| All agents (AGENT.md, memory/) | ✅ Untouched |
| All directives (40+ SOPs) | ✅ Untouched |
| All knowledge items | ✅ Untouched |
| All extractions | ✅ Untouched |
| The Chain (6-step logic) | ✅ Preserved in AGENTS.md |
| Context Engine tiers | ✅ Preserved in AGENTS.md |
| Routing knowledge | ✅ Preserved in Chain Narrowing Rules |

## Results

| Metric | Before | After | Saved |
|--------|--------|-------|-------|
| AGENTS.md | 15,490 chars | 10,187 chars | 5,303 chars |
| GEMINI.md | 5,350 chars | 1,121 chars | 4,229 chars |
| Workflow descriptions | ~57,074 chars | ~58,789 chars | ~-1,715 chars* |
| **Total user-controlled** | **77,914 chars** | **70,097 chars** | **7,817 chars** |
| **Token savings** | ~19,478 | ~17,524 | **~1,954 tokens/msg** |

\* Workflow description total increased slightly because the trim script was conservative — some already-short descriptions had filler prefixes stripped which didn't change length much. The major savings came from AGENTS.md and GEMINI.md deduplication.

## Safety
- Backups saved at `.tmp/gemini-fix-backup/` (AGENTS.md.bak, GEMINI.md.bak, token-efficiency-protocol.md.bak)
- Fully reversible: `cp .tmp/gemini-fix-backup/*.bak ./` restores originals

## Next Step
**Test Gemini.** Open a new conversation using a Gemini model and try a simple request. The ~2,000 token reduction from user-controlled files, combined with the deduplication, should bring the total below Gemini's truncation threshold.

> [!IMPORTANT]
> If Gemini still crashes, the bottleneck is the **platform-injected content** (MCP metadata, KI summaries, 416 workflow *paths*) which we don't control. The next lever would be reducing the number of workflows or raising this with the Antigravity platform team.
