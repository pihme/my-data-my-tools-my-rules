---
name: Beszel
slug: beszel
category: Monitoring (tentative)
license: MIT
open_source: true
type: Server
audience: enthusiast
url: https://beszel.dev/
repo: https://github.com/henrygd/beszel
source_url: https://github.com/henrygd/beszel/blob/main/LICENSE
checked: 2026-11-05
note: Lightweight server monitoring with a central hub and small agents.
summary: Beszel is a lightweight server monitoring tool with a central hub and a small agent on each monitored machine. It shows CPU, memory, disk, network and Docker container usage over time and can send alerts through many notification services. The hub runs as a single binary or Docker container with a web interface. It is licensed under MIT.
icon: assets/icons/beszel.svg
icon_credit: Beszel icon from the MIT-licensed repository; used to identify the project
icon_source: https://github.com/henrygd/beszel/blob/main/internal/site/public/static/icon.svg
sources:
  - https://beszel.dev/
  - https://github.com/henrygd/beszel/blob/main/LICENSE
  - https://github.com/henrygd/beszel/blob/main/readme.md
  - https://beszel.dev/guide/getting-started
---

Beszel monitors your own servers: a hub collects metrics from agents and shows history and alerts in a web interface. The repository LICENSE is the MIT License.

## Why it fits

Free to self-host for monitoring your own machines; no external monitoring service is needed.

## Getting started

Prerequisites (from the official docs):

- A server or PC for the hub with Docker (a single binary is also available)
- Port 8090 for the web interface
- An agent on each system you want to monitor (Docker or binary)

Steps:

1. Create a docker-compose.yml for the hub (and optionally a local agent) from the getting-started guide.
2. Set APP_URL and start it with docker compose up -d.
3. Open http://<server>:8090 and create the admin account.
4. Click Add System, copy the shown key and token into the agent configuration and start the agent.

Official getting started guide: <https://beszel.dev/guide/getting-started>

## Notes

Agents can also run on systems without Docker as a single binary; GPU and S.M.A.R.T. disk data are supported on suitable hardware, per the project README.
