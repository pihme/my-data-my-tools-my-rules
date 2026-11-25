---
name: PhotoPrism
slug: photoprism
category: Media
license: AGPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://www.photoprism.app/
repo: https://github.com/photoprism/photoprism
source_url: https://github.com/photoprism/photoprism/blob/develop/LICENSE
demo: https://try.photoprism.app/
demo_note: Public demo linked from the README; the project asks not to upload private pictures.
checked: 2026-11-25
added: 2026-11-25
setup_steps: 5
setup_clarity: 4
setup_tested: 2026-11-25
note: Self-hosted photo and video library with search, automatic labels, face recognition and maps.
summary: PhotoPrism is a self-hosted app for browsing, organising and sharing photos and videos, including RAW files and Live Photos. It labels pictures by content and location, recognises faces, offers search filters and world maps, and can be installed as a web app on phones. Files are added by upload, from a folder on the server or over WebDAV. The free Community Edition runs in Docker.
corporate_note: Developed by PhotoPrism UG, which holds the copyright and the PhotoPrism trademarks; paid memberships unlock additional features, and commercial licenses are sold for teams.
funding_note: The README describes the project as self-funded, through personal memberships (website, Patreon, GitHub Sponsors) and commercial licenses.
icon: assets/icons/photoprism.svg
icon_credit: PhotoPrism® logo, a trademark of PhotoPrism UG; official file from the repository, unmodified, used to identify the project and linking to photoprism.app
icon_source: https://github.com/photoprism/photoprism/blob/develop/assets/static/icons/logo.svg
fireworks_image: assets/fireworks/cf-photoprism-b1.webp
fireworks_date: 2026-11
sources:
  - https://www.photoprism.app/
  - https://github.com/photoprism/photoprism/blob/develop/LICENSE
  - https://github.com/photoprism/photoprism/blob/develop/README.md
  - https://docs.photoprism.app/getting-started/
  - https://docs.photoprism.app/getting-started/docker-compose/
  - https://www.photoprism.app/kb/personal/
  - https://www.photoprism.app/trademark/
---
## Why it fits

The Community Edition is licensed under the GNU AGPL version 3 and free to self-host; your pictures stay on your own server. The LICENSE adds terms under section 7 that reserve the PhotoPrism trademarks and brand assets; they do not restrict the code license.

## Getting started

Prerequisites (from the official docs):

- A server with a 64-bit operating system, at least 2 CPU cores and 3 GB of RAM, and at least 4 GB of swap
- Docker with Docker Compose
- Enough disk space for your pictures; local SSD storage helps indexing

Steps (Docker Compose, as checked):

1. Download the official `compose.yaml` from the Docker Compose guide.
2. Change the admin and database passwords (default "insecure") and set the folder with your pictures (default `~/Pictures`).
3. Start the stack with `docker compose up -d` and wait for the database setup (about a minute).
4. Open port 2342 in the browser and log in as `admin`.
5. Start indexing in the library, or upload pictures.

Watch out: the Compose file publishes port 2342 on all interfaces and serves plain HTTP unless the site URL is set to HTTPS; use a reverse proxy with HTTPS before opening it to other devices. The initial admin password cannot be changed via the environment variable after the first start (use `photoprism passwd` instead).

Official Docker Compose guide: <https://docs.photoprism.app/getting-started/docker-compose/>

## Notes

Tested with PhotoPrism CE 261029 and MariaDB 12.3 on 2026-11-25. The `photoprism -v` output shows a "Plus" suffix even on the Community Edition image. According to the README, members get additional features such as interactive world maps; the comparison of editions is on photoprism.app. The Compose file also includes optional Ollama, Open WebUI and Watchtower services behind profiles; they are not started by default.
