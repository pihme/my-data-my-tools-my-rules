---
name: OpenCloud
slug: opencloud
category: Files
license: Apache-2.0
open_source: true
type: Server
audience: enthusiast
url: https://opencloud.eu/
repo: https://github.com/opencloud-eu/opencloud
source_url: https://github.com/opencloud-eu/opencloud/blob/main/LICENSE
checked: 2026-11-25
added: 2026-11-25
setup_steps: 4
setup_clarity: 4
setup_tested: 2026-11-25
note: Self-hosted file storage and sharing with spaces, a web interface and desktop and mobile apps; no database needed.
summary: OpenCloud is a self-hosted platform for storing, syncing and sharing files. Users get a personal space and shared team spaces in a web interface, with desktop and mobile apps for syncing. The Go server needs no database and keeps all data in the file system; sign-in uses OpenID Connect with a built-in identity provider or an external one such as Keycloak.
corporate_note: Developed by OpenCloud GmbH (Berlin), which states on its website that it is part of the Heinlein Group and sells Enterprise subscriptions; the repository history continues the ownCloud Infinite Scale (oCIS) code base.
icon: assets/icons/opencloud.svg
icon_credit: OpenCloud icon from the Apache-2.0 repository, unmodified; Source: OpenCloud GmbH
icon_source: https://github.com/opencloud-eu/opencloud/blob/main/services/web/assets/themes/opencloud/assets/favicon.svg
fireworks_image: assets/fireworks/cf-opencloud-b1.webp
fireworks_date: 2026-11
sources:
  - https://opencloud.eu/
  - https://github.com/opencloud-eu/opencloud/blob/main/LICENSE
  - https://github.com/opencloud-eu/opencloud/blob/main/README.md
  - https://docs.opencloud.eu/docs/admin/getting-started/container/docker/
  - https://docs.opencloud.eu/docs/admin/getting-started/container/docker-compose/
  - https://docs.opencloud.eu/docs/admin/getting-started/container/volume-permissions
  - https://opencloud.eu/en/press/terms-of-use
---
## Why it fits

The server is licensed under the Apache License 2.0 and can be run on your own hardware at no cost; the web interface and the apps are separate repositories under GPL or AGPL licenses. Your files stay in the file system of your own server.

## Getting started

Prerequisites (from the official docs):

- A Linux host with Docker
- Two folders for configuration and data, writable by UID 1000
- A browser that accepts the self-signed certificate for a local test; a domain and a reverse proxy for real use (Docker Compose setup)

Steps (the Docker quick start, as checked):

1. Create the config and data folders and give them to UID 1000 (`chown 1000:1000`).
2. Run the `init` command once with an admin password (`IDM_ADMIN_PASSWORD`).
3. Start the container with `OC_URL` set to the exact address you open in the browser, for example `https://localhost:9200`.
4. Open that address and log in as admin; the personal space opens.

Watch out: the quick start is meant for a temporary local instance and uses the rolling image (`opencloudeu/opencloud-rolling`); the stable releases are published as `opencloudeu/opencloud`, and the Docker Compose guide covers a setup with a domain and reverse proxy. The `chown` is only explained on the separate Volume Permissions page. `OC_URL` must match the browser address exactly, otherwise the login fails.

Docker quick start: <https://docs.opencloud.eu/docs/admin/getting-started/container/docker/>

Docker Compose setup: <https://docs.opencloud.eu/docs/admin/getting-started/container/docker-compose/>

## Notes

Tested with OpenCloud 9.2.0 (rolling image) on 2026-11-25; the full Docker Compose setup with reverse proxy and office integration was not tested. Repository licenses checked 2026-11-25: server Apache-2.0, web interface (opencloud-eu/web) AGPL-3.0, desktop and Android apps GPL-2.0, iOS app GPL-3.0. OpenCloud's terms for its logos allow non-commercial use with the source named and no modification.
