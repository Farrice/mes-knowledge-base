from pathlib import Path
import hashlib
import json
import shutil
import subprocess

source = Path('/Users/farricecain/Documents/Codex/2026-09-07/jen-content-studio')
hub = Path('/Users/farricecain/Google Antigravity')
lane = hub / '.tmp/codex-worktrees/jen-content-recovery-20260907'
package = Path('_active/clients/jen-listings/04-deliverables/social-content/2026-09-07-content-recovery')
destinations = [lane / package, hub / package]
approved_hash = '9a49863f03c746c54541c30de0a2325db6e851bb6618267d6fdb2461dc9f89d3'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def tracked_changes():
    return subprocess.run(['git', '-C', str(hub), 'diff', '--name-only', 'HEAD'], check=True, capture_output=True, text=True).stdout

assert digest(source / 'outputs/jen-asking-again.md') == approved_hash
assert subprocess.run(['git', '-C', str(lane), 'branch', '--show-current'], check=True, capture_output=True, text=True).stdout.strip() == 'codex/jen-content-recovery-20260907'
for destination in destinations:
    if destination.exists():
        raise SystemExit(f'Transfer destination already exists; refusing overwrite: {destination}')

files = sorted(p for p in source.rglob('*') if p.is_file())
assert all(not p.is_symlink() for p in files), 'Inspect symlinks before copying.'
entries = [{'path': str(p.relative_to(source)), 'bytes': p.stat().st_size, 'sha256': digest(p)} for p in files]
manifest = {'source': str(source), 'destinations': [str(p) for p in destinations], 'scope': 'Every existing project file, including outputs and work. Manifest and final receipt verified separately.', 'files': entries, 'approved_sha256': approved_hash}
manifest_path = source / 'work/jen-transfer-manifest.json'
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
all_files = files + [manifest_path]
tracked_before = tracked_changes()

for destination in destinations:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    for original in all_files:
        copied = destination / original.relative_to(source)
        assert copied.is_file() and digest(original) == digest(copied), f'Copy mismatch: {copied}'
    assert digest(destination / 'outputs/jen-asking-again.md') == approved_hash

assert tracked_before == tracked_changes(), 'Unexpected tracked main-file changes during import.'
count = len(all_files) + 1
total_bytes = sum(p.stat().st_size for p in all_files)
receipt = f'''# Jen transferred to Google Antigravity

The complete current Jen project has been copied into Google Antigravity and verified. **{count} files** are present in both the project import and its dedicated working copy, including this receipt. Every transferred file matches its source byte for byte. The approved post's original SHA-256 is unchanged.

## Open the transferred project

Google Antigravity project folder:

`{destinations[1]}`

Read `outputs/GOOGLE-ANTIGRAVITY-START.md` there. It points to the exact approved post, current brief, corrections, source evidence and next creative action.

The dedicated writing copy is:

`{destinations[0]}`

Its branch is `codex/jen-content-recovery-20260907`. The existing workspace bootstrap reported FULL POWER. The import added a new Jen-specific folder; it did not overwrite existing project files, merge branches, change global settings, or remove the Documents copy.

## What survived

- Exact approved overlay and caption, approved visual assets, eight research documents and the 239-record source ledger.
- Review history with failed drafts excluded from writing references.
- Recovered conversation messages, original approval trace, latest critique and continuation instructions.
- New VidIQ responses plus 98 portable copies of older source-evidence files and their provenance map.

The VidIQ pass spent **20 of 30 approved credits**; checked balance: **1,689**. It did not find a new complete reference that met the requested standard. The new post remains unfinished. No replacement was represented as approved or proven.

## Conversation location

The files and recovered conversation content are transferred. **This native Codex task itself still belongs to its original projectless location.** The available task handoff action cannot move the calling task, and computer use cannot control Codex. No replacement task was created without an explicit request.

Transfer manifest: `work/jen-transfer-manifest.json`. Source files verified before the final receipt: {len(all_files)} ({total_bytes:,} bytes). This receipt is verified separately in both destinations.
'''
receipt_path = source / 'outputs/GOOGLE-ANTIGRAVITY-TRANSFER.md'
receipt_path.write_text(receipt)
for destination in destinations:
    target = destination / receipt_path.relative_to(source)
    shutil.copy2(receipt_path, target)
    assert digest(target) == digest(receipt_path)
    assert len([p for p in destination.rglob('*') if p.is_file()]) == count

print(json.dumps({'result': 'PASS', 'files_verified_per_destination': count, 'destinations': [str(p) for p in destinations], 'approved_sha256': approved_hash, 'existing_tracked_main_changes_preserved': True, 'native_task_reassigned': False}, indent=2))
