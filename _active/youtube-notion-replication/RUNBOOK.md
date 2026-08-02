# Runbook: Ingest the Source Video + Test the New Glue

For Farrice, on the Mac (not cloud) — this cloud session confirmed YouTube hard-blocks datacenter IPs, so video ingestion has to run where yt-dlp/ffmpeg/the claude-video plugin/`.env` actually live. Everything below is copy-pasteable, one command per line.

## 1. Ingest this video

Two commands. Run from the repo root once you're home.

```bash
python3 execution/fetch-transcript.py "https://youtu.be/gOx37on-iA8" "source"
```
Free, no key needed (`youtube-transcript-api`). Writes the transcript to `extractions/source/<video_id>.txt`. If this fails, YouTube likely changed its caption delivery again — check for a library update before assuming the video has no captions.

```bash
python3 execution/fetch-video-context.py "https://youtu.be/gOx37on-iA8" "source" --max-duration 3600
```
Pulls the video via yt-dlp, extracts frames, and writes `extractions/source/visual-context.md` plus `extractions/source/frames/`. The `--max-duration 3600` override is needed because the default skip threshold is 600s (10 min) — bump it further if the video runs longer than an hour. Exit code 2 means it was skipped (non-video source, or plugin missing); exit code 1 means a real failure (missing dep, network, plugin error).

**Then pick one:**

- **Run `/extract` locally** against `extractions/source/` to produce the full expert/pattern extraction, or
- **Commit `extractions/source/` to this branch** (`claude/youtube-notion-integration-analysis-ubiusy`) and push, then tell the cloud session to proceed — it can pick up the transcript and visual-context files from there without needing to touch YouTube itself.

## 2. Prereq check (run this first if step 1 fails)

```bash
command -v yt-dlp ffmpeg ffprobe && pip show youtube-transcript-api
```
All four should resolve. If any is missing:

```bash
brew install ffmpeg yt-dlp
```
```bash
pip install youtube-transcript-api
```

For the claude-video plugin itself (what `fetch-video-context.py` wraps):

```bash
/plugin marketplace add bradautomates/claude-video
```
If that plugin isn't installed, `fetch-video-context.py` exits 2 (skipped, no plugin) rather than failing loud — check its stdout for the specific reason before assuming it's a network issue.

## 3. Test the new glue (after pulling this branch)

`execution/social_to_notion.py` just landed on this branch — it's the URL-to-Notion-page script that chains the scrapers into the Notion writer. Test it in this order.

**Dry run first — no Notion write, prints the normalized record + payload as JSON:**
```bash
python3 execution/social_to_notion.py "https://youtu.be/gOx37on-iA8" --dry-run --transcript-file extractions/source/<video_id>.txt
```
Swap in the actual filename from step 1's output. `--transcript-file` injects the transcript from disk so this is testable fully offline — no Apify calls happen when a transcript file is supplied for a YouTube URL.

**Live run against Captures — the safe target, not Content Pipeline or Knowledge Vault:**
```bash
python3 execution/social_to_notion.py "https://youtu.be/gOx37on-iA8" --db captures --transcript-file extractions/source/<video_id>.txt
```
This actually writes a Notion page. Captures is the right first target because it's the low-stakes inbox database — nothing downstream treats a Captures entry as authoritative the way it would a Knowledge Vault entry.

**Then check the page in Notion** — confirm the transcript landed in full, the embed resolves, and the source ledger block shows what was fetched and what (if anything) degraded. If a field is missing, check the script's stdout first — it logs every degradation explicitly rather than failing silently.

If you try a TikTok or Instagram URL instead, expect Apify calls to fire (capped at 3 per invocation by the script's own local counter, on top of `apify_client.py`'s existing $/month guard) — don't be surprised by ledger activity in `.agent/apify-usage.json` after a live run. A LinkedIn URL will exit 2 immediately — that's expected, not a bug (see `FULL-PICTURE.md § LinkedIn gap`).

## 4. Optional: GROQ_API_KEY

Not required for anything above. This only matters if you hit a video with no native captions and want Whisper transcription as a fallback (`fetch-video-context.py --whisper`). Free tier exists on Groq's side. If you decide you want it:

```bash
echo "GROQ_API_KEY=your_key_here" >> .env
```

One thing to know before flipping this on: the Whisper/Groq call path isn't currently in `execution/hooks/cost_gate_hook.py`'s paid-pattern list, so usage past Groq's free tier wouldn't be caught by the cost gate today. That's flagged as a system-hardening TODO in `FULL-PICTURE.md`, not a blocker — just don't assume the gate is watching this one yet. The core transcript + Notion loop above needs zero new keys.
