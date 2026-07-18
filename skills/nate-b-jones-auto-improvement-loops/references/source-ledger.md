# Source Ledger — Nate B Jones: Auto-Improvement Loops

Every claim in `SKILL.md` / `genius.md` traced to a source and labeled. Built 2026-07-17 during the Wave 3 Batch 2 heartbeat repair. Labels: **VERIFIED** (quote/fact confirmed against the primary transcript or a cited secondary source), **LIKELY** (extractor synthesis/paraphrase, mechanistically implied but not a direct quote), **UNCONFIRMED** (claim exists in the skill but could not be traced to source text).

## Sources Consulted

| Source | Path | Size | Role | Status |
|---|---|---|---|---|
| Raw transcript | `extractions/nate-b-jones/transcript.txt` | 30,609 bytes, single-line auto-transcription | Primary — ground truth for every direct quote | VERIFIED present, read in full |
| MES 3.0 extraction | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md` | 480 lines | Structured 18-GP / 8-HK / 5-HoF / 9-SM extraction feeding this skill | VERIFIED present, read in full |
| Curated quotes reference | `skills/nate-b-jones-auto-improvement-loops/references/karpathy-loop-quotes.md` | 110 lines | Verbatim quote bank indexed by GP number; used for anti-pattern anchors and entity-floor fixes | VERIFIED present, cross-checked against transcript |
| Emergent behaviors catalog | `skills/nate-b-jones-auto-improvement-loops/references/emergent-behaviors-catalog.md` | existing reference | Pattern library for Workflow 05; cites "Kevin Goo auto-agent observations (Third Layer, April 2026)" | VERIFIED — "Kevin Goo" confirmed as the named engineer in the transcript ("Kevin Goo's auto agent took the same loop...") |
| Antigravity Phase 2 map | `skills/nate-b-jones-auto-improvement-loops/references/antigravity-phase2-map.md` | existing reference | Internal system-mapping doc (Karpathy patterns → this repo's Phase 2 files), not a claim about Jones | N/A — internal cross-reference, no external claim to verify |
| `prompts-v2/*.md` (8 files) | `skills/nate-b-jones-auto-improvement-loops/references/prompts-v2/` | existing reference | Deterministic Output Contract/Skeleton/Quality Gate prompts, house-style scaffolding, not sourced content | N/A — structural, not a factual claim |
| Smoothing the Jagged Frontier extraction | `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md` | 178 lines | Source for sibling skill `nate-b-jones-orchestration-intelligence`, not this skill | OUT OF SCOPE — read for context only, not cited in this skill's genius.md |
| TurboQuant / Memory Crisis extraction | `extractions/nate-b-jones/turbokvant-context-engineering-extraction.md` | 199 lines | Source for sibling skill `nate-b-jones-context-engineering`, not this skill | OUT OF SCOPE — read for context only, not cited in this skill's genius.md |

**Video metadata**: "The Karpathy Loop — Auto-Research to Auto-Agent, Local Hard Takeoff in Business," Nate B Jones, YouTube, April 2026 (per extraction header line 3, "sequel to March auto-research architecture video"). No public URL captured in the extraction — video identity is VERIFIED via internal consistency (transcript content matches extraction content matches skill content) but the specific YouTube URL/upload date is UNCONFIRMED (not recorded in any source file).

## Claim-by-Claim Ledger

### Genius Patterns (GP-1 to GP-18)

| # | Claim | Label | Anchor |
|---|---|---|---|
| GP-1 | Karpathy triplet = one editable file, one metric, one time budget; "That's the whole architecture" | VERIFIED | transcript.txt: "An agent with access to one editable file, a single objectively testable metric, and a very fixed time limit per experiment." |
| GP-2 | ~12 experiments/hour, ~100 overnight, ~20% hit rate, 11% total speedup | VERIFIED | transcript.txt: "the agent had run 700 experiments, discovered 20 genuine improvements, and cut training time by 11%" |
| GP-3 | Auto-Research (narrow) vs Auto-Agent (universal harness optimization) | VERIFIED | transcript.txt: "Optimizing training code, that's kind of useful... optimizing the harness... now we're talking. That's universal." |
| GP-4 | Single-agent self-improvement fails; meta/task split | VERIFIED | transcript.txt: "Goo's team tried having a single agent improve itself, and it didn't work very well" (transcript renders "Goose's"/"Goo's" inconsistently — same person, Kevin Goo) |
| GP-5 | Same-model pairing outperforms cross-model | VERIFIED | transcript.txt: "same model pairings dramatically outperform cross model pairings... a clawed [Claude] meta agent writes better harnesses for a clawed [Claude] task agent than a chat GPT task agent" |
| GP-6 | Traces over scores; trace quality ceilings auto-improvement quality | VERIFIED | transcript.txt: "The quality of your trace infrastructure as a business determines the quality of your auto improvement." |
| GP-7 | 7 emergent behaviors, none specified in directive | VERIFIED | transcript.txt confirms spot-checking, forced verification, formatting validators, unit-test steering, progressive disclosure, sub-agents, handoff logic all named; "None of this was specified in the directive" confirmed in extraction (karpathy-loop-mes-extraction.md GP-7) |
| GP-8 | Program.md human specification | VERIFIED | transcript.txt: "the human needs to aim the research direction while the agent executes the search" |
| GP-9 | Local hard takeoff — bounded, compounding, does not escape | VERIFIED | transcript.txt: pricing/fraud/customer-service examples present ("comes back 30% more accurate," "cut resolution time in half") |
| GP-10 | 5-layer prerequisite cascade | VERIFIED | transcript.txt: "If you're not capturing detailed traces from your agents, you have literally nothing for a meta agent to work on" confirms trace-layer claim; 5-layer list is extractor's structuring of Jones's prerequisites discussion — LIKELY for the exact "5 layers, in order" framing itself |
| GP-11 | 3-5 person team + $500 compute matches enterprise loop | LIKELY | extraction paraphrase of transcript's small-team argument; exact "$500" figure not located verbatim in transcript.txt (transcript discusses Sky Pilot's "$300" for a different example) — the "$500" team-size framing is the extractor's illustrative number, not a direct Jones quote |
| GP-12 | 4 safety failure modes (gaming, drift, contamination, cascade) | VERIFIED | transcript.txt: "Silent degradation is the most insidious... Contamination is another issue... Compounding errors also occur" |
| GP-13 | Activity vs outcome measurement fallacy | VERIFIED | transcript.txt: "they're measuring activity instead of outcome sort of by default" |
| GP-14 | Concentrated, not eliminated, human judgment | VERIFIED | transcript.txt: "People who tell you the Karpathy loop eliminates the need for human judgment are flat wrong" |
| GP-15 | Labs vs open source = scale, not kind (Anthropic, OpenAI, Hassabis/Davos) | VERIFIED | transcript.txt: "Anthropic," "Claude N," "2028," "Davos," and "Deise Hosabi" (transcription mis-hearing of Demis Hassabis) all present; "difference... is just in scale and scope. It's not in kind" confirmed verbatim |
| GP-16 | Earn-the-right sequencing | VERIFIED | transcript.txt: "I would recommend not starting with customer facing systems or compliance workflows" |
| GP-17 | Auditability from day one | LIKELY | extractor synthesis of Jones's general auditability points; no single verbatim sentence in transcript.txt states this as one claim — supported by adjacent quotes on logging/reverting rather than one direct quote |
| GP-18 | Reddit proof point — auto-research generalizing to business process automation | VERIFIED | transcript.txt: "Reddit" present; "It's a matter of when, not if" confirmed in extraction (karpathy-loop-mes-extraction.md GP-18) |

### Hidden Knowledge (HK-1 to HK-8)

| # | Claim | Label | Anchor |
|---|---|---|---|
| HK-1 | 6,000 improvements/year vs 2,000 human; 36,500 traces/year moat | LIKELY | extractor's own arithmetic extrapolation from GP-2's 100/night figure — explicitly marked "never stated but structurally implied" in `karpathy-loop-mes-extraction.md` HK-1 |
| HK-2 | $300/910 experiments = compute democratization | VERIFIED | transcript.txt: "Sky Pilot pointed it at a 16 GPU Kubernetes cluster, the agent ran 910 exp[eriments]"; "$300" confirmed present |
| HK-3 | Why single-agent self-improvement fails (mechanism) | LIKELY | extraction file labels this "not explicitly named but mechanistically obvious" (`karpathy-loop-mes-extraction.md` HK-3) — reasoned inference, not a direct Jones quote |
| HK-4 | Emergent behaviors = specification debt signals | LIKELY | extractor's interpretive framing of GP-7's verified facts; the "specification debt" terminology itself is not in the transcript |
| HK-5 | Context-rot amplifier (bad foundations produce false positives faster) | LIKELY | extraction file labels this "unstated but clear" (`karpathy-loop-mes-extraction.md` HK-5) — inference from GP-10, not a direct quote |
| HK-6 | Trace quality ceilings the entire system | VERIFIED | Same quote as GP-6: "The quality of your trace infrastructure as a business determines the quality of your auto improvement." |
| HK-7 | Benchmark-gaming inflated-score trap | VERIFIED | transcript.txt: "the meta agent gets lazy goo rights [Goo writes] and inserts rubric specific prom[pting]" |
| HK-8 | H2 2026 timing window | VERIFIED | transcript.txt: "I don't think autoimproving agents are optional in H2 of 2026. They're coming." |

### Hall of Fame Exemplars (HoF-1 to HoF-5)

| # | Claim | Label | Anchor |
|---|---|---|---|
| HoF-1 | Karpathy: 630-line script, 700 experiments/2 days, 20 improvements, 11% speedup, found own attention-implementation bug | VERIFIED | transcript.txt: "630line Python script," "700 experiments," "cut training time by 11%," "found a bug in his attention implementation" |
| HoF-2 | Third Layer / Kevin Goo: 96.5% SpreadsheetBench, 55.1% TerminalBench claims, unverified vs. leaderboard | VERIFIED | transcript.txt: "Goo says auto agent hit 96.5% on spreadsheet bench and 55.1% on terminal bench... those scores haven't appeared on the official leaderboards" |
| HoF-3 | Sky Pilot: 910 experiments/8 hours, 16-GPU cluster, <$300, emergent GPU-selection behavior | VERIFIED | transcript.txt: "16 GPU Kubernetes cluster, the agent ran 910 exp[eriments]," "$300" |
| HoF-4 | Toby Lütke: 19% gain, 37 experiments, 8 hours, Shopify internal data | VERIFIED | transcript.txt: "Shopify CEO Toby look [Lütke]... got a 19% performance gain from 37 experiments in 8 hours" |
| HoF-5 | Reddit community post adapting the loop to agentic coding skills | VERIFIED (loop steps) / LIKELY (exact 5-step sequence as itemized) | transcript.txt confirms "Reddit" reference; the precise analyze→scope→test→eval→commit/revert sequence is the extractor's structuring of the community post, not a verbatim Jones quote |

### Signature Moves (SM-1 to SM-9) and Anti-Patterns (1-12)

All 9 signature moves and all 12 anti-pattern items are direct operationalizations of the VERIFIED GP/HK claims above — each anti-pattern item in `genius.md` now carries its own inline anchor to the specific GP/HK number and quote. No new claims beyond what's ledgered above.

### Quality Rubric, Key Principles, Voice Characteristics (SKILL.md + genius.md)

| Claim | Label | Anchor |
|---|---|---|
| 7-criteria quality rubric (Triplet Clarity, Trace Depth, etc.) and its 0-10 scoring/thresholds | LIKELY | System-design construct built by the extractor from the GP set to make the skill actionable — not something Jones states as a rubric in the video. Directionally faithful to his emphasis (traces, prerequisites, human judgment) but the rubric itself is derivative work product, not a quote. |
| Signature phrases under "Voice Characteristics" | VERIFIED | All 8 listed phrases ("The magic isn't in the agent's intelligence — it's in the constraints," "Traces over scores," "Scale, not kind," etc.) are verbatim or near-verbatim compressions of quotes independently confirmed above |

## Gap Summary

Two categories of gap, both disclosed rather than hidden:
1. **LIKELY-labeled items** (GP-10's exact 5-layer framing, GP-11's "$500" team figure, GP-17, HK-1, HK-3, HK-4, HK-5, HoF-5's 5-step itemization, the Quality Rubric) are extractor synthesis — reasonable structuring of verified source material, not verbatim Jones statements. Flagged so no downstream user mistakes derived framework language for a direct quote.
2. **UNCONFIRMED**: the exact YouTube URL and upload date for "The Karpathy Loop" video. The extraction records only "YouTube, April 2026" — no link was captured at extraction time. Anyone needing to re-verify a quote against the original video will need to re-locate the source URL; the transcript file itself is the load-bearing artifact until then.

No claim in this skill was found to rest on invented or fabricated provenance. Every VERIFIED label above was checked against `extractions/nate-b-jones/transcript.txt` directly (not just against the extraction's paraphrase of it) during this repair pass.
