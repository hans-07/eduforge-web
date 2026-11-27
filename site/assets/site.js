const theme = document.querySelector(".theme");
const preference = matchMedia("(prefers-color-scheme: light)");
const choices = ["system", "light", "dark"];
let selection = "system";
try {
  const stored = localStorage.getItem("eduforge-theme");
  if (choices.includes(stored)) selection = stored;
} catch {
  // Theme selection remains available without local storage.
}
function applyTheme() {
  document.documentElement.dataset.theme = selection === "system"
    ? (preference.matches ? "light" : "dark") : selection;
}
theme.value = selection;
applyTheme();
theme.hidden = false;
preference.addEventListener("change", () => {
  if (selection === "system") applyTheme();
});
theme.addEventListener("change", () => {
  selection = theme.value;
  applyTheme();
  try {
    localStorage.setItem("eduforge-theme", selection);
  } catch {
    // Keep the selection for this page.
  }
});

const gallery = document.querySelector("[data-gallery]");
if (gallery) {
  const screenshot = gallery.querySelector("[data-screenshot]");
  const caption = gallery.querySelector("figcaption");
  const views = [...gallery.querySelectorAll(".view")];

  for (const view of views) {
    view.addEventListener("click", (event) => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      screenshot.src = view.href;
      screenshot.alt = view.dataset.caption;
      caption.textContent = view.dataset.caption;
      for (const item of views) item.removeAttribute("aria-current");
      view.setAttribute("aria-current", "true");
    });
  }
}

const search = document.querySelector(".doc-search");
if (search) {
  const entries = [...document.querySelectorAll("[data-guide]")];
  const feedback = document.querySelector(".doc-search-status");
  const normalize = (value) => value.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase();
  search.hidden = false;
  search.addEventListener("input", () => {
    const terms = normalize(search.value).trim().split(/\s+/).filter(Boolean);
    for (const entry of entries) {
      const content = normalize(entry.dataset.guide);
      entry.hidden = !terms.every((term) => content.includes(term));
    }
    feedback.hidden = entries.some((entry) => !entry.hidden);
  });
}
