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

  // Catalog filters + search (index page only). Groups and search combine with AND.
  var cards = document.querySelectorAll(".card[data-cat]");
  var bar = document.querySelector(".filterbar");
  if (!cards.length || !bar) return;
  bar.hidden = false;
  // Search row has its own hidden so it stays gone without JS even if CSS
  // ever pulls it out of .filterbar (e.g. mobile display:contents quirks).
  var searchRow = bar.querySelector(".fsearch-row");
  if (searchRow) searchRow.hidden = false;
  var groups = ["lic", "run", "aud"];
  var state = { lic: "all", run: "all", aud: "all", cat: "all", q: "" };
  var navLinks = document.querySelectorAll(".cats a[data-cat]");
  var empty = document.querySelector(".empty");
  var status = document.getElementById("filter-status");
  var search = document.getElementById("search");

  function has(list, v) { return (" " + list + " ").indexOf(" " + v + " ") >= 0; }

  function fold(s) {
    try {
      s = s.normalize("NFKD").replace(/[\u0300-\u036f]/g, "");
    } catch (e) {}
    return s.toLowerCase().replace(/\s+/g, " ").trim();
  }

  function searchMatch(blob, q) {
    if (!q) return true;
    var terms = fold(q).split(" ").filter(Boolean);
    if (!terms.length) return true;
    var hay = blob || "";
    for (var i = 0; i < terms.length; i++) {
      if (hay.indexOf(terms[i]) < 0) return false;
    }
    return true;
  }

  function syncUrl() {
    var q = state.q ? ("?q=" + encodeURIComponent(state.q)) : "";
    var h = state.cat !== "all" ? ("#" + state.cat) : "";
    history.replaceState(null, "", location.pathname + q + h);
  }

  function apply() {
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (state.lic === "all" || has(c.dataset.kinds, state.lic)) &&
        (state.run === "all" || has(c.dataset.kinds, state.run)) &&
        (state.aud === "all" || c.dataset.aud === state.aud) &&
        (state.cat === "all" || c.dataset.cat === state.cat) &&
        searchMatch(c.dataset.search || "", state.q);
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
    var filtered = groups.some(function (g) { return state[g] !== "all"; }) ||
      state.cat !== "all" || !!state.q;
    bar.classList.toggle("is-filtered", filtered);
    navLinks.forEach(function (a) { a.classList.toggle("on", a.dataset.cat === state.cat); });
    if (empty) empty.hidden = shown > 0;
    if (status) status.textContent = shown + (shown === 1 ? " project shown" : " projects shown");
  }

  function reset() {
    groups.forEach(function (g) { state[g] = "all"; });
    state.cat = "all";
    state.q = "";
    if (search) search.value = "";
    history.replaceState(null, "", location.pathname);
    apply();
  }

  function setQuery(raw) {
    state.q = raw;
    syncUrl();
    apply();
  }

  bar.addEventListener("click", function (e) {
    var b = e.target.closest("button");
    if (!b) return;
    if (b.classList.contains("freset")) { reset(); return; }
    groups.forEach(function (g) { if (b.hasAttribute("data-" + g)) state[g] = b.getAttribute("data-" + g); });
    syncUrl();
    apply();
  });
  document.querySelectorAll(".empty .freset").forEach(function (r) { r.addEventListener("click", reset); });
  navLinks.forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      state.cat = (state.cat === a.dataset.cat) ? "all" : a.dataset.cat;
      syncUrl();
      apply();
      window.scrollTo({ top: 0 });
    });
  });

  if (search) {
    search.addEventListener("input", function () { setQuery(search.value); });
    search.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        e.preventDefault();
        search.value = "";
        setQuery("");
      }
    });
  }

  document.addEventListener("keydown", function (e) {
    if (e.key !== "/" || e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target;
    if (!t) return;
    var tag = (t.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea" || tag === "select" || t.isContentEditable) return;
    if (!search) return;
    e.preventDefault();
    search.focus();
  });

  var focusSearch = false;
  var h = decodeURIComponent(location.hash.slice(1));
  if (h === "search") {
    focusSearch = true;
  } else if (h && document.querySelector('.cats a[data-cat="' + h + '"]')) {
    state.cat = h;
  }
  try {
    var params = new URLSearchParams(location.search);
    if (params.has("q")) {
      state.q = params.get("q") || "";
      if (search) search.value = state.q;
    }
  } catch (e) {}
  apply();
  if (focusSearch && search) {
    search.focus();
    // Drop #search from the URL without a history entry so Back stays useful,
    // but keep any ?q= and category hash after focus.
    if (location.hash === "#search") {
      history.replaceState(null, "", location.pathname + location.search +
        (state.cat !== "all" ? "#" + state.cat : ""));
    }
  }
})();

/* right-edge fade on horizontally scrollable filter rows */
(function () {
  var groups = document.querySelectorAll(".filterbar .fgroup");
  function upd(g) {
    var p = g.querySelector(".pills");
    if (!p) return;
    g.style.setProperty("--ph", p.offsetHeight + "px");
    g.classList.toggle("more", p.scrollWidth - p.clientWidth - p.scrollLeft > 2);
  }
  function all() { groups.forEach(upd); }
  groups.forEach(function (g) {
    var p = g.querySelector(".pills");
    if (p) p.addEventListener("scroll", function () { upd(g); }, { passive: true });
  });
  window.addEventListener("resize", all);
  window.addEventListener("load", all);
  all();
})();
