---
name: F-Droid
slug: f-droid
category: Mobile/App Stores (tentative)
license: GPL-3.0-or-later
open_source: true
type: App
url: https://f-droid.org/
repo: https://github.com/f-droid/fdroidclient
source_url: https://github.com/f-droid/fdroidclient/blob/master/LICENSE
checked: 2026-11-05
note: Android app store client for free and open-source apps; repos can be self-hosted.
corporate_note: Alternative distribution to Google Play (info only).
summary: "F-Droid is a catalog of free and open-source Android apps together with a client app to install and update them. It is an alternative to Google Play for the apps it carries, and its main repository builds apps from their source code. You install the F-Droid client on your phone; the server tools also let you publish your own app repository."
audience: End user
icon:
  file: "icon.svg"
  credit: "William Theaker, Robert Martinez, Andrew Nayenko"
  license: "CC-BY-SA-3.0 OR GPL-3.0-or-later"
  source: "https://github.com/f-droid/fdroidclient/blob/master/logo-icon.svg"
  note: "License stated at https://f-droid.org/docs/Licenses/"
screenshots:
  - file: "screenshot-1.webp"
    caption: "Latest apps, search, and app details in the Android client"
    credit: "F-Droid contributors"
    license: "GPL-3.0-or-later"
    source: "https://github.com/f-droid/fdroidclient/tree/master/src/full/fastlane/metadata/android/en-US/images/phoneScreenshots"
funding:
  - funder: "NLnet"
    what: "NGI0 Entrust grant (Reproducible F-Droid)"
    when: "2023-06 to 2025-05"
    source: "https://nlnet.nl/project/Reproducible-F-Droid/"
  - funder: "NLnet"
    what: "NGI Mobifree grant (F-Droid App Overhaul)"
    when: "2025-04 to 2026-05"
    source: "https://nlnet.nl/project/F-Droid-App/"
sources:
  - https://f-droid.org/
  - https://github.com/f-droid/fdroidclient/blob/master/LICENSE
  - https://f-droid.org/docs/
---

F-Droid is an Android app catalog and client focused on free and open-source applications. The client README states GPL version 3 or, at your option, any later version. Separate components exist for the server/repo tooling.

## Why it fits

The client installs without Google Play. You can also host your own package repositories with F-Droid server tools (separate docs).

## Getting started

Official site and docs: <https://f-droid.org/> · <https://f-droid.org/docs/>

## Notes

License verified for the client repository named in `source_url`. Server/repo tools are adjacent projects.
