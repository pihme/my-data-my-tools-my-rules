---
name: SearXNG
slug: searxng
category: Search (tentative)
license: AGPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://searxng.org/
repo: https://github.com/searxng/searxng
source_url: https://github.com/searxng/searxng/blob/master/LICENSE
checked: 2026-11-05
note: Self-hosted metasearch engine; results may come from third parties.
summary: SearXNG is a metasearch engine that sends your query to many search services and merges the results. Your instance does not profile users, and upstream engines see the server rather than your browser. You can run it privately for yourself or for a group. It is a fork of the earlier searx project.
corporate_note: Metasearch may query third-party engines depending on configuration.
icon: assets/icons/searxng.svg
icon_credit: SearXNG logo, AGPL-3.0-or-later (SearXNG repository); used to identify the project
icon_source: https://github.com/searxng/searxng/blob/master/client/simple/src/brand/searxng-wordmark.svg
sources:
  - https://searxng.org/
  - https://github.com/searxng/searxng/blob/master/LICENSE
  - https://docs.searxng.org/admin/installation.html
  - https://docs.searxng.org/admin/installation-docker.html
---

SearXNG is a metasearch engine you can run yourself. It aggregates results from configured upstream engines. LICENSE is GNU AGPL version 3.

## Why it fits

Self-hosting an instance for private use is free under AGPL.

## Getting started

Prerequisites (from the official docs):

- A server or PC with Docker or Podman
- A port for the web interface (the example maps 8888 to the container's 8080)

Steps:

1. Create a directory for SearXNG and its configuration.
2. Download the compose template from the official container guide.
3. Set a secret key and your base URL in the settings.
4. Start the container and open the web interface; optionally set it as your browser's search engine.

Official container guide: <https://docs.searxng.org/admin/installation-docker.html>

All installation methods: <https://docs.searxng.org/admin/installation.html>

## Notes

Upstream search providers are third parties; privacy characteristics depend on instance configuration.
