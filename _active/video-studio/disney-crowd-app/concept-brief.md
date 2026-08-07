# Concept Brief: The Locals' Go/No-Go App for Disneyland

**One-liner:** A weather app for Disneyland. Open it, get a verdict — "Today's a 2. Go." — and a 10-day crowd forecast built for people who live 20 minutes away, not 2,000 miles.

**Status:** Concept validation. Demo: `../90-exports/demo.html`. Risks: `../RISKS.md`.

---

## The Wedge

Crowd *forecasting* is a solved category. The locals' *decision* problem is not.

Every incumbent answers the vacationer's question: "When should I plan my trip?" Nobody answers the local's question: "Is it worth going **today**?" Locals don't plan trips — they make go/no-go calls, often same-morning. That's a different product: glanceable, push-driven, verdict-first, blockout-aware.

The structural moat: **Disney's own app can never build this.** Telling guests "stay home today" is against its commercial interest. The most useful feature for locals is the one the incumbent is structurally forbidden from shipping.

## Competitive Map (verified 2026-06-11)

| Player | What they do | Price | Why locals are unserved |
|---|---|---|---|
| [Touring Plans](https://touringplans.com/disneyland-resort/crowd-calendar) (Lines app) | 1–10 crowd calendar, claims 140K+ subscribers | $14.95/yr — VERIFIED | Trip-planner-first; built for vacations planned months out |
| [Thrill Data](https://www.thrill-data.com/trip-planning/crowd-calendar/disneyland) | Free predictive wait-time calendars (claims ±3.2 min accuracy) | Free — VERIFIED | Data-dense web tables; no mobile polish, no push, no verdict |
| [MouseWait](https://mousewait.com/) | Wait times + locals community + dining alerts; paid PLAT tier | Freemium — VERIFIED; "3M users" claim LIKELY (self-reported) | Dated UX; in-park utility, not a forecast/decision tool |
| [Mickey Visit](https://mickeyvisit.com/disneyland-crowd-calendar/) / [Is It Packed](https://www.isitpacked.com/disneyland-crowd-forecast-predictor-calendar/) | Editorial crowd calendars | Free (content/affiliate) | Blog-grade; not a product |
| Disney official app | Live waits, reservations | Free | Will never tell you not to come |

## Product Outline — 3 Surfaces

1. **Today (the verdict).** One number, one verb, one reason. "7 — Skip it. Grad Nite + SoCal ticket surge." Gate-to-gate stats (rope-drop quality, peak window, evening fade), weather. Five seconds to a decision.
2. **10-Day Forecast.** Weather-app row list. Crowd score per day, event badges (runDisney weekend, school breaks, ticket promos), best-day highlight. The "find my next window" surface.
3. **Key Layer + Alerts.** Pass-holder mode: overlay YOUR blockout calendar on the forecast, surface the rare intersections. Push alerts only when it matters: "Tuesday: forecast 2 + your pass is valid — rarest combo in 6 weeks." Plus **Ghost Day alerts** — live signal that today is running unexpectedly empty (locals' favorite magic: the spontaneous empty-park day).

## Monetization Ladder

- **Free:** Today verdict + 3-day forecast. (Acquisition + the shareable layer.)
- **Local — $39/yr** (test $29–49): 10-day forecast, pass-blockout layer, push alerts, Ghost Day alerts, historical accuracy receipts.
- Precedent: Touring Plans proves $15/yr at 140K+ subs; MouseWait PLAT proves locals pay premium tiers; Disney-adult willingness-to-pay is famously elastic. 25K subscribers × $39 = ~$1M ARR ceiling for a single-resort app — niche but real; expandable to WDW/Universal with the same engine.

## Viral Mechanics

- **Verdict cards** — the Wordle move. One-tap share of today's verdict as a designed card ("Checked. Today's a 9. Stay home. 🚫🏰"). Locals already post this organically in Facebook groups and Discords with screenshots of wait-time apps; give them a designed artifact instead.
- **Accuracy receipts** — "We called Saturday a 9. Actual: 9.2." Trust compounds; receipts are shareable proof.
- **Ghost Day FOMO** — every shared "park is EMPTY right now" alert is an ad for the alert system.

## Naming (none cleared — see RISKS.md)

- **Lowkey** — double meaning: low-key days + key-holder culture. Disney-free, ownable vibe. Generic-word collision risk; needs clearance.
- **Gatekeep** — slang energy ("we're gatekeeping the empty days"); built-in share line. Tone risk: irony may not read for older pass-holders.
- **Parkcast** — most descriptive (forecast mental model) but COLLIDES with a [UK theme-park podcast](https://open.spotify.com/show/19AHeuxgXDcC9l6g8loU9Q) of the same name in the same industry. Backup only.

## Honest Assessment

Worth building **only as the locals' decision app, not another crowd calendar.** The forecast data itself is commodity (Thrill Data gives it away). The defensible asset is the verdict UX + alert intelligence + pass-layer + share loop. If the demo's "open → verdict → decision in 5 seconds" feel doesn't hold, the idea collapses back into the existing category. Biggest non-product risk: data sourcing and Disney IP posture (RISKS.md).
