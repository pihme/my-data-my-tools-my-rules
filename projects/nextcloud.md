---
name: Nextcloud
slug: nextcloud
category: Cloud/Files
license: AGPL-3.0-only
open_source: true
type: Server
audience: enthusiast
url: https://nextcloud.com/
repo: https://github.com/nextcloud/server
source_url: https://github.com/nextcloud/server/blob/master/COPYING
checked: 2026-11-05
setup_steps: 7
setup_clarity: 4
setup_tested: 2026-11-06
note: Self-hosted file sync and collaboration suite.
summary: Nextcloud is a self-hosted platform for file sync and sharing, with optional apps for calendars, contacts, office documents, chat and video calls. Desktop and mobile clients keep files in sync with your server. The official All-in-One Docker setup bundles the components for new installations. Nextcloud GmbH sells enterprise support; the server is AGPL-licensed.
corporate_note: Nextcloud GmbH; optional enterprise and hosted offerings exist (info only).
funding_note: NLnet funded a Nextcloud search project run by Nextcloud through the NGI0 Discovery Fund (EU Next Generation Internet).
funders: [nlnet, ngi]
icon: assets/icons/nextcloud.svg
icon_credit: Nextcloud and the Nextcloud logo are registered trademarks of Nextcloud GmbH; used online as a link to nextcloud.com per its trademark guidelines
icon_source: https://github.com/nextcloud/server/blob/master/core/img/favicon-touch.svg
sources:
  - https://nextcloud.com/
  - https://github.com/nextcloud/server/blob/master/COPYING
  - https://nlnet.nl/project/NextCloudSearch/
  - https://github.com/nextcloud/all-in-one
---
## Why it fits

Self-hosting the community/server code for private use does not require a paid license.

## Getting started

Prerequisites (from the official docs):

- A Linux server with Docker for Nextcloud All-in-One (AIO)
- A domain pointing to the server, or a free dynamic DNS domain that AIO can register
- Ports 80 and 8080 (AIO interface) and 443 for Nextcloud itself, unless you run behind a reverse proxy

Steps:

1. Start the AIO master container with the docker run command from the AIO README.
2. Open the AIO interface on port 8080 over HTTPS.
3. Note the generated passphrase shown in the interface.
4. Enter your domain name.
5. Start the Nextcloud containers from the AIO interface.
6. Wait until AIO reports that all containers are running.
7. Log in to Nextcloud with the admin credentials shown in AIO.

Official All-in-One guide: <https://github.com/nextcloud/all-in-one>

## Notes

Corporate cloud/enterprise products are optional; they are not required for private self-install.
