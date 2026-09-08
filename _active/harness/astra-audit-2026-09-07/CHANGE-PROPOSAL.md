# Small first change: remove two competing automatic instructions

Status: APPROVED AND APPLIED on September 7. Fresh task startup confirms both payloads absent; see `evidence/startup-activation.json`. Owner: system-audit. Target: `/Users/farricecain/.codex/config.toml` only. All unrelated parsed settings were preserved. The original proposal below is retained as the change specification. Follow-up scope and outcomes are in `REPAIR-RESULT.md`.

## Exact proposed changes

1. In `[plugins."learning-output-style@claude-plugins-official"]`, change `enabled = true` to `enabled = false`.
2. In `[hooks.state."jarvis-command-center@jcc-local:hooks/hooks.json:session_start:0:0"]`, add `enabled = false`; preserve the existing trusted hash. Keep the JARVIS plugin itself enabled.

The first removes teaching homework as a global default. The second removes automatic injection of the complete competing orchestrator and historical failure registry while retaining the plugin's manually available functions. Use the supported per-hook setting; do not edit cached plugin source or uninstall the entire library. Re-read the current file before applying because another task may change it.

## Proof required after application

- Confirm exactly those two settings changed and the settings file still parses.
- Start a fresh Google Antigravity project task only with the user's authorization, or have the user start one. Confirm the teaching and full orchestrator SessionStart payloads are absent. A config diff alone is not activation proof.
- Confirm the canonical Google routing and protective hooks remain available.
- Test a small clear task for immediate execution without a deployment menu or user coding assignment.
- Test one Jen adaptation from the preserved approved packet. Compare complete writing, scope retention and question burden. Do not claim improved craft from the absence of a plugin injection alone.
- Roll back these exact two setting changes if the affected controls or intended capabilities regress.

Current-session limitation: instructions already injected remain part of this conversation. Changing a settings file does not erase them retroactively.

## Subsequent local repairs, separately scoped

- Make unavailable performance data UNKNOWN instead of zero, with an offline negative control.
- Remove the canonical/deferred verifier contradiction from the existing system-audit workflow.
- Preserve active intent when a follow-up names a domain as evidence during a system audit.
- Add a Codex-specific interpretation of seating in the existing doctrine without altering Claude's configuration or requiring additional delegation.
- Replace instruction-presence claims in the existing weekly behavioral eval with observed task outputs.

Do not bundle these into the two-setting experiment or add a new universal prompt layer. Each repair needs a demonstrated failure and a proportionate check.
