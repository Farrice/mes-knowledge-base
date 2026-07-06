#!/usr/bin/env python3
"""
Backfill human-readable BODY blocks onto existing Knowledge Vault entries.

Context: every entry written by the pre-2026-07-06 `create_knowledge_vault_entry`
had its full content packed into the page TITLE + database properties, with an
EMPTY page body. Farrice reviews these pages manually and the giant run-on
titles with nothing underneath are unreadable. `notion_api.py` now writes rich
bodies going forward; this script retrofits the existing backlog.

Best-effort reconstruction: the only surviving "what was produced" text for a
pre-upgrade row IS its (already-truncated, up to ~100 char) title, plus
whatever landed in Key Patterns (which held the finalize --notes text,
truncated to 200 chars) and the other properties. There is no way to recover
the ORIGINAL full output_description — it was never stored anywhere else. The
reconstructed body is honestly partial and is labeled as such.

Usage:
    python3 execution/notion_backfill_knowledge.py --limit 60
    python3 execution/notion_backfill_knowledge.py --limit 60 --dry-run
"""

import argparse
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from notion_api import NotionAPI, NotionAPIError, build_vault_body_blocks, _short_title  # noqa: E402

VAULT_DB_ID = '5c63b25c-e040-4c6f-8a7b-906643090694'
RATE_LIMIT_SECONDS = 0.4

_SOURCE_WORKFLOW_RE = re.compile(r'chain_runner finalize \(([^)]*)\)')


def _plain(prop: dict, kind: str):
    """Extract plain text/number/select-name from a Notion property value."""
    if not prop:
        return None
    if kind == 'rich_text':
        runs = prop.get('rich_text', [])
        return ''.join(r.get('plain_text', '') for r in runs) or None
    if kind == 'title':
        runs = prop.get('title', [])
        return ''.join(r.get('plain_text', '') for r in runs) or None
    if kind == 'number':
        return prop.get('number')
    if kind == 'select':
        sel = prop.get('select')
        return sel.get('name') if sel else None
    if kind == 'date':
        d = prop.get('date')
        return d.get('start') if d else None
    return None


def _fetch_all_entries(api: NotionAPI, db_id: str) -> list:
    results, cursor = [], None
    while True:
        body = {'page_size': 100}
        if cursor:
            body['start_cursor'] = cursor
        r = api._request('POST', f'/databases/{db_id}/query', body)
        results.extend(r.get('results', []))
        if not r.get('has_more'):
            break
        cursor = r.get('next_cursor')
    return results


def _has_empty_body(api: NotionAPI, page_id: str) -> bool:
    r = api._request('GET', f'/blocks/{page_id}/children')
    return len(r.get('results', [])) == 0


def reconstruct_and_backfill(api: NotionAPI, page: dict, dry_run: bool = False) -> dict:
    props = page.get('properties', {})
    old_title = _plain(props.get('Name'), 'title') or 'Untitled'
    source = _plain(props.get('Source'), 'rich_text') or ''
    expert = _plain(props.get('Expert'), 'rich_text') or ''
    domain = _plain(props.get('Domain'), 'rich_text') or ''
    key_patterns = _plain(props.get('Key Patterns'), 'rich_text') or ''
    genius_score = _plain(props.get('Genius Score'), 'number')
    entry_type = _plain(props.get('Type'), 'select') or ''
    date_extracted = _plain(props.get('Date Extracted'), 'date') or ''
    skill = _plain(props.get('Antigravity Skill'), 'rich_text') or ''

    m = _SOURCE_WORKFLOW_RE.search(source)
    workflow = m.group(1) if m else ''

    # genius_score = min(5, max(2, int(composite/2))) at write time — this is
    # a lossy, approximate inverse. Labeled as approximate in the body.
    approx_composite = genius_score * 2 if genius_score is not None else None

    new_title = _short_title(old_title)

    notes_text = key_patterns
    if key_patterns:
        notes_text += ' (truncated at original write time — Key Patterns held the first 200 chars of finalize --notes)'

    score_note = ''
    if approx_composite is not None:
        score_note = f"Composite (approximate, back-derived from Genius Score {genius_score}): ~{approx_composite}/10 — sub-dimension scores were not stored separately, so this is a reconstruction, not the original value."

    children = build_vault_body_blocks(
        old_title,
        composite_score=None,  # avoid double-printing; approx note goes in Notes-adjacent line below
        expert=expert, skill=skill, workflow=workflow,
        entry_type=entry_type, task_type='', sub_agents=None,
        session_date=date_extracted, notes=notes_text,
    )
    # Insert the reconstruction caveat + approx composite right after "What
    # was produced" so it's the first thing a reader sees, not buried.
    caveat = NotionAPI.para(
        "[Backfilled 2026-07 from properties only — the original full "
        "summary was never stored separately from this title, so this page "
        "shows the pre-upgrade title text as the summary.]"
        + (f" {score_note}" if score_note else '')
    )
    children.insert(1, caveat)

    result = {
        'page_id': page['id'],
        'old_title': old_title[:100],
        'new_title': new_title,
        'workflow': workflow,
        'expert': expert,
    }

    if dry_run:
        result['action'] = 'dry-run'
        return result

    try:
        api._request('PATCH', f"/blocks/{page['id']}/children", {'children': children})
        api.update_page(page['id'], {'Name': api.title(new_title)})
        result['action'] = 'backfilled'
    except NotionAPIError as e:
        result['action'] = 'error'
        result['error'] = f'[{e.status}] {e.code} — {e}'

    return result


def main():
    ap = argparse.ArgumentParser(description='Backfill empty Knowledge Vault page bodies')
    ap.add_argument('--limit', type=int, default=60, help='Max entries to backfill this run (default 60)')
    ap.add_argument('--dry-run', action='store_true', help='Report what would change without writing')
    args = ap.parse_args()

    api = NotionAPI()

    print(f"Fetching all Knowledge Vault entries from {VAULT_DB_ID} ...")
    all_entries = _fetch_all_entries(api, VAULT_DB_ID)
    print(f"  Total entries in DB: {len(all_entries)}")

    print("Checking page bodies for emptiness (this makes one API call per entry) ...")
    empty_entries = []
    for i, page in enumerate(all_entries):
        if _has_empty_body(api, page['id']):
            empty_entries.append(page)
        time.sleep(RATE_LIMIT_SECONDS)
    print(f"  Entries with empty bodies (before): {len(empty_entries)} / {len(all_entries)}")

    to_process = empty_entries[:args.limit]
    print(f"  Processing {len(to_process)} (capped by --limit {args.limit}) ...")

    results = []
    for i, page in enumerate(to_process):
        res = reconstruct_and_backfill(api, page, dry_run=args.dry_run)
        results.append(res)
        status = res['action']
        print(f"  [{i+1}/{len(to_process)}] {status}: {res['new_title'][:70]}")
        time.sleep(RATE_LIMIT_SECONDS)

    ok = sum(1 for r in results if r['action'] in ('backfilled', 'dry-run'))
    errors = [r for r in results if r['action'] == 'error']

    print("\n--- Backfill Summary ---")
    print(f"Empty bodies before this run: {len(empty_entries)}")
    print(f"Processed this run: {len(to_process)} (succeeded: {ok}, errors: {len(errors)})")
    print(f"Empty bodies remaining after this run (est.): {len(empty_entries) - ok}")
    if errors:
        print("Errors:")
        for e in errors:
            print(f"  {e['page_id']}: {e.get('error')}")
    if len(empty_entries) > args.limit:
        print(f"\n{len(empty_entries) - len(to_process)} empty entries remain — re-run with --limit to continue.")


if __name__ == '__main__':
    main()
