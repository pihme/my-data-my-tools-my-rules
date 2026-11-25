---
name: Kopia
slug: kopia
category: Server
license: Apache-2.0
open_source: true
type: [App, Server]
audience: enthusiast
url: https://kopia.io/
repo: https://github.com/kopia/kopia
source_url: https://github.com/kopia/kopia/blob/master/LICENSE
checked: 2026-11-25
added: 2026-11-25
setup_steps: 5
setup_clarity: 3
setup_tested: 2026-11-25
note: Encrypted, deduplicated backups to your own disks, servers or cloud storage, with a desktop app and a command line.
summary: Kopia is a backup and restore tool for Windows, macOS and Linux. It stores encrypted, compressed and deduplicated snapshots in a repository on a local disk, a NAS, an SFTP or WebDAV server, or S3-compatible and other cloud storage that you pick and pay for yourself. It comes as a command-line program and as KopiaUI, which runs as a desktop app or as a web interface in server mode.
icon: assets/icons/kopia.svg
icon_credit: Kopia logo from the Apache-2.0 repository; used to identify the project
icon_source: https://github.com/kopia/kopia/blob/master/icons/kopia.svg
fireworks_image: assets/fireworks/cf-kopia-b1.webp
fireworks_date: 2026-11
sources:
  - https://kopia.io/
  - https://github.com/kopia/kopia/blob/master/LICENSE
  - https://github.com/kopia/kopia/blob/master/README.md
  - https://kopia.io/docs/installation/
  - https://kopia.io/docs/getting-started/
  - https://kopia.io/docs/repository-server/
---
## Why it fits

Kopia is licensed under the Apache License 2.0 and free to use. The README states that you choose the storage location yourself, so backups can stay on your own disk, NAS or server without any vendor service.

## Getting started

Prerequisites (from the official docs):

- Desktop route: Windows, macOS or Linux and the KopiaUI installer, or the `kopia` command-line binary
- Server route: a machine with Docker and the sample Compose file from the installation page
- A storage location for the repository: a local or USB disk, a NAS, an SFTP or WebDAV server, or S3-compatible or other supported cloud storage

Steps (server route with Docker, as checked):

1. Copy the sample Compose file from the installation page and adjust the paths for config, cache, repository and the data to back up.
2. Set the web UI user name and password and the repository password (`KOPIA_PASSWORD`).
3. Start the container with `docker compose up -d` and open the web interface on port 51515.
4. Create or connect a repository in the web interface or with `kopia repository create`.
5. Create the first snapshot and check that you can browse and restore it.

Watch out: the sample mounts `/tmp` with the `:shared` option, which fails on hosts where `/` is not a shared mount; without `:shared` the server starts (the option is only needed for browsing mounted snapshots). The server starts with "Repository not configured", and the Docker section does not show the repository step. The sample also publishes the port on all interfaces and runs without TLS (`--insecure`).

Official installation docs: <https://kopia.io/docs/installation/>

Getting started guide: <https://kopia.io/docs/getting-started/>

## Notes

The setup rating covers the Docker server route (Kopia 0.23.1, tested 2026-11-25). The desktop app (KopiaUI) and the plain command-line route were not tested. Any storage costs depend on the location you pick. restic and Backrest are separate projects with a similar purpose.
