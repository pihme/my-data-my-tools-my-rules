#!/usr/bin/env python3
"""My Data, My Tools, My Rules - static site builder. No dependencies beyond Python 3.8+.

    python3 build.py               # build ./projects/*.md into ./site
    python3 build.py --out DIR     # other output directory
    python3 build.py --serve       # build, then serve on http://localhost:8000

All links are relative, so the output works under any base path
(GitHub Pages serves it at /my-data-my-tools-my-rules/) and from file://.
"""
import argparse, datetime, html, os, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TH = os.path.join(ROOT, "theme")
REPO = "https://github.com/pihme/my-data-my-tools-my-rules"
VERSION = "2.1.0"  # bump per release; busts browser caches for theme/style.css and theme/site.js
SKIP = {"README.md", "TEMPLATE.md"}
COLORS = ["#ff5c39", "#ffc531", "#2ec4a6", "#6c7bff", "#e95fb3", "#7bd14b"]
E = html.escape

# ---------- front matter (small YAML subset: scalars, [a, b], "- item" lists) ----------
def scalar(v):
    v = v.strip()
    if v[:1] not in "\"'": v = re.sub(r"\s+#.*$", "", v)
    if v.startswith("[") and v.endswith("]"):
        return [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
    if v.lower() in ("true", "false"): return v.lower() == "true"
    return v.strip("\"'")

def parse(path):
    """Front matter subset: `key: scalar`, `key: [a, b]`, `key:` followed by an
    indented block that is either `- item` lines (list of scalars or of maps)
    or `sub: value` lines (a map)."""
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m: sys.exit(f"{path}: missing front matter")
    meta, key, item = {}, None, None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"): continue
        ind = len(line) - len(line.lstrip())
        if ind == 0 and ":" in line:
            key, v = line.split(":", 1); key = key.strip(); item = None
            meta[key] = scalar(v) if v.strip() else None
            continue
        if key is None: sys.exit(f"{path}: indented line outside a block: {line!r}")
        li = re.match(r"^\s+-\s+(.*)$", line)
        if li:
            if meta[key] is None: meta[key] = []
            if not isinstance(meta[key], list): sys.exit(f"{path}: '{key}' mixes list and map")
            body = li.group(1)
            km = re.match(r"^([A-Za-z_]+):\s*(.*)$", body)
            if km and not body.startswith(("http:", "https:")):
                item = {km.group(1): scalar(km.group(2))}; meta[key].append(item)
            else:
                item = None; meta[key].append(scalar(body))
            continue
        km = re.match(r"^\s+([A-Za-z_]+):\s*(.*)$", line)
        if not km: sys.exit(f"{path}: cannot parse line {line!r}")
        if isinstance(meta[key], list):
            if item is None: sys.exit(f"{path}: stray map line in list '{key}': {line!r}")
            item[km.group(1)] = scalar(km.group(2))
        else:
            if meta[key] is None: meta[key] = {}
            meta[key][km.group(1)] = scalar(km.group(2))
    for k, v in meta.items():
        if v is None: meta[k] = []
    meta["body"] = m.group(2)
    meta.setdefault("slug", os.path.splitext(os.path.basename(path))[0])
    return meta

# ---------- tiny Markdown ----------
def inline(t):
    codes = []
    t = re.sub(r"`([^`]+)`", lambda m: codes.append(m.group(1)) or f"\x00{len(codes)-1}\x00", t)
    t = E(t, quote=False)
    t = re.sub(r"&lt;(https?://[^\s&]+)&gt;", r'<a href="\1">\1</a>', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(.+?)\*(?![\w*])", r"<em>\1</em>", t)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{E(codes[int(m.group(1))])}</code>", t)

def markdown(src, shift=0):
    """Paragraphs, headings, ordered/unordered lists (blank lines between items are fine,
    numbering is kept), fenced code blocks (also indented inside a list item), `> ` callouts."""
    out, para, lst = [], [], None   # lst = [kind, start, [item_html, ...]]
    def flush_para():
        nonlocal para
        if not para: return
        text = " ".join(para); para = []
        if re.match(r"(?i)^Watch out:", text):
            out.append('<aside class="callout callout-watch"><p>' + inline(text) + "</p></aside>")
        else:
            out.append("<p>" + inline(text) + "</p>")
    def flush_list():
        nonlocal lst
        if lst:
            st = f' start="{lst[1]}"' if lst[0] == "ol" and lst[1] != 1 else ""
            out.append(f"<{lst[0]}{st}>" + "".join(f"<li>{i}</li>" for i in lst[2]) + f"</{lst[0]}>"); lst = None
    lines = src.splitlines(); i = 0
    while i < len(lines):
        l = lines[i]
        if l.strip().startswith("```"):
            ind = len(l) - len(l.lstrip()); code = []; i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i][ind:] if lines[i][:ind].strip() == "" else lines[i]); i += 1
            html_code = "<pre><code>" + E("\n".join(code)) + "</code></pre>"
            if lst and ind > 0: lst[2][-1] += html_code
            else: flush_para(); flush_list(); out.append(html_code)
            i += 1; continue
        if l.startswith(">"):
            flush_para(); flush_list(); q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i][1:].strip()); i += 1
            out.append('<aside class="callout">' + "".join(f"<p>{inline(x)}</p>" for x in "\n".join(q).split("\n\n") if x.strip()).replace("\n", " ") + "</aside>")
            continue
        if re.match(r"^#{1,6} ", l):
            flush_para(); flush_list(); n = len(l) - len(l.lstrip("#")); h = min(6, n + shift)
            out.append(f"<h{h}>{inline(l[n+1:].strip())}</h{h}>")
        elif re.match(r"^([-*]|\d+\.) ", l):
            flush_para()
            num = re.match(r"^(\d+)\.", l); kind = "ol" if num else "ul"
            if not lst or lst[0] != kind: flush_list(); lst = [kind, int(num.group(1)) if num else 1, []]
            lst[2].append(inline(re.sub(r"^([-*]|\d+\.) ", "", l)))
        elif not l.strip():
            flush_para()
            nxt = next((x for x in lines[i+1:] if x.strip()), "")
            if lst and not (re.match(r"^([-*]|\d+\.) ", nxt) or nxt.startswith((" ", "\t"))): flush_list()
        elif lst and l.startswith((" ", "\t")):
            lst[2][-1] += " " + inline(l.strip())
        else:
            flush_list(); para.append(l.strip())
        i += 1
    flush_para(); flush_list()
    return "\n".join(out)

# ---------- helpers ----------
def cat_name(c): return re.sub(r"\s*\(tentative\)\s*$", "", c).strip()
def cat_id(c): return re.sub(r"[^a-z0-9]+", "-", cat_name(c).lower()).strip("-")
def types(p): return p["type"] if isinstance(p["type"], list) else [p["type"]]
def is_server(p): return "Server" in types(p)
def is_app(p): return "App" in types(p)
def host(u): return re.sub(r"^https?://(www\.)?", "", u).rstrip("/")
def nice_date(d):
    try: return datetime.date.fromisoformat(str(d)).strftime("%-d %B %Y")
    except ValueError: return str(d)

def license_tag(p):
    if p["open_source"]: return '<span class="tag t-os" title="OSI-approved license">Open source</span>'
    return '<span class="tag t-sa" title="Source is public, license is not OSI-approved">Source-available</span>'

def type_tags(p):
    t = []
    if is_server(p): t.append('<span class="tag t-sh" title="Server software you run yourself">Self-host</span>')
    if is_app(p): t.append('<span class="tag t-app" title="Installed on your own device">App</span>')
    return "".join(t)

def kinds(p):
    k = ["open-source" if p["open_source"] else "source-available"]
    if is_server(p): k.append("self-host")
    if is_app(p): k.append("app")
    return " ".join(k)

AUDIENCE = {"End user": 1, "Enthusiast": 2, "Expert": 3}
AUD_HELP = {"End user": "Installs like any other app or program",
            "Enthusiast": "Needs some comfort with a home server, Docker or similar",
            "Expert": "Running it well needs server administration skills and ongoing maintenance"}
ASSETS = os.path.join(ROOT, "assets", "ASSETS.md")

def load_assets():
    """assets/ASSETS.md tables: | File | Project | Source URL | License / terms URL | Terms in short | Credit line | Verdict |.
    Only rows whose verdict starts with "ok" may be used."""
    out = {}
    if not os.path.isfile(ASSETS): return out
    for l in open(ASSETS, encoding="utf-8"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) == 7 and c[0].startswith(("icons/", "screenshots/")) and c[6].lower().startswith("ok"):
            terms = re.findall(r"https?://[^\s;,)]+", c[3])
            out["assets/" + c[0]] = {"source": c[2], "terms": terms[0] if terms else c[2], "short": c[4], "credit": c[5]}
    return out

MEDIA = load_assets()

def check_media(f, p):
    for k in ("icon", "screenshot"):
        v = p.get(k)
        if not v: continue
        if not isinstance(v, str): sys.exit(f"projects/{f}: {k} must be a path like assets/{k}s/<slug>.<ext>")
        if v not in MEDIA: sys.exit(f"projects/{f}: {k} '{v}' is not cleared (verdict ok) in assets/ASSETS.md")
        if not os.path.isfile(os.path.join(ROOT, v)): sys.exit(f"projects/{f}: file not found: {v}")
        if p.get(k + "_source") and p[k + "_source"] != MEDIA[v]["source"]:
            print(f"warning: projects/{f}: {k}_source differs from assets/ASSETS.md", file=sys.stderr)

REQUIRED = ["name", "slug", "category", "license", "open_source", "type", "url", "repo", "source_url", "checked", "sources"]

def load_projects():
    d = os.path.join(ROOT, "projects"); ps = []
    for f in sorted(os.listdir(d)):
        if not f.endswith(".md") or f in SKIP: continue
        p = parse(os.path.join(d, f))
        miss = [k for k in REQUIRED if k not in p or p[k] in ("", [])]
        if miss: sys.exit(f"projects/{f}: missing {', '.join(miss)}")
        if p["slug"] + ".md" != f: sys.exit(f"projects/{f}: slug '{p['slug']}' does not match file name")
        if not isinstance(p["open_source"], bool): sys.exit(f"projects/{f}: open_source must be true or false")
        if p["open_source"] and "LicenseRef-" in p["license"]:
            sys.exit(f"projects/{f}: open_source is true but license is {p['license']}")
        if len(p.get("note", "")) > 120: print(f"warning: projects/{f}: note longer than 120 characters", file=sys.stderr)
        if p.get("summary") and not 120 <= len(p["summary"]) <= 700:
            print(f"warning: projects/{f}: summary should be a paragraph of about 2-4 sentences", file=sys.stderr)
        if p.get("audience"):
            norm = {k.lower().replace(" ", "-"): k for k in AUDIENCE}
            p["audience"] = norm.get(str(p["audience"]).strip().lower().replace(" ", "-"), p["audience"])
        if p.get("audience") and p["audience"] not in AUDIENCE:
            sys.exit(f"projects/{f}: audience must be one of {', '.join(AUDIENCE)}")
        if p.get("icon_scale"):
            try: ok = 1 <= float(p["icon_scale"]) <= 2
            except ValueError: ok = False
            if not ok: sys.exit(f"projects/{f}: icon_scale must be a number between 1 and 2")
        has_setup = any(k in p for k in ("setup_steps", "setup_clarity", "setup_tested"))
        if has_setup:
            for k in ("setup_steps", "setup_clarity", "setup_tested"):
                if k not in p or p[k] in ("", None, []):
                    sys.exit(f"projects/{f}: setup_* fields must be set together (missing {k})")
            try:
                steps = int(str(p["setup_steps"]))
                if steps < 1: raise ValueError
                p["setup_steps"] = steps
            except ValueError:
                sys.exit(f"projects/{f}: setup_steps must be a positive integer")
            try:
                clarity = int(str(p["setup_clarity"]))
                if not 1 <= clarity <= 5: raise ValueError
                p["setup_clarity"] = clarity
            except ValueError:
                sys.exit(f"projects/{f}: setup_clarity must be an integer from 1 to 5")
            try:
                datetime.date.fromisoformat(str(p["setup_tested"]))
            except ValueError:
                sys.exit(f"projects/{f}: setup_tested must be a date YYYY-MM-DD")
        check_media(f, p)
        ps.append(p)
    return sorted(ps, key=lambda p: p["name"].lower())

FUNDERS = os.path.join(ROOT, "content", "funders.md")
FUNDER_IDS = {"futo": "FUTO", "nlnet": "NLnet", "ngi": "Next Generation Internet"}

def load_funders(ps):
    """content/funders.md: `## Funder` sections. Dossiers reference them with `funders: [slug, ...]`."""
    fs = parse(FUNDERS)
    heads = re.findall(r"^##\s+(.*)$", fs["body"], re.M)
    known = {}
    for slug, word in FUNDER_IDS.items():
        h = next((x for x in heads if x.startswith(word)), None)
        if h: known[slug] = h
    for p in ps:
        for x in p.get("funders") or []:
            if x not in known: sys.exit(f"projects/{p['slug']}.md: funder '{x}' has no section in content/funders.md")
    fs["known"] = known
    return fs

def categories(ps):
    names = sorted({cat_name(p["category"]) for p in ps}, key=str.lower)
    return [(cat_id(n), n, COLORS[i % len(COLORS)], [p for p in ps if cat_name(p["category"]) == n]) for i, n in enumerate(names)]

def nav(cats, root, active=None, index=False):
    items = []
    total = sum(len(c[3]) for c in cats)
    if index:
        items.append(f'<li><a href="#top" data-cat="all" class="on"><b>··</b>Catalog<span>{total}</span></a></li>')
    else:
        items.append(f'<li><a href="{root}index.html" data-cat="all"><b>··</b>Catalog<span>{total}</span></a></li>')
    for i, (cid, n, col, ps) in enumerate(cats):
        href = f"#{cid}" if index else f"{root}index.html#{cid}"
        on = ' class="on"' if cid == active else ""
        items.append(f'<li><a href="{href}" data-cat="{cid}" style="--c:{col}"{on}><b>{i+1:02d}</b>{E(n)}<span>{len(ps)}</span></a></li>')
    return "".join(items)

def page(title, main, root, navhtml, desc, bodyclass="", about=None):
    """about: which About-list entry to mark class=on — "omakase", "about", "funders", or None."""
    base = open(os.path.join(TH, "base.html"), encoding="utf-8").read()
    on = ' class="on"'
    rep = {"{{TITLE}}": E(title), "{{DESCRIPTION}}": E(desc), "{{NAV}}": navhtml, "{{MAIN}}": main,
           "{{REPO}}": REPO, "{{BUILT}}": datetime.date.today().isoformat(), "{{BODYCLASS}}": bodyclass}
    rep["{{VERSION}}"] = VERSION
    if os.path.isfile(OMAKASE):
        rep["{{OMAKASE}}"] = f'<li><a href="{{{{ROOT}}}}omakase.html"{on if about == "omakase" else ""}>Omakase</a></li>'
        rep["{{OMAKASE_FOOT}}"] = ' · <a href="{{ROOT}}omakase.html">Omakase</a>'
    else:
        rep["{{OMAKASE}}"] = ""; rep["{{OMAKASE_FOOT}}"] = ""
    rep["{{ABOUT_ON}}"] = on if about == "about" else ""
    rep["{{FUNDERS_ON}}"] = on if about == "funders" else ""
    for k, v in rep.items(): base = base.replace(k, v)
    return base.replace("{{ROOT}}", root)

ICON_PX = {"card": 24, "omakase": 20, "dossier": 60}

def icon_html(p, root, kind="card", cls="lt"):
    """Logo tile. The <img> carries explicit width/height so it stays small even if the
    stylesheet is missing or stale; `icon_scale` (1-2) optically enlarges logos with built-in whitespace."""
    ic = p.get("icon")
    if ic:
        px = ICON_PX[kind]
        sc = p.get("icon_scale")
        st = f' style="--s:{float(sc):g}"' if sc else ""
        return (f'<a class="{cls} ic ic-{kind}" href="{E(p["url"])}" tabindex="-1" aria-hidden="true"><img src="{root}{E(ic)}" alt="" '
                f'width="{px}" height="{px}"{st} loading="lazy" decoding="async"></a>')
    return f'<span class="{cls}" aria-hidden="true">{E(p["name"][0].upper())}</span>'

def aud_html(p, cls="aud"):
    a = p.get("audience")
    if not a: return ""
    n = AUDIENCE[a]
    return (f'<span class="{cls}" role="img" aria-label="Audience: {a}" title="Audience: {a}. {AUD_HELP[a]}">'
            f'<span aria-hidden="true">{"●" * n}{"○" * (3 - n)} {a}</span></span>')

def aud_id(p): return re.sub(r"[^a-z]+", "-", (p.get("audience") or "").lower()).strip("-")

# ---------- pages ----------
def setup_html(p, cls="setup-meta"):
    """Shown only when the getting-started path was hands-on checked."""
    if not p.get("setup_tested"): return ""
    return (f'<p class="{cls}" title="Hands-on check of the official getting-started path '
            f'on {E(str(p["setup_tested"]))}">{p["setup_steps"]} steps · clarity {p["setup_clarity"]}/5</p>')

def card(p, col, cid):
    note = E(p.get("summary") or p.get("note") or "") or '<span class="nonote">No note.</span>'
    setup = setup_html(p, "setup-meta setup-card")
    return f'''<article class="card" data-cat="{cid}" data-kinds="{kinds(p)}" data-aud="{aud_id(p)}"><div class="ct">{icon_html(p, "")}<div><h3><a href="projects/{p["slug"]}.html">{E(p["name"])}</a></h3><span class="spdx" title="SPDX license id">{E(p["license"])}</span></div></div>
<div class="tags">{license_tag(p)}{type_tags(p)}</div>
<p>{note}</p>{setup}<div class="lnk"><a class="web" href="{E(p["url"])}" title="Website">{E(host(p["url"]))}</a>{aud_html(p)}<a class="repo" href="{E(p["repo"])}" title="Source code">repo</a><a class="more" href="projects/{p["slug"]}.html" aria-label="Details on {E(p["name"])}">→</a></div></article>'''

def index(ps, cats):
    nos = sum(p["open_source"] for p in ps); nsh = sum(is_server(p) for p in ps)
    secs = ""
    for i, (cid, n, col, cps) in enumerate(cats):
        k = min(len(cps), 4)
        secs += (f'<section class="cat span-{k}" id="{cid}" style="--c:{col};--n:{k}"><header class="sh"><span class="num">{i+1:02d}</span>'
                 f'<div><h2>{E(n)}</h2><p><span class="cnt">{len(cps)} {"entry" if len(cps) == 1 else "entries"}</span></p></div></header>\n'
                 f'<div class="grid">{"".join(card(p, col, cid) for p in cps)}</div></section>\n')
    main = f'''<section class="hero" id="top"><div class="h1w"><p class="kick">An open catalog</p>
<h1>My data.<br>My tools.<br><em>My rules.</em></h1></div>
<div class="hside"><p class="intro">A curated list of open-source and source-available software that keeps your data under your control, sorted by what you want to do and labeled by how you can run it.</p>
<div class="stats"><div><b>{len(ps)}</b><span>entries</span></div><div><b>{len(cats)}</b><span>categories</span></div><div><b>{nos}</b><span>open source</span></div><div><b>{nsh}</b><span>self-host</span></div></div>
<div class="filterbar" hidden><div class="frow"><div class="fgroup" role="group" aria-label="License"><span class="flabel">License</span><div class="pills"><button type="button" data-lic="all" class="on" aria-pressed="true">Any</button><button type="button" data-lic="open-source" aria-pressed="false">Open source</button><button type="button" data-lic="source-available" data-sa aria-pressed="false">Source-available</button></div></div><span class="fdiv" aria-hidden="true"></span><div class="fgroup" role="group" aria-label="Runs as"><span class="flabel">Runs as</span><div class="pills"><button type="button" data-run="all" class="on" aria-pressed="true">Any</button><button type="button" data-run="app" aria-pressed="false">App</button><button type="button" data-run="self-host" aria-pressed="false">Self-host</button></div></div></div><div class="frow"><div class="fgroup" role="group" aria-label="For"><span class="flabel">For</span><div class="pills"><button type="button" data-aud="all" class="on" aria-pressed="true">Everyone</button><button type="button" data-aud="end-user" aria-pressed="false"><span class="dots" aria-hidden="true">●○○</span> End user</button><button type="button" data-aud="enthusiast" aria-pressed="false"><span class="dots" aria-hidden="true">●●○</span> Enthusiast</button><button type="button" data-aud="expert" aria-pressed="false"><span class="dots" aria-hidden="true">●●●</span> Expert</button></div></div><button type="button" class="freset">Reset filters</button></div></div></section>
<div class="catflow">
{secs}</div><p class="empty" hidden>No projects match these filters. <button type="button" class="freset">Reset filters</button></p>'''
    return page("My Data, My Tools, My Rules", main, "", nav(cats, "", index=True),
                "An open catalog of open-source and source-available software that keeps your data under your control.")

def media_credit(path):
    m = MEDIA[path]
    return f'{E(m["credit"])} · <a href="{E(m["terms"])}">terms</a> · <a href="{E(m["source"])}">source</a>'

def fid(name): return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

FUNDER_LABELS = {"futo": "FUTO", "nlnet": "NLnet", "ngi": "NGI"}

def funding_html(p, fs):
    """Funder names link to stable section ids on funders.html (#futo, #nlnet, #ngi)."""
    links = ", ".join(
        f'<a href="../funders.html#{E(x)}">{E(FUNDER_LABELS.get(x, x))}</a>'
        for x in (p.get("funders") or []) if x in fs["known"]
    )
    note = f'<div>{inline(p["funding_note"])}</div>' if p.get("funding_note") else ""
    fl = f'<div class="sub">Funders: {links}</div>' if links else ""
    return note + fl

def shots_html(p):
    s = p.get("screenshot")
    if not s: return ""
    return (f'<figure class="shot"><img src="../{E(s)}" alt="Screenshot of {E(p["name"])}" '
            f'loading="lazy" decoding="async"><figcaption><span class="cr">Screenshot: {media_credit(s)}</span></figcaption></figure>')

def project(p, cats):
    cid = cat_id(p["category"]); i, col = next((k, c[2]) for k, c in enumerate(cats) if c[0] == cid)
    tlabel = " and ".join(["Self-host (server)" if t == "Server" else "App" for t in types(p)])
    rows = [("License", f'<a href="{E(p["source_url"])}"><code>{E(p["license"])}</code></a><div class="tags">{license_tag(p)}</div>'),
            ("Type", f'{tlabel}<div class="tags">{type_tags(p)}</div>')]
    if p.get("audience"): rows.append(("Audience", f'{aud_html(p, "aud aud-l")}<div class="sub">{E(AUD_HELP[p["audience"]])}</div>'))
    if p.get("setup_tested"):
        rows.append(("Setup", f'{p["setup_steps"]} steps · clarity {p["setup_clarity"]}/5'
                     f'<div class="sub">Checked <time datetime="{E(str(p["setup_tested"]))}">{nice_date(p["setup_tested"])}</time></div>'))
    rows += [("Website", f'<a href="{E(p["url"])}">{E(host(p["url"]))}</a>'),
             ("Source code", f'<a href="{E(p["repo"])}">{E(host(p["repo"]))}</a>'),
             ("Category", f'<a href="../index.html#{cid}">{E(cat_name(p["category"]))}</a>')]
    if p.get("corporate_note"): rows.append(("Organization", inline(p["corporate_note"])))
    if p.get("funding_note") or p.get("funders"):
        rows.append(("Funding", funding_html(p, FS) + '<div class="sub">Funding says nothing about the license.</div>'))
    if p.get("icon"): rows.append(("Logo", media_credit(p["icon"]) + '<div class="sub">Shown unmodified to identify the project. No endorsement implied.</div>'))
    rows.append(("Checked", f'<time datetime="{E(str(p["checked"]))}">{nice_date(p["checked"])}</time>'))
    facts = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    srcs = "".join(f'<li><a href="{E(s)}">{E(host(s))}</a></li>' for s in p["sources"])
    body = markdown(p["body"]); shots = shots_html(p)
    if shots:
        k = body.find("</p>")
        body = body[:k + 4] + shots + body[k + 4:] if k >= 0 else shots + body
    setup = setup_html(p)
    if setup:
        body = body.replace("<h2>Getting started</h2>", "<h2>Getting started</h2>\n" + setup, 1)
    summary = p.get("summary") or p.get("note", "")
    main = f'''<section class="phead proj" style="--c:{col}"><div><p class="kick"><a href="../index.html">Catalog</a> · <a href="../index.html#{cid}">{i+1:02d} {E(cat_name(p["category"]))}</a></p>
<h1>{icon_html(p, "../", "dossier")}{E(p["name"])}</h1></div>
<p class="intro">{E(summary)}</p></section>
<div class="body-wrap" style="--c:{col}"><article class="prose">{body}
<section class="sources"><h2>Sources</h2><ol>{srcs}</ol></section>
<a class="back" href="../index.html#{cid}">← Back to the catalog</a></article>
<aside class="facts" aria-label="Facts"><dl>{facts}</dl></aside></div>'''
    return page(f'{p["name"]} · My Data, My Tools, My Rules', main, "../", nav(cats, "../", active=cid),
                p.get("note") or p["name"])

def about(cats):
    readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    m = re.search(r"^## About this site\n(.*?)(?=^## |\Z)", readme, re.S | re.M)
    if not m: sys.exit("README.md: no '## About this site' section")
    crit = open(os.path.join(ROOT, "content", "selection-criteria.md"), encoding="utf-8").read()
    crit = re.sub(r"^## How projects are selected", '## How projects are selected {#selection-criteria}', crit, flags=re.M)
    crit_html = markdown(crit).replace("<h2>How projects are selected {#selection-criteria}</h2>", '<h2 id="selection-criteria">How projects are selected</h2>')
    main = f'''<section class="phead"><div><p class="kick"><a href="index.html">Catalog</a> · About</p><h1>About this site</h1></div>
<p class="intro">What goes in, how projects are selected and what the labels mean.</p></section>
<div class="body-wrap"><article class="prose">
<h2 id="what-belongs-here">What belongs here</h2>
<p>Open-source and source-available projects that help people keep control of their data and stay independent of large tech companies. Anything an individual can install for private use free of charge qualifies.</p>
{crit_html}
<h2 id="how-this-site-is-made">How this site is made</h2>
{markdown(m.group(1).strip())}
<h2 id="license-labels">License labels</h2>
<p><strong>Open source</strong> means the license is OSI-approved. <strong>Source-available</strong> means the source code is public, but the license is not OSI-approved and usually restricts some uses; these entries carry a <code>LicenseRef-*</code> id instead of a standard SPDX id. Every entry shows its license id and links to the license file it was checked against, with the date of the check.</p>
<p><strong>Self-host</strong> marks server software you run on your own hardware. <strong>App</strong> marks software you install on your own device. Some projects are both.</p>
<h2 id="cards">What a card shows</h2>
<p>Each card has a short paragraph on what the project is, what it replaces or helps with, and how you run it, followed by the license labels, links to the website and source code, and an audience indicator:</p>
<ul><li><strong>●○○ End user</strong>: {AUD_HELP["End user"]}.</li><li><strong>●●○ Enthusiast</strong>: {AUD_HELP["Enthusiast"]}.</li><li><strong>●●● Expert</strong>: {AUD_HELP["Expert"]}.</li></ul>
<p>The audience level is an editorial estimate, not a rating of the project.</p>
<h2 id="logos-and-screenshots">Logos and screenshots</h2>
<p>Project logos and screenshots are shown only when their license or the project's brand guidelines allow this kind of use. They are shown unmodified, only to identify the project, and do not imply endorsement. Every logo and screenshot is credited on the project page with its author, license and source. Where the terms are unclear, the card shows a letter tile instead.</p>
<h2 id="funding">Funding</h2>
<p>If a project is developed or funded by an organization such as FUTO or NLnet, its page says so and links to the source. The <a href="funders.html">Funders</a> page describes these organizations. Funding never decides inclusion, and it says nothing about a project's license.</p>
<h2 id="suggest-a-project">Suggest a project</h2>
{markdown(open(os.path.join(ROOT, "content", "suggest.md"), encoding="utf-8").read())}
</article></div>'''
    return page("About · My Data, My Tools, My Rules", main, "", nav(cats, ""), "About this site, how projects are selected and what the labels mean.", about="about")

def funders_page(fs, ps, cats):
    """Render content/funders.md. Section ids for known funders are the dossier slugs
    (futo, nlnet, ngi); other headings keep a slugified id. Project lists live on the
    funders' own sites — this page does not generate per-funder project lists."""
    body = re.sub(r"^#\s+.*\n", "", fs["body"].lstrip(), count=1)
    intro, _, rest = body.partition("\n## ")
    html_rest = markdown("## " + rest)
    by_head = {h: slug for slug, h in fs["known"].items()}
    def h2id(m):
        text = re.sub(r"<[^>]+>", "", m.group(1))
        slug = by_head.get(text)
        if not slug:
            for s, word in FUNDER_IDS.items():
                if text.startswith(word):
                    slug = s; break
        if not slug:
            slug = fid(text)
        return f'<h2 id="{E(slug)}">{m.group(1)}</h2>'
    html_rest = re.sub(r"<h2>(.*?)</h2>", h2id, html_rest)
    main = f'''<section class="phead"><div><p class="kick"><a href="index.html">Catalog</a> · Funders</p><h1>{E(fs.get("title") or "Funders")}</h1></div>
<div class="intro">{markdown(intro.strip())}</div></section>
<div class="body-wrap"><article class="prose funders">{html_rest}
<p>Spotted a missing grant or a mistake? <a href="{REPO}/issues">Open an issue on GitHub</a>.</p></article></div>'''
    return page("Funders · My Data, My Tools, My Rules", main, "", nav(cats, ""), "Organizations that develop or fund projects in this catalog.", about="funders")

OMAKASE = os.path.join(ROOT, "content", "omakase.md")

def omakase_page(ps, cats):
    """content/omakase.md: front matter (title), a `# Heading`, an intro paragraph, then
    `## Course` sections with `- **[Name](projects/<slug>.html)**: why` rows (or an external
    https link for things outside the catalog). An indented `*...*` line is a side note."""
    o = parse(OMAKASE); by = {p["slug"]: p for p in ps}
    courses, cur, row, h1, intro = [], None, None, None, []
    for l in o["body"].splitlines():
        if not l.strip(): continue
        m = re.match(r"^#\s+(.*)$", l)
        if m: h1 = m.group(1).strip(); continue
        m = re.match(r"^##\s+(.*)$", l)
        if m: cur = (m.group(1).strip(), []); courses.append(cur); row = None; continue
        if cur is None: intro.append(l.strip()); continue
        m = re.match(r"^\s+\*(.+)\*\s*$", l)
        if m:
            if row is not None: row["note"] = m.group(1).strip()
            continue
        m = re.match(r"^-\s+\*\*\[([^\]]+)\]\(([^)]+)\)\*\*\s*:\s*(.*)$", l)
        if not m: sys.exit(f"content/omakase.md: cannot parse line {l!r}")
        name, url, why = m.groups()
        pm = re.match(r"^projects/([a-z0-9-]+)\.html$", url)
        if pm:
            if pm.group(1) not in by: sys.exit(f"content/omakase.md: no dossier for '{pm.group(1)}'")
            row = {"p": by[pm.group(1)], "why": why}
        elif url.startswith("https://"): row = {"name": name, "url": url, "why": why}
        else: sys.exit(f"content/omakase.md: unsupported link {url!r}")
        cur[1].append(row)
    secs = ""
    for n, (title, rows) in enumerate(courses, 1):
        lab, _, nm = title.partition(":")
        if not nm: lab, nm = "", title
        items = ""
        for r in rows:
            if "p" in r:
                p = r["p"]; head = f'{icon_html(p, "", "omakase")}<a class="on-name" href="projects/{p["slug"]}.html">{E(p["name"])}</a>'
            else:
                head = f'<span class="lt" aria-hidden="true">{E(r["name"][0].upper())}</span><a class="on-name" href="{E(r["url"])}">{E(r["name"])} ↗</a>'
            note = f'<span class="on-note">{inline(r["note"])}</span>' if r.get("note") else ""
            items += f'<li class="on-row"><div class="on-head">{head}</div><p class="on-why">{inline(r["why"])}{note}</p></li>'
        kick = f'<span class="cl">{E(lab.strip())}</span>' if lab else ""
        secs += f'<section class="course"><h2><span class="cn">{n:02d}</span>{kick}{E(nm.strip())}</h2><ul class="menu">{items}</ul></section>'
    intro = f'<p class="intro">{inline(" ".join(intro))}</p>' if intro else ""
    title = h1 or o.get("title") or "Omakase"
    main = f'''<section class="phead omk-head"><div><p class="kick"><a href="index.html">Catalog</a> · Omakase</p>
<h1>{E(title)} <span class="jp" lang="ja">お任せ</span></h1></div>{intro}</section>
<div class="omakase">{secs}</div>'''
    return page("Omakase · My Data, My Tools, My Rules", main, "", nav(cats, ""), "A short, personal selection from the catalog.", "omk", about="omakase")

def build(out):
    global FS
    ps = load_projects(); cats = categories(ps); fs = FS = load_funders(ps)
    if os.path.isdir(out): shutil.rmtree(out)
    os.makedirs(os.path.join(out, "projects"))
    w = lambda rel, s: open(os.path.join(out, rel), "w", encoding="utf-8").write(s)
    w("index.html", index(ps, cats)); w("about.html", about(cats)); w("funders.html", funders_page(fs, ps, cats))
    if os.path.isfile(OMAKASE): w("omakase.html", omakase_page(ps, cats))
    for p in ps: w(f"projects/{p['slug']}.html", project(p, cats))
    shutil.copytree(TH, os.path.join(out, "theme"), ignore=shutil.ignore_patterns("base.html"))
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(out, "assets"))
    print(f"built {len(ps)} projects in {len(cats)} categories, {len(fs['known'])} funders into {out}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "site"))
    ap.add_argument("--serve", action="store_true")
    a = ap.parse_args()
    build(a.out)
    if a.serve:
        import functools, http.server
        h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=a.out)
        print("serving on http://localhost:8000"); http.server.ThreadingHTTPServer(("", 8000), h).serve_forever()
