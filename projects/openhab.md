---
name: openHAB
slug: openhab
category: Smart Home
license: EPL-2.0
open_source: true
type: Server
audience: enthusiast
url: https://www.openhab.org/
repo: https://github.com/openhab/openhab-core
source_url: https://github.com/openhab/openhab-core/blob/main/LICENSE
checked: 2026-11-05
setup_steps: 5
setup_clarity: 2
setup_tested: 2026-11-06
note: Vendor-neutral open home automation runtime.
summary: openHAB is a vendor-neutral home automation platform that integrates devices and services from many manufacturers through add-ons called bindings. It runs locally on Java, for example on a Raspberry Pi with the openHABian image or in Docker. Rules, dashboards and automations are configured through a web interface.
funding_note: FUTO microgrant (June 2023).
funders: [futo]
icon: assets/icons/openhab.svg
icon_credit: openHAB logo, a mark of the openHAB Foundation e.V.; used to refer to the openHAB project as permitted by its trademark policy
icon_source: https://github.com/openhab/openhab-docs/blob/main/.vuepress/public/openhab-logo-square.svg
sources:
  - https://www.openhab.org/
  - https://github.com/openhab/openhab-core/blob/main/LICENSE
  - https://www.openhab.org/docs/installation/
  - https://futo.tech/grants
  - https://www.openhab.org/docs/installation/docker.html
---
## Why it fits

Self-installation for private home control is free under EPL-2.0.

## Getting started

Prerequisites (from the official docs):

- A Raspberry Pi for the openHABian image, or a Linux host with Docker, or any system with Java for a manual install
- Network access to your smart devices

Steps:

1. Create an openhab user on the host (or note the UID/GID you will run as).
2. Create the three host directories the Docker guide mounts.
3. Start the openhab/openhab container with a concrete image tag and your UID/GID.
4. Open http://<server>:8080.
5. Create the admin account and install bindings for your devices.

Watch out: replace the image tag placeholder `openhab/openhab:<version>-<distribution>` with a concrete tag from Docker Hub (for example `openhab/openhab:latest`). Prefer the `TZ` environment variable over mounting `/etc/localtime`; the current image warns that the localtime mount is obsolete.

Official installation overview: <https://www.openhab.org/docs/installation/>

Docker guide: <https://www.openhab.org/docs/installation/docker.html>

## Notes

Bindings and add-ons may carry additional notices; the license shown applies to the core.
