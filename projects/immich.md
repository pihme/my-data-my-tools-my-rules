---
name: Immich
slug: immich
category: Photos
license: AGPL-3.0-only
open_source: true
type: [Server, App]
audience: enthusiast
url: https://immich.app/
repo: https://github.com/immich-app/immich
source_url: https://github.com/immich-app/immich/blob/main/LICENSE
checked: 2026-11-05
setup_steps: 7
setup_clarity: 5
setup_tested: 2026-11-06
note: Self-hosted photo and video backup with mobile apps.
summary: Immich is a self-hosted photo and video library with mobile apps that back up your camera roll automatically. It offers a timeline, albums, sharing, a map view and machine-learning features such as face recognition and smart search that run on your own server. It is deployed with Docker Compose and licensed under AGPL-3.0.
corporate_note: Team/brand associated with FUTO; project remains AGPL-3.0.
funding_note: A FUTO project: the core team joined FUTO in May 2024 and works on Immich full-time; the license stays AGPL-3.0.
funders: [futo]
screenshot: assets/screenshots/immich.webp
screenshot_credit: Screenshot from the Immich documentation, AGPL-3.0 repository
screenshot_source: https://github.com/immich-app/immich/blob/main/docs/static/img/screenshot-light.webp
sources:
  - https://immich.app/
  - https://github.com/immich-app/immich/blob/main/LICENSE
  - https://futo.tech/projects
  - https://immich.app/blog/immich-joins-futo
  - https://docs.immich.app/overview/quick-start/
---

Immich is a self-hosted photo and video backup stack with server, web UI, and mobile clients. It stores media on hardware you control. The server repository LICENSE file is GNU AGPL version 3 (no “or later” clause observed in the LICENSE header).

## Why it fits

You can install the server and apps yourself at no charge for private use. Source is public under an OSI-approved license.

## Getting started

Prerequisites (from the official docs):

- A Linux server (or a supported OS) with Docker and Docker Compose
- At least 6 GB RAM and 2 CPU cores according to the official requirements
- Enough disk space for your photo library (set via UPLOAD_LOCATION)
- Port 2283 reachable from your devices

Steps:

1. Create a directory and download docker-compose.yml and example.env from the latest release, as shown in the quick start.
2. Rename example.env to .env and set UPLOAD_LOCATION and a database password.
3. Start the stack with docker compose up -d.
4. Open http://<server>:2283 and create the admin account.
5. Install the mobile app, log in to your server and enable backup.

Official quick start: <https://docs.immich.app/overview/quick-start/>

## Notes

Association with FUTO is organizational context only; it does not change the AGPL license label.
