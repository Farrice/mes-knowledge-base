# Provenance — daniel-thrasher-affiliate repair

Anchor → source file + location. Source file for all anchors below:
`_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/95bf31f8-08bc-421c-96f7-44d91a50833a.md`
(extract with `tar -xzf _archive/claude-export-2026-07-01.tar.gz -O claude-export/normalized/conversations/95bf31f8-08bc-421c-96f7-44d91a50833a.md`).
Line numbers below are lines of that extracted file, which mirrors the YouTube
transcript for "The Top 7 Affiliate Marketing Skills You'll Need in 2026 (In Order!)"
(https://www.youtube.com/watch?v=G8eJCr4-14c) at ~one line per caption chunk.

| Anchor (genius.md location) | Quote used | Source lines | Timestamp |
|---|---|---|---|
| Pattern: Three-Filter Offer Selection | "a three-part filter of demand, competition, and competency" | 66–70 | 1:09–1:14 |
| Pattern: Bridge Page as the Only Owned Lever | "you don't own the social media site unless your name is Mark Zuckerberg" | 402–406 | 11:59–12:04 |
| Pattern: Single-Channel Mastery Before Expansion | "I recently added Pinterest to my repertoire this year as a new source of organic traffic" | 579–583 | 17:37–17:42 |
| Pattern: Tracking-ID Granularity and North-Star Metrics | "your traffic source, your traffic type, your campaign, your creative, your ad" (truncated before garbled final field) | 667–673 | 20:24–20:27 |
| Pattern: Amplify, Don't Substitute | "I've used a no code automation tool called Make.com to create an automation for ClickBank's ongoing segments of top offers" | 958–964 | 29:32–29:39 |
| Insight: Your Competition Isn't Just Other Affiliates | "there are also both bigger brands and solo creators selling their own diet or weight loss products through these same channels" | 206–213 | 5:40–5:46 |
| Insight: One Channel Is a Single Point of Failure | "you have only one main traffic source, then your business is basically vulnerable to a single point of failure, like an account shutdown, an ad rejection, an algorithm change" | 824–829 | 25:15–25:23 |
| Anti-Pattern 1 (validate before chasing a mirage) | "it's a good idea to look at some numbers and validate before you go chasing a mirage" | 96–100 | 2:06–2:10 |
| Anti-Pattern 2 (competency mismatch) | "spirituality and manifestation which I have zero knowledge or experience in, I would have absolutely struggled to succeed" | 229–239 | 6:29–6:38 (quote spans 6:30–6:36) |
| Anti-Pattern 3 (bridge page overbuild) | "Don't make it complicated. There's only one action you want someone to take" + "no navigation menu, there's no sidebar, there's no pop-ups" | 429–441 | 12:51–13:11 |
| Anti-Pattern 4 (premature email layer) | "spreading yourself too thin between the main traffic channel you're trying to master, and trying to build up an email list, probably isn't the best idea" | 746–753 | 22:47–22:56 |
| Anti-Pattern 5 (AI/automation as shortcut) | "If you treat AI and automation as a shortcut, so you don't have to do the work, you'll likely end up disappointed by the results of your affiliate campaign" | 869–878 | 26:48–26:57 |
| Anti-Pattern 6 (unsupervised automation) | "I don't think we're at a point yet where you can set these tools completely free without any supervision" | 992–998 | 30:44–30:47 |

## Recognition-test language (for `recognition_test` check)

`## How to Use This Skill (Model Calibration)` section, genius.md, new content this
repair. Not a quote from Thrasher — an original calibration paragraph written for this
repair, modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7–16
per the envelope instruction, but built from this expert's own texture (evidence-first,
five-element bridge page, sequencing discipline) rather than copied.

## Discarded / excluded material (do not re-cite)

- `edf9bee0-194b-4aa6-8ff6-abd91ed7b968.md` (same archive) — "Crown Jewel" income
  projections ($50-200 RPV, $15K-30K/mo). Confirmed fabricated (no basis in the primary
  transcript) by re-reading the full file this session. Already correctly excluded by
  `agents/daniel-thrasher/memory/context.md`; this repair does not touch it.
- `video-context-ledger.md` (uf4fR3qcDkU) — false-positive filename match, unrelated
  content ("thrasher magazines," skateboarding). See `references/source-ledger.md`.
