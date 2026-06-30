(function () {
  const params = new URLSearchParams(window.location.search);
  const editMode = params.get("edit") === "1";
  if (!editMode) return;

  const style = document.createElement("style");
  style.textContent = `
    body.portfolio-editing [data-edit-id] {
      outline: 1px dashed rgba(176, 141, 79, 0.7);
      outline-offset: 4px;
      cursor: text;
    }

    body.portfolio-editing [data-edit-id]:focus {
      outline: 2px solid #b08d4f;
      background: rgba(176, 141, 79, 0.12);
    }

    .portfolio-editor-toolbar {
      position: fixed;
      left: 16px;
      right: 16px;
      bottom: 16px;
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      padding: 12px;
      background: rgba(20, 23, 31, 0.94);
      border: 1px solid rgba(176, 141, 79, 0.55);
      box-shadow: 0 18px 50px rgba(0, 0, 0, 0.3);
      color: #f3f0e9;
      font: 600 13px/1.3 Inter, system-ui, sans-serif;
    }

    .portfolio-editor-toolbar button,
    .portfolio-editor-toolbar a {
      border: 1px solid rgba(243, 240, 233, 0.24);
      background: #2e4034;
      color: #f3f0e9;
      padding: 8px 10px;
      font: inherit;
      cursor: pointer;
    }

    .portfolio-editor-toolbar button:hover,
    .portfolio-editor-toolbar a:hover {
      background: #3f5a48;
    }

    .portfolio-editor-status {
      color: #b08d4f;
      margin-left: auto;
    }

    @media print {
      .portfolio-editor-toolbar {
        display: none !important;
      }
    }
  `;
  document.head.appendChild(style);

  function makeToolbar() {
    const toolbar = document.createElement("div");
    toolbar.className = "portfolio-editor-toolbar";
    toolbar.innerHTML = `
      <strong>Portfolio editor</strong>
      <button type="button" data-editor-save>Save text</button>
      <button type="button" data-editor-pdf>Regenerate PDF</button>
      <button type="button" data-editor-export>Download JSON</button>
      <button type="button" data-editor-token>Set CMS token</button>
      <button type="button" data-editor-clear>Clear saved edits</button>
      <a href="/" data-editor-exit>Exit edit mode</a>
      <span class="portfolio-editor-status" data-editor-status>Click text to edit.</span>
    `;
    document.body.appendChild(toolbar);
    return toolbar;
  }

  function collectEdits() {
    const edits = {};
    document.querySelectorAll("[data-edit-id]").forEach((element) => {
      const id = element.dataset.editId;
      const value = element.innerHTML.trim();
      if (value !== window.PortfolioText.originals[id]) {
        edits[id] = value;
      }
    });
    return edits;
  }

  function downloadJson(edits) {
    const blob = new Blob([JSON.stringify(edits, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "site-edits.json";
    link.click();
    URL.revokeObjectURL(url);
  }

  async function saveEdits(status) {
    const edits = collectEdits();
    try {
      const response = await fetch("/save-edits", {
        method: "POST",
        headers: editorHeaders(),
        body: JSON.stringify(edits, null, 2)
      });

      if (!response.ok) throw new Error(`Save failed: ${response.status}`);
      status.textContent = "Saved to site-edits.json";
      window.PortfolioText.overrides = edits;
    } catch (error) {
      status.textContent = "Could not save automatically. Download JSON instead.";
      console.warn(error);
    }
  }

  async function clearEdits(status) {
    try {
      const response = await fetch("/save-edits", {
        method: "POST",
        headers: editorHeaders(),
        body: "{}"
      });

      if (!response.ok) throw new Error(`Clear failed: ${response.status}`);
      status.textContent = "Saved edits cleared. Reloading...";
      setTimeout(() => window.location.reload(), 500);
    } catch (error) {
      status.textContent = "Could not clear automatically.";
      console.warn(error);
    }
  }

  function editorHeaders() {
    const headers = { "Content-Type": "application/json" };
    const token = window.localStorage.getItem("portfolioCmsToken");
    if (token) headers.Authorization = `Bearer ${token}`;
    return headers;
  }

  function setToken(status) {
    const current = window.localStorage.getItem("portfolioCmsToken") || "";
    const token = window.prompt("CMS token for a hosted editor. Leave blank to clear.", current);
    if (token === null) return;

    if (token.trim()) {
      window.localStorage.setItem("portfolioCmsToken", token.trim());
      status.textContent = "CMS token saved in this browser.";
    } else {
      window.localStorage.removeItem("portfolioCmsToken");
      status.textContent = "CMS token cleared.";
    }
  }

  async function exportPdf(status) {
    status.textContent = "Regenerating PDF...";

    try {
      await saveEdits(status);
      const response = await fetch("/export-pdf", {
        method: "POST",
        headers: editorHeaders(),
        body: "{}"
      });
      const result = await response.json();
      if (!response.ok || !result.ok) throw new Error(result.error || `PDF export failed: ${response.status}`);

      status.innerHTML = `PDF regenerated: <a href="${result.pdf}" target="_blank" rel="noreferrer">${result.pdf}</a>`;
    } catch (error) {
      status.textContent = "Could not regenerate PDF. Ask Codex to export it.";
      console.warn(error);
    }
  }

  window.PortfolioText.ready.then(() => {
    document.body.classList.add("portfolio-editing");
    window.PortfolioText.assignEditIds();
    document.querySelectorAll("[data-edit-id]").forEach((element) => {
      element.setAttribute("contenteditable", "true");
      element.setAttribute("spellcheck", "true");
    });

    const toolbar = makeToolbar();
    const status = toolbar.querySelector("[data-editor-status]");

    toolbar.querySelector("[data-editor-save]").addEventListener("click", () => saveEdits(status));
    toolbar.querySelector("[data-editor-pdf]").addEventListener("click", () => exportPdf(status));
    toolbar.querySelector("[data-editor-export]").addEventListener("click", () => downloadJson(collectEdits()));
    toolbar.querySelector("[data-editor-token]").addEventListener("click", () => setToken(status));
    toolbar.querySelector("[data-editor-clear]").addEventListener("click", () => clearEdits(status));
  });
})();
