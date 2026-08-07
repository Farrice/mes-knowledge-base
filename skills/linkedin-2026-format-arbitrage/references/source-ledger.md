# Source Ledger — LinkedIn 2026 Format Arbitrage

Claim-by-claim provenance for every attributed pattern in `SKILL.md`, `genius.md`,
and `references/genius-patterns.md`. Labels: **VERIFIED** (quote/number found
verbatim in a source file, or independently confirmed via live search),
**LIKELY** (concept matches source material but the skill's wording is a
paraphrase/synthesis, not a verbatim lift), **UNCONFIRMED** (no source file in
this repo backs the specific number/claim — flagged as a gap, not deleted per
the additive-only repair boundary).

## Tim Danilov — Niche Bending

| Claim | Label | Source |
|---|---|---|
| "Niche = Format + Market" formula label | LIKELY | Paraphrase of Danilov's documented mechanic, anchored `00:01:12`–`00:02:02` in the source video per `_active/harness/codex-harvest-2026-06-11/extractions/tim-danilov/niche-bending-system/source-map.md`. The compact `Format + Market` equation is a summary label, not a verbatim Danilov quote — never anchor it as one. |
| "Most people think a niche is just a topic" (anti-pattern) | VERIFIED | Verbatim, `_active/harness/codex-harvest-2026-06-11/extractions/video-context/fLDrB_wmbNE/transcript.txt` line 56-58, ~00:00:59. |
| "Anyone can copy a format, but very few can fill the formats with [genuine expertise]" (anti-pattern) | VERIFIED | Verbatim, same transcript, lines 580-586, ~00:10:26–00:10:36. |
| Tim Danilov took a channel "from zero to $56,000 a month in just 30 days," another to "150 million views," a third to "$23,000 in less than 90 days" | VERIFIED | Verbatim, same transcript, lines 27-38, ~00:00:26–00:00:41. |
| Source video is vidIQ's *"The NEW YouTube Strategy Dominating in 2026,"* uploader vidIQ, published 2026-02-16 | VERIFIED | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/fLDrB_wmbNE/metadata.json` (`upload_date: "20260216"`). |
| "Big-channel bias" and "No experiment" failure modes | VERIFIED | `_active/harness/codex-harvest-2026-06-11/extractions/tim-danilov/niche-bending-system/failure-modes.md` (named table rows, not paraphrased). |
| Note on provenance path | — | These Tim Danilov files live under `_active/harness/codex-harvest-2026-06-11/extractions/`, a historical import archive, not the top-level `extractions/` directory. Verified present and readable on disk at full size (not 0-byte/unrecoverable) — checked directly, not assumed. |

## Jasmin Alic — Three-Line Rule / Rhythm

| Claim | Label | Source |
|---|---|---|
| "The Three-Line Rule" — Line 1 hook, Line 2 blank, Line 3 cliffhanger re-hook | VERIFIED | `extractions/Jasmin_Alic_Extraction.md`, "The Three-Line Rule" section (Genius Patterns). |
| "If you want to get *through* to people, first get *in front* of people" | VERIFIED | Verbatim, `extractions/Jasmin_Alic_Extraction.md`, "Core Philosophy" (Agent Configuration section). |
| "Rhythmic Asymmetry (The Hip-Hop Carryover)" — balancing X-vs-Y statements | VERIFIED | `extractions/Jasmin_Alic_Extraction.md`, "Rhythmic Asymmetry" pattern. |
| 1-3-1 structural rhythm attributed jointly to Alic/Acosta | LIKELY | Alic's Three-Line Rule + Acosta's readability formatting are each independently sourced; the skill's fused "1-3-1" label is a synthesis, not a single verbatim source. |

## Lara Acosta — Content System

| Claim | Label | Source |
|---|---|---|
| "This defeats the typical viral LinkedIn slop" (anti-pattern) | VERIFIED | Verbatim, `extractions/lara-acosta-content-system/transcript.txt`. |
| "Where people fail in the execution is that they'll try and copy a viral post but they won't copy it correctly. They won't emulate it." (anti-pattern) | VERIFIED | Verbatim, `extractions/lara-acosta-content-system/transcript.txt`. |
| "...generic AI fluff that Chad GPT writes" (anti-pattern) | VERIFIED | Verbatim as auto-captioned (the transcript's auto-caption artifact "Chad GPT" = ChatGPT), `extractions/lara-acosta-content-system/transcript.txt`. |
| 1+3 Comment Formula ("leave 1 substantive comment, then 3 replies to other comments") credited by Acosta to Jasmin Alic, yielding "4x more profile views daily" | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md`, Pattern 7. |
| 4-3-2-1 content system, IFP/ICP targeting | VERIFIED | `extractions/lara-acosta-content-system/extraction-report.md`, Pattern 1 + Hidden Knowledge (IFP Engine). |

## Platform / Algorithm Claims

| Claim | Label | Source |
|---|---|---|
| LinkedIn's "360 Brew" algorithm update — foundation-model-based feed ranking, shift from engagement volume to depth signals | VERIFIED | Independently confirmed via live search: LinkedIn's 360Brew is a real, published decoder-only foundation model for personalized ranking (arXiv:2501.16450; LinkedIn engineering blog), not a fabricated name. Skill's *specific* framing ("focus shifted from likes to saves/dwell/2nd-degree comments") is the skill author's interpretation of public reporting on the model, not a direct LinkedIn quote — treat that framing as LIKELY, the model's existence as VERIFIED. |
| Zeigarnik Effect (open-loop psychology behind the Trapdoor Hook) | VERIFIED | Established psychological phenomenon (Bluma Zeigarnik, 1927) — general knowledge, not specific to any extraction in this repo. |
| Costly Signaling Theory applied to "Contextual Selfies" / "Anti-Guru" positioning | LIKELY | Costly signaling is an established concept in evolutionary biology/economics (Zahavi's handicap principle, Spence signaling theory); its specific application here to unpolished LinkedIn photos is this skill's synthesis, not a verbatim source claim. |

## Unconfirmed / Flagged Gaps

| Claim | Label | Why |
|---|---|---|
| Document carousels command "a 24.42% engagement rate" | **UNCONFIRMED** | No file under `extractions/` or the Tim Danilov/Alic/Acosta source packages contains this figure. Not removed (additive-only repair boundary) — flag before using this number in client-facing output; source it live or soften to a qualitative claim. |
| "Optimal length is 8-10 slides" for document carousels | **UNCONFIRMED** | Plausible platform best-practice but not traced to any source file in this repo. Treat as a working heuristic, not a cited fact. |
| Hall of Fame Exemplars ("SaaS Demo for Personal Branding," "Fitness Transformation for Career Growth") | N/A — not a factual claim | Both are explicitly labeled "(Reconstructed)" in `genius.md` — illustrative composites, not real posts being presented as real. No verification needed; flagged here only so the labeling isn't mistaken for an omission. |
