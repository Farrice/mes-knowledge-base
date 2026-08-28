import json

import yt_dlp

for handle in ["@kallawaymarketing", "@AlexHormozi", "@GaryVee"]:
    opts = {
        "quiet": True,
        "extract_flat": "in_playlist",
        "playlistend": 2,
        "skip_download": True,
        "extractor_args": {"youtubetab": {"approximate_date": [""]}},
        "no_warnings": True,
    }
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(f"https://www.youtube.com/{handle}/videos", download=False)
        entries = list(info.get("entries") or [])
        e0 = entries[0] if entries else {}
        print(
            handle,
            "| channel:", info.get("channel"),
            "| id:", info.get("channel_id"),
            "| followers:", info.get("channel_follower_count"),
        )
        print(
            "   first entry:",
            json.dumps(
                {k: e0.get(k) for k in ("id", "title", "view_count", "duration", "timestamp", "upload_date")},
                default=str,
            )[:300],
        )
        print("   non-null keys:", sorted(k for k in e0 if e0.get(k) is not None))
    except Exception as exc:
        print(handle, "FAILED:", type(exc).__name__, str(exc)[:200])
