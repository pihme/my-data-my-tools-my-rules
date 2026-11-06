---
name: Uptime Kuma
slug: uptime-kuma
category: Server
license: MIT
open_source: true
type: Server
audience: enthusiast
url: https://uptime.kuma.pet/
repo: https://github.com/louislam/uptime-kuma
source_url: https://github.com/louislam/uptime-kuma/blob/master/LICENSE
demo: https://demo.kuma.pet/start-demo
demo_note: Temporary demo; data is deleted after 10 minutes.
checked: 2026-11-05
setup_steps: 4
setup_clarity: 5
setup_tested: 2026-11-06
note: Self-hosted uptime monitoring with notifications and status pages.
summary: Uptime Kuma is a self-hosted monitoring tool that checks whether websites, servers and services are reachable, for example via HTTP, TCP port, ping or DNS. It sends notifications through many channels such as email, Telegram or Matrix when something goes down, and it can publish status pages. It runs in a single Docker container.
funding_note: The project README lists Atlas Cloud as a special sponsor (USD 400 per month) besides Open Collective and GitHub Sponsors.
icon: assets/icons/uptime-kuma.svg
icon_credit: Uptime Kuma icon from the MIT-licensed repository; used to identify the project
icon_source: https://github.com/louislam/uptime-kuma/blob/master/public/icon.svg
fireworks_image: assets/fireworks/cf-uptime-kuma-b1.webp
fireworks_date: 2026-11
sources:
  - https://uptime.kuma.pet/
  - https://github.com/louislam/uptime-kuma/blob/master/LICENSE
  - https://github.com/louislam/uptime-kuma/blob/master/README.md
  - https://github.com/louislam/uptime-kuma/wiki/%F0%9F%94%A7-How-to-Install
---
## Why it fits

It is licensed under the MIT License. Free to self-host for monitoring your own services.

## Getting started

Prerequisites (from the official docs):

- A server or PC with Docker (a non-Docker Node.js install is also documented)
- Port 3001 for the web interface
- A local disk or volume for /app/data; the docs warn against network file systems such as NFS because SQLite needs POSIX file locks

Steps:

1. Start the container with the docker run command from the install wiki, mapping port 3001 and a data volume.
2. Open http://<server>:3001 and create the admin account.
3. Add monitors for your websites and services.
4. Set up notifications and, optionally, a status page.

Official install guide: <https://github.com/louislam/uptime-kuma/wiki/%F0%9F%94%A7-How-to-Install>

## Notes

The project README links a temporary live demo whose data is deleted after 10 minutes.
