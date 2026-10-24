/* Learning with Differences — Glossary Explorer.
 * Classic script (no modules) so it also works from file://.
 * Mounts on any page containing [data-lwd-explorer]; re-mounts on
 * instant navigation via document$. Data comes from glossary.js, whose
 * URL is read from a Markdown link Zensical has already rewritten. */
(function () {
  "use strict";

  var PAGE = 50;
  var pending = {};

  function loadScript(src, globalName) {
    if (window[globalName]) return Promise.resolve(window[globalName]);
    if (pending[src]) return pending[src];
    pending[src] = new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src;
      s.async = true;
      s.onload = function () {
        if (window[globalName]) resolve(window[globalName]);
        else reject(new Error("data did not define " + globalName));
      };
      s.onerror = function () { delete pending[src]; reject(new Error("could not load " + src)); };
      document.head.appendChild(s);
    });
    return pending[src];
  }

  function norm(text) {
    return String(text || "")
      .normalize("NFKD").replace(/[̀-ͯ]/g, "")
      .toLowerCase()
      .replace(/[^a-z0-9#+.\s]/g, " ")
      .replace(/\s+/g, " ").trim();
  }

  function words(text) { return norm(text).split(" ").filter(Boolean); }

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        if (k === "text") node.textContent = attrs[k];
        else if (k === "class") node.className = attrs[k];
        else node.setAttribute(k, attrs[k]);
      });
    }
    (children || []).forEach(function (c) {
      if (c == null) return;
      node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    });
    return node;
  }

  function editDistance(a, b, cap) {
    if (Math.abs(a.length - b.length) > cap) return cap + 1;
    var prev = [], cur, i, j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur = [i];
      var best = i;
      for (j = 1; j <= b.length; j++) {
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        if (cur[j] < best) best = cur[j];
      }
      if (best > cap) return cap + 1;
      prev = cur;
    }
    return prev[b.length];
  }

  function prepare(data) {
    var labels = {};
    Object.keys(data.facets).forEach(function (f) {
      labels[f] = {};
      data.facets[f].forEach(function (v) { labels[f][v.id] = v.label; });
    });
    data.terms.forEach(function (t) {
      t._title = norm(t.title);
      t._titleWords = words(t.title);
      t._acr = (t.acronyms || []).map(norm);
      t._alias = (t.aliases || []).map(norm);
      t._former = (t.formerly || []).map(norm);
      t._summaryWords = words(t.summary);
      t._facetText = norm([labels.domains[t.domain], labels.clouds[t.cloud], labels.levels[t.level]]
        .concat((t.tracks || []).map(function (x) { return labels.tracks[x]; })).join(" "));
      t._hasEq = (t.equivalents || []).length > 0;
    });
    data._labels = labels;
    return data;
  }

  /* Score one term for the query tokens; null when a token matches nothing. */
  function score(t, tokens, whole) {
    if (!tokens.length) return { score: 0, via: "" };
    var total = 0, via = "";
    for (var i = 0; i < tokens.length; i++) {
      var tok = tokens[i], best = 0, why = "";
      function consider(s, w) { if (s > best) { best = s; why = w; } }
      t._acr.forEach(function (a) { if (a === tok) consider(100, "acronym"); else if (a.indexOf(tok) === 0) consider(60, "acronym"); });
      if (t._title === tok) consider(90, "");
      else if (t._title.indexOf(tok) === 0) consider(70, "");
      else if (t._titleWords.some(function (w) { return w.indexOf(tok) === 0; })) consider(50, "");
      t._alias.forEach(function (a, k) {
        if (a === tok) consider(80, "alias: " + t.aliases[k]);
        else if (a.indexOf(tok) === 0 || a.split(" ").some(function (w) { return w.indexOf(tok) === 0; })) consider(45, "alias: " + t.aliases[k]);
      });
      t._former.forEach(function (a, k) {
        if (a === tok) consider(80, "formerly: " + t.formerly[k]);
        else if (a.indexOf(tok) === 0 || a.split(" ").some(function (w) { return w.indexOf(tok) === 0; })) consider(45, "formerly: " + t.formerly[k]);
      });
      if (t._facetText.split(" ").some(function (w) { return w.indexOf(tok) === 0; })) consider(10, "");
      if (t._summaryWords.some(function (w) { return w.indexOf(tok) === 0; })) consider(5, "");
      if (!best) return null;
      total += best;
      if (why && !via) via = why;
    }
    if (whole && t._title.indexOf(whole) !== -1) total += 20;
    return { score: total, via: via };
  }

  var FACETS = [
    { key: "track", label: "Track", values: "tracks", get: function (t) { return t.tracks || []; } },
    { key: "cloud", label: "Cloud", values: "clouds", get: function (t) { return [t.cloud]; } },
    { key: "domain", label: "Domain", values: "domains", get: function (t) { return [t.domain]; }, collapsible: true },
    { key: "level", label: "Level", values: "levels", get: function (t) { return [t.level]; } },
    { key: "status", label: "Status", values: "statuses", get: function (t) { return [t.status]; } },
    { key: "fresh", label: "Freshness", values: "freshness", get: function (t) { return [t.freshness]; } },
    { key: "exam", label: "Exam", values: "exams", get: function (t) { return t.exams || []; }, collapsible: true },
    { key: "map", label: "Cross-cloud", values: null, get: function (t) { return t._hasEq ? ["yes"] : ["no"]; } }
  ];

  function readState() {
    var params = new URLSearchParams(window.location.search);
    var state = { q: params.get("q") || "", filters: {} };
    FACETS.forEach(function (f) {
      var v = params.get(f.key);
      state.filters[f.key] = v ? v.split(",").filter(Boolean) : [];
    });
    return state;
  }

  function writeState(state) {
    var params = new URLSearchParams(window.location.search);
    params.delete("q");
    FACETS.forEach(function (f) { params.delete(f.key); });
    if (state.q) params.set("q", state.q);
    FACETS.forEach(function (f) { if (state.filters[f.key].length) params.set(f.key, state.filters[f.key].join(",")); });
    var qs = params.toString();
    var url = window.location.pathname + (qs ? "?" + qs : "") + window.location.hash;
    try { window.history.replaceState(window.history.state, "", url); } catch (e) { /* file:// */ }
  }

  function matchesFilters(t, filters, skip) {
    for (var i = 0; i < FACETS.length; i++) {
      var f = FACETS[i];
      if (f.key === skip) continue;
      var want = filters[f.key];
      if (!want.length) continue;
      var have = f.get(t);
      if (!have.some(function (v) { return want.indexOf(v) !== -1; })) return false;
    }
    return true;
  }

  function mount(root, data, dataHref) {
    data = data._labels ? data : prepare(data);
    var siteRoot = new URL(data.base, dataHref);
    var state = readState();
    var shown = PAGE;
    var timer = null;

    var fallback = root.querySelector(".lwd-explorer__fallback");
    if (fallback) fallback.hidden = true;

    var input = el("input", { type: "search", id: "lwd-q", class: "lwd-explorer__input", placeholder: "Search names, acronyms, former names…", autocomplete: "off", "aria-describedby": "lwd-status" });
    input.value = state.q;
    var clear = el("button", { type: "button", class: "md-button lwd-explorer__clear", text: "Clear filters" });
    var status = el("p", { id: "lwd-status", class: "lwd-explorer__status", role: "status", "aria-live": "polite" });
    var facetsBox = el("div", { class: "lwd-explorer__facets" });
    var results = el("ol", { class: "lwd-explorer__results" });
    var more = el("button", { type: "button", class: "md-button lwd-explorer__more", text: "Show 50 more" });
    var search = el("div", { role: "search", class: "lwd-explorer__search" }, [
      el("label", { for: "lwd-q", class: "lwd-explorer__label", text: "Search the glossary" }), input, clear
    ]);
    var layout = el("div", { class: "lwd-explorer__layout" }, [facetsBox, el("div", { class: "lwd-explorer__main" }, [status, results, more])]);
    root.insertBefore(layout, root.firstChild);
    root.insertBefore(search, layout);

    var checkboxes = {};
    FACETS.forEach(function (f) {
      var values = f.values ? data.facets[f.values] : [{ id: "yes", label: "Has a counterpart" }, { id: "no", label: "No counterpart yet" }];
      if (!values || !values.length) return;
      var fs = el("fieldset", { class: "lwd-explorer__facet" }, [el("legend", { text: f.label })]);
      var list = el("div", { class: "lwd-explorer__options" });
      checkboxes[f.key] = [];
      values.forEach(function (v) {
        var id = "lwd-" + f.key + "-" + v.id;
        var cb = el("input", { type: "checkbox", id: id, value: v.id });
        cb.checked = state.filters[f.key].indexOf(v.id) !== -1;
        var count = el("span", { class: "lwd-explorer__count" });
        var lab = el("label", { for: id }, [cb, " " + v.label + " ", count]);
        lab._count = count;
        lab._value = v.id;
        checkboxes[f.key].push(lab);
        list.appendChild(lab);
        cb.addEventListener("change", function () {
          var arr = state.filters[f.key];
          var at = arr.indexOf(v.id);
          if (cb.checked && at === -1) arr.push(v.id);
          if (!cb.checked && at !== -1) arr.splice(at, 1);
          shown = PAGE;
          update();
        });
      });
      if (f.collapsible) {
        var filter = el("input", { type: "search", class: "lwd-explorer__optfilter", placeholder: "Filter " + f.label.toLowerCase() + "…", "aria-label": "Filter " + f.label });
        filter.addEventListener("input", function () {
          var q = norm(filter.value);
          checkboxes[f.key].forEach(function (lab) { lab.hidden = q && norm(lab.textContent).indexOf(q) === -1; });
        });
        var det = el("details", { class: "lwd-explorer__details" }, [el("summary", { text: f.label }), filter, list]);
        if (state.filters[f.key].length) det.open = true;
        fs.appendChild(det);
      } else {
        fs.appendChild(list);
      }
      facetsBox.appendChild(fs);
    });

    function termUrl(t) { return new URL(t.url, siteRoot).href; }

    function chip(kind, value, label) {
      return el("span", { class: "lwd-chip lwd-chip--" + kind + " lwd-chip--" + kind + "-" + value, text: label });
    }

    function highlight(text, tokens) {
      var frag = document.createDocumentFragment();
      if (!tokens.length) { frag.appendChild(document.createTextNode(text)); return frag; }
      var parts = text.split(/(\s+)/);
      parts.forEach(function (p) {
        var n = norm(p);
        if (n && tokens.some(function (tok) { return n.indexOf(tok) === 0; })) frag.appendChild(el("mark", { text: p }));
        else frag.appendChild(document.createTextNode(p));
      });
      return frag;
    }

    function card(t, via, tokens) {
      var L = data._labels;
      var h = el("h3", { class: "lwd-explorer__title" }, [el("a", { href: termUrl(t), text: t.title })]);
      if (t.acronyms && t.acronyms.length) h.appendChild(el("span", { class: "lwd-explorer__acr", text: " (" + t.acronyms.join(", ") + ")" }));
      var chips = el("p", { class: "lwd-explorer__chips" }, [
        chip("cloud", t.cloud, L.clouds[t.cloud] || t.cloud),
        chip("domain", t.domain, L.domains[t.domain] || t.domain),
        chip("level", t.level, L.levels[t.level] || t.level)
      ]);
      if (t.status !== "complete") chips.appendChild(chip("status", t.status, L.statuses[t.status] || t.status));
      var summary = el("p", { class: "lwd-explorer__summary" });
      summary.appendChild(highlight(t.summary, tokens));
      var li = el("li", { class: "lwd-explorer__card" }, [h, chips, summary]);
      if (via) li.appendChild(el("p", { class: "lwd-explorer__via", text: "Matched via " + via }));
      if (t.equivalents && t.equivalents.length) {
        var eq = el("p", { class: "lwd-explorer__eq" }, [t.cloud === "azure" ? "AWS: " : "Azure: "]);
        t.equivalents.forEach(function (e, i) {
          var other = data.titles[e.slug] || e.slug;
          if (i) eq.appendChild(document.createTextNode(" · "));
          eq.appendChild(el("a", { href: new URL("terms/" + e.slug + (data.url_style === "directory" ? "/" : ".html"), siteRoot).href, text: other }));
          eq.appendChild(document.createTextNode(" "));
          eq.appendChild(chip("fidelity", e.fidelity, e.fidelity));
        });
        li.appendChild(eq);
      }
      return li;
    }

    function update() {
      state.q = input.value.trim();
      var tokens = words(state.q);
      var whole = norm(state.q);
      var scored = [];
      data.terms.forEach(function (t) {
        var s = score(t, tokens, whole);
        if (s) scored.push({ t: t, s: s });
      });
      var visible = scored.filter(function (x) { return matchesFilters(x.t, state.filters, null); });
      visible.sort(function (a, b) {
        if (b.s.score !== a.s.score) return b.s.score - a.s.score;
        var ca = a.t.status === "complete" ? 0 : 1, cb = b.t.status === "complete" ? 0 : 1;
        if (ca !== cb) return ca - cb;
        return a.t.title.localeCompare(b.t.title);
      });
      // Faceted counts: query plus every other facet's filter.
      FACETS.forEach(function (f) {
        (checkboxes[f.key] || []).forEach(function (lab) {
          var n = 0;
          scored.forEach(function (x) {
            if (matchesFilters(x.t, state.filters, f.key) && f.get(x.t).indexOf(lab._value) !== -1) n++;
          });
          lab._count.textContent = "(" + n + ")";
        });
      });
      results.textContent = "";
      var firstNew = null;
      visible.slice(0, shown).forEach(function (x, i) {
        var c = card(x.t, x.s.via, tokens);
        if (i === shown - PAGE && shown > PAGE) firstNew = c;
        results.appendChild(c);
      });
      more.hidden = visible.length <= shown;
      status.textContent = visible.length + " of " + data.terms.length + " terms";
      if (!visible.length && tokens.length) {
        var pool = [];
        data.terms.forEach(function (t) {
          [t.title].concat(t.acronyms || []).forEach(function (name) {
            var d = editDistance(norm(name), whole, 2);
            if (d <= 2) pool.push({ name: name, t: t, d: d });
          });
        });
        pool.sort(function (a, b) { return a.d - b.d; });
        if (pool.length) {
          var p = el("p", { class: "lwd-explorer__suggest" }, ["Did you mean "]);
          pool.slice(0, 5).forEach(function (s, i) {
            if (i) p.appendChild(document.createTextNode(", "));
            p.appendChild(el("a", { href: termUrl(s.t), text: s.name }));
          });
          p.appendChild(document.createTextNode("?"));
          results.appendChild(el("li", {}, [p]));
        }
      }
      if (firstNew) {
        var a = firstNew.querySelector("a");
        if (a) a.focus();
      }
      clearTimeout(timer);
      timer = setTimeout(function () { writeState(state); }, 300);
    }

    input.addEventListener("input", function () { shown = PAGE; update(); });
    more.addEventListener("click", function () { shown += PAGE; update(); });
    clear.addEventListener("click", function () {
      FACETS.forEach(function (f) {
        state.filters[f.key] = [];
        (checkboxes[f.key] || []).forEach(function (lab) { lab.querySelector("input").checked = false; });
      });
      input.value = "";
      shown = PAGE;
      update();
      input.focus();
    });
    update();
  }

  function fail(root, err) {
    var fallback = root.querySelector(".lwd-explorer__fallback");
    if (fallback) {
      fallback.hidden = false;
      fallback.insertBefore(document.createTextNode("Could not load the glossary data (" + err.message + "). "), fallback.firstChild);
    }
  }

  function onPage() {
    var root = document.querySelector("[data-lwd-explorer]");
    if (!root || root.getAttribute("data-lwd-mounted")) return;
    root.setAttribute("data-lwd-mounted", "1");
    var link = root.querySelector("a.lwd-explorer__data");
    if (!link) return;
    loadScript(link.href, "__LWD_GLOSSARY__").then(function (data) { mount(root, data, link.href); }, function (err) { fail(root, err); });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") window.document$.subscribe(onPage);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", onPage);
  else onPage();
})();
