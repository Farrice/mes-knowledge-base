# Tool Stack — The One-Person AI Marketing Machine

The named tools Oren cites, mapped to the weekly block they serve. The point isn't the specific vendor (swap freely) — it's that each block has a *named input, named tool, named output* so the solo operator never wonders what to do with the hour.

## By Weekly Block

| Block | Tools | What they do |
|-------|-------|--------------|
| **New Creative (8h)** | Dribbble, Behance | Source designers for new statics |
| | Minea / Insense-style UGC packs | Buy packs of UGC at decent rates |
| | Meta Creator Manager (Marketplace), Tribe | Creator outreach; Tribe enables % -of-ad-spend deals |
| | Motion, Social Growth Engineers (SaaS), video databases, Cut/30 content-review newsletter | Ad-idea references → turn quickly into briefs |
| | Notion / spreadsheet | The lightweight brief + follow-up tracker for the creative funnel |
| **Performance (2× 2h, capped)** | Facebook Blueprint, Google Ads certification | Free, platform-provided media-buying training (done in pre-prep) |
| | Meta → Google → TikTok (physical/lifestyle) → YouTube (services at scale) | The channel-sequence; the brand-voice machine feeds the creative |
| **Funnel (4h)** | Landing-page builder + lead-form tooling | Match LP to messages; optimize form rows; abandoned-cart flows |
| **Collateral + Email (4h)** | Email platform (broadcast/automation/segmentation) | Sales enablement (PDFs, testimonials, templates), founder plain-text emails |
| **Influencer (1 day)** | Social Snowball (affiliate at checkout + outreach), Meta Creator Manager, Tribe | Outreach, contracts, % deals, deliverable tracking |
| **Word-of-Mouth (prep)** | Social Snowball (the Grunes growth pattern) | Affiliate/referral layer at checkout + post-purchase emails so every sale can compound |

## The AI Layer (cross-block)

- **Brand-Voice Machine** — a Claude/ChatGPT **Project** loaded with the four-block substrate (positioning + personas + voice samples + named framework), per Oren × HubSpot "Teach AI Your Brand Voice." Mass-produces homepage copy, ads, emails, landing pages, scripts, collateral, and the 6 info-release surface variants in brand voice. The anti-slop way: framework-bounded, persistent, reviewed — never paste-and-pray. *This is the load-bearing tool of the whole skill.*
- **Perplexity** — the message-aggregation layer. Clusters the 4 friction channels (support questions, social comments, competitor copy, sales objections) into themes for the monthly Messages Meeting; scans for this-month trending value-props. AI reads the market; the operator decides. **Budget-gate paid research per `directives/perplexity-usage-policy.md`.**
- **Self-analytics (5-year lookback)** — the data source for cycle-counting (reaction-vs-structure threshold) and confirming the datable seasonal trough against real numbers, not feel.

## Budget Gates (this system's deterministic backstops)

- Paid research (Perplexity / Gemini Deep Research) → `directives/research-protocol.md` (Gemini PRIMARY → Perplexity fallback).
- Any paid-API call → `execution/cost_gate.py` pre-flight.
- Image/video generation for creative → route via `creative_router.py`; gate via `execution/fal_budget_guard.py`.

The tools change; the *block → named-input → named-tool → named-output* discipline doesn't.

## Funnel Flywheel Tool Categories

| Funnel job | Tool category | Required behavior |
|---|---|---|
| Capture/page | Landing-page or form builder | One job, one next action, consent-aware capture |
| Lead state | CRM or lightweight pipeline | Source, consent, lifecycle stage, owner, next action |
| Booking/show-up | Calendar and reminder system | Booked/held states, preparation, reminders, reschedule path |
| Nurture | Email/SMS platform | Immediate confirmation, next-day education, exit conditions |
| Funnel evidence | Screenshot/swipe/reference board | Source, date, full-spine capture, mechanism annotations |
| Measurement | Analytics, sales, and payment records | Stage-level events without collapsing calls into revenue |
| Learning | Experiment ledger | Hypothesis, variable, result, limit, decision, next test |

Framer, Kit, HubSpot, and similar tools are optional examples. No workflow may require a vendor merely because it appeared in the source demonstration.
