---
name: Paperless-ngx
slug: paperless-ngx
category: Office
license: GPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://docs.paperless-ngx.com/
repo: https://github.com/paperless-ngx/paperless-ngx
source_url: https://github.com/paperless-ngx/paperless-ngx/blob/dev/LICENSE
demo: https://demo.paperless-ngx.com/
demo_note: Log in with demo / demo; content is reset frequently, do not upload private files.
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
fireworks_image: assets/fireworks/cf-paperless-ngx-b1.webp
fireworks_date: 2026-11
sources:
  - https://docs.paperless-ngx.com/
  - https://github.com/paperless-ngx/paperless-ngx/blob/dev/LICENSE
  - https://github.com/paperless-ngx/paperless-ngx/blob/dev/README.md
  - https://docs.paperless-ngx.com/setup/
  - https://github.com/jonaswinkler/paperless-ng
---
## Why it fits

The repository LICENSE is GNU GPL version 3 with no "or later" statement (GPL-3.0-only). Free to self-host for a private household archive; documents stay on your own server.

## Getting started

Prerequisites (from the official docs):

- A Linux server or PC with Docker and Docker Compose
- Disk space for your documents
- Optionally a scanner that can save to a network folder (the consume folder)

Steps:

1. Download the three Docker Compose template files from the setup guide for your database.
2. Edit the compose file for your paths and database choice.
3. Edit docker-compose.env (consume/media/data paths and UID/GID).
4. Replace PAPERLESS_SECRET_KEY=change-me with a real secret (for example openssl rand -hex 32).
5. Pull the images with docker compose pull.
6. Start the stack with docker compose up -d.
7. Open http://<server>:8000.
8. Create the Django superuser and drop a first PDF into the consume folder.

Watch out: before `compose up` on the Compose route, replace `PAPERLESS_SECRET_KEY=change-me` in `docker-compose.env` with a real secret (for example `openssl rand -hex 32`); the webserver will not start while the default value remains.

Official setup guide: <https://docs.paperless-ngx.com/setup/>

## Notes

The earlier project paperless-ng is discontinued: its GitHub repository is archived (last push February 2023) and its README points to paperless-ngx as the direct continuation and drop-in replacement. The paperless-ngx README calls itself the official successor of Paperless and Paperless-ng.
