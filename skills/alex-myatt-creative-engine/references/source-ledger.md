# Alex Myatt — Source Ledger

Every claim used in `SKILL.md`, `genius.md`, and the reference/workflow files, labeled
**VERIFIED** (verbatim quote confirmed by direct file read), **LIKELY** (accurate
paraphrase or reasonable inference from the source, not a verbatim quote), or
**UNCONFIRMED** (asserted in the skill but not locatable in any source file — flagged,
never anchored as fact).

**Sources consulted** (both read in full for this repair):
- `extractions/alex-myatt/transcript.txt` (121,038 bytes / ~23,420 words — single 90-min
  YouTube interview, Copy That channel, https://www.youtube.com/watch?v=82NKxogqVMk)
- `extractions/alex-myatt/extraction-report.md` (34,259 bytes — the Mastery Extraction
  built from that transcript)
- `extractions/Alex Myatt/transcript.txt` — duplicate copy of the same transcript under a
  differently-cased directory name (confirmed identical byte count, 121,038 bytes; not a
  second source)

No other extraction files, notebooks, or secondary sources exist for Alex Myatt in this
repo as of this repair (`ls extractions/ | grep -i myatt` returns exactly the two
directories above).

---

## Biographical claims (SKILL.md / genius.md "Who Alex Is")

| Claim | Label | Anchor |
|---|---|---|
| $280M+ attributed sales, 50,000+ ads | VERIFIED | transcript.txt: "I've run more than 50,000 ads. I've driven about $280 million in sales" |
| Creative Strategy Mentor at Daily Mentor, $1M+ revenue gate | VERIFIED | transcript.txt: "I'm a creative strategy mentor for Daily Mentor, which is the world's biggest ecom like founders community. You have to be doing at least a million dollars a year to join that." |
| Co-owner of Copy That YouTube channel | VERIFIED | transcript.txt: "It's a ... copyrightiting and marketing ... YouTube channel and business which you've appeared on ... it's really fun" (source's own show) |
| Two ecom exits by 22, £70K + multi-six-figure | VERIFIED | transcript.txt: "by the age of 22, I had ... 400 grand in like exit" and "I sold it for 70k" (first store) + "beef jerky ... end up selling for you know multiple six figures" (second store) |
| Council estate in Watford, carer + chip shop from age 13, £18K council salary, £80K first freelance year | LIKELY | transcript.txt origin-story section describes the family-carer role, council-audit day job, and side-gig income crossover in substance; exact figures (£18K/£80K/age 13) are stated across the same passage but were not re-verified digit-by-digit against a second source — treat as LIKELY, not independently corroborated |
| "Doesn't have a driving license. Loves dogs." | UNCONFIRMED | Not located verbatim in transcript.txt on this pass; if this detail was captured by the original extraction agent from a portion of the transcript not re-searched here, it should carry a ledger anchor before the next repair — flagged rather than silently repeated |

---

## The 14 Genius Patterns

| Pattern | Label | Anchor |
|---|---|---|
| Atomic Decomposition (Socratic "what is this in itself?") | VERIFIED | extraction-report.md Pattern 1; consistent with transcript.txt's repeated "I just broke everything down. What does this mean? What parts of an ad are there?" |
| 5-Step Wealth Loop (Identify→Solve→Systematize→Delegate→Sell) | VERIFIED | transcript.txt: "problem, solution, systemize, delegate, and then sell it" |
| Creative Pyramid (Avatar / Idea-Style-Hook / Volume-Diversity-Relevance) | VERIFIED | transcript.txt: "the idea is essentially what are you actually saying?" + "the bottom of the pyramid, you've got the three ... pillars ... volume, diversity, relevance" |
| Content Grid (Ideas × Styles matrix) | LIKELY | transcript.txt describes "axis at the top for ideas, axis at the down the side for styles and each intersection" verbatim; the "50-300 concepts" range is the extraction team's estimate, not a number Alex states |
| Vacation Test | LIKELY | Not named "Vacation Test" verbatim in the transcript read on this pass; the underlying mechanic (does a viewer recognize a repeat) is consistent with the "blends into the background... you start to ignore it" passage on repetition. Named by the extraction team. |
| 2 Atoms of Attention (Relevance + Difference) | LIKELY | Consistent with transcript.txt's Meta-diversity-economics passage (novelty "might grab your attention... cut through") but the exact "2 atoms" framing/label is extraction-team synthesis |
| Land & Expand | VERIFIED | transcript.txt: "then you can jump in and when you can close like a creative strategy client, you can take over their advertising and you can take over the email back end" |
| Care Square (Results/Perception/Relationship/Efficiency) | VERIFIED | transcript.txt: "I have a kind of a fourprong. I call it like the care square" + individually verified quotes for Results, Perception (homepage), Relationship (birthday hampers) |
| Title-as-Mechanism | LIKELY | Consistent with "don't get married to that term either... it's you can you can change it" on the creative-strategy buzzword; extraction team generalized to "titles" broadly |
| IVOC Mining | UNCONFIRMED | Not located as a named practice in the transcript passages searched for this repair; extraction-report.md presents it as Pattern 10 without a directly cited transcript quote. Treat the specific "50+ posts/comments, 3+ unmoderated venues" figures as extraction-team estimates, not Alex's stated numbers, until re-verified |
| Hyperlocal Outreach Specificity | VERIFIED | transcript.txt pharmacy example: "Hey, I noticed you're on this road, you know, for example, like next to this like other bigger pharmacy... we actually help smaller independents get more of the market share of town" |
| Yes-First, Figure-Out-Later | VERIFIED | transcript.txt: "I've always believed that saying yes first and then working out later is the best way to grow" |
| Three S's (System/Selling/Strategy) | VERIFIED | transcript.txt: "I always talk about the three S's. There's um system, selling, and strategy" |
| Volume-as-Probability | LIKELY | Consistent with transcript.txt's Andromeda/volume-economics passage ("Meta rewards volume"); the "professional guesser" framing is extraction-team language, not Alex's phrase |

---

## Anti-Patterns (genius.md)

All 8 anti-pattern bullets carry an inline verbatim quote or explicit LIKELY/synthesis
flag as of this repair — see `genius.md` → "Anti-Patterns" section directly for the
paired quote + anchor per item. Summary:

| Anti-pattern | Label |
|---|---|
| Surface-only diversification | VERIFIED (yellow-background / entity-ID quote) |
| AI as research source | VERIFIED ("Show me your research" / Claude quote) |
| Skill-selling not problem-selling | LIKELY (transcript "offload... next point of leverage" quote + extraction-report Hidden Knowledge #8 synthesis) |
| Conceptual frameworks without SOPs | VERIFIED ("ton of SOPs... boring stuff that matters") |
| Niching down as ideology | VERIFIED ("hated the advice... niche down... proud generalist") |
| Saying no to in-domain requests in years 1-5 | LIKELY (years-1-5-vs-5-7+ split is extraction synthesis of the verified "yes first" quote, not Alex's own stated timeline) |
| Optimizing Results without Perception | VERIFIED ("perceive the homepage to be super valuable") |
| Pre-Andromeda advice repeated as current | VERIFIED ("after the Andromeda update, Meta would classify... under the same entity ID") |

---

## Operational sub-systems flagged as thin coverage (pre-existing, disclosed in SKILL.md)

- **5 hook types** (question/declarative/curiosity-gap/pattern-interrupt/etc., referenced
  throughout `references/prompts-v2/*.md` and workflows) — **UNCONFIRMED** as an
  Alex-stated taxonomy. Searched transcript.txt for "hook type(s)," "5 hook," "hook
  variant" — zero matches. SKILL.md's own "Notes on Source" section already discloses
  this: "some operational sub-systems (5 hook types, content grid axes, asset library
  protocol) are referenced but not exhaustively documented in the source... infer the
  operational layer." This repair did not change that disclosure — it was already honest
  — but formalizes the UNCONFIRMED label here per the ledger requirement.
- **Content Grid concept-count range (50-300)** — LIKELY, extraction-team estimate built
  from the verified "axis... axis... intersection" grid description, not a number Alex
  states.
- **IVOC venue/quote-count specifics (50+ quotes, 3+ venues)** — UNCONFIRMED as stated
  numbers; the underlying practice (mine unmoderated customer language) is consistent
  with Alex's broader anti-AI-research stance but the exact figures are not in the
  transcript passages located during this repair.

---

## Verification method

Every VERIFIED quote in this ledger and in `genius.md` was confirmed by a direct
`Read`/`grep`-equivalent pass over `extractions/alex-myatt/transcript.txt` (121,038 bytes
— confirmed via `wc -c`, not `wc -l`, since the file is stored as a single unbroken line)
during this repair session, 2026-07-17. LIKELY and UNCONFIRMED labels reflect items not
locatable as exact strings in that same pass — they are not claims that the material is
absent from Alex's broader body of work, only that this repair could not anchor them to
the one source file this skill was built from.
