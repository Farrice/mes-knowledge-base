# Context Window Optimization Diagnostic

## The Problem: Where Your Tokens Actually Go

Every Claude Code conversation starts with a massive **static overhead** before you type a single word. Then each workflow execution stacks additional dynamic loading on top. Here's the full breakdown.

---

## Static Context Budget (Every Conversation)

| Component | Chars | Est. Tokens | % of Static |
|---|---|---|---|
| **Workflow listing** (524 entries with full paths) | ~68,120 | **~17,030** | **53.8%** |
| Tool definitions (MCP servers, 70+ tools) | ~40,000 | ~10,000 | 31.6% |
| Knowledge Item summaries (20 items) | ~8,000 | ~2,000 | 6.3% |
| Conversation summaries (10 recent) | ~5,000 | ~1,250 | 3.9% |
| AGENTS.md (user rule) | 3,290 | ~820 | 2.6% |
| GEMINI.md (user rule) | 2,119 | ~530 | 1.7% |
| **TOTAL STATIC OVERHEAD** | **~126,500** | **~31,630** | **100%** |

> [!CAUTION]
> **~31,630 tokens are consumed before you type your first message.** That's roughly 15-20% of a 200K context window eaten by static scaffolding alone.

### The #1 Offender: The Workflow Listing

**524 workflow entries** are injected into every system prompt. Each entry includes the full absolute path (`/Users/farricecain/Google Antigravity/.agent/workflows/name.md`) plus a description. This single component eats **17,000+ tokens** — more than half of all static overhead.

You can't control this directly (it's Antigravity infrastructure), but there are structural moves to reduce its impact.

---

## Dynamic Loading Per Session

When you invoke a workflow, additional files get read into context:

| Load Type | Avg Chars | Avg Tokens | When |
|---|---|---|---|
| Workflow file | 2,214 | ~554 | Every `/command` |
| SKILL.md | 3,527 | ~882 | Chain Step 4 |
| genius.md | **17,079** | **~4,270** | Tier 2 (creative/complex) |
| Directive files (chain gates) | ~9,400 | ~2,350 | Intent pipeline, QA gates |
| KI artifact reads | varies | ~1,000-3,000 | Per artifact |

### A Typical `/extract-forge` Session

```
Static overhead:                    ~31,630 tokens
Workflow file (extract-forge):         ~1,830 tokens
Source transcript read:              ~5,000-15,000 tokens
Sub-workflow reads (extract, amplify):  ~2,000 tokens
SKILL.md creation/reading:              ~882 tokens
genius.md creation/reading:           ~4,270 tokens
Directive reads (QA, gates):          ~2,350 tokens
Chain runner output:                    ~300 tokens
Your prompts + AI responses:        ~20,000-50,000 tokens
─────────────────────────────────────────────
TOTAL: ~68,000-108,000 tokens PER FORGE SESSION
```

> [!WARNING]
> A single forge session can consume **35-55% of a 200K context window**. Multi-expert sessions (swarms, councils) can hit the ceiling fast.

---

## The Biggest Genius Files (Context Monsters)

| File | Chars | Tokens |
|---|---|---|
| kallaway-content-psychology/genius.md | 50,421 | **~12,605** |
| david-mcraney-belief-change/genius.md | 45,475 | ~11,369 |
| tom-noske-personal-brand/genius.md | 44,752 | ~11,188 |
| eric-roth-writing-mastery/genius.md | 44,691 | ~11,173 |
| jeremy-miner-identity-persuasion/genius.md | 42,217 | ~10,554 |
| sean-kochel-ai-business/genius.md | 42,162 | ~10,541 |
| ghostwriting-voice-engine/genius.md | 35,295 | ~8,824 |

> [!IMPORTANT]
> Loading ONE of these genius files uses as much context as all 20 Knowledge Item summaries combined. The Kallaway genius.md alone is **12,605 tokens** — that's 40% of your entire static overhead in a single file read.

---

## Optimization Strategy

The goal: **Cut 40-60% of overhead without losing any capability, nuance, or output quality.** Not by pruning knowledge — by restructuring access patterns.

### Tier 1: Structural Wins (High Impact, No Knowledge Loss)

#### 1. Workflow Index Restructuring
**Problem**: 524 workflow entries with full absolute paths take 17K tokens.
**Solution**: Create a lightweight routing index that clusters workflows by domain, so the system only needs to surface relevant clusters instead of the full list.

- Create `execution/workflow_router.py` — a script that takes a natural language query and returns the top 5-10 matching workflows
- This moves the routing intelligence from "dump everything in the prompt" to "query when needed"
- **Savings**: If the listing were reduced to top 50 most-used + domain routing, that's ~15K tokens saved per conversation

#### 2. Genius File Compression
**Problem**: 162 genius files averaging 17K chars each. The top 7 are 35-50K chars.
**Solution**: Already partially done (conversation `476914e3` referenced 149 genius files for compression). Continue that sprint.

- Target: Every genius.md under 15K chars (compress the 7 monsters above)
- Method: Extract reusable patterns into shared reference files, leave only expert-specific insights in genius.md
- **Savings**: 3-8K tokens per Tier 2 load

#### 3. AGENTS.md + GEMINI.md Deduplication
**Problem**: These two files contain ~50% overlapping instructions (The Chain, environment rules, critical overrides).
**Solution**: Merge into a single, tighter instruction set.

- Both define The Chain identically
- Both define environment rules
- Both define critical overrides
- A merged file could be ~3,500 chars instead of ~5,400
- **Savings**: ~500 tokens per conversation

### Tier 2: Loading Protocol Enforcement (Medium Impact, Better Discipline)

#### 4. Enforce Tier 0 First — Always
**Problem**: The Chain says "LOAD EXPERT BEFORE PRODUCING" which often jumps straight to Tier 1 or Tier 2. Many tasks only need routing (Tier 0).
**Solution**: Make the card check actually sufficient. Ensure `agents/_framework/invocation-cards.md` has enough information to route accurately without loading full skill files.

#### 5. Lazy Directive Loading
**Problem**: Directives like `intent-pipeline.md` (12K chars), `quality_assurance.md` (13.7K chars) are read in full even when only specific sections are needed.
**Solution**: Split hot-path directives into smaller, section-specific files:
- `directives/chain/score.md` (~500 chars)
- `directives/chain/sharpen.md` (~1,000 chars)
- `directives/chain/route.md` (~800 chars)
- Only load the section that's actually relevant

#### 6. Session State Discipline
**Problem**: `session-state.md` exists but is only 772 bytes. It's underused.
**Solution**: After every major operation, write the current expert, loaded files, and key decisions to session state. After compaction, this becomes the recovery point instead of re-reading everything.

### Tier 3: Architectural Moves (High Impact, Requires Some Restructuring)

#### 7. Two-Phase Conversation Architecture
Instead of one long conversation that loads everything, split work into:
- **Phase 1 (Light)**: Intent scoring, routing, planning — uses only Tier 0-1 loading
- **Phase 2 (Heavy)**: Expert execution — loads only what's needed for the specific task

This aligns with how Claude Code already handles context — each new conversation starts fresh. Strategic conversation splitting means each one carries less overhead.

#### 8. Workflow Deprecation Audit
**524 workflows is a massive surface area.** Some clusters have clear overlap:
- `content-series` + `content-series-plan` (identical intent)
- 5 `ai-brain-*` workflows (could be one with sub-steps)
- Multiple `proof-*` workflows (11 total — could consolidate to 3-4)
- Multiple `newsletter-*` workflows (8 total)
- Multiple `drk-*` workflows (12 total — not all deployed regularly)

A consolidation pass could reduce 524 → ~350-400 workflows, saving ~3-4K tokens in the listing alone.

---

## Implementation Priority

| # | Action | Token Savings | Effort | When |
|---|---|---|---|---|
| 1 | Merge AGENTS.md + GEMINI.md | ~500/conv | Low | Now |
| 2 | Continue genius compression sprint | ~3-8K/load | Medium | This week |
| 3 | Workflow deprecation audit | ~3-4K/conv | Medium | This week |
| 4 | Workflow router script | ~12-15K/conv | High | Next sprint |
| 5 | Split hot-path directives | ~2-5K/chain | Medium | Next sprint |
| 6 | Session state enhancement | Recovery savings | Low | Now |

---

## Key Insight: Structure > Compression

You're right that the fix isn't pruning or cutting. The Antigravity system has **incredible depth** — 193 skills, 162 genius files, 524 workflows, 51 directives. That's the asset.

The problem is that the system treats context like a buffet — everything gets plated before the order is taken. The optimization is in **access patterns**, not in reducing what exists:

1. **Don't list everything. Route to the right thing.**
2. **Don't load everything. Load just enough, then deepen on demand.**
3. **Don't keep everything in one conversation. Split when the task shifts.**

The intelligence is already there. The scaffolding just needs to be smarter about when and how it loads.
