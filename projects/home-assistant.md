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
## Why it fits

The core is licensed under Apache License 2.0. You can install Home Assistant on your own device without a mandatory subscription for core local control.

## Getting started

Prerequisites (from the official docs):

- Recommended: dedicated hardware such as Home Assistant Green, a Raspberry Pi or a small x86 PC for Home Assistant OS
- Alternative: an existing Linux host with Docker for the Container installation (fewer features, no add-on store)
- A local network connection to your smart devices

Steps:

1. Create a config directory on the host.
2. Start the official container with your timezone and config path (see the Container install guide).
3. Open http://<server>:8123 (or http://homeassistant.local:8123).
4. Create your account in onboarding.
5. Finish onboarding (location, analytics and first integrations).

Official installation overview: <https://www.home-assistant.io/installation/>

## Notes

Optional cloud subscriptions (e.g. Nabu Casa) are not required for basic self-hosted use.
