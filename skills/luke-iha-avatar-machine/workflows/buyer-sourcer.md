---
description: Source raw "specific language" for a market via the 4S swiping protocol, VOC mining, and the 26 Master Survey Questions — EXECUTES real research (Perplexity / Playwright / Apify), does not invent VOC
tier: 2
stacks_with: avatar-manifold, competitor-intel, luke-iha-vsl-leads
wired: true
---

# Buyer Research Sourcer (WIRED)

The system models the *structure* of the wound; the **specific language** must be pulled from the market. This workflow gathers that raw VOC feedstock so the Manifold reads like a private monologue, not ad copy.

> **This workflow EXECUTES real research. It does not generate VOC from contextual knowledge.** Invented "voice of customer" is an auto-fail (Quality Gate). Every soundbite must be a verbatim pull with a source URL/handle.

## Pre-Flight Gate
- Market named + at least one place to mine (product reviews, a competitor offer, a subreddit, a YouTube channel, an email list).
- Live/JS-rendered or login-gated sources → use Playwright per `directives/browser-automation-safety.md`, not WebFetch.
- Budget awareness: Perplexity research is the primary engine ($30/mo, tracked `.agent/perplexity-usage.json`). Apify (review-scale scraping) only if needed, per `directives/apify-usage-policy.md` ($29/mo, `.agent/apify-usage.json`). Both degrade to WebFetch on synthesizable public pages.
- This is the difference between a 6 and a 9 on rubric criterion 6. Don't skip it for any client deliverable.

## Skill Acquisition
Load `references/framework-library.md` § J + § K. Load `source-prompts/sop-for-swiping.md` (where/how to swipe) + `source-prompts/master-survey-questions.md` (the 26 questions).

## Execution

### PHASE A — EXECUTE THE MINING (real tools, not recall)

**Recommended: dispatch a VOC sub-agent for context isolation** (raw scraping pollutes the main window). Use the 4-field envelope from `directives/sub_agent_protocol.md`:

```
Agent(subagent_type="deep-research", description="VOC mining: <market>", prompt="""
═══ OBJECTIVE ═══
Mine ≥30 VERBATIM voice-of-customer soundbites + 30–40 existing hooks for <market>, from REAL sources, each with a source URL/handle. No invented language.
═══ OUTPUT FORMAT ═══
- Write to: .tmp/copy-engine/voc-pack.md  (standalone runs may use .tmp/buyer-sourcer/voc-pack.md)
- Each soundbite row: "verbatim phrase" | source_url | tag(emotion|objection|failed-solution|desired-outcome|belief)
- Separate hook bank section (30–40 lines) with source.
- Return to orchestrator: STATUS + count-by-tag + source count + FILE + ≤500-token summary + CONFIDENCE.
═══ TOOLS ALLOWED ═══
ALLOW: mcp__perplexity-ask__perplexity_research, mcp__perplexity-ask__perplexity_search, WebFetch, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_click, Write(.tmp/**)
DENY: no further sub-agent spawns (no nesting); NO AI-generated/paraphrased VOC — verbatim only; do not clean up typos (raw phrasing is the gold)
═══ BOUNDARIES ═══
SCOPE: real, source-traceable soundbites + hooks only
ANTI-SCOPE: do NOT write copy, do NOT build the manifold, do NOT plot dimensions
HALT: after ≥30 soundbites OR sources genuinely exhausted (report which)
""")
```

**Or inline (when context budget allows)** — fire the tools directly:

```bash
// turbo
# Perplexity synthesis of reviews/forums/comments (primary). Logs to .agent/perplexity-usage.json via the perplexity-budget hook.
# (MCP call — run mcp__perplexity-ask__perplexity_research with a verbatim-VOC query, then WebFetch top sources for raw pulls.)
mkdir -p .tmp/copy-engine
echo "VOC mining started $(date -u +%FT%TZ) for market: <market>" >> .tmp/copy-engine/voc-mining.log
```
- **Perplexity** (`mcp__perplexity-ask__perplexity_research`): query for "verbatim complaints, objections, failed solutions, and desires from real <market> buyers on Reddit / Amazon / ClickBank / YouTube." Pull the cited source URLs.
- **WebFetch**: read the top 3–8 cited review/forum/comment pages in full to extract *verbatim* phrasing (Perplexity summarizes; WebFetch gets the raw voice).
- **Playwright** (`mcp__playwright__browser_*`): for JS-rendered / login-gated sources — FB Ad Library, gated forums, the offer's own funnel — per `directives/browser-automation-safety.md` (Tier 1 read-only auto-fires; state-changes need confirmation).
- **Apify** (optional, scale): for bulk review scraping, gate first per `directives/apify-usage-policy.md`; falls back to Perplexity at 90% budget.

### PHASE B — TAG + HARVEST (on the real pulls)
2. **Tag VOC** — every verbatim soundbite tagged: emotion · objection · failed-solution · desired-outcome · belief. Keep raw phrasing (typos and all).
3. **Survey option** — if the user has list/audience access, deploy a trimmed set of the 26 Master Survey Questions (Problem / Solution / Past-Experience / Belief / Constraint groups). Recommend 8–12 most relevant.
4. **Hook harvest** — 30–40 existing high-performing hooks from the niche (for Epiphany Threshold + Pick-Up Lines).

### PHASE C — PACKAGE
5. **Specific-Language Pack** → `.tmp/copy-engine/voc-pack.md`: soundbites by tag + hook bank + survey raw data + source list. Feeds directly into `/avatar-manifold`.

```bash
// turbo
# Deterministic floor check — fail loudly if the pack is thin or unsourced
python3 - <<'PY' || echo "VOC GATE: pack thin/missing — re-mine before proceeding"
import re,sys,glob
f=(glob.glob(".tmp/copy-engine/voc-pack.md")+glob.glob(".tmp/buyer-sourcer/voc-pack.md"))
if not f: sys.exit(1)
t=open(f[0]).read()
urls=len(re.findall(r'https?://',t)); modeled=t.upper().count("[MODELED]")
print(f"VOC pack: {urls} source links, {modeled} [MODELED] flags")
sys.exit(0 if urls>=15 and modeled==0 else 1)
PY
```

## Content Type Adaptations
| Source | Best for | Tool |
|---|---|---|
| Amazon/ClickBank reviews | Failed solutions, post-purchase soundbites | Perplexity + WebFetch (Apify at scale) |
| Reddit | Raw private-monologue language, taboo fears | Perplexity + WebFetch |
| YouTube comments | Beliefs, objections, market addictions | Perplexity + WebFetch |
| FB Ad Library | Live winning angles + hooks | Playwright (JS-rendered) |
| Offer funnel (gated) | Upsells, abandon-cart angles | Playwright |

## Output Requirements
- Tagged VOC soundbite bank (verbatim, ≥30) + hook bank (30–40) + optional survey set — at `.tmp/copy-engine/voc-pack.md`.
- Source list with links/handles for traceability (≥15 source URLs).

## Quality Gate
Soundbites are verbatim and tagged; sourced from real market locations (not invented); ≥15 source URLs; zero `[MODELED]`. The deterministic floor check above must pass. **Auto-fail**: "VOC" that is AI-generated or paraphrased; no source traceability; cleaned-up language that loses the raw voice; running this from contextual knowledge instead of firing the tools.
