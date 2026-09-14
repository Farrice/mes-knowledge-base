import json
import tempfile
from pathlib import Path
roots=[Path('/Users/farricecain/Work')/p for p in ('20 Clients','30 Business','40 Creative','50 Reference/Asset Filing')]
results=[]
for root in roots:
    try:
        with tempfile.NamedTemporaryFile(prefix='.asset-filing-access-check-',dir=root) as stream:
            stream.write(b'asset filing access proof\n')
            stream.flush()
            assert Path(stream.name).read_bytes()==b'asset filing access proof\n'
        results.append({'folder':str(root),'write_read':'PASS'})
    except OSError as e:
        results.append({'folder':str(root),'write_read':'FAIL','error':str(e)})
print(json.dumps({'test':'fresh Codex CLI sandbox, no model or browser','results':results},indent=2))
raise SystemExit(0 if all(r['write_read']=='PASS' for r in results) else 1)
