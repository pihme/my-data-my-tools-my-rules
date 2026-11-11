---
name: Amperfy
slug: amperfy
category: Media
license: GPL-3.0-or-later
open_source: true
type: App
audience: end-user
url: https://github.com/BLeeEZ/amperfy
repo: https://github.com/BLeeEZ/amperfy
source_url: https://github.com/BLeeEZ/amperfy/blob/master/LICENSE
checked: 2026-11-08
added: 2026-11-08
note: Music player for iPhone, iPad and Mac that streams from your own Ampache or Subsonic server.
summary: Amperfy is an iOS, iPadOS and macOS app that plays music, podcasts and radio from an Ampache or Subsonic-compatible server. It supports several accounts, an offline mode, CarPlay, gapless playback, an equalizer, replay gain and scrobbling. It is a client only, so you need a music server such as Ampache or another Subsonic-compatible server.
icon: assets/icons/amperfy.png
icon_credit: Amperfy app icon from the GPL-3.0 repository; used to identify the project
icon_source: https://github.com/BLeeEZ/amperfy/blob/master/AmperfyKit/Assets/Assets.xcassets/Icon-1024.imageset/Icon-1024.png
sources:
  - https://github.com/BLeeEZ/amperfy
  - https://github.com/BLeeEZ/amperfy/blob/master/LICENSE
  - https://apps.apple.com/app/amperfy-music/id1530145038
---
## Why it fits

It is licensed under GPL version 3 or later and is free on the App Store. It plays music from a server you run yourself, and the App Store privacy label states that the developer does not collect any data from the app.

## Getting started

Prerequisites (from the official docs):

- An iPhone, iPad or Mac with iOS, iPadOS or macOS 26.0 or later (App Store listing)
- A running Ampache server or a server with the Subsonic API 1.8 or newer (Subsonic 4.8+), with your music and a user account (App Store listing)
- The server address reachable from your device

Steps:

1. Install Amperfy Music from the App Store (iPhone, iPad or Mac).
2. Open the app and log in to your server.

Official download links: <https://github.com/BLeeEZ/amperfy#basics>

## Notes

The app is a client only and needs a music server. The README names Ampache and Subsonic. It also works with [Navidrome](navidrome.html), which speaks the Subsonic API (tested in our own use, November 2026), although the README does not list Navidrome by name. The app has no official website; the GitHub repository is the project home. The App Store build is published by Dirk Hildebrand, while the source code is by Maximilian Bauer (BLeeEZ). Building from source needs Xcode 26; testing CarPlay and Siri on a real device needs an Apple developer certificate.
