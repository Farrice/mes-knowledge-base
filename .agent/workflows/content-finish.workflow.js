export const meta = {
  name: 'content-finish-loop',
  description: 'Produce → gate → self-correct loop. Every piece is written with the real voice + skills loaded, then must pass content_finish_gate (banned-moves + format) and the relevant ethics/voice gate BEFORE it returns. Slop cannot escape this loop.',
  phases: [
    { title: 'Produce+Gate', detail: 'write with voice/skills loaded, then self-correct against content_finish_gate until CLEAN' },
  ],
}

// THE PERMANENT FIX, as a production loop. Origin (2026-06-01): a teardown batch
// shipped raw agent output that tripped 4 voice bans and finalized at a hollow
// 8.33 because nothing mechanically scanned structure. This workflow makes that
// impossible: each agent must run execution/content_finish_gate.py on its own
// draft and rewrite until it returns CLEAN (exit 0). No piece returns FAIL-state.
//
// args: [{ label, brief, platform, voiceFile, skillFiles[], outFile }]
const tasks = args && args.length ? args : []
if (!tasks.length) {
  log('No tasks passed. Usage: Workflow({ name:"content-finish-loop", args:[{label,brief,platform,voiceFile,skillFiles,outFile}] })')
  return { error: 'no tasks' }
}

const SCHEMA = {
  type: 'object',
  required: ['label', 'final_text', 'gate_verdict', 'iterations', 'out_file'],
  properties: {
    label: { type: 'string' },
    final_text: { type: 'string', description: 'the finished piece, gate-CLEAN' },
    gate_verdict: { type: 'string', enum: ['CLEAN', 'WARN', 'FAIL'], description: 'final content_finish_gate verdict — must be CLEAN or WARN to return' },
    iterations: { type: 'integer', description: 'how many produce→gate cycles it took' },
    out_file: { type: 'string' },
    fixed: { type: 'array', items: { type: 'string' }, description: 'banned moves caught + fixed by the gate' },
  },
}

const results = await pipeline(
  tasks,
  (t) => agent(
    `Write the piece for: ${t.label}\nPlatform: ${t.platform || 'linkedin'}\n\nBRIEF:\n${t.brief}\n\n` +
    `STEP 1 — LOAD THE REAL VOICE + SKILLS (this is non-negotiable; the failure that created this loop was skipping it):\n` +
    (t.voiceFile ? `• Voice: read ${t.voiceFile} and write in THIS person's actual voice + vocabulary.\n` : '') +
    (t.skillFiles && t.skillFiles.length ? `• Skills: read ${t.skillFiles.join(', ')} and apply their methodology (insight-vectors, proof-braid, hooks, etc.).\n` : '') +
    `• Format: read skills/lara-acosta-linkedin-mastery/genius.md for ${t.platform || 'linkedin'} structure (≤14-word scroll-stop hook, whitespace/F-shape, strong non-cheap close).\n\n` +
    `STEP 2 — WRITE it to ${t.outFile}.\n\n` +
    `STEP 3 — SELF-GATE (the loop). Run:\n` +
    `   python3 execution/content_finish_gate.py check --file ${t.outFile} --platform ${t.platform || 'linkedin'} --label "${t.label}"\n` +
    `If it exits non-zero (FAIL), READ the flags, rewrite the offending lines (kill em-dashes >2, "It's not X. It's Y." reveals, triple anaphora, "here's the part nobody…", cheap-question closes; tighten the hook to ≤14 words), rewrite ${t.outFile}, and run the gate AGAIN. Repeat until it returns CLEAN. Max 4 cycles.\n\n` +
    `STEP 4 — Return the final text, the CLEAN verdict, the iteration count, and the list of banned moves you fixed. Do NOT return until the gate is CLEAN.`,
    { label: `finish:${t.label}`, phase: 'Produce+Gate', schema: SCHEMA }
  ),
)

return results.map(r => ({
  label: r.label, gate_verdict: r.gate_verdict, iterations: r.iterations,
  fixed: r.fixed || [], out_file: r.out_file, final_text: r.final_text,
}))
