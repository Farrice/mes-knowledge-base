#!/usr/bin/env python3
"""File explicitly identified assets; never scan, move, or delete Downloads."""
import argparse
import fcntl
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

WORK = Path('/Users/farricecain/Work')
CATEGORIES = {'client': '20 Clients', 'business': '30 Business', 'creative': '40 Creative'}
SLOTS = {'source': '01-source', 'draft': '03-working-drafts', 'review': '05-assets', 'approved': '04-deliverables', 'export': '90-exports'}


def slug(value):
    value = re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')
    if not value or len(value) > 100:
        raise ValueError('Use a descriptive name of 1–100 characters after normalization.')
    return value


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def safe_home(path):
    home = Path(path).resolve(strict=True)
    if not home.is_dir() or not any(home.is_relative_to(WORK.resolve() / c) and home != WORK.resolve() / c for c in CATEGORIES.values()):
        raise ValueError('Choose a project inside Work/20 Clients, 30 Business, or 40 Creative. Repository projects retain their native artifact router and worktree rules.')
    return home


def child(home, relative):
    path = home / relative
    if not path.resolve().is_relative_to(home) or path.is_symlink():
        raise ValueError(f'Unsafe linked path: {path}')
    return path


def init(category, title):
    home = WORK / CATEGORIES[category] / slug(title)
    if home.is_symlink() or (WORK / CATEGORIES[category]).is_symlink():
        raise ValueError('An existing link owns this destination; use its established home.')
    home.mkdir(parents=True, exist_ok=True)
    home = safe_home(home)
    # Create folders only when populated.
    index = child(home, 'INDEX.md')
    if not index.exists():
        with index.open('x') as out:
            out.write(f'# {title}\n\nOne stable project home.\n\n'
                      '- [Approved deliverables](04-deliverables/)\n'
                      '- [Assets awaiting review](05-assets/)\n'
                      '- [Working drafts](03-working-drafts/)\n'
                      '- [Sources](01-source/)\n'
                      '- [Exports](90-exports/)\n\n'
                      'ASSET-INDEX.md appears after the first filed asset and lists all versions.\n')
    return home


def records(home):
    ledger = child(home, '06-system/asset-register.jsonl')
    rows = [json.loads(line) for line in ledger.read_text().splitlines() if line.strip()] if ledger.exists() else []
    latest = {}
    for row in rows:
        latest[(row['stem'], row['version'])] = row
    return list(latest.values())


def write_index(home, rows):
    lines = ['# Asset Index', '', 'All filed versions. Higher version numbers do not imply approval.', '', '| Asset | Status | Original filename |', '|---|---|---|']
    for row in rows:
        if row.get('lifecycle') in {'parked', 'superseded', 'archived'}:
            continue
        original = row['original_name'].replace('|', '\\|').replace('\n', ' ').replace('\r', ' ')
        lines.append(f'| [{Path(row["path"]).name}]({quote(row["path"])}) | {row["status"]} | {original} |')
    lines += ['', 'History is excluded here; consult CANON.md or 99-archive for an explicit historical request.', '', 'Provenance: [asset register](06-system/asset-register.jsonl).', '']
    pending = child(home, '06-system/asset-index-pending.md')
    pending.write_text('\n'.join(lines))
    pending.replace(child(home, 'ASSET-INDEX.md'))


def file_asset(source, home, asset, status='review', source_url='', approval_note=''):
    home = safe_home(home)
    source = Path(source).resolve(strict=True)
    if not source.is_file() or source.name.endswith(('.crdownload', '.part', '.download')):
        raise ValueError('Source must be a completed regular file.')
    if status not in SLOTS or (status == 'approved' and not approval_note.strip()):
        raise ValueError('Approved status needs a note identifying the actual approval.')
    stem = f'{slug(home.name)}-{slug(asset)}'
    extension = source.suffix.lower()
    if not re.fullmatch(r'\.[a-z0-9]{1,12}', extension):
        raise ValueError('Source needs a recognizable file extension.')
    child(home, '06-system').mkdir(exist_ok=True)
    with child(home, '06-system/asset-filing.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        rows = records(home)
        sha = digest(source)
        for row in rows:
            existing = child(home, row['path'])
            if row.get('lifecycle', 'active') not in {'parked', 'superseded', 'archived'} and row['stem'] == stem and row['status'] == status and row['sha256'] == sha and existing.is_file() and digest(existing) == sha:
                write_index(home, rows)
                return {'path': str(existing), 'result': 'already-filed', 'sha256': sha}
        versions = [r['version'] for r in rows if r['stem'] == stem]
        for folder in SLOTS.values():
            for p in child(home, folder).glob(f'{stem}-v*-*'):
                match = re.fullmatch(re.escape(stem) + r'-v(\d+)-[^.]+\.[a-z0-9]+', p.name)
                if match:
                    versions.append(int(match[1]))
        version = max(versions, default=0) + 1
        child(home, SLOTS[status]).mkdir(exist_ok=True)
        while True:
            target = child(home, f'{SLOTS[status]}/{stem}-v{version:02d}-{status}{extension}')
            try:
                out = target.open('xb')
                break
            except FileExistsError:
                version += 1
        with source.open('rb') as inp, out:
            shutil.copyfileobj(inp, out)
        if digest(target) != sha or digest(source) != sha:
            raise RuntimeError(f'Copy check failed; retained files for inspection: {target}')
        row = dict(stem=stem, version=version, status=status, path=str(target.relative_to(home)),
                   original_name=source.name, original_path=str(source), source_url=source_url,
                   sha256=sha, approval_note=approval_note, filed_at=datetime.now(timezone.utc).isoformat())
        with child(home, '06-system/asset-register.jsonl').open('a') as ledger:
            ledger.write(json.dumps(row) + '\n')
        rows.append(row)
        write_index(home, rows)
        return {'path': str(target), 'result': 'filed-copy', 'sha256': sha, 'original_preserved': source.exists()}


def find_assets(query='', status=None, verify=False, include_history=False):
    result = []
    for category in CATEGORIES.values():
        for home in sorted((WORK / category).glob('*')):
            if not home.is_dir() or home.is_symlink():
                continue
            home = safe_home(home)
            for row in records(home):
                if not include_history and (row.get('lifecycle') in {'parked', 'superseded', 'archived'} or '99-archive' in Path(row['path']).parts):
                    continue
                if query.lower() not in (home.name + ' ' + row['path'] + ' ' + row['original_name']).lower() or (status and row['status'] != status):
                    continue
                path = child(home, row['path'])
                state = 'missing' if not path.is_file() else ('verified' if verify and digest(path) == row['sha256'] else 'changed' if verify else 'exists')
                result.append({**row, 'absolute_path': str(path), 'file_state': state})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('init')
    p.add_argument('--category', choices=CATEGORIES, required=True)
    p.add_argument('--project', required=True)
    p = commands.add_parser('file')
    p.add_argument('source')
    p.add_argument('--project-home', required=True)
    p.add_argument('--asset', required=True)
    p.add_argument('--status', choices=SLOTS, default='review')
    p.add_argument('--source-url', default='')
    p.add_argument('--approval-note', default='')
    p = commands.add_parser('find')
    p.add_argument('query', nargs='?', default='')
    p.add_argument('--status', choices=SLOTS)
    p.add_argument('--verify', action='store_true')
    p.add_argument('--include-history', action='store_true')
    args = parser.parse_args()
    try:
        if args.command == 'init':
            result = {'project_home': str(init(args.category, args.project))}
        elif args.command == 'find':
            result = find_assets(args.query, args.status, args.verify, args.include_history)
        else:
            result = file_asset(args.source, args.project_home, args.asset, args.status, args.source_url, args.approval_note)
        print(json.dumps(result, indent=2))
    except (ValueError, OSError, RuntimeError) as error:
        parser.exit(1, f'Not filed: {error}\n')


if __name__ == '__main__':
    main()
