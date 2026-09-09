Done. The verdict-to-diff proposals are written to `evolution_store/proposed-diffs/2026-08-16.md`.

**Summary of what I found:**

All 5 low-composite entries (6.67) share the same root cause: **expert loaded, but no matching execution prompt exists for the deliverable type being produced.** This leaves the finalize without an anchored expert-standard rubric, so the dimension scores default to the 6-7 range.

**5 proposals drafted (all observe-not-block):**

1. **New prompt:** Daily Listening Brief for Oren Operational Systems — the automation runs daily with no contract to finalize against
2. **Chain_runner check:** Log when expert is loaded but `--type general` is used — makes the pattern visible
3. **New prompt:** Offer Verdict for Andrew Dun — the skill covers diagnostics but not the "should I pursue this offer" decision that comes before
4. **Chain_runner check:** Surface prompt-coverage miss at finalize when skill has prompts but none match the output description
5. **Sharpen existing prompt:** Alan Aragon plateau-rescue had a matching prompt but the Quality Gate wasn't specific enough to anchor an 8

All drafts only — Farrice reviews and applies.
