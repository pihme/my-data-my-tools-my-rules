---
name: Element
slug: element
category: Messaging
license: AGPL-3.0-only
open_source: true
type: [App, Server]
audience: end-user
url: https://element.io/
repo: https://github.com/element-hq/element-web
source_url: https://github.com/element-hq/element-web/blob/develop/LICENSE-AGPL-3.0
checked: 2026-11-05
setup_steps: 3
setup_clarity: 4
setup_tested: 2026-11-06
note: Matrix client; pair with a self-hosted homeserver for full control.
summary: Element is a client for the Matrix network, available for web, desktop, Android and iOS. Matrix is federated, so you can use an account on any homeserver, including one you run yourself. Element supports end-to-end encrypted chats, group rooms, and voice and video calls. The web client source is licensed under AGPL-3.0.
corporate_note: Element / New Vector Ltd.; part of the Matrix ecosystem.
icon: assets/icons/element.svg
icon_credit: Element is a trademark of Element Software Inc in the U.S. and other countries; official logo used unaltered to reference Element
icon_source: https://github.com/element-hq/logos/blob/master/element/Element%20Logomark.svg
sources:
  - https://element.io/
  - https://github.com/element-hq/element-web/blob/develop/LICENSE-AGPL-3.0
  - https://element.io/download
  - https://github.com/element-hq/element-web/blob/develop/docs/install.md
  - https://github.com/element-hq/element-web
---
## Why it fits

Full self-hosted messaging typically also needs a Matrix homeserver such as Synapse (a separate project and license). Clients are free to install; combined with a self-hosted homeserver, private messaging stays under your control.

## Getting started

Prerequisites (from the official docs):

- A web browser, desktop computer or phone for the Element apps
- A Matrix account on a homeserver; for fully self-hosted chat you also need a homeserver such as Synapse (separate project, not covered here)
- For hosting Element Web yourself: Docker or a web server, plus HTTPS for real use

Steps:

1. Start Element Web with the documented docker run command (or download the app for your platform).
2. Open the UI in a browser (or launch the app) and sign in with a Matrix account on a homeserver of your choice.
3. Optionally mount your own config.json so the client points at your homeserver instead of the default.

Official downloads: <https://element.io/download>

Element Web install docs: <https://github.com/element-hq/element-web/blob/develop/docs/install.md>

## Notes

Homeserver software is not bundled in this entry. Element may also offer commercial licensing options; the open-source status shown here refers to the public AGPL-licensed code.
