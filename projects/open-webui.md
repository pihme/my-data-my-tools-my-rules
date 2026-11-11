---
name: Open WebUI
slug: open-webui
category: AI
license: LicenseRef-OpenWebUI
open_source: false
type: Server
audience: enthusiast
url: https://openwebui.com/
repo: https://github.com/open-webui/open-webui
source_url: https://github.com/open-webui/open-webui/blob/main/LICENSE
checked: 2026-11-11
added: 2026-11-11
note: Self-hosted chat interface for local or API language models; source-available (BSD-3 plus branding clause).
summary: Open WebUI is a self-hosted chat interface for language models. It runs in Docker or via Python, keeps chats, users and settings in its own data volume, and connects to a local Ollama or to any OpenAI-compatible API; it has no models of its own. Its license is BSD-3-Clause with an added clause that forbids removing the Open WebUI branding, so it is labeled source-available.
corporate_note: Developed by Open WebUI Inc. (copyright holder in the LICENSE; created by Timothy Jaeryang Baek). An enterprise license is sold for rebranding and enterprise-only features; contributions require a CLA.
icon: assets/icons/open-webui.png
icon_credit: Open WebUI icon from the official brand page (docs.openwebui.com/brand), used unmodified to identify the project; no endorsement implied
icon_source: https://docs.openwebui.com/images/open-webui-icon.png
sources:
  - https://openwebui.com/
  - https://github.com/open-webui/open-webui/blob/main/LICENSE
  - https://github.com/open-webui/open-webui/blob/main/LICENSE_HISTORY
  - https://docs.openwebui.com/license
  - https://docs.openwebui.com/brand
  - https://docs.openwebui.com/enterprise/
  - https://docs.openwebui.com/getting-started/quick-start/
---
## Why it fits

Free to self-host for private use, with all data in your own volume. Pair it with Ollama to keep everything on your own hardware, or connect a hosted API of your choice.

## Getting started

Prerequisites (from the official docs):

- macOS, Linux (x86_64 or ARM64, including Raspberry Pi) or Windows
- Docker (officially supported and recommended); Python 3.11 or 3.12 for the pip/uv route (3.13 is not supported)
- A model source: Ollama on the same or another machine, or an API key for an OpenAI-compatible provider

Steps:

1. Generate a secret key with `openssl rand -hex 32`.
2. Start the container with the Quick Start `docker run` command (port 3000, volume `open-webui`, `WEBUI_SECRET_KEY` set, image `ghcr.io/open-webui/open-webui:main`).
3. Open http://localhost:3000 and create the admin account (the first account becomes administrator; sign-up then switches off).
4. Under your avatar > Settings > Admin > Connections, check that Ollama is detected or add an OpenAI-compatible API.
5. Start a new chat and pick a model.

Watch out: without a fixed `WEBUI_SECRET_KEY`, everyone is logged out whenever the container is recreated. If Ollama runs on the host and Open WebUI in Docker, Ollama must listen on `0.0.0.0`.

Official install guide: <https://docs.openwebui.com/getting-started/quick-start/>

## Notes

License: the LICENSE is BSD-3-Clause-style with an added clause 4: you may not alter, remove or replace any "Open WebUI" branding in any deployment or distribution, except (i) when no more than 50 end users have access within a rolling 30-day period, (ii) with prior written permission, or (iii) with an enterprise license. The software stays free to use at any size; the 50-user limit only governs changing the branding. Code up to and including v0.6.5 remains under the original BSD-3 license (LICENSE_HISTORY). The license is not OSI-approved, hence `open_source: false`. A stock install makes a few outbound calls (version check, default OpenAI connection, embedding-model update check); the docs list switches to turn them off.
