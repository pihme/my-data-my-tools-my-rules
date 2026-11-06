# Changelog

## 2.3.13

- Dossier pages: optional Code Fireworks tile (variant B1) in the header when `fireworks_image` and `fireworks_date` (YYYY-MM) are set. Dark `#111` tile (~270 px), always the same in light and dark mode; caption "As of …" plus a link to https://x.com/code_fireworks. Hidden below 1280 px so the intro does not shift. Dossiers without the fields are unchanged.

## 2.3.12

- Content v2.15 (supersedes v2.14): Jitsi Meet getting-started path hands-on checked (docker-jitsi-meet `stable-11248-3`); dossier adds `setup_steps: 6`, `setup_clarity: 3`, `setup_tested: 2026-11-06`, concrete Compose v2 steps, and notes what was and was not verified.

## 2.3.11

- Content v2.12: optional `demo` / `demo_note` front-matter fields; dossier facts show a "Try the online demo" link (and optional note) for CryptPad, Forgejo, Home Assistant, Immich, Jellyfin, Jitsi Meet, mailcow, Navidrome, Nextcloud, openHAB, Paperless-ngx, Uptime Kuma and YunoHost.
- Content v2.13: Jitsi Meet icon replaced with the official blue Android app icon (PNG); the pale favicon SVG is removed.

## 2.3.10

- Home page: packed category rows keep equal card heights (category stretches, cards `height:100%`, footer pinned with `margin-top:auto`). Card footer always shows the hostname on its own line, then audience level left and `repo →` right (no mid-footer wrap).

## 2.3.9

- Content v2.11: new dossier Jitsi Meet under Office (Apache-2.0; self-hostable; meet.jit.si login note); 30 dossiers.

## 2.3.8

- Open Graph / Twitter Card meta tags on every page (`og:image` points at `assets/social-preview.png`, 1280×640).

## 2.3.7

- Content v2.10: category Cloud/Files renamed to Files (anchor `#files`, still second).

## 2.3.6

- Content v2.9: Organic Maps (from Utilities) and Grayjay (from Media) move to Mobile; the "Not found" section is removed from the funders page.

## 2.3.5

- Content v2.8: Omakase page reordered (Paperless-ngx, Immich and Navidrome open the second course), Mobile text clarified (uploads only on the home network, app offline otherwise), Syncthing text corrected (a public discovery server helps peers find each other). Syncthing dossier names the discovery and relay servers.

## 2.3.4

- Content v2.7: CryptPad moves from Collaboration to Office (Office 3); the empty Collaboration category is dropped (9 categories). PeerTube is removed from the catalog (dossier, icon and ASSETS.md row deleted); 29 dossiers.

## 2.3.3

- Content v2.5: new dossier Pangolin (Server, AGPL-3.0 Community Edition; FUTO microgrant noted as funding). 30 dossiers, Server 8. No icon (Fossorial trademark terms), letter tile; ASSETS.md lists the reason.

## 2.3.2 (unreleased)

### Changed
- Omakase marker set to variant B: 2px ink frame on marked cards, the お任せ OMAKASE badge sits as a tab on the card's top edge (no longer squeezes long names), extra row gap in grids with marked cards; same badge style under the dossier title.
- Dossier facts box: new row “Omakase” (“In daily use by the curator”, linking to the Omakase page) for marked projects.
- Content v2.6: Garage moves from Cloud/Files to Server; new category Office with ONLYOFFICE and Paperless-ngx (10 categories: Cloud/Files 2, Collaboration 1, Office 2, Server 7). New anchor `#office`. Omakase: Syncthing added under Desktop (8 marked projects).

## 2.3.1 (unreleased)

### Changed
- Content v2.4: Signal moves to Mobile; the Messaging category is gone (29 projects, 9 categories). Anchor `#messaging` removed; Signal is now under `#mobile`.

### Removed
- Element dossier and icon.

## 2.3.0 (unreleased)

### Added
- Omakase marker: catalog cards of projects on the Omakase page get a black frame and an “お任せ Omakase” badge; their dossiers show the same badge under the title. The badge links to the Omakase page. The set is derived from `content/omakase.md`.

## 2.2.1 (unreleased)

### Changed
- Omakase: new course “Dessert: Mobile” with the Immich app (camera-roll backup to your own server, library on the go); the phone-app mention moved out of the home-server Immich entry.

## 2.2.0 (unreleased)

### Changed
- Content v2.2: categories merged to 10 — AI, Cloud/Files, Collaboration, Media, Messaging, Mobile, Passwords, Server, Smart Home, Utilities.
- Category anchors: `#photos` and `#video-media` → `#media`; `#keyboard` and `#mobile-app-stores` → `#mobile`; `#backup`, `#email`, `#monitoring` and `#hosting-platform` → `#server`; `#maps` and `#search` → `#utilities`.
- Dossier abstracts: summary is again the short v2.1 lead; the duplicate first body paragraph is gone. Unique facts from that paragraph now open “Why it fits”.
- Getting started step lists aligned with `setup_steps` for all 21 tested projects.

## 2.1.0 (unreleased)

### Changed
- Dossier intro: summary shown as a full-width lead under the title with a category-colour bar (variant A); catalog hero and Omakase unchanged.
- Content update: fixed setup links and Getting started paths for Vaultwarden, YunoHost, Nextcloud (AIO), PeerTube (Docker), Element and Syncthing.
- Short Watch out notes for known pitfalls in the official guides of Garage, Jellyfin, ONLYOFFICE, CryptPad, Paperless-ngx and openHAB.
- "(tentative)" removed from remaining category labels in dossiers that the v2.1 package did not re-export.

### Added
- Optional dossier fields `setup_steps`, `setup_clarity` (1–5) and `setup_tested` (date). When a project was hands-on checked, the Getting started section (and the catalog card) show e.g. "7 steps · clarity 4/5"; untested projects show nothing. No minutes.
- "Watch out:" lines in dossiers render as styled callouts.
- Sidebar "Catalog" entry on every page (not only the index), linking back to the catalog. About-list entries (Omakase, About this site, Funders) get `class="on"` on their own page.
- Cache-bust query `?v=<VERSION>` also on `theme/fonts.css`.
- Funders page no longer lists supported projects per funder (PM v2.2); dossiers with `funders:` link to `#futo` / `#nlnet` / `#ngi` on the Funders page.
- Tested projects show a Setup row in the dossier fact box (below Audience), repeating e.g. "5 steps · clarity 3/5" with the check date; the same line stays under Getting started.

## 2.0.1 (unreleased)

### Fixed
- Logos no longer spill out of their tiles. Cause: browsers kept the cached 1.x stylesheet, which has no logo rules, so logos were drawn at their full file size (up to 512 px). The stylesheet and script are now loaded as `theme/style.css?v=<VERSION>` and `theme/site.js?v=<VERSION>`, with `VERSION` in `build.py` bumped per release.
- Every logo `<img>` now has explicit `width`/`height` attributes (24 px on cards, 20 px on Omakase rows, 60 px on project pages), so logos stay small even without the stylesheet. Tiles are fixed-size with `overflow: hidden` and fixed pixel logo sizes in CSS (40 px project-page logo on screens up to 600 px), with no percentage heights. Percentage heights can resolve against an SVG's intrinsic size in WebKit.

### Changed
- "Provisional" wording removed: no "provisional" label next to Categories in the sidebar, category headers show only the entry count, the hero kicker reads "An open catalog", project pages no longer mark the category as provisional, and the About text drops the sentence about provisional categories.

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
