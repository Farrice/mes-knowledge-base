# PROVENANCE — skills/self-evolving-systems repair (Wave 3 Lane 4 Batch 15)

Anchor → source file + location, for every new citation added to `genius.md` during this repair. All sources were opened and read directly by this worker (not assumed); byte sizes were captured with `wc -c`.

| Anchor text added | Location in repaired genius.md | Source file (bytes) | Location in source |
|---|---|---|---|
| "700 experiments in 48 hours. 20 genuine improvements discovered" | GP-2 Grounding; Anti-Pattern #? (not used there) | `research_outputs/research-karpathy-wiki-architecture.md` (16,007) | "Results" bullet, line ~45 |
| "even failures are data" | GP-3 Grounding; Anti-Pattern #3 (Success Bias) | `directives/skill-evolution-protocol.md` (9,363) | "Safety Rails," rule 4 |
| "94-99% of finalize scores were 8+ while real iteration counts were 2-3 passes" | GP-4 Grounding; Anti-Pattern #1 (Score Worship) | `directives/excellence-prediction-protocol.md` (7,555) | "Purpose" section, paragraph 2 |
| "10 minutes per benchmark task" / "inspired by Karpathy's 5-minute training runs" | GP-5 Grounding | `directives/skill-evolution-protocol.md` (9,363) | Step 5, "Test Variant (Time-Boxed)" |
| one file (`train.py`), one metric, fixed 5-minute window | GP-6 Grounding | `research_outputs/research-karpathy-wiki-architecture.md` (16,007) | "Constrained Arena" bullet, line ~41 |
| "11% speedup (2.02 → 1.80 hours)"; QK-Norm scalar multiplier | GP-7 Grounding | `research_outputs/research-karpathy-wiki-architecture.md` (16,007) | "Results" bullet, line ~45 |
| "42,000 GitHub stars in one week" | GP-8 Grounding | `research_outputs/research-karpathy-wiki-architecture.md` (16,007) | "Generalizability" bullet, line ~49 |
| Activation Count 42, 76 Phase 1 entries, 2026-04-09 | HK-1 Grounding | `directives/skill-evolution-protocol.md` (9,363) | "Usage Tracking" table |
| `evolution_store/v2_traces/` corpus, "159 files at time of writing" | HK-2 Grounding | `directives/excellence-prediction-protocol.md` (7,555) | "Why predictions can be trusted" |
| grade-inflation detector, >80% of last 10 traces ≥8 | HK-3 Grounding | `directives/excellence-prediction-protocol.md` (7,555) | "2. `detect_grade_inflation()`" section |
| `execution/skill_benchmark.py benchmark <skill-name>` | HK-4 Grounding | `directives/skill-evolution-protocol.md` (9,363) | Step 1, "Benchmark Current State" |
| "3 consecutive DISCARD results on the same skill" | HK-5 Grounding; Anti-Pattern #5 (Iteration Inflation) | `directives/skill-evolution-protocol.md` (9,363) | "Stopping Criteria" |
| "94-99% of finalize scores were 8+..." (2026-04-24 audit) | Anti-Pattern #1 (Score Worship) | `directives/excellence-prediction-protocol.md` (7,555) | "Purpose" section |
| "the ratchet name comes from git: each success adds a commit, each failure reverts" | Anti-Pattern #2 (Trace Amnesia); Verbatim Grounding blockquote 2 | `research_outputs/research-karpathy-wiki-architecture.md` (16,007) | "The Ratcheting Loop" bullet, line ~39 |
| "10+ outputs with < 0.5 variance" (Plateau trigger) | Anti-Pattern #4 (Premature Optimization) | `directives/skill-evolution-protocol.md` (9,363) | "When to Trigger Evolution" table |
| "Load `skills/<skill>/genius.md` at session start (tier 2 instead of tier 1)" | Anti-Pattern #6 (Skill Neglect) | `directives/excellence-prediction-protocol.md` (7,555) | "Routing decisions /autopilot makes" table |
| "modify only the targeted aspect (process steps, inline patterns, quality gate criteria)" | Anti-Pattern #7 (Monolithic Prompts) | `directives/skill-evolution-protocol.md` (9,363) | Step 4, "Generate Variant" |
| "You're not touching any of the Python files. Instead, you are programming the program.md Markdown files..." | Verbatim Grounding blockquote 1 | `research_outputs/research-karpathy-wiki-architecture.md` (16,007) | "Program.md" bullet, line ~43 |

Every anchor above was cross-checked against the cited file's actual text at repair time (2026-07-18). None is fabricated; none paraphrases a quote that isn't present verbatim where quotation marks are used. Items NOT anchored to a real source (the MetaHarness arXiv paper's own GP/HK claims, "Yoonho Lee") are left as pre-existing, unaltered content and flagged UNCONFIRMED/LIKELY in `references/source-ledger.md` rather than given a fabricated anchor.
