# Changelog

## 2.0.1 (unreleased)

### Fixed
- Logos no longer spill out of their tiles. Cause: browsers kept the cached 1.x stylesheet, which has no logo rules, so logos were drawn at their full file size (up to 512 px). The stylesheet and script are now loaded as `theme/style.css?v=<VERSION>` and `theme/site.js?v=<VERSION>`, with `VERSION` in `build.py` bumped per release.
- Every logo `<img>` now has explicit `width`/`height` attributes (24 px on cards, 20 px on Omakase rows, 60 px on project pages), so logos stay small even without the stylesheet. Tiles are fixed-size with `overflow: hidden` and fixed pixel logo sizes in CSS (40 px project-page logo on screens up to 600 px), with no percentage heights. Percentage heights can resolve against an SVG's intrinsic size in WebKit.

### Added
- Optional `icon_scale` (1–2) in dossiers to optically enlarge logos with built-in whitespace. The logo file stays unchanged. Used for ONLYOFFICE (2).

## 2.0 (unreleased)

### Added
- Card paragraphs: every entry has a 2–4 sentence summary.
- Project logos on cards and project pages where the logo license or brand guidelines allow it, with credit; letter tile otherwise. Every file is listed with source, terms and credit in `assets/ASSETS.md`, and the build accepts only files cleared there.
- Screenshots on project pages (16:10 frame, with credit, terms and source) where a reusable license is stated.
- Audience indicator (End user / Enthusiast / Expert) on cards and project pages.
- Filter bar grouped into License, Runs as and For, with "Reset filters", an empty state and a right-edge fade on scrollable rows on mobile.
- New projects: Restic, Paperless-ngx, Beszel, Uptime Kuma, ONLYOFFICE and OpenCode; new categories Backup, Monitoring and AI. The catalog now has 30 projects.
- Funding notes on project pages, linked to the Funders page.
- Funders page (FUTO, NLnet, Next Generation Internet) with each organization's mission in its own words and the listed projects it supports.
- Omakase page: a short personal selection in two courses (Desktop, Home server).
- Selection criteria on the About page; "Suggest a project" issue form.
- Markdown support for fenced code blocks, numbered steps and callouts in dossiers.

### Changed
- "hand-picked" is now "curated"; the "All projects" entry is now "Catalog".
- About page starts with "What belongs here", followed by the selection criteria.
- Getting started sections rewritten as prerequisites, steps and the official install link; Vaultwarden link points to the Using-Docker-Compose wiki page.
- US spelling throughout; compact, horizontally scrolling category chips on mobile; mobile spacing fixes (merged after 1.0, first released with 2.0).

## 1.0
- First version of the site with 24 project dossiers.
