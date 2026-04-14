---
name: "Kill Switch Protocol"
skill: "prediction-market-risk-management"
produces: "3-level emergency shutdown with triggers, automated actions, recovery procedures, and test protocol"
version: "1.0"
---

# Kill Switch Protocol

Define, configure, test, and execute emergency shutdown procedures for prediction market trading systems. Based on the 8-check sequential validation chain from polymarket-arbitrage `risk_manager.py`, the Sovereign analysis 5% circuit breaker, WeatherBot implicit limits, PolySwarm daily loss suspension, and poly-maker's compound stop-loss with risk-off cooldown.

The kill switch is not a failure — it is a success. It means the system worked as designed. The failure is NOT having a kill switch when you need one. The arbitrage bot implements it as a one-way state machine: once `kill_switch_triggered = True`, ALL subsequent orders are rejected. There is no auto-reset. This is deliberate.

---

## Part A: Kill Switch Configuration (Run Before Going Live)

### A1: Three-Level Kill Switch Architecture

Each level is progressively aggressive. The 8-check validation chain feeds into this — Checks 7 (daily loss) and 8 (drawdown) auto-trigger Level 3 when `kill_switch_enabled` is set.

---

### LEVEL 1: YELLOW — Reduced Operations

**Trigger Conditions (ANY of):**

| Trigger | Threshold | Rationale | Source |
|---------|-----------|-----------|--------|
| Daily P&L | -50% of max_daily_loss | Early warning before hard limit | Sovereign 5% circuit breaker |
| Single position loss | >2x expected max loss | Trade went worse than worst case | WeatherBot stop-loss architecture |
| API error rate | >5% of requests in 10 min | Platform degrading | Polymarket rate limits |
| Heartbeat response | >7 seconds | Approaching 10s platform kill | Polymarket docs — 10s window, 5s buffer |
| Win rate (rolling 10) | <40% | Edge may have decayed | PolySwarm uncertainty filter logic |
| Global exposure | >70% of max_global_exposure | Approaching hard ceiling | Arb bot Check 6 |
| Consecutive losses | >=5 | Beyond normal variance | Statistical threshold |

**Automated Actions (within 1 second):**
1. Reduce all new position sizes by 50% (halve max_bet / max_order_size)
2. Widen all market-making spreads by 2x (poly-maker spread_threshold)
3. Increase position monitoring frequency: 10 min -> 5 min (WeatherBot), 10s -> 5s (arb bot)
4. Block market-making new inventory (cancel resting limit orders for new markets)
5. Log alert with full RiskState snapshot
6. Set `level = "YELLOW"` in state

**Recovery to GREEN:**
- All trigger conditions clear for 30+ minutes
- No new alerts in recovery window
- Automatic (no manual approval needed)
- Resume normal thresholds

---

### LEVEL 2: ORANGE — New Positions Halted

**Trigger Conditions (ANY of):**

| Trigger | Threshold | Rationale | Source |
|---------|-----------|-----------|--------|
| Daily P&L | -80% of max_daily_loss | Approaching hard kill switch | Arb bot Check 7 |
| Drawdown from peak | 75% of max_drawdown_pct | Approaching hard kill switch | Arb bot Check 8 |
| HTTP 503 received | Any | Trading disabled / cancel-only mode | Polymarket docs |
| HTTP 425 received | Any | Matching engine restart (Tuesdays 7 AM ET) | Polymarket docs |
| Two+ stops in 30 min | 2 positions hit stop-loss | Correlated losses — potential cascade | WeatherBot monitor_positions |
| Consecutive losses | >=8 | Well beyond variance | Statistical threshold |
| Slippage event | Any fill >5% from expected | Execution environment hostile | Arb bot slippage_tolerance |
| Heartbeat missed | 1 miss (>10s) | Platform may have cancelled orders | Polymarket heartbeat protocol |

**Automated Actions (within 5 seconds):**
1. Halt ALL new position entry across all strategies (`check_order()` returns False for new orders)
2. Existing positions: stops remain active, no modifications to exit parameters
3. Cancel all resting limit orders (market-making inventory, pending entries)
4. Begin exponential backoff on API requests (1s, 2s, 4s, 8s) for monitoring calls
5. Enter per-market risk-off cooldown for any market that triggered (poly-maker pattern)
6. Log alert with full state + P&L breakdown per strategy
7. Send alert to operator (email + push notification)
8. Set `level = "ORANGE"` in state

**Recovery to YELLOW:**
- HTTP 503/425 resolved (successful API response confirmed)
- P&L recovers above -60% of max_daily_loss
- All slippage events investigated
- **Manual approval required** — operator confirms conditions are safe
- Resume at YELLOW (reduced operations) for minimum 4 hours before GREEN

---

### LEVEL 3: RED — Full Emergency Exit

**Trigger Conditions (ANY of):**

| Trigger | Threshold | Rationale | Source |
|---------|-----------|-----------|--------|
| Daily P&L | Exceeds max_daily_loss | Kill switch trigger | Arb bot `_trigger_kill_switch()` |
| Drawdown | Exceeds max_drawdown_pct | Kill switch trigger | Arb bot `_trigger_kill_switch()` |
| API unreachable | 5+ minutes | Cannot monitor or exit positions | Platform failure |
| Heartbeat missed | Platform cancelled all orders | Unhedged exposure if one side filled | Polymarket 10s window |
| Security compromise | Unauthorized API calls or wallet activity | Existential threat | Two-layer architecture breach |
| Catastrophic loss | >30% of capital in 48 hours | Beyond recovery at current scale | Sovereign analysis |
| Manual trigger | Operator panic button | Human sees something wrong | Always available |

**Automated Actions (within 10 seconds):**
1. Trigger kill_switch permanently: `state.kill_switch_triggered = True` — one-way door
2. Cancel ALL open orders via cancel-all endpoint
   - Respect 250/10s rate limit on cancel-all
   - If position count > 250: batch in 10s windows (this is why you monitor position count)
3. **If `auto_unwind_on_breach = True`**: Market-sell all positions at best available bid
   - Accept slippage — capital preservation, not P&L optimization
   - Use `bestBid` price (what you'd ACTUALLY get), not midpoint
4. **If `auto_unwind_on_breach = False`** (default): Positions remain open but no new orders
   - This is the arb bot's default — auto-unwinding during stress can lock in recoverable losses
5. Log complete state: all positions, all P&L, order history, API error logs, kill_switch_reason
6. Send notification to operator via ALL channels (email + SMS + push + phone if configured)
7. Enter 24-hour minimum cooldown — no trading regardless of manual reset
8. Set `level = "RED"` in state

**The Kill Switch is a One-Way Door:**
```python
def _trigger_kill_switch(self, reason):
    self.state.kill_switch_triggered = True
    self.state.kill_switch_reason = reason
    logger.critical(f"KILL SWITCH TRIGGERED: {reason}")
```
Once triggered, every subsequent `check_order()` call hits Check 1 and returns False immediately. The `update_pnl()` method ALSO checks independently, so the kill switch fires even between orders during portfolio mark-to-market.

**Recovery from RED — MANUAL ONLY:**
1. Root cause analysis document completed (use post-mortem template below)
2. Parameter review: were limits too loose? too tight?
3. Paper trading for minimum 2 days before live re-entry (full scaling protocol restart)
4. Manual state reset: `state.kill_switch_triggered = False`
5. If security trigger: rotate ALL API keys, revoke wallet permissions, withdraw to cold storage
6. Minimum 7-day cooling period before redeploying live capital (psychological — prevents revenge trading)
7. Restart at YELLOW thresholds for first 24 hours

---

### A2: Heartbeat Configuration

The heartbeat is the most critical monitoring mechanism. Polymarket's specification: "If a valid heartbeat is not received within 10 seconds (with a 5-second buffer), all open orders are cancelled."

```yaml
platform_heartbeat:
  # Polymarket WebSocket heartbeat — MANDATORY for order management
  interval: 5 seconds          # Send every 5s to stay within 10s window
  timeout: 10 seconds          # Platform cancels ALL orders at 10s
  buffer: 5 seconds            # Your safety margin
  heartbeat_id: latest         # Must use latest heartbeat_id from server
  
  # Impact of miss for market maker with 50 open orders:
  # - All 50 orders cancelled simultaneously
  # - If one side already filled: unhedged directional exposure
  # - Re-posting takes time, during which can't capture spread
  # - Cancel-all rate limit (250/10s) may throttle recovery

system_heartbeat:
  # Internal health check — separate from platform heartbeat
  interval: 30 seconds         # Arb bot uses 30s internal monitoring interval
  missed_threshold: 2          # 2 misses (60s) = Level 2 trigger
  
  # CRITICAL: Monitor process MUST be separate OS process
  # A deadlocked trading system cannot kill itself
  # A thread within a crashed process cannot cancel orders
  # The monitor must act when the trading system cannot
  
  monitor_actions_on_missed:
    - cancel_all_open_orders
    - close_all_positions_at_market
    - send_urgent_alert
    - set_level: "ORANGE"
```

---

### A3: Alert Configuration

```yaml
alerts:
  yellow:
    channels: ["log", "dashboard"]
    message: "YELLOW: {trigger} fired. Value: {value}, Threshold: {threshold}. 
              Position sizes halved. Monitoring frequency doubled."
  
  orange:
    channels: ["log", "dashboard", "email", "push"]
    message: "ORANGE: {trigger} fired. New positions halted. Existing stops active. 
              Manual approval required for recovery. Review immediately."
  
  red:
    channels: ["log", "dashboard", "email", "sms", "push", "phone"]
    message: "RED — KILL SWITCH TRIGGERED: {trigger}. {reason}. 
              All orders cancelled. Kill switch is ONE-WAY — manual reset required. 
              Post-mortem required before restart. 24h minimum cooldown."
```

---

## Part B: Emergency Execution Playbook

### B1: YELLOW Execution

When a YELLOW trigger fires:

**Immediate (automated, <1 second):**
1. Log trigger event with full context (metric, value, threshold, all positions)
2. Halve max_bet / max_order_size for all new trades
3. Widen market-making spreads by 2x
4. Increase monitoring: WeatherBot 10min->5min, arb bot 10s->5s
5. Start 30-minute observation window

**Within 5 minutes (operator review):**
1. Check dashboard — real signal or noise? (false positives are acceptable)
2. Review last 10 trades — any bad fills or strategy errors?
3. Check platform status — is this a platform issue or strategy issue?
4. Check if multiple YELLOW triggers are firing simultaneously (could cascade to ORANGE)

**After 30 minutes:**
- All triggers clear: automatic recovery to GREEN
- Some triggers remain: extend observation 30 more minutes
- Triggers worsening: manually escalate to ORANGE

---

### B2: ORANGE Execution

**Immediate (automated, <5 seconds):**
1. Log trigger with full context
2. Halt all new position entry
3. Cancel all resting limit orders
4. Enter risk-off cooldown per affected market (poly-maker pattern — no re-entry for `sleep_period` hours)
5. Start exponential backoff on monitoring API calls
6. Alert operator

**Within 30 minutes (operator REQUIRED):**
1. Verify halt is effective (no new orders in logs)
2. Review all active positions — any need manual exit?
3. Check if stops on existing positions are still set correctly
4. Diagnose trigger: platform issue, strategy failure, or market event?
5. If HTTP 425: wait for matching engine restart (~90s), verify 200 OK before any action
6. If HTTP 503: confirm cancel-only mode works, use it if positions need exiting

**Recovery Checklist (manual approval required):**
```
ORANGE RECOVERY CHECKLIST
==========================================
[ ] Root cause identified: _________________________________
[ ] Root cause resolved (not just symptoms): ________________
[ ] Platform API confirmed operational
[ ] Heartbeat confirmed responsive (<5s)
[ ] Fee schedule confirmed unchanged
[ ] All resting orders confirmed cancelled
[ ] Active positions reviewed — stops intact
[ ] System logs reviewed for anomalies
[ ] Decision: resume at YELLOW for minimum 4 hours

Operator: _______________
Date/time: _______________
```

---

### B3: RED Execution

**Immediate (automated, <10 seconds):**
1. Execute everything in ORANGE
2. Set `kill_switch_triggered = True` — permanent until manual reset
3. Cancel ALL open orders (batch within 250/10s rate limit)
4. If `auto_unwind_on_breach = True`: market-sell all positions at best bid
5. If `auto_unwind_on_breach = False`: no auto-liquidation (default — prevents locking in recoverable losses)
6. Log EVERYTHING: positions, P&L history, order book snapshots, API errors
7. Send alerts on ALL channels
8. Begin 24-hour cooldown timer

**If security trigger (unauthorized activity):**
1. Generate new API keys on platform immediately
2. Verify new keys work (test read-only endpoint)
3. Revoke old keys
4. Revoke wallet trading permissions (keep withdrawal)
5. Initiate full withdrawal to cold storage / bank
6. Log old key hashes for audit trail (NEVER log actual keys)
7. DO NOT update trading system config — system stays offline

**Fund withdrawal procedure:**
1. Log into platform directly (not through trading system)
2. Verify current balance matches expected
3. Initiate full withdrawal to verified destination
4. Set calendar reminder to verify receipt in 24h
5. If delayed >24h: contact platform support
6. If blocked: consult legal counsel immediately

---

### Post-Mortem Template (REQUIRED Before Restart from RED)

```
LEVEL 3 POST-MORTEM
==========================================
Date of incident: {date}
Trigger: {what fired}
Kill switch reason: {state.kill_switch_reason}
Duration: trigger -> full shutdown: {seconds}

TIMELINE:
{timestamp}: {event — be specific}
{timestamp}: {event}
...

ROOT CAUSE ANALYSIS:
What happened:              {factual description}
Why it happened:            {contributing factors}
Why it wasn't caught earlier: {monitoring gaps}
Was this in the 8-check chain? {which check should have caught it}

FINANCIAL IMPACT:
P&L at trigger:             ${amount}
Emergency close slippage:   ${amount}
Total impact:               ${amount} ({pct}% of bankroll)
Kill switch prevented:      ${estimated_additional_loss} (what would have happened without it)

SYSTEM ASSESSMENT:
Kill switch executed correctly?     {yes/no + details}
Alerts fired correctly?             {yes/no + details}
Shutdown completed in <10s?         {yes/no + actual time}
Cancel-all within rate limits?      {yes/no — if >250 orders, how was this handled?}
Auto-unwind setting was correct?    {yes/no + reasoning}
Any failures in shutdown process?   {details}

PARAMETER REVIEW:
max_daily_loss was:         ${value} — should it be: {tighter/same/looser}?
max_drawdown_pct was:       {value}% — should it be: {tighter/same/looser}?
YELLOW triggers caught it early enough? {yes/no}
ORANGE halted new positions? {yes/no}
Escalation path worked? {yes/no}

CORRECTIVE ACTIONS:
1. {Action + owner + deadline}
2. {Action + owner + deadline}
3. {Action + owner + deadline}

RESTART PLAN:
Restart date:         {no earlier than 7 days from incident}
Restart phase:        Paper trading (full scaling protocol)
Duration at paper:    Minimum 2 weeks (50+ trades)
Gate to micro-live:   {specific metrics}
Parameter changes:    {list any threshold adjustments}

LESSONS LEARNED:
- {What this taught us about risk management}
- {What we would do differently}
- {How this changes our operational checklist}
```

---

## Part C: Testing and Maintenance

### C1: Monthly Kill Switch Test

Test that automated shutdown ACTUALLY works. Systems degrade. API endpoints change. Alert channels break.

**Test Procedure:**
1. Set up test environment OR use live system during non-trading hours (no open positions)
2. Artificially trigger a YELLOW condition (e.g., inject fake 5-loss streak)
3. **Verify YELLOW:**
   - [ ] Position sizes halved in config
   - [ ] Monitoring frequency doubled
   - [ ] Log entry created with full state
   - [ ] Dashboard shows YELLOW status
   - [ ] Auto-recovery fires after 30 minutes of clear metrics
4. Artificially trigger an ORANGE condition (e.g., inject fake HTTP 503)
5. **Verify ORANGE:**
   - [ ] New position entry blocked
   - [ ] Resting orders cancelled
   - [ ] Risk-off cooldown set for affected markets
   - [ ] Alert delivered to correct channels within 60 seconds
   - [ ] Exponential backoff active on API calls
6. **Do NOT test RED on live system.** Test components separately:
   - [ ] Kill switch state transition works (set and verify Check 1 rejects)
   - [ ] Cancel-all endpoint works within rate limits
   - [ ] Alert channels all deliver (email, SMS, push)
   - [ ] Key rotation procedure documented and rehearsed
   - [ ] Withdrawal procedure tested with small amount

**Test Report:**
```
KILL SWITCH TEST REPORT
==========================================
Date: {date}
Environment: {test | live-non-trading-hours}

YELLOW Test:
  Trigger fired:           {yes/no}
  Position sizes halved:   {yes/no}
  Monitoring doubled:      {yes/no}
  Logging correct:         {yes/no}
  Alert sent:              {yes/no}
  Auto-recovery worked:    {yes/no}
  Time to full activation: {seconds}

ORANGE Test:
  Trigger fired:           {yes/no}
  New positions blocked:   {yes/no}
  Orders cancelled:        {yes/no} ({count})
  Alert delivered:         {yes/no} ({channels})
  Time to full activation: {seconds}

RED Component Tests:
  Kill switch state:       {works/broken}
  Cancel-all endpoint:     {works/broken} ({latency}ms)
  All alert channels:      {list status}
  Key rotation rehearsed:  {yes/no}
  Withdrawal tested:       {yes/no} ({time to complete})

Issues Found:             {list or "none"}
Actions Required:         {list or "none"}
Next Test Date:           {date — 30 days from now}
```

### C2: Threshold Review (Monthly)

As portfolio grows or strategy mix changes, thresholds need recalibration.

**Review Questions:**
- Has average daily P&L changed? (Session loss trigger may need recalibrating)
- Has API latency baseline changed? (2x multiplier may fire too often or not enough)
- Any false positives last month? (Triggers that fired but shouldn't have — thresholds too tight)
- Any near-misses? (Situations that SHOULD have triggered but didn't — thresholds too loose)
- Kill switch fired? How many times? Would continuing have been profitable? (If the kill switch triggered during temporary drawdowns that recovered: limits may be too tight. If it triggered before catastrophic losses: correctly calibrated.)
- Has the number of open positions grown? (Cancel-all rate limit 250/10s may not cover all orders)

### C3: Cascading Escalation Test (Quarterly)

Test the full YELLOW -> ORANGE -> RED escalation path in one session:
1. Trigger YELLOW via win rate
2. Verify YELLOW actions fire
3. While in YELLOW, trigger ORANGE via consecutive losses
4. Verify ORANGE escalation (new positions halt, orders cancel)
5. While in ORANGE, trigger RED via drawdown limit
6. Verify RED escalation (kill switch, all exits, alerts)
7. Verify recovery: RED requires manual reset, paper trading restart
8. Time the entire cascade — from first trigger to full RED should be <30 seconds

### C4: Recovery Drill (Quarterly)

Practice full ORANGE recovery:
1. Simulate ORANGE event
2. Run through recovery checklist as if real
3. Time the process: trigger -> verified restart
4. Identify bottlenecks (e.g., "took 45 minutes to verify all positions closed because we had to check 3 platforms manually")
5. Improve process based on findings

---

## Practitioner Notes

- **False positives are acceptable. False negatives are not.** A kill switch that fires too aggressively costs trading time. A kill switch that fails to fire costs capital. Err on the side of caution.

- **The separate monitoring process is non-negotiable.** A thread within the trading system cannot save you when the trading system crashes. A deadlocked process cannot cancel its own orders. The monitor must be independently capable of executing Level 2 actions.

- **The 24-hour cooldown after RED is mandatory, not suggested.** Catastrophic losses create emotional pressure to "win it back." The cooling period prevents revenge trading — which is how moderate losses become terminal losses. This is Step 6 of the 92.4% failure cascade: "Increase size to recover losses."

- **`auto_unwind_on_breach = False` is the safer default.** The arb bot chose this deliberately. During market stress, everyone is selling. Market-selling into a panic locks in the worst possible prices. Better to stop digging (no new trades) without filling in the hole at the worst price. Review positions manually when markets calm.

- **The heartbeat is existential for market makers.** 50 open orders, missed heartbeat, all cancelled, one side already filled = naked directional exposure. This is not theoretical. One network hiccup, one Cloudflare throttle, one server restart. Monitor heartbeat latency continuously. If it creeps above 7 seconds, treat it as YELLOW.

- **Tuesday 7 AM ET is a known risk window.** Polymarket matching engine restarts weekly. ~90 seconds downtime. HTTP 425 during restart. Plan accordingly — no new orders, existing orders may be affected.

- **Level 3 is rare but real.** You may never need it. But the 7 days you spend recovering without a post-mortem template and recovery plan will be the most expensive 7 days of your trading career. Have the plan before you need the plan.

- **Document everything during an event.** In the heat of ORANGE or RED, it is tempting to just fix things and move on. Resist this. Every action, every observation, every decision — log it in real time. Post-mortem quality depends entirely on the quality of notes taken during the event.

- **The manual panic button exists for a reason.** Sometimes you see something that doesn't fit any automated trigger but feels wrong. Trust that instinct. Hit the button. Investigate. Being wrong costs you a few hours. Being right saves your capital.

- **Test regularly.** The monthly test catches degraded alert channels, changed API endpoints, and broken state transitions BEFORE a real emergency reveals them. A kill switch you haven't tested is a kill switch you can't trust.
