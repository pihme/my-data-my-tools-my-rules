---
name: Paperless-ngx
slug: paperless-ngx
category: Cloud/Files
license: GPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://docs.paperless-ngx.com/
repo: https://github.com/paperless-ngx/paperless-ngx
source_url: https://github.com/paperless-ngx/paperless-ngx/blob/dev/LICENSE
checked: 2026-11-05
setup_steps: 8
setup_clarity: 2
setup_tested: 2026-11-06
note: Self-hosted document archive with OCR, tagging and full-text search.
summary: Paperless-ngx is a document management system that turns scanned paper and PDFs into a searchable archive. It runs OCR on incoming documents, assigns tags, correspondents and document types, and keeps the originals on your server. It is the community-maintained successor of Paperless and Paperless-ng and is usually installed with Docker Compose.
funding_note: The project README credits Fyra Stack with hosting the public demo.
icon: assets/icons/paperless-ngx.svg
icon_credit: Paperless-ngx leaf logo from the GPL-3.0 repository; used to identify the project
icon_source: https://github.com/paperless-ngx/paperless-ngx/blob/dev/docs/assets/logo_leaf.svg
screenshot: assets/screenshots/paperless-ngx.webp
screenshot_credit: Screenshot from the Paperless-ngx documentation, GPL-3.0 repository
screenshot_source: https://github.com/paperless-ngx/paperless-ngx/blob/dev/docs/assets/screenshots/documents-smallcards.png
sources:
  - https://docs.paperless-ngx.com/
  - https://github.com/paperless-ngx/paperless-ngx/blob/dev/LICENSE
  - https://github.com/paperless-ngx/paperless-ngx/blob/dev/README.md
  - https://docs.paperless-ngx.com/setup/
  - https://github.com/jonaswinkler/paperless-ng
---

Paperless-ngx indexes scanned documents and PDFs, runs OCR and makes them searchable in a web interface. The repository LICENSE is the GNU GPL version 3 (no "or later" statement found, hence `GPL-3.0-only`).

## Why it fits

Free to self-host for a private household archive; documents stay on your own server.

## Getting started

Prerequisites (from the official docs):

- A Linux server or PC with Docker and Docker Compose
- Disk space for your documents
- Optionally a scanner that can save to a network folder (the consume folder)

Steps:

1. Run the interactive install script from the setup guide, or download a Docker Compose template for your database.
2. Adjust the paths for the consume, media and data folders and the settings in docker-compose.env.
3. Pull the images and start the stack with docker compose up -d.
4. Open the web interface, log in with the admin account and drop a first PDF into the consume folder.

Watch out: before `compose up` on the Compose route, replace `PAPERLESS_SECRET_KEY=change-me` in `docker-compose.env` with a real secret (for example `openssl rand -hex 32`); the webserver will not start while the default value remains.

Official setup guide: <https://docs.paperless-ngx.com/setup/>

## Notes

The earlier project paperless-ng is discontinued: its GitHub repository is archived (last push February 2023) and its README points to paperless-ngx as the direct continuation and drop-in replacement. The paperless-ngx README calls itself the official successor of Paperless and Paperless-ng.
