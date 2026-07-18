# Source Ledger — erica-mallet-brand-magnetism

Claim-by-claim provenance for every anchor cited in `genius.md`. Labels:
**VERIFIED** (primary source read directly, quote confirmed verbatim) /
**LIKELY** (consistent with verified public material or a real in-repo
artifact, but not independently confirmed word-for-word against a primary
recording) / **UNCONFIRMED** (no source located; flagged, not deleted).

Real person confirmed: **Erica Mallett** (the podcast/site spell it with a
double-t; this skill's slug and file headers use "Erica Mallet," single-t —
a pre-existing naming inconsistency, out of scope for this repair pass, noted
here so it isn't mistaken for a different person). Brand strategist, former
national radio host (Australia), YouTube channel "Theory Of One"
(@ericamallett), site ericamallett.com. — **VERIFIED** via live WebSearch/
WebFetch, 2026-07-17.

## Primary transcript (T-series) — VERIFIED

**Source**: Transcript of "How to Make Your Brand So Magnetic They Stop
Scrolling ft. Erica Mallett," THE 505 PODCAST episode 177
(YouTube: `https://www.youtube.com/watch?v=aN02fSGO2TU`; also on Spotify/
Apple/RedCircle). Transcribed by Merlin AI. Retrieved from this system's own
historical export: `_archive/claude-export-2026-07-01.tar.gz` →
`claude-export/raw/batch-0001/conversations.json`, conversation uuid
`0306caa8-5469-4c3d-9096-7cf8f7e15167` ("Erica Mallet | How to Make Your
Brand So Magnetic They Stop Scrolling | 505 Podcast & Personal Brand
Mastery," captured 2026-01-20), first human message's attachment
`extracted_content` field — 118,576 characters, full transcript. This is the
same source the skill's own `agents/erica-mallet/AGENT.md` (in
`_active/codex-harvest-2026-06-11/`) footnotes as "Erica Mallet MES 3.0
Extraction (505 Podcast)" — this repair pass independently re-opened and
re-quoted the raw transcript rather than trusting that footnote at face
value, per the envelope's rule against invented-provenance claims.

Status: **VERIFIED** — text below was read directly from the extracted
transcript file, not reconstructed from memory or the skill's prior
paraphrase.

| Item | Verbatim quote (as transcribed) | Used in genius.md |
|---|---|---|
| T1 | "Your job as a creator is to find a thousand different ways to say the same nine things... why copying others is the quickest way to kill your magnetism before it even starts... I don't think attention is the biggest asset anymore. It is connection." (opening teaser, one continuous block) | Pattern 1, Anti-Patterns (copying, attention-vs-connection) |
| T2 | "Gary Vee has been saying the same thing for years and years and years... I call this hiding the vegetables in the cake." (one continuous answer) | Pattern 5, Pattern 13, Tacit 6, Anti-Patterns (belief-as-sermon) |
| T3 | "[Zeigarnik-effect, transcribed as 'zonic effect'] open loops make us want to come back time and time again. So, the Mona Lisa, for example... you don't know if she's smiling or frowning." | Pattern 6 |
| T4 | "I got people calling me cringe when I was speaking on air... I didn't have my voice then. I found it." / "...you talk about getting over this uh the cringe mountain." (two related moments, same interview) | Pattern 12, Tacit 5, Anti-Patterns (discomfort-as-stop-sign) |
| T5 | "It's a little bit of a cheat code to have two of you because you're instantly different because it's a combination that no one else can really [replicate]... your chemistry can't be replicated really." | Pattern 3, Tacit 7, Tacit 12 |
| T6 | "It's not about copying. It's about understanding what is taking place... having the mind of a scientist when you're looking at outliers." | Anti-Patterns, Tacit 12 |
| T7 | "I think that be authentic is the most annoying thing that anyone could ever say. It pisses me off so much... this identity work... is just so vital." | Tacit 14, Anti-Patterns |
| T8 | "One strategy that I really love is called the enemy effect which is uniting your audience against an ideological enemy... it creates an in-group and an out group." (goes on to contrast Andrew Tate/"the matrix" vs. Taylor Swift/"the cool girl") | Tacit 2 |
| T9 | "If you can build a belief-based content strategy and brand strategy, you're far ahead of 99% of people... First, you sit down and you nut out your themes, your brand themes... [Gary Vee's theme is business, he believes] slow growth is the only way. Whereas someone like Alex [Hormozi]... grind hard, win fast..." | Tacit 3, Tacit 4, Tacit 13 |
| T10 | "For us, it's YouTube. Like YouTube is our child... it is one of the only platforms tha—" (quote runs past the captured context window; NOT completed with invented text) | Tacit 8 |
| T11 | "...we're moving away from the attention economy and we're moving more into the... connection economy... he wrote a book called Day Trading Attention..." (referring to Gary Vaynerchuk's real book) | Tacit 11 |

## Live web sources (W-series) — VERIFIED (fetched 2026-07-17)

| Item | Source | What it confirms |
|---|---|---|
| W1 | `https://www.ericamallett.com/` | Bio: "over a decade shaping cultural influence," former national radio host, "built platforms for billion-dollar corporations like ALDI," "Strategy rooted in human behaviour, not short sighted hacks," "Obsession Framework" (Identity/Expression/Obsession). |
| W2 | `https://www.ericamallett.com/themagneticedge` | "Build a cult-like brand." / "A simple framework for turning brand beliefs (vegetables) into entertaining, viral ready content (cake)." / "Post less, and get more traction" / "The Cult Brand Blueprint" (point of view, beliefs, tone, enemy). Independently corroborates the transcript's vegetable/cake and enemy-effect language. |
| W3 | `https://realbusinessconnections.com/podcast/ericamallett/` (episode: "Why Ellen Was CANCELLED But Kanye Isn't") | "Imperfections are the point of a brand... it's necessary to have them built into your brand." / "It's important to be aware of your imperfections and then use them strategically in your brand." / "The best way to attract your people is to have a set of beliefs." / "A niche is important, but you also have to think about your emotional niche." |
| W4 | WebSearch: 505 Podcast episode 177 listing (Spotify/Apple/RedCircle), YouTube "Theory Of One" (@ericamallett), LinkedIn `linkedin.com/in/erica-mallett-ab7232a0` | Confirms the episode and person exist as described; RedCircle episode page itself returned HTTP 403 on direct fetch (not used as a quote source — see Gaps below). |

## In-repo LIKELY sources (L-series)

| Item | Source | Status |
|---|---|---|
| L1 | `references/prompts-v2/crown_jewel_prompt_1_belief_architecture.md` line 50: "The through-line frequently reveals itself through energy and enthusiasm patterns, not resume bullet points." | **LIKELY** — this is a system-authored practitioner prompt built from the extraction, not a Mallett verbatim line. Directionally consistent with T5's "chemistry can't be replicated" framing but not independently confirmed against a Mallett recording. |
| L2 | `references/prompts-v2/crown_jewel_prompt_7_tone_filter.md` lines 11-51 (tone-word-as-filter framework) | **LIKELY** — same caveat as L1. The "3 tone words" framework itself is a real, pre-existing part of this skill's practitioner-prompt library, but its exact phrasing as Mallett's own words was not found in the retrieved transcript. |
| L3 | Skill's pre-existing Pattern 7 / Tacit 4: "Could I talk about this for 5 years without getting bored?" | **LIKELY, downgraded from implied-verified.** The general theme-durability instinct is attested (T9: "nut out your themes"), but this specific "5 years without getting bored" phrasing was not found in the retrieved transcript segment (118,576 chars, searched for "5 year," "bored" — zero direct hits on this exact framing). Not deleted (pre-existing, additive-first boundary) but flagged honestly rather than left as an implied-verified claim. |

## Explicitly non-factual content (U-series)

| Item | Content | Status |
|---|---|---|
| U1 | genius.md "Hall of Fame Exemplars" — "The Philosopher-Carpenter" and "The Reformed Corporate Strategist" — plus the "Anti-Exemplar: Generic Productivity Coach" | **Illustrative composites, not real people or real case studies.** Pre-existing content; not attributed to Mallett as documented clients or real creators. Labeled inline in genius.md as illustrative, not verified/factual claims about real individuals. |

## Absence checks (per envelope rule: verify before claiming "no source")

- `extractions/` — `ls extractions/ | grep -i mallet` returns **zero results**. No dedicated `extractions/erica-mallett*` or `extractions/erica-mallet*` directory exists. Confirmed absent, not assumed.
- `_active/codex-harvest-2026-06-11/` — **NOT absent.** Contains `agents/erica-mallet/AGENT.md` (8,285 bytes, read in full) and a near-duplicate `skills/erica-mallet-brand-magnetism/` mirror of the current skill (adds an unshipped "Pattern 16 / Tacit 16: Category Container" pair and a "category-of-one" workflow row not present in the live skill — out of scope for this repair pass since it targets different, non-failing content; noted in REPAIR-NOTES.md, not ported).
- `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) — **NOT absent, and load-bearing.** Content-grepped (not just filename-grepped): 252 lines matching "mallet" case-insensitive across the full extracted archive. 23 conversation files in `claude-export/normalized/conversations/` reference Erica Mallett by name, several of them full MES 3.0 extraction sessions from real YouTube transcripts of her videos (not just this one — also a nostalgia-marketing/"Memory Lane Rule" video and a "cult-like fans" cognitive-bias video, which were not pulled into this skill and are out of scope here). The raw JSON (`claude-export/raw/batch-0001/conversations.json`, 867,859,945 bytes) was targeted with `ijson` streaming (not a full load) to pull the single relevant conversation object by uuid; this is how the T-series verbatim transcript above was recovered.

## What this repair pass did NOT verify

- The RedCircle episode page (`redcircle.com/shows/.../ep/...`) returned HTTP 403 and was not used as a source.
- The two additional claude-export conversations about a "cult-like fans" cognitive-bias video and a "Memory Lane Rule" nostalgia-marketing video were located but not opened/quoted — they cover different Erica Mallett content than this skill's brand-magnetism scope and pulling them in would be scope creep beyond the six failing checks this pass targets.
- No attempt was made to verify the "52 prompts" count claimed in SKILL.md's original description, or the `crown_jewel_prompt_*` / `apex_*` / `writing_mastery_*` / `pop_culture_*` prompt files' fidelity to Mallett's actual teaching beyond the specific L1/L2 lines cited above — those files are pre-existing, unedited by this pass, and were graded PASS by the auditor's `workflow_contracts` check independently of this ledger.
