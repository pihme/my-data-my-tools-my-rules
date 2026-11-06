---
name: Syncthing
slug: syncthing
category: Cloud/Files
license: MPL-2.0
open_source: true
type: App
audience: end-user
url: https://syncthing.net/
repo: https://github.com/syncthing/syncthing
source_url: https://github.com/syncthing/syncthing/blob/main/LICENSE
checked: 2026-11-05
setup_steps: 4
setup_clarity: 3
setup_tested: 2026-11-06
note: Peer-to-peer continuous file synchronization across your devices.
summary: Syncthing continuously synchronizes folders between your own devices over the local network or the internet, without a central cloud. Data is transferred encrypted, and devices are paired by exchanging device IDs. It runs on Windows, macOS, Linux and other systems and is managed through a local web interface.
icon: assets/icons/syncthing.svg
icon_credit: Syncthing logo, MPL-2.0 (same license as the source); used unmodified to identify the project
icon_source: https://github.com/syncthing/syncthing/blob/main/assets/logo-only.svg
sources:
  - https://syncthing.net/
  - https://github.com/syncthing/syncthing/blob/main/LICENSE
  - https://docs.syncthing.net/intro/getting-started.html
---

Syncthing synchronizes folders directly between devices you control, without a mandatory central cloud. LICENSE is Mozilla Public License 2.0.

## Why it fits

Binaries and source are free to install for private use on your own machines.

## Getting started

Prerequisites (from the official docs):

- At least two devices you want to keep in sync
- Network access between them (Syncthing can relay if direct connections are blocked)

Steps:

1. Install Syncthing on each device from the official downloads or your package manager.
2. Open the local web interface (by default http://127.0.0.1:8384).
3. Add the other device by its device ID on both sides.
4. Share a folder and accept it on the other device.

Watch out: Syncthing's official getting-started guide covers native installs, not Docker. Community container examples that leave `STGUIADDRESS` empty bind the GUI to localhost inside the container, so a plain bridge port publish will not reach it; use host networking or set `STGUIADDRESS` as those examples describe.

Official getting started guide: <https://docs.syncthing.net/intro/getting-started.html>

## Notes

Typed as App (P2P clients on your devices). There is no separate mandatory hosted service.
