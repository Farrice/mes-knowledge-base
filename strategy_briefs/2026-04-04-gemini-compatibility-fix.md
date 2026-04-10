# Intelligence Brief: Making Gemini Functional in Antigravity

**Date**: 2026-04-04
**Scan Type**: Research Swarm (3 parallel agents)
**Classification**: Technical Intelligence + Platform Research

---

## Executive Summary

Gemini fails in Antigravity for **5 confirmed reasons**, 3 of which are fixable in under an hour. The production GEMINI.md is a broken 25-line stub that delegates to AGENTS.md (a Claude-specific file), while the purpose-built `.gemini/rules/` system and a higher-scoring variant (002, clarity 10/10, integrity 10/10) sit unused in the evolution store. Beyond this configuration error, Google's own documentation confirms that Gemini drops constraints placed early in long prompts -- exactly where our system puts The Chain. The community consensus is that Gemini should NOT be a drop-in Claude replacement for orchestration, but should be deployed for research, scanning, and cost-sensitive bulk work. Three quick fixes will make Gemini functional; a gated execution architecture will make it good.

---

## Root Cause Confirmation Table

| # | Root Cause | Prior Status | New Status | Evidence |
|---|-----------|-------------|-----------|----------|
| 1 | Zero-Crash Law (tool/text mixing) | Known bug | **CONFIRMED + EXPANDED** | Still broken in April 2026. Gemini randomly cycles between 3 response formats. `thought_signature` field in Gemini 3.x is a new mandatory requirement that breaks all middleware/proxies that strip it. Reported across 10+ projects (Vercel AI SDK, Goose, ADK-Python, n8n, OpenCode). |
| 2 | System prompt truncation (~58K) | Known crash | **MODIFIED** | Actual workflow injection is **29,814 chars** (not 58K). Total system prompt is ~43K bytes (~10.8K tokens). Size is NOT the primary issue. The real problem is **constraint placement** -- Google's own prompting guide confirms Gemini drops constraints that appear early in long prompts. |
| 3 | Shallow execution | Known pattern | **CONFIRMED + ROOT CAUSE FOUND** | Three causes: (a) critical instructions at prompt START get dropped; (b) gated execution modes not implemented; (c) ambient context (folder names, existing files) overrides explicit instructions. Official Google documentation: "constraints placed too early may be dropped for complex requests." |
| 4 | Multiple GEMINI.md copies (7 versions) | Known mess | **CONFIRMED + FIX READY** | Root production copy (1,121 bytes) is a stub pointing to AGENTS.md. Variant 002 (1,317 bytes, clarity 10/10, integrity 10/10) properly references `.gemini/rules/` + `gemini-reference.md`. Was never promoted to production. |
| 5 | AGENTS.md dependency unclear | Suspected | **CONFIRMED BROKEN** | AGENTS.md opens with "guidance to Claude Code" and includes Artifact-First Delivery Rule (Claude-only). All critical Chain/routing/quality content IS duplicated in `.gemini/rules/`. Missing pieces (env, directories) ARE covered by `directives/gemini-reference.md`. AGENTS.md should NOT be referenced. |

### NEW Root Causes Discovered

| # | New Root Cause | Severity | Evidence |
|---|---------------|----------|----------|
| 6 | **.gemini/rules/ files may NOT auto-load** | CRITICAL | Gemini CLI auto-discovers files named `GEMINI.md` via BFS, NOT arbitrarily-named `.md` files. Our `chain.md`, `routing.md`, `quality.md`, etc. may be invisible to Gemini. If true, Gemini sees ONLY the 25-line stub. **Needs live testing to confirm.** |
| 7 | **`thought_signature` field (Gemini 3.x)** | HIGH | New mandatory field for multi-step tool calling. Any middleware that strips it causes hard failures. Wasn't in Gemini 2.5, mandatory in 3.x. Breaks all OpenAI-compatible proxies. |
| 8 | **Constraint placement is inverted** | HIGH | Our system puts critical rules at the TOP of GEMINI.md. Google's own Gemini 3 Prompting Guide says: "Place core request and most critical restrictions as the FINAL line." We're doing exactly the opposite. |
| 9 | **52+ workflows reference Claude-only tools** | MEDIUM | 35 files reference `search_web`, 30 reference `read_url_content`, 27 reference sub-agent spawning. These tools don't exist in Gemini CLI. Affected workflows will fail silently. |

---

## Fix Priority Matrix

| # | Fix | Effort | Impact | Dependencies |
|---|-----|--------|--------|-------------|
| 1 | **Replace root GEMINI.md with Variant 002** | 5 min | CRITICAL | None |
| 2 | **Verify .gemini/rules/ auto-loading** (run `/memory show` in Gemini session) | 2 min | CRITICAL | None -- determines if rules are even visible |
| 3 | **Restructure constraint placement** -- move critical rules to END of GEMINI.md | 30 min | HIGH | Depends on #2 results |
| 4 | **Patch 3 sub-agent references** in .gemini/rules/ (context-engine.md, memory.md x2) | 15 min | MEDIUM | None |
| 5 | **Implement gated execution pattern** (Default/Plan/Execute/Finalize modes) | 2-4 hrs | HIGH | After #1-3 validated |
| 6 | **Create Gemini tool alias layer** for 52+ affected workflows | 4-8 hrs | MEDIUM | Strategic decision on Gemini's role |
| 7 | **Investigate thought_signature handling** in IDE model switcher | 1 hr | HIGH | May require IDE version check |
| 8 | **Define Gemini's role** (research/scanning vs full orchestration) | Decision | STRATEGIC | Informs effort allocation for #5-6 |

---

## Immediate Actions (This Week)

### Action 1: Promote Variant 002 to Root GEMINI.md

**Current state:** Root GEMINI.md says "Read AGENTS.md" (wrong file, Claude-specific language)
**Fix:** Copy `evolution_store/variant_002/GEMINI.md` to root `GEMINI.md`

This alone fixes:
- Broken delegation chain (stops referencing AGENTS.md)
- Proper reference to `.gemini/rules/` (where the real system lives)
- Proper reference to `directives/gemini-reference.md` (env, directories, knowledge sources)
- Removes the Artifact-First Delivery Rule dependency (Claude-only feature)

### Action 2: Verify Rules Auto-Loading

**Test:** Open a Gemini session, run `/memory show` to see what the model actually has in its context.

**If `.gemini/rules/` files ARE loaded:** Great -- proceed with constraint placement fixes.
**If `.gemini/rules/` files are NOT loaded:** Two options:
- (a) Rename them to `GEMINI.md` pattern (e.g., `.gemini/rules/chain/GEMINI.md`)
- (b) Use `@chain.md` import syntax in root GEMINI.md to explicitly include them

### Action 3: Restructure for Gemini's Attention Pattern

Google's official guidance: constraints at the END of prompts, not the beginning.

Current structure (WRONG for Gemini):
```
CRITICAL RULES  ← Gemini drops these first
Environment
Reference
Modular rules list
```

Correct structure (per Google prompting guide):
```
Environment
Reference  
Modular rules list
CRITICAL RULES  ← Gemini pays most attention here
```

Also apply to `.gemini/rules/chain.md` -- the Zero-Crash Law should be the LAST rule, not the first.

### Action 4: Patch Sub-Agent References

3 locations in `.gemini/rules/` reference sub-agent spawning (Gemini can't do this):
- `context-engine.md` line 13: "Tier 3 -- Sub-Agent"
- `memory.md` line 19: "Sub-agent spawn" as compaction trigger
- `memory.md` line 76: "Sub-Agent: 2+ experts loaded"

Replace with: "When 7+ files loaded or 2+ experts needed: save session state via `execution/checkpoint_manager.py`, then load sequentially in fresh context."

---

## Medium-Term Actions (Next 2 Weeks)

### Action 5: Implement Gated Execution Architecture

The leading Gemini configuration pattern from Google Cloud community:

```markdown
## <PROTOCOL:DEFAULT>
[Listening mode -- score intent, identify domain]

## <PROTOCOL:PLAN>  
[Read-only -- load expert files, read workflows, no output]
[Activated by: receiving a deliverable request]
[Gate: Cannot produce without completing PLAN]

## <PROTOCOL:EXECUTE>
[Production mode -- produce output using loaded context]
[Activated by: explicit user approval OR Score 4-5]

## <PROTOCOL:FINALIZE>
[Quality gate -- score, run chain_runner.py]
[Activated by: completion of EXECUTE]
```

This maps directly to our Chain:
- DEFAULT = Step 1-2 (SCORE + SHARPEN)
- PLAN = Step 3-4 (ROUTE + LOAD)
- EXECUTE = Step 5 (PRODUCE)
- FINALIZE = Step 6 (FINALIZE)

Each mode is a "hermetically sealed container" preventing instruction bleed.

### Action 6: Define Gemini's Role in Antigravity

Community consensus on multi-model task splitting:

| Task Type | Best Model | Rationale |
|-----------|-----------|-----------|
| Complex orchestration, multi-file refactoring | Claude Opus | Deep instruction following, reliable tool calls |
| Research, scanning, context analysis | Gemini 2.5 Pro | 1M token context, lower cost |
| Cost-sensitive bulk operations | Gemini Flash | ~80% cheaper, good for parallel tasks |
| Strategic decisions | Claude | "Makes decisions with clean inputs, not raw noise" |
| Creative content, expert frameworks | Claude | Embodies expert thinking, not just terminology |

**Recommendation:** Don't make GEMINI.md equivalent to CLAUDE.md. Create a reduced-scope Gemini role:
- **Use Gemini for**: `/research-swarm`, `/parallel-research`, `/spy-market`, large file scanning, first-pass analysis
- **Keep Claude for**: The Chain, expert loading, content production, quality gates, `/extract`, `/writers-room`

### Action 7: Tool Compatibility Layer for Workflows

52+ workflow files reference Claude-only tools. Three approaches:

**(a) Gemini tool mapping** (add to GEMINI.md or .gemini/rules/):
```
When a workflow says "search_web" → use google_web_search
When a workflow says "read_url_content" → use web_fetch
When a workflow says "Agent tool" → use sequential execution (no sub-agents)
```

**(b) Wrapper scripts** in `execution/`:
- `execution/web_search.py "query"` → works on any model
- `execution/url_reader.py "url"` → works on any model

**(c) Accept that research workflows are Claude-only** and route them accordingly.

---

## What We Still Don't Know

| Unknown | Why It Matters | How to Resolve |
|---------|---------------|---------------|
| Does `.gemini/rules/` auto-load in the IDE? | If not, Gemini has NO Chain, no routing, no quality gates | Run `/memory show` in a live Gemini session |
| Does the IDE model switcher handle `thought_signature`? | If not, all Gemini 3.x tool calls fail | Test Gemini 3.x in IDE, check for `thought_signature` errors |
| Which Gemini model does the IDE use? (2.5 Pro, 3 Flash, 3.1 Pro) | Different models have different tool-calling reliability | Check IDE model picker options |
| Does prompt caching work across model switches? | Could reduce cost of model-specific prompt engineering | Test with IDE |
| Is the `@file.md` import syntax available in the IDE? | Determines our modular loading strategy | Test in live session |

---

## Testing Protocol

### Quick Validation (5 minutes)
1. Replace root GEMINI.md with Variant 002 content
2. Open fresh Gemini session in IDE
3. Run `/memory show` -- confirm what Gemini sees
4. Ask: "Score this intent: write me a LinkedIn post about content creation" 
5. Check: Does it print CHAIN Step 1? Does it name Lara Acosta? Does it attempt to load SKILL.md?

### Chain Compliance Test (15 minutes)
1. Request: "Write me 3 LinkedIn headline options for an S&C coach"
2. Expected: Steps 1-6 executed, Lara Acosta loaded, real file reads, quality gate scored
3. Fail conditions: Training data substitution, no file reads, no quality scores, tool/text mixing crash

### Research Workflow Test (10 minutes)
1. Request: `/research-swarm "test topic"`
2. Expected: Web searches attempted, URLs read, structured output
3. Fail conditions: `search_web` tool not found error, hallucinated research, crash

---

## Sources (Cross-Referenced)

### Official Google Documentation
- [Gemini CLI Configuration](https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html)
- [Gemini CLI Tools Reference](https://geminicli.com/docs/reference/tools/)
- [GEMINI.md Context Files](https://geminicli.com/docs/cli/gemini-md/)
- [Gemini 3 Prompting Guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide)

### Bug Reports & Issues
- [TrajectoryChatConverter truncation crash](https://discuss.ai.google.dev/t/trajectorychatconverter-loads-all-installed-skills-into-system-message-causing-truncation-crash-on-gemini-models/135808)
- [thought_signature breaking tool calls](https://community.n8n.io/t/issue-with-gemini-3-0-gemini-3-pro-preview-tools-function-call-is-missing-a-thought-signature/223824) + [Vercel #10344](https://github.com/vercel/ai/issues/10344) + [ADK-Python #3705](https://github.com/google/adk-python/issues/3705) + [Goose #5792](https://github.com/block/goose/issues/5792)
- [Instruction following degradation P0](https://github.com/google-gemini/gemini-cli/issues/6474)
- [Gemini 3 ignoring system prompts](https://discuss.ai.google.dev/t/gemini-3-not-adhering-to-system-prompts/110320)
- [150K+ token system prompt investigation](https://github.com/openclaw/openclaw/issues/21999)

### Community Best Practices
- [Gated Execution / Bloated GEMINI.md fix](https://medium.com/google-cloud/practical-gemini-cli-structured-approach-to-bloated-gemini-md-360d8a5c7487) (Prashanth Subrahmanyam)
- [GEMINI.md Hierarchy Part 1](https://medium.com/google-cloud/practical-gemini-cli-instruction-following-gemini-md-hierarchy-part-1-3ba241ac5496) + [Part 2](https://medium.com/google-cloud/practical-gemini-cli-instruction-following-gemini-md-hierarchy-part-2-84386bba51a6)
- [Multi-Model AI Orchestration](https://dev.to/zaferdace/multi-model-ai-orchestration-for-software-development-how-i-ship-10x-faster-with-claude-codex-53l3)

### Multi-Model Tools
- [LiteLLM](https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models) -- unified proxy for multi-model routing
- [claude-code-proxy](https://github.com/1rgs/claude-code-proxy) -- purpose-built for running Claude Code on non-Anthropic models

---

## Claims Grounding

| Claim | Source | Status |
|-------|--------|--------|
| Gemini drops constraints placed early in long prompts | Google Gemini 3 Prompting Guide (official) | GROUNDED |
| `.gemini/rules/*.md` files may not auto-load | Gemini CLI docs show only GEMINI.md auto-discovery | GROUNDED (needs testing) |
| `thought_signature` is mandatory in Gemini 3.x | 10+ independent project bug reports | GROUNDED |
| Variant 002 scored clarity 10/10, integrity 10/10 | Local evolution store metadata | GROUNDED |
| Root GEMINI.md delegates to AGENTS.md | Direct file read | GROUNDED |
| 52+ workflow files reference Claude-only tools | Grep audit of 445 workflow files | GROUNDED |
| Community recommends Gemini for research, Claude for orchestration | Multiple practitioner reports (DEV.to, Arsturn, Ofox) | GROUNDED |
| Gemini tool/text mixing crash still occurs (April 2026) | Multiple Google AI Forum reports | GROUNDED |
| System prompt is ~43K bytes (~10.8K tokens) | wc -c measurements | GROUNDED |
| 60% cost savings with intelligent multi-model routing | Arsturn analysis | SUPPLEMENTED (their specific setup) |
| Gated execution fixes shallow instruction following | Google Cloud community (one detailed case study) | SUPPLEMENTED (limited sample) |
