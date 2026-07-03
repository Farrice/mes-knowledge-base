---
name: "source-command-raw-intent-bridge"
description: "Run /raw-intent-bridge when the user gives raw intent, messy entrepreneurial context, rough notes, asks for a prompt-engineering bridge, says they do not know how to ask Codex, wants a Codex-ready run packet, or needs predicted need, objective, quality bar, route, gates, first safe action, and proof before normal execution."
---

# source-command-raw-intent-bridge

Put this skill before any raw context when the user invokes
`/raw-intent-bridge`, `raw-intent-bridge:`,
`source-command-raw-intent-bridge:`, asks for the Raw Intent Virtuoso Bridge, or
needs messy operator intent compiled into a deterministic Codex run packet.

## Invocation Contract

Accepted forms are equivalent:

```text
/raw-intent-bridge [payload]
raw-intent-bridge: [payload]
source-command-raw-intent-bridge: [payload]
```

The payload is everything after the prefix. Strip the prefix before packet
generation, route selection, first safe action generation, and handoff. Never
echo `/raw-intent-bridge`, `raw-intent-bridge:`, or
`source-command-raw-intent-bridge:` back into the first safe action.

## Stage 0: Vision Translation (mandatory — before the compiler)

The packet compiler routes lexically; raw vision-speech mis-routes it. Never
compile flow-speech directly. First build a Translation Card from the stripped
payload:

- **Anchor** — which active project/client/system this belongs to (match
  against project memory; never guess across projects)
- **Deliverable** — the concrete artifact implied
- **Audience** — who receives it
- **Felt standard** — the vision phrases in Farrice's exact words, verbatim.
  Never paraphrase this away; it is the creative payload.
- **Sharpened intent line** — ONE sentence:
  `<verb> <deliverable> for <anchor> using <owning OS/expert if known> —
  <felt standard, compressed>`, containing route-findable keywords.

If Anchor or Deliverable cannot be filled, ask exactly ONE question covering
both gaps, then proceed. One round max — never interrogate flow-state.

The sharpened line is for the ROUTER; the verbatim quotes are for the EXPERT.
Compile with the sharpened line, execute the route with the original payload +
Translation Card as context.

## Packet + Run Default

Default behavior is Packet + Run: translate (Stage 0), compile the packet from
the sharpened intent line, then follow the first safe local action when it is
reversible, current-workspace local, and inside the boundaries. Stop for approval before global writes, external writes,
publishing, outreach, paid/quota-heavy tools, destructive cleanup, connector
writes, plugin marketplace edits, non-current-workspace harness edits, or real
Codex subagents.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/raw-intent-bridge.md` as the
canonical behavior source. It must preserve:

- raw intent is compiled before normal routing
- the durable compiler is `execution/raw_intent_run_packet.py`
- `/autopilot` and `/virtuoso` remain support surfaces, not competing owners
- `/source-to-skill-system` owns bridge-build and companion-layer evolution
- prompt-engineer/world-class/virtuoso wording does not capture unrelated
  creative-writing routes
- plugin packaging is deferred to `antigravity-operator-core` after cold-start
  proof
- no global mirrors, plugin marketplace edits, external writes, destructive
  actions, or real Codex subagents without explicit authorization; a thin
  global trigger wrapper is allowed only when Farrice explicitly asks for
  global deployment

## Command Template

Read and execute `.agent/workflows/raw-intent-bridge.md`. Run Stage 0 Vision
Translation, then compile the packet from the SHARPENED line (never the raw
payload — raw_intent_run_packet.py routes lexically and mis-routes on
vision-speech):

```bash
python3 execution/raw_intent_run_packet.py "<sharpened intent line>" --plain
```

Use one of these modes when useful:

```bash
python3 execution/raw_intent_run_packet.py "<sharpened intent line>" --mode revenue --plain
python3 execution/raw_intent_run_packet.py "<sharpened intent line>" --mode creative --plain
python3 execution/raw_intent_run_packet.py "<sharpened intent line>" --mode system --plain
```

Then follow the packet's chosen route, support gates, first safe action, and
verification plan.
