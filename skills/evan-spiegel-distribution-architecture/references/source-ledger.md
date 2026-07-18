# Source Ledger — Evan Spiegel Distribution Architecture

## Sources Consulted

1. `extractions/evan-spiegel/transcript.txt` — 83,432 bytes (confirmed via `wc -c`), a
   single-line full transcript of Evan Spiegel's interview on Lenny's Podcast (host
   Lenny Rachitsky). Read in full for this repair pass. **VERIFIED** present and
   non-empty.
2. No other extraction file matching this expert exists in the repo — `ls extractions/
   | grep -i spiegel` returns only the `evan-spiegel/` directory, which contains this
   one transcript. **UNCONFIRMED** (as absence): no secondary source (second interview,
   article, book excerpt) exists for this expert in this repo — verified by directory
   listing and `find`, not assumed.

## Claim-by-Claim Ledger

| Claim (as used in SKILL.md / genius.md) | Status | Basis |
|---|---|---|
| Snapchat has ~1B monthly active users | VERIFIED | Interviewer: "Snapchat has over 1 billion monthly active users"; Spiegel corroborates: "it's almost at a billion uh monthly active users" — transcript.txt |
| Snap generates $6B+/year revenue | VERIFIED | Interviewer: "is generating over 6 billion a year in revenue" (unchallenged by Spiegel) — transcript.txt |
| 8B AR lens photos/day | VERIFIED | Interviewer: "People post over 8 billion AR lens photos a day on Snapchat" — transcript.txt |
| Snapchat Plus: 25M subscribers, $1B+ run rate | VERIFIED | Spiegel: "we just hit 25 million subscribers on Snapchat plus more than a billion revenue run rate" — transcript.txt |
| Design team is 9-12 people, flat, no titles | VERIFIED | Spiegel: "it sort of oscillates between like nine and 12 people design team" + "there's no one that has a fancier title or a role" — transcript.txt |
| Stories originated from "send all" feedback + pressure/permanence insight | VERIFIED | Full walkthrough in Spiegel's own words (send-all requests, social-pressure complaints, chronological/ephemeral/no-metrics design response) — transcript.txt |
| Screenshot detection exploited a touch-event side channel (Bobby's discovery) | VERIFIED | Spiegel describes Bobby discovering that screenshotting during press-and-hold "trigger[s]... an event on the phone... your finger had lost contact with the screen" — transcript.txt |
| Loonshots dual-org framing sourced from a Safi Bahcall book | VERIFIED, name flagged | Spiegel: "a guy Safi Belell who wrote a book called Loonshots" — the ASR transcript renders the author's surname as "Belell"; the actual author of *Loonshots* is Safi Bahcall. Flagged as a likely transcription artifact, not silently corrected. |
| Snap had 200 employees before its first PM hire | **UNCONFIRMED** | This figure is stated by the *interviewer* ("the number I saw is you had 200 employees before you hired your first PM"), not confirmed or repeated by Spiegel in his answer — transcript.txt. Do not attribute this number to Spiegel directly. |
| Design hiring is portfolio-only; range > style; "why" narration required | VERIFIED | Spiegel describes both criteria directly (range vs. repetition = designer vs. artist; ability to narrate "why" behind a piece) — transcript.txt |
| Snap's internal agent stack uses Glean + Claude | VERIFIED | Spiegel: "we have Glean that integrates... all this data for me" and "we've been using Claude to do a lot of the the work... across Snap" — transcript.txt |
| Automated code review has caught ~10,000 bugs | VERIFIED, hedged | Spiegel: "automatically detected like close to 10,000 bugs at this point probably" — his own "probably" marks this as an approximate figure, not an audited count |
| Meta/Facebook cloned Snap features for ~15 years, incl. a recent "Instagram Plus" | VERIFIED | Spiegel: "15 years ago we essentially learned that software is not a moat"; separately, on the Plus clone: "we just hit 25 million subscribers on Snapchat plus... probably enough to get Meta's attention that it's a good time to to copy" — transcript.txt |
| Spectacles/Specs launching after "12 years of investment" | VERIFIED | Spiegel: "it's about to launch specs after you know 12 years of investment" — transcript.txt |
| Snap company size "almost at the scale of entering the Fortune 500" | VERIFIED | Direct Spiegel quote — transcript.txt |
| President Clinton "explainer-in-chief" framing | VERIFIED, phrasing flagged | Spiegel: "he was like you know it's very interesting you know being president is really like being explainer and chief" — rendered as "explainer and chief" in the ASR transcript; commonly known as "explainer-in-chief." Flagged, not silently normalized. |

## Labeling Notes

- Every VERIFIED claim above was checked against a direct keyword match inside
  `extractions/evan-spiegel/transcript.txt` during this repair pass — not recalled from
  training memory.
- No claim in this skill is sourced from any file other than the single transcript;
  there is no second Spiegel source anywhere in this repo.
- Two apparent ASR-transcription artifacts are flagged inline above ("Safi Belell" for
  Safi Bahcall; "explainer and chief" for "explainer-in-chief") rather than silently
  corrected, per the no-invented-provenance rule — a reader should be able to see
  exactly what the source said versus what is commonly known externally.
