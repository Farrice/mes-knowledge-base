---
description: Multi-model deliberation — run the same prompt through Claude + Gemini in parallel, surface explicit contradictions. Distinct from /council (single-model multi-persona). Built for high-stakes decisions where blended output hides disagreement.
---

# `/deliberate` — Multi-Model Deliberation Runbook

The executable runbook for the deliberate skill. Read `skills/deliberate/SKILL.md` for the full philosophy. This workflow is the step-by-step runner. (Mirrors `.agent/workflows/deliberate.md`, the invocation-level copy the router reads; this copy lives inside the skill folder so the skill's own heartbeat audit can verify the deliverable contract below.)

## Quick Start

```
/deliberate "Should we price the Authority Flywheel at $5K, $7.5K, or $10K?"
/deliberate "Is Andrea's positioning 'sober dance party' or 'curated daytime experience'?"
/deliberate "Should I hire the contractor or bring it in-house?"
```

With project anchoring:
```
/deliberate "..." --project farrice-brand
```

## Args

| Flag | Required | Purpose |
|---|---|---|
| `<prompt>` (positional) | yes | The question or decision to deliberate |
| `--project <slug>` | optional | Project slug; fold result into anchor memory |
| `--grounding` | optional | Enable Google Search grounding on Gemini side (use only for factual-surface prompts) |
| `--model <tier>` | optional | Gemini tier: `pro` (default), `flash` (cheaper), or full model ID |
| `--system <text>` | optional | System instruction passed to Gemini (e.g., "You are a senior strategist.") |

---

## Step 1 — Capture the Prompt

If the slash command included a clear prompt, use it. If invocation was bare (`/deliberate` with nothing), ask ONCE:

> "What's the prompt or decision you want deliberated?"

Then echo the captured prompt back to user in ONE line:

```
Deliberation engaged. Prompt: "<verbatim>". Running Claude + Gemini in parallel.
```

---

## Step 2 — Claude Take (inline)

Produce YOUR answer directly in this conversation. Required structure (per `skills/deliberate/SKILL.md`):

```markdown
### Claude take

**Position:** [recommendation]
**Top 2-3 reasons:** [load-bearing arguments]
**Where I'm uncertain:** [explicit confidence calibration — not boilerplate]
**Strongest argument against my position:** [genuine disconfirmation]
```

**Discipline:** the "strongest argument against" is non-optional. If you can't articulate one, the deliberation is degraded — you're entering Step 3 with false confidence. Take 30 seconds to find a real counter before producing the take. Write this take BEFORE running Step 3 — never retrofit it to agree with Gemini once you've seen the response.

---

## Step 3 — Gemini Take

Build the command:

```bash
python3 execution/deliberate.py \
    --prompt "<user prompt verbatim>" \
    --model pro \
    --json
```

Add `--system "<text>"` if there's natural expert framing (e.g., for a pricing question: `--system "You are a senior pricing strategist. Surface tensions, not consensus."`). Skip if you don't have a strong system frame — default behavior works.

Add `--grounding` ONLY if the prompt has factual surface (market sizes, competitor pricing, statistics). Skip for judgment-call prompts — grounding noises up taste calls.

Parse the JSON. Expected shape:
```json
{
  "model": "gemini-2.5-pro",
  "response": "<Gemini's full answer>",
  "input_tokens": int,
  "output_tokens": int,
  "estimated_cost_usd": float,
  "duration_seconds": float
}
```

Render Gemini's response under this header:

```markdown
### Gemini take  (<model_id>, ~$<cost>)

[Gemini's response verbatim]
```

**Failure handling:** if the JSON has an `"error"` key (script returned exit 1), surface to user:

> "Gemini voice failed: `<error>`. Want me to retry, fall back to Claude-only synthesis, or abort?"

Wait for direction. Do NOT silently single-model-synthesize — that defeats the skill's purpose.

---

## Step 4 — Synthesis (the actual deliverable)

Produce the deliberation block in this EXACT structure (the consistency matters — Farrice scans for these headers):

```markdown
## Deliberation: [one-line subject extracted from prompt]

### Where they agree
- [convergence point 1]
- [convergence point 2]
- [...]

### Where they disagree (the real signal)
**Claude says:** [Claude's position, restated cleanly]
**Gemini says:** [Gemini's position, restated cleanly]
**The actual disagreement is about:** [the underlying assumption — what would have to be true for one to be right]

### Confidence asymmetry
- Claude expressed [more/less/comparable] confidence than Gemini on: [specific claim]
- This matters because: [why the asymmetry is decision-relevant]

### Recommendation
**Winner:** [Claude / Gemini / synthesize / neither — pick a side OR explain the synthesis condition]
**Confidence:** [High / Medium / Low]
**Reasoning:** [why this resolution holds]
**If Farrice disagrees with the winner, the next-best path is:** [explicit alternative]
```

**Hard rules** (these are the skill's purpose — do not soften them):

1. **If there are ZERO contradictions** between Claude and Gemini, FLAG this explicitly:
   > "Both models converged — deliberation may have been wasted on a consensus question. The prompt likely doesn't have genuinely contested answers. Consider whether the question was the right shape."
2. **Never blend a contradiction into "both are right" mush.** Either name a winner (the strong default) or explicitly explain the synthesis condition ("Claude is right IF X; Gemini is right IF Y; the user must decide which world they're in"). Smoothing disagreement into invisibility is the failure mode.
3. **If one model is verifiably wrong on a fact** (not opinion — fact), surface this as a separate block BEFORE the recommendation:
   ```markdown
   ### Factual divergence
   [Model] claimed [X]. This is verifiable as [true/false] because [source]. Adjusting deliberation accordingly.
   ```

---

## Step 5 — Optional Anchor Fold-in

If `--project <slug>` was passed:

1. Save the synthesis block (the entire `## Deliberation: ...` markdown from Step 4) to:
   ```
   projects/<slug>/deliberations/<topic-kebab>-<YYYYMMDD>.md
   ```
   Create the `deliberations/` subdir if needed.

2. Register as anchor:
   ```bash
   python3 execution/anchor_memory.py anchor <slug> \
       --type deliberation \
       --path "projects/<slug>/deliberations/<topic-kebab>-<YYYYMMDD>.md" \
       --desc "Deliberation: <one-line subject>. Winner: <picked model or 'synthesize'>." \
       --phase "deliberate"
   ```

3. State to user:
   > "Deliberation logged as anchor in `projects/<slug>/state.yaml`. Future supercomputer missions in this project will surface it as context."

If `--project` was NOT passed, the deliberation just lives in this chat. Skip Step 5 cleanly — don't ask the user if they want to save.

---

## Step 6 (implicit) — Finalize

For non-trivial deliberations, fire the chain finalize:

```bash
python3 execution/chain_runner.py finalize "Deliberation: <subject>. Winner: <model/synthesize>." \
    --expert "claude+gemini" \
    --skill deliberate \
    --workflow deliberate \
    --type "Analysis" \
    --intent <1-10 self-score> \
    --expert-score <1-10 self-score> \
    --adversarial <1-10 self-score> \
    --notes "Deliberation cost: ~$<gemini_cost>. Contradictions surfaced: <count>. Convergence: <full|partial|none>."
```

Skip finalize for low-stakes / exploratory deliberations the user invoked casually.

---

## Output Contract

This workflow produces exactly one deliverable: the **Deliberation Block** rendered in Step 4, preceded by the raw Claude take (Step 2) and Gemini take (Step 3) so the reader can audit the synthesis against the two unblended source positions. Section order is fixed and non-negotiable: `### Claude take` → `### Gemini take` → `## Deliberation: [subject]` → `### Where they agree` → `### Where they disagree` → (optional `### Factual divergence`) → `### Confidence asymmetry` → `### Recommendation`.

Requirements specific to this deliverable (not a generic checklist — each maps to a named failure mode above):
- **Claude take** must include all four fields (Position / Top 2-3 reasons / Where I'm uncertain / Strongest argument against), written BEFORE Gemini's response is seen.
- **Gemini take** must be the `response` field from `execution/deliberate.py`'s JSON output, rendered verbatim — no summarizing, no trimming, no "cleaning up" its phrasing.
- **"The actual disagreement is about"** must name an underlying assumption (e.g., "positioning premium vs. accessibility"), never a restatement of the two surface positions already given above it.
- **Recommendation** must name an actual winner (Claude / Gemini / synthesize-with-named-condition) — "it depends" alone, with no named condition, is not a valid Recommendation.
- If `--project` was passed, the saved file at `projects/<slug>/deliberations/<topic-kebab>-<YYYYMMDD>.md` must contain the full Deliberation Block, not a summary of it.

## Quality Gate

- [ ] Was the Claude take (Step 2) written and locked before Gemini's response was read?
- [ ] Is Gemini's take rendered verbatim (matches the `response` field from `execution/deliberate.py`'s JSON output, unedited)?
- [ ] If zero contradictions existed, was that flagged explicitly per the Step 4 hard rule rather than a manufactured disagreement inserted to fill the section?
- [ ] Does "the actual disagreement is about" name an underlying assumption rather than restate the two surface positions?
- [ ] Does the Recommendation name an actual winner or an actual synthesis condition — never unresolved "both are right" mush?
- [ ] If the Gemini call failed (JSON `"error"` key present), was the failure surfaced to the user rather than silently falling back to Claude-only synthesis?
- [ ] If `--project` was passed, was the anchor registered via `execution/anchor_memory.py anchor` (not just saved to disk and left unlinked)?

---

## Anti-Patterns (workflow FAIL)

1. Skipping Step 2's "strongest argument against" — false confidence enters Step 3.
2. Adding `--grounding` to judgment-call prompts — pollutes the deliberation with web context.
3. Picking Claude every time — confirmation bias dressed as deliberation. Audit if it happens 3+ times in a row.
4. "Both make great points" in Step 4 — that's not synthesis, that's avoidance. Name a winner or name the synthesis condition.
5. Silently falling back to Claude-only when Gemini fails — defeats the entire point. Always surface the failure to user.
6. Using `/deliberate` for low-stakes / single-decision-already-made work — overhead exceeds value.

## See Also

- `skills/deliberate/SKILL.md` — when-to-use + composition table
- `skills/deliberate/genius.md` — design philosophy + competitive positioning vs Perplexity
- `skills/deliberate/references/prompts-v2/deliberation-synthesis.md` — the structure-pure v2 Output Contract this workflow's contract mirrors
- `execution/deliberate.py` — Gemini voice executor
- `.agent/workflows/council.md` — the OTHER (single-model multi-persona) council pattern
