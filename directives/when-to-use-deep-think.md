# When to Use Deep Think (Manual Workflow)

> **Gemini 3 Deep Think** is the current state-of-the-art reasoning mode (April 2026). Runs on the Gemini 3 family via the Gemini app for Google AI Ultra subscribers. Supersedes the earlier "Gemini 2.5 Deep Think."
>
> **API access**: Early access only — available via Gemini API to select researchers, engineers, and enterprises through Google's interest form. NOT yet generally available. Use manually in the browser for now.

---

## What Deep Think Is

Deep Think is a toggle in the Gemini app that switches the model into extended multi-step reasoning — the model thinks step-by-step, explores multiple hypotheses simultaneously, and solves problems iteratively before responding. Similar in spirit to Claude's extended thinking, but Google's implementation is purpose-built for complex math, science, logic, and open-ended strategic problems.

**Where to find it**: Gemini app (web or mobile) → model selector → **Gemini 3.1 Pro** (or Gemini 3 Pro) → toggle **"Deep Think"** in the prompt bar.

**Cost**: Covered by Google AI Ultra subscription. No marginal cost. Usage limits apply but are generous for Ultra subscribers.

---

## When Deep Think Is the Right Tool

Use Deep Think MANUALLY (not via API, not via any agent) for:

| Situation | Why Deep Think Wins |
|---|---|
| **Strategic decisions** — which offer to launch, which niche to enter, which client to take | Extended reasoning catches trade-offs a fast response misses |
| **Research synthesis** — you have 5+ documents, need to find patterns across them | Multi-step reasoning holds more of the corpus in working memory |
| **Adversarial self-review** — stress-testing your own thinking before committing | Deep Think is known for surfacing hidden assumptions |
| **Architecture decisions** — system design trade-offs, database schemas, workflow structures | Reasoning through second-order consequences |
| **Complex arguments** — constructing or deconstructing a multi-premise argument | Chain-of-thought quality matters more than latency |
| **Post-mortem analysis** — why did X fail, what would need to be true for Y | Holds multiple hypotheses simultaneously |

---

## When NOT to Use Deep Think

- **Quick answers**: Use regular Gemini or Claude Code chat.
- **Creative writing / content generation**: Deep Think is reasoning-focused. Claude Code (me) or regular Gemini produces better prose.
- **Code generation for small features**: Claude Code. Deep Think is overkill.
- **Research gathering**: Use Deep Research (API-integrated via `/deep-research` or manual in Gemini app). Deep Think is for thinking ABOUT research, not gathering it.
- **Recurring automated workflows**: Deep Think has no API. Don't plan around it.

---

## How to Integrate Into Your Workflow

**Weekly Strategic Review (recommended cadence):**
1. Open Gemini app, switch to Gemini 3.1 Pro + toggle Deep Think on
2. Paste the week's open questions (3-5 strategic decisions you're sitting with)
3. Read the extended reasoning output
4. Copy the high-signal conclusions back into your session state / plan docs

**Research Synthesis (after `/deep-research` runs):**
1. Export the research report to markdown
2. Paste into Deep Think with the prompt: "Based on this research, what are the 3 non-obvious conclusions I should act on?"
3. Compare Deep Think's synthesis to the research report's built-in synthesis
4. Use whichever is sharper

**Adversarial Self-Review (before high-stakes commits):**
1. Paste your plan / strategy / deliverable
2. Prompt: "What assumptions am I making that might not hold? What's the strongest counter-argument? What would need to be true for this to fail?"
3. Deep Think surfaces hidden assumptions better than single-pass models

---

## Why This Is Manual (Not Integrated)

Gemini 3 Deep Think API is in **Early Access only** as of April 2026 — available to select researchers, engineers, and enterprises via an interest form. General developer API access has not shipped. For now, Ultra subscribers use it through the Gemini app UI.

**If you want to apply for Early Access**, submit the interest form linked from Google's Gemini 3 Deep Think announcement. If granted, revisit this document — Deep Think could then slot into Step 5.5 verification (adversarial claim checking) or `/writers-room` (structural review). Until Early Access is granted or general API ships, manual use only.

---

## Related Tools

- **Deep Research** (`/deep-research-gemini`, API-integrated): For gathering research. Separate from Deep Think.
- **`/writers-room`**: For adversarial content review with 9 experts. Different mechanism (prompt engineering), same goal (catching hidden issues).
- **`/adversarial-review`**: Stress-test deliverables with scorer + challenger agents. Uses Claude/Gemini programmatically.
- **Claude Code + Opus 4.7**: My extended reasoning via thinking budget. Comparable quality for most tasks; Deep Think shines on strategic/architectural decisions.

---

## Usage Tracking (Manual)

Since this is a manual workflow, tracking is light. Consider noting in `.agent/session-state.md` when Deep Think contributed to a major decision, so you can audit whether it's pulling weight.

*Created: 2026-04-23*
