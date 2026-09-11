# Cost table — keep Poppy vs the Canvas vs hybrid (2026-09-10)

## What he pays today (his words: "over $600 in the highest memberships")
Claude Max, Google AI Ultra, ChatGPT Pro — the three plans the Canvas seats ride on.
Poppy on top: $1/7-day trial now; the $399/yr self-serve tier is gone, current tiers are
demo-call priced (reviewers report $66–90/mo; AppSumo lifetime $279–$4,459 by credit cap).

## Monthly, steady state

| Line | Keep Poppy | The Canvas (as built) | Hybrid |
|---|---|---|---|
| Tool fee | ~$66–90/mo (credit tier) or $399/yr legacy if still honored | $0 | $0 |
| Claude turns | included in Poppy credits | $0 marginal — `claude -p` on the Claude Max plan (usage counts against the plan's quota, not dollars) | same |
| Gemini turns | included | ~$0.0006 (Flash) to ~$0.01 (Pro) per turn, metered | same |
| GPT turns | included | $0 marginal on ChatGPT Pro via codex — blocked until the codex CLI is upgraded | same |
| YouTube / TikTok listing, YouTube transcripts, articles, PDFs, voice notes | included | $0 (yt-dlp, transcript API, trafilatura, pypdf, whisper.cpp) | $0 |
| Instagram profile pulls | included | 5 vidIQ credits per creator (2,000/mo already in the plan he pays) | same |
| TikTok / Instagram video transcripts | included (their vendor) | vidIQ watch credits, or his own browser cookies to yt-dlp (his call) | keep Poppy only for this |
| Infra | none | none — the always-on server already runs on his Mac | none |
| **Total new spend** | **$66–90/mo** | **$0–2/mo** | **$0–2/mo + Poppy only if IG/TikTok transcripts matter weekly** |

## One heavy session (5 × 30-min videos → 10 chat turns)
| | Poppy | Canvas |
|---|---|---|
| Ingest | credits (reviewer: 5 long videos ate "a noticeable chunk" of 2,000) | ~20 s, $0 |
| Context per turn | their cap | ~50K tokens |
| 10 Sonnet turns | credits | $0 marginal; the plan's own quota is the ceiling (est. shown per turn: ~$0.30–0.50 each at API rates, for reference) |
| Wall time per reply | streams as it thinks | 6–15 s, arrives whole |

## Build cost
| | |
|---|---|
| Spent so far | one Fable session (~5 h wall, on plan) + 2 Sonnet test turns + $0.0006 Gemini + 5 vidIQ credits |
| Remaining polish for option A (replace for the one job) | ~1 session: source-card thumbnails, "send to /extract", IG profile node via vidIQ, TikTok/IG transcript via vidIQ watch |
| Remaining for option B (feature parity) | +1–2 sessions: image nodes (Claude vision), streaming replies (needs the API seat, breaks the $0 rule), multiplayer never |

## The honest line
The Canvas is free at the margin because it spends the three plans he already pays for.
The only thing Poppy still does that costs money to replicate is reading a TikTok or
Instagram video's words; vidIQ credits cover it inside the plan he already has.
