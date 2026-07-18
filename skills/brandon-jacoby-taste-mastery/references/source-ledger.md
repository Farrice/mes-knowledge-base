# Source Ledger: Brandon Jacoby Taste Mastery

Every claim, quote, and anchor used across `SKILL.md`, `genius.md`, and `references/` is labeled here. Absence of a source was verified by direct file read + `wc -c` byte count on 2026-07-17, not inferred.

## Primary Source

| Source | Path | Verified size | Status |
|---|---|---|---|
| Video transcript | `_active/codex-harvest-2026-06-11/extractions/brandon-jacoby-taste-mastery/transcript.txt` | 56,449 bytes (confirmed via `wc -c`, 2026-07-17) | VERIFIED — read in full |
| Source metadata | `_active/codex-harvest-2026-06-11/extractions/brandon-jacoby-taste-mastery/source-metadata.md` | 741 bytes (confirmed via `wc -c`, 2026-07-17) | VERIFIED — read in full |

**Note on location**: No `extractions/brandon-jacoby-taste-mastery/` directory exists at repo root (confirmed by directory listing, 2026-07-17) — the only copy of the source transcript lives under `_active/codex-harvest-2026-06-11/extractions/brandon-jacoby-taste-mastery/`. `SKILL.md`'s "Source Transcript" pointer (`extractions/brandon-jacoby-taste-mastery/transcript.txt`) is therefore a stale root-relative path from an earlier repo layout; the file itself is real, present, and was read for this repair. This is flagged, not silently fixed, since correcting the pointer is outside this repair's scope (not a failing check).

## Video Metadata (from source-metadata.md)

| Field | Value | Status |
|---|---|---|
| Video title | "Brandon Jacoby - Seeing Taste vs. Creating Taste as a designer" | VERIFIED — literal string in source-metadata.md |
| Channel | Dive Club | VERIFIED — literal string in source-metadata.md |
| URL | https://www.youtube.com/watch?v=RaKFP_DuqpA | LIKELY — as recorded in source-metadata.md; not re-verified against YouTube live (no network fetch performed in this repair) |
| Duration | 52:37 | VERIFIED — literal string in source-metadata.md |
| Word count | ~10,650 | VERIFIED — literal string in source-metadata.md (not independently recounted) |
| Extraction date | 2026-05-05 | VERIFIED — literal string in source-metadata.md |
| Video publish date | Not stated in source-metadata.md | UNCONFIRMED — no publish date field exists in the source file; do not infer one |

## Claims Used in genius.md — Claim-by-Claim

| Claim / quote | Location in genius.md | Status |
|---|---|---|
| "I think the tastemakers know when to break the rules and when to push beyond the boundaries of what exists today and when to quiet and to go with the flow." | Core Genius; Verbatim Exemplars | VERIFIED — exact substring, transcript.txt (appears twice: cold open and mid-interview) |
| "that process of zooming in and out, I think is is what creates taste." | Master Principle | VERIFIED — exact substring (including the "is is" stutter, transcribed verbatim) |
| "there are patterns that work that show up in 90% of the products out there." | Pattern 1 | VERIFIED — exact substring, from the Nikita/X onboarding segment |
| "a lot of like the issue our industry faces right now is like people trying to stick to the pattern a little bit too much and kind of like revert to the mean a little bit too much." | Pattern 1; Anti-Patterns | VERIFIED — exact substring |
| "if someone says anything that would get in the way of questioning a requirement, why is that a requirement in and of itself?" | Pattern 2 | VERIFIED — exact substring, from the X/Elon design-review anecdote |
| "decisiveness actually is a really, really big deal for this year and beyond." | Pattern 2 | VERIFIED — exact substring |
| "great design has always been great design agnostic of the tools." | Pattern 3 | VERIFIED — exact substring |
| "The single biggest way that AI specifically has helped with client work is actually the ability to like build my own design tools." | Pattern 4 | VERIFIED — exact substring |
| "the technology inspired the art, the art challenged the technology." | Pattern 4 | VERIFIED — exact substring; Jacoby attributes this to John Lasseter re: Toy Story. Lasseter's original authorship of the line is LIKELY (widely attributed to him in design/animation circles) but not independently verified against a primary Lasseter source in this repair — treat the attribution as Jacoby's claim, not independently fact-checked. |
| "I made this really cool like particle effect where it assembles into icons for these feature cards." | Pattern 4 | VERIFIED — exact substring |
| "the in-between moments that you get when you're moving things around on a Figma canvas, like that's where like the real discovery happens." | Pattern 5; Anti-Patterns | VERIFIED — exact substring |
| "it's not just A or B, but it's some weird C thing that you didn't think of originally that like you stumbled upon as like a happy accident." | Pattern 5 | VERIFIED — exact substring |
| "Craft meets consequence to me is like a idea where it challenges where a lot of our industry has gone to designing for other designers." | Pattern 6; Verbatim Exemplars | VERIFIED — exact substring |
| "craft follows consequence, consequence follows craft." | Pattern 6 | VERIFIED — exact substring |
| "The number one thing that I would say to that person is find someone who you enjoy working with." | Pattern 7; Verbatim Exemplars | VERIFIED — exact substring |
| "the more artifacts you can produce actually accelerates the founders thinking." | Pattern 7 | VERIFIED — exact substring |
| "Two-thirds of the world I think have an iPhone." | Pattern 8 | VERIFIED — exact substring. Underlying statistic (actual global iPhone ownership share) is Jacoby's own estimate, not independently fact-checked in this repair — treat the "two-thirds" figure as his claim (UNCONFIRMED as external fact), the quote itself as VERIFIED transcript content. |
| "that's something that just most people could never experience until Uber and and Lyft and it was created. That's taste." | Pattern 8 | VERIFIED — exact substring |
| "I know that I will design something the first time that looks like absolute garbage." | Pattern 9; How to Use This Skill; Verbatim Exemplars | VERIFIED — exact substring |
| "starting is not where you finish and doesn't have to be where you finish." | Pattern 9 | VERIFIED — exact substring |
| "collaborating to bring more taste to fight the slop." | Pattern 10 | VERIFIED — exact substring |
| "there is something with, you know, my signature on it that can, you know, stand out." | Pattern 10 | VERIFIED — exact substring |
| "you just have to question every requirement." | Signature Moves | VERIFIED — exact substring, from the Elon/X first-principles anecdote |
| "an agent that helps me with like logistics and some client management and my email." | Signature Moves | VERIFIED — exact substring |
| "it's not a hard and fast rule where, you know, tastemakers break all the rules and reinvent the wheel." | Anti-Patterns | VERIFIED — exact substring |
| "we're really good at understanding other designers and producing work, meaning like a portfolio, that looks great to them." | Anti-Patterns | VERIFIED — exact substring |
| "maybe they're for a specific set of people that are not accessible to everyone. And like I actually I don't think that's true." | Anti-Patterns | VERIFIED — exact substring, from the high-taste-hotels discussion |
| "vibe code products or like people that are just jumping to AI to kind of fill their the gaps in the visual design." | Anti-Patterns | VERIFIED — exact substring |
| "for most people like good enough will be okay. That's not a bad thing." / "there's always like the ones that push it just a little further." | Anti-Patterns | VERIFIED — exact substrings, adjacent in transcript |
| Build Decision (Oren / Nate B Jones / Jacoby differentiation) | Stacking Notes | VERIFIED — literal text from source-metadata.md "Build Decision" section |

## Claims NOT Verified (flagged, not silently dropped)

| Claim | Status | Why |
|---|---|---|
| Any statement about Brandon Jacoby's current client roster, pricing, or availability beyond what's stated in the transcript | UNCONFIRMED | Not present in source material; do not fabricate |
| YouTube video's publish date (as distinct from extraction date) | UNCONFIRMED | Not recorded in source-metadata.md |
| "Two-thirds of the world" iPhone ownership as external fact | UNCONFIRMED as fact / VERIFIED as Jacoby's quoted claim | See table above — the quote is real, the underlying statistic was not independently checked |
| Lasseter's original authorship/wording of the "technology inspired the art" line | LIKELY | Commonly attributed to Lasseter re: Pixar/Toy Story in design discourse, but not checked against a primary Lasseter source in this repair |
