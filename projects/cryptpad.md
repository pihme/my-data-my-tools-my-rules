---
name: CryptPad
slug: cryptpad
category: Collaboration (tentative)
license: AGPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://cryptpad.org/
repo: https://github.com/cryptpad/cryptpad
source_url: https://github.com/cryptpad/cryptpad/blob/main/LICENSE
checked: 2026-11-05
note: End-to-end encrypted collaborative documents you can self-host.
summary: CryptPad is a collaborative office suite with rich text documents, spreadsheets, presentations, forms, kanban boards, whiteboards and a calendar. Content is encrypted in the browser before it reaches the server, so the server operator cannot read it. You can use a public instance or run your own; self-hosting needs two domains and a reverse proxy.
funding_note: FUTO microgrant (November 2024); NLnet funded CryptPad through the NGI0 PET Fund (EU Next Generation Internet).
funders: [futo, nlnet, ngi]
icon: assets/icons/cryptpad.svg
icon_credit: Logo © 2023 XWiki CryptPad Team and contributors, AGPL-3.0-or-later; used to identify the project
icon_source: https://github.com/cryptpad/cryptpad/blob/main/customize.dist/CryptPad_logo.svg
sources:
  - https://cryptpad.org/
  - https://github.com/cryptpad/cryptpad/blob/main/LICENSE
  - https://docs.cryptpad.org/en/admin_guide/installation.html
  - https://futo.tech/grants
  - https://nlnet.nl/project/Cryptpad/
---

CryptPad is a collaborative office suite designed around client-side encryption. You may use a public instance or self-host. LICENSE is GNU AGPL version 3.

## Why it fits

Self-hosting for private groups is free of charge under the AGPL.

## Getting started

Prerequisites (from the official docs):

- A Linux server (the guide targets Debian-class systems) with at least 2 GB RAM, 2 CPU cores and about 20 GB disk
- Two domains or subdomains: one main domain and a separate sandbox domain
- Git and Node.js LTS with npm, or Docker
- A reverse proxy such as Nginx with TLS certificates for public access

Steps:

1. Clone the CryptPad repository and check out the release tag named in the admin guide.
2. Install the dependencies (or follow the Docker section of the same guide).
3. Copy the example configuration and set both domains.
4. Configure the reverse proxy with TLS for both domains.
5. Start CryptPad and open the one-time setup link to create the first administrator.

Official admin installation guide: <https://docs.cryptpad.org/en/admin_guide/installation.html>

## Notes

Public hosted instances may have their own terms; this entry concerns self-install.
