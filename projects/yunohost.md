---
name: YunoHost
slug: yunohost
category: Server
license: AGPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://yunohost.org/
repo: https://github.com/YunoHost/yunohost
source_url: https://github.com/YunoHost/yunohost/blob/dev/LICENSE
demo: https://demo.yunohost.org/
demo_note: Log in with demo / demo; reset every 30 minutes.
checked: 2026-11-05
note: Debian-based server distro that packages self-hosted web apps.
summary: YunoHost is a Debian-based server system that makes it easier to run your own web services. It provides a web admin panel, single sign-on, a mail server and a catalog of packaged apps that install from the admin interface. It is aimed at people who want to self-host without configuring every service by hand.
funding_note: NLnet funded YunoHost work through the NGI0 PET and NGI0 Commons funds (EU Next Generation Internet), run by the Support Self-Hosting association.
funders: [nlnet, ngi]
icon: assets/icons/yunohost.svg
icon_credit: YunoHost logo by ToZz, CC BY-SA 4.0
icon_source: https://github.com/YunoHost/yunohost-artwork/blob/main/logos/svg/yunohost-logo_roundcorners.svg
fireworks_image: assets/fireworks/cf-yunohost-b1.webp
fireworks_date: 2026-11
sources:
  - https://yunohost.org/
  - https://github.com/YunoHost/yunohost/blob/dev/LICENSE
  - https://doc.yunohost.org/en/install/
  - https://nlnet.nl/project/InternetCube/
  - https://nlnet.nl/project/YunoHost-DeclarativeSettings/
  - https://doc.yunohost.org/en/admin/get_started/install_on/
  - https://doc.yunohost.org/en/admin/what_is_yunohost/demo
---
## Why it fits

It is licensed under GNU AGPL version 3. You can install it on your own hardware or VPS for private services without a proprietary panel license.

## Getting started

Prerequisites (from the official docs):

- A spare computer, single-board computer or VPS (YunoHost installs as a Debian-based system)
- Network access; a domain is recommended for reaching the server from outside

Steps:

1. Pick your hardware type on the official install chooser.
2. Install YunoHost with the image or the install script for that hardware.
3. Run the post-installation: choose a main domain and create the first user.
4. Install apps from the YunoHost catalog through the web admin.

Official install guide: <https://doc.yunohost.org/en/install/>

## Notes

Individual packaged apps have their own licenses.
