# Source Ledger — Boris Claude Code

Claim-by-claim provenance for content added/modified during Wave 3 Lane 4 Batch 2 repair (2026-07-17). Existing skill content (not touched this pass) is not re-audited here — see the pre-existing `references/prompts-v2/*.md` files and `extractions/boris/` for their own grounding.

## Sources Consulted

| Source | Type | Size (verified via `wc -c`) |
|---|---|---|
| `extractions/boris/transcript.txt` | Full transcript, Lenny's Podcast interview with Boris Cherny (Head of Claude Code, Anthropic) | 103,343 bytes |
| `extractions/boris/extraction-report.md` | MES 3.0 extraction summary derived from the transcript | 6,686 bytes |

No 0-byte or missing files were claimed absent without a direct read + `wc -c` check. Both files above were opened in full and are real, populated source material — the extraction is **not** thin or absent for this skill.

## Claims — VERIFIED / LIKELY / UNCONFIRMED

| Claim | Label | Anchor |
|---|---|---|
| "plan mode is actually really simple" / "we inject one sentence into the model's prompt to say please don't write any code yet. That's it." | VERIFIED | `extractions/boris/transcript.txt` (exact substring match) |
| "Don't don't try to cost cut at the beginning" / "My advice generally is don't try to optimize... Start by just giving engineers as many tokens as possible." | VERIFIED | `extractions/boris/transcript.txt` |
| "So, one is don't try to box the model in." / "Don't try to overcurate it. Don't try to put it into a box. Don't try to give it a bunch of context up front." | VERIFIED | `extractions/boris/transcript.txt` |
| "the more general model will always outperform the more specific model" / "...often these gains just get wiped out with the next model" | VERIFIED | `extractions/boris/transcript.txt` (Bitter Lesson discussion, referencing Rich Sutton) |
| "you kind of like you still do want some of these checkpoints like you still want a human looking at the code" | VERIFIED | `extractions/boris/transcript.txt` |
| "You don't want to make people use a different workflow. You don't want to make them go out of their way to learn a new thing." | VERIFIED | `extractions/boris/transcript.txt` |
| "It's abuse in that no one designed the product for this, but they're kind of figuring it out because it's just so useful for this." / "It's like people are abusing the Facebook groups product to buy and sell" | VERIFIED | `extractions/boris/transcript.txt` (Facebook Marketplace latent-demand story) |
| "you really have to understand the layer under the layer at which you work" | VERIFIED | `extractions/boris/transcript.txt` |
| "Every week everyone fills out a status and every Monday co-work just goes through and it messages every engineer on Slack that hasn't filled out their status" | VERIFIED | `extractions/boris/transcript.txt` |
| "this is just one prompt. It'll do everything." | VERIFIED | `extractions/boris/transcript.txt` (same status-tracking anecdote as above) |
| "there is this kind of like transfer where you teach the model to do you know X and it kind of gets better at Y" | VERIFIED | `extractions/boris/transcript.txt` |
| The artifact name "CLAUDE.md" as Boris's specific living-context file | LIKELY | Not a verbatim term in this transcript — the compounding-context *behavior* is directly described (see transfer quote above), but the file-naming convention is a reasonable inference from his broader public practice, not something he says on this recording. Flagged inline in genius.md Pattern 3 rather than presented as a direct quote. |
| "Boris achieves a 200% productivity increase, shipping 10-30 PRs daily" (pre-existing extraction-report framing) | VERIFIED | `extractions/boris/transcript.txt` — "Productivity per engineer has increased 200%" and "Every day I ship 10, 20, 30 p[ull] requests" both appear verbatim (near-start of transcript) |

## Absence Checks (per envelope Rule 2 — absence itself is a provenance claim)

- Searched transcript for "CLAUDE.md" — 0 hits. Confirmed by direct `grep -c` and `re.finditer` scan of the full 103,343-byte file, not assumed.
- Searched for "reusable prompt library", "slash command", "template" — 0 hits each. The `Teaching Through Prompts` pattern's grounding is drawn from the adjacent, thematically matching "one prompt. It'll do everything." line rather than an invented direct quote about prompt libraries.
- No timestamps exist in the transcript file (continuous prose, no `HH:MM` markers) — anchors cite the source file and interview name rather than a fabricated timestamp.
