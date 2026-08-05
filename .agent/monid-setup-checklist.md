# Monid AI Setup Checklist

**Status**: Cost-gate infrastructure READY (cost_gate.py + cost_gate_hook.py + monid_client.py + policy)
**Manual steps**: Activate on 3 surfaces + fund wallet

---

## Surface 1: claude.ai (Browser)

✅ **Ready to configure**

1. Open https://claude.ai
2. Settings → Connectors
3. Click "Add custom connector"
4. Fill in:
   - **Name**: Monid
   - **MCP URL**: `https://mcp.monid.ai/v1`
5. Click "Add"
6. Authorize Monid login → Allow

**Result**: $1 free credit on first login. Then prompt Monid in any chat:
```
Find the latest posts about [your topic] using Monid MCP
```

---

## Surface 2: Claude Code (This Project)

⚠️ **Pending: `.mcp.json` sensitive file — manual edit required**

File: `/Users/farricecain/Google Antigravity/.mcp.json`

Add to `mcpServers` object:
```json
"monid": {
  "type": "http",
  "url": "https://mcp.monid.ai/v1"
}
```

After saving, reload Claude Code's MCP service.

**Verification**:
```bash
python3 execution/monid_client.py budget-status  # should show GREEN
```

---

## Surface 3: Codex / CLI

⚠️ **Pending: Codex config file — contact Codex support or check Codex docs**

Codex uses its own MCP configuration. Add Monid:
```json
{
  "type": "http",
  "url": "https://mcp.monid.ai/v1"
}
```

---

## Wallet Funding (CRITICAL)

**Monid requires a funded wallet to make API calls.**

1. Open https://app.monid.ai (login with your Monid account from step 1 above)
2. Go to Billing → Add payment method
3. Add credit card or prepaid balance
4. **Suggested**: Start with $10 (good for ~300+ exploratory queries)

**Note**: Cost-gate will allow up to $5.00 per query (approve via token for higher). Monthly cap: $25.00.

---

## Cost-Gate Integration Status

✅ **READY** — Infrastructure deployed:

- `execution/cost_gate.py`: Monid service entry added
- `execution/hooks/cost_gate_hook.py`: Monid pattern registered
- `execution/monid_client.py`: Tracking + budget commands
- `.agent/monid-usage.json`: Tracker initialized
- `directives/monid-usage-policy.md`: Policy documented

**Self-test**:
```bash
python3 execution/hooks/cost_gate_hook.py --self-test  # should pass
python3 execution/monid_client.py budget-status         # should show GREEN
```

---

## Next Steps

1. **Surface 1 (claude.ai)**: Complete when you have time (one-click setup)
2. **Surface 2 (.mcp.json)**: Edit `.mcp.json` to add Monid (or Farrice can do it)
3. **Surface 3 (Codex)**: Coordinate with Codex user
4. **Wallet funding**: Go to app.monid.ai and add payment (Farrice manual step)
5. **Test run**: After wallet funded, try:
   ```bash
   python3 execution/monid_client.py log --query "test" --cost 0.02 --results 5
   ```

---

## Safety Nets

- **Monthly budget**: $25.00 (auto-resets 1st of month)
- **Per-run cap**: $5.00 (override with approval token: `cost_gate.py approve --service monid --minutes 15`)
- **Cost-gate hook**: Pre-flight gate on all monid_client.py calls
- **Fallback**: If budget exhausted, route to Apify or Perplexity per `directives/monid-usage-policy.md`

**Cost tracking**: Every query logged to `.agent/monid-usage.json` (actual cost from Monid response).

---

**Date**: 2026-08-05  
**Phase**: D (Monid trial wiring, cost-gate registration DONE)
