---
name: CryptPad
slug: cryptpad
category: Office
license: AGPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://cryptpad.org/
repo: https://github.com/cryptpad/cryptpad
source_url: https://github.com/cryptpad/cryptpad/blob/main/LICENSE
demo: https://cryptpad.fr/
demo_note: Public instance run by the CryptPad team; no account needed to try it.
checked: 2026-11-05
setup_steps: 6
setup_clarity: 2
setup_tested: 2026-11-06
note: End-to-end encrypted collaborative documents you can self-host.
summary: CryptPad is a collaborative office suite with rich text documents, spreadsheets, presentations, forms, kanban boards, whiteboards and a calendar. Content is encrypted in the browser before it reaches the server, so the server operator cannot read it. You can use a public instance or run your own; self-hosting needs two domains and a reverse proxy.
funding_note: FUTO microgrant (November 2024); NLnet funded CryptPad through the NGI0 PET Fund (EU Next Generation Internet).
funders: [futo, nlnet, ngi]
icon: assets/icons/cryptpad.svg
icon_credit: Logo © 2023 XWiki CryptPad Team and contributors, AGPL-3.0-or-later; used to identify the project
icon_source: https://github.com/cryptpad/cryptpad/blob/main/customize.dist/CryptPad_logo.svg
fireworks_image: assets/fireworks/cf-cryptpad-b1.webp
fireworks_date: 2026-11
sources:
  - https://cryptpad.org/
  - https://github.com/cryptpad/cryptpad/blob/main/LICENSE
  - https://docs.cryptpad.org/en/admin_guide/installation.html
  - https://futo.tech/grants
  - https://nlnet.nl/project/Cryptpad/
---
## Why it fits

Self-hosting for private groups is free of charge under the AGPL.

## Getting started

Prerequisites (from the official docs):

- A Linux server (the guide targets Debian-class systems) with at least 2 GB RAM, 2 CPU cores and about 20 GB disk
- Two domains or subdomains: one main domain and a separate sandbox domain
- Git and Node.js LTS with npm, or Docker
- A reverse proxy such as Nginx with TLS certificates for public access

Steps:

1. Get the official Docker Compose file from the admin installation guide.
2. Edit the two domain settings (main domain and sandbox domain).
3. Create the data directories, including config, and chown them to UID/GID 4001.
4. Start the stack with docker compose up -d.
5. Read the one-time admin install URL from the container logs.
6. Open that URL and create the first administrator.

Watch out: if you use Docker Compose, create and chown the `config` directory (UID/GID 4001) before `compose up`; the documented mkdir list omits it, Docker then creates it as root, and the container fails writing `config.js`. Use the environment variable names from the compose file you run (the docs and compose disagree on the OnlyOffice install flag name).

Official admin installation guide: <https://docs.cryptpad.org/en/admin_guide/installation.html>

## Notes

Public hosted instances may have their own terms; this entry concerns self-install.
