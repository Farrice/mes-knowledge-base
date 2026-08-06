#!/usr/bin/env python3
"""
notify.py — Push a short message to Farrice (Mac notification + optional phone).

Born 2026-08-06, God Agent delta move #4 ("channel delivery for briefs"): COS
digests, mission-run results, and event-listener activity should reach Farrice
away from the terminal — WITHOUT a resident bot (Jarvis Telegram lesson:
subprocess-on-cloud bots are fragile and decommissioned; this is fire-and-forget
API/local delivery only).

Channels (both $0):
  1. macOS notification via osascript — always on, zero config, Mac only.
  2. ntfy.sh push — reaches his PHONE. Opt-in: install the free ntfy app,
     subscribe to a private topic, put `NTFY_TOPIC=<topic>` in .env.
     No account needed. Topic names are the only secret — pick something
     unguessable (e.g. antigravity-frbpm-8k2n).

Usage:
    python3 execution/notify.py send "Title" "Body text"
    python3 execution/notify.py send "Title" "Body" --priority high
    python3 execution/notify.py test
"""

import argparse
import os
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _env_topic():
    env_path = os.path.join(ROOT, '.env')
    if os.path.exists(env_path):
        for line in open(env_path):
            line = line.strip()
            if line.startswith('NTFY_TOPIC='):
                return line.split('=', 1)[1].strip().strip('"\'')
    return os.environ.get('NTFY_TOPIC')


def mac_notify(title, body):
    try:
        script = f'display notification "{body[:200]}" with title "{title[:80]}"'
        subprocess.run(['osascript', '-e', script], capture_output=True, timeout=10)
        return True
    except Exception:
        return False


def ntfy_notify(title, body, priority='default'):
    topic = _env_topic()
    if not topic:
        return None  # not configured — silent, not an error
    try:
        req = urllib.request.Request(
            f'https://ntfy.sh/{topic}',
            data=body.encode('utf-8'),
            headers={'Title': title[:120], 'Priority': priority},
        )
        urllib.request.urlopen(req, timeout=10)
        return True
    except Exception:
        return False


def send(title, body, priority='default'):
    mac = mac_notify(title, body)
    phone = ntfy_notify(title, body, priority)
    return {'mac': mac, 'phone': phone if phone is not None else 'unconfigured'}


def main():
    p = argparse.ArgumentParser(description='Notify Farrice (Mac + optional ntfy phone push)')
    sub = p.add_subparsers(dest='command')
    ps = sub.add_parser('send')
    ps.add_argument('title')
    ps.add_argument('body')
    ps.add_argument('--priority', default='default', choices=['min', 'low', 'default', 'high', 'urgent'])
    sub.add_parser('test')
    args = p.parse_args()
    if args.command == 'send':
        print(send(args.title, args.body, args.priority))
    elif args.command == 'test':
        print(send('Antigravity test', 'Notification channel is live. Phone requires NTFY_TOPIC in .env.'))
    else:
        p.print_help()


if __name__ == '__main__':
    main()
