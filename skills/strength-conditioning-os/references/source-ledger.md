# Source Ledger — Strength & Conditioning OS

Every claim the hub's `genius.md` and `references/field-guide.md` attribute to a named
expert, graded VERIFIED / LIKELY / UNCONFIRMED. Ground truth = the four lane skills'
own `genius.md` files (`andy-galpin-training-intelligence`, `michael-israetel-hypertrophy`,
`eugene-teo-training`, `alan-aragon-nutrition`) plus `references/field-guide.md`'s
11 single-conversation expert entries, all dated to the source ingestion:
**claude.ai export, 2026-07-01** (per each skill's SKILL.md frontmatter `source:` field).
No dedicated `extractions/` folder exists for Galpin, Israetel, Teo, Aragon, Ethier,
Magness, Lieberman, or Bikman — confirmed by `find extractions/ -iname` search
returning zero matches for all four lane-expert surnames on 2026-07-17. The lane
skills' own genius.md files, already carrying verbatim-quoted material, are the
canonical ground truth this hub cites against.

VERIFIED = the exact quote or figure was found verbatim (or near-verbatim with only
punctuation/markdown-bold stripped) in the cited file at the cited section.
LIKELY = the claim is consistent with the cited file's stated position but is a
paraphrase, not a direct quote.
UNCONFIRMED = the claim is the named expert's stated position per the source file,
but the file itself flags it as exceeding the broader evidence base (used only for
Bikman's more extreme claims, per the source's own caveat).

---

## Anti-Patterns (genius.md, `## Anti-Patterns (Sourced)`)

| Anti-Pattern | Quote cited | Source | Confidence |
|---|---|---|---|
| "Just add volume" without checking recovery ceiling | `Volume past MRV is "junk volume" — cost without return.` | `skills/michael-israetel-hypertrophy/genius.md`, Pattern: Volume Landmarks & The Deload (line ~43) | VERIFIED — exact string match |
| High-intensity work on a depleted recovery substrate | `even a little high-intensity training overflows it and the system fights back` | `skills/andy-galpin-training-intelligence/genius.md`, Hidden Knowledge: The Stress Bucket (line ~88) | VERIFIED — exact string match |
| Accepting "it felt hard" as proof of a stimulating set | `trained individuals who "knew" 100kg was a hard 10-rep set hit 20 reps` | `skills/eugene-teo-training/genius.md`, Pattern: Effort Miscalibration (line ~17) | VERIFIED — exact string match |
| Treating a plateau as proof the plan failed | `A plateau is "the body doing its job" — homeostasis` | `skills/alan-aragon-nutrition/genius.md`, Pattern: Staircases and Landings (line ~38) | VERIFIED — exact string match |
| Handing a time-crunched client an unsustainable plan | `Never prescribe a plan you couldn't imagine the client following for a year.` | `skills/alan-aragon-nutrition/genius.md`, Pattern: Flexibility Maximization (line ~24) | VERIFIED — exact string match |
| Ignoring the 70/30 training-intensity distribution | `Distribute ~70% of training volume at moderate intensity... and ~30% at high intensity` | `skills/andy-galpin-training-intelligence/genius.md`, Pattern: 70/30 Training Distribution (line ~25) | VERIFIED — exact string match |

## Genius Patterns — Cross-Lane Quotes (genius.md body)

| Pattern | Quote cited | Source | Confidence |
|---|---|---|---|
| Fuel and Recovery Gate Adaptation | `you can't burn fat while insulin keeps you burning glucose` | `skills/strength-conditioning-os/references/field-guide.md`, Benjamin Bikman entry (line ~75) | VERIFIED — exact string match. Corrected 2026-07-17: an earlier uncommitted draft in this same skill directory misquoted this as "keeps the body on glucose," which does not appear verbatim in the source — fixed to match the field guide exactly. |
| One Recovery Budget, Shared by All Lanes | `the same 4×4 done identically forever stops adapting` | `skills/strength-conditioning-os/references/field-guide.md`, Steve Magness entry (line ~59) | VERIFIED — exact string match |
| Compose to the Adherable Minimum | `we evolved to be physically active when it was necessary or rewarding, and to rest whenever possible` | `skills/strength-conditioning-os/references/field-guide.md`, Daniel Lieberman entry (line ~67) | VERIFIED — exact string match |

## Field Guide Entries (references/field-guide.md, unchanged by this repair)

11 single-conversation experts, each already labeled `[from source]` or `[referenced]`
in the field guide itself. Re-verified names against the live file on 2026-07-17
(an earlier uncommitted draft in this skill directory misspelled two names — corrected
here, not carried forward):

| Expert | Field-guide label | Confidence | Note |
|---|---|---|---|
| Jeremy Ethier | [from source] | VERIFIED | Named repeatedly in genius.md patterns; entry matches field-guide.md |
| Eric Helms | [referenced] | LIKELY | Established public framework (pyramid of priorities); not a direct transcript quote |
| Layne Norton | [referenced] | LIKELY | Established public framework (reverse dieting); not a direct transcript quote |
| Brad Schoenfeld | [referenced] | LIKELY | Peer-reviewed research summary; not a direct transcript quote |
| Greg Nuckols | [from source (referenced in tracker panel)] | LIKELY | Field guide's own label already hedges "referenced in tracker panel" |
| Chris Beardsley | [referenced] | LIKELY | Mechanistic research summary; not a direct transcript quote |
| Steve Magness | [from source] | VERIFIED | Quoted verbatim above (4×4 line) |
| Daniel Lieberman | [from source] | VERIFIED | Quoted verbatim above (evolved-to-rest line) |
| **Benjamin Bikman** | [from source] | VERIFIED for the core mechanism; UNCONFIRMED for his extreme claims | Field guide and genius.md both flag: "his more extreme claims (specific reversal rates, salt/cholesterol/fasting positions) exceed the source evidence." **Correction:** an earlier uncommitted draft in this skill directory (found in the working tree, not part of any commit) named him "Ron Bikman" — the field guide and every lane reference consistently say **Benjamin Bikman**; corrected here. |
| **Menno Henselmans** | [referenced] | LIKELY | Data-driven physique coaching. **Correction:** the same earlier uncommitted draft named him "Martin Henselmans" — the field guide says **Menno Henselmans**; corrected here. |

## Provenance note on the four lane experts (Galpin, Israetel, Teo, Aragon)

No raw transcript/extraction folder exists under `extractions/` for these four names
(verified via `find extractions/ -iname "*galpin*"` etc., zero results, 2026-07-17).
Each lane's own `SKILL.md` frontmatter states `source: "claude.ai export 2026-07-01"`
and each lane's `genius.md` already carries verbatim-quoted material from that export.
This hub treats those genius.md files as its ground truth for cross-lane citation —
per the assignment's sourcing rule, "verbatim quotes already inside the skill files"
count as ground truth. No claim in this repair asserts a transcript or video source
beyond what each lane skill already states about its own provenance.
