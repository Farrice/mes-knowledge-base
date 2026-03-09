---
description: Rate the last expert output — quick feedback on routing quality.
---

# /rate — Quick Output Rating

Rate the last expert-driven output so the system can track routing effectiveness.

## Usage

```
/rate                    — Interactive (asks for rating)
/rate positive           — Quick thumbs up
/rate negative           — Quick thumbs down (will ask for correction)
/rate mixed              — It was okay, not great
```

## Steps

### 1. Get Last Routing ID

```bash
python execution/routing_intelligence.py last-id
```

If no routing has been logged in this session, tell the user:

> "No routing decision found for this session. Feedback works best when paired with a routed expert task. Try again after I've deployed an expert for you."

### 2. Collect Rating

If the user provided a rating in the command (e.g., `/rate positive`), use it directly.

Otherwise, ask:

> **How was that output?**
> - **Positive** — Nailed it, right expert, good result
> - **Negative** — Wrong expert, off-target, or poor quality
> - **Mixed** — Some good, some not

### 3. Collect Correction (Negative/Mixed Only)

If rating is negative or mixed, ask:

> "Quick correction — who should I have used instead? (Or just say 'skip')"
>
> Optional: "Any notes on what went wrong?"

### 4. Log Feedback

```bash
python execution/routing_intelligence.py feedback \
    --routing-id "[from step 1]" \
    --rating [positive|negative|mixed] \
    --session "[current_session]" \
    --correction "[if provided]" \
    --notes "[if provided]"
```

### 5. Confirm

> "Logged as [rating]. This helps me route better over time."

Keep it lightweight. The whole interaction should take under 10 seconds for a positive rating.

## When to Use

- After any expert-driven output
- When the routing felt wrong
- As a habit after substantial deliverables
- When you want to build up the routing scoreboard (`/routing-intelligence`)
