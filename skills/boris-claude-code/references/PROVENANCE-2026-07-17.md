# Provenance — Boris Claude Code repair (Wave 3 Lane 4 Batch 2)

Anchor → source file+location table for every quote/claim added this pass. All quotes verified as exact substrings of the source file via direct read + `re.finditer`/`in` checks before use — none copied from memory.

| Anchor (where it appears in modified `genius.md`) | Quote | Source | Verified |
|---|---|---|---|
| How to Use This Skill § bullet 2 | "plan mode is actually really simple" | `extractions/boris/transcript.txt` | exact substring match |
| How to Use This Skill § bullet 2 | "we inject one sentence into the model's prompt to say please don't write any code yet. That's it." | `extractions/boris/transcript.txt` | exact substring match |
| How to Use This Skill § bullet 3 | "Don't don't try to cost cut at the beginning" | `extractions/boris/transcript.txt` | exact substring match |
| How to Use This Skill § bullet 4 | "10, 20, 30" (PRs/day) | `extractions/boris/transcript.txt` — opening lines: "Every day I ship 10, 20, 30 p[ull] requests" | exact substring match |
| Pattern 3 source note | "there is this kind of like transfer where you teach the model to do you know X and it kind of gets better at Y" | `extractions/boris/transcript.txt` | exact substring match |
| Pattern 8 grounding | "Every week everyone fills out a status and every Monday co-work just goes through and it messages every engineer on Slack that hasn't filled out their status" | `extractions/boris/transcript.txt` | exact substring match |
| Pattern 10 grounding | "this is just one prompt. It'll do everything." | `extractions/boris/transcript.txt` | exact substring match |
| Pattern 12 grounding | "you kind of like you still do want some of these checkpoints like you still want a human looking at the code" | `extractions/boris/transcript.txt` | exact substring match |
| Pattern 13 grounding | "you really have to understand the layer under the layer at which you work" | `extractions/boris/transcript.txt` | exact substring match |
| Pattern 14 grounding | "It's like people are abusing the Facebook groups product to buy and sell" / "It's abuse in that no one designed the product for this, but they're kind of figuring it out because it's just so useful for this" | `extractions/boris/transcript.txt` | exact substring match |
| Pattern 16 grounding | "the more general model will always outperform the more specific model" / "often these gains just get wiped out with the next model" | `extractions/boris/transcript.txt` | exact substring match |
| Evolution Log intro | "1 entry logged to date (2026-04-09)" | Verified by reading the pre-existing Evolution Log entry itself (dated 2026-04-09, one entry total) — a file-fact, not a source quote | direct file inspection |
| Anti-Patterns item 1 | "So, one is don't try to box the model in." / "Don't try to overcurate it. Don't try to put it into a box. Don't try to give it a bunch of context up front." | `extractions/boris/transcript.txt` | exact substring match, presented as two separate quotes (not adjacent in source — no false contiguity implied) |
| Anti-Patterns item 2 | "My advice generally is don't try to optimize. Don't don't try to cost cut at the beginning. Start by just giving engineers as many tokens as possible." | `extractions/boris/transcript.txt` | exact substring match |
| Anti-Patterns item 3 | "the more general model will always outperform the more specific model" / "often these gains just get wiped out with the next model" | `extractions/boris/transcript.txt` | exact substring match |
| Anti-Patterns item 4 | "you kind of like you still do want some of these checkpoints like you still want a human looking at the code" | `extractions/boris/transcript.txt` | exact substring match |
| Anti-Patterns item 5 | "You don't want to make people use a different workflow. You don't want to make them go out of their way to learn a new thing." | `extractions/boris/transcript.txt` | exact substring match |
| Anti-Patterns item 6 | "It's abuse in that no one designed the product for this, but they're kind of figuring it out because it's just so useful for this." | `extractions/boris/transcript.txt` | exact substring match |

Full claim-by-claim VERIFIED/LIKELY/UNCONFIRMED breakdown: `references/source-ledger.md` in this output directory.
