# Provenance — evan-spiegel-distribution-architecture repair

Single ground-truth source for this expert: `extractions/evan-spiegel/transcript.txt`
(83,432 bytes, confirmed via `wc -c`; single-line ASR transcript of Evan Spiegel on
Lenny's Podcast). No second source file exists for this expert in this repo.

## Anchor → Source Map (genius.md additions)

| Anchor location | Quote (verbatim, verified via substring match against transcript.txt) |
|---|---|
| GP-6 (Design-as-Strategic-Bottleneck) | "design actually has always operated as like a bottleneck at the company, which is incredibly important, right? it's intentional uh that things need to be approved by design to ship" |
| GP-11 (Founder Evolution Mapping) | "the job has just changed so dramatically and I think that that's part of what's so energizing about it" |
| GP-14 (JTBD Agent Architecture) | "for Snapchatters right are jobs to be done. And it's as simple as like get people to download the app, right?" |
| HK-2 (Empathy-Velocity Paradox) | "I went to to Stanford for the product design program, which is really focused on empathy" + "I had also been to art school. So I had studied at Art Center. I'd studied at Otis here uh in Los Angeles" |
| HK-3 (Anti-Hierarchy Innovation Tax) | "people become very focused on getting a promotion, right? getting, you know, into the next step of the hierarchy" |
| HK-4 (Rotation Anti-Stagnation) | "if you're a great designer and you're stuck, you know, designing the chat experience for three years, like I mean, how boring is that?" |
| HK-5 (Designer-Who-Codes Inflection) | "automatically detected like close to 10,000 bugs at this point probably" |
| HK-6 (Middle Child Strategic Advantage) | "we're much larger than a a Pinterest or Reddit for example, we're also way smaller than Meta and Google" |
| HK-7 (Crucible Moment Diagnostic) | "it's about to launch specs after you know 12 years of investment" |
| HK-8 (Humanity-First AI Adoption Curve) | "people are massively underestimating the role that human adoption and human comfort" |
| HK-9 (Agent-as-Leadership-Enabler) | "I've built just an agent that will go and comb through everything that's happening in the company" + "we have Glean that integrates uh you know, all this data for me" |
| Capability Unlocks | "25 million" subscribers figure (Snapchat Plus) |

## Anchor → Source Map (Anti-Patterns (Sourced) section)

| Anti-pattern | Quote |
|---|---|
| Never mistake a cloned feature for a moat | "we just hit 25 million subscribers on Snapchat plus more than a billion revenue run rate so was I think probably enough to get Meta's attention that it's a good time to to copy" |
| Don't let designers become PM order-takers | "designers really are producing visuals. They're not really producing the product direction or the strategy or the vision" |
| Never build the literal feature request | "they did create a way to easily share with all of your friends without spamming them all day long" |
| Don't listen via survey | "it's not like the survey model of listening. I don't think that's particularly helpful" |
| Never let hierarchy near the innovation team | "people become very focused on getting a promotion, right? getting, you know, into the next step of the hierarchy" |
| Don't design notification-based wearables | "I don't think receiving phone notifications on your face is like you know a a valuable you know proposition for most folks" + "you're actually looking at like your friend's crotch" |
| Never let PM/design/engineering turf wars go unmanaged | "it sounds highly dysfunctional if folks are having that standoff. That is not not a good thing" |

All quotes above were checked with a Python substring test against the full transcript
text (not recalled from memory) before being written into genius.md. See
`references/source-ledger.md` for the claim-level VERIFIED/LIKELY/UNCONFIRMED table,
including two flagged ASR-transcription artifacts ("Safi Belell" for Safi Bahcall;
"explainer and chief" for "explainer-in-chief") and one claim explicitly marked
UNCONFIRMED as a Spiegel statement (the "200 employees before first PM" figure, which
in the transcript is stated by the interviewer, not Spiegel).
