const sections = [...document.querySelectorAll("main section[id], main .hero")];
const railLinks = [...document.querySelectorAll(".dot-rail a")];

const byHash = new Map(
  railLinks.map((link) => [link.getAttribute("href").replace("#", ""), link])
);

const observer = new IntersectionObserver(
  (entries) => {
    const visible = entries
      .filter((entry) => entry.isIntersecting)
      .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

    if (!visible) return;

    const id = visible.target.id || "top";
    railLinks.forEach((link) => link.classList.remove("active"));
    const link = byHash.get(id);
    if (link) link.classList.add("active");
  },
  { rootMargin: "-35% 0px -45% 0px", threshold: [0.1, 0.3, 0.6] }
);

sections.forEach((section) => observer.observe(section));
