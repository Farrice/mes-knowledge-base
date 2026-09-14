from pathlib import Path
import subprocess
import sys
import json
import tomllib
WORK=Path('/Users/farricecain/Work')
SUPPORT=WORK/'50 Reference'/'Asset Filing'
helper=SUPPORT/'asset_filing.py'
def run(*args):
    p=subprocess.run([sys.executable,str(helper),*args],capture_output=True,text=True,check=True)
    return json.loads(p.stdout)
home=run('init','--category','business','--project','Asset Filing Setup')['project_home']
first=run('file',str(WORK/'ASSET-FILING.md'),'--project-home',home,'--asset','filing-guide','--status','review')
repeat=run('file',str(WORK/'ASSET-FILING.md'),'--project-home',home,'--asset','filing-guide','--status','review')
found=run('find','asset-filing-setup','--status','review','--verify')
assert first['result']=='filed-copy' and repeat['result']=='already-filed'
assert len(found)==1 and found[0]['file_state']=='verified'
config=tomllib.loads(Path('/Users/farricecain/.codex/config.toml').read_text())
assert 'sandbox_workspace_write' not in config
assert '<!-- BEGIN:asset-filing-default -->' not in Path('/Users/farricecain/.codex/AGENTS.md').read_text()
receipt={'local_helper_installed':True,'filed_asset':first['path'],'idempotent_repeat':True,'retrieved_and_hash_verified':True,'original_preserved':(WORK/'ASSET-FILING.md').is_file(),'downloads_touched':False,'global_activation':'BLOCKED_PENDING_EXPLICIT_APPROVAL','browser_download_upload':'NOT_RUN','local_regression_checks_passed':9}
(SUPPORT/'installation.json').write_text(json.dumps(receipt,indent=2)+'\n')
(SUPPORT/'SETUP-RECEIPT.md').write_text('''# Asset Filing Setup — Proof and Remaining Activation

## Installed and tested

- Human guide: `/Users/farricecain/Work/ASSET-FILING.md`, linked from Work/START-HERE.md.
- Installed helper creates readable project folders, copies explicitly chosen assets, assigns versions, and writes readable indexes plus provenance records.
- Nine regression checks passed: original preservation, duplicate import, version retention, approval-note requirement, verified retrieval, changed-file detection, partial-download refusal, linked-destination refusal, and readable indexes.
- Live local proof: filed the actual guide in Work/30 Business/asset-filing-setup, repeated the import without creating another copy, then found it by project and verified its SHA-256. The guide remains in review; no human approval was fabricated.
- No personal Downloads files were changed. No watcher, website upload, or publication ran.

## Pending

Automatic approval review rejected global Codex config/instruction changes because the exact global scope needs explicit user approval. Those files remain unchanged.

Proposed scope: add Work/20 Clients, Work/30 Business, Work/40 Creative, and Work/50 Reference/Asset Filing as additional writable folders; add a short global instruction to read the installed filing guide during asset tasks. Existing approval policy, network restrictions, and default Downloads destination remain unchanged. Backups will be created before activation.

A fresh-task automatic-access test and a real browser download/upload test remain unrun. The local helper is proven; unattended computer transfers and automatic global adoption are not yet proven.

## Repository source

The installation source and tests are preserved in the codex/asset-filing-setup worktree. Integration into main is a separate repository step; the installed local files do not depend on that worktree remaining open.
''')
print(json.dumps(receipt,indent=2))
