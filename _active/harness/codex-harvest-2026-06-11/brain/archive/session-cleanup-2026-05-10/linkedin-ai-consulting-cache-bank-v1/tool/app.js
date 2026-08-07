const form = document.querySelector("#misfire-form");
const report = document.querySelector("#report");
const emptyState = document.querySelector("#empty-state");
const reportActions = document.querySelector("#report-actions");
const copyButton = document.querySelector("#copy-report");
const mailto = document.querySelector("#mailto-report");

const genericPhrases = [
  "unlock",
  "streamline",
  "transform",
  "high-quality",
  "save time",
  "leverage",
  "cutting-edge",
  "revolutionize",
  "seamless",
  "at scale",
  "book a call",
  "let's talk"
];

const buyerLanguage = [
  "close",
  "can't send",
  "cannot send",
  "not what we mean",
  "fix",
  "rewrite",
  "rescue",
  "missed",
  "generic",
  "sounds like ai",
  "not us",
  "trust"
];

const proofWords = ["proof", "example", "case", "result", "because", "before", "after", "evidence", "data"];
const boundaryWords = ["avoid", "never", "must not", "do not", "unless", "stop", "ask", "verify"];
const sourceWords = ["source", "customer", "buyer", "research", "call", "voice", "transcript", "example"];
const mechanismWords = ["rule", "system", "process", "framework", "map", "diagnostic", "workflow", "standard"];

function includesAny(text, terms) {
  const lower = text.toLowerCase();
  return terms.some((term) => lower.includes(term));
}

function countMatches(text, terms) {
  const lower = text.toLowerCase();
  return terms.reduce((count, term) => count + (lower.includes(term) ? 1 : 0), 0);
}

function sentenceSnippet(text) {
  const cleaned = text.replace(/\s+/g, " ").trim();
  if (!cleaned) return "No artifact supplied.";
  const first = cleaned.split(/[.!?]/).find(Boolean) || cleaned;
  return first.slice(0, 180);
}

function buildGuesses(data) {
  const text = `${data.artifact} ${data.desiredOutcome} ${data.feltOff}`;
  const guesses = [];
  const genericCount = countMatches(data.artifact, genericPhrases);

  if (genericCount > 0 || !includesAny(text, buyerLanguage)) {
    guesses.push({
      title: "Buyer language gap",
      diagnosis: "The output may be using category language before it proves it understands the buyer's private sentence.",
      missing: "Real phrases, objections, and frustration language from the person this is meant to move."
    });
  }

  if (!includesAny(data.artifact, proofWords)) {
    guesses.push({
      title: "Proof rule missing",
      diagnosis: "The artifact makes a claim but does not show why the claim should be trusted.",
      missing: "A proof hierarchy: example, result, before/after, source, or observed pattern."
    });
  }

  if (!includesAny(data.artifact, mechanismWords)) {
    guesses.push({
      title: "Mechanism is invisible",
      diagnosis: "The output gestures at a result without explaining the operating layer that produces it.",
      missing: "A named rule, map, process, or standard that makes the work repeatable."
    });
  }

  if (data.artifact.toLowerCase().includes("book a call") || data.artifact.toLowerCase().includes("let's talk")) {
    guesses.push({
      title: "CTA timing rushed",
      diagnosis: "The output asks for time before it has earned enough trust or shown the diagnostic value.",
      missing: "An artifact-first next step: send one output, try the tool, or inspect one before/after."
    });
  }

  if (!includesAny(data.artifact, sourceWords)) {
    guesses.push({
      title: "No source of truth",
      diagnosis: "The model appears to be writing from generic category memory instead of a ranked source.",
      missing: "Customer language, call notes, offer rules, examples, or a known standard to trust first."
    });
  }

  if (!includesAny(data.artifact, boundaryWords)) {
    guesses.push({
      title: "Boundary missing",
      diagnosis: "The output does not tell AI what not to infer, where to stop, or when to ask.",
      missing: "Do-not-cross rules, escalation triggers, verification requirements, and stopping conditions."
    });
  }

  if (data.feltOff.trim()) {
    guesses.unshift({
      title: "Founder judgment signal",
      diagnosis: `"${data.feltOff.trim().slice(0, 160)}" is not a complaint. It is diagnostic data.`,
      missing: "Turn that correction into a reusable rule, example, counterexample, or quality test."
    });
  }

  return guesses.slice(0, 7);
}

function buildPrimitive(data, guesses) {
  const topMissing = guesses[0]?.missing || "a clearer rule for the work";
  const intended = data.desiredOutcome.trim() || "move the right buyer toward the next step";
  const felt = data.feltOff.trim() || "the output felt close but not trustworthy";
  return [
    "WORK PRIMITIVE STARTER",
    "",
    `Artifact type: ${data.artifactType}`,
    `Job to be done: ${intended}`,
    `Quality signal: If the reviewer says "${felt}", the output has not passed.`,
    `First missing rule: ${topMissing}`,
    "",
    "Before AI writes, it must know:",
    "1. the buyer's private sentence",
    "2. the proof standard",
    "3. the source of truth",
    "4. the CTA timing",
    "5. what it must not invent"
  ].join("\n");
}

function buildReport(data) {
  const guesses = buildGuesses(data);
  const genericCount = countMatches(data.artifact, genericPhrases);
  const score = Math.max(18, Math.min(92, 84 - genericCount * 7 - Math.max(0, 5 - guesses.length) * 3));
  const primitive = buildPrimitive(data, guesses);
  const snippet = sentenceSnippet(data.artifact);
  return { guesses, score, primitive, snippet };
}

function renderReport(data, result) {
  const guessItems = result.guesses
    .map(
      (guess) => `
        <li>
          <strong>${guess.title}</strong><br />
          ${guess.diagnosis}<br />
          <span class="muted">Missing: ${guess.missing}</span>
        </li>
      `
    )
    .join("");

  report.innerHTML = `
    <div class="score">
      <strong>${result.score}</strong>
      <div>
        <h3>Trust-readiness score</h3>
        <p>This is a directional score, not a claim of quality. It estimates how much hidden judgment the artifact may still need before AI can be trusted with this work.</p>
      </div>
    </div>
    <div>
      <h3>Artifact read</h3>
      <p>${result.snippet}</p>
    </div>
    <div>
      <h3>Likely guess points</h3>
      <ul class="guess-list">${guessItems}</ul>
    </div>
    <div class="primitive">
      <h3>First agent-ready primitive</h3>
      <code>${result.primitive}</code>
    </div>
    <div>
      <h3>Suggested next step</h3>
      <p>If these guesses repeat across more than one artifact, this is bigger than a prompt tweak. A paid Misfire Map would turn the repeated correction into a reusable rule, example, boundary, source of truth, or quality test.</p>
    </div>
  `;

  const plainReport = [
    "AI MISFIRE DIAGNOSTIC REPORT",
    "",
    `Name: ${data.name || "Not provided"}`,
    `Email: ${data.email || "Not provided"}`,
    `Artifact type: ${data.artifactType}`,
    `Trust-readiness score: ${result.score}`,
    "",
    "Likely guess points:",
    ...result.guesses.map((guess, index) => `${index + 1}. ${guess.title}: ${guess.diagnosis} Missing: ${guess.missing}`),
    "",
    result.primitive
  ].join("\n");

  report.dataset.plain = plainReport;
  localStorage.setItem("aiMisfireDiagnosticReport", plainReport);
  const subject = encodeURIComponent("AI Misfire Diagnostic Report");
  const body = encodeURIComponent(plainReport);
  mailto.href = `mailto:${encodeURIComponent(data.email || "")}?subject=${subject}&body=${body}`;
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const data = {
    name: document.querySelector("#name").value.trim(),
    email: document.querySelector("#email").value.trim(),
    artifactType: document.querySelector("#artifact-type").value,
    desiredOutcome: document.querySelector("#desired-outcome").value.trim(),
    artifact: document.querySelector("#artifact").value.trim(),
    feltOff: document.querySelector("#felt-off").value.trim()
  };

  if (!data.artifact) {
    document.querySelector("#artifact").focus();
    return;
  }

  const result = buildReport(data);
  renderReport(data, result);
  emptyState.classList.add("hidden");
  report.classList.remove("hidden");
  reportActions.classList.remove("hidden");
});

copyButton.addEventListener("click", async () => {
  const text = report.dataset.plain || "";
  if (!text) return;
  await navigator.clipboard.writeText(text);
  copyButton.textContent = "Copied";
  setTimeout(() => {
    copyButton.textContent = "Copy report";
  }, 1400);
});

