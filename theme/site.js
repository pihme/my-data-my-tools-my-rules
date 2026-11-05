// Progressive enhancement only: without JS every page still works
// (category links jump to their section, all cards stay visible).
(function () {
  var root = document.documentElement;

  // Dark / light toggle (remembers the choice; default follows the system).
  var mode = document.querySelector(".mode");
  if (mode) {
    mode.hidden = false;
    mode.addEventListener("click", function () {
      var dark = root.classList.contains("dark") ||
        (!root.classList.contains("light") && matchMedia("(prefers-color-scheme: dark)").matches);
      root.classList.remove("dark", "light");
      root.classList.add(dark ? "light" : "dark");
      try { localStorage.setItem("mdmtmr-mode", dark ? "light" : "dark"); } catch (e) {}
    });
  }

  // Catalog filters (index page only). Groups combine with AND, and with the active category.
  var cards = document.querySelectorAll(".card[data-cat]");
  var bar = document.querySelector(".filterbar");
  if (!cards.length || !bar) return;
  bar.hidden = false;
  var groups = ["lic", "run", "aud"];
  var state = { lic: "all", run: "all", aud: "all", cat: "all" };
  var navLinks = document.querySelectorAll(".cats a[data-cat]");
  var empty = document.querySelector(".empty");

  function has(list, v) { return (" " + list + " ").indexOf(" " + v + " ") >= 0; }

  function apply() {
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (state.lic === "all" || has(c.dataset.kinds, state.lic)) &&
        (state.run === "all" || has(c.dataset.kinds, state.run)) &&
        (state.aud === "all" || c.dataset.aud === state.aud) &&
        (state.cat === "all" || c.dataset.cat === state.cat);
      c.hidden = !ok;
      if (ok) shown++;
    });
    document.querySelectorAll("section.cat").forEach(function (s) {
      var n = s.querySelectorAll(".card:not([hidden])").length;
      s.hidden = n === 0;
      var k = Math.max(1, Math.min(n, 4));
      s.className = s.className.replace(/\bspan-\d\b/, "span-" + k);
      s.style.setProperty("--n", k);
      var cnt = s.querySelector(".cnt");
      if (cnt) cnt.textContent = n + (n === 1 ? " entry" : " entries");
    });
    groups.forEach(function (g) {
      bar.querySelectorAll("button[data-" + g + "]").forEach(function (b) {
        var on = b.getAttribute("data-" + g) === state[g];
        b.classList.toggle("on", on);
        b.setAttribute("aria-pressed", on ? "true" : "false");
      });
    });
    var filtered = groups.some(function (g) { return state[g] !== "all"; }) || state.cat !== "all";
    bar.classList.toggle("is-filtered", filtered);
    navLinks.forEach(function (a) { a.classList.toggle("on", a.dataset.cat === state.cat); });
    if (empty) empty.hidden = shown > 0;
  }

  function reset() {
    groups.forEach(function (g) { state[g] = "all"; });
    state.cat = "all";
    history.replaceState(null, "", location.pathname);
    apply();
  }

  bar.addEventListener("click", function (e) {
    var b = e.target.closest("button");
    if (!b) return;
    if (b.classList.contains("freset")) { reset(); return; }
    groups.forEach(function (g) { if (b.hasAttribute("data-" + g)) state[g] = b.getAttribute("data-" + g); });
    apply();
  });
  document.querySelectorAll(".empty .freset").forEach(function (r) { r.addEventListener("click", reset); });
  navLinks.forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      state.cat = (state.cat === a.dataset.cat) ? "all" : a.dataset.cat;
      history.replaceState(null, "", state.cat === "all" ? location.pathname : "#" + state.cat);
      apply();
      window.scrollTo({ top: 0 });
    });
  });
  var h = decodeURIComponent(location.hash.slice(1));
  if (h && document.querySelector('.cats a[data-cat="' + h + '"]')) state.cat = h;
  apply();
})();
