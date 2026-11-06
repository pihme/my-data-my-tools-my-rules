---
name: ONLYOFFICE
slug: onlyoffice
category: Office
license: AGPL-3.0-only
open_source: true
type: [App, Server]
audience: end-user
url: https://www.onlyoffice.com/
repo: https://github.com/ONLYOFFICE/DocumentServer
source_url: https://github.com/ONLYOFFICE/DocumentServer/blob/master/LICENSE
checked: 2026-11-05
setup_steps: 3
setup_clarity: 3
setup_tested: 2026-11-06
note: Office suite: free Desktop Editors plus self-hostable Docs Community Edition.
summary: ONLYOFFICE is an office suite for text documents, spreadsheets, presentations and PDFs with strong compatibility with Microsoft Office formats. The free Desktop Editors run offline on Windows, macOS and Linux. Docs Community Edition is a self-hosted server for editing and co-editing in the browser; it needs a host platform such as Nextcloud and is recommended for up to 20 users.
corporate_note: Developed by Ascensio System SIA (Riga, Latvia), which also sells proprietary Enterprise and Developer editions of Docs.
icon: assets/icons/onlyoffice.svg
icon_credit: ONLYOFFICE is a trademark of Ascensio System SIA. Official logo symbol from the ONLYOFFICE press kit, unmodified
icon_source: https://static-site.onlyoffice.com/public/images/templates/press-downloads/logo/logos/logo_symbol_color.svg
screenshot: assets/screenshots/onlyoffice.webp
screenshot_credit: Screenshot from the ONLYOFFICE DocumentServer repository; non-code elements CC BY-SA 4.0 per the LICENSE additional terms; ONLYOFFICE is a trademark of Ascensio System SIA
screenshot_source: https://github.com/ONLYOFFICE/DocumentServer/blob/master/screenshots/ONLYOFFICE%20Docs.png
sources:
  - https://www.onlyoffice.com/
  - https://github.com/ONLYOFFICE/DocumentServer/blob/master/LICENSE
  - https://github.com/ONLYOFFICE/DesktopEditors/blob/master/LICENSE
  - https://github.com/ONLYOFFICE/DocumentServer/blob/master/Readme.md
  - https://www.onlyoffice.com/blog/2026/05/onlyoffice-license-and-trademark-policy
  - https://helpcenter.onlyoffice.com/docs/installation/docs-community-install-docker.aspx
  - https://www.onlyoffice.com/download-desktop
---
## Why it fits

Both Desktop Editors and Docs Community Edition carry GNU AGPL version 3 with additional terms appended by Ascensio System SIA. The Desktop Editors are free to install, and Docs Community Edition is free to self-host for private use under the AGPL.

## Getting started

Prerequisites (from the official docs):

- Desktop Editors: a Windows, macOS or Linux computer
- Docs Community Edition: a server with Docker, at least a dual-core 2 GHz CPU, 4 GB RAM, 40 GB free disk and 4 GB swap (official requirements)
- Docs needs a host application for file storage and sharing, for example Nextcloud; a built-in test example exists for trying it out
- A JWT secret that you set yourself, and HTTPS (the image can obtain a Let's Encrypt certificate) for internet use

Steps:

1. Generate a JWT secret of your own (do not leave the example value).
2. Start the onlyoffice/documentserver container with that JWT_SECRET, as in the Docker guide.
3. Open http://<server>/welcome to confirm Docs is running, then connect it to a host app such as Nextcloud with the same secret.

Watch out: set your own `JWT_SECRET` (do not leave the example `my_jwt_secret`). The "store data outside containers" `docker run` example ends after the volume flags and omits the image name and JWT flags; finish it with `-e JWT_SECRET=… onlyoffice/documentserver`.

Official Docker guide (Docs Community Edition): <https://helpcenter.onlyoffice.com/docs/installation/docs-community-install-docker.aspx>

Desktop Editors download: <https://www.onlyoffice.com/download-desktop>

## Notes

The LICENSE files add terms under AGPL Section 7: keep all copyright and attribution notices; mark modified versions as modified and as based on ONLYOFFICE by Ascensio System SIA; show these notices in the user interface; no trademark rights are granted (see the ONLYOFFICE Trademark Policy); non-code elements such as illustrations and icons are CC BY-SA 4.0. Source file headers state `SPDX-License-Identifier: AGPL-3.0-only`. ONLYOFFICE's license FAQ says the original logo may not be removed from its products. The README lists Community Edition as "up to 20 recommended" users; the current docs state no hard connection limit. Mobile web editors are listed as not included in Community Edition. The Desktop Editors are a normal app install; self-hosting Docs Community Edition takes server and Docker experience.
