---
name: Bitwarden clients
slug: bitwarden-clients
category: Passwords
license: GPL-3.0-only
open_source: true
type: App
audience: end-user
url: https://bitwarden.com/
repo: https://github.com/bitwarden/clients
source_url: https://github.com/bitwarden/clients/blob/main/LICENSE.txt
checked: 2026-11-25
added: 2026-11-25
setup_steps: 5
setup_clarity: 3
setup_tested: 2026-11-25
note: Official Bitwarden password manager apps (browser, desktop, web, command line); can use a self-hosted server.
summary: The Bitwarden clients are the official password manager apps by Bitwarden, Inc.: the web vault, browser extensions, desktop apps and the command-line tool bw; Android and iOS have separate apps. By default they connect to Bitwarden's hosted servers, but each client can be pointed at a self-hosted server instead, such as a Bitwarden server or a compatible one like Vaultwarden.
corporate_note: Developed by Bitwarden, Inc.; "Bitwarden" and its logo are trademarks of Bitwarden, Inc., and the repository grants no trademark rights.
fireworks_image: assets/fireworks/cf-bitwarden-clients-b1.webp
fireworks_date: 2026-11
role: Client apps
works_with: [vaultwarden]
sources:
  - https://bitwarden.com/
  - https://github.com/bitwarden/clients/blob/main/LICENSE.txt
  - https://github.com/bitwarden/clients/blob/main/LICENSE_GPL.txt
  - https://github.com/bitwarden/clients/blob/main/LICENSE_BITWARDEN.txt
  - https://github.com/bitwarden/clients/blob/main/apps/cli/README.md
  - https://github.com/bitwarden/clients/blob/main/.github/workflows/build-cli.yml
  - https://github.com/bitwarden/sdk-internal/blob/main/LICENSE
  - https://github.com/bitwarden/android/blob/main/LICENSE.txt
  - https://github.com/bitwarden/ios/blob/main/LICENSE.txt
  - https://github.com/bitwarden/server/blob/main/TRADEMARK_GUIDELINES.md
  - https://bitwarden.com/download/
  - https://bitwarden.com/help/change-client-environment/
---
## Why it fits

The client apps are licensed under GNU GPL version 3 and free to install. Because every client can be set to your own server URL, you can keep the whole password vault on hardware you control, for example with Vaultwarden.

## Getting started

Prerequisites (from the official docs):

- A Bitwarden-compatible server reachable over HTTPS, for example your own Vaultwarden
- A browser, desktop computer, phone or Node.js for the command-line tool

Steps (web vault and command line against Vaultwarden, as checked):

1. Make sure your server is reachable over HTTPS (a self-signed certificate works for a local test).
2. Install a client: the browser extension, desktop or mobile app from the download page, or the CLI with `npm install -g @bitwarden/cli`.
3. Before logging in, set the server URL to your own server (in the apps: "Self-hosted" in the "Logging in on" menu; in the CLI: `bw config server <url>`).
4. Create your account in the web vault; the CLI has no register command.
5. Log in on each client and sync (`bw login`, `bw sync` in the CLI).

Watch out: over plain HTTP, account creation in the web vault did nothing in our test, and the only hint was a browser-console error ("Insecure URL not allowed. All URLs must use HTTPS."). With a self-signed certificate the CLI needs `NODE_EXTRA_CA_CERTS`. After the first login the web vault shows an extension setup page and a tour that you can skip.

Download page: <https://bitwarden.com/download/>

Connecting clients to a self-hosted server: <https://bitwarden.com/help/change-client-environment/>

## Notes

License labels: LICENSE.txt says the default license in the repository is GPL v3.0 and that code under `/bitwarden_license` is under the Bitwarden License v1.0, a source-available license for commercial modules. The CLI build workflow produces an open source build and a commercial build. The apps use Bitwarden's internal SDK, whose repository offers GPL v3.0 or the Bitwarden SDK License, with some parts under the SDK license only. The Android and iOS apps are separate GPL-3.0 repositories. Tested on 2026-11-25: CLI `bw` 2026.11.1 and the web vault 2026.10.1 as bundled with Vaultwarden 1.37.5; the browser extensions, desktop and mobile apps were not tested. No logo is shown: Bitwarden's trademark guidelines do not allow use of its logos without written permission.
