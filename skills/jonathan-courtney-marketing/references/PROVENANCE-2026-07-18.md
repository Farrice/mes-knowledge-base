# Provenance — Jonathan Courtney (CEO Marketing Strategy)

Anchor-to-source table for every new claim/quote added in this repair. All
locations are within `extractions/jonathan-courtney/transcript.txt` (41,144
bytes, `wc -c` confirmed) unless noted. The transcript is one continuous
paragraph (no line breaks), so locations are given by surrounding context
rather than line number.

| Anchor (genius.md § Anti-Patterns) | Quote | Source location (context) |
|---|---|---|
| The Procrastination Machine | "These can be procrastination machines that you're basically building for yourself." | transcript.txt — early segment, right after Courtney describes asking CEO friends "are you making more money now or are you making any money now?" |
| The Restaurant Nobody Told | "You literally never told even one person this place exists. That will die pretty quick even though you get to do your little fun procrastination thing." | transcript.txt — the restaurant analogy paragraph, immediately following "Like a analogy that I use for my friends is imagine you start a restaurant." |
| The Skill-Hoarding Delay | "there's a lot of people who listen to this podcast and... they'll set up like a thousand skills before like building one thing" | transcript.txt — closing third of the transcript, Eisenberg's turn beginning "Yeah, I feel like there's a lot of people who listen to this podcast" |
| The Over-Preparation Tell | "the biggest sign for me that they're going to move very slowly is too much preparation" | transcript.txt — "So when I meet other entrepreneurs, the biggest sign for me..." paragraph, shortly before the "less prep, more action" closing line |
| The Off-The-Shelf Blind Spot | "I spent three days building this proposal builder. And then I asked Claude, would it be easier for me to use an off-the-shelf solution?" | transcript.txt — Laura anecdote, in the "I will warn other CEOs out there" paragraph near the end |
| The Efficiency-Over-Abundance Trap | "it's very easy to optimize for the wrong thing and end up spending. It's It's okay if it's for fun, but don't be me." / "I don't think being efficient right now is the is the play." | transcript.txt — same closing paragraph, immediately following the Laura anecdote and preceding "I think the play is scaling up like crazy" |

Note on transcription artifacts: two of the six quotes preserve verbatim
ASR stutters ("It's It's okay," "is the is the play") rather than
silently cleaning them up — this is deliberate so the quote is checkable
by exact string search against the source file, per the envelope's rule
that a quote that cannot be found verbatim must not be anchored.

## Recognition-Test Language (genius.md § How to Use This Skill)

"would Jonathan Courtney recognize this as theirs — his own cold-money,
CEO-as-promoter diagnosis — or does it read like generic growth-hacking
advice wearing his vocabulary?" — newly written for this repair, grounded in
Courtney's own framing in transcript.txt ("cold money angle," "your job as
CEO is not... your job is to promote your business") rather than copied from
another skill's calibration section.

## Model Calibration Section (genius.md § How to Use This Skill)

New section, not present before this repair. Every specific texture claim
(swears mid-sentence, self-deprecating, "cold money angle," "crickets to
dollar signs," "don't be me") is drawn from direct transcript language
already quoted/paraphrased elsewhere in the file (see Genius Patterns #3,
Hidden Knowledge #3, and the new Anti-Patterns section) — no invented
biographical detail was added.

## What Was NOT Touched

SKILL.md, both workflow files, and `references/genius-patterns.md` /
`references/hidden-knowledge.md` were read but not modified — they already
passed their respective checks (`verbatim_exemplars`, `named_entity_floor`,
`workflow_contracts`) and additive-first boundary means no rewrite was
warranted.
