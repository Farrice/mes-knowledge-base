(function () {
  const originals = {};
  const EDITABLE_SELECTOR = [
    ".brand span:last-child",
    ".top-nav a",
    "main h1",
    "main h2",
    "main h3",
    "main p",
    "main article span",
    "main strong",
    "main small",
    "main dt",
    "main dd",
    "main figcaption",
    ".button",
    ".site-footer p"
  ].join(",");

  function scopeFor(element) {
    const scope = element.closest("section[id], section, header, footer, .proof-lens");
    if (!scope) return "page";
    if (scope.id) return scope.id;
    if (scope.classList.contains("hero")) return "hero";
    if (scope.classList.contains("proof-lens")) return "proof-lens";
    if (scope.tagName === "HEADER") return "header";
    if (scope.tagName === "FOOTER") return "footer";
    return "section";
  }

  function assignEditIds(root = document) {
    const counts = new Map();
    const elements = Array.from(root.querySelectorAll(EDITABLE_SELECTOR)).filter((element) => {
      if (!element.textContent.trim()) return false;
      if (element.closest(".dot-rail")) return false;
      if (element.parentElement && element.parentElement.closest(EDITABLE_SELECTOR)) return false;
      return true;
    });

    elements.forEach((element) => {
      if (element.dataset.editId) return;
      const scope = scopeFor(element);
      const tag = element.tagName.toLowerCase();
      const key = `${scope}-${tag}`;
      const next = (counts.get(key) || 0) + 1;
      counts.set(key, next);
      element.dataset.editId = `${key}-${next}`;

      if (!(element.dataset.editId in originals)) {
        originals[element.dataset.editId] = element.innerHTML.trim();
      }
    });

    return elements;
  }

  function sanitize(html) {
    const template = document.createElement("template");
    template.innerHTML = html;
    template.content.querySelectorAll("script, style, iframe, object, embed").forEach((node) => node.remove());
    template.content.querySelectorAll("*").forEach((node) => {
      for (const attr of Array.from(node.attributes)) {
        if (attr.name.startsWith("on")) node.removeAttribute(attr.name);
        if (attr.name === "style") node.removeAttribute(attr.name);
      }
    });
    return template.innerHTML;
  }

  function applyOverrides(overrides) {
    const elements = assignEditIds();
    elements.forEach((element) => {
      const edit = overrides[element.dataset.editId];
      if (typeof edit === "string") {
        element.innerHTML = sanitize(edit);
      }
    });
  }

  async function loadOverrides() {
    try {
      const response = await fetch("site-edits.json", { cache: "no-store" });
      if (!response.ok) return {};
      return await response.json();
    } catch (_error) {
      return {};
    }
  }

  const ready = document.readyState === "loading"
    ? new Promise((resolve) => document.addEventListener("DOMContentLoaded", resolve, { once: true }))
    : Promise.resolve();

  window.PortfolioText = {
    assignEditIds,
    applyOverrides,
    loadOverrides,
    originals,
    overrides: {},
    ready: ready.then(async () => {
      assignEditIds();
      const overrides = await loadOverrides();
      window.PortfolioText.overrides = overrides;
      applyOverrides(overrides);
      return overrides;
    })
  };
})();
