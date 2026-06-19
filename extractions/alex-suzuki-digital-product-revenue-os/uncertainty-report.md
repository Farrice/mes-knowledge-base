# Uncertainty Report

## Verified Locally
- The two videos were fetched with `yt-dlp` metadata and auto captions.
- Auto-caption files, cleaned transcripts, and timestamped segment JSON files exist under `sources/`.
- Both videos are from the Alex Suzuki YouTube channel metadata captured locally.
- The source package keeps each video in its own folder.

## Source-Backed But Not Independently Verified
- The post and funnel mechanics are source-backed by captions.
- Claims about sales amounts, application counts, call counts, close rates, and cash collected are creator claims.
- Claims about X algorithm behavior are treated as practitioner claims, not platform-confirmed rules.

## Not Available
- Manual subtitles were not found in the captured package.
- Visual context was skipped because both videos exceed the local 600-second cap.
- No independent payment processor, analytics, Stripe, X account, or platform data was checked.

## Required Safety Language
Use this note in deliverables when discussing results:

> Revenue figures are creator claims from the source videos. This system extracts the operating method and proof standards; it does not promise matching results.

## Third Source Slot
Add the third video by creating:

```text
extractions/alex-suzuki-digital-product-revenue-os/sources/<video_id>/
```

Then add auto captions, `metadata-summary.json`, `transcript.txt`, `transcript_segments.json`, and timestamp ledger entries. Only change the skill architecture if the third source adds a new capability that the current workflow set cannot express.
