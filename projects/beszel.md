---
name: Beszel
slug: beszel
category: Server
license: MIT
open_source: true
type: Server
audience: enthusiast
url: https://beszel.dev/
repo: https://github.com/henrygd/beszel
source_url: https://github.com/henrygd/beszel/blob/main/LICENSE
checked: 2026-11-05
setup_steps: 8
setup_clarity: 4
setup_tested: 2026-11-06
note: Lightweight server monitoring with a central hub and small agents.
summary: Beszel is a lightweight server monitoring tool with a central hub and a small agent on each monitored machine. It shows CPU, memory, disk, network and Docker container usage over time and can send alerts through many notification services. The hub runs as a single binary or Docker container with a web interface. It is licensed under MIT.
icon: assets/icons/beszel.svg
icon_credit: Beszel icon from the MIT-licensed repository; used to identify the project
icon_source: https://github.com/henrygd/beszel/blob/main/internal/site/public/static/icon.svg
fireworks_image: assets/fireworks/cf-beszel-b1.webp
fireworks_date: 2026-11
sources:
  - https://beszel.dev/
  - https://github.com/henrygd/beszel/blob/main/LICENSE
  - https://github.com/henrygd/beszel/blob/main/readme.md
  - https://beszel.dev/guide/getting-started
---
## Why it fits

Free to self-host for monitoring your own machines; no external monitoring service is needed.

## Getting started

Prerequisites (from the official docs):

- A server or PC for the hub with Docker (a single binary is also available)
- Port 8090 for the web interface
- An agent on each system you want to monitor (Docker or binary)

Steps:

1. Create a directory for the hub and agent Compose files.
2. Write a docker-compose.yml for the hub (and optionally a local agent) from the getting-started guide.
3. Set APP_URL to the URL you will use for the hub.
4. Start the stack with docker compose up -d.
5. Open http://<server>:8090 and create the admin account.
6. Click Add System and copy the shown agent key and token.
7. Put the key and token into the agent environment in the compose file.
8. Restart the agent so it connects to the hub.

Official getting started guide: <https://beszel.dev/guide/getting-started>

## Notes

Agents can also run on systems without Docker as a single binary; GPU and S.M.A.R.T. disk data are supported on suitable hardware, per the project README.
