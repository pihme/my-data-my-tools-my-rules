---
name: PeerTube
slug: peertube
category: Video/Media
license: AGPL-3.0-only
open_source: true
type: Server
audience: expert
url: https://joinpeertube.org/
repo: https://github.com/Chocobozzz/PeerTube
source_url: https://github.com/Chocobozzz/PeerTube/blob/develop/LICENSE
checked: 2026-11-05
setup_steps: 11
setup_clarity: 3
setup_tested: 2026-11-06
note: Federated video hosting you can run on your own server.
summary: PeerTube is software for running your own video platform. Instances can federate with each other via ActivityPub, so viewers can follow channels across servers, and video delivery can use peer-to-peer sharing to reduce server load. It is developed by the French non-profit Framasoft. A public instance needs a domain, TLS, email and ongoing moderation.
corporate_note: Developed by Framasoft.
funding_note: FUTO microgrant (April 2023); NLnet funded PeerTube through the NGI0 Discovery Fund (EU Next Generation Internet).
funders: [futo, nlnet, ngi]
icon: assets/icons/peertube.svg
icon_credit: PeerTube logo by Framasoft, CC BY-SA 4.0; PeerTube is a trademark of Framasoft
icon_source: https://github.com/Chocobozzz/PeerTube/blob/develop/client/src/assets/images/logo.svg
sources:
  - https://joinpeertube.org/
  - https://github.com/Chocobozzz/PeerTube/blob/develop/LICENSE
  - https://futo.tech/grants
  - https://nlnet.nl/project/PeerTube/
  - https://docs.joinpeertube.org/install/docker
---

PeerTube is free software for hosting video with ActivityPub federation. You run an instance on your own hardware or VPS. LICENSE is GNU AGPL version 3.

## Why it fits

Self-installation of a private or small public instance is free of charge. OSI-approved license.

## Getting started

Prerequisites (from the official docs):

- A Linux server with Docker and Docker Compose v2
- A domain name; the guide notes it cannot be changed after the first start
- Ports 80 and 443 open for HTTPS (Let's Encrypt via certbot in the official setup)
- An SMTP server for account and notification emails

Steps:

1. Download the official production docker-compose file and .env template.
2. Set your domain, database credentials and email settings in .env.
3. Adjust the Nginx template and obtain the first TLS certificate with certbot as described.
4. Start the stack with docker compose up -d.
5. Read the generated admin password from the logs and log in.

Official Docker guide: <https://docs.joinpeertube.org/install/docker>

## Notes

Federation is optional; a private instance can stay non-federated.
