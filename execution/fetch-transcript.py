#!/usr/bin/env python3
"""
fetch-transcript.py — YouTube Transcript Fetcher for Antigravity Extractions

Usage:
    python3 execution/fetch-transcript.py <youtube_url_or_id> [expert_name]

Examples:
    python3 execution/fetch-transcript.py "https://www.youtube.com/watch?v=abc123" "sabrina-ramonov"
    python3 execution/fetch-transcript.py abc123 "april-dunford"
    python3 execution/fetch-transcript.py "https://youtu.be/abc123"

If expert_name is provided, saves to extractions/<expert_name>/transcript.txt
If not provided, saves to extractions/transcripts/<video_id>.txt

Requires: pip install youtube-transcript-api
"""

import sys
import os
import re
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("ERROR: youtube-transcript-api not installed.")
    print("Run: pip install youtube-transcript-api")
    sys.exit(1)


def extract_video_id(url_or_id: str) -> str:
    """Extract YouTube video ID from various URL formats or bare ID."""
    # Already a bare video ID (11 chars, alphanumeric + dash/underscore)
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id

    # Standard youtube.com/watch?v= format
    match = re.search(r'[?&]v=([a-zA-Z0-9_-]{11})', url_or_id)
    if match:
        return match.group(1)

    # Short youtu.be/ format
    match = re.search(r'youtu\.be/([a-zA-Z0-9_-]{11})', url_or_id)
    if match:
        return match.group(1)

    # youtube.com/embed/ format
    match = re.search(r'youtube\.com/embed/([a-zA-Z0-9_-]{11})', url_or_id)
    if match:
        return match.group(1)

    # youtube.com/v/ format
    match = re.search(r'youtube\.com/v/([a-zA-Z0-9_-]{11})', url_or_id)
    if match:
        return match.group(1)

    raise ValueError(f"Could not extract video ID from: {url_or_id}")


def fetch_transcript(video_id: str) -> str:
    """Fetch transcript for a YouTube video. Compatible with youtube-transcript-api v1.2.x (instance-based API)."""
    ytt_api = YouTubeTranscriptApi()

    try:
        # v1.2.x API: use instance.list() to get available transcripts
        transcript_list = ytt_api.list(video_id)

        # Try to find English transcript (manual first, then auto-generated)
        target_transcript = None
        for t in transcript_list:
            if t.language_code == 'en' and not t.is_generated:
                target_transcript = t
                break
        if target_transcript is None:
            for t in transcript_list:
                if t.language_code == 'en':
                    target_transcript = t
                    break
        if target_transcript is None:
            # Take whatever's available
            for t in transcript_list:
                target_transcript = t
                break

        if target_transcript is None:
            raise RuntimeError("No transcripts available for this video")

        snippets = target_transcript.fetch()
        full_text = ' '.join(snippet.text for snippet in snippets)
        return full_text

    except Exception as e:
        # Fallback: try the simple .fetch() API directly
        try:
            snippets = ytt_api.fetch(video_id)
            full_text = ' '.join(snippet.text for snippet in snippets)
            return full_text
        except Exception as e2:
            raise RuntimeError(f"Failed to fetch transcript: {e2}")


def save_transcript(text: str, video_id: str, expert_name: str = None) -> str:
    """Save transcript to the appropriate location. Returns the file path."""
    # Determine base directory (project root)
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent

    if expert_name:
        output_dir = project_root / "extractions" / expert_name
        filename = "transcript.txt"
    else:
        output_dir = project_root / "extractions" / "transcripts"
        filename = f"{video_id}.txt"

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    # If file already exists, create a numbered version
    if output_path.exists() and not expert_name:
        counter = 1
        while output_path.exists():
            output_path = output_dir / f"{video_id}_{counter}.txt"
            counter += 1

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    return str(output_path)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    url_or_id = sys.argv[1]
    expert_name = sys.argv[2] if len(sys.argv) > 2 else None

    # Extract video ID
    try:
        video_id = extract_video_id(url_or_id)
        print(f"Video ID: {video_id}")
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    # Fetch transcript
    print("Fetching transcript...")
    try:
        transcript = fetch_transcript(video_id)
    except RuntimeError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    # Stats
    word_count = len(transcript.split())
    char_count = len(transcript)
    print(f"Transcript fetched: {word_count:,} words ({char_count:,} characters)")

    # Save
    output_path = save_transcript(transcript, video_id, expert_name)
    print(f"Saved to: {output_path}")

    return output_path


if __name__ == "__main__":
    main()
