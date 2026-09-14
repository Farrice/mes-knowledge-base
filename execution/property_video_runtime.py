#!/usr/bin/env python3
"""Install and verify a private property-video runtime. No network or generation calls.

Only this loader and thin skills belong in the public repository. Licensed source
packs, media, prompts and production state are copied into an ignored local home.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

CLIENT = Path('_active/clients/jen-listings')
PRIVATE = Path('.private/property-video')
NAMES = ('property-video-ai', 'jen-cinematic-property-film', 'real-estate-marketing-fal')
SKIP = {'.git', '.env', '.env.local', '.DS_Store', '__pycache__', 'credentials.json', 'token.json'}

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def copy_tree(src, dst, records):
    if src.name in SKIP:
        return
    if src.is_symlink():
        target = os.readlink(src)
        if dst.is_symlink() and os.readlink(dst) == target:
            return
        if dst.exists() or dst.is_symlink():
            raise ValueError(f'Existing link conflict: {dst}')
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.symlink_to(target)
    elif src.is_dir():
        dst.mkdir(parents=True, exist_ok=True)
        for child in sorted(src.iterdir()):
            copy_tree(child, dst / child.name, records)
    elif src.is_file():
        source_hash = digest(src)
        if dst.exists() and digest(dst) != source_hash:
            raise ValueError(f'Refusing to overwrite changed private asset: {dst}')
        if not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        if digest(dst) != source_hash:
            raise ValueError(f'Copy mismatch: {dst}')
        if 'node_modules' not in src.parts:
            records.append({'source': str(src), 'file': str(dst), 'sha256': source_hash})

def install(repo, rosita, armida):
    home = repo / PRIVATE
    check = subprocess.run(['git', '-C', str(repo), 'check-ignore', '--quiet', str(PRIVATE / 'probe')])
    if check.returncode:
        raise ValueError('Private runtime must be gitignored before installation')
    if (home / 'INSTALL-RECEIPT.json').exists():
        raise ValueError('Runtime already installed; verify it instead of overwriting it')
    records = []
    selections = [(rosita, CLIENT / '06-system/andynocode-fal'),
                  (rosita, CLIENT / '06-system/luke-property-workflow'),
                  (rosita, CLIENT / '04-deliverables/2026-09-12-rosita-reel-test'),
                  (armida, CLIENT / '06-system/listing-video-workflow')]
    selections += [(armida, p.relative_to(armida)) for p in sorted((armida / CLIENT / '04-deliverables').glob('2026-09-12-armida*'))]
    for root, rel in selections:
        if not (root / rel).is_dir():
            raise ValueError(f'Missing source: {root / rel}')
    for root, rel in selections:
        copy_tree(root / rel, home / rel, records)
    for source in sorted((rosita / '.tmp').glob('reel-reference-b*')):
        copy_tree(source, home / '.tmp' / source.name, records)
    # Internal aliases retain the source verifier's original directory contract.
    for harness in ('.agents', '.claude'):
        for name in ('property-video-ai', 'real-estate-marketing-fal'):
            copy_tree(rosita / harness / 'skills' / name, home / harness / 'skills' / name, records)
    (home / 'execution').symlink_to(repo / 'execution', target_is_directory=True)
    workflow = home / CLIENT / '06-system/listing-video-workflow'
    current = {'primary_workflow': str(workflow / 'SKILL.md'),
               'approved_standard': str(workflow / 'APPROVED-STANDARD.md'),
               'source_owner': str(home / CLIENT / '06-system/luke-property-workflow'),
               'rosita_baseline': str(home / CLIENT / '04-deliverables/2026-09-12-rosita-reel-test/story-v2/APPROVED-BASELINE.json'),
               'budget_ledger': str(home / CLIENT / '04-deliverables/2026-09-12-armida-proof/flow-budget.json'),
               'credit_rule': 'Historical ledger only. Reconcile active tasks and live balance before new spend. Never reset or duplicate the original cap.',
               'music': 'off', 'new_provider_spend': 'not authorized by installation',
               'live_claude_generation': 'not tested', 'snapshot_roots': [str(rosita), str(armida)]}
    (home / 'CURRENT.json').write_text(json.dumps(current, indent=2) + '\n')
    # Keep source configuration untouched; supply a relocated runtime map separately.
    mapping = json.loads((workflow / 'integration-map.json').read_text())
    def relocated(value):
        if isinstance(value, str):
            for root in (rosita, armida):
                value = value.replace(str(root), str(home))
            return value
        if isinstance(value, list): return [relocated(v) for v in value]
        if isinstance(value, dict): return {k: relocated(v) for k, v in value.items()}
        return value
    runtime = home / 'runtime'
    runtime.mkdir(exist_ok=True)
    (runtime / 'integration-map.json').write_text(json.dumps(relocated(mapping), indent=2) + '\n')
    (home / 'INSTALL-RECEIPT.json').write_text(json.dumps({'files': records, 'current': current}, indent=2) + '\n')
    return verify(repo)

def verify(repo):
    home = repo / PRIVATE
    data = json.loads((home / 'INSTALL-RECEIPT.json').read_text())
    failures = [r['file'] for r in data['files'] if not Path(r['file']).is_file() or digest(Path(r['file'])) != r['sha256']]
    for rel in ['06-system/luke-property-workflow/luke_workflow.py', '06-system/listing-video-workflow/verify_approved_baseline.py']:
        command = [sys.executable, str(home / CLIENT / rel)]
        if rel.endswith('luke_workflow.py'): command.append('verify')
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode: failures.append(rel + ': ' + result.stdout + result.stderr)
    for rel in ['06-system/andynocode-fal/project/node_modules/.bin/hyperframes', '06-system/listing-video-workflow/renderer/node_modules/.bin/remotion']:
        if not (home / CLIENT / rel).is_file(): failures.append('Missing renderer: ' + rel)
    return {'status': 'FAIL' if failures else 'PASS', 'files_checked': len(data['files']), 'failures': failures, 'current': data['current']}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('action', choices=['install', 'verify', 'status'])
    ap.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument('--rosita-root', type=Path)
    ap.add_argument('--armida-root', type=Path)
    args = ap.parse_args()
    if args.action == 'install':
        if not args.rosita_root or not args.armida_root: ap.error('Both source roots are required')
        result = install(args.repo.resolve(), args.rosita_root.resolve(), args.armida_root.resolve())
    elif args.action == 'verify': result = verify(args.repo.resolve())
    else: result = json.loads((args.repo / PRIVATE / 'CURRENT.json').read_text())
    print(json.dumps(result, indent=2))
    return 1 if result.get('status') == 'FAIL' else 0

if __name__ == '__main__':
    raise SystemExit(main())
