# Provenance — Semantic Document Library OS Repair

Every anchor added to `genius.md`, mapped to its exact source location. All
quotes were checked character-for-character against the cited file before
use; none were paraphrased into quotation marks.

## Source Discovery

`ls extractions/ | grep -iE "semantic|document|library"` returned nothing at
repo root. Before concluding sources were absent, ran a per-fragment search
across the repo (`grep -rli "work primitive"` / `"semantic document"`) which
surfaced the real extraction inside the historical harvest copy:
`_active/harness/codex-harvest-2026-06-11/extractions/semantic-document-library-os/`.
Confirmed with `wc -c` (not `wc -l`):

- `transcript.txt` — 26,202 bytes
- `extraction-brief.md` — 987 bytes
- `generated-docs/ai-operating-partner-deep-stack-offer-v2.md` — 17,529 bytes
- `proof-demos/codex-session-kickoff-first-proof-demo.md` — 16,252 bytes (present only in the harvest copy, not at repo-root `extractions/`)

The `_archive/claude-export-2026-07-01.tar.gz` per-member scan (the batch's
fallback instruction for when nothing is under `extractions/`) was not
needed — the harvest copy already had a full, readable, correctly-sized
transcript, so that was ground truth.

## Quote → Source Line Map

All quotes below are verbatim substrings of
`_active/harness/codex-harvest-2026-06-11/extractions/semantic-document-library-os/transcript.txt`
(single continuous paragraph, no line numbers in the source file — located by
exact-string presence, confirmed by direct read of the full 26,202-byte
file during this repair).

| Quote used in genius.md | Section |
|---|---|
| "But access only gets the agent into the work space. It doesn't make the work understandable." | Pattern 1 |
| "The future is software where the button is no longer the primitive. The primitive is the action behind it." | Pattern 2 |
| "Trust is not a switch." | Pattern 3, Anti-Pattern 1 |
| "We're talking about semantic meaning artifacts. They tell the agent what world it's operating in." | Pattern 4 |
| "can it build a durable work graph above the underlying apps?" | Pattern 5 |
| "one of those classic problem shapes is make a semantic meaning of work legible to agents today." | Pattern 6 |
| "Humans need clear interfaces. Agents need clear semantics. The best software will provide both." | Pattern 7 |
| "If you expose too little, generic agents will operate clumsily through the UI. If you expose too much, the product risks becoming back-end infrastructure for someone else's agentic interface." | Pattern 8 |
| "But the action is not really click save." | Anti-Pattern 2 |
| "guessing is not a strategy for high-consequence work." | Anti-Pattern 3 |
| "there were real production systems deleted as a result of exactly that issue" | Anti-Pattern 4 |
| "If it cannot tell the difference between issuing a refund from your chosen Shopify shop versus issuing a refund from your Stripe, you're going to have problems as well." | Anti-Pattern 5 |
| "SAP is locking off agents right now. They don't want agents to use their products." | Anti-Pattern 6 |
| "The human sees a calendar event and brings all of that context with them. The software seeds fields in a database, right?" | In His Own Words |
| "If there's a connector, use the connector. If there's a proper protocol, use the protocol. If the system exposes a typed object and a permissioned action, use that." | In His Own Words |
| "Do not ask only whether the agent can act. Ask whether the product knows what that action means. That is your key takeaway." | In His Own Words (final line of the transcript) |
| "A refund, a reschedule, a payment authorization, a compliance exception, a meeting brief." | The Work Primitive |
| "the loop is powerful because the work environment itself gives the agent semantic feedback." | Why Coding Agents Arrived First |
| "Agents should use the richest semantic interface available." | The Hierarchy Of Meaning |
| "does the system understand what kind of work is being done, who's allowed to do it, what could go wrong, and how the result is checked" | Source Thesis |

Two anti-pattern anchors are NOT Jones quotes and are labeled as such in
`references/source-ledger.md`:

- "Do not sell this as documentation, better prompts, or an automation project." — verbatim from the already-existing, already-passing `skills/semantic-document-library-os/references/productized-service-blueprint.md` (unmodified in this repair; quote confirmed by direct read).
- "The best libraries are organized by work primitives, not departments or file types." — verbatim from the already-existing, already-passing `skills/semantic-document-library-os/references/hidden-knowledge.md` (unmodified in this repair; quote confirmed by direct read).

## Metadata (video title, channel, URL, date)

Source: `_active/harness/codex-harvest-2026-06-11/extractions/semantic-document-library-os/extraction-brief.md`, confirmed also in the live `skills/semantic-document-library-os/SKILL.md` frontmatter line 10 (`source: "Nate B. Jones - The Work Primitive: What Every AI Product Leader Gets Wrong (YouTube, 2026-05) + existing Nate B. Jones Antigravity skills"`) — both agree, so this was treated as VERIFIED metadata rather than re-fetched from YouTube.
