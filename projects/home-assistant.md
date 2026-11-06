---
name: Home Assistant
slug: home-assistant
category: Smart Home
license: Apache-2.0
open_source: true
type: Server
audience: enthusiast
url: https://www.home-assistant.io/
repo: https://github.com/home-assistant/core
source_url: https://github.com/home-assistant/core/blob/dev/LICENSE.md
checked: 2026-11-05
setup_steps: 5
setup_clarity: 4
setup_tested: 2026-11-06
note: Local-first home automation platform for self-hosting.
summary: Home Assistant is a home automation platform that connects smart devices from many vendors and runs automations locally on your own hardware. It is controlled through a web interface and mobile apps and has a large library of integrations. The recommended setup is Home Assistant OS on dedicated hardware; Nabu Casa's cloud service is optional.
corporate_note: Open Home Foundation; Nabu Casa is an optional paid service (info only).
icon: assets/icons/home-assistant.png
icon_credit: Home Assistant logo, a trademark of the Open Home Foundation; used non-commercially to identify the project
icon_source: https://github.com/home-assistant/brands/blob/master/core_integrations/_homeassistant/icon@2x.png
sources:
  - https://www.home-assistant.io/
  - https://github.com/home-assistant/core/blob/dev/LICENSE.md
  - https://www.home-assistant.io/installation/
---

Home Assistant is an open home-automation platform intended to run on local hardware. Core LICENSE.md is Apache License 2.0.

## Why it fits

You can install Home Assistant on your own device without a mandatory subscription for core local control.

## Getting started

Prerequisites (from the official docs):

- Recommended: dedicated hardware such as Home Assistant Green, a Raspberry Pi or a small x86 PC for Home Assistant OS
- Alternative: an existing Linux host with Docker for the Container installation (fewer features, no add-on store)
- A local network connection to your smart devices

Steps:

1. Pick an installation method on the official installation page.
2. Flash Home Assistant OS to your device, or start the official container.
3. Open http://homeassistant.local:8123 (or the host's IP on port 8123).
4. Complete onboarding and add your first integrations.

Official installation overview: <https://www.home-assistant.io/installation/>

## Notes

Optional cloud subscriptions (e.g. Nabu Casa) are not required for basic self-hosted use.
