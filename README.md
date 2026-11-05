# My Data, My Tools, My Rules

A catalog of open-source projects that help people keep control of their
data and stay independent of large tech companies. The site is published
with GitHub Pages and will be structured like a wiki.

Status: just started. Inclusion criteria and the first project list are
being worked out.

## About this site

Most of this site is written and maintained with the help of AI tools: project research, descriptions, license labels and the site code itself. A human does light editorial review, picks what goes in and has the final say, but does not check every detail by hand. If you spot a mistake, an outdated license or a project that doesn't belong here, please open an issue on GitHub.

The person behind this site uses it too, to discover new tools and try them out. It is a list we rely on ourselves, not just one we publish.

## Building the site

The site is generated from the dossiers in `projects/` by a small Python
script with no dependencies beyond Python 3.8+.

```sh
python3 build.py              # writes the site to ./site
python3 build.py --serve      # build, then serve on http://localhost:8000
python3 tools/check_links.py  # check internal links in ./site
tools/deploy.sh               # build, check and publish to the gh-pages branch
```

Other content: `funders/` (one Markdown file per funding organization,
used for the Funders page), `content/` (selection criteria shown on the
About page and the optional Omakase page), project logos and screenshots in
`assets/projects/<slug>/` (licenses tracked in `projects/MEDIA.md`).

The theme lives in `theme/` (HTML template, CSS, a small script for the
filters and dark mode, self-hosted fonts under the SIL Open Font License),
logos and favicons in `assets/`. All links are relative, so the output
works under the GitHub Pages path `/my-data-my-tools-my-rules/`.

## License

CC BY-ND 4.0, see [LICENSE](LICENSE).
