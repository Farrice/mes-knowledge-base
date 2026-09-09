#!/usr/bin/env python3
"""Free source acquisition: public yt-dlp + native captions or local whisper.cpp.
No API clients, keys, installs, subscriptions, or global configuration writes.
Outputs source-package files; frame review is always a separate human/model step.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
from urllib.parse import urlparse
import re
import html

def clean_vtt(vtt):
    """Parse VTT cues, remove markup and collapse rolling caption overlap."""
    segments, previous = [], []
    stamp = r"(?:\d{2}:)?\d{2}:\d{2}[.,]\d{3}"
    def seconds(value):
        parts = value.replace(",", ".").split(":")
        return sum(float(x) * 60 ** i for i, x in enumerate(reversed(parts)))
    for block in re.split(r"\n\s*\n", vtt.strip()):
        match = re.search(r"(" + stamp + r")\s+-->\s+(" + stamp + r")[^\n]*\n(.*)", block, re.S)
        if not match:
            continue
        start, end = seconds(match[1]), seconds(match[2])
        words = html.unescape(re.sub(r"<[^>]+>", "", match[3])).split()
        overlap = 0
        for n in range(min(len(previous), len(words)), 0, -1):
            if previous[-n:] == words[:n]:
                overlap = n
                break
        fresh = " ".join(words[overlap:])
        previous = words
        if fresh and end > start:
            segments.append({"start_seconds": start, "end_seconds": end, "text": fresh})
    return "\n".join(f"[{int(s['start_seconds'])//60:02d}:{int(s['start_seconds'])%60:02d}] {s['text']}" for s in segments), segments



def run(cmd, log, timeout=180):
    """Kill the entire child process group on timeout; never inherit token retries."""
    with Path(log).open('w') as f:
        proc = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            return proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.wait()
            f.write('\nTIMEOUT: process group terminated\n')
            return 124


def ytdlp_args():
    return ['yt-dlp', '--ignore-config', '--no-plugin-dirs', '--no-playlist',
            '--socket-timeout', '15', '--retries', '0', '--extractor-retries', '0',
            '--fragment-retries', '0', '--no-progress',
            '--extractor-args', 'youtube:player_client=web_embedded']


def fingerprint(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def sample_times(duration, count, cues=()):
    if not math.isfinite(duration) or duration <= 0 or not 2 <= count <= 200:
        raise ValueError('positive finite duration and 2..200 frames required')
    if any(not math.isfinite(t) or not 0 <= t < duration for t in cues):
        raise ValueError('cue outside video')
    pinned = sorted(set(cues))
    if len(pinned) > count:
        raise ValueError('more cue frames than frame budget')
    uniform = [round(i * max(0, duration - 0.1) / (count - 1), 3) for i in range(count)]
    # Cues take precedence; include full-range coverage wherever capacity remains.
    selected = list(pinned)
    for index in [0, count - 1] + list(range(1, count - 1)):
        if len(selected) >= count:
            break
        t = uniform[index]
        if not any(abs(t - old) < .05 for old in selected):
            selected.append(t)
    return sorted(selected)


def coverage(segments, duration):
    if not segments:
        return {'status': 'missing', 'timeline_fraction': 0, 'gaps_over_30s': []}
    spans = sorted((max(0, s['start_seconds']), min(duration, s['end_seconds'])) for s in segments)
    end, covered, gaps = 0., 0., []
    for a, b in spans:
        if a - end > 30:
            gaps.append([round(end, 2), round(a, 2)])
        covered += max(0, b - max(a, end))
        end = max(end, b)
    if duration - end > 30:
        gaps.append([round(end, 2), round(duration, 2)])
    return {'status': 'captured_needs_accuracy_review',
            'timeline_fraction': round(covered / duration, 4),
            'first_seconds': spans[0][0], 'last_seconds': end, 'gaps_over_30s': gaps}


def acquire(args):
    out = Path(args.out_dir).expanduser().resolve()
    if out.exists() and any(out.iterdir()):
        raise ValueError('Output directory must be empty; preserves previous source identity and receipts')
    out.mkdir(parents=True, exist_ok=True)
    raw = out / 'raw'
    raw.mkdir()
    report = {'source': args.source, 'origin_url': args.origin_url,
              'started_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
              'paid_api_calls': 0, 'new_dependencies': 0, 'stages': [],
              'review_status': 'NOT_REVIEWED', 'status': 'FAILED'}
    def save():
        (out / 'acquisition.json').write_text(json.dumps(report, indent=2) + '\n')
    save()
    try:
        for binary in ('ffmpeg', 'ffprobe'):
            if not shutil.which(binary):
                raise RuntimeError(f'Missing existing dependency: {binary}; nothing installed')
        is_url = urlparse(args.source).scheme in ('https', 'http')
        subtitle = None
        metadata = {}
        if is_url:
            if not shutil.which('yt-dlp'):
                raise RuntimeError('yt-dlp unavailable')
            template = str(raw / 'video.%(ext)s')
            rc = run(ytdlp_args() + ['--skip-download', '--write-subs', '--write-auto-subs',
                     '--sub-langs', 'en-orig,en', '--sub-format', 'vtt', '-o', template, '--', args.source],
                     out / 'captions.log', 120)
            report['stages'].append({'captions_exit': rc})
            candidates = sorted(raw.glob('*.vtt'))
            subtitle = next((p for p in candidates if p.stat().st_size > 50), None)
            rc = run(ytdlp_args() + ['--write-info-json', '-f', 'bv*[height<=720]+ba/b[height<=720]',
                     '--merge-output-format', 'mp4', '-o', template, '--', args.source],
                     out / 'download.log', args.download_timeout)
            report['stages'].append({'download_exit': rc})
            media = raw / 'video.mp4'
            if rc or not media.exists():
                raise RuntimeError(f'Video acquisition failed ({rc}); inspect download.log')
            metadata = json.loads((raw / 'video.info.json').read_text())
        else:
            media = Path(args.source).expanduser().resolve()
            if not media.is_file():
                raise ValueError('Local source does not exist')
        probe = subprocess.run(['ffprobe', '-v', 'error', '-show_format', '-show_streams',
                                '-of', 'json', str(media)], capture_output=True, text=True, timeout=30)
        if probe.returncode:
            raise ValueError('Media probe failed')
        details = json.loads(probe.stdout)
        duration = float(details['format']['duration'])
        if not any(s['codec_type'] == 'video' for s in details['streams']):
            raise ValueError('No video stream')
        report.update({'duration_seconds': duration, 'media_path': str(media),
                       'media_sha256': fingerprint(media)})
        (out / 'metadata.json').write_text(json.dumps({k: metadata.get(k) for k in
                  ('id','title','channel','uploader','upload_date','duration','webpage_url','description')}, indent=2)+'\n')
        text, segments = ('', [])
        if subtitle:
            text, segments = clean_vtt(subtitle.read_text())
        if segments:
            shutil.copyfile(subtitle, out / 'transcript.vtt')
            report['transcript_source'] = 'native_captions'
        else:
            model = Path(args.model).expanduser()
            if not shutil.which('whisper-cli') or not model.is_file():
                raise RuntimeError('Native captions unavailable and local whisper-cli/model missing; no paid fallback')
            audio = raw / 'audio.wav'
            rc = run(['ffmpeg', '-v', 'error', '-y', '-i', str(media), '-vn', '-ac', '1', '-ar',
                      '16000', '-c:a', 'pcm_s16le', str(audio)], out/'audio.log', 180)
            if rc:
                raise RuntimeError('Audio conversion failed')
            # CPU mode works inside sandboxed shells without requiring Metal privileges.
            rc = run(['whisper-cli', '-ng', '-m', str(model), '-f', str(audio), '-oj', '-ovtt',
                      '-otxt', '-of', str(out/'local-transcript'), '-np'], out/'transcription.log', args.transcribe_timeout)
            report['stages'].append({'local_transcription_exit': rc})
            if rc or not (out/'local-transcript.vtt').exists():
                raise RuntimeError(f'Local transcription failed ({rc})')
            shutil.copyfile(out/'local-transcript.vtt', out/'transcript.vtt')
            text, segments = clean_vtt((out/'transcript.vtt').read_text())
            report.update({'transcript_source': 'local_whisper_cpp', 'model_path': str(model),
                           'model_sha256': fingerprint(model), 'audio_processed_range': [0, duration]})
        (out/'transcript.txt').write_text(text+'\n')
        (out/'transcript_segments.json').write_text(json.dumps(segments, indent=2)+'\n')
        if not segments:
            raise RuntimeError('Empty transcript; cannot claim source captured')
        report['transcript_coverage'] = coverage(segments, duration)
        frame_dir = out / 'frames'
        frame_dir.mkdir()
        frames = []
        for t in sample_times(duration, args.frames, args.timestamps):
            target = frame_dir/f'{t:09.3f}.jpg'
            rc = run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', str(media),
                      '-frames:v', '1', '-vf', 'scale=960:-2', str(target)], out/'frame-last.log', 30)
            if rc or not target.exists():
                raise RuntimeError(f'Frame extraction failed at {t}')
            frames.append({'seconds': t, 'path': str(target.relative_to(out)),
                           'reason': 'transcript-cue' if t in args.timestamps else 'uniform',
                           'reviewed': False})
        (out/'frames.json').write_text(json.dumps(frames, indent=2)+'\n')
        report.update({'frames_extracted': len(frames), 'frames_reviewed': 0,
                       'status': 'CAPTURED_REVIEW_REQUIRED',
                       'limits': ['ASR/captions can contain errors; timeline coverage is not accuracy.',
                                  'Sparse frames can miss brief visuals; inspect cue frames before visual claims.',
                                  'Public source availability is not guaranteed; no access-control bypass.']})
        save()
        return report
    except Exception as exc:
        report['error'] = str(exc)
        save()
        raise


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source')
    p.add_argument('--out-dir', required=True)
    p.add_argument('--origin-url', default=None, help='Provenance for a user-supplied local source; not independently verified')
    p.add_argument('--model', default='~/.cache/whisper-cpp/ggml-base.en.bin')
    p.add_argument('--frames', type=int, default=40)
    p.add_argument('--timestamps', type=float, nargs='*', default=[])
    p.add_argument('--download-timeout', type=int, default=300)
    p.add_argument('--transcribe-timeout', type=int, default=1800)
    args = p.parse_args()
    try:
        print(json.dumps(acquire(args), indent=2))
    except Exception as exc:
        print(f'FAILED: {exc}', file=sys.stderr)
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
