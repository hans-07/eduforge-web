const theme = document.querySelector(".theme");
const root = document.documentElement;
const preference = matchMedia("(prefers-color-scheme: light)");
let savedTheme;
try {
  savedTheme = localStorage.getItem("eduforge-theme");
} catch {
  // The theme can still be changed for the current page.
}
function setTheme(value) {
  root.dataset.theme = value;
  theme.setAttribute("aria-pressed", String(value === "light"));
}
setTheme(savedTheme || (preference.matches ? "light" : "dark"));
theme.hidden = false;
preference.addEventListener("change", (event) => {
  if (!savedTheme) setTheme(event.matches ? "light" : "dark");
});
theme.addEventListener("click", () => {
  savedTheme = root.dataset.theme === "dark" ? "light" : "dark";
  setTheme(savedTheme);
  try {
    localStorage.setItem("eduforge-theme", savedTheme);
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
