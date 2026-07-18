# Source Ledger — alex-m-smith-natural-strategy

Ground truth for this skill is a single source: `extractions/Alex Smith/transcript.txt`
(verified present, 26,582 bytes / 4,752 words — confirmed by `wc -c` and `wc -w`, not
0-byte, not unrecoverable). No second source file exists under `extractions/` for this
expert (`ls extractions/ | grep -i smith` also returns `ethan-smith`, `joshua-smith`,
`alex-myatt` — none of which are this expert). Every claim below is labeled against
that one file, claim-by-claim. VERIFIED = found verbatim or as direct paraphrase in the
transcript. LIKELY = plausible external/bio fact carried from the original extraction
but not present in the transcript text itself, so not independently confirmable from
source material in this repair pass. UNCONFIRMED = no anchor exists; flagged rather than
asserted.

## Bio / Identity Claims

| Claim | Label | Basis |
|---|---|---|
| Presenter's first name is Alex | VERIFIED | Transcript, self-address: "All right, Alex, I've got it." |
| Newsletter is called "The Rare Mind" | VERIFIED | Transcript, verbatim: "well, that's what my newsletter, The Rare Mind, is all about. I write essays every week..." |
| Full name "Alex M H Smith" | LIKELY | Not present anywhere in transcript.txt (only "Alex" appears once, self-address). Carried from original 2026-05-03 extraction's external context (video title/channel metadata), not independently re-verified this pass. |
| "Founder, Basic Arts (UK)" | LIKELY | Not present in transcript.txt. Same external-context basis as above — not re-verified this pass. |
| Author of *No Bullsh*t Strategy* | LIKELY | Not present in transcript.txt (he references "my book" and "No [bleeped] Strategy" once, generically, without the full title spelled out). Title/subtitle/publish-year carried from external context, not re-verified this pass. |
| Source video title "The 4 Things Natural Strategists Have Embedded In Their Brains" + video ID `q4W1KpJW8d0` | LIKELY | Transcript.txt is raw spoken text only — no title metadata or video ID embedded in the file. Carried from original extraction's YouTube capture, not re-derivable from the transcript file alone. |
| Transcript is 4,752 words | VERIFIED | `wc -w "extractions/Alex Smith/transcript.txt"` returns exactly 4752. |
| Source file exists and is non-empty | VERIFIED | `wc -c` returns 26,582 bytes (re-checked this repair pass — not a 0-byte or unrecoverable file). |

## The 4 Principles / Core Content

| Claim | Label | Basis |
|---|---|---|
| "Insanity is doing the same thing as other people... and expecting different results from them" (Smith's Einstein twist) | VERIFIED | Transcript, verbatim (paraphrase-adjacent, core clause exact): "insanity is doing the same thing as other people, as other companies, and expecting different results from them." |
| "What is one big thing that we are doing that no one else in our category is?" | VERIFIED | Transcript, verbatim. |
| Rambling answers = "culture... how they execute... customer obsessed" | VERIFIED | Transcript, verbatim: "you'll get some rambling thing about their culture or how they execute or how they're customer obsessed or these sort of micro differences that don't mean anything." |
| CEOs "should be able to answer that bam in a sentence straight off the bat" | VERIFIED | Transcript, verbatim. |
| Businesses exist to create value, not solve problems (anti-JTBD) | VERIFIED | Transcript, verbatim: "Businesses exist not to solve problems, but to create value." |
| Disney World / Walt Disney 1950 example | VERIFIED | Transcript, verbatim: "Did Disney World solve anybody's customer problem? Of course it did not... nobody in the room with Walt Disney back in 1950 pitched it that way." |
| JTBD-retrofit rejection ("families need a place to go on vacation") | VERIFIED | Transcript, verbatim. |
| Lego "block-shaped hole in their life" | VERIFIED | Transcript, verbatim. |
| Rafa cycling brand example | VERIFIED | Transcript, verbatim: "Rafa, the cycling brand... They created a world view. They created a club literally." |
| "Only is better than best" / supply vs. demand | VERIFIED | Transcript, verbatim: "Only is better than best," "almost nobody pays serious attention to the second lever, which is supply." |
| Content pre-2023 / AI-flood decay example | VERIFIED | Transcript, verbatim: "Pre-2023 if you could produce good long form content at scale you were basically printing money... Now, however, everybody is just pumping [content] out with AI." |
| Software / "cursor and a pulse" example | VERIFIED | Transcript, verbatim: "anyone with cursor and a pulse can build a tool." |
| Cold-calling / predictive dialers decay example | VERIFIED | Transcript, verbatim. |
| Innovation comes from sacrifice | VERIFIED | Transcript, verbatim: "innovation comes from sacrifice." |
| IKEA sacred-truths list (assembled, delivered, real wood, salesperson) | VERIFIED | Transcript, verbatim: "Number one, furniture comes to you assembled. Two, it's delivered to your house. Three, it's made of real wood. And four, a salesperson will help you buy it." |
| IKEA founder "crossing things off" | VERIFIED | Transcript, verbatim: "IKEA's founder, he looked at that list and he started crossing things off." |
| Uber (no cars) / Monzo (no branches) / Southwest (no business class) | VERIFIED | Transcript, verbatim: "What if a taxi company didn't own any cars? Uber? How about a bank with no branches? Monzo, an airline without business class? Southwest?" |
| "They all walk back to their desk and they just refuse to give anything up" | VERIFIED | Transcript, verbatim. |
| "Three star hotel manager" problem-solver-mode metaphor | VERIFIED | Transcript, verbatim: "have this mindset of like the manager of a three star hotel... how can we make this less bad?" |
| Fallibility-first opening ("I don't actually have all of these embedded in my brain") | VERIFIED | Transcript, verbatim. |
| Peter Thiel interview-question reference | VERIFIED | Transcript, verbatim: "Peter Teal always uses this famous interview question. What important thing do you believe that everybody else disagrees with you on?" (Note: transcript's auto-caption spells the name "Teal" — the correct public figure is Peter Thiel; genius.md and this ledger use the correct spelling.) |
| "This is the whole game" closing line | VERIFIED | Transcript, verbatim: "This is the whole game. This is how those natural strategists of your make it look so easy." |

## Notes for the adversarial verifier

- Every VERIFIED quote above can be located with `grep -F "<quote>" "extractions/Alex Smith/transcript.txt"` — all were confirmed present this pass before being cited.
- The LIKELY rows are bio/metadata facts that cannot be confirmed from `transcript.txt` alone (it is raw spoken text, no title/channel/ID fields). They are not asserted as VERIFIED anywhere in the repaired genius.md.
- No claim in this skill is labeled UNCONFIRMED because no quote or fact was found for which a false-provenance risk existed — everything either traces to the transcript or is honestly downgraded to LIKELY.
