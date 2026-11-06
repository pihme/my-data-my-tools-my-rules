---
name: Vaultwarden
slug: vaultwarden
category: Passwords
license: AGPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://github.com/dani-garcia/vaultwarden
repo: https://github.com/dani-garcia/vaultwarden
source_url: https://github.com/dani-garcia/vaultwarden/blob/main/LICENSE.txt
checked: 2026-11-05
setup_steps: 3
setup_clarity: 4
setup_tested: 2026-11-06
note: Bitwarden-compatible password vault server for self-hosting.
summary: Vaultwarden is a lightweight, unofficial implementation of the Bitwarden server API, written in Rust. It lets you use the official Bitwarden apps and browser extensions with a password vault on your own server, and it needs few resources, which makes it popular for home setups. It is not affiliated with Bitwarden, Inc.
corporate_note: Community server compatible with Bitwarden clients; not Bitwarden Inc.
icon: assets/icons/vaultwarden.svg
icon_credit: Vaultwarden icon by Mathijs van Veluw (based on the Rust logo), from the AGPL-3.0 repository; used to identify the project
icon_source: https://github.com/dani-garcia/vaultwarden/blob/main/resources/vaultwarden-icon.svg
fireworks_image: assets/fireworks/cf-vaultwarden-b1.webp
fireworks_date: 2026-11
sources:
  - https://github.com/dani-garcia/vaultwarden
  - https://github.com/dani-garcia/vaultwarden/blob/main/LICENSE.txt
  - https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose
---
## Why it fits

It is licensed under GNU AGPL version 3; the official project presence is primarily the GitHub repository. You can run your own vault backend without paying for hosted Bitwarden for private use.

## Getting started

Prerequisites (from the official docs):

- A server with Docker and Docker Compose
- A data volume for the vault
- A domain and HTTPS via a reverse proxy if clients connect over the internet
- Official Bitwarden apps or browser extensions as clients

Steps:

1. Create a data directory and start vaultwarden/server with DOMAIN set (docker run or Compose), as in the README Usage section.
2. Open the web vault in a browser (HTTPS is required except on localhost).
3. Create your account, then point the Bitwarden clients at your server URL.

Official wiki: Using Docker Compose: <https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose>

Starting a container (docker run): <https://github.com/dani-garcia/vaultwarden/wiki/Starting-a-Container>

## Notes

Uses Bitwarden clients; those clients have their own licenses/distribution channels.
