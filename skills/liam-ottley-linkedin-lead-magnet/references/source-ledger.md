# Source Ledger — liam-ottley-linkedin-lead-magnet (Wave 3 Lane 4 repair)

Repair pass sourcing. Existing `references/source-evidence.md` (unchanged, still authoritative for evidence counts/anchors) is not duplicated here — this ledger covers only claims/quotes ADDED during this repair.

Primary package: `extractions/video-context/3iR3kHxCwfo/` — "How to Turn LinkedIn into a Personal Brand Lead Magnet with AI," Liam Ottley's channel, guest Lara Acosta. Ground truth files used: `3iR3kHxCwfo.en.vtt` (607,294 bytes, word-level karaoke timestamps) and `transcript.txt` (244,345 bytes, line-timestamped). Both read directly; quotes below reconstructed by de-duplicating the VTT's overlapping rolling-caption rows (each caption block repeats trailing words from the prior block — a known artifact of this caption format, not double-speech) via longest-suffix-overlap merge, then verified as exact substrings of the merged text.

| Claim / Quote Added | Timestamp | Label | Source | Note |
|---|---|---|---|---|
| "Studies show that LinkedIn is responsible for generating 80% of all B2B leads" | 00:00:01 | VERIFIED | transcript.txt / .vtt | Opening line, exact substring |
| "You think about two things. You think about monetizable expertise and you think about strategic arbitrage. Those are the two key pillars that every single time we implement them, we get results." | 00:11:48–00:11:57 | VERIFIED | .vtt (reconstructed) | Exact substring after dedup merge |
| "The rehook is your second chance to retain someone and get them to click more." | 00:14:35 | VERIFIED | .vtt (reconstructed) | Exact substring |
| "my one person business is about to cross $200,000 a month" | 00:35:05–00:35:09 | VERIFIED | .vtt (reconstructed) | Exact substring; ASR mis-hears "hook" as "hawk" earlier in same sentence — bracket-corrected in genius.md and flagged inline |
| "when you are choosing to schedule it, you're also choosing to forget about it... the post has a higher chance of dying" | 00:57:33–00:57:45 | VERIFIED | .vtt (reconstructed) | Exact substring, "..." elides "of of the" ASR stutter |
| "here's your problem. Founders, your LinkedIn content sucks. Agitate: it's costing you thousands of dollars daily. And then the solution is: here's how to write content that sells." | 00:49:22–00:49:34 | LIKELY | .vtt (reconstructed) | Content verbatim; colons after "Agitate"/"is" added for readability (VTT has no punctuation) and one stutter repeat ("Founders founders") silently normalized to single word — flagged here per envelope Rule 1 |
| "biggest mistakes I see with people whether it's LinkedIn content or even YouTube content is they... got a bunch of videos of like case studies... it's probably not... going to get a few hundred views realistically" | 00:32:41–00:32:53 | VERIFIED | .vtt (reconstructed) | Ellipses mark elided disfluency repeats ("the the," "they they," "I'm I'm"); retained words are exact substrings |
| "the main mistake that people make when storytelling and using authority jacking... is that they get too broad that they forget to talk about their business themselves or what they actually help people with" | 00:33:47–00:34:00 | VERIFIED | .vtt (reconstructed) | Exact substring |
| "stories tend to seem cringe on LinkedIn... because they'll be like, 'Oh my god, my dad died.' And it's a selfie of this girl" | 00:36:46–00:36:55 | VERIFIED | .vtt (reconstructed) | Exact substring |
| "LinkedIn hates spam... tagging people that you know you can't reach, that you don't have on your phone to message" | 00:38:57–00:39:07 | VERIFIED | .vtt (reconstructed) | Exact substring |
| "he's educating on what's happening as well. And then he actually turned this into a lead magnet" | 00:42:51–00:42:55 | VERIFIED | .vtt (reconstructed) | Exact substring |
| "eight word long hooks are best. Always use a specific outcome or number" | 00:50:04–00:50:07 | VERIFIED | .vtt (reconstructed) | Exact substring |
| SLAY framework named by Lara; reports 40-year-old men in her audience using it | 00:45:09–00:45:26 | LIKELY | .vtt (reconstructed) | Underlying ASR is garbled here ("40y old 40 men," cross-talk from a second speaker) — paraphrased in prose rather than quoted verbatim for this reason; not presented as a direct quote in genius.md |
| "let's say I say, 'I love this post that I just saved from my swipe file. Based on what you know about me, write me a similar post'" | 00:51:19–00:51:26 | VERIFIED | .vtt (reconstructed) | "Uh" filler dropped between "file." and "based" |
| "we have a knowledge base where you basically just upload every single document that you've ever created" | 00:52:14 | VERIFIED | .vtt (reconstructed) | Exact substring |
| "go beyond the cringe part of posting on LinkedIn and feeling like a robot" | 00:06:56–00:07:02 | VERIFIED | .vtt (reconstructed) | "uh" filler dropped after "beyond" |
| "it's literally seen as the cringiest platform" (AI slop framing) | 00:05:44–00:05:52 | VERIFIED | .vtt (reconstructed) | Exact substring |
| "The Real Product Is The Bridge" (lead magnet = bridge to paid transformation) | n/a | VERIFIED | `skills/liam-ottley-linkedin-lead-magnet/references/hidden-knowledge.md` (pre-existing file, unchanged) | Cross-referenced, not re-derived from raw transcript |
| Recognition-test framing (Lara's two-pillar method, "SLAY... because I'm a girl and I slay all the time") | 00:45:09–00:45:12 | VERIFIED | .vtt (reconstructed) | Exact substring, used in "How to Use This Skill" section |

## Method note on reconstruction

The `.vtt` file uses rolling/karaoke-style captions: each timed block repeats the tail of the previous block plus 2–6 new words. A naive read of consecutive blocks therefore triples word counts. Reconstruction script: parse blocks in time order, for each new block find the longest suffix-of-accumulated-words that matches a prefix-of-new-block, append only the non-overlapping remainder. Verified against `transcript.txt` (which carries the same duplication pattern from the same source) for cross-check — timestamps and word order matched in every case above.

## UNCONFIRMED

None of the claims added in this repair required an UNCONFIRMED label — every quote used traces to a verified exact or near-exact (documented above) substring of the source captions. No claim in this pass asserts source absence.
