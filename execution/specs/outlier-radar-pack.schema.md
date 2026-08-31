# Outlier Radar — Signal Pack Contract (pack_version 2)

Produced by `execution/outlier_radar.py refresh --niche <slug>`.
Read from `.agent/outlier-radar/packs/<niche-slug>/latest.json` (dated copies sit beside it).
This is THE interface between the data spine and any consumer (skills, briefs, a future
`sandcastles_bridge.py` or `manual_csv` lane). Validate with `outlier_radar.validate_pack()`.

## Top level

| Field | Type | Meaning |
|---|---|---|
| `pack_version` | int | Contract version. Currently `2`. |
| `niche_slug` / `niche_label` | str | Which niche (from `.agent/outlier-radar/channels.json`). |
| `generated_at` | ISO-8601 UTC | When the pack was written. |
| `freshness_ttl_hours` | float | Stale after this (12). Consumers should re-run `refresh` past it. |
| `run_id` / `run_receipt_path` | str | Producing run + its receipt under `.agent/outlier-radar/receipts/`. |
| `status` | `"ok"` \| `"degraded"` | `degraded` = >50% of channel fetches failed this run. Data may be stale/partial; the receipt says why. |
| `coverage` | obj | Per platform: `"measured"` \| `"partial"` \| `"none"`. TikTok/IG are always `"none"` in this build — honest, in-pack. |
| `source_lanes` | list | Lanes present: `"ytdlp_public"` \| `"manual_csv"` \| `"owned_metrics"` \| `"sandcastles_mcp"`. This build emits only `ytdlp_public`. |
| `evidence_class` | enum | Highest-truth metric class in the pack: `PRIVATE_OUTCOME`, `OWNED_PROXY`, or `PUBLIC_PROXY`. The yt-dlp lane emits `PUBLIC_PROXY`; views do not prove demand or revenue. |
| `owned_corpus_size` | int \| null | Published first-party post count supplied at refresh. Null means the operator has not declared it. |
| `data_maturity_state` | enum | `UNDECLARED`, `COLD_START` (<10 owned posts), `HYBRID` (10–19), or `OWNED_LEARNING` (20+). |
| `channels` | list | Per-channel rows: `channel_id, handle, title, subscriber_count, median_vpd, fetch_status, last_refreshed_at`. |
| `ranked_videos` | list | Outlier records (below), sorted `outlier_score` desc, capped at 50. |
| `leaderboard.topics` | list | `{topic, score_sum, video_count, example_video_ids}` sorted by `score_sum`. |
| `leaderboard.formats` | list | `{hook_format, desire_template, avg_score, count, sample_hooks}` — clustered by the radar's `cluster_patterns`. |
| `watchlist_adds` | list | Video ids flagged above the winner line and enriched this run (cap 10). |
| `cost` | obj | `{usd, yt_dlp_requests}` — always `usd: 0.0` for the ytdlp lane. |
| `errors` | list | `{channel, stage, message}` per failure. Partial failure never raises; it lands here. |

## Outlier record (each `ranked_videos` entry)

`video_id, platform, channel_id, channel_handle, channel_title, url, title, published_at,
age_days, duration_s, views, views_per_day, channel_median_vpd, channel_video_count_sampled,
outlier_score, outlier_multiplier, winner_line_status, confidence, likes, comments,
velocity_vpd_7d, hook_text, format_hint, topic, transcript_path, first_seen_at,
last_refreshed_at, source_lane, evidence_class, cohort_role, engagement_rate,
signal_hygiene, rejection_reasons`

Semantics and nullability:

- `views_per_day` = `views / max(age_days, 2)`, effective age capped at 90d. Null when
  `published_at` is unknown (flat dumps carry only an approximate timestamp; rows missing
  it stay null and drop to `confidence: "low"`).
- `outlier_multiplier` = vpd / `channel_median_vpd`. Baseline is the channel's rolling
  median vpd over sampled videos when ≥5 are usable, else the niche-global median.
- `winner_line_status`: `above_winner_line` \| `study_but_not_winner` \| `below_winner_line`
  — thresholds via the radar's largest-drop logic (`winner_thresholds`).
- `confidence`: `high` (channel baseline + known date) / `medium` (global baseline) /
  `low` (no multiplier — missing views or date).
- `likes`, `comments`: null unless the video was enriched (flagged outliers only, cap 10/run).
- `engagement_rate`: `(likes + comments) / views` when enrichment supplied both counts; otherwise null.
- `signal_hygiene`: `PASS` at or above the source-backed 2% engagement floor, `REJECT` below it, or `REVIEW` when engagement is unavailable. `rejection_reasons` preserves the exact reason.
- `cohort_role`: producer default `UNCLASSIFIED`. A consumer or human must assign `TOPIC_COHORT`, `FORMAT_ONLY`, or `EXCLUDE`; the collector cannot infer niche and scale fit honestly.
- `evidence_class`: the yt-dlp producer emits `PUBLIC_PROXY` on every row.
- `velocity_vpd_7d`: null until the video has 2+ snapshots inside a 7-day window.
- `transcript_path`: null unless flagged + captions found; points into
  `.agent/outlier-radar/transcripts/<video_id>.txt`.
- `hook_text`: transcript opening (~200 chars) when a transcript exists, else the title.
- `platform` + `source_lane` ride on every record so future lanes (TikTok/IG via
  `sandcastles_mcp`, `manual_csv`) drop in behind the same contract unchanged.

## Interop

`outlier_radar.py emit-radar-rows --niche <slug> --out <path>` converts the latest pack to
rows JSON that `kallaway_trend_hook_radar.py --signals-json <path>` ingests directly
(`avg_views` there is a raw-view channel median, since the radar multiplies views/avg_views).
The emitted rows preserve `evidence_class`, `cohort_role`, `engagement_rate`,
`signal_hygiene`, `rejection_reasons`, `confidence`, and `outlier_multiplier`.

## Enrichment (optional, additive — `execution/pack_enrich.py`)

Manual-fire live-market enrichment writes ONE additive `enrichment` key onto the pack —
one data spine; every consumer (gb-* artifacts, the lead-magnet mini-report) inherits it.
No pack contract field above is touched; `validate_pack()` ignores the key. Producer flow:
`pack_enrich.py plan` → assistant research per `skills/growth-blueprint-os/workflows/gb-enrich.md`
(`/gb-enrich`) → `pack_enrich.py merge` (snapshots the pack to a dated sibling first).
Manual-fire only — never scheduled.

```
enrichment: {
  generated_at: ISO-8601 UTC,            # when the research was collected
  lanes_used: ["tavily" | "perplexity" | "research.py" | ...],
  cost_usd_est: float,                   # honest estimate, stated as estimate
  topics: [{                             # demand/freshness per leaderboard topic
    topic, demand_note,                  # demand_note is reader-grade language
    trend_direction: rising|flat|falling|unknown,
    sources: [{url, title}],             # >=1 required
    label: VERIFIED|LIKELY|UNCONFIRMED
  }],
  buyer_language: [{ quote, context, url, label }],   # sourced verbatim quotes (>=3 asked)
  market_pulse:  [{ note, url, label }]               # what changed last ~30d
}
```

Anti-fabrication is structural, enforced at merge: every entry carries ≥1 http(s) source
URL **and** a label, or it is dropped with a visible count; zero valid entries → nothing
is written. Consumers treat a pack without `enrichment` exactly as before (silent degrade).
