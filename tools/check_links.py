#!/usr/bin/env python3
"""Check that every internal link and asset reference in the built site resolves.

    python3 tools/check_links.py [SITE_DIR]   # default: ./site
External http(s) links are listed but not fetched.
"""
import html.parser, os, sys, urllib.parse

class Refs(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.refs, self.ids = [], set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a: self.ids.add(a["id"])
        for k in ("href", "src"):
            if a.get(k): self.refs.append(a[k])

def main(site):
    pages, bad, ext = {}, [], set()
    for d, _, fs in os.walk(site):
        for f in fs:
            if f.endswith(".html"):
                p = os.path.join(d, f); r = Refs(); r.feed(open(p, encoding="utf-8").read()); pages[os.path.abspath(p)] = r
    css_refs = []
    for d, _, fs in os.walk(site):
        for f in fs:
            if f.endswith(".css"):
                import re
                p = os.path.join(d, f)
                css_refs += [(p, u) for u in re.findall(r'url\("?([^")]+)"?\)', open(p, encoding="utf-8").read()) if not u.startswith("data:")]
    for p, r in pages.items():
        for ref in r.refs:
            u = urllib.parse.urlparse(ref)
            if u.scheme in ("http", "https"): ext.add(ref); continue
            if u.scheme or ref.startswith("//"): bad.append((p, ref, "unexpected scheme")); continue
            target = os.path.abspath(os.path.join(os.path.dirname(p), urllib.parse.unquote(u.path))) if u.path else p
            if os.path.isdir(target): target = os.path.join(target, "index.html")
            if not os.path.exists(target): bad.append((p, ref, "missing file")); continue
            if u.fragment and u.fragment != "top" and target.endswith(".html"):
                if u.fragment not in pages[target].ids: bad.append((p, ref, "missing anchor"))
            elif u.fragment == "top" and target.endswith(".html") and "top" not in pages[target].ids:
                bad.append((p, ref, "missing anchor"))
    for p, u in css_refs:
        if not os.path.exists(os.path.join(os.path.dirname(p), u)): bad.append((p, u, "missing file (css)"))
    for p, ref, why in bad: print(f"BROKEN {os.path.relpath(p, site)}: {ref} ({why})")
    print(f"{len(pages)} pages checked, {len(bad)} broken internal links, {len(ext)} distinct external links (not fetched)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")))
