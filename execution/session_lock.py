#!/usr/bin/env python3
"""Session lock — one driver per tree, as a mechanism (orchestration doctrine Law 5).

A long autonomous run (wave loops, fleets, backfills) claims the lock with a
heartbeat. Other sessions' machinery refuses to start wave-building while a
FRESH foreign lock exists. Stale locks (no heartbeat for TTL) are claimable —
a crashed session never bricks the tree.

Usage:
  python3 execution/session_lock.py claim "<mission>"     # claim or renew (prints token)
  python3 execution/session_lock.py heartbeat <token>     # renew (call between waves)
  python3 execution/session_lock.py check [<token>]       # exit 0 = clear to run / own lock
  python3 execution/session_lock.py release <token>
  python3 execution/session_lock.py status
"""
import json
import os
import sys
import time
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SESSION_LOCK_PATH override exists for test isolation ONLY (verify_mission_runner
# fixtures were 5/5-or-0/5 depending on the live tree's lock state, 2026-07-18) —
# never set it in production runs.
LOCK = os.environ.get("SESSION_LOCK_PATH") or os.path.join(ROOT, ".agent", "session.lock")
TTL = 45 * 60  # heartbeat older than this = stale, claimable


def read():
    try:
        return json.load(open(LOCK))
    except (OSError, ValueError):
        return None


def fresh(d):
    return d and (time.time() - d.get("heartbeat", 0)) < TTL


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    arg = sys.argv[2] if len(sys.argv) > 2 else None
    d = read()

    if cmd == "claim":
        if fresh(d):
            print(f"BLOCKED: fresh lock held by another session — mission '{d['mission']}' "
                  f"(heartbeat {int(time.time() - d['heartbeat'])}s ago). "
                  "One driver per tree; wait or coordinate with Farrice.")
            sys.exit(1)
        token = uuid.uuid4().hex[:12]
        json.dump({"token": token, "mission": arg or "unnamed", "claimed": time.time(),
                   "heartbeat": time.time(), "pid": os.getpid()}, open(LOCK, "w"))
        print(f"claimed: {token}  (heartbeat every wave: session_lock.py heartbeat {token})")
    elif cmd == "heartbeat":
        if not d or d.get("token") != arg:
            print("ERROR: lock not held by this token (claim first)")
            sys.exit(1)
        d["heartbeat"] = time.time()
        json.dump(d, open(LOCK, "w"))
        print("heartbeat ok")
    elif cmd == "check":
        if not fresh(d) or (arg and d.get("token") == arg):
            print("clear")
            sys.exit(0)
        print(f"BLOCKED: fresh foreign lock — mission '{d['mission']}' "
              f"(heartbeat {int(time.time() - d['heartbeat'])}s ago)")
        sys.exit(1)
    elif cmd == "release":
        if d and d.get("token") == arg:
            os.remove(LOCK)
            print("released")
        else:
            print("ERROR: lock not held by this token")
            sys.exit(1)
    else:
        if not d:
            print("no lock")
        else:
            age = int(time.time() - d["heartbeat"])
            print(f"{'FRESH' if fresh(d) else 'STALE'}: '{d['mission']}' token={d['token']} heartbeat {age}s ago")


if __name__ == "__main__":
    main()
