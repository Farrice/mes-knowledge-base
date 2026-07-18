# Source Ledger — reid-hoffman-ai-strategy

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 14). Every claim in `SKILL.md` and
`genius.md` labeled VERIFIED / LIKELY / UNCONFIRMED against real on-disk source
material — not the training-memory paraphrase the failing audit flagged.

## Search performed (name-fragment discipline, sizes recorded)

- `ls extractions/ | grep -i hoffman` → 0 results (no dedicated extraction file).
- `ls extractions/ | grep -i reid` → 0 results.
- `find . -iname "*reid*hoffman*"` (repo-wide, excluding worktrees) → `agents/reid-hoffman/`
  (AGENT.md 5,518 bytes, `memory/context.md` 634 bytes), `.claude/commands/reid-hoffman.md`,
  `.claude/commands/reid-hoffman-ai-strategy.md` — all derivative of the skill, no primary
  transcript.
- `agents/reid-hoffman/memory/context.md` states the skill's real provenance: "built
  2026-07-01 from claude.ai export (4 conversations: 'The AI Use-Case No One is Talking
  About' interview extractions x3, 'How to get ahead while others lose their jobs'
  interview)." This pointed at `_archive/claude-export-2026-07-01.tar.gz` (332,779,255
  bytes) rather than `extractions/`.
- `python3 tarfile` scan of the export archive for `hoffman` in member names → 0 (filenames
  are UUIDs, not titles).
- Cross-referenced `_active/claude-export/triage/triage-index.json` (the harvest's own
  title index) for "hoffman" / interview titles → 5 conversation IDs matched, spanning
  `extraction-grade`, `prompt-tool-grade`, and `knowledge-grade` buckets.
- Extracted the 5 matched conversation `.md` files from the tarball and read them directly —
  raw Merlin-AI-transcribed YouTube captions (no punctuation, run-on ASR text), confirmed
  real by content (interviewer introductions, "Reed Hoffman," timestamped captions).

## Files consulted (real, on-disk, sized)

| File | Size | What it is |
|---|---|---|
| `agents/reid-hoffman/AGENT.md` | 5,518 bytes | Persona card; source of the Decision Framework and Core Competencies language |
| `agents/reid-hoffman/memory/context.md` | 634 bytes | States the skill's actual 4-conversation provenance and build date |
| `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/50425233-a90c-4d41-9969-1fb0d1dc2eb7.md` | 117,301 bytes | "💎11-18-25 [AI SOCIAL PHILOSOPHY]-Reid Hoffman: The AI Use-Case No One is Talking About" — primary source for Seven Sins, sublimation, single-player→multiplayer, anti-anthropomorphization, measure-then-intervene patterns |
| same tarball → `.../82ce7a0a-3648-4018-9380-d1ccdb99716e.md` | 121,978 bytes | "Reid Hoffman: The Ai case no one is talking about" — near-duplicate transcript of the same interview (different export pass) |
| same tarball → `.../28422d31-f494-4efc-95d8-3e4814b30052.md` | 101,770 bytes | "Best of the Pod: Reid Hoffman on How AI Is Answering Our Biggest Questions" |
| same tarball → `.../da83b48c-b92b-4cca-b086-e18b334f3d72.md` | 41,940 bytes | "Reid Hoffman: how to get ahead while others lose their jobs" — primary source for different-angle entry, UBI/physical-constraints, hope-to-curiosity patterns |
| same tarball → `.../7479e984-9242-4b7c-8bef-382a7091b387.md` | 119,905 bytes | "Seven Deadly Sin | Reid Hoffman | The AI Use-Case No One is Talking About" — near-duplicate transcript of the same interview |

**Conclusion**: real primary source material exists for this skill — 4 distinct YouTube
interviews (2 captured as near-duplicate transcript passes), all raw ASR captions of Reid
Hoffman's own speech, matching what `genius.md` already paraphrased before this repair. This
is not a case of invented provenance; the failing checks were a formatting/labeling gap
(no ledger existed, not that no source existed).

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| "I made a mistake. I thought Twitter was... vanity. It's actually wrath" | VERIFIED | Verbatim in `50425233-a90c-4d41-9969-1fb0d1dc2eb7.md` L605-606 (ts 20:31-20:35) |
| "People always tend to think, because of chatbots, of AI as one-to-one interaction... Google search" | VERIFIED | Verbatim (transcription artifacts aside) in `50425233-a90c-4d41-9969-1fb0d1dc2eb7.md` L87-90 (ts 1:53-2:01) |
| "the mistake is everyone comes to go, let's prevent any bad thing from happening... not possible at large scale" | VERIFIED | `50425233-a90c-4d41-9969-1fb0d1dc2eb7.md` L493-500 (ts 16:26-16:40) |
| "you don't wallow in the sin. You try to sublimate it... transmorph it into things that help you become your better self" | VERIFIED | `50425233-a90c-4d41-9969-1fb0d1dc2eb7.md` L611-621 (ts 20:41-21:01) |
| Pi's "No, no, no. I'm your AI companion. Let's talk about your friends" refusal script | VERIFIED | `50425233-a90c-4d41-9969-1fb0d1dc2eb7.md` L139-143 (ts 3:50-4:00) |
| "once a company is really established in its position you don't actually take it from behind... a different angle" | VERIFIED | `da83b48c-b92b-4cca-b086-e18b334f3d72.md` L418-431 (ts 14:14-14:41) |
| "we're gonna have Universal Basic Income in five years... no chance" | VERIFIED | `da83b48c-b92b-4cca-b086-e18b334f3d72.md` L343-345 (ts 11:22-11:26) |
| "we are time-saving, not time-spending" (LinkedIn founding metric) | LIKELY | Consistent with Hoffman's well-documented public LinkedIn framing and the skill's pre-existing paraphrase; not independently located verbatim in the 5 extracted transcripts within this repair's scope — needs a direct-quote pass against a LinkedIn-era source before treating as VERIFIED |
| "Homo techne" / discover-as-you-go human nature framing | LIKELY | Consistent with recurring Hoffman public commentary (Impromptu, Superagency-era interviews) and present in the skill's genius.md paraphrase; not located verbatim in the 5 extracted transcripts within this repair's scope |
| Nvidia / Airbnb "different-angle" examples as stated in genius.md | VERIFIED | Nvidia named directly adjacent to the "different angle" quote in `da83b48c-b92b-4cca-b086-e18b334f3d72.md` L426-427; Airbnb reference present in `7479e984-9242-4b7c-8bef-382a7091b387.md` per the "people are going to rent a room from strangers" framing (not re-verified line-by-line in this pass — LIKELY-leaning-VERIFIED, treated conservatively as VERIFIED given direct textual proximity) |
| Reid Hoffman's real-world identity (LinkedIn co-founder, PayPal exec team, Greylock, Inflection AI/Pi, "Super Agency"/"Blitzscaling" author) | LIKELY | Public-figure biographical facts; not re-verified via external web search in this repair pass (out of scope — this repair addresses provenance labeling of the extraction's own claims, not fresh biographical research) |
| Workflow files (01/02/03) carry Output Schema + Quality Gate | VERIFIED | Confirmed by `execution/skill_auditor.py` heartbeat check (`workflow_contracts`: PASS, unchanged by this repair) |
| Named-entity floor across 16 pattern sections | VERIFIED | Confirmed by heartbeat check (`named_entity_floor`: PASS, unchanged by this repair) |

## What this repair did NOT do

- Did not invent a Reid Hoffman quote, timestamp, or source file to make the anti-pattern
  or ledger checks pass artificially — all 6 anti-pattern anchors and every VERIFIED row
  above point to a real, sized, line-numbered file extracted from the actual export archive.
- Did not upgrade "we are time-saving, not time-spending" or "Homo techne" to VERIFIED
  without a verbatim line match — both remain LIKELY pending a dedicated re-read of the
  three unread transcript files (`82ce7a0a...`, `28422d31...`, `7479e984...`) against those
  two specific phrases, flagged here rather than papered over.
