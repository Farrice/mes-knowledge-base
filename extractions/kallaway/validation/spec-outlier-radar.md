# Spec — outlier_radar.py (data spine, Phase 3)

Approved via Checkpoint 1 (2026-08-27). Design source: architecture pass, this session. Constraint: EXTEND-NEVER-REBUILD; no Apify anywhere; deterministic Python in execution/; visible degradation, never silent.

## Module: `execution/outlier_radar.py` (new sibling)

Imports as a library from `execution/kallaway_trend_hook_radar.py`: `compute_group_baselines`, `winner_thresholds`, `hook_format`, `desire_template`, `cluster_patterns` (verify exact names on read; adapt import list to what exists — the scorer/clustering math is the reuse target). Reuses the caption path from `execution/social_intel.py` (`fetch_yt_transcript_ytdlp` + `_vtt_to_text` — import or minimally vendor with attribution comment if import coupling is unclean).

### Fetch (yt-dlp, two-stage, $0, keyless)
- Stage 1 flat dump per channel: `yt-dlp --flat-playlist --skip-download` JSON, `--playlist-end 30`, `--extractor-args "youtubetab:approximate_date"`, URL form `https://www.youtube.com/@{handle}/videos`. Fields: id, title, view_count, duration, approximate upload_date. Run under `.venv/bin/python3 -m yt_dlp` or the yt_dlp python API (prefer API).
- Stage 2 enrich ONLY flagged outliers (cap 10/run): full metadata + captions → `.agent/outlier-radar/transcripts/<video_id>.txt`.
- Politeness: 3–8s jittered sleep between channels; `sleep_requests=1`; cap 12 channels/run, 30 videos/channel; one retry w/ exponential backoff on 429/403; NO cookies ever.
- Per-channel TTL 12h (skip fresh channels on re-run). Snapshots record view deltas per run → `velocity_vpd_7d` after 2+ runs.
- Degradation: >50% channel failures → pack `status:"degraded"` + receipt note ("pip install -U yt-dlp"); log to `.agent/health/degradations.jsonl` if that pattern is importable; never raise to the caller for partial failure.

### Scoring
`views_per_day = views / max(age_days, 2)`, effective age capped at 90d. `outlier_multiplier = vpd / channel_median_vpd` (rolling median over sampled videos; min 5 videos else niche-global median). Winner line via radar's `winner_thresholds` largest-drop logic. Confidence field reflects sample size.

### Storage — `.agent/outlier-radar/`
- `radar.db` SQLite: tables `channels(channel_id, handle, title, subscriber_count, median_vpd, last_refreshed_at, fetch_status)`, `videos(video_id, channel_id, platform, url, title, published_at, duration_s, first_seen_at, last_refreshed_at, source_lane)`, `snapshots(video_id, run_id, views, captured_at)`, `runs(run_id, niche_slug, started_at, finished_at, status, cost_usd, requests)`
- `channels.json`: `{ "<niche-slug>": { "label": str, "seeds": ["@handle", ...] } }`
- `receipts/<run_id>.json` (RunReceipt pattern mirroring the radar's)
- `packs/<niche-slug>/latest.json` + dated copy `<YYYY-MM-DD>.json`

### Signal-pack contract (THE interface — exact fields)
```
pack_version, niche_slug, niche_label, generated_at, freshness_ttl_hours,
run_id, run_receipt_path, status ("ok"|"degraded"),
coverage {youtube, tiktok, instagram: "measured"|"partial"|"none"},
source_lanes ["ytdlp_public"|"manual_csv"|"owned_metrics"|"sandcastles_mcp"],
channels [...per-channel rows...],
ranked_videos [outlier records, score desc, cap 50],
leaderboard { topics[{topic, score_sum, video_count, example_video_ids}],
              formats[{hook_format, desire_template, avg_score, count, sample_hooks}] },
watchlist_adds [video_id...], cost {usd, yt_dlp_requests}, errors [{channel, stage, message}]
```
Outlier record: `video_id, platform, channel_id, channel_handle, channel_title, url, title, published_at, age_days, duration_s, views, views_per_day, channel_median_vpd, channel_video_count_sampled, outlier_score, outlier_multiplier, winner_line_status, confidence, likes(null ok), comments(null ok), velocity_vpd_7d(null until 2+ snapshots), hook_text, format_hint, topic, transcript_path(null unless flagged+captions), first_seen_at, last_refreshed_at, source_lane`.
TikTok/IG: always `coverage: "none"` this build — honest, in-pack. `platform` + `source_lane` on every record so a future `sandcastles_bridge.py` or manual_csv lane drops in behind the same contract.

### CLI
`refresh --niche <slug>` (fetch+score+pack), `pack --niche <slug>` (print latest pack path/summary), `add-channels --niche <slug> @h1 @h2`, `emit-radar-rows --niche <slug> --out <path>` (radar-compatible rows JSON for `kallaway_trend_hook_radar.py --signals-json` interop), `status` (freshness per niche). All commands print a one-line receipt.

## Verification (must pass before done)
1. Seed a test niche with 3 channels (use `@kallawaymarketing` + 2 real adjacent creator channels). Run `refresh` twice: 2nd run TTL-skips fresh channels; receipts exist; snapshots grow.
2. `emit-radar-rows` output feeds `kallaway_trend_hook_radar.py --signals-json` without error and produces clustering.
3. Transcripts exist only for flagged outliers, count ≤ cap.
4. Pack validates against the field list above (write a tiny `validate_pack()` used in tests and at pack-write time).
5. No network call paths import or reference apify_client.

Cost: $0. No new dashboards; a later single row in homebase_board.py is a separate step.
