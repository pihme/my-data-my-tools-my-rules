---
name: Jellyfin
slug: jellyfin
category: Video/Media
license: GPL-2.0-only
open_source: true
type: [Server, App]
audience: enthusiast
url: https://jellyfin.org/
repo: https://github.com/jellyfin/jellyfin
source_url: https://github.com/jellyfin/jellyfin/blob/master/LICENSE
checked: 2026-11-05
setup_steps: 5
setup_clarity: 3
setup_tested: 2026-11-06
note: Self-hosted media server for your own libraries.
summary: Jellyfin is a media server for your own movies, TV shows, music and photos. It organizes the library with metadata and streams to web browsers, phones, TVs and other clients, transcoding when needed. It has no premium tier and needs no external account. Jellyfin is a volunteer project that started as a fork of Emby.
corporate_note: Jellyfin Foundation / community project.
funding_note: The project README names JetBrains as a supporter.
icon: assets/icons/jellyfin.svg
icon_credit: Jellyfin logo from jellyfin-ux, CC BY-SA 4.0
icon_source: https://github.com/jellyfin/jellyfin-ux/blob/master/logos/SVG/jellyfin-icon--color-on-light.svg
screenshot: assets/screenshots/jellyfin.webp
screenshot_credit: Screenshot from jellyfin-ux (Android store assets), CC BY-SA 4.0
screenshot_source: https://github.com/jellyfin/jellyfin-ux/blob/master/branding/android/mobile/fastlane/phoneScreenshots/screenshot_phone_1.png
sources:
  - https://jellyfin.org/
  - https://github.com/jellyfin/jellyfin/blob/master/LICENSE
  - https://jellyfin.org/docs/general/installation/
  - https://github.com/jellyfin/jellyfin/blob/master/README.md
  - https://jellyfin.org/docs/general/installation/container/
---

Jellyfin is a media system that lets you stream your own video and audio libraries from a server you operate. Clients exist for several platforms. Server LICENSE is GPL version 2.

## Why it fits

Server and clients can be installed without a paid product license for private use.

## Getting started

Prerequisites (from the official docs):

- A server or PC with Docker (native packages for Linux, Windows and macOS are also available)
- Your media files on a disk the server can read
- Port 8096 for the web interface (UDP ports are used for optional client discovery)

Steps:

1. Pull the official jellyfin/jellyfin image.
2. Start it with volumes for config, cache and your media, as shown in the container guide.
3. Open http://<server>:8096 and run the setup wizard.
4. Add your media libraries and install Jellyfin clients on your devices.

Watch out: the main `docker run` example puts comments after line continuations (`\`); pasting that as-is stops the command early and runs the remaining lines on the host. Use the Compose example, or remove the inline comments before pasting.

Official container guide: <https://jellyfin.org/docs/general/installation/container/>

All installation methods: <https://jellyfin.org/docs/general/installation/>

## Notes

Some client stores may have their own distribution terms; core server remains GPL-2.0.
