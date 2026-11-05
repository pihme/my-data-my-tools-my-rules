---
name: Forgejo
slug: forgejo
category: Hosting Platform
license: GPL-3.0-or-later
open_source: true
type: Server
audience: enthusiast
url: https://forgejo.org/
repo: https://codeberg.org/forgejo/forgejo
source_url: https://codeberg.org/forgejo/forgejo/src/branch/forgejo/LICENSE
checked: 2026-11-05
setup_steps: 6
setup_clarity: 4
setup_tested: 2026-11-06
note: Self-hosted Git forge (community soft-fork lineage from Gitea).
summary: Forgejo is a self-hosted software forge for Git repositories, issues, pull requests, wikis, package registries and CI. It started as a fork of Gitea and is developed as a community project; Codeberg e.V. runs the best-known public instance. It runs as a single binary or container and works with SQLite, PostgreSQL or MySQL.
corporate_note: Community project; Codeberg e. V. is a major deployer/context (info only).
funding_note: NLnet funded Forgejo through the NGI0 Entrust Fund (EU Next Generation Internet), run by Codeberg e.V.
funders: [nlnet, ngi]
icon: assets/icons/forgejo.svg
icon_credit: Forgejo logo by Caesar Schinas, CC BY-SA 4.0
icon_source: https://codeberg.org/forgejo/forgejo/src/branch/forgejo/assets/logo.svg
sources:
  - https://forgejo.org/
  - https://codeberg.org/forgejo/forgejo/src/branch/forgejo/LICENSE
  - https://forgejo.org/docs/latest/admin/installation/
  - https://nlnet.nl/project/Forgejo/
  - https://forgejo.org/docs/latest/admin/installation/docker/
---

Forgejo is a self-hosted software forge for Git hosting and collaboration. The README states GPL version 3.0 or any later version (since v9.0).

## Why it fits

You can run a private Git service without relying on a commercial SaaS.

## Getting started

Prerequisites (from the official docs):

- A Linux host with Docker (a single binary install is also documented)
- Free ports for the web interface (default 3000) and Git over SSH
- SQLite for small setups, or PostgreSQL/MySQL
- A reverse proxy with TLS if the forge is reachable from the internet

Steps:

1. Create a directory with the Docker Compose file from the official Docker guide.
2. Choose the database and set the data volume.
3. Start the stack with docker compose up -d.
4. Open the web interface and complete the initial configuration, including the admin account.

Official Docker installation guide: <https://forgejo.org/docs/latest/admin/installation/docker/>

All installation methods: <https://forgejo.org/docs/latest/admin/installation/>

## Notes

Funding note points at NLnet’s general project index; specific grant line items were not individually re-audited.
