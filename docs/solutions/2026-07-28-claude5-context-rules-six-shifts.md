# Solution Card — Claude-5 Context Rules: the Six Shifts (+ vetted video commentary)

**Date**: 2026-07-28 · **Type**: harness doctrine · **Status**: ACTIVE — this card is the rubric for the canonical-file diet

## Primary source (the real thing — contrast with the fabricated "Boris graph-engineering" wave)
**"The New Rules of Context Engineering for Claude 5 Generation Models"** — Thariq Shihipar, Member of Technical Staff, Anthropic, **2026-07-24** (Opus 5 launch day): https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
Headline claim (VERIFIED, author-stated): *"We removed over 80% of Claude Code's system prompt for models like Claude Opus 5 and Claude Fable 5 with no measurable loss on our coding evaluations."* (No public benchmark tables — the eval evidence is asserted, not published.)

## The six shifts (all VERIFIED at primary source)

| # | From → To | Author's reasoning | Antigravity status |
|---|---|---|---|
| 1 | Rules → Judgment | "Newer models have better judgement and can handle these decisions well without explicit rules" — old rules guarded weaker models' worst cases | Partially adopted 2026-07-27 (Model Dialect block); CLAUDE.md still carries 4.8-era defensive prose |
| 2 | Examples → Interface design | "Giving examples actually constrains them to a certain exploration space" — hint via parameter/enum design instead | **This is Farrice's standing fear, confirmed by the vendor.** Template-heavy skills may cap ceiling on creative work |
| 3 | Upfront → Progressive disclosure | Load context at the right time; verification moved into selectable skills; deferred tool loading | Largely already ours (Context Engine tiers, skills, deferred tools) |
| 4 | Repetition → Simplicity | Duplicated instructions across surfaces create conflicts; "conflicting rules make the model burn reasoning tokens deciding which instruction wins" | CLAUDE.md ↔ MEMORY.md ↔ directives triple-state many rules — prime diet target |
| 5 | Manual CLAUDE.md memory → Auto-memory | "Claude now automatically saves memories that are relevant" | Already ours (auto-memory dir + episodic L1) |
| 6 | Simple specs → Rich references | Test suites, HTML artifacts, rubrics, verifier agents over verbose markdown | Partially ours (Output Contracts v2, eval anchors); room to replace prose rules with checkable artifacts |

**CLAUDE.md guidance verbatim**: "Keep your CLAUDE.md lightweight and briefly describe what your repo is for, but spend most of the tokens on gotchas inside of the codebase." Tooling: **`claude doctor` / in-session `/doctor`** "to rightsize your skills, and CLAUDE.md files" (present in installed CLI 2.1.220).

**What the post does NOT say**: it contains **no caveat list** (nothing on cost gates, factual rules, safety constraints). The keep-list below is ours, not Anthropic's.

## Video claim-vet — youtube.com/watch?v=B7SfSrJcIBQ ("Anthropic Deleted 80% of Claude's Own Instructions", creator "Dylan", AI consultant, 17:22, transcript 4,280 words at `extractions/claude5-context-rules/transcript.txt`)

| Claim | Verdict |
|---|---|
| "Anthropic deleted 80% of the instructions for their own AI" | VERIFIED, minor scope inflation — it's Claude Code's system prompt specifically |
| The three "myths" (examples, hard rules, repetition) | VERIFIED — matches shifts 1/2/4; video omits shifts 3/5/6 |
| "Examples set a ceiling / narrow intelligence" | VERIFIED — near-verbatim from post |
| Aesthetics-vs-standards split (match format, don't copy approach); extract "standards" from examples, preserve disagreements between examples | Dylan's own framework, NOT in post — SOUND, adoptable |
| Rules → "pointers" ("write code that reads like the code around it"; "match my last 3 messages in this thread") | VERIFIED concept (post's rules→judgment example); "pointer" is Dylan's coinage |
| "AI randomly chooses between conflicting instructions" | PARAPHRASE — post says conflicts burn reasoning tokens; "random" overstates |
| Contradiction-audit prompt (list every instruction from every surface; show only conflicts; say which you'd keep) | Dylan's own — SOUND, directly applicable to CLAUDE.md/MEMORY.md/directives triple-state |
| One instruction, one home (project file vs skill vs chat) + scope skills to folders | VERIFIED — real Claude Code features, aligned with shift 4 |
| Keep HARD rules where financial/legal/reputational risk lives | Dylan's escape hatch, ABSENT from the Anthropic post — matches our compass doctrine exactly |
| OpenAI GPT-5.6 "shorter prompts scored better + ~50% cost savings" studies | UNCONFIRMED — no primary source located this pass; do not cite |

**Extract-forge gate verdict (recorded per gate-first binding)**: source is 4,280 words of derivative commentary → **below forge floor (8,000+ rich)**. Light extract only — this card IS the extraction. No standalone skill.

## Known pushback (capture, don't ignore — HN via developersdigest.tech)
- First-day Opus 5 regression reports ("accidental deletions, far more mistakes")
- "+30–40% document length after switching to Opus 5" — matches our own P2/P6 verbosity-drift probe finding
- Lock-in concern: judgment moves from portable .md into Anthropic tooling
- Auto-memory: "I absolutely don't want things added to some memory behind my back"

## The Antigravity keep-list (immune to the diet — ours, since the post has no caveats)
1. **Cost gate** (money) 2. **Factual veto** (truth) 3. **Git/citation integrity + one-tool-per-tree** (loss prevention) 4. **Notion version pin** (a real gotcha — exactly what Anthropic says CLAUDE.md is FOR) 5. **Extraction-never-gated** (standing decision)

## Baseline for post-diet measurement (recorded 2026-07-28)
- Last 15 performance-log entries: 9 System / 3 production (20%); composites flat 7.0–9.0
- CLAUDE.md 3,672 words · 8-file canonical surface 35,121 words · 17 hook registrations (4 per prompt)
- Re-measure after 5 post-diet sessions: production share should rise; felt-verdict from Farrice wins over metrics (auto-evolution ≠ ground truth)

Related: `memory/project_graph-engineering-verdict.md` (the fake-attribution contrast case) · `directives/model-dialects/claude-opus-5.md` · `research_outputs/2026-07-28-graph-engineering-deep-research.md`
