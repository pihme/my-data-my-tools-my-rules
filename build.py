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
SKIP = {"README.md", "TEMPLATE.md", "MEDIA.md"}
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
        if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
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
ICON_KEYS = ["file", "credit", "license", "source"]
SHOT_KEYS = ["file", "caption", "credit", "license", "source"]
FUND_KEYS = ["funder", "what", "source"]

def check_media(f, p):
    def need(d, keys, what):
        if not isinstance(d, dict): sys.exit(f"projects/{f}: {what} must be a map")
        miss = [k for k in keys if not d.get(k)]
        if miss: sys.exit(f"projects/{f}: {what} missing {', '.join(miss)}")
    def exists(name):
        path = os.path.join(ROOT, "assets", "projects", p["slug"], name)
        if not os.path.isfile(path): sys.exit(f"projects/{f}: file not found: assets/projects/{p['slug']}/{name}")
    if p.get("icon"):
        need(p["icon"], ICON_KEYS, "icon"); exists(p["icon"]["file"])
    for s in p.get("screenshots") or []:
        need(s, SHOT_KEYS, "screenshot"); exists(s["file"])
    for x in p.get("funding") or []:
        need(x, FUND_KEYS, "funding entry")

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
        if p.get("audience") and p["audience"] not in AUDIENCE:
            sys.exit(f"projects/{f}: audience must be one of {', '.join(AUDIENCE)}")
        check_media(f, p)
        ps.append(p)
    return sorted(ps, key=lambda p: p["name"].lower())

def load_funders(ps):
    d = os.path.join(ROOT, "funders"); fs = {}
    for f in sorted(os.listdir(d)):
        if not f.endswith(".md") or f in SKIP: continue
        x = parse(os.path.join(d, f))
        miss = [k for k in ("name", "url", "mission", "mission_source", "sources") if not x.get(k)]
        if miss: sys.exit(f"funders/{f}: missing {', '.join(miss)}")
        fs[x["name"]] = x
    for p in ps:
        for e in p.get("funding") or []:
            if e["funder"] not in fs: sys.exit(f"projects/{p['slug']}.md: funder '{e['funder']}' has no file in funders/")
    return fs

def categories(ps):
    names = sorted({cat_name(p["category"]) for p in ps}, key=str.lower)
    return [(cat_id(n), n, COLORS[i % len(COLORS)], [p for p in ps if cat_name(p["category"]) == n]) for i, n in enumerate(names)]

def nav(cats, root, active=None, index=False):
    items = []
    if index:
        items.append(f'<li><a href="#top" data-cat="all" class="on"><b>··</b>Catalog<span>{sum(len(c[3]) for c in cats)}</span></a></li>')
    for i, (cid, n, col, ps) in enumerate(cats):
        href = f"#{cid}" if index else f"{root}index.html#{cid}"
        on = ' class="on"' if cid == active else ""
        items.append(f'<li><a href="{href}" data-cat="{cid}" style="--c:{col}"{on}><b>{i+1:02d}</b>{E(n)}<span>{len(ps)}</span></a></li>')
    return "".join(items)

def page(title, main, root, navhtml, desc, bodyclass=""):
    base = open(os.path.join(TH, "base.html"), encoding="utf-8").read()
    rep = {"{{TITLE}}": E(title), "{{DESCRIPTION}}": E(desc), "{{NAV}}": navhtml, "{{MAIN}}": main,
           "{{REPO}}": REPO, "{{BUILT}}": datetime.date.today().isoformat(), "{{BODYCLASS}}": bodyclass}
    rep["{{OMAKASE}}"] = '<li><a href="{{ROOT}}omakase.html">Omakase</a></li>' if os.path.isfile(OMAKASE) else ""
    for k, v in rep.items(): base = base.replace(k, v)
    return base.replace("{{ROOT}}", root)

def icon_html(p, root, cls="lt"):
    ic = p.get("icon")
    if ic:
        return (f'<span class="{cls} ic" aria-hidden="true"><img src="{root}assets/projects/{E(p["slug"])}/{E(ic["file"])}" alt="" '
                f'loading="lazy" decoding="async"></span>')
    return f'<span class="{cls}" aria-hidden="true">{E(p["name"][0].upper())}</span>'

def aud_html(p, cls="aud"):
    a = p.get("audience")
    if not a: return ""
    n = AUDIENCE[a]
    return (f'<span class="{cls}" role="img" aria-label="Audience: {a}" title="Audience: {a}. {AUD_HELP[a]}">'
            f'<span aria-hidden="true">{"●" * n}{"○" * (3 - n)} {a}</span></span>')

def aud_id(p): return re.sub(r"[^a-z]+", "-", (p.get("audience") or "").lower()).strip("-")

# ---------- pages ----------
def card(p, col, cid):
    note = E(p.get("summary") or p.get("note") or "") or '<span class="nonote">No note.</span>'
    return f'''<article class="card" data-cat="{cid}" data-kinds="{kinds(p)}" data-aud="{aud_id(p)}"><div class="ct">{icon_html(p, "")}<div><h3><a href="projects/{p["slug"]}.html">{E(p["name"])}</a></h3><span class="spdx" title="SPDX license id">{E(p["license"])}</span></div></div>
<div class="tags">{license_tag(p)}{type_tags(p)}</div>
<p>{note}</p><div class="lnk"><a class="web" href="{E(p["url"])}" title="Website">{E(host(p["url"]))}</a>{aud_html(p)}<a class="repo" href="{E(p["repo"])}" title="Source code">repo</a><a class="more" href="projects/{p["slug"]}.html" aria-label="Details on {E(p["name"])}">→</a></div></article>'''

def index(ps, cats):
    nos = sum(p["open_source"] for p in ps); nsh = sum(is_server(p) for p in ps)
    secs = ""
    for i, (cid, n, col, cps) in enumerate(cats):
        k = min(len(cps), 4)
        secs += (f'<section class="cat span-{k}" id="{cid}" style="--c:{col};--n:{k}"><header class="sh"><span class="num">{i+1:02d}</span>'
                 f'<div><h2>{E(n)}</h2><p>Provisional category · <span class="cnt">{len(cps)} {"entry" if len(cps) == 1 else "entries"}</span></p></div></header>\n'
                 f'<div class="grid">{"".join(card(p, col, cid) for p in cps)}</div></section>\n')
    main = f'''<section class="hero" id="top"><div class="h1w"><p class="kick">An open catalog · categories are provisional</p>
<h1>My data.<br>My tools.<br><em>My rules.</em></h1></div>
<div class="hside"><p class="intro">A curated list of open-source and source-available software that keeps your data under your control, sorted by what you want to do and labeled by how you can run it.</p>
<div class="stats"><div><b>{len(ps)}</b><span>entries</span></div><div><b>{len(cats)}</b><span>categories</span></div><div><b>{nos}</b><span>open source</span></div><div><b>{nsh}</b><span>self-host</span></div></div>
<div class="filters" hidden><span>Show</span><button type="button" data-kind="all" class="on" aria-pressed="true">Everything</button><button type="button" data-kind="open-source" aria-pressed="false">Open source</button><button type="button" data-kind="source-available" aria-pressed="false">Source-available</button><button type="button" data-kind="self-host" aria-pressed="false">Self-host</button><button type="button" data-kind="app" aria-pressed="false">App</button></div>
<div class="filters aud-filters" hidden><span>For</span><button type="button" data-aud="all" class="on" aria-pressed="true">Everyone</button><button type="button" data-aud="end-user" aria-pressed="false">●○○ End user</button><button type="button" data-aud="enthusiast" aria-pressed="false">●●○ Enthusiast</button><button type="button" data-aud="expert" aria-pressed="false">●●● Expert</button></div></div></section>
<div class="catflow">
{secs}</div><p class="empty" hidden>No entries match this filter.</p>'''
    return page("My Data, My Tools, My Rules", main, "", nav(cats, "", index=True),
                "An open catalog of open-source and source-available software that keeps your data under your control.")

def media_credit(m):
    note = f'<div class="sub">{inline(m["note"])}</div>' if m.get("note") else ""
    return f'{E(m["credit"])} · <code>{E(m["license"])}</code> · <a href="{E(m["source"])}">source</a>{note}'

def funding_html(p):
    out = []
    for e in p.get("funding") or []:
        when = f', {E(e["when"])}' if e.get("when") else ""
        out.append(f'<li><a href="../funders.html#{fid(e["funder"])}">{E(e["funder"])}</a>: {E(e["what"])}{when} '
                   f'(<a href="{E(e["source"])}">source</a>)</li>')
    return f'<ul class="fund">{"".join(out)}</ul>' if out else ""

def fid(name): return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

def shots_html(p):
    figs = []
    for s in p.get("screenshots") or []:
        figs.append(f'<figure class="shot"><img src="../assets/projects/{E(p["slug"])}/{E(s["file"])}" alt="{E(p["name"])}: {E(s["caption"])}" '
                    f'width="1600" height="1000" loading="lazy" decoding="async"><figcaption>{E(s["caption"])}. '
                    f'<span class="cr">Screenshot: {media_credit(s)}</span></figcaption></figure>')
    return "".join(figs)

def project(p, cats):
    cid = cat_id(p["category"]); i, col = next((k, c[2]) for k, c in enumerate(cats) if c[0] == cid)
    tlabel = " and ".join(["Self-host (server)" if t == "Server" else "App" for t in types(p)])
    rows = [("License", f'<a href="{E(p["source_url"])}"><code>{E(p["license"])}</code></a><div class="tags">{license_tag(p)}</div>'),
            ("Type", f'{tlabel}<div class="tags">{type_tags(p)}</div>')]
    if p.get("audience"): rows.append(("Audience", f'{aud_html(p, "aud aud-l")}<div class="sub">{E(AUD_HELP[p["audience"]])}</div>'))
    rows += [("Website", f'<a href="{E(p["url"])}">{E(host(p["url"]))}</a>'),
             ("Source code", f'<a href="{E(p["repo"])}">{E(host(p["repo"]))}</a>'),
             ("Category", f'<a href="../index.html#{cid}">{E(cat_name(p["category"]))}</a> (provisional)')]
    if p.get("corporate_note"): rows.append(("Organization", inline(p["corporate_note"])))
    if p.get("funding"): rows.append(("Funding", funding_html(p) + '<div class="sub">Funding says nothing about the license.</div>'))
    if p.get("funding_note"): rows.append(("Funding note", inline(p["funding_note"])))
    if p.get("icon"): rows.append(("Logo", media_credit(p["icon"]) + '<div class="sub">Shown unmodified to identify the project. No endorsement implied.</div>'))
    rows.append(("Checked", f'<time datetime="{E(str(p["checked"]))}">{nice_date(p["checked"])}</time>'))
    facts = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    srcs = "".join(f'<li><a href="{E(s)}">{E(host(s))}</a></li>' for s in p["sources"])
    body = markdown(p["body"]); shots = shots_html(p)
    if shots:
        k = body.find("</p>")
        body = body[:k + 4] + shots + body[k + 4:] if k >= 0 else shots + body
    summary = p.get("summary") or p.get("note", "")
    main = f'''<section class="phead" style="--c:{col}"><div><p class="kick"><a href="../index.html">Catalog</a> · <a href="../index.html#{cid}">{i+1:02d} {E(cat_name(p["category"]))}</a></p>
<h1>{icon_html(p, "../")}{E(p["name"])}</h1></div>
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
<p>Open-source and source-available projects that help people keep control of their data and stay independent of large tech companies. Anything an individual can install for private use free of charge qualifies. The categories are provisional and will be refined.</p>
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
<p>Tips and suggestions are always welcome. If you know a project that belongs here, or spot a mistake or an outdated license, please <a href="{REPO}/issues/new?template=suggest-a-project.yml">open an issue on GitHub</a>. We look at every suggestion and check it against the criteria above before adding anything.</p>
</article></div>'''
    return page("About · My Data, My Tools, My Rules", main, "", nav(cats, ""), "About this site, how projects are selected and what the labels mean.")

def funders_page(fs, ps, cats):
    secs = []
    for name, f in sorted(fs.items(), key=lambda x: x[0].lower()):
        items = []
        for p in ps:
            es = [e for e in (p.get("funding") or []) if e["funder"] == name]
            if not es: continue
            what = "; ".join(f'{E(e["what"])}{", " + E(e["when"]) if e.get("when") else ""} (<a href="{E(e["source"])}">source</a>)' for e in es)
            items.append(f'<li><a href="projects/{p["slug"]}.html">{E(p["name"])}</a>: {what}</li>')
        srcs = "".join(f'<li><a href="{E(u)}">{E(host(u))}</a></li>' for u in f["sources"])
        secs.append(f'''<section class="funder" id="{fid(name)}"><h2>{E(name)}</h2>
<p class="fmeta"><a href="{E(f["url"])}">{E(host(f["url"]))}</a></p>
<blockquote><p>“{E(f["mission"])}”</p><footer>— <a href="{E(f["mission_source"])}">{E(name)}, {E(host(f["mission_source"]))}</a></footer></blockquote>
{markdown(f["body"])}
<h3>Projects in this catalog ({len(items)})</h3><ul>{"".join(items)}</ul>
<p class="fsrc">Sources: </p><ol class="flist">{srcs}</ol></section>''')
    main = f'''<section class="phead"><div><p class="kick"><a href="index.html">Catalog</a> · Funders</p><h1>Funders</h1></div>
<p class="intro">Organizations that develop or fund projects listed in this catalog, described in their own words. Funding is shown for transparency; it never decides inclusion and says nothing about a project's license.</p></section>
<div class="body-wrap"><article class="prose">{"".join(secs)}
<p>Spotted a missing grant or a mistake? <a href="{REPO}/issues">Open an issue on GitHub</a>.</p></article></div>'''
    return page("Funders · My Data, My Tools, My Rules", main, "", nav(cats, ""), "Organizations that develop or fund projects in this catalog.")

OMAKASE = os.path.join(ROOT, "content", "omakase.md")

def omakase_page(ps, cats):
    """content/omakase.md: front matter (title, intro), then `## Course` headings with
    `- slug: why` rows (or `- [Name](https://url): why` for things outside the catalog);
    an indented `note: ...` line adds a side note to the row above."""
    o = parse(OMAKASE); by = {p["slug"]: p for p in ps}
    by.update({p["name"].lower(): p for p in ps})
    courses, cur, row = [], None, None
    for l in o["body"].splitlines():
        if not l.strip(): continue
        h = re.match(r"^##\s+(.*)$", l)
        if h: cur = (h.group(1).strip(), []); courses.append(cur); continue
        if cur is None:
            continue
        nm = re.match(r"^\s+note:\s*(.*)$", l)
        if nm:
            if row is not None: row["note"] = nm.group(1).strip().strip('"')
            continue
        li = re.match(r"^-\s+(?:\[([^\]]+)\]\((https?://[^)]+)\)|([^:]+?))\s*:\s*(.*)$", l)
        if not li: sys.exit(f"content/omakase.md: cannot parse line {l!r}")
        if li.group(1): row = {"name": li.group(1), "url": li.group(2), "why": li.group(4)}
        else:
            key = li.group(3).strip(); p = by.get(key) or by.get(key.lower())
            if not p:
                print(f"warning: content/omakase.md: '{key}' has no dossier yet, row skipped", file=sys.stderr); row = None; continue
            row = {"p": p, "why": li.group(4)}
        cur[1].append(row)
    secs = ""
    for n, (title, rows) in enumerate(courses, 1):
        items = ""
        for r in rows:
            if "p" in r:
                p = r["p"]; head = f'{icon_html(p, "")}<a class="on-name" href="projects/{p["slug"]}.html">{E(p["name"])}</a>'
            else:
                head = f'<span class="lt" aria-hidden="true">{E(r["name"][0].upper())}</span><a class="on-name" href="{E(r["url"])}">{E(r["name"])} ↗</a>'
            note = f'<span class="on-note">{inline(r["note"])}</span>' if r.get("note") else ""
            items += f'<li class="on-row"><div class="on-head">{head}</div><p class="on-why">{inline(r["why"])}{note}</p></li>'
        secs += f'<section class="course"><h2><span class="cn">{n:02d}</span>{E(title)}</h2><ul class="menu">{items}</ul></section>'
    intro = f'<p class="intro">{inline(o["intro"])}</p>' if o.get("intro") else ""
    main = f'''<section class="phead omk-head"><div><p class="kick"><a href="index.html">Catalog</a> · Omakase</p>
<h1>{E(o.get("title") or "Omakase")} <span class="jp" lang="ja">お任せ</span></h1></div>{intro}</section>
<div class="omakase">{secs}</div>'''
    return page("Omakase · My Data, My Tools, My Rules", main, "", nav(cats, ""), "A short, personal selection from the catalog.", "omk")

def build(out):
    ps = load_projects(); cats = categories(ps); fs = load_funders(ps)
    if os.path.isdir(out): shutil.rmtree(out)
    os.makedirs(os.path.join(out, "projects"))
    w = lambda rel, s: open(os.path.join(out, rel), "w", encoding="utf-8").write(s)
    w("index.html", index(ps, cats)); w("about.html", about(cats)); w("funders.html", funders_page(fs, ps, cats))
    if os.path.isfile(OMAKASE): w("omakase.html", omakase_page(ps, cats))
    for p in ps: w(f"projects/{p['slug']}.html", project(p, cats))
    shutil.copytree(TH, os.path.join(out, "theme"), ignore=shutil.ignore_patterns("base.html"))
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(out, "assets"))
    print(f"built {len(ps)} projects in {len(cats)} categories, {len(fs)} funders into {out}")

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
