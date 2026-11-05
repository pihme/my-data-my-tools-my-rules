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
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m: sys.exit(f"{path}: missing front matter")
    meta, key = {}, None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"): continue
        li = re.match(r"^\s+-\s+(.*)$", line)
        if li and key:
            if not isinstance(meta.get(key), list): meta[key] = []
            meta[key].append(scalar(li.group(1)))
        elif ":" in line and not line[0].isspace():
            key, v = line.split(":", 1); key = key.strip()
            meta[key] = scalar(v) if v.strip() else []
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
    out, para, lst = [], [], None
    def flush():
        nonlocal para, lst
        if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
        if lst: out.append(f"<{lst[0]}>" + "".join(f"<li>{inline(i)}</li>" for i in lst[1]) + f"</{lst[0]}>"); lst = None
    for l in src.splitlines():
        if re.match(r"^#{1,6} ", l):
            flush(); n = len(l) - len(l.lstrip("#")); h = min(6, n + shift)
            out.append(f"<h{h}>{inline(l[n+1:].strip())}</h{h}>")
        elif re.match(r"^\s*([-*]|\d+\.) ", l):
            if para: flush()
            kind = "ol" if re.match(r"^\s*\d+\.", l) else "ul"
            if not lst or lst[0] != kind: flush(); lst = (kind, [])
            lst[1].append(re.sub(r"^\s*([-*]|\d+\.) ", "", l))
        elif not l.strip(): flush()
        else:
            if lst: flush()
            para.append(l.strip())
    flush()
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
        ps.append(p)
    return sorted(ps, key=lambda p: p["name"].lower())

def categories(ps):
    names = sorted({cat_name(p["category"]) for p in ps}, key=str.lower)
    return [(cat_id(n), n, COLORS[i % len(COLORS)], [p for p in ps if cat_name(p["category"]) == n]) for i, n in enumerate(names)]

def nav(cats, root, active=None, index=False):
    items = []
    if index:
        items.append(f'<li><a href="#top" data-cat="all" class="on"><b>··</b>All projects<span>{sum(len(c[3]) for c in cats)}</span></a></li>')
    for i, (cid, n, col, ps) in enumerate(cats):
        href = f"#{cid}" if index else f"{root}index.html#{cid}"
        on = ' class="on"' if cid == active else ""
        items.append(f'<li><a href="{href}" data-cat="{cid}" style="--c:{col}"{on}><b>{i+1:02d}</b>{E(n)}<span>{len(ps)}</span></a></li>')
    return "".join(items)

def page(title, main, root, navhtml, desc, bodyclass=""):
    base = open(os.path.join(TH, "base.html"), encoding="utf-8").read()
    rep = {"{{TITLE}}": E(title), "{{DESCRIPTION}}": E(desc), "{{NAV}}": navhtml, "{{MAIN}}": main,
           "{{REPO}}": REPO, "{{BUILT}}": datetime.date.today().isoformat(), "{{BODYCLASS}}": bodyclass}
    for k, v in rep.items(): base = base.replace(k, v)
    return base.replace("{{ROOT}}", root)

# ---------- pages ----------
def card(p, col, cid):
    note = E(p.get("note") or "") or '<span class="nonote">No note.</span>'
    return f'''<article class="card" data-cat="{cid}" data-kinds="{kinds(p)}"><div class="ct"><span class="lt" aria-hidden="true">{E(p["name"][0].upper())}</span><div><h3><a href="projects/{p["slug"]}.html">{E(p["name"])}</a></h3><span class="spdx" title="SPDX license id">{E(p["license"])}</span></div></div>
<div class="tags">{license_tag(p)}{type_tags(p)}</div>
<p>{note}</p><div class="lnk"><a class="web" href="{E(p["url"])}" title="Website">{E(host(p["url"]))}</a><a class="repo" href="{E(p["repo"])}" title="Source code">repo</a><a class="more" href="projects/{p["slug"]}.html" aria-label="Details on {E(p["name"])}">→</a></div></article>'''

def index(ps, cats):
    nos = sum(p["open_source"] for p in ps); nsh = sum(is_server(p) for p in ps)
    secs = ""
    for i, (cid, n, col, cps) in enumerate(cats):
        k = min(len(cps), 4)
        secs += (f'<section class="cat span-{k}" id="{cid}" style="--c:{col};--n:{k}"><header class="sh"><span class="num">{i+1:02d}</span>'
                 f'<div><h2>{E(n)}</h2><p>Provisional category · <span class="cnt">{len(cps)} {"entry" if len(cps) == 1 else "entries"}</span></p></div></header>\n'
                 f'<div class="grid">{"".join(card(p, col, cid) for p in cps)}</div></section>\n')
    main = f'''<section class="hero" id="top"><div class="h1w"><p class="kick">An open catalogue · categories are provisional</p>
<h1>My data.<br>My tools.<br><em>My rules.</em></h1></div>
<div class="hside"><p class="intro">A hand-picked list of open-source and source-available software that keeps your data under your control, sorted by what you want to do and labeled by how you can run it.</p>
<div class="stats"><div><b>{len(ps)}</b><span>entries</span></div><div><b>{len(cats)}</b><span>categories</span></div><div><b>{nos}</b><span>open source</span></div><div><b>{nsh}</b><span>self-host</span></div></div>
<div class="filters" hidden><span>Show</span><button type="button" data-kind="all" class="on" aria-pressed="true">Everything</button><button type="button" data-kind="open-source" aria-pressed="false">Open source</button><button type="button" data-kind="source-available" aria-pressed="false">Source-available</button><button type="button" data-kind="self-host" aria-pressed="false">Self-host</button><button type="button" data-kind="app" aria-pressed="false">App</button></div></div></section>
<div class="catflow">
{secs}</div><p class="empty" hidden>No entries match this filter.</p>'''
    return page("My Data, My Tools, My Rules", main, "", nav(cats, "", index=True),
                "An open catalogue of open-source and source-available software that keeps your data under your control.")

def project(p, cats):
    cid = cat_id(p["category"]); i, col = next((k, c[2]) for k, c in enumerate(cats) if c[0] == cid)
    tlabel = " and ".join(["Self-host (server)" if t == "Server" else "App" for t in types(p)])
    rows = [("License", f'<a href="{E(p["source_url"])}"><code>{E(p["license"])}</code></a><div class="tags">{license_tag(p)}</div>'),
            ("Type", f'{tlabel}<div class="tags">{type_tags(p)}</div>'),
            ("Website", f'<a href="{E(p["url"])}">{E(host(p["url"]))}</a>'),
            ("Source code", f'<a href="{E(p["repo"])}">{E(host(p["repo"]))}</a>'),
            ("Category", f'<a href="../index.html#{cid}">{E(cat_name(p["category"]))}</a> (provisional)')]
    if p.get("corporate_note"): rows.append(("Organisation", inline(p["corporate_note"])))
    if p.get("funding_note"): rows.append(("Funding", inline(p["funding_note"])))
    rows.append(("Checked", f'<time datetime="{E(str(p["checked"]))}">{nice_date(p["checked"])}</time>'))
    facts = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    srcs = "".join(f'<li><a href="{E(s)}">{E(host(s))}</a></li>' for s in p["sources"])
    main = f'''<section class="phead" style="--c:{col}"><div><p class="kick"><a href="../index.html">Catalogue</a> · <a href="../index.html#{cid}">{i+1:02d} {E(cat_name(p["category"]))}</a></p>
<h1><span class="lt" aria-hidden="true">{E(p["name"][0].upper())}</span>{E(p["name"])}</h1></div>
<p class="intro">{E(p.get("note", ""))}</p></section>
<div class="body-wrap" style="--c:{col}"><article class="prose">{markdown(p["body"])}
<section class="sources"><h2>Sources</h2><ol>{srcs}</ol></section>
<a class="back" href="../index.html#{cid}">← Back to the catalogue</a></article>
<aside class="facts" aria-label="Facts"><dl>{facts}</dl></aside></div>'''
    return page(f'{p["name"]} · My Data, My Tools, My Rules', main, "../", nav(cats, "../", active=cid),
                p.get("note") or p["name"])

def about(cats):
    readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    m = re.search(r"^## About this site\n(.*?)(?=^## |\Z)", readme, re.S | re.M)
    if not m: sys.exit("README.md: no '## About this site' section")
    main = f'''<section class="phead"><div><p class="kick"><a href="index.html">Catalogue</a> · About</p><h1>About this site</h1></div>
<p class="intro">How this catalogue is made, what goes in and what the labels mean.</p></section>
<div class="body-wrap"><article class="prose">{markdown(m.group(1).strip())}
<h2 id="what-belongs-here">What belongs here</h2>
<p>Open-source and source-available projects that help people keep control of their data and stay independent of large tech companies. Anything an individual can install for private use free of charge qualifies. The categories are provisional and will be refined.</p>
<h2 id="license-labels">License labels</h2>
<p><strong>Open source</strong> means the license is OSI-approved. <strong>Source-available</strong> means the source code is public, but the license is not OSI-approved and usually restricts some uses; these entries carry a <code>LicenseRef-*</code> id instead of a standard SPDX id. Every entry shows its license id and links to the license file it was checked against, with the date of the check.</p>
<p><strong>Self-host</strong> marks server software you run on your own hardware. <strong>App</strong> marks software you install on your own device. Some projects are both.</p>
<p>Want to suggest a project or report a mistake? <a href="{REPO}/issues">Open an issue on GitHub</a>.</p>
</article></div>'''
    return page("About · My Data, My Tools, My Rules", main, "", nav(cats, ""), "About this site, what belongs here and what the license labels mean.")

def build(out):
    ps = load_projects(); cats = categories(ps)
    if os.path.isdir(out): shutil.rmtree(out)
    os.makedirs(os.path.join(out, "projects"))
    w = lambda rel, s: open(os.path.join(out, rel), "w", encoding="utf-8").write(s)
    w("index.html", index(ps, cats)); w("about.html", about(cats))
    for p in ps: w(f"projects/{p['slug']}.html", project(p, cats))
    shutil.copytree(TH, os.path.join(out, "theme"), ignore=shutil.ignore_patterns("base.html"))
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(out, "assets"))
    print(f"built {len(ps)} projects in {len(cats)} categories into {out}")

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
