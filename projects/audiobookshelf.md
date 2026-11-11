---
name: Audiobookshelf
slug: audiobookshelf
category: Media
license: GPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://audiobookshelf.org/
repo: https://github.com/advplyr/audiobookshelf
source_url: https://github.com/advplyr/audiobookshelf/blob/master/LICENSE
demo: https://audiobooks.dev/
demo_note: Linked from the official docs; hosted by community member Vito0912; login demo / demo (user account).
checked: 2026-11-11
added: 2026-11-11
setup_steps: 4
setup_clarity: 4
setup_tested: 2026-11-11
note: Self-hosted audiobook and podcast server with progress sync and companion mobile apps.
summary: Audiobookshelf is a self-hosted server for audiobooks and podcasts. It streams your library to the browser and to companion apps for Android and iOS, keeps listening progress per user across devices, downloads podcast episodes and fetches metadata and cover art. It runs in Docker or from Linux packages.
icon: assets/icons/audiobookshelf.svg
icon_credit: Audiobookshelf icon from the GPL-3.0 repository; used to identify the project
icon_source: https://github.com/advplyr/audiobookshelf/blob/master/client/static/icon.svg
sources:
  - https://audiobookshelf.org/
  - https://github.com/advplyr/audiobookshelf/blob/master/LICENSE
  - https://github.com/advplyr/audiobookshelf/blob/master/package.json
  - https://www.audiobookshelf.org/docs
  - https://github.com/advplyr/audiobookshelf-web/blob/master/content/docs/install/2.docker-compose-install.md
  - https://github.com/advplyr/audiobookshelf-web/blob/master/content/docs/install/20.mobile-apps.md
  - https://github.com/advplyr/audiobookshelf-web/blob/master/content/faq/2.server.md
---
## Why it fits

GPL-licensed and free to run on your own server; your audiobooks, podcasts and listening progress stay on hardware you control.

## Getting started

Prerequisites (from the official docs):

- A server or PC with Docker (multi-arch image for amd64, arm64 and arm/v7); Debian/RPM/Nix packages and Windows are also documented
- Separate folders for config, metadata, audiobooks and podcasts
- Port 13378 (host) for the web interface

Steps:

1. Create the Docker Compose file from the install docs (image `ghcr.io/advplyr/audiobookshelf:latest`, port `13378:80`, volumes for `/config`, `/metadata`, `/audiobooks`, `/podcasts`, `TZ` set).
2. Start it with Docker Compose (or the `docker run` command shown on the same page).
3. Open http://<server>:13378 and set the root username and password.
4. Create a library pointing at your audiobook or podcast folder.
5. Optional: install the Android app (Google Play) or join the iOS TestFlight beta and log in to your server.

Watch out: the volume folders must be separate and not nested in each other, and from version 2.3.x `/config` must be on the same machine as the server (no network share).

Official install docs: <https://www.audiobookshelf.org/docs#docker-compose-install>

## Notes

License: the repository LICENSE is GNU GPL version 3 with no "or later" statement and `package.json` says `GPL-3.0`, hence `GPL-3.0-only`. The repository lives under the personal GitHub account advplyr. The mobile apps are a separate repository (advplyr/audiobookshelf-app); per the docs the iOS app is distributed through TestFlight beta testing and the apps are described as beta. The demo is community-hosted, not run by the project.
