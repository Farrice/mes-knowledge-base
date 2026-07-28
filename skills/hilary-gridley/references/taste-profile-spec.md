# The Taste Profile — Canonical Spec (v1)

The single context asset that instantly raises the floor of all AI work for a brand/operator. Concept: Bodnar/Flanagan (*Loop*) — see `loop-frameworks.md`. Depth architecture: Gridley (calibrated context, what-good-looks-like). Assembly + structuring: this system (excavation → spec → machine-native profile).

**Position in the stack**: the Taste Profile is the CONTENT layer. It feeds `context-profile-architect` (machine-native JSON structuring) and draws on `avatar-machine` / `icp-deep-canvasser` (audience grounding). It is NOT another ICP — it is everything the ICP leaves out, plus the brand's narrative canon, plus the quality bar. Three layers:

## Layer 1 — Emotional Customer Understanding (the anti-ICP)

Everything demographic profiles omit. "The instructions AI actually needs."

| Field | What it captures | Test of depth |
|---|---|---|
| **Beliefs** | What this customer holds true about the problem, the category, themselves | Would the customer say "finally, someone gets it" reading it back? |
| **Feelings** | The emotional states they cycle through around the problem (shame, hope, skepticism, pride) | Named as *states with triggers*, not adjectives |
| **Thresholds** ("what pushes them too far") | Lines that break trust: claims too big, tone too hype, familiarity too fast, price frames that insult | Each threshold has a concrete violating example |
| **Identity stakes** | Who buying/not-buying makes them; who they refuse to become | Links to resistance, not just desire |
| **Language map** | Words they use vs words that mark an outsider | Verbatim sourced (reviews, comments, interviews) — never invented |

## Layer 2 — Brand Narrative Canon (the stories you're telling)

| Field | What it captures |
|---|---|
| **Core product narrative** | The one mechanism-story of what this product changes and how |
| **Emotional brand story** | "The thing you want people to feel" — the single feeling, named |
| **Origin/why** | The founder-true story that earns the narrative |
| **Enemy & stakes** | What the brand is against; what's lost if the customer does nothing |
| **Proof spine** | The receipts that make the narrative credible, ranked |

## Layer 3 — The Quality Bar (Gridley layer — what turns a context doc into a taste profile)

Without this layer it's a brand doc. With it, every human AND agent can self-grade.

| Field | What it captures |
|---|---|
| **What good looks like, per artifact class** | Plain-English pass/fail criteria per deliverable type (post, email, ad, page) — mined from edit pairs where they exist (`hg-judgment-encode`), articulated fresh where they don't |
| **Hall of fame** | 3-5 real artifacts that hit the bar, with why |
| **Anti-patterns** | The specific slop this brand produces under pressure (its personal ban-bank) |
| **Voice thresholds** | Dial positions: how bold / how warm / how technical before it stops sounding like us |

## Assembly Rules

1. **Ground before writing** — Layer 1 from real customer language (reviews, calls, comments), Layer 2 from founder interview + existing canon, Layer 3 from edit pairs/verdict history. Zero invented fields; thin evidence → field marked `UNGROUNDED — needs [source]` rather than filled with plausible slop.
2. **Calibrated, not maximal** (Gridley): the profile is what a smart person/agent *needs*, not everything known. Every field must change a downstream decision; if removing it changes nothing, cut it.
3. **Codify-before-AI test**: the profile must make a zero-AI team better. If a section only helps prompting, it's hackery — rewrite or cut.
4. **One canonical copy** — versioned, one owner, everything cites it. Conflicting context is slop root #2.
5. **Living document** — re-mine Layer 3 as new edits/verdicts accumulate (`hg-verdict-to-evaluator`); revisit Layer 1 thresholds after every campaign that tripped one.

## Deployment Pattern

Load the Taste Profile at the top of any content/copy/brand/strategy task (human or agent) → produce → self-grade against Layer 3 → iterate before human review. Expected effect (Bodnar): quality ↑, consistency ↑, judgment focus ↑ for both AI and people — the slop cycle breaks because the bar precedes the work.

## Productized Offer Shape

See workflow `hg-taste-profile-offer` — the engagement that builds this asset for a client, with the evaluator-tool fleet as the delivery vehicle and the profile as the moat deliverable.
