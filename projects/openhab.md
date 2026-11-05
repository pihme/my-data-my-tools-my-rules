---
name: openHAB
slug: openhab
category: Smart Home (tentative)
license: EPL-2.0
open_source: true
type: Server
audience: enthusiast
url: https://www.openhab.org/
repo: https://github.com/openhab/openhab-core
source_url: https://github.com/openhab/openhab-core/blob/main/LICENSE
checked: 2026-11-05
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

openHAB is a home-automation platform with a modular binding model. openhab-core LICENSE is Eclipse Public License 2.0.

## Why it fits

Self-installation for private home control is free under EPL-2.0.

## Getting started

Prerequisites (from the official docs):

- A Raspberry Pi for the openHABian image, or a Linux host with Docker, or any system with Java for a manual install
- Network access to your smart devices

Steps:

1. Choose a method on the installation page: openHABian on a Raspberry Pi, Docker, or a package install.
2. Install openHAB with that method (for Docker, follow the Docker page).
3. Open the web interface on port 8080 and create the admin account.
4. Install bindings for your devices and add things and items.

Official installation overview: <https://www.openhab.org/docs/installation/>

Docker guide: <https://www.openhab.org/docs/installation/docker.html>

## Notes

Bindings and add-ons may carry additional notices; the license shown applies to the core.
