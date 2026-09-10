# Ingestion edges — every input Poppy takes, tried once (2026-09-10)

| Input | Result | Time | Path | Cost |
|---|---|---|---|---|
| YouTube video (captions on) | PASS | 1–11 s | youtube-transcript-api + oEmbed title | free |
| YouTube video (captions off) | not hit in tests; falls to yt-dlp download → whisper.cpp | minutes | watch_free.py | free |
| YouTube channel → latest N videos | PASS | 1 s | `yt-dlp --flat-playlist` with views + duration | free |
| TikTok profile → latest N videos | PASS | 1 s | `yt-dlp --flat-playlist` with views + duration | free |
| TikTok single video → transcript | FAIL | — | yt-dlp 2026.08.19 + curl_cffi: "Requested format is not available" | vendor: vidIQ `watch_shortform_content` (credits) |
| Instagram profile → reels | FAIL via yt-dlp ("Unsupported URL") · PASS via vidIQ | 3 s | `vidiq_ig_profile_reels` returns 12 reels with plays/likes/captions/covers | 5 vidIQ credits |
| Instagram single reel → transcript | FAIL | — | yt-dlp: "Requested format is not available" (login-walled) | vendor: vidIQ watch (credits) |
| PDF (local or https) | PASS | 1 s | pypdf; https via requests | free |
| Article URL | PASS | 1.3 s | trafilatura | free |
| Voice note (.m4a/.mp3/.wav) | PASS | 2.5 s | ffmpeg → whisper.cpp base.en, local | free |
| Local video file | PASS (existing watch_free path) | minutes | ffmpeg + whisper.cpp | free |
| Pasted text | PASS | 0 s | passthrough | free |
| Image node | NOT BUILT | — | would be a Claude vision call | on plan |
| LinkedIn post / profile | NOT BUILT | — | no vendor since Apify retired | — |

What Poppy does that we can't do free: read a TikTok or Instagram video's words.
Both are login-walled for scrapers. The honest options are vidIQ credits (already
connected, 1,607 in the balance) or his own browser cookies handed to yt-dlp
(`--cookies-from-browser chrome`), which is his call, not mine.
