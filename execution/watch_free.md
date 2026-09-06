# Free video acquisition fallback

For when `/watch` cannot acquire a public video. This preserves existing watch; it does not edit its global installation. No API keys, paid services, new dependencies or model downloads. Uses installed yt-dlp, ffmpeg/ffprobe and optional whisper.cpp with an existing local model.

```bash
python3 execution/watch_free.py 'https://www.youtube.com/watch?v=MqjmPknAvuw' --out-dir /private/tmp/new-source-capture
python3 execution/watch_free.py /absolute/path/video.mp4 --out-dir /private/tmp/local-source-capture --frames 40 --timestamps 515 895 1158
python3 execution/test_watch_free.py
```

Output directory must be empty. This prevents one video's stale files from becoming another video's evidence. Reuse an existing completed package by reading it; create a new directory for a deliberate rerun.

The tool tries English captions, then obtains video independently so a caption failure cannot cancel a valid video download. It ignores personal yt-dlp configuration/plugins, uses bounded deadlines and zero automatic extractor retries, and falls back to local CPU transcription only if captions are absent. A download requiring login/region access cannot be guaranteed; errors are preserved rather than hidden.

`--model` selects an already downloaded model; no automatic installation. `--transcribe-timeout` defaults to 1800 seconds. `--frames` defaults to 40, bounded to 200; cue timestamps reserve capacity. Full-video uniform samples may miss brief visuals. Use an existing watch scene pass or targeted local frames when the transcript references an on-screen detail.

Read `acquisition.json`, `transcript.txt`, `transcript_segments.json` and every frame listed in `frames.json`. Only then write a separate review record; the tool deliberately returns CAPTURED_REVIEW_REQUIRED. Temporal coverage is not ASR accuracy. Keep native captions when available; offline recognition can mishear names and numbers.

Proof: `extractions/video-context/MqjmPknAvuw/validation-receipt.md`. Upstream tools: [yt-dlp](https://github.com/yt-dlp/yt-dlp), [whisper.cpp](https://github.com/ggml-org/whisper.cpp). These are already installed here. No promise of support for every public video or arbitrary future upstream changes.
