# Fix: Context Window Truncation Crash

## Problem

The error `could not convert a single message before hitting truncation` means a **single message** in your conversation exceeds the model's maximum context window. The system prompt — injected into every single turn — is the culprit.

### Root Cause: System Prompt Obesity

Every message you send gets wrapped with **~57,000+ characters** of system injection before the model ever sees your actual request:

| Component | Characters | ~Tokens | % of Budget |
|-----------|-----------|---------|-------------|
| AGENTS.md (user rules) | 15,490 | 3,872 | 27% |
| GEMINI.md (user rules) | 5,350 | 1,337 | 9% |
| **416 workflow descriptions** | **57,074** | **14,268** | **64%** |
| Path overhead (full absolute paths × 416) | 22,880 | 5,720 | (included above) |
| **Total system prompt** | **~77,914** | **~19,478** | **100%** |

> [!CAUTION]
> **416 workflows consume 64% of your system prompt budget.** When combined with knowledge item summaries, conversation summaries, MCP server descriptions, and the platform's own system instructions, a single message can easily approach or exceed model limits — especially on smaller-context Gemini models.

### Why Gemini Models Hit This First

The error stack trace shows `jetski/cortex` and `gemini_coder` — Google's internal Gemini executor. Gemini models may have **smaller effective context windows** than Claude's 200K/1M, or the system applies heavier truncation budgets. Your AGENTS.md + GEMINI.md + 416 workflows = a system prompt so bloated that even a single user message can't fit after it's injected.

---

## Proposed Changes

### Phase 1: Emergency Workflow Triage (saves ~10,000 tokens)

#### [MODIFY] Workflow descriptions — trim to maximum 8 words each

Current descriptions average ~54 chars. Many are full sentences. The framework only needs a routing hint.

**Before:**
```
description: Build a systematic competitive intelligence system for analyzing competitors
```
**After:**
```
description: Competitive intelligence system
```

This alone saves ~5,000-8,000 tokens from the workflow injection block.

#### [NEW] `.agent/workflows/_index.md` — Workflow category index

Create a compact index that groups workflows by domain. The model can read this on-demand instead of having 416 paths injected into every message. This is a reference file, not a replacement for the frontmatter — but it gives the model a way to discover workflows without the full list.

---

### Phase 2: AGENTS.md Diet (saves ~1,500 tokens)

#### [MODIFY] [AGENTS.md](file:///Users/farricecain/Google%20Antigravity/AGENTS.md)

The Directive Index table alone is ~3,000 chars. Several sections duplicate information already in GEMINI.md. Specific trims:

1. **Remove the full Directive Index table** — replace with a single line: `Directives in directives/. Fire at trigger point. See directives/ listing.`
2. **Remove the "When Steps Narrow" table** — already covered by the chain logic itself
3. **Remove the "Chain Efficiency Rules" section** — duplicated in the Context Engine section
4. **Compress the Context Engine tier table** — it's already in both AGENTS.md AND GEMINI.md

Target: **AGENTS.md from 15,490 → ~10,000 chars** (~1,300 token savings)

---

### Phase 3: GEMINI.md Consolidation (saves ~500 tokens)

#### [MODIFY] [GEMINI.md](file:///Users/farricecain/Google%20Antigravity/GEMINI.md)

GEMINI.md duplicates large portions of AGENTS.md (The Chain steps, Context Engine tiers, Artifact-First rule). Since both are loaded as user rules simultaneously, this is pure waste.

**GEMINI.md should contain ONLY:**
1. The Zero-Crash Law (tool/text severance + compaction recovery)
2. The Deep Alignment Protocol (3 truths)
3. A one-liner: "See AGENTS.md for The Chain, Context Engine, and all protocols."

Target: **GEMINI.md from 5,350 → ~2,000 chars** (~800 token savings)

---

### Phase 4: Token Efficiency Protocol Update

#### [MODIFY] [token-efficiency-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/token-efficiency-protocol.md)

Add **Rule 7: System Prompt Hygiene** documenting:
- Maximum workflow description length: 8 words
- Quarterly audit: if workflows exceed 400, archive dormant ones
- AGENTS.md + GEMINI.md combined target: < 15,000 chars
- No duplication between AGENTS.md and GEMINI.md

---

## User Review Required

> [!IMPORTANT]
> This requires modifying your two core system files (AGENTS.md and GEMINI.md). The changes preserve all functionality — they only remove duplication and compress verbose descriptions.

> [!WARNING] 
> **The 416-workflow injection is the #1 problem.** Even after trimming descriptions, 416 workflows × ~30 chars each is still ~12,000 chars. Long-term, you may need to cap workflows at ~200 or implement a category-based lazy-loading system. But the immediate fix (trimming descriptions) should resolve the Gemini crash.

**Decisions needed:**
1. Approve trimming all 416 workflow descriptions to ≤8 words?
2. Approve de-duplicating GEMINI.md (removing Chain/Context Engine sections that are already in AGENTS.md)?
3. Do you want to archive any dormant workflows, or keep all 416?

---

## Verification Plan

### Automated Tests
```bash
# After changes, verify file sizes
wc -c AGENTS.md GEMINI.md
# Target: AGENTS.md < 11000, GEMINI.md < 2500

# Verify workflow description lengths
python3 -c "
import os, re
for f in sorted(os.listdir('.agent/workflows')):
    if f.endswith('.md'):
        with open(f'.agent/workflows/{f}') as fh:
            m = re.search(r'description:\s*(.+)', fh.read(500))
            if m and len(m.group(1).strip().split()) > 8:
                print(f'TOO LONG: {f}: {m.group(1).strip()}')
"
```

### Manual Verification
- Switch to a Gemini model and send a complex request with the full system prompt
- Confirm no truncation errors
- Verify all slash commands still route correctly with compressed descriptions
