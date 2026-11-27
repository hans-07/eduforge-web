(() => {
  const panel = document.querySelector("[data-releases]");
  const status = panel.querySelector("[role=status]");
  const list = panel.querySelector("ul");
  const lang = document.documentElement.lang;
  const official = "https://github.com/hans-07/eduforge-releases/releases";
  const endpoint = "https://api.github.com/repos/hans-07/eduforge-releases/releases";
  const tagPattern = /^v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[\w.-]+)?$/;
  const formatDate = new Intl.DateTimeFormat(lang, { dateStyle: "long", timeZone: "UTC" });
  const formatBytes = new Intl.NumberFormat(lang, { style: "unit", unit: "megabyte", maximumFractionDigits: 2 });
  const link = (label, url) => Object.assign(document.createElement("a"), { textContent: label, href: url });

  function releaseFrom(record) {
    const tag = record?.tag_name;
    if (typeof tag !== "string" || !tagPattern.test(tag) || record.draft !== false) return null;
    const date = new Date(record.published_at || NaN);
    if (!Number.isFinite(date.getTime()) || !Array.isArray(record.assets)) return null;
    const filename = "EduForge-Studio-" + tag + "-windows-x64-setup.exe";
    const assetBase = official + "/download/" + tag + "/";
    const find = (name) => record.assets.find((asset) =>
      asset?.name === name && asset.state === "uploaded" &&
      Number.isSafeInteger(asset.size) && asset.size > 0 &&
      asset.browser_download_url === assetBase + name);
    const installer = find(filename);
    const checksum = find(filename + ".sha256");
    return {
      tag, date, installer, checksum,
      stable: record.prerelease === false && !tag.includes("-"),
    };
  }

  function render(release) {
    const row = document.createElement("li");
    const notes = link(release.tag, official + "/tag/" + release.tag);
    const date = document.createElement("time");
    date.dateTime = release.date.toISOString();
    date.textContent = formatDate.format(release.date);
    row.append(notes, " · ", date);
    if (release.installer && release.checksum) {
      row.append(
        " · ", link("Windows x64 (" + formatBytes.format(release.installer.size / 1e6) + ")", release.installer.browser_download_url),
        " · ", link("SHA-256", release.checksum.browser_download_url),
      );
    }
    return row;
  }

  async function load() {
    const response = await fetch(endpoint + "?per_page=100", {
      credentials: "omit",
      headers: { Accept: "application/vnd.github+json" },
      signal: AbortSignal.timeout(6500),
    });
    if (!response.ok) throw Error("GitHub Releases: " + response.status);
    const records = await response.json();
    if (!Array.isArray(records)) throw Error("Invalid release list");
    const releases = records.map(releaseFrom).filter(Boolean)
      .sort((a, b) => b.date - a.date);
    const stable = releases.find((release) => release.stable && release.installer && release.checksum);
    if (stable) {
      status.textContent = panel.dataset.stable + " ";
      status.append(link(stable.tag, official + "/tag/" + stable.tag));
    } else {
      status.textContent = panel.dataset.empty;
    }
    list.replaceChildren(...releases.map(render));
    list.hidden = releases.length === 0;
  }

  load().catch(() => { status.textContent = panel.dataset.unavailable; });
})();
