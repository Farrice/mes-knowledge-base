# Source Ledger — nick-saraev-agentic-workflows

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 12). Every claim of Saraev provenance in this skill, labeled VERIFIED / LIKELY / UNCONFIRMED, with the file actually checked.

## Sources checked (with sizes, per envelope rule 2 — no "unrecoverable" claim without a file read)

| File | Size | Content |
|---|---|---|
| `extractions/Nick Saraev/transcript.txt` | 276,999 bytes | Full transcript, "the definitive guide to copywriting for outbound" (cold email/DM/LinkedIn course) |
| `extractions/nick-saraev/transcript.txt` | 276,999 bytes | Byte-identical to above (`diff -q` confirms) |
| `extractions/nick-saraev-cold-outreach/transcript.txt` | 276,999 bytes | Byte-identical to above |
| `extractions/nick-saraev-outreach/transcript.txt` | 276,999 bytes | Byte-identical to above |
| `extractions/nick-saraev-bottleneck-thinking/transcript.txt` | 13,589 bytes | Separate, shorter transcript — sibling skill's source, not this skill's |
| `extractions/nick-saraev-bottleneck-thinking/extraction-report.md` | 8,773 bytes | Sibling skill's extraction report |
| `extractions/nick-saraev-cold-outreach/research.md` | 4,979 bytes | Secondary research notes, not a primary transcript |
| `_active/codex-harvest-2026-06-11/agents/nick-saraev/AGENT.md` | — | Codex-harvested persona description; no citations of its own |
| `_active/harness/claude-export/` | — | Harvest index/state files present (`index.json`, `triage/*.json`, `INDEX.md`); no file matching "saraev" by name; no content match for the claimed 2026-07-01 export |

**Finding**: the only located primary-source Saraev material is one 276,999-byte transcript (duplicated across four extraction folders), and it is a cold-outbound/copywriting course — not the "6-hour agentic workflows course" this skill is named for. No transcript, report, or export file for a Saraev agentic-workflows/DO-framework/self-annealing course was found anywhere in the repo.

## Claim-by-claim

### VERIFIED (verbatim, quote matched against the transcript above)

- "no fluff" — Saraev's stated course standard. `extractions/Nick Saraev/transcript.txt`, offset ~1,150.
- "if it is not clear to my prospect what the meeting is... a conversation sort of has a different connotation than a meeting" — same file, offset ~85,768.
- "if you don't have some sort of like definition of done, you won't be able to go to the next part, which is the risk mitigation" — same file, offset ~86,706.
- "a template that you use once may work for like a week or two weeks or a month or a year or whatever, but eventually it'll stop working" — same file, offset ~112,814.
- "tactics don't work anywhere near as the higher level strategy. The strategy is the system. The tactic is the template." — same file, offset ~114,493.
- "I don't actually recommend having offers be like financially based" — same file, offset ~70,045.

These six quotes ground the new "Anti-Patterns (Sourced)" and "How to Use This Skill (Model Calibration)" sections in genius.md. They are genuinely Saraev's words — but drawn from his cold-outbound course, applied here to offer-design and system-design principles that generalize (definition of done, template-vs-system) rather than to agentic-build specifics, since no agentic-build transcript exists.

### UNCONFIRMED (no locatable source file)

- The entire "Patterns from claude.ai export — Nick Saraev conversations (2026-07-01)" subsection in genius.md (Start-at-the-End Build Sequencing, Template Conditioning, Component Reuse Library, Close the Revision Loop, C-I-O-R-E Prompt Skeleton, The Compression Pass, One-Shot Sweet Spot, Monte Carlo Prompt Testing, Smarter-Model Debiasing, Conversational vs Knowledge Engines, The Spartan Tone Hack, Revenue Proximity Principle, The Paradox of Speed, Become Infrastructure, Perceived Value Stacking, Price Doubling, Value = Cash Flow ÷ Risk, AI Is the Least Important Part of AI Consulting, Auxiliary-Service COGS Arbitrage). The section claims "six transcript-grounded extractions" dated 2026-07-01. Verified absent from the one located transcript: searched for "1SecondCopy", "900" (deal count), "Golden Goose", "GPT-3", "big-four", "ChatGPT wrapper", "efficiency," and "generic" as distinguishing terms — none appear in `extractions/Nick Saraev/transcript.txt`. The genius.md file itself carries a 2026-07-01 mtime, consistent with an editing pass on that date, but the underlying export was not found in `_active/harness/claude-export/` or anywhere else searched. Flagged inline in genius.md with a provenance note; content preserved (additive-first) but must not be cited as verbatim Saraev quotes.
- The "6-hour masterclass," "DO framework," and "self-annealing systems" framing in `SKILL.md` and `_active/codex-harvest-2026-06-11/agents/nick-saraev/AGENT.md` — plausible description of Saraev's public content (he does teach agentic/automation building on YouTube), but no transcript of that specific course exists in this repo to verify wording, structure, or the "DO framework" name against.
- Hall of Fame Exemplars 1 and 2 in genius.md (Adaptive Content Curator, Dynamic Customer Support Triage) — illustrative constructed workflows, not attributed to a specific Saraev case study. Treat as pattern illustration, not sourced provenance.
- The 39 `references/prompts-v2/crown_jewel_*.md` execution prompts — built on the DO-framework/self-annealing frame above; not independently re-verified in this pass (out of scope: `workflow_contracts` already passes and prompts-v2 files were not touched).

### LIKELY

- None promoted to LIKELY this pass — the binary split above (one verified cold-outbound transcript vs. one unconfirmed agentic-workflows pattern set) didn't produce a middle tier. Any future source discovery for the UNCONFIRMED tier should re-grade those items VERIFIED before they're cited as quotes.

## What would resolve the UNCONFIRMED tier

Locate the original 2026-07-01 claude.ai export (six Saraev conversations: graphic design agent live build, "$2.4M prompt engineering hacks," 900-deal offer analysis, premium positioning, AI monetization, big-four consulting frameworks) or the source video/transcript for Saraev's actual agentic-workflows course. Until then, the patterns are directionally usable (they're internally consistent with Saraev's documented systems/pricing philosophy in the verified transcript) but should not be delivered to a client as verbatim Saraev quotes.
