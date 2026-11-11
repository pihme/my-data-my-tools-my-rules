---
name: Navidrome
slug: navidrome
category: Media
license: GPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://www.navidrome.org/
repo: https://github.com/navidrome/navidrome
source_url: https://github.com/navidrome/navidrome/blob/master/LICENSE
demo: https://www.navidrome.org/demo/
checked: 2026-11-05
setup_steps: 4
setup_clarity: 4
setup_tested: 2026-11-06
note: Self-hosted music server compatible with Subsonic clients.
summary: Navidrome is a music server that streams your own music collection to its web player and to any Subsonic-compatible app. It is a single lightweight program that also runs well on small hardware such as a Raspberry Pi. It supports multiple users, playlists, lyrics and on-the-fly transcoding.
funding_note: FUTO microgrant (May 2025).
funders: [futo]
icon: assets/icons/navidrome.png
icon_credit: Navidrome logo from the GPL-3.0 repository; used to identify the project
icon_source: https://github.com/navidrome/navidrome/blob/master/resources/logo-192x192.png
fireworks_image: assets/fireworks/cf-navidrome-b1.webp
fireworks_date: 2026-11
role: Music server
sources:
  - https://www.navidrome.org/
  - https://github.com/navidrome/navidrome/blob/master/LICENSE
  - https://www.navidrome.org/docs/installation/
  - https://futo.tech/grants
  - https://www.navidrome.org/docs/installation/docker/
---
## Why it fits

It is licensed under GPL version 3. You can install it on your own machine for private libraries at no license cost.

## Getting started

Prerequisites (from the official docs):

- A server or PC with Docker (a standalone binary is also available)
- Your music collection on a disk the server can read
- Port 4533 reachable from your devices
- The correct user and group IDs so the container can read the music folder

Steps:

1. Create a Docker Compose file (or docker run command) from the official Docker guide.
2. Mount your music folder read-only and a data folder for Navidrome's database.
3. Start the container and open http://<server>:4533.
4. Create the admin user, then connect a Subsonic-compatible app.

Official Docker guide: <https://www.navidrome.org/docs/installation/docker/>

All installation methods: <https://www.navidrome.org/docs/installation/>

## Notes

It works with Subsonic-API clients such as [Amperfy](amperfy.html) for iPhone, iPad and Mac (tested in our own use, November 2026).
