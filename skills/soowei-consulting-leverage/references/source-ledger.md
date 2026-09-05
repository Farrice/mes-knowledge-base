# Source Ledger — soowei-consulting-leverage

Ground truth located per envelope discipline: `extractions/` has **no** file matching
`soowei`/`soo wei`/`soo-wei` (confirmed via `ls extractions/ | grep -i` — zero hits, all
extractions/ subfolders checked). Fallback per envelope Rule 2 (an absence claim is
itself a provenance claim): a per-member `tarfile` content scan of
`_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed via `wc -c`,
7,728 members) for `soowei|soo\s*wei|soo-wei` (case-insensitive) returned **6 hits**, all
`claude-export/normalized/conversations/<uuid>.md`. Three are duplicate re-runs of the
same underlying transcript at different capture dates; one (`a78311e1...`) is a *meta*-
conversation about the extraction system itself, not primary source material, and was
excluded from quote-sourcing.

## Primary sources consulted (extracted from archive, read in full)

| # | Archive member (within `_archive/claude-export-2026-07-01.tar.gz`) | Title | Size (bytes, `wc -c`) | Captured | Used for |
|---|---|---|---|---|---|
| 1 | `claude-export/normalized/conversations/09e3e3a2-87b5-4c81-9416-807bd8dcad2c.md` | "SooWei \| exactly how i built a $2m/yr profit consulting business" | 70,264 | 2026-01-17 | Primary anti-pattern quotes (7 anchors below), corroborates Patterns 1-15 |
| 2 | `claude-export/normalized/conversations/1bd10a63-52be-42f4-8cad-da5f6118a41e.md` | "11-10-25 SooWei Goh: my exact $1.5M content strategy to sign $10k+ clients" | 61,583 | 2026-01-xx (session), content dated 2025-11-10 | Corroborates $1.5M content-strategy claim in SKILL.md |
| 3 | `claude-export/normalized/conversations/2083854b-6809-4431-930b-97316832951b.md` | "11-27-25 SooWei Goh: my exact $1.5M content strategy to sign $10k+ clients" | 70,264 (dup. capture) | content dated 2025-11-27 | Duplicate re-capture of #2's transcript, not independently used |
| 4 | `claude-export/normalized/conversations/c56b2204-7820-4aa0-89f1-ab0b1f6c466f.md` | "11-26-25 SooWei Goh: how to build a qualified audience of buyers" | 82,359 | content dated 2025-11-26 | Corroborates the $224K/month figure ("$224,000 a month" at transcript timestamp 13:31) |
| 5 | `claude-export/normalized/conversations/ee4e2fcb-91b4-4e09-874a-13815c74fb43.md` | "11-25-25 [Qualified Audiences of Buyers]-SooWei Goh: how to build a qualified audience of buyers" | 67,837 | content dated 2025-11-25 | Duplicate re-capture of #4's transcript, not independently used |
| — | `extractions/` (repo) | — | 0 hits | — | Confirmed absent for this expert; not a false-negative (per-member scan run, see above) |

Excluded: `a78311e1-f3bd-4a11-adbe-bfd1cd0dd9cc.md` — meta-conversation about restructuring
the extraction system itself (mentions SooWei by name as a prioritized skill, not source
transcript material). Not used for quotes.

## Claim-by-claim labels

| Claim | Where it appears | Label | Basis |
|---|---|---|---|
| "you're building yourself a hamster wheel that you can't get off" | genius.md Anti-Patterns | **VERIFIED** | Verbatim contiguous substring, source #1 |
| "That's exactly why you guys are not making the money you want to make." | genius.md Anti-Patterns | **VERIFIED** | Verbatim contiguous substring, source #1 |
| "you are posting your content in the epher and hoping it sticks" | genius.md Anti-Patterns | **VERIFIED** | Verbatim contiguous substring, source #1 (transcription artifact "epher" for "ether" preserved as-is) |
| "people could literally take my reel, put in the transcript, read the script word for word and have the same brand as me" | genius.md Anti-Patterns | **VERIFIED** | Verbatim contiguous substring, source #1 |
| "It's that awkward period. Get rid of it." | genius.md Anti-Patterns | **VERIFIED** | Verbatim contiguous substring, source #1 |
| "your appointment center doesn't even talk to the content person. Why? Like, why?" | genius.md Anti-Patterns | **VERIFIED** | Verbatim contiguous substring, source #1 |
| "I don't make any claims. I'm like, these are the results I get. You decide the claim that you want for yourself." | genius.md Anti-Patterns | **VERIFIED** | Verbatim contiguous substring, source #1 (source has stutter "I I don't"; trimmed the duplicate leading word only, rest verbatim) |
| Pattern 1 (Leverage Hierarchy: 1:1/1:10/1:1000) | genius.md Pattern 1 | **VERIFIED** | Source #1: "a guy digging sand with his hands versus... a shovel and a guy digging sand with a bulldozer" |
| Pattern 2 (Dopamine Detachment) | genius.md Pattern 2 | **VERIFIED** | Source #1: "Your dopamine is tied to how much and how many tasks you do, which doesn't get you anywhere" |
| Pattern 3 (Sunday Reset) | genius.md Pattern 3 | **VERIFIED** | Source #1: "Sunday should be your reset day... Please take Sundays off" |
| Pattern 4 (Calendar Stacking) | genius.md Pattern 4 | **VERIFIED** | Source #1: "1 p.m. to 7:00 p.m. I'm stacking my calls back to back to back" |
| Pattern 5 (Content-as-Oxygen) | genius.md Pattern 5 | **VERIFIED** | Source #1: "I have eight videos in the backlog" / "block off my first two to three hours for content" |
| Pattern 6 (One-to-Infinity) | genius.md Pattern 6 | **VERIFIED** | Source #1: "content/brand building" vs. delegate everything else, discussed at length |
| Pattern 7 (Top-of-Funnel Forcing Function) | genius.md Pattern 7 | **VERIFIED** | Source #1: topofunnel content section, "desired reality" framing |
| Pattern 8 (Objection Elimination Machine) | genius.md Pattern 8 | **VERIFIED** | Source #1: "Your sales calls should have zero objections" |
| Pattern 9 (Appointment-Setter-as-Creative-Director) | genius.md Pattern 9 | **VERIFIED** | Source #1: "The appointment setter is almost your creative director" |
| Pattern 10 (Forcing Function Strategy) | genius.md Pattern 10 | **VERIFIED** | Source #1: "I paid Devon JTO 5 figures... a monthly retainer to force myself" |
| Pattern 11 (ICP Data Mining Protocol) | genius.md Pattern 11 | **VERIFIED** | Source #1: onboarding-form question list ("What made you want to work with me?" etc.) |
| Pattern 12 (Desired Reality Resonance) | genius.md Pattern 12 | **VERIFIED** | Source #1: "tell your mom how much you make" reel example |
| Pattern 13 (Zero-Claims Marketing) | genius.md Pattern 13 | **VERIFIED** | Source #1: "I never make claims... You decide the claim that you want for yourself" |
| Pattern 14 (SOP Documentation Obsession) | genius.md Pattern 14 | **VERIFIED** | Source #1: "I document all my SOPs... No one does this" |
| Pattern 15 (MVP Culture Protocol) | genius.md Pattern 15 | **VERIFIED** | Source #1: "we have an MVP voting form... gets $1,000 bonus" |
| Pattern 16 (Engagement-as-IP-Factory / Triple-Output Design) | genius.md Pattern 16 | **LIKELY** | Not found verbatim in any of sources #1-5. Reads as a plausible extension of Pattern 14 (SOP obsession) but not a confirmed SooWei quote — flagged in-line in genius.md rather than silently kept as if sourced. |
| Hall of Fame Exemplars ("Life of Leverage" IG series, "Objection-to-Content Production Line") | genius.md | **LIKELY** | Illustrative synthesis built from the verified patterns above, not verbatim transcript scenes. Internally consistent with sourced patterns; not independently confirmed as things SooWei actually posted. |
| Signature Moves (4 items) | genius.md | **LIKELY** | Same basis as Hall of Fame Exemplars — synthesized behavioral summaries of verified patterns, not verbatim. |
| "$2M+/year profit" (SKILL.md) | SKILL.md frontmatter/body | **UNCONFIRMED** (as objective fact) / VERIFIED (as self-reported claim) | Source #1: "how I built a $2 million consulting business" — SooWei's own stated figure. No independent (non-self-reported) financial verification exists in the recovered sources; treat as self-reported. |
| "$0→$137K/month" client (SKILL.md) | SKILL.md | **UNCONFIRMED** (as objective fact) / VERIFIED (as self-reported claim) | Source #1: "Alec went from 0 to 137K a month in 4 months" — self-reported by SooWei, not third-party verified. |
| "$224K/month" (referenced in extraction history, not currently in SKILL.md) | — | **UNCONFIRMED** (as objective fact) / VERIFIED (as self-reported claim) | Source #4, transcript timestamp 13:31: "$224,000 a month" — self-reported. |
| `references/prompts/`, `references/prompts-v2/`, `references/_legacy-prompts/` (14 files each) | skill dir | **LIKELY** | Structure-pure execution prompts generated from the extraction; not individually re-verified against transcript quotes in this repair pass (out of scope — this pass targets the 3 failing heartbeat checks only). |

## Labeling key
- **VERIFIED**: exact or near-exact (documented edit) contiguous match found in a read
  source file, cited above with member path.
- **LIKELY**: consistent with verified material and plausible given the expert's
  documented patterns, but not itself a verbatim quote found in recovered sources.
- **UNCONFIRMED**: could not be corroborated beyond the expert's own self-report; no
  external/third-party verification exists in the sources recovered for this repair.

No claim in this ledger is labeled based on absence-without-search — every UNCONFIRMED
or LIKELY label above followed a full read of the five recovered transcript files.

## 2026-09-04 organic content acquisition expansion

Two additional primary sources were supplied by Farrice and preserved under
`extractions/soowei-goh-organic-content-acquisition-2026/sources/`:

| ID | Published title | Evidence package | Integrity |
|---|---|---|---|
| `Y388trCakrs` | “my exact $3M content strategy to sign $50k+ clients” | raw VTT, continuous transcript, 908 timestamped segments, metadata, 7 decision-relevant frames, spoken/visual ledger | VTT SHA-256 `9348cf689f42e29a746e7d8e45e2e0467670455bf7accea10a90dfc272af7e4c` |
| `PRqSCE8uZns` | “i made over $7M by posting on instagram… here’s what actually works in 2026” | raw VTT, continuous transcript, 1,090 timestamped segments, metadata, 6 decision-relevant frames, spoken/visual ledger | VTT SHA-256 `45d9936df6a622ceb4fdcb29454a6563bc6d3f6637bac8ea09132294de47feaf` |

New Patterns 17–26 and the eight organic-content workflows are grounded through
`references/organic-content-acquisition-source-map.md`. Revenue, conversion share,
client value, and performance claims remain **SELF-REPORTED**. The system mechanics
are **VERIFIED FROM SOURCE**; their transfer to Farrice's business is **UNTESTED**.
