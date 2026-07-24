---
description: Create custom Cal.com booking links with constrained availability + a matching outreach draft — Riley Brown pattern; needs Farrice's Cal.com API key to go live
---

# /scheduling-links — Custom Booking Link + Outreach Draft

Riley Brown's pattern #8: per-guest booking links with *deliberately shaped* availability ("only September–October", "Tue/Thu noon–5"), paired with the outreach email that carries the link. His setup insight applies verbatim: **"go to cal.com, get an API key, paste it in and say create a skill that fully controls cal.com and it'll work one minute later"** — the self-authoring integration pattern.

> **ACTIVATION REQUIRED (one-time, free, ~3 min of Farrice's hands)**
> Cal.com account (free tier) → Settings → Developer → API keys → add `CALCOM_API_KEY=` to root `.env`.
> First run after that, the agent reads https://cal.com/docs/api-reference (v2 API: event-types, availability, bookings) and exercises create→verify→delete on a throwaway event type — the Riley bootstrap, done once, honestly verified.

## Usage

```
/scheduling-links [who/purpose] [--window "Sep-Oct" | --days "Tue,Thu" | --hours "12-17"] [--with-email]
```

## Steps

1. **Shape the availability**: translate intent into event-type config (date range, weekday/hour constraints, duration, buffer). Strategic shaping is the point — near-term for hot topics, far-out for evergreen guests (Riley's podcast-booking logic).
2. **Create the event type** via Cal.com API v2 (`POST /v2/event-types` + availability schedule). Verify by GET before handing over — a booking link that 404s in a guest's inbox is the failure mode.
3. **Open the link headless** (Playwright, read-only) and confirm the visible availability matches the intent (Riley's own on-screen check: "No availability in August… Nothing in November. See, it created a custom link").
4. **`--with-email`**: draft the outreach carrying the link via `/inbox-drafts` step 3-4 (voice card applies; draft only, never send).
5. If `CALCOM_API_KEY` missing → deliver the shaped availability spec + activation note. Never fake a link.

## Quality Gate

- Link verified live with correct availability before delivery
- Availability shaping stated back in plain language ("Shaq can only pick Tue/Thu, Sep–Oct")
- Outreach email passes voice + slop gates
